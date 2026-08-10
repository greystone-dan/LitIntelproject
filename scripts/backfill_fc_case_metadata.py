from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
import sys
from typing import Any

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal
from fc_ingest.document_scraper import _extract_metadata_with_quality


FIELD_ORDER = [
    "date",
    "docket",
    "neutral citation",
    "judge",
    "style of cause",
    "place of hearing",
    "date of hearing",
    "dated",
    "counsel",
    "present",
    "between",
    "solicitors of record",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill extracted FC metadata into cases.metadata_json")
    parser.add_argument("--limit", type=int, default=2000)
    parser.add_argument("--batch-size", type=int, default=250)
    parser.add_argument("--min-confidence", type=float, default=0.9)
    parser.add_argument("--apply", action="store_true", help="Persist changes")
    parser.add_argument("--report-json", type=Path, default=Path("data/eval/reports/fc_metadata_backfill_report.json"))
    return parser.parse_args()


def _coverage_from_rows(rows: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    totals = Counter()
    for row in rows:
        for field in FIELD_ORDER:
            if row.get(field):
                totals[field] += 1
    denom = len(rows) or 1
    return {
        field: {
            "count": int(totals[field]),
            "percent": round((totals[field] / denom) * 100.0, 2),
        }
        for field in FIELD_ORDER
    }


def _extract_existing(metadata_json: dict[str, Any] | None) -> dict[str, Any]:
    metadata_json = metadata_json or {}
    extracted = metadata_json.get("reader_extracted")
    if isinstance(extracted, dict):
        return extracted
    return {}


def main() -> None:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    if args.min_confidence <= 0 or args.min_confidence > 1:
        raise SystemExit("--min-confidence must be in (0, 1]")

    scanned = 0
    changed = 0

    before_rows: list[dict[str, Any]] = []
    after_rows: list[dict[str, Any]] = []

    with SessionLocal() as session:
        query = (
            select(Case)
            .where(Case.full_text.is_not(None))
            .where(Case.full_text != "")
            .where((Case.court == "FC") | (Case.citation.ilike("% FC %")) | (Case.citation.ilike("% FCA %")))
            .order_by(Case.id.desc())
            .limit(args.limit)
        )
        rows = list(session.scalars(query))

        for idx, case in enumerate(rows, start=1):
            scanned += 1
            existing = _extract_existing(case.metadata_json)
            before_rows.append(existing)

            extracted = _extract_metadata_with_quality(case.full_text or "")
            confidence = extracted.get("_field_confidence") or {}

            merged = dict(existing)
            local_change = False
            for field in FIELD_ORDER:
                value = extracted.get(field)
                if not value:
                    continue
                conf = float(confidence.get(field, 0.0))
                if conf < args.min_confidence and field in {"date", "docket", "neutral citation", "judge", "style of cause"}:
                    continue
                if merged.get(field) != value:
                    merged[field] = value
                    local_change = True

            merged["_field_confidence"] = extracted.get("_field_confidence", {})
            merged["_field_sources"] = extracted.get("_field_sources", {})
            merged["_quality_flags"] = extracted.get("_quality_flags", [])
            merged["_needs_review"] = extracted.get("_needs_review", False)

            after_rows.append(merged)

            if args.apply and local_change:
                payload = dict(case.metadata_json or {})
                payload["reader_extracted"] = merged
                case.metadata_json = payload
                changed += 1

            if args.apply and idx % args.batch_size == 0:
                session.commit()

        if args.apply:
            session.commit()

    before_cov = _coverage_from_rows(before_rows)
    after_cov = _coverage_from_rows(after_rows)

    report = {
        "scanned": scanned,
        "changed": changed,
        "applied": args.apply,
        "min_confidence": args.min_confidence,
        "before": before_cov,
        "after": after_cov,
        "delta": {
            field: round(after_cov[field]["percent"] - before_cov[field]["percent"], 2)
            for field in FIELD_ORDER
        },
    }

    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print({
        "scanned": scanned,
        "changed": changed,
        "applied": args.apply,
        "report_json": str(args.report_json),
    })


if __name__ == "__main__":
    main()
