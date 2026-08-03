"""Ingest A2AJ citation-network data into local provenance tables and graph edges."""
from __future__ import annotations

import argparse
from pathlib import Path

import pyarrow.parquet as pq

from backend.citations import (
	build_a2aj_case_map,
	convert_a2aj_edges_to_local,
	ingest_a2aj_cases_from_rows,
	ingest_a2aj_citation_edges_from_rows,
)
from backend.database import SessionLocal

SOURCE = Path("data/raw/a2aj/FC/train.parquet")


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("source_file", nargs="?", type=Path, default=SOURCE)
	parser.add_argument("--batch-size", type=int, default=500)
	parser.add_argument("--limit", type=int, default=None)
	parser.add_argument("--build-map", action="store_true", help="Match A2AJ neutral citations to local cases")
	parser.add_argument("--convert", action="store_true", help="Convert A2AJ edges into local citations")
	return parser.parse_args()


def main() -> None:
	args = parse_args()
	if not args.source_file.exists():
		raise SystemExit(f"Source file does not exist: {args.source_file}")

	seen = 0
	rows: list[dict] = []
	with SessionLocal() as session:
		parquet = pq.ParquetFile(args.source_file)
		for batch in parquet.iter_batches(batch_size=args.batch_size):
			for record in batch.to_pylist():
				rows.append(record)
				seen += 1
				if args.limit is not None and seen >= args.limit:
					break
			if args.limit is not None and seen >= args.limit:
				break

		cases_inserted = ingest_a2aj_cases_from_rows(session, rows)
		edges_inserted = ingest_a2aj_citation_edges_from_rows(session, rows)
		print(f"a2aj_cases_inserted={cases_inserted}")
		print(f"a2aj_edges_inserted={edges_inserted}")
		if args.build_map:
			mapped = build_a2aj_case_map(session)
			print(f"a2aj_case_map_updated={mapped}")
		if args.convert:
			converted = convert_a2aj_edges_to_local(session)
			print(f"local_citations_inserted={converted}")


if __name__ == "__main__":
	main()