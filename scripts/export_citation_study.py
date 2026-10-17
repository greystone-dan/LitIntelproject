"""Read-only export for the citation study (cited together, most relied on, paragraph cited-by, where a case is cited).

SELECTs only: the whole run is one READ ONLY transaction, nothing is written to the database, no model is
called, no network is used. Output is one zip of small CSV files (well under 20 MiB). Low CPU: one reader,
lowered priority, a short pause between decisions.

  python scripts/export_citation_study.py --counts-only      # quick: just print table sizes (seconds)
  python scripts/export_citation_study.py                    # full export -> citation_study_export.zip
  python scripts/export_citation_study.py --sample 1500      # smaller position/pinpoint sample

Files in the zip:
  cases.csv            id, court, year, citation, title (no text)
  edges.csv            citing case, cited case, citation rows, rows that carry a stored pinpoint paragraph
  metrics.csv          the stored citation_metrics (in_degree, out_degree, pagerank) for comparison
  paragraph_edges.csv  the current paragraph_citation_edges table
  pinpoint_pairs.csv   cited case, paragraph, number of distinct citing cases (2 or more)
  occurrences.csv      sample of citing decisions: where each citation sits (paragraph role) and its signal phrase
  summary.txt          counts and settings
"""

from __future__ import annotations

import argparse
import csv
import io
import os
import sys
import time
import zipfile
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

# Same switch the live site uses for paragraph roles; set before the role module is imported.
os.environ.setdefault("ILIT_LEARNED_ROLES", "1")

from sqlalchemy import func, select, text

from backend.database import Case, Citation, CitationMetrics, ParagraphCitationEdge, ParagraphCitationStatus, SessionLocal

MAX_BYTES = 20 * 1024 * 1024
STATEMENT_TIMEOUT_MS = 15 * 60 * 1000
PAUSE_SECONDS = 0.05
SAMPLE_COURTS = {"FC": 0.75, "FCA": 0.25}  # share of --sample per court (RPD and RAD left out on purpose)


def _lower_priority() -> None:
	try:
		os.nice(10)
	except (AttributeError, OSError):
		pass  # Windows has no os.nice; the pause between decisions keeps the load light


def _start(session) -> None:
	"""One read-only transaction for the whole run."""
	session.execute(text("SET TRANSACTION READ ONLY"))
	session.execute(text(f"SET LOCAL statement_timeout = {STATEMENT_TIMEOUT_MS}"))


def _csv_bytes(header: list[str], rows) -> tuple[bytes, int]:
	buffer = io.StringIO()
	writer = csv.writer(buffer, lineterminator="\n")
	writer.writerow(header)
	count = 0
	for row in rows:
		writer.writerow(row)
		count += 1
	return buffer.getvalue().encode("utf-8"), count


def counts(session) -> dict[str, int]:
	linked = session.scalar(select(func.count()).select_from(Citation).where(Citation.target_case_id.is_not(None))) or 0
	return {
		"cases": session.scalar(select(func.count()).select_from(Case)) or 0,
		"citation_rows": session.scalar(select(func.count()).select_from(Citation)) or 0,
		"citation_rows_linked": linked,
		"citation_rows_with_stored_pinpoint": session.scalar(
			select(func.count()).select_from(Citation).where(Citation.target_paragraph.is_not(None), Citation.target_case_id.is_not(None))
		)
		or 0,
		"citation_metrics_rows": session.scalar(select(func.count()).select_from(CitationMetrics)) or 0,
		"paragraph_edges": session.scalar(select(func.count()).select_from(ParagraphCitationEdge)) or 0,
		"paragraph_status_rows": session.scalar(select(func.count()).select_from(ParagraphCitationStatus)) or 0,
	}


def case_rows(session):
	for row in session.execute(select(Case.id, Case.court, Case.date, Case.citation, Case.title).execution_options(yield_per=5000)):
		yield row.id, row.court, row.date.year if row.date else "", row.citation or "", (row.title or "")[:120]


def edge_rows(session):
	query = (
		select(
			Citation.source_case_id,
			Citation.target_case_id,
			func.count().label("rows"),
			func.count(Citation.target_paragraph).label("pinned"),
		)
		.where(Citation.target_case_id.is_not(None), Citation.target_case_id != Citation.source_case_id)
		.group_by(Citation.source_case_id, Citation.target_case_id)
		.execution_options(yield_per=5000)
	)
	for row in session.execute(query):
		yield row.source_case_id, row.target_case_id, row.rows, row.pinned


def pinpoint_pair_rows(session):
	citers = func.count(func.distinct(Citation.source_case_id))
	query = (
		select(Citation.target_case_id, Citation.target_paragraph, citers.label("citers"))
		.where(Citation.target_case_id.is_not(None), Citation.target_paragraph.is_not(None))
		.group_by(Citation.target_case_id, Citation.target_paragraph)
		.having(citers >= 2)
		.execution_options(yield_per=5000)
	)
	for row in session.execute(query):
		yield row.target_case_id, row.target_paragraph, row.citers


def sample_ids(session, total: int) -> list[int]:
	"""A repeatable spread of citing decisions from 2005 on, per court, that have at least one linked citation."""
	chosen: list[int] = []
	for court, share in SAMPLE_COURTS.items():
		limit = max(1, int(total * share))
		rows = session.execute(
			text(
				"SELECT c.id FROM cases c WHERE c.court = :court AND c.date >= '2005-01-01' AND c.full_text IS NOT NULL "
				"AND EXISTS (SELECT 1 FROM citations x WHERE x.source_case_id = c.id AND x.target_case_id IS NOT NULL) "
				"ORDER BY md5(c.id::text) LIMIT :limit"
			),
			{"court": court, "limit": limit},
		).all()
		chosen.extend(int(r[0]) for r in rows)
	return chosen


def occurrence_rows(session, source_ids: list[int]):
	"""One row per citation of another decision: paragraph role, signal phrase label and pinpoint."""
	from bisect import bisect_right

	from backend.citation_refine.pinpoints import target_paragraphs
	from backend.contextual_authority.case_structure import label_paragraph_roles, split_decision_text
	from backend.paragraph_cited_by import classify_signal, signal_window

	for done, source_id in enumerate(source_ids, 1):
		text_ = session.scalar(select(Case.full_text).where(Case.id == source_id)) or ""
		if not text_:
			continue
		rows = session.execute(
			select(
				Citation.target_case_id,
				Citation.citation_text,
				Citation.normalized_citation,
				Citation.target_paragraph,
				Citation.chunk_id,
				Citation.offset_start,
				Citation.offset_end,
			).where(Citation.source_case_id == source_id)
		).all()
		# Offsets are chunk-relative when a chunk is attached: place the chunk in the full text first.
		chunk_starts: dict[int, int] = {}
		chunk_ids = {r.chunk_id for r in rows if r.chunk_id is not None}
		if chunk_ids:
			from backend.database import CaseChunk

			cursor = 0
			for chunk_id, chunk_text in session.execute(
				select(CaseChunk.id, CaseChunk.text).where(CaseChunk.id.in_(chunk_ids)).order_by(CaseChunk.chunk_index)
			):
				position = text_.find(chunk_text, cursor)
				if position < 0:
					position = text_.find(chunk_text)
				if position >= 0:
					chunk_starts[chunk_id] = position
					cursor = position
		spans: list[tuple[int, int, int | None, str | None, str | None, int | None]] = []
		for r in rows:
			if r.offset_start is None or r.offset_end is None:
				continue
			shift = 0
			if r.chunk_id is not None:
				if r.chunk_id not in chunk_starts:
					continue
				shift = chunk_starts[r.chunk_id]
			start, end = r.offset_start + shift, r.offset_end + shift
			if 0 <= start < end <= len(text_):
				spans.append((start, end, r.target_case_id, r.citation_text, r.normalized_citation, r.target_paragraph))
		if not spans:
			continue
		paragraphs = split_decision_text(text_)
		roles = label_paragraph_roles(paragraphs)
		starts: list[int] = []
		cursor = 0
		for paragraph in paragraphs:
			position = text_.find(paragraph[:60], cursor)
			if position < 0:
				position = cursor
			starts.append(position)
			cursor = position
		ends = sorted({end for _, end, *_ in spans})
		for start, end, target, citation_text, normalized, stored in sorted(spans):
			if target is None or target == source_id:
				continue
			index = max(0, bisect_right(starts, start) - 1)
			prior = bisect_right(ends, start) - 1
			previous_end = ends[prior] if prior >= 0 and ends[prior] <= start else 0
			purpose, _phrase = classify_signal(signal_window(text_, start, previous_end))
			pins = target_paragraphs(citation_text, normalized, stored)
			first = pins.first if pins is not None else ""
			role = roles[index] if index < len(roles) else ""
			yield source_id, target, index, len(paragraphs), role, purpose, first
		time.sleep(PAUSE_SECONDS)
		if done % 200 == 0:
			print(f"  positions: {done}/{len(source_ids)} decisions", flush=True)


def main() -> None:
	parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
	parser.add_argument("--counts-only", action="store_true", help="Print table sizes and stop.")
	parser.add_argument("--sample", type=int, default=3000, help="Citing decisions to read for paragraph roles (default 3000).")
	parser.add_argument("--out", default="citation_study_export.zip", help="Output zip (default: current folder).")
	args = parser.parse_args()

	_lower_priority()
	with SessionLocal() as session:
		_start(session)
		sizes = counts(session)
		for name, value in sizes.items():
			print(f"{name}: {value:,}")
		if args.counts_only:
			return
		started = time.time()
		parts: dict[str, tuple[bytes, int]] = {}
		print("cases ...", flush=True)
		parts["cases.csv"] = _csv_bytes(["id", "court", "year", "citation", "title"], case_rows(session))
		print("edges ...", flush=True)
		parts["edges.csv"] = _csv_bytes(["citing_id", "cited_id", "citation_rows", "rows_with_pinpoint"], edge_rows(session))
		print("stored metrics and paragraph cited-by ...", flush=True)
		parts["metrics.csv"] = _csv_bytes(
			["case_id", "in_degree", "out_degree", "pagerank"],
			(
				(r.case_id, r.in_degree, r.out_degree, r.pagerank)
				for r in session.execute(select(CitationMetrics.case_id, CitationMetrics.in_degree, CitationMetrics.out_degree, CitationMetrics.pagerank))
			),
		)
		parts["paragraph_edges.csv"] = _csv_bytes(
			["citing_id", "cited_id", "paragraph", "mentions", "purpose", "signal"],
			(
				(r.source_case_id, r.target_case_id, r.target_paragraph, r.mentions, r.purpose, r.signal or "")
				for r in session.execute(
					select(
						ParagraphCitationEdge.source_case_id,
						ParagraphCitationEdge.target_case_id,
						ParagraphCitationEdge.target_paragraph,
						ParagraphCitationEdge.mentions,
						ParagraphCitationEdge.purpose,
						ParagraphCitationEdge.signal,
					)
				)
			),
		)
		print("pinpoint pairs ...", flush=True)
		parts["pinpoint_pairs.csv"] = _csv_bytes(["cited_id", "paragraph", "citing_decisions"], pinpoint_pair_rows(session))
		print(f"positions for up to {args.sample} decisions ...", flush=True)
		ids = sample_ids(session, args.sample)
		parts["occurrences.csv"] = _csv_bytes(
			["citing_id", "cited_id", "paragraph_index", "paragraph_total", "role", "signal_label", "pinpoint_paragraph"],
			occurrence_rows(session, ids),
		)
		session.rollback()  # ends the read-only transaction; nothing was written

	summary = [f"{key}: {value}" for key, value in sizes.items()]
	summary.append(f"position sample decisions: {len(ids)} (ILIT_LEARNED_ROLES={os.environ.get('ILIT_LEARNED_ROLES')})")
	summary += [f"{name}: {count:,} rows" for name, (_, count) in parts.items()]
	summary.append(f"seconds: {time.time() - started:.0f}")
	out = Path(args.out)
	with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
		for name, (data, _) in parts.items():
			archive.writestr(name, data)
		archive.writestr("summary.txt", "\n".join(summary) + "\n")
	size = out.stat().st_size
	print("\n".join(summary))
	print(f"wrote {out} ({size / 1024 / 1024:.1f} MiB)")
	if size > MAX_BYTES:
		print("WARNING: over 20 MiB; tell Claude before sending it anywhere.")


if __name__ == "__main__":
	main()
