"""ONE bundled, capped, unattended run (run on the PC): pick 100 recent decisions, mini paragraph summaries + citation purposes + structure, cited-paragraph export.
Database: SELECTs only (steps 1 and 3). OpenAI: gpt-4.1-mini only (step 2). Nothing is written to the database, the site or main.
Steps (one at a time with --step N, or all):
  1  read-only pick of 100 recent decisions (prepare_recent.py) + paragraph reports
  2  summaries + citations by purpose + idea flag + structure, per decision        step ceiling US$2.00 (dry-run sum must be below it)
  3  read-only export of the pinpointed cited paragraphs (from step 2 outputs + the 51 hand-listed ones)
Total hard cap = ledger total at first start + US$2.50, written once to <out-root>\\bundle2_cap.txt, never raised. Every call is also refused by the ledger if it would pass it.
Stop rule: create <out-root>\\STOP.txt (stops before the next call); any error, cap refusal or dry run above the step ceiling stops the run. No retries with higher caps.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = sys.executable
ALLOWANCE = 2.50
STEP2_CEILING = 2.00


def ledger_total(path: Path) -> float:
	t = 0.0
	if path.exists():
		for line in path.read_text(encoding="utf-8").splitlines():
			try:
				t += float(json.loads(line).get("usd", 0))
			except Exception:
				pass
	return t


def run(cmd: list[str]):
	p = subprocess.run(cmd, capture_output=True, text=True)
	rows = []
	for ln in p.stdout.splitlines():
		try:
			rows.append(json.loads(ln))
		except Exception:
			pass
	return p.returncode, rows, p.stdout + p.stderr


def main() -> int:
	ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	ap.add_argument("--step", required=True, help="1, 2, 3 or all")
	ap.add_argument("--out-root", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	args = ap.parse_args()
	root = args.out_root
	root.mkdir(parents=True, exist_ok=True)
	stop = root / "STOP.txt"
	capfile = root / "bundle2_cap.txt"
	if capfile.exists():
		hard = float(capfile.read_text().split()[-1])
	else:
		start = ledger_total(args.ledger)
		hard = math.ceil((start + ALLOWANCE) * 100) / 100
		capfile.write_text(f"START {start:.4f} HARD_CAP {hard:.2f}\n")
	print(json.dumps({"hard_cap": hard, "ledger_now": round(ledger_total(args.ledger), 4)}), flush=True)
	recent = root / "recent"
	steps = ["1", "2", "3"] if args.step == "all" else [args.step]
	for s in steps:
		if stop.exists():
			print(json.dumps({"stopped": "STOP.txt", "step": s}))
			return 2
		if s == "1":
			code, rows, text = run([PY, str(HERE / "prepare_recent.py"), "--out-dir", str(recent)])
			print(text[-2500:])
			sel = recent / "selection.csv"
			n = len(list(csv.DictReader(sel.open(encoding="utf-8")))) if sel.exists() else 0
			print(json.dumps({"step_done": "1 pick", "exit": code, "picked": n}))
			if code != 0 or n < 90:
				print(json.dumps({"stopped": "pick failed or fewer than 90 decisions", "step": "1"}))
				return 2
		elif s == "2":
			cases = [r["case_id"] for r in csv.DictReader((recent / "selection.csv").open(encoding="utf-8"))]
			now = ledger_total(args.ledger)
			cap = min(hard, math.ceil((now + STEP2_CEILING) * 100) / 100)
			base = [PY, str(HERE / "summarize_paragraphs.py"), "--model", "gpt-4.1-mini", "--run", "bundle2_summaries", "--reports-dir", str(recent / "reports"), "--meta-csv", str(recent / "selection.csv"),
				"--out-dir", str(root / "summaries"), "--ledger", str(args.ledger), "--cap-usd", f"{cap:.2f}", "--stop-file", str(stop)]
			code, rows, text = run(base + ["--cases", ",".join(cases)])
			est = sum(r.get("est_usd_max", 0) for r in rows)
			print(json.dumps({"step": "2 dry run", "cases": len(cases), "dry_run_ceiling_sum": round(est, 4), "step_ceiling": STEP2_CEILING, "exit": code}), flush=True)
			if code != 0 or est > STEP2_CEILING or now + est > hard:
				print(text[-1500:])
				print(json.dumps({"stopped": "dry run failed or above the ceiling", "step": "2"}))
				return 2
			for c in cases:
				if stop.exists():
					print(json.dumps({"stopped": "STOP.txt", "step": "2", "before_case": c}))
					return 2
				code, rows, text = run(base + ["--cases", c, "--send"])
				for r in rows:
					print(json.dumps(r), flush=True)
				if code != 0:
					print(text[-1500:])
					print(json.dumps({"stopped": "error or cap refusal", "step": "2", "case": c, "exit": code}))
					return 2
			print(json.dumps({"step_done": "2 summaries", "ledger": round(ledger_total(args.ledger), 4), "spent_in_step": round(ledger_total(args.ledger) - now, 4)}), flush=True)
		elif s == "3":
			rows_out = []
			for f in sorted((root / "summaries").glob("case_*_summary_*.json")):
				d = json.loads(f.read_text(encoding="utf-8"))
				for i, p in enumerate(d.get("pinpoints", [])):
					rows_out.append([f"{d['case_id']}:{p['citing_para']}:{i}", p["neutral_citation"], p["para_start"], p["para_end"]])
			hand = HERE / "cited_pinpoints_handlists.csv"
			if hand.exists():
				rows_out += [[f"hand:{r['row_id']}", r["neutral_citation"], r["para_start"], r["para_end"]] for r in csv.DictReader(hand.open(encoding="utf-8"))]
			cited = root / "cited_pinpoints.csv"
			with cited.open("w", newline="", encoding="utf-8") as h:
				w = csv.writer(h)
				w.writerow(["row_id", "neutral_citation", "para_start", "para_end"])
				w.writerows(rows_out)
			code, rows, text = run([PY, str(HERE / "export_cited_paragraphs.py"), "--in", str(cited), "--out", str(root / "cited_paragraphs.json")])
			print(text[-800:])
			print(json.dumps({"step_done": "3 export", "requested": len(rows_out), "exit": code}))
			if code != 0:
				return 2
		else:
			raise SystemExit("unknown step")
	print(json.dumps({"finished": args.step, "ledger": round(ledger_total(args.ledger), 4), "hard_cap": hard}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
