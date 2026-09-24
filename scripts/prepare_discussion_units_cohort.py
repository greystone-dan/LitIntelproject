"""Prepare deterministic reports and no-network requests for a Discussion Unit cohort."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import SessionLocal
from scripts.inspect_discussion_units import _render_markdown, inspect_case
from scripts.package_discussion_units_llm import build_request

DEFAULT_CORE = Path("data/eval/llm_discussion_units_pilot/discussion_unit_core_300.csv")
DEFAULT_RUN_DIR = Path("data/eval/llm_discussion_units_pilot/core_300_run")


def load_case_ids(path: Path) -> list[int]:
	with path.open(newline="", encoding="utf-8-sig") as handle:
		rows = list(csv.DictReader(handle))
	if len(rows) != 300:
		raise ValueError(f"expected 300 core rows, found {len(rows)}")
	case_ids = [int(float(row["case_id"])) for row in rows]
	if len(set(case_ids)) != 300:
		raise ValueError("core manifest source contains duplicate case IDs")
	return case_ids


def prepare_case(case_id: int, run_dir: Path, *, chunk_set: str, model: str, budget_usd: float) -> dict[str, str]:
	report_path = run_dir / "reports" / f"case_{case_id}_deterministic.json"
	deterministic_markdown_path = run_dir / "reports" / f"case_{case_id}_deterministic.md"
	request_path = run_dir / "requests" / f"case_{case_id}_request.json"
	markdown_path = run_dir / "reviews" / f"case_{case_id}_hybrid.md"
	with SessionLocal() as session:
		report = {"status": "dry_run", **inspect_case(session, case_id, chunk_set, 0.35, 2)}
	report_path.parent.mkdir(parents=True, exist_ok=True)
	report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
	deterministic_markdown_path.parent.mkdir(parents=True, exist_ok=True)
	deterministic_markdown_path.write_text(_render_markdown(report), encoding="utf-8")
	request = build_request(report, model=model, budget_usd=budget_usd)
	request_path.parent.mkdir(parents=True, exist_ok=True)
	request_path.write_text(json.dumps(request, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
	return {
		"case_id": str(case_id),
		"input_json": str(report_path),
		"output_request": str(request_path),
		"output_markdown": str(markdown_path),
	}


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--core-csv", type=Path, default=DEFAULT_CORE)
	parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN_DIR)
	parser.add_argument("--chunk-set", default="paragraph")
	parser.add_argument("--model", default="gpt-4.1-nano")
	parser.add_argument("--budget-usd", type=float, default=1.0)
	args = parser.parse_args()
	if args.budget_usd <= 0 or args.budget_usd > 3:
		parser.error("--budget-usd must be between 0 and 3")
	case_ids = load_case_ids(args.core_csv)
	manifest_path = args.run_dir / "manifest.csv"
	ledger_path = args.run_dir / "ledger.json"
	rows: list[dict[str, str]] = []
	for case_id in case_ids:
		rows.append(prepare_case(case_id, args.run_dir, chunk_set=args.chunk_set, model=args.model, budget_usd=args.budget_usd))
	manifest_path.parent.mkdir(parents=True, exist_ok=True)
	with manifest_path.open("w", newline="", encoding="utf-8") as handle:
		writer = csv.DictWriter(handle, fieldnames=["case_id", "input_json", "output_request", "output_markdown"])
		writer.writeheader()
		writer.writerows(rows)
	if not ledger_path.exists():
		ledger_path.write_text(json.dumps({"ledger_version": 1, "cases": {}}, indent=2) + "\n", encoding="utf-8")
	summary: dict[str, Any] = {
		"status": "prepared",
		"case_count": len(rows),
		"chunk_set": args.chunk_set,
		"model": args.model,
		"manifest": str(manifest_path),
		"ledger": str(ledger_path),
		"network_called": False,
	}
	(args.run_dir / "preparation_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
	print(json.dumps(summary, sort_keys=True))
	return 0


if __name__ == "__main__":
	raise SystemExit(main())