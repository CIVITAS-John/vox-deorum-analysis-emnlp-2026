#!/usr/bin/env python3
"""
Naive baseline model that always predicts the training set win rate.
This serves as the simplest possible baseline for comparison.
"""

import json
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Optional, List

from .base_predictor import BasePredictor


class NaivePredictor(BasePredictor):
    """
    Naive baseline that predicts constant probability = (positive / total).

    This model calculates the overall win rate from training data and returns
    this constant probability for all predictions, regardless of input features.

    Useful as a simple baseline to measure whether more complex models
    actually learn meaningful patterns.

    Note: This model disables resampling because it predicts a constant probability
    based on training class distribution. Resampling would artificially inflate the
    predicted probability, causing miscalibration on validation data.
    """

    # Disable resampling for naive model (see class docstring)
    DISABLE_RESAMPLING = True

    def __init__(
        self,
        include_features: Optional[List[str]] = None,
        exclude_features: Optional[List[str]] = None,
        random_state: int = 42
    ):
        """
        Initialize naive predictor.

        Args:
            include_features: Ignored (no features used)
            exclude_features: Ignored (no features used)
            random_state: Random seed for reproducibility
        """
        super().__init__(include_features, exclude_features, random_state)
        self.win_rate_ = None  # Will store positive / total from training

    def fit(self, X: pd.DataFrame, y: pd.Series, clusters: Optional[pd.Series] = None, epoch_callback=None) -> 'NaivePredictor':
        """
        Fit the model by calculating win rate from training data.

        Args:
            X: Feature matrix (not used, but kept for interface compatibility)
            y: Target vector (is_winner: 0 or 1)
            clusters: Cluster IDs (not used)

        Returns:
            Self for method chaining
        """
        # Calculate win rate: positive / total
        y_array = y.values if isinstance(y, pd.Series) else y
        self.win_rate_ = float(np.mean(y_array))

        # Store empty feature list (we don't use any features)
        self.selected_features_ = []

        return self

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predict constant probability for all samples.

        Args:
            X: Feature matrix (not used)

        Returns:
            Array of shape (n_samples, 2) with [P(loss), P(win)]
            where P(win) = training win rate for all samples
        """
        if self.win_rate_ is None:
            raise ValueError("Model must be fitted before making predictions")

        n_samples = len(X)
        probs_win = np.full(n_samples, self.win_rate_)
        probs_loss = 1 - probs_win

        return np.column_stack([probs_loss, probs_win])

    def get_feature_importance(self) -> None:
        """
        Naive model has no feature importance.

        Returns:
            None
        """
        return None

    def get_model_summary(self) -> dict:
        """
        Get summary statistics about the fitted model.

        Returns:
            Dictionary with model metadata
        """
        if self.win_rate_ is None:
            raise ValueError("Model must be fitted before getting summary")

        return {
            'model_type': 'Naive (constant probability)',
            'win_rate': self.win_rate_,
            'n_features': 0,
            'description': f'Always predicts P(win) = {self.win_rate_:.4f}'
        }

    # ------------------------------------------------------------------
    # Save / Load
    # ------------------------------------------------------------------

    def _save_model_state(self, dir_path: Path) -> None:
        state = {'win_rate': self.win_rate_}
        with open(dir_path / 'model.json', 'w') as f:
            json.dump(state, f)

    @classmethod
    def _load_model_state(cls, dir_path: Path, metadata: dict) -> 'NaivePredictor':
        instance = cls(
            include_features=metadata.get('include_features'),
            exclude_features=metadata.get('exclude_features'),
            random_state=metadata.get('random_state', 42),
        )
        with open(dir_path / 'model.json', 'r') as f:
            state = json.load(f)
        instance.win_rate_ = state['win_rate']
        instance.selected_features_ = metadata.get('selected_features', [])
        return instance