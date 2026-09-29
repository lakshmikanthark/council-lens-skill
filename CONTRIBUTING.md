<!-- SPDX-License-Identifier: Apache-2.0 -->

# Contributing

Issues and pull requests are welcome.

By submitting a contribution, you represent that you have the right to submit it and agree that your contribution will be licensed under the repository's Apache License 2.0.

Please:

1. keep the Skill host-accurate and do not add fake multi-agent claims;
2. preserve political/high-stakes/external-action guardrails;
3. keep runtime instructions concise and move detail into direct reference files;
4. add or update tests/eval cases for behavior-changing edits;
5. run the complete local QA before opening a PR:

```bash
python scripts/release_qa.py
```

Do not submit third-party code, prompts, documentation, or assets unless their license clearly permits inclusion and the required attribution is added.
