"""ONE capped, unattended run (run on the PC): propositions layer prop_v4 on the SAME 100 decisions as batch 3 (their v3 output already exists, so the two can be compared).
gpt-4.1-mini only. NO database access at all: it reads the paragraph reports already saved under <bundle4>\\recent\\reports.
Total hard cap = ledger total at first start + US$3.00, written once to <out-root>\\bundle5_cap.txt, never raised. Dry run first; the run stops if the dry-run ceiling is above US$2.60.
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
CEILING = 2.60


def ledger_total(path: Path) -> float:
	t = 0.0
	if path.exists():
		for line in path.read_text(encoding="utf-8").splitlines():
			try:
				t += float(json.loads(line).get("usd", 0))
			except Exception:
				pass
	return t


def run(cmd):
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
	ap.add_argument("--out-root", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--bundle4-recent", type=Path, required=True, help="the batch 3 folder holding selection.csv and reports\\")
	args = ap.parse_args()
	root = args.out_root
	root.mkdir(parents=True, exist_ok=True)
	stop = root / "STOP.txt"
	capfile = root / "bundle5_cap.txt"
	if capfile.exists():
		hard = float(capfile.read_text().split()[-1])
	else:
		start = ledger_total(args.ledger)
		hard = math.ceil((start + ALLOWANCE) * 100) / 100
		capfile.write_text(f"START {start:.4f} HARD_CAP {hard:.2f}\n")
	print(json.dumps({"hard_cap": hard, "ledger_now": round(ledger_total(args.ledger), 4)}), flush=True)
	sel = args.bundle4_recent / "selection.csv"
	cases = [r["case_id"] for r in csv.DictReader(sel.open(encoding="utf-8"))]
	now = ledger_total(args.ledger)
	cap = min(hard, math.ceil((now + CEILING) * 100) / 100)

	def cmd(cs, send):
		c = [PY, str(HERE / "summarize_v4.py"), "--model", "gpt-4.1-mini", "--run", "bundle5_prop", "--reports-dir", str(args.bundle4_recent / "reports"), "--meta-csv", str(sel),
			"--out-dir", str(root / "props"), "--ledger", str(args.ledger), "--cap-usd", f"{cap:.2f}", "--stop-file", str(stop), "--cases", ",".join(cs)]
		return c + (["--send"] if send else [])

	code, rows, text = run(cmd(cases, False))
	est = sum(r.get("est_usd_max", 0) for r in rows)
	print(json.dumps({"step": "dry run", "cases": len(cases), "ceiling": round(est, 4), "limit": CEILING, "exit": code}), flush=True)
	if code != 0 or est > CEILING or now + est > hard:
		print(text[-1500:])
		print(json.dumps({"stopped": "dry run failed or above the ceiling"}))
		return 2
	for c in cases:
		if stop.exists():
			print(json.dumps({"stopped": "STOP.txt", "before_case": c}))
			return 2
		code, rows, text = run(cmd([c], True))
		for r in rows:
			print(json.dumps(r), flush=True)
		if code != 0:
			print(text[-1500:])
			print(json.dumps({"stopped": "error or cap refusal", "case": c, "exit": code}))
			return 2
	print(json.dumps({"step_done": "propositions layer", "ledger": round(ledger_total(args.ledger), 4), "spent": round(ledger_total(args.ledger) - now, 4)}), flush=True)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
