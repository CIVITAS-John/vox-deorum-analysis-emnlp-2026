# Ablation Bradley-Terry Ratings

## Methodology

### Purpose

Standard Bradley-Terry (BT) ratings fit a single model on all games simultaneously, producing one point estimate per player type. This leaves a key question unanswered: **how sensitive is each player type's rating to the number of games observed?**

The ablation approach answers this by isolating each player type's evidence contribution. For a target player type X, we hold all other games constant and progressively add X's games one at a time, refitting the BT model at each step. This measures the marginal contribution of each additional game.

### Procedure

For each non-Vanilla player type X with N games sorted chronologically:

1. **Base set**: All games that do **not** contain player type X. This set remains constant throughout the ablation sequence for X.
2. **Step k** (k = 1, 2, …, N): Fit a Bradley-Terry model on `base_set ∪ {game_1, …, game_k}`. Record all player types' Elo ratings and standard errors.
3. Repeat for each non-Vanilla player type independently.

Vanilla is never ablated because it participates in every game and serves as the Elo reference (1500).

### Key Properties

- **Isolation**: Each ablation sequence changes only one variable — the number of target games. All background evidence (other player types' games) is held constant.
- **Independence**: Different player types' ablation sequences are fully independent and run in parallel.
- **Stability baseline**: The base set is large (typically 300+ games), so all non-target player types have stable ratings from the start. Only the target's rating moves meaningfully as its games are added.

### Strength Computation

Before BT fitting, per-player strength is computed through the same pipeline used for all rating analyses:

1. **Weighted win probability**: Late-game turns (progress > 20%) are averaged, weighted by turn progress (later turns count more).
2. **Relative strength**: Normalized by the strongest player in each game.
3. **Winner enforcement**: Winners with relative strength < 1.0 are adjusted upward.
4. **Civilization adjustment**: OLS regression in logit space removes systematic civilization bonuses/penalties (Sum contrast coding, effects sum to zero).
5. **LLM filtering**: Games with only Vanilla or Null AI players are excluded.

### Bradley-Terry Model

Each game is decomposed into pairwise comparisons between different player types. Pairs are weighted by score difference: `weight = 1 + log(1 + |score_diff| / margin)`, where margin is auto-detected as the median pairwise score difference. The model is fit via maximum likelihood using R's `BradleyTerry2` package.

Elo conversion: `Elo = 1500 + 400 × log₁₀(worth)`, centered on Vanilla = 1500.

## Output

### CSV (`ablation_bt_ratings.csv`)

| Column | Description |
|---|---|
| `target_type` | The player type being ablated |
| `ablation_step` | Step number in the ablation sequence (1-indexed) |
| `game_id` | UUID of the game added at this step |
| `n_target_games` | Number of target's games included so far (= ablation_step) |
| `n_total_games` | Total games in the model (base + n_target_games) |
| `player_type` | The rated player type (all types are recorded, not just the target) |
| `elo` | Bradley-Terry Elo rating at this step |
| `se_elo` | Standard error of the Elo estimate |
| `log_worth` | Log-worth on BT scale (Vanilla = 0) |
| `se_log_worth` | Standard error of log-worth |

### Charts

- **Per-target charts** (`ablation_bt_{type}.png`): Elo convergence with 95% CI band, Vanilla reference line (1500), final Elo reference line, and new opponent introduction markers.
- **Combined chart** (`ablation_bt_all.png`): All targets overlaid on one plot.

## Interpreting Results

### Convergence Pattern

A typical ablation curve starts volatile and stabilizes:

- **Early steps** (n_target_games < 10): High standard error, large Elo swings. A few strong or weak performances dominate the estimate. Ratings at this stage are unreliable.
- **Mid steps**: Standard error shrinks as evidence accumulates. The rating oscillates around its eventual value.
- **Late steps**: Minimal change per additional game. The curve flattens — the rating has converged.

### What Convergence Speed Tells You

- **Fast convergence** (stable by ~10 games): The player type's strength relative to others is clear and consistent. Individual games don't change the picture much.
- **Slow convergence** (still moving at 20+ games): The player type has high variance across games, or its strength depends heavily on matchup composition. More data would improve the estimate.
- **Non-convergence** (oscillating throughout): Possible indicator of matchup-dependent performance — the player type may be strong against some opponents but weak against others, so the rating depends on which games are included.

### Standard Error Bands

The shaded 95% CI band (±1.96 × SE) shows estimation uncertainty. Key patterns:

- **Band shrinks monotonically**: Normal convergence. More games → more precision.
- **Band widens at a step**: The added game introduced conflicting evidence (e.g., a strong player type losing badly), temporarily increasing model uncertainty.
- **Band never narrows below ~20 Elo**: The player type has genuinely high game-to-game variance that cannot be reduced by more data.

### New Opponent Markers

Vertical dotted lines mark steps where the target first plays against a new opponent type. Opponents encountered before the chart's visible range (steps 1–4) are listed in a text box at the bottom-left.

These markers explain rating jumps: encountering a new opponent can shift the BT model's estimate because the target's pairwise comparisons now include a previously-unseen matchup.

### Final Elo Reference Line

The horizontal dotted line shows the target's Elo at the final step (all games included). This is the same value you'd get from a standard (non-ablation) BT fit. Use it to gauge how quickly the convergence curve reaches its final value:

- If the curve is close to the final line by step 10, the first 10 games already provide a reliable estimate.
- If the curve only approaches the final line near the end, early estimates were misleading and the full dataset is needed.

## Usage

```bash
# Ablate all player types (parallel)
python -m ratings.iterative_bt

# Ablate specific targets
python -m ratings.iterative_bt --targets Sonnet-4.5-Simple GPT-OSS-120B-Briefed

# Force recomputation (ignore cache)
python -m ratings.iterative_bt --no-cache

# Limit parallelism
python -m ratings.iterative_bt --max-workers 4
```

### CLI Arguments

| Flag | Default | Description |
|---|---|---|
| `--no-cache` | off | Ignore existing cache and recompute all BT fits |
| `--output-dir` | `ratings/output` | Directory for CSV and chart output |
| `--max-workers` | min(n_targets, cpu_count) | Number of parallel worker processes |
| `--min-target-games` | 3 | Minimum target games before fitting BT (skip earlier steps) |
| `--targets` | all non-Vanilla | Space-separated list of specific player types to ablate |
