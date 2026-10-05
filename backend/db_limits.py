"""Opt-in engine limits and narrowly classified, safe HTTP timeout responses.

Configuration is evaluated per engine/process; importing this module neither
loads dotenv files nor creates an engine. See docs/CONFIGURATION_REFERENCE.md.
"""

from __future__ import annotations

import math
import os
import re
from collections.abc import Mapping
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, Response
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, URL, make_url
from sqlalchemy.exc import OperationalError, TimeoutError
from starlette._utils import is_async_callable
from starlette.concurrency import run_in_threadpool


_INTEGER = re.compile(r"[+-]?[0-9]+\Z")
_POOL_TIMEOUT = re.compile(
    r"^QueuePool limit of size [0-9]+ overflow -?[0-9]+ reached, "
    r"connection timed out, timeout [0-9]+(?:\.[0-9]+)?(?:\s|$)"
)
_MESSAGE = "The database is busy. Please try again in a few seconds."


def _integer(
    environ: Mapping[str, str], name: str, minimum: int, maximum: int | None = None
) -> int | None:
    if name not in environ:
        return None
    raw = environ[name].strip()
    bounds = f"{minimum}..{maximum}" if maximum is not None else f">= {minimum}"
    if not _INTEGER.fullmatch(raw):
        raise ValueError(f"{name} must be an integer {bounds}.")
    try:
        value = int(raw)
    except ValueError:
        raise ValueError(f"{name} must be an integer {bounds}.") from None
    if value < minimum or (maximum is not None and value > maximum):
        raise ValueError(f"{name} must be an integer {bounds}.")
    return value


def engine_kwargs(
    database_url: str | URL,
    *,
    environ: Mapping[str, str] | None = None,
    include_timeouts: bool = True,
) -> dict[str, Any]:
    """Return only explicitly configured kwargs, validating even ignored values.

    SQLite omits PostgreSQL settings and QueuePool-only settings regardless of
    URL shape, so in-memory engines retain their dialect's pool implementation.
    """
    env = os.environ if environ is None else environ
    statement = _integer(env, "DB_STATEMENT_TIMEOUT_MS", 0, 2147483647)
    lock = _integer(env, "DB_LOCK_TIMEOUT_MS", 0, 2147483647)
    pool = {
        "pool_size": _integer(env, "DB_POOL_SIZE", 0),
        "max_overflow": _integer(env, "DB_MAX_OVERFLOW", -1),
        "pool_recycle": _integer(env, "DB_POOL_RECYCLE_SECONDS", -1),
    }
    if "DB_POOL_TIMEOUT_SECONDS" in env:
        try:
            timeout = float(env["DB_POOL_TIMEOUT_SECONDS"])
        except (ValueError, OverflowError):
            raise ValueError("DB_POOL_TIMEOUT_SECONDS must be finite seconds >= 0.") from None
        if not math.isfinite(timeout) or timeout < 0:
            raise ValueError("DB_POOL_TIMEOUT_SECONDS must be finite seconds >= 0.")
        pool["pool_timeout"] = timeout

    backend = make_url(database_url).get_backend_name()
    kwargs = {
        name: value
        for name, value in pool.items()
        if value is not None
        and (backend != "sqlite" or name == "pool_recycle")
    }
    if backend == "postgresql" and include_timeouts:
        options = []
        if statement is not None:
            options.append(f"-c statement_timeout={statement}")
        if lock is not None:
            options.append(f"-c lock_timeout={lock}")
        if options:
            kwargs["connect_args"] = {"options": " ".join(options)}
    return kwargs


def engine_without_timeout(
    database_url: str | URL | None = None,
    *,
    environ: Mapping[str, str] | None = None,
) -> Engine:
    """Create a separate engine for scripts, omitting both client query limits.

    Supply a URL to avoid importing database settings. Otherwise import the
    configured DATABASE_URL lazily, after database.py initialization. Callers
    own sessions/transactions and must close sessions and dispose this engine.
    Server/role defaults are not overridden or disabled by this helper.
    """
    if database_url is None:
        from .database import DATABASE_URL

        database_url = DATABASE_URL
    return create_engine(
        database_url,
        pool_pre_ping=True,
        **engine_kwargs(database_url, environ=environ, include_timeouts=False),
    )


def _is_timeout(exc: Exception) -> bool:
    if isinstance(exc, OperationalError):
        original = exc.orig
        code = getattr(original, "pgcode", None) or getattr(original, "sqlstate", None)
        primary = getattr(getattr(original, "diag", None), "message_primary", None)
        return (code, primary) in (
            ("57014", "canceling statement due to statement timeout"),
            ("55P03", "canceling statement due to lock timeout"),
        )
    if isinstance(exc, TimeoutError):
        # TimeoutError also covers non-pool timeouts; require QueuePool's
        # canonical exhaustion diagnostic, never a generic "timed out" match.
        return bool(_POOL_TIMEOUT.match(str(exc)))
    return False


def _wants_html(request: Request) -> bool:
    path = request.url.path
    if path == "/api" or path.startswith("/api/"):
        return False
    response_class = getattr(request.scope.get("route"), "response_class", None)
    response_class = getattr(response_class, "value", response_class)
    if isinstance(response_class, type) and issubclass(response_class, JSONResponse):
        return False
    return "text/html" in request.headers.get("accept", "")


def register_timeout_handlers(app: FastAPI) -> None:
    """Wrap only SQLAlchemy operational/pool errors, preserving old fallbacks."""
    existing = dict(app.exception_handlers)

    async def handler(request: Request, exc: Exception) -> Response:
        if not _is_timeout(exc):
            fallback = next(
                (existing[cls] for cls in type(exc).__mro__ if cls in existing),
                None,
            )
            if fallback is None:
                raise exc
            if is_async_callable(fallback):
                return await fallback(request, exc)
            return await run_in_threadpool(fallback, request, exc)

        headers = {"Retry-After": "5"}
        if _wants_html(request):
            return HTMLResponse(
                '<!doctype html><html lang="en"><head><meta charset="utf-8">'
                "<title>Please try again</title></head><body>"
                f"<h1>Please try again</h1><p>{_MESSAGE}</p></body></html>",
                status_code=503,
                headers=headers,
            )
        return JSONResponse({"detail": _MESSAGE}, status_code=503, headers=headers)

    app.add_exception_handler(OperationalError, handler)
    app.add_exception_handler(TimeoutError, handler)
