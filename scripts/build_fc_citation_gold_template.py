"""Generate a gold-annotation template from normalized FC seed links.

This is a fixture-construction helper for citation QA. It does not perform extraction.
"""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


DEFAULT_SEED_CSV = Path("data/eval/fc_priority_seed_links.csv")
DEFAULT_TEMPLATE_CSV = Path("data/eval/fc_citation_gold_template.csv")
DEFAULT_SUMMARY_JSON = Path("data/eval/fc_citation_gold_template_summary.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-csv", type=Path, default=DEFAULT_SEED_CSV)
    parser.add_argument("--out-csv", type=Path, default=DEFAULT_TEMPLATE_CSV)
    parser.add_argument("--summary-json", type=Path, default=DEFAULT_SUMMARY_JSON)
    parser.add_argument("--limit", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.seed_csv.exists():
        raise SystemExit(f"Seed CSV not found: {args.seed_csv}")
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")

    with args.seed_csv.open("r", encoding="utf-8", newline="") as file_obj:
        rows = list(csv.DictReader(file_obj))

    selected = rows[: args.limit] if args.limit else rows

    args.out_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.out_csv.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=[
                "annotation_id",
                "seed_source_row",
                "seed_item_id",
                "seed_normalized_url",
                "local_case_id",
                "citation_text",
                "normalized_citation",
                "citation_type",
                "paragraph_index",
                "expected_target_case_id",
                "expected_target_citation",
                "notes",
                "status",
            ],
        )
        writer.writeheader()
        for index, row in enumerate(selected, start=1):
            writer.writerow(
                {
                    "annotation_id": f"fc_gold_{index:05d}",
                    "seed_source_row": row.get("source_row", ""),
                    "seed_item_id": row.get("item_id", ""),
                    "seed_normalized_url": row.get("normalized_url", ""),
                    "local_case_id": "",
                    "citation_text": "",
                    "normalized_citation": "",
                    "citation_type": "",
                    "paragraph_index": "",
                    "expected_target_case_id": "",
                    "expected_target_citation": "",
                    "notes": "",
                    "status": "pending",
                }
            )

    summary = {
        "seed_csv": str(args.seed_csv),
        "out_csv": str(args.out_csv),
        "total_seed_rows": len(rows),
        "template_rows": len(selected),
    }
    args.summary_json.parent.mkdir(parents=True, exist_ok=True)
    args.summary_json.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(f"seed_csv={args.seed_csv}")
    print(f"template_rows={len(selected)}")
    print(f"out_csv={args.out_csv}")
    print(f"summary_json={args.summary_json}")


if __name__ == "__main__":
    main()
