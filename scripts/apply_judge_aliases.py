"""Propose, apply or revert judge profile aliases (reversible; dry-run by default).

Duplicate judge profiles (same person under different strings) are mapped onto one canonical
profile in `judge_profile_aliases`. No profile or case link is rewritten or deleted.

  python scripts/apply_judge_aliases.py            # dry run: print proposed merges
  python scripts/apply_judge_aliases.py --apply    # write alias rows (needs Daniel's go)
  python scripts/apply_judge_aliases.py --prune    # dry run: rule rows the current rules no longer propose
  python scripts/apply_judge_aliases.py --prune --apply   # delete those rows (e.g. Marc/Simon Noël)
  python scripts/apply_judge_aliases.py --revert   # delete every source='rule' alias row
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import delete, func, select

from backend.database import Case, CaseJudgeProfile, JudgeProfile, JudgeProfileAlias, SessionLocal
from backend.judge_normalization import best_display_name, group_judge_names


def propose(session) -> list[tuple[JudgeProfile, list[JudgeProfile], dict]]:
	"""Return (canonical profile, alias profiles, group info) for each safe merge group."""
	profiles = list(session.scalars(select(JudgeProfile).order_by(JudgeProfile.id)))
	links: dict[int, int] = defaultdict(int)
	for profile_id, count in session.execute(
		select(CaseJudgeProfile.judge_profile_id, func_count()).group_by(CaseJudgeProfile.judge_profile_id)
	):
		links[profile_id] = count
	by_name: dict[str, list[JudgeProfile]] = defaultdict(list)
	for profile in profiles:
		by_name[profile.display_name].append(profile)
	counts = {name: sum(links[p.id] for p in plist) for name, plist in by_name.items()}
	dates: dict[int, list[int]] = {}
	for profile_id, first, last in session.execute(
		select(CaseJudgeProfile.judge_profile_id, func.min(Case.date), func.max(Case.date))
		.join(Case, Case.id == CaseJudgeProfile.case_id).group_by(CaseJudgeProfile.judge_profile_id)
	):
		if first and last:
			dates[profile_id] = [first.toordinal(), last.toordinal()]
	spans = {}
	for name, plist in by_name.items():
		known = [dates[p.id] for p in plist if p.id in dates]
		if known:
			spans[name] = (min(a for a, _ in known), max(b for _, b in known))
	courts = {name: {p.primary_court for p in plist if p.primary_court} for name, plist in by_name.items()}
	result = []
	for group in group_judge_names(counts, spans, courts):
		members = [p for name in group.members for p in by_name[name]]
		if len(members) < 2:
			continue
		canonical = max(members, key=lambda p: links[p.id])
		aliases = [p for p in members if p.id != canonical.id]
		result.append((canonical, aliases, {"display": group.canonical, "needs_review": group.needs_review}))
	return result


def func_count():
	return func.count()


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write alias rows.")
	parser.add_argument("--prune", action="store_true", help="Remove rule rows the current rules no longer propose.")
	parser.add_argument("--revert", action="store_true", help="Delete all rule-sourced alias rows.")
	args = parser.parse_args()
	with SessionLocal() as session:
		if args.revert:
			removed = session.execute(delete(JudgeProfileAlias).where(JudgeProfileAlias.source == "rule")).rowcount
			session.commit()
			print(f"alias_rows_removed={removed}")
			return
		if args.prune:
			wanted = {p.id: c.id for c, aliases, _ in propose(session) for p in aliases}
			names = {p.id: p.display_name for p in session.scalars(select(JudgeProfile))}
			stale = [row for row in session.scalars(select(JudgeProfileAlias).where(JudgeProfileAlias.source == "rule"))
				if wanted.get(row.alias_profile_id) != row.canonical_profile_id]
			for row in stale:
				print(f"remove: {names.get(row.alias_profile_id)}  -/->  {names.get(row.canonical_profile_id)}")
				if args.apply:
					session.delete(row)
			if args.apply:
				session.commit()
			print(f"alias_rows_{'removed' if args.apply else 'to_remove'}={len(stale)}")
			return
		existing = {a for (a,) in session.execute(select(JudgeProfileAlias.alias_profile_id))}
		proposals = propose(session)
		total_aliases = 0
		for canonical, aliases, info in proposals:
			new = [p for p in aliases if p.id not in existing]
			total_aliases += len(new)
			shown = best_display_name([canonical.display_name, *(p.display_name for p in aliases)]) or canonical.display_name
			print(f"{shown}  <-  {' | '.join(p.display_name for p in aliases)}"
				+ (f"  [review: {len(info['needs_review'])} surname-only left alone]" if info["needs_review"] else ""))
			if args.apply:
				for p in new:
					session.add(JudgeProfileAlias(alias_profile_id=p.id, canonical_profile_id=canonical.id, source="rule"))
		if args.apply:
			session.commit()
		print(f"merge_groups={len(proposals)} alias_rows_{'written' if args.apply else 'proposed'}={total_aliases}")


if __name__ == "__main__":
	main()
