"""One bundled, capped, unattended run of the AI proof of concept steps (run on the PC). No database access, no writes outside --out-root.

Steps (run one at a time with --step N, or all with --step all; each step re-checks the stop file, the step ceiling and the total cap):
  1  themes v5c (gpt-4.1-mini) on the 10 new cases                         ceiling US$0.60
  2  copy all theme files into one folder (no spend)
  3  rebuttal pass A (gpt-4.1-mini), control, on the 29 cases              ceiling US$0.90
  4  rebuttal pass with our own data, arms H, I, K, HIK, on 12 cases       ceiling US$0.35 per arm, US$1.40 in all
Total hard cap = ledger total at first start + US$3.00, written once to <out-root>\\bundle_cap.txt and never raised.
Every step: dry run first (no --send) and refuse to continue if its printed ceiling is above the step ceiling; every call is also capped by the
shared ledger (the call is refused if it would pass the cap). Stop rule: create <out-root>\\STOP.txt and the run stops before the next case.
Any error or non-zero exit stops the whole run; nothing is retried automatically except by the scripts' own call retry (which is billed and ledgered).
"""
from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = sys.executable
TOTAL_ALLOWANCE = 3.00
NEW10 = "44223,37148,39526,59341,52431,40225,50174,70165,62466,67972"
OLD_B = "7522,64240,46057,51014,19246,23342"
OLD_C = "16152,17038,19499,23057,23409,23574,25379,26403,27234,33096,38873,52403,7161"  # 48289 (no paragraph numbers) is left out
ALL29 = OLD_B + "," + OLD_C + "," + NEW10
ARM_CASES = "51014,64240,17038,33096,52403,7522,16152,19499,23057,38873,25379,23409"
ARMS = ["H", "I", "K", "HIK"]


def ledger_total(path: Path) -> float:
	t = 0.0
	if path.exists():
		for line in path.read_text(encoding="utf-8").splitlines():
			try:
				t += float(json.loads(line).get("usd", 0))
			except Exception:
				pass
	return t


def run(cmd: list[str]) -> tuple[int, list[dict], str]:
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
	ap.add_argument("--step", required=True, help="1, 2, 3, 4 or all")
	ap.add_argument("--out-root", type=Path, required=True)
	ap.add_argument("--ledger", type=Path, required=True)
	ap.add_argument("--unseen-reports", type=Path, required=True, help="reports of the 6 earlier picks (unseen\\reports)")
	ap.add_argument("--unseen-csv", type=Path, required=True, help="unseen\\selection.csv")
	ap.add_argument("--new10-dir", type=Path, required=True, help="ai_poc_data\\unseen10 (reports + selection.csv)")
	ap.add_argument("--v5c-dir", type=Path, required=True, help="folder with the 6 v5c theme files (mini6_v5c)")
	ap.add_argument("--v5b-dir", type=Path, required=True, help="folder with the 20 v5b theme files (mini25_unseen)")
	args = ap.parse_args()
	root = args.out_root
	root.mkdir(parents=True, exist_ok=True)
	stop = root / "STOP.txt"
	capfile = root / "bundle_cap.txt"
	if capfile.exists():
		hard = float(capfile.read_text().split()[-1])
	else:
		start = ledger_total(args.ledger)
		hard = math.ceil((start + TOTAL_ALLOWANCE) * 100) / 100
		capfile.write_text(f"START {start:.4f} HARD_CAP {hard:.2f}\n")
	print(json.dumps({"hard_cap": hard, "ledger_now": round(ledger_total(args.ledger), 4)}), flush=True)
	reports = ["--reports-dir", "data/eval/llm_discussion_units_pilot/core_300_run/reports", "--reports-dir", str(args.unseen_reports), "--reports-dir", str(args.new10_dir / "reports")]
	metas = ["--meta-csv", "data/eval/ai_poc_unseen_fc14.csv", "--meta-csv", str(args.unseen_csv), "--meta-csv", str(args.new10_dir / "selection.csv")]
	themes_all = root / "themes_all"
	steps = ["1", "2", "3", "4"] if args.step == "all" else [args.step]

	def guarded(name: str, script: str, base: list[str], cases: list[str], ceiling: float, out_dir: Path) -> bool:
		if stop.exists():
			print(json.dumps({"stopped": "STOP.txt", "step": name}))
			return False
		now = ledger_total(args.ledger)
		cap = min(hard, math.ceil((now + ceiling) * 100) / 100)
		if now + ceiling > hard + 1e-9:
			print(json.dumps({"stopped": "step ceiling would pass the total cap", "step": name, "ledger": now, "ceiling": ceiling, "hard_cap": hard}))
			return False
		cmd = [PY, str(HERE / script), *base, "--cases", ",".join(cases), "--out-dir", str(out_dir), "--ledger", str(args.ledger), "--cap-usd", f"{cap:.2f}"]
		code, rows, text = run(cmd)
		est = sum(r.get("est_usd_max", 0) for r in rows)
		print(json.dumps({"step": name, "dry_run_ceiling_sum": round(est, 4), "step_ceiling": ceiling, "exit": code}), flush=True)
		if code != 0 or est > ceiling:
			print(text[-1500:])
			print(json.dumps({"stopped": "dry run failed or above the step ceiling", "step": name}))
			return False
		for c in cases:
			if stop.exists():
				print(json.dumps({"stopped": "STOP.txt", "step": name, "before_case": c}))
				return False
			code, rows, text = run(cmd[: cmd.index("--cases")] + ["--cases", c] + cmd[cmd.index("--out-dir"):] + ["--send"])
			for r in rows:
				print(json.dumps(r), flush=True)
			if code != 0:
				print(text[-1500:])
				print(json.dumps({"stopped": "error or cap refusal", "step": name, "case": c, "exit": code}))
				return False
		print(json.dumps({"step_done": name, "ledger": round(ledger_total(args.ledger), 4), "spent_in_step": round(ledger_total(args.ledger) - now, 4)}), flush=True)
		return True

	for s in steps:
		if s == "1":
			ok = guarded("1 themes new10", "extract_themes_v5.py", ["--model", "gpt-4.1-mini", "--run", "bundle_themes10", *reports, *metas], NEW10.split(","), 0.60, root / "themes10")
		elif s == "2":
			themes_all.mkdir(exist_ok=True)
			for d in (args.v5b_dir, args.v5c_dir, root / "themes10"):  # later folders win, so v5c replaces v5b
				for f in sorted(Path(d).glob("case_*_themes_*_v5*_gpt-4.1-mini.json")):  # v5 < v5b < v5c, mini only
					for old in themes_all.glob(f"case_{f.name.split('_')[1]}_themes_*.json"):
						old.unlink()
					shutil.copy(f, themes_all / f.name)
			print(json.dumps({"step_done": "2 merge", "files": len(list(themes_all.glob("*.json")))}))
			ok = True
		elif s == "3":
			ok = guarded("3 rebuttal A control", "extract_rebuttals.py", ["--model", "gpt-4.1-mini", "--run", "bundle_rebut_A", "--themes-dir", str(themes_all), *reports, *metas], ALL29.split(","), 0.90, root / "rebut_A")
		elif s == "4":
			ok = True
			for arm in ARMS:
				ok = guarded(f"4 arm {arm}", "extract_rebuttals.py", ["--model", "gpt-4.1-mini", "--run", f"bundle_rebut_{arm}", "--context", arm, "--stop-file", str(stop), "--themes-dir", str(themes_all), *reports, *metas], ARM_CASES.split(","), 0.35, root / f"rebut_{arm}")
				if not ok:
					break
		else:
			raise SystemExit("unknown step")
		if not ok:
			return 2
	print(json.dumps({"finished": args.step, "ledger": round(ledger_total(args.ledger), 4), "hard_cap": hard}))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
