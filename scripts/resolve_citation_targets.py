"""Resolve stored citation rows to locally available target cases.

This intentionally does not extract citations again or call external services.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import _citation_variants, _normalize_alias_lookup, build_local_case_resolution_index
from backend.database import Case, Citation, SessionLocal


FORMAL_CIT_RE = re.compile(
	r"(?<![A-Za-z0-9])(?:\[)?((?:19|20)\d{2})(?:\])?\s+"
	r"(CanLII|[A-Z]{1,8}(?:\.[A-Z]{1,4})?)\s+(\d{1,7})\b",
	re.IGNORECASE,
)
PINPOINT_RE = re.compile(
	r"(?:,?\s+)?(?:at\s+)?(?:para(?:s|graph(?:s)?)?\.?|paragraph(?:s)?)\s+"
	r"\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*",
	re.IGNORECASE,
)
REPORTER_SUFFIX_RE = re.compile(
	r"\s*,?\s*(?:\[(?:19|20)\d{2}\]\s+\d+\s+[A-Z.]{2,}\s+\d+|"
	r"\((?:19|20)\d{2}\)\s*,?\s*\d+\s+[A-Z.]{2,}\s+\d+|"
	r"(?:19|20)\d{2}\s+[A-Z]{2,}\s+\d+)\b.*$",
	re.IGNORECASE,
)


def _citation_title_key(value: str | None) -> str:
	normalized = " ".join((value or "").split()).lower()
	match = PINPOINT_RE.search(normalized)
	if match is not None:
		normalized = normalized[: match.start()].rstrip(" ,;:-")
	normalized = REPORTER_SUFFIX_RE.sub("", normalized).rstrip(" ,;:-")
	return _normalize_alias_lookup(normalized)


def _build_title_resolution_index(session) -> dict[str, set[int]]:
	index: dict[str, set[int]] = defaultdict(set)
	for case_id, title in session.execute(select(Case.id, Case.title)):
		key = _normalize_alias_lookup(title)
		if key:
			index[key].add(case_id)
	return index


def _build_title_year_resolution_index(session) -> dict[tuple[str, int], set[int]]:
	index: dict[tuple[str, int], set[int]] = defaultdict(set)
	for case_id, title, decision_date in session.execute(select(Case.id, Case.title, Case.date)):
		key = _normalize_alias_lookup(title)
		if key and decision_date is not None:
			index[(key, decision_date.year)].add(case_id)
	return index


def _citation_years(value: str) -> set[int]:
	years = set()
	for variant in _citation_variants(value):
		try:
			years.add(int(variant.split(maxsplit=1)[0]))
		except (IndexError, ValueError):
			continue
	return years


def _title_year_target_id(
	citation: Citation,
	title_index: dict[str, set[int]],
	title_year_index: dict[tuple[str, int], set[int]],
) -> int | None:
	value = citation.normalized_citation or citation.citation_text or ""
	title_key = _citation_title_key(value)
	title_matches = set(title_index.get(title_key, set()))
	if len(title_matches) < 2:
		return None
	year_matches: set[int] = set()
	for year in _citation_years(value):
		year_matches.update(title_year_index.get((title_key, year), set()))
	year_matches.difference_update({citation.source_case_id})
	return next(iter(year_matches)) if len(year_matches) == 1 else None


def _title_target_id(
	citation: Citation,
	title_index: dict[str, set[int]],
	title_year_index: dict[tuple[str, int], set[int]],
) -> int | None:
	matches = set(title_index.get(_citation_title_key(citation.normalized_citation or citation.citation_text), set()))
	matches.discard(citation.source_case_id)
	if len(matches) == 1:
		return next(iter(matches))
	return _title_year_target_id(citation, title_index, title_year_index)


def _case_name_target_id(citation: Citation, title_index: dict[str, set[int]]) -> int | None:
	matches = set(title_index.get(_citation_title_key(citation.normalized_citation or citation.citation_text), set()))
	if len(matches) != 1:
		return None
	target_case_id = next(iter(matches))
	return target_case_id if target_case_id != citation.source_case_id else None


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--batch-size", type=int, default=5_000)
	parser.add_argument("--limit", type=int, default=None, help="Maximum unresolved rows to inspect.")
	parser.add_argument("--resume-from-id", type=int, default=0, help="Start after this citation row id.")
	parser.add_argument(
		"--citation-kind",
		choices=("case", "case_name", "case_short", "neutral"),
		default=None,
		help="Inspect only one unresolved citation kind.",
	)
	parser.add_argument("--dry-run", action="store_true")
	return parser.parse_args()


def _target_case_id(citation: Citation, index: dict[str, int | None]) -> int | None:
	for variant in _citation_variants(citation.normalized_citation or citation.citation_text or ""):
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
	if args.resume_from_id < 0:
		raise SystemExit("--resume-from-id must be >= 0")

	with SessionLocal() as session:
		index = build_local_case_resolution_index(session)
		title_index = _build_title_resolution_index(session)
		title_year_index = _build_title_year_resolution_index(session)
		print(f"local_citation_keys={len(index)}")
		print(f"local_title_keys={len(title_index)}")
		last_id = args.resume_from_id
		inspected = candidates = resolved = title_resolved = 0
		while args.limit is None or inspected < args.limit:
			remaining = args.limit - inspected if args.limit is not None else args.batch_size
			batch_limit = min(args.batch_size, remaining)
			query = select(Citation).where(Citation.id > last_id, Citation.target_case_id.is_(None))
			if args.citation_kind is not None:
				query = query.where(Citation.citation_kind == args.citation_kind)
			rows = list(
				session.scalars(
					query.order_by(Citation.id)
					.limit(batch_limit)
				)
			)
			if not rows:
				break
			last_id = rows[-1].id
			updates = []
			for citation in rows:
				inspected += 1
				variants = _citation_variants(citation.normalized_citation or citation.citation_text or "")
				if not variants and citation.citation_kind == "case_name":
					target_case_id = _case_name_target_id(citation, title_index)
					if target_case_id is not None:
						resolved += 1
						title_resolved += 1
						updates.append({"id": citation.id, "target_case_id": target_case_id, "unresolved": False})
					continue
				if not variants:
					continue
				candidates += 1
				target_case_id = _target_case_id(citation, index)
				if target_case_id is None and citation.citation_kind in {"case", "case_name", "case_short", "neutral"}:
					target_case_id = _title_target_id(citation, title_index, title_year_index)
					if target_case_id is not None:
						title_resolved += 1
				if target_case_id is not None:
					resolved += 1
					updates.append({"id": citation.id, "target_case_id": target_case_id, "unresolved": False})
			if updates and not args.dry_run:
				session.bulk_update_mappings(Citation, updates)
				session.commit()
			print(
				f"inspected={inspected} candidates={candidates} resolved={resolved} "
				f"title_resolved={title_resolved} last_id={last_id}"
			)

	print(
		f"finished inspected={inspected} neutral_candidates={candidates} resolved={resolved} "
		f"title_resolved={title_resolved} last_id={last_id}"
	)


if __name__ == "__main__":
	main()