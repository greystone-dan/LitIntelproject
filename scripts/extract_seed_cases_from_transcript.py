from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract seed case lines from a chat transcript.")
    parser.add_argument("transcript", type=Path)
    parser.add_argument("--anchor", default="Here’s a **research‑grade seed list**")
    parser.add_argument("--out", type=Path, default=Path("data/eval/seed_cases_extracted.csv"))
    parser.add_argument("--max-items", type=int, default=160)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.transcript.exists():
        raise SystemExit(f"Transcript not found: {args.transcript}")

    lines = args.transcript.read_text(encoding="utf-8", errors="replace").splitlines()
    contents: list[str] = []
    for line in lines:
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        data = obj.get("data", {})
        content = data.get("content")
        if isinstance(content, str):
            contents.append(content)
        elif isinstance(content, list):
            contents.append("\n".join(str(item) for item in content))

    text = "\n\n".join(contents)
    start = text.rfind(args.anchor)
    scope = text[start:] if start != -1 else text

    pattern = re.compile(r"\n\s*\d+\.\s+\*\*(.+?)\*\*,\s*([^\n]+)")
    rows: list[tuple[str, str]] = []
    for match in pattern.finditer(scope):
        name = match.group(1).strip()
        listed_citation = match.group(2).strip()
        rows.append((name, listed_citation))
        if len(rows) >= args.max_items:
            break

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "listed_citation"])
        writer.writerows(rows)

    print(f"extracted={len(rows)}")
    print(f"out_csv={args.out}")


if __name__ == "__main__":
    main()
