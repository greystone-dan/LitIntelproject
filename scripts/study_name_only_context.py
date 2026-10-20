"""Read-only: how many name-only unlinked citations could be linked from the same decision.

A name-only citation such as "Hunter v. Canada" often sits in a decision that also cites the
same case in full ("Hunter v. Canada (MCI), 2010 FC 123") and that full citation is already
linked. This study counts, for FC, FCA and SCC citing decisions, unlinked case citations without
a formal citation and sorts them by what the same decision shows:

  SAME_DECISION_LINKED_UNIQUE      one linked row with the same party names, one target
  SAME_DECISION_LINKED_CONFLICT    linked rows with the same party names point at different targets
  SAME_DECISION_FULL_CITE_UNLINKED same names appear with a formal cite that is also unlinked
  SURNAME_ONLY_LINKED_UNIQUE       single-word alias; one linked row in the decision shares the first surname
  NO_CONTEXT                       nothing in the decision to go on

SELECTs only in a READ ONLY transaction; no model, no network, no writes.

    python scripts/study_name_only_context.py --output-dir C:\\ilit_backups\\unlinked_study
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from itertools import groupby
from pathlib import Path

from sqlalchemy import text

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import FORMAL_CIT_RE, REPORTED_CIT_RE  # noqa: E402
from scripts.analyze_unlinked_citations import CASE_KINDS, DEFAULT_SOURCE_COURTS  # noqa: E402

PINPOINT_RE = re.compile(r",?\s*(?:at\s+)?(?:paras?\.?|paragraphs?|pp?\.)\s*\d.*$", re.IGNORECASE)
PAREN_RE = re.compile(r"\([^)]*\)")
CITE_TAIL_RE = re.compile(r",\s*(?:\[?(?:19|20)\d{2}\]?|\(\d{4}\)).*$")
CONNECTOR_RE = re.compile(r"\s+(?:v\.?|vs\.?|c\.?|versus)\s+", re.IGNORECASE)


def has_formal_cite(raw: str) -> bool:
	return bool(FORMAL_CIT_RE.search(raw or "") or REPORTED_CIT_RE.search(raw or ""))


def party_key(raw: str) -> str:
	"""'Hunter v. Canada (MCI), 2010 FC 1, at para 5' -> 'hunter v canada'."""
	value = " ".join((raw or "").split())
	value = PINPOINT_RE.sub("", value)
	value = CITE_TAIL_RE.sub("", value)
	value = PAREN_RE.sub(" ", value)
	parts = CONNECTOR_RE.split(value, maxsplit=1)
	if len(parts) != 2:
		return re.sub(r"[^a-z0-9 ]", "", value.lower()).strip()
	left, right = (re.sub(r"[^a-z0-9 ]", "", p.lower()).strip() for p in parts)
	return f"{' '.join(left.split())} v {' '.join(right.split())}".strip()


def first_surname(key: str) -> str:
	return key.split(" v ")[0].split()[0] if key else ""


def classify_decision(rows: list[tuple]) -> list[tuple[str, tuple, int | None, str | None]]:
	"""rows: (id, kind, raw, target). Returns (signal, row, candidate_target, matching_text) per unlinked name-only row."""
	linked_by_key: dict[str, dict[int, str]] = defaultdict(dict)
	linked_by_surname: dict[str, dict[int, str]] = defaultdict(dict)
	cited_unlinked_keys: set[str] = set()
	for _cid, _kind, raw, target in rows:
		key = party_key(raw)
		if " v " not in key:
			continue
		if target is not None:
			linked_by_key[key].setdefault(target, raw)
			linked_by_surname[first_surname(key)].setdefault(target, raw)
		elif has_formal_cite(raw):
			cited_unlinked_keys.add(key)
	out = []
	for row in rows:
		_cid, kind, raw, target = row
		if target is not None or has_formal_cite(raw):
			continue
		key = party_key(raw)
		if " v " in key:
			hits = linked_by_key.get(key, {})
			if len(hits) == 1:
				(t, m), = hits.items()
				out.append(("SAME_DECISION_LINKED_UNIQUE", row, t, m))
			elif len(hits) > 1:
				out.append(("SAME_DECISION_LINKED_CONFLICT", row, None, " || ".join(hits.values())[:300]))
			elif key in cited_unlinked_keys:
				out.append(("SAME_DECISION_FULL_CITE_UNLINKED", row, None, None))
			else:
				out.append(("NO_CONTEXT", row, None, None))
		elif key and len(key.split()) == 1:
			hits = linked_by_surname.get(key, {})
			if len(hits) == 1:
				(t, m), = hits.items()
				out.append(("SURNAME_ONLY_LINKED_UNIQUE", row, t, m))
			else:
				out.append(("NO_CONTEXT", row, None, None))
		else:
			out.append(("NO_CONTEXT", row, None, None))
	return out


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--source-courts", default=DEFAULT_SOURCE_COURTS)
	parser.add_argument("--sample-per-signal", type=int, default=150)
	parser.add_argument("--output-dir", type=Path, required=True)
	parser.add_argument("--seed", type=int, default=7)
	args = parser.parse_args()

	from backend.database import SessionLocal

	rng = random.Random(args.seed)
	kinds = ",".join(f"'{k}'" for k in CASE_KINDS)
	counts: Counter = Counter()
	by_court: Counter = Counter()
	seen: Counter = Counter()
	samples: dict[str, list] = defaultdict(list)
	with SessionLocal() as session:
		session.execute(text("SET TRANSACTION READ ONLY"))
		result = session.execute(
			text(
				f"""SELECT ci.source_case_id, s.court, ci.id, ci.citation_kind,
				coalesce(ci.citation_text, ci.normalized_citation, ''), ci.target_case_id
				FROM citations ci JOIN cases s ON s.id = ci.source_case_id
				WHERE s.court ~* :src AND ci.citation_kind IN ({kinds})
				ORDER BY ci.source_case_id, ci.id"""
			),
			{"src": args.source_courts},
		).yield_per(20000)
		for source_id, group in groupby(result, key=lambda r: (r[0], r[1])):
			court = source_id[1]
			rows = [(r[2], r[3], r[4], r[5]) for r in group]
			for signal, row, target, matching in classify_decision(rows):
				counts[signal] += 1
				by_court[(court, signal)] += 1
				seen[signal] += 1
				entry = (signal, source_id[0], court, row[0], row[1], row[2], target, matching)
				pool = samples[signal]
				if len(pool) < args.sample_per_signal:
					pool.append(entry)
				else:
					j = rng.randrange(seen[signal])
					if j < args.sample_per_signal:
						pool[j] = entry
		targets = {e[6] for pool in samples.values() for e in pool if e[6] is not None}
		titles = {}
		if targets:
			titles = dict(
				session.execute(
					text("SELECT id, coalesce(title,'') || ' | ' || coalesce(citation,'') FROM cases WHERE id = ANY(:ids)"),
					{"ids": sorted(targets)},
				).all()
			)
	args.output_dir.mkdir(parents=True, exist_ok=True)
	report = {
		"name_only_unlinked_total": sum(counts.values()),
		"signals": dict(counts.most_common()),
		"signals_by_court": {f"{c} | {s}": n for (c, s), n in sorted(by_court.items())},
	}
	(args.output_dir / "name_only_context.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
	with (args.output_dir / "name_only_context_sample.csv").open("w", newline="", encoding="utf-8") as handle:
		writer = csv.writer(handle)
		writer.writerow(["signal", "source_case_id", "source_court", "citation_id", "kind", "unlinked_text", "candidate_target_id", "candidate_title_cite", "matching_linked_text"])
		for signal, pool in sorted(samples.items()):
			for _s, src, court, cid, kind, raw, target, matching in pool:
				writer.writerow([signal, src, court, cid, kind, raw, target, titles.get(target, ""), matching or ""])
	print(json.dumps(report, indent=2))


if __name__ == "__main__":
	main()
