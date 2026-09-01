"""
Shared plotting and analysis helpers for Vox Deorum experiments.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import matplotlib


def _show():
    """Display the current figure in notebooks, or call plt.show() interactively."""
    try:
        from IPython.display import display
        display(plt.gcf())
        plt.close()
    except ImportError:
        backend = matplotlib.get_backend()
        if backend and "agg" not in backend.lower():
            plt.show()


def logit(p):
    """Transform probability to log-odds space"""
    # Clip to avoid log(0) or log of negative numbers
    p_clipped = np.clip(p, 1e-5, 1 - 1e-5)
    return np.log(p_clipped / (1 - p_clipped))


def inv_logit(x):
    """Transform log-odds back to probability space"""
    return 1 / (1 + np.exp(-x))


def setup_notebook_display(max_columns=None, max_rows=100, width=120,
                           style='whitegrid', figsize=(12, 6), font_size=11):
    """
    Set up consistent display options and plotting style for notebooks.

    Args:
        max_columns: Maximum number of columns to display (None for all)
        max_rows: Maximum number of rows to display
        width: Display width for pandas
        style: Seaborn style preset
        figsize: Default figure size tuple (width, height)
        font_size: Default font size for plots

    Example:
        from shared.plot_utilities import setup_notebook_display
        setup_notebook_display()
    """
    # Set pandas display options
    pd.set_option('display.max_columns', max_columns)
    pd.set_option('display.max_rows', max_rows)
    pd.set_option('display.width', width)

    # Set plotting style
    sns.set_style(style)
    plt.rcParams['figure.figsize'] = figsize
    plt.rcParams['font.size'] = font_size


# Shared experiment metadata and style config now live under shared/.
def filter_non_llm_games(df, keep_null_ai=False):
    """
    Filter out games where ALL players are Vanilla or Null.

    Works on any DataFrame with a 'condition' or 'experiment' column.
    For notebooks that load all data first, then filter for LLM-specific analysis.
    """
    col = 'condition' if 'condition' in df.columns else 'experiment'
    exclude = VANILLA_EXPERIMENTS if keep_null_ai else NON_LLM_EXPERIMENTS
    return df[~df[col].isin(exclude)]


from shared.experiments import (
    CONDITION_PLAYER_MAPPING as SHARED_CONDITION_PLAYER_MAPPING,
    DEFAULT_EXCLUDED_EXPERIMENTS as SHARED_DEFAULT_EXCLUDED_EXPERIMENTS,
    LLM_EXPERIMENTS as SHARED_LLM_EXPERIMENTS,
    NON_LLM_EXPERIMENTS as SHARED_NON_LLM_EXPERIMENTS,
    NULL_AI_EXPERIMENTS as SHARED_NULL_AI_EXPERIMENTS,
    VANILLA_EXPERIMENTS as SHARED_VANILLA_EXPERIMENTS,
)
from shared.model_catalog import split_player_type as shared_split_player_type
from shared.plot_styles import (
    MODEL_COLORS as SHARED_MODEL_COLORS,
    PROMPT_PATTERNS as SHARED_PROMPT_PATTERNS,
    get_all_player_styles as shared_get_all_player_styles,
    get_player_alpha as shared_get_player_alpha,
    get_player_color as shared_get_player_color,
    get_player_hatch as shared_get_player_hatch,
    get_player_linestyle as shared_get_player_linestyle,
    get_player_marker as shared_get_player_marker,
    sort_player_types as shared_sort_player_types,
)


CONDITION_PLAYER_MAPPING = SHARED_CONDITION_PLAYER_MAPPING
VANILLA_EXPERIMENTS = SHARED_VANILLA_EXPERIMENTS
NULL_AI_EXPERIMENTS = SHARED_NULL_AI_EXPERIMENTS
NON_LLM_EXPERIMENTS = SHARED_NON_LLM_EXPERIMENTS
DEFAULT_EXCLUDED_EXPERIMENTS = SHARED_DEFAULT_EXCLUDED_EXPERIMENTS
LLM_EXPERIMENTS = SHARED_LLM_EXPERIMENTS
MODEL_COLORS = SHARED_MODEL_COLORS
PROMPT_PATTERNS = SHARED_PROMPT_PATTERNS


def sort_player_types(player_types):
    """Sort player types: Null first, Vanilla second, rest alphabetically."""
    pinned = ['Null', 'Vanilla']
    pts = set(player_types)
    return [p for p in pinned if p in pts] + sorted(pts - set(pinned))


def get_player_color(player_type):
    """
    Get the color for a player type based on model.

    Args:
        player_type: Player type string (e.g., 'GPT-OSS-120B-Simple', 'Vanilla')

    Returns:
        Color string (hex format)
    """
    if player_type == 'Vanilla':
        return MODEL_COLORS['Vanilla']

    # Extract model name from player_type
    for model in MODEL_COLORS:
        if model in player_type:
            return MODEL_COLORS[model]

    # Default fallback color
    return '#000000'  # Black


def get_player_hatch(player_type):
    """
    Get the hatch pattern for a player type (for bar charts).

    Args:
        player_type: Player type string (e.g., 'GPT-OSS-120B-Simple', 'Vanilla')

    Returns:
        Hatch pattern string
    """
    if player_type == 'Vanilla':
        return PROMPT_PATTERNS['Vanilla']['hatch']
    elif 'Simple' in player_type:
        return PROMPT_PATTERNS['Simple']['hatch']
    elif 'Briefed' in player_type:
        return PROMPT_PATTERNS['Briefed']['hatch']

    # Default fallback
    return None


def get_player_linestyle(player_type):
    """
    Get the line style for a player type (for time series plots).

    Args:
        player_type: Player type string (e.g., 'GPT-OSS-120B-Simple', 'Vanilla')

    Returns:
        Line style string
    """
    if player_type == 'Vanilla':
        return PROMPT_PATTERNS['Vanilla']['linestyle']
    elif 'Simple' in player_type:
        return PROMPT_PATTERNS['Simple']['linestyle']
    elif 'Briefed' in player_type:
        return PROMPT_PATTERNS['Briefed']['linestyle']

    # Default fallback
    return '-'


def get_player_marker(player_type):
    """
    Get the marker style for a player type (for scatter plots).

    Args:
        player_type: Player type string (e.g., 'GPT-OSS-120B-Simple', 'Vanilla')

    Returns:
        Marker style string
    """
    if player_type == 'Vanilla':
        return PROMPT_PATTERNS['Vanilla']['marker']
    elif 'Simple' in player_type:
        return PROMPT_PATTERNS['Simple']['marker']
    elif 'Briefed' in player_type:
        return PROMPT_PATTERNS['Briefed']['marker']

    # Default fallback
    return 'o'


def get_player_alpha(player_type):
    """
    Get the alpha (transparency) for a player type.

    Args:
        player_type: Player type string (e.g., 'GPT-OSS-120B-Simple', 'Vanilla')

    Returns:
        Alpha value (0-1)
    """
    if player_type == 'Vanilla':
        return PROMPT_PATTERNS['Vanilla']['alpha']
    elif 'Simple' in player_type:
        return PROMPT_PATTERNS['Simple']['alpha']
    elif 'Briefed' in player_type:
        return PROMPT_PATTERNS['Briefed']['alpha']

    # Default fallback
    return 0.8


def get_all_player_styles(player_types):
    """
    Get complete style dictionary for a list of player types.

    Args:
        player_types: List of player type strings

    Returns:
        Dictionary with player_type as key and style dict as value
    """
    styles = {}
    for player_type in player_types:
        styles[player_type] = {
            'color': get_player_color(player_type),
            'hatch': get_player_hatch(player_type),
            'linestyle': get_player_linestyle(player_type),
            'marker': get_player_marker(player_type),
            'alpha': get_player_alpha(player_type)
        }
    return styles


sort_player_types = shared_sort_player_types
get_player_color = shared_get_player_color
get_player_hatch = shared_get_player_hatch
get_player_linestyle = shared_get_player_linestyle
get_player_marker = shared_get_player_marker
get_player_alpha = shared_get_player_alpha
get_all_player_styles = shared_get_all_player_styles


def bootstrap_ci(data, y, x='player_type', statistic='median',
                 n_bootstrap=5000, ci_level=0.95):
    """Compute bootstrapped CI for a statistic, grouped by *x*.

    Parameters
    ----------
    data : DataFrame
        Source data (rows with NaN in *y* or *x* are dropped).
    y : str
        Continuous column to summarise.
    x : str
        Grouping column (default ``'player_type'``).
    statistic : ``'median'`` | ``'mean'``
        Central-tendency measure to bootstrap.
    n_bootstrap : int
        Number of bootstrap resamples (default 5000).
    ci_level : float
        Confidence level (default 0.95 → 95 % CI).

    Returns
    -------
    DataFrame
        Columns: ``Name``, ``Effect``, ``CI_Low``, ``CI_High``, ``N``, ``Sig``.
        Compatible with :func:`plot_forest_plot` (``use_prob_scale=False``).
    """
    clean = data.dropna(subset=[y, x])
    stat_fn = np.median if statistic == 'median' else np.mean

    if x == 'player_type':
        categories = sort_player_types(clean[x].unique())
    else:
        categories = sorted(clean[x].unique())

    rng = np.random.default_rng(42)
    alpha = (1 - ci_level) / 2
    rows = []
    for cat in categories:
        values = clean.loc[clean[x] == cat, y].values
        n = len(values)
        point = float(stat_fn(values))
        if n > 1:
            boot = rng.choice(values, size=(n_bootstrap, n), replace=True)
            boot_stats = stat_fn(boot, axis=1)
            ci_lo = float(np.percentile(boot_stats, alpha * 100))
            ci_hi = float(np.percentile(boot_stats, (1 - alpha) * 100))
        else:
            ci_lo = ci_hi = point
        rows.append(dict(Name=cat, Effect=point, CI_Low=ci_lo, CI_High=ci_hi,
                         N=n, Sig=''))
    return pd.DataFrame(rows)


# =====================================================
# STRATEGY & WIN PROBABILITY UTILITIES
# =====================================================

# Maps internal grand_strategy names to display names used in analysis
STRATEGY_DISPLAY_NAMES = {
    'Conquest': 'Domination',
    'Spaceship': 'Science',
    'UnitedNations': 'Diplomatic',
    'Culture': 'Culture',
}


def forward_fill_strategy(df):
    """
    Forward-fill grand_strategy per (game_id, player_id) and map to display names.

    Adds a 'strategy_filled' column. Empty strings are treated as missing.
    The original 'grand_strategy' column is not modified.

    Args:
        df: DataFrame with columns game_id, player_id, grand_strategy.
            Must be sorted by (game_id, player_id, turn).

    Returns:
        The same DataFrame with 'strategy_filled' added in-place.
    """
    df['grand_strategy'] = df['grand_strategy'].replace('', np.nan)
    df['strategy_filled'] = (
        df.groupby(['game_id', 'player_id'])['grand_strategy']
        .transform(lambda x: x.ffill())
    )
    df['strategy_filled'] = df['strategy_filled'].map(STRATEGY_DISPLAY_NAMES)
    return df


def compute_post_pivot_win_prob(pivot_df, turn_df, window=50):
    """
    Compute post-event weighted average win probability using linear decay.

    For each row in *pivot_df*, looks ahead up to *window* turns in *turn_df*
    and returns a linearly-decayed weighted average of predicted_win_probability
    (closer turns weighted more).

    Args:
        pivot_df: DataFrame of event rows; must have game_id, player_id, turn.
        turn_df: Full turn-level DataFrame with predicted_win_probability.
        window:  Number of future turns to consider (default 50).

    Returns:
        pandas Series aligned to pivot_df.index with the weighted average
        post-event win probability (NaN where no future data exists).
    """
    _wp = turn_df.dropna(subset=['predicted_win_probability'])
    # Pre-build per-player Series indexed by turn for fast slicing
    wp_lookup = {
        key: grp.set_index('turn')['predicted_win_probability'].sort_index()
        for key, grp in _wp.groupby(['game_id', 'player_id'])
    }
    max_weights = np.arange(window, 0, -1, dtype=float)
    results = pd.Series(np.nan, index=pivot_df.index, name='after_prob')
    # Batch events by player to reuse Series lookup
    for (gid, pid), event_idx in pivot_df.groupby(
        ['game_id', 'player_id']
    ).groups.items():
        series = wp_lookup.get((gid, pid))
        if series is None:
            continue
        for idx in event_idx:
            t = int(pivot_df.loc[idx, 'turn'])
            future = series.loc[t + 1:t + window]
            if len(future):
                w = max_weights[:len(future)]
                results.loc[idx] = np.average(future.values, weights=w)
    return results


def detect_strategy_pivots(df, min_turn=20):
    """
    Detect turns where grand strategy changes from one victory type to another.

    Requires ``forward_fill_strategy()`` to have been called first (i.e. the
    DataFrame must already have a ``strategy_filled`` column).

    Adds ``prev_strategy`` and ``is_pivot`` columns to *df* **in-place**, then
    returns a **copy** of only the pivot rows.

    Args:
        df: DataFrame with columns game_id, player_id, strategy_filled.
        min_turn: Minimum turn number for a pivot to be included (default 20).
            Pivots before this turn are excluded as early-game noise.

    Returns:
        DataFrame (copy) of rows where strategy changed, with ``prev_strategy``
        populated.
    """
    df['prev_strategy'] = (
        df.groupby(['game_id', 'player_id'])['strategy_filled'].shift(1)
    )
    df['is_pivot'] = (
        (df['strategy_filled'] != df['prev_strategy'])
        & df['strategy_filled'].notna()
        & df['prev_strategy'].notna()
        & (df['prev_strategy'] != '')
        & (df['turn'] >= min_turn)
    )
    return df[df['is_pivot']].copy()


def compute_flavor_deltas(pivots, df, flavor_cols=None):
    """
    Compute per-flavor deltas (current minus previous turn) for pivot rows.

    Adds ``{flavor}_prev``, ``{flavor}_delta``, and ``n_flavors_changed``
    columns to *pivots* **in-place**.

    Args:
        pivots: DataFrame of pivot rows (subset of *df*).
        df: Full turn-level DataFrame, sorted by (game_id, player_id, turn).
        flavor_cols: List of flavor column names. If None, auto-detected from
            columns starting with ``flavor_``.

    Returns:
        List of flavor column names used (convenience for downstream code).
    """
    if flavor_cols is None:
        flavor_cols = [c for c in df.columns if c.startswith('flavor_')]
    prev_flavors = df.groupby(['game_id', 'player_id'])[flavor_cols].shift(1)
    delta_cols = [f'{c}_delta' for c in flavor_cols]
    for col in flavor_cols:
        pivots[f'{col}_prev'] = prev_flavors.loc[pivots.index, col]
        cur = pd.to_numeric(pivots[col], errors='coerce')
        prev = pd.to_numeric(pivots[f'{col}_prev'], errors='coerce')
        pivots[f'{col}_delta'] = cur - prev
    pivots['n_flavors_changed'] = (pivots[delta_cols].abs() > 0).sum(axis=1)
    return flavor_cols


def detect_all_flavor_changes(df, flavor_cols=None):
    """
    Detect all turns where any flavor value changed from the previous turn.

    Unlike :func:`detect_strategy_pivots` (which only finds grand-strategy
    changes), this captures **every** flavor adjustment regardless of whether
    the high-level strategy changed.

    Adds ``{flavor}_prev``, ``{flavor}_delta``, and ``n_flavors_changed``
    columns to the returned DataFrame.

    Args:
        df: Full turn-level DataFrame, **sorted** by
            (game_id, player_id, turn).
        flavor_cols: List of flavor column names.  If *None*, auto-detected
            from columns starting with ``flavor_``.

    Returns:
        (changes, flavor_cols) tuple where *changes* is a **copy** containing
        only rows with at least one nonzero flavor delta.
    """
    if flavor_cols is None:
        flavor_cols = [c for c in df.columns if c.startswith('flavor_')]
    prev_flavors = df.groupby(['game_id', 'player_id'])[flavor_cols].shift(1)
    delta_cols = []
    for col in flavor_cols:
        prev_col = f'{col}_prev'
        delta_col = f'{col}_delta'
        df[prev_col] = prev_flavors[col]
        cur = pd.to_numeric(df[col], errors='coerce')
        prev = pd.to_numeric(df[prev_col], errors='coerce')
        df[delta_col] = cur - prev
        delta_cols.append(delta_col)
    df['n_flavors_changed'] = (df[delta_cols].abs() > 0).sum(axis=1)
    changes = df[df['n_flavors_changed'] > 0].copy()
    # Clean up columns added to the original df
    df.drop(columns=[f'{c}_prev' for c in flavor_cols]
            + [f'{c}_delta' for c in flavor_cols]
            + ['n_flavors_changed'], inplace=True)
    return changes, flavor_cols


def compute_pivot_impact(pivots, df, panel_csv='../panel_data.csv', window=50):
    """
    Enrich pivot rows with win-probability impact and game-level metadata.

    Adds ``before_prob``, ``after_prob``, ``win_prob_delta``, ``final_win_prob``,
    ``victory_type``, and ``victory_turn`` columns.  Drops rows where
    ``win_prob_delta`` is NaN.

    Args:
        pivots: DataFrame of pivot rows with ``predicted_win_probability``.
        df: Full turn-level DataFrame with ``predicted_win_probability``.
        panel_csv: Path to panel_data.csv for game-level metadata.
        window: Number of future turns for post-pivot win-prob averaging.

    Returns:
        Filtered copy of *pivots* with impact columns added.
    """
    pivots['before_prob'] = pivots['predicted_win_probability']
    pivots['after_prob'] = compute_post_pivot_win_prob(pivots, df, window=window)
    pivots['win_prob_delta'] = pivots['after_prob'] - pivots['before_prob']

    # Final win probability from last observed turn per player
    final_probs = (
        df.groupby(['game_id', 'player_id'])['predicted_win_probability']
        .last()
        .rename('final_win_prob')
    )
    pivots = pivots.join(final_probs, on=['game_id', 'player_id'])

    # Victory type and turn from panel data
    panel = pd.read_csv(
        panel_csv,
        usecols=['game_id', 'victory_type', 'turn'],
    ).drop_duplicates('game_id').rename(columns={'turn': 'victory_turn'})
    pivots = pivots.merge(panel, on='game_id', how='left')

    pivots = pivots.dropna(subset=['win_prob_delta']).copy()
    return pivots


def classify_pivots(pivots, threshold=0.05):
    """
    Classify pivots by effectiveness using a fixed win-prob-delta threshold.

    Adds an ``impact_class`` column with values ``very_effective``,
    ``very_ineffective``, or ``neutral``.

    Args:
        pivots: DataFrame with ``win_prob_delta`` column.
        threshold: Absolute delta threshold (default 0.05).

    Returns:
        The same DataFrame (modified in-place).
    """
    pivots['impact_class'] = 'neutral'
    pivots.loc[pivots['win_prob_delta'] >= threshold, 'impact_class'] = 'very_effective'
    pivots.loc[pivots['win_prob_delta'] <= -threshold, 'impact_class'] = 'very_ineffective'
    return pivots


def export_pivot_markdown(extreme, output_dir, flavor_cols, n_top_flavors=8):
    """
    Write per-model markdown files summarising extreme pivots.

    Each entry shows civilization, turn, strategy change, win-probability
    impact, top flavor changes (by absolute delta), and LLM rationale.

    Args:
        extreme: DataFrame of extreme pivots (very_effective + very_ineffective).
        output_dir: Directory to write markdown files into.
        flavor_cols: List of flavor column names (used to derive delta column names).
        n_top_flavors: Number of top flavor changes to display per pivot.
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    delta_cols = [f'{c}_delta' for c in flavor_cols]

    for model, grp in extreme.groupby('player_type'):
        eff = grp[grp['impact_class'] == 'very_effective'].sort_values('win_prob_delta', ascending=False)
        ineff = grp[grp['impact_class'] == 'very_ineffective'].sort_values('win_prob_delta')

        lines = [f'# {model} — Extreme Strategy Pivots\n\n']
        lines.append(f'Very effective: {len(eff)} · Very ineffective: {len(ineff)}\n\n')

        for label, section_df in [('Very Effective', eff), ('Very Ineffective', ineff)]:
            lines.append(f'## {label}\n\n')
            for _, row in section_df.iterrows():
                rationale = str(row.get('rationale', '')).replace('\n', ' ').strip()
                outcome = 'Won' if row.get('is_winner') == 1 else 'Lost'
                final_p = row.get('final_win_prob', float('nan'))
                vtype = row.get('victory_type', 'N/A')
                vturn = int(row['victory_turn']) if pd.notna(row.get('victory_turn')) else 'N/A'

                lines.append(
                    f'**{row["civilization"]}** · Turn {int(row["turn"])} · '
                    f'{row["prev_strategy"]} \u2192 {row["strategy_filled"]} · '
                    f'Win prob: {row["before_prob"]:.3f} \u2192 {row["after_prob"]:.3f} '
                    f'(**{row["win_prob_delta"]:+.3f}**) · '
                    f'{outcome} (final: {final_p:.3f}) · {vtype} victory turn {vturn}\n\n'
                )

                # Top flavor changes by absolute delta
                deltas = pd.to_numeric(row[delta_cols], errors='coerce').dropna()
                top = deltas.abs().nlargest(n_top_flavors)
                if len(top) > 0:
                    parts = []
                    for dc in top.index:
                        name = dc.replace('flavor_', '').replace('_delta', '')
                        parts.append(f'{name}: {deltas[dc]:+.0f}')
                    lines.append(f'Flavors: {", ".join(parts)}\n\n')

                if rationale:
                    lines.append(f'> {rationale}\n\n')

        slug = model.replace(' ', '_')
        out_path = f'{output_dir}/{slug}.md'
        with open(out_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print(f'Written: {out_path}')


def export_pivot_csv(extreme, output_path, flavor_cols):
    """
    Export extreme pivots to CSV with structured columns (no text summaries).

    Args:
        extreme: DataFrame of extreme pivots.
        output_path: Path for the output CSV file.
        flavor_cols: List of flavor column names.
    """
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    delta_cols = [f'{c}_delta' for c in flavor_cols]
    export_cols = [
        'game_id', 'player_id', 'turn', 'player_type', 'civilization',
        'prev_strategy', 'strategy_filled', 'impact_class',
        'before_prob', 'after_prob', 'win_prob_delta',
        'is_winner', 'final_win_prob', 'victory_type', 'victory_turn',
        'n_flavors_changed', 'rationale',
    ] + flavor_cols + delta_cols
    # Only include columns that exist
    export_cols = [c for c in export_cols if c in extreme.columns]
    extreme.sort_values(['impact_class', 'win_prob_delta'])[export_cols].to_csv(
        output_path, index=False
    )
    print(f'Written: {output_path}  ({len(extreme)} rows)')


# =====================================================
# COMMON DATA LOADING UTILITIES
# =====================================================

def _load_csv_with_condition_mapping(csv_path):
    """
    Load CSV and add condition column from experiment column.

    Args:
        csv_path: Path to the CSV file

    Returns:
        DataFrame with 'condition' column added
    """
    df = pd.read_csv(csv_path)

    # The 'experiment' column is our condition
    if 'experiment' in df.columns:
        df['condition'] = df['experiment']

    return df


def _apply_player_type_mapping(df, skip_mapping=False):
    """
    Apply player type mapping based on condition and player_id.
    Uses vectorized operations for better performance.

    Args:
        df: DataFrame with 'condition' and 'player_id' columns
        skip_mapping: If True, force player_type to 'Player {player_id}' for all rows

    Returns:
        DataFrame with 'player_type' column added
    """
    if skip_mapping:
        df = df.copy()
        df['player_type'] = 'Player ' + df['player_id'].astype(str)
        return df

    # Create a mapping DataFrame from CONDITION_PLAYER_MAPPING
    mapping_rows = []
    for condition, player_types in CONDITION_PLAYER_MAPPING.items():
        for player_id, player_type in enumerate(player_types):
            mapping_rows.append({
                'condition': condition,
                'player_id': player_id,
                'player_type': player_type
            })

    mapping_df = pd.DataFrame(mapping_rows)

    # Merge with the original DataFrame
    df_with_types = df.merge(
        mapping_df,
        on=['condition', 'player_id'],
        how='left'
    )

    # Fill any missing values with fallback
    df_with_types['player_type'] = df_with_types['player_type'].fillna(
        'Player ' + df_with_types['player_id'].astype(str)
    )

    return df_with_types


def _apply_data_filters(df, player_id=None, version_filter=None,
                        condition_exclude=None, condition_include=None,
                        turn_filter=None, min_turn=None, max_turn=None,
                        exclude_non_llm=False):
    """
    Apply various filters to the dataframe.

    Args:
        df: DataFrame to filter
        player_id: Player ID to filter for (optional)
        version_filter: Version number to filter for (optional)
        condition_exclude: Condition/experiment name(s) to exclude (string or list of strings) (optional)
        condition_include: Condition/experiment name(s) to include exclusively (string or list of strings) (optional)
        turn_filter: Specific turn to filter for (optional)
        min_turn: Minimum turn to include (optional)
        max_turn: Maximum turn to include (optional)
        exclude_non_llm: If True, exclude non-LLM experiments (optional)

    Returns:
        Filtered DataFrame
    """
    cond_col = 'condition' if 'condition' in df.columns else 'experiment'

    # Apply version filter
    if version_filter is not None and 'version' in df.columns:
        df = df[df['version'] == version_filter]

    # Apply default exclusions (always applied at load time)
    if DEFAULT_EXCLUDED_EXPERIMENTS:
        df = df[~df[cond_col].isin(DEFAULT_EXCLUDED_EXPERIMENTS)]

    # Apply non-LLM exclusion (from centralized list)
    if exclude_non_llm:
        df = df[~df[cond_col].isin(NON_LLM_EXPERIMENTS)]

    # Apply condition exclusion filter
    if condition_exclude is not None:
        if isinstance(condition_exclude, (list, tuple)):
            df = df[~df[cond_col].isin(condition_exclude)]
        else:
            df = df[df[cond_col] != condition_exclude]

    # Apply condition inclusion filter
    if condition_include is not None:
        if isinstance(condition_include, (list, tuple)):
            df = df[df[cond_col].isin(condition_include)]
        else:
            df = df[df[cond_col] == condition_include]

    # Apply player ID filter
    if player_id is not None:
        df = df[df['player_id'] == player_id]

    # Apply turn filters (for turn data)
    if 'turn' in df.columns:
        if turn_filter is not None:
            df = df[df['turn'] == turn_filter]
        if min_turn is not None:
            df = df[df['turn'] >= min_turn]
        if max_turn is not None:
            df = df[df['turn'] <= max_turn]

    return df


def _print_data_summary(df, data_type='panel', filters_info=None):
    """
    Print summary statistics for loaded data.

    Args:
        df: DataFrame with loaded data
        data_type: Type of data ('panel' or 'turn')
        filters_info: Dictionary with filter information
    """
    print(f"✓ Loaded {data_type} data: {len(df)} rows")

    # Print filter information
    if filters_info:
        filters_applied = []
        for key, value in filters_info.items():
            if value is not None:
                filters_applied.append(f"{key}={value}")

        if filters_applied:
            print(f"✓ Filters applied: {', '.join(filters_applied)}")

    # Print unique values for key columns
    if 'condition' in df.columns:
        unique_conditions = df['condition'].nunique()
        print(f"✓ Unique conditions: {unique_conditions}")

    if 'player_type' in df.columns:
        unique_player_types = df['player_type'].nunique()
        print(f"✓ Unique player types: {unique_player_types}")

    if data_type == 'turn' and 'turn' in df.columns:
        print(f"✓ Turn range: {df['turn'].min()} - {df['turn'].max()}")

    if data_type == 'turn' and 'civilization' in df.columns:
        unique_civs = df['civilization'].nunique()
        print(f"✓ Unique civilizations: {unique_civs}")

    # Show player type distribution
    if 'player_type' in df.columns:
        print(f"\nPlayer Type Distribution:")
        player_type_counts = df.groupby('player_type').size().sort_values(ascending=False)
        for player_type, count in player_type_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {player_type}: {count} rows ({percentage:.1f}%)")

    # Show conditions if multiple
    if 'condition' in df.columns and df['condition'].nunique() > 1:
        print(f"\nCondition Distribution:")
        condition_counts = df.groupby('condition').size().sort_values(ascending=False)
        for condition, count in condition_counts.items():
            percentage = (count / len(df)) * 100
            print(f"  {condition}: {count} rows ({percentage:.1f}%)")

    # Additional info for turn data
    if data_type == 'turn':
        if 'game_id' in df.columns:
            unique_games = df['game_id'].nunique()
            print(f"\n✓ Unique games: {unique_games}")

        if 'civilization' in df.columns:
            print(f"\nCivilization Distribution:")
            civ_counts = df.groupby('civilization').size().sort_values(ascending=False).head(10)
            for civ, count in civ_counts.items():
                percentage = (count / len(df)) * 100
                print(f"  {civ}: {count} rows ({percentage:.1f}%)")


# Note: _fill_eliminated_players function has been removed.
# Eliminated players are now filled during SQL extraction in extract_turns.py
# This significantly improves performance by avoiding post-processing of large datasets.


def load_turn_data(csv_path='turn_data.csv', player_id=None, version_filter=None,
                   condition_exclude=None, turn_filter=None, min_turn=None,
                   max_turn=None, print_metadata=True, exclude_non_llm=False,
                   skip_mapping=False):
    """
    Load and prepare turn-by-turn data with player type mapping.

    Note: Eliminated players are now filled during SQL extraction, so all player-turn
    combinations are included in the data with zeros for eliminated players.

    Args:
        csv_path: Path to the turn data CSV file (default: 'turn_data.csv')
        player_id: Player ID to filter for. Set to None to include all players (default: None)
        version_filter: Optional version number to filter for
        condition_exclude: Optional condition/experiment name(s) to exclude (string or list of strings)
        turn_filter: Optional specific turn to filter for
        min_turn: Optional minimum turn to include
        max_turn: Optional maximum turn to include
        print_metadata: If True, prints summary information about loaded data (default: True)
        exclude_non_llm: If True, exclude experiments with only Vanilla/Null players (default: False)
        skip_mapping: If True, force player_type to 'Player {player_id}' for all rows (default: False)

    Returns:
        DataFrame with turn data including 'condition' and 'player_type' columns

    Example:
        # Load all turn data
        df = load_turn_data()

        # Load data for specific player
        df = load_turn_data(player_id=0)

        # Filter by turn range
        df = load_turn_data(min_turn=100, max_turn=200)

        # Filter by specific turn
        df = load_turn_data(turn_filter=150)

        # Combine filters
        df = load_turn_data(player_id=2, condition_exclude='2026-arena-glm', min_turn=50)
    """
    # Load the data with condition mapping
    df = _load_csv_with_condition_mapping(csv_path)

    # Apply player type mapping
    df = _apply_player_type_mapping(df, skip_mapping=skip_mapping)

    # Note: Eliminated players are now filled during SQL extraction in extract_turns.py
    # No need for post-processing here

    # Apply filters
    df = _apply_data_filters(df, player_id=player_id,
                             version_filter=version_filter,
                             condition_exclude=condition_exclude,
                             turn_filter=turn_filter,
                             min_turn=min_turn,
                             max_turn=max_turn,
                             exclude_non_llm=exclude_non_llm)

    # Create turn_progress variable
    df['turn_progress'] = round(df['turn'] / df['max_turn'], 2)

    # Print metadata if requested
    if print_metadata:
        filters_info = {
            'player_id': player_id,
            'version': version_filter,
            'condition_exclude': condition_exclude,
            'exclude_non_llm': exclude_non_llm if exclude_non_llm else None,
            'turn': turn_filter,
            'min_turn': min_turn,
            'max_turn': max_turn
        }
        _print_data_summary(df, data_type='turn', filters_info=filters_info)

    return df


def load_panel_data(csv_path='panel_data.csv', player_id=None, version_filter=None,
                    condition_exclude=None, condition_include=None,
                    print_metadata=True, exclude_non_llm=False, skip_mapping=False):
    """
    Load and prepare panel data with player type mapping.

    Args:
        csv_path: Path to the panel data CSV file (default: 'panel_data.csv')
        player_id: Player ID to filter for. Set to None to include all players (default: None)
        version_filter: Optional version number to filter for (e.g., 13)
        condition_exclude: Optional condition/experiment name(s) to exclude (string or list of strings) (e.g., '2026-arena-oss')
        condition_include: Optional condition/experiment name(s) to include exclusively (string or list of strings)
        print_metadata: If True, prints summary information about loaded data (default: True)
        exclude_non_llm: If True, exclude experiments with only Vanilla/Null players (default: False)
        skip_mapping: If True, skip condition and player type mapping (default: False)

    Returns:
        DataFrame with panel data including 'condition' and 'player_type' columns

    Example:
        # Load all data
        df = load_panel_data()

        # Load data for specific player
        df = load_panel_data(player_id=0)

        # Exclude a condition
        df = load_panel_data(condition_exclude='observe-vanilla-standard')

        # Include only specific conditions
        df = load_panel_data(condition_include=['2026-arena-oss', '2026-arena-glm'])

        # Exclude all non-LLM experiments
        df = load_panel_data(exclude_non_llm=True)

        # Combine filters
        df = load_panel_data(player_id=2, condition_exclude='2026-arena-glm')
    """
    df = _load_csv_with_condition_mapping(csv_path)

    # Apply player type mapping
    df = _apply_player_type_mapping(df, skip_mapping=skip_mapping)

    # Apply filters
    df = _apply_data_filters(df, player_id=player_id,
                             version_filter=version_filter,
                             condition_exclude=condition_exclude,
                             condition_include=condition_include,
                             exclude_non_llm=exclude_non_llm)

    # Print metadata if requested
    if print_metadata:
        filters_info = {
            'player_id': player_id,
            'version': version_filter,
            'condition_exclude': condition_exclude,
            'condition_include': condition_include,
            'exclude_non_llm': exclude_non_llm if exclude_non_llm else None
        }
        _print_data_summary(df, data_type='panel', filters_info=filters_info)

    return df


def add_value_labels_on_bars(ax, bars, format_str='{:.1f}', suffix=''):
    """
    Add value labels on top of bars.

    Args:
        ax: Matplotlib axis object
        bars: Bar objects to label
        format_str: Format string for values
        suffix: Suffix to append to labels
    """
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            label = format_str.format(height) + suffix
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   label, ha='center', va='bottom', fontsize=9)


def calculate_percentages(df_grouped, group_column='player_type'):
    """
    Calculate percentages within each group.

    Args:
        df_grouped: Grouped DataFrame with 'count' column
        group_column: Column name for grouping (default: 'player_type')

    Returns:
        DataFrame with added 'percentage' column
    """
    for group in df_grouped[group_column].unique():
        mask = df_grouped[group_column] == group
        total = df_grouped.loc[mask, 'count'].sum()
        df_grouped.loc[mask, 'percentage'] = (df_grouped.loc[mask, 'count'] / total * 100)
    return df_grouped


def print_statistics(data, name, indent="  "):
    """
    Print summary statistics for a data series.

    Args:
        data: Data series to summarize
        name: Name of the data
        indent: Indentation string
    """
    if len(data) > 0:
        print(f"{indent}{name}:")
        print(f"{indent}  Mean: {data.mean():.2f}")
        print(f"{indent}  Median: {data.median():.2f}")
        print(f"{indent}  Std: {data.std():.2f}")
        print(f"{indent}  Min: {data.min():.0f}")
        print(f"{indent}  Max: {data.max():.0f}")
        print(f"{indent}  Count: {len(data)}")
    else:
        print(f"{indent}{name}: No data")


def plot_bar_chart(df_data, category_col, value_col=None,
                   xlabel=None, ylabel=None, title=None,
                   use_percentage=True, show_error_bars=True,
                   value_format='{:.1f}', x_labels=None,
                   rotation=45, confidence_level=0.95,
                   print_summary=True,
                   colormap='viridis', figsize=(10, 6),
                   target_value=None, color_by_category=False):
    """
    Create a simple bar chart from DataFrame with color scale.

    Args:
        df_data: DataFrame with the data
        category_col: Column name for x-axis categories
        value_col: Column name for values to plot. For percentage mode, this is the column
                  to calculate percentages for (counts value_col==1 by default)
        xlabel, ylabel, title: Chart labels (auto-generated if None)
        use_percentage: If True, calculate percentage of value_col==1 within each category
        show_error_bars: Whether to show confidence interval error bars
        value_format: Format string for value labels
        x_labels: Optional custom labels for x-axis
        rotation: Rotation angle for x-axis labels (default 45 degrees)
        confidence_level: Confidence level for error bars (default 0.95)
        print_summary: Whether to print summary statistics
        colormap: Matplotlib colormap name for color scale (default 'viridis')
        figsize: Figure size tuple
        target_value: For percentage mode, the specific value to show percentage of
                     (default is 1 when use_percentage=True)
        color_by_category: If True, color bars by category (player_type/model) using MODEL_COLORS
                          and apply hatch patterns using get_player_hatch() instead of coloring by value.
                          No colorbar will be shown in this mode.

    Returns:
        DataFrame with aggregated data
    """
    import matplotlib.cm as cm
    import matplotlib.colors as mcolors

    fig, ax = plt.subplots(figsize=figsize)

    if use_percentage:
        if value_col is None:
            # If no value_col specified, just count categories (legacy behavior)
            value_counts = df_data[category_col].value_counts().sort_index()
            if category_col == 'player_type':
                value_counts = value_counts.loc[sort_player_types(value_counts.index)]
            total = len(df_data)
            categories = value_counts.index.tolist()
            values = (value_counts / total * 100).values
            counts = value_counts.values
            totals = [total] * len(categories)
            actual_target = "category occurrence"

        else:
            # Calculate percentage of value_col within each category
            categories = sort_player_types(df_data[category_col].unique()) if category_col == 'player_type' else sorted(df_data[category_col].unique())
            values = []
            counts = []
            totals = []

            # When use_percentage=True, count value_col == 1
            if target_value is None:
                target_value = 1

            actual_target = target_value

            # Calculate percentages for each category
            for cat in categories:
                cat_data = df_data[df_data[category_col] == cat]
                cat_total = len(cat_data)
                if cat_total > 0:
                    target_count = (cat_data[value_col] == target_value).sum()
                    percentage = (target_count / cat_total) * 100
                    values.append(percentage)
                    counts.append(target_count)
                    totals.append(cat_total)
                else:
                    values.append(0)
                    counts.append(0)
                    totals.append(0)

        suffix = '%'

        # Calculate error bars for binomial proportions
        if show_error_bars:
            z_score = stats.norm.ppf((1 + confidence_level) / 2)
            errors = []
            for val, total in zip(values, totals):
                if total > 0:
                    p = val / 100
                    se = np.sqrt(p * (1 - p) / total)
                    ci = z_score * se * 100
                    errors.append(ci)
                else:
                    errors.append(0)
        else:
            errors = None

        # Create aggregated DataFrame
        aggregated = pd.DataFrame({
            category_col: categories,
            'count': counts,
            'total': totals,
            'percentage': values
        })
        if value_col:
            aggregated['target_value'] = actual_target

    else:
        # Calculate mean and std for continuous data
        if value_col is None:
            raise ValueError("value_col must be specified when use_percentage=False")

        aggregated = df_data.groupby(category_col)[value_col].agg(['mean', 'std', 'count']).reset_index()
        if category_col == 'player_type':
            sort_order = sort_player_types(aggregated[category_col])
            aggregated = aggregated.set_index(category_col).loc[sort_order].reset_index()
        categories = aggregated[category_col].tolist()
        values = aggregated['mean'].values
        suffix = ''

        # Calculate error bars for means
        if show_error_bars:
            z_score = stats.norm.ppf((1 + confidence_level) / 2)
            errors = []
            for _, row in aggregated.iterrows():
                if row['count'] > 1 and not pd.isna(row['std']):
                    se = row['std'] / np.sqrt(row['count'])
                    ci = z_score * se
                    errors.append(ci)
                else:
                    errors.append(0)
        else:
            errors = None

    # Create color map based on values or categories
    if color_by_category:
        # Color by category (player_type/model) using MODEL_COLORS and hatch patterns
        colors = [get_player_color(str(cat)) for cat in categories]
        hatches = [get_player_hatch(str(cat)) for cat in categories]
        norm = None
        cmap = None
    else:
        # Color by values using colormap
        if len(values) > 0 and max(values) > min(values):
            norm = mcolors.Normalize(vmin=min(values), vmax=max(values))
            cmap = cm.get_cmap(colormap)
            colors = [cmap(norm(val)) for val in values]
        else:
            # All values are the same, use single color
            colors = [cm.get_cmap(colormap)(0.5)] * len(values)
            norm = None
            cmap = None
        hatches = [None] * len(values)

    # Create bar chart with color scale
    x = np.arange(len(categories))
    bars = ax.bar(x, values, color=colors, alpha=0.9, edgecolor='black', linewidth=0.5,
                  yerr=errors, capsize=5 if show_error_bars else 0)

    # Apply hatch patterns if using category-based coloring
    if color_by_category:
        for bar, hatch in zip(bars, hatches):
            if hatch:
                bar.set_hatch(hatch)

    # Add value labels on bars
    for bar, val in zip(bars, values):
        height = bar.get_height()
        if height > 0:
            label = value_format.format(val) + suffix
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   label, ha='center', va='bottom', fontsize=9)

    # Set labels and formatting
    if xlabel is None:
        xlabel = category_col.replace('_', ' ').title()
    if ylabel is None:
        if use_percentage:
            ylabel = f'Percentage (%)' if not value_col else f'Percentage with {value_col}={actual_target} (%)'
        else:
            ylabel = value_col.replace('_', ' ').title() if value_col else 'Value'
    if title is None:
        if use_percentage and value_col:
            title = f'{value_col}={actual_target} by {category_col}'
        else:
            title = f'{ylabel} by {xlabel}'

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    if show_error_bars:
        ax.set_title(f'{title} ({int(confidence_level*100)}% CI)', fontsize=14, fontweight='bold')
    else:
        ax.set_title(title, fontsize=14, fontweight='bold')

    ax.set_xticks(x)
    if x_labels:
        ax.set_xticklabels(x_labels, rotation=rotation, ha='right' if rotation else 'center')
    else:
        ax.set_xticklabels(categories, rotation=rotation, ha='right' if rotation else 'center')

    ax.grid(axis='y', alpha=0.3)

    # Add colorbar if there's a meaningful range (only for value-based coloring)
    if not color_by_category and len(values) > 1 and max(values) > min(values) and norm is not None and cmap is not None:
        sm = cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])
        cbar = plt.colorbar(sm, ax=ax, pad=0.02, fraction=0.046)
        cbar.set_label(ylabel, fontsize=10)

    plt.tight_layout()
    _show()

    # Print summary if requested
    if print_summary:
        from IPython.display import display

        if use_percentage:
            summary_df = aggregated[[category_col, 'count', 'total', 'percentage']].copy()
            summary_df['summary'] = summary_df['count'].astype(str) + '/' + summary_df['total'].astype(str) + ' (' + summary_df['percentage'].round(1).astype(str) + '%)'
            summary_df = summary_df[[category_col, 'summary']].set_index(category_col)
            summary_df.index.name = None
            summary_df.columns = [f'{value_col}={actual_target}' if value_col else 'Count (%)']
            display(summary_df)
        else:
            summary_df = aggregated.copy()
            summary_df = summary_df.rename(columns={'mean': 'Mean', 'std': 'Std', 'count': 'N'})
            summary_df = summary_df.set_index(category_col)
            summary_df.index.name = None
            display(summary_df)

    return None  # Suppress Jupyter auto-display


def plot_grouped_bar_chart(df_data, value_col, category_col,
                           xlabel, ylabel, title,
                           use_percentage=True, show_error_bars=True,
                           value_format='{:.1f}', x_labels=None,
                           rotation=0, confidence_level=0.95,
                           print_summary=True):
    """
    Create grouped bar chart from DataFrame, display it, and print statistics.
    Groups are automatically determined by unique player_type values.

    Args:
        df_data: DataFrame with the data (must contain 'player_type' column)
        value_col: Column name for values to plot
        category_col: Column name for x-axis categories
        xlabel, ylabel, title: Chart labels
        use_percentage: If True, calculate and show percentages
        show_error_bars: Whether to show error bars
        value_format: Format string for value labels
        x_labels: Optional custom labels for x-axis
        rotation: Rotation angle for x-axis labels
        confidence_level: Confidence level for error bars (default 0.95 for 95% CI)
        print_summary: Whether to print summary statistics

    Returns:
        Grouped DataFrame
    """
    group_col = 'player_type'  # Always use player_type for grouping

    fig, ax = plt.subplots(figsize=(12, 6))

    # Group and count
    if use_percentage:
        grouped = df_data.groupby([group_col, category_col]).size().reset_index(name='count')
        grouped = calculate_percentages(grouped, group_col)
        value_to_plot = 'percentage'
        suffix = '%'
    else:
        # For continuous data, we need mean, std, and count for error bars
        grouped_agg = df_data.groupby([group_col, category_col])[value_col].agg(['mean', 'std', 'count']).reset_index()
        grouped_agg.columns = [group_col, category_col, value_col, f'{value_col}_std', f'{value_col}_count']
        grouped = grouped_agg
        value_to_plot = value_col
        suffix = ''

    # Get unique player types and categories
    player_types = sort_player_types(df_data[group_col].unique())
    categories = sorted(df_data[category_col].unique())

    # Prepare data dictionaries
    data_dict = {}
    sample_sizes = {}
    std_dict = {}  # Store standard deviations for continuous data
    count_dict = {}  # Store counts for continuous data

    for player_type in player_types:
        player_data = grouped[grouped[group_col] == player_type]

        # Ensure all categories are present
        values = []
        std_devs = []
        counts = []

        for cat in categories:
            cat_data = player_data[player_data[category_col] == cat]
            if len(cat_data) > 0:
                values.append(cat_data[value_to_plot].values[0])
                if not use_percentage:
                    std_devs.append(cat_data[f'{value_col}_std'].values[0] if not pd.isna(cat_data[f'{value_col}_std'].values[0]) else 0)
                    counts.append(cat_data[f'{value_col}_count'].values[0])
            else:
                values.append(0)
                if not use_percentage:
                    std_devs.append(0)
                    counts.append(0)

        data_dict[player_type] = values
        sample_sizes[player_type] = len(df_data[df_data[group_col] == player_type])
        if not use_percentage:
            std_dict[player_type] = std_devs
            count_dict[player_type] = counts

    # Create the chart
    player_types_list = list(data_dict.keys())
    n_groups = len(categories)
    x = np.arange(n_groups)
    width = 0.8 / len(player_types_list)

    # Calculate z-score for confidence interval
    z_score = stats.norm.ppf((1 + confidence_level) / 2)

    # Get unified styles for all player types
    player_styles = get_all_player_styles(player_types_list)

    for idx, (player_type, values) in enumerate(data_dict.items()):
        offset = (idx - len(player_types_list)/2 + 0.5) * width
        style = player_styles[player_type]

        # Calculate error bars (95% CI) if requested
        if show_error_bars:
            errors = []
            if use_percentage:
                # Binomial proportion confidence interval
                n = sample_sizes[player_type]
                for val in values:
                    if n > 0:
                        p = val / 100
                        # Calculate 95% confidence interval for binomial proportion
                        se = np.sqrt(p * (1 - p) / n)
                        ci = z_score * se * 100
                        errors.append(ci)
                    else:
                        errors.append(0)
            else:
                # Continuous data confidence interval (for means)
                std_devs = std_dict[player_type]
                counts = count_dict[player_type]
                for std_val, count_val in zip(std_devs, counts):
                    if count_val > 1:
                        se = std_val / np.sqrt(count_val)
                        ci = z_score * se
                        errors.append(ci)
                    else:
                        errors.append(0)

            bars = ax.bar(x + offset, values, width, label=player_type,
                         color=style['color'], alpha=style['alpha'],
                         hatch=style['hatch'], edgecolor='black', linewidth=0.8,
                         yerr=errors, capsize=3)
        else:
            bars = ax.bar(x + offset, values, width, label=player_type,
                         color=style['color'], alpha=style['alpha'],
                         hatch=style['hatch'], edgecolor='black', linewidth=0.8)

        # Add value labels
        add_value_labels_on_bars(ax, bars, value_format, suffix)

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title + f' ({int(confidence_level*100)}% CI)', fontsize=14, fontweight='bold')
    ax.set_xticks(x)

    # Set x-axis labels
    if x_labels:
        ax.set_xticklabels(x_labels, rotation=rotation, ha='right' if rotation else 'center')
    else:
        ax.set_xticklabels(categories, rotation=rotation, ha='right' if rotation else 'center')

    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    _show()

    # Print summary statistics if requested
    if print_summary:
        # Create pivot table for summary
        if use_percentage:
            count_pivot = grouped.pivot(index=category_col, columns=group_col, values='count').fillna(0).astype(int)
            pct_pivot = grouped.pivot(index=category_col, columns=group_col, values='percentage').fillna(0)
            # Combine into "count (pct%)" strings
            summary = count_pivot.astype(str) + ' (' + pct_pivot.round(1).astype(str) + '%)'
        else:
            summary = grouped.pivot(index=category_col, columns=group_col, values=value_col)

        # Rename index if x_labels provided
        if x_labels and len(x_labels) == len(summary.index):
            summary.index = x_labels

        # Transpose so player types are rows (fits better with many player types)
        summary = summary.T
        summary.index.name = None

        # Use pandas display for proper formatting in notebooks
        from IPython.display import display
        display(summary)

    return None  # Suppress Jupyter auto-display of raw grouped DataFrame


def plot_policy_adoption_bars(panel_df, policy_list, policy_labels=None,
                              title="Policy Branch Adoption Rates",
                              figsize=(12, 6), show_error_bars=True):
    """
    Create a grouped bar chart specifically for policy adoption rates.

    Args:
        panel_df: DataFrame with policy columns and player_type column
        policy_list: List of policy column names in desired order
        policy_labels: Optional custom labels for policies
        title: Chart title
        figsize: Figure size tuple
        show_error_bars: Whether to show 95% confidence intervals

    Returns:
        Figure and axis objects
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from scipy import stats

    fig, ax = plt.subplots(figsize=figsize)

    # Get unique player types
    player_types = sort_player_types(panel_df['player_type'].unique())
    n_player_types = len(player_types)
    n_policies = len(policy_list)

    # Prepare labels
    if policy_labels is None:
        policy_labels = [p.capitalize() for p in policy_list]

    # Set up bar positions
    x = np.arange(n_policies)
    width = 0.8 / n_player_types

    # Get unified styles for all player types
    player_styles = get_all_player_styles(player_types)

    # Calculate adoption rates for each player type
    for idx, player_type in enumerate(player_types):
        player_df = panel_df[panel_df['player_type'] == player_type]
        total_players = len(player_df)
        style = player_styles[player_type]

        adoption_rates = []
        error_bars = []

        for policy in policy_list:
            # Count adoptions
            adopted = player_df[policy].notna().sum()
            rate = (adopted / total_players * 100) if total_players > 0 else 0
            adoption_rates.append(rate)

            # Calculate 95% CI for binomial proportion
            if show_error_bars and total_players > 0:
                p = adopted / total_players
                se = np.sqrt(p * (1 - p) / total_players)
                ci = 1.96 * se * 100  # 95% CI
                error_bars.append(ci)
            else:
                error_bars.append(0)

        # Plot bars
        offset = (idx - n_player_types/2 + 0.5) * width
        bars = ax.bar(x + offset, adoption_rates, width,
                      label=player_type, color=style['color'], alpha=style['alpha'],
                      hatch=style['hatch'], edgecolor='black', linewidth=0.8,
                      yerr=error_bars if show_error_bars else None,
                      capsize=3 if show_error_bars else 0)

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.0f}%', ha='center', va='bottom', fontsize=9)

    # Customize plot
    ax.set_xlabel('Policy Branch', fontsize=12)
    ax.set_ylabel('Adoption Rate (%)', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(policy_labels, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, 105)

    plt.tight_layout()
    _show()

    # Print summary statistics
    print(f"\n{'='*60}")
    print(f"{title} Summary")
    print('='*60)

    for player_type in player_types:
        player_df = panel_df[panel_df['player_type'] == player_type]
        total = len(player_df)

        print(f"\n{player_type} (n={total}):")
        print("-" * 40)

        for policy, label in zip(policy_list, policy_labels):
            adopted = player_df[policy].notna().sum()
            rate = (adopted / total * 100) if total > 0 else 0
            print(f"  {label:15} {rate:5.1f}% ({adopted:4d} players)")

    _show()
    return fig, ax


def plot_distribution_histograms(df_data, column_name, xlabel, title,
                                xlim=None, n_bins=15, player_type_filter=None):
    """
    Create distribution histograms for a given metric across player types with consistent bins.

    Args:
        df_data: DataFrame with data (must contain 'player_type' column)
        column_name: Column name to plot
        xlabel: X-axis label for the plots
        title: Overall title for the figure
        xlim: Optional tuple (min, max) to set consistent x-axis limits across all plots
        n_bins: Number of bins for histograms (default 15)
        player_type_filter: Optional list of player types to include (None = all)
    """
    # Extract unique player types from data
    if player_type_filter:
        df_filtered = df_data[df_data['player_type'].isin(player_type_filter)]
        player_types = player_type_filter
    else:
        df_filtered = df_data
        player_types = sort_player_types(df_data['player_type'].unique())

    if len(player_types) == 0:
        print(f"No player types found in the data")
        return

    # Collect all data to determine common xlim and bins
    all_data = []
    for player_type in player_types:
        data = df_filtered[df_filtered['player_type'] == player_type][column_name].dropna()
        if len(data) > 0:
            all_data.extend(data.values)

    if not all_data:
        print(f"No data found for {column_name}")
        return

    # Calculate common xlim if not provided
    if xlim is None:
        data_min, data_max = min(all_data), max(all_data)
        data_range = data_max - data_min
        # Add a small buffer (5%) to the range
        xlim = (data_min - 0.05 * data_range, data_max + 0.05 * data_range)

    # Calculate common bin edges based on xlim
    common_bins = np.linspace(xlim[0], xlim[1], n_bins + 1)

    # Setup subplots
    n_cols = min(3, len(player_types))
    n_rows = (len(player_types) + n_cols - 1) // n_cols

    if len(player_types) == 1:
        fig, ax = plt.subplots(1, 1, figsize=(6, 5))
        axes = [ax]
    else:
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(6*n_cols, 5*n_rows))
        axes = axes.flatten()

    # Get unified styles for all player types
    player_styles = get_all_player_styles(player_types)

    # First pass: create histograms and track max y value
    max_y_value = 0
    hist_data = []

    for idx, player_type in enumerate(player_types):
        data = df_filtered[df_filtered['player_type'] == player_type][column_name].dropna()
        style = player_styles[player_type]

        if len(data) > 0:
            # Create histogram with weights to show percentages
            weights = np.ones_like(data) / len(data) * 100  # Convert to percentages
            n_vals, _, _ = axes[idx].hist(data, bins=common_bins, weights=weights,
                          alpha=style['alpha'], color=style['color'],
                          edgecolor='black', linewidth=1.2)

            # Track max y value across all histograms
            max_y_value = max(max_y_value, max(n_vals))

            axes[idx].set_xlabel(xlabel, fontsize=11)
            axes[idx].set_ylabel('Percentage (%)', fontsize=11)
            axes[idx].set_title(f'{player_type}', fontsize=12, fontweight='bold')
            axes[idx].grid(axis='y', alpha=0.3)

            # Set consistent x-axis limits
            axes[idx].set_xlim(xlim)

            # Store data for second pass
            hist_data.append((idx, data, True))
        else:
            hist_data.append((idx, None, False))

    # Add a small buffer to max_y_value for better visualization
    max_y_value = max_y_value * 1.1

    # Second pass: set consistent y-axis limits and add statistics
    for idx, data, has_data in hist_data:
        # Set consistent y-axis limits for all subplots
        axes[idx].set_ylim(0, max_y_value)

        if has_data:
            # Calculate 95% CI for the mean
            mean_val = data.mean()
            se = stats.sem(data)  # Standard error of the mean
            ci_95 = stats.t.interval(0.95, len(data)-1, loc=mean_val, scale=se)

            # Add 95% CI shading for mean
            axes[idx].axvspan(ci_95[0], ci_95[1], alpha=0.2, color='gray',
                             label=f'95% CI: [{ci_95[0]:.1f}, {ci_95[1]:.1f}]')

            # Add mean and median lines
            axes[idx].axvline(mean_val, color='red', linestyle='--', linewidth=2,
                             label=f'Mean: {mean_val:.1f}')
            median_val = data.median()
            axes[idx].axvline(median_val, color='green', linestyle='--', linewidth=2,
                             label=f'Median: {median_val:.1f}')

            axes[idx].legend(loc='upper right', fontsize=9)
        else:
            # For empty plots, still set the proper labels and limits
            player_type = player_types[idx]
            axes[idx].text(0.5, 0.5, 'No Data Available',
                          ha='center', va='center',
                          transform=axes[idx].transAxes, fontsize=14)
            axes[idx].set_title(f'{player_type}', fontsize=12, fontweight='bold')
            axes[idx].set_xlabel(xlabel, fontsize=11)
            axes[idx].set_ylabel('Percentage (%)', fontsize=11)
            # Set xlim even for empty plots to maintain consistency
            axes[idx].set_xlim(xlim)

    # Hide unused subplots if multiple subplots exist
    if len(player_types) > 1:
        for idx in range(len(player_types), n_rows * n_cols):
            axes[idx].axis('off')

    plt.suptitle(title, fontsize=14, fontweight='bold', y=1.00)
    plt.tight_layout()
    _show()

    # Print statistics with 95% CI as a single table
    print(f"\n{title} Statistics:")
    rows = []
    for player_type in player_types:
        data = df_filtered[df_filtered['player_type'] == player_type][column_name].dropna()
        if len(data) > 0:
            mean_val = data.mean()
            se = stats.sem(data)
            ci_95 = stats.t.interval(0.95, len(data)-1, loc=mean_val, scale=se)
            rows.append({
                'Player Type': player_type,
                'N': len(data),
                'Mean': round(mean_val, 2),
                'Median': round(data.median(), 2),
                'Std': round(data.std(), 2),
                'Min': round(data.min(), 1),
                'Max': round(data.max(), 1),
                '95% CI': f'[{ci_95[0]:.2f}, {ci_95[1]:.2f}]',
            })
    if rows:
        from IPython.display import display
        summary_df = pd.DataFrame(rows).set_index('Player Type')
        summary_df.index.name = None
        display(summary_df)


# =====================================================
# REGRESSION VISUALIZATION UTILITIES
# =====================================================

def pvalue_to_stars(p):
    """Convert p-value to significance stars: *** (p<0.001), ** (p<0.01), * (p<0.05), or ''."""
    if np.isnan(p):
        return ''
    elif p < 0.001:
        return '***'
    elif p < 0.01:
        return '**'
    elif p < 0.05:
        return '*'
    return ''


def clean_variable_name(name, var_type='condition'):
    """
    Clean up variable names from statsmodels coefficient names.

    Handles interaction terms (contains ':') by cleaning each part and
    joining with ' × '. For non-interaction terms, extracts content from
    square brackets [...] if present, otherwise returns the original name.

    Args:
        name: Raw coefficient name from statsmodels
        var_type: Type of variable (kept for backwards compatibility but not used)

    Returns:
        Cleaned variable name
    """
    import re

    # Handle interaction terms: split on ':', clean each part, rejoin
    if ':' in name:
        parts = name.split(':')
        cleaned_parts = [clean_variable_name(p, var_type) for p in parts]
        return ' × '.join(cleaned_parts)

    # Look for pattern [...] and extract what's inside
    match = re.search(r'\[([^\]]+)\]', name)
    if match:
        content = match.group(1)
        # Remove common prefixes like 'T.' or 'S.'
        if content.startswith('T.') or content.startswith('S.'):
            return content[2:]
        return content

    # If no brackets found, return original name
    return name


def log_odds_to_prob_change(log_odds, baseline_prob=0.125):
    """
    Convert log odds ratio to probability change from baseline.

    Args:
        log_odds: Log odds ratio coefficient
        baseline_prob: Baseline probability

    Returns:
        Change in probability as percentage points
    """
    baseline_odds = baseline_prob / (1 - baseline_prob)
    new_odds = baseline_odds * np.exp(log_odds)
    new_prob = new_odds / (1 + new_odds)
    return (new_prob - baseline_prob) * 100  # Return as percentage points


def deviation_coefficients(model, reference_type):
    """
    Compute deviation-from-grand-mean effects for all player types via contrasts.

    Uses a Treatment-coded OLS model and linear contrasts to get proper CIs/p-values
    for every player type (including the reference). The returned effects are
    deviations from the grand mean — not relative to the reference category.

    Args:
        model: Fitted statsmodels OLS result (Treatment coding on player_type)
        reference_type: Name of the reference player type (e.g., 'GLM-4.7-Simple')

    Returns:
        DataFrame with columns: Name, Effect, CI_Low, CI_High, P_Value, Sig,
        Prob_Change, CI_Low_Prob, CI_High_Prob (last 3 are NaN placeholders)
    """
    params = model.params
    pt_vars = [c for c in params.index if 'player_type' in c]
    K = len(pt_vars) + 1  # total player types (including reference)

    rows = []
    # Non-reference types: deviation = beta_i - (1/K)*sum(betas)
    for var in pt_vars:
        contrast = np.zeros(len(params))
        for j, name in enumerate(params.index):
            if name == var:
                contrast[j] = (K - 1) / K
            elif 'player_type' in name:
                contrast[j] = -1 / K
        t = model.t_test(contrast)
        ci = t.conf_int(alpha=0.05).flatten()
        pval = float(np.squeeze(t.pvalue))
        rows.append({
            'Name': clean_variable_name(var),
            'Effect': float(np.squeeze(t.effect)),
            'CI_Low': float(ci[0]), 'CI_High': float(ci[1]),
            'P_Value': pval,
            'Sig': '***' if pval < 0.001 else '**' if pval < 0.01 else '*' if pval < 0.05 else '',
        })

    # Reference type: deviation = -(1/K)*sum(betas)
    contrast = np.zeros(len(params))
    for j, name in enumerate(params.index):
        if 'player_type' in name:
            contrast[j] = -1 / K
    t = model.t_test(contrast)
    ci = t.conf_int(alpha=0.05).flatten()
    pval = float(np.squeeze(t.pvalue))
    rows.append({
        'Name': reference_type,
        'Effect': float(np.squeeze(t.effect)),
        'CI_Low': float(ci[0]), 'CI_High': float(ci[1]),
        'P_Value': pval,
        'Sig': '***' if pval < 0.001 else '**' if pval < 0.01 else '*' if pval < 0.05 else '',
    })

    df = pd.DataFrame(rows)
    df['Prob_Change'] = np.nan
    df['CI_Low_Prob'] = np.nan
    df['CI_High_Prob'] = np.nan
    return df.sort_values('Effect')


def prepare_coefficient_data(params, conf_int, pvalues, var_names, var_type='condition'):
    """
    Prepare coefficient data for visualization.

    Args:
        params: Model parameters
        conf_int: Confidence intervals
        pvalues: P-values
        var_names: Variable names to extract
        var_type: Type of variable ('condition' or 'civilization')

    Returns:
        DataFrame with cleaned names, effects, CIs, and significance
    """
    data = []
    for var in var_names:
        clean_name = clean_variable_name(var, var_type)
        effect = params[var]
        ci_low, ci_high = conf_int.loc[var]
        pval = pvalues[var]

        # Add significance stars
        if pval < 0.001:
            sig_star = '***'
        elif pval < 0.01:
            sig_star = '**'
        elif pval < 0.05:
            sig_star = '*'
        else:
            sig_star = ''

        data.append({
            'Name': clean_name,
            'Effect': effect,
            'CI_Low': ci_low,
            'CI_High': ci_high,
            'P_Value': pval,
            'Sig': sig_star
        })

    df = pd.DataFrame(data)

    # Add probability change columns
    df['Prob_Change'] = df['Effect'].apply(log_odds_to_prob_change)
    df['CI_Low_Prob'] = df['CI_Low'].apply(log_odds_to_prob_change)
    df['CI_High_Prob'] = df['CI_High'].apply(log_odds_to_prob_change)

    return df.sort_values('Effect')


def plot_forest_plot(df, title, xlabel='Marginal Effect (Relative Rate %)', color='darkblue',
                     figsize=(12, 8), reference_line_label=None,
                     use_prob_scale=True, print_summary=True, sort_alphabetically=False,
                     colors=None, markers=None, annotate_n=False):
    """
    Create a forest plot for regression coefficients with integrated summary.

    Args:
        df: DataFrame with coefficients (from prepare_coefficient_data or bootstrap_ci)
        title: Plot title
        xlabel: X-axis label
        color: Color for significant effects (ignored when *colors* is set)
        figsize: Figure size
        reference_line_label: Label for reference line (if any)
        use_prob_scale: If True, use probability change scale instead of log odds (default True)
        print_summary: If True, print summary statistics after plotting
        sort_alphabetically: If True, sort by name alphabetically; if False, sort by effect size (default False)
        colors: dict mapping Name → colour string; overrides significance-based colouring
        markers: dict mapping Name → matplotlib marker; overrides default 'o'
        annotate_n: If True and 'N' column exists, show sample sizes

    Returns:
        matplotlib figure and axis objects
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Choose which scale to use (default to probability scale for better interpretation)
    if use_prob_scale:
        effect_col = 'Prob_Change'
        ci_low_col = 'CI_Low_Prob'
        ci_high_col = 'CI_High_Prob'
        if xlabel == 'Log Odds Ratio':  # Update default xlabel
            xlabel = 'Marginal Effect (Relative Rate %)'
    else:
        effect_col = 'Effect'
        ci_low_col = 'CI_Low'
        ci_high_col = 'CI_High'

    # Sort by name alphabetically or by effect size
    if sort_alphabetically:
        df = df.sort_values('Name')
    else:
        df = df.sort_values(effect_col)

    # Create the plot
    y_pos = np.arange(len(df))

    # Plot confidence intervals
    for i, row in enumerate(df.itertuples()):
        # Determine colour and marker
        if colors:
            plot_color = colors.get(row.Name, color)
            alpha = 0.8
        else:
            plot_color = color if row.Sig else 'gray'
            alpha = 0.8 if row.Sig else 0.5
        mk = markers.get(row.Name, 'o') if markers else 'o'

        # Draw CI line
        ax.plot([getattr(row, ci_low_col), getattr(row, ci_high_col)], [i, i],
                color=plot_color, linewidth=2.5, alpha=alpha, solid_capstyle='round')

        # Draw point estimate
        ax.scatter(getattr(row, effect_col), i, s=100, color=plot_color,
                   marker=mk, alpha=alpha, zorder=3, edgecolors='black', linewidth=0.5)

        # Add significance stars (only in coefficient mode).  When an FDR pass
        # supplied an 'FDR_Sig' column, append its dagger next to the raw stars
        # (getattr default keeps every other caller unchanged).
        if not colors and row.Sig:
            star_text = row.Sig + (getattr(row, 'FDR_Sig', '') or '')
            ax.text(getattr(row, ci_high_col) + (1 if use_prob_scale else 0.05), i, star_text,
                    fontsize=12, va='center', color='darkred')

    # n= annotations (second pass so x-range is settled)
    if annotate_n and 'N' in df.columns:
        x_lo, x_hi = ax.get_xlim()
        x_pad = (x_hi - x_lo) * 0.015
        for i, row in enumerate(df.itertuples()):
            ax.text(getattr(row, ci_high_col) + x_pad, i,
                    f'n={row.N}', fontsize=8, va='center', color='gray')

    # Add vertical line at zero
    ax.axvline(x=0, color='red', linestyle='--', alpha=0.5, linewidth=1)

    # Customize plot
    ax.set_yticks(y_pos)
    ax.set_yticklabels(df['Name'])
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)

    # Add legend (skip in custom-colour mode — y-tick labels suffice)
    if not colors:
        from matplotlib.patches import Patch
        from matplotlib.lines import Line2D
        legend_elements = [
            Patch(facecolor=color, alpha=0.8, label='Significant (p < 0.05)'),
            Patch(facecolor='gray', alpha=0.5, label='Not Significant')
        ]
        if reference_line_label:
            legend_elements.append(
                Line2D([0], [0], color='red', linestyle='--', alpha=0.5,
                       label=reference_line_label)
            )
        if 'FDR_Sig' in df.columns:
            legend_elements.append(
                Line2D([0], [0], color='none', marker=r'$\dagger$',
                       markerfacecolor='darkred', markeredgecolor='darkred',
                       linestyle='none', label='Survives FDR (q < 0.05)')
            )
        ax.legend(handles=legend_elements, loc='center right')

    plt.tight_layout()

    # Print summary statistics if requested
    if print_summary:
        print("\n" + "=" * 60)
        print(f"{title.split('\\n')[0]} SUMMARY")
        print("=" * 60)

        if colors:
            # Simple listing for bootstrap / custom-colour mode
            n_col = 'N' in df.columns
            for _, row in df.iterrows():
                n_str = f'  (n={row["N"]})' if n_col else ''
                print(f"  {row['Name']:30} {row[effect_col]:.4f} [{row[ci_low_col]:.4f}, {row[ci_high_col]:.4f}]{n_str}")
        else:
            if reference_line_label:
                print(f"\nBaseline: {reference_line_label.replace('No effect ', '').replace('Mean ', 'Average of all ')}")

            # Separate significant and non-significant effects
            sig_effects = df[df['Sig'] != ''].copy()
            nonsig_effects = df[df['Sig'] == ''].copy()

            if len(sig_effects) > 0:
                print(f"\nStatistically Significant Effects (p < 0.05):")
                print("-" * 40)
                for _, row in sig_effects.iterrows():
                    if use_prob_scale:
                        print(f"  {row['Name']:30} {row['Prob_Change']:+6.2f}% [{row['CI_Low_Prob']:+6.2f}%, {row['CI_High_Prob']:+6.2f}%] {row['Sig']}")
                    else:
                        print(f"  {row['Name']:30} {row['Effect']:+6.3f} [{row['CI_Low']:+6.3f}, {row['CI_High']:+6.3f}] {row['Sig']}")
            else:
                print("\n  No statistically significant effects found")

            if len(nonsig_effects) > 0:
                print(f"\nNon-Significant Effects:")
                print("-" * 40)
                for _, row in nonsig_effects.iterrows():
                    if use_prob_scale:
                        print(f"  {row['Name']:30} {row['Prob_Change']:+6.2f}% [{row['CI_Low_Prob']:+6.2f}%, {row['CI_High_Prob']:+6.2f}%]")
                    else:
                        print(f"  {row['Name']:30} {row['Effect']:+6.3f} [{row['CI_Low']:+6.3f}, {row['CI_High']:+6.3f}]")

        if not colors:
            # Add overall statistics
            print(f"\nOverall Statistics:")
            print("-" * 40)
            print(f"  Total effects analyzed: {len(df)}")
            print(f"  Significant effects: {len(sig_effects)} ({len(sig_effects)/len(df)*100:.1f}%)")
            if use_prob_scale:
                print(f"  Range of effects: {df[effect_col].min():.2f}% to {df[effect_col].max():.2f}%")
                if len(sig_effects) > 0:
                    print(f"  Strongest positive effect: {sig_effects.loc[sig_effects[effect_col].idxmax(), 'Name']} ({sig_effects[effect_col].max():.2f}%)")
                    if sig_effects[effect_col].min() < 0:
                        print(f"  Strongest negative effect: {sig_effects.loc[sig_effects[effect_col].idxmin(), 'Name']} ({sig_effects[effect_col].min():.2f}%)")

    _show()
    return fig, ax


def plot_matchup_heatmap(matchup_df, count_df=None, pvalue_df=None,
                         title="Head-to-Head Matchup Probabilities",
                         figsize=(12, 10), cmap='RdYlGn', annot_format='.1f',
                         as_percentage=True, vmin=None, vmax=None, center=None,
                         cbar_label=None):
    """
    Create a heatmap visualization of pairwise outperform probabilities.

    Args:
        matchup_df: DataFrame from create_matchup_matrix() with probabilities
        count_df: Optional DataFrame with match counts for each cell
        pvalue_df: Optional DataFrame with p-values for statistical significance
        title: Plot title
        figsize: Figure size tuple (width, height)
        cmap: Colormap name (default: RdYlGn for Red/Yellow/Green)
        annot_format: Format string for annotations (default: '.1f' for 1 decimal)
        as_percentage: If True, display values as percentages (0-100)
        vmin: Optional minimum value for colormap scale
        vmax: Optional maximum value for colormap scale
        center: Optional center value for colormap scale
        cbar_label: Optional colorbar label

    Returns:
        fig, ax: Matplotlib figure and axes objects
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    # Reorder rows and columns by player type ordering
    sorted_idx = sort_player_types(matchup_df.index)
    matchup_df = matchup_df.loc[sorted_idx, sorted_idx]
    if count_df is not None:
        count_df = count_df.loc[sorted_idx, sorted_idx]
    if pvalue_df is not None:
        pvalue_df = pvalue_df.loc[sorted_idx, sorted_idx]

    # Convert to percentage if requested
    if as_percentage:
        plot_data = matchup_df * 100
        _cbar_label = 'Outperform Probability (%)'
        _vmin, _vmax = 0, 100
        _center = 50
    else:
        plot_data = matchup_df
        _cbar_label = 'Outperform Probability'
        _vmin, _vmax = 0, 1
        _center = 0.5

    # Allow caller overrides
    vmin = vmin if vmin is not None else _vmin
    vmax = vmax if vmax is not None else _vmax
    center = center if center is not None else _center
    cbar_label = cbar_label if cbar_label is not None else _cbar_label

    # Helper function to extract base model name (without strategist suffix)
    def get_base_model(player_name):
        """Extract base model id from a player-type label."""
        parsed = shared_split_player_type(player_name)
        return parsed["model_id"] or player_name

    # Create annotations with counts if provided
    if count_df is not None:
        annot_array = np.empty(plot_data.shape, dtype=object)
        for i in range(plot_data.shape[0]):
            for j in range(plot_data.shape[1]):
                prob = plot_data.iloc[i, j]
                count = count_df.iloc[i, j]
                player_i = plot_data.index[i]
                player_j = plot_data.columns[j]

                # Check if same base model but different strategist
                base_i = get_base_model(player_i)
                base_j = get_base_model(player_j)
                is_same_model = (base_i == base_j) and (player_i != player_j) and (base_i != 'Vanilla')

                if np.isnan(prob):
                    # Skip NA cells - leave empty
                    annot_array[i, j] = ''
                else:
                    # Get significance stars from pvalue_df if provided
                    if pvalue_df is not None:
                        p_value = pvalue_df.iloc[i, j]
                        sig_stars = pvalue_to_stars(p_value)
                    else:
                        sig_stars = ''

                    if is_same_model:
                        # Same base model with different strategist - make it bold
                        annot_array[i, j] = f'$\\bf{{{prob:{annot_format}}{sig_stars}}}$\n(n={int(count)})'
                    else:
                        annot_array[i, j] = f'{prob:{annot_format}}{sig_stars}\n(n={int(count)})'

        annot = annot_array
        fmt = ''
    else:
        annot = True
        fmt = annot_format

    # Create figure
    fig, ax = plt.subplots(figsize=figsize)

    # Create heatmap
    sns.heatmap(
        plot_data,
        annot=annot,
        fmt=fmt,
        cmap=cmap,
        square=True,
        cbar_kws={'label': cbar_label},
        vmin=vmin,
        vmax=vmax,
        center=center,
        linewidths=0.5,
        linecolor='gray',
        ax=ax
    )

    # Formatting
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Player B (Defending)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Player A (Attacking)', fontsize=12, fontweight='bold')

    # Rotate labels for readability
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)

    # Add significance legend if count_df is provided
    if count_df is not None:
        legend_text = 'Significance (ANOVA): * p<0.05, ** p<0.01, *** p<0.001\nBold = same model, different strategist'
        fig.text(0.02, 0.02, legend_text, fontsize=9, style='italic',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    plt.tight_layout()

    _show()
    return fig, ax


def plot_coefficient_heatmap(coef_df, pval_df=None, count_df=None, pct_df=None,
                              title="Coefficient Heatmap",
                              figsize=(8, 10), cmap='RdYlGn', vmin=None, vmax=None,
                              center=None, cbar_label='OLS β', footnote=None,
                              value_fmt='{:.2f}'):
    """
    Create a heatmap of regression coefficients with significance stars and counts.

    Args:
        coef_df: DataFrame (rows=groups, columns=variables) of coefficients
        pval_df: Optional DataFrame of p-values (same shape)
        count_df: Optional DataFrame of counts (same shape)
        pct_df: Optional DataFrame of percentages (same shape)
        title: Plot title
        figsize: Figure size tuple
        cmap: Colormap name
        vmin, vmax: Colormap range (None = auto from data)
        center: Value to center colormap at (None = no centering, 0 for diverging)
        cbar_label: Colorbar label
        footnote: Optional footnote text at bottom
        value_fmt: Format string for cell values (default '{:.2f}')

    Returns:
        fig, ax: Matplotlib figure and axes objects
    """
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Reorder rows by player type ordering
    sorted_idx = sort_player_types(coef_df.index)
    coef_df = coef_df.loc[sorted_idx]
    if pval_df is not None:
        pval_df = pval_df.loc[sorted_idx]
    if count_df is not None:
        count_df = count_df.loc[sorted_idx]
    if pct_df is not None:
        pct_df = pct_df.loc[sorted_idx]

    annot_array = np.empty(coef_df.shape, dtype=object)
    for i in range(coef_df.shape[0]):
        for j in range(coef_df.shape[1]):
            b = coef_df.iloc[i, j]
            if np.isnan(b):
                annot_array[i, j] = ''
                continue

            stars = pvalue_to_stars(pval_df.iloc[i, j]) if pval_df is not None else ''
            label = f'{value_fmt.format(b)}{stars}'

            if count_df is not None and pct_df is not None:
                n = count_df.iloc[i, j]
                pct = pct_df.iloc[i, j]
                label += f'\n({int(n)}, {pct:.0f}%)'
            elif count_df is not None:
                n = count_df.iloc[i, j]
                label += f'\n(n={int(n)})'

            annot_array[i, j] = label

    fig, ax = plt.subplots(figsize=figsize)
    heatmap_kw = dict(
        annot=annot_array, fmt='',
        cmap=cmap, vmin=vmin, vmax=vmax,
        linewidths=0.5, linecolor='gray', ax=ax,
        cbar_kws={'label': cbar_label},
    )
    if center is not None:
        heatmap_kw['center'] = center
    sns.heatmap(coef_df, **heatmap_kw)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_ylabel('')

    plt.tight_layout()
    if footnote:
        fig.subplots_adjust(bottom=0.08)
        fig.text(0.02, 0.01, footnote, fontsize=9, style='italic',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

    _show()
    return fig, ax


def plot_replay_heatmap(df, metric='replay_use_nuke',
                        delta=False,
                        title=None, figsize=(10, 8), cmap=None,
                        vmin=None, vmax=None, center=None,
                        cbar_label=None, value_fmt='{:.1f}',
                        footnote=None):
    """
    Create a heatmap of replay metrics with [Before] and [Episode] reference rows.

    Args:
        df: Raw replay DataFrame from load_replay_data()
        metric: Metric to visualize ('replay_use_nuke' or 'replay_nuke')
        delta: If True, plot per-instance delta (metric - before_metric) instead of
               raw values. The [Before] row is dropped (absorbed into the delta) and
               [Episode] shows (episode_metric - before_metric) per condition.
        title: Plot title (auto-generated if None)
        figsize: Figure size tuple
        cmap: Colormap name. Default: 'YlOrRd' for raw, 'RdBu_r' for delta.
        vmin, vmax: Colormap range (None = auto from data)
        center: Value to center colormap at. Defaults to 0 when delta=True.
        cbar_label: Colorbar label (auto-generated if None)
        value_fmt: Format string for mean values (default '{:.1f}')
        footnote: Optional footnote text at bottom (auto-generated if None)

    Returns:
        fig, ax: Matplotlib figure and axes objects
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    import numpy as np

    # Map metric to before/episode metrics
    metric_map = {
        'replay_use_nuke': {'before': 'prev_use_nuke', 'episode': 'after_use_nuke'},
        'replay_nuke': {'before': 'prev_nuke', 'episode': 'after_nuke'}
    }

    if metric not in metric_map:
        raise ValueError(f"metric must be one of {list(metric_map.keys())}")

    before_metric = metric_map[metric]['before']
    episode_metric = metric_map[metric]['episode']

    # Delta-aware defaults
    if cmap is None:
        cmap = 'RdBu_r' if delta else 'YlOrRd'
    if delta and center is None:
        center = 0

    # Auto-generate title and label if not provided
    if title is None:
        metric_name = metric.replace('_', ' ').title()
        suffix = f" Δ (vs {before_metric})" if delta else ""
        title = f"{metric_name}{suffix} by Condition and Model"

    if cbar_label is None:
        cbar_label = f"Δ {metric}" if delta else metric.replace('_', ' ').title()

    # Ensure we have the replay_model_canonical column
    if 'replay_model_canonical' not in df.columns:
        raise ValueError("DataFrame must have 'replay_model_canonical' column. "
                        "Apply canonical_replay_model mapping first.")

    # Step 1: Calculate per-instance means across 3 replays
    instance_agg = df.groupby(['condition', 'replay_model_canonical',
                               'game_id', 'player_id', 'turn']).agg({
        metric: 'mean',  # Mean across 3 replays per instance
        before_metric: 'first',  # Same for all replays
        episode_metric: 'first'  # Same for all replays
    }).reset_index()

    # Compute per-instance delta for the plotted metric if delta mode
    plot_col = metric
    if delta:
        plot_col = f'{metric}_delta'
        instance_agg[plot_col] = instance_agg[metric] - instance_agg[before_metric]

    # Step 2: Calculate mean and std across instances for each (condition, model)
    model_stats = instance_agg.groupby(['condition', 'replay_model_canonical']).agg({
        plot_col: ['mean', 'std']
    }).reset_index()

    # Flatten multi-index columns
    model_stats.columns = ['condition', 'replay_model_canonical', 'mean', 'std']

    # Pivot to heatmap format
    heatmap_mean = model_stats.pivot(index='replay_model_canonical',
                                      columns='condition', values='mean')
    heatmap_std = model_stats.pivot(index='replay_model_canonical',
                                     columns='condition', values='std')

    # Step 3: Create reference rows
    if delta:
        # [Episode] = episode_metric - before_metric (paired per row)
        episode_delta = df[episode_metric] - df[before_metric]
        episode_stats = df.assign(_delta=episode_delta).groupby('condition')['_delta'].agg(['mean', 'std'])
        episode_row_mean = pd.DataFrame([episode_stats['mean'].values],
                                         columns=episode_stats.index,
                                         index=['[Episode]'])
        episode_row_std = pd.DataFrame([episode_stats['std'].values],
                                        columns=episode_stats.index,
                                        index=['[Episode]'])
        # [Before] is absorbed into the delta; omit.
        heatmap_mean = pd.concat([episode_row_mean, heatmap_mean])
        heatmap_std = pd.concat([episode_row_std, heatmap_std])
    else:
        before_stats = df.groupby('condition')[before_metric].agg(['mean', 'std'])
        episode_stats = df.groupby('condition')[episode_metric].agg(['mean', 'std'])

        before_row_mean = pd.DataFrame([before_stats['mean'].values],
                                        columns=before_stats.index,
                                        index=['[Before]'])
        before_row_std = pd.DataFrame([before_stats['std'].values],
                                       columns=before_stats.index,
                                       index=['[Before]'])
        episode_row_mean = pd.DataFrame([episode_stats['mean'].values],
                                         columns=episode_stats.index,
                                         index=['[Episode]'])
        episode_row_std = pd.DataFrame([episode_stats['std'].values],
                                        columns=episode_stats.index,
                                        index=['[Episode]'])
        heatmap_mean = pd.concat([before_row_mean, episode_row_mean, heatmap_mean])
        heatmap_std = pd.concat([before_row_std, episode_row_std, heatmap_std])

    # Step 4: Compute p-values for two t-tests per non-special cell:
    #   † vs 'original' condition for same model (Welch's t-test, independent)
    #   ‡ vs 'before' values for same (model, condition)
    #     - raw mode: paired t-test (metric vs before_metric per instance)
    #     - delta mode: one-sample t-test (delta vs 0)
    from scipy import stats as _stats

    baseline_condition = 'original'
    pval_vs_original = pd.DataFrame(np.nan, index=heatmap_mean.index, columns=heatmap_mean.columns)
    pval_vs_before = pd.DataFrame(np.nan, index=heatmap_mean.index, columns=heatmap_mean.columns)

    for model in heatmap_mean.index:
        if model == '[Before]':
            continue

        # [Episode] row: ‡ only (vs before), aggregated across all models
        if model == '[Episode]':
            for cond in heatmap_mean.columns:
                cond_df = df[df['condition'] == cond]
                if delta:
                    ep_delta = (cond_df[episode_metric] - cond_df[before_metric]).dropna().values
                    if len(ep_delta) >= 2 and np.std(ep_delta) > 0:
                        res = _stats.ttest_1samp(ep_delta, 0.0)
                        pval_vs_before.loc[model, cond] = res.pvalue
                else:
                    paired = cond_df[[episode_metric, before_metric]].dropna()
                    if len(paired) >= 2 and paired[episode_metric].std() + paired[before_metric].std() > 0:
                        res = _stats.ttest_rel(paired[episode_metric].values, paired[before_metric].values)
                        pval_vs_before.loc[model, cond] = res.pvalue
            continue

        # Baseline values (original condition) for vs-original test
        baseline_vals = instance_agg[
            (instance_agg['replay_model_canonical'] == model) &
            (instance_agg['condition'] == baseline_condition)
        ][plot_col].dropna().values if baseline_condition in heatmap_mean.columns else np.array([])

        for cond in heatmap_mean.columns:
            cell_rows = instance_agg[
                (instance_agg['replay_model_canonical'] == model) &
                (instance_agg['condition'] == cond)
            ]
            cond_vals = cell_rows[plot_col].dropna().values

            # vs original (skip the original column itself)
            if cond != baseline_condition and len(cond_vals) >= 2 and len(baseline_vals) >= 2:
                res = _stats.ttest_ind(cond_vals, baseline_vals, equal_var=False)
                pval_vs_original.loc[model, cond] = res.pvalue

            # vs before
            if delta:
                # one-sample t-test: delta vs 0
                if len(cond_vals) >= 2 and np.std(cond_vals) > 0:
                    res = _stats.ttest_1samp(cond_vals, 0.0)
                    pval_vs_before.loc[model, cond] = res.pvalue
            else:
                paired = cell_rows[[metric, before_metric]].dropna()
                if len(paired) >= 2 and paired[metric].std() + paired[before_metric].std() > 0:
                    res = _stats.ttest_rel(paired[metric].values, paired[before_metric].values)
                    pval_vs_before.loc[model, cond] = res.pvalue

    # Create annotations: "mean ± std" on line 1, "O:** B:***" on line 2 for non-special cells
    annot_array = np.empty(heatmap_mean.shape, dtype=object)
    for i in range(heatmap_mean.shape[0]):
        for j in range(heatmap_mean.shape[1]):
            mean_val = heatmap_mean.iloc[i, j]
            std_val = heatmap_std.iloc[i, j]
            if np.isnan(mean_val):
                annot_array[i, j] = ''
                continue

            line1 = f'{value_fmt.format(mean_val)} ± {std_val:.1f}'

            p_o = pval_vs_original.iloc[i, j]
            p_b = pval_vs_before.iloc[i, j]
            parts = []
            if not np.isnan(p_o):
                parts.append(f'†{pvalue_to_stars(p_o) or "ns"}')
            if not np.isnan(p_b):
                parts.append(f'‡{pvalue_to_stars(p_b) or "ns"}')
            line2 = '  '.join(parts)

            annot_array[i, j] = f'{line1}\n{line2}' if line2 else line1

    # Create heatmap
    fig, ax = plt.subplots(figsize=figsize)
    heatmap_kw = dict(
        annot=annot_array, fmt='',
        cmap=cmap, vmin=vmin, vmax=vmax,
        linewidths=0.5, linecolor='white', ax=ax,
        cbar_kws={'label': cbar_label},
    )
    if center is not None:
        heatmap_kw['center'] = center

    sns.heatmap(heatmap_mean, **heatmap_kw)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Condition', fontsize=12)
    ax.set_ylabel('Model', fontsize=12)

    def _two_line_condition_label(label):
        label = str(label)
        parts = label.split('-')
        if len(parts) <= 1:
            return label

        candidates = []
        for split_at in range(1, len(parts)):
            left = '-'.join(parts[:split_at])
            right = '-'.join(parts[split_at:])
            candidates.append((max(len(left), len(right)), abs(len(left) - len(right)), left, right))

        _, _, left, right = min(candidates)
        return f'{left}\n{right}'

    ax.set_xticks(np.arange(len(heatmap_mean.columns)) + 0.5)
    ax.set_xticklabels(
        [_two_line_condition_label(label) for label in heatmap_mean.columns],
        rotation=0, ha='center', va='top'
    )
    ax.tick_params(axis='x', labelsize=10, pad=6)

    # Auto-generate footnote
    if footnote is None:
        if delta:
            footnote = (
                f"Cells: mean ± std of Δ = ({metric} − {before_metric}) across instances "
                f"(per-instance mean over 3 replays). "
                f"[Episode] = ({episode_metric} − {before_metric}) per condition. "
                f"[Before] row absorbed into the delta. "
                f"Stars (2nd line): † = Welch's t-test vs '{baseline_condition}' condition (same model); "
                f"‡ = one-sample t-test of Δ vs 0. "
                f"* p<0.05, ** p<0.01, *** p<0.001, ns = not significant."
            )
        else:
            footnote = (
                f"Cells: mean ± std of {metric} across instances (per-instance mean over 3 replays). "
                f"[Before] = {before_metric}, [Episode] = {episode_metric} (per-condition mean ± std). "
                f"Stars (2nd line): † = Welch's t-test vs '{baseline_condition}' condition (same model); "
                f"‡ = paired t-test vs {before_metric} (same cell). "
                f"* p<0.05, ** p<0.01, *** p<0.001, ns = not significant."
            )

    plt.tight_layout()
    if footnote:
        fig.subplots_adjust(bottom=0.15)
        fig.text(0.02, 0.01, footnote, fontsize=9, style='italic',
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3),
                 wrap=True)

    _show()
    return fig, ax


def print_within_instance_variance_table(df, metrics=None):
    """
    Print a table showing within-instance variance for each replay model.

    Calculates the mean standard deviation across 3 replays per instance,
    averaged across all instances and conditions for each model. Also reports
    direction variation ratio, where 0 means all retries share the same
    direction and higher values indicate less directional agreement.

    Args:
        df: Raw replay DataFrame from load_replay_data()
        metrics: List of metrics to analyze (default: ['replay_use_nuke', 'replay_nuke'])

    Returns:
        DataFrame with variance statistics
    """
    import numpy as np
    import pandas as pd

    if metrics is None:
        metrics = ['replay_use_nuke', 'replay_nuke']
    metrics = list(metrics)

    # Ensure we have the replay_model_canonical column
    if 'replay_model_canonical' not in df.columns:
        raise ValueError("DataFrame must have 'replay_model_canonical' column. "
                        "Apply canonical_replay_model mapping first.")

    group_cols = ['condition', 'replay_model_canonical', 'game_id', 'player_id', 'turn']

    # Calculate per-instance standard deviations across 3 replays
    instance_stds = df.groupby(group_cols, observed=True)[metrics].std().reset_index()

    # Calculate mean std for each model (across all conditions and instances)
    model_variance = instance_stds.groupby('replay_model_canonical')[metrics].mean()

    # Rename columns for clarity
    model_variance.columns = [f'{col} (mean within-instance std)' for col in model_variance.columns]

    # Direction variation ratio: 1 - majority direction share within each instance.
    # Floor convention: staying at 0 is counted as decrease/non-escalatory because
    # the metric cannot deescalate further.
    direction_variation = {}
    for metric in metrics:
        if metric not in _REPLAY_METRIC_MAP:
            continue
        before_col = _REPLAY_METRIC_MAP[metric]['before']
        if before_col not in df.columns:
            continue

        work = df[group_cols + [metric, before_col]].copy()
        values = pd.to_numeric(work[metric], errors='coerce')
        before = pd.to_numeric(work[before_col], errors='coerce')
        delta = values - before

        direction = pd.Series(np.nan, index=work.index, dtype='float64')
        direction.loc[delta < -0.5] = -1
        direction.loc[delta.between(-0.5, 0.5, inclusive='both')] = 0
        direction.loc[delta > 0.5] = 1
        direction.loc[(before == 0) & (values == 0)] = -1
        work['_direction'] = direction

        def variation_ratio(directions):
            directions = directions.dropna()
            if len(directions) == 0:
                return np.nan
            return 1 - (directions.value_counts().max() / len(directions))

        instance_direction_variation = (
            work.groupby(group_cols, observed=True)['_direction']
            .agg(variation_ratio)
            .reset_index()
        )
        direction_variation[f'{metric} (mean direction variation ratio)'] = (
            instance_direction_variation
            .groupby('replay_model_canonical')['_direction']
            .mean()
        )

    if direction_variation:
        direction_variation = pd.DataFrame(direction_variation)
        model_variance = model_variance.join(direction_variation, how='left')

    # Sort by first metric
    model_variance = model_variance.sort_values(by=model_variance.columns[0])

    print("Within-Instance Variance by Model")
    print("=" * 80)
    print("(Mean standard deviation and direction variation ratio across 3 replays per instance,")
    print(" averaged across all instances)")
    print(" Direction variation ratio = 1 - majority direction share; 0->0 is counted as decrease/non-escalatory.")
    print()
    display(model_variance)
    print()

    return model_variance


def plot_strategy_radar_charts(panel_df, columns=None, labels=None,
                                figsize=None, ylim=None,
                                title="Grand Strategy Profiles by Player Type",
                                print_summary=True):
    """
    Create radar charts showing metric distributions for each player type.

    Each radar chart displays the mean values for specified columns across player types.
    Useful for visualizing strategic profiles, change rates, or any multi-dimensional metrics.

    Args:
        panel_df: DataFrame with metric columns and player_type column
        columns: List of column names to plot. If None, defaults to grand strategy ratios
                 (default: ['domination_ratio', 'culture_ratio', 'diplomatic_ratio', 'science_ratio'])
        labels: List of labels for the axes. If None, auto-generates from column names
        figsize: Figure size tuple (auto-calculated if None)
        ylim: Tuple of (min, max) for radial axis limits. If None, auto-scales to data
        title: Overall title for the figure
        print_summary: Whether to print summary statistics

    Returns:
        Figure and axes objects

    Examples:
        # Grand strategy ratios (default)
        plot_strategy_radar_charts(panel_df)

        # Custom columns with change rates
        plot_strategy_radar_charts(
            panel_df,
            columns=['domination_ratio', 'culture_ratio', 'diplomatic_ratio',
                     'science_ratio', 'strategy_change_rate', 'persona_change_rate'],
            labels=['Domination', 'Culture', 'Diplomatic', 'Science',
                    'Strategy Changes', 'Persona Changes']
        )
    """
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import stats

    # Default columns: grand strategy ratios
    if columns is None:
        columns = ['domination_ratio', 'culture_ratio', 'diplomatic_ratio', 'science_ratio']

    # Auto-generate labels if not provided
    if labels is None:
        labels = [col.replace('_ratio', '').replace('_rate', '').replace('_', ' ').title()
                  for col in columns]

    # Get unique player types
    player_types = sort_player_types(panel_df['player_type'].unique())
    n_player_types = len(player_types)

    # Auto-calculate figure size if not provided
    if figsize is None:
        n_cols = min(3, n_player_types)
        n_rows = (n_player_types + n_cols - 1) // n_cols
        figsize = (6 * n_cols, 5 * n_rows)
    else:
        n_cols = min(3, n_player_types)
        n_rows = (n_player_types + n_cols - 1) // n_cols

    # Create subplots with polar projection
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize,
                             subplot_kw=dict(projection='polar'))

    # Flatten axes array for easier iteration
    if n_player_types == 1:
        axes = [axes]
    else:
        axes = axes.flatten()

    # Number of variables
    num_vars = len(columns)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    # Complete the circle
    angles += angles[:1]

    # Get unified styles for all player types
    player_styles = get_all_player_styles(player_types)

    # Determine ylim if not provided
    if ylim is None:
        all_values = []
        for col in columns:
            all_values.extend(panel_df[col].dropna().values)
        if all_values:
            data_min = min(all_values)
            data_max = max(all_values)
            # Add 10% padding
            padding = (data_max - data_min) * 0.1
            ylim = (max(0, data_min - padding), data_max)
        else:
            ylim = (0, 1)

    # Create radar chart for each player type
    for idx, player_type in enumerate(player_types):
        ax = axes[idx]
        player_data = panel_df[panel_df['player_type'] == player_type]
        style = player_styles[player_type]

        # Calculate mean values for each column
        values = []
        for col in columns:
            mean_val = player_data[col].mean()
            values.append(mean_val)

        # Complete the circle
        values += values[:1]

        # Plot data
        ax.plot(angles, values, 'o-', linewidth=2, color=style['color'],
                label=player_type, markersize=8)
        ax.fill(angles, values, alpha=0.25, color=style['color'])

        # Set labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, fontsize=10)
        ax.set_ylim(ylim)
        ax.set_title(player_type, fontsize=12, fontweight='bold', pad=20)

        # Add gridlines
        ax.grid(True, alpha=0.3)

        # Add y-axis labels
        num_ticks = 5
        y_ticks = np.linspace(ylim[0], ylim[1], num_ticks)
        ax.set_yticks(y_ticks)
        ax.set_yticklabels([f'{val:.2f}' for val in y_ticks], fontsize=8)

    # Hide unused subplots
    for idx in range(n_player_types, len(axes)):
        axes[idx].axis('off')

    plt.suptitle(title, fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    _show()

    # Print summary statistics as a single table
    if print_summary:
        print(f"\n{title} Summary:")
        rows = []
        for player_type in player_types:
            player_data = panel_df[panel_df['player_type'] == player_type]
            row = {'Player Type': player_type, 'N': len(player_data)}
            for col, label in zip(columns, labels):
                table_label = label.replace('\n', ' ')
                data = player_data[col].dropna()
                if len(data) > 0:
                    mean_val = data.mean()
                    se = stats.sem(data)
                    ci_95 = stats.t.interval(0.95, len(data)-1, loc=mean_val, scale=se) if len(data) > 1 else (mean_val, mean_val)
                    row[table_label] = f'{mean_val:.3f} [{ci_95[0]:.3f}, {ci_95[1]:.3f}]'
                else:
                    row[table_label] = 'N/A'
            rows.append(row)
        if rows:
            import pandas as pd
            from IPython.display import display
            summary_df = pd.DataFrame(rows).set_index('Player Type')
            summary_df.index.name = None
            display(summary_df)

    return fig, axes


# =====================================================
# SANKEY DIAGRAM UTILITIES FOR POLICY ANALYSIS
# =====================================================

def _apply_filters(df, condition_filter, player_filter):
    """Apply condition and player filters to dataframe."""
    df_filtered = df.copy()

    if condition_filter is not None:
        if 'condition' in df_filtered.columns:
            df_filtered = df_filtered[df_filtered['condition'] == condition_filter]
        elif 'experiment' in df_filtered.columns:
            df_filtered['condition'] = df_filtered['experiment']
            df_filtered = df_filtered[df_filtered['condition'] == condition_filter]

    if player_filter is not None:
        if isinstance(player_filter, (int, str)):
            player_filter = [player_filter]
        df_filtered = df_filtered[df_filtered['player_id'].isin(player_filter)]

    return df_filtered


def _extract_policy_sequences(df_filtered, all_policies):
    """Extract policy sequences for each player."""
    policy_sequences = []

    for _, row in df_filtered.iterrows():
        adopted = []
        for policy in all_policies:
            if policy in row and pd.notna(row[policy]) and row[policy] != 'N/A':
                try:
                    turn = float(row[policy])
                    adopted.append((policy, turn))
                except:
                    continue

        adopted.sort(key=lambda x: x[1])
        sequence = [p[0] for p in adopted]

        if sequence:
            policy_sequences.append(sequence)

    return policy_sequences


def _count_transitions(policy_sequences, ideologies):
    """Count transitions between policies and their positions."""
    from collections import defaultdict

    transitions = defaultdict(int)
    position_counts = defaultdict(lambda: defaultdict(int))

    for sequence in policy_sequences:
        for i, policy in enumerate(sequence):
            is_final = (i == len(sequence) - 1 and policy in ideologies)
            position = "Final" if is_final else f"Position {i+1}"
            position_counts[position][policy] += 1

            if i < len(sequence) - 1:
                next_policy = sequence[i+1]
                is_next_final = (i+1 == len(sequence) - 1 and next_policy in ideologies)

                source = f"{policy} (Pos {i+1})"
                target = f"{next_policy} ({'Final' if is_next_final else f'Pos {i+2}'})"
                transitions[(source, target)] += 1

    return transitions, position_counts


def _prune_low_flows(transitions, min_flow_ratio):
    """Remove low-flow branches while maintaining connectivity."""
    from collections import defaultdict

    total_flow = sum(transitions.values())
    min_flow = max(1, int(total_flow * min_flow_ratio))

    # Build connectivity maps
    incoming = defaultdict(list)
    outgoing = defaultdict(list)
    all_nodes = set()

    for (source, target), flow in transitions.items():
        incoming[target].append((source, flow))
        outgoing[source].append((target, flow))
        all_nodes.update([source, target])

    # Identify special nodes that should always be kept
    terminal_nodes = {node for node in all_nodes if node not in outgoing}  # End nodes
    beginning_nodes = {node for node in all_nodes if '(Pos 1)' in node}   # Start nodes
    final_nodes = {node for node in all_nodes if '(Final)' in node}       # Final ideology nodes

    # Always keep beginning, terminal, and final nodes
    nodes_to_keep = set(beginning_nodes) | terminal_nodes | final_nodes
    nodes_to_process = list(nodes_to_keep)

    # Backward propagation from special nodes
    while nodes_to_process:
        node = nodes_to_process.pop(0)
        # Add all nodes that feed into this kept node
        for source, _ in incoming.get(node, []):
            if source not in nodes_to_keep:
                total_flow_from_source = sum(flow for _, flow in outgoing.get(source, []))
                # Keep node if it has sufficient flow or connects to important nodes
                if total_flow_from_source >= min_flow:
                    nodes_to_keep.add(source)
                    nodes_to_process.append(source)

    # Filter transitions - only apply min_flow filter if both nodes are kept
    filtered_transitions = {
        (s, t): flow for (s, t), flow in transitions.items()
        if s in nodes_to_keep and t in nodes_to_keep
    }

    return filtered_transitions


def create_policy_sankey(df, condition_filter=None, player_filter=None,
                         title="Policy Branch Adoption Flow",
                         figsize=(14, 10), min_flow_ratio=0.001):
    """
    Create a Sankey diagram showing the flow of policy branch adoptions.

    Args:
        df: DataFrame with policy branch columns (should contain turn numbers for each policy)
        condition_filter: Optional condition name to filter data
        player_filter: Optional player ID or list of player IDs to filter
        title: Title for the diagram
        figsize: Figure size tuple
        min_flow_ratio: Minimum flow ratio to keep (as fraction of total flows)

    Returns:
        fig, ax: Figure and axis objects
    """
    import plotly.graph_objects as go
    from collections import defaultdict

    # Apply filters
    df_filtered = _apply_filters(df, condition_filter, player_filter)

    # Define policy categories
    policy_categories = {
        'ancient': ['tradition', 'authority', 'progress'],
        'medieval': ['fealty', 'statecraft', 'artistry'],
        'industrial': ['industry', 'imperialism', 'rationalism'],
        'ideologies': ['freedom', 'autocracy', 'order']
    }
    all_policies = sum(policy_categories.values(), [])

    # Extract sequences
    policy_sequences = _extract_policy_sequences(df_filtered, all_policies)

    if not policy_sequences:
        print(f"No policy sequences found for the given filters")
        return None, None

    # Count transitions and positions
    transitions, position_counts = _count_transitions(policy_sequences, policy_categories['ideologies'])

    # Apply pruning if needed
    if min_flow_ratio > 0 and transitions:
        transitions = _prune_low_flows(transitions, min_flow_ratio)

    # Create Sankey diagram
    fig = _create_sankey_figure(transitions, policy_sequences, condition_filter,
                                player_filter, title, figsize, position_counts)

    # Print summary
    _print_sankey_summary(policy_sequences, transitions, position_counts, title)

    return fig, None


def _create_sankey_figure(transitions, policy_sequences, condition_filter,
                          player_filter, title, figsize, position_counts):
    """Create the Plotly Sankey figure."""
    import plotly.graph_objects as go

    # Prepare data for Sankey
    labels = []
    label_map = {}
    sources = []
    targets = []
    values = []

    # Add all unique labels from transitions
    for (source, target), value in transitions.items():
        for label in [source, target]:
            if label not in label_map:
                label_map[label] = len(labels)
                labels.append(label)

        sources.append(label_map[source])
        targets.append(label_map[target])
        values.append(value)

    # Define policy colors
    policy_colors = {
        'tradition': '#8B4513', 'authority': '#DC143C', 'progress': '#4169E1',
        'fealty': '#FFD700', 'statecraft': '#800080', 'artistry': '#FF69B4',
        'industry': '#696969', 'imperialism': '#FF4500', 'rationalism': '#00CED1',
        'freedom': '#1E90FF', 'autocracy': '#8B0000', 'order': '#2F4F4F'
    }

    # Assign colors to nodes
    node_colors = [
        policy_colors.get(label.split(' ')[0].lower(), '#808080')
        for label in labels
    ]

    # Sample size for percentage calculations
    sample_size = len(policy_sequences)

    # Create custom hover data for links (with percentages relative to sample)
    link_hover_text = []
    for s_idx, t_idx, val in zip(sources, targets, values):
        source_label = labels[s_idx]
        target_label = labels[t_idx]
        percentage = (val / sample_size) * 100
        hover = f'{source_label} → {target_label}<br>Count: {val} ({percentage:.1f}% of players)'
        link_hover_text.append(hover)

    # Calculate node counts from position_counts
    node_counts = {}
    for label in labels:
        # Parse label to get policy name and position
        parts = label.split(' (')
        if len(parts) == 2:
            policy = parts[0]
            pos_str = parts[1].rstrip(')')

            # Convert position string to match position_counts keys
            if pos_str == 'Final':
                position = 'Final'
            else:
                position = pos_str.replace('Pos ', 'Position ')

            # Get count from position_counts
            count = position_counts.get(position, {}).get(policy, 0)
            node_counts[label] = count
        else:
            node_counts[label] = 0

    # Create custom hover for nodes
    node_hover_text = []
    for label in labels:
        count = node_counts.get(label, 0)
        percentage = (count / sample_size) * 100 if sample_size > 0 else 0
        hover = f'{label}<br>Players: {count} ({percentage:.1f}%)'
        node_hover_text.append(hover)

    # Create Sankey diagram
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15, thickness=20,
            line=dict(color="black", width=0.5),
            label=labels, color=node_colors,
            hovertemplate='%{customdata}<extra></extra>',
            customdata=node_hover_text
        ),
        link=dict(
            source=sources, target=targets, value=values,
            color='rgba(128, 128, 128, 0.4)',
            hovertemplate='%{customdata}<extra></extra>',
            customdata=link_hover_text
        )
    )])

    # Update layout with subtitle
    subtitle = _create_subtitle(policy_sequences, condition_filter, player_filter)
    fig.update_layout(
        title=dict(text=f"{title}<br><sub>{subtitle}</sub>", x=0.5, xanchor='center'),
        font_size=12,
        height=figsize[1] * 72,
        width=figsize[0] * 72
    )

    return fig


def _create_subtitle(policy_sequences, condition_filter, player_filter):
    """Create subtitle for the Sankey diagram."""
    subtitle = f"(n={len(policy_sequences)} players"
    if condition_filter:
        subtitle += f", condition: {condition_filter}"
    if player_filter:
        subtitle += f", player(s): {player_filter}"
    subtitle += ")"
    return subtitle


def _print_sankey_summary(policy_sequences, transitions, position_counts, title):
    """Print summary statistics for the Sankey diagram."""
    print(f"\n{title} Summary:")
    print(f"Total players analyzed: {len(policy_sequences)}")
    print(f"Total transitions: {sum(transitions.values())}")

    # Most common first choices
    print(f"\nMost common first choices:")
    first_policies = position_counts.get('Position 1', {})
    for policy, count in sorted(first_policies.items(), key=lambda x: x[1], reverse=True)[:5]:
        percentage = (count / len(policy_sequences)) * 100
        print(f"  {policy}: {count} ({percentage:.1f}%)")

    # Most common second choices
    print(f"\nMost common second choices:")
    second_policies = position_counts.get('Position 2', {})
    if second_policies:
        total_second = sum(second_policies.values())
        for policy, count in sorted(second_policies.items(), key=lambda x: x[1], reverse=True)[:5]:
            percentage = (count / total_second) * 100
            print(f"  {policy}: {count} ({percentage:.1f}%)")

    # Most common transitions
    print(f"\nMost common transitions:")
    for (source, target), count in sorted(transitions.items(), key=lambda x: x[1], reverse=True)[:5]:
        percentage = (count / sum(transitions.values())) * 100
        source_policy = source.split(' ')[0]
        target_policy = target.split(' ')[0]
        print(f"  {source_policy} → {target_policy}: {count} ({percentage:.1f}%)")


# =====================================================
# TOKEN USAGE VISUALIZATION UTILITIES
# =====================================================

def plot_metric_over_time(turn_df, metric_col=None, metric_calculation=None,
                         title="Metric Over Time by Player Type",
                         xlabel=None, ylabel="Metric Value",
                         figsize=(12, 6), show_confidence=True, confidence_level=0.95,
                         turn_interval=None, max_turn=None, min_turn=None,
                         player_type_filter=None, print_summary=True,
                         ylim=None, legend_loc='best', invert_y=False,
                         use_turn_progress=False, use_logit=False):
    """
    Plot any metric over time for different player types with confidence intervals.

    This is a generalized function that can plot any metric from the turn data.
    You can either specify an existing column or provide a calculation function.

    Args:
        turn_df: DataFrame with turn data (must contain 'turn' and 'player_type')
        metric_col: Name of the column to plot (e.g., 'score', 'rank')
        metric_calculation: Optional function to calculate metric from df (e.g., lambda df: df['score']/df['max_score'])
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        figsize: Figure size tuple
        show_confidence: Whether to show confidence intervals
        confidence_level: Confidence level for intervals (default 0.95)
        turn_interval: Interval for x-axis ticks (default 10)
        max_turn: Maximum turn to include (None = all) - ignored if use_turn_progress=True
        min_turn: Minimum turn to include (None = all) - ignored if use_turn_progress=True
        player_type_filter: List of player types to include (None = all)
        print_summary: Whether to print summary statistics
        ylim: Optional tuple (ymin, ymax) for y-axis limits
        legend_loc: Location for legend (default 'best')
        invert_y: If True, invert the y-axis (useful for rank where lower is better)
        use_turn_progress: If True, plot using turn_progress (0-1 scale) instead of turn number,
                          and ignore max_turn/min_turn filters (default False)
        use_logit: If True, transform metric values to log-odds space before averaging,
                  then transform back for plotting (default False)

    Returns:
        Figure and axis objects
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from scipy import stats

    # Set defaults based on use_turn_progress
    if xlabel is None:
        xlabel = "Progress %" if use_turn_progress else "Turn"
    if turn_interval is None:
        turn_interval = 0.05 if use_turn_progress else 10

    # Filter data if needed
    df = turn_df.copy()

    if min_turn is not None:
        df = df[df['turn'] >= min_turn]
    if max_turn is not None:
        df = df[df['turn'] <= max_turn]

    if player_type_filter is not None:
        df = df[df['player_type'].isin(player_type_filter)]

    # Calculate or select the metric
    if metric_calculation is not None:
        df['metric_value'] = metric_calculation(df)
    elif metric_col is not None:
        df['metric_value'] = df[metric_col]
    else:
        raise ValueError("Either metric_col or metric_calculation must be provided")

    # Transform to logit space if requested
    if use_logit:
        df['metric_value'] = logit(df['metric_value'])

    # Determine x-axis variable (turn or turn_progress)
    x_var = 'turn_progress' if use_turn_progress else 'turn'

    # Group by x_var and player_type to calculate statistics
    grouped = df.groupby([x_var, 'player_type'])['metric_value'].agg([
        'mean',
        'std',
        'count',
        'sem'  # Standard error of mean
    ]).reset_index()

    # Calculate confidence intervals
    z_score = stats.norm.ppf((1 + confidence_level) / 2)
    grouped['ci_lower'] = grouped['mean'] - z_score * grouped['sem']
    grouped['ci_upper'] = grouped['mean'] + z_score * grouped['sem']

    # Transform back from logit space if requested
    if use_logit:
        grouped['mean'] = inv_logit(grouped['mean'])
        grouped['ci_lower'] = inv_logit(grouped['ci_lower'])
        grouped['ci_upper'] = inv_logit(grouped['ci_upper'])

    # Create the plot
    fig, ax = plt.subplots(figsize=figsize)

    # Get unique player types and assign unified styles
    player_types = sort_player_types(df['player_type'].unique())
    player_styles = get_all_player_styles(player_types)

    # Plot each player type
    for player_type in player_types:
        player_data = grouped[grouped['player_type'] == player_type]
        style = player_styles[player_type]

        # Plot mean line with unified style
        ax.plot(player_data[x_var], player_data['mean'],
               label=player_type, color=style['color'],
               linestyle=style['linestyle'], linewidth=2.5,
               marker=style['marker'], markersize=4, markevery=10)

        # Add confidence interval as shaded area
        if show_confidence:
            ax.fill_between(player_data[x_var],
                          player_data['ci_lower'],
                          player_data['ci_upper'],
                          alpha=0.15, color=style['color'])

    # Customize plot
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title + (f' ({int(confidence_level*100)}% CI)' if show_confidence else ''),
                fontsize=14, fontweight='bold')

    # Set x-axis ticks
    turn_min = df[x_var].min()
    turn_max = df[x_var].max()
    ax.set_xticks(np.arange(turn_min, turn_max, turn_interval))
    ax.set_xlim(turn_min, turn_max)

    # Add grid
    ax.grid(True, alpha=0.3)

    # Create custom legend that shows line styles
    from matplotlib.lines import Line2D
    legend_elements = []

    # Add legend entries for each player type with their line style
    for player_type in player_types:
        style = player_styles[player_type]
        legend_elements.append(
            Line2D([0], [0],
                   color=style['color'],
                   linestyle=style['linestyle'],
                   linewidth=2.5,
                   marker=style['marker'],
                   markersize=6,
                   label=player_type)
        )

    # Add additional legend entries to explain line styles
    legend_elements.extend([
        Line2D([0], [0], color='none', label=''),  # Empty line for spacing
        Line2D([0], [0], color='black', linestyle='-', linewidth=2, label='— Simple'),
        Line2D([0], [0], color='black', linestyle='--', linewidth=2, label='-- Briefed'),
    ])

    ax.legend(handles=legend_elements, title='Player Type', loc=legend_loc)

    # Set y-axis limits if provided
    if ylim is not None:
        ax.set_ylim(ylim)

    # Invert y-axis if requested (useful for rank)
    if invert_y:
        ax.invert_yaxis()

    plt.tight_layout()
    _show()

    # Print summary statistics if requested
    if print_summary:
        # Statistics by player type as a single table
        import pandas as pd
        from IPython.display import display

        rows = []
        for player_type in player_types:
            pt_data = df[df['player_type'] == player_type]['metric_value']
            row = {
                'Player Type': player_type,
                'N': len(pt_data),
                'Mean': round(pt_data.mean(), 3),
                'Std': round(pt_data.std(), 3),
                'Min': round(pt_data.min(), 3),
                'Max': round(pt_data.max(), 3),
            }

            # Calculate trend (linear regression slope)
            pt_turn_data = df[df['player_type'] == player_type]
            if len(pt_turn_data) > 1:
                slope, intercept, r_value, p_value, std_err = stats.linregress(
                    pt_turn_data[x_var], pt_turn_data['metric_value']
                )
                row['Slope'] = round(slope, 6)
                row['r'] = round(r_value, 3)

            rows.append(row)

        if rows:
            summary_df = pd.DataFrame(rows).set_index('Player Type')
            summary_df.index.name = None
            display(summary_df)

    return fig, ax


def plot_score_ratio_over_time(turn_df, title="Score Ratio Over Time by Player Type",
                               xlabel="Turn", ylabel="Score Ratio (Score/Max Score)",
                               figsize=(12, 6), show_confidence=True, confidence_level=0.95,
                               turn_interval=10, max_turn=None, min_turn=None,
                               player_type_filter=None, print_summary=True):
    """
    Plot score ratio (score/max_score) over time for different player types with confidence intervals.

    This is a convenience wrapper around plot_metric_over_time specifically for score ratio.

    Args:
        turn_df: DataFrame with turn data (must contain 'turn', 'score', 'max_score', 'player_type')
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        figsize: Figure size tuple
        show_confidence: Whether to show 95% confidence intervals
        confidence_level: Confidence level for intervals (default 0.95)
        turn_interval: Interval for x-axis ticks (default 10)
        max_turn: Maximum turn to include (None = all)
        min_turn: Minimum turn to include (None = all)
        player_type_filter: List of player types to include (None = all)
        print_summary: Whether to print summary statistics

    Returns:
        Figure and axis objects
    """
    # Use the generalized function with score ratio calculation
    return plot_metric_over_time(
        turn_df=turn_df,
        metric_calculation=lambda df: df['score'] / df['max_score'],
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        figsize=figsize,
        show_confidence=show_confidence,
        confidence_level=confidence_level,
        turn_interval=turn_interval,
        max_turn=max_turn,
        min_turn=min_turn,
        player_type_filter=player_type_filter,
        print_summary=print_summary,
        ylim=(0, 1)  # Score ratio is always between 0 and 1
    )


def plot_token_scatter(df, x_col='survival_turn', y_col='input_tokens',
                       title=None, xlabel=None, ylabel=None,
                       add_trend_line=True, add_correlation=True,
                       figsize=(12, 8), point_size=30,
                       fit_degree=1, fit_by_player_type=True):
    """
    Create a scatter plot with tokens vs survival turn, colored by player_type.

    Args:
        df: DataFrame with token and survival data (must contain 'player_type' column)
        x_col: Column name for x-axis (default: 'survival_turn')
        y_col: Column name for y-axis (default: 'input_tokens')
        title: Plot title (auto-generated if None)
        xlabel: X-axis label (auto-generated if None)
        ylabel: Y-axis label (auto-generated if None)
        add_trend_line: Whether to add trend line(s)
        add_correlation: Whether to show correlation coefficient
        figsize: Figure size tuple
        point_size: Size of scatter points
        fit_degree: Degree of polynomial fit (1=linear, 2=quadratic, etc.)
        fit_by_player_type: If True, fit separately for each player type; if False, fit overall

    Returns:
        Figure and axis objects
    """
    fig, ax = plt.subplots(figsize=figsize)

    # Get unique player types and unified styles
    player_types = sort_player_types(df['player_type'].unique())
    player_styles = get_all_player_styles(player_types)

    # Plot scatter for each player type
    for player_type in player_types:
        player_data = df[df['player_type'] == player_type]
        style = player_styles[player_type]

        ax.scatter(player_data[x_col],
                  player_data[y_col],
                  alpha=style['alpha'],
                  s=point_size,
                  label=player_type,
                  color=style['color'],
                  marker=style['marker'],
                  edgecolors='black',
                  linewidth=0.5)

    # Add trend line(s) if requested
    if add_trend_line:
        if fit_by_player_type:
            # Fit separately for each player type
            for player_type in player_types:
                player_data = df[df['player_type'] == player_type]
                style = player_styles[player_type]

                if len(player_data) > fit_degree:  # Need enough points for the fit
                    # Fit polynomial
                    z = np.polyfit(player_data[x_col], player_data[y_col], fit_degree)
                    p = np.poly1d(z)

                    # Generate smooth curve for plotting
                    x_sorted = np.linspace(player_data[x_col].min(),
                                          player_data[x_col].max(), 100)
                    ax.plot(x_sorted, p(x_sorted),
                           linestyle="--", alpha=0.7, linewidth=2,
                           label=f'{player_type} trend',
                           color=style['color'])
        else:
            # Single overall trend line
            z = np.polyfit(df[x_col], df[y_col], fit_degree)
            p = np.poly1d(z)
            x_sorted = np.linspace(df[x_col].min(), df[x_col].max(), 100)
            ax.plot(x_sorted, p(x_sorted),
                   linestyle="--", color='red', alpha=0.8, linewidth=2,
                   label=f'Overall Trend (deg={fit_degree})')

    # Set labels
    if xlabel is None:
        xlabel = x_col.replace('_', ' ').title()
    if ylabel is None:
        ylabel = y_col.replace('_', ' ').title()
    if title is None:
        title = f'Relationship between {xlabel} and {ylabel}'

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Create custom legend that shows marker styles
    from matplotlib.lines import Line2D
    legend_elements = []

    # Add legend entries for each player type with their marker style
    for player_type in player_types:
        style = player_styles[player_type]
        legend_elements.append(
            Line2D([0], [0],
                   color=style['color'],
                   marker=style['marker'],
                   linestyle='None',
                   markersize=8,
                   markeredgecolor='black',
                   markeredgewidth=0.5,
                   alpha=style['alpha'],
                   label=player_type)
        )

    # Add additional legend entries to explain marker styles
    legend_elements.extend([
        Line2D([0], [0], color='none', label=''),  # Empty line for spacing
        Line2D([0], [0], color='gray', marker='o', linestyle='None', markersize=8, label='○ Simple'),
        Line2D([0], [0], color='gray', marker='s', linestyle='None', markersize=8, label='□ Briefed'),
    ])

    ax.legend(handles=legend_elements, title='Player Type', loc='best')
    ax.grid(True, alpha=0.3)

    # Add correlation coefficient if requested
    if add_correlation:
        if fit_by_player_type:
            # Show correlation for each player type in a text box
            corr_text = "Correlations:\n"
            for player_type in player_types:
                player_data = df[df['player_type'] == player_type]
                corr = player_data[x_col].corr(player_data[y_col])
                corr_text += f"{player_type}: {corr:.3f}\n"
            ax.text(0.02, 0.98, corr_text.strip(),
                   transform=ax.transAxes,
                   verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        else:
            correlation = df[x_col].corr(df[y_col])
            ax.text(0.02, 0.98, f'Overall Correlation: {correlation:.3f}',
                   transform=ax.transAxes,
                   verticalalignment='top',
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()

    # Print correlation and fit information by player type
    print(f"\nCorrelation between {x_col} and {y_col} by player type:")
    for player_type in player_types:
        player_data = df[df['player_type'] == player_type]
        corr = player_data[x_col].corr(player_data[y_col])
        print(f"  {player_type}: {corr:.3f}")

    if add_trend_line and fit_degree > 1:
        print(f"\nPolynomial fit degree: {fit_degree}")

    _show()
    return fig, ax


def plot_violin(
    data, y, x='player_type', facet=None,
    title='', ylabel='', xlabel='',
    hline=None,
    annotate_n=True, annotations=None,
    annotation_fmt='{:.1f}', annotation_pos='below',
    figsize=None, sharey=True,
    n_cols=4, ylim=None,
    order=None, palette=None, strip=False,
):
    """Create violin plots, optionally faceted by a categorical column.

    Parameters
    ----------
    data : DataFrame
        Source data (rows with NaN in ``y`` or ``x`` are dropped automatically).
    y : str
        Column for the y-axis (continuous variable).
    x : str
        Column for the x-axis categories (default ``'player_type'``).
    facet : str or None
        Column to facet by (one subplot per unique value). ``None`` = single plot.
    title : str
        Figure suptitle (single plot) or suptitle (faceted).
    ylabel, xlabel : str
        Axis labels.
    hline : float or None
        Draw a horizontal reference line at this y-value.
    annotate_n : bool
        Show ``n=X`` below each violin (default True).
    annotations : dict or Series or None
        Per-x-category text placed near each violin.  Keyed by x-category value.
        Values are formatted with *annotation_fmt* (must be numeric).
    annotation_fmt : str
        Format string for *annotations* values (e.g. ``'{:.1f}/game'``).
    annotation_pos : ``'below'`` | ``'above'``
        Where to place *annotations* text relative to the violin.
    figsize : tuple or None
        Figure size; auto-calculated if ``None``.
    sharey : bool
        Share y-axis across faceted subplots.
    n_cols : int
        Max columns in faceted grid.
    ylim : tuple or None
        Y-axis limits.
    order : list or None
        Explicit x-axis category order. If None, auto-detected from data.
    palette : dict or None
        Explicit color palette ``{category: color}``. If None, auto-generated
        for ``player_type`` or left to seaborn defaults.
    strip : bool
        If True, overlay a stripplot showing individual data points.

    Returns
    -------
    fig, axes
    """
    plot_data = data.dropna(subset=[y, x]).copy()

    # Determine x-order and palette
    if order is not None:
        x_order = order
    elif x == 'player_type':
        x_order = sort_player_types(plot_data[x].unique())
    else:
        x_order = sorted(plot_data[x].unique())

    if palette is None and x == 'player_type':
        palette = {v: get_player_color(v) for v in x_order}

    facet_values = sorted(plot_data[facet].dropna().unique()) if facet else [None]
    n_facets = len(facet_values)

    if n_facets == 1 and facet is None:
        # Single plot
        if figsize is None:
            figsize = (max(14, len(x_order) * 0.9), 6)
        fig, ax = plt.subplots(figsize=figsize)
        axes_flat = [ax]
    else:
        n_rows = int(np.ceil(n_facets / n_cols))
        actual_cols = min(n_facets, n_cols)
        if figsize is None:
            figsize = (4 * actual_cols, 3.5 * n_rows)
        fig, axes = plt.subplots(n_rows, actual_cols, figsize=figsize, sharey=sharey)
        axes_flat = axes.flatten() if n_facets > 1 else [axes]

    for idx, fval in enumerate(facet_values):
        ax = axes_flat[idx]
        subset = plot_data[plot_data[facet] == fval] if facet else plot_data

        sns.violinplot(
            data=subset, x=x, y=y,
            order=x_order, cut=0, inner='quartile',
            palette=palette, ax=ax, linewidth=0.8,
        )

        if strip:
            sns.stripplot(
                data=subset, x=x, y=y,
                order=x_order, palette=palette,
                size=2, alpha=0.3, jitter=0.25, ax=ax,
                zorder=0,
            )

        if hline is not None:
            ax.axhline(y=hline, color='gray', linestyle=':', alpha=0.5, linewidth=0.8)

        # n= annotations below each violin
        if annotate_n:
            y_pos = (ylim[0] + 0.03) if ylim else ax.get_ylim()[0]
            for i, cat in enumerate(x_order):
                n = (subset[x] == cat).sum()
                if n > 0:
                    ax.text(i, y_pos, f'n={n}', ha='center', va='top', fontsize=7, color='gray')

        # Custom annotations (e.g. avg pivots per game)
        if annotations is not None:
            for i, cat in enumerate(x_order):
                val = annotations.get(cat, None) if hasattr(annotations, 'get') else None
                if val is not None:
                    y_ann = (ylim[1] - 0.02) if ylim else ax.get_ylim()[1]
                    va = 'bottom' if annotation_pos == 'above' else 'top'
                    ax.text(i, y_ann, annotation_fmt.format(val),
                            ha='center', va=va, fontsize=8, fontweight='bold')

        if facet:
            ax.set_title(fval, fontsize=12, fontweight='bold')
        ax.set_xlabel('')
        if idx % (min(n_facets, n_cols)) == 0:
            ax.set_ylabel(ylabel, fontsize=11)
        else:
            ax.set_ylabel('')
        if ylim:
            ax.set_ylim(ylim)
        ax.tick_params(axis='x', rotation=45)
        for label in ax.get_xticklabels():
            label.set_ha('right')

    # Hide unused subplots
    for idx in range(n_facets, len(axes_flat)):
        axes_flat[idx].set_visible(False)

    if title:
        if n_facets == 1 and facet is None:
            axes_flat[0].set_title(title, fontsize=14, fontweight='bold')
        else:
            fig.suptitle(title, fontsize=14, fontweight='bold', y=1.02)

    if xlabel:
        fig.supxlabel(xlabel, fontsize=11)

    plt.tight_layout()
    _show()
    return fig, axes_flat


# ---------------------------------------------------------------------------
# Model palette helper
# ---------------------------------------------------------------------------

def get_model_palette(model_names):
    """Build a ``{name: color}`` dict from the canonical model catalog.

    Each *model_name* is looked up (case-insensitive) via
    :func:`shared.model_catalog.get_strategist_model`.  Unknown names get
    a neutral gray fallback.
    """
    from shared.model_catalog import get_strategist_model

    palette = {}
    for name in model_names:
        model = get_strategist_model(name)
        palette[name] = model["color"] if model else "#888888"
    return palette


# ---------------------------------------------------------------------------
# Agreement scatter (predicted vs actual, faceted)
# ---------------------------------------------------------------------------

def plot_agreement_scatter(
    data, x_col, y_col, facet_col,
    title='', xlabel='', ylabel='',
    figsize=None, n_cols=4, alpha=0.35, s=18,
):
    """Faceted scatter with a diagonal reference line and r² per panel.

    Parameters
    ----------
    data : DataFrame
    x_col, y_col : str
        Columns for x and y axes.
    facet_col : str
        Column whose unique values define the subplot panels.
    title, xlabel, ylabel : str
    figsize : tuple or None
    n_cols : int
        Max columns in the grid.
    alpha, s : float
        Scatter point transparency and size.

    Returns
    -------
    fig, axes
    """
    plot_data = data.dropna(subset=[x_col, y_col, facet_col]).copy()
    facet_values = sorted(plot_data[facet_col].unique())
    n_facets = len(facet_values)

    actual_cols = min(n_facets, n_cols)
    n_rows = int(np.ceil(n_facets / actual_cols))
    if figsize is None:
        figsize = (5 * actual_cols, 4.5 * n_rows)

    fig, axes = plt.subplots(n_rows, actual_cols, figsize=figsize, squeeze=False)
    axes_flat = axes.flatten()

    palette = get_model_palette(facet_values)

    # Shared axis limits
    lo = min(plot_data[x_col].min(), plot_data[y_col].min())
    hi = max(plot_data[x_col].max(), plot_data[y_col].max())
    margin = (hi - lo) * 0.05
    lims = (lo - margin, hi + margin)

    for idx, fval in enumerate(facet_values):
        ax = axes_flat[idx]
        subset = plot_data[plot_data[facet_col] == fval]
        color = palette.get(fval, "#888888")

        ax.scatter(subset[x_col], subset[y_col],
                   alpha=alpha, s=s, color=color, edgecolors='none')
        ax.plot(lims, lims, ls='--', color='gray', lw=0.8, alpha=0.6)
        ax.set_xlim(lims)
        ax.set_ylim(lims)
        ax.set_aspect('equal', adjustable='box')

        # r²
        valid = subset[[x_col, y_col]].dropna()
        if len(valid) > 2:
            r = valid[x_col].corr(valid[y_col])
            ax.text(0.05, 0.95, f'r² = {r**2:.2f}',
                    transform=ax.transAxes, fontsize=9,
                    va='top', ha='left',
                    bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.7))

        ax.set_title(fval, fontsize=11, fontweight='bold')
        ax.set_xlabel(xlabel if idx >= (n_rows - 1) * actual_cols else '', fontsize=10)
        ax.set_ylabel(ylabel if idx % actual_cols == 0 else '', fontsize=10)

    for idx in range(n_facets, len(axes_flat)):
        axes_flat[idx].set_visible(False)

    if title:
        fig.suptitle(title, fontsize=13, fontweight='bold', y=1.02)
    plt.tight_layout()
    _show()
    return fig, axes_flat


# ---------------------------------------------------------------------------
# Shared replay-grid layout
# ---------------------------------------------------------------------------

_REPLAY_METRIC_MAP = {
    'replay_use_nuke': {'before': 'prev_use_nuke', 'episode': 'after_use_nuke'},
    'replay_nuke':     {'before': 'prev_nuke',     'episode': 'after_nuke'},
}


def _replay_grid_layout(df, delta=True, model_order=None, condition_order=None):
    """Canonical (row_labels, col_labels) for replay model x condition grids.

    Mirrors ``plot_replay_heatmap`` layout: rows = reference rows + models,
    columns = conditions.
    """
    if model_order is None:
        model_order = sorted(df['replay_model_canonical'].dropna().unique())
    if condition_order is None:
        cond_col = df['condition'].dropna()
        if hasattr(cond_col, 'cat') and cond_col.cat.ordered:
            condition_order = [c for c in cond_col.cat.categories if c in cond_col.values]
        else:
            condition_order = sorted(cond_col.unique())

    if delta:
        row_labels = ['[Episode]'] + list(model_order)
    else:
        row_labels = ['[Before]', '[Episode]'] + list(model_order)

    return row_labels, list(condition_order)


# ---------------------------------------------------------------------------
# Small-multiples histogram grid (model x condition)
# ---------------------------------------------------------------------------

def plot_replay_delta_grid(
    df, metric='replay_use_nuke',
    delta=True,
    model_order=None, condition_order=None,
    palette=None,
    title=None,
    figsize=None, ylim=None,
    episode_scalar=3,
):
    """Small-multiples histogram grid matching ``plot_replay_heatmap`` layout.

    Each cell shows the raw per-retry delta distribution (no averaging).
    Rows = ``[Episode]`` reference + replay models;  columns = conditions.

    Parameters
    ----------
    df : DataFrame
        Raw replay data from ``load_replay_data()``.
    metric : ``'replay_use_nuke'`` or ``'replay_nuke'``
        Which metric to compute deltas for.
    delta : bool
        If True (default), rows start with ``[Episode]``; if False,
        ``[Before]`` then ``[Episode]`` -- same as the heatmap.
    model_order, condition_order : list or None
        Explicit ordering; auto-sorted if None.
    palette : dict or None
        ``{model_name: color}`` for histogram bars. Falls back to gray.
    title : str or None
        Figure suptitle (auto-generated if None).
    figsize : tuple or None
        Figure size; auto-calculated if None.
    ylim : tuple or None
        Shared y-axis (count) limits. Auto-calculated if None.

    Returns
    -------
    fig, axes : 2-D ndarray of Axes
    """
    import matplotlib.pyplot as plt
    import numpy as np

    if metric not in _REPLAY_METRIC_MAP:
        raise ValueError(f"metric must be one of {list(_REPLAY_METRIC_MAP)}")

    before_col = _REPLAY_METRIC_MAP[metric]['before']
    episode_col = _REPLAY_METRIC_MAP[metric]['episode']
    delta_col = f'{metric}_delta'

    if delta_col not in df.columns:
        df = df.copy()
        df[delta_col] = df[metric] - df[before_col]

    row_labels, col_labels = _replay_grid_layout(
        df, delta=delta, model_order=model_order, condition_order=condition_order,
    )
    n_rows = len(row_labels)
    n_cols = len(col_labels)

    if figsize is None:
        figsize = (2.4 * n_cols, 1.8 * n_rows)

    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize, sharex=True, sharey=True)
    if n_rows == 1:
        axes = axes[np.newaxis, :]
    if n_cols == 1:
        axes = axes[:, np.newaxis]

    # Fixed semantic bins: <-10 | -10…-1 | 0 | 1…10 | >10
    _bin_edges = [-np.inf, -10.5, -0.5, 0.5, 10.5, np.inf]
    _bin_labels = ['<-10', '-10…-1', '0', '1…10', '>10']
    _n_bars = len(_bin_labels)

    def _draw_cell(ax, values, color, count_scalar=1):
        """Render one bar-chart cell with counts per bin."""
        if len(values) == 0:
            ax.text(0.5, 0.5, 'n/a', transform=ax.transAxes,
                    ha='center', va='center', fontsize=8, color='gray')
            return
        counts = np.histogram(values, bins=_bin_edges)[0] * count_scalar
        pcts = counts / counts.sum() * 100
        x_pos = np.arange(_n_bars)
        ax.bar(x_pos, pcts, color=color, alpha=0.75,
               edgecolor='white', linewidth=0.3)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(_bin_labels, fontsize=8, rotation=45)
        med = np.nanmedian(values)
        mean = np.nanmean(values)
        ax.text(0.97, 0.93, f'n={len(values)}\nmed={med:+.0f}\navg={mean:+.1f}',
                transform=ax.transAxes, fontsize=8, va='top', ha='right', color='#333')

    for i, row_label in enumerate(row_labels):
        for j, cond in enumerate(col_labels):
            ax = axes[i, j]
            cond_mask = df['condition'] == cond

            if row_label == '[Episode]':
                ep_df = df.loc[cond_mask].drop_duplicates(subset=['game_id', 'player_id'])
                vals = (ep_df[episode_col] - ep_df[before_col]).dropna().values
                color = '#aaaaaa'
                scalar = episode_scalar
            elif row_label == '[Before]':
                vals = np.zeros(int(cond_mask.sum()))
                color = '#cccccc'
                scalar = 1
            else:
                vals = df.loc[
                    cond_mask & (df['replay_model_canonical'] == row_label), delta_col
                ].dropna().values
                color = (palette or {}).get(row_label, '#888888')
                scalar = 1

            _draw_cell(ax, vals, color, count_scalar=scalar)

            if i == 0:
                ax.set_title(cond, fontsize=8, fontweight='bold')
            if j == 0:
                ax.set_ylabel(row_label, fontsize=8, fontweight='bold')
            ax.tick_params(axis='y', labelsize=6)

    if ylim is not None:
        for ax_row in axes:
            for ax in ax_row:
                ax.set_ylim(ylim)

    metric_label = metric.replace('_', ' ')
    if title is None:
        title = f'Per-Retry Δ {metric_label} Distribution'
    fig.suptitle(title, fontsize=12, fontweight='bold', y=1.02)
    fig.supxlabel(f'Δ {metric_label} (replay − before)', fontsize=9)
    fig.supylabel('% of retries', fontsize=9)
    plt.tight_layout()
    _show()
    return fig, axes


# ---------------------------------------------------------------------------
# Direction heatmap: decrease / same / increase per (model x condition)
# ---------------------------------------------------------------------------

def plot_replay_direction_heatmap(
    df, metric='replay_use_nuke',
    compare_to=None,
    model_order=None, condition_order=None,
    presence_cols=None, presence_labels=None,
    grand_average_col=False,
    title=None, figsize=None,
    cmap='RdBu_r', footnote=None,
):
    """Annotated heatmap showing decrease / same / increase rates.

    Each retry is classified by whether the replay model chose a lower, same,
    or higher value compared to a baseline column.

    The cell background color encodes net direction = increase% - decrease%,
    centered at 0 with a diverging colormap.  Annotations show all three
    percentages plus sample count.

    By default, columns are replay conditions.  When ``presence_cols`` is
    provided, columns are tag/presence indicators and each cell only includes
    rows where that presence column equals 1.

    Parameters
    ----------
    df : DataFrame
        Raw replay data from ``load_replay_data()``.
    metric : ``'replay_use_nuke'`` or ``'replay_nuke'``
        Which replay column to classify.
    compare_to : str or None
        Baseline column name to compare against (e.g. ``'prev_use_nuke'``,
        ``'after_use_nuke'``).  Defaults to the "before" column from
        ``_REPLAY_METRIC_MAP`` when None.
    model_order : list or None
        Row ordering of models.  Auto-sorted if None.
    condition_order : list or None
        Column ordering of conditions.  Auto-sorted if None (respects
        categorical ordering when present). Ignored when ``presence_cols`` is
        provided.
    presence_cols : list or None
        Optional indicator columns to use as heatmap columns.  Each column
        filters to rows where that indicator equals 1.
    presence_labels : list or None
        Optional display labels for ``presence_cols``.  Defaults to column
        names.
    grand_average_col : bool
        If True, prepend a ``'Grand avg'`` column.  In condition mode this
        includes all rows; in presence mode this includes rows with any
        provided presence column covered (non-null).
    title : str or None
        Figure suptitle (auto-generated if None).
    figsize : tuple or None
        Figure size; auto-calculated if None.
    cmap : str
        Diverging colormap for net direction.  Default ``'RdBu_r'``.
    footnote : str or None
        Optional footnote text (auto-generated if None).

    Returns
    -------
    fig, ax
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import pandas as pd

    if metric not in _REPLAY_METRIC_MAP:
        raise ValueError(f"metric must be one of {list(_REPLAY_METRIC_MAP)}")

    if compare_to is None:
        compare_to = _REPLAY_METRIC_MAP[metric]['before']

    work = df.copy()
    work['_direction_delta'] = work[metric] - work[compare_to]

    # Classify each row: decrease / same / increase
    work['_direction'] = pd.cut(
        work['_direction_delta'],
        bins=[-np.inf, -0.5, 0.5, np.inf],
        labels=['decrease', 'same', 'increase'],
    )

    # Resolve row ordering
    if model_order is None:
        model_order = sorted(work['replay_model_canonical'].dropna().unique())

    # Resolve column groups.  Default behavior remains model x condition; the
    # optional presence mode reuses the same direction heatmap machinery for
    # tag-conditioned subsets.
    if presence_cols is None:
        if condition_order is None:
            cond_col = work['condition'].dropna()
            if hasattr(cond_col, 'cat') and cond_col.cat.ordered:
                condition_order = [c for c in cond_col.cat.categories if c in cond_col.values]
            else:
                condition_order = sorted(cond_col.unique())
        col_labels = list(condition_order)
        col_masks = [work['condition'] == cond for cond in col_labels]
        x_axis_label = 'Condition'
        split_x_labels = True
    else:
        presence_cols = list(presence_cols)
        missing_cols = [col for col in presence_cols if col not in work.columns]
        if missing_cols:
            raise ValueError(f"presence_cols not found in df: {missing_cols}")

        if presence_labels is None:
            presence_labels = presence_cols
        else:
            presence_labels = list(presence_labels)
            if len(presence_labels) != len(presence_cols):
                raise ValueError("presence_labels must have the same length as presence_cols")

        col_labels = list(presence_labels)
        col_masks = [work[col] == 1 for col in presence_cols]
        if grand_average_col:
            coverage_mask = work[presence_cols].notna().any(axis=1)
            col_labels = ['Grand avg'] + col_labels
            col_masks = [coverage_mask] + col_masks
        x_axis_label = 'Tag'
        split_x_labels = False

    if grand_average_col and presence_cols is None:
        col_labels = ['Grand avg'] + col_labels
        col_masks = [pd.Series(True, index=work.index)] + col_masks

    row_labels = list(model_order) + ['All Models']
    n_rows = len(row_labels)
    n_cols = len(col_labels)

    # Build matrices
    net_direction = np.full((n_rows, n_cols), np.nan)
    annot_array = np.empty((n_rows, n_cols), dtype=object)

    for i, model_label in enumerate(row_labels):
        for j, col_mask in enumerate(col_masks):
            if model_label == 'All Models':
                cell = work.loc[col_mask, '_direction'].dropna()
            else:
                cell = work.loc[
                    col_mask & (work['replay_model_canonical'] == model_label),
                    '_direction',
                ].dropna()

            n = len(cell)
            if n == 0:
                annot_array[i, j] = 'n/a'
                continue

            vc = cell.value_counts(normalize=True) * 100
            d = vc.get('decrease', 0.0)
            s = vc.get('same', 0.0)
            inc = vc.get('increase', 0.0)
            net_direction[i, j] = inc - d
            annot_array[i, j] = f'\u2193{d:.0f}%  ={s:.0f}%  \u2191{inc:.0f}%\nn={n}'

    # Create heatmap
    if figsize is None:
        figsize = (max(14, 1.8 * n_cols), max(8, 0.7 * n_rows))

    net_df = pd.DataFrame(net_direction, index=row_labels, columns=col_labels)
    finite_direction = net_direction[np.isfinite(net_direction)]
    abs_max = max(np.nanmax(np.abs(finite_direction)), 1.0) if finite_direction.size else 1.0

    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        net_df,
        annot=annot_array, fmt='',
        cmap=cmap, center=0, vmin=-abs_max, vmax=abs_max,
        linewidths=0.5, linecolor='white',
        ax=ax,
        cbar_kws={'label': 'Net direction (\u2191% \u2212 \u2193%)'},
        annot_kws={'fontsize': 9, 'fontfamily': 'monospace'},
    )

    # Separator line above "All Models"
    ax.hlines(y=n_rows - 1, xmin=0, xmax=n_cols,
              colors='black', linewidths=2, clip_on=False)
    ytick_labels = ax.get_yticklabels()
    for label in ytick_labels:
        if label.get_text() == 'All Models':
            label.set_fontweight('bold')
    ax.set_yticklabels(ytick_labels, rotation=0)

    # Split long condition names across two lines
    def _split_condition(lbl):
        lbl = str(lbl)
        parts = lbl.split('-')
        if len(parts) <= 1:
            return lbl
        candidates = []
        for k in range(1, len(parts)):
            left = '-'.join(parts[:k])
            right = '-'.join(parts[k:])
            candidates.append((max(len(left), len(right)),
                               abs(len(left) - len(right)), left, right))
        _, _, left, right = min(candidates)
        return f'{left}\n{right}'

    ax.set_xticks(np.arange(n_cols) + 0.5)
    x_tick_labels = (
        [_split_condition(c) for c in col_labels]
        if split_x_labels
        else [str(c) for c in col_labels]
    )
    ax.set_xticklabels(
        x_tick_labels,
        rotation=45, ha='right', va='top',
    )
    ax.tick_params(axis='x', labelsize=11, pad=6)
    ax.tick_params(axis='y', labelsize=11)

    # Title and footnote
    metric_label = metric.replace('_', ' ')
    if title is None:
        if presence_cols is None:
            title = f'Replay Direction: {metric_label} (vs {compare_to})'
        else:
            title = f'Replay Direction by Presence: {metric_label} (vs {compare_to})'
    ax.set_title(title, fontsize=15, fontweight='bold', pad=12)
    ax.set_xlabel(x_axis_label, fontsize=13)
    ax.set_ylabel('Model', fontsize=13)

    if footnote is None:
        if presence_cols is None:
            footnote = (
                f'Each retry classified by {metric} \u2212 {compare_to}: '
                f'\u2193 = lower, = = same, \u2191 = higher. '
                f'Cell color = net direction (\u2191% \u2212 \u2193%), centered at 0.'
            )
        else:
            footnote = (
                f'Each retry with the column tag present is classified by {metric} \u2212 {compare_to}: '
                f'\u2193 = lower, = = same, \u2191 = higher. '
                f'Cell color = net direction (\u2191% \u2212 \u2193%), centered at 0.'
            )
    if footnote:
        plt.tight_layout(rect=[0, 0.05, 1, 1])
        fig.text(0.02, 0.005, footnote, fontsize=9, style='italic',
                 color='#555555', wrap=True)
    else:
        plt.tight_layout()

    _show()
    return fig, ax
