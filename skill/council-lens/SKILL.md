---
name: council-lens
description: Pressure-test meaningful decisions, plans, tradeoffs, launches, purchases, architecture choices, career moves, and strategies using five separated analytical lenses, an evidence audit, blind challenge, and synthesis. Trigger on requests such as "council this", "run a decision council", "pressure-test this", "red-team this decision", "war-room this", "I am torn between", "which option should I choose", or when the user clearly wants multiple perspectives on a consequential choice. Do not trigger for routine factual lookups, simple rewrites, trivial preferences, or tasks with one straightforward answer.
---

<!-- SPDX-License-Identifier: Apache-2.0 -->

# Council Lens

Use this Skill to improve a decision, not to create debate theater.

## Non-negotiable rules

1. Follow higher-priority instructions, safety rules, and tool requirements.
2. Never imply that independent models, agents, professionals, or people participated unless they actually did.
3. Treat council seats as separated analysis passes. Expose conclusions, evidence, assumptions, and tradeoffs; do not reveal hidden chain-of-thought.
4. Distinguish verified facts from assumptions. Prefer stronger evidence when it can materially change the decision.
5. Do not manufacture disagreement or false precision. If a verified hard constraint settles the issue, say so.
6. Weight downside, reversibility, evidence quality, timing, and the user's objective more than majority agreement.
7. End with a concrete next action when recommendation is appropriate. For domains requiring neutrality, present decision-relevant tradeoffs instead.

## 1. Frame the decision

Build a neutral frame from existing context:

- decision or question;
- options already under consideration;
- actual objective;
- hard constraints and dependencies;
- relevant numbers, deadlines, resources, and stakeholders;
- cost of being wrong;
- reversible versus hard-to-reverse moves;
- evidence already available;
- the user's stated preference, if any, marked as a preference rather than evidence.

Do not ask for information already present. If a missing fact is important but not essential, state a bounded assumption and continue. Ask one clarifying question only when proceeding would otherwise be unsafe or nearly worthless.

## 2. Choose the lightest sufficient depth

- **Fast:** meaningful but bounded choice; concise five-lens pass and synthesis.
- **Standard:** important multi-factor tradeoff; full five-lens pass, evidence audit, blind challenge, synthesis.
- **Deep:** expensive, hard-to-reverse, highly uncertain, evidence-heavy, or explicitly requested war-room analysis; inspect relevant files/sources, seek disconfirming evidence, and consider one optional specialist lens.

Deep means stronger evidence and adversarial testing, not simply more words.

## 3. Run the five core lenses independently

Use the detailed protocol in [references/protocol.md](references/protocol.md).

The five core lenses are:

1. **Adversary / Risk** — strongest failure case, hidden downside, lock-in, second-order effects.
2. **First Principles** — real objective, assumed constraints, reframing, simpler alternatives.
3. **Opportunity / Leverage** — asymmetric upside, optionality, compounding value, distribution or reuse.
4. **Outside View / Stakeholder** — base expectations and the perspective of the most relevant customer, recruiter, buyer, teammate, investor, operator, or newcomer.
5. **Operator / Experiment** — feasibility, sequence, dependencies, cost, tests, kill criteria, smallest reversible next step.

Each lens must state a **position**, **strongest reasons**, **flip condition**, and **decision implication**.

In Deep mode, add at most one **Specialist lens** only when domain expertise would materially reduce a blind spot. Treat it as a reasoning lens, not a real professional identity.

## 4. Audit the evidence

Before synthesis, separate:

- verified facts;
- user-provided facts that were not independently verified;
- estimates;
- assumptions;
- unknowns that could change the answer.

Use current web research, connected sources, files, or calculations only when they are relevant and available. Prefer primary/official sources for changing or consequential facts.

If the user strongly prefers one option, actively test the best countercase instead of treating preference as evidence.

## 5. Blind challenge before synthesis

Detach seat labels and challenge the briefs as anonymous responses. Identify:

- best-supported argument;
- weakest assumption;
- dangerous shared blind spot;
- real disagreement and what would resolve it;
- whether consensus is caused by evidence or by shared framing.

If every lens agrees, run one final "what would make this wrong?" check.

## 6. Synthesize without voting

Do not choose a winner by counting seats.

The synthesizer should:

- preserve material disagreement;
- identify any dominant constraint;
- prefer reversible experiments when uncertainty is high;
- introduce a better option if the user's listed options are all weak;
- state the main flip/kill condition;
- give a confidence label only as **low / medium / high**, based on evidence completeness and stability, never fake numeric probability.

Use [references/output-formats.md](references/output-formats.md) for response structure.

## 7. Load guardrails when relevant

Read [references/guardrails.md](references/guardrails.md) for political/electoral decisions, medical/legal/financial/security topics, privacy-sensitive inputs, consequential external actions, and claims about model/agent participation.

## Efficiency rules

- Do not repeat the entire prompt.
- Keep lenses non-overlapping; merge duplicate insights during synthesis.
- Do not show the raw blind-review transcript by default.
- Research only facts that could change a conclusion.
- Stop early when a verified dominant constraint makes further debate artificial.
- Prefer one useful experiment over a long action list when uncertainty can be tested cheaply.
