<!-- SPDX-License-Identifier: Apache-2.0 -->

# Release QA

A release is accepted only after all of these layers pass:

1. `scripts/validate_skill.py` — native Skill contract and progressive-reference checks.
2. `python -m unittest discover -s tests -v` — protocol/guardrail/eval-schema unit tests.
3. `scripts/build_skill.py --check-reproducible` — deterministic package proof.
4. `scripts/validate_repo.py` — license, provenance, links, secret patterns, Unicode controls and archive-safety checks.
5. `scripts/release_qa.py` — clean-copy rebuild plus adversarial negative controls.
6. Independent ChatGPT Skill packaging/validation during release preparation.

Negative controls deliberately inject:

- an AWS-style credential pattern;
- a broken local Markdown link;
- an archive traversal path.

The QA is intentionally capable of failing. A green run is evidence for the checks above, not a legal or security guarantee beyond their scope.
