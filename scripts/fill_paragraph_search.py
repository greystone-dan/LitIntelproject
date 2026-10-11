"""Add decisions that are missing from the paragraph keyword index (table paragraph_search). Dry run by default.

The index behind the case search box and unit search was filled once by a one-off SQL file. Decisions whose paragraph
chunks were created after that, or below the id it resumed from, are not in it, so they never show up in search. The
dry run counts, per court, paragraph chunks and how many are indexed. --apply adds only the missing rows (nothing is
changed or deleted), in small committed batches, so it can be stopped and run again.

  python scripts/fill_paragraph_search.py                      # dry run: counts per court
  python scripts/fill_paragraph_search.py --apply --court RAD  # add the missing RAD rows
Undo: DELETE FROM paragraph_search WHERE case_id IN (SELECT id FROM cases WHERE court ILIKE '%Refugee Appeal%');
(only valid when the dry run showed no RAD rows indexed before).
If a court shows no paragraph chunks at all, it needs `scripts/chunk_cases.py` first; this script cannot help.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text

from backend.database import SessionLocal

COUNTS_SQL = text(
	"""
	SELECT c.court AS court, count(*) AS paragraph_chunks, count(ps.chunk_id) AS indexed
	FROM case_chunks ch
	JOIN cases c ON c.id = ch.case_id
	LEFT JOIN paragraph_search ps ON ps.chunk_id = ch.id
	WHERE ch.chunk_set = 'paragraph'
	GROUP BY c.court ORDER BY c.court
	"""
)

FILL_SQL = text(
	"""
	INSERT INTO paragraph_search (chunk_id, case_id, tsv)
	SELECT ch.id, ch.case_id, to_tsvector('english', ch.text)
	FROM case_chunks ch
	JOIN cases c ON c.id = ch.case_id
	WHERE ch.chunk_set = 'paragraph'
	  AND (c.court = :court OR c.court ILIKE :court_like)
	  AND NOT EXISTS (SELECT 1 FROM paragraph_search p WHERE p.chunk_id = ch.id)
	ORDER BY ch.id
	LIMIT :batch
	ON CONFLICT (chunk_id) DO NOTHING
	"""
)

COURT_LIKE = {"FC": "Federal Court", "FCA": "%Appeal%", "SCC": "%Supreme%", "RAD": "%Refugee Appeal%", "RPD": "%Refugee Protection%"}


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--apply", action="store_true", help="Insert the missing rows (needs --court).")
	parser.add_argument("--court", default="", help="Court to fill: as stored in cases.court, or FC, FCA, SCC, RAD, RPD.")
	parser.add_argument("--batch", type=int, default=5000, help="Rows per committed batch.")
	parser.add_argument("--sleep", type=float, default=0.5, help="Seconds to pause between batches.")
	args = parser.parse_args()

	with SessionLocal() as session:
		print(f"{'court':32} {'paragraph chunks':>17} {'indexed':>10} {'missing':>10}")
		for row in session.execute(COUNTS_SQL).mappings():
			print(f"{str(row['court']):32} {row['paragraph_chunks']:>17,} {row['indexed']:>10,} {row['paragraph_chunks'] - row['indexed']:>10,}")
		if not args.apply:
			print("Dry run: nothing written. Add --apply --court <court> to fill the missing rows.")
			return
		if not args.court:
			parser.error("--apply needs --court")
		court = args.court.strip()
		like = COURT_LIKE.get(court.upper(), court)
		total = 0
		while True:
			added = session.execute(FILL_SQL, {"court": court, "court_like": like, "batch": args.batch}).rowcount
			session.commit()
			if not added:
				break
			total += added
			print(f"added {total:,} rows", flush=True)
			time.sleep(args.sleep)
		session.execute(text("ANALYZE paragraph_search"))
		session.commit()
		print(f"Done: {total:,} rows added for {court}.")


if __name__ == "__main__":
	main()
