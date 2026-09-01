Perform iterative grounded theory coding on AI rationale quote files found in the target folder.

**Target folder**: Use `$ARGUMENTS` if provided. Otherwise use the folder containing the currently focused file in the IDE. Default fallback: `exploratory/nuke`.

All file paths in outputs must be **relative** to the project root. Never use absolute paths.

---

## Step 0 — Discover files and inventory quotes

1. List all `.md` files in the target folder.
2. For each file, record:
   - Model name (from filename, e.g., `Deepseek-3.2-Simple` → short key `DS32S`)
   - Escalation rate (from the summary line `N / M players escalated ...`)
3. Assign each quote a stable ID: `<ModelShortKey>-<CivName>-T<Turn>` (e.g., `DS32S-Poland-T387`). Replace spaces in civ names with underscores.

Hold this inventory in memory for subsequent steps.

---

## Phase 1 — Open Coding (parallel general-purpose sub-agents, one per file)

Create the `<target_folder>/coding/` subfolder if it does not exist.

Launch **all sub-agents simultaneously in a single message** (one Agent tool call per file, all in the same response). Each agent is type `general-purpose`.

Each agent receives:
- The full raw text of its assigned `.md` file.
- The model short key (e.g., `DS32S`).
- The target folder path.
- This instruction:

  > Read every blockquote (`>`) in this file. For each quote, apply open coding. Generate as many verb-phrase codes as the data warrants — there is no minimum or maximum. A code is a short verb phrase (2–6 words) that names what the speaker is doing conceptually: e.g., "invoking nuclear deterrence," "perceiving imminent cultural loss," "framing nukes as last resort," "rationalizing aggression through desperation." Codes must be **interpretative**, not merely descriptive — they should capture meaning, motivation, or social action, not just paraphrase content.
  >
  > Format your output as structured markdown:
  >
  > ```
  > ## <QuoteID>
  > Civ: <name> | Turn: <N> | Strategy: <grand strategy>
  > - <verb-phrase code>
  > - <verb-phrase code>
  > ...
  > ```
  >
  > Write your complete output to `<target_folder>/coding/open_codes_<ModelKey>.md`. Return only a one-line summary: the number of quotes coded and the file path written.

---

## Phase 2 — Category Building (sequential general-purpose sub-agents)

This phase is **sequential**: each round's sub-agent informs the next. Do not run rounds in parallel.

**Round 1**: Launch one `general-purpose` sub-agent with:
- All per-model open-codes files from Phase 1 (`open_codes_*.md` in the `coding/` subfolder).
- This instruction:

  > You are doing focused coding and early category building. Review all the verb-phrase codes across all quotes. Group similar codes together, merge synonyms, and name each emerging category with a short label and a one-sentence definition. Produce an initial set of categories — as many or as few as the data requires. For each category list: (a) category name, (b) definition, (c) the member codes it subsumes, (d) the quote IDs where it appears.
  >
  > Return structured markdown. Do not invent concepts not present in the codes.

Write the round's output to `<target_folder>/coding/categories_round1.md`.

**Evaluate**: Read the round's output. Ask: Are categories still redundant, overlapping, or too granular? If yes, proceed to another round.

**Subsequent rounds**: Launch one `general-purpose` sub-agent with:
- The previous round's categories file.
- All per-model open-codes files (`open_codes_*.md`).
- This instruction:

  > You are doing a further round of category consolidation. The categories below were produced in the previous round. Some may still overlap, be redundant, or be too fine-grained. Consolidate further: merge where appropriate, rename for clarity, and eliminate any category that is not meaningfully distinct. Do not add new concepts. Preserve the quote-ID mapping.
  >
  > Return structured markdown in the same format as the input.

Write output to `<target_folder>/coding/categories_roundN.md` (increment N).

**Termination**: Stop launching new rounds when the categories feel stable — mutually exclusive enough, clearly defined, and collectively covering the data. Typically 2–4 rounds, but follow the data.

---

## Phase 3 — Codebook Creation (single general-purpose sub-agent)

Launch one `general-purpose` sub-agent with:
- The final round's categories file.
- All per-model open-codes files (`open_codes_*.md`).
- This instruction:

  > You are creating a formal qualitative codebook. For each category from the final category set, write a codebook entry with:
  > 1. **Code name** (short label, title-case)
  > 2. **Definition** (2–3 sentences explaining what this category captures)
  > 3. **Inclusion criteria** (what kinds of statements belong here)
  > 4. **Exclusion criteria** (what might look similar but does not belong)
  > 5. **Anchor examples** (2–3 QuoteIDs with a one-sentence explanation of why each fits)
  >
  > Return structured markdown, one section per code.

Write output to `<target_folder>/coding/codebook.md`.

---

## Phase 4 — Systematic Coding (parallel general-purpose sub-agents, one per file)

Launch **all sub-agents simultaneously in a single message**. Each agent is type `general-purpose`.

Each agent receives:
- The full text of its assigned `.md` file.
- The full text of `codebook.md`.
- The model short key (e.g., `DS32S`).
- The target folder path.
- This instruction:

  > Apply the codebook to every quote in this file. For each quote, assign all applicable code names (a quote may receive multiple codes). Format as a markdown table:
  >
  > | QuoteID | Codes Applied | Brief Justification (one sentence per code) |
  > |---|---|---|
  >
  > Use only code numbers defined in the codebook. If a quote clearly resists all codes, mark it `UNCODED` and note why.
  >
  > Write your complete output to `<target_folder>/coding/coded_quotes_<ModelKey>.md` and a corresponding CSV file with one row per quote:
  > ```
  > QuoteID,Model,Civ,Turn,Code_1,Code_2,Code_3,Code_4,Code_5,Code_6,Code_7,Code_8,Code_9,Code_10,etc...
  > ```
  > Return only a one-line summary: the number of quotes coded and the file path written.

After all agents return, run the bundled concat script:

```bash
python .claude/skills/code-quotes/concat_coded_quotes.py <target_folder>/coding
```

---

## Phase 5 — Synthesis (single general-purpose sub-agent)

Launch one `general-purpose` sub-agent with:
- All per-model coded-quotes files (`coded_quotes_*.md`)
- `codebook.md` (full text)
- All per-model open-codes files (`open_codes_*.md`)
- The model escalation-rate summary from Step 0 (list of models with their N/M rates)
- This instruction:

  > You are writing the final grounded theory synthesis memo. Using all materials provided, produce the following:
  >
  > **1. Core Category**
  > Name and define the central phenomenon — the one concept that most other categories relate to, condition, or consequence from. Justify why this is the core.
  >
  > **2. Theoretical Narrative** (~500 words)
  > A prose integration of all categories around the core category. Use causal/conditional language: when X, then Y, because Z. Trace the typical trajectory from contextual conditions → action → consequence.
  >
  > **3. Theoretical Propositions**
  > 4–8 if-then statements grounded in the data. Each proposition should be falsifiable and cite at least one QuoteID as evidence.
  >
  > **4. Negative Cases and Exceptions**
  > Identify 2–4 quotes that resist the dominant pattern. Discuss what they reveal about boundary conditions.
  >
  > **5. Saturation Assessment**
  > For each codebook category: note whether it appears saturated (no new properties emerging) or underrepresented (needs more data). Reference escalation-rate differences across models where relevant.
  >
  > Return structured markdown.

Write output to `<target_folder>/coding/theory.md`.

---

## Completion

After all phases, print:
- The list of files written (relative paths), including `coded_quotes.csv`
- The core category name discovered
- The final code frequency table (top codes by quote count)
