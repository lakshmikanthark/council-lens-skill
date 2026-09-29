#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validate the Council Lens ChatGPT Skill using only Python stdlib."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "council-lens"
SKILL_MD = SKILL / "SKILL.md"
OPENAI_YAML = SKILL / "agents" / "openai.yaml"
MAX_DESCRIPTION = 1024
MAX_SKILL_MD_LINES = 500


def fail(message: str) -> None:
    raise AssertionError(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        fail("SKILL.md frontmatter is not closed")
    block = text[4:end]
    data: dict[str, str] = {}
    for raw in block.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            fail(f"Unsupported frontmatter line: {raw}")
        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in data:
            fail(f"Duplicate frontmatter key: {key}")
        data[key] = value
    return data


def main() -> int:
    if not SKILL_MD.is_file():
        fail("Missing skill/council-lens/SKILL.md")
    if not OPENAI_YAML.is_file():
        fail("Missing skill/council-lens/agents/openai.yaml")
    if not (SKILL / "LICENSE").is_file():
        fail("Missing skill/council-lens/LICENSE")

    text = SKILL_MD.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if set(fm) != {"name", "description"}:
        fail(f"Frontmatter must contain only name and description, got: {sorted(fm)}")
    if fm["name"] != "council-lens":
        fail("Skill name must be council-lens")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", fm["name"]):
        fail("Skill name is not valid hyphen-case")
    if not fm["description"] or len(fm["description"]) > MAX_DESCRIPTION:
        fail("Skill description must be non-empty and <= 1024 characters")
    if "<" in fm["description"] or ">" in fm["description"]:
        fail("Skill description cannot contain angle brackets")
    if len(text.splitlines()) > MAX_SKILL_MD_LINES:
        fail("SKILL.md exceeds progressive-loading target of 500 lines")

    required_refs = {
        "references/protocol.md",
        "references/output-formats.md",
        "references/guardrails.md",
    }
    for rel in required_refs:
        if not (SKILL / rel).is_file():
            fail(f"Missing reference: {rel}")
        if rel not in text:
            fail(f"SKILL.md does not link directly to {rel}")

    meta = OPENAI_YAML.read_text(encoding="utf-8")
    for token in ("display_name:", "Council Lens", "short_description:"):
        if token not in meta:
            fail(f"agents/openai.yaml missing {token}")

    lower = text.lower()
    banned = [
        "claude code",
        "claude cowork",
        "task tool",
        "five ai advisors",
        "five independent agents",
    ]
    for phrase in banned:
        if phrase in lower:
            fail(f"Claude/fake-agent residue found: {phrase}")

    must_have = [
        "flip condition",
        "blind challenge",
        "dominant constraint",
        "political",
        "external actions",
        "never imply that independent models",
    ]
    combined = "\n".join(
        p.read_text(encoding="utf-8")
        for p in [SKILL_MD, *[SKILL / r for r in sorted(required_refs)]]
    ).lower()
    for phrase in must_have:
        if phrase not in combined:
            fail(f"Required protocol concept missing: {phrase}")

    print("SKILL VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"SKILL VALIDATION FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
