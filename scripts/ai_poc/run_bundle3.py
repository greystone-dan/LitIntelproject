"""ONE bundled, capped, unattended run (run on the PC): paragraph layer batch 2 with a prompt A/B. gpt-4.1-mini only. NO database writes.
Steps (one at a time with --step N, or all):
  1  read-only pick of 100 NEW recent decisions (excludes batch 1) + paragraph reports; RPD from 2018, more SCC
  2  variant 'base' (fixes only) on all 100 + the 4 batch-1 decisions that lost paragraphs (re-run reports from --prior-reports);
     variants 'brief', 'role', 'g3' (one summary per 3-paragraph group) and 'ctx3' (neighbouring paragraphs as context) on the first 30 decisions of the pick only.     step ceiling US$2.90 (dry-run sum must be below it)
Total hard cap = ledger total at first start + US$3.00, written once to <out-root>\\bundle3_cap.txt, never raised. Every call is also refused by the ledger if it would pass it.
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
ALLOWANCE = 3.00
STEP2_CEILING = 2.90
RETRY = ["35739", "30484", "6202", "61482"]
AB_N = 30
QUOTA = "FC=30,FCA=15,SCC=15,RPD=20,RAD=20"


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
	ap.add_argument("--prior-selection", type=Path, required=True, help="batch 1 selection.csv (excluded from the new pick)")
	ap.add_argument("--prior-reports", type=Path, required=True, help="batch 1 reports folder (for the 4 retries)")
	args = ap.parse_args()
	root = args.out_root
	root.mkdir(parents=True, exist_ok=True)
	stop = root / "STOP.txt"
	capfile = root / "bundle3_cap.txt"
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
			code, rows, text = run([PY, str(HERE / "prepare_recent.py"), "--out-dir", str(recent), "--seed", "batch2", "--quota", QUOTA, "--since-rpd", "2018-01-01", "--exclude-selection", str(args.prior_selection)])
			print(text[-2500:])
			sel = recent / "selection.csv"
			n = len(list(csv.DictReader(sel.open(encoding="utf-8")))) if sel.exists() else 0
			print(json.dumps({"step_done": "1 pick", "exit": code, "picked": n}))
			if code != 0 or n < 90:
				print(json.dumps({"stopped": "pick failed or fewer than 90 decisions", "step": "1"}))
				return 2
		elif s == "2":
			new = [r["case_id"] for r in csv.DictReader((recent / "selection.csv").open(encoding="utf-8"))]
			jobs = [("base", new + RETRY), ("brief", new[:AB_N]), ("role", new[:AB_N]), ("g3", new[:AB_N]), ("ctx3", new[:AB_N])]
			now = ledger_total(args.ledger)
			cap = min(hard, math.ceil((now + STEP2_CEILING) * 100) / 100)

			def cmd(variant, cases, send):
				c = [PY, str(HERE / "summarize_v2.py"), "--model", "gpt-4.1-mini", "--run", "bundle3_" + variant, "--reports-dir", str(recent / "reports"), "--reports-dir", str(args.prior_reports),
					"--meta-csv", str(recent / "selection.csv"), "--meta-csv", str(args.prior_selection), "--variant", variant,
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
