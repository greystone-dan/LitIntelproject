"""Build a read-only statute and legal-instrument demand catalogue."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import extract_statute_reference_matches
from backend.database import Case, SessionLocal
from backend.statutes import LEGISLATION_REGISTRY, parse_legislation_citation

DEFAULT_OUTPUT = Path("data/eval/statute_demand_iteration1.json")
DEFAULT_QUOTAS = {"FC": 125, "FCA": 62, "SCC": 63}
COURT_ORDER = ("FC", "FCA", "SCC", "OTHER")
DEFAULT_CONTEXT_CHARS = 180


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
        for part in value.split(","):
            part = part.strip()
            if not part:
                continue
            try:
                bucket, count_text = part.split("=", 1)
                count = int(count_text)
            except ValueError as exc:
                raise ValueError(f"expected COURT=COUNT, got {part!r}") from exc
            bucket = bucket.upper()
            if bucket not in quotas or count < 0:
                raise ValueError(f"invalid court quota {part!r}")
            quotas[bucket] = count
    return quotas


def select_cases(rows: list[Any], limit_total: int, quotas: dict[str, int]) -> list[Any]:
    buckets = {bucket: [] for bucket in COURT_ORDER}
    for row in rows:
        buckets[court_bucket(row.court, row.citation)].append(row)
    selected: list[Any] = []
    for bucket in COURT_ORDER:
        selected.extend(buckets[bucket][: quotas.get(bucket, 0)])
    selected = selected[:limit_total]
    selected_ids = {row.id for row in selected}
    for row in rows:
        if len(selected) >= limit_total:
            break
        if row.id not in selected_ids:
            selected.append(row)
            selected_ids.add(row.id)
    return selected


def paragraph_location(text: str, start: int, end: int) -> dict[str, int]:
    line_start = text.count("\n", 0, start) + 1
    line_end = text.count("\n", 0, end) + 1
    previous_break = text.rfind("\n\n", 0, start)
    paragraph_start = previous_break + 2 if previous_break >= 0 else 0
    paragraph_end = text.find("\n\n", end)
    if paragraph_end < 0:
        paragraph_end = len(text)
    paragraph_index = text.count("\n\n", 0, start) + 1
    return {
        "line_start": line_start,
        "line_end": line_end,
        "paragraph_index": paragraph_index,
        "paragraph_offset_start": paragraph_start,
        "paragraph_offset_end": paragraph_end,
    }


def context_excerpt(text: str, start: int, end: int, context_chars: int) -> str:
    return text[max(0, start - context_chars) : min(len(text), end + context_chars)]


def instrument_key_for(match_text: str, normalized: str) -> str | None:
    parsed = parse_legislation_citation(match_text)
    if parsed:
        return parsed.instrument_key
    lowered = normalized.casefold()
    for key, definition in LEGISLATION_REGISTRY.items():
        aliases = definition["aliases"]
        if any(re.search(rf"\b{re.escape(alias)}\b", lowered, re.IGNORECASE) for alias in aliases):
            return key
    return None


def provision_path(normalized: str) -> str | None:
    match = re.search(r"\bss?\.\s+(.+)$", normalized, re.IGNORECASE)
    return match.group(1).strip() if match else None


def occurrence_record(row: Any, text: str, match: Any, occurrence_index: int, context_chars: int) -> dict[str, Any]:
    location = paragraph_location(text, match.offset_start, match.offset_end)
    instrument_key = instrument_key_for(match.citation_text, match.normalized_citation)
    parsed = parse_legislation_citation(match.citation_text)
    return {
        "occurrence_id": f"{row.id}:{occurrence_index}",
        "case_id": int(row.id),
        "case_title": row.title,
        "court": row.court,
        "case_citation": row.citation,
        "source_text_hash": row.full_text_hash or hashlib.sha256(text.encode("utf-8")).hexdigest(),
        "reference_kind": match.kind,
        "reference_text": match.citation_text,
        "normalized_reference": match.normalized_citation,
        "instrument_key": instrument_key,
        "pinpoint": parsed.pinpoint if parsed else provision_path(match.normalized_citation),
        "authority_url": parsed.legislation_url if parsed else None,
        "resolution_status": "identified_unresolved" if instrument_key else "instrument_unidentified",
        "offset_start": match.offset_start,
        "offset_end": match.offset_end,
        "exact_span_valid": text[match.offset_start : match.offset_end] == match.citation_text,
        "location": location,
        "context_excerpt": context_excerpt(text, match.offset_start, match.offset_end, context_chars),
    }


def build_report(limit_total: int, quotas: dict[str, int], context_chars: int) -> dict[str, Any]:
    query = (
        select(Case.id, Case.title, Case.court, Case.citation, Case.full_text, Case.full_text_hash)
        .where(Case.full_text.is_not(None), Case.full_text != "")
        .order_by(Case.id.asc())
    )
    with SessionLocal() as session:
        rows = list(session.execute(query))
        selected = select_cases(rows, limit_total, quotas)

    cases = []
    occurrences: list[dict[str, Any]] = []
    for row in selected:
        text = str(row.full_text)
        case_occurrences = [
            occurrence_record(row, text, match, index, context_chars)
            for index, match in enumerate(extract_statute_reference_matches(text))
        ]
        cases.append({"case_id": int(row.id), "court": row.court, "citation": row.citation, "title": row.title, "occurrence_count": len(case_occurrences)})
        occurrences.extend(case_occurrences)

    instrument_counts = Counter(item["instrument_key"] or "unidentified" for item in occurrences)
    reference_counts = Counter(item["normalized_reference"] for item in occurrences)
    court_counts = Counter(court_bucket(item["court"], item["case_citation"]) for item in occurrences)
    exact_span_valid_count = sum(item["exact_span_valid"] for item in occurrences)
    catalogue = [
        {
            "normalized_reference": reference,
            "instrument_key": next((item["instrument_key"] for item in occurrences if item["normalized_reference"] == reference), None),
            "occurrence_count": count,
            "case_count": len({item["case_id"] for item in occurrences if item["normalized_reference"] == reference}),
            "example_occurrence_ids": [item["occurrence_id"] for item in occurrences if item["normalized_reference"] == reference][:5],
        }
        for reference, count in reference_counts.most_common()
    ]
    return {
        "report_name": "statute_demand_iteration1",
        "report_type": "read_only_statute_demand_catalogue",
        "review_status": "proposed",
        "selection": {"limit_total": limit_total, "per_court": quotas, "database_writes": False},
        "cases": cases,
        "occurrences": occurrences,
        "catalogue": catalogue,
        "summary": {
            "case_count": len(cases),
            "occurrence_count": len(occurrences),
            "court_counts": dict(court_counts),
            "instrument_counts": dict(instrument_counts),
            "unresolved_instrument_occurrence_count": sum(item["instrument_key"] is None for item in occurrences),
            "distinct_normalized_reference_count": len(reference_counts),
            "exact_span_valid_count": exact_span_valid_count,
            "exact_span_invalid_count": len(occurrences) - exact_span_valid_count,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--limit-total", type=int, default=250)
    parser.add_argument("--per-court", nargs="+", metavar="COURT=COUNT")
    parser.add_argument("--context-chars", type=int, default=DEFAULT_CONTEXT_CHARS)
    args = parser.parse_args()
    try:
        quotas = parse_quotas(args.per_court)
        report = build_report(args.limit_total, quotas, args.context_chars)
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
