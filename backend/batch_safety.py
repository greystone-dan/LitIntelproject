"""Safety rails for long-running batch jobs that share a machine with the live site.

A batch job must never be able to slow the site down: it runs at the lowest process priority, holds
at most one database connection, gives every statement and lock a short time limit, sleeps in
proportion to the work it just did, and backs off (or stops) when the site itself answers slowly.
Standard library only; nothing here talks to anything except the local database and an optional
health URL the operator names.
"""

from __future__ import annotations

import os
import sys
import time
import urllib.request
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, make_url

# Windows priority classes (kernel32.SetPriorityClass).
_WIN_BACKGROUND_BEGIN = 0x00100000  # lowers CPU, I/O and memory priority together
_WIN_IDLE = 0x00000040
_WIN_BELOW_NORMAL = 0x00004000


def lower_process_priority() -> str:
    """Drop this process to the lowest priority the platform allows. Returns what was done, for the log."""
    if sys.platform == "win32":
        try:
            import ctypes

            kernel32 = ctypes.windll.kernel32  # type: ignore[attr-defined]
            handle = kernel32.GetCurrentProcess()
            for flag, name in (
                (_WIN_BACKGROUND_BEGIN, "background mode (low CPU and disk priority)"),
                (_WIN_IDLE, "idle priority"),
                (_WIN_BELOW_NORMAL, "below-normal priority"),
            ):
                if kernel32.SetPriorityClass(handle, flag):
                    return name
        except Exception:  # noqa: BLE001 - priority is best effort, the other limits still apply
            pass
        return "priority unchanged (could not set it); rely on the throttling"
    try:
        os.nice(19)
        return "nice 19"
    except (AttributeError, OSError):
        return "priority unchanged (could not set it); rely on the throttling"


def postgres_options(*, statement_timeout_ms: int, lock_timeout_ms: int, idle_in_transaction_ms: int, application_name: str) -> str:
    """Server options sent at connect time, so they hold for the whole connection (a plain SET is undone by a rollback)."""
    safe_name = "".join(ch for ch in application_name if ch.isalnum() or ch in "-_.")[:60] or "ilit-batch"
    return (
        f"-c statement_timeout={int(statement_timeout_ms)} "
        f"-c lock_timeout={int(lock_timeout_ms)} "
        f"-c idle_in_transaction_session_timeout={int(idle_in_transaction_ms)} "
        f"-c application_name={safe_name}"
    )


def make_limited_engine(
    url: object,
    *,
    statement_timeout_ms: int = 15_000,
    lock_timeout_ms: int = 2_000,
    idle_in_transaction_ms: int = 30_000,
    application_name: str = "ilit-batch",
) -> Engine:
    """An engine that can hold at most one connection, with short server-side time limits."""
    parsed = make_url(url) if isinstance(url, str) else url
    kwargs: dict = {"pool_pre_ping": True}
    if parsed.get_backend_name() == "postgresql":
        kwargs.update(
            pool_size=1,
            max_overflow=0,  # hard cap: this job can never hold more than one connection
            pool_timeout=30,
            connect_args={
                "options": postgres_options(
                    statement_timeout_ms=statement_timeout_ms,
                    lock_timeout_ms=lock_timeout_ms,
                    idle_in_transaction_ms=idle_in_transaction_ms,
                    application_name=application_name,
                ),
                "connect_timeout": 10,
            },
        )
    return create_engine(parsed, **kwargs)


def throttle_sleep(work_seconds: float, base_sleep: float, max_duty: float) -> float:
    """How long to rest after ``work_seconds`` of work so the job never works more than ``max_duty`` of the time."""
    base = max(float(base_sleep), 0.0)
    if not 0 < max_duty < 1:
        return base
    return max(base, work_seconds * (1.0 - max_duty) / max_duty)


def fetch_seconds(url: str, timeout: float = 10.0) -> float:
    """Time one GET of ``url``. Raises on a network error or a non-2xx answer."""
    if not url.lower().startswith(("http://", "https://")):
        raise ValueError("health URL must start with http:// or https://")
    started = time.monotonic()
    request = urllib.request.Request(url, headers={"User-Agent": "ilit-batch-health/1"})
    with urllib.request.urlopen(request, timeout=timeout) as response:  # noqa: S310 - scheme checked above
        response.read(2048)
        if not 200 <= response.status < 300:
            raise OSError(f"HTTP {response.status}")
    return time.monotonic() - started


@dataclass
class HealthGate:
    """Before each batch, time the site. If it is slow or down, wait (longer each time) and ask again; give up after a while."""

    url: str | None
    slow_seconds: float = 1.5
    base_wait: float = 10.0
    max_wait: float = 120.0
    max_waits: int = 12
    fetch: Callable[[str], float] = fetch_seconds
    sleeper: Callable[[float], None] = time.sleep
    log: Callable[[str], None] = print
    waits_total: int = 0

    def wait_until_healthy(self) -> bool:
        """True when the site answered quickly (or no URL was given); False when it never recovered."""
        if not self.url:
            return True
        wait = self.base_wait
        for attempt in range(self.max_waits + 1):
            try:
                took = self.fetch(self.url)
                problem = None if took <= self.slow_seconds else f"slow ({took:.1f}s > {self.slow_seconds:.1f}s)"
            except Exception as error:  # noqa: BLE001 - any failure to answer counts as unhealthy
                problem = f"not answering ({type(error).__name__})"
            if problem is None:
                return True
            if attempt == self.max_waits:
                break
            self.waits_total += 1
            self.log(f"  site {problem}; pausing {wait:.0f}s to leave the machine to it")
            self.sleeper(wait)
            wait = min(wait * 2, self.max_wait)
        return False


def stop_requested(stop_file: str | None) -> bool:
    """An operator can stop the job at any time by creating this file."""
    return bool(stop_file) and Path(stop_file).exists()
