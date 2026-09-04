"""THROWAWAY cross-court metadata-extraction audit (read-only).

Patterns on scripts/audit_fc_metadata_extraction.py but audits a court selected
via --court (FCA | SCC | both). Reuses
fc_ingest.document_scraper._extract_metadata_with_quality and backend.database.

Purpose: measure whether the recent FC metadata-extraction fixes generalize to
FCA and SCC without court-specific handling.

Usage:
    & ".\\venv\\Scripts\\python.exe" scripts\\_tmp_crosscourt_audit.py --court both
"""
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

CRITICAL_FIELDS = {"date", "docket", "neutral citation", "judge", "style of cause"}


def _court_clause(court: str):
    if court == "FCA":
        return (Case.court == "FCA") | (Case.citation.ilike("% FCA %"))
    if court == "SCC":
        return (Case.court == "SCC") | (Case.citation.ilike("% SCC %"))
    if court == "SCCmodern":
        # Diagnostic slice: SCC cases whose stored citation is the modern
        # neutral format (e.g. '2008 SCC 26'), excluding SCR-reporter-era rows.
        return (Case.court == "SCC") & (Case.citation.ilike("% SCC %"))
    raise ValueError(court)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Throwaway cross-court metadata extraction audit (read-only)")
    parser.add_argument("--court", choices=["FCA", "SCC", "SCCmodern", "both", "all"], default="all")
    parser.add_argument("--limit", type=int, default=40, help="Number of recent cases to audit per court")
    parser.add_argument("--low-samples", type=int, default=5, help="Lowest-confidence judge/style samples to print per court")
    parser.add_argument("--min-critical-confidence", type=float, default=0.9, help="Confidence threshold for critical fields")
    parser.add_argument(
        "--report-json",
        type=Path,
        default=Path("data/eval/metadata_audit_crosscourt.json"),
        help="Path to write combined audit report JSON",
    )
    return parser.parse_args()


def audit_court(court: str, args: argparse.Namespace) -> dict[str, object]:
    clause = _court_clause(court)
    with SessionLocal() as session:
        query = (
            select(Case.id, Case.citation, Case.court, Case.full_text)
            .where(Case.full_text.is_not(None))
            .where(Case.full_text != "")
            .where(clause)
            .order_by(Case.id.desc())
            .limit(args.limit)
        )
        rows = list(session.execute(query))

    totals = Counter()
    confidence_totals: dict[str, float] = {}
    confidence_counts: dict[str, int] = {}
    issue_counts = Counter()
    low_judge: list[tuple[float, int, str | None, object]] = []
    low_style: list[tuple[float, int, str | None, object]] = []

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
            flag_str = str(flag)
            name, _, flag_field = flag_str.partition(":")
            if name in {"missing_critical", "invalid_shape"} and flag_field not in CRITICAL_FIELDS:
                continue
            issue_counts[flag_str] += 1

        extracted_citation = str(metadata.get("neutral citation") or "").strip().upper()
        stored_citation = str(citation or "").strip().upper()
        if extracted_citation and stored_citation and extracted_citation != stored_citation:
            issue_counts["mismatch:neutral_citation_vs_case_citation"] += 1

        for field in CRITICAL_FIELDS:
            if field_confidence.get(field, 0.0) < args.min_critical_confidence:
                issue_counts[f"critical_below_threshold:{field}"] += 1

        judge_conf = field_confidence.get("judge")
        if isinstance(judge_conf, (int, float)):
            low_judge.append((float(judge_conf), int(case_id), citation, metadata.get("judge")))
        style_conf = field_confidence.get("style of cause")
        if isinstance(style_conf, (int, float)):
            low_style.append((float(style_conf), int(case_id), citation, metadata.get("style of cause")))

    low_judge.sort(key=lambda item: item[0])
    low_style.sort(key=lambda item: item[0])
    low_judge = low_judge[: args.low_samples]
    low_style = low_style[: args.low_samples]

    summary: dict[str, object] = {
        "court": court,
        "sampled_cases": len(rows),
        "min_critical_confidence": args.min_critical_confidence,
        "coverage": {},
        "confidence": {},
        "issues": dict(issue_counts),
        "low_confidence_judge": [
            {"confidence": round(conf, 3), "case_id": cid, "citation": cit, "value_repr": repr(val)}
            for conf, cid, cit, val in low_judge
        ],
        "low_confidence_style_of_cause": [
            {"confidence": round(conf, 3), "case_id": cid, "citation": cit, "value_repr": repr(val)}
            for conf, cid, cit, val in low_style
        ],
    }

    print(f"\n=== {court} ===")
    print({"sampled_cases": len(rows), "min_critical_confidence": args.min_critical_confidence})
    for field in FIELD_ORDER:
        count = totals[field]
        pct = (count / len(rows) * 100.0) if rows else 0.0
        avg_conf = (confidence_totals.get(field, 0.0) / confidence_counts.get(field, 1)) if confidence_counts.get(field) else 0.0
        summary["coverage"][field] = {"count": int(count), "percent": round(pct, 2)}
        summary["confidence"][field] = {"avg": round(avg_conf, 3), "observations": int(confidence_counts.get(field, 0))}
        print(f"{field}: {count}/{len(rows)} ({pct:.1f}%)  avg_confidence: {avg_conf:.3f}")

    if issue_counts:
        print("\nissue_counts:")
        for issue, count in sorted(issue_counts.items(), key=lambda item: (-item[1], item[0])):
            print(f"{issue}: {count}")

    print("\nlowest-confidence judge values:")
    for conf, cid, cit, val in low_judge:
        print(f"  conf={conf:.3f} case:{cid} | {cit} | {repr(val)}")
    print("lowest-confidence style-of-cause values:")
    for conf, cid, cit, val in low_style:
        print(f"  conf={conf:.3f} case:{cid} | {cit} | {repr(val)}")

    return summary


def main() -> None:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    if not 0 < args.min_critical_confidence <= 1:
        raise SystemExit("--min-critical-confidence must be in (0, 1]")

    courts = {"both": ["FCA", "SCC"], "all": ["FCA", "SCC", "SCCmodern"]}.get(args.court, [args.court])
    combined: dict[str, object] = {court: audit_court(court, args) for court in courts}

    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(combined, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nreport_json: {args.report_json}")


if __name__ == "__main__":
    main()
