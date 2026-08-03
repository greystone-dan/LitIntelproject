from __future__ import annotations

import logging
import re
import time
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .errors import HumanValidationRequired
from .models import DocumentData

logger = logging.getLogger(__name__)


def _normalize_whitespace(value: str | None) -> str | None:
    if value is None:
        return None
    normalized = " ".join(value.split())
    return normalized or None


def _extract_text(soup: BeautifulSoup) -> str:
    for selector in ("div.decision", "div#decision", "div#content"):
        container = soup.select_one(selector)
        if container is not None:
            return _normalize_whitespace(container.get_text("\n", strip=True)) or ""
    return _normalize_whitespace(soup.get_text("\n", strip=True)) or ""


def _extract_metadata(full_text: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    patterns = [
        ("date", r"Date:\s*(\d{8})", re.IGNORECASE),
        ("docket", r"Docket:\s*([A-Za-z0-9\-]+)", re.IGNORECASE),
        ("reference", r"Reference:\s*([0-9]{4}\s*FC\s*[0-9]+)", re.IGNORECASE),
        ("present", r"PRESENT:\s*(.+)", re.IGNORECASE | re.DOTALL),
        ("between", r"BETWEEN:(.*?)REASONS", re.IGNORECASE | re.DOTALL),
        ("place_of_hearing", r"PLACE OF HEARING:\s*(.+)", re.IGNORECASE | re.DOTALL),
        ("date_of_hearing", r"DATE OF HEARING:\s*(.+)", re.IGNORECASE | re.DOTALL),
        ("dated", r"DATED:\s*(.+)", re.IGNORECASE | re.DOTALL),
    ]
    for key, pattern_text, flags in patterns:
        match = re.search(pattern_text, full_text, flags)
        if match:
            value = _normalize_whitespace(match.group(1))
            if value:
                metadata[key] = value
    return metadata


def _extract_table_metadata(soup: BeautifulSoup) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    for row in soup.select("tr"):
        cells = row.select("th, td")
        if len(cells) < 2:
            continue
        key = _normalize_whitespace(cells[0].get_text(" ", strip=True).rstrip(":"))
        value = _normalize_whitespace(cells[1].get_text(" ", strip=True))
        if key and value:
            metadata[key.lower()] = value
    return metadata


def _extract_pdf_url(document_url: str, soup: BeautifulSoup) -> str:
    for anchor in soup.find_all("a", href=True):
        href = anchor.get("href", "")
        text = anchor.get_text(" ", strip=True).lower()
        href_lower = href.lower()
        if (
            href_lower.endswith(".pdf")
            or "/document.do" in href_lower
            or "pdf" in text
            or "download" in text
        ):
            return urljoin(document_url, href)
    return ""


def fetch_document_page(document_url: str, timeout: float = 60.0, retries: int = 3, backoff_seconds: float = 1.0) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(document_url, headers={"User-Agent": "AI-CaseLibrary-FCIngest/1.0"}, timeout=timeout)
            if response.status_code == 403 and "captcha" in response.text.lower():
                raise HumanValidationRequired(
                    "Lexum requires human CAPTCHA validation before Federal Court judgment ingestion can resume"
                )
            response.raise_for_status()
            return response.text
        except HumanValidationRequired:
            raise
        except requests.RequestException as exc:  # pragma: no cover - exercised in runtime
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise RuntimeError(f"Failed to fetch document page: {document_url}") from last_error


def parse_document_page(document_url: str, html: str) -> DocumentData:
    soup = BeautifulSoup(html, "html.parser")
    heading = soup.select_one("h1, h2")
    title = _normalize_whitespace(heading.get_text(" ", strip=True)) if heading else "Untitled decision"
    full_text = _extract_text(soup)
    metadata = _extract_metadata(full_text)
    metadata.update({k: v for k, v in _extract_table_metadata(soup).items() if k not in metadata})
    pdf_url = _extract_pdf_url(document_url, soup)
    if pdf_url:
        metadata.setdefault("pdf_url", pdf_url)
    metadata.setdefault("document_url", document_url)
    return DocumentData(title=title, full_text=full_text, metadata=metadata)


def scrape_document_page(document_url: str, timeout: float = 60.0, retries: int = 3, backoff_seconds: float = 1.0) -> DocumentData:
    html = fetch_document_page(document_url, timeout=timeout, retries=retries, backoff_seconds=backoff_seconds)
    return parse_document_page(document_url, html)
