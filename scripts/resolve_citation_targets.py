"""Resolve stored citation rows to locally available target cases.

This intentionally does not extract citations again or call external services.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import NEUTRAL_CIT_RE, normalize_neutral_citation
from backend.database import Case, Citation, SessionLocal


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--batch-size", type=int, default=5_000)
	parser.add_argument("--limit", type=int, default=None, help="Maximum unresolved rows to inspect.")
	parser.add_argument("--dry-run", action="store_true")
	return parser.parse_args()


def _citation_variants(value: str) -> list[str]:
	match = NEUTRAL_CIT_RE.search(value)
	if match is None:
		return []
	normalized = normalize_neutral_citation(match).upper()
	variants = [normalized]
	if " FCT " in f" {normalized} ":
		variants.append(normalized.replace(" FCT ", " FC "))
	if " FC " in f" {normalized} ":
		variants.append(normalized.replace(" FC ", " FCT "))
	return list(dict.fromkeys(variants))


def _local_citation_index(session) -> dict[str, int | None]:
	index: dict[str, int | None] = {}
	for case_id, citation, secondary_citation in session.execute(
		select(Case.id, Case.citation, Case.secondary_citation)
	):
		for raw_value in (citation, secondary_citation):
			if not raw_value:
				continue
			for variant in _citation_variants(raw_value):
				if variant in index and index[variant] != case_id:
					index[variant] = None
				else:
					index[variant] = case_id
	return index


def _target_case_id(citation: Citation, index: dict[str, int | None]) -> int | None:
	match = NEUTRAL_CIT_RE.search(citation.normalized_citation or "")
	if match is None:
		return None
	for variant in _citation_variants(match.group(0)):
		target_case_id = index.get(variant)
		if target_case_id is not None:
			return target_case_id
	return None


def main() -> None:
	args = parse_args()
	if args.batch_size < 1:
		raise SystemExit("--batch-size must be at least 1")
	if args.limit is not None and args.limit < 1:
		raise SystemExit("--limit must be at least 1")

	with SessionLocal() as session:
		index = _local_citation_index(session)
		print(f"local_citation_keys={len(index)}")
		last_id = 0
		inspected = candidates = resolved = 0
		while args.limit is None or inspected < args.limit:
			remaining = args.limit - inspected if args.limit is not None else args.batch_size
			batch_limit = min(args.batch_size, remaining)
			rows = list(
				session.scalars(
					select(Citation)
					.where(Citation.id > last_id, Citation.target_case_id.is_(None))
					.order_by(Citation.id)
					.limit(batch_limit)
				)
			)
			if not rows:
				break
			last_id = rows[-1].id
			updates = []
			for citation in rows:
				inspected += 1
				if NEUTRAL_CIT_RE.search(citation.normalized_citation or "") is None:
					continue
				candidates += 1
				target_case_id = _target_case_id(citation, index)
				if target_case_id is not None:
					resolved += 1
					updates.append({"id": citation.id, "target_case_id": target_case_id, "unresolved": False})
			if updates and not args.dry_run:
				session.bulk_update_mappings(Citation, updates)
				session.commit()
			print(f"inspected={inspected} candidates={candidates} resolved={resolved}")

	print(f"finished inspected={inspected} neutral_candidates={candidates} resolved={resolved}")


if __name__ == "__main__":
	main()