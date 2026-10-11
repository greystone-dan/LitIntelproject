"""Load the whose-position tag files (one case_<id>.json per decision) into paragraph_positions. Dry run by default.

Additive only: it adds a row for each decision that has none and never updates or deletes existing rows. Files whose
decision is not in the library are skipped and counted.

  python scripts/load_position_tags.py --dir data/position_learned            # dry run: counts, nothing written
  python scripts/load_position_tags.py --dir data/position_learned --apply    # write (live database: needs the go-ahead)

Undo: DROP TABLE paragraph_positions;   (or alembic downgrade 0045_issue_maps)
Run `alembic upgrade head` first so the table exists. Reading the tags in the reader still needs ILIT_LEARNED_POSITIONS=1.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import func, select

from backend.database import Case, ParagraphPosition, SessionLocal

DEFAULT_DIR = PROJECT_ROOT / "data" / "position_learned"
BATCH = 500


def read_file(path: Path) -> dict | None:
	"""One tag file as a row dict, or None when it is unreadable or has no paragraphs."""
	try:
		stored = json.loads(path.read_text(encoding="utf-8"))
		case_id = int(stored.get("case_id") or path.stem.split("_")[1])
	except (OSError, ValueError, IndexError):
		return None
	paragraphs = stored.get("paragraphs") or {}
	if not paragraphs:
		return None
	tagger = str((stored.get("source") or {}).get("tagger") or "unknown")[:40]
	return {"case_id": case_id, "tagger": tagger, "paragraph_count": len(paragraphs), "paragraphs": paragraphs}


def _count(session) -> int:
	return session.execute(select(func.count()).select_from(ParagraphPosition)).scalar_one()


def load(session, directory: Path, apply: bool = False, limit: int = 0) -> dict[str, int]:
	"""Add the decisions that are missing. Returns counts; writes only when apply is true."""
	paths = sorted(directory.glob("case_*.json"))
	if limit:
		paths = paths[:limit]
	stats = {"files": len(paths), "before": _count(session), "unreadable": 0, "not_in_library": 0, "already_loaded": 0, "to_add": 0, "paragraphs_to_add": 0}
	have = set(session.execute(select(ParagraphPosition.case_id)).scalars())
	for start in range(0, len(paths), BATCH):
		rows = []
		for path in paths[start : start + BATCH]:
			row = read_file(path)
			if row is None:
				stats["unreadable"] += 1
			elif row["case_id"] in have:
				stats["already_loaded"] += 1
			else:
				rows.append(row)
		known = set(session.execute(select(Case.id).where(Case.id.in_([r["case_id"] for r in rows]))).scalars()) if rows else set()
		for row in rows:
			if row["case_id"] not in known:
				stats["not_in_library"] += 1
				continue
			stats["to_add"] += 1
			stats["paragraphs_to_add"] += row["paragraph_count"]
			if apply:
				session.add(ParagraphPosition(**row))
				have.add(row["case_id"])
		if apply:
			session.commit()
	stats["after"] = _count(session) if apply else stats["before"]
	return stats


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write the missing rows.")
	parser.add_argument("--dir", default=str(DEFAULT_DIR), help="Folder of case_<id>.json tag files.")
	parser.add_argument("--limit", type=int, default=0, help="Only the first N files (for a trial).")
	args = parser.parse_args()
	with SessionLocal() as session:
		stats = load(session, Path(args.dir), apply=args.apply, limit=args.limit)
	print(f"files: {stats['files']} ({stats['unreadable']} unreadable, {stats['not_in_library']} not in the library, {stats['already_loaded']} already loaded)")
	print(f"database before: {stats['before']} decisions")
	print(f"to add: {stats['to_add']} decisions, {stats['paragraphs_to_add']} paragraphs")
	if args.apply:
		print(f"database after: {stats['after']} decisions")
	else:
		print("dry run: nothing written. Re-run with --apply to write.")


if __name__ == "__main__":
	main()
