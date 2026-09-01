#!/usr/bin/env python3
"""
Ablation Bradley-Terry ratings: for each player type, keep all other games
constant and progressively add that type's games one-by-one (chronologically).
This isolates the marginal contribution of each game for a given player type.

Outputs a CSV dataset and per-target-type Elo convergence charts.

Usage:
    python -m ratings.iterative_bt [--no-cache] [--output-dir DIR]
    python -m ratings.iterative_bt --targets Sonnet-4.5-Simple
"""

import sys
import os
import argparse
import hashlib
import pickle
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Add analysis root so "from ratings ..." and "from shared.plot_utilities ..." resolve
_ANALYSIS_ROOT = str(Path(__file__).resolve().parent.parent)
if _ANALYSIS_ROOT not in sys.path:
    sys.path.insert(0, _ANALYSIS_ROOT)

from ratings import calculate_ratings_bt
from shared.plot_utilities import (
    load_turn_data,
    filter_non_llm_games,
    get_player_color,
    get_player_linestyle,
)


# ---------------------------------------------------------------------------
# Data preprocessing (reproduces the turn_predicted.ipynb pipeline)
# ---------------------------------------------------------------------------

def prepare_strength_data(turn_data_path='models/output/attention_mlp_predictions.csv',
                          enforce_winner_relative_strength=True,
                          ols_civilization=True,
                          verbose=True):
    """
    Compute per-player strength from model predictions.

    Pipeline: weighted avg (late-game) → relative to game leader →
    optional winner adjustment → OLS civilization effects → civ-adjusted strength →
    filter to LLM experiments only.

    Args:
        turn_data_path: Path to predictions CSV with predicted_win_probability column
        enforce_winner_relative_strength: If True, force winners with
            relative_strength < 1.0 up to 1.0 before OLS adjustment
        ols_civilization: If True, fit OLS to estimate civilization effects
            and subtract them (in logit space) to produce adjusted_strength.
            If False, adjusted_strength = relative_strength (no civ correction).
        verbose: Print progress

    Returns:
        Tuple of (strength_df, civ_effects, ols_model):
        - strength_df: DataFrame with adjusted_strength per player per game
        - civ_effects: dict mapping civilization name → OLS coefficient
        - ols_model: fitted statsmodels OLS result (for downstream analysis)
    """
    if verbose:
        print("Loading turn data...")
    turn_df = load_turn_data(turn_data_path, condition_exclude=[], print_metadata=False)
    if verbose:
        print(f"  {len(turn_df)} rows, {turn_df['game_id'].nunique()} games")

    # Step 1: Compute weighted_strength per player per game
    if verbose:
        print("Computing weighted strength per player...")
    filtered = turn_df[turn_df['turn_progress'] > 0.2].copy()
    turn_progress_avg = filtered.groupby(
        ['game_id', 'player_id', 'turn_progress']
    ).agg({
        'predicted_win_probability': 'mean',
        'player_type': 'first',
        'experiment': 'first',
        'is_winner': 'last',
        'civilization': 'first',
    }).reset_index()
    turn_progress_avg['weight'] = turn_progress_avg['turn_progress']

    records = []
    for (game_id, player_id), grp in turn_progress_avg.groupby(['game_id', 'player_id']):
        w = grp['weight']
        p = grp['predicted_win_probability']
        weighted_avg = (w * p).sum() / w.sum()
        records.append({
            'game_id': game_id,
            'player_id': player_id,
            'player_type': grp['player_type'].iloc[0],
            'civilization': grp['civilization'].iloc[0],
            'experiment': grp['experiment'].iloc[0],
            'weighted_strength': weighted_avg,
            'is_winner': grp['is_winner'].iloc[-1],
        })

    strength_df = pd.DataFrame(records)

    # Step 2: Relative strength
    game_max = strength_df.groupby('game_id')['weighted_strength'].max().reset_index()
    game_max.columns = ['game_id', 'max_weighted_strength']
    strength_df = strength_df.merge(game_max, on='game_id')
    strength_df['relative_strength'] = (
        strength_df['weighted_strength'] / strength_df['max_weighted_strength']
    )

    # Step 3: Optionally adjust winners (winners should have relative_strength = 1.0)
    winner_mask = (strength_df['is_winner'] == 1) & (strength_df['relative_strength'] < 1.0)
    enforced_games = strength_df.loc[winner_mask, 'game_id'].nunique()
    total_games = strength_df['game_id'].nunique()
    enforced_share = enforced_games / total_games if total_games else 0.0
    avg_relative_strength_change = (
        (1.0 - strength_df.loc[winner_mask, 'relative_strength']).mean()
        if winner_mask.any() else 0.0
    )
    if enforce_winner_relative_strength:
        if verbose:
            print(
                f"Enforced winner relative_strength=1.0 in "
                f"{enforced_games}/{total_games} games ({enforced_share:.1%}); "
                f"avg relative_strength change = {avg_relative_strength_change:.4f}"
            )
        strength_df.loc[winner_mask, 'weighted_strength'] = (
            strength_df.loc[winner_mask, 'max_weighted_strength'] + 0.001
        )
        strength_df.loc[winner_mask, 'relative_strength'] = 1.0
    elif verbose:
        print(
            f"Winner relative_strength enforcement disabled; "
            f"would affect {enforced_games}/{total_games} games ({enforced_share:.1%}); "
            f"avg relative_strength change = {avg_relative_strength_change:.4f}"
        )

    # Step 4–5: OLS for civilization effects on logit scale
    # (fitted on ALL data before filtering)
    # Using logit scale so civ effects are proportional: a strong civ helps
    # a strong player more than a weak one, and outputs stay in (0, 1).
    if ols_civilization:
        if verbose:
            print("Fitting OLS for civilization effects (logit scale)...")
        from statsmodels.formula.api import ols
        from shared.plot_utilities import logit, inv_logit

        strength_df['logit_strength'] = logit(strength_df['relative_strength'])
        formula = 'logit_strength ~ C(civilization, Sum) + C(player_type, Treatment(reference="Vanilla"))'
        ols_model = ols(formula, data=strength_df).fit()

        params = ols_model.params
        civ_vars = [col for col in params.index if 'civilization' in col]
        civ_effects = {}
        for var in civ_vars:
            civ_name = var.split('[S.')[-1].rstrip(']')
            civ_effects[civ_name] = params[var]
        # Reference category (Sum coding: all effects sum to zero)
        civ_effects['Venice'] = -sum(civ_effects.values())

        # Compute adjusted_strength (adjust in logit space, back-transform)
        civ_adj = strength_df['civilization'].map(civ_effects).fillna(0)
        strength_df['adjusted_strength'] = inv_logit(
            logit(strength_df['relative_strength']) - civ_adj
        )
        strength_df.drop(columns=['logit_strength'], inplace=True)
    else:
        if verbose:
            print("Skipping OLS civilization adjustment (ols_civilization=False)")
        civ_effects = None
        ols_model = None
        strength_df['adjusted_strength'] = strength_df['relative_strength']

    # Step 6: Exclude non-LLM experiments (vanilla-only, null-only)
    strength_df = filter_non_llm_games(strength_df, True)

    if verbose:
        print(f"  {strength_df['game_id'].nunique()} games after excluding non-LLM experiments")
    return strength_df, civ_effects, ols_model


# ---------------------------------------------------------------------------
# Game ordering
# ---------------------------------------------------------------------------

def load_game_order(strength_df, timestamps_path='game_timestamps.csv'):
    """
    Return a list of game_ids sorted chronologically using game_timestamps.csv.
    Falls back to alphabetical game_id ordering if timestamps unavailable.
    """
    valid_game_ids = set(strength_df['game_id'].unique())

    if os.path.exists(timestamps_path):
        ts_df = pd.read_csv(timestamps_path)
        ts_df = ts_df[ts_df['game_id'].isin(valid_game_ids)]
        ts_df = ts_df.sort_values('timestamp')
        ordered = ts_df['game_id'].tolist()

        # Append any games missing from timestamps file
        missing = valid_game_ids - set(ordered)
        if missing:
            ordered.extend(sorted(missing))
            print(f"  Warning: {len(missing)} games not found in timestamps file, appended at end")

        return ordered
    else:
        print(f"  Warning: {timestamps_path} not found, using alphabetical game_id order")
        return sorted(valid_game_ids)


# ---------------------------------------------------------------------------
# Caching
# ---------------------------------------------------------------------------

def load_cache(cache_path):
    if os.path.exists(cache_path):
        with open(cache_path, 'rb') as f:
            return pickle.load(f)
    return {}


def save_cache(cache, cache_path):
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    with open(cache_path, 'wb') as f:
        pickle.dump(cache, f)


def cache_key(game_ids):
    """MD5 hash of sorted game_id list."""
    return hashlib.md5(','.join(sorted(game_ids)).encode()).hexdigest()


# ---------------------------------------------------------------------------
# Ablation helpers
# ---------------------------------------------------------------------------

def get_target_types(strength_df):
    """Return sorted list of non-Vanilla player types to ablate."""
    all_types = sorted(strength_df['player_type'].unique())
    return [t for t in all_types if t != 'Vanilla']


def build_ablation_schedule(strength_df, game_order, target_type):
    """
    Partition games into base set (no target) and target sequence.

    Returns:
        (base_game_ids, target_game_ids) — both in chronological order.
    """
    games_with_target = set(
        strength_df[strength_df['player_type'] == target_type]['game_id'].unique()
    )
    base_game_ids = [g for g in game_order if g not in games_with_target]
    target_game_ids = [g for g in game_order if g in games_with_target]
    return base_game_ids, target_game_ids


# ---------------------------------------------------------------------------
# Single-target ablation (runs in a worker process)
# ---------------------------------------------------------------------------

def _run_ablation_for_target(args):
    """
    Ablation loop for one target type. Designed for ProcessPoolExecutor.

    Accepts a single tuple to work with Pool.map / executor.submit.
    """
    (strength_df, base_game_ids, target_game_ids,
     target_type, cache, min_target_games) = args

    # Re-import inside worker (subprocess needs fresh module state)
    import sys
    from pathlib import Path
    _root = str(Path(__file__).resolve().parent.parent)
    if _root not in sys.path:
        sys.path.insert(0, _root)
    from ratings import calculate_ratings_bt

    results = []
    local_cache = {}
    n_target = len(target_game_ids)
    base_set = set(base_game_ids)

    # Track new opponent introductions as target games are added
    game_player_types = strength_df.groupby('game_id')['player_type'].apply(set).to_dict()
    opponents_seen = set()
    new_opponent_events = []  # list of (n_target_games, [new_opponent_names])

    for k in range(1, n_target + 1):
        # Detect new opponents in this game
        game_id = target_game_ids[k - 1]
        pts_in_game = game_player_types.get(game_id, set())
        new_opps = pts_in_game - {target_type} - opponents_seen
        if new_opps:
            opponents_seen.update(new_opps)
            new_opponent_events.append((k, sorted(new_opps)))

        if k < min_target_games:
            continue

        game_ids = base_game_ids + target_game_ids[:k]
        key = cache_key(game_ids)

        if key in cache:
            rating_df = cache[key]
        elif key in local_cache:
            rating_df = local_cache[key]
        else:
            game_id_set = base_set | set(target_game_ids[:k])
            subset = strength_df[strength_df['game_id'].isin(game_id_set)]
            n_types = subset['player_type'].nunique()
            if n_types < 2:
                continue
            try:
                rating_df = calculate_ratings_bt(subset, verbose=False)
                local_cache[key] = rating_df
            except Exception as e:
                print(f"  [{target_type} step {k}/{n_target}] BT failed: {e}")
                continue

        n_total = len(base_game_ids) + k

        for _, row in rating_df.iterrows():
            results.append({
                'target_type': target_type,
                'ablation_step': k,
                'game_id': game_id,
                'n_target_games': k,
                'n_total_games': n_total,
                'player_type': row['player_type'],
                'elo': row['elo'],
                'se_elo': row['se_elo'],
                'log_worth': row['log_worth'],
                'se_log_worth': row['se_log_worth'],
            })

        if k % 25 == 0 or k == n_target:
            print(f"  [{target_type}] step {k}/{n_target}")

    return results, local_cache, new_opponent_events


# ---------------------------------------------------------------------------
# Parallel orchestrator
# ---------------------------------------------------------------------------

def run_ablation(strength_df, game_order, cache, target_types=None,
                 max_workers=None, min_target_games=3):
    """
    Run ablation for all (or selected) non-Vanilla player types in parallel.

    Args:
        strength_df: Full strength data from prepare_strength_data()
        game_order: Chronologically sorted game IDs
        cache: Pre-loaded cache dict (read-only for workers)
        target_types: List of types to ablate, or None for all non-Vanilla
        max_workers: Parallel workers (default: min(n_targets, cpu_count))
        min_target_games: Skip steps with fewer target games than this

    Returns:
        (results_df, updated_cache, new_opponent_events)
        new_opponent_events is a dict: target_type -> list of (n_target_games, [names])
    """
    if target_types is None:
        target_types = get_target_types(strength_df)

    # Build schedules
    schedules = {}
    for tt in target_types:
        base, target = build_ablation_schedule(strength_df, game_order, tt)
        schedules[tt] = (base, target)
        print(f"  {tt}: base={len(base)} games, target={len(target)} games")

    n_workers = max_workers or min(len(target_types), multiprocessing.cpu_count())
    print(f"  Using {n_workers} parallel workers")

    # Build task args (tuple per target, for pickling)
    task_args = []
    for tt in target_types:
        base, target = schedules[tt]
        task_args.append((strength_df, base, target, tt, cache, min_target_games))

    all_results = []
    merged_cache = dict(cache)
    all_opponent_events = {}  # target_type -> list of (n_target_games, [names])

    with ProcessPoolExecutor(max_workers=n_workers) as executor:
        futures = {
            executor.submit(_run_ablation_for_target, args): args[3]  # args[3] = target_type
            for args in task_args
        }

        for future in as_completed(futures):
            tt = futures[future]
            try:
                results_list, local_cache, opponent_events = future.result()
                all_results.extend(results_list)
                merged_cache.update(local_cache)
                all_opponent_events[tt] = opponent_events
                print(f"  Completed {tt}: {len(results_list)} rows")
            except Exception as e:
                print(f"  FAILED {tt}: {e}")

    results_df = pd.DataFrame(all_results) if all_results else pd.DataFrame()
    return results_df, merged_cache, all_opponent_events


# ---------------------------------------------------------------------------
# Chart generation
# ---------------------------------------------------------------------------

def generate_ablation_charts(results_df, output_dir, new_opponent_events=None):
    """Generate per-target and combined Elo convergence charts.

    Args:
        results_df: Ablation results DataFrame.
        output_dir: Directory for output PNGs.
        new_opponent_events: dict of target_type -> list of (n_target_games, [names]).
    """
    sns.set_style('whitegrid')
    if new_opponent_events is None:
        new_opponent_events = {}

    target_types = sorted(results_df['target_type'].unique())

    for tt in target_types:
        tt_df = results_df[
            (results_df['target_type'] == tt) & (results_df['player_type'] == tt)
        ].copy()
        if tt_df.empty:
            continue

        # Skip early steps where BT estimates are unstable
        tt_df = tt_df[tt_df['n_target_games'] >= 5].sort_values('n_target_games')
        if tt_df.empty:
            continue

        fig, ax = plt.subplots(figsize=(12, 5))
        color = get_player_color(tt)
        ls = get_player_linestyle(tt)

        ax.plot(tt_df['n_target_games'], tt_df['elo'],
                color=color, linestyle=ls, linewidth=2, label=tt)
        ax.fill_between(
            tt_df['n_target_games'],
            tt_df['elo'] - 1.96 * tt_df['se_elo'],
            tt_df['elo'] + 1.96 * tt_df['se_elo'],
            color=color, alpha=0.15,
        )
        ax.axhline(1500, color='gray', linestyle='--', linewidth=1, label='Vanilla (1500)')

        # Final Elo reference line
        final_elo = tt_df['elo'].iloc[-1]
        ax.axhline(final_elo, color=color, linestyle=':', linewidth=1, alpha=0.5,
                    label=f'Final Elo ({final_elo:.0f})')

        # Draw new opponent introductions
        events = new_opponent_events.get(tt, [])
        if events:
            x_min = tt_df['n_target_games'].min()
            x_max = tt_df['n_target_games'].max()
            _, y_max = ax.get_ylim()

            # Split into initial (before visible range) and mid-chart events
            initial_opps = []
            for ev_x, names in events:
                if ev_x > x_max:
                    continue
                if ev_x < x_min:
                    initial_opps.extend(names)
                else:
                    label = ' + '.join(names)
                    ax.axvline(ev_x, color='black', linestyle=':', linewidth=1, alpha=0.5)
                    ax.text(
                        ev_x, y_max, f' {label}',
                        rotation=90, va='top', ha='left',
                        fontsize=7, color='black', alpha=0.7,
                        bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                                  alpha=0.7, edgecolor='none'),
                    )

            # Show initial opponents as a standalone label in the lower-left
            if initial_opps:
                label = 'Initial opponents: ' + ', '.join(sorted(set(initial_opps)))
                ax.text(
                    0.02, 0.02, label,
                    transform=ax.transAxes, fontsize=7, color='black', alpha=0.7,
                    va='bottom', ha='left',
                    bbox=dict(boxstyle='round,pad=0.4', facecolor='#f0f0f0',
                              alpha=0.8, edgecolor='gray', linewidth=0.5),
                )

        ax.set_xlabel('Number of Target Games Included', fontsize=12)
        ax.set_ylabel('Elo Rating', fontsize=12)
        ax.set_title(f'Ablation: {tt} Elo as Games Are Added', fontsize=14, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)

        plt.tight_layout()
        safe_name = tt.replace(' ', '_').replace('/', '_')
        fig.savefig(os.path.join(output_dir, f'ablation_bt_{safe_name}.png'), dpi=150)
        plt.close(fig)

    # Combined chart
    fig, ax = plt.subplots(figsize=(14, 7))
    for tt in target_types:
        tt_df = results_df[
            (results_df['target_type'] == tt) & (results_df['player_type'] == tt)
        ]
        tt_df = tt_df[tt_df['n_target_games'] >= 5].sort_values('n_target_games')
        if tt_df.empty:
            continue
        ax.plot(
            tt_df['n_target_games'], tt_df['elo'],
            color=get_player_color(tt),
            linestyle=get_player_linestyle(tt),
            linewidth=1.5,
            label=tt,
        )

    ax.axhline(1500, color='gray', linestyle='--', linewidth=1, label='Vanilla (1500)')
    ax.set_xlabel('Number of Target Games Included', fontsize=12)
    ax.set_ylabel('Elo Rating', fontsize=12)
    ax.set_title('Ablation: All Player Types\' Elo Convergence', fontsize=14, fontweight='bold')
    ax.legend(fontsize=8, bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(os.path.join(output_dir, 'ablation_bt_all.png'), dpi=150, bbox_inches='tight')
    plt.close(fig)

    print(f"  Saved {len(target_types) + 1} charts to {output_dir}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Ablation Bradley-Terry ratings')
    parser.add_argument('--no-cache', action='store_true', help='Ignore existing cache')
    parser.add_argument('--output-dir', default='ratings/output', help='Output directory')
    parser.add_argument('--max-workers', type=int, default=None,
                        help='Max parallel workers (default: min(n_targets, cpu_count))')
    parser.add_argument('--min-target-games', type=int, default=3,
                        help='Min target games before fitting BT (default: 3)')
    parser.add_argument('--targets', nargs='*', default=None,
                        help='Specific target types to ablate (default: all non-Vanilla)')
    args = parser.parse_args()

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)
    cache_path = os.path.join(output_dir, 'ablation_bt_cache.pkl')

    # Prepare data (reused from existing pipeline)
    strength_df, _, _ = prepare_strength_data()

    # Game ordering (reused from existing pipeline)
    print("Determining game order...")
    game_order = load_game_order(strength_df)
    print(f"  {len(game_order)} games")

    # Load cache
    cache = {} if args.no_cache else load_cache(cache_path)
    cached_count = len(cache)
    if cached_count:
        print(f"  Loaded {cached_count} cached results")

    # Run ablation
    print("Running ablation Bradley-Terry...")
    results_df, cache, new_opponent_events = run_ablation(
        strength_df, game_order, cache,
        target_types=args.targets,
        max_workers=args.max_workers,
        min_target_games=args.min_target_games,
    )

    # Save cache
    if len(cache) > cached_count:
        save_cache(cache, cache_path)
        print(f"  Cache saved ({len(cache)} entries)")

    if results_df.empty:
        print("No results produced. Exiting.")
        return

    # Save CSV
    csv_path = os.path.join(output_dir, 'ablation_bt_ratings.csv')
    results_df.to_csv(csv_path, index=False)
    print(f"Saved {len(results_df)} rows to {csv_path}")

    # Generate charts
    print("Generating charts...")
    generate_ablation_charts(results_df, output_dir, new_opponent_events)

    print("Done.")


if __name__ == '__main__':
    main()
