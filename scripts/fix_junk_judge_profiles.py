"""Delete judge profiles that exist only because of junk judge strings ("SOLICITORS OF RECORD", "AND ORDER"). Dry run by default.

Run after scripts/fix_junk_judges.py and scripts/backfill_judge_profiles.py. A profile is junk when every raw
name linked to it (case_judge_profiles.raw_name) is junk by the extractor's own test, or its name has no letters.
Deleting a profile also removes its case links and any alias rows pointing at it (the tables cascade). Profiles
with even one real raw name are left alone.

  python scripts/fix_junk_judge_profiles.py                          # dry run: junk profiles, their case counts
  python scripts/fix_junk_judge_profiles.py --csv names.csv          # also list every junk profile (and the review-only ones) in a CSV
  python scripts/fix_junk_judge_profiles.py --apply --expected-count N    # save an undo file, then delete (--expected-count is required)
  python scripts/fix_junk_judge_profiles.py --undo data/db_fix_backups/junk_judge_profiles_<stamp>.jsonl

Review-only names ("THE COURT") are never counted as junk or deleted here: some are real attributions to the court
as a whole. The dry run and CSV list those profiles with how many decisions have no other judge link (where deleting
the link would leave the decision without any judge), so a human can check before any of them is cleaned up.

Does NOT remove the profiles made from SCC panel strings (several judges in one string); that is a separate cleanup.
Run order: fix_junk_judges.py (add --include-label-only to also clear "AND ORDER", which needs its own approval),
check a sample of the changed rows, backfill_judge_profiles.py, then this script, then apply_judge_aliases.py.
"AND ORDER" counts as junk here whether or not fix_junk_judges was run with that flag; if it was not, the next
backfill recreates that profile from the cases that still carry the label.

Backup first: judge_profiles, case_judge_profiles and judge_profile_aliases. The undo file holds every deleted
profile, its links and its alias rows, and --undo puts them back with their original ids. Restored profiles
and links get the restore time as created_at/updated_at, not their original timestamps.
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
from scripts.fix_junk_judges import is_junk_judge as _is_junk


def is_junk_raw(name: Any) -> bool:
	"""Junk by the extractor's test, or a bare label such as \"AND ORDER\"."""
	return _is_junk(name, include_label_only=True)

RAW_NAMES_SQL = text(
	"SELECT p.id, p.slug, p.display_name, p.normalized_name, p.primary_court, p.aliases, "
	"l.raw_name, COUNT(*) AS n "
	"FROM judge_profiles p LEFT JOIN case_judge_profiles l ON l.judge_profile_id = p.id "
	"GROUP BY p.id, p.slug, p.display_name, p.normalized_name, p.primary_court, p.aliases, l.raw_name"
)


def find_junk_profiles(db, mixed: list | None = None) -> list[dict[str, Any]]:
	"""Profiles whose linked raw names are all junk (or that have a letterless name and no real link).

	Profiles that have some junk raw names next to real ones are left alone; pass a list as `mixed` to collect them."""
	profiles: dict[int, dict[str, Any]] = {}
	raw_names: dict[int, list[tuple[str | None, int]]] = defaultdict(list)
	for row in db.execute(RAW_NAMES_SQL).mappings().all():
		profiles[row["id"]] = {key: row[key] for key in ("id", "slug", "display_name", "normalized_name", "primary_court", "aliases")}
		raw_names[row["id"]].append((row["raw_name"], int(row["n"])))
	junk = []
	for profile_id, profile in profiles.items():
		raws = [(name, n) for name, n in raw_names[profile_id] if name]
		letterless = not any(ch.isalpha() for ch in str(profile["display_name"] or ""))
		if (raws and all(is_junk_raw(name) for name, _ in raws)) or (letterless and not any(not is_junk_raw(name) for name, _ in raws)):
			junk.append({**profile, "cases": sum(n for _, n in raws), "raw_names": sorted({name for name, _ in raws})})
		elif mixed is not None and any(is_junk_raw(name) for name, _ in raws):
			mixed.append({**profile, "cases": sum(n for _, n in raws), "junk_cases": sum(n for name, n in raws if is_junk_raw(name))})
	return sorted(junk, key=lambda p: -p["cases"])


REVIEW_ONLY_NAMES = ("THE COURT",)
REVIEW_SQL = text(
	"SELECT p.id, p.slug, p.display_name, p.primary_court, COUNT(*) AS links, "
	"COUNT(*) FILTER (WHERE NOT EXISTS (SELECT 1 FROM case_judge_profiles o "
	"WHERE o.case_id = l.case_id AND o.judge_profile_id <> p.id)) AS only_attribution "
	"FROM judge_profiles p JOIN case_judge_profiles l ON l.judge_profile_id = p.id "
	"WHERE upper(trim(p.display_name)) = ANY(:names) "
	"GROUP BY p.id, p.slug, p.display_name, p.primary_court ORDER BY links DESC"
)
CSV_FIELDS = ["status", "profile_id", "slug", "display_name", "primary_court", "linked_cases", "raw_names", "only_attribution_cases"]


def find_review_only(db) -> list[dict[str, Any]]:
	return [dict(row) for row in db.execute(REVIEW_SQL, {"names": list(REVIEW_ONLY_NAMES)}).mappings().all()]


def write_names_csv(path: Path, junk: list[dict[str, Any]], review: list[dict[str, Any]]) -> int:
	"""One row per profile: every junk profile (status junk) and every review-only profile (status review_only). Never overwrites."""
	import csv

	path.parent.mkdir(parents=True, exist_ok=True)
	count = 0
	with open(path, "x", encoding="utf-8", newline="") as handle:
		writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
		writer.writeheader()
		for profile in sorted(junk, key=lambda p: (p["display_name"] or "", p["id"])):
			writer.writerow({"status": "junk", "profile_id": profile["id"], "slug": profile["slug"],
				"display_name": profile["display_name"], "primary_court": profile["primary_court"],
				"linked_cases": profile["cases"], "raw_names": " | ".join(str(n) for n in profile["raw_names"]),
				"only_attribution_cases": ""})
			count += 1
		for profile in review:
			writer.writerow({"status": "review_only", "profile_id": profile["id"], "slug": profile["slug"],
				"display_name": profile["display_name"], "primary_court": profile["primary_court"],
				"linked_cases": profile["links"], "raw_names": "", "only_attribution_cases": profile["only_attribution"]})
			count += 1
	return count


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
	"""Put the profiles back first, then their case links, then the alias rows (which need both profiles to exist)."""
	import json

	records = list(read_undo_file(path))
	for record in records:
		profile = record["profile"]
		db.execute(
			text("INSERT INTO judge_profiles (id, slug, display_name, normalized_name, primary_court, aliases) "
			"VALUES (:id, :slug, :display_name, :normalized_name, :primary_court, CAST(:aliases AS json)) ON CONFLICT DO NOTHING"),
			{**profile, "aliases": json.dumps(profile["aliases"])},
		)
	for record in records:
		for link in record["links"]:
			db.execute(
				text("INSERT INTO case_judge_profiles (id, case_id, judge_profile_id, raw_name) "
				"SELECT :id, :case_id, :profile_id, :raw_name WHERE EXISTS (SELECT 1 FROM cases WHERE id = :case_id) ON CONFLICT DO NOTHING"),
				{**link, "profile_id": record["profile"]["id"]},
			)
	for record in records:
		for alias in record["aliases"]:
			db.execute(
				text("INSERT INTO judge_profile_aliases (id, alias_profile_id, canonical_profile_id, source) "
				"SELECT :id, :alias_profile_id, :canonical_profile_id, :source "
				"WHERE EXISTS (SELECT 1 FROM judge_profiles WHERE id = :alias_profile_id) "
				"AND EXISTS (SELECT 1 FROM judge_profiles WHERE id = :canonical_profile_id) ON CONFLICT DO NOTHING"),
				alias,
			)
	db.commit()
	return len(records)


def print_report(junk: list[dict[str, Any]], mixed: list[dict[str, Any]], sample: int, review: list[dict[str, Any]] | None = None) -> None:
	import random
	from collections import Counter

	print(f"junk_judge_profiles={len(junk)} linked_cases={sum(p['cases'] for p in junk)}")
	for court, count in Counter(p["primary_court"] or "(none)" for p in junk).most_common():
		print(f"  {count:6d} profiles  {court}")
	print(f"{sample} random junk profiles (check them before applying):")
	for profile in random.Random(0).sample(junk, min(sample, len(junk))):
		print(f"  {profile['cases']:6d}  {profile['slug']}  {profile['display_name']!r}  raw={profile['raw_names'][:3]}")
	print("largest junk profiles:")
	for profile in junk[:5]:
		print(f"  {profile['cases']:6d}  {profile['slug']}  {profile['display_name']!r}")
	if review:
		print(f"review-only profiles (never deleted by this script): {len(review)} profiles, "
			f"{sum(p['links'] for p in review)} links, {sum(p['only_attribution'] for p in review)} decisions have no other judge link")
		for profile in review[:5]:
			print(f"  {profile['links']:6d} links, {profile['only_attribution']} sole  {profile['slug']}  {profile['display_name']!r}  {profile['primary_court']}")
	print(f"not deleted, mixed (some junk raw names beside real ones): {len(mixed)} profiles, "
		f"{sum(p['junk_cases'] for p in mixed)} linked cases carry a junk raw name")
	for profile in sorted(mixed, key=lambda p: -p["junk_cases"])[:5]:
		print(f"  {profile['junk_cases']:6d} of {profile['cases']}  {profile['slug']}  {profile['display_name']!r}")


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Save an undo file, then delete the junk profiles (default is a dry run).")
	parser.add_argument("--undo", type=Path, help="Put back the profiles saved in this undo file.")
	parser.add_argument("--undo-file", type=Path, help="Where --apply writes the undo file (default data/db_fix_backups/).")
	parser.add_argument("--expected-count", type=int, help="With --apply: stop unless exactly this many profiles are found.")
	parser.add_argument("--batch-size", type=int, default=200)
	parser.add_argument("--csv", type=Path, help="Write every junk profile and review-only profile to this new CSV file.")
	parser.add_argument("--sample", type=int, default=20, help="Random junk profiles to list in the dry run.")
	args = parser.parse_args(argv)
	with SessionLocal() as db:
		if args.undo:
			print(f"restored={restore(db, args.undo)} profiles from {args.undo}")
			return 0
		if not args.apply:
			db.execute(text("SET TRANSACTION READ ONLY"))
		mixed: list[dict[str, Any]] = []
		junk = find_junk_profiles(db, mixed)
		review = find_review_only(db)
		print_report(junk, mixed, args.sample, review)
		if args.csv:
			print(f"names_csv_rows={write_names_csv(args.csv, junk, review)} file: {args.csv}")
		if not args.apply:
			print("Dry run: nothing written. Add --apply --expected-count N to delete.")
			return 0
		if args.expected_count is None:
			parser.error("--apply needs --expected-count N (the junk_judge_profiles number the dry run printed)")
		if args.expected_count != len(junk):
			print(f"Expected {args.expected_count} but found {len(junk)}; nothing changed.")
			return 1
		undo_path = args.undo_file or default_undo_path("junk_judge_profiles")
		print(f"deleted={apply_deletes(db, junk, undo_path, args.batch_size)} undo file: {undo_path}")
		print("Undo with: python scripts/fix_junk_judge_profiles.py --undo", undo_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
