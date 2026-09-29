<!-- SPDX-License-Identifier: Apache-2.0 -->

# Provenance and licensing rationale

## What is original here

The files shipped in this repository were independently written for Council Lens. The implementation includes its own Skill structure, lens definitions, adaptive depth logic, evidence audit, blind challenge, dominant-constraint rule, experiment-before-commitment rule, output formats, guardrails, build tooling, tests, evaluation cases and GitHub release infrastructure.

## What inspired the project

Two public projects informed the high-level idea:

- Andrej Karpathy's `karpathy/llm-council`, which publicly describes collecting multiple LLM responses, peer reviewing them and synthesizing a final answer.
- Ole Lehmann's `aiwithremy/claude-skills-llm-council`, which publicly describes a council workflow adapted as a Claude skill.

Those projects are **references, not dependencies**.

## Why no upstream code or prose is included

Public GitHub visibility does not itself grant permission to copy or redistribute copyrighted source. As reviewed on 2026-09-29, we did not find a repository-root software license granting redistribution rights in either referenced repository. Therefore Council Lens does not vendor, copy, translate, or redistribute their source files or documentation/prompt text.

The project uses the general idea of multi-perspective deliberation and implements it independently.

## License choice

Council Lens's original materials use **Apache License 2.0** because it provides clear permissions, conditions, warranty disclaimer and an explicit patent license. This makes the GitHub repository unambiguously reusable without pretending to grant rights in third-party projects.

The `NOTICE` and `THIRD_PARTY_NOTICES.md` files make that boundary explicit.

## Brand boundary

The product name is `Council Lens`. `ChatGPT` appears only to describe the compatible host. The project does not use OpenAI logos and includes a non-affiliation notice.

This document describes the project's release-engineering posture, not legal advice or a guarantee against every possible claim.
