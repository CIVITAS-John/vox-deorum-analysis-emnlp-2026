#!/usr/bin/env python3
"""
Shared CLI utilities for model scripts (compare_models, evaluate_model, tune_model).
Centralizes argument parsing helpers and common constants.
"""

from typing import List, Optional


# Columns to include in prediction output CSVs
PREDICTION_OUTPUT_COLUMNS = [
    'experiment', 'game_id', 'player_id', 'civilization',
    'turn', 'max_turn', 'is_winner',
    'predicted_win_probability', 'turn_progress',
]


def parse_comma_separated(value: Optional[str]) -> Optional[List[str]]:
    """Parse comma-separated string into list."""
    if value is None:
        return None
    return [item.strip() for item in value.split(',') if item.strip()]


def add_data_arguments(parser):
    """Add common data loading arguments."""
    parser.add_argument(
        '--data',
        type=str,
        default='../turn_data.csv',
        help="Path to turn data CSV (default: ../turn_data.csv)"
    )
    parser.add_argument(
        '--experiments',
        type=str,
        default=None,
        help="Comma-separated list of experiments to include (default: all)"
    )
    train_filter = parser.add_mutually_exclusive_group()
    train_filter.add_argument(
        '--train-non-llm-only',
        action='store_true',
        help="Train on non-LLM experiments only (Vanilla/Null), predict/validate on all"
    )
    train_filter.add_argument(
        '--train-llm-only',
        action='store_true',
        help="Train on LLM experiments only, predict/validate on all"
    )


def add_cv_arguments(parser):
    """Add cross-validation arguments."""
    parser.add_argument(
        '--n-splits',
        type=int,
        default=5,
        help="Number of k-fold CV splits (default: 5)"
    )
    parser.add_argument(
        '--random-state',
        type=int,
        default=42,
        help="Random seed for reproducibility (default: 42)"
    )
    parser.add_argument(
        '--resample',
        type=str,
        default='none',
        choices=['none', 'oversample', 'undersample', 'combined'],
        help="Resampling method for class imbalance (default: none)"
    )


def add_output_arguments(parser):
    """Add output directory arguments."""
    parser.add_argument(
        '--output-dir',
        type=str,
        default='output',
        help="Directory to save results (default: output/)"
    )


def add_model_save_load_arguments(parser):
    """Add model save/load arguments."""
    parser.add_argument(
        '--save-model',
        type=str,
        default=None,
        help="Save trained model to directory (default: auto-save to output/{model}_model/ with --full-train)"
    )
    parser.add_argument(
        '--load-model',
        type=str,
        default=None,
        help="Load pre-trained model from directory (skip training, go to prediction)"
    )
    parser.add_argument(
        '--no-save-model',
        action='store_true',
        help="Disable auto-save of model when using --full-train"
    )
