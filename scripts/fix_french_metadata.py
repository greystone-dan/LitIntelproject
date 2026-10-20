"""Re-read the judge, file number and outcome of French Federal Court / Court of Appeal decisions. Dry run by default.

French decisions (citation "CF" or "CAF") were read with English-only rules: wrong judge (the first name of the
panel), a file number with the next heading glued on, and no outcome. Since the French-decisions fix the current
extractor reads them. This script recomputes those fields from the stored text and writes them into
cases.metadata_json -> reader_extracted, for the French rows only, and only the keys listed below.

  python scripts/fix_french_metadata.py                                  # dry run: counts and 50 random old -> new
  python scripts/fix_french_metadata.py --apply --expected-count N       # save an undo file, then write
  python scripts/fix_french_metadata.py --undo data/db_fix_backups/french_metadata_<stamp>.jsonl

Keys touched: judge and docket (only when the stored one is the same file number with extra words after it).
Outcomes are NOT touched unless --include-outcomes is given: the outcome set (decision outcome, government role,
government outcome, case winner, case loser, outcome status), only for rows that have no decision outcome yet, so a
stored outcome is never overwritten. Do not use that flag until a fresh 35-decision check, not chosen by ruling
phrase, shows about 90% of the written French outcomes correct (see PR 592).
Backup first: this edits cases.metadata_json for the listed rows; the undo file holds the old values of every key.
Does not rebuild judge profiles: run backfill_judge_profiles.py separately, after checking the dry run.
"""

from __future__ import annotations

import argparse
import copy
import random
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select, text, update

from backend.database import Case, SessionLocal
from backend.metadata_outcomes import _derive_outcome_fields
from fc_ingest.document_scraper import _extract_metadata_with_quality
from scripts.fix_common import chunked, default_undo_path, read_undo_file, write_undo_file

OUTCOME_KEYS = ("decision outcome", "government role", "government outcome", "case winner", "case loser", "outcome status")
KEYS = ("judge", "docket", *OUTCOME_KEYS)

SELECT_SQL = text(
	"SELECT id, court, citation, metadata_json->'reader_extracted' AS extracted FROM cases "
	"WHERE id > :after AND court IN ('FC', 'FCA') AND citation ~ '\\m(CF|CAF)\\M' ORDER BY id LIMIT :limit"
)


def plan_row(row: dict[str, Any], full_text: str | None, include_outcomes: bool = False) -> dict[str, Any] | None:
	"""{key: (old, new)} for the keys that would change, or None when nothing changes."""
	if not full_text:
		return None
	old = row["extracted"] if isinstance(row["extracted"], dict) else {}
	found = _extract_metadata_with_quality(full_text)
	changes: dict[str, tuple[Any, Any]] = {}
	new_judge = " ".join(str(found.get("judge") or "").split()) or None
	if new_judge and new_judge != old.get("judge"):
		changes["judge"] = (old.get("judge"), new_judge)
	new_docket = " ".join(str(found.get("docket") or found.get("dossier") or "").split()) or None
	old_docket = old.get("docket")
	if new_docket and old_docket and old_docket != new_docket and str(old_docket).startswith(new_docket):
		changes["docket"] = (old_docket, new_docket)
	if include_outcomes and not old.get("decision outcome"):
		derived = _derive_outcome_fields(full_text, {**old, **{k: v for k, v in found.items() if not k.startswith("_")}})
		for key in OUTCOME_KEYS:
			if key in derived and derived[key][0] != old.get(key):
				changes[key] = (old.get(key), derived[key][0])
	return changes or None


def find_changes(db, batch_size: int, include_outcomes: bool = False) -> list[dict[str, Any]]:
	plan: list[dict[str, Any]] = []
	after = 0
	while True:
		rows = [dict(r) for r in db.execute(SELECT_SQL, {"after": after, "limit": batch_size}).mappings().all()]
		if not rows:
			return plan
		after = rows[-1]["id"]
		texts = dict(db.execute(select(Case.id, Case.full_text).where(Case.id.in_([r["id"] for r in rows]))).all())
		for row in rows:
			changes = plan_row(row, texts.get(row["id"]), include_outcomes)
			if changes:
				plan.append({"id": row["id"], "court": row["court"], "citation": row["citation"], "changes": changes})


def _set_keys(metadata: dict[str, Any] | None, values: dict[str, Any]) -> dict[str, Any]:
	meta = copy.deepcopy(metadata) if isinstance(metadata, dict) else {}
	extracted = dict(meta.get("reader_extracted")) if isinstance(meta.get("reader_extracted"), dict) else {}
	for key, value in values.items():
		if value is None:
			extracted.pop(key, None)
		else:
			extracted[key] = value
	meta["reader_extracted"] = extracted
	return meta


def _current(db, case_id: int) -> tuple[dict[str, Any] | None, dict[str, Any]]:
	metadata = db.scalar(select(Case.metadata_json).where(Case.id == case_id))
	extracted = metadata.get("reader_extracted") if isinstance(metadata, dict) else None
	return metadata, (extracted if isinstance(extracted, dict) else {})


def apply_plan(db, plan: list[dict[str, Any]], undo_path: Path, batch_size: int) -> int:
	records = ({"id": p["id"], "changes": {k: {"old": v[0], "new": v[1]} for k, v in p["changes"].items()}} for p in plan)
	if write_undo_file(undo_path, records) != len(plan):
		raise RuntimeError("undo file is incomplete; nothing changed")
	changed = 0
	for batch in chunked(plan, batch_size):
		for item in batch:
			metadata, current = _current(db, item["id"])
			if any(current.get(key) != old for key, (old, _) in item["changes"].items()):
				continue  # edited since the scan; leave it alone
			db.execute(update(Case).where(Case.id == item["id"]).values(
				metadata_json=_set_keys(metadata, {key: new for key, (_, new) in item["changes"].items()})))
			changed += 1
		db.commit()
	return changed


def undo(db, path: Path, batch_size: int) -> tuple[int, int]:
	records = list(read_undo_file(path))
	restored = skipped = 0
	for batch in chunked(records, batch_size):
		for item in batch:
			metadata, current = _current(db, item["id"])
			if any(current.get(key) != value["new"] for key, value in item["changes"].items()):
				skipped += 1  # changed again since the fix; do not overwrite
				continue
			db.execute(update(Case).where(Case.id == item["id"]).values(
				metadata_json=_set_keys(metadata, {key: value["old"] for key, value in item["changes"].items()})))
			restored += 1
		db.commit()
	return restored, skipped


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Save an undo file, then write (default is a dry run).")
	parser.add_argument("--undo", type=Path, help="Put back the old values saved in this undo file.")
	parser.add_argument("--undo-file", type=Path, help="Where --apply writes the undo file (default data/db_fix_backups/).")
	parser.add_argument("--expected-count", type=int, help="Required with --apply: the number of rows the dry run printed.")
	parser.add_argument("--include-outcomes", action="store_true", help="Also fill missing outcomes (held until the French outcome check passes).")
	parser.add_argument("--batch-size", type=int, default=500)
	parser.add_argument("--sample", type=int, default=50, help="Random old -> new rows to list in the dry run.")
	args = parser.parse_args(argv)
	if args.apply and args.expected_count is None:
		parser.error("--apply needs --expected-count N (the rows_to_change number the dry run printed)")
	with SessionLocal() as db:
		if args.undo:
			restored, skipped = undo(db, args.undo, args.batch_size)
			print(f"restored={restored} skipped_changed_since={skipped} from {args.undo}")
			return 0
		total = db.execute(text("SELECT count(*) FROM cases WHERE court IN ('FC', 'FCA') AND citation ~ '\\m(CF|CAF)\\M'")).scalar()
		plan = find_changes(db, args.batch_size, args.include_outcomes)
		print(f"french_decisions={total} rows_to_change={len(plan)}")
		per_key = Counter(key for p in plan for key in p["changes"])
		for key, count in per_key.most_common():
			print(f"  {count:6d}  {key}")
		outcomes = Counter(p["changes"]["decision outcome"][1] for p in plan if "decision outcome" in p["changes"])
		print(f"  new decision outcomes: {dict(outcomes)}")
		for p in random.Random(0).sample(plan, min(args.sample, len(plan))):
			shown = "; ".join(f"{k}: {str(v[0])[:28]!r} -> {str(v[1])[:28]!r}" for k, v in p["changes"].items())
			print(f"  case {p['id']} {p['court']} {p['citation']}: {shown}")
		if not args.apply:
			print("Dry run: nothing written. Read the sample, then add --apply --expected-count N.")
			return 0
		if args.expected_count != len(plan):
			print(f"Expected {args.expected_count} but found {len(plan)}; nothing changed.")
			return 1
		undo_path = args.undo_file or default_undo_path("french_metadata")
		changed = apply_plan(db, plan, undo_path, args.batch_size)
		print(f"fixed={changed} undo file: {undo_path}")
		print("Undo with: python scripts/fix_french_metadata.py --undo", undo_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
