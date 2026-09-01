"""
Config-backed strategist and prediction model metadata helpers.
"""

from __future__ import annotations

import json
from functools import lru_cache
from typing import Dict, List, Optional

from .paths import SHARED_CONFIG_DIR


MODELS_CONFIG_PATH = SHARED_CONFIG_DIR / "models.json"


@lru_cache(maxsize=1)
def _load_models_config() -> dict:
    with open(MODELS_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_models_config() -> dict:
    return _load_models_config()


def get_strategist_models() -> List[dict]:
    return list(get_models_config().get("strategist_models", []))


def get_strategist_variants() -> dict:
    return dict(get_models_config().get("strategist_variants", {}))


def get_prediction_models() -> List[dict]:
    return list(get_models_config().get("prediction_models", []))


@lru_cache(maxsize=1)
def _strategist_models_by_name() -> Dict[str, dict]:
    models = {}
    for model in get_strategist_models():
        models[model["id"].lower()] = model
        for alias in model.get("aliases", []):
            models[alias.lower()] = model
    return models


def normalize_model_base(model_raw: Optional[str]) -> Optional[str]:
    if not model_raw:
        return None
    return model_raw.split("@", 1)[0].strip()


def get_strategist_model(name: Optional[str]) -> Optional[dict]:
    if not name:
        return None
    return _strategist_models_by_name().get(name.lower())


def canonicalize_model_name(model_base: Optional[str]) -> str:
    normalized = normalize_model_base(model_base)
    if not normalized:
        return "N/A"

    lowered = normalized.lower()
    for model in get_strategist_models():
        candidates = [model["id"], *model.get("aliases", [])]
        if any(candidate and candidate.lower() in lowered for candidate in candidates):
            return model["id"]

    return normalized


def is_known_variant(name: Optional[str]) -> bool:
    return bool(name) and name in get_strategist_variants()


def get_variant_config(name: Optional[str]) -> Optional[dict]:
    if not name:
        return None
    return get_strategist_variants().get(name)


def get_variant_style_key(name: Optional[str]) -> Optional[str]:
    config = get_variant_config(name)
    if not config:
        return None
    return config.get("style_key", name)


def compose_player_type(model_id: str, variant: Optional[str] = None) -> str:
    if not model_id:
        return "N/A"

    if model_id in ("Vanilla", "Null") or not variant:
        return model_id

    config = get_variant_config(variant)
    if not config:
        return model_id

    return f"{model_id}{config['suffix']}"


def split_player_type(player_type: Optional[str]) -> dict:
    if not player_type:
        return {"model_id": None, "variant": None}

    model = get_strategist_model(player_type)
    if model is not None:
        return {"model_id": model["id"], "variant": None}

    for variant_name, config in sorted(
        get_strategist_variants().items(),
        key=lambda item: len(item[1].get("suffix", "")),
        reverse=True,
    ):
        suffix = config.get("suffix", "")
        if suffix and player_type.endswith(suffix):
            model_id = player_type[:-len(suffix)]
            base_model = get_strategist_model(model_id)
            resolved_id = base_model["id"] if base_model is not None else model_id
            return {"model_id": resolved_id, "variant": variant_name}

    return {"model_id": player_type, "variant": None}


def get_player_type(model_name: str, briefed: bool) -> str:
    variant = "Briefed" if briefed else "Simple"
    return compose_player_type(model_name, variant=variant)


def get_pricing_per_million() -> Dict[str, dict]:
    """Return ``{model_id: {input_per_million, output_per_million}}`` for all models with pricing."""
    pricing: Dict[str, dict] = {}
    for model in get_strategist_models():
        p = model.get("pricing")
        if p:
            pricing[model["id"]] = p
    return pricing


def get_strategist_model_colors() -> Dict[str, str]:
    return {model["id"]: model["color"] for model in get_strategist_models()}


def get_prediction_model_order() -> List[str]:
    models = sorted(
        get_prediction_models(),
        key=lambda model: model.get("predict_order", 0),
    )
    return [model["id"] for model in models]


def get_prediction_model_colors() -> Dict[str, str]:
    return {model["id"]: model["color"] for model in get_prediction_models()}


def get_prompt_patterns() -> dict:
    return dict(get_models_config().get("prompt_patterns", {}))
