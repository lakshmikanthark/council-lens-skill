<!-- SPDX-License-Identifier: Apache-2.0 -->

# Project story — STAR

## Situation

Important decisions made with a single LLM response can be vulnerable to framing bias, shallow “pros and cons,” unverified assumptions, and overconfident synthesis. Public council-style LLM projects demonstrated that independent viewpoints plus review can expose more of the decision surface, but existing examples were not packaged as a compact, evidence-aware, ChatGPT-native Skill with explicit release and safety controls.

## Task

Build an independent Council Lens Skill that makes multi-perspective review practical inside ChatGPT while remaining efficient, honest about its capabilities, reusable on GitHub, and safe to distribute under clear licensing terms.

## Action

I designed the Skill around five separated analytical jobs: adversarial risk, first-principles reframing, opportunity/leverage, outside stakeholder view, and execution/experimentation. I added Fast/Standard/Deep modes, flip conditions, an evidence-audit stage, blind challenge, dominant-constraint short-circuiting, anti-confirmation-bias rules, and an optional specialist lens for Deep mode.

I separated the Skill into a compact control plane plus progressive reference files, added high-stakes/political/external-action guardrails, and explicitly prevented false claims that independent agents/models participated when they did not.

For engineering quality, I built standard-library validators, behavioral contract tests, a static eval set, reproducible ZIP packaging, repository security/provenance checks, adversarial negative controls and GitHub Actions. I also separated conceptual attribution from shipped code and licensed the original implementation under Apache-2.0.

## Result

The result is a GitHub-ready, installable Council Lens Skill with a reproducible release pipeline and an explicit evaluation contract. The project can be used and modified under a standard open-source license while preserving third-party attribution boundaries and avoiding copied upstream source.

Outcome metrics such as adoption, decision-change rate and evaluation scores are intentionally not claimed until measured on real usage.

## Resume-ready direction after measurement

Once real usage data exists, quantify only measured outcomes, for example:

- number of council runs evaluated;
- average behavioral-eval score by version;
- percentage of cases where a flip condition changed the next action;
- cases where the council found a dominant constraint missed by the initial plan;
- build/QA pass rate across releases.
