#!/usr/bin/env python3
"""
CLI script for evaluating victory prediction models with k-fold cross-validation.

Usage:
    python evaluate_model.py --model baseline
    python evaluate_model.py --model baseline --exclude-features civ_*
    python evaluate_model.py --model baseline --include-features science_share,gold_share
    python evaluate_model.py --model baseline --experiments "2026-staff-standard,2026-oss-v-sonnet-standard"
"""

import argparse
import sys
from pathlib import Path

import _paths  # noqa: F401 — centralised sys.path setup
from shared.experiments import LLM_EXPERIMENTS, NON_LLM_EXPERIMENTS

from utils.model_registry import get_model, list_models
from utils.model_evaluator import run_kfold_evaluation, run_full_prediction
from utils.cli_utils import (
    parse_comma_separated, add_data_arguments, add_cv_arguments,
    add_output_arguments, add_model_save_load_arguments,
    PREDICTION_OUTPUT_COLUMNS,
)


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate victory prediction models with k-fold cross-validation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Evaluate baseline model with all features (k-fold CV)
  python evaluate_model.py --model baseline

  # Exclude civilization features
  python evaluate_model.py --model baseline --exclude-features "civ_*"

  # Include only economic features
  python evaluate_model.py --model baseline --include-features "science_share,gold_share,culture_share"

  # Filter to specific experiments
  python evaluate_model.py --model baseline --experiments "2026-staff-standard,2026-oss-v-sonnet-standard"

  # Save results to custom directory
  python evaluate_model.py --model baseline --output-dir results/baseline_full

  # Full-train mode: train on all data and output predictions CSV
  python evaluate_model.py --model baseline --full-train

  # Inference-only mode: load saved model and run inference (no training)
  python evaluate_model.py --model baseline --inference-only
  python evaluate_model.py --model baseline --inference-only --load-model custom/path
        """
    )

    # Required arguments
    parser.add_argument(
        '--model',
        type=str,
        required=True,
        help=f"Model name. Available: {', '.join(list_models())}"
    )

    # Shared arguments
    add_data_arguments(parser)
    add_cv_arguments(parser)
    add_output_arguments(parser)
    add_model_save_load_arguments(parser)

    # Feature filtering arguments
    parser.add_argument(
        '--include-features',
        type=str,
        default=None,
        help="Comma-separated list of features to include (supports wildcards like 'civ_*')"
    )

    parser.add_argument(
        '--exclude-features',
        type=str,
        default=None,
        help="Comma-separated list of features to exclude (supports wildcards)"
    )

    parser.add_argument(
        '--quiet',
        action='store_true',
        help="Suppress progress output"
    )

    # Execution mode (mutually exclusive)
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        '--full-train',
        action='store_true',
        help="Full-train mode: train on all data and output predictions CSV (no cross-validation)"
    )
    mode_group.add_argument(
        '--inference-only',
        action='store_true',
        help="Inference-only mode: load saved model and run inference (no training, no cross-validation). "
             "Loads from --load-model PATH or default output/{model}_model/"
    )

    args = parser.parse_args()

    # Parse comma-separated arguments
    filter_experiments = parse_comma_separated(args.experiments)
    include_features = parse_comma_separated(args.include_features)
    exclude_features = parse_comma_separated(args.exclude_features)

    # Prepare model kwargs
    model_kwargs = {}
    if include_features is not None:
        model_kwargs['include_features'] = include_features
    if exclude_features is not None:
        model_kwargs['exclude_features'] = exclude_features

    # Create output directory if specified
    if args.output_dir is not None:
        output_path = Path(args.output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()

    # Convert 'none' to None for resample method
    resample_method = None if args.resample == 'none' else args.resample

    # Determine training filter description
    if args.train_non_llm_only:
        train_filter_desc = 'non-LLM only (Vanilla/Null)'
    elif args.train_llm_only:
        train_filter_desc = 'LLM only'
    else:
        train_filter_desc = 'all'

    # Get model class/factory from registry
    try:
        from utils.model_registry import MODEL_REGISTRY
        model_class = MODEL_REGISTRY[args.model.lower()]
    except (ValueError, KeyError) as e:
        print(f"Error: Unknown model '{args.model}'", file=sys.stderr)
        sys.exit(1)

    # -----------------------------------------------------------------------
    # INFERENCE-ONLY MODE: load saved model, run inference, no training
    # -----------------------------------------------------------------------
    if args.inference_only:
        # Determine model load path
        if args.load_model:
            model_load_path = args.load_model
        else:
            model_load_path = str(output_path / f"{args.model}_model")

        model_dir = Path(model_load_path)
        if not model_dir.exists():
            print(
                f"Error: No saved model found at '{model_load_path}'.\n"
                f"Run with --full-train first to train and save the model.",
                file=sys.stderr
            )
            sys.exit(1)

        if not args.quiet:
            print("\n" + "=" * 80)
            print("INFERENCE-ONLY MODE")
            print("=" * 80)
            print(f"Model:            {args.model}")
            print(f"Model Path:       {model_load_path}")
            print(f"Data:             {args.data}")
            print(f"Experiments:      {filter_experiments if filter_experiments else 'all'}")
            print(f"Output Directory: {output_path}")
            print("=" * 80 + "\n")

        from utils.model_registry import load_model
        model = load_model(model_load_path)
        predictions_save_path = str(output_path / f"{args.model}_predictions.csv")

        from utils.data_utils import load_and_prepare_base_data, prepare_features, needs_variant_columns
        use_variants = needs_variant_columns(model_class)
        df_all = load_and_prepare_base_data(
            args.data, filter_experiments=filter_experiments,
            filter_zero_score=False, keep_variants=use_variants,
        )
        X_all, _ = prepare_features(df_all, use_variant_columns=use_variants)
        if '_is_zero_score' in X_all.columns:
            X_all = X_all.drop(columns=['_is_zero_score'])

        from utils.model_evaluator import _strip_id_columns_if_not_needed
        X_all = _strip_id_columns_if_not_needed(X_all, model)
        y_pred_proba = model.predict_proba(X_all)[:, 1]
        df_all['predicted_win_probability'] = y_pred_proba

        save_df = df_all[[c for c in PREDICTION_OUTPUT_COLUMNS if c in df_all.columns]]
        save_df.to_csv(predictions_save_path, index=False)

        if not args.quiet:
            print(f"\nPredictions saved to: {predictions_save_path}")
            print(f"Total turns:        {len(df_all)}")
            print("=" * 80 + "\n")

        return 0

    # Print configuration (for non-inference modes)
    if not args.quiet:
        print("\n" + "=" * 80)
        print("MODEL EVALUATION CONFIGURATION")
        print("=" * 80)
        print(f"Model:            {args.model}")
        print(f"Data:             {args.data}")
        print(f"Experiments:      {filter_experiments if filter_experiments else 'all'}")
        print(f"Train Filter:     {train_filter_desc}")
        print(f"CV Splits:        {args.n_splits}")
        print(f"Random State:     {args.random_state}")
        print(f"Resampling:       {args.resample}")
        print(f"Include Features: {include_features if include_features else 'all (default)'}")
        print(f"Exclude Features: {exclude_features if exclude_features else 'none'}")
        print(f"Output Directory: {output_path}")
        print("=" * 80 + "\n")

    # Build train_experiments and predict_df for train-filter modes
    train_experiments = None
    predict_df = None
    preloaded_df = None
    if args.train_non_llm_only or args.train_llm_only:
        from utils.data_utils import load_and_prepare_base_data, needs_variant_columns
        use_variants = needs_variant_columns(model_class)
        preloaded_df = load_and_prepare_base_data(
            args.data, filter_experiments=filter_experiments,
            filter_zero_score=False, keep_variants=use_variants,
        )
        if args.train_non_llm_only:
            train_experiments = NON_LLM_EXPERIMENTS
        else:
            train_experiments = LLM_EXPERIMENTS
        predict_df = preloaded_df
        exp_col = 'condition' if 'condition' in preloaded_df.columns else 'experiment'
        preloaded_df_train = preloaded_df[preloaded_df[exp_col].isin(train_experiments)].copy()
        n_train_games = preloaded_df_train['game_id'].nunique()
        n_all_games = preloaded_df['game_id'].nunique()
        if not args.quiet:
            print(f"Train filter: {train_filter_desc} — {n_train_games} games for training, {n_all_games} games for prediction\n")

    # -----------------------------------------------------------------------
    # FULL-TRAIN MODE: train on all data and output predictions
    # -----------------------------------------------------------------------
    if args.full_train:
        predictions_save_path = str(output_path / f"{args.model}_predictions.csv")

        # Determine model save path (auto-save unless --no-save-model)
        if args.save_model:
            save_model_path = args.save_model
        elif not args.no_save_model:
            save_model_path = str(output_path / f"{args.model}_model")
        else:
            save_model_path = None

        try:
            model, predictions_df = run_full_prediction(
                model_class=model_class,
                model_kwargs=model_kwargs,
                csv_path=args.data,
                filter_experiments=filter_experiments,
                random_state=args.random_state,
                verbose=not args.quiet,
                save_predictions_path=predictions_save_path,
                resample_method=resample_method,
                save_model_path=save_model_path,
                preloaded_df=preloaded_df_train if train_experiments is not None else None,
                predict_df=predict_df,
            )
        except Exception as e:
            print(f"\nError during prediction: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            sys.exit(1)

        # Print final summary for prediction mode
        if not args.quiet:
            print("\n" + "=" * 80)
            print("PREDICTION COMPLETE")
            print("=" * 80)
            print(f"Model:              {args.model}")
            print(f"Predictions file:   {predictions_save_path}")
            print(f"Total turns:        {len(predictions_df)}")

            # Print selected features
            if model.get_selected_features() is not None:
                selected_features = model.get_selected_features()
                print(f"\nFeatures Used: {len(selected_features)}")
                if len(selected_features) <= 20:
                    print(f"  {', '.join(selected_features)}")

            print("=" * 80 + "\n")

    # -----------------------------------------------------------------------
    # K-FOLD EVALUATION MODE (default)
    # -----------------------------------------------------------------------
    else:
        # Set up feature importance save path
        importance_save_path = str(output_path / f"{args.model}_feature_importance.csv")

        # Run evaluation
        try:
            summary, feature_importance, models, _, _ = run_kfold_evaluation(
                model_class=model_class,
                model_kwargs=model_kwargs,
                csv_path=args.data,
                filter_experiments=filter_experiments,
                n_splits=args.n_splits,
                random_state=args.random_state,
                verbose=not args.quiet,
                save_importance_path=importance_save_path,
                resample_method=resample_method,
                preloaded_df=preloaded_df,
                train_experiments=train_experiments,
            )
        except Exception as e:
            print(f"\nError during evaluation: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc()
            sys.exit(1)

        # Print final summary
        if not args.quiet:
            print("\n" + "=" * 80)
            print("EVALUATION COMPLETE")
            print("=" * 80)
            print(f"Model:              {args.model}")
            print(f"ROC-AUC:            {summary['roc_auc_mean']:.4f} ± {summary['roc_auc_std']:.4f}")
            print(f"Brier Score:        {summary['brier_score_mean']:.4f} ± {summary['brier_score_std']:.4f}")
            print(f"Log Loss:           {summary['log_loss_mean']:.4f} ± {summary['log_loss_std']:.4f}")
            print(f"Balanced Accuracy:  {summary['balanced_accuracy_mean']:.4f} ± {summary['balanced_accuracy_std']:.4f}")

            # Print selected features
            if models and models[0].get_selected_features() is not None:
                selected_features = models[0].get_selected_features()
                print(f"\nFeatures Used: {len(selected_features)}")
                if len(selected_features) <= 20:
                    print(f"  {', '.join(selected_features)}")

            print("=" * 80 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
