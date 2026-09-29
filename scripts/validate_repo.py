#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Static release checks for the Council Lens GitHub repository."""
from __future__ import annotations

import re
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".txt", ".py", ".yaml", ".yml", ".json", ".cff", ""}
SKIP_DIRS = {".git", "__pycache__", ".unlazy"}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "aws access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "openai-like secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
}
CONTROL_RE = re.compile("[\u202A-\u202E\u2066-\u2069\u200B\uFEFF]")


def fail(msg: str) -> None:
    raise AssertionError(msg)


def iter_files():
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        yield p


def scan_text_safety() -> None:
    for path in iter_files():
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE", "NOTICE"}:
            continue
        data = path.read_bytes()
        if b"\x00" in data:
            fail(f"NUL byte in text file: {path.relative_to(ROOT)}")
        text = data.decode("utf-8")
        if CONTROL_RE.search(text):
            fail(f"Hidden bidi/zero-width control in: {path.relative_to(ROOT)}")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                fail(f"Potential {label} in {path.relative_to(ROOT)}")


def check_license_and_provenance() -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if "Apache License" not in license_text or "Version 2.0, January 2004" not in license_text:
        fail("LICENSE is not recognizable Apache-2.0 text")
    skill_license = (ROOT / "skill" / "council-lens" / "LICENSE").read_text(encoding="utf-8")
    if skill_license != license_text:
        fail("Bundled Skill LICENSE must exactly match repository LICENSE")
    notice = (ROOT / "NOTICE").read_text(encoding="utf-8")
    third = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
    for phrase in ("original implementation", "does not grant rights", "OpenAI", "ChatGPT"):
        if phrase not in notice:
            fail(f"NOTICE missing legal boundary phrase: {phrase}")
    for url in ("github.com/karpathy/llm-council", "github.com/aiwithremy/claude-skills-llm-council"):
        if url not in third:
            fail(f"Missing attribution URL: {url}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "Council Lens" not in readme:
        fail("README product name mismatch")
    first_heading = next((line for line in readme.splitlines() if line.startswith("# ")), "")
    if "ChatGPT" in first_heading or "GPT" in first_heading:
        fail("OpenAI mark used in project title")
    if "not affiliated with, endorsed by, or sponsored by openai" not in readme.lower():
        fail("README missing OpenAI non-affiliation notice")


def check_markdown_links() -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in iter_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for target in link_re.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"Markdown link escapes repo: {path.relative_to(ROOT)} -> {target}")
            if not resolved.exists():
                fail(f"Broken local link: {path.relative_to(ROOT)} -> {target}")


def check_zip(path: Path) -> None:
    if not path.is_file():
        fail(f"Missing ZIP: {path.relative_to(ROOT)}")
    with zipfile.ZipFile(path) as zf:
        for info in zf.infolist():
            name = info.filename
            posix = PurePosixPath(name)
            if posix.is_absolute() or ".." in posix.parts or "\\" in name:
                fail(f"Unsafe ZIP entry: {name}")
            mode = (info.external_attr >> 16) & 0o170000
            if mode == 0o120000:
                fail(f"Symlink in ZIP: {name}")


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_skill.py")], check=True)
    scan_text_safety()
    check_license_and_provenance()
    check_markdown_links()
    if (ROOT / "dist" / "skill.zip").exists():
        check_zip(ROOT / "dist" / "skill.zip")
    print("REPO VALIDATION PASSED")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, UnicodeDecodeError, zipfile.BadZipFile) as exc:
        print(f"REPO VALIDATION FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
