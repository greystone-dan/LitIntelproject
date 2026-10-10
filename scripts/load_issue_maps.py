"""Load the stored issue maps (data/issue_maps/issue_maps.jsonl.gz) into issue_maps and issue_map_questions. Dry run by default.

Additive only: it adds rows that are missing and never updates or deletes existing ones. Each row is linked to a
library case by the live case id in the file when that case exists, otherwise by an exact citation match.

  python scripts/load_issue_maps.py                 # dry run: counts, how many rows link to a case, nothing written
  python scripts/load_issue_maps.py --apply         # write (live database: needs the go-ahead)

Undo: DROP TABLE issue_map_questions; DROP TABLE issue_maps;   (or alembic downgrade 0044_refined_pinpoints)
Run `alembic upgrade head` first so the tables exist.
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

from sqlalchemy import func, select

from backend.database import Case, IssueMap, IssueMapQuestion, SessionLocal

DEFAULT_FILE = PROJECT_ROOT / "data" / "issue_maps" / "issue_maps.jsonl.gz"


def read_rows(path: Path) -> list[dict]:
	rows: list[dict] = []
	counts: dict[str, int] = {}
	with gzip.open(path, "rt", encoding="utf-8") as handle:
		for line in handle:
			if not line.strip():
				continue
			row = json.loads(line)
			key = row["source_key"]
			counts[key] = counts.get(key, 0) + 1
			row["issue_no"] = counts[key]
			rows.append(row)
	return rows


def resolve_case_ids(session, rows: list[dict]) -> dict[str, int | None]:
	"""source_key -> cases.id (live id from the file if it exists, else a single exact citation match)."""
	live_ids = {r["live_case_id"] for r in rows if r.get("live_case_id")}
	existing = set(session.execute(select(Case.id).where(Case.id.in_(live_ids))).scalars()) if live_ids else set()
	resolved: dict[str, int | None] = {}
	unresolved: dict[str, str] = {}
	for r in rows:
		key = r["source_key"]
		if key in resolved or key in unresolved:
			continue
		if r.get("live_case_id") in existing:
			resolved[key] = r["live_case_id"]
		elif r.get("citation"):
			unresolved[key] = r["citation"]
		else:
			resolved[key] = None
	for key, citation in unresolved.items():
		resolved[key] = _match_citation(session, citation)
	return resolved


def _match_citation(session, citation: str) -> int | None:
	"""One library case for a citation. File keys use underscores (2022_FC_728, MB0_00148); the library uses
	spaces for court citations and dashes for tribunal ids, so those spellings are tried too."""
	for candidate in dict.fromkeys([citation, citation.replace("_", " "), citation.replace("_", "-")]):
		ids = list(session.execute(select(Case.id).where(Case.citation == candidate).limit(2)).scalars())
		if len(ids) == 1:
			return ids[0]
	return None


def relink(session, apply: bool = False) -> dict[str, int]:
	"""Fill case_id on stored issues that have none, by citation. Only fills empty links; never changes or deletes."""
	todo = list(session.execute(select(IssueMap).where(IssueMap.case_id.is_(None))).scalars())
	found = {}
	for citation in {row.citation for row in todo if row.citation}:
		case_id = _match_citation(session, citation)
		if case_id:
			found[citation] = case_id
	fixable = [row for row in todo if row.citation in found]
	if apply:
		for row in fixable:
			row.case_id = found[row.citation]
		session.commit()
	return {"unlinked": len(todo), "linkable": len(fixable), "decisions_linkable": len(found)}


def load(session, rows: list[dict], apply: bool = False) -> dict[str, int]:
	"""Add the rows that are missing. Returns counts; writes only when apply is true."""
	stats = {
		"file_issues": len(rows),
		"before_issues": session.execute(select(func.count()).select_from(IssueMap)).scalar_one(),
		"before_questions": session.execute(select(func.count()).select_from(IssueMapQuestion)).scalar_one(),
	}
	have = set(tuple(k) for k in session.execute(select(IssueMap.source_key, IssueMap.issue_no)).all())
	case_ids = resolve_case_ids(session, rows)
	todo = [r for r in rows if (r["source_key"], r["issue_no"]) not in have]
	stats["to_add"] = len(todo)
	stats["to_add_linked"] = sum(1 for r in todo if case_ids.get(r["source_key"]))
	if not apply:
		return stats
	for r in todo:
		issue = IssueMap(
			source_key=r["source_key"],
			issue_no=r["issue_no"],
			case_id=case_ids.get(r["source_key"]),
			citation=r.get("citation"),
			court=r.get("court"),
			issue=r["issue"],
			text=r["text"],
			result=r["result"],
			result_para=r.get("result_para") or None,
			soften=r.get("soften"),
			result_paragraph=r.get("result_paragraph"),
		)
		session.add(issue)
		session.flush()
		for position, question in enumerate(r.get("questions") or []):
			session.add(IssueMapQuestion(issue_map_id=issue.id, position=position, question=question))
	session.commit()
	stats["after_issues"] = session.execute(select(func.count()).select_from(IssueMap)).scalar_one()
	stats["after_questions"] = session.execute(select(func.count()).select_from(IssueMapQuestion)).scalar_one()
	return stats


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write the missing rows.")
	parser.add_argument("--relink", action="store_true", help="Only fill missing case links on stored issues (use with --apply to write).")
	parser.add_argument("--file", default=str(DEFAULT_FILE), help="Issue-map file (jsonl, gzip).")
	args = parser.parse_args()

	if args.relink:
		with SessionLocal() as session:
			stats = relink(session, apply=args.apply)
		print(f"stored issues without a link: {stats['unlinked']}; can be linked: {stats['linkable']} ({stats['decisions_linkable']} decisions)")
		print("linked." if args.apply else "dry run: nothing written. Re-run with --apply to write.")
		return
	rows = read_rows(Path(args.file))
	with SessionLocal() as session:
		stats = load(session, rows, apply=args.apply)
	print(f"file: {stats['file_issues']} issues from {len({r['source_key'] for r in rows})} decisions")
	print(f"database before: {stats['before_issues']} issues, {stats['before_questions']} questions")
	print(f"to add: {stats['to_add']} issues ({stats['to_add_linked']} linked to a library case, {stats['to_add'] - stats['to_add_linked']} not linked)")
	if args.apply:
		print(f"database after: {stats['after_issues']} issues, {stats['after_questions']} questions")
	else:
		print("dry run: nothing written. Re-run with --apply to write.")


if __name__ == "__main__":
	main()
