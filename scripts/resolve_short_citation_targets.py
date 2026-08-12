"""Link stored shortened citations to unambiguous resolved authorities in the same decision."""

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

from backend.database import Citation, SessionLocal


PINPOINT_RE = re.compile(
	r"(?:,?\s+)?(?:at\s+)?(?:para(?:s|graph(?:s)?)?\.?|paragraph(?:s)?)\s+\d+(?:\s*[-–]\s*\d+)?(?:\s*(?:,|;|and|or)\s*\d+(?:\s*[-–]\s*\d+)?)*",
	re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--batch-size", type=int, default=1_000)
	parser.add_argument("--limit-cases", type=int, default=None)
	parser.add_argument("--dry-run", action="store_true")
	return parser.parse_args()


def _base_authority(value: str | None) -> str:
	normalized = " ".join((value or "").split()).lower()
	match = PINPOINT_RE.search(normalized)
	if match is not None:
		normalized = normalized[: match.start()].rstrip(" ,;:-")
	return normalized


def _updates_for_case(rows: list[Citation]) -> tuple[list[dict[str, object]], int]:
	anchors: dict[str, set[int]] = defaultdict(set)
	for citation in rows:
		if citation.target_case_id is None:
			continue
		base_authority = _base_authority(citation.normalized_citation)
		if base_authority:
			anchors[base_authority].add(citation.target_case_id)

	updates = []
	ambiguous = 0
	for citation in rows:
		if citation.target_case_id is not None or citation.citation_kind != "case_short":
			continue
		target_ids = anchors.get(_base_authority(citation.normalized_citation), set())
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

	with SessionLocal() as session:
		rows = session.scalars(
			select(Citation)
			.where(Citation.citation_kind.in_(("case", "case_short", "case_name", "neutral")))
			.order_by(Citation.source_case_id, Citation.id)
		).yield_per(5_000)
		current_case_id: int | None = None
		case_rows: list[Citation] = []
		processed_cases = linked = ambiguous = 0
		pending_updates: list[dict[str, object]] = []

		def process_case() -> None:
			nonlocal processed_cases, linked, ambiguous
			if not case_rows:
				return
			updates, case_ambiguous = _updates_for_case(case_rows)
			processed_cases += 1
			linked += len(updates)
			ambiguous += case_ambiguous
			pending_updates.extend(updates)

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

	print(f"processed_cases={processed_cases} linked_short_forms={linked} ambiguous_short_forms={ambiguous}")


if __name__ == "__main__":
	main()