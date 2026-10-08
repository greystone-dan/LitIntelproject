"""Pick recent decisions of mixed courts and write their paragraph reports. READ-ONLY: SELECTs only, no database writes, no OpenAI.

Run on the PC. Writes <out>/selection.csv and <out>/reports/case_<id>_deterministic.json. Deterministic for a given --seed.
Quota (fallback fills any shortfall from Federal Court): FC 40, FCA 15, SCC 8, RPD 17, RAD 20. Decisions dated on or after --since, 12 to 90 paragraphs,
at most 30,000 estimated tokens. Ids already used in this project are excluded.
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

COURTS = {"FC": ("FC", "Federal Court"), "FCA": ("FCA", "Federal Court of Appeal"), "SCC": ("SCC", "Supreme Court of Canada"),
	"RPD": ("RPD", "Refugee Protection Division"), "RAD": ("RAD", "Refugee Appeal Division")}
QUOTA = [("FC", 40), ("FCA", 15), ("SCC", 8), ("RPD", 17), ("RAD", 20)]
USED = ("126,1046,1147,1292,1540,16152,17038,19246,19499,23057,23342,23409,23574,25379,26403,27234,33096,38873,46057,48289,51014,52403,64240,7161,7522,"
	"44223,37148,39526,59341,52431,40225,50174,70165,62466,67972")


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__)
	ap.add_argument("--out-dir", type=Path, required=True)
	ap.add_argument("--seed", default="recent100")
	ap.add_argument("--since", default="2021-01-01")
	ap.add_argument("--also-exclude", default=USED)
	ap.add_argument("--quota", default="", help="e.g. FC=35,FCA=15,SCC=15,RPD=15,RAD=20")
	ap.add_argument("--since-rpd", default=None, help="earlier start date for RPD (library thin after 2022)")
	ap.add_argument("--exclude-selection", type=Path, action="append", default=[], help="selection.csv files of earlier picks to exclude")
	ap.add_argument("--exclude-csv", type=Path, default=Path("data/eval/llm_discussion_units_pilot/discussion_unit_core_300.csv"))
	args = ap.parse_args()
	exclude = {int(x) for x in args.also_exclude.split(",") if x}
	if args.exclude_csv.exists():
		exclude |= {int(float(r["case_id"])) for r in csv.DictReader(args.exclude_csv.open(encoding="utf-8-sig"))}
	for sel in args.exclude_selection:
		if sel.exists():
			exclude |= {int(float(r["case_id"])) for r in csv.DictReader(sel.open(encoding="utf-8-sig"))}
	quota = [(c.split("=")[0], int(c.split("=")[1])) for c in args.quota.split(",") if c] or QUOTA
	picked: list[dict] = []
	with SessionLocal() as session:
		print("court values (top 25):", session.execute(select(Case.court, func.count()).group_by(Case.court).order_by(func.count().desc()).limit(25)).all())

		def draw(court: str, n: int) -> None:
			stmt = (select(Case.id, Case.title, Case.citation, Case.date, Case.court, func.count(CaseChunk.id).label("n"), func.sum(CaseChunk.token_estimate).label("tok"))
				.join(CaseChunk, CaseChunk.case_id == Case.id)
				.where(Case.court.in_(COURTS[court]), CaseChunk.chunk_set == "paragraph", Case.date >= (args.since_rpd if court == "RPD" and args.since_rpd else args.since))
				.group_by(Case.id)
				.having(func.count(CaseChunk.id).between(12, 90), func.sum(CaseChunk.token_estimate) <= 30000)
				.order_by(func.md5(func.concat(cast(Case.id, String), args.seed)))
				.limit(n * 4 + 40))
			got = 0
			for r in session.execute(stmt).all():
				if got >= n:
					break
				if r.id in exclude or r.id in {p["case_id"] for p in picked}:
					continue
				picked.append({"case_id": r.id, "title": r.title, "citation": r.citation or "", "decision_date": str(r.date), "court": r.court, "paragraphs": r.n, "approx_tokens": int(r.tok or 0)})
				got += 1
			print(f"{court}: wanted {n}, got {got}")

		for court, n in quota:
			draw(court, n)
		if len(picked) < sum(n for _, n in quota):
			draw("FC", sum(n for _, n in quota) - len(picked))
		args.out_dir.mkdir(parents=True, exist_ok=True)
		(args.out_dir / "reports").mkdir(exist_ok=True)
		for p in picked:
			report = {"status": "dry_run", **inspect_case(session, p["case_id"], "paragraph", 0.35, 2)}
			(args.out_dir / "reports" / f"case_{p['case_id']}_deterministic.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
	with (args.out_dir / "selection.csv").open("w", newline="", encoding="utf-8") as handle:
		w = csv.DictWriter(handle, fieldnames=list(picked[0]))
		w.writeheader()
		w.writerows(picked)
	print(json.dumps({"picked": len(picked), "by_court": {c: sum(1 for p in picked if p["court"] in COURTS[c]) for c in COURTS}}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
