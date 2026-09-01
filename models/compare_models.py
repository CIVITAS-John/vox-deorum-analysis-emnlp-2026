#!/usr/bin/env python3
"""
Compare multiple models side-by-side.

Usage:
    python compare_models.py --models baseline,grouped_mlp
"""

import argparse
from pathlib import Path
import sys
import numpy as np
import pandas as pd

import _paths  # noqa: F401 — centralised sys.path setup
from shared.experiments import LLM_EXPERIMENTS, NON_LLM_EXPERIMENTS

try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False

from utils.model_registry import list_models, MODEL_REGISTRY
from utils.model_evaluator import run_kfold_evaluation, run_full_prediction
from utils.data_utils import load_and_prepare_base_data, needs_variant_columns
from utils.cli_utils import (
    parse_comma_separated, add_data_arguments, add_cv_arguments,
    add_output_arguments, PREDICTION_OUTPUT_COLUMNS,
)


def main():
    parser = argparse.ArgumentParser(
        description="Compare multiple victory prediction models",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Required arguments
    parser.add_argument(
        '--models',
        type=str,
        required=True,
        help=f"Comma-separated model names. Available: {', '.join(list_models())}"
    )

    # Shared arguments
    add_data_arguments(parser)
    add_cv_arguments(parser)
    add_output_arguments(parser)

    # Execution mode (mutually exclusive)
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        '--full-train',
        action='store_true',
        help="Full-train mode: train each model on all data, save predictions CSV, "
             "and compare in-sample metrics (no cross-validation)"
    )
    mode_group.add_argument(
        '--inference-only',
        action='store_true',
        help="Inference-only mode: load saved models from output/{model}_model/ and run "
             "inference (no training). Errors if any model directory is missing."
    )

    parser.add_argument(
        '--no-save-model',
        action='store_true',
        help="Disable auto-save of models when using --full-train"
    )

    args = parser.parse_args()

    # Create output directory
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Parse model names
    model_names = parse_comma_separated(args.models)
    if not model_names:
        print("Error: No models specified", file=sys.stderr)
        sys.exit(1)

    # Validate model names
    available = list_models()
    for name in model_names:
        if name.lower() not in available:
            print(f"Error: Unknown model '{name}'. Available: {', '.join(available)}", file=sys.stderr)
            sys.exit(1)

    # Parse experiments
    filter_experiments = parse_comma_separated(args.experiments)

    # Convert 'none' to None for resample method
    resample_method = None if args.resample == 'none' else args.resample

    # Determine training filter description
    if args.train_non_llm_only:
        train_filter_desc = 'non-LLM only (Vanilla/Null)'
    elif args.train_llm_only:
        train_filter_desc = 'LLM only'
    else:
        train_filter_desc = 'all'

    print("=" * 80)
    print("MODEL COMPARISON")
    print("=" * 80)
    print(f"Models:      {', '.join(model_names)}")
    print(f"Data:        {args.data}")
    print(f"Experiments: {filter_experiments if filter_experiments else 'all'}")
    print(f"Train Filter: {train_filter_desc}")
    print(f"CV Splits:   {args.n_splits}")
    print(f"Resampling:  {args.resample}")
    print(f"Output Dir:  {output_path}")
    print("=" * 80 + "\n")

    # Preload data once - shared across all model evaluations (always load ALL data)
    # Use keep_variants if any model needs features outside SELECTED_FEATURES
    use_variants = any(
        needs_variant_columns(MODEL_REGISTRY[m.lower()])
        for m in model_names
    )
    preloaded_df = load_and_prepare_base_data(
        args.data, filter_experiments=filter_experiments,
        filter_zero_score=False, keep_variants=use_variants,
    )

    # Build train_experiments and predict_df for train-filter modes
    train_experiments = None
    predict_df = None
    preloaded_df_train = None
    if args.train_non_llm_only or args.train_llm_only:
        if args.train_non_llm_only:
            train_experiments = NON_LLM_EXPERIMENTS
        else:
            train_experiments = LLM_EXPERIMENTS
        # For predict mode: train on filtered subset, predict on all
        predict_df = preloaded_df
        exp_col = 'condition' if 'condition' in preloaded_df.columns else 'experiment'
        preloaded_df_train = preloaded_df[preloaded_df[exp_col].isin(train_experiments)].copy()
        n_train_games = preloaded_df_train['game_id'].nunique()
        n_all_games = preloaded_df['game_id'].nunique()
        print(f"Train filter: {train_filter_desc} — {n_train_games} games for training, {n_all_games} games for prediction\n")

    # Run evaluations
    results = []
    all_binned_loss = []

    # -----------------------------------------------------------------------
    # INFERENCE-ONLY MODE: load saved models, run inference, no training
    # -----------------------------------------------------------------------
    if args.inference_only:
        print("\n" + "=" * 80)
        print("INFERENCE-ONLY MODE")
        print("=" * 80 + "\n")

        # Validate all model directories exist before doing any work
        missing = []
        for model_name in model_names:
            model_dir = output_path / f"{model_name}_model"
            if not model_dir.exists():
                missing.append(str(model_dir))
        if missing:
            print("Error: The following saved model directories were not found:", file=sys.stderr)
            for p in missing:
                print(f"  {p}", file=sys.stderr)
            print("Run with --full-train first to train and save the models.", file=sys.stderr)
            sys.exit(1)

        from sklearn.metrics import roc_auc_score, brier_score_loss, log_loss, balanced_accuracy_score
        from utils.data_utils import prepare_features
        from utils.model_evaluator import _strip_id_columns_if_not_needed
        from utils.model_registry import load_model

        for model_name in model_names:
            model_dir = output_path / f"{model_name}_model"
            predictions_path = str(output_path / f"{model_name}_predictions.csv")
            print(f"\n--- Inference for {model_name.upper()} ---")

            model_class = MODEL_REGISTRY[model_name.lower()]
            trained_model = load_model(str(model_dir))

            df_for_pred = predict_df if predict_df is not None else preloaded_df
            use_variants_m = needs_variant_columns(model_class)
            X_all, _ = prepare_features(df_for_pred, use_variant_columns=use_variants_m)
            if '_is_zero_score' in X_all.columns:
                X_all = X_all.drop(columns=['_is_zero_score'])
            X_all = _strip_id_columns_if_not_needed(X_all, trained_model)

            y_pred_proba = trained_model.predict_proba(X_all)[:, 1]
            df_out = df_for_pred.copy()
            df_out['predicted_win_probability'] = y_pred_proba
            if 'turn_progress' not in df_out.columns:
                df_out['turn_progress'] = df_out['turn'] / df_out['max_turn']

            save_df = df_out[[c for c in PREDICTION_OUTPUT_COLUMNS if c in df_out.columns]]
            save_df.to_csv(predictions_path, index=False)
            print(f"  Predictions saved: {predictions_path}")

            # Compute in-sample metrics
            try:
                pred_df = pd.read_csv(predictions_path)
                y_true = pred_df['is_winner']
                y_prob = pred_df['predicted_win_probability']
                groups = [pred_df['game_id'], pred_df['turn']]
                p = pd.Series(y_prob.values, index=pred_df.index)
                preds = np.zeros(len(pred_df), dtype=np.int64)
                winner_idx = p.groupby(groups, sort=False).idxmax()
                idx_to_pos = pd.Series(np.arange(len(pred_df)), index=pred_df.index)
                preds[idx_to_pos[winner_idx].values] = 1
                result = {
                    'model': model_name,
                    'roc_auc_mean': roc_auc_score(y_true, y_prob),
                    'roc_auc_std': 0.0,
                    'brier_mean': brier_score_loss(y_true, y_prob),
                    'brier_std': 0.0,
                    'log_loss_mean': log_loss(y_true, y_prob),
                    'log_loss_std': 0.0,
                    'balanced_accuracy_mean': balanced_accuracy_score(y_true, preds),
                    'balanced_accuracy_std': 0.0,
                    'n_features': len(trained_model.get_selected_features()) if trained_model.get_selected_features() else 0,
                    'n_parameters': trained_model.get_parameter_count(),
                }
                results.append(result)
            except Exception as e:
                print(f"  Could not compute metrics for {model_name}: {e}", file=sys.stderr)

        # Print inference summary
        print("\n" + "=" * 80)
        print("INFERENCE SUMMARY")
        print("=" * 80)
        for model_name in model_names:
            pred_path = output_path / f"{model_name}_predictions.csv"
            if pred_path.exists():
                pred_df = pd.read_csv(pred_path)
                n_turns = len(pred_df)
                n_games = pred_df['game_id'].nunique()
                mean_prob = pred_df['predicted_win_probability'].mean()
                print(f"  {model_name:20s}  {n_turns:>8} turns, {n_games:>4} games, mean P(win)={mean_prob:.4f}")
            else:
                print(f"  {model_name:20s}  MISSING")
        print("=" * 80 + "\n")

    # -----------------------------------------------------------------------
    # FULL-TRAIN MODE: train on all data, save predictions, compare in-sample
    # -----------------------------------------------------------------------
    elif args.full_train:
        print("\n" + "=" * 80)
        print("FULL PREDICTION MODE")
        print("=" * 80 + "\n")

        from sklearn.metrics import roc_auc_score, brier_score_loss, log_loss, balanced_accuracy_score
        from utils.data_utils import prepare_features
        from utils.model_evaluator import _strip_id_columns_if_not_needed

        for model_name in model_names:
            predictions_path = str(output_path / f"{model_name}_predictions.csv")
            print(f"\n--- Training {model_name.upper()} ---")

            model_class = MODEL_REGISTRY[model_name.lower()]

            save_model_path = None if args.no_save_model else str(output_path / f"{model_name}_model")

            try:
                trained_model, _ = run_full_prediction(
                    model_class=model_class,
                    csv_path=args.data,
                    filter_experiments=filter_experiments,
                    random_state=args.random_state,
                    verbose=True,
                    save_predictions_path=predictions_path,
                    resample_method=resample_method,
                    preloaded_df=preloaded_df_train if train_experiments is not None else preloaded_df,
                    save_model_path=save_model_path,
                    predict_df=predict_df,
                )
                print(f"  Saved: {predictions_path}")
            except Exception as e:
                print(f"  Skipping {model_name}: {e}", file=sys.stderr)
                continue

            # Compute in-sample metrics from predictions
            try:
                pred_df = pd.read_csv(predictions_path)
                y_true = pred_df['is_winner']
                y_prob = pred_df['predicted_win_probability']
                # Group-based argmax: predict exactly one winner per (game_id, turn)
                groups = [pred_df['game_id'], pred_df['turn']]
                p = pd.Series(y_prob.values, index=pred_df.index)
                preds = np.zeros(len(pred_df), dtype=np.int64)
                winner_idx = p.groupby(groups, sort=False).idxmax()
                idx_to_pos = pd.Series(np.arange(len(pred_df)), index=pred_df.index)
                preds[idx_to_pos[winner_idx].values] = 1
                y_pred = preds

                result = {
                    'model': model_name,
                    'roc_auc_mean': roc_auc_score(y_true, y_prob),
                    'roc_auc_std': 0.0,
                    'brier_mean': brier_score_loss(y_true, y_prob),
                    'brier_std': 0.0,
                    'log_loss_mean': log_loss(y_true, y_prob),
                    'log_loss_std': 0.0,
                    'balanced_accuracy_mean': balanced_accuracy_score(y_true, y_pred),
                    'balanced_accuracy_std': 0.0,
                    'n_features': len(trained_model.get_selected_features()) if trained_model.get_selected_features() else 0,
                    'n_parameters': trained_model.get_parameter_count(),
                }
                results.append(result)
            except Exception as e:
                print(f"  Could not compute metrics for {model_name}: {e}", file=sys.stderr)

        # Print prediction summary
        print("\n" + "=" * 80)
        print("PREDICTION SUMMARY")
        print("=" * 80)
        for model_name in model_names:
            pred_path = output_path / f"{model_name}_predictions.csv"
            if pred_path.exists():
                pred_df = pd.read_csv(pred_path)
                n_turns = len(pred_df)
                n_games = pred_df['game_id'].nunique()
                mean_prob = pred_df['predicted_win_probability'].mean()
                print(f"  {model_name:20s}  {n_turns:>8} turns, {n_games:>4} games, mean P(win)={mean_prob:.4f}")
            else:
                print(f"  {model_name:20s}  MISSING")
        print("=" * 80 + "\n")

    # -----------------------------------------------------------------------
    # K-FOLD EVALUATION MODE (default)
    # -----------------------------------------------------------------------
    else:
        for model_name in model_names:
            print(f"\n{'=' * 80}")
            print(f"Evaluating: {model_name.upper()}")
            print(f"{'=' * 80}\n")

            model_class = MODEL_REGISTRY[model_name.lower()]
            importance_path = output_path / f"{model_name}_feature_importance.csv"

            try:
                summary, importance, models, binned_loss, oof_preds = run_kfold_evaluation(
                    model_class=model_class,
                    csv_path=args.data,
                    filter_experiments=filter_experiments,
                    n_splits=args.n_splits,
                    random_state=args.random_state,
                    verbose=True,
                    save_importance_path=str(importance_path),
                    resample_method=resample_method,
                    preloaded_df=preloaded_df,
                    train_experiments=train_experiments,
                )

                # Extract key metrics
                result = {
                    'model': model_name,
                    'roc_auc_mean': summary['roc_auc_mean'],
                    'roc_auc_std': summary['roc_auc_std'],
                    'brier_mean': summary['brier_score_mean'],
                    'brier_std': summary['brier_score_std'],
                    'log_loss_mean': summary['log_loss_mean'],
                    'log_loss_std': summary['log_loss_std'],
                    'balanced_accuracy_mean': summary['balanced_accuracy_mean'],
                    'balanced_accuracy_std': summary['balanced_accuracy_std'],
                    'n_features': len(models[0].get_selected_features()) if models else 0,
                    'n_parameters': models[0].get_parameter_count() if models else None
                }
                results.append(result)

                # Save out-of-fold predictions
                if not oof_preds.empty:
                    predictions_path = output_path / f"{model_name}_predictions.csv"
                    save_cols = [c for c in PREDICTION_OUTPUT_COLUMNS if c in oof_preds.columns]
                    oof_preds[save_cols].to_csv(predictions_path, index=False)
                    print(f"  OOF predictions saved: {predictions_path}")

                # Collect binned loss with model name
                if not binned_loss.empty:
                    binned_loss = binned_loss.copy()
                binned_loss.insert(0, 'model', model_name)
                all_binned_loss.append(binned_loss)

            except Exception as e:
                print(f"\nError evaluating {model_name}: {e}", file=sys.stderr)
                import traceback
                traceback.print_exc()
                continue

    # Print comparison summary (CV metrics or in-sample metrics depending on mode)
    if results:
        comparison_df = pd.DataFrame(results)

        print("\n" + "=" * 80)
        print("COMPARISON SUMMARY")
        print("=" * 80 + "\n")

        # Format for display
        display_df = comparison_df.copy()
        display_df['ROC-AUC'] = display_df.apply(
            lambda x: f"{x['roc_auc_mean']:.4f} ± {x['roc_auc_std']:.4f}", axis=1
        )
        display_df['Brier'] = display_df.apply(
            lambda x: f"{x['brier_mean']:.4f} ± {x['brier_std']:.4f}", axis=1
        )
        display_df['Log Loss'] = display_df.apply(
            lambda x: f"{x['log_loss_mean']:.4f} ± {x['log_loss_std']:.4f}", axis=1
        )
        display_df['Balanced Accuracy'] = display_df.apply(
            lambda x: f"{x['balanced_accuracy_mean']:.4f} ± {x['balanced_accuracy_std']:.4f}", axis=1
        )

        # Use tabulate if available, otherwise fall back to pandas
        table_df = display_df[['model', 'ROC-AUC', 'Brier', 'Log Loss', 'Balanced Accuracy', 'n_features']]
        if HAS_TABULATE:
            print(tabulate(table_df, headers='keys', tablefmt='simple', showindex=False))
        else:
            print(table_df.to_string(index=False))

        # Save to CSV
        if args.inference_only:
            comparison_filename = 'model_comparison_inference.csv'
        elif args.full_train:
            comparison_filename = 'model_comparison_predict.csv'
        else:
            comparison_filename = 'model_comparison.csv'
        output_file = output_path / comparison_filename
        comparison_df.to_csv(output_file, index=False)
        print(f"\nComparison saved to: {output_file}")

        # Determine best model per metric
        print("\n" + "=" * 80)
        print("BEST MODELS BY METRIC")
        print("=" * 80)
        print(f"Highest ROC-AUC:            {comparison_df.loc[comparison_df['roc_auc_mean'].idxmax(), 'model']} "
              f"({comparison_df['roc_auc_mean'].max():.4f})")
        print(f"Lowest Brier Score:         {comparison_df.loc[comparison_df['brier_mean'].idxmin(), 'model']} "
              f"({comparison_df['brier_mean'].min():.4f})")
        print(f"Lowest Log Loss:            {comparison_df.loc[comparison_df['log_loss_mean'].idxmin(), 'model']} "
              f"({comparison_df['log_loss_mean'].min():.4f})")
        print(f"Highest Balanced Accuracy:  {comparison_df.loc[comparison_df['balanced_accuracy_mean'].idxmax(), 'model']} "
              f"({comparison_df['balanced_accuracy_mean'].max():.4f})")
        print("=" * 80 + "\n")

        # Save binned loss by turn_progress (k-fold only)
        if all_binned_loss:
            binned_loss_df = pd.concat(all_binned_loss, ignore_index=True)
            binned_loss_file = output_path / 'loss_by_turn_progress.csv'
            binned_loss_df.to_csv(binned_loss_file, index=False)
            print(f"Loss by turn progress saved to: {binned_loss_file}")

    else:
        print("\nNo models successfully evaluated.", file=sys.stderr)
        sys.exit(1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
