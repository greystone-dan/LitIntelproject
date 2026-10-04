"""Standalone, stdlib-only interval jobs; never imported by application startup."""

from __future__ import annotations

import errno
import json
import math
import os
import re
import signal
import subprocess
import sys
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class Job:
    name: str
    command: tuple[str, ...]
    interval_seconds: float
    max_runtime_seconds: float
    enabled: bool = False
    overlap_policy: str = "skip"


def _positive_number(value: object, field: str) -> float:
    # Bound schedules to useful intervals and avoid float overflow/underflow.
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or not 0.01 <= value <= 315360000
    ):
        raise ValueError(f"{field} must be a number between 0.01 and 315360000 seconds")
    return float(value)


def load_jobs(path: Path) -> list[Job]:
    """Validate the entire config before permitting any command to run."""
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)
    if not isinstance(data, dict) or set(data) != {"jobs"} or not isinstance(data["jobs"], list):
        raise ValueError('config must contain only a "jobs" array')
    jobs = []
    names = set()
    required = {"name", "command", "interval_seconds", "max_runtime_seconds"}
    for item in data["jobs"]:
        if not isinstance(item, dict) or not required <= item.keys() or item.keys() - required - {"enabled", "overlap_policy"}:
            raise ValueError("job requires name, command, interval_seconds, max_runtime_seconds; optional enabled, overlap_policy")
        name = item["name"]
        if not isinstance(name, str) or not re.fullmatch(r"[a-z][a-z0-9_-]{0,63}", name):
            raise ValueError("job name must be 1-64 lowercase letters, digits, underscores or hyphens, starting with a letter")
        if name in names:
            raise ValueError(f"duplicate job name: {name}")
        names.add(name)
        argv = item["command"]
        if not isinstance(argv, list) or not argv or any(
            not isinstance(arg, str) or not arg.strip() or "\0" in arg for arg in argv
        ):
            raise ValueError(f"{name}: command must be a nonempty array of nonempty strings")
        enabled = item.get("enabled", False)
        if not isinstance(enabled, bool):
            raise ValueError(f"{name}: enabled must be a boolean")
        overlap_policy = item.get("overlap_policy", "skip")
        if not isinstance(overlap_policy, str) or overlap_policy != "skip":
            raise ValueError(f'{name}: overlap_policy must be the string "skip"')
        jobs.append(Job(
            name, tuple(argv),
            _positive_number(item["interval_seconds"], "interval_seconds"),
            _positive_number(item["max_runtime_seconds"], "max_runtime_seconds"),
            enabled,
            overlap_policy,
        ))
    return jobs


def log_event(event: str, **fields: object) -> None:
    """Emit one JSON record; commands and child output are deliberately omitted."""
    print(json.dumps({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event, **fields,
    }, allow_nan=False), flush=True)


class JobLock:
    """Nonblocking OS advisory lock on a persistent file, released on exit/crash."""

    def __init__(self, directory: Path, name: str):
        self.path = directory / f"{name}.lock"
        self.file = None

    def acquire(self) -> bool:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.file = self.path.open("a+b")
        try:
            if os.name == "nt":
                import msvcrt
                # msvcrt locks a byte at the current file position.
                if self.path.stat().st_size == 0:
                    self.file.write(b"\0")
                    self.file.flush()
                self.file.seek(0)
                msvcrt.locking(self.file.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            self.file.close()
            self.file = None
            if exc.errno in (errno.EACCES, errno.EAGAIN, errno.EDEADLK):
                return False
            raise
        return True

    def release(self) -> None:
        if self.file is not None:
            try:
                if os.name == "nt":
                    import msvcrt
                    self.file.seek(0)
                    msvcrt.locking(self.file.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(self.file.fileno(), fcntl.LOCK_UN)
            finally:
                self.file.close()
                self.file = None


@dataclass(frozen=True)
class Result:
    status: str
    returncode: int | None = None


def _cleanup_child(child: subprocess.Popen, grace_seconds: float = 1.0) -> None:
    if os.name == "nt":
        # Windows' built-in taskkill terminates descendants as well as the child.
        try:
            result = subprocess.run(
                ["taskkill", "/PID", str(child.pid), "/T", "/F"],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                check=False, timeout=5,
            )
            tree_killed = result.returncode == 0
        except (OSError, subprocess.TimeoutExpired):
            tree_killed = False
        if not tree_killed and child.poll() is None:
            child.kill()
    else:
        try:
            os.killpg(child.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            child.wait(timeout=grace_seconds)
        except subprocess.TimeoutExpired:
            pass
        # Also reap descendants that ignore TERM, even if their parent exited.
        try:
            os.killpg(child.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    child.wait()


def run_command(job: Job, stop: threading.Event, cwd: Path) -> Result:
    """Run argv without a shell, bounding runtime and cleaning up on interruption."""
    argv = [sys.executable if arg == "{python}" else arg for arg in job.command]
    kwargs = {"start_new_session": True} if os.name != "nt" else {
        "creationflags": subprocess.CREATE_NEW_PROCESS_GROUP,
    }
    child = subprocess.Popen(
        argv, cwd=cwd, stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True, **kwargs,
    )
    deadline = time.monotonic() + job.max_runtime_seconds
    try:
        while True:
            if stop.is_set():
                _cleanup_child(child)
                return Result("stopped", child.returncode)
            code = child.poll()
            if code is not None:
                return Result("success" if code == 0 else "failed", code)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                _cleanup_child(child)
                return Result("timeout", child.returncode)
            stop.wait(min(0.05, remaining))
    finally:
        if child.poll() is None:
            _cleanup_child(child)


class Runner:
    """Sequential monotonic scheduler with no catch-up, persistent state or DB."""

    def __init__(
        self, jobs: list[Job], lock_dir: Path, cwd: Path,
        *, clock: Callable[[], float] = time.monotonic,
        execute: Callable = run_command, emit: Callable = log_event,
        stop: threading.Event | None = None,
    ):
        self.jobs = jobs
        self.lock_dir = lock_dir
        self.cwd = cwd
        self.clock = clock
        self.execute = execute
        self.emit = emit
        self.stop = stop if stop is not None else threading.Event()
        self.next_due = {job.name: clock() for job in jobs}
        self.failed = False

    def tick(self, *, dry_run: bool = False) -> None:
        for job in self.jobs:
            if self.stop.is_set():
                break
            now = self.clock()
            if not job.enabled or now < self.next_due[job.name]:
                continue
            due = self.next_due[job.name]
            lock = JobLock(self.lock_dir, job.name)
            acquired = False
            try:
                if dry_run:
                    self.emit("would_run", job=job.name)
                elif not lock.acquire():
                    self.emit("overlap_skipped", job=job.name)
                else:
                    acquired = True
                    self.emit("job_started", job=job.name)
                    result = self.execute(job, self.stop, self.cwd)
                    self.failed |= result.status in {"failed", "timeout"}
                    self.emit("job_finished", job=job.name, status=result.status,
                              returncode=result.returncode,
                              duration_seconds=max(0, self.clock() - now))
            except OSError:
                self.failed = True
                self.emit("job_failed", job=job.name, reason="os_error")
            finally:
                if acquired:
                    try:
                        lock.release()
                    except OSError:
                        self.failed = True
                        self.emit("job_failed", job=job.name, reason="lock_release_error")
                # Advance to the first future slot, discarding all missed slots.
                elapsed = max(0, self.clock() - due)
                self.next_due[job.name] = due + (math.floor(elapsed / job.interval_seconds) + 1) * job.interval_seconds

    def run(self, *, once: bool = False, dry_run: bool = False) -> int:
        self.emit("runner_started", enabled=sum(job.enabled for job in self.jobs))
        if not any(job.enabled for job in self.jobs):
            self.emit("no_enabled_jobs")
            return 0
        while not self.stop.is_set():
            self.tick(dry_run=dry_run)
            if once or dry_run:
                break
            delay = max(0, min(self.next_due[job.name] for job in self.jobs if job.enabled) - self.clock())
            self.stop.wait(min(delay, 1.0))
        self.emit("runner_finished", failed=self.failed, stopped=self.stop.is_set())
        return int(self.failed)


def install_signal_handlers(stop: threading.Event) -> tuple[dict, list[int]]:
    """Signal handlers only set state; cleanup happens outside the handler."""
    previous = {}
    received = []

    def handle(signum, _frame):
        if not received:
            received.append(signum)
        stop.set()

    for signum in (signal.SIGINT, signal.SIGTERM):
        previous[signum] = signal.signal(signum, handle)
    return previous, received
