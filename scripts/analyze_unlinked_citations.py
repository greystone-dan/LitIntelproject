"""Read-only study of case citations that have no target case in the library.

Counts linked and unlinked case citations from FC, FCA and SCC decisions, sorts every
unlinked row into a reason bucket, and writes a stratified sample for hand checking.

Only SELECTs run, inside one READ ONLY transaction. No model, no network, no writes.
Use --counts-only first: it skips the per-row bucketing and is quick.

    python scripts/analyze_unlinked_citations.py --counts-only
    python scripts/analyze_unlinked_citations.py --output-dir C:\\ilit_backups\\unlinked_study
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sqlalchemy import text

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import (  # noqa: E402
	FORMAL_CIT_RE,
	REPORTED_CIT_RE,
	_citation_variants,
	_normalize_alias_lookup,
)

CASE_KINDS = ("case", "case_name", "case_short", "neutral")
DEFAULT_SOURCE_COURTS = r"^(FC|FCA|SCC|Federal Court|Federal Court of Appeal|Supreme Court of Canada)$"
LIBRARY_COURT_CODES = {
	"FC": "FC", "FCT": "FC", "CF": "FC",
	"FCA": "FCA", "CAF": "FCA", "FCJ": "FCA",
	"SCC": "SCC", "CSC": "SCC",
	"RAD": "RAD", "SAR": "RAD", "RPD": "RPD", "SPR": "RPD",
}
SELF_RE = re.compile(r"\b(?:id|ibid)\b\.?|\bsupra\b|\babove\b", re.IGNORECASE)
CONNECTOR_RE = re.compile(r"\s+(?:v\.?|vs\.?|c\.?|versus)\s+", re.IGNORECASE)


def _formal(raw: str):
	for m in FORMAL_CIT_RE.finditer(raw or ""):
		year, court, number = m.groups()
		yield int(year), court.replace(".", "").upper(), int(number)


def build_library_profile(session) -> dict:
	"""Citation index plus per court-year number ranges, from the cases table."""
	index: dict[str, set[int]] = defaultdict(set)
	numbers: dict[tuple[str, int], set[int]] = defaultdict(set)
	court_counts: Counter = Counter()
	null_cite: Counter = Counter()
	title_index: dict[str, set[int]] = defaultdict(set)
	rows = session.execute(text("SELECT id, title, court, citation, secondary_citation FROM cases"))
	for case_id, title, court, citation, secondary in rows:
		court_counts[court] += 1
		if not citation:
			null_cite[court] += 1
		key = _normalize_alias_lookup(title or "")
		if key:
			title_index[key].add(case_id)
		for raw in (citation, secondary):
			if not raw:
				continue
			for variant in _citation_variants(raw):
				index[variant].add(case_id)
			for year, code, number in _formal(raw):
				if code in LIBRARY_COURT_CODES:
					numbers[(LIBRARY_COURT_CODES[code], year)].add(number)
	return {
		"index": index,
		"numbers": numbers,
		"court_counts": court_counts,
		"null_cite": null_cite,
		"title_index": title_index,
	}


def classify(raw: str, kind: str, source_case_id: int, lib: dict) -> str:
	"""Return one reason bucket for an unlinked case citation."""
	raw = " ".join((raw or "").split())
	if len(re.sub(r"[^A-Za-z0-9]", "", raw)) < 4:
		return "junk_or_empty"
	index = lib["index"]
	hits: set[int] = set()
	for variant in _citation_variants(raw):
		hits |= index.get(variant, set())
	others = hits - {source_case_id}
	if len(others) == 1:
		return "LINKABLE_exact_citation_in_library"
	if len(others) > 1:
		return "ambiguous_citation_two_library_cases"
	if hits:
		return "self_citation"

	formal = list(_formal(raw))
	if formal:
		year, code, number = formal[0]
		if code == "CANLII":
			return "canlii_cite_not_in_library"
		court = LIBRARY_COURT_CODES.get(code)
		if court:
			known = lib["numbers"].get((court, year))
			if not known:
				return f"library_court_year_absent_{court}"
			if number > max(known):
				return f"library_court_number_above_max_{court}"
			return f"library_court_gap_in_range_{court}"
		return "neutral_other_court"
	if REPORTED_CIT_RE.search(raw):
		return "reporter_cite_not_in_library"

	base = CONNECTOR_RE.split(raw, maxsplit=1)
	title_key = _normalize_alias_lookup(re.split(r",\s*(?:at\s+)?para", raw, maxsplit=1, flags=re.I)[0])
	matches = lib["title_index"].get(title_key, set()) - {source_case_id}
	if len(matches) == 1:
		return "LINKABLE_name_unique_title"
	if len(matches) > 1:
		return "name_ambiguous_title"
	if SELF_RE.search(raw) and len(base) < 2:
		return "id_supra_above_no_name"
	if len(base) == 2:
		return "name_no_library_match"
	return "other_no_signal"


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--source-courts", default=DEFAULT_SOURCE_COURTS, help="Regex on cases.court for citing decisions.")
	parser.add_argument("--counts-only", action="store_true")
	parser.add_argument("--sample-per-bucket", type=int, default=25)
	parser.add_argument("--output-dir", type=Path, default=None)
	parser.add_argument("--seed", type=int, default=7)
	parser.add_argument("--batch-size", type=int, default=20000)
	args = parser.parse_args()

	from backend.database import SessionLocal

	rng = random.Random(args.seed)
	report: dict = {}
	kinds = ",".join(f"'{k}'" for k in CASE_KINDS)
	with SessionLocal() as session:
		session.execute(text("SET TRANSACTION READ ONLY"))
		session.execute(text("SET LOCAL statement_timeout = 0"))
		court_rows = session.execute(
			text("SELECT court, count(*) FROM cases GROUP BY 1 ORDER BY 2 DESC")
		).all()
		report["cases_by_court"] = {c: n for c, n in court_rows}
		params = {"src": args.source_courts}
		report["linked_by_source_court_and_kind"] = [
			[c, k, bool(linked), n]
			for c, k, linked, n in session.execute(
				text(
					f"""SELECT s.court, ci.citation_kind, ci.target_case_id IS NOT NULL, count(*)
					FROM citations ci JOIN cases s ON s.id = ci.source_case_id
					WHERE s.court ~* :src AND ci.citation_kind IN ({kinds})
					GROUP BY 1,2,3 ORDER BY 1,2,3"""
				),
				params,
			)
		]
		if args.counts_only:
			print(json.dumps(report, indent=2, default=str))
			return

		lib = build_library_profile(session)
		report["library_cases_without_citation_by_court"] = dict(lib["null_cite"])
		buckets: Counter = Counter()
		by_court_bucket: Counter = Counter()
		samples: dict[str, list] = defaultdict(list)
		seen: Counter = Counter()
		missing_formal: Counter = Counter()
		result = session.execute(
			text(
				f"""SELECT ci.id, ci.source_case_id, s.court, ci.citation_kind,
				coalesce(ci.normalized_citation, ci.citation_text, ''), ci.citation_text, s.citation, s.title
				FROM citations ci JOIN cases s ON s.id = ci.source_case_id
				WHERE s.court ~* :src AND ci.citation_kind IN ({kinds}) AND ci.target_case_id IS NULL"""
			),
			params,
		).yield_per(args.batch_size)
		for cid, src_id, court, kind, raw, text_raw, src_cite, src_title in result:
			bucket = classify(raw, kind, src_id, lib)
			buckets[bucket] += 1
			by_court_bucket[(court, bucket)] += 1
			if bucket.startswith("library_court_") or bucket == "LINKABLE_exact_citation_in_library":
				for year, code, number in _formal(raw):
					missing_formal[(LIBRARY_COURT_CODES.get(code, code), year, number)] += 1
					break
			seen[bucket] += 1
			pool = samples[bucket]
			if len(pool) < args.sample_per_bucket:
				pool.append((cid, src_id, court, kind, raw, src_cite, src_title))
			else:
				j = rng.randrange(seen[bucket])
				if j < args.sample_per_bucket:
					pool[j] = (cid, src_id, court, kind, raw, src_cite, src_title)
		report["unlinked_total"] = sum(buckets.values())
		report["buckets"] = dict(buckets.most_common())
		report["buckets_by_court"] = {f"{c} | {b}": n for (c, b), n in sorted(by_court_bucket.items())}
		by_year: Counter = Counter()
		for (court, year, number), n in missing_formal.items():
			by_year[(court, year)] += 1
		report["distinct_cited_library_court_citations_missing_by_court_year"] = {
			f"{c} {y}": n for (c, y), n in sorted(by_year.items())
		}

	text_out = json.dumps(report, indent=2, default=str)
	print(text_out)
	if args.output_dir is not None:
		args.output_dir.mkdir(parents=True, exist_ok=True)
		(args.output_dir / "summary.json").write_text(text_out + "\n", encoding="utf-8")
		with (args.output_dir / "sample.csv").open("w", newline="", encoding="utf-8") as handle:
			writer = csv.writer(handle)
			writer.writerow(["bucket", "citation_id", "source_case_id", "source_court", "kind", "citation", "source_cite", "source_title"])
			for bucket, rows in sorted(samples.items()):
				for row in rows:
					writer.writerow([bucket, *row])


if __name__ == "__main__":
	main()
