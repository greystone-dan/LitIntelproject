from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://www.fct-cf.ca/en/court-files-and-decisions/court-files"
ROBOTS_URL = "https://www.fct-cf.ca/robots.txt"
USER_AGENT = "AI-CaseLibrary-FCCollector/1.0 (+research; contact-local-admin)"


@dataclass
class CollectorConfig:
    prefixes: list[str]
    delay_ms: int
    max_pages: int | None
    max_records: int | None
    timeout: float
    retries: int
    backoff_seconds: float
    output_jsonl: Path
    checkpoint_json: Path
    expand_details: bool
    emit_import_ready: bool
    incremental_prefix_window: int | None
    incremental_run_id: int | None
    ignore_robots: bool


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Collect Federal Court file numbers and optional detail pages")
    parser.add_argument("--prefixes", default="IMM,T,A", help="Comma-separated file prefixes")
    parser.add_argument("--delay-ms", type=int, default=1200, help="Delay between requests in ms")
    parser.add_argument("--max-pages", type=int, default=None, help="Optional max pages per prefix")
    parser.add_argument("--max-records", type=int, default=None, help="Optional max total file-number records")
    parser.add_argument("--timeout", type=float, default=20.0, help="Request timeout in seconds")
    parser.add_argument("--retries", type=int, default=3, help="Retry attempts per request")
    parser.add_argument("--backoff-seconds", type=float, default=1.0, help="Backoff seconds between retries")
    parser.add_argument(
        "--output-jsonl",
        type=Path,
        default=Path("data/raw/fc/portal_file_numbers.jsonl"),
        help="Output JSONL path",
    )
    parser.add_argument(
        "--checkpoint-json",
        type=Path,
        default=Path("data/raw/fc/portal_checkpoint.json"),
        help="Checkpoint JSON path",
    )
    parser.add_argument("--expand-details", action="store_true", help="Fetch and parse each detail page")
    parser.add_argument(
        "--emit-import-ready",
        action="store_true",
        help="Emit stage=import_ready rows mapped to scripts/import_fc_decisions.py field names",
    )
    parser.add_argument(
        "--incremental-prefix-window",
        type=int,
        default=None,
        help="Rotate across this many prefixes per run (checkpoint-backed)",
    )
    parser.add_argument(
        "--incremental-run-id",
        type=int,
        default=None,
        help="Optional explicit run id for deterministic prefix rotation",
    )
    parser.add_argument("--ignore-robots", action="store_true", help="Skip robots.txt safety check")
    return parser.parse_args()


def build_config(args: argparse.Namespace) -> CollectorConfig:
    prefixes = [item.strip().upper() for item in args.prefixes.split(",") if item.strip()]
    if not prefixes:
        raise ValueError("At least one prefix is required")
    return CollectorConfig(
        prefixes=prefixes,
        delay_ms=max(0, args.delay_ms),
        max_pages=args.max_pages,
        max_records=args.max_records,
        timeout=max(1.0, args.timeout),
        retries=max(1, args.retries),
        backoff_seconds=max(0.0, args.backoff_seconds),
        output_jsonl=args.output_jsonl,
        checkpoint_json=args.checkpoint_json,
        expand_details=bool(args.expand_details),
        emit_import_ready=bool(args.emit_import_ready),
        incremental_prefix_window=(
            max(1, args.incremental_prefix_window) if args.incremental_prefix_window is not None else None
        ),
        incremental_run_id=args.incremental_run_id,
        ignore_robots=bool(args.ignore_robots),
    )


def select_prefixes_for_run(config: CollectorConfig, checkpoint: dict[str, Any]) -> list[str]:
    prefixes = list(config.prefixes)
    window = config.incremental_prefix_window
    if not window or window >= len(prefixes):
        return prefixes

    if config.incremental_run_id is not None:
        run_id = max(0, int(config.incremental_run_id))
    else:
        run_id = int(checkpoint.get("rotation_run", 0))
        checkpoint["rotation_run"] = run_id + 1

    start = (run_id * window) % len(prefixes)
    selected: list[str] = []
    for offset in range(window):
        selected.append(prefixes[(start + offset) % len(prefixes)])
    return selected


def load_checkpoint(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"prefix_page": {}, "records_written": 0}
    return json.loads(path.read_text(encoding="utf-8"))


def save_checkpoint(path: Path, checkpoint: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(checkpoint, indent=2), encoding="utf-8")


def load_seen_file_numbers(path: Path) -> set[str]:
    seen: set[str] = set()
    if not path.exists():
        return seen
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except Exception:
                continue
            number = str(row.get("file_number") or "").strip()
            if number:
                seen.add(number)
    return seen


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=True) + "\n")


def request_with_retry(
    client: httpx.Client,
    url: str,
    *,
    params: dict[str, Any] | None,
    retries: int,
    backoff_seconds: float,
) -> httpx.Response:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = client.get(url, params=params)
            response.raise_for_status()
            return response
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt == retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise RuntimeError(f"Request failed for {url}") from last_error


def is_allowed_by_robots(client: httpx.Client, target_path_fragment: str = "/court-files") -> bool:
    try:
        response = client.get(ROBOTS_URL)
        response.raise_for_status()
    except Exception:
        # Conservative default: if robots is unavailable, do not block.
        return True

    disallowed: list[str] = []
    active_star = False
    for raw in response.text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        lower = line.lower()
        if lower.startswith("user-agent:"):
            agent = line.split(":", 1)[1].strip()
            active_star = agent == "*"
        elif active_star and lower.startswith("disallow:"):
            path = line.split(":", 1)[1].strip()
            if path:
                disallowed.append(path)

    for path in disallowed:
        if target_path_fragment.startswith(path) or target_path_fragment in path:
            return False
    return True


def parse_listing_entries(html: str, prefix: str, base_url: str = BASE_URL) -> list[dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup.select("a.court-file-number")
    if not anchors:
        anchors = soup.find_all("a")

    entries: list[dict[str, str]] = []
    for anchor in anchors:
        text = anchor.get_text(" ", strip=True)
        if not text.startswith(prefix + "-"):
            continue
        href = anchor.get("href")
        entry: dict[str, str] = {"file_number": text}
        if href:
            entry["detail_url"] = urljoin(base_url, href)
        entries.append(entry)

    # Keep insertion order and uniqueness by file number.
    deduped: list[dict[str, str]] = []
    seen: set[str] = set()
    for item in entries:
        number = item["file_number"]
        if number in seen:
            continue
        seen.add(number)
        deduped.append(item)
    return deduped


def parse_detail_page(html: str, url: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else None
    headings = [h.get_text(" ", strip=True) for h in soup.find_all(["h1", "h2"]) if h.get_text(strip=True)]

    # Extract common label/value metadata from tables, definition lists, and text lines.
    labels: dict[str, str] = {}
    for row in soup.find_all("tr"):
        cells = row.find_all(["th", "td"])
        if len(cells) < 2:
            continue
        key = cells[0].get_text(" ", strip=True).rstrip(":").strip().lower()
        value = cells[1].get_text(" ", strip=True)
        if key and value and key not in labels:
            labels[key] = value

    dts = soup.find_all("dt")
    for dt in dts:
        dd = dt.find_next_sibling("dd")
        if not dd:
            continue
        key = dt.get_text(" ", strip=True).rstrip(":").strip().lower()
        value = dd.get_text(" ", strip=True)
        if key and value and key not in labels:
            labels[key] = value

    for node in soup.find_all(["li", "p"]):
        text = node.get_text(" ", strip=True)
        if ":" not in text:
            continue
        maybe_key, maybe_value = text.split(":", 1)
        key = maybe_key.strip().lower()
        value = maybe_value.strip()
        if key and value and len(key) < 64 and key not in labels:
            labels[key] = value

    paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
    text_excerpt = "\n\n".join(paragraphs[:8]).strip()[:10000] if paragraphs else None

    decision_links: list[str] = []
    for anchor in soup.find_all("a"):
        href = anchor.get("href")
        if not href:
            continue
        href_abs = urljoin(url, href)
        href_lower = href_abs.lower()
        if any(token in href_lower for token in ["decision", "judgment", "/eng/", ".pdf"]):
            decision_links.append(href_abs)

    # Keep unique link order.
    unique_links: list[str] = []
    seen: set[str] = set()
    for item in decision_links:
        if item in seen:
            continue
        seen.add(item)
        unique_links.append(item)

    return {
        "page_title": title,
        "headings": headings[:10],
        "decision_links": unique_links[:25],
        "labels": labels,
        "text_excerpt": text_excerpt,
    }


def _label_value(labels: dict[str, str], *keys: str) -> str | None:
    for key in keys:
        value = labels.get(key)
        if value:
            return value.strip()
    return None


def _normalize_date(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return value

    for pattern in ("%B %d, %Y", "%b %d, %Y", "%Y/%m/%d", "%d %B %Y", "%d %b %Y"):
        try:
            parsed = datetime.strptime(value, pattern)
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return None


def build_import_ready_record(listing_row: dict[str, Any], detail_row: dict[str, Any]) -> dict[str, Any]:
    labels = detail_row.get("labels") if isinstance(detail_row.get("labels"), dict) else {}
    if not isinstance(labels, dict):
        labels = {}

    neutral_citation = _label_value(
        labels,
        "neutral citation",
        "citation",
        "file citation",
    )
    if not neutral_citation:
        match = re.search(r"\b\d{4}\s+FC\s+\d+\b", detail_row.get("page_title") or "")
        neutral_citation = match.group(0) if match else None

    decision_date = _normalize_date(
        _label_value(labels, "date", "decision date", "date of decision", "file date")
    )
    title = _label_value(labels, "style of cause", "case title", "title")
    if not title:
        title = (detail_row.get("headings") or [None])[0]
    if not title:
        title = detail_row.get("page_title") or listing_row.get("file_number") or "Untitled Federal Court file"

    return {
        "style_of_cause": str(title).strip(),
        "neutral_citation": neutral_citation,
        "decision_date": decision_date,
        "full_text": detail_row.get("text_excerpt"),
        "docket_number": listing_row.get("file_number"),
        "url": listing_row.get("detail_url"),
        "court": "Federal Court",
        "jurisdiction": "Canada",
        "language": "en",
        "dataset": "fc_portal",
        "source_id": listing_row.get("file_number"),
    }


def run_collection(config: CollectorConfig) -> tuple[int, int]:
    headers = {"User-Agent": USER_AGENT}
    checkpoint = load_checkpoint(config.checkpoint_json)
    checkpoint_records_base = int(checkpoint.get("records_written", 0))
    prefix_page = checkpoint.setdefault("prefix_page", {})
    seen_numbers = load_seen_file_numbers(config.output_jsonl)

    written = 0
    scanned = 0

    with httpx.Client(timeout=config.timeout, headers=headers, follow_redirects=True) as client:
        if not config.ignore_robots and not is_allowed_by_robots(client):
            raise RuntimeError("robots.txt disallows /court-files crawling; use --ignore-robots only if authorized")

        prefixes_to_scan = select_prefixes_for_run(config, checkpoint)
        for prefix in prefixes_to_scan:
            page = int(prefix_page.get(prefix, 1))
            pages_seen = 0

            while True:
                if config.max_pages is not None and pages_seen >= config.max_pages:
                    break
                if config.max_records is not None and written >= config.max_records:
                    break

                response = request_with_retry(
                    client,
                    BASE_URL,
                    params={"court-file-number": prefix, "page": page},
                    retries=config.retries,
                    backoff_seconds=config.backoff_seconds,
                )
                entries = parse_listing_entries(response.text, prefix=prefix, base_url=BASE_URL)
                scanned += len(entries)

                if not entries:
                    break

                for entry in entries:
                    number = entry["file_number"]
                    if number in seen_numbers:
                        continue

                    row = {
                        "stage": "listing",
                        "collected_at": utc_now_iso(),
                        "prefix": prefix,
                        "page": page,
                        "file_number": number,
                        "detail_url": entry.get("detail_url"),
                    }
                    append_jsonl(config.output_jsonl, row)
                    seen_numbers.add(number)
                    written += 1

                    if config.expand_details and entry.get("detail_url"):
                        try:
                            detail_resp = request_with_retry(
                                client,
                                entry["detail_url"],
                                params=None,
                                retries=config.retries,
                                backoff_seconds=config.backoff_seconds,
                            )
                            detail = parse_detail_page(detail_resp.text, entry["detail_url"])
                            append_jsonl(
                                config.output_jsonl,
                                {
                                    "stage": "detail",
                                    "collected_at": utc_now_iso(),
                                    "file_number": number,
                                    "detail_url": entry["detail_url"],
                                    **detail,
                                },
                            )
                            if config.emit_import_ready:
                                import_ready = build_import_ready_record(entry, detail)
                                append_jsonl(
                                    config.output_jsonl,
                                    {
                                        "stage": "import_ready",
                                        "collected_at": utc_now_iso(),
                                        **import_ready,
                                    },
                                )
                        except Exception as exc:  # noqa: BLE001
                            append_jsonl(
                                config.output_jsonl,
                                {
                                    "stage": "detail_error",
                                    "collected_at": utc_now_iso(),
                                    "file_number": number,
                                    "detail_url": entry["detail_url"],
                                    "error": str(exc),
                                },
                            )

                    if config.max_records is not None and written >= config.max_records:
                        break

                page += 1
                pages_seen += 1
                prefix_page[prefix] = page
                checkpoint["records_written"] = checkpoint_records_base + written
                save_checkpoint(config.checkpoint_json, checkpoint)

                if config.max_records is not None and written >= config.max_records:
                    break

                if config.delay_ms > 0:
                    time.sleep(config.delay_ms / 1000)

    return scanned, written


def main() -> None:
    args = parse_args()
    config = build_config(args)
    scanned, written = run_collection(config)
    print(f"Scanned={scanned} Written={written} Output={config.output_jsonl}")


if __name__ == "__main__":
    main()
