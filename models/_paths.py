"""
Centralized path setup for the models package.

Import this module at the top of any entry-point script (compare_models,
evaluate_model, tune_model) to make cross-package imports work:

    import _paths  # noqa: F401

Sub-modules (utils/, models/) should NOT import this directly — they rely
on the entry point having already configured sys.path.
"""

import sys
from pathlib import Path

_MODELS_DIR = str(Path(__file__).resolve().parent)
_ANALYSIS_ROOT = str(Path(__file__).resolve().parent.parent)

# models/ — enables "from utils.xxx" and "from models.xxx"
if _MODELS_DIR not in sys.path:
    sys.path.insert(0, _MODELS_DIR)

# analysis/ — enables "from shared.plot_utilities import ..." and "from ratings import ..."
# Appended (not inserted) so models/ keeps higher priority — otherwise
# "import models" resolves to the outer package instead of models/models/.
if _ANALYSIS_ROOT not in sys.path:
    sys.path.append(_ANALYSIS_ROOT)
