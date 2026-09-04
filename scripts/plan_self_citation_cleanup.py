"""Plan self-citation cleanup candidates without modifying the database."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sqlalchemy import text as sql_text

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import SessionLocal
from scripts.audit_self_citations import classify_self_citation


def plan_cleanup(limit: int = 100) -> dict[str, Any]:
    bounded_limit = max(1, min(1000, limit))
    with SessionLocal() as db:
        rows = db.execute(
            sql_text(
                """
                SELECT c.id, c.source_case_id, c.citation_text, c.normalized_citation,
                       c.offset_start, c.offset_end, src.title AS source_title,
                       src.citation AS source_citation, src.full_text
                FROM citations c
                JOIN cases src ON src.id = c.source_case_id
                WHERE c.source_case_id = c.target_case_id
                ORDER BY c.id
                LIMIT :limit
                """
            ),
            {"limit": bounded_limit},
        ).mappings().all()

    candidates: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    for row in rows:
        full_text = row["full_text"] or ""
        start = int(row["offset_start"] or 0)
        end = int(row["offset_end"] or start)
        context = full_text[max(0, start - 120) : min(len(full_text), end + 160)]
        classification = classify_self_citation(
            row["normalized_citation"] or row["citation_text"],
            row["source_citation"],
            context,
            row["offset_start"],
        )
        counts[classification] += 1
        candidates.append(
            {
                "citation_id": row["id"],
                "source_case_id": row["source_case_id"],
                "source_title": row["source_title"],
                "source_citation": row["source_citation"],
                "citation_text": row["citation_text"],
                "offset_start": row["offset_start"],
                "offset_end": row["offset_end"],
                "classification": classification,
                "review_priority": "first" if classification.startswith("source_header") else "later",
                "context": " ".join(context.split()),
            }
        )

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sample_limit": bounded_limit,
        "sample_count": len(candidates),
        "classification_counts": dict(counts),
        "review_order": ["source_header_citation", "source_header_artifact", "early_source_citation", "other_self_link"],
        "candidates": candidates,
        "write_performed": False,
        "cleanup_authorized": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan self-citation cleanup candidates without modifying data.")
    parser.add_argument("--limit", type=int, default=100, help="Maximum rows to inspect (1-1000)")
    parser.add_argument("--output-file", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    report = plan_cleanup(args.limit)
    if args.output_file:
        args.output_file.parent.mkdir(parents=True, exist_ok=True)
        args.output_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Self-citation cleanup plan written to: {args.output_file}")
    print(json.dumps({key: value for key, value in report.items() if key != "candidates"}, indent=2))


if __name__ == "__main__":
    main()
