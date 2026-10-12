"""Load the three stored layers for the 150 core Federal Court decisions: case frames, issue maps, paragraph notes.
Dry run by default.

Reads data/core150/{frames,issue_maps,paragraph_notes}.jsonl.gz. Each row is keyed by the neutral citation written
with underscores (2005_FC_1103) and linked to the library case with that exact citation. Additive only: it adds rows
that are missing and never updates or deletes existing ones.

  python scripts/load_core150_layers.py                       # dry run: counts per layer, nothing written
  python scripts/load_core150_layers.py --apply               # write (live database: needs the go-ahead)
  python scripts/load_core150_layers.py --undo                # dry run of the undo: what would be removed
  python scripts/load_core150_layers.py --undo --apply        # remove only the rows this script added

Skipped, and counted in the output: a citation with no single library case; a case that already has the layer
(frames at this version, any issue map, any notes at this version); a frame that fails the text-match check; a case
whose notes do not line up with its paragraphs (the first words of a note's paragraph must be found in the stored
text for at least --min-match of the notes).

Undo also works by hand: DELETE FROM case_frames WHERE source = 'core150-haiku-v3';
DELETE FROM paragraph_notes WHERE source = 'core150-v12'; DELETE FROM issue_maps WHERE source_key ~ '^[0-9]{4}_[A-Z]+_[0-9]+$';
Run `alembic upgrade head` first (0048 adds paragraph_notes and the new issue_maps columns).
"""

from __future__ import annotations

import argparse
import gzip
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import delete, func, select

from backend.case_frame_plus import frame_matches_text
from backend.database import Case, CaseFrame, IssueMap, ParagraphNote, SessionLocal
from scripts.load_issue_maps import _match_citation

DATA = PROJECT_ROOT / "data" / "core150"
FRAME_SOURCE = "core150-haiku-v3"
NOTE_SOURCE = "core150-v12"
KEY = re.compile(r"^\d{4}_[A-Z]+_\d+$")
START_CHARS = 50


def read_jsonl(path: Path) -> list[dict]:
	with gzip.open(path, "rt", encoding="utf-8") as handle:
		return [json.loads(line) for line in handle if line.strip()]


def squash(text: str) -> str:
	return re.sub(r"\s+", " ", text or "").strip()


def resolve(session, keys) -> dict[str, int | None]:
	return {k: (_match_citation(session, k) if KEY.match(k) else None) for k in sorted(set(keys))}


def _count(session, model) -> int:
	return session.execute(select(func.count()).select_from(model)).scalar_one()


def load_frames(session, rows: list[dict], ids: dict[str, int | None], apply: bool) -> dict[str, int]:
	stats = {"file": len(rows), "before": _count(session, CaseFrame), "skipped_no_case": 0, "skipped_present": 0, "skipped_guard": 0, "to_add": 0}
	have = set(session.execute(select(CaseFrame.case_id).where(CaseFrame.version == 1)).scalars())
	cases = {i: c for i, c in session.execute(select(Case.id, Case.full_text).where(Case.id.in_([v for v in ids.values() if v]))).all()}
	todo = []
	for row in rows:
		case_id = ids.get(row["citation_key"])
		if not case_id:
			stats["skipped_no_case"] += 1
		elif case_id in have:
			stats["skipped_present"] += 1
		elif not frame_matches_text(row["frame"], cases.get(case_id) or ""):
			stats["skipped_guard"] += 1
		else:
			todo.append((case_id, row["frame"]))
	stats["to_add"] = len(todo)
	if apply:
		for case_id, frame in todo:
			session.add(CaseFrame(case_id=case_id, version=1, frame=frame, source=FRAME_SOURCE))
		session.commit()
		stats["after"] = _count(session, CaseFrame)
	return stats


def load_issue_maps(session, rows: list[dict], ids: dict[str, int | None], apply: bool) -> dict[str, int]:
	stats = {"file": len(rows), "before": _count(session, IssueMap), "skipped_no_case": 0, "skipped_case_has_map": 0, "to_add": 0, "cases_to_add": 0}
	linked = [v for v in ids.values() if v]
	has_map = set(session.execute(select(IssueMap.case_id).where(IssueMap.case_id.in_(linked)).distinct()).scalars()) if linked else set()
	have = set(tuple(k) for k in session.execute(select(IssueMap.source_key, IssueMap.issue_no)).all())
	todo, cases = [], set()
	for row in rows:
		case_id = ids.get(row["citation_key"])
		if not case_id:
			stats["skipped_no_case"] += 1
		elif case_id in has_map or (row["source_key"], row["issue_no"]) in have:
			stats["skipped_case_has_map"] += 1
		else:
			todo.append((case_id, row))
			cases.add(case_id)
	stats["to_add"], stats["cases_to_add"] = len(todo), len(cases)
	if apply:
		for case_id, r in todo:
			position = r["applicant_position"].strip()
			session.add(
				IssueMap(
					source_key=r["source_key"],
					issue_no=r["issue_no"],
					case_id=case_id,
					citation=r["citation_key"],
					court=r.get("court"),
					issue=r["issue"],
					# The search text is the issue plus the applicant's position, as in the earlier stored maps.
					text=(r["issue"] + " " + position).strip(),
					result=r["result"],
					result_para=r.get("result_para") or None,
					result_paragraph=r.get("result_quote") or None,
					applicant_position=position or None,
					respondent_position=r["respondent_position"].strip() or None,
					review_flags=r.get("review_flags") or None,
				)
			)
		session.commit()
		stats["after"] = _count(session, IssueMap)
	return stats


def load_notes(session, rows: list[dict], ids: dict[str, int | None], apply: bool, min_match: float) -> dict[str, int]:
	stats = {"file": len(rows), "before": _count(session, ParagraphNote), "skipped_no_case": 0, "cases_skipped_present": 0, "cases_skipped_misaligned": 0, "to_add": 0, "cases_to_add": 0}
	by_case: dict[str, list[dict]] = defaultdict(list)
	for row in rows:
		by_case[row["citation_key"]].append(row)
	linked = [v for v in ids.values() if v]
	have = set(session.execute(select(ParagraphNote.case_id).where(ParagraphNote.version == 1).distinct()).scalars())
	texts = {i: squash(t) for i, t in session.execute(select(Case.id, Case.full_text).where(Case.id.in_(linked))).all()}
	todo: list[tuple[int, dict]] = []
	for key, notes in by_case.items():
		case_id = ids.get(key)
		if not case_id:
			stats["skipped_no_case"] += len(notes)
		elif case_id in have:
			stats["cases_skipped_present"] += 1
		else:
			text = texts.get(case_id, "")
			found = sum(1 for n in notes if n["para_start"][:START_CHARS] and n["para_start"][:START_CHARS] in text)
			if notes and found / len(notes) < min_match:
				stats["cases_skipped_misaligned"] += 1
				continue
			todo += [(case_id, n) for n in notes]
			stats["cases_to_add"] += 1
	stats["to_add"] = len(todo)
	if apply:
		for case_id, n in todo:
			session.add(ParagraphNote(case_id=case_id, para=n["para"], version=1, note=n["note"], source=NOTE_SOURCE))
		session.commit()
		stats["after"] = _count(session, ParagraphNote)
	return stats


def undo(session, issue_keys: set[str], apply: bool) -> dict[str, int]:
	counts = {
		"case_frames": session.execute(select(func.count()).select_from(CaseFrame).where(CaseFrame.source == FRAME_SOURCE)).scalar_one(),
		"paragraph_notes": session.execute(select(func.count()).select_from(ParagraphNote).where(ParagraphNote.source == NOTE_SOURCE)).scalar_one(),
		"issue_maps": session.execute(select(func.count()).select_from(IssueMap).where(IssueMap.source_key.in_(issue_keys))).scalar_one(),
	}
	if apply:
		session.execute(delete(CaseFrame).where(CaseFrame.source == FRAME_SOURCE))
		session.execute(delete(ParagraphNote).where(ParagraphNote.source == NOTE_SOURCE))
		session.execute(delete(IssueMap).where(IssueMap.source_key.in_(issue_keys)))
		session.commit()
	return counts


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write (or, with --undo, remove).")
	parser.add_argument("--undo", action="store_true", help="Remove only what this script added.")
	parser.add_argument("--data", default=str(DATA), help="Folder holding the three .jsonl.gz files.")
	parser.add_argument("--min-match", type=float, default=0.9, help="Share of a case's notes whose paragraph start must be found in the stored text.")
	args = parser.parse_args()
	folder = Path(args.data)
	frames, issues, notes = (read_jsonl(folder / f"{n}.jsonl.gz") for n in ("frames", "issue_maps", "paragraph_notes"))
	with SessionLocal() as session:
		if args.undo:
			counts = undo(session, {r["source_key"] for r in issues}, args.apply)
			print(("removed: " if args.apply else "would remove: ") + ", ".join(f"{v} {k}" for k, v in counts.items()))
			if not args.apply:
				print("Dry run: nothing removed. Add --apply to remove.")
			return
		ids = resolve(session, [r["citation_key"] for r in frames + issues + notes])
		print(f"decisions in files: {len(ids)}; found in the library: {sum(1 for v in ids.values() if v)}")
		missing = [k for k, v in ids.items() if not v]
		for key in missing[:20]:
			print(f"  not found: {key}")
		if len(missing) > 20:
			print(f"  ... and {len(missing) - 20} more not found")
		layers = (
			("case frames", load_frames(session, frames, ids, args.apply)),
			("issue maps", load_issue_maps(session, issues, ids, args.apply)),
			("paragraph notes", load_notes(session, notes, ids, args.apply, args.min_match)),
		)
		for name, stats in layers:
			print(f"\n{name}")
			for key, value in stats.items():
				print(f"  {key}: {value}")
	print("\nwritten." if args.apply else "\nDry run: nothing written. Add --apply to write.")


if __name__ == "__main__":
	main()
