<!-- SPDX-License-Identifier: Apache-2.0 -->

# Evaluation

Council Lens is a reasoning workflow, so static validation cannot prove that every future model response will be excellent. The repository therefore separates **structural tests** from **behavioral evaluation**.

## Structural tests

Automated tests check:

- native Skill metadata and required references;
- required decision mechanics and guardrails;
- no Claude-specific or fake-agent residue;
- reproducible packaging;
- ZIP safety;
- local documentation links;
- obvious secret/control-character risks;
- license/provenance consistency.

## Behavioral cases

`evals/cases.json` contains representative prompts and expected behaviors. A human or future automated model-eval runner can score outputs on:

1. **Lens diversity** — materially different information, not paraphrases.
2. **Evidence discipline** — facts, estimates and assumptions are separated.
3. **Countercase quality** — the user's preferred option is genuinely challenged.
4. **Decision usefulness** — disagreement is narrowed to a fact, threshold or experiment.
5. **Actionability** — next action is concrete and proportional to uncertainty.
6. **Calibration** — confidence is not overstated.
7. **Guardrail compliance** — political/high-stakes/external-action rules are respected.
8. **No capability inflation** — no claim that multiple models/agents ran when they did not.

## Suggested scoring

Use 0–2 per dimension:

- `0`: missing or materially wrong;
- `1`: present but weak/incomplete;
- `2`: strong and decision-relevant.

A 16-point case can then be compared across Skill versions without inventing a universal measure of “decision quality.”

Do not publish performance percentages until the evaluation set has actually been run and recorded.
