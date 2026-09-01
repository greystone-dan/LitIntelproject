"""Build a stratified manual-adjudication template from an FC classification report."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=Path("data/eval/fc_activity_classification_500_per_year.json"))
    parser.add_argument("--output", type=Path, default=Path("data/eval/fc_activity_gold_template_100.csv"))
    parser.add_argument("--count", type=int, default=100)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = json.loads(args.report.read_text(encoding="utf-8"))
    selected = []
    years = sorted({row.get("year") for row in rows if row.get("year") is not None})
    base, remainder = divmod(args.count, len(years))
    for index, year in enumerate(years):
        take = base + (1 if index < remainder else 0)
        selected.extend([row for row in rows if row.get("year") == year][:take])
    fields = [
        "imm_number", "year", "case_name", "originating_entry_text",
        "gold_application_filed", "gold_application_perfected", "gold_leave_result",
        "gold_judicial_review_result", "gold_final_decision_type", "gold_closing_status",
        "gold_history_completeness", "reviewer_notes",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in selected:
            challenged = row.get("classification", {}).get("challenged_decision", {})
            writer.writerow({
                "imm_number": row.get("imm_number"),
                "year": row.get("year"),
                "case_name": row.get("case_name"),
                "originating_entry_text": challenged.get("text"),
                "gold_application_filed": "",
                "gold_application_perfected": "",
                "gold_leave_result": "",
                "gold_judicial_review_result": "",
                "gold_final_decision_type": "",
                "gold_closing_status": "",
                "gold_history_completeness": "",
                "reviewer_notes": "",
            })
    print(f"gold_rows={len(selected)} output={args.output}")


if __name__ == "__main__":
    main()
