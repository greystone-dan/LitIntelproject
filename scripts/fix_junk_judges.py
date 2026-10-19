"""Clear or replace junk judge values in cases.metadata_json -> reader_extracted -> judge. Dry run by default.

Why not just re-run scripts/backfill_fc_case_metadata.py: since PR 576 the extractor (fc_ingest/document_scraper.py,
_is_judge_junk) throws away court names, annex lines, counsel labels and rule lines, but that backfill only
overwrites a field when the new extraction HAS a value ("if not value: continue"). When the fixed extractor finds
no judge at all, the old junk value stays. It also only looks at the newest --limit FC/FCA decisions and has no
undo. This script touches only the `judge` key, only on rows whose stored judge is junk by the same test.

  python scripts/fix_junk_judges.py                            # dry run: counts by court, top junk strings, planned replacements
  python scripts/fix_junk_judges.py --apply --expected-count N      # save an undo file, then fix the rows
  python scripts/fix_junk_judges.py --undo data/db_fix_backups/junk_judges_<stamp>.jsonl

For each junk row the text is re-extracted with the current extractor. A usable judge replaces the junk; if
none is found the judge key is removed (so the case simply has no judge). --no-reextract only removes.
Backup first: this edits the cases table (metadata_json is rewritten for the listed rows only); the undo file
holds the old judge value of every row.

After --apply, judge pages only change once judge profiles are rebuilt: run
python scripts/backfill_judge_profiles.py (adds profiles for the new values; it does NOT delete old junk
profiles or case_judge_profiles links, which need a separate cleanup), and recompute any cached judge stats.
"""

from __future__ import annotations

import argparse
import copy
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select, text, update

from backend.database import Case, SessionLocal
from fc_ingest.document_scraper import _extract_metadata_with_quality, _is_judge_junk
from scripts.fix_common import chunked, default_undo_path, read_undo_file, write_undo_file

SELECT_SQL = text(
	"SELECT id, court, citation, metadata_json->'reader_extracted'->>'judge' AS judge FROM cases "
	"WHERE id > :after AND metadata_json->'reader_extracted'->>'judge' IS NOT NULL ORDER BY id LIMIT :limit"
)


def is_junk_judge(value: Any) -> bool:
	"""Same test the extractor uses: the first non-empty line (or the whole value) is junk."""
	if not value:
		return False
	lines = [line.strip() for line in str(value).splitlines() if line.strip()]
	return bool(lines) and (_is_judge_junk(lines[0]) or _is_judge_junk(" ".join(lines)))


def find_junk_rows(db, batch_size: int) -> list[dict[str, Any]]:
	found: list[dict[str, Any]] = []
	after = 0
	while True:
		rows = [dict(r) for r in db.execute(SELECT_SQL, {"after": after, "limit": batch_size}).mappings().all()]
		if not rows:
			return found
		after = rows[-1]["id"]
		found.extend(r for r in rows if is_junk_judge(r["judge"]))


def new_judge_for(full_text: str | None) -> str | None:
	"""The judge the current extractor finds in this text, or None (also None when it is itself junk)."""
	if not full_text:
		return None
	judge = _extract_metadata_with_quality(full_text).get("judge")
	judge = " ".join(str(judge).split()) if judge else None
	return None if not judge or is_junk_judge(judge) else judge


def plan_changes(db, junk_rows: list[dict[str, Any]], reextract: bool, batch_size: int) -> list[dict[str, Any]]:
	"""Add `new_judge` to each junk row (None means remove the key)."""
	plan: list[dict[str, Any]] = []
	for batch in chunked(junk_rows, batch_size):
		texts = {}
		if reextract:
			ids = [r["id"] for r in batch]
			texts = dict(db.execute(select(Case.id, Case.full_text).where(Case.id.in_(ids))).all())
		for row in batch:
			plan.append({**row, "new_judge": new_judge_for(texts.get(row["id"])) if reextract else None})
	return plan


def _set_judge(metadata: dict[str, Any] | None, judge: str | None) -> dict[str, Any]:
	meta = copy.deepcopy(metadata) if isinstance(metadata, dict) else {}
	extracted = meta.get("reader_extracted")
	extracted = dict(extracted) if isinstance(extracted, dict) else {}
	if judge is None:
		extracted.pop("judge", None)
	else:
		extracted["judge"] = judge
	meta["reader_extracted"] = extracted
	return meta


def _current(db, case_id: int) -> tuple[dict[str, Any] | None, Any]:
	metadata = db.scalar(select(Case.metadata_json).where(Case.id == case_id))
	extracted = metadata.get("reader_extracted") if isinstance(metadata, dict) else None
	return metadata, (extracted.get("judge") if isinstance(extracted, dict) else None)


def apply_plan(db, plan: list[dict[str, Any]], undo_path: Path, batch_size: int) -> int:
	records = ({"id": p["id"], "old_judge": p["judge"], "new_judge": p["new_judge"]} for p in plan)
	if write_undo_file(undo_path, records) != len(plan):
		raise RuntimeError("undo file is incomplete; nothing changed")
	changed = 0
	for batch in chunked(plan, batch_size):
		for item in batch:
			metadata, current = _current(db, item["id"])
			if current != item["judge"]:
				continue  # edited since the scan; leave it alone
			db.execute(update(Case).where(Case.id == item["id"]).values(
				metadata_json=_set_judge(metadata, item["new_judge"])))
			changed += 1
		db.commit()
	return changed


def undo(db, path: Path, batch_size: int) -> tuple[int, int]:
	records = list(read_undo_file(path))
	restored = skipped = 0
	for batch in chunked(records, batch_size):
		for item in batch:
			metadata, current = _current(db, item["id"])
			if current != item["new_judge"]:
				skipped += 1  # changed again since the fix; do not overwrite
				continue
			db.execute(update(Case).where(Case.id == item["id"]).values(
				metadata_json=_set_judge(metadata, item["old_judge"])))
			restored += 1
		db.commit()
	return restored, skipped


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Save an undo file, then fix the rows (default is a dry run).")
	parser.add_argument("--undo", type=Path, help="Put back the judge values saved in this undo file.")
	parser.add_argument("--undo-file", type=Path, help="Where --apply writes the undo file (default data/db_fix_backups/).")
	parser.add_argument("--expected-count", type=int, help="With --apply: stop unless exactly this many junk rows are found.")
	parser.add_argument("--no-reextract", action="store_true", help="Only remove junk judges; do not look for a replacement.")
	parser.add_argument("--batch-size", type=int, default=500)
	parser.add_argument("--sample", type=int, default=20, help="Planned changes to list in the dry run.")
	args = parser.parse_args(argv)
	if args.batch_size < 1:
		parser.error("--batch-size must be at least 1")

	with SessionLocal() as db:
		if args.undo:
			restored, skipped = undo(db, args.undo, args.batch_size)
			print(f"restored={restored} skipped_changed_since={skipped} from {args.undo}")
			print("Re-run scripts/backfill_judge_profiles.py if judge profiles were rebuilt after the fix.")
			return 0
		junk = find_junk_rows(db, 5000)
		print(f"junk_judge_rows={len(junk)}")
		for court, count in Counter(r["court"] for r in junk).most_common():
			print(f"  {count:7d}  {court}")
		for value, count in Counter(" ".join(str(r["judge"]).split())[:60] for r in junk).most_common(15):
			print(f"  {count:7d}  junk value {value!r}")
		plan = plan_changes(db, junk, not args.no_reextract, args.batch_size)
		replaced = sum(1 for p in plan if p["new_judge"])
		print(f"planned: replace={replaced} remove={len(plan) - replaced}")
		for p in plan[: args.sample]:
			print(f"  case {p['id']} {p['court']} {p['citation']}: {str(p['judge'])[:40]!r} -> {p['new_judge']!r}")
		if not args.apply:
			print("Dry run: nothing written. Add --apply --expected-count N to fix.")
			return 0
		if args.expected_count is not None and args.expected_count != len(plan):
			print(f"Expected {args.expected_count} but found {len(plan)}; nothing changed.")
			return 1
		undo_path = args.undo_file or default_undo_path("junk_judges")
		changed = apply_plan(db, plan, undo_path, args.batch_size)
		print(f"fixed={changed} undo file: {undo_path}")
		print("Next: python scripts/backfill_judge_profiles.py (new judge values); old junk profiles need a separate cleanup.")
		print("Undo with: python scripts/fix_junk_judges.py --undo", undo_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
