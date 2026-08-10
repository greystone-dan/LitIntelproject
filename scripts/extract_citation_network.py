"""Backfill the citation network from case texts and/or stored chunks."""
from __future__ import annotations

import argparse

from backend.citations import (
	batch_extract_citations_from_cases,
	batch_extract_citations_from_chunks,
	batch_extract_statute_references_from_cases,
	batch_extract_statute_references_from_chunks,
	compute_citation_metrics,
)
from backend.database import SessionLocal


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--cases", action="store_true", help="Extract citations from case full text")
	parser.add_argument("--chunks", action="store_true", help="Extract citations from stored chunks")
	parser.add_argument("--statutes", action="store_true", help="Extract statutes/instruments into statute_references")
	parser.add_argument("--metrics", action="store_true", help="Recompute citation metrics after extraction")
	parser.add_argument("--batch-size", type=int, default=500, help="Cases per transaction")
	parser.add_argument("--cases-start-after-id", type=int, default=0, help="Resume case extraction after this committed case ID")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	run_cases = args.cases or not args.chunks
	run_chunks = args.chunks
	run_statutes = args.statutes

	with SessionLocal() as session:
		if run_cases:
			inserted = batch_extract_citations_from_cases(
				session,
				batch_size=args.batch_size,
				start_after_case_id=args.cases_start_after_id,
			)
			print(f"case_citations_inserted={inserted}")
		if run_chunks:
			inserted = batch_extract_citations_from_chunks(session, batch_size=args.batch_size)
			print(f"chunk_citations_inserted={inserted}")
		if run_statutes:
			if run_chunks:
				inserted = batch_extract_statute_references_from_chunks(session, batch_size=args.batch_size)
				print(f"chunk_statute_references_inserted={inserted}")
			else:
				inserted = batch_extract_statute_references_from_cases(
					session,
					batch_size=args.batch_size,
					start_after_case_id=args.cases_start_after_id,
				)
				print(f"case_statute_references_inserted={inserted}")
		if args.metrics:
			updated = compute_citation_metrics(session)
			print(f"metrics_updated={updated}")


if __name__ == "__main__":
	main()