"""Guarded removal of exact citation self-links."""

from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import delete, select, func

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.citations import compute_citation_metrics
from backend.database import Citation, SessionLocal

COLUMNS = (
    "id",
    "source_case_id",
    "target_case_id",
    "citation_kind",
    "citation_text",
    "normalized_citation",
    "provenance",
    "chunk_id",
    "offset_start",
    "offset_end",
    "unresolved",
)


def remove_self_citations(*, expected_count: int, export_path: Path, apply: bool) -> int:
    """Export and optionally remove exact self-links, guarded by an expected count."""
    with SessionLocal() as db:
        count = int(
            db.scalar(
                select(func.count(Citation.id)).where(Citation.source_case_id == Citation.target_case_id)
            )
            or 0
        )
        if count != expected_count:
            raise RuntimeError(f"Expected {expected_count:,} self-citations, found {count:,}; no changes made")
        rows = list(
            db.scalars(
                select(Citation)
                .where(Citation.source_case_id == Citation.target_case_id)
                .order_by(Citation.id)
            )
        )
        export_path.parent.mkdir(parents=True, exist_ok=True)
        with export_path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=COLUMNS)
            writer.writeheader()
            for row in rows:
                writer.writerow({column: getattr(row, column) for column in COLUMNS})
        if not apply:
            return count
        db.execute(delete(Citation).where(Citation.source_case_id == Citation.target_case_id))
        db.flush()
        compute_citation_metrics(db)
        db.commit()
        remaining = int(
            db.scalar(
                select(func.count(Citation.id)).where(Citation.source_case_id == Citation.target_case_id)
            )
            or 0
        )
        if remaining:
            raise RuntimeError(f"Cleanup verification failed: {remaining:,} self-citations remain")
        return count


def main() -> int:
    parser = argparse.ArgumentParser(description="Export and remove exact citation self-links.")
    parser.add_argument("--expected-count", type=int, required=True, help="Abort unless this exact row count is found")
    parser.add_argument("--export-file", type=Path, required=True, help="Recovery CSV path written before deletion")
    parser.add_argument("--apply", action="store_true", help="Commit deletion; without this flag only export a dry-run")
    args = parser.parse_args()
    count = remove_self_citations(
        expected_count=args.expected_count,
        export_path=args.export_file,
        apply=args.apply,
    )
    action = "removed" if args.apply else "planned"
    print(f"{action}={count} export={args.export_file} write_performed={args.apply}")
    if args.apply:
        print("citation_metrics=recomputed self_citations=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
