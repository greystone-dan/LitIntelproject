"""Link stored case names and shortened citations to unambiguous authorities."""

from __future__ import annotations

import argparse
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import _normalize_alias_lookup
from backend.database import Case, Citation, SessionLocal


PINPOINT_RE = re.compile(
	r"(?:,?\s+)?(?:at\s+)?(?:para(?:s|graph(?:s)?)?\.?|paragraph(?:s)?)\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*",
	re.IGNORECASE,
)
REPORTER_SUFFIX_RE = re.compile(
	r"\s*,?\s*(?:\[(?:19|20)\d{2}\]\s+\d+\s+[A-Z.]{2,}\s+\d+|\((?:19|20)\d{2}\)\s*,?\s*\d+\s+[A-Z.]{2,}\s+\d+|(?:19|20)\d{2}\s+[A-Z]{2,}\s+\d+)\b.*$",
	re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--batch-size", type=int, default=1_000)
	parser.add_argument("--limit-cases", type=int, default=None)
	parser.add_argument("--dry-run", action="store_true")
	parser.add_argument("--progress-every", type=int, default=500)
	return parser.parse_args()


def _base_authority(value: str | None) -> str:
	normalized = " ".join((value or "").split()).lower()
	match = PINPOINT_RE.search(normalized)
	if match is not None:
		normalized = normalized[: match.start()].rstrip(" ,;:-")
	normalized = REPORTER_SUFFIX_RE.sub("", normalized).rstrip(" ,;:-")
	return normalized


def _alias_terms(value: str | None) -> list[str]:
	base = _base_authority(value)
	if not base:
		return []
	parts = re.split(r"\s+(?:v\.?|vs\.?|c\.?|versus)\s+", base, maxsplit=1, flags=re.IGNORECASE)
	choices = [base]
	if len(parts) == 2:
		choices.extend(parts)
	terms = []
	for choice in choices:
		term = _normalize_alias_lookup(choice)
		if term and len(term) >= 3 and term not in terms:
			terms.append(term)
	return sorted(terms, key=len, reverse=True)


def _case_alias_index(session) -> tuple[dict[str, set[int]], dict[str, set[int]], dict[int, tuple[str, ...]]]:
	exact_index: dict[str, set[int]] = defaultdict(set)
	token_index: dict[str, set[int]] = defaultdict(set)
	values_by_case: dict[int, tuple[str, ...]] = {}
	for case_id, title, citation, secondary_citation in session.execute(
		select(Case.id, Case.title, Case.citation, Case.secondary_citation)
	):
		values = tuple(
			_normalize_alias_lookup(value)
			for value in (title, citation, secondary_citation)
			if value
		)
		if values:
			values_by_case[case_id] = values
			for value in values:
				exact_index[value].add(case_id)
				for token in value.split():
					token_index[token].add(case_id)
	return exact_index, token_index, values_by_case


def _direct_case_target(
	citation: Citation,
	case_index: tuple[dict[str, set[int]], dict[str, set[int]], dict[int, tuple[str, ...]]],
) -> tuple[int | None, bool]:
	exact_index, token_index, values_by_case = case_index
	terms = _alias_terms(citation.normalized_citation or citation.citation_text)
	for term in terms:
		matches = set(exact_index.get(term, set()))
		if not matches:
			tokens = term.split()
			if tokens:
				matches = set(token_index.get(tokens[0], set()))
				for token in tokens[1:]:
					matches.intersection_update(token_index.get(token, set()))
				matches = {
					case_id
					for case_id in matches
					if any(term in value for value in values_by_case[case_id])
				}
		if len(matches) == 1:
			return next(iter(matches)), False
		if len(matches) > 1:
			return None, True
	return None, False


def _updates_for_case(
	rows: list[Citation], case_index: tuple[dict[str, set[int]], dict[str, set[int]], dict[int, tuple[str, ...]]]
) -> tuple[list[dict[str, object]], int]:
	anchors: dict[str, set[int]] = defaultdict(set)
	fuller_targets: dict[str, set[int]] = defaultdict(set)
	for citation in rows:
		if citation.target_case_id is None or citation.target_case_id == citation.source_case_id:
			continue
		fuller_base = _base_authority(citation.normalized_citation)
		if fuller_base:
			fuller_targets[fuller_base].add(citation.target_case_id)
		anchor_values = [citation.normalized_citation]
		anchor_values.extend(case_index[2].get(citation.target_case_id, ()))
		for value in anchor_values:
			for term in _alias_terms(value):
				anchors[term].add(citation.target_case_id)

	updates = []
	ambiguous = 0
	for citation in rows:
		if citation.target_case_id is not None or citation.citation_kind not in {"case_name", "case_short"}:
			continue
		target_id, direct_ambiguous = _direct_case_target(citation, case_index)
		if target_id is not None and target_id != citation.source_case_id:
			updates.append({"id": citation.id, "target_case_id": target_id, "unresolved": False})
			continue
		if direct_ambiguous:
			ambiguous += 1
			continue
		exact_targets = set(fuller_targets.get(_base_authority(citation.normalized_citation), set()))
		exact_targets.discard(citation.source_case_id)
		if len(exact_targets) == 1:
			updates.append({"id": citation.id, "target_case_id": next(iter(exact_targets)), "unresolved": False})
			continue
		if len(exact_targets) > 1:
			ambiguous += 1
			continue
		target_ids: set[int] = set()
		for term in _alias_terms(citation.normalized_citation or citation.citation_text):
			target_ids.update(anchors.get(term, set()))
		target_ids.discard(citation.source_case_id)
		if len(target_ids) == 1:
			updates.append({"id": citation.id, "target_case_id": next(iter(target_ids)), "unresolved": False})
		elif len(target_ids) > 1:
			ambiguous += 1
	return updates, ambiguous


def main() -> None:
	args = parse_args()
	if args.batch_size < 1:
		raise SystemExit("--batch-size must be at least 1")
	if args.limit_cases is not None and args.limit_cases < 1:
		raise SystemExit("--limit-cases must be at least 1")
	if args.progress_every < 1:
		raise SystemExit("--progress-every must be at least 1")

	with SessionLocal() as session:
		case_index = _case_alias_index(session)
		print(f"case_alias_records={len(case_index[2])}", flush=True)
		rows = session.scalars(
			select(Citation)
			.where(Citation.citation_kind.in_(("case", "case_short", "case_name", "neutral")))
			.order_by(Citation.source_case_id, Citation.id)
		).yield_per(5_000)
		current_case_id: int | None = None
		case_rows: list[Citation] = []
		processed_cases = linked = ambiguous = 0
		started_at = time.monotonic()
		pending_updates: list[dict[str, object]] = []

		def process_case() -> None:
			nonlocal processed_cases, linked, ambiguous
			if not case_rows:
				return
			updates, case_ambiguous = _updates_for_case(case_rows, case_index)
			processed_cases += 1
			linked += len(updates)
			ambiguous += case_ambiguous
			pending_updates.extend(updates)
			if processed_cases % args.progress_every == 0:
				elapsed = max(time.monotonic() - started_at, 0.001)
				print(
					f"progress cases={processed_cases} candidate_links={linked} "
					f"ambiguous={ambiguous} elapsed_seconds={elapsed:.1f}",
					flush=True,
				)

		for citation in rows:
			if current_case_id is None:
				current_case_id = citation.source_case_id
			if citation.source_case_id != current_case_id:
				process_case()
				if len(pending_updates) >= args.batch_size and not args.dry_run:
					session.bulk_update_mappings(Citation, pending_updates)
					session.commit()
					pending_updates.clear()
				if args.limit_cases is not None and processed_cases >= args.limit_cases:
					break
				current_case_id = citation.source_case_id
				case_rows = []
			case_rows.append(citation)
		else:
			process_case()

		if pending_updates and not args.dry_run:
			session.bulk_update_mappings(Citation, pending_updates)
			session.commit()

	print(f"processed_cases={processed_cases} candidate_links={linked} ambiguous={ambiguous}", flush=True)


if __name__ == "__main__":
	main()