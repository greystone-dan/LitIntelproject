"""Load the Hugging Face FC activity dataset into the canonical database tables."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date, datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Iterator

import pyarrow.parquet as pq
from huggingface_hub import hf_hub_download
from sqlalchemy import select

from backend.database import FCActivityCase, FCActivityDocument, SessionLocal, init_db
from backend.fc_activity import derive_case_source_key, load_hf_fc_activity_rows

DEFAULT_DATASET = "refugee-law-lab/luck-of-the-draw-iii"
DEFAULT_SPLIT = "train"
DEFAULT_SOURCE_FILE = Path("data/raw/a2aj/fc_activity/train.parquet")
LEGACY_SOURCE_FILE = Path("data/raw/a2aj/FC/train.parquet")


def resolve_source_file(source_file: str | Path | None) -> Path:
    if source_file is not None:
        candidate = Path(source_file)
        if candidate.exists():
            return candidate
        raise FileNotFoundError(f"Source file not found: {candidate}")

    if DEFAULT_SOURCE_FILE.exists():
        return DEFAULT_SOURCE_FILE
    if LEGACY_SOURCE_FILE.exists():
        return LEGACY_SOURCE_FILE
    raise FileNotFoundError(
        "No local FC activity parquet source found. Expected "
        f"{DEFAULT_SOURCE_FILE} or {LEGACY_SOURCE_FILE}."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default=DEFAULT_DATASET, help="Hugging Face dataset name")
    parser.add_argument("--split", default=DEFAULT_SPLIT, help="Dataset split to load")
    parser.add_argument("--source-file", type=str, default=str(DEFAULT_SOURCE_FILE), help="Local parquet file to ingest")
    parser.add_argument("--limit", type=int, default=None, help="Optional max rows to ingest")
    parser.add_argument("--batch-size", type=int, default=500, help="Rows to process per batch")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print counts without writing to DB")
    parser.add_argument("--download", action="store_true", help="Download the official parquet file before importing")
    return parser.parse_args()


def parse_iso_date(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return None
        try:
            return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
        except ValueError:
            try:
                return date.fromisoformat(text[:10])
            except ValueError:
                return None
    return None


def parse_iso_datetime(value: Any) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    if isinstance(value, date):
        return datetime.combine(value, datetime.min.time())
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


def download_source_file(dataset: str, split: str, target_path: Path) -> Path:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    path = hf_hub_download(
        repo_id=dataset,
        repo_type="dataset",
        filename=f"{split}.parquet",
        local_dir=str(target_path.parent),
        local_dir_use_symlinks=False,
    )
    return Path(path)


def iter_parquet_rows(source_file: Path, batch_size: int, limit: int | None = None) -> Iterator[list[dict[str, Any]]]:
    parquet = pq.ParquetFile(str(source_file))
    rows_seen = 0
    for batch in parquet.iter_batches(batch_size=batch_size):
        rows = batch.to_pylist()
        if limit is not None:
            remaining = max(limit - rows_seen, 0)
            if remaining <= 0:
                break
            rows = rows[:remaining]
        rows_seen += len(rows)
        yield rows
        if limit is not None and rows_seen >= limit:
            break


def batched(rows: Iterable[dict[str, Any]], batch_size: int) -> Iterator[list[dict[str, Any]]]:
    iterator = iter(rows)
    while batch := list(islice(iterator, batch_size)):
        yield batch


def ingest_rows(rows: list[dict[str, Any]], dry_run: bool = False) -> dict[str, int]:
    canonical_rows = load_hf_fc_activity_rows(rows)
    processed = 0
    upserts = 0
    docs = 0

    if dry_run:
        for row in canonical_rows:
            processed += 1
            docs += len(row.get("documents") or [])
        return {"rows": processed, "documents": docs, "upserts": 0}

    with SessionLocal() as session:
        for row in canonical_rows:
            source_key = row.get("source_key") or derive_case_source_key(row)
            citation = row.get("citation")
            case = session.scalar(select(FCActivityCase).where(FCActivityCase.source_key == source_key))
            if case is None:
                case = FCActivityCase(
                    source_key=source_key,
                    citation=citation,
                    year=row.get("year"),
                    case_name=row.get("case_name"),
                    date_filed=row.get("date_filed"),
                    city_filed=row.get("city_filed"),
                    nature=row.get("nature"),
                    case_class=row.get("case_class"),
                    track=row.get("track"),
                    source_url=row.get("source_url"),
                    scraped_timestamp=parse_iso_datetime(row.get("scraped_timestamp")),
                    raw_payload=row,
                )
                session.add(case)
                session.flush()
                upserts += 1
            else:
                case.citation = citation
                case.year = row.get("year")
                case.case_name = row.get("case_name")
                case.date_filed = row.get("date_filed")
                case.city_filed = row.get("city_filed")
                case.nature = row.get("nature")
                case.case_class = row.get("case_class")
                case.track = row.get("track")
                case.source_url = row.get("source_url")
                case.scraped_timestamp = parse_iso_datetime(row.get("scraped_timestamp"))
                case.raw_payload = row

            for doc in row.get("documents") or []:
                re_no = str(doc.get("re_no")) if doc.get("re_no") is not None else None
                docno = str(doc.get("docno")) if doc.get("docno") is not None else None
                entry_hash = doc.get("entry_hash") or (doc.get("re_no"), doc.get("docno"), doc.get("doc_dt"), doc.get("recorded_entry"))
                existing = session.scalar(
                    select(FCActivityDocument).where(
                        FCActivityDocument.case_id == case.id,
                        FCActivityDocument.re_no == re_no,
                        FCActivityDocument.docno == docno,
                    )
                )
                if existing is None:
                    entry_hash_value = (
                        hashlib.sha256(str(entry_hash).encode("utf-8")).hexdigest()
                        if isinstance(entry_hash, tuple)
                        else str(entry_hash)
                    )
                    session.add(
                        FCActivityDocument(
                            case_id=case.id,
                            re_no=re_no,
                            docno=docno,
                            doc_dt=parse_iso_date(doc.get("doc_dt")),
                            recorded_entry=doc.get("recorded_entry"),
                            entry_hash=entry_hash_value,
                            raw_document=doc,
                        )
                    )
                    docs += 1
                processed += 1

            session.commit()

    return {"rows": len(canonical_rows), "documents": docs, "upserts": upserts}


def main() -> None:
    args = parse_args()
    if args.batch_size < 1:
        raise SystemExit("--batch-size must be at least 1")

    init_db()
    source_file = resolve_source_file(args.source_file)
    if args.download:
        source_file = download_source_file(args.dataset, args.split, source_file)

    totals = {"rows": 0, "documents": 0, "upserts": 0}
    for batch in iter_parquet_rows(source_file, batch_size=args.batch_size, limit=args.limit):
        result = ingest_rows(batch, dry_run=args.dry_run)
        for key, value in result.items():
            totals[key] += value

    print(
        json.dumps(
            {
                "dataset": args.dataset,
                "split": args.split,
                "source_file": str(source_file),
                **totals,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
