#!/usr/bin/env python3
"""
Abstract base class for victory prediction models.
Provides unified interface for training, prediction, and feature filtering.
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Set, Dict, Any
from pathlib import Path
import json
import pandas as pd
import numpy as np
import fnmatch


class BasePredictor(ABC):
    """
    Abstract base class for all victory prediction models.

    Subclasses must implement:
    - fit(X, y, clusters): Train the model
    - predict_proba(X): Return probability predictions [n_samples, 2]
    - predict(X): Return binary predictions

    Optional methods:
    - get_feature_importance(): Return feature importance DataFrame
    - get_model_summary(): Return model metadata dictionary

    Class-level attributes to define (optional):
    - SUPPORTED_FEATURES: Set of all features this model can use (None = all)
    - DEFAULT_FEATURES: Default feature list if none specified (None = all)
    - REQUIRED_FEATURES: Features that must be included (None = none required)
    - DISABLE_RESAMPLING: If True, skip resampling even when requested (default: False)
    - REQUIRES_ID_COLUMNS: List of ID columns needed in X (e.g., ['game_id', 'turn', 'player_id'])
                           The evaluator will automatically inject these from df. (default: None)
    """

    # Subclasses can override these
    SUPPORTED_FEATURES: Optional[Set[str]] = None
    DEFAULT_FEATURES: Optional[List[str]] = None
    REQUIRED_FEATURES: Optional[Set[str]] = None
    DISABLE_RESAMPLING: bool = False
    REQUIRES_ID_COLUMNS: Optional[List[str]] = None
    FILTER_ZERO_SCORE: bool = True  # If True, filter out eliminated players before training

    def __init__(
        self,
        include_features: Optional[List[str]] = None,
        exclude_features: Optional[List[str]] = None,
        random_state: int = 42
    ):
        """
        Initialize base predictor with feature filtering.

        Args:
            include_features: Explicit list of features to include (supports wildcards like 'civ_*')
                            None = use DEFAULT_FEATURES or all available
            exclude_features: List of features to exclude (supports wildcards)
            random_state: Random seed for reproducibility
        """
        self.include_features = include_features
        self.exclude_features = exclude_features if exclude_features else []
        self.random_state = random_state
        self.selected_features_: Optional[List[str]] = None  # Set during fit

    def _expand_wildcards(self, patterns: List[str], available_features: List[str]) -> Set[str]:
        """
        Expand wildcard patterns to match feature names.

        Args:
            patterns: List of patterns (may include wildcards like 'civ_*')
            available_features: List of all available feature names

        Returns:
            Set of matched feature names
        """
        matched = set()
        for pattern in patterns:
            if '*' in pattern or '?' in pattern:
                # Wildcard pattern
                matches = fnmatch.filter(available_features, pattern)
                matched.update(matches)
            else:
                # Exact match
                matched.add(pattern)
        return matched

    def _filter_features(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Apply include/exclude logic to feature matrix.

        Logic:
        1. Start with available features in X
        2. If SUPPORTED_FEATURES defined, filter to those
        3. If include_features specified, use only those (else use DEFAULT_FEATURES or all)
        4. Remove exclude_features
        5. Ensure REQUIRED_FEATURES are present

        Args:
            X: Full feature matrix

        Returns:
            Filtered feature matrix

        Raises:
            ValueError: If required features are missing or requested features unavailable
        """
        available_features = list(X.columns)

        # Step 1: Filter by SUPPORTED_FEATURES if defined
        if self.SUPPORTED_FEATURES is not None:
            available_features = [f for f in available_features if f in self.SUPPORTED_FEATURES]

        # Step 2: Determine initial feature set
        if self.include_features is not None:
            # Expand wildcards in include_features
            included = self._expand_wildcards(self.include_features, available_features)
            # Check if all requested features are available
            missing = included - set(available_features)
            if missing:
                raise ValueError(f"Requested features not available in data: {missing}")
            selected = list(included)
        elif self.DEFAULT_FEATURES is not None:
            # Use default features (no wildcard expansion needed)
            missing = [f for f in self.DEFAULT_FEATURES if f not in available_features]
            if missing:
                raise ValueError(f"DEFAULT_FEATURES not found in data: {missing}")
            selected = list(self.DEFAULT_FEATURES)
        else:
            # Use all available features
            selected = available_features

        # Step 3: Apply exclusions
        if self.exclude_features:
            excluded = self._expand_wildcards(self.exclude_features, selected)
            selected = [f for f in selected if f not in excluded]

        # Step 4: Ensure required features are present
        if self.REQUIRED_FEATURES is not None:
            missing_required = self.REQUIRED_FEATURES - set(selected)
            if missing_required:
                raise ValueError(f"Required features missing after filtering: {missing_required}")

        # Store selected features for prediction time
        self.selected_features_ = selected

        # Return filtered DataFrame
        return X[selected].copy()

    @abstractmethod
    def fit(self, X: pd.DataFrame, y: pd.Series, clusters: Optional[pd.Series] = None, epoch_callback=None) -> 'BasePredictor':
        """
        Fit the model on training data.

        Implementations should:
        1. Call self._filter_features(X) to get filtered feature matrix
        2. Train the model on filtered features
        3. Store fitted model state

        Args:
            X: Feature matrix
            y: Target vector (is_winner: 0 or 1)
            clusters: Cluster IDs (e.g., game_id) for cluster-robust inference

        Returns:
            Self for method chaining
        """
        pass

    @abstractmethod
    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """
        Predict victory probabilities.

        Implementations should:
        1. Use self.selected_features_ to filter X to same features as training
        2. Return probabilities in sklearn format

        Args:
            X: Feature matrix

        Returns:
            Array of shape (n_samples, 2) with [P(loss), P(win)]
        """
        pass

    def predict(self, X: pd.DataFrame, groups=None) -> np.ndarray:
        """
        Predict binary outcomes (0 or 1).

        When *groups* is provided, picks the highest-probability player
        within each group (argmax) — appropriate for multi-player games
        where exactly one player wins per group.  Without groups, falls
        back to a 0.5 threshold.

        Args:
            X: Feature matrix
            groups: Group keys for argmax prediction (e.g.
                     [game_id_series, turn_series]).  Each element is a
                     Series aligned with X's index.

        Returns:
            Binary predictions (0 = loss, 1 = win)
        """
        proba = self.predict_proba(X)[:, 1]
        if groups is None:
            return (proba >= 0.5).astype(np.int64)
        p = pd.Series(proba, index=X.index)
        preds = np.zeros(len(X), dtype=np.int64)
        winner_idx = p.groupby(groups, sort=False).idxmax()
        idx_to_pos = pd.Series(np.arange(len(X)), index=X.index)
        preds[idx_to_pos[winner_idx].values] = 1
        return preds

    def get_feature_importance(self) -> Optional[pd.DataFrame]:
        """
        Get feature importance (optional method).

        Returns:
            DataFrame with columns: ['feature', 'coefficient', 'abs_coefficient', ...]
            or None if not implemented
        """
        return None

    def get_model_summary(self) -> Optional[Dict[str, Any]]:
        """
        Get model summary statistics (optional method).

        Returns:
            Dictionary with model metadata (type, parameters, metrics, etc.)
            or None if not implemented
        """
        return None

    def get_parameter_count(self) -> Optional[int]:
        """Return the number of trainable parameters, or None if not applicable."""
        return None

    def get_selected_features(self) -> Optional[List[str]]:
        """
        Get list of features actually used by fitted model.

        Returns:
            List of feature names, or None if not yet fitted
        """
        return self.selected_features_

    # ------------------------------------------------------------------
    # Save / Load
    # ------------------------------------------------------------------

    def save(self, path: str) -> None:
        """
        Save fitted model to a directory.

        Creates a directory containing metadata.json and model-specific files.
        Subclasses must implement _save_model_state() and _get_hyperparams().

        Args:
            path: Directory path to save the model to (created if needed)
        """
        save_dir = Path(path)
        save_dir.mkdir(parents=True, exist_ok=True)

        metadata = {
            'model_class': self.__class__.__name__,
            'selected_features': self.selected_features_,
            'random_state': self.random_state,
            'include_features': self.include_features,
            'exclude_features': self.exclude_features,
            'hyperparams': self._get_hyperparams(),
        }
        with open(save_dir / 'metadata.json', 'w') as f:
            json.dump(metadata, f, indent=2)

        self._save_model_state(save_dir)
        print(f"Model saved to {save_dir}")

    def _get_hyperparams(self) -> dict:
        """Return hyperparameters dict for serialization. Subclasses should override."""
        return {}

    def _save_model_state(self, dir_path: Path) -> None:
        """Save model-specific state to dir_path. Subclasses must override."""
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement _save_model_state(). "
            f"Save/load is not supported for this model."
        )

    @classmethod
    def _load_model_state(cls, dir_path: Path, metadata: dict) -> 'BasePredictor':
        """
        Load model-specific state and return a fitted instance.

        Subclasses must override this to reconstruct model architecture
        and load saved weights/parameters.

        Args:
            dir_path: Directory containing saved model files
            metadata: Parsed metadata.json contents

        Returns:
            Fitted BasePredictor instance
        """
        raise NotImplementedError(
            f"{cls.__name__} does not implement _load_model_state(). "
            f"Save/load is not supported for this model."
        )
