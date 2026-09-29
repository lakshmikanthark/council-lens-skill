#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Build a deterministic GitHub-ready source release ZIP outside the repository."""
from __future__ import annotations

import argparse
import hashlib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXED_DATE = (1980, 1, 1, 0, 0, 0)
EXCLUDE_PARTS = {".git", "__pycache__", ".unlazy"}
EXCLUDE_NAMES = {".DS_Store", "Thumbs.db"}


def sha256(path: Path) -> str:
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    return h


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", nargs="?", default=str(ROOT.parent / "council-lens-skill-github.zip"))
    args = parser.parse_args()
    output = Path(args.output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    files = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_PARTS for part in rel.parts) or p.name in EXCLUDE_NAMES:
            continue
        files.append(p)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as zf:
        for p in sorted(files, key=lambda x: x.relative_to(ROOT).as_posix()):
            arc = f"council-lens-skill/{p.relative_to(ROOT).as_posix()}"
            info = zipfile.ZipInfo(arc, FIXED_DATE)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            zf.writestr(info, p.read_bytes())
    print(f"RELEASE BUILT {output} sha256={sha256(output)} files={len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
