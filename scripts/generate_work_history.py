"""Generate the project work-history ledger from an exported session snapshot."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = PROJECT_ROOT / "docs" / "work_history_sessions.json"
DEFAULT_DAYS_INPUT = PROJECT_ROOT / "docs" / "work_history_days.json"
DEFAULT_MILESTONES_INPUT = PROJECT_ROOT / "docs" / "work_history_milestones.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "WORK_HISTORY.md"
IDLE_GAP_MINUTES = 5


def _hours(minutes: float) -> str:
	return f"{minutes / 60:.1f} h"


def _date(timestamp: str) -> str:
	return timestamp[:10] if timestamp else "unknown date"


def _escape_table(value: object) -> str:
	return str(value or "").replace("|", "\\|").replace("\n", " ")


def load_sessions(path: Path) -> list[dict[str, Any]]:
	payload = json.loads(path.read_text(encoding="utf-8"))
	if not isinstance(payload, list):
		raise ValueError("Work-history session export must be a JSON array")
	sessions: list[dict[str, Any]] = []
	for index, item in enumerate(payload, start=1):
		if not isinstance(item, dict):
			raise ValueError(f"Session #{index} must be an object")
		for field in ("id", "created_at", "summary", "turns", "active_minutes", "workstream"):
			if field not in item:
				raise ValueError(f"Session #{index} is missing {field}")
		sessions.append(item)
	return sorted(sessions, key=lambda item: str(item["created_at"]))


def load_days(path: Path) -> list[dict[str, Any]]:
	payload = json.loads(path.read_text(encoding="utf-8"))
	if not isinstance(payload, list):
		raise ValueError("Work-history day export must be a JSON array")
	days: list[dict[str, Any]] = []
	for index, item in enumerate(payload, start=1):
		if not isinstance(item, dict):
			raise ValueError(f"Day #{index} must be an object")
		for field in ("date", "turns", "active_minutes", "milestones", "features", "session_ids"):
			if field not in item:
				raise ValueError(f"Day #{index} is missing {field}")
		days.append(item)
	return sorted(days, key=lambda item: str(item["date"]))


def load_milestones(path: Path) -> dict[str, list[dict[str, Any]]]:
	payload = json.loads(path.read_text(encoding="utf-8"))
	if not isinstance(payload, dict):
		raise ValueError("Work-history milestones must be a JSON object keyed by date")
	for day, entries in payload.items():
		if not isinstance(entries, list) or not all(isinstance(entry, dict) for entry in entries):
			raise ValueError(f"Milestones for {day} must be a list of objects")
	return payload


def render_work_history(
	sessions: list[dict[str, Any]],
	days: list[dict[str, Any]],
	milestones_by_day: dict[str, list[dict[str, Any]]],
) -> str:
	total_minutes = sum(float(item["active_minutes"]) for item in sessions)
	total_turns = sum(int(item["turns"]) for item in sessions)
	by_stream: dict[str, dict[str, float]] = defaultdict(lambda: {"sessions": 0, "turns": 0, "minutes": 0})
	for item in sessions:
		stream = str(item["workstream"])
		by_stream[stream]["sessions"] += 1
		by_stream[stream]["turns"] += int(item["turns"])
		by_stream[stream]["minutes"] += float(item["active_minutes"])
	first = str(days[0]["date"]) if days else "none"
	last = str(days[-1]["date"]) if days else "none"
	daily_minutes = sum(float(item["active_minutes"]) for item in days)
	daily_turns = sum(int(item["turns"]) for item in days)
	lines = [
		"# AI CaseLibrary Work History",
		"",
		"Last generated: " + datetime.now(timezone.utc).isoformat(),
		"",
		"This is the project work ledger derived from retained local VS Code session "
		"history. It complements `CHANGELOG.md`: the changelog records repository "
		"changes, while this document records the larger work narrative and an "
		"estimated Copilot-assisted effort timeline.",
		"",
		"## Measurement Method",
		"",
		f"- Scope: sessions whose working directory contains `AI CaseLibrary`.",
		f"- Active-time rule: consecutive turns in the same session contribute no more than {IDLE_GAP_MINUTES} minutes each.",
		"- A session's first turn contributes zero minutes because there is no observed "
		"preceding activity interval.",
		"- The estimate includes recorded user/assistant turn intervals, not unrecorded "
		"reading, terminal work, browser work, or work performed outside retained VS Code history.",
		"- It is therefore a reproducible proxy, not a payroll-grade timesheet.",
		"",
		"## Coverage",
		"",
		f"- Retained period: {first} through {last}",
		f"- Retained sessions: {len(sessions)}",
		f"- Retained active dates: {len(days)}",
		f"- Recorded turns: {daily_turns}",
		f"- Five-minute-capped active time: {_hours(daily_minutes)} ({daily_minutes:.1f} minutes)",
		f"- Session-level cross-check: {_hours(total_minutes)} ({total_minutes:.1f} minutes across {total_turns} turns)",
		"- The small difference between daily and session totals comes from sessions that crossed midnight; the daily total is the primary calendar-day estimate.",
		"",
		"## Workstream Breakdown",
		"",
		"| Workstream | Sessions | Turns | Estimated active time |",
		"| --- | ---: | ---: | ---: |",
	]
	for stream, values in sorted(by_stream.items(), key=lambda item: (-item[1]["minutes"], item[0])):
		lines.append(f"| {stream} | {int(values['sessions'])} | {int(values['turns'])} | {_hours(values['minutes'])} |")
	lines.extend(["", "## Day-By-Day Delivery Ledger", ""])
	for item in days:
		lines.extend([
			f"### {item['date']}",
			"",
			f"- Recorded activity: {int(item['turns'])} turns; estimated active time: {_hours(float(item['active_minutes']))}",
			f"- Supporting sessions: {', '.join(f'`{session_id}`' for session_id in item['session_ids'])}",
		])
		lines.extend(["", "**Major milestones**", ""])
		for milestone in item["milestones"]:
			lines.append(f"- {_escape_table(milestone)}")
		lines.extend(["", "**Feature and system work**", ""])
		for feature in item["features"]:
			lines.append(f"- {_escape_table(feature)}")
		verified = milestones_by_day.get(str(item["date"]), [])
		if verified:
			lines.extend(["", "**Verified deliverables and artifacts**", ""])
			for milestone in verified:
				lines.append(f"- **{_escape_table(milestone.get('title'))}**: {_escape_table(milestone.get('detail'))}")
				artifacts = milestone.get("artifacts") or []
				if artifacts:
					lines.append("  Artifacts: " + ", ".join(f"`{_escape_table(artifact)}`" for artifact in artifacts) + ".")
		lines.append("")
	lines.extend([
		"## Refresh Procedure",
		"",
		"1. Query the local Chronicle session store for this workspace and calculate "
		f"per-session active minutes using the fixed {IDLE_GAP_MINUTES}-minute cap.",
		"2. Update `docs/work_history_sessions.json` with new retained session rows, "
		"`docs/work_history_days.json` with calendar-day turn/minute totals and session IDs, and "
		"`docs/work_history_milestones.json` with verified deliverables/artifacts for the affected dates.",
		"3. Regenerate this file:",
		"",
		"```powershell",
		".\\venv\\Scripts\\python.exe scripts\\generate_work_history.py",
		"```",
		"",
		"4. Review the generated chronological entries, then record implementation-level "
		"changes and validation results in `CHANGELOG.md` as appropriate.",
		"",
		"The generator deliberately does not read a private VS Code session database "
		"directly. The session store is accessed through Chronicle, then exported as a "
		"reviewable project artifact. This prevents the system documentation generator "
		"from depending on VS Code internal storage paths or secrets.",
	])
	return "\n".join(lines).rstrip() + "\n"


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
	parser.add_argument("--days-input", type=Path, default=DEFAULT_DAYS_INPUT)
	parser.add_argument("--milestones-input", type=Path, default=DEFAULT_MILESTONES_INPUT)
	parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
	args = parser.parse_args()
	output = args.output.resolve()
	output.write_text(
		render_work_history(
			load_sessions(args.input.resolve()),
			load_days(args.days_input.resolve()),
			load_milestones(args.milestones_input.resolve()),
		),
		encoding="utf-8",
	)
	print(f"generated={output}")


if __name__ == "__main__":
	main()