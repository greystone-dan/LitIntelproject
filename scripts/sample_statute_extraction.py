"""Draw a random sample of real decisions and write the statute references the extractor finds, for hand-checking.

READ-ONLY: SELECTs from cases and runs the extractor in memory; writes nothing to the database.
For each sampled decision it records every extracted statute reference (text, instrument, pinpoint,
context) and every "loose" provision mention (s. 12, subsection 5(1), paragraph 3(b) ...) that no
extracted reference covers, so both precision and recall can be hand-checked.

Sampling is deterministic for a given --seed (md5 order), per court, so a second run reproduces it.

Usage: python scripts/sample_statute_extraction.py --cases-per-court 40 --seed 20261006 --out sample.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import extract_statute_reference_matches
from backend.statutes import parse_legislation_citation

LOOSE_PROVISION_RE = re.compile(
    r"\b(?:ss?\.|sections?|subsections?|paragraphs?|paras?\.|rules?|regulation)\s*R?\d{1,3}(?:\.\d+)?[A-Za-z]?(?:\s*\([A-Za-z0-9]+\))*",
    re.IGNORECASE,
)
CONTEXT = 120


def analyze_text(text: str) -> dict[str, Any]:
    matches = extract_statute_reference_matches(text)
    extracted = []
    for match in matches:
        parsed = parse_legislation_citation(match.normalized_citation or match.citation_text)
        extracted.append(
            {
                "text": match.citation_text,
                "normalized": match.normalized_citation,
                "instrument_key": parsed.instrument_key if parsed else None,
                "pinpoint": parsed.pinpoint if parsed else None,
                "start": match.offset_start,
                "context": text[max(0, match.offset_start - CONTEXT) : match.offset_end + CONTEXT],
            }
        )
    spans = [(m.offset_start, m.offset_end) for m in matches]
    loose = []
    for found in LOOSE_PROVISION_RE.finditer(text):
        if any(start <= found.start() < end for start, end in spans):
            continue
        loose.append(
            {
                "text": found.group(0),
                "start": found.start(),
                "context": text[max(0, found.start() - CONTEXT) : found.end() + CONTEXT],
            }
        )
    return {"extracted": extracted, "loose_unmatched": loose}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases-per-court", type=int, default=40)
    parser.add_argument("--seed", default="20261006")
    parser.add_argument("--min-court-cases", type=int, default=500, help="only courts with at least this many decisions")
    parser.add_argument("--max-chars", type=int, default=400000, help="skip text beyond this length (keeps the run fast)")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    from sqlalchemy import text as sql

    from backend.database import SessionLocal

    with SessionLocal() as db, args.out.open("w", encoding="utf-8") as handle:
        courts = [
            row[0]
            for row in db.execute(
                sql("SELECT court FROM cases WHERE court IS NOT NULL GROUP BY court HAVING count(*) >= :n ORDER BY count(*) DESC"),
                {"n": args.min_court_cases},
            )
        ]
        print("courts:", courts)
        for court in courts:
            rows = db.execute(
                sql(
                    "SELECT id, citation, title, full_text FROM cases WHERE court = :court AND full_text IS NOT NULL "
                    "AND length(full_text) BETWEEN 2000 AND :maxchars ORDER BY md5(id::text || :seed) LIMIT :n"
                ),
                {"court": court, "seed": args.seed, "n": args.cases_per_court, "maxchars": args.max_chars},
            ).all()
            for case_id, citation, title, full_text in rows:
                record = {"case_id": case_id, "court": court, "citation": citation, "title": title}
                record.update(analyze_text(full_text))
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            print(court, len(rows), "decisions sampled")


if __name__ == "__main__":
    main()
