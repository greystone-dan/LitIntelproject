"""Request observability: ID generation, validation, and optional slow-request logging.

This module provides:
- X-Request-ID header management with validation and generation
- Optional structured slow-request logging (disabled by default)
- Safe version information for health and API endpoints

Configuration:
- SLOW_REQUEST_LOG_MS: Milliseconds threshold for logging (default: disabled)
  Only requests strictly exceeding this threshold are logged.
- No request bodies, uploaded text, query strings, raw paths, or secrets are logged.
"""

from __future__ import annotations

import logging
import json
import os
import re
import secrets
import string
import sys
import subprocess
import time
from functools import lru_cache
from contextvars import ContextVar
from pathlib import Path
from typing import Callable

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


_REQUEST_ID_PATTERN = re.compile(r"[a-zA-Z0-9_-]{8,64}")
_REQUEST_ID_CHARSET = string.ascii_letters + string.digits + "_-"
_REQUEST_ID_LENGTH = 24
_COMMIT_PATTERN = re.compile(r"[0-9a-fA-F]{7,40}")
_REPOSITORY_ROOT = Path(__file__).resolve().parents[1]

# ContextVar for tracking the request ID across async boundaries
_request_id_context: ContextVar[str | None] = ContextVar("request_id", default=None)

# Process start time for version reporting
_process_start_time = time.time()


def get_request_id() -> str | None:
    """Get the current request ID from context."""
    return _request_id_context.get()


def set_request_id(request_id: str):
    """Set the request ID in context. Returns a token to reset it later."""
    return _request_id_context.set(request_id)


def generate_request_id() -> str:
    """Generate a fresh, bounded request ID suitable for headers.

    Returns a random 24-character string using ASCII letters, digits, underscores, and hyphens.
    """
    return "".join(secrets.choice(_REQUEST_ID_CHARSET) for _ in range(_REQUEST_ID_LENGTH))


def validate_request_id(value: str | None) -> str:
    """Validate or generate a request ID.

    If value is provided and matches the bounded pattern, return it.
    Otherwise, generate and return a fresh ID.

    Patterns enforced:
    - ASCII only (letters, digits, underscore, hyphen)
    - Length 8-64 characters (malformed/control/oversized incoming values are replaced)

    Args:
        value: Incoming X-Request-ID header value or None

    Returns:
        A valid, bounded request ID string
    """
    if value and isinstance(value, str) and _REQUEST_ID_PATTERN.fullmatch(value):
        return value
    return generate_request_id()


class SlowRequestLogger:
    """Optional structured slow-request logging.

    Logs requests that take strictly longer than the configured threshold.
    Never logs request bodies, uploaded text, query strings, raw paths, hostnames, or secrets.
    Logs only: request ID, route template, method, status code, elapsed time.
    """

    def __init__(self):
        """Initialize the slow-request logger from environment configuration."""
        self.logger = None
        self.threshold_ms = None

        threshold_str = os.getenv("SLOW_REQUEST_LOG_MS", "").strip()
        if threshold_str:
            try:
                threshold_value = int(threshold_str)
                if threshold_value > 0:
                    self.threshold_ms = threshold_value
                    self.logger = logging.getLogger("uvicorn.error")
            except (ValueError, TypeError):
                pass

    def should_log(self, elapsed_ms: float) -> bool:
        """Check if elapsed time strictly exceeds the configured threshold.

        Only logs when elapsed time is strictly greater than threshold.
        Returns False if logging is disabled or elapsed time does not exceed threshold.
        """
        if self.threshold_ms is None:
            return False
        return elapsed_ms > self.threshold_ms

    def log(self, request_id: str, method: str, route_template: str | None, status: int, elapsed_ms: float) -> None:
        """Log a slow request with safe information only.

        Args:
            request_id: The request ID
            method: HTTP method (GET, POST, etc.)
            route_template: The resolved route template (never raw URL/path/query)
                           If unavailable, use a fixed safe marker like '<unknown>'
            status: HTTP status code
            elapsed_ms: Elapsed time in milliseconds
        """
        if not self.should_log(elapsed_ms) or self.logger is None:
            return

        template = route_template or "<unknown>"
        metadata = {
            "request_id": request_id,
            "method": method,
            "route_template": template,
            "status": status,
            "duration_ms": elapsed_ms,
        }
        self.logger.info(
            json.dumps(metadata, separators=(",", ":"), ensure_ascii=True)
        )


_slow_request_logger = SlowRequestLogger()


def get_slow_request_logger() -> SlowRequestLogger:
    """Retrieve the global slow-request logger instance."""
    return _slow_request_logger


@lru_cache(maxsize=1)
def _get_git_commit() -> str:
    """Get the short Git commit hash, if available.

    Returns:
        Sanitized short commit hash or 'unknown' if .git is not present
    """
    git_dir = _REPOSITORY_ROOT / ".git"
    if not git_dir.is_dir():
        return "unknown"

    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(_REPOSITORY_ROOT),
            capture_output=True,
            text=True,
            timeout=1,
        )
        if result.returncode == 0:
            commit = result.stdout.strip()
            if _COMMIT_PATTERN.fullmatch(commit):
                return commit.lower()
    except (subprocess.TimeoutExpired, OSError, FileNotFoundError):
        pass

    return "unknown"


def get_version_info() -> dict[str, str | int]:
    """Get safe version information for health and API endpoints.

    Returns a dict with:
    - commit: sanitized Git commit or 'unknown'
    - started_at: process start time (Unix timestamp)
    - python_version: running Python version string

    Never exposes environment variables, deployment details, hostnames, or secrets.
    """
    app_commit = os.getenv("APP_COMMIT", "").strip()
    commit = (
        app_commit.lower()
        if _COMMIT_PATTERN.fullmatch(app_commit)
        else _get_git_commit()
    )

    return {
        "commit": commit,
        "started_at": int(_process_start_time),
        "python_version": sys.version.split()[0],
    }


class RequestContextMiddleware(BaseHTTPMiddleware):
    """ASGI middleware for request ID tracking and slow-request logging.

    Sets a ContextVar with the request ID for the duration of request processing.
    Adds X-Request-ID header to every response.
    Optionally logs slow requests to structured logs.
    """

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Process the request with request ID and slow-request logging."""
        request_id = validate_request_id(request.headers.get("x-request-id"))
        token = set_request_id(request_id)
        request.state.request_id = request_id

        started_at = time.perf_counter()
        try:
            response = await call_next(request)
            # Add the request ID header to the response
            response.headers["X-Request-ID"] = request_id
        finally:
            # Always reset the context token
            _request_id_context.reset(token)

        # Log slow requests if configured
        elapsed_ms = (time.perf_counter() - started_at) * 1000
        slow_logger = get_slow_request_logger()
        if slow_logger.should_log(elapsed_ms):
            matched_route = request.scope.get("route")
            route_template = getattr(matched_route, "path", None)
            slow_logger.log(
                request_id=request_id,
                method=request.method,
                route_template=route_template,
                status=response.status_code,
                elapsed_ms=elapsed_ms,
            )

        return response
