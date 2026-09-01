Analyze the saved RESULTS of a Jupyter notebook. Mundane setup (path resolution, nbconvert) and first-pass summarization are delegated to subagents so the main agent's context is reserved for grounded analysis, not raw markdown dumps and image bytes.

**Argument**: `$ARGUMENTS` is `<notebook_path>` optionally followed by a free-form question. Examples:
- `nuke/reasoning_rationale_stems.ipynb`
- `nuke/replay_exploratory.ipynb what stands out about the model agreement plots?`

If no notebook path is given, fall back to the currently-focused `.ipynb` in the IDE. If neither is available, ask the user which notebook to analyze.

All paths in your tool calls and outputs must be **relative** to the project root.

---

## Step 1 — Isolate the path and question

Split `$ARGUMENTS` into a notebook-path token and the optional free-form question (everything after the `.ipynb` token). Hold the question for Step 4. Do not read the notebook yourself.

## Step 2 — Delegate setup to a subagent (resolve path + convert)

Spawn one `general-purpose` Agent to handle both path resolution and conversion. Its whole job is mechanical plumbing whose terminal output would otherwise pollute your context. Brief it with self-contained instructions — it has not seen this conversation.

Prompt template:

> Resolve and convert a Jupyter notebook for downstream analysis.
>
> 1. Validate that `<notebook_path>` exists and ends in `.ipynb`. If not, report the error and stop.
> 2. Let `<stem>` = the filename without extension.
> 3. Wipe and recreate `.tmp/notebooks/<stem>/`, then run nbconvert:
>    ```bash
>    python -c "import shutil, pathlib; p=pathlib.Path('.tmp/notebooks/<stem>'); shutil.rmtree(p, ignore_errors=True); p.mkdir(parents=True)"
>    jupyter nbconvert --to markdown --no-input --output-dir .tmp/notebooks/<stem> <notebook_path>
>    ```
>    `--no-input` strips code cells but keeps markdown cells and outputs. nbconvert auto-extracts images to `.tmp/notebooks/<stem>/<stem>_files/`. The output folder is project-relative on purpose — the Read tool cannot reach `%TEMP%`.
> 4. Glob `.tmp/notebooks/<stem>/<stem>_files/*` to list the generated images in the order they appear on disk.
> 5. **Report back in under 100 words**, exactly this shape and nothing else:
>    - `stem`: …
>    - `md_path`: `.tmp/notebooks/<stem>/<stem>.md`
>    - `image_paths`: bulleted list of project-relative paths
>    - `notes`: any warnings from nbconvert, else "none"

## Step 3 — Delegate summarization to a second subagent

Spawn a second `general-purpose` Agent to read the full markdown and every image, and produce a structured **index** the main agent can ground on. This is the expensive step — it consumes the full raw content — and MUST happen in a subagent, not in the main context.

Pass it `md_path` and `image_paths` from Step 2. Brief it:

> You are producing a factual index of a converted notebook — NOT answering any downstream question.
>
> 1. Read `<md_path>` in full.
> 2. Read each image in `<image_paths>` in the order they appear in the markdown (images render natively via Read).
> 3. Produce a report with these sections, grounded in specific line numbers and image paths. Be concrete; do NOT paraphrase content the main agent will later need verbatim.
>    - **Sections**: each heading with its line range in the md and a one-line gist.
>    - **Figures**: for each image, its path, the md line it is referenced at, what it shows, key visible values/trends, and any anomalies.
>    - **Key numbers & tables**: notable quantitative outputs with md line refs.
>    - **Narrative vs. output mismatches**: places where markdown claims diverge from what the outputs/figures actually show.
> 4. Target ~600 words. Point to locations rather than quoting at length — the caller can Read the specific lines/images directly when it needs the raw evidence.

## Step 4 — Ground and answer (main agent)

You now have the summarizer's index in your context without having loaded the raw markdown or images yourself. Use it as a map, not as the source of truth.

- **No question in `$ARGUMENTS`** → present what you learned from the notebook. Ground every claim in a specific cell or figure. Read the md or a specific image directly only when the index is ambiguous or missing a detail you need to confirm.
- **Question in `$ARGUMENTS`** → do a deep, focused analysis answering that question. Use the index to identify the *relevant* sections and figures, then **Read those specific md line ranges and images directly** (use the `offset`/`limit` args on Read for the markdown) to ground load-bearing claims in raw evidence. Quantify where possible and call out results that contradict or qualify the answer. Do not degrade into a generic summary and do not rely solely on the summarizer's paraphrase for any claim the user will act on.

## Step 5 — No cleanup

Leave `.tmp/notebooks/<stem>/` in place. Follow-up questions in this or a later conversation can re-Read the existing artifacts directly without re-invoking the skill. Re-invoking regenerates from scratch (Step 2).
