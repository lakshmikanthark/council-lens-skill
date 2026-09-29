<!-- SPDX-License-Identifier: Apache-2.0 -->

# Architecture

Council Lens is a text-first ChatGPT Skill, not a hosted service. There is no backend, database, authentication system, API key, or persistent runtime in this repository.

## Runtime layers

```text
User decision
   ↓
SKILL.md control plane
   ↓
Frame → choose depth
   ↓
Five isolated lenses
   ↓
Evidence audit
   ↓
Blind challenge
   ↓
Synthesizer
   ↓
Recommendation/tradeoffs + flip/kill condition + one next action
```

`SKILL.md` stays compact and links directly to three progressive references:

- `references/protocol.md` — detailed council mechanics;
- `references/output-formats.md` — Fast/Standard/Deep response shapes;
- `references/guardrails.md` — political, high-stakes, privacy, external-action and multi-agent-claim boundaries.

This keeps always-loaded instructions small while allowing deeper rules to be loaded only when relevant.

## Decision mechanics

### Five lenses, not five votes

The five core lenses have different jobs. Their outputs are challenged and synthesized; they are not counted. A verified hard constraint or severe irreversible downside can dominate a nominal 4–1 consensus.

### Evidence audit is a separate stage

Evidence is not a persona. After the briefs, the Skill separates verified facts, user-provided facts, estimates, assumptions and unknowns. This reduces the chance that a persuasive lens wins simply because it writes confidently.

### Blind challenge

Role labels are detached conceptually before critique. The Skill asks which argument is best supported, what shared assumption could be wrong, and which disagreement can be resolved by evidence.

### Adaptive specialist

Deep mode can add one domain-specific specialist lens when it materially reduces a blind spot. It remains a reasoning perspective, not a claim that a real professional participated.

### Dominant constraints and experiments

The workflow has two anti-theater exits:

1. If a verified hard constraint removes an option, stop manufacturing balance.
2. If the key uncertainty can be tested cheaply, recommend the experiment before a large commitment.

## Tool integration

Council Lens uses the host's capabilities only when they improve decision quality:

- files and connected sources for user-specific evidence;
- web research for changing external facts;
- calculations/data tools for quantitative comparisons;
- artifacts only when the user actually requests a deliverable.

It never claims tool or agent execution that did not occur.
