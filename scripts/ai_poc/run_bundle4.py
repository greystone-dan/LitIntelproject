"""ONE bundled, capped, unattended run (run on the PC): paragraph layer batch 3, refined prompt v3 vs base. gpt-4.1-mini only. NO database writes.
Steps (one at a time with --step N, or all):
  1  read-only pick of 100 NEW recent decisions (excludes batches 1 and 2) + paragraph reports; SCC 8 (relaxed length), FCA 15, RPD 20 (from 2018), RAD 20, FC 37
  2  variant 'v3' (sharper speaker and ideas rules + role tag) on all 100; variant 'base' on a court-balanced 24 of them, and 'g3' (one summary per 3 paragraphs) on a court-balanced 12.   step ceiling US$1.90 (dry-run sum must be below it)
Total hard cap = ledger total at first start + US$2.00, written once to <out-root>\\bundle4_cap.txt, never raised. Every call is also refused by the ledger if it would pass it.
Stop rule: create <out-root>\\STOP.txt (stops before the next call); any error, cap refusal or dry run above the ceiling stops the run.
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
ALLOWANCE = 2.00
STEP2_CEILING = 1.90
QUOTA = "SCC=8,FCA=15,RPD=20,RAD=20,FC=37"


def balanced(rows, n):
	"""every k-th decision after sorting by court, so the subset spans all courts"""
	rows = sorted(rows, key=lambda r: (r["court"], r["case_id"]))
	step = len(rows) / n
	return [rows[int(i * step)]["case_id"] for i in range(n)]


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
	ap.add_argument("--step", required=True, help="1, 2 or all")
	ap.add_argument("--out-root", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--prior-selection", type=Path, action="append", required=True, help="selection.csv of earlier batches (excluded from the new pick)")
	args = ap.parse_args()
	root = args.out_root
	root.mkdir(parents=True, exist_ok=True)
	stop = root / "STOP.txt"
	capfile = root / "bundle4_cap.txt"
	if capfile.exists():
		hard = float(capfile.read_text().split()[-1])
	else:
		start = ledger_total(args.ledger)
		hard = math.ceil((start + ALLOWANCE) * 100) / 100
		capfile.write_text(f"START {start:.4f} HARD_CAP {hard:.2f}\n")
	print(json.dumps({"hard_cap": hard, "ledger_now": round(ledger_total(args.ledger), 4)}), flush=True)
	recent = root / "recent"
	steps = ["1", "2"] if args.step == "all" else [args.step]
	for s in steps:
		if stop.exists():
			print(json.dumps({"stopped": "STOP.txt", "step": s}))
			return 2
		if s == "1":
			code, rows, text = run([PY, str(HERE / "prepare_recent.py"), "--out-dir", str(recent), "--seed", "batch3", "--quota", QUOTA, "--since-rpd", "2018-01-01", "--relax-scc"] + sum([["--exclude-selection", str(p)] for p in args.prior_selection], []))
			print(text[-2500:])
			sel = recent / "selection.csv"
			n = len(list(csv.DictReader(sel.open(encoding="utf-8")))) if sel.exists() else 0
			print(json.dumps({"step_done": "1 pick", "exit": code, "picked": n}))
			if code != 0 or n < 90:
				print(json.dumps({"stopped": "pick failed or fewer than 90 decisions", "step": "1"}))
				return 2
		elif s == "2":
			sel = list(csv.DictReader((recent / "selection.csv").open(encoding="utf-8")))
			new = [r["case_id"] for r in sel]
			jobs = [("v3", new), ("base", balanced(sel, 24)), ("g3", balanced(sel, 12))]
			now = ledger_total(args.ledger)
			cap = min(hard, math.ceil((now + STEP2_CEILING) * 100) / 100)

			def cmd(variant, cases, send):
				c = [PY, str(HERE / "summarize_v2.py"), "--model", "gpt-4.1-mini", "--run", "bundle4_" + variant, "--reports-dir", str(recent / "reports"),
					"--meta-csv", str(recent / "selection.csv"), "--variant", variant,
					"--out-dir", str(root / "paras" / variant), "--ledger", str(args.ledger), "--cap-usd", f"{cap:.2f}", "--stop-file", str(stop), "--cases", ",".join(cases)]
				return c + (["--send"] if send else [])

			est = 0.0
			for v, cs in jobs:
				code, rows, text = run(cmd(v, cs, False))
				e = sum(r.get("est_usd_max", 0) for r in rows)
				est += e
				print(json.dumps({"step": "2 dry run", "variant": v, "cases": len(cs), "ceiling": round(e, 4), "exit": code}), flush=True)
				if code != 0:
					print(text[-1500:])
					return 2
			print(json.dumps({"dry_run_ceiling_sum": round(est, 4), "step_ceiling": STEP2_CEILING}), flush=True)
			if est > STEP2_CEILING or now + est > hard:
				print(json.dumps({"stopped": "dry run above the ceiling", "step": "2"}))
				return 2
			for v, cs in jobs:
				for c in cs:
					if stop.exists():
						print(json.dumps({"stopped": "STOP.txt", "step": "2", "variant": v, "before_case": c}))
						return 2
					code, rows, text = run(cmd(v, [c], True))
					for r in rows:
						print(json.dumps(r), flush=True)
					if code != 0:
						print(text[-1500:])
						print(json.dumps({"stopped": "error or cap refusal", "variant": v, "case": c, "exit": code}))
						return 2
			print(json.dumps({"step_done": "2 paragraph layer A/B", "ledger": round(ledger_total(args.ledger), 4), "spent_in_step": round(ledger_total(args.ledger) - now, 4)}), flush=True)
		else:
			raise SystemExit("unknown step")
	print(json.dumps({"finished": args.step, "ledger": round(ledger_total(args.ledger), 4), "hard_cap": hard}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
