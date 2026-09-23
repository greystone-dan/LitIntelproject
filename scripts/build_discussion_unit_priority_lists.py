"""Build the bounded Discussion Unit priority lists without database writes."""

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

from backend.database import Case, CitationMetrics, SessionLocal

DEFAULT_CORE = Path("data/eval/core_immigration_cases.csv")
DEFAULT_OUT_DIR = Path("data/eval/llm_discussion_units_pilot")
DEFAULT_CUTOFF = date(2005, 1, 1)
COURT_QUOTAS = {"SCC": 500, "FCA": 750, "FC": 1250}


@dataclass(frozen=True)
class CaseRecord:
	case_id: int
	title: str
	citation: str | None
	decision_date: date
	court: str
	inbound_count: int
	inbound_count_source: str


def normalize_court(value: str | None) -> str:
	upper = (value or "").strip().upper()
	if "SCC" in upper or "SUPREME COURT" in upper:
		return "SCC"
	if "FCA" in upper or "FEDERAL COURT OF APPEAL" in upper:
		return "FCA"
	if upper in {"FC", "FCT", "FEDERAL", "FEDERAL COURT"} or "FEDERAL COURT" in upper:
		return "FC"
	return upper


def parse_case_id(value: str) -> int:
	case_id = int(float(value))
	if float(value) != case_id:
		raise ValueError(f"Non-integer case ID: {value}")
	return case_id


def load_core(path: Path) -> list[CaseRecord]:
	with path.open(newline="", encoding="utf-8-sig") as handle:
		rows = list(csv.DictReader(handle))
	if len(rows) != 300:
		raise ValueError(f"Expected 300 core rows, found {len(rows)} in {path}")
	return [
		CaseRecord(
			case_id=parse_case_id(row["local_case_id"]),
			title=row.get("title", ""),
			citation=row.get("neutral_citation") or None,
			decision_date=date.fromisoformat(row["decision_date"][:10]),
			court=normalize_court(row.get("court")),
			inbound_count=int(float(row.get("local_incoming") or row.get("a2aj_incoming") or 0)),
			inbound_count_source="core_csv.local_incoming",
		)
		for row in rows
	]


def select_layers(
	core: list[CaseRecord],
	candidates: list[CaseRecord],
	*,
	cutoff: date = DEFAULT_CUTOFF,
	quotas: dict[str, int] = COURT_QUOTAS,
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
	core_ids = {record.case_id for record in core}
	if len(core_ids) != 300:
		raise ValueError("Core list contains duplicate case IDs")
	core_counts = {court: sum(record.court == court for record in core) for court in quotas}
	if any(core_counts[court] > quota for court, quota in quotas.items()):
		raise ValueError(f"Core list exceeds court quota: {core_counts}")

	def output(record: CaseRecord, layer: str, reason: str, rank: int | None) -> dict[str, object]:
		return {
			**asdict(record),
			"decision_date": record.decision_date.isoformat(),
			"layer": layer,
			"inclusion_reason": reason,
			"rank": rank,
		}

	core_rows = [output(record, "core_300", "core_case", None) for record in sorted(core, key=lambda item: item.case_id)]
	selected_ids = set(core_ids)
	additional_rows: list[dict[str, object]] = []
	for court, quota in quotas.items():
		eligible = sorted(
			(
				record
				for record in candidates
				if record.case_id not in selected_ids
				and record.court == court
				and record.decision_date >= cutoff
			),
			key=lambda item: (-item.inbound_count, item.decision_date, item.case_id),
		)
		needed = quota - core_counts[court]
		if len(eligible) < needed:
			raise ValueError(f"Not enough eligible {court} candidates: need {needed}, found {len(eligible)}")
		for rank, record in enumerate(eligible[:needed], start=1):
			selected_ids.add(record.case_id)
			additional_rows.append(output(record, "priority_2500", "court_quota_inbound_rank", rank))

	return core_rows, additional_rows


def load_candidates(core_ids: set[int]) -> list[CaseRecord]:
	with SessionLocal() as session:
		rows = session.execute(
			select(Case, CitationMetrics.in_degree)
			.outerjoin(CitationMetrics, CitationMetrics.case_id == Case.id)
			.where(Case.id.not_in(core_ids))
		).all()
	return [
		CaseRecord(
			case_id=case.id,
			title=case.title,
			citation=case.citation,
			decision_date=case.date,
			court=normalize_court(case.court),
			inbound_count=int(metric_count if metric_count is not None else case.citing_cases_count or 0),
			inbound_count_source="citation_metrics.in_degree" if metric_count is not None else "cases.citing_cases_count",
		)
		for case, metric_count in rows
	]


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
	path.parent.mkdir(parents=True, exist_ok=True)
	with path.open("w", newline="", encoding="utf-8") as handle:
		writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
		writer.writeheader()
		writer.writerows(rows)


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--core-csv", type=Path, default=DEFAULT_CORE)
	parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR)
	parser.add_argument("--cutoff", type=date.fromisoformat, default=DEFAULT_CUTOFF)
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	core = load_core(args.core_csv)
	core_rows, additional_rows = select_layers(core, load_candidates({record.case_id for record in core}), cutoff=args.cutoff)
	expanded_rows = core_rows + additional_rows
	if len(expanded_rows) != 2500:
		raise ValueError(f"Expanded list must contain 2,500 rows, found {len(expanded_rows)}")
	write_csv(args.out_dir / "discussion_unit_core_300.csv", core_rows)
	write_csv(args.out_dir / "discussion_unit_priority_2500.csv", expanded_rows)
	summary = {
		"core_count": len(core_rows),
		"expanded_count": len(expanded_rows),
		"court_counts": {court: sum(row["court"] == court for row in expanded_rows) for court in COURT_QUOTAS},
		"cutoff": args.cutoff.isoformat(),
		"ranking": "descending inbound citation count; ascending decision date; ascending case ID",
	}
	(args.out_dir / "discussion_unit_priority_2500_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
	print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
	main()