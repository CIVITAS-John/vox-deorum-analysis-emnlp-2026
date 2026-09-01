"""
Shared player-type styling helpers backed by shared model config.
"""

from __future__ import annotations

from .model_catalog import (
    get_prompt_patterns,
    get_strategist_model_colors,
    get_variant_style_key,
    split_player_type,
)


MODEL_COLORS = get_strategist_model_colors()
PROMPT_PATTERNS = get_prompt_patterns()


def sort_player_types(player_types):
    pinned = ["Null", "Vanilla"]
    pts = set(player_types)
    return [player for player in pinned if player in pts] + sorted(pts - set(pinned))


def get_player_color(player_type):
    parsed = split_player_type(player_type)
    model_id = parsed["model_id"]
    if model_id in MODEL_COLORS:
        return MODEL_COLORS[model_id]

    return "#000000"


def _get_style_key(player_type):
    if player_type in PROMPT_PATTERNS:
        return player_type

    parsed = split_player_type(player_type)
    return get_variant_style_key(parsed["variant"])


def get_player_hatch(player_type):
    style_key = _get_style_key(player_type)
    if style_key in PROMPT_PATTERNS:
        return PROMPT_PATTERNS[style_key]["hatch"]
    return None


def get_player_linestyle(player_type):
    style_key = _get_style_key(player_type)
    if style_key in PROMPT_PATTERNS:
        return PROMPT_PATTERNS[style_key]["linestyle"]
    return "-"


def get_player_marker(player_type):
    style_key = _get_style_key(player_type)
    if style_key in PROMPT_PATTERNS:
        return PROMPT_PATTERNS[style_key]["marker"]
    return "o"


def get_player_alpha(player_type):
    style_key = _get_style_key(player_type)
    if style_key in PROMPT_PATTERNS:
        return PROMPT_PATTERNS[style_key]["alpha"]
    return 0.8


def get_all_player_styles(player_types):
    styles = {}
    for player_type in player_types:
        styles[player_type] = {
            "color": get_player_color(player_type),
            "hatch": get_player_hatch(player_type),
            "linestyle": get_player_linestyle(player_type),
            "marker": get_player_marker(player_type),
            "alpha": get_player_alpha(player_type),
        }
    return styles
