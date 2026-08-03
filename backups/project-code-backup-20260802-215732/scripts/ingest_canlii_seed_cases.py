"""Ingest seed immigration cases from CanLII by citation.

Mode A: direct HTML fetch + parse from CanLII case pages.

Notes:
- CanLII may return anti-bot 403 pages for some requests. This script logs those
  failures and continues so you can still ingest whatever is accessible.
- The script posts normalized payloads to the existing local /ingest endpoint.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

import httpx
from bs4 import BeautifulSoup
from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal
from backend.models import CaseIngestRequest
from scripts.import_seed_cases_from_a2aj_api import fetch_a2aj_case as a2aj_fetch_case
from scripts.import_seed_cases_from_a2aj_api import search_a2aj_case as a2aj_search_case
from scripts.ingest_a2aj_parquet import build_case as build_a2aj_case

INGEST_URL = os.getenv("CASELIBRARY_INGEST_URL", "http://127.0.0.1:8000/ingest")
DEFAULT_SEED_CSV = Path("data/eval/seed_cases_extracted.csv")

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)

A2AJ_FETCH_URL = "https://api.a2aj.ca/fetch"
A2AJ_SEARCH_URL = "https://api.a2aj.ca/search"

CANLII_CITATION_RE = re.compile(r"(?P<year>\d{4})\s+CanLII\s+(?P<num>\d+)\s*\((?P<court>SCC|FCA|FC|FCT)\)", re.IGNORECASE)
NEUTRAL_CITATION_RE = re.compile(r"(?P<year>\d{4})\s+(?P<court>SCC|FCA|FC|FCT)\s+(?P<num>\d+)", re.IGNORECASE)


@dataclass
class SeedCase:
    name: str
    listed_citation: str
    citation_hint: str
    url: str | None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-csv", type=Path, default=DEFAULT_SEED_CSV)
    parser.add_argument("--ingest-url", default=INGEST_URL)
    parser.add_argument("--source-type", default="canlii_html_seed")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--delay", type=float, default=1.5)
    parser.add_argument("--timeout", type=float, default=25.0)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--fallback-a2aj", action="store_true", help="Fallback to A2AJ API when CanLII HTML fetch fails")
    parser.add_argument("--a2aj-fetch-url", default=A2AJ_FETCH_URL)
    parser.add_argument("--a2aj-search-url", default=A2AJ_SEARCH_URL)
    parser.add_argument("--a2aj-min-search-score", type=float, default=0.75)
    return parser.parse_args()


def court_path(court_code: str) -> str:
    code = court_code.upper()
    if code == "SCC":
        return "scc"
    if code == "FCA":
        return "fca"
    # FCT is old Federal Court Trial Division; CanLII path is still /fc.
    if code in {"FC", "FCT"}:
        return "fc"
    raise ValueError(f"Unsupported court code: {court_code}")


def canlii_citation_to_url(citation: str) -> str:
    match = CANLII_CITATION_RE.search(citation.strip())
    if not match:
        raise ValueError(f"Unsupported CanLII citation format: {citation}")
    year = match.group("year")
    number = match.group("num")
    court = court_path(match.group("court"))
    doc_id = f"{year}canlii{number}".lower()
    return f"https://www.canlii.org/en/ca/{court}/doc/{year}/{doc_id}/{doc_id}.html"


def neutral_citation_to_url(citation: str) -> str:
    match = NEUTRAL_CITATION_RE.search(citation.strip())
    if not match:
        raise ValueError(f"Unsupported neutral citation format: {citation}")
    year = match.group("year")
    number = match.group("num")
    court_code = match.group("court").upper()
    court = court_path(court_code)
    doc_id = f"{year}{court_code.lower()}{number}".replace("fct", "fc")
    return f"https://www.canlii.org/en/ca/{court}/doc/{year}/{doc_id}/{doc_id}.html"


def extract_citation_hint(listed_citation: str) -> str:
    canlii = CANLII_CITATION_RE.search(listed_citation)
    if canlii:
        year = canlii.group("year")
        number = canlii.group("num")
        court = canlii.group("court").upper()
        return f"{year} CanLII {number} ({court})"
    neutral = NEUTRAL_CITATION_RE.search(listed_citation)
    if neutral:
        year = neutral.group("year")
        number = neutral.group("num")
        court = neutral.group("court").upper()
        return f"{year} {court} {number}"
    return ""


def resolve_seed_url(citation_hint: str) -> str | None:
    if not citation_hint:
        return None
    if "canlii" in citation_hint.lower():
        return canlii_citation_to_url(citation_hint)
    return neutral_citation_to_url(citation_hint)


def load_seed_cases(seed_csv: Path) -> list[SeedCase]:
    if not seed_csv.exists():
        raise SystemExit(f"Seed file not found: {seed_csv}")
    seeds: list[SeedCase] = []
    with seed_csv.open("r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            name = (row.get("name") or "").strip()
            listed = (row.get("listed_citation") or "").strip()
            hint = extract_citation_hint(listed)
            url = None
            try:
                url = resolve_seed_url(hint)
            except Exception:
                url = None
            seeds.append(SeedCase(name=name, listed_citation=listed, citation_hint=hint, url=url))
    return seeds


def fetch_canlii_html(client: httpx.Client, url: str, retries: int, delay: float, verbose: bool = False) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = client.get(url)
            if response.status_code == 200:
                return response.text
            if response.status_code == 403:
                raise RuntimeError("403 anti-bot page returned by CanLII")
            raise RuntimeError(f"HTTP {response.status_code}")
        except Exception as exc:  # noqa: PERF203
            last_error = exc
            if verbose:
                print(f"fetch_retry attempt={attempt} url={url} error={exc}")
            time.sleep(delay)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def _extract_labeled_value(soup: BeautifulSoup, label: str) -> str | None:
    target = f"{label.strip().lower()}:"
    for node in soup.find_all(string=True):
        text = " ".join(str(node).split()).strip().lower()
        if text != target:
            continue
        parent = node.parent
        if parent is None:
            continue
        sibling = parent.find_next_sibling()
        if sibling is not None:
            value = sibling.get_text(" ", strip=True)
            if value:
                return value
        value = parent.get_text(" ", strip=True)
        value = re.sub(rf"^{re.escape(label)}\s*:\s*", "", value, flags=re.IGNORECASE).strip()
        if value:
            return value
    return None


def _parse_date(text: str | None) -> date | None:
    if not text:
        return None
    text = text.strip()
    for fmt in ("%Y-%m-%d", "%Y/%m/%d"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    match = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", text)
    if match:
        return datetime.strptime(match.group(1), "%Y-%m-%d").date()
    return None


def _extract_best_full_text(soup: BeautifulSoup) -> str:
    selectors = [
        "#originalDocument",
        "#decision",
        ".contentBody",
        ".documentcontent",
        ".documentContent",
        "main",
    ]
    best = ""
    for selector in selectors:
        for node in soup.select(selector):
            text = node.get_text("\n", strip=True)
            if len(text) > len(best):
                best = text
    best = re.sub(r"\n{3,}", "\n\n", best).strip()
    return best


def parse_canlii_html(html: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")

    heading = soup.find("h1")
    heading_text = heading.get_text(" ", strip=True) if heading else ""

    source = _extract_labeled_value(soup, "Source") or "Unknown"
    date_text = _extract_labeled_value(soup, "Date")
    decision_date = _parse_date(date_text)

    neutral_match = NEUTRAL_CITATION_RE.search(heading_text)
    neutral = neutral_match.group(0).upper() if neutral_match else ""

    # Example heading:
    # "Canada (...) v. Vavilov, 2019 SCC 65 (CanLII), [2019] 4 SCR 653"
    title = heading_text
    if "," in heading_text:
        title = heading_text.split(",", 1)[0].strip()

    full_text = _extract_best_full_text(soup)
    if len(full_text) < 500:
        raise RuntimeError("Could not extract decision text from HTML")
    if decision_date is None:
        raise RuntimeError("Could not parse decision date")

    return {
        "citation": neutral or None,
        "secondary_citation": None,
        "court": source,
        "decision_date": decision_date,
        "title": title,
        "full_text": full_text,
    }


def build_ingest_request(data: dict[str, Any], url: str, source_type: str, seed_name: str, citation_hint: str) -> CaseIngestRequest:
    full_text = str(data["full_text"])
    full_text_hash = hashlib.sha256(full_text.encode("utf-8")).hexdigest()
    return CaseIngestRequest(
        title=str(data["title"]),
        court=str(data["court"]),
        jurisdiction="Canada",
        date=data["decision_date"],
        citation=data.get("citation"),
        secondary_citation=data.get("secondary_citation"),
        full_text=full_text,
        source_url=url,
        source_name="CanLII",
        source_id=(data.get("citation") or citation_hint or full_text_hash)[:255],
        source_type=source_type,
        dataset_version=None,
        upstream_license="Refer to CanLII Terms of Use and licensing notes.",
        scraped_at=datetime.now(timezone.utc),
        language="en",
        full_text_hash=full_text_hash,
        processing_status="raw",
        metadata_json={
            "ingestion_mode": "canlii_html",
            "seed_case_name": seed_name,
            "seed_citation_hint": citation_hint,
        },
    )


def build_ingest_request_from_a2aj_record(
    record: dict[str, Any],
    source_type: str,
    seed_name: str,
    citation_hint: str,
) -> CaseIngestRequest | None:
    case = build_a2aj_case(record)
    if case is None:
        return None
    payload = case.model_dump(mode="python")
    payload["source_type"] = source_type
    payload["source_name"] = "CanLII via A2AJ API"
    payload["metadata_json"] = {
        **(payload.get("metadata_json") or {}),
        "ingestion_mode": "canlii_html_fallback_a2aj",
        "seed_case_name": seed_name,
        "seed_citation_hint": citation_hint,
    }
    return CaseIngestRequest(**payload)


def resolve_with_a2aj_fallback(
    seed: SeedCase,
    fetch_url: str,
    search_url: str,
    min_search_score: float,
    verbose: bool,
) -> dict[str, Any] | None:
    candidates: list[str] = []
    if seed.citation_hint:
        candidates.append(seed.citation_hint)
    if seed.listed_citation:
        head = seed.listed_citation.split(",", 1)[0].replace("**", "").strip()
        if head:
            candidates.append(head)

    seen: set[str] = set()
    for citation in candidates:
        key = citation.lower()
        if key in seen:
            continue
        seen.add(key)
        try:
            record = a2aj_fetch_case(fetch_url, citation)
        except Exception as exc:
            if verbose:
                print(f"a2aj_fetch_error: citation={citation} error={exc}")
            record = None
        if record is not None:
            return record

    try:
        candidate, citation = a2aj_search_case(
            search_url,
            name=seed.name,
            listed_citation=seed.listed_citation,
            min_score=min_search_score,
        )
    except Exception as exc:
        if verbose:
            print(f"a2aj_search_error: name={seed.name} error={exc}")
        candidate = None
        citation = ""

    if candidate is None:
        return None
    if citation:
        try:
            fetched = a2aj_fetch_case(fetch_url, citation)
        except Exception as exc:
            if verbose:
                print(f"a2aj_fetch_after_search_error: citation={citation} error={exc}")
            fetched = None
        if fetched is not None:
            return fetched
    return candidate


def post_case(ingest_url: str, case: CaseIngestRequest) -> dict[str, Any]:
    request = Request(
        ingest_url,
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

    seeds = load_seed_cases(args.seed_csv)

    with SessionLocal() as session:
        existing_citations = set(session.scalars(select(Case.citation)).all())
        existing_hashes = set(session.scalars(select(Case.full_text_hash)).all())

    checked = imported = skipped = failed = unresolved = 0

    with httpx.Client(
        timeout=args.timeout,
        follow_redirects=True,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-CA,en;q=0.9",
        },
    ) as client:
        for seed in seeds:
            if args.limit is not None and checked >= args.limit:
                break
            checked += 1

            if not seed.url:
                unresolved += 1
                print(f"unresolved_citation: {seed.name} | {seed.listed_citation}")
                continue

            try:
                html = fetch_canlii_html(client, seed.url, retries=args.retries, delay=args.delay, verbose=args.verbose)
                parsed = parse_canlii_html(html)
                request_model = build_ingest_request(
                    parsed,
                    url=seed.url,
                    source_type=args.source_type,
                    seed_name=seed.name,
                    citation_hint=seed.citation_hint,
                )

                if request_model.citation in existing_citations or request_model.full_text_hash in existing_hashes:
                    skipped += 1
                    if args.verbose:
                        print(f"already_present: {request_model.citation or seed.name}")
                    continue

                if args.dry_run:
                    print(f"would_import: {request_model.citation or seed.name} | {seed.url}")
                else:
                    result = post_case(args.ingest_url, request_model)
                    print(f"imported: id={result['id']} citation={result.get('citation')}")

                existing_citations.add(request_model.citation)
                existing_hashes.add(request_model.full_text_hash)
                imported += 1
            except Exception as exc:  # noqa: PERF203
                if args.fallback_a2aj:
                    record = resolve_with_a2aj_fallback(
                        seed,
                        fetch_url=args.a2aj_fetch_url,
                        search_url=args.a2aj_search_url,
                        min_search_score=args.a2aj_min_search_score,
                        verbose=args.verbose,
                    )
                    if record is not None:
                        request_model = build_ingest_request_from_a2aj_record(
                            record,
                            source_type=f"{args.source_type}_fallback",
                            seed_name=seed.name,
                            citation_hint=seed.citation_hint,
                        )
                        if request_model is not None:
                            if request_model.citation in existing_citations or request_model.full_text_hash in existing_hashes:
                                skipped += 1
                                if args.verbose:
                                    print(f"already_present_fallback: {request_model.citation or seed.name}")
                                continue
                            if args.dry_run:
                                print(f"would_import_fallback: {request_model.citation or seed.name}")
                            else:
                                result = post_case(args.ingest_url, request_model)
                                print(f"imported_fallback: id={result['id']} citation={result.get('citation')}")
                            existing_citations.add(request_model.citation)
                            existing_hashes.add(request_model.full_text_hash)
                            imported += 1
                            continue

                failed += 1
                print(f"failed: {seed.name} | {seed.citation_hint or seed.listed_citation} | {exc}")

    print(
        " ".join(
            [
                f"checked={checked}",
                f"imported={imported}",
                f"skipped={skipped}",
                f"failed={failed}",
                f"unresolved={unresolved}",
                f"dry_run={args.dry_run}",
            ]
        )
    )


if __name__ == "__main__":
    main()
