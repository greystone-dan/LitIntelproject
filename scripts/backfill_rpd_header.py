"""Fix the panel member and place of hearing stored for Refugee Protection Division decisions. Dry run by default.

The old extractor left RPD decision makers blank and let "place of hearing" run on through the cover page.
This re-reads those two fields from the cover page (`backend.metadata._rpd_header_fields`) and updates only
`metadata_json -> reader_extracted -> judge` and `-> place of hearing` on RPD cases.

  python scripts/backfill_rpd_header.py --limit 20           # dry run: print before/after for 20 cases
  python scripts/backfill_rpd_header.py --apply              # write (needs Daniel's go for the live database)
  python scripts/backfill_rpd_header.py --revert-file undo.json   # put the old values back
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import select
from sqlalchemy.orm.attributes import flag_modified

from backend.database import Case, SessionLocal
from backend.metadata import _rpd_header_fields

FIELDS = ("judge", "place of hearing")


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write the changes.")
	parser.add_argument("--limit", type=int, default=0, help="Stop after this many changed cases (0 = all).")
	parser.add_argument("--undo-file", default="rpd_header_undo.json", help="Where --apply saves the old values.")
	parser.add_argument("--revert-file", help="Restore old values from a file written by --apply.")
	args = parser.parse_args()

	with SessionLocal() as session:
		if args.revert_file:
			undo = json.loads(Path(args.revert_file).read_text(encoding="utf-8"))
			for case_id, old in undo.items():
				case = session.get(Case, int(case_id))
				if case is None:
					continue
				extracted = dict((case.metadata_json or {}).get("reader_extracted") or {})
				for field in FIELDS:
					if old.get(field) is None:
						extracted.pop(field, None)
					else:
						extracted[field] = old[field]
				case.metadata_json = {**(case.metadata_json or {}), "reader_extracted": extracted}
				flag_modified(case, "metadata_json")
			session.commit()
			print(f"Restored {len(undo)} cases.")
			return

		undo: dict[int, dict[str, str | None]] = {}
		changed = 0
		scanned = 0
		last_id = 0
		while True:
			rows = list(
				session.scalars(
					select(Case).where(Case.court == "RPD", Case.id > last_id).order_by(Case.id).limit(200)
				)
			)
			if not rows:
				break
			for case in rows:
				last_id = case.id
				scanned += 1
				new = _rpd_header_fields(case.full_text or "")
				extracted = dict((case.metadata_json or {}).get("reader_extracted") or {})
				diff = {f: v for f, v in new.items() if f in FIELDS and extracted.get(f) != v}
				if not diff:
					continue
				changed += 1
				if changed <= 20 or not args.apply:
					for field, value in diff.items():
						before = str(extracted.get(field))[:70].replace("\n", " / ")
						print(f"{case.id} {case.citation} {field}: {before!r} -> {value!r}")
				if args.apply:
					undo[case.id] = {f: extracted.get(f) for f in diff}
					extracted.update(diff)
					case.metadata_json = {**(case.metadata_json or {}), "reader_extracted": extracted}
					flag_modified(case, "metadata_json")
				if args.limit and changed >= args.limit:
					break
			if args.apply:
				session.commit()
			if args.limit and changed >= args.limit:
				break
		if args.apply:
			Path(args.undo_file).write_text(json.dumps(undo), encoding="utf-8")
		print(f"Scanned {scanned} RPD cases, {changed} {'updated' if args.apply else 'would change'}.")
		if not args.apply:
			print("Dry run: nothing written. Add --apply to write.")


if __name__ == "__main__":
	main()
