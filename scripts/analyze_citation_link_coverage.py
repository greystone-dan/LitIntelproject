"""Explain why unresolved citation rows do not link (read-only: SELECTs only).

Each unresolved case-citation row goes into one bucket: already linkable by the
standard rules, linkable by the extended exact-key rules, or a named reason it
cannot link (cited case not in the library, other court, ambiguous key, name
only, back reference, and so on). Also reports what the library's own citation
fields look like, because a cite can only link if the library case carries the
same key.

    python scripts/analyze_citation_link_coverage.py --output logs/link_coverage.json
    python scripts/analyze_citation_link_coverage.py --probe-case 61200 --limit 50000
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citation_link_rules import build_index, classify_unresolved, title_counts_for
from backend.citations import CASE_CITATION_KINDS, _citation_variants, build_local_case_resolution_index
from backend.database import Case, Citation, SessionLocal

SAMPLES_PER_BUCKET = 5


def legacy_would_link(text: str, source_case_id: int, legacy_index: dict[str, int | None]) -> bool:
	targets = {
		legacy_index[variant]
		for variant in _citation_variants(text)
		if variant in legacy_index and legacy_index[variant] not in (None, source_case_id)
	}
	return len(targets) == 1


def library_census(session, per_court_samples: int = 4) -> dict[str, object]:
	by_court: dict[str, Counter] = defaultdict(Counter)
	samples: dict[str, list[dict[str, object]]] = defaultdict(list)
	for case_id, court, decision_date, citation, secondary in session.execute(
		select(Case.id, Case.court, Case.date, Case.citation, Case.secondary_citation)
	):
		counts = by_court[court or "?"]
		counts["cases"] += 1
		counts["with_citation"] += 1 if citation else 0
		counts["with_secondary_citation"] += 1 if secondary else 0
		era = "pre1985" if decision_date and decision_date.year < 1985 else "1985+"
		bucket = samples[f"{court}|{era}"]
		if len(bucket) < per_court_samples and (citation or secondary):
			bucket.append({"id": case_id, "year": decision_date.year if decision_date else None, "citation": citation, "secondary": secondary})
	return {"by_court": {court: dict(counts) for court, counts in by_court.items()}, "samples": samples}


def analyze(session, limit: int | None, batch_size: int, probe_case: int | None) -> dict[str, object]:
	legacy_index = build_local_case_resolution_index(session)
	key_index = build_index(session.execute(select(Case.id, Case.title, Case.citation, Case.secondary_citation)))
	title_counts = title_counts_for(key_index)

	buckets: Counter = Counter()
	details: dict[str, Counter] = defaultdict(Counter)
	samples: dict[str, list[dict[str, object]]] = defaultdict(list)
	probe: Counter = Counter()
	probe_samples: list[dict[str, object]] = []
	inspected = 0

	query = (
		select(Citation.id, Citation.source_case_id, Citation.citation_kind, Citation.citation_text, Citation.normalized_citation)
		.where(Citation.target_case_id.is_(None), Citation.citation_kind.in_(sorted(CASE_CITATION_KINDS)))
		.order_by(Citation.id)
	)
	for row_id, source_case_id, kind, citation_text, normalized in session.execute(query).yield_per(batch_size):
		if limit is not None and inspected >= limit:
			break
		inspected += 1
		text = normalized or citation_text or ""
		if legacy_would_link(text, source_case_id, legacy_index):
			bucket, detail = "would_link:standard_rules", None
		else:
			bucket, detail = classify_unresolved(text, kind, source_case_id, key_index, title_counts)
		buckets[bucket] += 1
		if detail:
			details[bucket][detail] += 1
		if len(samples[bucket]) < SAMPLES_PER_BUCKET:
			samples[bucket].append({"id": row_id, "source_case_id": source_case_id, "kind": kind, "text": text[:200]})
		if probe_case is not None and source_case_id == probe_case:
			probe[bucket] += 1
			if len(probe_samples) < 25:
				probe_samples.append({"bucket": bucket, "kind": kind, "text": text[:160]})

	gains = sum(count for name, count in buckets.items() if name.startswith("would_link:") and name != "would_link:standard_rules")
	return {
		"inspected": inspected,
		"buckets": dict(buckets.most_common()),
		"extended_rules_gain": gains,
		"standard_rules_would_link": buckets.get("would_link:standard_rules", 0),
		"bucket_details_top40": {name: dict(counter.most_common(40)) for name, counter in details.items()},
		"samples": samples,
		"probe_case": {"id": probe_case, "buckets": dict(probe), "samples": probe_samples} if probe_case else None,
		"library_census": library_census(session),
	}


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--limit", type=int, default=None, help="Stop after this many unresolved rows.")
	parser.add_argument("--batch-size", type=int, default=20_000)
	parser.add_argument("--probe-case", type=int, default=None, help="Also break down one source case (for example 61200).")
	parser.add_argument("--output", type=Path, default=None)
	args = parser.parse_args()
	with SessionLocal() as session:
		report = analyze(session, args.limit, args.batch_size, args.probe_case)
		session.rollback()
	serialized = json.dumps(report, indent=2, ensure_ascii=False, default=str)
	if args.output is not None:
		args.output.parent.mkdir(parents=True, exist_ok=True)
		args.output.write_text(serialized + "\n", encoding="utf-8")
	print(serialized)


if __name__ == "__main__":
	main()
