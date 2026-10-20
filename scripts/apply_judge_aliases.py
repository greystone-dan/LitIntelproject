"""Propose, apply or revert judge profile aliases (reversible; dry-run by default).

Duplicate judge profiles (same person under different strings) are mapped onto one canonical
profile in `judge_profile_aliases`. No profile or case link is rewritten or deleted.

  python scripts/apply_judge_aliases.py            # dry run: print proposed merges
  python scripts/apply_judge_aliases.py --prune    # dry run first: rule rows the current rules no longer propose
  python scripts/apply_judge_aliases.py --apply --expected-count N   # write alias rows (needs Daniel's go); saves an undo file
  python scripts/apply_judge_aliases.py --undo data/db_fix_backups/judge_aliases_<stamp>.jsonl   # delete exactly the rows that run wrote
  python scripts/apply_judge_aliases.py --prune --apply --expected-count N   # delete those rows (e.g. Marc/Simon Noël)
  python scripts/apply_judge_aliases.py --revert   # delete every source='rule' alias row (all runs, not one)

The dry run lists every merge group with each member's case count, court and date span, and flags groups whose
members sit in different courts (CROSS-COURT) or overlap in time while in different courts (OVERLAP): those are
the ones that may be two different people. Read every group before approving.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import delete, func, select

from backend.database import Case, CaseJudgeProfile, JudgeProfile, JudgeProfileAlias, SessionLocal
from backend.judge_normalization import best_display_name, group_judge_names
from scripts.fix_common import default_undo_path, read_undo_file, write_undo_file


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
		stats = [
			{"name": p.display_name, "id": p.id, "cases": links[p.id], "court": p.primary_court,
				"first": date.fromordinal(dates[p.id][0]) if p.id in dates else None,
				"last": date.fromordinal(dates[p.id][1]) if p.id in dates else None}
			for p in members
		]
		result.append((canonical, aliases, {"display": group.canonical, "needs_review": group.needs_review, "members": stats}))
	return result


def stale_rows(session) -> list[JudgeProfileAlias]:
	"""Rule alias rows whose two profiles are no longer in the same proposed person group.

	A row is kept when the group still holds both profiles, even if a different member is now the
	canonical one (a new spelling can become the biggest profile without the merge being wrong).
	"""
	group_of: dict[int, int] = {}
	for index, (canonical, aliases, _) in enumerate(propose(session)):
		for profile in [canonical, *aliases]:
			group_of[profile.id] = index
	return [row for row in session.scalars(select(JudgeProfileAlias).where(JudgeProfileAlias.source == "rule"))
		if group_of.get(row.alias_profile_id) is None
		or group_of.get(row.alias_profile_id) != group_of.get(row.canonical_profile_id)]


def group_flags(members: list[dict]) -> list[str]:
	"""CROSS-COURT when members are in different courts; OVERLAP when two members in different courts were active together."""
	flags = []
	courts = {m["court"] for m in members if m["court"]}
	if len(courts) > 1:
		flags.append("CROSS-COURT")
		for index, a in enumerate(members):
			for b in members[index + 1 :]:
				if a["court"] != b["court"] and a["first"] and b["first"] and a["first"] <= b["last"] and b["first"] <= a["last"]:
					flags.append("OVERLAP")
					return flags
	return flags


def format_member(m: dict) -> str:
	span = f"{m['first']:%Y-%m}..{m['last']:%Y-%m}" if m["first"] else "no dates"
	return f"{m['name']} [{m['cases']} cases, {m['court'] or 'no court'}, {span}]"


def func_count():
	return func.count()


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write alias rows (needs --expected-count).")
	parser.add_argument("--expected-count", type=int, help="With --apply: stop unless exactly this many rows would change.")
	parser.add_argument("--prune", action="store_true", help="Remove rule rows the current rules no longer propose.")
	parser.add_argument("--revert", action="store_true", help="Delete all rule-sourced alias rows.")
	parser.add_argument("--undo", type=Path, help="Delete the alias rows written by the run that saved this undo file.")
	parser.add_argument("--undo-file", type=Path, help="Where --apply writes its undo file (default data/db_fix_backups/).")
	args = parser.parse_args()
	if args.apply and args.expected_count is None:
		parser.error("--apply needs --expected-count N (the number the dry run printed)")
	with SessionLocal() as session:
		if args.undo:
			ids = [row["id"] for row in read_undo_file(args.undo)]
			removed = session.execute(delete(JudgeProfileAlias).where(JudgeProfileAlias.id.in_(ids))).rowcount if ids else 0
			session.commit()
			print(f"alias_rows_removed={removed} of {len(ids)} listed in {args.undo}")
			return 0
		if args.revert:
			removed = session.execute(delete(JudgeProfileAlias).where(JudgeProfileAlias.source == "rule")).rowcount
			session.commit()
			print(f"alias_rows_removed={removed}")
			return 0
		if args.prune:
			names = {p.id: p.display_name for p in session.scalars(select(JudgeProfile))}
			stale = stale_rows(session)
			for row in stale:
				print(f"remove: {names.get(row.alias_profile_id)}  -/->  {names.get(row.canonical_profile_id)}")
			if args.apply:
				if args.expected_count != len(stale):
					print(f"Expected {args.expected_count} but found {len(stale)}; nothing changed.")
					return 1
				undo_path = args.undo_file or default_undo_path("judge_aliases_pruned")
				write_undo_file(undo_path, ({"id": r.id, "alias_profile_id": r.alias_profile_id,
					"canonical_profile_id": r.canonical_profile_id, "source": r.source} for r in stale))
				for row in stale:
					session.delete(row)
				session.commit()
				print(f"pruned rows saved in {undo_path} (re-insert them by hand if needed)")
			print(f"alias_rows_{'removed' if args.apply else 'to_remove'}={len(stale)}")
			return 0
		existing = {a for (a,) in session.execute(select(JudgeProfileAlias.alias_profile_id))}
		proposals = propose(session)
		total_aliases = 0
		to_write: list[tuple[int, int]] = []
		flagged = 0
		for canonical, aliases, info in proposals:
			new = [p for p in aliases if p.id not in existing]
			total_aliases += len(new)
			flags = group_flags(info["members"])
			flagged += bool(flags)
			shown = best_display_name([canonical.display_name, *(p.display_name for p in aliases)]) or canonical.display_name
			print(f"{'[' + ', '.join(flags) + '] ' if flags else ''}{shown}"
				+ (f"  [review: {len(info['needs_review'])} surname-only left alone]" if info["needs_review"] else ""))
			print(f"    keep: {format_member(next(m for m in info['members'] if m['id'] == canonical.id))}")
			for m in info["members"]:
				if m["id"] != canonical.id:
					print(f"    alias{'' if m['id'] in {p.id for p in new} else ' (already merged)'}: {format_member(m)}")
			to_write.extend((p.id, canonical.id) for p in new)
		print(f"merge_groups={len(proposals)} flagged_groups={flagged} alias_rows_{'to_write' if args.apply else 'proposed'}={total_aliases}")
		if args.apply:
			if args.expected_count != total_aliases:
				print(f"Expected {args.expected_count} but found {total_aliases}; nothing changed.")
				return 1
			rows = [JudgeProfileAlias(alias_profile_id=a, canonical_profile_id=c, source="rule") for a, c in to_write]
			session.add_all(rows)
			session.flush()
			undo_path = args.undo_file or default_undo_path("judge_aliases")
			write_undo_file(undo_path, ({"id": r.id, "alias_profile_id": r.alias_profile_id,
				"canonical_profile_id": r.canonical_profile_id} for r in rows))
			session.commit()
			print(f"alias_rows_written={len(rows)} undo file: {undo_path}")
			print("Undo with: python scripts/apply_judge_aliases.py --undo", undo_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
