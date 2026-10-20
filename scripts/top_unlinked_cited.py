"""Read-only: most cited case citations that have no target decision in the library.

Groups unlinked case citations from FC, FCA and SCC decisions by a cleaned key (neutral or
reporter citation when present, otherwise the case name without pinpoint), counts occurrences
and distinct citing decisions, and writes the top rows with the library-gap bucket.

SELECTs only, one READ ONLY transaction, no model, no network.

    python scripts/top_unlinked_cited.py --output C:\\ilit_backups\\unlinked_study\\top_unlinked.csv
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sqlalchemy import text

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import FORMAL_CIT_RE, REPORTED_CIT_RE  # noqa: E402
from scripts.analyze_unlinked_citations import (  # noqa: E402
	CASE_KINDS,
	DEFAULT_SOURCE_COURTS,
	build_library_profile,
	classify,
)

PINPOINT_TAIL_RE = re.compile(r",?\s*(?:at\s+)?(?:paras?\.?|paragraphs?|pp?\.)\s*\d.*$", re.IGNORECASE)


def group_key(raw: str) -> str:
	raw = " ".join((raw or "").split())
	m = FORMAL_CIT_RE.search(raw)
	if m:
		year, court, number = m.groups()
		return f"{year} {court.replace('.', '').upper()} {int(number)}"
	m = REPORTED_CIT_RE.search(raw)
	if m:
		year = m.group(1) or m.group(2) or m.group(3)
		return f"[{year}] {int(m.group(4))} {re.sub(r'[^A-Z0-9]', '', m.group(5).upper())} {int(m.group(6))}"
	return PINPOINT_TAIL_RE.sub("", raw).strip(" ,;:-").lower()


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--source-courts", default=DEFAULT_SOURCE_COURTS)
	parser.add_argument("--top", type=int, default=300)
	parser.add_argument("--output", type=Path, required=True)
	args = parser.parse_args()

	from backend.database import SessionLocal

	kinds = ",".join(f"'{k}'" for k in CASE_KINDS)
	counts: Counter = Counter()
	citing: dict[str, set[int]] = defaultdict(set)
	spellings: dict[str, Counter] = defaultdict(Counter)
	with SessionLocal() as session:
		session.execute(text("SET TRANSACTION READ ONLY"))
		lib = build_library_profile(session)
		rows = session.execute(
			text(
				f"""SELECT ci.source_case_id, coalesce(ci.citation_text, ci.normalized_citation, '')
				FROM citations ci JOIN cases s ON s.id = ci.source_case_id
				WHERE s.court ~* :src AND ci.citation_kind IN ({kinds}) AND ci.target_case_id IS NULL"""
			),
			{"src": args.source_courts},
		).yield_per(20000)
		for src_id, raw in rows:
			key = group_key(raw)
			if len(key) < 4:
				continue
			counts[key] += 1
			citing[key].add(src_id)
			if len(spellings[key]) < 20:
				spellings[key][" ".join(raw.split())[:160]] += 1
	args.output.parent.mkdir(parents=True, exist_ok=True)
	with args.output.open("w", newline="", encoding="utf-8") as handle:
		writer = csv.writer(handle)
		writer.writerow(["rank", "key", "times_cited", "distinct_citing_decisions", "bucket", "common_spellings"])
		for rank, (key, n) in enumerate(counts.most_common(args.top), 1):
			bucket = classify(key, "case", -1, lib)
			spell = " || ".join(s for s, _ in spellings[key].most_common(3))
			writer.writerow([rank, key, n, len(citing[key]), bucket, spell])
	print(f"wrote {args.output} ({min(args.top, len(counts))} of {len(counts)} distinct keys)")


if __name__ == "__main__":
	main()
