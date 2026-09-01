"""
Centralized repo-relative paths for shared analysis utilities.
"""

import json
from pathlib import Path


SHARED_DIR = Path(__file__).resolve().parent
ANALYSIS_ROOT = SHARED_DIR.parent
SHARED_CONFIG_DIR = SHARED_DIR / "config"


def _load_root_dir() -> Path:
    config_path = SHARED_CONFIG_DIR / "paths.json"
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    raw = cfg["root_dir"]
    p = Path(raw)
    return (ANALYSIS_ROOT / p).resolve() if not p.is_absolute() else p.resolve()


ROOT_DIR = _load_root_dir()

TURN_DATA_PATH = ANALYSIS_ROOT / "turn_data.csv"
PANEL_DATA_PATH = ANALYSIS_ROOT / "panel_data.csv"
GAME_TIMESTAMPS_PATH = ANALYSIS_ROOT / "game_timestamps.csv"
MODEL_TOKEN_USAGE_PATH = ANALYSIS_ROOT / "model_token_usage.csv"

MODELS_DIR = ANALYSIS_ROOT / "models"
MODELS_OUTPUT_DIR = MODELS_DIR / "output"
MODELS_OUTPUT_CROSS_DIR = MODELS_DIR / "output_cross"
