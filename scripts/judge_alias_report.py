"""Read-only report of proposed same-person judge merge groups (no writes)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import func, select

from backend.database import CaseJudgeProfile, SessionLocal
from backend.judge_normalization import group_judge_names, parse_judge_name


def build_report(counts: dict[str, int]) -> dict:
	groups = group_judge_names(counts)
	unparsed = sorted(raw for raw in counts if parse_judge_name(raw) is None)
	return {
		"raw_values": len(counts),
		"merge_groups": len(groups),
		"values_in_groups": sum(len(g.members) for g in groups),
		"unparseable_values": len(unparsed),
		"unparseable_sample": unparsed[:50],
		"groups": [
			{"canonical": g.canonical, "members": g.members, "needs_review": g.needs_review,
			 "roles": g.roles, "decisions": sum(counts[m] for m in g.members)}
			for g in groups
		],
	}


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--out", help="Write the full JSON report to this path.")
	parser.add_argument("--top", type=int, default=40, help="Groups to print.")
	args = parser.parse_args()
	with SessionLocal() as session:
		counts = dict(session.execute(
			select(CaseJudgeProfile.raw_name, func.count()).group_by(CaseJudgeProfile.raw_name)
		).all())
	report = build_report(counts)
	for key in ("raw_values", "merge_groups", "values_in_groups", "unparseable_values"):
		print(f"{key}={report[key]}")
	for group in report["groups"][: args.top]:
		print(f"{group['decisions']:>6}  {group['canonical']}  <-  {' | '.join(group['members'])}"
			+ (f"  [review: {' | '.join(group['needs_review'])}]" if group["needs_review"] else ""))
	if args.out:
		Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
	main()
