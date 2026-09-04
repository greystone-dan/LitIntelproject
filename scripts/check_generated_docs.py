"""Check that checked-in generated documentation matches its generators."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATED = {
    "scripts/generate_api_reference.py": "docs/API_REFERENCE.generated.md",
    "scripts/generate_schema_reference.py": "docs/SCHEMA_REFERENCE.generated.md",
    "scripts/generate_script_catalog.py": "docs/SCRIPT_CATALOG.generated.md",
}
def normalized(path: Path) -> str:
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("Generated:"):
            line = "Generated: <normalized>"
        elif line.startswith("Last generated:"):
            line = "Last generated: <normalized>"
        lines.append(line)
    return "\n".join(lines) + "\n"


def main() -> int:
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="caselibrary-generated-docs-") as directory:
        temp_root = Path(directory)
        for generator, output in GENERATED.items():
            temp_output = temp_root / output
            command = [
                sys.executable,
                str(ROOT / generator),
                "--output",
                str(temp_output),
            ]
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
            if result.returncode:
                print(result.stdout, end="")
                print(result.stderr, end="", file=sys.stderr)
                failures.append(f"generator failed: {generator}")
                continue
            checked_in = ROOT / output
            if not checked_in.exists() or normalized(checked_in) != normalized(temp_output):
                failures.append(output)

    if failures:
        print("Generated documentation drift detected:")
        for failure in failures:
            print(f"- {failure}")
        print("Run the corresponding generator and review the resulting diff.")
        return 1
    print(f"Generated documentation is current ({len(GENERATED)} references checked).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
