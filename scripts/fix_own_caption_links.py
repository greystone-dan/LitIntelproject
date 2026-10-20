"""Unlink citation rows that resolved a decision's own caption to a different case (site review R6). Dry run by default.

Example: Baker v. Canada (case 35899) prints "Indexed as: Baker v. Canada". The bare name was stored as a
citation row and the title resolver (scripts/resolve_citation_targets.py) linked it to 2005 FCA 185 (case 36940),
another decision with the same caption, because it removes the source case from the candidates and then accepts
the one that is left. Fixed going forward in backend/citations.py (is_self_case_name_match) and in the resolver;
this script cleans the rows that already exist.

A row is a candidate when ALL of these hold (this is the exact selection):
  citation_kind IN ('case_name', 'case_short')
  AND target_case_id IS NOT NULL AND target_case_id <> source_case_id
  AND the row's text is the whole caption of the source case (same test the extractor now uses)
  AND (default) the first 6000 characters of the source text contain "Indexed as: <that caption>".
--any-own-caption drops the last condition (every bare mention of the source's own caption).

  python scripts/fix_own_caption_links.py                        # dry run: list candidates
  python scripts/fix_own_caption_links.py --apply --expected-count N   # save an undo file, then unlink
  python scripts/fix_own_caption_links.py --undo data/db_fix_backups/own_caption_links_<stamp>.jsonl

Apply sets target_case_id = NULL, unresolved = true, target_paragraph = NULL, target_chunk_id = NULL on the
listed rows only (the row is kept; nothing is deleted). Do not run scripts/resolve_citation_targets.py from an
older checkout afterwards: it would link them again. Afterwards recompute the cited-by numbers
(python scripts/recompute_citation_metrics.py --apply) and, for a target with paragraph links, rebuild
scripts/build_paragraph_cited_by.py for the source case.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text

from backend.citations import _is_own_full_caption
from backend.database import SessionLocal
from scripts.fix_common import chunked, default_undo_path, read_undo_file, write_undo_file

HEADER_CHARS = 6000

# Prefilter in SQL (same first four letters as the source title), the exact test is done in Python.
SELECT_SQL = text(
	"SELECT c.id, c.source_case_id, c.target_case_id, c.citation_kind, c.citation_text, c.normalized_citation, "
	"c.offset_start, c.offset_end, c.unresolved, c.target_paragraph, c.target_chunk_id, "
	"src.title AS source_title, src.citation AS source_citation, src.court AS source_court, "
	"tgt.title AS target_title, tgt.citation AS target_citation, "
	"substr(src.full_text, 1, :header) AS header "
	"FROM citations c JOIN cases src ON src.id = c.source_case_id JOIN cases tgt ON tgt.id = c.target_case_id "
	"WHERE c.citation_kind IN ('case_name', 'case_short') "
	"AND c.target_case_id IS NOT NULL AND c.target_case_id <> c.source_case_id "
	"AND lower(left(src.title, 4)) = lower(left(c.citation_text, 4)) "
	"AND c.id > :after ORDER BY c.id LIMIT :limit"
)
UNLINK_SQL = text(
	"UPDATE citations SET target_case_id = NULL, unresolved = TRUE, target_paragraph = NULL, target_chunk_id = NULL "
	"WHERE id = :id AND target_case_id = :target_case_id"
)
RESTORE_SQL = text(
	"UPDATE citations SET target_case_id = :target_case_id, unresolved = :unresolved, "
	"target_paragraph = :target_paragraph, target_chunk_id = :target_chunk_id "
	"WHERE id = :id AND target_case_id IS NULL"
)


def _alias(citation_text: str | None) -> str:
	head = re.split(r"\s*,\s*(?:at\s+)?para", citation_text or "", maxsplit=1, flags=re.IGNORECASE)[0]
	return " ".join(head.split())


def indexed_as_caption(header: str | None, citation_text: str | None) -> bool:
	"""True when the header has "Indexed as: <caption>" for this row's caption text."""
	tokens = re.findall(r"\w+", _alias(citation_text))
	if not tokens or not header:
		return False
	pattern = r"\W+".join(re.escape(token) for token in tokens)
	return re.search(rf"indexed\s+as\s*:?\s*{pattern}\b", header, re.IGNORECASE) is not None


def is_candidate(row: dict[str, Any], any_own_caption: bool = False) -> bool:
	if row["target_case_id"] is None or row["target_case_id"] == row["source_case_id"]:
		return False
	if not _is_own_full_caption(row["source_title"], _alias(row["citation_text"])):
		return False
	return any_own_caption or indexed_as_caption(row.get("header"), row["citation_text"])


def find_candidates(db, batch_size: int, any_own_caption: bool = False) -> list[dict[str, Any]]:
	found: list[dict[str, Any]] = []
	after = 0
	while True:
		rows = [dict(r) for r in db.execute(
			SELECT_SQL, {"header": HEADER_CHARS, "after": after, "limit": batch_size}
		).mappings().all()]
		if not rows:
			return found
		after = rows[-1]["id"]
		found.extend(r for r in rows if is_candidate(r, any_own_caption))


def undo_record(row: dict[str, Any]) -> dict[str, Any]:
	return {key: row[key] for key in ("id", "source_case_id", "target_case_id", "unresolved", "target_paragraph", "target_chunk_id")}


def apply_unlink(db, candidates: list[dict[str, Any]], undo_path: Path, batch_size: int) -> int:
	written = write_undo_file(undo_path, (undo_record(r) for r in candidates))
	if written != len(candidates):
		raise RuntimeError("undo file is incomplete; nothing changed")
	changed = 0
	for batch in chunked(candidates, batch_size):
		result = db.execute(UNLINK_SQL, [{"id": r["id"], "target_case_id": r["target_case_id"]} for r in batch])
		db.commit()
		changed += result.rowcount or 0
	return changed


def undo(db, path: Path, batch_size: int) -> int:
	rows = [
		{k: r[k] for k in ("id", "target_case_id", "unresolved", "target_paragraph", "target_chunk_id")}
		for r in read_undo_file(path)
	]
	restored = 0
	for batch in chunked(rows, batch_size):
		result = db.execute(RESTORE_SQL, list(batch))
		db.commit()
		restored += result.rowcount or 0
	return restored


def main(argv: list[str] | None = None) -> int:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Save an undo file, then unlink the rows (default is a dry run).")
	parser.add_argument("--undo", type=Path, help="Restore the links saved in this undo file.")
	parser.add_argument("--undo-file", type=Path, help="Where --apply writes the undo file (default data/db_fix_backups/).")
	parser.add_argument("--expected-count", type=int, help="With --apply: stop unless exactly this many candidates are found.")
	parser.add_argument("--any-own-caption", action="store_true", help='Do not require "Indexed as:" in the source header.')
	parser.add_argument("--batch-size", type=int, default=5000)
	parser.add_argument("--sample", type=int, default=50, help="Candidates to list in the dry run.")
	args = parser.parse_args(argv)
	if args.batch_size < 1:
		parser.error("--batch-size must be at least 1")

	with SessionLocal() as db:
		if args.undo:
			print(f"restored={undo(db, args.undo, args.batch_size)} from {args.undo}")
			return 0
		candidates = find_candidates(db, args.batch_size, args.any_own_caption)
		print(f"candidates={len(candidates)} (any_own_caption={args.any_own_caption})")
		for row in candidates[: args.sample]:
			print(f"  row {row['id']}: case {row['source_case_id']} {row['source_citation']} {row['source_title'][:50]!r} "
			      f"text={str(row['citation_text'])[:40]!r} -> case {row['target_case_id']} {row['target_citation']} "
			      f"{str(row['target_title'])[:50]!r}")
		if not args.apply:
			print("Dry run: nothing written. Check the list, then add --apply --expected-count N.")
			return 0
		if args.expected_count is not None and args.expected_count != len(candidates):
			print(f"Expected {args.expected_count} but found {len(candidates)}; nothing changed.")
			return 1
		undo_path = args.undo_file or default_undo_path("own_caption_links")
		changed = apply_unlink(db, candidates, undo_path, args.batch_size)
		print(f"unlinked={changed} undo file: {undo_path}")
		print("Next: python scripts/recompute_citation_metrics.py --apply (cited-by numbers of the old targets).")
		print("Undo with: python scripts/fix_own_caption_links.py --undo", undo_path)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
