"""
Shared CSV loading, mapping, and filter helpers for panel and turn data.
"""

from __future__ import annotations

import pandas as pd

from .experiments import (
    CONDITION_PLAYER_MAPPING,
    DEFAULT_EXCLUDED_EXPERIMENTS,
    NON_LLM_EXPERIMENTS,
    VANILLA_EXPERIMENTS,
    iter_condition_player_rows,
)


def filter_non_llm_games(df, keep_null_ai=False):
    col = "condition" if "condition" in df.columns else "experiment"
    exclude = VANILLA_EXPERIMENTS if keep_null_ai else NON_LLM_EXPERIMENTS
    return df[~df[col].isin(exclude)]


def _load_csv_with_condition_mapping(csv_path):
    df = pd.read_csv(csv_path)
    if "experiment" in df.columns:
        df["condition"] = df["experiment"]
    return df


def _apply_player_type_mapping(df, skip_mapping=False):
    if skip_mapping:
        df = df.copy()
        df["player_type"] = "Player " + df["player_id"].astype(str)
        return df

    mapping_df = pd.DataFrame(iter_condition_player_rows())
    if mapping_df.empty:
        df = df.copy()
        df["player_type"] = "Player " + df["player_id"].astype(str)
        return df

    df_with_types = df.merge(
        mapping_df,
        on=["condition", "player_id"],
        how="left",
    )
    df_with_types["player_type"] = df_with_types["player_type"].fillna(
        "Player " + df_with_types["player_id"].astype(str)
    )
    return df_with_types


def _apply_data_filters(
    df,
    player_id=None,
    version_filter=None,
    condition_exclude=None,
    condition_include=None,
    turn_filter=None,
    min_turn=None,
    max_turn=None,
    exclude_non_llm=False,
):
    cond_col = "condition" if "condition" in df.columns else "experiment"

    if version_filter is not None and "version" in df.columns:
        df = df[df["version"] == version_filter]

    if DEFAULT_EXCLUDED_EXPERIMENTS:
        df = df[~df[cond_col].isin(DEFAULT_EXCLUDED_EXPERIMENTS)]

    if exclude_non_llm:
        df = df[~df[cond_col].isin(NON_LLM_EXPERIMENTS)]

    if condition_exclude is not None:
        if isinstance(condition_exclude, (list, tuple)):
            df = df[~df[cond_col].isin(condition_exclude)]
        else:
            df = df[df[cond_col] != condition_exclude]

    if condition_include is not None:
        if isinstance(condition_include, (list, tuple)):
            df = df[df[cond_col].isin(condition_include)]
        else:
            df = df[df[cond_col] == condition_include]

    if player_id is not None:
        df = df[df["player_id"] == player_id]

    if "turn" in df.columns:
        if turn_filter is not None:
            df = df[df["turn"] == turn_filter]
        if min_turn is not None:
            df = df[df["turn"] >= min_turn]
        if max_turn is not None:
            df = df[df["turn"] <= max_turn]

    return df


def _print_data_summary(df, data_type="panel", filters_info=None):
    print(f"\u2713 Loaded {data_type} data: {len(df)} rows")

    if filters_info:
        filters_applied = []
        for key, value in filters_info.items():
            if value is not None:
                filters_applied.append(f"{key}={value}")
        if filters_applied:
            print(f"\u2713 Filters applied: {', '.join(filters_applied)}")

    if "condition" in df.columns:
        print(f"\u2713 Unique conditions: {df['condition'].nunique()}")

    if "player_type" in df.columns:
        print(f"\u2713 Unique player types: {df['player_type'].nunique()}")

    if data_type == "turn" and "turn" in df.columns:
        print(f"\u2713 Turn range: {df['turn'].min()} - {df['turn'].max()}")

    if data_type == "turn" and "civilization" in df.columns:
        print(f"\u2713 Unique civilizations: {df['civilization'].nunique()}")

    if "player_type" in df.columns:
        print("\nPlayer Type Distribution:")
        player_type_counts = df.groupby("player_type").size().sort_values(ascending=False)
        for player_type, count in player_type_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {player_type}: {count} rows ({percentage:.1f}%)")

    if "condition" in df.columns and df["condition"].nunique() > 1:
        print("\nCondition Distribution:")
        condition_counts = df.groupby("condition").size().sort_values(ascending=False)
        for condition, count in condition_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {condition}: {count} rows ({percentage:.1f}%)")

    if data_type == "turn" and "game_id" in df.columns:
        print(f"\n\u2713 Unique games: {df['game_id'].nunique()}")

    if data_type == "turn" and "civilization" in df.columns:
        print("\nCivilization Distribution:")
        civ_counts = df.groupby("civilization").size().sort_values(ascending=False).head(10)
        for civ, count in civ_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {civ}: {count} rows ({percentage:.1f}%)")


def load_turn_data(
    csv_path="turn_data.csv",
    player_id=None,
    version_filter=None,
    condition_exclude=None,
    turn_filter=None,
    min_turn=None,
    max_turn=None,
    print_metadata=True,
    exclude_non_llm=False,
    skip_mapping=False,
):
    df = _load_csv_with_condition_mapping(csv_path)
    df = _apply_player_type_mapping(df, skip_mapping=skip_mapping)
    df = _apply_data_filters(
        df,
        player_id=player_id,
        version_filter=version_filter,
        condition_exclude=condition_exclude,
        turn_filter=turn_filter,
        min_turn=min_turn,
        max_turn=max_turn,
        exclude_non_llm=exclude_non_llm,
    )
    df["turn_progress"] = round(df["turn"] / df["max_turn"], 2)

    if print_metadata:
        filters_info = {
            "player_id": player_id,
            "version": version_filter,
            "condition_exclude": condition_exclude,
            "exclude_non_llm": exclude_non_llm if exclude_non_llm else None,
            "turn": turn_filter,
            "min_turn": min_turn,
            "max_turn": max_turn,
        }
        _print_data_summary(df, data_type="turn", filters_info=filters_info)

    return df


def load_panel_data(
    csv_path="panel_data.csv",
    player_id=None,
    version_filter=None,
    condition_exclude=None,
    condition_include=None,
    print_metadata=True,
    exclude_non_llm=False,
    skip_mapping=False,
):
    df = _load_csv_with_condition_mapping(csv_path)
    df = _apply_player_type_mapping(df, skip_mapping=skip_mapping)
    df = _apply_data_filters(
        df,
        player_id=player_id,
        version_filter=version_filter,
        condition_exclude=condition_exclude,
        condition_include=condition_include,
        exclude_non_llm=exclude_non_llm,
    )

    if print_metadata:
        filters_info = {
            "player_id": player_id,
            "version": version_filter,
            "condition_exclude": condition_exclude,
            "condition_include": condition_include,
            "exclude_non_llm": exclude_non_llm if exclude_non_llm else None,
        }
        _print_data_summary(df, data_type="panel", filters_info=filters_info)

    return df
