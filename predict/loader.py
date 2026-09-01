"""Shared model-loading utility for prediction notebooks.

Usage:
    from loader import load_models, MODEL_ORDER, MODEL_COLORS, OUTPUT_DIR
    models = load_models(usecols=["game_id", "is_winner", ...])
"""

from collections import OrderedDict
from pathlib import Path

import pandas as pd

from shared.model_catalog import get_prediction_model_colors, get_prediction_model_order
from shared.paths import MODELS_OUTPUT_DIR, PANEL_DATA_PATH

# ── Single source of truth: data paths ──────────────────────────────
OUTPUT_DIR = MODELS_OUTPUT_DIR

# ── Single source of truth: model ordering ──────────────────────────
MODEL_ORDER = get_prediction_model_order()

# ── Single source of truth: model colors (colorblind-friendly) ─────
MODEL_COLORS = get_prediction_model_colors()


def load_models(usecols=None, output_dir=None):
    """Load all *_predictions.csv files and return them in canonical order.

    Parameters
    ----------
    usecols : list[str] | None
        Columns to read from each CSV. None reads all columns.
    output_dir : str | Path | None
        Directory containing prediction CSVs. Defaults to ../models/output/
        relative to this file.

    Returns
    -------
    OrderedDict[str, pd.DataFrame]
        Model name -> predictions DataFrame, ordered by MODEL_ORDER.
    """
    if output_dir is None:
        output_dir = OUTPUT_DIR
    else:
        output_dir = Path(output_dir)

    pred_files = {
        f.stem.replace("_predictions", ""): f
        for f in sorted(output_dir.glob("*_predictions.csv"))
    }

    # Order: known models first, then any extras alphabetically
    known = [m for m in MODEL_ORDER if m in pred_files]
    extras = sorted(m for m in pred_files if m not in MODEL_ORDER)
    ordered_names = known + extras

    models = OrderedDict()
    for name in ordered_names:
        models[name] = pd.read_csv(pred_files[name], usecols=usecols)
        print(f"Loaded {name}: {len(models[name]):,} rows")

    return models
