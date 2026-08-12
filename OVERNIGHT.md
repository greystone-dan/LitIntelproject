# Overnight Operations

The overnight runner executes jobs sequentially, holds an exclusive lock, writes
one log per job, and atomically updates `state.json` after every transition.
CanLII and all hosted-AI embedding jobs are intentionally excluded.

For a citations-only full-corpus refresh procedure, use
`docs/EXTRACTION_35K_RUNBOOK.md`.

## Readiness Snapshot

Operational guidance refresh:

- Do not rely on historical readiness counts in older handoff files.
- Re-run preflight before every unattended run.
- Use this file for run semantics; use `CHANGELOG.md` for latest test baseline.

Most recent verified full regression baseline in changelog: `113 passed`.

Historical baseline (2026-08-01):

- both `safe` and `pull` profiles pass live preflight
- the full regression suite passed at that time (`94 passed`)
- workspace diagnostics are clean
- PostgreSQL is reachable
- `35,902` cases are available for enrichment
- `35,519` text-bearing cases need chunks
- zero local BGE-M3 embeddings exist, so the local embedding job has a full backlog
- `18/18` reference documents pass the current manifest state

The run is ready to start. Do not run another PostgreSQL-writing maintenance job
at the same time.

## First Run Result

Historical run snapshot (`20260801-234642`, 2026-08-02):

- all `35,902` cases were tagged under `ca_legal_v2`
- all `35,902` cases now have chunks (`168,282` total)
- citations and local embeddings remained at zero because their direct-script
	subprocesses could not import `backend`
- those commands now use module mode and pass focused and full regression tests

Resume the same run to retry only failed jobs; completed tagging, chunking,
portal, and reference jobs will be skipped:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --resume 20260801-234642 --continue-on-error
```

## Recommended Full Run

Run from the repository root:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --continue-on-error
```

The safe profile runs, in order:

1. Official Federal Court IMM decision discovery and available document capture.
2. Federal Court IMM portal collection with page checkpointing.
3. Prototype IMM procedural-history backfill with per-record commits.
4. Reference-library checksum verification and resume.
5. `ca_legal_v2` deterministic tagging.
6. Resumable chunk creation for cases without stored chunks.
7. Citation extraction and metrics, including the new chunks.
8. Local BGE-M3 chunk embeddings.

Chunking uses the established 6,000-character size and 600-character overlap.
It commits every 50 cases and does not call an AI service. Cases that already
own chunks are skipped. Local BGE-M3 embedding then commits every four chunks,
uses CPU by default, and makes no hosted API calls. Its first execution may
download the BGE-M3 model files.

Use `--continue-on-error` overnight so one unavailable network source does not
prevent independent maintenance jobs from running.

## Pull Only

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile pull --continue-on-error
```

This runs only the three official Federal Court acquisition jobs.

## Preflight

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --profile safe --preflight
```

Preflight checks the interpreter, scripts, free disk space, and PostgreSQL when
selected jobs require it. It does not create a run or contact remote sources.

## Resume

Resume the latest interrupted or failed run:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --resume --continue-on-error
```

Resume a specific run:

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --resume 20260801-233659 --continue-on-error
```

Completed jobs are skipped. Failed and interrupted jobs are retried. Individual
collectors retain their own database, page, or record checkpoints as an
additional recovery layer.

## Status And Logs

Runs are stored under `data/overnight_runs/<run-id>/`:

- `state.json`: durable run and per-job status.
- `<job>.log`: complete combined stdout and stderr for that job.
- `data/overnight_runs/overnight.lock`: active-run lock, removed on clean exit.

Only use `--force-unlock` after verifying that no overnight Python process is
still active.

## Official Decision Discovery

`data/raw/fc/fc_decisions.db` currently contains 830 discovered official
Federal Court decision IDs. The source's embedded judgment endpoint may reject
automated payload requests even when discovery succeeds. Discovery records are
preserved; portal and procedural-history jobs continue independently. Do not
treat a discovered ID as proof that full text or a PDF was captured.