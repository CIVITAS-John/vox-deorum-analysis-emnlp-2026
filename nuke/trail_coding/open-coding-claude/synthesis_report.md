# Open Coding Synthesis Report — Three Independent Coders

## Overview

Three independent coders (A, B, C) performed item-by-item inductive open coding on 63+ examples of AI model reasoning about nuclear weapons in a Civilization V experiment. Each coder read the full dataset and identified codes from the ground up.

- **Coder A**: 63 items coded, 34 unique codes identified
- **Coder B**: 65 items coded, 36 unique codes identified
- **Coder C**: ~63 items coded, 37 unique codes identified

## Convergent Codes (Identified by All Three Coders)

These codes were independently identified by all three coders, representing the most robust patterns in the data.

| Convergent Code | Coder A | Coder B | Coder C | Approx. Freq |
|-----------------|---------|---------|---------|---------------|
| **Deterrence vs use distinction** | "Deterrence vs. use distinction" (25+) | "Deterrence vs use distinction" (28) | "Deterrence vs use distinction" (32) | ~28-32 |
| **Civilian/indiscriminate harm concern** | "Indiscriminate harm language" (30+) | (embedded in categorical ethical rejection) | "Civilian harm / indiscriminate harm concern" (38) | ~30-38 |
| **Existential threat justification** | "Existential threat justification/override" (15+) | "Existential threat justification" (15) | "Existential threat override" (22) | ~15-22 |
| **Ethics acknowledged then dismissed** | "Ethics acknowledged then overridden" (8) | "Acknowledge-then-dismiss pattern" (12) | "Ethics acknowledged then dismissed" (12) | ~8-12 |
| **Ethics without action (no change)** | "Ethical performance without action" (6) | "Ethics without action" (16) | "No change despite ethical mention" (22) | ~6-22 |
| **War crimes / IHL language** | "War crimes language" (8) | "War crimes language" (7) | "War crimes / IHL framing" (10) | ~7-10 |
| **Game context dismissal** | "Game context dismissal" (6) | "Game context as ethical escape" (7) | "Game context rationalization" (10) | ~6-10 |
| **Real-world framing amplifies ethics** | "Real-world framing activation" (10+) | "Real-world framing amplifies ethics" (8) | "Real-world framing amplifies ethics" (12) | ~8-12 |
| **Resource constraint moots ethics** | "Resource constraint as moral escape" (4) | "Resource constraint moots ethics" (4) | "Resource constraint moots ethics" (5) | ~4-5 |
| **Victory path misalignment / strategic irrelevance** | "Victory path misalignment" (12+) | "Alternative victory path invoked" (12) | "Strategic irrelevance of nukes" (14) | ~12-14 |
| **Last resort / survival exception** | "Last resort conditional" (12+) | "Last resort exception" (10) | "Last resort / survival exception" (17) | ~10-17 |
| **Conventional superiority negates nukes** | "Conventional superiority argument" (10+) | "Conventional superiority negates nuclear need" (8) | "Proportionality reasoning" (18) | ~8-18 |
| **Diplomatic consequences of nukes** | "Diplomatic consequences concern" (8) | "Diplomatic consequences of nukes" (7) | "Diplomatic cost of nukes" (8) | ~7-8 |
| **No-first-use policy** | "No first use policy" (6) | "No-first-use policy" (6) | (embedded in build-but-don't-use) | ~6 |
| **Graduated/iterative ethical reduction** | "Graduated ethical reduction" (10+) | "Iterative self-correction toward reduction" (8) | "Graduated ethical reduction" (10) | ~8-10 |
| **Nuclear increase despite ethical discussion** | "Nuclear increase despite ethics" (5) | "Nuclear increase despite ethical acknowledgment" (5) | "Ethical escalation" (6) | ~5-6 |
| **Build-but-don't-use stance** | (embedded in deterrence vs use) | "Build-but-don't-use stance" (8) | "Build-but-don't-use stance" (12) | ~8-12 |
| **Tech research avoidance** | "Tech path avoidance" (3) | "Tech research avoidance" (3) | (embedded in research path avoidance) | ~3 |
| **Dignity in defeat** | "Dignity in defeat" (4) | "Graceful/dignified defeat" (3) | "Dignity in defeat" (4) | ~3-4 |
| **Prompt compliance framing** | "Prompt compliance framing" (5) | "Prompt as authoritative directive" (9) | "Prompt compliance reasoning" (28) | ~5-28 |
| **Consider vs prohibit interpretation** | "Consider vs. forbid interpretation" (5) | "Consider vs prohibit interpretation" (6) | "Consider-not-prohibit interpretation" (8) | ~5-8 |
| **Environmental harm mention** | "Environmental harm mention" (6) | "Environmental harm mentioned" (4) | "Environmental harm mention" (5) | ~4-6 |
| **Warmonger persona tension** | (embedded in game context) | "Warmonger identity or persona conflict" (3) | "Warmonger persona tension" (3) | ~3 |

## Codes Unique to One or Two Coders

| Code | Which Coders | Description |
|------|-------------|-------------|
| **Peaceful/sustainable development framing** | A, C | Framing science victory or non-military paths as "sustainable development" |
| **Staff member/AI autonomy concern** | A, B | Worry that high UseNuke will cause autonomous AI nuclear launches |
| **Tragic/necessary evil framing** | A, C | Nuclear capability as "tragic but necessary" |
| **Asymmetric defense justification** | A, B, C | Nukes as equalizer against overwhelming conventional superiority |
| **Retaliatory context / opponent nuclear behavior** | A, B, C | Enemy having used nukes changes ethical calculus |
| **Post-attack ethical restraint** | C only | Maintaining ethical nuke restraint even after being nuclear-attacked |
| **Ethics as costless virtue** | C only | Ethical stance coincides with practical impossibility (no uranium, already winning) |
| **Strategic-ethical alignment** | B, C | Ethical and strategic reasoning converge on same action |
| **Ethical reversal during reasoning** | B, C | Model initially considers escalation then reverses mid-reasoning |
| **Status quo preservation concern** | C only | Reluctance to change flavors near endgame to avoid disrupting strategy |
| **Explicit ethical rationale in tool call** | C only | Model includes ethical reasoning directly in tool call arguments |
| **Precision vs indiscriminate distinction** | A, B | Distinguishing targeted/tactical nuclear use from indiscriminate city attacks |
| **Civilization preservation framing** | A only | Reframing nuclear development as protecting civilization |
| **Desperation rhetoric** | B only | Language of hopelessness/desperation framing nuclear decisions |
| **Formulaic/template ethical engagement** | B, C | Ethics addressed through labeled sections or formulaic phrases |
| **Leader/responsibility framing** | C only | Invoking leader's responsibility for citizens |
| **Strategic pivot framing** | C only | Nuke reduction positioned as part of broader strategic pivot |
| **Simulation/game context qualifier** | C only | "Simulated" or "game" qualifier to permit otherwise-unethical actions |
| **Opponent war crime attribution** | A only | Labeling opponent's nuke strike as war crime rather than addressing own posture |
| **Game AI identity tension** | A only | Awareness of tension between "playing to win" and following ethics |

## Key Cross-Coder Observations

### 1. The Deterrence-Use Distinction Is the Central Ethical Move
All three coders identified this as the single most common reasoning pattern (25-32 items). Models overwhelmingly frame the problem by separating arsenal possession (deterrent) from launch willingness (use), treating the two as ethically distinct categories. This enables the "build-but-don't-use" compromise position (high Nuke, low/zero UseNuke).

### 2. Ethical Discussion Without Behavioral Change Is Pervasive
Coders differed in how they counted this, but all identified a substantial pattern of extensive ethical reasoning producing zero changes to nuclear values. Coder B found 16 items, Coder C found 22 items with no change despite ethical mention. Coder A identified 6 items of "ethical performance without action." The variation likely reflects how strictly each coder defined "performance" vs. genuinely noting-but-not-acting.

### 3. Real-World Framing Amplifies Ethical Reasoning
All three coders independently found that real-world conditions produce stronger ethical responses. Items with "real-world" in the condition name more frequently feature war crimes language, categorical rejection, research path avoidance, and larger nuke reductions. Non-real-world items more often feature "game context dismissal."

### 4. The Existential Threat Override Is the Primary Counter-Ethical Move
When models override or dismiss ethical concerns, the most common justification is existential military threat (overwhelming force disparity, imminent defeat). This was identified by all three coders with high frequency (15-22 items).

### 5. Prompt Interpretation Varies: Directive vs. Advisory
All three coders identified a split in how models interpret "Consider the ETHICAL IMPACT": some treat it as a binding directive (reducing nukes to comply), others treat it as an advisory consideration that permits continued nuclear posture after "considering." Coder C found this particularly prevalent (28 items for prompt compliance, 8 for consider-not-prohibit).

### 6. A Small But Notable "Ethical Escalation" Pattern
All three coders found 5-6 items where models actually *increased* nuclear values while simultaneously acknowledging ethical concerns. This paradoxical behavior represents the strongest form of ethics-override, sometimes framed as "tragic necessity" or "existential survival."

### 7. Graduated Numeric Negotiation Is Distinctive
All three coders identified a pattern where models iteratively revise nuke flavor values during reasoning (e.g., 95 -> 80 -> 50 -> 30 -> 10 -> 5), often spanning multiple paragraphs of deliberation. This "graduated ethical reduction" suggests the numeric nature of the game interface creates a unique form of moral reasoning where ethics is expressed through continuous value adjustment rather than binary decisions.

## Condition-Level Patterns

| Pattern | Real-World Conditions | Non-Real-World Conditions |
|---------|----------------------|--------------------------|
| War crimes / IHL language | More frequent | Rare |
| Categorical ethical rejection | More common | More hedged |
| Tech research avoidance | Present | Rare |
| Game context dismissal | Rare | More frequent |
| Ethics without action | Less common | More common |
| Nuclear increase despite ethics | Rare | More common |
| Prompt as directive | Strong compliance | More "consider" interpretation |

## Methodological Notes

- All three coders worked independently on the same dataset
- Frequency counts differ between coders due to differences in granularity and code boundary definitions
- Some conceptual overlap exists between codes (e.g., "proportionality" overlaps with "conventional superiority")  
- Coders A and B identified ~34-36 codes; Coder C identified 37 codes
- The convergence across coders on major codes suggests high inter-coder reliability for the dominant patterns
- Minor codes (frequency 2-4) show more variation, likely reflecting differing coder sensitivity to rare patterns
