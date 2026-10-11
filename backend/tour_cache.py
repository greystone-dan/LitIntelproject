"""A short-lived server cache for the site tour's fixed demo requests.

The tour always shows the same few things: the same searches, the same decision, Vavilov's citation snapshot,
one judge profile. On the real library some of those take 5 to 15 seconds each. This keeps the answers to
exactly those requests, listed as ``cache`` in ``pages/site_tour_steps.json``, for a few hours, so the tour (and
anyone who happens to make the very same request) gets them at once. Nothing else is cached, nothing a
visitor types or uploads is cached, and a cached answer is the answer the route itself gave.

When the same listed request is already being worked out (the tour warms them when it starts), a second one
waits for that answer instead of starting the work again.
"""

from __future__ import annotations

import asyncio
import logging
import os
import re
import time
from urllib.parse import parse_qsl, urlencode

from .site_tour import tour_steps

logger = logging.getLogger(__name__)

_TTL_DEFAULT = 6 * 3600
_MAX_BODY = 4 * 1024 * 1024
_RETRY_IDS = 300            # a tour case not in the library yet is looked up again after this many seconds


def canonical(path: str, query: str) -> str:
    pairs = sorted(parse_qsl(query or "", keep_blank_values=True))
    return path + ("?" + urlencode(pairs) if pairs else "")


def _ttl() -> int:
    try:
        return max(0, int(os.getenv("CASELIBRARY_TOUR_CACHE_SECONDS", str(_TTL_DEFAULT))))
    except ValueError:
        return _TTL_DEFAULT


def _case_id(citation: str) -> int | None:
    from sqlalchemy import text

    from .database import SessionLocal

    db = SessionLocal()
    try:
        row = db.execute(text("SELECT id FROM cases WHERE citation = :c ORDER BY id LIMIT 1"), {"c": citation}).first()
        return int(row[0]) if row else None
    finally:
        db.close()


class TourCache:
    def __init__(self, lookup=_case_id):
        self._lookup = lookup
        self._keys: set[str] | None = None
        self._keys_at = 0.0
        self._store: dict[str, tuple[float, int, list, bytes]] = {}
        self._pending: dict[str, asyncio.Event] = {}

    def keys(self) -> set[str]:
        """The listed requests, with each {name} replaced by that tour case's id in this library."""
        if self._keys is not None and (self._keys_at == 0 or time.time() - self._keys_at < _RETRY_IDS):
            return self._keys
        data = tour_steps()
        ids, missing = {}, False
        for name, spec in (data.get("cases") or {}).items():
            try:
                ids[name] = self._lookup(spec["citation"])
            except Exception:  # noqa: BLE001 - no database: nothing is cached
                logger.warning("tour cache: could not look up %s", spec.get("citation"))
                ids[name] = None
            missing = missing or ids[name] is None
        keys = set()
        for url in data.get("cache") or []:
            names = re.findall(r"\{(\w+)\}", url)
            if any(ids.get(n) is None for n in names):
                continue
            for n in names:
                url = url.replace("{" + n + "}", str(ids[n]))
            path, _, query = url.partition("?")
            keys.add(canonical(path, query))
        self._keys, self._keys_at = keys, (time.time() if missing else 0)
        return keys

    def get(self, key: str):
        hit = self._store.get(key)
        if hit and hit[0] > time.time():
            return hit
        return None

    def put(self, key: str, status: int, headers: list, body: bytes) -> None:
        ttl = _ttl()
        if ttl and status == 200 and len(body) <= _MAX_BODY:
            self._store[key] = (time.time() + ttl, status, headers, body)

    def clear(self) -> None:
        self._store.clear()
        self._keys = None


CACHE = TourCache()
_SKIP_HEADERS = {b"set-cookie", b"content-length", b"date", b"server", b"x-request-id", b"x-tour-cache"}


class TourCacheMiddleware:
    """Pure ASGI, so a cached answer goes out as the same bytes and headers the route sent."""

    def __init__(self, app, cache: TourCache = CACHE):
        self.app = app
        self.cache = cache

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http" or scope.get("method") != "GET":
            return await self.app(scope, receive, send)
        key = canonical(scope.get("path", ""), (scope.get("query_string") or b"").decode("latin-1"))
        try:
            listed = key in self.cache.keys()
        except Exception:  # noqa: BLE001
            listed = False
        if not listed:
            return await self.app(scope, receive, send)
        hit = self.cache.get(key)
        while hit is None and key in self.cache._pending:                  # the same request is already being worked out
            await self.cache._pending[key].wait()
            hit = self.cache.get(key)
            if hit is None:
                break
        if hit is not None:
            return await self._replay(hit, send)
        event = self.cache._pending.setdefault(key, asyncio.Event())
        status, headers, chunks = 0, [], []

        async def capture(message):
            nonlocal status, headers
            if message["type"] == "http.response.start":
                status, headers = message["status"], list(message.get("headers") or [])
            elif message["type"] == "http.response.body":
                chunks.append(message.get("body", b""))
            await send(message)

        try:
            await self.app(scope, receive, capture)
            if not any(name.lower() == b"set-cookie" for name, _ in headers):
                self.cache.put(key, status, [(n, v) for n, v in headers if n.lower() not in _SKIP_HEADERS], b"".join(chunks))
        finally:
            event.set()
            if self.cache._pending.get(key) is event:
                del self.cache._pending[key]

    @staticmethod
    async def _replay(hit, send):
        _, status, headers, body = hit
        await send({"type": "http.response.start", "status": status,
                    "headers": headers + [(b"content-length", str(len(body)).encode()), (b"x-tour-cache", b"hit")]})
        await send({"type": "http.response.body", "body": body})
