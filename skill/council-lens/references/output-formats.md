<!-- SPDX-License-Identifier: Apache-2.0 -->

# Output formats

Adapt to the task. Do not add empty sections.

## Fast Council

```markdown
## Council Lens: [topic]

- **Risk:** [sharp downside]
- **First principles:** [reframe]
- **Opportunity:** [upside]
- **Outside view:** [stakeholder/base-rate insight]
- **Operator:** [execution reality]

**Synthesis:** [recommendation or tradeoff + main reason]
**Key uncertainty:** [fact/assumption most likely to flip the answer]
**Do this first:** [one concrete action]
```

## Standard Council

Prefer a compact table when it improves scanability:

```markdown
## Council Lens: [topic]

| Lens | Current view | Strongest reason | Flip condition |
|---|---|---|---|
| Risk | ... | ... | ... |
| First principles | ... | ... | ... |
| Opportunity | ... | ... | ... |
| Outside view | ... | ... | ... |
| Operator | ... | ... | ... |

### Evidence that matters
- Verified: ...
- Assumed/unknown: ...

### Where the council converges
...

### Real disagreement / blind spot
...

### Recommendation
...

**Confidence:** low / medium / high — [brief reason]

### One thing to do first
...
```

## Deep Council

Use when stronger evidence, files, calculations, or current research materially matter.

Possible sections:

- Executive verdict
- Decision frame
- Council briefs
- Specialist lens, if used
- Evidence audit with citations where required
- Disconfirming evidence
- Convergence and real disagreement
- Dominant constraint or biggest blind spot
- Recommendation / decision-relevant tradeoffs
- Flip and kill conditions
- One immediate experiment or action

Do not inflate length merely because Deep mode was selected.

## Decision matrix

Use only when the user has 3+ comparable options and explicit criteria.

- Derive criteria from the user's objective.
- Use transparent weights only if the user supplies them or they can be plainly justified.
- Prefer qualitative labels when evidence cannot support precise numbers.
- Do not turn subjective guesses into fake decimal scores.
