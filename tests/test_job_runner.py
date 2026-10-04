"""DB-free scheduling, locking, timeout and signal contracts."""

import json
import os
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

import pytest

from backend.job_runner import Job, JobLock, Result, Runner, load_jobs, run_command


ROOT = Path(__file__).resolve().parents[1]


def job(name="test", enabled=True, interval=10, runtime=1, code="pass"):
    return Job(name, ("{python}", "-c", code), interval, runtime, enabled)


def write_config(tmp_path, items):
    path = tmp_path / "jobs.json"
    path.write_text(json.dumps({"jobs": items}), encoding="utf-8")
    return path


def config_item(**changes):
    return {
        "name": "test", "command": ["{python}", "-c", "pass"],
        "interval_seconds": 10, "max_runtime_seconds": 1, **changes,
    }


def test_due_disabled_and_no_catchup(tmp_path):
    now = [100.0]
    ran = []
    events = []

    def execute(item, stop, cwd):
        ran.append(item.name)
        now[0] += 25
        return Result("success", 0)

    runner = Runner(
        [job(), job("disabled", False)], tmp_path / "locks", tmp_path,
        clock=lambda: now[0], execute=execute,
        emit=lambda event, **fields: events.append((event, fields)),
    )
    runner.tick()
    assert ran == ["test"]
    assert runner.next_due["test"] == 130
    runner.tick()
    assert ran == ["test"]
    now[0] = 130
    runner.tick()
    assert ran == ["test", "test"]
    assert runner.next_due["test"] == 160


def test_exact_due_and_clock_jump(tmp_path):
    now = [0.0]
    calls = []
    runner = Runner([job()], tmp_path, tmp_path, clock=lambda: now[0],
                    execute=lambda *args: (calls.append(1) or Result("success", 0)),
                    emit=lambda *args, **kwargs: None)
    runner.tick()
    now[0] = 9.999
    runner.tick()
    assert len(calls) == 1
    now[0] = 10
    runner.tick()
    now[0] = 1000
    runner.tick()
    assert len(calls) == 3
    assert runner.next_due["test"] == 1010


def test_lock_skips_overlap_and_is_reusable(tmp_path):
    first = JobLock(tmp_path, "test")
    second = JobLock(tmp_path, "test")
    assert first.acquire()
    try:
        assert not second.acquire()
        events = []
        runner = Runner([job()], tmp_path, tmp_path,
                        execute=lambda *args: pytest.fail("overlap ran"),
                        emit=lambda event, **kwargs: events.append(event))
        assert runner.run(once=True) == 0
        assert "overlap_skipped" in events
        other = JobLock(tmp_path, "different")
        assert other.acquire()
        other.release()
    finally:
        first.release()
    assert second.acquire()
    second.release()


def test_lock_is_cross_process_and_released_on_crash(tmp_path):
    code = (
        "import sys,time; from pathlib import Path; from backend.job_runner import JobLock;"
        " lock=JobLock(Path(sys.argv[1]), 'test');"
        " print(lock.acquire(), flush=True); time.sleep(60)"
    )
    child = subprocess.Popen([sys.executable, "-c", code, str(tmp_path)],
                             cwd=ROOT, stdout=subprocess.PIPE, text=True)
    try:
        assert child.stdout.readline().strip() == "True"
        lock = JobLock(tmp_path, "test")
        assert not lock.acquire()
    finally:
        child.kill()
        child.wait(timeout=5)
        child.stdout.close()
    assert lock.acquire()
    lock.release()


def test_no_enabled_jobs_and_dry_run_have_no_side_effects(tmp_path):
    lock_dir = tmp_path / "missing"
    runner = Runner([job(enabled=False)], lock_dir, tmp_path,
                    execute=lambda *args: pytest.fail("disabled ran"))
    assert runner.run() == 0
    enabled = Runner([job()], lock_dir, tmp_path,
                     execute=lambda *args: pytest.fail("dry run executed"))
    assert enabled.run(dry_run=True) == 0
    assert not lock_dir.exists()


def test_disabled_by_default_and_example_has_only_disabled_jobs(tmp_path):
    assert not load_jobs(write_config(tmp_path, [config_item()]))[0].enabled
    jobs = load_jobs(ROOT / "config/jobs.example.json")
    assert {item.name for item in jobs} == {"ingest", "embedding", "tagging"}
    assert all(not item.enabled for item in jobs)
    assert all("--dry-run" in item.command for item in jobs)
    examples = json.loads((ROOT / "config/jobs.example.json").read_text(encoding="utf-8"))
    assert all(item["overlap_policy"] == "skip" for item in examples["jobs"])


def test_job_overlap_policy_default_preserves_positional_enabled():
    assert Job("test", ("echo",), 10, 1).overlap_policy == "skip"
    item = Job("test", ("echo",), 10, 1, True)
    assert item.enabled is True
    assert item.overlap_policy == "skip"


@pytest.mark.parametrize("changes", [{}, {"overlap_policy": "skip"}])
@pytest.mark.parametrize("enabled", [False, True])
def test_load_jobs_accepts_skip_overlap_policy(tmp_path, changes, enabled):
    item = load_jobs(write_config(tmp_path, [config_item(enabled=enabled, **changes)]))[0]
    assert item.overlap_policy == "skip"
    assert item.enabled is enabled


@pytest.mark.parametrize("value", [
    "", "queue", "replace", "parallel", "SKIP", " skip", "skip ",
    None, True, False, 0, 1, 1.5, [], ["skip"], {}, {"policy": "skip"},
])
@pytest.mark.parametrize("enabled", [False, True])
def test_load_jobs_rejects_invalid_overlap_policy_even_if_disabled(tmp_path, value, enabled):
    with pytest.raises(ValueError, match="overlap_policy"):
        load_jobs(write_config(tmp_path, [config_item(enabled=enabled, overlap_policy=value)]))


@pytest.mark.parametrize("changes", [
    {"name": "../unsafe"}, {"name": "TEST"}, {"name": ""}, {"command": "echo hello"},
    {"command": []}, {"command": [""]}, {"command": ["x\0"]}, {"command": [1]},
    {"enabled": "false"}, {"enabled": 1}, {"interval_seconds": 0},
    {"interval_seconds": -1}, {"interval_seconds": True},
    {"interval_seconds": float("nan")}, {"max_runtime_seconds": float("inf")},
    {"interval_seconds": 1e-320}, {"max_runtime_seconds": 10 ** 500},
    {"max_runtime_seconds": None}, {"cron": "* * * * *"}, {"function": "work"},
    {"unknown": 1},
])
def test_invalid_job_configs(tmp_path, changes):
    with pytest.raises(ValueError):
        load_jobs(write_config(tmp_path, [config_item(**changes)]))


@pytest.mark.parametrize("data", [
    "not json", "[]", '{"jobs": {}}', '{"other": []}',
    '{"jobs": [], "jobs": []}', '{"jobs": [null]}', '{"jobs": [{}]}',
])
def test_invalid_config_shapes(tmp_path, data):
    path = tmp_path / "jobs.json"
    path.write_text(data, encoding="utf-8")
    with pytest.raises(ValueError):
        load_jobs(path)


def test_duplicate_names_and_missing_config(tmp_path):
    with pytest.raises(ValueError, match="duplicate job name"):
        load_jobs(write_config(tmp_path, [config_item(), config_item()]))
    with pytest.raises(OSError):
        load_jobs(tmp_path / "missing")


def test_real_command_success_failure_and_literal_argv(tmp_path):
    stop = threading.Event()
    assert run_command(job(), stop, tmp_path) == Result("success", 0)
    assert run_command(job(code="raise SystemExit(7)"), stop, tmp_path) == Result("failed", 7)
    # No shell interpretation of argv.
    literal = Job("literal", ("{python}", "-c",
                  "import sys; assert sys.argv[1] == '$(echo unsafe); *'", "$(echo unsafe); *"),
                  10, 5, True)
    assert run_command(literal, stop, tmp_path).status == "success"


def test_real_subprocess_timeout(tmp_path):
    started = time.monotonic()
    result = run_command(job(runtime=0.1, code="import time; time.sleep(60)"),
                         threading.Event(), tmp_path)
    assert result.status == "timeout"
    assert result.returncode is not None
    assert time.monotonic() - started < 5


@pytest.mark.skipif(os.name == "nt", reason="POSIX process-group escalation")
def test_timeout_kills_term_ignoring_child(tmp_path):
    pidfile = tmp_path / "stubborn.pid"
    code = (
        "import os,signal,time; from pathlib import Path;"
        " signal.signal(signal.SIGTERM, signal.SIG_IGN);"
        f" Path({str(pidfile)!r}).write_text(str(os.getpid()));"
        " time.sleep(60)"
    )
    # Allow startup even under the external full-suite safety guard.
    result = run_command(job(runtime=1, code=code), threading.Event(), tmp_path)
    assert result == Result("timeout", -signal.SIGKILL)
    assert pidfile.exists()
    with pytest.raises(ProcessLookupError):
        os.kill(int(pidfile.read_text()), 0)


def test_stop_cleans_real_child_and_prevents_next_job(tmp_path):
    stop = threading.Event()
    timer = threading.Timer(0.2, stop.set)
    timer.start()
    try:
        result = run_command(job(runtime=60, code="import time; time.sleep(60)"), stop, tmp_path)
        assert result.status == "stopped"
        assert result.returncode is not None
        runner = Runner([job()], tmp_path / "locks", tmp_path, stop=stop,
                        execute=lambda *args: pytest.fail("ran after stop"))
        assert runner.run(once=True) == 0
        assert not (tmp_path / "locks").exists()
    finally:
        timer.cancel()
        timer.join()


def test_failure_timeout_and_spawn_error_exit_codes(tmp_path):
    for result in (Result("failed", 4), Result("timeout", -9)):
        runner = Runner([job()], tmp_path, tmp_path,
                        execute=lambda *args: result)
        assert runner.run(once=True) == 1
    missing = Job("missing", (str(tmp_path / "no-executable"),), 1, 1, True)
    assert Runner([missing], tmp_path, tmp_path).run(once=True) == 1
    # The failed process must not leave a held lock.
    lock = JobLock(tmp_path, "missing")
    assert lock.acquire()
    lock.release()


def test_lock_io_error_is_failure_not_overlap(tmp_path, monkeypatch, capsys):
    def fail(self):
        raise OSError("synthetic lock error")

    monkeypatch.setattr(JobLock, "acquire", fail)
    assert Runner([job()], tmp_path, tmp_path).run(once=True) == 1
    events = [json.loads(line) for line in capsys.readouterr().out.splitlines()]
    assert any(event["event"] == "job_failed" for event in events)
    assert not any(event["event"] == "overlap_skipped" for event in events)


def test_continuous_loop_stops_after_fake_job(tmp_path):
    stop = threading.Event()
    ran = []

    def execute(item, event, cwd):
        ran.append(item.name)
        event.set()
        return Result("stopped", -15)

    runner = Runner([job(), job("second")], tmp_path, tmp_path,
                    stop=stop, execute=execute)
    assert runner.run() == 0
    assert ran == ["test"]


def cli(*args, timeout=10):
    return subprocess.run([sys.executable, str(ROOT / "scripts/run_jobs.py"), *args],
                          cwd=ROOT, capture_output=True, text=True, timeout=timeout)


@pytest.mark.parametrize("mode", ["--list", "--dry-run", "--once"])
def test_default_cli_never_runs_jobs(tmp_path, mode):
    locks = tmp_path / "locks"
    result = cli(mode, "--lock-dir", str(locks))
    assert result.returncode == 0
    events = [json.loads(line) for line in result.stdout.splitlines()]
    assert not any(event["event"] in {"job_started", "would_run"} for event in events)
    assert not locks.exists()


def test_cli_enabled_once_dry_run_list_and_bad_config(tmp_path):
    config = write_config(tmp_path, [config_item(enabled=True)])
    for mode in ("--once", "--dry-run", "--list"):
        result = cli(mode, "--config", str(config), "--lock-dir", str(tmp_path / "locks"))
        assert result.returncode == 0, result.stderr
        assert all(isinstance(json.loads(line), dict) for line in result.stdout.splitlines())
        if mode == "--list":
            events = [json.loads(line) for line in result.stdout.splitlines()]
            assert len(events) == 1
            assert events[0]["event"] == "job_config"
            assert events[0]["overlap_policy"] == "skip"
    assert cli("--config", str(tmp_path / "missing"), "--once").returncode == 2
    write_config(tmp_path, [config_item(command=["{python}", "-c", "raise SystemExit(7)"], enabled=True)])
    assert cli("--config", str(config), "--once", "--lock-dir", str(tmp_path / "locks")).returncode == 1
    write_config(tmp_path, [config_item(
        command=["{python}", "-c", "import time; time.sleep(60)"],
        max_runtime_seconds=0.1, enabled=True,
    )])
    result = cli("--config", str(config), "--once", "--lock-dir", str(tmp_path / "locks"))
    assert result.returncode == 1
    assert any(json.loads(line).get("status") == "timeout" for line in result.stdout.splitlines())


@pytest.mark.skipif(os.name == "nt", reason="Windows terminate is not catchable SIGTERM")
@pytest.mark.parametrize("signum", [signal.SIGTERM, signal.SIGINT])
def test_cli_actual_signal_cleans_child_and_releases_lock(tmp_path, signum):
    pidfile = tmp_path / "child.pid"
    config = write_config(tmp_path, [config_item(
        enabled=True, max_runtime_seconds=60,
        command=["{python}", "-c",
                 "import os,time; from pathlib import Path;"
                 f" Path({str(pidfile)!r}).write_text(str(os.getpid())); time.sleep(60)"],
    ), config_item(name="second", enabled=True)])
    locks = tmp_path / "locks"
    child = subprocess.Popen([sys.executable, str(ROOT / "scripts/run_jobs.py"),
                              "--config", str(config), "--lock-dir", str(locks)],
                             cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        deadline = time.monotonic() + 5
        while not pidfile.exists() and time.monotonic() < deadline:
            time.sleep(0.02)
        assert pidfile.exists()
        pid = int(pidfile.read_text())
        child.send_signal(signum)
        stdout, stderr = child.communicate(timeout=5)
        assert child.returncode == 128 + signum, stderr
        events = [json.loads(line) for line in stdout.splitlines()]
        assert not any(event.get("job") == "second" for event in events)
        with pytest.raises(ProcessLookupError):
            os.kill(pid, 0)
        lock = JobLock(locks, "test")
        assert lock.acquire()
        lock.release()
    finally:
        if child.poll() is None:
            child.kill()
            child.wait(timeout=5)


def test_runner_imports_only_stdlib():
    result = subprocess.run(
        [sys.executable, "-S", "-c",
         "import sys; import backend.job_runner;"
         " assert 'backend.database' not in sys.modules;"
         " assert 'dotenv' not in sys.modules"],
        cwd=ROOT, capture_output=True, text=True, timeout=5,
    )
    assert result.returncode == 0, result.stderr
