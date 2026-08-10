from __future__ import annotations

from datetime import datetime, timezone
import json
import os
import threading
import time
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen


@dataclass
class CanLiiApiClient:
    api_key: str
    base_url: str = "https://api.canlii.org"
    user_agent: str = "AI-CaseLibrary/1.0"
    max_requests_per_second: int = 2
    max_requests_per_day: int = 1000

    _request_lock: threading.Lock = field(default_factory=threading.Lock, init=False, repr=False)
    _last_request_monotonic: float = field(default=0.0, init=False, repr=False)
    _quota_day_utc: str = field(default="", init=False, repr=False)
    _quota_used_today: int = field(default=0, init=False, repr=False)

    @classmethod
    def from_env(cls) -> "CanLiiApiClient | None":
        api_key = (os.getenv("CANLII_API_KEY") or "").strip()
        if not api_key:
            return None
        base_url = (os.getenv("CANLII_API_BASE_URL") or "https://api.canlii.org").strip()
        user_agent = (os.getenv("CANLII_API_USER_AGENT") or "AI-CaseLibrary/1.0").strip()
        return cls(api_key=api_key, base_url=base_url, user_agent=user_agent)

    def _prepare_request_locked(self) -> bool:
        day_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if self._quota_day_utc != day_utc:
            self._quota_day_utc = day_utc
            self._quota_used_today = 0

        if self._quota_used_today >= self.max_requests_per_day:
            return False

        # Keep throughput at or below 2 requests/sec.
        min_interval = 1.0 / float(max(1, self.max_requests_per_second))
        elapsed = time.monotonic() - self._last_request_monotonic
        if self._last_request_monotonic > 0.0 and elapsed < min_interval:
            time.sleep(min_interval - elapsed)

        self._last_request_monotonic = time.monotonic()
        self._quota_used_today += 1
        return True

    def get_json(self, path: str, params: dict[str, Any] | None = None, timeout: float = 8.0) -> dict[str, Any] | None:
        with self._request_lock:
            if not self._prepare_request_locked():
                return None

            clean_path = path if path.startswith("/") else f"/{path}"
            query = urlencode(params or {})
            url = f"{self.base_url.rstrip('/')}{clean_path}"
            if query:
                url = f"{url}?{query}"

            headers = {
                "Accept": "application/json",
                "User-Agent": self.user_agent,
                "Authorization": f"Bearer {self.api_key}",
            }
            request = Request(url=url, headers=headers, method="GET")
            try:
                with urlopen(request, timeout=timeout) as response:
                    body = response.read().decode("utf-8", errors="replace")
            except Exception:
                return None

            try:
                payload = json.loads(body)
            except Exception:
                return None
            return payload if isinstance(payload, dict) else {"data": payload}

    def lookup_by_neutral(self, neutral_citation: str) -> dict[str, Any] | None:
        """
        Lightweight hook for future enrichment.
        Endpoint can vary by tenant/product; configurable callers can
        replace this with the exact CanLII route used in deployment.
        """
        neutral = (neutral_citation or "").strip()
        if not neutral:
            return None
        return self.get_json(
            "/v1/cases/search",
            params={"q": neutral},
        )
