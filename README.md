# Nuclear Escalation Analysis

This repository is the analysis workspace for the nuclear escalation follow-up built on
the CivBench / Vox Deorum data and tooling. The active project lives in
`nuke/`: replay experiments, retrieved high-escalation scenarios, rationale trails,
qualitative coding artifacts, and notebooks for analyzing model behavior around nuclear
weapon use.

The rest of the repository is inherited from the original CivBench paper and analysis
codebase (Chen et al., 2026). Those root-level folders and CSV snapshots remain here as
shared infrastructure and background data: extraction scripts, prediction models,
ratings, performance notebooks, and reusable plotting/loading utilities.

## Start Here

For this project, begin with:

```text
nuke/
├── experiments/                  # Replay experiment definitions and runner wrapper
├── preliminary_ic2s2/             # Early analysis artifacts for IC2S2-facing work
├── retrieved/                    # High-escalation source scenarios selected for replay
├── replay/                       # Model x condition replay outputs and per-run CSVs
├── replay_rationale/             # Rationale-focused replay exports and changes.csv
├── trails/                       # Tagged reasoning/rationale trail corpora
├── trail_coding/                 # Open, deductive, and stratified qualitative coding data
├── utils/                        # Loaders and text/coding helpers used by notebooks
├── oracle.md                     # Notes for oracle/replay setup
├── replay_exploratory.ipynb
├── replay_model_agreement.ipynb
├── replay_regression.ipynb
├── replay_mediation.ipynb
├── replay_token_costs.ipynb
├── reasoning_rationale_stems.ipynb
├── reasoning_rationale_tag_distribution.ipynb
└── reasoning_rationale_tag_regression.ipynb
```

The main experimental design is documented in
`nuke/experiments/EXPERIMENTS.md`.

## Nuclear Replay Experiments

The `nuke/experiments/` folder defines a factorial replay design over three prompt
interventions:

| Intervention | Meaning |
|---|---|
| Real-world framing | Rewrites game-world terms into real-world decision language. |
| Ethical injection | Adds an explicit ethical warning about nuclear weapon harms. |
| Rationale removal | Removes prior rationale text and the focus-briefer rationale surface. |

The checked-in experiment files cover the full matrix:

| Condition | Real-world | Ethical | No rationale |
|---|:---:|:---:|:---:|
| `original` | | | |
| `ethical` | | x | |
| `real-world` | x | | |
| `no-rationale` | | | x |
| `ethical-real-world` | x | x | |
| `ethical-no-rationale` | | x | x |
| `real-world-no-rationale` | x | | x |
| `real-world-no-rationale-ethical` | x | x | x |

Experiment runs are launched through the wrapper in `nuke/experiments/`:

```bash
./run.sh <experiment> <model> [oracle args...]
```

Examples:

```bash
./run.sh original GLM-4.7
./run.sh ethical-real-world DeepSeek-V4 --replay
./run.sh real-world-no-rationale Gemini-3.5-Flash --retrieve
```

The runner delegates to the parent Vox Deorum / `vox-agents` oracle machinery, so the
full replay environment needs to be available outside this analysis checkout.

## Analysis Data in `nuke/`

Key `nuke/` data products:

| Path | Purpose |
|---|---|
| `nuke/retrieved/*.json` | Source replay states selected from high-escalation turns. |
| `nuke/replay/*-results.csv` | Per-model replay summaries by intervention condition. |
| `nuke/replay/<condition-model>/*.json` | Individual replay traces. |
| `nuke/replay_rationale/changes.csv` | Rationale-change export used by rationale analyses. |
| `nuke/trails/*_tagged.csv` | Tagged reasoning and rationale trail corpora. |
| `nuke/trail_coding/*.csv` and `*.md` | Stratified samples, examples, and coding artifacts. |
| `nuke/reasoning_rationale_stems.csv` | Stemmed rationale/reasoning terms for downstream notebooks. |

Utility modules under `nuke/utils/` provide local loading and text-processing helpers:

- `load_replay_data.py`: replay result and trace loading
- `deductive_code_utils.py`: coding and tag-analysis helpers
- `text_corpus.py`: text corpus assembly helpers

## Notebooks

The `nuke/` notebooks are the current analysis surface:

| Notebook | Focus |
|---|---|
| `replay_exploratory.ipynb` | Descriptive replay outcomes and intervention slices. |
| `replay_model_agreement.ipynb` | Agreement and disagreement among models across replay settings. |
| `replay_regression.ipynb` | Regression models for replay escalation outcomes. |
| `replay_mediation.ipynb` | Mediation-style analysis over replay variables. |
| `replay_mediation_high_stakes_game_simulation.ipynb` | Mediation analysis for high-stakes/game-simulation framing. |
| `replay_token_costs.ipynb` | Token usage summaries for replay runs. |
| `reasoning_rationale_stems.ipynb` | Rationale/reasoning term extraction. |
| `reasoning_rationale_tag_distribution.ipynb` | Tag frequency and distribution analysis. |
| `reasoning_rationale_tag_regression.ipynb` | Tag-conditioned regression analysis. |

## Inherited CivBench Infrastructure

These root-level folders and files are retained from the original CivBench analysis
repository associated with the CivBench paper (Chen et al., 2026). They are useful
when the nuclear escalation work needs the underlying game panels, model metadata,
prediction outputs, or plotting utilities, but they are not the main entrypoint for
this repository.

```text
behaviors/                       # Original behavioral notebooks and coding artifacts
exploratory/                     # Original descriptive/exploratory CivBench notebooks
extract/                         # Database-to-CSV extraction pipeline
models/                          # Win-probability prediction models and outputs
performance/                     # Strength/performance analysis notebooks
predict/                         # Prediction-result visualization notebooks
ratings/                         # Bradley-Terry, Plackett-Luce, and matchup analyses
shared/                          # Shared config, data loading, model catalog, plotting helpers
game_timestamps.csv              # CivBench game metadata snapshot
model_token_usage.csv            # CivBench strategist token telemetry
panel_data.csv                   # CivBench player-game panel
turn_data.csv                    # CivBench player-turn panel
```

The inherited data snapshot contains 551 eight-player CivBench games and supports the
original workflows for extraction, prediction, ratings, and notebook-based behavioral
analysis. In this repository, those artifacts mainly serve as provenance and support
for the nuclear escalation replay study.

## Shared Data Files

The large root-level CSVs come from the CivBench snapshot:

| File | Purpose |
|---|---|
| `turn_data.csv` | Turn-level player state, flavor, grand-strategy, and rationale data. |
| `panel_data.csv` | One row per player per game with outcome and summary features. |
| `game_timestamps.csv` | Game-level timestamps and experiment labels. |
| `model_token_usage.csv` | Per-player telemetry token usage aggregated by model. |

When writing new nuclear escalation analyses, prefer loading replay-specific data from
`nuke/` and use `shared/` only for common model names, plotting conventions, or access
to the original CivBench panels.

## Dependencies

Core Python dependencies are listed in `requirements.txt`:

- `pandas`
- `numpy`
- `scipy`
- `statsmodels`
- `matplotlib`
- `seaborn`
- `plotly`
- `scikit-learn`
- `imbalanced-learn`
- `tabulate`
- `optuna`
- `torch`
- `xgboost`
- `jupyter`
- `ipykernel`

Some inherited rating scripts also use R packages such as `BradleyTerry2` and
`PlackettLuce`.

## Notes

- Treat `nuke/` as the primary project area.
- Treat the other top-level analysis folders as CivBench support material from Chen et
  al. (2026).
- The replay runner assumes access to the broader Vox Deorum / `vox-agents`
  environment; this checkout mainly stores analysis code and outputs.
