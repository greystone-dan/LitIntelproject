# Standalone background jobs

`scripts/run_jobs.py` runs opt-in interval commands using the standard-library
implementation in `backend/job_runner.py`. It is a separate process, never
started by FastAPI or imported into its lifecycle. It neither imports
`backend/database.py` nor loads `.env`; children retain their own existing
configuration and operational requirements. Existing batch scripts and
`backend/batch_jobs.py` are unchanged.

## Safe first commands

Run from the repository root with your chosen Python environment:

```bash
python scripts/run_jobs.py --help
python scripts/run_jobs.py --list
python scripts/run_jobs.py --dry-run
python scripts/run_jobs.py --once
```

The default `config/jobs.example.json` contains only **disabled** ingestion,
local embedding and tagging examples, all bounded and using their scripts'
dry-run flags. No job runs by default, including in continuous mode; the runner
exits successfully when there are no enabled jobs. No bulk reembedding is
enabled. Inspect each script's documentation before preparing your own config.
The ingestion example requires an operator-supplied source endpoint.

## JSON contract

The root object contains only `jobs`, an array. Every entry requires:

| Field | Contract |
| --- | --- |
| `name` | Unique lowercase identifier, 1–64 characters; starts with a letter, then letters, digits, `_` or `-`. Also determines the cross-runner lock identity. |
| `command` | Nonempty array of nonempty argv strings; never a shell string. NUL bytes are rejected. `{python}` as a whole argument expands to the runner's interpreter. |
| `interval_seconds` | Number from 0.01 through 315360000 seconds (ten years); booleans and nonfinite numbers are rejected. |
| `max_runtime_seconds` | Same numeric range; bounds the launched child runtime. |
| `enabled` | Optional boolean, default `false`. |
| `overlap_policy` | Optional string, default `"skip"`; the only accepted value is exactly `"skip"`. All other values reject the config, including for disabled jobs. |

Unknown fields, missing required fields, duplicate JSON keys and duplicate job
names reject the **entire config before execution**. Empty `jobs` is valid.
Only interval scheduling and argv commands are supported; there is no cron
parser, function registry, shell expansion, env substitution or hot reload.
Commands run with repository-root working directory and inherited environment.
Treat config as trusted executable instructions; never put secrets in argv.

Copy the example and opt in explicitly with `enabled: true`. Supply that file
with `--config PATH`. `--list` validates and lists scheduling metadata,
including the effective `overlap_policy`;
`--dry-run` validates and logs what would run, then exits. Neither launches
commands nor creates lock files. `--once` runs each enabled job once, unless
its lock is busy, then exits; it still obeys timeouts and signal cleanup.
These three modes are mutually exclusive.

## Scheduling and overlap

- Enabled jobs are immediately due at each runner start. Schedules are held
  **in memory**, not persisted across restarts.
- Monotonic time determines interval slots; wall-clock changes have no effect.
- Commands execute **sequentially in configuration order**, never in parallel
  within one runner. A slow earlier job can delay later jobs.
- After execution, failure or lock skip, advance to the next future interval
  slot. Missed slots are discarded, not replayed. If a job outlasts its interval,
  it cannot spin in a catch-up loop.
- A nonblocking per-name filesystem lock skips a due job if another runner
  already holds its lock. It does not queue or retry until the next slot.
- POSIX uses `flock`; Windows uses `msvcrt.locking` on the file's first byte.
  Locks are database-free and kernel-released when the runner exits or crashes.
  Persistent `.lock` files are not evidence of active work: **do not delete
  them**, because replacing an inode can break mutual exclusion.
- The default lock directory is `data/job_runner_locks`. All cooperating
  runners must use the **same directory and stable job names**, on a local
  filesystem supporting these locks. `--lock-dir PATH` changes that directory.
  This is host-local coordination, not a distributed lease.

Different job names, different lock directories, direct script invocations and
the overnight runner do **not** share this exclusion. Before enabling a writer,
confirm no other bulk PostgreSQL writer is active. Per-job exclusion is not
permission to run different bulk writers concurrently. Existing source terms,
limits, preflight, dry-run, approval and resume rules still apply.

## Stop, cleanup and logs

SIGINT/SIGTERM set a stop event: no subsequent job is started. On POSIX,
timeout/stop sends TERM to the child's isolated process group, waits up to one
second, then sends KILL to remove remaining members and reaps the child.
On Windows, timeout/stop uses the built-in `taskkill /PID ... /T /F` for the
child tree (bounded to five seconds), with direct-child kill as a fallback if
taskkill is unavailable, times out or reports failure. That fallback cannot
guarantee descendant cleanup.
Windows forcibly terminating the runner is not equivalent to delivering a
catchable signal; use Ctrl+C for an orderly stop.

Use synchronous commands that do not daemonize, detach or escape their process
group. SIGKILL, power loss and forced runner termination cannot guarantee child
cleanup; inspect for orphaned children before restarting. A timeout or stop
does not roll back a child's committed work; its own checkpoint/recovery
contract remains authoritative. Do not add deployment/service hooks here.

Stdout contains newline-delimited JSON events with UTC timestamp, event name,
job name where applicable, completion status/return code and elapsed seconds.
Config errors and OS errors are logged without sensitive exception text.
Argv and child stdout/stderr are deliberately omitted/discarded; commands
needing durable diagnostics must use their existing log-file options.
Failures/timeouts are recorded and later due jobs can still run. Continuous
mode does not stop on a failed job; its final exit status remembers failures.

| Exit | Meaning |
| --- | --- |
| `0` | Success, no enabled jobs, dry-run/list success, or overlap-only skips |
| `1` | Any child nonzero exit, timeout, spawn error or lock I/O failure |
| `2` | Invalid/unreadable config or invalid CLI arguments |
| `130` | Runner stopped by SIGINT (takes precedence over earlier failures) |
| `143` | Runner stopped by SIGTERM (takes precedence over earlier failures) |

## Windows Task Scheduler setup (future PC use, manual approval only)

These are documentation-only instructions for an operator's future workstation.
**Obtain explicit approval before creating, enabling or running a task.**
This change registers no tasks and adds no deployment scripts. Create a
separate task named, for example, **AI CaseLibrary Background Jobs**; never
modify, reuse or couple it to the existing **iLitSite** task or web startup.

The workstation repository working directory is
`"C:\Users\danny\OneDrive\Desktop\AI CaseLibrary"`. Verify the project venv
and prepare an operator-owned config at the absolute path below, initially
with every job disabled. Do not use global Python. Review limits, dry runs,
source terms and writer coordination before opting any job in.

1. Manually inspect the config in a foreground PowerShell session first:

   ```powershell
   Set-Location -LiteralPath "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary"
   & "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\venv\Scripts\python.exe" "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\scripts\run_jobs.py" --config "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\config\jobs.operator.json" --list
   & "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\venv\Scripts\python.exe" "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\scripts\run_jobs.py" --config "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\config\jobs.operator.json" --dry-run
   ```

2. After approval, open **Task Scheduler → Create Task** manually. Use the
   separate name above, the intended workstation user, and **Run only when
   user is logged on** for the initial supervised trial. Do not request highest
   privileges unless separately justified and approved. Leave **Triggers**
   empty: initial use is manual, not startup/logon or unattended scheduling.

3. Add one **Start a program** action with these values:

   | Field | Value |
   | --- | --- |
   | Program/script | `"C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\venv\Scripts\python.exe"` |
   | Add arguments | `"C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\scripts\run_jobs.py" --config "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\config\jobs.operator.json" --lock-dir "C:\Users\danny\AppData\Local\AI CaseLibrary\job_runner_locks"` |
   | Start in | `C:\Users\danny\OneDrive\Desktop\AI CaseLibrary` |

   The fully quoted directory is
   `"C:\Users\danny\OneDrive\Desktop\AI CaseLibrary"`; enter it **without the
   surrounding quote characters in the Start in field**, which expects a
   directory rather than a command-line argument. Program and argv paths
   above are fully quoted because they contain spaces. No shell, batch wrapper
   or deployment script is needed. Continuous mode maintains its own intervals;
   add `--once` only for an approved one-pass trial.

4. In **Settings**, select **If the task is already running → Do not start a
   new instance**. This complements, not replaces, the runner's kernel-backed
   per-job locks. Every cooperating foreground or scheduled runner must use
   the same local lock directory and stable job names; do not use a synced
   OneDrive lock directory for cross-machine coordination. Do not delete lock
   files. Neither lock mechanism excludes direct scripts, the overnight runner
   or differently named jobs: confirm no other bulk PostgreSQL writer is
   active before each approved writer run.

5. Avoid automatic execution time limits, forced stops on idle/power changes,
   and automatic restart-on-failure during the supervised trial. The child
   `max_runtime_seconds` remains enforced by the runner. Save the task and
   explicitly **Disable** it before leaving Task Scheduler; keep it disabled
   with no triggers until an operator approves enablement. For a trial,
   explicitly enable and **Run** it manually, then disable it again after
   confirming the runner and its children have exited. Any later automatic
   trigger or unattended enablement needs separate approval.

### Windows logs, retention and stopping

The runner emits newline-delimited JSON to stdout; **Task Scheduler history
does not retain that stream**, and the direct Python action above adds no
stdout capture. Before enabling unattended use, approve a durable JSON log
capture/rotation arrangement; it is not implemented by these instructions.
For a supervised foreground trial, an operator can manually capture stdout
without creating a script (first create the local log directory manually):

```powershell
& "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\venv\Scripts\python.exe" "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\scripts\run_jobs.py" --config "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\config\jobs.operator.json" --lock-dir "C:\Users\danny\AppData\Local\AI CaseLibrary\job_runner_locks" --once | Tee-Object -FilePath "C:\Users\danny\AppData\Local\AI CaseLibrary\job_runner_logs\approved-trial-001.jsonl"
```

Use a fresh run-specific filename, retain the JSON events and any child-owned
logs/checkpoints together, and agree a retention period before use (for
example, 30 days for successful trials). Preserve failed/interrupted run
evidence until recovery is accepted; review/archive old logs manually rather
than silently overwriting them. There is no built-in log rotation or retention
deletion. Child stdout/stderr is discarded, so JSON events are not a substitute
for script-specific diagnostics. Do not put secrets in configs, argv or logs.

**Task Scheduler End, forced task stop and machine shutdown are not graceful
SIGINT delivery.** They can bypass runner cleanup and leave orphaned children;
kernel lock release on runner exit does not prove its children exited. For an
orderly stop use Ctrl+C in a foreground runner. After a forced scheduled stop,
inspect the specific runner/child processes and their logs/checkpoints, confirm
all writers stopped, and follow each child's recovery contract before restart.
Disablement alone does not stop an already running task. Do not infer rollback
of committed work or launch another writer merely because the task says stopped.

## Focused validation

```bash
python -m pytest -q tests/test_job_runner.py --noconftest
python scripts/generate_script_catalog.py
python scripts/check_generated_docs.py
git diff --check
```

The focused test uses fake clocks/jobs and harmless subprocesses for actual
timeouts, locks and signals. `--noconftest` avoids the existing suite's
PostgreSQL availability probe. Actual SIGINT/SIGTERM process tests are
POSIX-only; Windows lock/timeout branches need a Windows validation run.
No live jobs, database operations, deployment or dependency changes are needed.

See [architecture inventory](ARCHITECTURE.md),
[overnight ownership boundaries](../OVERNIGHT.md),
[generated script catalog](SCRIPT_CATALOG.generated.md), and the
[operations walkthrough](../.swm/8.upryk5h6.sw.md).

## Issue #196 review checkpoint

- Task: Close explicit overlap config and future Windows setup requirements.
- Why now: Parent review found both missing from the uncommitted runner slice.
- Owner surface: Standalone background-job operations.
- Dependencies: Existing runner and disabled examples; no new dependencies.
- Risk boundary: No DB or `.env` access, batch-script changes, task registration,
  deployment, commits or pushes. Commit allowed: no. Push allowed: no.
- Smallest falsifiable check: `python -m pytest -q tests/test_job_runner.py --noconftest`;
  omitted/explicit `"skip"` must pass, every other policy must fail.
- Acceptance criteria: Strict policy validation, example/list metadata and
  docs-only manual Windows setup with approval, locks and recovery caveats.
- Docs/generated references: This runbook and `.swm/8.upryk5h6.sw.md`;
  generated references checked, never hand-edited.
- Rollback/recovery: Remove only this review's policy additions and Windows
  explanation; preserve the existing uncommitted issue work.
- Evidence: Coordinator ran `python -m pytest -q tests/test_job_runner.py --noconftest`
  (88 passed), `PYTHONPATH=/tmp/caselibrary-job-test-guard python scripts/check_generated_docs.py`
  (all three references current, dotenv reads/live DB connections blocked),
  and `python scripts/run_jobs.py` with `--help`, `--list`, `--dry-run`,
  `--once` and no mode (all exit 0; defaults execute no jobs).
  Updated Swimm: `.swm/8.upryk5h6.sw.md`; updated canonical runbook:
  `docs/BACKGROUND_JOBS.md`. Local links and `git diff --check` passed.
  The managed worker changed only runner/config/test files; the coordinator
  performed all final checks. This record stays in the requested runbook to
  respect the no-new-Markdown constraint.
- Residual risk: Windows Task Scheduler/lock/cleanup behavior was not tested
  on this Linux host; direct scheduled stdout capture remains operator-owned.
  The previously reported broad-suite dependency/network failures were not
  rerun or claimed fixed.
- Next recommended task: An approved Windows supervised validation of locks,
  timeout cleanup and durable JSON capture before any unattended enablement.
- Status: complete.
