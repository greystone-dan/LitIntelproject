from __future__ import annotations

import argparse
import calendar
import logging
import re
import time
from datetime import date, timedelta
from typing import Any
from urllib.parse import urlparse

from backend.database import SessionLocal
from sqlalchemy import text
from .db import SQLiteDb
from .document_scraper import scrape_document_page
from .errors import HumanValidationRequired
from .index_scraper import get_result_count, scrape_index_urls
from .item_scraper import scrape_item_page
from .models import DocumentData, ItemData
from .pdf_downloader import download_pdf

logger = logging.getLogger(__name__)
_FC_ITEM_RE = re.compile(r"/item/(\d+)/", re.IGNORECASE)


def _normalize_fc_item_url(url: str | None) -> str | None:
    if not url:
        return None

    value = str(url).strip()
    if not value:
        return None

    parsed = urlparse(value)
    host = (parsed.netloc or "").lower()
    if "decisions.fct-cf.gc.ca" not in host:
        return None

    match = _FC_ITEM_RE.search(parsed.path)
    if not match:
        return None

    item_id = match.group(1)
    return f"https://decisions.fct-cf.gc.ca/fc-cf/decisions/en/item/{item_id}/index.do"


def load_a2aj_fc_item_urls(limit: int | None = None) -> list[str]:
    """Load canonical FC item URLs from A2AJ-derived case rows in Postgres."""
    session = SessionLocal()
    urls: list[str] = []
    seen: set[str] = set()
    try:
        rows = session.execute(
            text(
                """
            SELECT source_url, metadata_json
            FROM cases
            WHERE source_type LIKE 'a2aj%'
              AND (
                    court ILIKE '%Federal Court%'
                    OR court = 'FC'
                    OR citation ILIKE '% FC %'
                  )
            ORDER BY id
            """
            )
        )
        for source_url, metadata_json in rows:
            metadata = metadata_json or {}
            candidates = [
                source_url,
                metadata.get("source_url"),
                metadata.get("document_url"),
                metadata.get("pdf_url"),
            ]
            for candidate in candidates:
                normalized = _normalize_fc_item_url(candidate)
                if normalized and normalized not in seen:
                    seen.add(normalized)
                    urls.append(normalized)
                    break
            if limit is not None and len(urls) >= limit:
                break
    finally:
        session.close()
    return urls


def _coerce_value(mapping: dict[str, Any] | None, *keys: str) -> str | None:
    if not mapping:
        return None
    for key in keys:
        value = mapping.get(key)
        if value is not None and str(value).strip():
            return str(value).strip()
    return None


def _split_by_quarters(start_date: date, end_date: date) -> list[tuple[date, date]]:
    windows: list[tuple[date, date]] = []
    current = start_date
    while current <= end_date:
        quarter_index = (current.month - 1) // 3
        quarter_start = date(current.year, quarter_index * 3 + 1, 1)
        quarter_end = min(end_date, date(current.year, quarter_index * 3 + 3, 1) - timedelta(days=1))
        windows.append((quarter_start, quarter_end))
        current = quarter_end + timedelta(days=1)
    return windows


def _split_by_months(start_date: date, end_date: date) -> list[tuple[date, date]]:
    windows: list[tuple[date, date]] = []
    current = start_date
    while current <= end_date:
        last_day = calendar.monthrange(current.year, current.month)[1]
        month_end = min(end_date, date(current.year, current.month, last_day))
        windows.append((current, month_end))
        if current.month < 12:
            current = date(current.year, current.month + 1, 1)
        else:
            current = date(current.year + 1, 1, 1)
    return windows


def _build_date_windows(start_date: date, end_date: date, *, depth: int = 0) -> list[tuple[date, date]]:
    """Recursively split date ranges so each window has ≤500 results (Lexum cap)."""
    if start_date > end_date:
        return []
    if depth == 0:
        windows = [(start_date, end_date)]
    elif depth == 1:
        windows = _split_by_quarters(start_date, end_date)
    else:
        windows = _split_by_months(start_date, end_date)

    if depth >= 2:
        return windows

    result: list[tuple[date, date]] = []
    for window_start, window_end in windows:
        count = get_result_count(window_start, window_end)
        logger.info("Date window %s -> %s: %d results", window_start, window_end, count)
        if count > 500:
            result.extend(_build_date_windows(window_start, window_end, depth=depth + 1))
        else:
            result.append((window_start, window_end))
    return result


def _build_decision_record(item: ItemData, document: DocumentData, pdf_url: str, mime_type: str) -> dict[str, Any]:
    metadata = dict(item.metadata)
    # Promote extracted document metadata so key fields (date/citation/docket) can be normalized.
    for key, value in (document.metadata or {}).items():
        metadata.setdefault(key, value)
    metadata["document_metadata"] = document.metadata
    metadata["document_title"] = document.title
    return {
        "fc_id": item.fc_id,
        "neutral_citation": _coerce_value(metadata, "neutral citation", "citation", "neutral_citation"),
        "docket": _coerce_value(metadata, "docket", "docket number", "file numbers", "file number"),
        "decision_date": _coerce_value(metadata, "date", "decision date", "decision_date"),
        "judge": _coerce_value(metadata, "judge", "judges"),
        "style_of_cause": _coerce_value(metadata, "style of cause", "style", "style_of_cause"),
        "item_url": metadata.get("source_url"),
        "document_url": item.document_url,
        "pdf_url": pdf_url,
        "full_text": document.full_text,
        "metadata": metadata,
    }


def _build_pdf_record(decision_record: dict[str, Any], pdf_bytes: bytes, mime_type: str) -> dict[str, Any]:
    metadata = dict(decision_record.get("metadata") or {})
    metadata.setdefault("document_url", decision_record.get("document_url"))
    metadata.setdefault("item_url", decision_record.get("item_url"))
    return {
        "fc_id": decision_record.get("fc_id"),
        "pdf_url": decision_record.get("pdf_url"),
        "pdf_bytes": pdf_bytes,
        "mime_type": mime_type,
        "case_title": decision_record.get("style_of_cause") or metadata.get("style of cause") or "",
        "decision_date": decision_record.get("decision_date") or metadata.get("date") or "",
        "neutral_citation": decision_record.get("neutral_citation") or metadata.get("neutral citation") or "",
        "docket": decision_record.get("docket") or metadata.get("docket") or "",
        "metadata": metadata,
    }


def _ingest_item_url(
    db: SQLiteDb,
    item_url: str,
    *,
    timeout: float,
    retries: int,
    backoff_seconds: float,
    item_delay_seconds: float,
) -> dict[str, Any]:
    fc_id = item_url.rstrip("/").split("/")[-2]
    item = scrape_item_page(item_url, timeout=timeout, retries=retries, backoff_seconds=backoff_seconds)
    time.sleep(item_delay_seconds)
    document_blocked = False
    if item.document_url:
        try:
            document = scrape_document_page(
                item.document_url,
                timeout=timeout,
                retries=retries,
                backoff_seconds=backoff_seconds,
            )
            time.sleep(item_delay_seconds)
        except HumanValidationRequired:
            if item.pdf_url:
                # Preserve a PDF-first path when document rendering is blocked.
                logger.warning(
                    "Document blocked for fc_id=%s; proceeding with PDF-only capture from %s",
                    item.fc_id or fc_id,
                    item.pdf_url,
                )
                document_blocked = True
                document = DocumentData(title=item.title, full_text="", metadata={"document_blocked": True})
            else:
                raise
    else:
        document = DocumentData(title=item.title, full_text="", metadata={})

    pdf_bytes = b""
    mime_type = ""
    pdf_url = item.pdf_url or str(document.metadata.get("pdf_url") or "")
    if pdf_url:
        pdf_bytes, mime_type = download_pdf(
            pdf_url,
            timeout=timeout,
            retries=retries,
            backoff_seconds=backoff_seconds,
        )
        time.sleep(item_delay_seconds)

    decision_record = _build_decision_record(item, document, pdf_url or "", mime_type)
    if document_blocked:
        decision_record.setdefault("metadata", {})["document_blocked"] = True
    db.insert_fc_decision(decision_record)
    if pdf_url and pdf_bytes:
        db.insert_fc_pdf(_build_pdf_record(decision_record, pdf_bytes, mime_type))
    return decision_record


def run_full_ingestion(
    db: SQLiteDb | None = None,
    *,
    start_date: date | None = None,
    end_date: date | None = None,
    max_items: int | None = None,
    timeout: float = 60.0,
    retries: int = 3,
    backoff_seconds: float = 1.0,
    item_delay_seconds: float = 1.5,
    page_delay_seconds: float = 1.0,
    monthly_windows: bool = False,
    a2aj_direct: bool = False,
    a2aj_limit: int | None = None,
) -> list[dict[str, Any]]:
    if db is None:
        db = SQLiteDb("fc_decisions.db")

    today = date.today()
    if start_date is None:
        start_date = date(today.year - 1, 1, 1)
    if end_date is None:
        end_date = today

    windows: list[tuple[date, date]] = []
    if not a2aj_direct:
        logger.info("Starting FC IMM ingestion for %s -> %s", start_date, end_date)
        if monthly_windows:
            # Monthly windows: IMM cases per month are always well under 500, skip probing
            windows = _split_by_months(start_date, end_date)
            logger.info("Using monthly windows (%d total)", len(windows))
        else:
            windows = _build_date_windows(start_date, end_date)
        logger.info("Split into %d date windows", len(windows))
    else:
        logger.info("Starting direct A2AJ -> FC item ingestion")
    if hasattr(db, "get_completed_fc_ids"):
        completed_fc_ids = db.get_completed_fc_ids()
    else:
        completed_fc_ids = db.get_existing_fc_ids()
    inserted: list[dict[str, Any]] = []
    failed_windows = 0

    pending_item_urls = db.get_pending_item_urls() if hasattr(db, "get_pending_item_urls") else []
    if pending_item_urls:
        logger.info("Phase 2: resuming %d incomplete discovered item URLs", len(pending_item_urls))
    for item_url in pending_item_urls:
        if max_items is not None and len(inserted) >= max_items:
            return inserted
        try:
            decision_record = _ingest_item_url(
                db,
                item_url,
                timeout=timeout,
                retries=retries,
                backoff_seconds=backoff_seconds,
                item_delay_seconds=item_delay_seconds,
            )
            inserted.append(decision_record)
            completed_fc_ids.add(decision_record.get("fc_id") or item_url.rstrip("/").split("/")[-2])
            logger.info("Phase 2 ingested pending item total=%d url=%s", len(inserted), item_url)
        except HumanValidationRequired:
            logger.error(
                "Federal Court phase 2 paused: complete Lexum human validation in a browser, then resume this run"
            )
            raise
        except Exception as exc:
            logger.exception("Failed phase 2 ingestion for %s: %s", item_url, exc)

    if a2aj_direct:
        direct_urls = load_a2aj_fc_item_urls(limit=a2aj_limit)
        logger.info("Direct mode: loaded %d candidate item URLs from A2AJ corpus", len(direct_urls))
        for item_url in direct_urls:
            if max_items is not None and len(inserted) >= max_items:
                break
            fc_id = item_url.rstrip("/").split("/")[-2]
            if fc_id in completed_fc_ids:
                logger.debug("Skipping completed fc_id %s", fc_id)
                continue
            try:
                decision_record = _ingest_item_url(
                    db,
                    item_url,
                    timeout=timeout,
                    retries=retries,
                    backoff_seconds=backoff_seconds,
                    item_delay_seconds=item_delay_seconds,
                )
                inserted.append(decision_record)
                completed_fc_ids.add(decision_record.get("fc_id") or fc_id)
                logger.info("Direct-mode ingested fc_id=%s total=%d url=%s", fc_id, len(inserted), item_url)
            except HumanValidationRequired:
                logger.warning(
                    "Direct-mode item blocked by human validation; skipping item_url=%s",
                    item_url,
                )
                continue
            except Exception as exc:
                logger.exception("Failed direct-mode ingestion for %s: %s", item_url, exc)

        logger.info("Completed direct A2AJ FC ingestion: %d decisions inserted", len(inserted))
        return inserted

    logger.info("Phase 1: discovering Federal Court IMM item URLs")
    for window_start, window_end in windows:
        try:
            item_urls = scrape_index_urls(
                window_start, window_end,
                english_only=True,
                timeout=timeout,
                retries=retries,
                backoff_seconds=backoff_seconds,
                page_delay_seconds=page_delay_seconds,
            )
        except HumanValidationRequired:
            logger.error(
                "Federal Court discovery paused: complete Lexum human validation in a browser, then resume this run"
            )
            raise
        except Exception as exc:
            failed_windows += 1
            logger.error("Failed date window %s -> %s: %s", window_start, window_end, exc)
            continue
        logger.info("Window %s -> %s: %d item URLs", window_start, window_end, len(item_urls))
        for item_url in item_urls:
            if max_items is not None and len(inserted) >= max_items:
                break
            fc_id = item_url.rstrip("/").split("/")[-2]
            if fc_id in completed_fc_ids:
                logger.debug("Skipping completed fc_id %s", fc_id)
                continue
            try:
                decision_record = _ingest_item_url(
                    db,
                    item_url,
                    timeout=timeout,
                    retries=retries,
                    backoff_seconds=backoff_seconds,
                    item_delay_seconds=item_delay_seconds,
                )
                inserted.append(decision_record)
                completed_fc_ids.add(decision_record.get("fc_id") or fc_id)
                logger.info("Ingested fc_id=%s  total=%d  url=%s", fc_id, len(inserted), item_url)
            except Exception as exc:
                logger.exception("Failed to ingest %s: %s", item_url, exc)
        if max_items is not None and len(inserted) >= max_items:
            break

    if windows and failed_windows == len(windows):
        raise RuntimeError(f"All {failed_windows} Federal Court date windows failed")
    logger.info("Completed FC IMM ingestion: %d decisions inserted", len(inserted))
    return inserted


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest Federal Court IMM decisions")
    parser.add_argument("--db-path", default="fc_decisions.db")
    parser.add_argument("--start-date", type=date.fromisoformat, default=None)
    parser.add_argument("--end-date", type=date.fromisoformat, default=None)
    parser.add_argument("--max-items", type=int, default=None)
    parser.add_argument("--timeout", type=float, default=60.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--backoff-seconds", type=float, default=1.0)
    parser.add_argument("--item-delay-seconds", type=float, default=1.5)
    parser.add_argument("--page-delay-seconds", type=float, default=1.0)
    parser.add_argument("--monthly", action="store_true",
                        help="Split by calendar month directly (faster startup; safe since IMM results per month << 500)")
    parser.add_argument("--a2aj-direct", action="store_true",
                        help="Bypass discovery windows and ingest directly from A2AJ-linked FC item URLs")
    parser.add_argument("--a2aj-limit", type=int, default=None,
                        help="Optional cap on A2AJ candidate URLs loaded from Postgres")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    db = SQLiteDb(args.db_path)
    run_full_ingestion(
        db,
        start_date=args.start_date,
        end_date=args.end_date,
        max_items=args.max_items,
        timeout=args.timeout,
        retries=args.retries,
        backoff_seconds=args.backoff_seconds,
        item_delay_seconds=args.item_delay_seconds,
        page_delay_seconds=args.page_delay_seconds,
        monthly_windows=args.monthly,
        a2aj_direct=args.a2aj_direct,
        a2aj_limit=args.a2aj_limit,
    )


if __name__ == "__main__":
    main()
