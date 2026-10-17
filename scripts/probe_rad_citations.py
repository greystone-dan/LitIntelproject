"""Read-only probe: why do RAD decisions have no linked citations?

SELECTs only, inside one READ ONLY transaction. No keys, no model, no network, nothing written to the database.
Writes one small zip (a few MiB):

  courts.csv      per court: decisions, with full text, with chunks, with any citation row, citation rows, linked,
                  unresolved, statute references (shows which layers ever ran for each court)
  kinds.csv       per court and citation kind: rows and linked rows
  decisions.jsonl one line per sampled decision (RAD, plus a few RPD and FC as controls): id, court, date, citation,
                  title, processing status, chunk count, full text (cut at 80,000 characters), and every stored
                  citation row (kind, text, normalized form, target, unresolved flag, offsets, chunk)
  summary.txt     settings and counts

  python scripts/probe_rad_citations.py                # RAD 200, RPD 30, FC 30
  python scripts/probe_rad_citations.py --rad 100
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import zipfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import func, select, text

from backend.database import Case, CaseChunk, Citation, SessionLocal, StatuteReference

STATEMENT_TIMEOUT_MS = 10 * 60 * 1000
TEXT_LIMIT = 80_000


def _lower_priority() -> None:
	try:
		os.nice(10)
	except (AttributeError, OSError):
		pass


def courts_table(session) -> list[list]:
	cases = dict(session.execute(select(Case.court, func.count()).group_by(Case.court)).all())
	with_text = dict(
		session.execute(select(Case.court, func.count()).where(Case.full_text.is_not(None), Case.full_text != "").group_by(Case.court)).all()
	)
	with_chunks = dict(
		session.execute(
			select(Case.court, func.count(func.distinct(CaseChunk.case_id))).join(CaseChunk, CaseChunk.case_id == Case.id).group_by(Case.court)
		).all()
	)
	rows = {
		court: (n_cases, n_linked, n_unres, n_rows)
		for court, n_cases, n_linked, n_unres, n_rows in session.execute(
			select(
				Case.court,
				func.count(func.distinct(Citation.source_case_id)),
				func.count(Citation.target_case_id),
				func.count().filter(Citation.unresolved.is_(True)),
				func.count(),
			)
			.join(Citation, Citation.source_case_id == Case.id)
			.group_by(Case.court)
		).all()
	}
	statutes = dict(
		session.execute(
			select(Case.court, func.count()).join(StatuteReference, StatuteReference.source_case_id == Case.id).group_by(Case.court)
		).all()
	)
	table = [["court", "decisions", "with_full_text", "with_chunks", "with_any_citation_row", "citation_rows", "linked_rows", "unresolved_rows", "statute_refs"]]
	for court in sorted(cases):
		with_any, linked, unres, total = rows.get(court, (0, 0, 0, 0))
		table.append([court, cases[court], with_text.get(court, 0), with_chunks.get(court, 0), with_any, total, linked, unres, statutes.get(court, 0)])
	return table


def kinds_table(session) -> list[list]:
	table = [["court", "citation_kind", "rows", "linked_rows"]]
	for court, kind, rows, linked in session.execute(
		select(Case.court, Citation.citation_kind, func.count(), func.count(Citation.target_case_id))
		.join(Citation, Citation.source_case_id == Case.id)
		.group_by(Case.court, Citation.citation_kind)
		.order_by(Case.court, Citation.citation_kind)
	).all():
		table.append([court, kind, rows, linked])
	return table


def sample(session, court: str, limit: int) -> list[int]:
	rows = session.execute(
		text("SELECT id FROM cases WHERE court = :court AND full_text IS NOT NULL ORDER BY md5(id::text) LIMIT :limit"),
		{"court": court, "limit": limit},
	).all()
	return [int(r[0]) for r in rows]


def decision_lines(session, ids: list[int]):
	for case_id in ids:
		case = session.execute(
			select(Case.id, Case.court, Case.date, Case.citation, Case.title, Case.processing_status, Case.full_text).where(Case.id == case_id)
		).one()
		chunks = session.scalar(select(func.count()).select_from(CaseChunk).where(CaseChunk.case_id == case_id)) or 0
		cites = [
			{
				"kind": c.citation_kind,
				"text": (c.citation_text or "")[:200],
				"normalized": (c.normalized_citation or "")[:200],
				"target": c.target_case_id,
				"unresolved": c.unresolved,
				"start": c.offset_start,
				"end": c.offset_end,
				"chunk": c.chunk_id,
			}
			for c in session.execute(
				select(
					Citation.citation_kind,
					Citation.citation_text,
					Citation.normalized_citation,
					Citation.target_case_id,
					Citation.unresolved,
					Citation.offset_start,
					Citation.offset_end,
					Citation.chunk_id,
				).where(Citation.source_case_id == case_id)
			)
		]
		yield json.dumps(
			{
				"id": case.id,
				"court": case.court,
				"date": case.date.isoformat() if case.date else None,
				"citation": case.citation,
				"title": case.title,
				"processing_status": case.processing_status,
				"chunks": chunks,
				"text_length": len(case.full_text or ""),
				"text": (case.full_text or "")[:TEXT_LIMIT],
				"citation_rows": cites,
			},
			ensure_ascii=False,
		)


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--rad", type=int, default=200)
	parser.add_argument("--rpd", type=int, default=0, help="RPD is left out on purpose.")
	parser.add_argument("--fc", type=int, default=30)
	parser.add_argument("--out", default="rad_citation_probe.zip")
	args = parser.parse_args()

	_lower_priority()
	with SessionLocal() as session:
		session.execute(text("SET TRANSACTION READ ONLY"))
		session.execute(text(f"SET LOCAL statement_timeout = {STATEMENT_TIMEOUT_MS}"))
		courts = courts_table(session)
		kinds = kinds_table(session)
		ids = sample(session, "RAD", args.rad) + (sample(session, "RPD", args.rpd) if args.rpd else []) + sample(session, "FC", args.fc)
		lines = list(decision_lines(session, ids))
		session.rollback()

	def to_csv(table: list[list]) -> str:
		buffer = io.StringIO()
		csv.writer(buffer, lineterminator="\n").writerows(table)
		return buffer.getvalue()

	summary = [f"sampled decisions: {len(ids)} (RAD {args.rad}, RPD {args.rpd}, FC {args.fc})", f"text cut at {TEXT_LIMIT} characters"]
	summary += [",".join(str(x) for x in row) for row in courts]
	out = Path(args.out)
	with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
		archive.writestr("courts.csv", to_csv(courts))
		archive.writestr("kinds.csv", to_csv(kinds))
		archive.writestr("decisions.jsonl", "\n".join(lines) + "\n")
		archive.writestr("summary.txt", "\n".join(summary) + "\n")
	print("\n".join(summary))
	print(f"wrote {out} ({out.stat().st_size / 1024 / 1024:.1f} MiB)")


if __name__ == "__main__":
	main()
