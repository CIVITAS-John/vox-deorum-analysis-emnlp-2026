"""Per-strategy ELO ratings using composite player identities.

Relabels each player as {PlayerType}-{Strategy} based on their dominant strategy,
then runs a single Bradley-Terry model on the full dataset. Every pairwise comparison
is preserved; each composite identity is rated against the full field.
"""

import pandas as pd
import numpy as np
from scipy.stats import norm
from .bradley_terry import calculate_ratings


STRATEGY_COLS = ['domination_ratio', 'culture_ratio', 'diplomatic_ratio', 'science_ratio']
STRATEGY_LABELS = {c: c.replace('_ratio', '').title() for c in STRATEGY_COLS}


def calculate_strategy_ratings(panel_df, min_games=5, verbose=True):
    """
    Calculate per-strategy ELO ratings via composite player identities.

    For each player-game row, determines the dominant strategy (argmax of the
    four strategy ratio columns) and creates a composite player_type like
    'Kimi-K2.5-Briefed-Science'. Runs a single Bradley-Terry model on the full
    dataset with these composite types, then splits results back into player_type
    and strategy columns. Low-count composites are dropped post-fit.

    Args:
        panel_df: DataFrame with columns: game_id, player_id, player_type,
                  adjusted_strength, civilization, and the four strategy ratio columns.
        min_games: Minimum games for a composite type to appear in output.
        verbose: Print progress and results.

    Returns:
        DataFrame with columns: player_type, strategy, composite_type, elo, se_elo,
        worth, log_worth, se_log_worth, z_value, p_value, n_games, mu, sigma.
        After re-centering, z_value/p_value test against the displayed null of
        log_worth = 0 (equivalently Elo = 1500, the average Vanilla baseline).
    """
    df = panel_df.copy()

    # Determine dominant strategy per row
    ratios = df[STRATEGY_COLS]
    df['dominant_strategy'] = ratios.idxmax(axis=1).map(STRATEGY_LABELS)

    # Build composite type
    df['composite_type'] = df['player_type'] + '-' + df['dominant_strategy']

    # Count games per composite type (for post-fit filtering)
    game_counts = df.groupby('composite_type')['game_id'].nunique()

    if verbose:
        print(f"Composite types: {len(game_counts)}")
        print(f"Will drop post-fit: {(game_counts < min_games).sum()} types with <{min_games} games")

    # Replace player_type with composite for BT fitting
    bt_input = df[['game_id', 'player_id', 'composite_type', 'adjusted_strength', 'civilization']].copy()
    bt_input = bt_input.rename(columns={'composite_type': 'player_type'})

    # Use the most common Vanilla composite as reference level
    vanilla_composites = game_counts[game_counts.index.str.startswith('Vanilla-')]
    reference = vanilla_composites.idxmax() if len(vanilla_composites) > 0 else None

    # Run BT on full dataset
    results = calculate_ratings(bt_input, reference=reference, verbose=verbose)

    # Split composite type back into player_type and strategy
    results = results.rename(columns={'player_type': 'composite_type'})
    split = results['composite_type'].str.rsplit('-', n=1, expand=True)
    results['player_type'] = split[0]
    results['strategy'] = split[1]

    # Attach game counts
    results['n_games'] = results['composite_type'].map(game_counts)

    # Re-center so average Vanilla ELO = 1500
    vanilla_mask = results['player_type'] == 'Vanilla'
    if vanilla_mask.any():
        vanilla_mean_elo = results.loc[vanilla_mask, 'elo'].mean()
        shift = 1500 - vanilla_mean_elo
        results['elo'] += shift
        # Recompute displayed scores on the re-centered scale.
        results['log_worth'] = (results['elo'] - 1500) / 400 * np.log(10)
        results['worth'] = np.exp(results['log_worth'])
        results['mu'] = results['log_worth']
        # SEs do not change under a constant shift, but significance does.
        positive_se = results['se_log_worth'] > 0
        results['z_value'] = np.where(
            positive_se,
            results['log_worth'] / results['se_log_worth'],
            np.nan,
        )
        results['p_value'] = np.where(
            positive_se,
            2 * norm.sf(np.abs(results['z_value'])),
            np.nan,
        )
        if verbose:
            print(f"\nRe-centered: Vanilla avg ELO = 1500 (shift = {shift:+.0f})")

    # Drop low-count composites (post-fit)
    before = len(results)
    results = results[results['n_games'] >= min_games].copy()
    if verbose and len(results) < before:
        print(f"Dropped {before - len(results)} composite types with <{min_games} games")

    # Reorder columns
    col_order = ['player_type', 'strategy', 'composite_type', 'n_games',
                 'elo', 'se_elo', 'worth', 'log_worth', 'se_log_worth',
                 'z_value', 'p_value', 'mu', 'sigma']
    results = results[[c for c in col_order if c in results.columns]]
    results = results.sort_values(['strategy', 'elo'], ascending=[True, False])

    return results.reset_index(drop=True)
