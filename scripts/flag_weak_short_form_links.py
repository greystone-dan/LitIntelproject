"""Find (and optionally unlink) live short-form citations that point at the wrong case.

Pass one anchored many capitalised common words ("Lake", "Bank", "Council", "Quebec") to a nearby full
citation, and the resolver then linked those rows to the anchored case, so cited-by counts on the live site include
links that are not citations of that case. This script re-judges every LINKED short-form row with the same rules the
refinement uses (`backend/citation_refine/short_forms.py`) plus one more: the alias must appear as whole words in the
linked case's own title.

DRY RUN BY DEFAULT: it only reads, prints counts by reason, and writes the suspect rows to a CSV for review.

    python scripts/flag_weak_short_form_links.py --backup logs/weak_links.csv                  # dry run
    python scripts/flag_weak_short_form_links.py --backup logs/weak_links.csv --apply          # unlink the suspects
    python scripts/flag_weak_short_form_links.py --revert-from logs/weak_links.csv --apply     # put the links back

`--apply` sets `target_case_id` to NULL and `unresolved` to true on the suspect rows only (the backup CSV holds each
row's id and previous target and is written BEFORE any change). Cited-by counts and paragraph cited-by data derive from
these links and need their usual recompute afterwards; nothing here recomputes them.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

from sqlalchemy import select, update

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.citation_refine.models import RefinedCitation
from backend.citation_refine.short_forms import _words, alias_of, is_weak_short_form
from backend.database import Case, Citation, SessionLocal

BACKUP_FIELDS = ["id", "source_case_id", "previous_target_case_id", "reason", "citation_text", "target_title"]


def alias_in_title(alias: str, title: str | None) -> bool:
	words, tokens = _words(alias), _words(title or "")
	if not words or not tokens:
		return True  # nothing to compare: do not flag
	return any(tokens[start : start + len(words)] == words for start in range(len(tokens) - len(words) + 1))


def judge(citation_text: str | None, normalized: str | None, target_title: str | None) -> str | None:
	"""Reason this linked short form is suspect, or None."""
	row = RefinedCitation(
		kind="case_short", citation_text=citation_text or "", normalized_citation=normalized or "", offset_start=0,
		offset_end=1, step="pass1", action="kept", confidence=0.8,
	)
	if is_weak_short_form(row):
		return "weak_short_form"
	if not alias_in_title(alias_of(row), target_title):
		return "alias_not_in_target_title"
	return None


def find_suspects(session, limit: int | None, batch_size: int):
	query = (
		select(Citation.id, Citation.source_case_id, Citation.target_case_id, Citation.citation_text, Citation.normalized_citation, Case.title)
		.join(Case, Case.id == Citation.target_case_id)
		.where(Citation.citation_kind == "case_short", Citation.target_case_id.is_not(None))
		.order_by(Citation.id)
	)
	seen = 0
	for row in session.execute(query).yield_per(batch_size):
		if limit is not None and seen >= limit:
			return
		seen += 1
		reason = judge(row.citation_text, row.normalized_citation, row.title)
		yield seen, row, reason


def main(argv: list[str] | None = None) -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Write changes. Without it nothing is written.")
	parser.add_argument("--backup", type=Path, default=None, help="CSV of suspect rows (written before any change).")
	parser.add_argument("--revert-from", type=Path, default=None, help="Restore target_case_id from a backup CSV.")
	parser.add_argument("--limit", type=int, default=None, help="Inspect at most this many linked short-form rows.")
	parser.add_argument("--batch-size", type=int, default=20_000)
	parser.add_argument(
		"--reasons",
		default="weak_short_form",
		help="Comma list of reasons to act on (default weak_short_form, the high-precision rule; alias_not_in_target_title is "
		"about half real errors and is only counted unless named here).",
	)
	parser.add_argument("--examples", type=int, default=0, help="Print this many random suspect examples (with their reason).")
	args = parser.parse_args(argv)

	with SessionLocal() as session:
		if args.revert_from is not None:
			with args.revert_from.open(encoding="utf-8", newline="") as handle:
				rows = list(csv.DictReader(handle))
			if args.apply:
				for start in range(0, len(rows), 5_000):
					for item in rows[start : start + 5_000]:
						session.execute(
							update(Citation)
							.where(Citation.id == int(item["id"]), Citation.target_case_id.is_(None))
							.values(target_case_id=int(item["previous_target_case_id"]), unresolved=False)
						)
					session.commit()
			print(f"{'REVERTED' if args.apply else 'DRY RUN (nothing written)'} rows_in_backup={len(rows)}")
			return

		acted_reasons = {item.strip() for item in args.reasons.split(",") if item.strip()}
		inspected = 0
		reasons: Counter = Counter()
		suspects: list[dict] = []
		for inspected, row, reason in find_suspects(session, args.limit, args.batch_size):
			if reason is None:
				continue
			reasons[reason] += 1
			if reason not in acted_reasons:
				continue
			suspects.append(
				{
					"id": row.id,
					"source_case_id": row.source_case_id,
					"previous_target_case_id": row.target_case_id,
					"reason": reason,
					"citation_text": (row.citation_text or "")[:120].replace("\n", " "),
					"target_title": (row.title or "")[:120],
				}
			)
		session.rollback()
		print(f"inspected={inspected} suspects_to_act_on={len(suspects)} counted_by_reason={dict(reasons)} acting_on={sorted(acted_reasons)}")
		if args.examples and suspects:
			import random

			for item in random.Random(1).sample(suspects, min(args.examples, len(suspects))):
				print(f"EXAMPLE id={item['id']} source={item['source_case_id']} reason={item['reason']} text={item['citation_text']!r} -> {item['target_title']!r}")
		if args.backup is not None:
			args.backup.parent.mkdir(parents=True, exist_ok=True)
			with args.backup.open("w", encoding="utf-8", newline="") as handle:
				writer = csv.DictWriter(handle, fieldnames=BACKUP_FIELDS)
				writer.writeheader()
				writer.writerows(suspects)
			print(f"wrote {len(suspects)} rows to {args.backup}")
		if not args.apply:
			print("DRY RUN (nothing written)")
			return
		if args.backup is None:
			raise SystemExit("--apply needs --backup so the change can be reverted")
		ids = [item["id"] for item in suspects]
		for start in range(0, len(ids), 5_000):
			session.execute(update(Citation).where(Citation.id.in_(ids[start : start + 5_000])).values(target_case_id=None, unresolved=True))
			session.commit()
		print(f"APPLIED unlinked={len(ids)}")


if __name__ == "__main__":
	main()
