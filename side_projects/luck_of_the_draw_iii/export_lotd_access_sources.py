"""Export Access-sized LotD slices from PostgreSQL into CSV staging files."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

from sqlalchemy import text

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
	sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import engine


PROJECT_DIR = Path(__file__).resolve().parent
STAGING_DIR = PROJECT_DIR / "output" / "access_staging"
CASES_CSV = STAGING_DIR / "lotd_access_cases.csv"
SUMMARY_CSV = STAGING_DIR / "lotd_access_docket_summary.csv"


def export_query(path: Path, query: str) -> int:
	row_count = 0
	with engine.connect() as connection, path.open("w", encoding="utf-8", newline="") as file_obj:
		result = connection.execution_options(stream_results=True).execute(text(query))
		writer = csv.writer(file_obj)
		writer.writerow(list(result.keys()))
		for row in result:
			writer.writerow(list(row))
			row_count += 1
	return row_count


def main() -> None:
	STAGING_DIR.mkdir(parents=True, exist_ok=True)
	cases = export_query(
		CASES_CSV,
		"""
		SELECT imm_number, year, name, date_filed, city_filed, nature, class, track, doc_count, source_url, scraped_timestamp
		FROM lotd.access_cases
		ORDER BY imm_number
		""",
	)
	summary = export_query(
		SUMMARY_CSV,
		"""
		SELECT imm_number, name, year, date_filed, city_filed, nature, class, track, doc_count, first_doc_dt, last_doc_dt, max_re_no, docket_rows_with_docno
		FROM lotd.access_docket_summary
		ORDER BY imm_number
		""",
	)
	print(f"cases_csv={CASES_CSV}")
	print(f"cases_rows={cases}")
	print(f"summary_csv={SUMMARY_CSV}")
	print(f"summary_rows={summary}")


if __name__ == "__main__":
	main()