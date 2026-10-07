"""Keep the paragraph_search table in step with case_chunks (additive; no model, no AI).

New paragraph chunks (from RAD/RLLR imports, the daily intake, or re-chunking) get a tsvector row; rows whose
chunk no longer exists can be pruned. Safe to run repeatedly and while the site is up: it reads case_chunks
in id order in small committed batches and writes only paragraph_search.
"""

from __future__ import annotations

import time
from typing import Any

from sqlalchemy import text

from .paragraph_search import TS_CONFIG

BATCH_ROWS = 5000

_TABLE_EXISTS = text("SELECT to_regclass('public.paragraph_search') IS NOT NULL")
_MAX_ID = text("SELECT coalesce(max(chunk_id), 0) FROM paragraph_search")
_INSERT = text(
	f"""
	INSERT INTO paragraph_search (chunk_id, case_id, tsv)
	SELECT id, case_id, to_tsvector('{TS_CONFIG}', text)
	FROM case_chunks
	WHERE chunk_set = 'paragraph' AND id > :after_id
	ORDER BY id
	LIMIT :batch
	ON CONFLICT (chunk_id) DO NOTHING
	"""
)
_MISSING_BELOW = text(
	"""
	SELECT count(*) FROM case_chunks c
	WHERE c.chunk_set = 'paragraph' AND c.id <= :max_id
	  AND NOT EXISTS (SELECT 1 FROM paragraph_search p WHERE p.chunk_id = c.id)
	"""
)
_COUNT_AFTER = text("SELECT count(*) FROM case_chunks WHERE chunk_set = 'paragraph' AND id > :after_id")
_ORPHANS = text(
	"SELECT count(*) FROM paragraph_search p WHERE NOT EXISTS (SELECT 1 FROM case_chunks c WHERE c.id = p.chunk_id)"
)
_PRUNE = text(
	"DELETE FROM paragraph_search p WHERE NOT EXISTS (SELECT 1 FROM case_chunks c WHERE c.id = p.chunk_id)"
)


def sync_paragraph_search(
	db: Any,
	*,
	apply: bool = True,
	prune: bool = False,
	max_rows: int | None = None,
	pause_seconds: float = 0.2,
) -> dict[str, Any]:
	"""Add tsvector rows for paragraph chunks newer than the table's highest chunk id.

	Returns counts. With apply=False nothing is written. A missing table is reported, not created.
	"""
	report: dict[str, Any] = {"table_exists": bool(db.execute(_TABLE_EXISTS).scalar()), "added": 0}
	if not report["table_exists"]:
		return report
	after_id = int(db.execute(_MAX_ID).scalar() or 0)
	report["highest_chunk_id_before"] = after_id
	report["new_paragraphs_waiting"] = int(db.execute(_COUNT_AFTER, {"after_id": after_id}).scalar() or 0)
	report["missing_below_highest"] = int(db.execute(_MISSING_BELOW, {"max_id": after_id}).scalar() or 0)
	report["orphans"] = int(db.execute(_ORPHANS).scalar() or 0)
	if not apply:
		return report
	remaining = max_rows
	while True:
		batch = BATCH_ROWS if remaining is None else min(BATCH_ROWS, remaining)
		if batch <= 0:
			break
		added = db.execute(_INSERT, {"after_id": after_id, "batch": batch}).rowcount or 0
		db.commit()
		if added == 0:
			break
		report["added"] += added
		after_id = int(db.execute(_MAX_ID).scalar() or after_id)
		if remaining is not None:
			remaining -= added
		time.sleep(pause_seconds)
	if prune and report["orphans"]:
		report["pruned"] = db.execute(_PRUNE).rowcount or 0
		db.commit()
	return report
