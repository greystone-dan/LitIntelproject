from __future__ import annotations

import logging
import time
from typing import Any
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from .models import ItemData

logger = logging.getLogger(__name__)


def _normalize_whitespace(value: str | None) -> str | None:
    if value is None:
        return None
    normalized = " ".join(value.split())
    return normalized or None


def _extract_metadata(soup: BeautifulSoup) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    for definition_list in soup.select("dl"):
        pairs = []
        terms = definition_list.select("dt")
        descriptions = definition_list.select("dd")
        for index in range(max(len(terms), len(descriptions))):
            term = _normalize_whitespace(terms[index].get_text(" ", strip=True)) if index < len(terms) else None
            description = _normalize_whitespace(descriptions[index].get_text(" ", strip=True)) if index < len(descriptions) else None
            if term and description:
                pairs.append((term, description))
        if pairs:
            for term, description in pairs:
                metadata[term.lower()] = description
    for table in soup.select("table"):
        for row in table.select("tr"):
            cells = [cell.get_text(" ", strip=True) for cell in row.select(["th", "td"])]
            if len(cells) >= 2:
                key = _normalize_whitespace(cells[0].rstrip(":"))
                value = _normalize_whitespace(cells[1])
                if key and value:
                    metadata[key.lower()] = value
    for block in soup.select("div.metadata"):
        text = _normalize_whitespace(block.get_text(" ", strip=True))
        if text:
            metadata["metadata_text"] = text
    return metadata


def _extract_title(soup: BeautifulSoup, metadata: dict[str, Any]) -> str:
    heading = soup.select_one("h1, h2")
    heading_text = _normalize_whitespace(heading.get_text(" ", strip=True)) if heading else None
    citation = metadata.get("neutral citation") or metadata.get("citation")
    style = metadata.get("style of cause") or metadata.get("style")
    if citation and style:
        return f"{citation} — {style}"
    if citation:
        return citation
    if style:
        return style
    return heading_text or "Untitled decision"


def fetch_item_page(item_url: str, timeout: float = 60.0, retries: int = 3, backoff_seconds: float = 1.0) -> str:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(item_url, headers={"User-Agent": "AI-CaseLibrary-FCIngest/1.0"}, timeout=timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as exc:  # pragma: no cover - exercised in runtime
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise RuntimeError(f"Failed to fetch item page: {item_url}") from last_error


def parse_item_page(item_url: str, html: str) -> ItemData:
    soup = BeautifulSoup(html, "html.parser")
    metadata = _extract_metadata(soup)
    title = _extract_title(soup, metadata)

    document_url = ""
    pdf_url = ""
    for anchor in soup.find_all("a", href=True):
        href = anchor.get("href", "")
        if not href:
            continue
        resolved = urljoin(item_url, href)
        if "document.do" in href.lower():
            document_url = resolved
        if href.lower().endswith(".pdf") or "pdf" in anchor.get_text(" ", strip=True).lower():
            pdf_url = resolved

    if not document_url:
        iframe = soup.find("iframe", src=lambda value: value and "iframe=true" in value.lower())
        if iframe:
            document_url = urljoin(item_url, iframe.get("src", ""))

    parsed = urlparse(item_url)
    path_parts = parsed.path.split("/")
    fc_id = path_parts[5] if len(path_parts) > 5 else ""

    metadata.setdefault("source_url", item_url)
    if document_url:
        metadata.setdefault("document_url", document_url)
    if pdf_url:
        metadata.setdefault("pdf_url", pdf_url)

    return ItemData(
        fc_id=fc_id,
        title=title,
        metadata=metadata,
        document_url=document_url,
        pdf_url=pdf_url,
    )


def scrape_item_page(item_url: str, timeout: float = 60.0, retries: int = 3, backoff_seconds: float = 1.0) -> ItemData:
    html = fetch_item_page(item_url, timeout=timeout, retries=retries, backoff_seconds=backoff_seconds)
    return parse_item_page(item_url, html)
