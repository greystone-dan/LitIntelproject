"""Aggregate report-level estimated costs from evaluation artifacts."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "data" / "eval"
DEFAULT_OUTPUT = PROJECT_ROOT / "docs" / "EVALUATION_COSTS.md"
COST_KEYS = ("spent_usd", "actual_cost_usd", "cost_usd", "estimated_cost_usd", "cost")


def _find_cost(value: Any, *, is_root: bool = True) -> tuple[str, float] | None:
	if isinstance(value, dict):
		for key in COST_KEYS:
			candidate = value.get(key)
			if isinstance(candidate, (int, float)) and not isinstance(candidate, bool):
				return key, float(candidate)
		for key, child in value.items():
			found = _find_cost(child, is_root=False)
			if found:
				return f"{key}.{found[0]}", found[1]
	return None


def collect_costs(input_dir: Path) -> list[dict[str, Any]]:
	rows: list[dict[str, Any]] = []
	paths = sorted(input_dir.rglob("*.json"))
	path_set = {path for path in paths}
	for path in paths:
		relative = path.relative_to(input_dir).as_posix()
		if "/requests/" in f"/{relative}" or path.name.endswith("_aggregate.json"):
			continue
		if path.name.endswith(".checkpoint.json") and path.with_name(path.name.removesuffix(".checkpoint.json") + ".json") in path_set:
			continue
		try:
			payload = json.loads(path.read_text(encoding="utf-8"))
		except (OSError, json.JSONDecodeError):
			continue
		found = _find_cost(payload)
		if found:
			rows.append({"artifact": relative, "field": found[0], "estimated_cost_usd": found[1]})
	return rows


def render_report(rows: list[dict[str, Any]]) -> str:
	total = sum(float(row["estimated_cost_usd"]) for row in rows)
	lines = [
		"# Evaluation Cost Ledger",
		"",
		"Last generated: " + datetime.now(timezone.utc).isoformat(),
		"",
		"This report aggregates one report-level recorded estimate per JSON artifact under `data/eval/`.",
		"It is an estimated-cost ledger, not an OpenAI invoice or provider billing export.",
		"",
		"## Measurement Method",
		"",
		"- Fields are selected in this order: `spent_usd`, `actual_cost_usd`, `cost_usd`, `estimated_cost_usd`, `cost`.",
		"- Per-request artifacts under an `requests/` directory are excluded when a report-level artifact exists.",
		"- Comparison artifacts ending in `_aggregate.json` are excluded because they restate earlier report costs.",
		"- A `.checkpoint.json` artifact is excluded when its finalized non-checkpoint counterpart exists.",
		"- Estimates use the rates recorded by each producing script; they are not retroactively repriced.",
		"",
		"## Total",
		"",
		f"- Report-level artifacts: {len(rows)}",
		f"- Recorded estimated spend: ${total:.6f} USD",
		"",
		"## Artifacts",
		"",
		"| Artifact | Cost field | Estimated USD |",
		"| --- | --- | ---: |",
	]
	for row in rows:
		lines.append(f"| `{row['artifact']}` | `{row['field']}` | ${float(row['estimated_cost_usd']):.6f} |")
	return "\n".join(lines).rstrip() + "\n"


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
	parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
	args = parser.parse_args()
	rows = collect_costs(args.input.resolve())
	args.output.resolve().write_text(render_report(rows), encoding="utf-8")
	print(f"artifacts={len(rows)} total_usd={sum(float(row['estimated_cost_usd']) for row in rows):.6f} output={args.output.resolve()}")


if __name__ == "__main__":
	main()