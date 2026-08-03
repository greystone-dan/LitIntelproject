"""Ingest A2AJ records from a paginated API into local /ingest.

This complements parquet ingestion by allowing direct sync from a live A2AJ API.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse
from urllib.request import Request, urlopen

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal
from scripts.ingest_a2aj_parquet import API_URL as DEFAULT_INGEST_URL
from scripts.ingest_a2aj_parquet import build_case, value


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--api-url", default=os.getenv("A2AJ_SOURCE_API_URL"), help="Source A2AJ API endpoint")
    parser.add_argument("--records-path", default="results", help="Dot-path to list of records in API response")
    parser.add_argument("--next-path", default="next", help="Dot-path to next page URL/cursor in API response")
    parser.add_argument("--page-param", default="page", help="Page query parameter name")
    parser.add_argument("--page-start", type=int, default=1)
    parser.add_argument("--page-size-param", default="page_size")
    parser.add_argument("--page-size", type=int, default=200)
    parser.add_argument("--cursor-param", default=None, help="Cursor query parameter name when next-path returns a token")
    parser.add_argument("--court", default=None, help="Optional court filter (e.g. FC)")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--max-pages", type=int, default=None)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--api-key-env", default="A2AJ_API_KEY")
    parser.add_argument("--api-key-header", default="Authorization")
    parser.add_argument("--api-key-prefix", default="Bearer ")
    parser.add_argument("--header", action="append", default=[], help="Extra header as KEY:VALUE")
    parser.add_argument("--ingest-url", default=os.getenv("CASELIBRARY_INGEST_URL", DEFAULT_INGEST_URL))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def nested_get(obj: object, dot_path: str) -> object:
    current = obj
    for token in dot_path.split("."):
        if not token:
            continue
        if isinstance(current, dict):
            current = current.get(token)
        else:
            return None
    return current


def merge_query(base_url: str, params: dict[str, object]) -> str:
    parts = urlparse(base_url)
    current = dict(parse_qsl(parts.query, keep_blank_values=True))
    for key, raw in params.items():
        if raw is None:
            continue
        current[key] = str(raw)
    query = urlencode(current)
    return urlunparse((parts.scheme, parts.netloc, parts.path, parts.params, query, parts.fragment))


def normalize_api_record(record: dict) -> dict:
    normalized = dict(record)
    if "citation_en" not in normalized and "neutral_citation" in normalized:
        normalized["citation_en"] = normalized.get("neutral_citation")
    if "document_date_en" not in normalized and "decision_date" in normalized:
        normalized["document_date_en"] = normalized.get("decision_date")
    if "name_en" not in normalized and "style_of_cause" in normalized:
        normalized["name_en"] = normalized.get("style_of_cause")
    if "unofficial_text_en" not in normalized and "full_text" in normalized:
        normalized["unofficial_text_en"] = normalized.get("full_text")
    if "url_en" not in normalized and "url" in normalized:
        normalized["url_en"] = normalized.get("url")
    if "scraped_timestamp_en" not in normalized and "scraped_at" in normalized:
        normalized["scraped_timestamp_en"] = normalized.get("scraped_at")
    if "cases_cited_en" not in normalized and "cases_cited" in normalized:
        normalized["cases_cited_en"] = normalized.get("cases_cited")
    if "cases_citing_en" not in normalized and "cases_citing" in normalized:
        normalized["cases_citing_en"] = normalized.get("cases_citing")
    if "dataset" not in normalized and "court" in normalized:
        normalized["dataset"] = normalized.get("court")
    return normalized


def parse_headers(extra_headers: list[str], api_key_env: str, api_key_header: str, api_key_prefix: str) -> dict[str, str]:
    headers: dict[str, str] = {"Accept": "application/json"}
    api_key = os.getenv(api_key_env)
    if api_key:
        headers[api_key_header] = f"{api_key_prefix}{api_key}"
    for item in extra_headers:
        if ":" not in item:
            raise SystemExit(f"Invalid --header value: {item}. Expected KEY:VALUE")
        key, raw_value = item.split(":", 1)
        headers[key.strip()] = raw_value.strip()
    return headers


def fetch_json(url: str, headers: dict[str, str], timeout: float) -> object:
    request = Request(url, headers=headers, method="GET")
    with urlopen(request, timeout=timeout) as response:
        return json.load(response)


def post_case(ingest_url: str, payload: dict) -> dict:
    request = Request(
        ingest_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request) as response:
        return json.load(response)


def main() -> None:
    args = parse_args()
    if not args.api_url:
        raise SystemExit("Missing --api-url (or set A2AJ_SOURCE_API_URL)")
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")
    if args.max_pages is not None and args.max_pages < 1:
        raise SystemExit("--max-pages must be at least 1")

    headers = parse_headers(args.header, args.api_key_env, args.api_key_header, args.api_key_prefix)

    with SessionLocal() as session:
        existing_citations = set(session.scalars(select(Case.citation)).all())
        existing_hashes = set(session.scalars(select(Case.full_text_hash)).all())

    selected = imported = skipped = invalid = pages = fetched = 0
    next_url = args.api_url
    page = args.page_start
    cursor: str | None = None

    while next_url:
        if args.max_pages is not None and pages >= args.max_pages:
            break

        query_params: dict[str, object] = {}
        if args.page_param:
            query_params[args.page_param] = page
        if args.page_size_param:
            query_params[args.page_size_param] = args.page_size
        if args.cursor_param and cursor:
            query_params[args.cursor_param] = cursor

        request_url = merge_query(next_url, query_params)
        response = fetch_json(request_url, headers=headers, timeout=args.timeout)
        pages += 1

        if isinstance(response, list):
            records = response
            next_token = None
        elif isinstance(response, dict):
            raw_records = nested_get(response, args.records_path)
            if not isinstance(raw_records, list):
                raise SystemExit(f"records-path '{args.records_path}' did not resolve to a list on page {pages}")
            records = raw_records
            next_token = nested_get(response, args.next_path) if args.next_path else None
        else:
            raise SystemExit(f"Unexpected response type: {type(response)}")

        fetched += len(records)
        if args.verbose:
            print(f"page={pages} fetched_records={len(records)} url={request_url}")

        for raw_record in records:
            if not isinstance(raw_record, dict):
                continue
            record = normalize_api_record(raw_record)
            if args.court and value(record, "dataset", "court") != args.court:
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
                result = post_case(args.ingest_url, case.model_dump(mode="json"))
                print(f"imported: id={result['id']} citation={result['citation']}")

            existing_citations.add(case.citation)
            existing_hashes.add(case.full_text_hash)
            imported += 1

            if args.limit is not None and imported >= args.limit:
                break

        if args.limit is not None and imported >= args.limit:
            break

        if isinstance(next_token, str) and next_token:
            if next_token.startswith("http://") or next_token.startswith("https://"):
                next_url = next_token
                page += 1
                cursor = None
                continue
            if args.cursor_param:
                cursor = next_token
                page += 1
                next_url = args.api_url
                continue

        if len(records) == 0:
            break
        page += 1

    print(
        " ".join(
            [
                f"pages={pages}",
                f"fetched={fetched}",
                f"selected={selected}",
                f"imported={imported}",
                f"skipped={skipped}",
                f"invalid={invalid}",
                f"dry_run={args.dry_run}",
            ]
        )
    )


if __name__ == "__main__":
    main()
