#!/usr/bin/env python3
"""
Model-agnostic evaluation utilities for victory prediction models.
Supports k-fold cross-validation and feature importance aggregation.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import (
    roc_auc_score, brier_score_loss, log_loss,
    balanced_accuracy_score
)
from typing import Dict, List, Tuple, Optional, Literal, TYPE_CHECKING
try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False

from utils.data_utils import load_and_prepare_data, apply_resampling, needs_variant_columns

if TYPE_CHECKING:
    from models.base_predictor import BasePredictor

def _strip_id_columns_if_not_needed(X: pd.DataFrame, model: BasePredictor) -> pd.DataFrame:
    """
    Strip ID columns from X if model doesn't require them.

    This is the inverse of injecting IDs - instead of adding IDs when needed,
    we remove them when NOT needed. More efficient since most models don't need IDs.

    Args:
        X: Feature DataFrame (may include game_id, turn, player_id)
        model: BasePredictor instance

    Returns:
        DataFrame with IDs stripped if model doesn't need them
    """
    required_ids = getattr(model, 'REQUIRES_ID_COLUMNS', None)

    if required_ids is None:
        # Model doesn't need IDs - strip common ID columns
        id_cols_to_strip = ['game_id', 'turn', 'player_id', 'experiment']
        cols_to_keep = [c for c in X.columns if c not in id_cols_to_strip]
        return X[cols_to_keep]
    else:
        # Model needs IDs - keep them
        return X


def evaluate_fold(
    model: BasePredictor,
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_val: pd.DataFrame,
    y_val: pd.Series,
    clusters_train: pd.Series = None,
    resample_method: Optional[Literal['oversample', 'undersample', 'combined']] = None,
    random_state: int = 42,
    _resample_skip_warned: Optional[set] = None,
    epoch_callback=None,
    val_df: pd.DataFrame = None,
) -> Tuple[Dict[str, float], Optional[pd.DataFrame]]:
    """
    Train and evaluate model on a single fold.

    Args:
        model: BasePredictor instance
        X_train, y_train: Training data (may include ID columns game_id, turn, player_id)
        X_val, y_val: Validation data (may include ID columns)
        clusters_train: Cluster IDs (game_id) for training data
        resample_method: Resampling method to apply to training data
        random_state: Random seed for resampling
        _resample_skip_warned: Internal tracking set for warning messages
        val_df: Original df rows for the validation set (metadata for OOF predictions).

    Returns:
        Tuple of (metrics_dict, val_predictions_df)
        val_predictions_df has columns [game_id, player_id, turn, max_turn, experiment,
        civilization, turn_progress, is_winner, predicted_win_probability] if val_df is
        provided, otherwise None.

    Note:
        X_train and X_val may include ID columns. These will be stripped if the model
        doesn't require them (i.e., REQUIRES_ID_COLUMNS is None).
    """
    # Filter out zero-score rows from training data if model requests it
    if getattr(model, 'FILTER_ZERO_SCORE', True):
        if '_is_zero_score' in X_train.columns:
            keep = ~X_train['_is_zero_score']
            X_train, y_train = X_train[keep], y_train[keep]
            if clusters_train is not None:
                clusters_train = clusters_train[keep]

    # Strip _is_zero_score from both train and val (metadata, not a feature)
    if '_is_zero_score' in X_train.columns:
        X_train = X_train.drop(columns=['_is_zero_score'])
    if '_is_zero_score' in X_val.columns:
        X_val = X_val.drop(columns=['_is_zero_score'])

    # Save val groups for predict() argmax before stripping IDs.
    # Train groups are NOT saved: resampling changes X_train indices/length,
    # so pre-resampling groups would be misaligned.  Train balanced accuracy
    # uses 0.5 threshold (only a diagnostic; val metrics are what matter).
    val_groups = [X_val['game_id'], X_val['turn']] if 'game_id' in X_val.columns else None

    # Strip ID columns if model doesn't need them
    X_train = _strip_id_columns_if_not_needed(X_train, model)
    X_val = _strip_id_columns_if_not_needed(X_val, model)

    # Apply resampling to training data if requested (and model allows it)
    if resample_method is not None:
        # Check if model disables resampling
        if hasattr(model, 'DISABLE_RESAMPLING') and model.DISABLE_RESAMPLING:
            # Only warn once per model class
            if _resample_skip_warned is not None:
                model_name = model.__class__.__name__
                if model_name not in _resample_skip_warned:
                    print(f"  ⚠ Skipping resampling for {model_name} (model disables resampling)")
                    _resample_skip_warned.add(model_name)
        else:
            # Apply resampling
            X_train, y_train, clusters_train = apply_resampling(
                X_train, y_train, clusters_train,
                method=resample_method,
                random_state=random_state
            )

    # Train model with cluster information
    model.fit(X_train, y_train, clusters=clusters_train, epoch_callback=epoch_callback)

    # Predict on BOTH training and validation sets
    y_train_pred_proba = model.predict_proba(X_train)[:, 1]  # P(win) on train
    y_train_pred = model.predict(X_train)
    y_val_pred_proba = model.predict_proba(X_val)[:, 1]  # P(win) on val
    y_val_pred = model.predict(X_val, groups=val_groups)

    # Compute metrics for BOTH train and validation
    metrics = {
        # Validation metrics
        'roc_auc': roc_auc_score(y_val, y_val_pred_proba),
        'brier_score': brier_score_loss(y_val, y_val_pred_proba),
        'log_loss': log_loss(y_val, y_val_pred_proba),
        'balanced_accuracy': balanced_accuracy_score(y_val, y_val_pred),
        # Train metrics (for overfitting detection)
        'train_roc_auc': roc_auc_score(y_train, y_train_pred_proba),
        'train_brier_score': brier_score_loss(y_train, y_train_pred_proba),
        'train_log_loss': log_loss(y_train, y_train_pred_proba),
        'train_balanced_accuracy': balanced_accuracy_score(y_train, y_train_pred),
        # Overfitting gaps (positive = overfitting for all metrics)
        'overfitting_gap_roc_auc': roc_auc_score(y_train, y_train_pred_proba) - roc_auc_score(y_val, y_val_pred_proba),
        'overfitting_gap_brier': brier_score_loss(y_val, y_val_pred_proba) - brier_score_loss(y_train, y_train_pred_proba),
        'overfitting_gap_log_loss': log_loss(y_val, y_val_pred_proba) - log_loss(y_train, y_train_pred_proba),
        'overfitting_gap_balanced_accuracy': balanced_accuracy_score(y_train, y_train_pred) - balanced_accuracy_score(y_val, y_val_pred),
        # Dataset info
        'n_train': len(y_train),
        'n_val': len(y_val),
        'train_win_rate': y_train.mean(),
        'val_win_rate': y_val.mean(),
        'n_clusters_train': clusters_train.nunique() if clusters_train is not None else 0
    }

    # Build validation predictions DataFrame with full metadata if val_df provided
    val_preds = None
    if val_df is not None:
        meta_cols = [c for c in ['game_id', 'player_id', 'turn', 'max_turn', 'experiment', 'civilization', 'turn_progress'] if c in val_df.columns]
        val_preds = val_df[meta_cols].copy().reset_index(drop=True)
        val_preds['is_winner'] = y_val.values
        val_preds['predicted_win_probability'] = y_val_pred_proba

    return metrics, val_preds


def aggregate_feature_importance(
    models: List[BasePredictor],
    use_robust_se: bool = True
) -> Optional[pd.DataFrame]:
    """
    Aggregate feature importance across all folds.

    Args:
        models: List of fitted BasePredictor models from each fold
        use_robust_se: Include cluster-robust standard errors if available

    Returns:
        DataFrame with mean importance across folds, or None if not supported
    """
    importance_dfs = []

    for i, model in enumerate(models):
        imp_df = model.get_feature_importance()
        if imp_df is None:
            # Model doesn't support feature importance
            return None
        imp_df['fold'] = i
        importance_dfs.append(imp_df)

    if not importance_dfs:
        return None

    # Combine all folds
    all_importance = pd.concat(importance_dfs, ignore_index=True)

    # Aggregate by feature
    agg_cols = {
        'coefficient': ['mean', 'std']
    }

    # Add robust SE columns if available
    if use_robust_se and 'robust_se' in all_importance.columns:
        agg_cols['robust_se'] = ['mean', 'std']
        agg_cols['z_statistic'] = ['mean', 'std']
        agg_cols['significant_95'] = 'sum'  # Count how many folds are significant

    agg_importance = all_importance.groupby('feature').agg(agg_cols).reset_index()

    # Flatten column names
    if use_robust_se and 'robust_se' in all_importance.columns:
        agg_importance.columns = [
            'feature', 'coef_mean', 'coef_std',
            'robust_se_mean', 'robust_se_std', 'z_stat_mean', 'z_stat_std', 'n_folds_significant'
        ]
    else:
        agg_importance.columns = [
            'feature', 'coef_mean', 'coef_std'
        ]

    # Sort by mean coefficient magnitude
    agg_importance = agg_importance.sort_values('coef_mean', ascending=False, key=abs)

    return agg_importance


def run_kfold_evaluation(
    model_class: type,
    model_kwargs: Dict = None,
    csv_path: str = "../turn_data.csv",
    filter_experiments: List[str] = None,
    n_splits: int = 5,
    random_state: int = 42,
    verbose: bool = True,
    save_importance_path: Optional[str] = None,
    resample_method: Optional[Literal['oversample', 'undersample', 'combined']] = None,
    preloaded_df: Optional[pd.DataFrame] = None,
    precomputed_data: Optional[Tuple[pd.DataFrame, pd.DataFrame, pd.Series, list]] = None,
    train_experiments: Optional[List[str]] = None,
) -> Tuple[Dict, Optional[pd.DataFrame], List[BasePredictor], pd.DataFrame, pd.DataFrame]:
    """
    Run full k-fold cross-validation evaluation for any BasePredictor model.

    Args:
        model_class: BasePredictor subclass (e.g., BaselineVictoryPredictor)
        model_kwargs: Keyword arguments to pass to model constructor
        csv_path: Path to turn data
        filter_experiments: Experiment filter
        n_splits: Number of folds
        random_state: Random seed
        verbose: Print progress and results
        save_importance_path: Path to save feature importance CSV (if None, auto-saves)
        resample_method: Resampling method ('oversample', 'undersample', 'combined', or None)
        preloaded_df: Pre-processed DataFrame from load_and_prepare_base_data.
                      When provided, skips CSV loading and feature engineering.
        precomputed_data: Tuple of (df, X, y, cv_splits) from a prior load_and_prepare_data call.
                          When provided, skips all data loading and split generation entirely.
        train_experiments: List of experiment names to include in training. When provided,
                           training indices in each fold are filtered to only include rows
                           from these experiments. Validation indices remain unfiltered.

    Returns:
        Tuple of (metrics_summary, feature_importance, fitted_models, binned_loss_df)
        binned_loss_df has columns: turn_progress_bin, brier_mean, brier_std,
        log_loss_mean, log_loss_std, n_samples
    """
    if model_kwargs is None:
        model_kwargs = {}

    if verbose:
        print("=" * 80)
        print(f"{model_class.__name__.upper()} - K-FOLD EVALUATION")
        print("=" * 80)
        if resample_method:
            print(f"Resampling Method: {resample_method}")
        else:
            print("Resampling Method: None (using original class distribution)")

    if precomputed_data is not None:
        df, X, y, cv_splits = precomputed_data
    else:
        use_variants = needs_variant_columns(model_class)
        df, X, y, cv_splits = load_and_prepare_data(
            csv_path, filter_experiments, n_splits, random_state, phase_filter=None,
            preloaded_df=preloaded_df, use_variant_columns=use_variants
        )

    # Store results
    fold_metrics = []
    fold_models = []
    val_predictions_all = []
    resample_skip_warned = set()  # Track which models we've warned about

    # Run k-fold CV
    if verbose:
        print("\n" + "=" * 80)
        print("TRAINING AND EVALUATION")
        print("=" * 80)
        print(f"\n{'Fold':<6} {'Val ROC-AUC':<12} {'Train ROC-AUC':<13} {'Gap':<8} {'Val Brier':<11} {'Train Brier':<13} {'Gap':<8}")
        print("-" * 80)

    # Build train_mask from train_experiments after data loading / phase filtering
    train_mask = None
    if train_experiments is not None:
        exp_col = 'condition' if 'condition' in df.columns else 'experiment'
        train_mask = df[exp_col].isin(train_experiments).values

    for fold_idx, (train_idx, val_idx) in enumerate(cv_splits):
        # Filter training indices if train_mask provided
        if train_mask is not None:
            train_idx = train_idx[train_mask[train_idx]]

        # Split data
        X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]
        clusters_train = df.iloc[train_idx]['game_id']

        # Train and evaluate
        model = model_class(random_state=random_state, **model_kwargs)
        metrics, val_preds = evaluate_fold(
            model, X_train, y_train, X_val, y_val,
            clusters_train=clusters_train,
            resample_method=resample_method,
            random_state=random_state,
            _resample_skip_warned=resample_skip_warned,
            val_df=df.iloc[val_idx],
        )

        if verbose:
            # Display train vs validation metrics with overfitting gaps
            gap_roc = metrics['overfitting_gap_roc_auc']
            gap_brier = metrics['overfitting_gap_brier']

            # Add warning indicator if gap is excessive
            warning_roc = " ⚠" if gap_roc > 0.05 else ""
            warning_brier = " ⚠" if gap_brier > 0.01 else ""

            print(f"{fold_idx + 1:<6} "
                  f"{metrics['roc_auc']:<12.4f} "
                  f"{metrics['train_roc_auc']:<13.4f} "
                  f"{gap_roc:+.4f}{warning_roc:<6} "
                  f"{metrics['brier_score']:<11.4f} "
                  f"{metrics['train_brier_score']:<13.4f} "
                  f"{gap_brier:+.4f}{warning_brier}")

        fold_metrics.append(metrics)
        fold_models.append(model)
        if val_preds is not None:
            val_preds['fold'] = fold_idx
            val_predictions_all.append(val_preds)

    # Aggregate metrics
    if verbose:
        print("\n" + "=" * 80)
        print("CROSS-VALIDATION SUMMARY")
        print("=" * 80)

    metrics_df = pd.DataFrame(fold_metrics)
    summary = {
        # Validation metrics
        'roc_auc_mean': metrics_df['roc_auc'].mean(),
        'roc_auc_std': metrics_df['roc_auc'].std(),
        'brier_score_mean': metrics_df['brier_score'].mean(),
        'brier_score_std': metrics_df['brier_score'].std(),
        'log_loss_mean': metrics_df['log_loss'].mean(),
        'log_loss_std': metrics_df['log_loss'].std(),
        'balanced_accuracy_mean': metrics_df['balanced_accuracy'].mean(),
        'balanced_accuracy_std': metrics_df['balanced_accuracy'].std(),
        # Train metrics
        'train_roc_auc_mean': metrics_df['train_roc_auc'].mean(),
        'train_roc_auc_std': metrics_df['train_roc_auc'].std(),
        'train_brier_score_mean': metrics_df['train_brier_score'].mean(),
        'train_brier_score_std': metrics_df['train_brier_score'].std(),
        'train_log_loss_mean': metrics_df['train_log_loss'].mean(),
        'train_log_loss_std': metrics_df['train_log_loss'].std(),
        'train_balanced_accuracy_mean': metrics_df['train_balanced_accuracy'].mean(),
        'train_balanced_accuracy_std': metrics_df['train_balanced_accuracy'].std(),
        # Overfitting gaps
        'overfitting_gap_roc_auc_mean': metrics_df['overfitting_gap_roc_auc'].mean(),
        'overfitting_gap_brier_mean': metrics_df['overfitting_gap_brier'].mean(),
        'overfitting_gap_log_loss_mean': metrics_df['overfitting_gap_log_loss'].mean(),
        'overfitting_gap_balanced_accuracy_mean': metrics_df['overfitting_gap_balanced_accuracy'].mean(),
    }

    if verbose:
        print(f"\nVALIDATION Metrics:")
        print(f"  ROC-AUC:           {summary['roc_auc_mean']:.4f} ± {summary['roc_auc_std']:.4f}")
        print(f"  Brier Score:    {summary['brier_score_mean']:.4f} ± {summary['brier_score_std']:.4f}")
        print(f"  Log Loss: {summary['log_loss_mean']:.4f} ± {summary['log_loss_std']:.4f}")
        print(f"  Balanced Accuracy: {summary['balanced_accuracy_mean']:.4f} ± {summary['balanced_accuracy_std']:.4f}")

        print(f"\nTRAIN Metrics:")
        print(f"  ROC-AUC:           {summary['train_roc_auc_mean']:.4f} ± {summary['train_roc_auc_std']:.4f}")
        print(f"  Brier Score:    {summary['train_brier_score_mean']:.4f} ± {summary['train_brier_score_std']:.4f}")
        print(f"  Log Loss: {summary['train_log_loss_mean']:.4f} ± {summary['train_log_loss_std']:.4f}")
        print(f"  Balanced Accuracy: {summary['train_balanced_accuracy_mean']:.4f} ± {summary['train_balanced_accuracy_std']:.4f}")

        print(f"\nOVERFITTING GAPS (positive = overfitting):")
        print(f"  ROC-AUC Gap:       {summary['overfitting_gap_roc_auc_mean']:+.4f}")
        print(f"  Brier Gap:       {summary['overfitting_gap_brier_mean']:+.4f}")
        print(f"  Log Loss Gap:    {summary['overfitting_gap_log_loss_mean']:+.4f}")
        print(f"  Bal.Acc Gap:       {summary['overfitting_gap_balanced_accuracy_mean']:+.4f}")

        # Add overfitting warnings
        if summary['overfitting_gap_roc_auc_mean'] > 0.05:
            print(f"\n⚠ WARNING: ROC-AUC gap > 5% - model may be overfitting!")
        if summary['overfitting_gap_brier_mean'] > 0.01:
            print(f"\n⚠ WARNING: Brier score gap > 0.01 - model may be overfitting!")
        if summary['overfitting_gap_log_loss_mean'] > 0.05:
            print(f"\n⚠ WARNING: Log loss gap > 0.05 - model may be overfitting!")

    # Feature importance (if supported)
    feature_importance = None
    if verbose:
        print("\n" + "=" * 80)
        print("FEATURE IMPORTANCE (Top 15)")
        print("=" * 80)

    feature_importance = aggregate_feature_importance(fold_models, use_robust_se=True)

    if feature_importance is not None and verbose:
        # Display format with robust SEs if available
        if 'robust_se_mean' in feature_importance.columns:
            display_cols = ['feature', 'coef_mean', 'robust_se_mean', 'z_stat_mean', 'n_folds_significant']
            display_df = feature_importance[display_cols].head(15)
        else:
            display_df = feature_importance.head(15)

        # Use tabulate if available, otherwise fall back to pandas
        if HAS_TABULATE:
            print("\n" + tabulate(display_df, headers='keys', tablefmt='simple', showindex=False, floatfmt='.4f'))
        else:
            print("\n" + display_df.to_string(index=False))

        if 'robust_se_mean' in feature_importance.columns:
            print("\nNote: n_folds_significant = number of folds where 95% CI excludes zero")
    elif verbose:
        print("\n(Feature importance not supported by this model)")

    # Auto-save feature importance if available
    if feature_importance is not None:
        if save_importance_path is None:
            # Auto-generate filename based on model class name
            model_name = model_class.__name__.lower().replace('predictor', '').replace('victory', '')
            save_importance_path = Path("output") / f"{model_name}_feature_importance.csv"

        save_importance_path = Path(save_importance_path)
        save_importance_path.parent.mkdir(parents=True, exist_ok=True)

        feature_importance.to_csv(save_importance_path, index=False)
        if verbose:
            print(f"\nFeature importance saved to: {save_importance_path}")

    # Assemble out-of-fold predictions (each row predicted by a held-out model)
    oof_predictions_df = pd.DataFrame()
    if val_predictions_all:
        oof_predictions_df = pd.concat(val_predictions_all, ignore_index=True).drop(columns=['fold'])

    # Compute binned loss by turn_progress
    binned_loss_df = pd.DataFrame()
    if val_predictions_all:
        all_preds = pd.concat(val_predictions_all, ignore_index=True)
        bins = np.arange(0, 1.1, 0.1)
        labels = [f"{bins[i]:.1f}-{bins[i+1]:.1f}" for i in range(len(bins) - 1)]
        all_preds['bin'] = pd.cut(all_preds['turn_progress'], bins=bins, labels=labels, right=False)

        # Compute metrics per (fold, bin), then aggregate across folds
        fold_bin_rows = []
        for (fold, bin_label), group in all_preds.groupby(['fold', 'bin'], observed=True):
            if len(group) < 2:
                continue
            fold_bin_rows.append({
                'fold': fold,
                'turn_progress_bin': bin_label,
                'brier_score': brier_score_loss(group['is_winner'], group['predicted_win_probability']),
                'log_loss': log_loss(group['is_winner'], group['predicted_win_probability']),
                'n_samples': len(group),
            })

        if fold_bin_rows:
            fold_bin_df = pd.DataFrame(fold_bin_rows)
            binned_loss_df = fold_bin_df.groupby('turn_progress_bin', observed=True).agg(
                brier_mean=('brier_score', 'mean'),
                brier_std=('brier_score', 'std'),
                log_loss_mean=('log_loss', 'mean'),
                log_loss_std=('log_loss', 'std'),
                n_samples=('n_samples', 'sum'),
            ).reset_index()

    return summary, feature_importance, fold_models, binned_loss_df, oof_predictions_df


def run_full_prediction(
    model_class: type,
    model_kwargs: Dict = None,
    csv_path: str = "../turn_data.csv",
    filter_experiments: List[str] = None,
    random_state: int = 42,
    verbose: bool = True,
    save_predictions_path: Optional[str] = None,
    resample_method: Optional[Literal['oversample', 'undersample', 'combined']] = None,
    preloaded_df: Optional[pd.DataFrame] = None,
    save_model_path: Optional[str] = None,
    predict_df: Optional[pd.DataFrame] = None,
) -> Tuple[BasePredictor, pd.DataFrame]:
    """
    Train model on full dataset and generate predictions for all turns.

    This mode is for production use: trains on ALL available data and outputs
    predictions for each turn. No cross-validation is performed.

    Args:
        model_class: BasePredictor subclass (e.g., BaselineVictoryPredictor)
        model_kwargs: Keyword arguments to pass to model constructor
        csv_path: Path to turn data
        filter_experiments: Experiment filter
        random_state: Random seed
        verbose: Print progress and results
        save_predictions_path: Path to save predictions CSV (if None, auto-generates)
        resample_method: Resampling method (typically None for full predictions)
        preloaded_df: Pre-processed DataFrame from load_and_prepare_base_data
                      (filter_zero_score=False). Contains _is_zero_score marker;
                      zero-score filtering happens at training time per model flag.
        save_model_path: Path to save fitted model (if None, model is not saved)
        predict_df: Separate DataFrame for generating predictions (e.g., all data
                    when training on a subset). When None, predictions use df_all.

    Returns:
        Tuple of (fitted_model, predictions_df)
            predictions_df contains all original turn data + 'predicted_win_probability' column
    """
    if model_kwargs is None:
        model_kwargs = {}

    if verbose:
        print("=" * 80)
        print(f"{model_class.__name__.upper()} - FULL PREDICTION MODE")
        print("=" * 80)
        print("Training on all data (no cross-validation)")
        if resample_method:
            print(f"Resampling Method: {resample_method}")
        else:
            print("Resampling Method: None")

    # Load data (without creating CV splits)
    from utils.data_utils import load_turn_data, apply_city_adjustments, add_relative_features, add_raw_share_features, add_competitive_features, prepare_features, drop_transformed_columns, needs_variant_columns

    # Check if model needs variant (non-SELECTED_FEATURES) columns
    use_variants = needs_variant_columns(model_class)

    # Load data — single DataFrame with _is_zero_score marker
    # Zero-score filtering happens below based on model's FILTER_ZERO_SCORE flag
    if preloaded_df is not None:
        df_all = preloaded_df.copy()
    else:
        df_all = load_turn_data(csv_path, filter_experiments, phase_filter=None, filter_zero_score=False)
        df_all = apply_city_adjustments(df_all)
        df_all = add_relative_features(df_all)
        if use_variants:
            df_all = add_raw_share_features(df_all)
        df_all = add_competitive_features(df_all)
        df_all = drop_transformed_columns(df_all, keep_variants=use_variants)

    # Training data: all turns (no phase filtering)
    df_train = df_all.copy()

    # Prepare features for training
    X_train, y_train = prepare_features(df_train, use_variant_columns=use_variants)
    clusters_train = df_train['game_id']

    # Filter zero-score rows from training based on model class flag
    filter_zero = getattr(model_class, 'FILTER_ZERO_SCORE', True)
    if filter_zero and '_is_zero_score' in X_train.columns:
        keep = ~X_train['_is_zero_score']
        X_train, y_train = X_train[keep], y_train[keep]
        clusters_train = clusters_train[keep]

    # Strip _is_zero_score from training features (metadata, not a feature)
    if '_is_zero_score' in X_train.columns:
        X_train = X_train.drop(columns=['_is_zero_score'])

    if verbose:
        print(f"\nTraining Dataset (all turns): {len(df_train)} turns from {df_train['game_id'].nunique()} games")
        print(f"  After zero-score filtering: {len(X_train)} training rows")
        print(f"Features: {X_train.shape[1]}")
        print(f"Win rate: {y_train.mean():.2%}")

    # Instantiate and train model
    model = model_class(random_state=random_state, **model_kwargs)

    # Apply resampling if requested (usually not recommended for full predictions)
    if resample_method is not None:
        if hasattr(model, 'DISABLE_RESAMPLING') and model.DISABLE_RESAMPLING:
            if verbose:
                print(f"  ⚠ Skipping resampling for {model.__class__.__name__} (model disables resampling)")
        else:
            from utils.data_utils import apply_resampling
            X_train, y_train, clusters_train = apply_resampling(
                X_train, y_train, clusters_train,
                method=resample_method,
                random_state=random_state
            )
            if verbose:
                print(f"After resampling: {len(y_train)} samples")

    if verbose:
        print("\nTraining model...")

    # Strip ID columns if model doesn't need them
    X_train = _strip_id_columns_if_not_needed(X_train, model)

    model.fit(X_train, y_train, clusters=clusters_train)

    if verbose:
        print("Training complete!")

    # Save model if path provided (skip for NaivePredictor — trivially retrainable)
    if save_model_path is not None:
        from models.naive_model import NaivePredictor
        if isinstance(model, NaivePredictor):
            if verbose:
                print(f"  Note: skipping model save for NaivePredictor (trivially retrainable)")
        else:
            model.save(save_model_path)  # Let NotImplementedError propagate for non-naive models

    # Generate predictions — use predict_df if provided (e.g., train on subset, predict on all)
    df_pred = predict_df if predict_df is not None else df_all
    X_all, _ = prepare_features(df_pred, use_variant_columns=use_variants)

    # Strip _is_zero_score from prediction features
    if '_is_zero_score' in X_all.columns:
        X_all = X_all.drop(columns=['_is_zero_score'])

    if verbose:
        print(f"\nGenerating predictions for {len(df_pred)} turns (including early/mid game)...")

    # Strip ID columns if model doesn't need them
    X_all = _strip_id_columns_if_not_needed(X_all, model)

    # Predict probabilities
    y_pred_proba = model.predict_proba(X_all)[:, 1]  # P(win)

    # Add predictions to dataframe
    df_pred = df_pred.copy()
    df_pred['predicted_win_probability'] = y_pred_proba

    if verbose:
        print(f"Predictions generated: {len(y_pred_proba)} turns")
        print(f"  Mean predicted probability: {y_pred_proba.mean():.4f}")
        print(f"  Std predicted probability: {y_pred_proba.std():.4f}")
        print(f"  Min: {y_pred_proba.min():.4f}, Max: {y_pred_proba.max():.4f}")

    # Save predictions
    if save_predictions_path is None:
        model_name = model_class.__name__.lower().replace('predictor', '').replace('victory', '')
        save_predictions_path = f"{model_name}_predictions.csv"

    # Keep only metadata + prediction (drop signal/feature columns)
    from utils.cli_utils import PREDICTION_OUTPUT_COLUMNS
    save_df = df_pred[[c for c in PREDICTION_OUTPUT_COLUMNS if c in df_pred.columns]]
    save_df.to_csv(save_predictions_path, index=False)
    if verbose:
        print(f"\nPredictions saved to: {save_predictions_path}")
        print("=" * 80)

    # Display feature importance if available
    if verbose:
        feature_importance = model.get_feature_importance()
        if feature_importance is not None:
            print("\nFEATURE IMPORTANCE (Top 15)")
            print("=" * 80)

            if 'robust_se' in feature_importance.columns:
                display_cols = ['feature', 'coefficient', 'robust_se', 'z_statistic', 'significant_95']
                display_df = feature_importance[display_cols].head(15)
            else:
                display_df = feature_importance.head(15)

            if HAS_TABULATE:
                print("\n" + tabulate(display_df, headers='keys', tablefmt='simple', showindex=False, floatfmt='.4f'))
            else:
                print("\n" + display_df.to_string(index=False))

    return model, df_pred
