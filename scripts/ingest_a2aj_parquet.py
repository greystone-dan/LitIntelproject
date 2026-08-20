"""Raw-ingest A2AJ case-law Parquet records without OpenAI calls."""
import argparse
import hashlib
import json
import os
from datetime import date, datetime
from pathlib import Path
from urllib.request import Request, urlopen

import pyarrow.parquet as pq
from sqlalchemy import select

from backend.database import Case, SessionLocal
from backend.models import CaseIngestRequest

API_URL = os.getenv("CASELIBRARY_INGEST_URL", "http://127.0.0.1:8000/ingest")


def clamp_text(value, max_length: int) -> str | None:
    if value is None:
        return None
    normalized = " ".join(str(value).replace("\x00", "").split()).strip()
    if not normalized:
        return None
    if len(normalized) <= max_length:
        return normalized
    return normalized[:max_length].rstrip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_file", type=Path)
    parser.add_argument("--court", default="FC", help="A2AJ dataset code, default: FC")
    parser.add_argument("--limit", type=int, default=None, help="Optional cap on imported cases")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def value(record: dict, *names: str):
    for name in names:
        result = record.get(name)
        if result is not None and result != "":
            return result
    return None


def parse_date(value_to_parse) -> date | None:
    if isinstance(value_to_parse, datetime):
        return value_to_parse.date()
    if isinstance(value_to_parse, date):
        return value_to_parse
    if value_to_parse:
        return date.fromisoformat(str(value_to_parse)[:10])
    return None


def parse_datetime(value_to_parse) -> datetime | None:
    if isinstance(value_to_parse, datetime):
        return value_to_parse
    if value_to_parse:
        return datetime.fromisoformat(str(value_to_parse).replace("Z", "+00:00"))
    return None


def parse_version(value_to_parse) -> str | None:
    parsed = parse_datetime(value_to_parse)
    return parsed.isoformat() if parsed else None


def json_safe(value_to_serialize):
    if isinstance(value_to_serialize, (date, datetime)):
        return value_to_serialize.isoformat()
    if isinstance(value_to_serialize, str):
        return value_to_serialize.replace("\x00", "")
    if isinstance(value_to_serialize, dict):
        return {str(key): json_safe(value) for key, value in value_to_serialize.items()}
    if isinstance(value_to_serialize, (list, tuple)):
        return [json_safe(value) for value in value_to_serialize]
    return value_to_serialize


def source_metadata(record: dict) -> dict:
    metadata = {
        key: json_safe(value)
        for key, value in record.items()
        if key not in {"unofficial_text_en", "unofficial_text_fr"}
    }
    metadata.update(
        {
            "a2aj_dataset": record.get("dataset"),
            "verification_status": "a2aj_unverified",
            "verification_notes": (
                "Unofficial A2AJ copy; verify critical information against the official source."
            ),
        }
    )
    return metadata


def build_case(record: dict) -> CaseIngestRequest | None:
    decision_date = parse_date(value(record, "document_date_en", "document_date_fr"))
    full_text = value(record, "unofficial_text_en", "unofficial_text_fr")
    if full_text is not None:
        full_text = str(full_text).replace("\x00", "")
    citation = clamp_text(value(record, "citation_en", "citation_fr"), 255)
    title = clamp_text(value(record, "name_en", "name_fr"), 255) or citation
    if not title or not decision_date or not full_text:
        return None

    full_text_hash = hashlib.sha256(full_text.encode("utf-8")).hexdigest()
    return CaseIngestRequest(
        title=title,
        court=clamp_text(value(record, "dataset"), 255) or "Unknown",
        jurisdiction="Canada",
        date=decision_date,
        citation=citation,
        secondary_citation=clamp_text(value(record, "citation2_en", "citation2_fr"), 255),
        full_text=full_text,
        source_url=clamp_text(value(record, "url_en", "url_fr"), 2048),
        source_name="A2AJ Canadian Legal Data",
        source_id=clamp_text(citation or full_text_hash, 255),
        source_type="a2aj_parquet",
        dataset_version=clamp_text(parse_version(value(record, "scraped_timestamp_en", "scraped_timestamp_fr")), 100),
        upstream_license=value(record, "upstream_license"),
        scraped_at=parse_datetime(value(record, "scraped_timestamp_en", "scraped_timestamp_fr")),
        language="en" if record.get("unofficial_text_en") else "fr",
        full_text_hash=full_text_hash,
        processing_status="raw",
        cases_cited=value(record, "cases_cited_en", "cases_cited_fr"),
        cases_citing=value(record, "cases_citing_en", "cases_citing_fr"),
        citing_cases_count=record.get("citing_cases_count"),
        metadata_json=source_metadata(record),
    )


def post_case(case: CaseIngestRequest, api_url: str = API_URL) -> dict:
    request = Request(
        api_url,
        data=json.dumps(case.model_dump(mode="json")).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request) as response:
        return json.load(response)


def main() -> None:
    args = parse_args()
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    if not args.source_file.exists():
        raise SystemExit(f"Source file does not exist: {args.source_file}")

    with SessionLocal() as session:
        existing_citations = set(session.scalars(select(Case.citation)).all())
        existing_hashes = set(session.scalars(select(Case.full_text_hash)).all())

    selected = imported = skipped = invalid = 0
    parquet = pq.ParquetFile(args.source_file)
    for batch in parquet.iter_batches(batch_size=256):
        for record in batch.to_pylist():
            if value(record, "dataset") != args.court:
                continue
            selected += 1
            case = build_case(record)
            if case is None:
                invalid += 1
                continue
            if case.citation in existing_citations or case.full_text_hash in existing_hashes:
                skipped += 1
                continue
            if args.dry_run:
                print(f"would import: {case.citation or case.title}")
            else:
                result = post_case(case)
                print(f"imported: id={result['id']} citation={result['citation']}")
            existing_citations.add(case.citation)
            existing_hashes.add(case.full_text_hash)
            imported += 1
            if args.limit is not None and imported >= args.limit:
                break
        if args.limit is not None and imported >= args.limit:
            break

    print(f"selected={selected} imported={imported} skipped={skipped} invalid={invalid} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
