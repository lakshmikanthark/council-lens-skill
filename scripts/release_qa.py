#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Adversarial release QA with negative controls."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(script: str, cwd: Path = ROOT, expect: int = 0) -> subprocess.CompletedProcess[str]:
    p = subprocess.run([sys.executable, script], cwd=cwd, text=True, capture_output=True)
    if p.returncode != expect:
        print(p.stdout)
        print(p.stderr, file=sys.stderr)
        raise AssertionError(f"{script} returned {p.returncode}, expected {expect}")
    return p


def copy_repo(dst: Path) -> Path:
    target = dst / "repo"
    shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns("__pycache__", ".git", ".unlazy"))
    return target


def negative_secret_control() -> None:
    with tempfile.TemporaryDirectory() as td:
        r = copy_repo(Path(td))
        (r / "NEGATIVE_CONTROL.md").write_text("fake " + "AK" + "IA" + "ABCDEFGHIJKLMNOP\n", encoding="utf-8")
        run("scripts/validate_repo.py", r, expect=1)


def negative_broken_link_control() -> None:
    with tempfile.TemporaryDirectory() as td:
        r = copy_repo(Path(td))
        with (r / "README.md").open("a", encoding="utf-8") as f:
            f.write("\n[broken](docs/definitely-missing.md)\n")
        run("scripts/validate_repo.py", r, expect=1)


def negative_zip_traversal_control() -> None:
    with tempfile.TemporaryDirectory() as td:
        r = copy_repo(Path(td))
        bad = r / "dist" / "skill.zip"
        bad.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(bad, "w") as zf:
            zf.writestr("../escape.txt", "nope")
        run("scripts/validate_repo.py", r, expect=1)


def clean_copy_reproducibility() -> None:
    with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
        ra = copy_repo(Path(a))
        rb = copy_repo(Path(b))
        run("scripts/build_skill.py", ra)
        run("scripts/build_skill.py", rb)
        za = (ra / "dist" / "skill.zip").read_bytes()
        zb = (rb / "dist" / "skill.zip").read_bytes()
        if za != zb:
            raise AssertionError("Clean-copy builds are not byte-identical")


def main() -> int:
    run("scripts/validate_repo.py")
    run("scripts/build_skill.py")
    p = subprocess.run([sys.executable, "scripts/build_skill.py", "--check-reproducible"], cwd=ROOT)
    if p.returncode:
        raise AssertionError("Reproducibility check failed")
    p = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=ROOT)
    if p.returncode:
        raise AssertionError("Unit tests failed")
    clean_copy_reproducibility()
    negative_secret_control()
    negative_broken_link_control()
    negative_zip_traversal_control()
    print("RELEASE QA PASSED")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"RELEASE QA FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
