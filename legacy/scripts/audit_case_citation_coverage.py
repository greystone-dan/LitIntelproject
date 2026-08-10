from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

from sqlalchemy import select

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend.citations import _BARE_CASE_ALIAS_NOISE, _extract_short_aliases, extract_case_citation_matches
from backend.database import Case, SessionLocal


DEFAULT_CSV = ROOT / "data" / "eval" / "fc_priority_seed_case_map.csv"
DEFAULT_OUT = ROOT / "data" / "eval" / "reports" / "case_citation_coverage.json"
PARENTHETICAL_RE = re.compile(r"\([^()]{1,240}\)")
PERSON_FRAGMENT_RE = re.compile(r"^(?:Mr|Ms|Mrs|Dr)\.?\s+v\.?$", re.IGNORECASE)


def load_case_ids(path: Path) -> list[int]:
    case_ids: list[int] = []
    seen: set[int] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            raw = str(row.get("local_case_id") or "").strip()
            if str(row.get("status") or "") != "matched" or not raw.isdigit():
                continue
            case_id = int(raw)
            if case_id not in seen:
                seen.add(case_id)
                case_ids.append(case_id)
    return case_ids


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit deterministic case-citation span coverage.")
    parser.add_argument("--csv", default=str(DEFAULT_CSV))
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()

    case_ids = load_case_ids(Path(args.csv))
    if args.limit > 0:
        case_ids = case_ids[: args.limit]

    session = SessionLocal()
    issues: list[dict[str, object]] = []
    totals = {
        "cases": 0,
        "citations": 0,
        "span_errors": 0,
        "anchored_alias_occurrences": 0,
        "missed_anchored_aliases": 0,
        "missed_parentheticals": 0,
        "person_fragments": 0,
    }
    try:
        cases = list(session.scalars(select(Case).where(Case.id.in_(case_ids))))
        by_id = {case.id: case for case in cases}
        for case_id in case_ids:
            case = by_id.get(case_id)
            if case is None:
                continue
            text = case.full_text or case.summary or ""
            matches = extract_case_citation_matches(text)
            totals["cases"] += 1
            totals["citations"] += len(matches)

            span_errors = [
                match
                for match in matches
                if text[match.offset_start:match.offset_end] != match.citation_text
            ]
            person_fragments = [match for match in matches if PERSON_FRAGMENT_RE.fullmatch(match.citation_text.strip())]
            aliases: set[str] = set()
            for match in matches:
                if match.kind != "case":
                    continue
                parties_match = re.match(r"(.+?),\s+(?:19|20)\d{2}\s+", match.normalized_citation)
                if parties_match:
                    aliases.update(_extract_short_aliases(parties_match.group(1)))

            alias_occurrences: list[re.Match[str]] = []
            alias_patterns: list[re.Pattern[str]] = []
            for alias in sorted(aliases, key=len, reverse=True):
                if len(alias) < 4 or alias.lower() in _BARE_CASE_ALIAS_NOISE:
                    continue
                pattern = re.compile(rf"(?<![\w'’-]){re.escape(alias)}(?![\w'’-])", re.IGNORECASE)
                alias_patterns.append(pattern)
                alias_occurrences.extend(pattern.finditer(text))
            occurrence_spans = {(occurrence.start(), occurrence.end()) for occurrence in alias_occurrences}
            missed_anchored_aliases = [
                text[start:end]
                for start, end in sorted(occurrence_spans)
                if not any(match.offset_start <= start and match.offset_end >= end for match in matches)
            ]
            missed_parentheticals = []
            for occurrence in PARENTHETICAL_RE.finditer(text):
                named_aliases = [
                    pattern
                    for pattern in alias_patterns
                    if pattern.search(occurrence.group(0))
                    and re.search(r"\bpara(?:s|graphs?)?\.?\s+\d", occurrence.group(0), re.IGNORECASE)
                ]
                if len(named_aliases) != 1:
                    continue
                if not any(
                    match.offset_start <= occurrence.start() and match.offset_end >= occurrence.end()
                    for match in matches
                ):
                    missed_parentheticals.append(occurrence.group(0))

            totals["span_errors"] += len(span_errors)
            totals["person_fragments"] += len(person_fragments)
            totals["anchored_alias_occurrences"] += len(occurrence_spans)
            totals["missed_anchored_aliases"] += len(missed_anchored_aliases)
            totals["missed_parentheticals"] += len(missed_parentheticals)
            if span_errors or person_fragments or missed_anchored_aliases or missed_parentheticals:
                issues.append(
                    {
                        "case_id": case.id,
                        "title": case.title,
                        "citation": case.citation,
                        "span_errors": len(span_errors),
                        "person_fragments": [match.citation_text for match in person_fragments],
                        "missed_anchored_aliases": missed_anchored_aliases,
                        "missed_parentheticals": missed_parentheticals,
                    }
                )
    finally:
        session.close()

    report = {"summary": totals, "cases_with_issues": issues}
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(totals, indent=2))
    print(f"report={out_path}")


if __name__ == "__main__":
    main()