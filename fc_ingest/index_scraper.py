from __future__ import annotations

import logging
import re
import time
from datetime import date
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from .errors import HumanValidationRequired

BASE_ROOT = "https://decisions.fct-cf.gc.ca"
# &iframe=true makes the server render real search results instead of the JS shell.
# The search uses:
#   ref=IMM  -> file number prefix filter (IMM = immigration cases only)
#   col=54   -> Federal Court Decisions collection
#   page=N   -> pagination (NOT p=N)
#   iframe=true -> server-rendered results mode
INDEX_URL = f"{BASE_ROOT}/fc-cf/en/d/s/index.do"
RESULTS_PER_PAGE = 25
MAX_SAFE_RESULTS = 500  # Lexum caps results at 500; split date windows if over this

logger = logging.getLogger(__name__)

_SESSION = requests.Session()
_SESSION.headers.update({
    "User-Agent": "AI-CaseLibrary-FCIngest/1.0 (research; polite crawler; contact: admin@example.com)",
    "Referer": f"{BASE_ROOT}/fc-cf/en/d/s/index.do?col=54",
})


def _build_params(start_date: date, end_date: date, page: int) -> dict:
    return {
        "cont": "",
        "ref": "IMM",
        "d1": start_date.strftime("%Y-%m-%d"),
        "d2": end_date.strftime("%Y-%m-%d"),
        "p": "",
        "col": 54,
        "or": "",
        "page": page,
        "iframe": "true",
    }


def fetch_index_page(
    start_date: date,
    end_date: date,
    page: int = 1,
    timeout: float = 60.0,
    retries: int = 3,
    backoff_seconds: float = 1.0,
) -> str:
    params = _build_params(start_date, end_date, page)
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = _SESSION.get(INDEX_URL, params=params, timeout=timeout)
            if response.status_code == 403 and "captcha" in response.text.lower():
                raise HumanValidationRequired(
                    "Lexum requires human CAPTCHA validation before Federal Court index discovery can resume"
                )
            response.raise_for_status()
            return response.text
        except HumanValidationRequired:
            raise
        except requests.RequestException as exc:
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise RuntimeError(
        f"Failed to fetch index page {page} for {start_date} -> {end_date}"
    ) from last_error


def parse_result_count(html: str) -> int:
    """Extract total result count from the iframe HTML (e.g. '89 result(s)')."""
    m = re.search(r"(\d[\d,]*)\s+result", html, re.IGNORECASE)
    if m:
        return int(m.group(1).replace(",", ""))
    return 0


def parse_index_page(html: str, *, english_only: bool = True) -> list[str]:
    """Return item-page URLs from one rendered search-results page.

    Skips French-language items (/fr/ path) when english_only=True.
    """
    soup = BeautifulSoup(html, "html.parser")
    item_urls: list[str] = []
    for anchor in soup.find_all("a", href=True):
        href: str = anchor.get("href", "")
        if "/item/" not in href:
            continue
        if english_only and "/decisions/fr/" in href:
            continue
        item_url = urljoin(BASE_ROOT, href)
        parsed = urlparse(item_url)
        if parsed.scheme and parsed.netloc:
            item_urls.append(item_url)
    return list(dict.fromkeys(item_urls))


def get_result_count(start_date: date, end_date: date, timeout: float = 60.0) -> int:
    """Fetch page 1 just to get the total result count for this date window."""
    html = fetch_index_page(start_date, end_date, page=1, timeout=timeout)
    return parse_result_count(html)


def scrape_index_urls(
    start_date: date,
    end_date: date,
    *,
    max_pages: int | None = None,
    english_only: bool = True,
    timeout: float = 60.0,
    retries: int = 3,
    backoff_seconds: float = 1.0,
    page_delay_seconds: float = 1.0,
) -> list[str]:
    """Fetch all item URLs for the given date window, paginating as needed."""
    item_urls: list[str] = []
    page = 1
    while True:
        if max_pages is not None and page > max_pages:
            break
        html = fetch_index_page(
            start_date, end_date, page=page,
            timeout=timeout, retries=retries, backoff_seconds=backoff_seconds,
        )
        page_urls = parse_index_page(html, english_only=english_only)
        logger.debug("Index page %d for %s->%s: %d items", page, start_date, end_date, len(page_urls))
        if not page_urls:
            break
        item_urls.extend(page_urls)
        page += 1
        if page_delay_seconds > 0:
            time.sleep(page_delay_seconds)
    return item_urls
