#!/usr/bin/env python3
"""
Model registry for victory prediction models.
Provides factory functions to instantiate models by name.
"""

from pathlib import Path
from typing import Dict, Type, List
import json

from models.base_predictor import BasePredictor
from models.baseline_model import BaselineVictoryPredictor
from models.grouped_mlp_model import GroupedMLPPredictor
from models.interaction_mlp_model import InteractionMLPPredictor
from models.attention_model import AttentionMLPPredictor
from models.naive_model import NaivePredictor
from models.score_model import ScorePredictor

# Try to import new models (may fail if dependencies not installed)
try:
    from models.xgboost_model import XGBoostPredictor
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False
    XGBoostPredictor = None

from models.mlp_model import MLPPredictor


# Registry mapping model names to classes
MODEL_REGISTRY: Dict[str, Type[BasePredictor]] = {
    'baseline': BaselineVictoryPredictor,
    'grouped_mlp': GroupedMLPPredictor,
    'naive': NaivePredictor,
    'score': ScorePredictor,
}

# Add optional models if dependencies are available
if HAS_XGBOOST:
    MODEL_REGISTRY['xgboost'] = XGBoostPredictor

MODEL_REGISTRY['mlp'] = MLPPredictor
MODEL_REGISTRY['interaction_mlp'] = InteractionMLPPredictor
MODEL_REGISTRY['attention_mlp'] = AttentionMLPPredictor


def get_model(name: str, **kwargs) -> BasePredictor:
    """
    Get a model instance by name.

    Args:
        name: Model name (must be in MODEL_REGISTRY)
        **kwargs: Keyword arguments to pass to model constructor

    Returns:
        Instantiated BasePredictor model

    Raises:
        ValueError: If model name is not recognized

    Example:
        >>> model = get_model('baseline', random_state=42)
        >>> model = get_model('baseline', include_features=['science_share', 'gold_share'])
        >>> model = get_model('baseline', exclude_features=['civ_*'])
    """
    name_lower = name.lower()
    if name_lower not in MODEL_REGISTRY:
        available = ', '.join(MODEL_REGISTRY.keys())
        raise ValueError(f"Unknown model: '{name}'. Available models: {available}")

    model_class = MODEL_REGISTRY[name_lower]
    return model_class(**kwargs)


def list_models() -> List[str]:
    """
    Get list of all available model names.

    Returns:
        List of model name strings
    """
    return sorted(MODEL_REGISTRY.keys())


def register_model(name: str, model_class: Type[BasePredictor]) -> None:
    """
    Register a new model in the registry.

    Args:
        name: Model name (will be converted to lowercase)
        model_class: BasePredictor subclass

    Raises:
        TypeError: If model_class is not a BasePredictor subclass
        ValueError: If name is already registered

    Example:
        >>> from my_models import MyCustomPredictor
        >>> register_model('custom', MyCustomPredictor)
    """
    if not issubclass(model_class, BasePredictor):
        raise TypeError(f"{model_class.__name__} must be a subclass of BasePredictor")

    name_lower = name.lower()
    if name_lower in MODEL_REGISTRY:
        raise ValueError(f"Model name '{name}' is already registered")

    MODEL_REGISTRY[name_lower] = model_class


def load_model(path: str) -> BasePredictor:
    """
    Load a saved model, dispatching to the correct class via metadata.json.

    Args:
        path: Directory containing saved model files (metadata.json + model state)

    Returns:
        Fitted BasePredictor instance

    Raises:
        ValueError: If model class in metadata is not found in registry
        FileNotFoundError: If metadata.json is missing
    """
    load_dir = Path(path)
    metadata_path = load_dir / 'metadata.json'

    if not metadata_path.exists():
        raise FileNotFoundError(f"No metadata.json found in {load_dir}")

    with open(metadata_path, 'r') as f:
        metadata = json.load(f)

    class_name = metadata['model_class']

    # Find the model class by class name in registry
    model_class = None
    for key, cls in MODEL_REGISTRY.items():
        if cls.__name__ == class_name:
            model_class = cls
            break

    if model_class is None:
        raise ValueError(
            f"Unknown model class: '{class_name}'. "
            f"Available: {[cls.__name__ for cls in MODEL_REGISTRY.values()]}"
        )

    model = model_class._load_model_state(load_dir, metadata)
    print(f"Model loaded from {load_dir} ({class_name})")
    return model
