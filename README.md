<!-- SPDX-License-Identifier: Apache-2.0 -->

# Council Lens

**A decision-review Skill for ChatGPT that pressure-tests consequential choices through separated analytical lenses, evidence audit, blind challenge, and synthesis.**

> Independent community project. Not affiliated with, endorsed by, or sponsored by OpenAI. ChatGPT and OpenAI are trademarks of OpenAI.

Council Lens is designed for the moment when a normal “pros and cons” answer is not enough. It forces a decision through deliberately different jobs: attack the plan, rebuild it from first principles, search for leverage, inspect the outside view, and test execution reality. Then it audits the evidence, challenges the briefs without role labels, and synthesizes a recommendation without simple majority voting.

## Why this is different from “ask for five opinions”

A weak multi-perspective prompt often produces five versions of the same answer. Council Lens adds structure that makes disagreement useful:

- **Five separated lenses** with non-overlapping jobs.
- **Flip conditions**: each lens states what evidence could reverse its view.
- **Evidence audit**: verified facts, user-provided facts, estimates, assumptions, and unknowns are separated.
- **Blind challenge**: arguments are stress-tested without relying on their role labels.
- **No majority vote**: irreversible downside or decisive evidence can outweigh four weaker opinions.
- **Dominant-constraint rule**: if a verified hard constraint settles an option, the council stops pretending the tradeoff is balanced.
- **Experiment-before-commitment**: uncertainty is converted into a reversible test when possible.
- **Optional specialist lens** in Deep mode when one domain blind spot actually matters.
- **No fake agent claims**: five lenses are not described as five independent models unless independent execution really occurred.

## The five core lenses

| Lens | Job |
|---|---|
| Adversary / Risk | Find failure modes, lock-in, hidden downside and second-order effects |
| First Principles | Reconstruct the real objective and challenge assumed constraints |
| Opportunity / Leverage | Find asymmetric upside, optionality and compounding value |
| Outside View / Stakeholder | Apply base expectations and the perspective of the stakeholder who can make the plan succeed or fail |
| Operator / Experiment | Test feasibility, sequence, bottlenecks, kill criteria and the smallest reversible next step |

## Adaptive depth

Council Lens uses the lightest level that preserves decision quality:

- **Fast** — bounded meaningful choices.
- **Standard** — important multi-factor decisions.
- **Deep** — expensive, hard-to-reverse, highly uncertain or evidence-heavy decisions; files, current research, calculations and one optional specialist lens can be used when material.

Deep means better evidence and stronger challenge, not merely a longer answer.

## Example

```text
Council this: should I launch my product free first or charge from day one?
```

A typical Standard Council response includes a compact view from each lens, evidence that matters, real disagreement, the biggest blind spot, a recommendation, confidence expressed only as low/medium/high, and one concrete first action.

More examples: [`examples/prompts.md`](examples/prompts.md)

## Install

1. Download [`dist/skill.zip`](dist/skill.zip).
2. Open your ChatGPT Skill library at `/skills`.
3. Upload `skill.zip`.
4. Try: `Council this: <your decision>`.

The distributable package contains the Skill source, progressive references, metadata, notice, and a copy of the Apache-2.0 license so the standalone ZIP carries its reuse terms with it.

## Repository structure

```text
council-lens-skill/
├── skill/council-lens/
│   ├── SKILL.md
│   ├── NOTICE
│   ├── LICENSE
│   ├── agents/openai.yaml
│   └── references/
├── evals/cases.json
├── tests/
├── scripts/
│   ├── validate_skill.py
│   ├── build_skill.py
│   ├── validate_repo.py
│   ├── release_qa.py
│   └── build_release.py
├── docs/
├── examples/
├── dist/skill.zip
├── LICENSE
├── NOTICE
├── THIRD_PARTY_NOTICES.md
└── README.md
```

## Build and validate

Requires Python 3.10+ and no third-party Python packages.

```bash
python scripts/validate_skill.py
python scripts/build_skill.py --check-reproducible
python -m unittest discover -s tests -v
python scripts/validate_repo.py
python scripts/release_qa.py
```

The builder normalizes ZIP ordering, timestamps, permissions and compression so identical Skill source bytes produce identical `skill.zip` bytes.

## Evaluation contract

The repository ships static evaluation cases covering product strategy, architecture, high-stakes commitments, false dichotomies, political neutrality, medical/legal guardrails, preferred-option bias, dominant constraints, non-trigger cases and file-backed Deep Council requests.

See [`docs/EVALUATION.md`](docs/EVALUATION.md) and [`evals/cases.json`](evals/cases.json).

## Safety and scope

Council Lens is decision-support infrastructure, not a substitute for licensed professional judgment. High-stakes topics must surface uncertainty and verification steps. Political/electoral requests are handled neutrally rather than turning the council into an endorsement engine. Consequential external actions require confirmation before execution when applicable.

See [`SECURITY.md`](SECURITY.md) and the Skill's [`guardrails.md`](skill/council-lens/references/guardrails.md).

## License

This repository's **original implementation and documentation are licensed under Apache License 2.0**. Apache-2.0 was chosen to make reuse terms explicit, provide a standard patent grant, and avoid the ambiguity of publishing source with no software license.

The license does **not** apply to third-party projects merely referenced for conceptual attribution, and it does not grant rights in third-party trademarks. See [`NOTICE`](NOTICE), [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md), and [`docs/PROVENANCE.md`](docs/PROVENANCE.md).

## Provenance

Council Lens is an independent implementation. It acknowledges public council-style LLM work by Andrej Karpathy and Ole Lehmann as conceptual inspiration, but no source files or prompt/documentation text from those repositories are included here.

This distinction matters because, as reviewed on 2026-09-29, the referenced repositories did not expose a clear repository-root license granting redistribution rights. The project therefore uses the ideas at a high level while shipping independently written implementation and documentation.

## Contributing

Issues and pull requests are welcome. By contributing, you represent that you have the right to submit the contribution and agree that it is licensed under Apache-2.0 as part of this project. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Project story

For a portfolio/interview-ready explanation of the problem, design decisions and result, see [`docs/STAR.md`](docs/STAR.md).
