"""Bounded, read-only benchmark for citation occurrence resolution."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import (  # noqa: E402
    CASE_CITATION_KINDS,
    NEUTRAL_CIT_RE,
    extract_case_citation_matches,
    is_self_case_citation,
    is_self_case_name_match,
)
from backend.database import Case, SessionLocal  # noqa: E402


@dataclass(frozen=True)
class TargetRecord:
    case_id: int
    title: str | None
    citation: str | None
    secondary_citation: str | None


def _normalize(value: str | None) -> str:
    return " ".join((value or "").upper().split())


def _citation_variants(value: str | None) -> set[str]:
    normalized = _normalize(value)
    if not normalized:
        return set()
    variants = {normalized}
    if " FC " in f" {normalized} ":
        variants.add(normalized.replace(" FC ", " FCT "))
    if " FCT " in f" {normalized} ":
        variants.add(normalized.replace(" FCT ", " FC "))
    return variants


def _alias_terms(match: Any) -> set[str]:
    clean = re.split(r"\s*,?\s*(?:at\s+)?para", getattr(match, "citation_text", ""), maxsplit=1, flags=re.IGNORECASE)[0]
    clean = " ".join(clean.split())
    parts = re.split(r"\s+(?:v\.?|vs\.?|c\.?|versus)\s+", clean, maxsplit=1, flags=re.IGNORECASE)
    terms = set()
    for choice in (clean, *parts):
        term = re.sub(r"[^A-Za-z0-9\s]", " ", choice).strip().lower()
        term = " ".join(term.split())
        if len(term) >= 3:
            terms.add(term)
    return terms


def _candidate_ids(term: str, targets: Iterable[TargetRecord]) -> set[int]:
    return {
        target.case_id
        for target in targets
        if any(term in (value or "").lower() for value in (target.title, target.citation, target.secondary_citation))
    }


def resolve_occurrence(match: Any, targets: Iterable[TargetRecord]) -> str:
    """Classify one occurrence using a benchmark-local in-memory target index."""
    targets = tuple(targets)
    if match.kind == "neutral":
        variants = _citation_variants(getattr(match, "normalized_citation", None))
        candidate_ids = {
            target.case_id
            for target in targets
            if variants & (_citation_variants(target.citation) | _citation_variants(target.secondary_citation))
        }
    elif match.kind in {"case", "case_short", "case_name"}:
        embedded = NEUTRAL_CIT_RE.search(getattr(match, "normalized_citation", ""))
        if embedded:
            variants = _citation_variants(embedded.group(0))
            candidate_ids = {
                target.case_id
                for target in targets
                if variants & (_citation_variants(target.citation) | _citation_variants(target.secondary_citation))
            }
        else:
            candidate_ids = set()
            for term in _alias_terms(match):
                candidate_ids.update(_candidate_ids(term, targets))
    else:
        return "unresolved"
    if len(candidate_ids) == 1:
        return "unique"
    if len(candidate_ids) > 1:
        return "ambiguous"
    return "unresolved"


def is_exact_span_valid(full_text: str, match: Any) -> bool:
    start = getattr(match, "offset_start", None)
    end = getattr(match, "offset_end", None)
    text = getattr(match, "citation_text", None)
    return isinstance(start, int) and isinstance(end, int) and 0 <= start < end <= len(full_text) and isinstance(text, str) and full_text[start:end] == text


def duplicate_occurrence_count(matches: Iterable[Any]) -> int:
    counts = Counter(getattr(match, "normalized_citation", "") for match in matches)
    return sum(max(0, count - 1) for value, count in counts.items() if value)


def aggregate_case(case: Any, full_text: str, matches: Iterable[Any], targets: Iterable[TargetRecord]) -> dict[str, int | str]:
    rows = list(matches)
    statuses = [resolve_occurrence(match, targets) for match in rows]
    return {
        "source_cases": 1,
        "all_extracted_occurrence_count": len(rows),
        "long_form_count": sum(match.kind == "case" for match in rows),
        "neutral_count": sum(match.kind == "neutral" for match in rows),
        "case_name_count": sum(match.kind == "case_name" for match in rows),
        "short_form_count": sum(match.kind == "case_short" for match in rows),
        "explicit_pinpoint_count": sum(bool(getattr(match, "pinpoint", None)) for match in rows),
        "exact_span_valid_count": sum(is_exact_span_valid(full_text, match) for match in rows),
        "exact_span_invalid_count": sum(not is_exact_span_valid(full_text, match) for match in rows),
        "duplicate_occurrence_count": duplicate_occurrence_count(rows),
        "self_citation_occurrence_count": sum(is_self_case_citation(case, match) or is_self_case_name_match(getattr(case, "title", None), match) for match in rows),
        "resolved_occurrence_count": statuses.count("unique"),
        "unresolved_occurrence_count": statuses.count("unresolved"),
        "ambiguous_alias_occurrence_count": sum(status == "ambiguous" and match.kind in {"case_short", "case_name"} for status, match in zip(statuses, rows)),
        "ambiguous_occurrence_count": statuses.count("ambiguous"),
    }


def _empty_metrics() -> dict[str, int | str]:
    return {
        "source_cases": 0,
        "all_extracted_occurrence_count": 0,
        "long_form_count": 0,
        "neutral_count": 0,
        "case_name_count": 0,
        "short_form_count": 0,
        "explicit_pinpoint_count": 0,
        "exact_span_valid_count": 0,
        "exact_span_invalid_count": 0,
        "duplicate_occurrence_count": 0,
        "self_citation_occurrence_count": 0,
        "resolved_occurrence_count": 0,
        "unresolved_occurrence_count": 0,
        "ambiguous_alias_occurrence_count": 0,
        "ambiguous_occurrence_count": 0,
    }


def _sum_metrics(rows: Iterable[dict[str, int | str]]) -> dict[str, int | str]:
    result = _empty_metrics()
    for row in rows:
        for key in result:
            result[key] += int(row[key])
    return result


def _present_metrics(metrics: dict[str, int | str], target_inventory_count: int) -> dict[str, Any]:
    resolved = int(metrics["resolved_occurrence_count"])
    total = int(metrics["all_extracted_occurrence_count"])
    return {
        **metrics,
        "target_inventory_count": target_inventory_count,
        "resolution_coverage": resolved / total if total else 0.0,
        "explicit_pinpoint_status": "measured from RawCitationMatch.pinpoint",
        "database_writes": False,
        "resolution_mode": "benchmark-local in-memory resolver",
    }


def benchmark(courts: list[str], limit: int) -> dict[str, Any]:
    per_court: dict[str, dict[str, Any]] = {}
    with SessionLocal() as session:
        target_rows = session.execute(select(Case.id, Case.title, Case.citation, Case.secondary_citation)).all()
        targets = tuple(TargetRecord(*row) for row in target_rows)
        for court in courts:
            source_rows = session.execute(
                select(Case.id, Case.title, Case.citation, Case.secondary_citation, Case.full_text)
                .where(Case.court == court, Case.full_text.is_not(None), Case.full_text != "")
                .order_by(Case.id)
                .limit(limit)
            ).all()
            case_metrics = []
            for row in source_rows:
                case = TargetRecord(row.id, row.title, row.citation, row.secondary_citation)
                matches = extract_case_citation_matches(row.full_text)
                case_metrics.append(aggregate_case(case, row.full_text, matches, targets))
            per_court[court] = _present_metrics(_sum_metrics(case_metrics), len(targets))

    totals = _present_metrics(_sum_metrics(per_court.values()), len(targets))
    return {
        "benchmark": "citation_resolution_035_m3",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "courts": courts,
        "limit_per_court": limit,
        "database_writes": False,
        "resolution_mode": "benchmark-local in-memory resolver",
        "per_court": per_court,
        "totals": totals,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--courts", nargs="+", default=["FC", "FCA", "SCCmodern"])
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--report-json", type=Path)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    report = benchmark(args.courts, args.limit)
    if args.report_json:
        args.report_json.parent.mkdir(parents=True, exist_ok=True)
        args.report_json.write_text(json.dumps(report, separators=(",", ":")), encoding="utf-8")
    print(json.dumps(report, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
