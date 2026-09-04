"""Build a deterministic, proposed five-case citation review fixture."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import RawCitationMatch, extract_case_citation_matches
from backend.database import Case, SessionLocal

DEFAULT_OUTPUT = Path("data/eval/five_case_citation_gold_candidate.json")
CONTEXT_RADIUS = 90
MODERN_SCC_YEAR = 2000
YEAR_RE = re.compile(r"\b((?:19|20)\d{2})\s+SCC\s+\d+\b", re.IGNORECASE)


def validate_match_span(text: str, start: int, end: int, expected: str) -> bool:
    """Return whether an extractor span is in bounds and source-backed."""
    return 0 <= start <= end <= len(text) and text[start:end] == expected


def context_excerpt(text: str, start: int, end: int, radius: int = CONTEXT_RADIUS) -> str:
    """Return a bounded excerpt surrounding a match."""
    if not 0 <= start <= end <= len(text):
        raise ValueError("match span is outside source text")
    return text[max(0, start - radius) : min(len(text), end + radius)]


def occurrence_from_match(text: str, match: RawCitationMatch) -> dict[str, Any]:
    """Serialize one emitted match without deduplicating repeated occurrences."""
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
        "source_context_excerpt": context_excerpt(text, match.offset_start, match.offset_end),
        "review_status": "proposed",
    }


def _court_bucket(court: str | None, citation: str | None) -> str:
    value = f"{court or ''} {citation or ''}".upper()
    if re.search(r"\bFCA\b", value):
        return "FCA"
    if re.search(r"\bFC(?:T)?\b", value):
        return "FC"
    if re.search(r"\bSCC\b", value):
        return "SCC"
    return "OTHER"


def _is_modern_scc(citation: str | None) -> bool:
    match = YEAR_RE.search(citation or "")
    return bool(match and int(match.group(1)) >= MODERN_SCC_YEAR)


def select_cases(rows: list[Any]) -> tuple[list[Any], bool]:
    """Select exactly five rows, preferring three FC, one FCA, and one SCC."""
    buckets: dict[str, list[Any]] = {"FC": [], "FCA": [], "SCC": [], "OTHER": []}
    modern_scc_available = any(_is_modern_scc(row.citation) for row in rows)
    for row in rows:
        buckets[_court_bucket(row.court, row.citation)].append(row)

    selected: list[Any] = []
    selected.extend(buckets["FC"][:3])
    selected.extend(buckets["FCA"][:1])
    if modern_scc_available:
        selected.extend([row for row in buckets["SCC"] if _is_modern_scc(row.citation)][:1])
    for bucket in ("FC", "FCA", "SCC", "OTHER"):
        for row in buckets[bucket]:
            if len(selected) >= 5:
                break
            if row not in selected:
                selected.append(row)
        if len(selected) >= 5:
            break
    if len(selected) != 5:
        raise RuntimeError(f"expected at least five full-text cases, found {len(selected)}")
    return selected, modern_scc_available


def _load_case_rows(session: Any) -> list[Any]:
    query = (
        select(Case.id, Case.title, Case.court, Case.citation, Case.full_text)
        .where(Case.full_text.is_not(None), Case.full_text != "")
        .where(Case.citation.is_not(None), Case.citation != "")
        .order_by(Case.id.desc())
    )
    return list(session.execute(query))


def _case_payload(row: Any) -> dict[str, Any]:
    text = str(row.full_text)
    occurrences = [occurrence_from_match(text, match) for match in extract_case_citation_matches(text)]
    return {
        "case_id": int(row.id),
        "court": row.court,
        "citation": row.citation,
        "title": row.title,
        "occurrences": occurrences,
        "occurrence_count": len(occurrences),
    }


def build_fixture() -> dict[str, Any]:
    with SessionLocal() as session:
        rows = _load_case_rows(session)
        selected, modern_scc_available = select_cases(rows)

    cases = [_case_payload(row) for row in selected]
    counts = {str(case["case_id"]): case["occurrence_count"] for case in cases}
    return {
        "fixture_name": "five_case_citation_gold_candidate",
        "review_status": "proposed",
        "selection": {
            "method": "descending case ID, preferring 3 FC, 1 FCA, and 1 modern SCC",
            "modern_scc_available": modern_scc_available,
            "modern_scc_definition": f"SCC citation year >= {MODERN_SCC_YEAR}",
        },
        "review_guide": {
            "status": "candidate/proposed, not confirmed gold",
            "instructions": [
                "For every occurrence, confirm valid or invalid.",
                "Confirm the expected kind for every valid occurrence.",
                "Record any missed case-to-case citations not emitted here.",
            ],
            "external_api_used": False,
            "database_writes": False,
        },
        "cases": cases,
        "summary": {
            "case_count": len(cases),
            "occurrence_counts_by_case": counts,
            "total_occurrences": sum(counts.values()),
            "exact_span_valid_count": sum(occ["exact_span_valid"] for case in cases for occ in case["occurrences"]),
            "exact_span_invalid_count": sum(not occ["exact_span_valid"] for case in cases for occ in case["occurrences"]),
            "counts_by_kind": dict(Counter(occ["kind"] for case in cases for occ in case["occurrences"])),
        },
    }


def verify_fixture(output: Path) -> None:
    fixture = json.loads(output.read_text(encoding="utf-8"))
    if fixture.get("review_status") != "proposed":
        raise RuntimeError("fixture is not marked proposed")
    with SessionLocal() as session:
        row_by_id = {int(row.id): row for row in _load_case_rows(session)}
        for case in fixture.get("cases", []):
            case_id = int(case["case_id"])
            row = row_by_id.get(case_id)
            if row is None:
                raise RuntimeError(f"case {case_id} is missing or no longer has full text")
            source = str(row.full_text)
            matches = extract_case_citation_matches(source)
            occurrences = case.get("occurrences", [])
            if len(matches) != len(occurrences):
                raise RuntimeError(f"case {case_id} occurrence count changed")
            for match, occurrence in zip(matches, occurrences):
                if occurrence["review_status"] != "proposed":
                    raise RuntimeError(f"case {case_id} occurrence is not proposed")
                if not validate_match_span(source, occurrence["offset_start"], occurrence["offset_end"], occurrence["citation_text"]):
                    raise RuntimeError(f"case {case_id} has an invalid exact span")
                emitted = (match.kind, match.citation_text, match.offset_start, match.offset_end)
                recorded = (occurrence["kind"], occurrence["citation_text"], occurrence["offset_start"], occurrence["offset_end"])
                if emitted != recorded:
                    raise RuntimeError(f"case {case_id} occurrence differs from extractor output")
    print(f"verified {len(fixture.get('cases', []))} cases and {fixture['summary']['total_occurrences']} occurrences")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--verify", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.verify:
        verify_fixture(args.output)
        return
    fixture = build_fixture()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(fixture, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"wrote proposed candidate fixture for {len(fixture['cases'])} cases to {args.output}")


if __name__ == "__main__":
    main()
