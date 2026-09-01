"""Utilities for explicit deductive-code analysis."""

from __future__ import annotations

import re
import warnings
from collections import OrderedDict
from typing import Iterable, Mapping, Sequence

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


CODE_PREFIX = "code_"

CODE_GROUPS: Mapping[str, tuple[str, ...]] = OrderedDict(
    [
        (
            "Moderating Factors",
            (
                "ethical-prompt-directive",
                "ethical-prompt-constraint",
                "ethical-prompt-acknowledgement",
                "diplomatic-costs",
                "conventional-sufficiency",
                "counterproductive-to-victory",
                "collateral-damages",
                "lack-of-capability",
                "cause-retaliation",
            ),
        ),
        (
            "Escalating Factors",
            (
                "game-scenario",
                "leader-persona",
                "previous-rationale",
                "critical-situations",
                "existing-investment",
                "pursuing-domination",
                "nuke-victim",
                "credible-deterrence",
            ),
        ),
    ]
)

CODE_LABELS: Mapping[str, str] = {
    "ethical-prompt-directive": "Ethical Prompt: Directive",
    "ethical-prompt-constraint": "Ethical Prompt: Constraint",
    "ethical-prompt-acknowledgement": "Ethical Prompt: Acknowledgement",
    "diplomatic-costs": "Diplomatic Costs",
    "conventional-sufficiency": "Conventional Sufficiency",
    "counterproductive-to-victory": "Counterproductive to Victory",
    "collateral-damages": "Collateral Damages",
    "lack-of-capability": "Lack of Capability",
    "cause-retaliation": "Cause Retaliation",
    "game-scenario": "Game Scenario",
    "leader-persona": "Leader Persona",
    "previous-rationale": "Previous Rationale",
    "critical-situations": "Critical Situations",
    "existing-investment": "Existing Investment",
    "pursuing-domination": "Pursuing Domination",
    "nuke-victim": "Nuke Victim",
    "credible-deterrence": "Credible Deterrence",
}
DISPLAY_LABEL_TO_CODE_LABEL = {display: label for label, display in CODE_LABELS.items()}

CODE_COLORS: Mapping[str, str] = {
    "ethical-prompt-directive": "#2CB1A1",
    "ethical-prompt-constraint": "#5BC8BC",
    "ethical-prompt-acknowledgement": "#90DED6",
    "diplomatic-costs": "#3B6EA8",
    "conventional-sufficiency": "#4F83BD",
    "counterproductive-to-victory": "#6797CA",
    "collateral-damages": "#80ACD6",
    "lack-of-capability": "#99C0E2",
    "cause-retaliation": "#B2D5EE",
    "game-scenario": "#A83232",
    "leader-persona": "#B74436",
    "previous-rationale": "#C6553A",
    "critical-situations": "#D4663E",
    "existing-investment": "#E07945",
    "pursuing-domination": "#EA8D52",
    "nuke-victim": "#F2A264",
    "credible-deterrence": "#F8B878",
}


ORTHODOX_CODE_LABELS = tuple(
    label for labels in CODE_GROUPS.values() for label in labels
)
ORTHODOX_CODE_SET = set(ORTHODOX_CODE_LABELS)


def sanitize_code_label(label: str) -> str:
    """Return a stable snake-case suffix for a deductive-code label."""
    return re.sub(r"_+", "_", re.sub(r"[^0-9a-zA-Z]+", "_", str(label).strip().lower())).strip("_")


def code_column(label: str, prefix: str = CODE_PREFIX) -> str:
    """Return the binary column name for a deductive-code label."""
    return f"{prefix}{sanitize_code_label(label)}"


def code_columns(labels: Iterable[str] | None = None, prefix: str = CODE_PREFIX) -> list[str]:
    """Return ordered binary code columns for labels, defaulting to orthodox taxonomy."""
    source = ORTHODOX_CODE_LABELS if labels is None else labels
    return [code_column(label, prefix=prefix) for label in source]


def code_label_from_column(column: str, prefix: str = CODE_PREFIX) -> str:
    """Recover a hyphenated code label from a code column name."""
    column = str(column)
    if column in DISPLAY_LABEL_TO_CODE_LABEL:
        return DISPLAY_LABEL_TO_CODE_LABEL[column]
    if column.startswith(prefix):
        column = column.removeprefix(prefix)
    return column.replace("_", "-")


def display_label(label_or_column: str) -> str:
    """Return a display label for a code label or code column."""
    label = code_label_from_column(label_or_column)
    return CODE_LABELS.get(label, label.replace("-", " ").title())


def display_labels(labels_or_columns: Iterable[str]) -> list[str]:
    """Return display labels for code labels or code columns."""
    return [display_label(value) for value in labels_or_columns]


def code_group(label_or_column: str) -> str | None:
    """Return the taxonomy group for a code label or column."""
    label = code_label_from_column(label_or_column)
    for group, labels in CODE_GROUPS.items():
        if label in labels:
            return group
    return None


def code_color(label_or_column: str, fallback: str = "#888888") -> str:
    """Return the taxonomy color for a code label or column."""
    label = code_label_from_column(label_or_column)
    return CODE_COLORS.get(label, fallback)


def code_colors(labels_or_columns: Iterable[str]) -> list[str]:
    """Return taxonomy colors for code labels or columns."""
    return [code_color(value) for value in labels_or_columns]


def split_orthodox_unorthodox(labels: Iterable[str]) -> tuple[list[str], list[str]]:
    """Split labels into orthodox taxonomy labels and unorthodox extras."""
    labels = list(labels)
    label_set = set(labels)
    orthodox = [label for label in ORTHODOX_CODE_LABELS if label in label_set]
    unorthodox = sorted(label for label in labels if label not in ORTHODOX_CODE_SET)
    return orthodox, unorthodox


def warn_unorthodox_codes(unorthodox: Sequence[str], action: str = "Dropping") -> None:
    """Emit a visible warning for unorthodox labels."""
    if unorthodox:
        warnings.warn(
            f"{action} unorthodox deductive tags: {', '.join(unorthodox)}",
            UserWarning,
            stacklevel=2,
        )


def filter_orthodox_code_labels(labels: Iterable[str], warn: bool = True) -> list[str]:
    """Return orthodox labels in taxonomy order and optionally warn about extras."""
    orthodox, unorthodox = split_orthodox_unorthodox(labels)
    if warn:
        warn_unorthodox_codes(unorthodox)
    return orthodox


def ordered_code_columns_from_df(df: pd.DataFrame, prefix: str = CODE_PREFIX, warn: bool = True) -> list[str]:
    """Return present orthodox code columns in taxonomy order, warning on extras."""
    present_labels = [
        code_label_from_column(column, prefix=prefix)
        for column in df.columns
        if str(column).startswith(prefix)
    ]
    orthodox_labels, unorthodox = split_orthodox_unorthodox(present_labels)
    if warn:
        warn_unorthodox_codes(unorthodox, action="Ignoring")
    return [code_column(label, prefix=prefix) for label in orthodox_labels if code_column(label, prefix=prefix) in df.columns]


def assert_binary_code_columns(df: pd.DataFrame, columns: Sequence[str]) -> None:
    """Raise if any provided code column contains values other than 0/1."""
    bad_binary = {
        column: sorted(set(df[column].dropna().unique()) - {0, 1})
        for column in columns
        if column in df.columns and set(df[column].dropna().unique()) - {0, 1}
    }
    if bad_binary:
        raise AssertionError(f"Non-binary code columns found: {bad_binary}")


def apply_code_tick_colors(ax, axis: str = "x") -> None:
    """Color tick labels according to the deductive-code taxonomy."""
    ticks = ax.get_xticklabels() if axis == "x" else ax.get_yticklabels()
    for tick in ticks:
        tick.set_color(code_color(tick.get_text()))


def plot_code_frequency_bar(
    df: pd.DataFrame,
    columns: Sequence[str],
    title: str = "Deductive Code Frequency",
    xlabel: str = "Tagged threads",
    figsize: tuple[float, float] | None = None,
    weight_col: str | None = None,
):
    """Plot colored deductive-code frequency counts in taxonomy order."""
    columns = list(columns)
    if not columns:
        raise ValueError("No code columns provided")

    if weight_col is None:
        counts = df[columns].sum().astype(float)
    else:
        weights = pd.to_numeric(df[weight_col], errors="coerce")
        counts = df[columns].mul(weights, axis=0).sum().astype(float)

    if figsize is None:
        figsize = (10, max(4, 0.36 * len(columns)))

    fig, ax = plt.subplots(figsize=figsize)
    labels = display_labels(columns)
    y_pos = range(len(columns))
    ax.barh(y_pos, counts.values, color=code_colors(columns), alpha=0.9)
    ax.set_yticks(list(y_pos))
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("")
    ax.grid(axis="x", alpha=0.25)

    for i, value in enumerate(counts.values):
        ax.text(value, i, f" {value:.0f}", va="center", fontsize=9)

    apply_code_tick_colors(ax, axis="y")
    plt.tight_layout()
    return fig, ax


def _blank_zero_annotations(matrix: pd.DataFrame, fmt: str = ".1f") -> pd.DataFrame:
    """Return formatted annotation strings, leaving exact zero/NaN cells blank."""
    return matrix.apply(lambda column: column.map(lambda value: "" if pd.isna(value) or value == 0 else format(value, fmt)))


def _default_heatmap_figsize(matrix: pd.DataFrame) -> tuple[float, float]:
    """Pick a readable default size for code-by-row heatmaps."""
    return (
        max(10.0, 0.58 * matrix.shape[1]),
        max(3.0, 0.45 * matrix.shape[0]),
    )


def plot_code_heatmap(
    matrix: pd.DataFrame,
    title: str,
    cbar_label: str,
    cmap: str = "YlOrRd",
    center: float | None = None,
    fmt: str = ".1f",
    blank_zeros: bool = False,
    annotations: pd.DataFrame | None = None,
    figsize: tuple[float, float] | None = None,
    square: bool = False,
):
    """Plot a code-column heatmap with taxonomy-colored code tick labels."""
    if figsize is None:
        figsize = _default_heatmap_figsize(matrix)

    if annotations is not None:
        annot = annotations
        annot_fmt = ""
    elif blank_zeros:
        annot = _blank_zero_annotations(matrix, fmt=fmt)
        annot_fmt = ""
    else:
        annot = True
        annot_fmt = fmt

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        matrix,
        annot=annot,
        fmt=annot_fmt,
        cmap=cmap,
        center=center,
        square=square,
        linewidths=0.5,
        linecolor="white",
        cbar_kws={"label": cbar_label},
        ax=ax,
    )
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel("")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    apply_code_tick_colors(ax, axis="x")
    apply_code_tick_colors(ax, axis="y")
    plt.tight_layout()
    return fig, ax


def code_prevalence_matrix(
    df: pd.DataFrame,
    columns: Sequence[str],
    group_col: str,
    group_order: Sequence[str] | None = None,
    include_overall: bool = True,
    weight_col: str | None = None,
) -> pd.DataFrame:
    """Return percent prevalence by group, optionally with an overall row."""
    columns = list(columns)

    if weight_col is None:
        matrix = df.groupby(group_col, observed=True)[columns].mean().mul(100)
    else:
        def _weighted_prevalence(group: pd.DataFrame) -> pd.Series:
            weights = pd.to_numeric(group[weight_col], errors="coerce")
            denominator = weights.sum()
            if denominator == 0 or pd.isna(denominator):
                return pd.Series(np.nan, index=columns, dtype=float)
            return group[columns].mul(weights, axis=0).sum().div(denominator).mul(100)

        matrix = df.groupby(group_col, observed=True).apply(_weighted_prevalence)

    if group_order is not None:
        matrix = matrix.reindex(group_order)
    else:
        matrix = matrix.sort_index()

    if include_overall:
        if weight_col is None:
            overall = df[columns].mean().mul(100).to_frame().T
        else:
            weights = pd.to_numeric(df[weight_col], errors="coerce")
            denominator = weights.sum()
            overall = (
                df[columns].mul(weights, axis=0).sum().div(denominator).mul(100).to_frame().T
                if denominator != 0 and not pd.isna(denominator)
                else pd.DataFrame([[np.nan] * len(columns)], columns=columns)
            )
        overall.index = ["Overall"]
        matrix = pd.concat([overall, matrix])

    matrix.columns = display_labels(columns)
    return matrix


def plot_code_prevalence_heatmap(
    df: pd.DataFrame,
    columns: Sequence[str],
    group_col: str,
    group_order: Sequence[str] | None = None,
    title: str | None = None,
    figsize: tuple[float, float] | None = None,
    weight_col: str | None = None,
):
    """Plot code prevalence by group with an Overall row."""
    matrix = code_prevalence_matrix(
        df,
        columns=columns,
        group_col=group_col,
        group_order=group_order,
        include_overall=True,
        weight_col=weight_col,
    )
    return (*plot_code_heatmap(
        matrix,
        title=title or f"Deductive Code Prevalence by {group_col}",
        cbar_label="% of rows" if weight_col is None else "% of weighted rows",
        cmap="YlOrRd",
        fmt=".1f",
        figsize=figsize,
    ), matrix)


def code_cooccurrence_matrix(
    df: pd.DataFrame,
    columns: Sequence[str],
) -> pd.DataFrame:
    """Return Jaccard co-occurrence among binary code columns."""
    columns = list(columns)
    binary = df[columns].fillna(0).astype(int).clip(0, 1).to_numpy()
    intersection = binary.T @ binary
    counts = np.diag(intersection).astype(float)
    union = counts[:, None] + counts[None, :] - intersection
    jaccard = np.divide(
        intersection,
        union,
        out=np.zeros_like(intersection, dtype=float),
        where=union > 0,
    )
    labels = display_labels(columns)
    return pd.DataFrame(jaccard, index=labels, columns=labels)


def plot_code_cooccurrence_heatmap(
    df: pd.DataFrame,
    columns: Sequence[str],
    title: str = "Deductive Code Co-occurrence (Jaccard Similarity)",
    figsize: tuple[float, float] | None = None,
):
    """Plot Jaccard co-occurrence, annotating all non-zero cells."""
    matrix = code_cooccurrence_matrix(df, columns=columns)
    return (*plot_code_heatmap(
        matrix,
        title=title,
        cbar_label="Jaccard similarity",
        cmap="YlOrRd",
        fmt=".2f",
        blank_zeros=True,
        figsize=figsize,
        square=True,
    ), matrix)


def code_metric_matrix_by_group(
    df: pd.DataFrame,
    columns: Sequence[str],
    metric_col: str,
    group_col: str,
    group_order: Sequence[str] | None = None,
    include_overall: bool = True,
    min_examples: int | None = None,
) -> pd.DataFrame:
    """Return mean metric by code for Overall plus each group."""
    columns = list(columns)
    groups = list(group_order) if group_order is not None else sorted(df[group_col].dropna().unique())
    rows = []
    index = []

    if include_overall:
        rows.append([
            df.loc[df[column] == 1, metric_col].mean()
            if min_examples is None or df.loc[df[column] == 1, metric_col].notna().sum() >= min_examples
            else float("nan")
            for column in columns
        ])
        index.append("Overall")

    for group in groups:
        group_df = df[df[group_col] == group]
        rows.append([
            group_df.loc[group_df[column] == 1, metric_col].mean()
            if min_examples is None or group_df.loc[group_df[column] == 1, metric_col].notna().sum() >= min_examples
            else float("nan")
            for column in columns
        ])
        index.append(group)

    matrix = pd.DataFrame(rows, index=index, columns=display_labels(columns))
    return matrix


def code_metric_std_matrix_by_group(
    df: pd.DataFrame,
    columns: Sequence[str],
    metric_col: str,
    group_col: str,
    group_order: Sequence[str] | None = None,
    include_overall: bool = True,
    min_examples: int | None = None,
) -> pd.DataFrame:
    """Return metric standard deviation by code for Overall plus each group."""
    columns = list(columns)
    groups = list(group_order) if group_order is not None else sorted(df[group_col].dropna().unique())
    rows = []
    index = []

    if include_overall:
        rows.append([
            df.loc[df[column] == 1, metric_col].std()
            if min_examples is None or df.loc[df[column] == 1, metric_col].notna().sum() >= min_examples
            else float("nan")
            for column in columns
        ])
        index.append("Overall")

    for group in groups:
        group_df = df[df[group_col] == group]
        rows.append([
            group_df.loc[group_df[column] == 1, metric_col].std()
            if min_examples is None or group_df.loc[group_df[column] == 1, metric_col].notna().sum() >= min_examples
            else float("nan")
            for column in columns
        ])
        index.append(group)

    matrix = pd.DataFrame(rows, index=index, columns=display_labels(columns))
    return matrix


def _mean_std_annotations(mean_matrix: pd.DataFrame, std_matrix: pd.DataFrame) -> pd.DataFrame:
    """Return heatmap annotations with mean +/- standard deviation."""
    annotations = pd.DataFrame("", index=mean_matrix.index, columns=mean_matrix.columns)
    for row in mean_matrix.index:
        for col in mean_matrix.columns:
            mean_value = mean_matrix.loc[row, col]
            std_value = std_matrix.loc[row, col]
            if pd.isna(mean_value):
                annotations.loc[row, col] = "N/A"
            elif pd.isna(std_value):
                annotations.loc[row, col] = f"{mean_value:.1f}\n± n/a"
            else:
                annotations.loc[row, col] = f"{mean_value:.1f}\n± {std_value:.1f}"
    return annotations


def plot_code_metric_heatmap_by_group(
    df: pd.DataFrame,
    columns: Sequence[str],
    metric_col: str,
    group_col: str,
    group_order: Sequence[str] | None = None,
    title: str | None = None,
    figsize: tuple[float, float] | None = None,
    min_examples: int | None = None,
):
    """Plot mean metric by code, annotating each cell with standard deviation."""
    matrix = code_metric_matrix_by_group(
        df,
        columns=columns,
        metric_col=metric_col,
        group_col=group_col,
        group_order=group_order,
        include_overall=True,
        min_examples=min_examples,
    )
    std_matrix = code_metric_std_matrix_by_group(
        df,
        columns=columns,
        metric_col=metric_col,
        group_col=group_col,
        group_order=group_order,
        include_overall=True,
        min_examples=min_examples,
    )
    annotations = _mean_std_annotations(matrix, std_matrix)
    return (*plot_code_heatmap(
        matrix,
        title=title or f"Mean {metric_col} by Deductive Code and {group_col} (with SD)",
        cbar_label=f"Mean {metric_col}",
        cmap="RdBu_r",
        center=0,
        fmt=".1f",
        annotations=annotations,
        figsize=figsize,
    ), matrix, std_matrix)
