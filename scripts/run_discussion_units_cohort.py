"""Run a manifest of Discussion Unit cases with durable skip/retry state."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import subprocess
import sys

try:
	from scripts.discussion_units_ledger import should_skip
except ModuleNotFoundError:
	from discussion_units_ledger import should_skip


def load_manifest(path: Path) -> list[dict[str, str]]:
	with path.open(newline="", encoding="utf-8-sig") as handle:
		rows = list(csv.DictReader(handle))
	required = {"case_id", "input_json", "output_request", "output_markdown"}
	missing = required.difference(rows[0] if rows else {})
	if missing:
		raise ValueError(f"manifest missing columns: {sorted(missing)}")
	return rows


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--manifest", type=Path, required=True)
	parser.add_argument("--ledger-path", type=Path, required=True)
	parser.add_argument("--python", type=Path, default=Path(sys.executable))
	parser.add_argument("--send", action="store_true")
	parser.add_argument("--retry-failed", action="store_true")
	parser.add_argument("--max-cases", type=int)
	args, package_args = parser.parse_known_args()
	if args.max_cases is not None and args.max_cases < 1:
		parser.error("--max-cases must be positive")
	rows = load_manifest(args.manifest)
	if args.max_cases is not None:
		rows = rows[: args.max_cases]
	summary = {"selected": len(rows), "skipped": 0, "completed": 0, "failed": 0}
	for row in rows:
		case_id = int(row["case_id"])
		if should_skip(args.ledger_path, case_id, retry_failed=args.retry_failed):
			summary["skipped"] += 1
			continue
		command = [
			str(args.python),
			"scripts/package_discussion_units_llm.py",
			"--input-json", row["input_json"],
			"--output-request", row["output_request"],
			"--output-markdown", row["output_markdown"],
			"--ledger-path", str(args.ledger_path),
		]
		if args.send:
			command.append("--send")
		if args.retry_failed:
			command.append("--retry-failed")
		command.extend(package_args)
		result = subprocess.run(command, text=True, capture_output=True)
		if result.returncode == 0:
			summary["completed"] += 1
		else:
			summary["failed"] += 1
	print(json.dumps(summary, sort_keys=True))
	return 1 if summary["failed"] else 0


if __name__ == "__main__":
	raise SystemExit(main())