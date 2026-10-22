"""Merge ONE duplicate judge profile into another through the reversible alias layer (dry run by default).

Writes exactly one row to `judge_profile_aliases` (alias profile -> canonical profile). No profile or case link is
changed or deleted; the judge list and judge page already add an alias profile's decisions to its canonical profile.

  python scripts/merge_one_judge_profile.py --alias-id A --canonical-id C                          # dry run
  python scripts/merge_one_judge_profile.py --alias-id A --canonical-id C --apply --expected-count 1  # writes 1 row, saves an undo file
  python scripts/merge_one_judge_profile.py --undo data/db_fix_backups/merge_one_judge_<stamp>.jsonl   # delete exactly that row

The dry run prints both profiles (court, decision count, date span, raw names linked) and refuses when the two are
not plainly the same person: different primary courts, no shared surname, either profile already aliased, or
the alias profile being someone else's canonical profile.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import delete, func, select

from backend.database import Case, CaseJudgeProfile, JudgeProfile, JudgeProfileAlias, SessionLocal
from scripts.fix_common import default_undo_path, read_undo_file, write_undo_file


def describe(session, profile: JudgeProfile) -> dict:
	first, last, links, cases = session.execute(
		select(func.min(Case.date), func.max(Case.date), func.count(CaseJudgeProfile.id), func.count(func.distinct(CaseJudgeProfile.case_id)))
		.join(Case, Case.id == CaseJudgeProfile.case_id).where(CaseJudgeProfile.judge_profile_id == profile.id)
	).one()
	raw = session.execute(
		select(CaseJudgeProfile.raw_name, func.count()).where(CaseJudgeProfile.judge_profile_id == profile.id)
		.group_by(CaseJudgeProfile.raw_name).order_by(func.count().desc())
	).all()
	return {"id": profile.id, "slug": profile.slug, "name": profile.display_name, "court": profile.primary_court,
		"links": links, "cases": cases, "first": first, "last": last, "raw_names": raw}


def surname_tokens(profile: JudgeProfile) -> set[str]:
	text = (profile.normalized_name or profile.display_name or "").lower()
	return {t.strip(".,") for t in text.split() if len(t.strip(".,")) > 2}


def problems(session, alias: JudgeProfile, canonical: JudgeProfile) -> list[str]:
	found = []
	if alias.id == canonical.id:
		found.append("alias and canonical are the same profile")
	if alias.primary_court and canonical.primary_court and alias.primary_court != canonical.primary_court:
		found.append(f"different primary courts ({alias.primary_court} vs {canonical.primary_court})")
	if not surname_tokens(alias) & surname_tokens(canonical):
		found.append("no shared name word")
	if session.scalar(select(JudgeProfileAlias.id).where(JudgeProfileAlias.alias_profile_id == alias.id)):
		found.append("alias profile is already aliased")
	if session.scalar(select(JudgeProfileAlias.id).where(JudgeProfileAlias.canonical_profile_id == alias.id)):
		found.append("alias profile is the canonical profile of other aliases")
	if session.scalar(select(JudgeProfileAlias.id).where(JudgeProfileAlias.alias_profile_id == canonical.id)):
		found.append("canonical profile is itself an alias")
	return found


def write_alias_row(session, alias_id: int, canonical_id: int, undo_path: Path) -> JudgeProfileAlias:
	"""Add the alias row (flushed, not committed) and save the undo file with its id and both profile ids."""
	row = JudgeProfileAlias(alias_profile_id=alias_id, canonical_profile_id=canonical_id, source="manual")
	session.add(row)
	session.flush()
	write_undo_file(undo_path, [{"id": row.id, "alias_profile_id": alias_id, "canonical_profile_id": canonical_id}])
	return row


def remove_alias_rows(session, rows: list[dict]) -> int:
	"""Delete only rows whose id AND both profile ids match the undo file; returns how many were removed."""
	removed = 0
	for r in rows:
		removed += session.execute(delete(JudgeProfileAlias).where(
			JudgeProfileAlias.id == r["id"], JudgeProfileAlias.alias_profile_id == r["alias_profile_id"],
			JudgeProfileAlias.canonical_profile_id == r["canonical_profile_id"])).rowcount
	return removed


def main() -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--alias-id", type=int, help="The duplicate (smaller) profile id.")
	parser.add_argument("--canonical-id", type=int, help="The profile to keep (larger).")
	parser.add_argument("--apply", action="store_true", help="Write the alias row (needs --expected-count 1).")
	parser.add_argument("--expected-count", type=int)
	parser.add_argument("--undo", type=Path, help="Delete the alias row written by the run that saved this undo file.")
	parser.add_argument("--undo-file", type=Path)
	args = parser.parse_args()
	with SessionLocal() as session:
		if args.undo:
			rows = [r for r in read_undo_file(args.undo) if {"id", "alias_profile_id", "canonical_profile_id"} <= r.keys()]
			print(f"alias_rows_to_remove={len(rows)} of {sum(1 for _ in read_undo_file(args.undo))} lines in {args.undo}")
			if args.apply:
				removed = remove_alias_rows(session, rows)
				session.commit()
				print(f"alias_rows_removed={removed}")
			else:
				print("Dry run. Add --apply to remove them.")
			return 0
		if args.alias_id is None or args.canonical_id is None:
			parser.error("--alias-id and --canonical-id are required")
		alias = session.get(JudgeProfile, args.alias_id)
		canonical = session.get(JudgeProfile, args.canonical_id)
		if alias is None or canonical is None:
			print("A profile id does not exist; nothing changed.")
			return 1
		for label, profile in (("keep ", canonical), ("alias", alias)):
			d = describe(session, profile)
			span = f"{d['first']}..{d['last']}" if d["first"] else "no dates"
			print(f"{label}: id={d['id']} slug={d['slug']} name={d['name']!r} court={d['court']} cases={d['cases']} links={d['links']} span={span}")
			for raw, n in d["raw_names"][:10]:
				print(f"        raw_name {raw!r} x{n}")
		both = session.scalar(
			select(func.count()).where(
				CaseJudgeProfile.judge_profile_id == alias.id,
				CaseJudgeProfile.case_id.in_(select(CaseJudgeProfile.case_id).where(CaseJudgeProfile.judge_profile_id == canonical.id)),
			)
		)
		print(f"cases linked to both profiles: {both}")
		bad = problems(session, alias, canonical)
		for item in bad:
			print(f"REFUSED: {item}")
		to_write = 0 if bad else 1
		print(f"alias_rows_{'to_write' if not args.apply else 'writing'}={to_write}")
		if args.apply:
			if bad or args.expected_count != to_write:
				print(f"Expected {args.expected_count} but would write {to_write}; nothing changed.")
				return 1
			undo_path = args.undo_file or default_undo_path("merge_one_judge")
			try:
				write_alias_row(session, alias.id, canonical.id, undo_path)
				session.commit()
			except Exception:
				session.rollback()
				undo_path.unlink(missing_ok=True)
				raise
			print(f"alias_rows_written=1 undo file: {undo_path}")
			print("Undo with: python scripts/merge_one_judge_profile.py --undo", undo_path, "--apply")
		else:
			print("Dry run: nothing written.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
