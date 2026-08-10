from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
import sys

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
    parser = argparse.ArgumentParser(description="Audit real-case metadata extraction coverage for FC texts")
    parser.add_argument("--limit", type=int, default=500, help="Number of recent cases to audit")
    parser.add_argument("--show-samples", type=int, default=5, help="Number of style-of-cause samples to print")
    parser.add_argument("--min-critical-confidence", type=float, default=0.9, help="Confidence threshold for critical fields")
    parser.add_argument("--report-json", type=Path, default=None, help="Optional path to write full audit report JSON")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    if args.min_critical_confidence <= 0 or args.min_critical_confidence > 1:
        raise SystemExit("--min-critical-confidence must be in (0, 1]")

    with SessionLocal() as session:
        query = (
            select(Case.id, Case.citation, Case.court, Case.full_text)
            .where(Case.full_text.is_not(None))
            .where(Case.full_text != "")
            .where((Case.court == "FC") | (Case.citation.ilike("% FC %")))
            .order_by(Case.id.desc())
            .limit(args.limit)
        )
        rows = list(session.execute(query))

    totals = Counter()
    confidence_totals: dict[str, float] = {}
    confidence_counts: dict[str, int] = {}
    issue_counts = Counter()
    style_samples: list[tuple[int, str | None, str]] = []
    issue_samples: list[dict[str, object]] = []

    critical_fields = {"date", "docket", "neutral citation", "judge", "style of cause"}

    for case_id, citation, _court, full_text in rows:
        metadata = _extract_metadata_with_quality(full_text or "")
        field_confidence = metadata.get("_field_confidence") or {}
        quality_flags = metadata.get("_quality_flags") or []

        for field in FIELD_ORDER:
            if metadata.get(field):
                totals[field] += 1
            confidence = field_confidence.get(field)
            if isinstance(confidence, (int, float)):
                confidence_totals[field] = confidence_totals.get(field, 0.0) + float(confidence)
                confidence_counts[field] = confidence_counts.get(field, 0) + 1

        for flag in quality_flags:
            issue_counts[str(flag)] += 1
            if len(issue_samples) < 20:
                issue_samples.append(
                    {
                        "case_id": int(case_id),
                        "citation": citation,
                        "flag": str(flag),
                        "style_of_cause": metadata.get("style of cause"),
                        "judge": metadata.get("judge"),
                    }
                )

        extracted_citation = str(metadata.get("neutral citation") or "").strip().upper()
        stored_citation = str(citation or "").strip().upper()
        if extracted_citation and stored_citation and extracted_citation != stored_citation:
            issue_counts["mismatch:neutral_citation_vs_case_citation"] += 1

        for field in critical_fields:
            if field_confidence.get(field, 0.0) < args.min_critical_confidence:
                issue_counts[f"critical_below_threshold:{field}"] += 1

        style = metadata.get("style of cause")
        if style and len(style_samples) < args.show_samples:
            style_samples.append((int(case_id), citation, str(style)))

    summary: dict[str, object] = {
        "sampled_cases": len(rows),
        "min_critical_confidence": args.min_critical_confidence,
        "coverage": {},
        "confidence": {},
        "issues": dict(issue_counts),
        "style_samples": [
            {
                "case_id": case_id,
                "citation": case_citation,
                "style_of_cause": style,
            }
            for case_id, case_citation, style in style_samples
        ],
        "issue_samples": issue_samples,
    }

    print({"sampled_cases": len(rows), "min_critical_confidence": args.min_critical_confidence})
    for field in FIELD_ORDER:
        count = totals[field]
        pct = (count / len(rows) * 100.0) if rows else 0.0
        avg_conf = (confidence_totals.get(field, 0.0) / confidence_counts.get(field, 1)) if confidence_counts.get(field) else 0.0
        summary["coverage"][field] = {
            "count": int(count),
            "percent": round(pct, 2),
        }
        summary["confidence"][field] = {
            "avg": round(avg_conf, 3),
            "observations": int(confidence_counts.get(field, 0)),
        }
        print(f"{field}: {count}/{len(rows)} ({pct:.1f}%)")
        print(f"  avg_confidence: {avg_conf:.3f}")

    if issue_counts:
        print("\nissue_counts:")
        for issue, count in sorted(issue_counts.items(), key=lambda item: (-item[1], item[0])):
            print(f"{issue}: {count}")

    if style_samples:
        print("\nstyle_samples:")
        for case_id, citation, style in style_samples:
            print(f"case:{case_id} | {citation} | {style[:180]}")

    if args.report_json:
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        args.report_json.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nreport_json: {args.report_json}")


if __name__ == "__main__":
    main()
