#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build a byte-reproducible ChatGPT skill.zip."""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "council-lens"
DIST = ROOT / "dist"
OUT = DIST / "skill.zip"
FIXED_DATE = (1980, 1, 1, 0, 0, 0)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build(output: Path) -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_skill.py")], check=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in SKILL.rglob("*") if p.is_file())
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as zf:
        for path in files:
            rel = path.relative_to(SKILL.parent).as_posix()
            info = zipfile.ZipInfo(rel, FIXED_DATE)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            zf.writestr(info, path.read_bytes())


def check_reproducible() -> None:
    first = DIST / ".skill.first.zip"
    second = DIST / ".skill.second.zip"
    try:
        build(first)
        build(second)
        if first.read_bytes() != second.read_bytes():
            raise AssertionError("Two builds from identical source are not byte-identical")
        print(f"REPRODUCIBLE BUILD PASSED sha256={sha256(first)}")
    finally:
        first.unlink(missing_ok=True)
        second.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-reproducible", action="store_true")
    args = parser.parse_args()
    if args.check_reproducible:
        check_reproducible()
    build(OUT)
    print(f"BUILT {OUT} sha256={sha256(OUT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
