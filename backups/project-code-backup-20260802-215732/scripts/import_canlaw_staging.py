"""Import Hugging Face staging records into the primary CaseLibrary database."""

import argparse
import json
import os
import sqlite3
from collections.abc import Iterator
from pathlib import Path

from scripts.ingest_a2aj_parquet import build_case, post_case

MERGE_URL = os.getenv("CASELIBRARY_MERGE_URL", "http://127.0.0.1:8000/ingest/merge")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staging-db", type=Path, default=Path("canlaw.db"))
    parser.add_argument("--courts", nargs="+", default=["FC", "RPD", "FCA", "SCC"])
    parser.add_argument("--start-after-id", type=int, default=0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def iter_staging_records(
    database_path: Path,
    courts: list[str],
    start_after_id: int = 0,
) -> Iterator[tuple[int, dict]]:
    if not database_path.exists():
        raise FileNotFoundError(f"Staging database does not exist: {database_path}")

    normalized_courts = list(dict.fromkeys(court.strip().upper() for court in courts))
    placeholders = ",".join("?" for _ in normalized_courts)
    uri = f"file:{database_path.resolve().as_posix()}?mode=ro"
    with sqlite3.connect(uri, uri=True) as connection:
        cursor = connection.execute(
            f"""
            SELECT id, raw_payload
            FROM cases
            WHERE id > ? AND dataset IN ({placeholders})
            ORDER BY id
            """,
            [start_after_id, *normalized_courts],
        )
        for row_id, raw_payload in cursor:
            yield row_id, json.loads(raw_payload)


def main() -> None:
    args = parse_args()
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    if args.start_after_id < 0:
        raise SystemExit("--start-after-id cannot be negative")

    seen = candidates = created = merged = invalid = 0
    last_id = args.start_after_id
    for row_id, record in iter_staging_records(args.staging_db, args.courts, args.start_after_id):
        seen += 1
        last_id = row_id
        case = build_case(record)
        if case is None or not case.full_text:
            invalid += 1
            continue

        if args.dry_run:
            print(f"would merge: staging_id={row_id} citation={case.citation or case.title}")
            candidates += 1
        else:
            result = post_case(case, MERGE_URL)
            action = result["action"]
            merged_case = result["case"]
            if action == "created":
                created += 1
            else:
                merged += 1
            print(
                f"{action}: staging_id={row_id} case_id={merged_case['id']} "
                f"citation={merged_case['citation']} changed={','.join(result['changed_fields'])}"
            )

        processed = candidates if args.dry_run else created + merged
        if args.limit is not None and processed >= args.limit:
            break

    print(
        f"seen={seen} candidates={candidates} created={created} merged={merged} invalid={invalid} "
        f"last_staging_id={last_id} dry_run={args.dry_run}"
    )


if __name__ == "__main__":
    main()
