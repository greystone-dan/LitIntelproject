"""Load stored case frames (one JSON file per decision) into case_frames. Dry run by default.

Additive only: it adds frames that are missing and never updates or deletes existing ones. A file is named
<COURT>_<case id>.json (for example FC_1445.json) and holds the frame with "id" inside. A frame is skipped when
its case does not exist, its "id" does not match the file name, or it fails the text-match check (a frame
written for a different decision).

  python scripts/load_case_frames.py DIR                # dry run: counts, nothing written
  python scripts/load_case_frames.py DIR --apply        # write (live database: needs the go-ahead)

Undo: DROP TABLE case_frames;   (or alembic downgrade 0046_paragraph_positions)
Run `alembic upgrade head` first so the table exists.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import func, select

from backend.case_frame_plus import frame_matches_text
from backend.database import Case, CaseFrame, SessionLocal

NAME = re.compile(r"^([A-Z]+)_(\d+)$")


def read_frames(folder: Path) -> list[tuple[int, dict, str]]:
	"""(case id, frame, problem) for each file; problem is '' when the file is usable."""
	rows = []
	for path in sorted(folder.glob("*.json")):
		match = NAME.match(path.stem)
		if not match:
			continue
		case_id = int(match.group(2))
		try:
			frame = json.loads(path.read_text(encoding="utf-8"))
		except ValueError:
			rows.append((case_id, {}, "unreadable"))
			continue
		problem = "" if isinstance(frame, dict) and frame.get("id") == path.stem else "id_mismatch"
		rows.append((case_id, frame if isinstance(frame, dict) else {}, problem))
	return rows


def load(session, rows: list[tuple[int, dict, str]], source: str, version: int = 1, apply: bool = False) -> dict[str, int]:
	stats = {
		"files": len(rows),
		"before": session.execute(select(func.count()).select_from(CaseFrame)).scalar_one(),
		"skipped_bad_file": 0,
		"skipped_no_case": 0,
		"skipped_guard": 0,
		"skipped_present": 0,
		"to_add": 0,
	}
	have = set(session.execute(select(CaseFrame.case_id).where(CaseFrame.version == version)).scalars())
	texts = {c.id: c.full_text for c in session.execute(select(Case).where(Case.id.in_([r[0] for r in rows]))).scalars()}
	todo = []
	for case_id, frame, problem in rows:
		if problem:
			stats["skipped_bad_file"] += 1
		elif case_id not in texts:
			stats["skipped_no_case"] += 1
		elif case_id in have:
			stats["skipped_present"] += 1
		elif not frame_matches_text(frame, texts[case_id] or ""):
			stats["skipped_guard"] += 1
		else:
			todo.append((case_id, frame))
	stats["to_add"] = len(todo)
	if not apply:
		return stats
	for case_id, frame in todo:
		session.add(CaseFrame(case_id=case_id, version=version, frame=frame, source=source))
	session.commit()
	stats["after"] = session.execute(select(func.count()).select_from(CaseFrame)).scalar_one()
	return stats


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("folder", help="Folder of <COURT>_<id>.json frame files.")
	parser.add_argument("--apply", action="store_true", help="Write the missing frames.")
	parser.add_argument("--source", default="haiku-v3", help="Label stored with each frame.")
	args = parser.parse_args()
	with SessionLocal() as session:
		stats = load(session, read_frames(Path(args.folder)), args.source, apply=args.apply)
	for key, value in stats.items():
		print(f"{key}: {value}")
	if not args.apply:
		print("Dry run: nothing written. Add --apply to write.")


if __name__ == "__main__":
	main()
