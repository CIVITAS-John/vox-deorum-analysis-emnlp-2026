#!/usr/bin/env python3
"""
Check whether reconstructed slot order matters for adjusted_strength.

This reproduces the strength pipeline from ratings.iterative_bt.prepare_strength_data
but intentionally keeps non-LLM experiments so we can inspect the vanilla-only
baseline (`observe-vanilla-standard`).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# Add analysis root so shared utilities resolve when run as a script.
_ANALYSIS_ROOT = str(Path(__file__).resolve().parent.parent)
if _ANALYSIS_ROOT not in sys.path:
    sys.path.insert(0, _ANALYSIS_ROOT)

from shared.plot_utilities import inv_logit, load_turn_data, logit


DEFAULT_PREDICTIONS = "models/output/attention_mlp_predictions.csv"
DEFAULT_EXPERIMENT = "observe-vanilla-standard"


def build_strength_df(turn_data_path: str) -> pd.DataFrame:
    """Recreate civ-adjusted strength without filtering out non-LLM games."""
    turn_df = load_turn_data(turn_data_path, condition_exclude=[], print_metadata=False)

    filtered = turn_df[turn_df["turn_progress"] > 0.2].copy()
    turn_progress_avg = filtered.groupby(
        ["game_id", "player_id", "turn_progress"]
    ).agg(
        {
            "predicted_win_probability": "mean",
            "player_type": "first",
            "experiment": "first",
            "is_winner": "last",
            "civilization": "first",
        }
    ).reset_index()
    turn_progress_avg["weight"] = turn_progress_avg["turn_progress"]

    records = []
    for (game_id, player_id), grp in turn_progress_avg.groupby(["game_id", "player_id"]):
        weights = grp["weight"]
        probs = grp["predicted_win_probability"]
        weighted_avg = (weights * probs).sum() / weights.sum()
        records.append(
            {
                "game_id": game_id,
                "player_id": player_id,
                "player_type": grp["player_type"].iloc[0],
                "civilization": grp["civilization"].iloc[0],
                "experiment": grp["experiment"].iloc[0],
                "weighted_strength": weighted_avg,
                "is_winner": grp["is_winner"].iloc[-1],
            }
        )

    strength_df = pd.DataFrame(records)

    game_max = strength_df.groupby("game_id")["weighted_strength"].max().rename(
        "max_weighted_strength"
    )
    strength_df = strength_df.merge(game_max, on="game_id")
    strength_df["relative_strength"] = (
        strength_df["weighted_strength"] / strength_df["max_weighted_strength"]
    )

    winner_mask = (
        (strength_df["is_winner"] == 1) & (strength_df["relative_strength"] < 1.0)
    )
    strength_df.loc[winner_mask, "weighted_strength"] = (
        strength_df.loc[winner_mask, "max_weighted_strength"] + 0.001
    )
    strength_df.loc[winner_mask, "relative_strength"] = 1.0

    strength_df["logit_strength"] = logit(strength_df["relative_strength"])
    model = ols(
        'logit_strength ~ C(civilization, Sum) + C(player_type, Treatment(reference="Vanilla"))',
        data=strength_df,
    ).fit()

    civ_effects = {}
    civ_terms = [name for name in model.params.index if "civilization" in name]
    for term in civ_terms:
        civ_name = term.split("[S.")[-1].rstrip("]")
        civ_effects[civ_name] = model.params[term]
    civ_effects["Venice"] = -sum(civ_effects.values())

    civ_adjustment = strength_df["civilization"].map(civ_effects).fillna(0.0)
    strength_df["adjusted_strength"] = inv_logit(
        logit(strength_df["relative_strength"]) - civ_adjustment
    )
    return strength_df.drop(columns=["logit_strength"])


def assign_slot_ids(strength_df: pd.DataFrame) -> pd.DataFrame:
    """Reconstruct slot IDs exactly the way the ratings code does."""
    slot_ids = pd.Series(index=strength_df.index, dtype=object)
    for _, game in strength_df.groupby("game_id", sort=False):
        type_counters: dict[str, int] = {}
        for idx in game.index:
            player_type = strength_df.at[idx, "player_type"]
            count = type_counters.get(player_type, 0)
            slot_ids.at[idx] = f"{player_type}_{count}"
            type_counters[player_type] = count + 1
    return strength_df.assign(slot_id=slot_ids)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check whether slot order matters in vanilla adjusted_strength."
    )
    parser.add_argument(
        "--predictions",
        default=DEFAULT_PREDICTIONS,
        help=f"Predictions CSV to analyze (default: {DEFAULT_PREDICTIONS})",
    )
    parser.add_argument(
        "--experiment",
        default=DEFAULT_EXPERIMENT,
        help=f"Experiment to isolate (default: {DEFAULT_EXPERIMENT})",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    strength_df = build_strength_df(args.predictions)
    subset = assign_slot_ids(
        strength_df[strength_df["experiment"] == args.experiment].copy()
    )

    if subset.empty:
        raise SystemExit(f"No rows found for experiment: {args.experiment}")

    print("=" * 80)
    print(f"SLOT EFFECT CHECK: {args.experiment}")
    print("=" * 80)
    print(
        f"Rows: {len(subset)} | Games: {subset['game_id'].nunique()} | "
        f"Slots: {subset['slot_id'].nunique()}"
    )
    print()

    mapping = (
        subset[["slot_id", "player_id"]]
        .drop_duplicates()
        .sort_values(["slot_id", "player_id"])
    )
    print("Slot-to-player_id mapping:")
    print(mapping.to_string(index=False))
    print()

    summary = (
        subset.groupby(["slot_id", "player_id"])
        .agg(
            count=("adjusted_strength", "count"),
            win_rate=("is_winner", "mean"),
            raw_str_mean=("weighted_strength", "mean"),
            raw_str_std=("weighted_strength", "std"),
            adj_str_mean=("adjusted_strength", "mean"),
            adj_str_std=("adjusted_strength", "std"),
            adj_str_min=("adjusted_strength", "min"),
            adj_str_max=("adjusted_strength", "max"),
        )
        .reset_index()
        .sort_values("player_id")
    )
    print("Per-slot summary (win_rate = raw wins / games):")
    print(summary.to_string(index=False))
    print()

    grand_raw_mean = subset["weighted_strength"].mean()
    grand_adj_mean = subset["adjusted_strength"].mean()
    grand_win_rate = subset["is_winner"].mean()
    slot_raw_means = subset.groupby("slot_id")["weighted_strength"].mean()
    slot_adj_means = subset.groupby("slot_id")["adjusted_strength"].mean()
    slot_win_rates = subset.groupby("slot_id")["is_winner"].mean()
    print(f"Grand mean raw_strength:      {grand_raw_mean:.6f}")
    print(f"Grand mean adjusted_strength: {grand_adj_mean:.6f}")
    print(f"Grand mean win_rate:          {grand_win_rate:.6f}")
    print(
        "Max absolute slot raw_strength gap from grand mean:      "
        f"{(slot_raw_means - grand_raw_mean).abs().max():.6f}"
    )
    print(
        "Max absolute slot adjusted_strength gap from grand mean: "
        f"{(slot_adj_means - grand_adj_mean).abs().max():.6f}"
    )
    print(
        "Max absolute slot win_rate gap from grand mean:          "
        f"{(slot_win_rates - grand_win_rate).abs().max():.6f}"
    )
    print()

    for label, col in [("raw_strength (weighted_strength)", "weighted_strength"),
                        ("adjusted_strength", "adjusted_strength")]:
        reduced = ols(f"{col} ~ C(game_id)", data=subset).fit()
        full = ols(f"{col} ~ C(game_id) + C(slot_id)", data=subset).fit()
        comparison = anova_lm(reduced, full)
        row = comparison.iloc[1]

        print(f"Game-fixed-effects slot test ({label}):")
        print(f"  df_diff: {row['df_diff']:.0f}")
        print(f"  F:       {row['F']:.6f}")
        print(f"  p-value: {row['Pr(>F)']:.6f}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
