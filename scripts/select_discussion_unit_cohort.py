"""Select a bounded, report-only cohort for Discussion Unit labeling."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

from sqlalchemy import func, select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:

	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, Citation, CitationMetrics, SessionLocal

DEFAULT_PRIORITY_CSV = Path("data/eval/core_immigration_cases.csv")
DEFAULT_OUTPUT = Path("data/eval/llm_discussion_units_pilot/selected_cohort.json")
DEFAULT_CUTOFF = date(2005, 1, 1)
DEFAULT_RANKED_LIMIT = 2500
DEFAULT_CASE_COST = 0.0065556


@dataclass(frozen=True)
class Candidate:
	case_id: int
	title: str
	citation: str | None
	decision_date: date
	inbound_count: int
	inbound_count_source: str


def load_priority_ids(path: Path) -> set[int]:
	def parse_case_id(value: str) -> int:
		case_id = int(float(value))
		if float(value) != case_id:
			raise ValueError(f"Priority CSV contains a non-integer case ID: {value}")
		return case_id

	with path.open(newline="", encoding="utf-8-sig") as handle:
		rows = csv.DictReader(handle)
		field = next(
			(
				name
				for name in ("local_case_id", "case_id", "id")
				if name in (rows.fieldnames or [])
			),
			None,
		)
		if field is None:
			raise ValueError(f"Priority CSV needs local_case_id, case_id, or id: {path}")
		return {parse_case_id(row[field]) for row in rows if row.get(field)}


def select_cohort(
	candidates: list[Candidate],
	priority_ids: set[int],
	*,
	cutoff: date = DEFAULT_CUTOFF,
	ranked_limit: int = DEFAULT_RANKED_LIMIT,
) -> list[dict[str, object]]:
	by_id = {candidate.case_id: candidate for candidate in candidates}
	selected: list[dict[str, object]] = []

	for case_id in sorted(priority_ids):
		candidate = by_id.get(case_id)
		if candidate is None:
			continue
		selected.append(
			{
				**asdict(candidate),
				"decision_date": candidate.decision_date.isoformat(),
				"inclusion_reason": "explicit_priority",
				"rank": None,
			}
		)

	ranked = sorted(
		(candidate for candidate in candidates if candidate.case_id not in priority_ids and candidate.decision_date >= cutoff),
		key=lambda candidate: (-candidate.inbound_count, candidate.decision_date, candidate.case_id),
	)[:ranked_limit]
	for rank, candidate in enumerate(ranked, start=1):
		selected.append(
			{
				**asdict(candidate),
				"decision_date": candidate.decision_date.isoformat(),
				"inclusion_reason": "inbound_citation_rank",
				"rank": rank,
			}
		)
	return selected


def load_candidates() -> list[Candidate]:
	with SessionLocal() as session:
		rows = session.execute(
			select(Case, CitationMetrics.in_degree).outerjoin(
				CitationMetrics, CitationMetrics.case_id == Case.id
			)
		).all()
		missing_ids = [case.id for case, metric_count in rows if metric_count is None]
		fallback_counts = dict(
			session.execute(
				select(Citation.target_case_id, func.count(Citation.id))
				.where(Citation.target_case_id.in_(missing_ids))
				.group_by(Citation.target_case_id)
			).all()
		) if missing_ids else {}

	return [
		Candidate(
			case_id=case.id,
			title=case.title,
			citation=case.citation,
			decision_date=case.date,
			inbound_count=int(metric_count if metric_count is not None else fallback_counts.get(case.id, 0)),
			inbound_count_source="citation_metrics.in_degree" if metric_count is not None else "citations.target_case_id",
		)
		for case, metric_count in rows
	]


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--priority-csv", type=Path, default=DEFAULT_PRIORITY_CSV)
	parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
	parser.add_argument("--ranked-limit", type=int, default=DEFAULT_RANKED_LIMIT)
	parser.add_argument("--cutoff", type=date.fromisoformat, default=DEFAULT_CUTOFF)
	parser.add_argument("--case-cost", type=float, default=DEFAULT_CASE_COST)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	priority_ids = load_priority_ids(args.priority_csv)
	cohort = select_cohort(load_candidates(), priority_ids, cutoff=args.cutoff, ranked_limit=args.ranked_limit)
	priority_count = sum(item["inclusion_reason"] == "explicit_priority" for item in cohort)
	ranked_count = len(cohort) - priority_count
	result = {
		"selection_rule": {
			"priority_csv": str(args.priority_csv),
			"cutoff": args.cutoff.isoformat(),
			"ranked_limit": args.ranked_limit,
			"ranking": "descending inbound citation count; ascending decision date; ascending case ID",
		},
		"summary": {
			"selected_count": len(cohort),
			"explicit_priority_count": priority_count,
			"ranked_addition_count": ranked_count,
			"estimated_discussion_unit_cost_usd": round(len(cohort) * args.case_cost, 6),
		},
		"cases": cohort,
	}
	args.output.parent.mkdir(parents=True, exist_ok=True)
	args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
	print(json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
	main()