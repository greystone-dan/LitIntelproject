"""Run resumable case acquisition and corpus maintenance jobs overnight."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RUNS_DIR = PROJECT_ROOT / "data" / "overnight_runs"
STATE_FILENAME = "state.json"
LOCK_FILENAME = "overnight.lock"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass(frozen=True)
class Job:
    name: str
    description: str
    arguments: tuple[str, ...]
    needs_database: bool = False
    network: bool = False

    def command(self, python_executable: Path) -> list[str]:
        return [str(python_executable), *self.arguments]


JOBS: dict[str, Job] = {
    "fc_decisions": Job(
        "fc_decisions",
        "Resume official Federal Court IMM decision discovery and capture",
        (
            "-m",
            "fc_ingest",
            "--db-path",
            "data/raw/fc/fc_decisions.db",
            "--monthly",
            "--timeout",
            "60",
            "--retries",
            "4",
            "--item-delay-seconds",
            "2",
            "--page-delay-seconds",
            "1.5",
        ),
        network=True,
    ),
    "fc_portal": Job(
        "fc_portal",
        "Resume Federal Court IMM portal collection",
        (
            "scripts/fc_portal_collector.py",
            "--prefixes",
            "IMM",
            "--delay-ms",
            "1500",
            "--expand-details",
            "--emit-import-ready",
        ),
        network=True,
    ),
    "fc_history": Job(
        "fc_history",
        "Resume procedural histories for prototype IMM files",
        (
            "scripts/fetch_fc_procedural_history.py",
            "--from-prototype",
            "--delay-ms",
            "1200",
        ),
        needs_database=True,
        network=True,
    ),
    "reference_verify": Job(
        "reference_verify",
        "Verify and resume the separate reference library",
        ("scripts/download_reference_library.py", "--timeout", "90"),
        network=True,
    ),
    "tag_cases": Job(
        "tag_cases",
        "Tag unprocessed cases with the current legal taxonomy",
        ("scripts/tag_cases.py", "--batch-size", "250"),
        needs_database=True,
    ),
    "chunk_cases": Job(
        "chunk_cases",
        "Create text chunks for cases that do not have any",
        ("scripts/chunk_cases.py", "--batch-size", "50"),
        needs_database=True,
    ),
    "citations": Job(
        "citations",
        "Rebuild case citations and citation metrics",
        (
            "-m",
            "scripts.extract_citation_network",
            "--cases",
            "--chunks",
            "--metrics",
            "--batch-size",
            "500",
        ),
        needs_database=True,
    ),
    "local_embeddings": Job(
        "local_embeddings",
        "Embed pending chunks locally with BGE-M3",
        ("-m", "scripts.embed_local_chunks", "--batch-size", "32"),
        needs_database=True,
    ),
    "regression_tests": Job(
        "regression_tests",
        "Run the full regression suite",
        ("-m", "pytest", "-q"),
    ),
}

PROFILES: dict[str, tuple[str, ...]] = {
    "pull": ("fc_decisions", "fc_portal", "fc_history"),
    "enrich": (
        "reference_verify",
        "tag_cases",
        "chunk_cases",
        "citations",
        "local_embeddings",
    ),
    "safe": (
        "fc_decisions",
        "fc_portal",
        "fc_history",
        "reference_verify",
        "tag_cases",
        "chunk_cases",
        "citations",
        "local_embeddings",
    ),
    "verify": ("regression_tests",),
}


def python_executable() -> Path:
    configured = os.getenv("OVERNIGHT_PYTHON")
    if configured:
        return Path(configured).resolve()
    candidate = PROJECT_ROOT / "venv" / "Scripts" / "python.exe"
    return candidate if candidate.exists() else Path(sys.executable).resolve()


def atomic_write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def process_is_running(pid: int) -> bool:
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except PermissionError:
        return True
    except OSError:
        return False
    return True


class RunLock:
    def __init__(self, path: Path, *, force_unlock: bool = False) -> None:
        self.path = path
        self.force_unlock = force_unlock
        self.acquired = False

    def __enter__(self) -> "RunLock":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists():
            try:
                lock_data = json.loads(self.path.read_text(encoding="utf-8"))
                active = process_is_running(int(lock_data.get("pid", 0)))
            except (OSError, ValueError, TypeError, json.JSONDecodeError):
                active = True
            if active and not self.force_unlock:
                raise RuntimeError(f"Another overnight run owns {self.path}")
            self.path.unlink(missing_ok=True)

        descriptor = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        try:
            payload = json.dumps({"pid": os.getpid(), "created_at": utc_now_iso()})
            os.write(descriptor, payload.encode("utf-8"))
        finally:
            os.close(descriptor)
        self.acquired = True
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self.acquired:
            self.path.unlink(missing_ok=True)
            self.acquired = False


def selected_job_names(profile: str, explicit_jobs: Sequence[str] | None) -> list[str]:
    names = list(explicit_jobs) if explicit_jobs else list(PROFILES[profile])
    unknown = [name for name in names if name not in JOBS]
    if unknown:
        raise ValueError(f"Unknown jobs: {', '.join(unknown)}")
    return list(dict.fromkeys(names))


def create_state(run_id: str, job_names: Sequence[str], continue_on_error: bool) -> dict:
    return {
        "schema_version": 1,
        "run_id": run_id,
        "created_at": utc_now_iso(),
        "updated_at": utc_now_iso(),
        "status": "pending",
        "continue_on_error": continue_on_error,
        "selected_jobs": list(job_names),
        "jobs": {
            name: {
                "status": "pending",
                "attempts": 0,
                "started_at": None,
                "finished_at": None,
                "exit_code": None,
                "log": f"{name}.log",
            }
            for name in job_names
        },
    }


def load_state(run_dir: Path) -> dict:
    state_path = run_dir / STATE_FILENAME
    if not state_path.exists():
        raise FileNotFoundError(f"Missing run state: {state_path}")
    state = json.loads(state_path.read_text(encoding="utf-8"))
    for job_state in state.get("jobs", {}).values():
        if job_state.get("status") == "running":
            job_state["status"] = "interrupted"
            job_state["finished_at"] = utc_now_iso()
    return state


def latest_run_dir(runs_dir: Path) -> Path:
    candidates = sorted(
        (path for path in runs_dir.iterdir() if path.is_dir() and (path / STATE_FILENAME).exists()),
        reverse=True,
    ) if runs_dir.exists() else []
    if not candidates:
        raise FileNotFoundError(f"No resumable runs under {runs_dir}")
    return candidates[0]


def preflight(job_names: Sequence[str], python_path: Path, runs_dir: Path) -> list[str]:
    errors: list[str] = []
    if not python_path.exists():
        errors.append(f"Python executable is missing: {python_path}")
    for name in job_names:
        script = JOBS[name].arguments[0]
        if script.endswith(".py") and not (PROJECT_ROOT / script).exists():
            errors.append(f"Job {name} is missing script: {script}")

    runs_dir.mkdir(parents=True, exist_ok=True)
    free_bytes = shutil.disk_usage(runs_dir).free
    if free_bytes < 2 * 1024**3:
        errors.append(f"Less than 2 GiB free at {runs_dir}")

    if any(JOBS[name].needs_database for name in job_names) and python_path.exists():
        check = subprocess.run(
            [
                str(python_path),
                "-c",
                "from sqlalchemy import text; from backend.database import engine; "
                "c=engine.connect(); c.execute(text('SELECT 1')); c.close()",
            ],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if check.returncode:
            detail = (check.stderr or check.stdout).strip().splitlines()
            errors.append(f"Database preflight failed: {detail[-1] if detail else 'unknown error'}")
    return errors


def run_job(job: Job, command: Sequence[str], log_path: Path) -> int:
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"\n[{utc_now_iso()}] START {' '.join(command)}\n")
        log.flush()
        process = subprocess.Popen(
            list(command),
            cwd=PROJECT_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
        )
        assert process.stdout is not None
        for line in process.stdout:
            log.write(line)
            log.flush()
            print(f"[{job.name}] {line}", end="", flush=True)
        return_code = process.wait()
        log.write(f"[{utc_now_iso()}] EXIT {return_code}\n")
        return return_code


JobRunner = Callable[[Job, Sequence[str], Path], int]


def execute_jobs(
    state: dict,
    run_dir: Path,
    python_path: Path,
    *,
    runner: JobRunner = run_job,
) -> int:
    state_path = run_dir / STATE_FILENAME
    state["status"] = "running"
    state["updated_at"] = utc_now_iso()
    atomic_write_json(state_path, state)

    had_failure = False
    for name in state["selected_jobs"]:
        job_state = state["jobs"][name]
        if job_state["status"] == "completed":
            print(f"[skip] {name} already completed")
            continue

        job = JOBS[name]
        command = job.command(python_path)
        job_state.update(
            {
                "status": "running",
                "attempts": int(job_state.get("attempts", 0)) + 1,
                "started_at": utc_now_iso(),
                "finished_at": None,
                "exit_code": None,
                "command": command,
            }
        )
        state["updated_at"] = utc_now_iso()
        atomic_write_json(state_path, state)
        print(f"[start] {name}: {job.description}")

        try:
            exit_code = runner(job, command, run_dir / job_state["log"])
        except KeyboardInterrupt:
            job_state["status"] = "interrupted"
            job_state["finished_at"] = utc_now_iso()
            state["status"] = "interrupted"
            state["updated_at"] = utc_now_iso()
            atomic_write_json(state_path, state)
            return 130
        except Exception as exc:
            exit_code = 1
            job_state["error"] = f"{type(exc).__name__}: {exc}"

        job_state["exit_code"] = exit_code
        job_state["finished_at"] = utc_now_iso()
        job_state["status"] = "completed" if exit_code == 0 else "failed"
        state["updated_at"] = utc_now_iso()
        atomic_write_json(state_path, state)
        if exit_code:
            had_failure = True
            print(f"[failed] {name} exit={exit_code} log={job_state['log']}")
            if not state["continue_on_error"]:
                state["status"] = "failed"
                atomic_write_json(state_path, state)
                return exit_code
        else:
            print(f"[done] {name}")

    state["status"] = "completed_with_failures" if had_failure else "completed"
    state["updated_at"] = utc_now_iso()
    atomic_write_json(state_path, state)
    return 1 if had_failure else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", choices=sorted(PROFILES), default="safe")
    parser.add_argument("--jobs", nargs="+", choices=sorted(JOBS))
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--list-jobs", action="store_true")
    parser.add_argument(
        "--resume",
        nargs="?",
        const="latest",
        metavar="RUN_ID",
        help="Resume a run by ID, or the latest run when no ID is supplied",
    )
    parser.add_argument("--continue-on-error", action="store_true")
    parser.add_argument("--force-unlock", action="store_true")
    parser.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.list_jobs:
        for name, job in JOBS.items():
            flags = ", ".join(flag for flag, enabled in (("network", job.network), ("database", job.needs_database)) if enabled)
            print(f"{name:18} {job.description}{f' [{flags}]' if flags else ''}")
        return

    runs_dir = args.runs_dir.resolve()
    python_path = python_executable()
    if args.resume:
        run_dir = latest_run_dir(runs_dir) if args.resume == "latest" else runs_dir / args.resume
        state = load_state(run_dir)
        job_names = list(state["selected_jobs"])
        if args.continue_on_error:
            state["continue_on_error"] = True
    else:
        job_names = selected_job_names(args.profile, args.jobs)
        run_id = datetime.now().strftime("%Y%m%d-%H%M%S")
        run_dir = runs_dir / run_id
        state = create_state(run_id, job_names, args.continue_on_error)

    errors = preflight(job_names, python_path, runs_dir)
    print(f"python={python_path}")
    print(f"run_dir={run_dir}")
    print(f"jobs={','.join(job_names)}")
    if errors:
        for error in errors:
            print(f"[preflight-error] {error}", file=sys.stderr)
        raise SystemExit(2)
    print("preflight=ok")
    if args.preflight:
        return

    run_dir.mkdir(parents=True, exist_ok=True)
    atomic_write_json(run_dir / STATE_FILENAME, state)
    try:
        with RunLock(runs_dir / LOCK_FILENAME, force_unlock=args.force_unlock):
            raise SystemExit(execute_jobs(state, run_dir, python_path))
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc


if __name__ == "__main__":
    main()