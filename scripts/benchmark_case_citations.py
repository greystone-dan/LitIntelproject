"""Bounded, read-only baseline for case-to-case citation extraction."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import extract_case_citation_matches, is_self_case_citation, is_self_case_name_match
from backend.database import Case, SessionLocal


def is_exact_span_valid(full_text: str, match: Any) -> bool:
	"""Return whether a match's offsets identify exactly its extracted text."""
	start = getattr(match, "offset_start", None)
	end = getattr(match, "offset_end", None)
	citation_text = getattr(match, "citation_text", None)
	return (
		isinstance(start, int)
		and isinstance(end, int)
		and 0 <= start < end <= len(full_text)
		and isinstance(citation_text, str)
		and full_text[start:end] == citation_text
	)


def duplicate_occurrence_count(matches: Iterable[Any]) -> int:
	"""Count repeated occurrences after the first normalized citation mention."""
	counts = Counter(getattr(match, "normalized_citation", "") for match in matches)
	return sum(max(0, count - 1) for value, count in counts.items() if value)


def citation_metrics(case: Any, full_text: str, matches: Iterable[Any]) -> dict[str, Any]:
	rows = list(matches)
	valid_count = sum(is_exact_span_valid(full_text, match) for match in rows)
	pinpoint_count = sum(bool(getattr(match, "pinpoint", None)) for match in rows)
	return {
		"extracted_citations": len(rows),
		"exact_span_valid_count": valid_count,
		"invalid_span_count": len(rows) - valid_count,
		"duplicate_occurrence_count": duplicate_occurrence_count(rows),
		"self_citation_count": sum(
			is_self_case_citation(case, match)
			or is_self_case_name_match(getattr(case, "title", None), match)
			for match in rows
		),
		"resolved_citations": None,
		"unresolved_citations": None,
		"resolution_status": "not_measured",
		"pinpoint_available_count": pinpoint_count,
		"pinpoint_unavailable_count": len(rows) - pinpoint_count,
		"pinpoint_status": "available only when explicit match data exposes pinpoint",
	}


def _empty_metrics() -> dict[str, Any]:
	return {
		"sampled_cases": 0,
		**citation_metrics(
			type("CaseValue", (), {"title": None, "citation": None, "secondary_citation": None})(),
			"",
			[],
		),
	}


def benchmark(courts: list[str], limit: int) -> dict[str, Any]:
	per_court: dict[str, dict[str, Any]] = {}
	with SessionLocal() as db:
		for court in courts:
			cases = list(
				db.scalars(
					select(Case)
					.where(Case.court == court, Case.full_text.is_not(None), Case.full_text != "")
					.order_by(Case.id)
					.limit(limit)
				)
			)
			metrics = _empty_metrics()
			metrics["sampled_cases"] = len(cases)
			for case in cases:
				full_text = case.full_text or ""
				case_metrics = citation_metrics(case, full_text, extract_case_citation_matches(full_text))
				for key, value in case_metrics.items():
					if isinstance(value, int):
						metrics[key] += value
			per_court[court] = metrics

	all_metrics = _empty_metrics()
	all_metrics["sampled_cases"] = sum(item["sampled_cases"] for item in per_court.values())
	for item in per_court.values():
		for key, value in item.items():
			if key != "sampled_cases" and isinstance(value, int):
				all_metrics[key] += value
	return {
		"benchmark": "case_citations_035_m1",
		"timestamp": datetime.now(timezone.utc).isoformat(),
		"courts": courts,
		"limit_per_court": limit,
		"database_writes": False,
		"resolution_status": "not_measured; no resolver invoked",
		"per_court": per_court,
		"totals": all_metrics,
	}


def main() -> int:
	parser = argparse.ArgumentParser(description="Run a bounded read-only case citation baseline.")
	parser.add_argument("--courts", nargs="+", default=["FC", "FCA", "SCCmodern"])
	parser.add_argument("--limit", type=int, default=20)
	parser.add_argument("--report-json", type=Path)
	args = parser.parse_args()
	if args.limit < 1:
		parser.error("--limit must be positive")
	report = benchmark(args.courts, args.limit)
	if args.report_json:
		args.report_json.parent.mkdir(parents=True, exist_ok=True)
		args.report_json.write_text(json.dumps(report, separators=(",", ":")), encoding="utf-8")
	print(json.dumps(report, separators=(",", ":")))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())