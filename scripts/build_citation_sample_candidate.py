"""Build a deterministic, read-only citation extraction candidate report."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import RawCitationMatch, extract_case_citation_matches
from backend.database import Case, SessionLocal

DEFAULT_OUTPUT = Path("data/eval/citation_sample_iteration1.json")
DEFAULT_QUOTAS = {"FC": 10, "FCA": 5, "SCC": 5}
COURT_ORDER = ("FC", "FCA", "SCC", "OTHER")
DEFAULT_CONTEXT_CHARS = 120


def validate_match_span(text: str, start: int, end: int, expected: str) -> bool:
    """Return whether an occurrence is in bounds and exactly source-backed."""
    return 0 <= start <= end <= len(text) and text[start:end] == expected


def context_excerpt(text: str, start: int, end: int, context_chars: int = DEFAULT_CONTEXT_CHARS) -> str:
    """Return a bounded source excerpt with context on both sides of a match."""
    if not 0 <= start <= end <= len(text):
        raise ValueError("match span is outside source text")
    if context_chars < 0:
        raise ValueError("context_chars must be non-negative")
    return text[max(0, start - context_chars) : min(len(text), end + context_chars)]


def occurrence_from_match(
    text: str, match: RawCitationMatch, context_chars: int = DEFAULT_CONTEXT_CHARS
) -> dict[str, Any]:
    """Serialize one emitted match; repeated emissions are deliberately retained."""
    return {
        "kind": match.kind,
        "citation_text": match.citation_text,
        "normalized_citation": match.normalized_citation,
        "offset_start": match.offset_start,
        "offset_end": match.offset_end,
        "exact_span_valid": validate_match_span(text, match.offset_start, match.offset_end, match.citation_text),
        "pinpoint": match.pinpoint,
        "declared_alias": match.declared_alias,
        "anchor_citation_text": match.anchor_citation_text,
        "anchor_offset_start": match.anchor_offset_start,
        "anchor_offset_end": match.anchor_offset_end,
        "source_context_excerpt": context_excerpt(text, match.offset_start, match.offset_end, context_chars),
        "review_status": "proposed",
    }


def court_bucket(court: str | None, citation: str | None) -> str:
    value = f"{court or ''} {citation or ''}".upper()
    if re.search(r"\bFCA\b", value):
        return "FCA"
    if re.search(r"\bFC(?:T)?\b", value) or "FEDERAL COURT" in value:
        return "FC"
    if re.search(r"\bSCC\b", value) or "SUPREME COURT" in value:
        return "SCC"
    return "OTHER"


def parse_quotas(values: Iterable[str] | None) -> dict[str, int]:
    quotas = dict(DEFAULT_QUOTAS)
    if values is None:
        return quotas
    quotas = {bucket: 0 for bucket in COURT_ORDER}
    for value in values:
        if "," in value:
            parts = value.split(",")
        else:
            parts = [value]
        for part in parts:
            value = part.strip()
            if not value:
                continue
            try:
                bucket, count_text = value.split("=", 1)
                count = int(count_text)
            except ValueError as exc:
                raise ValueError(f"expected COURT=COUNT, got {value!r}") from exc
            bucket = bucket.upper()
            if bucket not in quotas or count < 0:
                raise ValueError(f"invalid court quota {value!r}")
            quotas[bucket] = count
    return quotas


def select_cases(rows: list[Any], limit_total: int, quotas: dict[str, int]) -> list[Any]:
    """Select rows in stable ID order, satisfying available court quotas first."""
    buckets = {bucket: [] for bucket in COURT_ORDER}
    for row in rows:
        buckets[court_bucket(row.court, row.citation)].append(row)

    selected: list[Any] = []
    for bucket in COURT_ORDER:
        selected.extend(buckets[bucket][: quotas.get(bucket, 0)])
    selected = selected[:limit_total]
    if len(selected) >= limit_total:
        return selected

    selected_ids = {row.id for row in selected}
    for row in rows:
        if len(selected) >= limit_total:
            break
        if row.id not in selected_ids:
            selected.append(row)
            selected_ids.add(row.id)
    return selected


def _load_case_rows(session: Any) -> list[Any]:
    query = (
        select(Case.id, Case.title, Case.court, Case.citation, Case.full_text)
        .where(Case.full_text.is_not(None), Case.full_text != "")
        .order_by(Case.id.asc())
    )
    return list(session.execute(query))


def _case_payload(row: Any, context_chars: int) -> dict[str, Any]:
    text = str(row.full_text)
    occurrences = [
        occurrence_from_match(text, match, context_chars)
        for match in extract_case_citation_matches(text)
    ]
    return {
        "case_id": int(row.id),
        "court": row.court,
        "citation": row.citation,
        "title": row.title,
        "occurrences": occurrences,
        "occurrence_count": len(occurrences),
    }


def build_report(limit_total: int = 20, quotas: dict[str, int] | None = None, context_chars: int = DEFAULT_CONTEXT_CHARS) -> dict[str, Any]:
    if limit_total < 0:
        raise ValueError("limit_total must be non-negative")
    if context_chars < 0:
        raise ValueError("context_chars must be non-negative")
    quotas = dict(DEFAULT_QUOTAS if quotas is None else quotas)
    with SessionLocal() as session:
        rows = _load_case_rows(session)
        selected = select_cases(rows, limit_total, quotas)

    cases = [_case_payload(row, context_chars) for row in selected]
    occurrences = [occ for case in cases for occ in case["occurrences"]]
    case_counts = Counter(court_bucket(case["court"], case["citation"]) for case in cases)
    occurrence_counts = Counter(
        court_bucket(case["court"], case["citation"])
        for case in cases
        for _ in case["occurrences"]
    )
    return {
        "report_name": "citation_sample_iteration1",
        "report_type": "citation_extraction_candidate",
        "review_status": "proposed",
        "selection": {
            "method": "ascending case ID with court quotas, then deterministic fill",
            "requested_limit_total": limit_total,
            "requested_per_court": quotas,
            "database_writes": False,
        },
        "cases": cases,
        "summary": {
            "case_count": len(cases),
            "occurrence_count": len(occurrences),
            "case_counts_by_court": dict(case_counts),
            "occurrence_counts_by_court": dict(occurrence_counts),
            "counts_by_kind": dict(Counter(occ["kind"] for occ in occurrences)),
            "exact_span_valid_count": sum(occ["exact_span_valid"] for occ in occurrences),
            "exact_span_invalid_count": sum(not occ["exact_span_valid"] for occ in occurrences),
        },
    }


def verify_report(output: Path) -> None:
    report = json.loads(output.read_text(encoding="utf-8"))
    if report.get("review_status") != "proposed":
        raise RuntimeError("report is not marked proposed")
    with SessionLocal() as session:
        rows = {int(row.id): row for row in _load_case_rows(session)}
        for case in report.get("cases", []):
            row = rows.get(int(case["case_id"]))
            if row is None:
                raise RuntimeError(f"case {case['case_id']} is missing or has no full text")
            text = str(row.full_text)
            matches = extract_case_citation_matches(text)
            occurrences = case.get("occurrences", [])
            if len(matches) != len(occurrences):
                raise RuntimeError(f"case {case['case_id']} occurrence count changed")
            for match, occurrence in zip(matches, occurrences):
                if occurrence.get("review_status") != "proposed":
                    raise RuntimeError(f"case {case['case_id']} occurrence is not proposed")
                if not validate_match_span(text, occurrence["offset_start"], occurrence["offset_end"], occurrence["citation_text"]):
                    raise RuntimeError(f"case {case['case_id']} has an invalid exact span")
                emitted = (match.kind, match.citation_text, match.offset_start, match.offset_end)
                recorded = (occurrence["kind"], occurrence["citation_text"], occurrence["offset_start"], occurrence["offset_end"])
                if emitted != recorded:
                    raise RuntimeError(f"case {case['case_id']} occurrence differs from extractor output")
    print(f"verified {len(report.get('cases', []))} cases and {report['summary']['occurrence_count']} occurrences")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--limit-total", type=int, default=20)
    parser.add_argument("--per-court", nargs="+", metavar="COURT=COUNT")
    parser.add_argument("--context-chars", type=int, default=DEFAULT_CONTEXT_CHARS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.verify:
        verify_report(args.output)
        return
    try:
        quotas = parse_quotas(args.per_court)
        report = build_report(args.limit_total, quotas, args.context_chars)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"wrote proposed citation report for {report['summary']['case_count']} cases to {args.output}")
    print(json.dumps(report["summary"], sort_keys=True))


if __name__ == "__main__":
    main()