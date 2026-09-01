"""
Load and combine all nuke replay CSV files from nuke/replay/,
adding a `condition` column extracted from each filename.

Filename pattern: nuke-{condition}-{model_friendly}-results.csv
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Sequence

import pandas as pd

from shared.model_catalog import (
    canonicalize_model_name,
    get_strategist_model,
    get_strategist_models,
)


_DEFAULT_REPLAY_DIR = Path(__file__).resolve().parent.parent / "replay"
_KNOWN_CONDITIONS = [
    "original",
    "no-rationale",
    "high-stakes",
    "high-stakes-no-rationale",
    "ethical",
    "ethical-high-stakes",
    "ethical-no-rationale",
    "high-stakes-no-rationale-ethical",
]
_LEGACY_CONDITION_ALIASES = {
    "real-world": "high-stakes",
    "real-world-no-rationale": "high-stakes-no-rationale",
    "ethical-real-world": "ethical-high-stakes",
    "real-world-no-rationale-ethical": "high-stakes-no-rationale-ethical",
}
_FILENAME_CONDITIONS = [*_KNOWN_CONDITIONS, *_LEGACY_CONDITION_ALIASES]
REPLAY_TAG_JOIN_KEYS = [
    "game_id",
    "player_id",
    "turn",
    "condition",
    "repetition",
    "replay_model",
]
CONDITION_FACTOR_META = {
    "no_rationale": {"token": "no-rationale", "label": "No-rationale"},
    "high_stakes": {"token": "high-stakes", "label": "High-stakes"},
    "ethical": {"token": "ethical", "label": "Ethical"},
}
CONDITION_FACTORS = list(CONDITION_FACTOR_META)
_REPLAY_INSTANCE_COLUMNS = ["game_id", "player_id", "turn"]
_REPLAY_FILL_COLUMNS = {
    "replay_nuke": "prev_nuke",
    "replay_use_nuke": "prev_use_nuke",
}
_ORIGINAL_METRIC_COLUMNS = ["prev_nuke", "after_nuke", "prev_use_nuke", "after_use_nuke"]


def safe_tier_name(tier: str) -> str:
    """Strip non-alphanumeric characters from a reasoning/rationale tier name."""
    return re.sub(r"[^A-Za-z0-9]", "", tier)


def canonical_condition_name(condition: object) -> str | None:
    """Return the canonical in-memory replay condition name."""
    if pd.isna(condition):
        return None
    return _LEGACY_CONDITION_ALIASES.get(str(condition), str(condition))


def canonical_replay_model(name: str | None) -> str:
    """Return the configured strategist model id for a raw replay model name."""
    model = get_strategist_model(name)
    return model["id"] if model else canonicalize_model_name(name)


def add_canonical_replay_model(
    df: pd.DataFrame,
    source_col: str = "replay_model",
    target_col: str = "replay_model_canonical",
) -> pd.DataFrame:
    """Add a canonical replay model column and return ``df``."""
    df[target_col] = df[source_col].map(canonical_replay_model)
    return df


def get_present_strategist_model_order(
    df: pd.DataFrame,
    model_col: str = "replay_model_canonical",
) -> list[str]:
    """Return present replay models in configured strategist catalog order."""
    present_models = set(df[model_col].dropna())
    return [
        model["id"]
        for model in get_strategist_models()
        if model["id"] in present_models
    ]


def add_condition_factor_columns(
    df: pd.DataFrame,
    condition_col: str = "condition",
) -> pd.DataFrame:
    """Add binary columns for replay condition factors and return ``df``."""
    df[condition_col] = df[condition_col].map(canonical_condition_name)
    conditions = df[condition_col].astype(str)
    for factor, meta in CONDITION_FACTOR_META.items():
        df[factor] = conditions.str.contains(meta["token"], regex=False).astype(int)
    return df


def _ordered_required_conditions(
    df: pd.DataFrame,
    condition_col: str,
    required_conditions: Sequence[str] | None,
) -> list[str]:
    if required_conditions is not None:
        return [str(canonical_condition_name(condition)) for condition in required_conditions]

    present = {
        str(canonical_condition_name(condition))
        for condition in df[condition_col].dropna().unique()
    }
    known_present = [condition for condition in _KNOWN_CONDITIONS if condition in present]
    other_present = sorted(present - set(known_present))
    return known_present + other_present


def get_complete_replay_models(
    df: pd.DataFrame,
    model_col: str = "replay_model_canonical",
    condition_col: str = "condition",
    required_conditions: Sequence[str] | None = None,
    model_order: Sequence[str] | None = None,
) -> list[str]:
    """Return models with at least one row for every required condition."""
    required = set(_ordered_required_conditions(df, condition_col, required_conditions))
    if model_order is None:
        model_order = get_present_strategist_model_order(df, model_col=model_col)

    complete = []
    for model_id in model_order:
        model_conditions = {
            str(canonical_condition_name(condition))
            for condition in df.loc[df[model_col] == model_id, condition_col].dropna().unique()
        }
        if required.issubset(model_conditions):
            complete.append(model_id)
    return complete


def filter_complete_replay_models(
    df: pd.DataFrame,
    model_col: str = "replay_model_canonical",
    condition_col: str = "condition",
    required_conditions: Sequence[str] | None = None,
    model_order: Sequence[str] | None = None,
    print_summary: bool = True,
) -> tuple[pd.DataFrame, list[str]]:
    """Filter replay data to models with every required condition."""
    if model_order is None:
        model_order = get_present_strategist_model_order(df, model_col=model_col)

    complete_models = get_complete_replay_models(
        df,
        model_col=model_col,
        condition_col=condition_col,
        required_conditions=required_conditions,
        model_order=model_order,
    )
    skipped = [model for model in model_order if model not in complete_models]
    filtered = df[df[model_col].isin(complete_models)].copy()

    if print_summary:
        print(f"Using {len(complete_models)} complete replay models.")
        if skipped:
            print(f"Skipped incomplete replay models: {', '.join(skipped)}")

    return filtered, complete_models


def tier_source_columns(tiers: Sequence[str]) -> list[str]:
    """Return source tier column names for tagged trail CSVs."""
    return [f"tier_{tier}" for tier in tiers]


def prefixed_tier_columns(tiers: Sequence[str], prefix: str) -> list[str]:
    """Return safe tier column names with a prefix, e.g. ``rea_tier_Explicit``."""
    return [f"{prefix}_tier_{safe_tier_name(tier)}" for tier in tiers]


def _parse_filename(filename: str) -> tuple[str, str]:
    """Extract (condition, replay_model) from a replay CSV filename.

    The filename format is ``nuke-{condition}-{model}-results.csv``.
    Since both conditions and model names can contain hyphens, resolve
    ambiguity by trying known condition prefixes longest-first.
    """
    stem = filename.removesuffix("-results.csv").removeprefix("nuke-")
    for condition in sorted(_FILENAME_CONDITIONS, key=len, reverse=True):
        prefix = f"{condition}-"
        if stem.startswith(prefix):
            return str(canonical_condition_name(condition)), stem.removeprefix(prefix)
    raise ValueError(f"Could not parse known condition from replay filename: {filename}")


def _fill_unanimous_replay_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing replay metrics from unanimous same-instance before values."""
    def unanimous_non_null_value(values: pd.Series) -> float:
        non_null = values.dropna()
        if non_null.nunique(dropna=True) == 1:
            return non_null.iloc[0]
        return float("nan")

    for column in [*_REPLAY_FILL_COLUMNS, *_ORIGINAL_METRIC_COLUMNS]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    grouped = df.groupby(_REPLAY_INSTANCE_COLUMNS, dropna=False)

    for column in _ORIGINAL_METRIC_COLUMNS:
        fill_values = grouped[column].transform(unanimous_non_null_value)
        df[column] = pd.to_numeric(
            df[column].where(df[column].notna(), fill_values),
            errors="coerce",
        )

    for replay_column, before_column in _REPLAY_FILL_COLUMNS.items():
        fill_values = grouped[before_column].transform(unanimous_non_null_value)
        df[replay_column] = pd.to_numeric(
            df[replay_column].where(df[replay_column].notna(), fill_values),
            errors="coerce",
        )

    return df


def load_replay_data(
    replay_dir: str | Path | None = None,
    print_metadata: bool = True,
) -> pd.DataFrame:
    """Read all replay CSVs and return a combined DataFrame with a condition column.

    Parameters
    ----------
    replay_dir : path, optional
        Directory containing ``nuke-*-results.csv`` files.
        Defaults to ``nuke/replay/`` relative to this script.
    print_metadata : bool
        If True, print a short summary after loading.
    """
    replay_dir = Path(replay_dir) if replay_dir else _DEFAULT_REPLAY_DIR
    csv_files = sorted(replay_dir.glob("nuke-*-results.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No replay CSVs found in {replay_dir}")

    frames: list[pd.DataFrame] = []
    for csv_path in csv_files:
        df = pd.read_csv(csv_path)
        condition, replay_model = _parse_filename(csv_path.name)
        df["condition"] = condition
        df["replay_model"] = replay_model
        df["source_file"] = csv_path.name
        frames.append(df)

    combined = pd.concat(frames, ignore_index=True)
    combined["condition"] = pd.Categorical(
        combined["condition"],
        categories=_KNOWN_CONDITIONS,
        ordered=True,
    )
    combined = combined.sort_values(["condition", "replay_model", "source_file"]).reset_index(drop=True)
    combined = _fill_unanimous_replay_values(combined)

    # Compute delta columns
    for metric in ("nuke", "use_nuke"):
        combined[f"original_{metric}_delta"] = combined[f"after_{metric}"] - combined[f"prev_{metric}"]
        combined[f"replay_{metric}_delta"] = combined[f"replay_{metric}"] - combined[f"prev_{metric}"]
        combined[f"{metric}_deviation"] = combined[f"replay_{metric}"] - combined[f"after_{metric}"]

    if print_metadata:
        _print_summary(combined)

    return combined


def _print_summary(df: pd.DataFrame) -> None:
    n_files = df["source_file"].nunique()
    present_conditions = set(df["condition"].astype(str))
    conditions = [condition for condition in _KNOWN_CONDITIONS if condition in present_conditions]
    models = sorted(df["replay_model"].unique())

    ct = df.groupby(["condition", "replay_model"], observed=True).size().unstack(fill_value=0)
    ct = ct.reindex(conditions)
    ct["Total"] = ct.sum(axis=1)
    totals = ct.sum(axis=0)
    totals.name = "Total"
    ct = pd.concat([ct, totals.to_frame().T])

    # Build a fixed-width table
    row_labels = list(ct.index)
    col_labels = list(ct.columns)
    row_w = max(len(str(r)) for r in row_labels) + 2
    col_w = max(max(len(str(c)) for c in col_labels), 6) + 2

    header = "".rjust(row_w) + "".join(str(c).rjust(col_w) for c in col_labels)
    sep = "\u2500" * len(header)

    lines = [
        f"\u2713 Loaded {len(df):,} rows from {n_files} files",
        f"  Conditions   : {', '.join(conditions)}",
        f"  Replay models: {', '.join(models)}",
        "",
        "  Rows per condition \u00d7 replay model:",
        f"  {sep}",
        f"  {header}",
        f"  {sep}",
    ]
    for label in row_labels:
        row_str = str(label).rjust(row_w)
        row_str += "".join(str(int(ct.loc[label, c])).rjust(col_w) for c in col_labels)
        lines.append(f"  {row_str}")
        if label == row_labels[-2]:  # separator before totals row
            lines.append(f"  {sep}")
    lines.append(f"  {sep}")

    print("\n".join(lines))
