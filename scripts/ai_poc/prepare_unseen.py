"""Pick unseen non-Federal-Court decisions and write their paragraph reports. READ-ONLY: SELECTs only, no database writes.

Needs the project database (run on the PC). Writes <out>/selection.csv and <out>/reports/case_<id>_deterministic.json
(the same report format the earlier runs used). Deterministic: the same --seed gives the same picks.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import String, cast, func, select  # noqa: E402

from backend.database import Case, CaseChunk, SessionLocal  # noqa: E402
from scripts.inspect_discussion_units import inspect_case  # noqa: E402

COURTS = {
	"FCA": ("FCA", "Federal Court of Appeal"),
	"SCC": ("SCC", "Supreme Court of Canada"),
	"RPD": ("RPD", "Refugee Protection Division"),
	"RAD": ("RAD", "Refugee Appeal Division"),
}
# (court, min paragraphs, max paragraphs): varied lengths, none too long to send.
SPEC = [("FCA", 20, 45), ("FCA", 60, 120), ("SCC", 30, 60), ("SCC", 80, 130), ("RPD", 15, 40), ("RAD", 20, 50)]
SPEC_MORE = [("FCA", 20, 45), ("FCA", 20, 45), ("FCA", 60, 120), ("SCC", 30, 60), ("SCC", 80, 130), ("RPD", 15, 40), ("RPD", 15, 40), ("RAD", 20, 50), ("RAD", 20, 50), ("RAD", 20, 50)]
MAX_TOKENS = 45000
DEFAULT_EXCLUDE = Path("data/eval/llm_discussion_units_pilot/discussion_unit_core_300.csv")


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--out-dir", type=Path, required=True)
	parser.add_argument("--seed", default="unseen25")
	parser.add_argument("--exclude-csv", type=Path, default=DEFAULT_EXCLUDE, help="case_id column; these are never picked")
	parser.add_argument("--also-exclude", default="126,1046,1147,1292,1540")
	parser.add_argument("--more", action="store_true", help="pick the 10-case expansion set (SPEC_MORE) instead of the first 6")
	args = parser.parse_args()
	exclude = {int(float(r["case_id"])) for r in csv.DictReader(args.exclude_csv.open(encoding="utf-8-sig"))}
	exclude |= {int(x) for x in args.also_exclude.split(",") if x}
	picked: list[dict] = []
	with SessionLocal() as session:
		courts_seen = session.execute(select(Case.court, func.count()).group_by(Case.court).order_by(func.count().desc()).limit(25)).all()
		print("court values in the database (top 25):", [(c, n) for c, n in courts_seen])
		for court, lo, hi in (SPEC_MORE if args.more else SPEC):
			names = COURTS[court]
			stmt = (
				select(Case.id, Case.title, Case.citation, Case.date, Case.court,
					func.count(CaseChunk.id).label("n"), func.sum(CaseChunk.token_estimate).label("tok"))
				.join(CaseChunk, CaseChunk.case_id == Case.id)
				.where(Case.court.in_(names), CaseChunk.chunk_set == "paragraph")
				.group_by(Case.id)
				.having(func.count(CaseChunk.id).between(lo, hi), func.sum(CaseChunk.token_estimate) <= MAX_TOKENS)
				.order_by(func.md5(func.concat(cast(Case.id, String), args.seed)))
				.limit(40)
			)
			rows = [r for r in session.execute(stmt).all() if r.id not in exclude and r.id not in {p["case_id"] for p in picked}]
			if not rows:
				print(f"NO ELIGIBLE CASE for {court} {lo}-{hi} paragraphs; report the court values above and stop.")
				return 2
			r = rows[0]
			picked.append({"case_id": r.id, "title": r.title, "citation": r.citation or "", "decision_date": str(r.date), "court": r.court,
				"paragraphs": r.n, "approx_tokens": int(r.tok or 0)})
		args.out_dir.mkdir(parents=True, exist_ok=True)
		(args.out_dir / "reports").mkdir(exist_ok=True)
		for p in picked:
			report = {"status": "dry_run", **inspect_case(session, p["case_id"], "paragraph", 0.35, 2)}
			(args.out_dir / "reports" / f"case_{p['case_id']}_deterministic.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
	with (args.out_dir / "selection.csv").open("w", newline="", encoding="utf-8") as handle:
		writer = csv.DictWriter(handle, fieldnames=list(picked[0]))
		writer.writeheader()
		writer.writerows(picked)
	print(json.dumps(picked, indent=1))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
