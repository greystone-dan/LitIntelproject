from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path
from typing import Any

import httpx


def normalize_record(record: dict[str, Any]) -> dict[str, Any] | None:
    stage = str(record.get("stage") or "").strip().lower()
    if not stage:
        return record

    if stage == "import_ready":
        return {
            "style_of_cause": record.get("style_of_cause") or record.get("title"),
            "neutral_citation": record.get("neutral_citation") or record.get("citation"),
            "decision_date": record.get("decision_date") or record.get("date"),
            "full_text": record.get("full_text") or record.get("text"),
            "docket_number": record.get("docket_number") or record.get("source_id"),
            "url": record.get("url") or record.get("source_url"),
            "court": record.get("court") or "Federal Court",
            "jurisdiction": record.get("jurisdiction") or "Canada",
            "language": record.get("language") or "en",
            "dataset": record.get("dataset") or "fc_portal",
            "source_id": record.get("source_id"),
        }

    if stage in {"listing", "detail", "detail_error"}:
        return None

    return record


def load_records(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, list):
            return [item for item in payload if isinstance(item, dict)]
        if isinstance(payload, dict):
            return [payload]
        raise ValueError("JSON input must be an object or array of objects")

    if suffix == ".jsonl":
        out: list[dict[str, Any]] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            if isinstance(record, dict):
                normalized = normalize_record(record)
                if normalized:
                    out.append(normalized)
        return out

    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]

    raise ValueError(f"Unsupported file type: {suffix}")


def to_ingest_payload(record: dict[str, Any], source_name: str) -> dict[str, Any]:
    citation = str(record.get("neutral_citation") or record.get("citation") or "").strip()
    source_url = str(record.get("url") or record.get("source_url") or "").strip()

    return {
        "title": str(record.get("style_of_cause") or record.get("title") or "Untitled case").strip(),
        "court": str(record.get("court") or "Federal Court").strip(),
        "jurisdiction": str(record.get("jurisdiction") or "Canada").strip(),
        "date": record.get("decision_date") or record.get("date"),
        "citation": citation or None,
        "secondary_citation": record.get("secondary_citation"),
        "summary": record.get("summary") or None,
        "full_text": record.get("full_text") or record.get("text") or None,
        "source_url": source_url or None,
        "source_name": source_name,
        "source_id": record.get("source_id") or record.get("docket_number") or citation or source_url or None,
        "source_type": "federal_court",
        "language": record.get("language") or "en",
        "metadata_json": {
            "docket_number": record.get("docket_number"),
            "judges": record.get("judges"),
            "keywords": record.get("keywords"),
            "dataset": record.get("dataset") or "fc_import",
        },
    }


def dedupe_key(payload: dict[str, Any]) -> str:
    return (
        str(payload.get("source_id") or payload.get("citation") or payload.get("source_url") or payload.get("title"))
        .strip()
        .lower()
    )


def import_records(
    records: list[dict[str, Any]],
    base_url: str,
    source_name: str,
    sleep_ms: int,
    timeout: float,
) -> tuple[int, int, int]:
    success = 0
    skipped = 0
    failed = 0
    seen: set[str] = set()

    with httpx.Client(timeout=timeout) as client:
        for record in records:
            payload = to_ingest_payload(record, source_name)
            if not payload.get("date") or not (payload.get("summary") or payload.get("full_text")):
                skipped += 1
                continue

            key = dedupe_key(payload)
            if key in seen:
                skipped += 1
                continue
            seen.add(key)

            try:
                response = client.post(f"{base_url.rstrip('/')}/ingest", json=payload)
                if response.status_code in {200, 201}:
                    success += 1
                elif response.status_code == 409:
                    skipped += 1
                else:
                    failed += 1
            except Exception:
                failed += 1

            if sleep_ms > 0:
                time.sleep(sleep_ms / 1000)

    return success, skipped, failed


def main() -> None:
    parser = argparse.ArgumentParser(description="Import Federal Court decisions into /ingest")
    parser.add_argument("--input", type=Path, required=True, help="Input file (.json, .jsonl, .csv)")
    parser.add_argument("--base-url", default="http://127.0.0.1:8000", help="API base URL")
    parser.add_argument("--source-name", default="Federal Court import", help="source_name value for records")
    parser.add_argument("--sleep-ms", type=int, default=25, help="Delay between requests")
    parser.add_argument("--timeout", type=float, default=60.0, help="HTTP timeout seconds")
    args = parser.parse_args()

    records = load_records(args.input)
    success, skipped, failed = import_records(
        records=records,
        base_url=args.base_url,
        source_name=args.source_name,
        sleep_ms=args.sleep_ms,
        timeout=args.timeout,
    )

    print(f"Imported={success} Skipped={skipped} Failed={failed}")


if __name__ == "__main__":
    main()
