"""Read-only report: non-immigration decisions in FC / FCA / SCC and how much they skew judge win rates (T7, T9).

The existing marker is `case_type_labels.status = 'not_immigration'` (rule-based, written by
scripts/classify_case_types.py, one row per decision and taxonomy version). Nothing in the judge statistics reads
it yet, so this script never writes: it shows (1) how many decisions of each court are labelled, (2) the
not_immigration candidates per court, and (3) per judge, the government win rate with and without them.

  python scripts/fix_non_immigration_report.py                       # all three courts, top 25 judges
  python scripts/fix_non_immigration_report.py --courts FCA --top 50
  python scripts/fix_non_immigration_report.py --export data/db_fix_backups/non_immigration_candidates.csv

If the coverage lines show unlabelled decisions, label them first (this is the reversible writer that already
exists; it is a dry run unless --apply, and --revert removes the rows):
  python scripts/classify_case_types.py --court FCA --apply
Win rate = government outcome 'won' / ('won' + 'lost') from reader_extracted, the same rule the judge pages use.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import bindparam, text

from backend.case_types import STATUS_NOT_IMMIGRATION, TAXONOMY_VERSION
from backend.database import SessionLocal

GOV_OUTCOME = "c.metadata_json->'reader_extracted'->>'government outcome'"

COVERAGE_SQL = text(
	"SELECT c.court AS court, COUNT(*) AS total, COUNT(l.id) AS labelled, "
	"COUNT(*) FILTER (WHERE l.status = :status) AS not_immigration, "
	"COUNT(*) FILTER (WHERE l.status = 'unclear') AS unclear "
	"FROM cases c LEFT JOIN case_type_labels l ON l.case_id = c.id AND l.taxonomy_version = :version "
	"WHERE c.court IN :courts GROUP BY c.court ORDER BY c.court"
).bindparams(bindparam("courts", expanding=True))

JUDGE_SQL = text(
	"SELECT jp.slug AS slug, jp.display_name AS name, jp.primary_court AS court, COUNT(*) AS total, "
	"COUNT(*) FILTER (WHERE l.status = :status) AS non_immigration, "
	f"COUNT(*) FILTER (WHERE {GOV_OUTCOME} = 'won') AS won_all, "
	f"COUNT(*) FILTER (WHERE {GOV_OUTCOME} = 'lost') AS lost_all, "
	f"COUNT(*) FILTER (WHERE {GOV_OUTCOME} = 'won' AND l.status IS DISTINCT FROM :status) AS won_imm, "
	f"COUNT(*) FILTER (WHERE {GOV_OUTCOME} = 'lost' AND l.status IS DISTINCT FROM :status) AS lost_imm "
	"FROM case_judge_profiles cjp JOIN judge_profiles jp ON jp.id = cjp.judge_profile_id "
	"JOIN cases c ON c.id = cjp.case_id "
	"LEFT JOIN case_type_labels l ON l.case_id = c.id AND l.taxonomy_version = :version "
	"WHERE c.court IN :courts GROUP BY jp.id, jp.slug, jp.display_name, jp.primary_court "
	"HAVING COUNT(*) FILTER (WHERE l.status = :status) > 0 "
	"ORDER BY COUNT(*) FILTER (WHERE l.status = :status) DESC, jp.display_name LIMIT :top"
).bindparams(bindparam("courts", expanding=True))

CANDIDATES_SQL = text(
	"SELECT c.id AS id, c.court AS court, c.citation AS citation, c.title AS title, c.date AS date, "
	"l.confidence AS confidence FROM cases c JOIN case_type_labels l ON l.case_id = c.id "
	"WHERE l.taxonomy_version = :version AND l.status = :status AND c.court IN :courts "
	"ORDER BY c.court, c.date DESC, c.id LIMIT :limit"
).bindparams(bindparam("courts", expanding=True))


def win_rate(won: int, lost: int) -> float | None:
	"""Government win rate in percent over classified outcomes only, or None when there are none."""
	return round(100.0 * won / (won + lost), 1) if won + lost else None


def judge_impact(row: dict[str, Any]) -> dict[str, Any]:
	all_rate = win_rate(int(row["won_all"]), int(row["lost_all"]))
	imm_rate = win_rate(int(row["won_imm"]), int(row["lost_imm"]))
	delta = None if all_rate is None or imm_rate is None else round(all_rate - imm_rate, 1)
	return {
		"slug": row["slug"], "name": row["name"], "court": row["court"], "total": int(row["total"]),
		"non_immigration": int(row["non_immigration"]), "rate_all": all_rate, "rate_immigration_only": imm_rate,
		"delta": delta,
	}


def _fmt(value: float | None) -> str:
	return "n/a" if value is None else f"{value:.1f}%"


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--courts", default="FC,FCA,SCC", help="Comma-separated court column values (default FC,FCA,SCC).")
	parser.add_argument("--top", type=int, default=25, help="Judges to list, most non-immigration decisions first.")
	parser.add_argument("--export", type=Path, help="Also write the not_immigration candidates to this CSV.")
	parser.add_argument("--export-max", type=int, default=5000)
	args = parser.parse_args(argv)
	courts = [court.strip() for court in args.courts.split(",") if court.strip()]
	if not courts:
		parser.error("--courts needs at least one court")
	params = {"courts": courts, "version": TAXONOMY_VERSION, "status": STATUS_NOT_IMMIGRATION}

	with SessionLocal() as db:
		print(f"taxonomy_version={TAXONOMY_VERSION} (read-only report, nothing is written)")
		coverage = [dict(r) for r in db.execute(COVERAGE_SQL, params).mappings().all()]
		print("court   total  labelled  not_immigration  unclear")
		for row in coverage:
			print(f"{row['court']:<6} {row['total']:6d} {row['labelled']:9d} {row['not_immigration']:16d} {row['unclear']:8d}")
		unlabelled = sum(int(r["total"]) - int(r["labelled"]) for r in coverage)
		if unlabelled:
			print(f"{unlabelled} decisions have no label yet; label them first with scripts/classify_case_types.py --court <court> --apply")
		judges = [judge_impact(dict(r)) for r in db.execute(JUDGE_SQL, {**params, "top": args.top}).mappings().all()]
		print("\njudge (court): non-immigration / all decisions, government win rate all -> immigration only")
		for j in judges:
			print(f"  {j['name']} ({j['court']}): {j['non_immigration']}/{j['total']}  "
			      f"{_fmt(j['rate_all'])} -> {_fmt(j['rate_immigration_only'])}  delta {_fmt(j['delta'])}  [{j['slug']}]")
		if args.export:
			rows = [dict(r) for r in db.execute(CANDIDATES_SQL, {**params, "limit": args.export_max}).mappings().all()]
			args.export.parent.mkdir(parents=True, exist_ok=True)
			with open(args.export, "w", newline="", encoding="utf-8") as handle:
				writer = csv.DictWriter(handle, fieldnames=["id", "court", "citation", "title", "date", "confidence"])
				writer.writeheader()
				writer.writerows(rows)
			print(f"\nwrote {len(rows)} candidates to {args.export}")
		print("\nTo keep these out of judge win rates the judge queries must skip case_type_labels.status = 'not_immigration' "
		      "(backend/analytics_service.py); no data change is needed for that.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
