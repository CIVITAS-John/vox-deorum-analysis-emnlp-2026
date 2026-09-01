"""
Experiment group and player-slot mapping helpers backed by shared JSON config.
"""

from __future__ import annotations

import json
from functools import lru_cache

from .paths import SHARED_CONFIG_DIR
from .model_catalog import compose_player_type


EXPERIMENTS_CONFIG_PATH = SHARED_CONFIG_DIR / "experiments.json"


@lru_cache(maxsize=1)
def _load_experiments_config() -> dict:
    with open(EXPERIMENTS_CONFIG_PATH, "r", encoding="utf-8") as handle:
        return json.load(handle)


def get_experiments_config() -> dict:
    return _load_experiments_config()


def _expand_player_seat(seat) -> str:
    if isinstance(seat, str):
        return seat
    if isinstance(seat, dict):
        return compose_player_type(seat.get("model"), seat.get("variant"))
    return str(seat)


def _expand_condition_player_mapping() -> dict:
    raw_mapping = get_experiments_config().get("condition_player_mapping", {})
    return {
        condition: [_expand_player_seat(seat) for seat in seats]
        for condition, seats in raw_mapping.items()
    }


RAW_CONDITION_PLAYER_MAPPING = get_experiments_config().get("condition_player_mapping", {})
CONDITION_PLAYER_MAPPING = _expand_condition_player_mapping()
VANILLA_EXPERIMENTS = list(get_experiments_config().get("vanilla_experiments", []))
NULL_AI_EXPERIMENTS = list(get_experiments_config().get("null_ai_experiments", []))
DEFAULT_EXCLUDED_EXPERIMENTS = list(
    get_experiments_config().get("default_excluded_experiments", [])
)
NON_LLM_EXPERIMENTS = VANILLA_EXPERIMENTS + NULL_AI_EXPERIMENTS
LLM_EXPERIMENTS = [
    exp for exp, players in CONDITION_PLAYER_MAPPING.items()
    if any(player not in ("Vanilla", "Null") for player in players)
]


def iter_condition_player_rows():
    for condition, player_types in CONDITION_PLAYER_MAPPING.items():
        for player_id, player_type in enumerate(player_types):
            yield {
                "condition": condition,
                "player_id": player_id,
                "player_type": player_type,
            }
