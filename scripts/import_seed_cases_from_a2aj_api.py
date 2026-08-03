"""Import missing seed cases via A2AJ REST API /fetch.

Designed for targeted backfill of known citations (not bulk scraping).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import pandas as pd
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal
from scripts.ingest_a2aj_parquet import API_URL as DEFAULT_INGEST_URL
from scripts.ingest_a2aj_parquet import build_case

A2AJ_FETCH_URL = "https://api.a2aj.ca/fetch"
A2AJ_SEARCH_URL = "https://api.a2aj.ca/search"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--missing-csv", type=Path, default=Path("data/eval/reports/seed_case_missing_exact.csv"))
    parser.add_argument("--a2aj-fetch-url", default=A2AJ_FETCH_URL)
    parser.add_argument("--a2aj-search-url", default=A2AJ_SEARCH_URL)
    parser.add_argument("--min-search-score", type=float, default=0.75)
    parser.add_argument("--ingest-url", default=os.getenv("CASELIBRARY_INGEST_URL", DEFAULT_INGEST_URL))
    parser.add_argument("--source-type", default="a2aj_api_seed")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def fetch_a2aj_case(fetch_url: str, citation: str) -> dict | None:
    query = urlencode({
        "citation": citation,
        "doc_type": "cases",
        "output_language": "en",
    })
    request = Request(f"{fetch_url}?{query}", method="GET")
    with urlopen(request, timeout=60) as response:
        payload = json.load(response)
    results = payload.get("results") or []
    if not results:
        return None
    first = results[0]
    if not isinstance(first, dict):
        return None
    return first


def normalize_name(text: str) -> str:
    lowered = text.lower()
    lowered = re.sub(r"\s*\([^)]*\)", "", lowered)
    lowered = re.sub(r"[^a-z0-9\s]", " ", lowered)
    lowered = re.sub(r"\s+", " ", lowered).strip()
    return lowered


def significant_tokens(name: str) -> list[str]:
    stopwords = {
        "canada",
        "minister",
        "citizenship",
        "immigration",
        "employment",
        "attorney",
        "general",
        "public",
        "safety",
        "preparedness",
        "manpower",
        "and",
        "the",
        "of",
        "re",
        "v",
    }
    tokens = [token for token in normalize_name(name).split(" ") if len(token) >= 4]
    return [token for token in tokens if token not in stopwords]


def infer_dataset_filter(listed_citation: str) -> str:
    upper = listed_citation.upper()
    if "SCC" in upper:
        return "SCC"
    if "F.C.A" in upper or "FCA" in upper:
        return "FCA"
    if "FCT" in upper:
        return "FC"
    if " FC " in f" {upper} ":
        return "FC"
    return ""


def parse_expected_year(listed_citation: str) -> int | None:
    match = re.search(r"\b(19|20)\d{2}\b", listed_citation)
    if not match:
        return None
    return int(match.group(0))


def search_a2aj_case(
    search_url: str,
    name: str,
    listed_citation: str,
    min_score: float,
) -> tuple[dict | None, str]:
    dataset = infer_dataset_filter(listed_citation)
    expected_year = parse_expected_year(listed_citation)
    params = {
        "query": name,
        "search_type": "name",
        "doc_type": "cases",
        "size": 20,
        "search_language": "en",
    }
    if dataset:
        params["dataset"] = dataset

    request = Request(f"{search_url}?{urlencode(params)}", method="GET")
    with urlopen(request, timeout=60) as response:
        payload = json.load(response)
    results = payload.get("results") or []
    if not results:
        return None, ""

    seed_tokens = significant_tokens(name)

    best: dict | None = None
    best_rank = -1.0
    for item in results:
        if not isinstance(item, dict):
            continue
        score = float(item.get("score") or 0.0)
        candidate_name = str(item.get("name_en") or "")
        normalized_candidate = normalize_name(candidate_name)
        token_hits = sum(1 for token in seed_tokens if token in normalized_candidate)
        overlap = (token_hits / len(seed_tokens)) if seed_tokens else 0.0
        year_bonus = 0
        year_match_ok = True
        if expected_year is not None:
            date_text = str(item.get("document_date_en") or "")
            year_match = re.search(r"\b(19|20)\d{2}\b", date_text)
            if year_match and abs(int(year_match.group(0)) - expected_year) <= 1:
                year_bonus = 2
            else:
                year_match_ok = False

        if not year_match_ok:
            continue
        if seed_tokens and overlap < 0.5:
            continue
        rank = score + (0.03 * token_hits) + (0.05 * year_bonus)
        if rank > best_rank:
            best_rank = rank
            best = item

    if best is None:
        return None, ""

    if float(best.get("score") or 0.0) < min_score:
        return None, ""

    return best, str(best.get("citation_en") or "")


def list_candidate_citations(row: pd.Series) -> list[str]:
    candidates: list[str] = []
    neutral = str(row.get("neutral_citation", "") or "").strip()
    if neutral and neutral.lower() != "nan":
        candidates.append(neutral)

    listed = str(row.get("listed_citation", "") or "").strip()
    listed = listed.replace("**", "")
    leading = listed.split(",", 1)[0].strip()
    if leading:
        candidates.append(leading)

    # Deduplicate while preserving order.
    deduped: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        key = candidate.lower()
        if key in seen:
            continue
        seen.add(key)
        deduped.append(candidate)
    return deduped


def post_case(ingest_url: str, payload: dict) -> dict:
    request = Request(
        ingest_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=60) as response:
        return json.load(response)


def main() -> None:
    args = parse_args()
    if not args.missing_csv.exists():
        raise SystemExit(f"Missing CSV not found: {args.missing_csv}")
    if args.limit is not None and args.limit < 1:
        raise SystemExit("--limit must be at least 1")

    missing = pd.read_csv(args.missing_csv)

    with SessionLocal() as session:
        existing_citations = set(session.scalars(select(Case.citation)).all())
        existing_hashes = set(session.scalars(select(Case.full_text_hash)).all())

    processed = imported = fetched = skipped_existing = not_found = invalid = 0

    for _, row in missing.iterrows():
        if args.limit is not None and processed >= args.limit:
            break
        processed += 1

        name = str(row.get("name", "") or "").strip()
        listed_citation = str(row.get("listed_citation", "") or "").strip()
        candidates = list_candidate_citations(row)
        fetched_record: dict | None = None
        fetched_with = ""

        for candidate in candidates:
            try:
                response_record = fetch_a2aj_case(args.a2aj_fetch_url, candidate)
            except Exception as exc:
                if args.verbose:
                    print(f"fetch_error: name={name} citation={candidate} error={exc}")
                continue
            if response_record:
                fetched_record = response_record
                fetched_with = candidate
                break

        if fetched_record is None:
            try:
                found_via_search, search_citation = search_a2aj_case(
                    args.a2aj_search_url,
                    name=name,
                    listed_citation=listed_citation,
                    min_score=args.min_search_score,
                )
            except Exception as exc:
                found_via_search = None
                search_citation = ""
                if args.verbose:
                    print(f"search_error: name={name} error={exc}")

            if found_via_search is None:
                not_found += 1
                print(f"not_found: {name}")
                continue

            fetched_with = search_citation or name
            if search_citation:
                try:
                    fetched_record = fetch_a2aj_case(args.a2aj_fetch_url, search_citation)
                except Exception as exc:
                    fetched_record = None
                    if args.verbose:
                        print(f"fetch_after_search_error: name={name} citation={search_citation} error={exc}")
            if fetched_record is None:
                # Keep fallback for rare cases where /fetch doesn't return but search does.
                fetched_record = found_via_search

        fetched += 1
        case = build_case(fetched_record)
        if case is None:
            invalid += 1
            print(f"invalid_payload: {name} (citation={fetched_with})")
            continue

        if case.citation in existing_citations or case.full_text_hash in existing_hashes:
            skipped_existing += 1
            if args.verbose:
                print(f"already_present: {case.citation or name}")
            continue

        payload = case.model_dump(mode="json")
        payload["source_type"] = args.source_type
        payload["source_name"] = "A2AJ Canadian Legal Data API"
        payload["metadata_json"] = {
            **(payload.get("metadata_json") or {}),
            "seed_import": True,
            "seed_case_name": name,
            "seed_lookup_citation": fetched_with,
        }

        if args.dry_run:
            print(f"would_import: {name} | {payload.get('citation')}")
        else:
            result = post_case(args.ingest_url, payload)
            print(f"imported: id={result['id']} citation={result.get('citation')}")

        existing_citations.add(case.citation)
        existing_hashes.add(case.full_text_hash)
        imported += 1

    print(
        " ".join(
            [
                f"processed={processed}",
                f"fetched={fetched}",
                f"imported={imported}",
                f"skipped_existing={skipped_existing}",
                f"not_found={not_found}",
                f"invalid={invalid}",
                f"dry_run={args.dry_run}",
            ]
        )
    )


if __name__ == "__main__":
    main()
