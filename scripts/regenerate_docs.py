"""Regenerate every checked-in generated doc and sync the backend file inventory.

Run this before pushing any change that adds, renames or removes a script or a
file under backend/, or changes routes or tables:

    python scripts/regenerate_docs.py

It rewrites docs/API_REFERENCE.generated.md, docs/SCHEMA_REFERENCE.generated.md
and docs/SCRIPT_CATALOG.generated.md, then adds a row to the backend inventory in
docs/ARCHITECTURE.md for each new backend file (description taken from the
module docstring; edit it afterwards if you like) and drops rows for files that
no longer exist. Finally it runs scripts/check_generated_docs.py.
"""

from __future__ import annotations

import ast
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHITECTURE = ROOT / "docs" / "ARCHITECTURE.md"
GENERATORS = (
    "scripts/generate_api_reference.py",
    "scripts/generate_schema_reference.py",
    "scripts/generate_script_catalog.py",
)
ROW = re.compile(r"^\| `(backend/[^`]+)` \|")


def describe(path: Path) -> str:
    if path.suffix == ".py":
        try:
            doc = ast.get_docstring(ast.parse(path.read_text(encoding="utf-8")))
        except (SyntaxError, UnicodeDecodeError):
            doc = None
        if doc:
            line = doc.strip().splitlines()[0].strip().rstrip(".")
            return line.replace("|", "/")
    return "TODO: describe this file"


def sync_inventory() -> tuple[list[str], list[str]]:
    lines = ARCHITECTURE.read_text(encoding="utf-8").splitlines()
    rows = [i for i, line in enumerate(lines) if ROW.match(line)]
    first, last = rows[0], rows[-1]
    existing = {ROW.match(lines[i]).group(1): lines[i] for i in rows}
    on_disk = {
        p.relative_to(ROOT).as_posix(): p
        for p in (ROOT / "backend").rglob("*")
        if p.is_file() and "__pycache__" not in p.parts
    }
    added = sorted(set(on_disk) - set(existing))
    removed = sorted(set(existing) - set(on_disk))
    table = {k: v for k, v in existing.items() if k in on_disk}
    for name in added:
        table[name] = f"| `{name}` | {describe(on_disk[name])} |"
    new_rows = [table[k] for k in sorted(table)]
    if added or removed:
        lines[first:last + 1] = new_rows
        ARCHITECTURE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return added, removed


def main() -> int:
    for generator in GENERATORS:
        result = subprocess.run([sys.executable, str(ROOT / generator)], cwd=ROOT)
        if result.returncode:
            print(f"generator failed: {generator}")
            return result.returncode
    added, removed = sync_inventory()
    for name in added:
        print(f"ARCHITECTURE.md: added {name}")
    for name in removed:
        print(f"ARCHITECTURE.md: removed {name}")
    return subprocess.run([sys.executable, str(ROOT / "scripts/check_generated_docs.py")], cwd=ROOT).returncode


if __name__ == "__main__":
    raise SystemExit(main())
