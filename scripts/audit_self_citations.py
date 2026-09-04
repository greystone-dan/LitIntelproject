"""Bounded, read-only audit of existing citation self-links."""

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


def normalize(value: str | None) -> str:
    return " ".join((value or "").casefold().replace(".", "").split())


def classify_self_citation(
    citation: str | None,
    source_citation: str | None,
    context: str,
    offset_start: int | None,
) -> str:
    """Classify a self-link using conservative, explainable evidence."""
    same_citation = bool(citation and source_citation and normalize(citation) == normalize(source_citation))
    header_language = any(
        marker in context.casefold()
        for marker in ("neutral citation", "citation:", "citation ", "decision content")
    )
    if header_language and offset_start is not None and offset_start < 500:
        return "source_header_citation" if same_citation else "source_header_artifact"
    if same_citation and offset_start is not None and offset_start < 500:
        return "early_source_citation"
    if same_citation:
        return "same_citation_outside_header"
    return "other_self_link"


def audit_self_citations(limit: int = 100) -> dict[str, Any]:
    """Return a bounded sample and classification counts without data writes."""
    bounded_limit = max(1, min(1000, limit))
    with SessionLocal() as db:
        total = int(
            db.execute(
                sql_text("SELECT COUNT(*) FROM citations WHERE source_case_id = target_case_id")
            ).scalar_one()
        )
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

    sample: list[dict[str, Any]] = []
    classifications: Counter[str] = Counter()
    for row in rows:
        full_text = row["full_text"] or ""
        start = int(row["offset_start"] or 0)
        end = int(row["offset_end"] or start)
        context_start = max(0, start - 120)
        context_end = min(len(full_text), end + 160)
        context = full_text[context_start:context_end]
        classification = classify_self_citation(
            row["normalized_citation"] or row["citation_text"],
            row["source_citation"],
            context,
            row["offset_start"],
        )
        classifications[classification] += 1
        sample.append(
            {
                "citation_id": row["id"],
                "source_case_id": row["source_case_id"],
                "source_title": row["source_title"],
                "source_citation": row["source_citation"],
                "citation_text": row["citation_text"],
                "normalized_citation": row["normalized_citation"],
                "offset_start": row["offset_start"],
                "offset_end": row["offset_end"],
                "classification": classification,
                "context": " ".join(context.split()),
            }
        )

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sample_limit": bounded_limit,
        "total_self_citations": total,
        "sample_count": len(sample),
        "classification_counts": dict(classifications),
        "sample": sample,
        "write_performed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit existing citation self-links without modifying data.")
    parser.add_argument("--limit", type=int, default=100, help="Maximum rows to inspect (1-1000)")
    parser.add_argument("--output-file", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    report = audit_self_citations(args.limit)
    if args.output_file:
        args.output_file.parent.mkdir(parents=True, exist_ok=True)
        args.output_file.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Self-citation audit written to: {args.output_file}")
    print(json.dumps({key: value for key, value in report.items() if key != "sample"}, indent=2))


if __name__ == "__main__":
    main()
