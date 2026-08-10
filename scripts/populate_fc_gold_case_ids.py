"""Populate local_case_id in FC gold template from seed-to-case mapping."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

DEFAULT_GOLD_CSV = Path("data/eval/fc_citation_gold_template.csv")
DEFAULT_MAP_CSV = Path("data/eval/fc_priority_seed_case_map.csv")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold-csv", type=Path, default=DEFAULT_GOLD_CSV)
    parser.add_argument("--map-csv", type=Path, default=DEFAULT_MAP_CSV)
    parser.add_argument("--out-csv", type=Path, default=None)
    return parser.parse_args()


def _load_map(path: Path) -> dict[str, str]:
    if not path.exists():
        raise SystemExit(f"Map CSV not found: {path}")

    mapping: dict[str, str] = {}
    with path.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            status = str(row.get("status") or "")
            if status != "matched":
                continue
            source_row = str(row.get("source_row") or "").strip()
            local_case_id = str(row.get("local_case_id") or "").strip()
            if source_row and local_case_id:
                mapping[source_row] = local_case_id
    return mapping


def main() -> None:
    args = parse_args()
    if not args.gold_csv.exists():
        raise SystemExit(f"Gold CSV not found: {args.gold_csv}")

    out_csv = args.out_csv or args.gold_csv
    mapping = _load_map(args.map_csv)

    with args.gold_csv.open("r", encoding="utf-8", newline="") as file_obj:
        rows = list(csv.DictReader(file_obj))
        fieldnames = list(rows[0].keys()) if rows else []

    if not fieldnames:
        raise SystemExit("Gold CSV has no header/rows")

    updated = 0
    for row in rows:
        source_row = str(row.get("seed_source_row") or "").strip()
        if not source_row:
            continue
        local_case_id = mapping.get(source_row)
        if not local_case_id:
            continue
        if str(row.get("local_case_id") or "").strip() == local_case_id:
            continue
        row["local_case_id"] = local_case_id
        updated += 1

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"gold_csv={args.gold_csv}")
    print(f"map_csv={args.map_csv}")
    print(f"out_csv={out_csv}")
    print(f"updated_local_case_id_rows={updated}")


if __name__ == "__main__":
    main()
