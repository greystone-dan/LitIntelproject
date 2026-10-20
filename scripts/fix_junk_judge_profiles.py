"""Delete judge profiles that exist only because of junk judge strings ("SOLICITORS OF RECORD", "AND ORDER"). Dry run by default.

Run after scripts/fix_junk_judges.py and scripts/backfill_judge_profiles.py. A profile is junk when every raw
name linked to it (case_judge_profiles.raw_name) is junk by the extractor's own test, or its name has no letters.
Deleting a profile also removes its case links and any alias rows pointing at it (the tables cascade). Profiles
with even one real raw name are left alone.

  python scripts/fix_junk_judge_profiles.py                          # dry run: junk profiles, their case counts
  python scripts/fix_junk_judge_profiles.py --apply --expected-count N    # save an undo file, then delete
  python scripts/fix_junk_judge_profiles.py --undo data/db_fix_backups/junk_judge_profiles_<stamp>.jsonl

Backup first: judge_profiles, case_judge_profiles and judge_profile_aliases. The undo file holds every deleted
profile, its links and its alias rows, and --undo puts them back with their original ids.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text

from backend.database import SessionLocal
from scripts.fix_common import chunked, default_undo_path, read_undo_file, write_undo_file
from scripts.fix_junk_judges import is_junk_judge

RAW_NAMES_SQL = text(
	"SELECT p.id, p.slug, p.display_name, p.normalized_name, p.primary_court, p.aliases, "
	"l.raw_name, COUNT(*) AS n "
	"FROM judge_profiles p LEFT JOIN case_judge_profiles l ON l.judge_profile_id = p.id "
	"GROUP BY p.id, p.slug, p.display_name, p.normalized_name, p.primary_court, p.aliases, l.raw_name"
)


def find_junk_profiles(db) -> list[dict[str, Any]]:
	"""Profiles whose linked raw names are all junk (or that have a letterless name and no real link)."""
	profiles: dict[int, dict[str, Any]] = {}
	raw_names: dict[int, list[tuple[str | None, int]]] = defaultdict(list)
	for row in db.execute(RAW_NAMES_SQL).mappings().all():
		profiles[row["id"]] = {key: row[key] for key in ("id", "slug", "display_name", "normalized_name", "primary_court", "aliases")}
		raw_names[row["id"]].append((row["raw_name"], int(row["n"])))
	junk = []
	for profile_id, profile in profiles.items():
		raws = [(name, n) for name, n in raw_names[profile_id] if name]
		letterless = not any(ch.isalpha() for ch in str(profile["display_name"] or ""))
		if (raws and all(is_junk_judge(name) for name, _ in raws)) or (letterless and not any(not is_junk_judge(name) for name, _ in raws)):
			junk.append({**profile, "cases": sum(n for _, n in raws), "raw_names": sorted({name for name, _ in raws})})
	return sorted(junk, key=lambda p: -p["cases"])


def undo_records(db, profiles: list[dict[str, Any]]):
	for profile in profiles:
		links = db.execute(
			text("SELECT id, case_id, raw_name FROM case_judge_profiles WHERE judge_profile_id = :id ORDER BY id"), {"id": profile["id"]}
		).mappings().all()
		aliases = db.execute(
			text("SELECT id, alias_profile_id, canonical_profile_id, source FROM judge_profile_aliases "
			"WHERE alias_profile_id = :id OR canonical_profile_id = :id"), {"id": profile["id"]}
		).mappings().all()
		yield {
			"profile": {key: profile[key] for key in ("id", "slug", "display_name", "normalized_name", "primary_court", "aliases")},
			"links": [dict(link) for link in links],
			"aliases": [dict(alias) for alias in aliases],
		}


def apply_deletes(db, profiles: list[dict[str, Any]], undo_path: Path, batch_size: int) -> int:
	if write_undo_file(undo_path, undo_records(db, profiles)) != len(profiles):
		raise RuntimeError("undo file is incomplete; nothing changed")
	deleted = 0
	for batch in chunked(profiles, batch_size):
		for profile in batch:
			db.execute(text("DELETE FROM judge_profiles WHERE id = :id"), {"id": profile["id"]})
			deleted += 1
		db.commit()
	return deleted


def restore(db, path: Path) -> int:
	import json

	restored = 0
	for record in read_undo_file(path):
		profile = record["profile"]
		db.execute(
			text("INSERT INTO judge_profiles (id, slug, display_name, normalized_name, primary_court, aliases) "
			"VALUES (:id, :slug, :display_name, :normalized_name, :primary_court, CAST(:aliases AS json)) ON CONFLICT DO NOTHING"),
			{**profile, "aliases": json.dumps(profile["aliases"])},
		)
		for link in record["links"]:
			db.execute(
				text("INSERT INTO case_judge_profiles (id, case_id, judge_profile_id, raw_name) "
				"SELECT :id, :case_id, :profile_id, :raw_name WHERE EXISTS (SELECT 1 FROM cases WHERE id = :case_id) ON CONFLICT DO NOTHING"),
				{**link, "profile_id": profile["id"]},
			)
		for alias in record["aliases"]:
			db.execute(
				text("INSERT INTO judge_profile_aliases (id, alias_profile_id, canonical_profile_id, source) "
				"SELECT :id, :alias_profile_id, :canonical_profile_id, :source "
				"WHERE EXISTS (SELECT 1 FROM judge_profiles WHERE id = :alias_profile_id) "
				"AND EXISTS (SELECT 1 FROM judge_profiles WHERE id = :canonical_profile_id) ON CONFLICT DO NOTHING"),
				alias,
			)
		restored += 1
	db.commit()
	return restored


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Save an undo file, then delete the junk profiles (default is a dry run).")
	parser.add_argument("--undo", type=Path, help="Put back the profiles saved in this undo file.")
	parser.add_argument("--undo-file", type=Path, help="Where --apply writes the undo file (default data/db_fix_backups/).")
	parser.add_argument("--expected-count", type=int, help="With --apply: stop unless exactly this many profiles are found.")
	parser.add_argument("--batch-size", type=int, default=200)
	parser.add_argument("--sample", type=int, default=25, help="Profiles to list in the dry run.")
	args = parser.parse_args(argv)
	with SessionLocal() as db:
		if args.undo:
			print(f"restored={restore(db, args.undo)} profiles from {args.undo}")
			return 0
		junk = find_junk_profiles(db)
		print(f"junk_judge_profiles={len(junk)} linked_cases={sum(p['cases'] for p in junk)}")
		for profile in junk[: args.sample]:
			print(f"  {profile['cases']:6d}  {profile['slug']}  {profile['display_name']!r}  raw={profile['raw_names'][:3]}")
		if not args.apply:
			print("Dry run: nothing written. Add --apply --expected-count N to delete.")
			return 0
		if args.expected_count is not None and args.expected_count != len(junk):
			print(f"Expected {args.expected_count} but found {len(junk)}; nothing changed.")
			return 1
		undo_path = args.undo_file or default_undo_path("junk_judge_profiles")
		print(f"deleted={apply_deletes(db, junk, undo_path, args.batch_size)} undo file: {undo_path}")
		print("Undo with: python scripts/fix_junk_judge_profiles.py --undo", undo_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
