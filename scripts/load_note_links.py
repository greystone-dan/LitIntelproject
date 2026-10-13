"""Load stored "possibly the same point" links between paragraph notes. Dry run by default.

Reads data/note_links/links.jsonl.gz: rows {citation_key, para, other_citation_key, other_para, score}. Each end is linked to the
library case with that exact citation (neutral citation written with underscores). A link is added only when both decisions are in
the library and both paragraph notes are already stored (run scripts/load_core150_layers.py first). Additive: existing links are
never updated or deleted.

  python scripts/load_note_links.py                  # dry run: counts, nothing written
  python scripts/load_note_links.py --apply          # write (live database: needs the go-ahead)
  python scripts/load_note_links.py --undo           # dry run of the undo
  python scripts/load_note_links.py --undo --apply   # remove only rows with this --source label

Undo by hand: DELETE FROM paragraph_note_links WHERE source = 'links-v1';  (or DROP TABLE paragraph_note_links).
Run `alembic upgrade head` first (0049 adds the table).
"""

from __future__ import annotations

import argparse
import gzip
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import delete, func, select

from backend.database import ParagraphNote, ParagraphNoteLink, SessionLocal
from scripts.load_core150_layers import KEY, resolve

DATA = PROJECT_ROOT / "data" / "note_links" / "links.jsonl.gz"
SOURCE = "links-v1"


def read_jsonl(path: Path) -> list[dict]:
	with gzip.open(path, "rt", encoding="utf-8") as handle:
		return [json.loads(line) for line in handle if line.strip()]


def _count(session, source: str | None = None) -> int:
	query = select(func.count()).select_from(ParagraphNoteLink)
	if source:
		query = query.where(ParagraphNoteLink.source == source)
	return session.execute(query).scalar_one()


def load(session, rows: list[dict], apply: bool, source: str = SOURCE) -> dict[str, int]:
	stats = {"file": len(rows), "before": _count(session), "skipped_bad_row": 0, "skipped_no_case": 0, "skipped_no_note": 0, "skipped_present": 0, "to_add": 0}
	keys = {r[k] for r in rows for k in ("citation_key", "other_citation_key") if isinstance(r.get(k), str)}
	ids = resolve(session, keys)
	notes = set(tuple(x) for x in session.execute(select(ParagraphNote.case_id, ParagraphNote.para).where(ParagraphNote.version == 1)).all())
	have = set(tuple(x) for x in session.execute(select(ParagraphNoteLink.case_id, ParagraphNoteLink.para, ParagraphNoteLink.other_case_id, ParagraphNoteLink.other_para)).all())
	todo = []
	for r in rows:
		if not (isinstance(r.get("score"), int) and isinstance(r.get("para"), int) and isinstance(r.get("other_para"), int)) or not KEY.match(str(r.get("citation_key"))):
			stats["skipped_bad_row"] += 1
			continue
		a, b = ids.get(r["citation_key"]), ids.get(r["other_citation_key"])
		if not a or not b or a == b:
			stats["skipped_no_case"] += 1
		elif (a, r["para"]) not in notes or (b, r["other_para"]) not in notes:
			stats["skipped_no_note"] += 1
		elif (a, r["para"], b, r["other_para"]) in have:
			stats["skipped_present"] += 1
		else:
			have.add((a, r["para"], b, r["other_para"]))
			todo.append(ParagraphNoteLink(case_id=a, para=r["para"], other_case_id=b, other_para=r["other_para"], score=r["score"], source=source))
	stats["to_add"] = len(todo)
	if apply:
		session.add_all(todo)
		session.commit()
		stats["after"] = _count(session)
	return stats


def undo(session, apply: bool, source: str = SOURCE) -> dict[str, int]:
	stats = {"before": _count(session), "to_remove": _count(session, source)}
	if apply:
		session.execute(delete(ParagraphNoteLink).where(ParagraphNoteLink.source == source))
		session.commit()
		stats["after"] = _count(session)
	return stats


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write (or, with --undo, remove).")
	parser.add_argument("--undo", action="store_true", help="Remove only rows with this source label.")
	parser.add_argument("--data", default=str(DATA), help="links.jsonl.gz to read.")
	parser.add_argument("--source", default=SOURCE, help="Source label written to (and undone from) paragraph_note_links.")
	args = parser.parse_args()
	with SessionLocal() as session:
		result = undo(session, args.apply, args.source) if args.undo else load(session, read_jsonl(Path(args.data)), args.apply, args.source)
	print(("UNDO " if args.undo else "LOAD ") + ("APPLIED " if args.apply else "DRY RUN ") + json.dumps(result))


if __name__ == "__main__":
	main()
