from __future__ import annotations

import logging
import time

import requests

logger = logging.getLogger(__name__)


def download_pdf(pdf_url: str, timeout: float = 60.0, retries: int = 3, backoff_seconds: float = 1.0) -> tuple[bytes, str]:
    if not pdf_url:
        return b"", ""
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(pdf_url, headers={"User-Agent": "AI-CaseLibrary-FCIngest/1.0"}, timeout=timeout)
            response.raise_for_status()
            return response.content, response.headers.get("Content-Type", "application/octet-stream")
        except requests.RequestException as exc:  # pragma: no cover - exercised in runtime
            last_error = exc
            if attempt >= retries:
                break
            time.sleep(backoff_seconds * attempt)
    raise RuntimeError(f"Failed to download PDF: {pdf_url}") from last_error
