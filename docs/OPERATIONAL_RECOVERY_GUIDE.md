# Operational Recovery Guide

Last reviewed: 2026-09-01

Use this guide when the application, source collection, enrichment, migration, test, tunnel, or Git publish workflow fails. It is deliberately conservative: identify the owner and persisted state first, then resume or repair the narrow failed layer. Do not start a second bulk database writer while the first may still be active.

## First Response

1. Stop and record the command, time, working directory, error, and affected dataset/table/route.
2. Determine whether the failed process is still active before rerunning anything.
3. Preserve logs, run state, source artifacts, and database error text. Do not delete them to clear a symptom.
4. Classify the failure: configuration, server, database, migration, source access, enrichment, browser/UI, test, tunnel, or Git/LFS.
5. Use the smallest relevant check before escalating to a full run.

## Overnight Runner And Bulk Jobs

### Lock Conflict Or Interrupted Run

Inspect `data/overnight_runs/<run-id>/state.json`, the per-job logs, and `data/overnight_runs/overnight.lock`. The runner changes a `running` job to `interrupted` when state is reloaded after interruption.

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --resume --continue-on-error
```

Use `--force-unlock` only after confirming the PID recorded in `overnight.lock` is not running. A stale lock is recoverable; deleting a live lock permits concurrent writers and can corrupt/reconcile work unpredictably.

### Job Failed But Others Completed

Read `<job>.log`, then rerun only the failed job through `--jobs` or resume the run. Completed jobs are skipped on resume. Use `--continue-on-error` when independent source acquisition should not block deterministic enrichment.

### Bulk Writer Appears Stalled

Check whether log output/state timestamps advance and whether the owning Python process exists. Check database activity before terminating a process. If stopped, resume from the runner/state or documented `--start-after-id` position. Do not launch a duplicate `chunk_cases`, citation rebuild, tag, embedding, import, or backfill process.

## Database And Migration Failures

### Wrong Database Or Authentication Failure

Inspect `POSTGRES_*` and `DATABASE_URL` without printing secret values. `backend/database.py` prefers explicit `POSTGRES_*` whenever any is present. Confirm connectivity with a bounded query:

```powershell
.\venv\Scripts\python.exe -c "from sqlalchemy import text; from backend.database import engine; c=engine.connect(); c.execute(text('SELECT 1')); c.close(); print('ok')"
```

Correct the intended local `.env`/`backend/.env` settings, then retry the narrow command. Do not run migrations against an uncertain database target.

### Migration Error

Check current revision and the failing migration before retrying:

```powershell
.\venv\Scripts\python.exe -m alembic current
.\venv\Scripts\python.exe -m alembic heads
.\venv\Scripts\python.exe -m alembic upgrade head
```

Back up a production/shared database before repair. Do not manually mark a migration applied unless the schema matches its intended state. Compare the generated schema reference with direct database inspection when drift is suspected.

## Server, Browser, And Tunnel Failures

### UI Shows Old Code Or Routes Behave Inconsistently

Identify the process that owns the configured port. Multiple Uvicorn instances can serve different code revisions. Refresh the controlled local process/tunnel workflow:

```powershell
.\scripts\refresh_site.ps1
```

Then check the local route and a lightweight API route. For reader/UI failures, check browser console errors before changing backend logic: inline JavaScript escaping in `routes.py` can break the page while Python still imports.

### Local Service Works But Tunnel Returns 502/Unavailable

First verify `http://127.0.0.1:8000/health`. A short initial 502 can occur while the server process binds. If local health is good, inspect the active Cloudflare process/config and wait only for normal startup; otherwise restart with the controlled refresh script. Do not assume a tunnel provides authentication.

### Reader Highlights Or Linked Context Missing

Verify the reader-data or analytics case payload has chunks/citations, then check citation `chunk_id`, offsets, resolution target, and browser script errors. Offset repairs belong in extractors/stored data, not browser-only heuristics. Use `/citation-pass` to compare stored and live deterministic evidence.

## Source Acquisition Failures

### Federal Court Or CanLII Request Blocked

Record HTTP status and response evidence. Respect source access controls; do not bypass anti-bot protections. Preserve discovered IDs/staging state and use documented API, source fallback, bounded collector, or resume behavior. Discovery does not equal document capture.

### Reference Library Download Fails Validation

The downloader intentionally rejects invalid MIME/signature/content combinations. Inspect manifest entry URL, redirect target, content type, and error reason. Correct the manifest/source classification only when verified, then rerun the selected source with `--source-id`; do not force an HTML error page into a PDF snapshot.

### A2AJ/Canlaw Import Problem

Use `--dry-run` and small `--limit` first. Verify input schema, source URL/API configuration, court filter, and canonical ingest endpoint. Preserve staging data; bridge it through canonical ingestion so deduplication, source precedence, provenance rows, and ingestion-run records apply.

## Enrichment And Quality Failures

### Citation Or Statute Counts Change Unexpectedly

Identify whether the count is case citation occurrences, resolved targets, aggregated edges, statute references, or unique authorities. They are different layers. Use a bounded case/sample audit and `/citation-pass`; verify chunk offsets and provenance before changing patterns. Do not place statute rows in `citations` to satisfy an old expectation.

### IRPA/IRPR Provision Miss

Create a focused deterministic fixture containing the exact form, including punctuation and heading/running-text context. Run the statute-focused test slice, then inspect `extract_statute_reference_matches()`. Nested forms such as `34(1)(f)` are release-sensitive; broaden rules only with precision safeguards.

### Metadata, Tag, Or Docket Quality Problem

Run the relevant audit/build script with a small limit, inspect confidence/source/evidence fields, and correct the extractor or source mapping. Preserve `_quality_flags` and `_needs_review`; do not overwrite low-confidence source data with an untraceable display value.

### Embedding Failure Or Dimension Mismatch

Confirm model name, configured device, dependencies, available disk/memory, and expected vector dimension before retrying. BGE-M3 local chunk vectors expect 1024 dimensions; common OpenAI case vectors use 1536. A model change may require schema/index/retrieval changes, not just a new environment variable.

## Test And Documentation Failures

### Test Failure

Run the narrow test first. Determine whether it asserts the active contract or an obsolete design. Current known stale expectations include statutes being in `citations` and retired standalone-reader wording. Update the test only after confirming the active route/data model contract; do not regress runtime behavior to satisfy stale copy.

### Generated Documentation Is Stale

Regenerate the relevant appendix after source changes:

```powershell
.\venv\Scripts\python.exe scripts\generate_api_reference.py
.\venv\Scripts\python.exe scripts\generate_schema_reference.py
.\venv\Scripts\python.exe scripts\generate_work_history.py
.\venv\Scripts\python.exe scripts\generate_script_catalog.py
```

Then run link validation and `git diff --check`. Update human-maintained source registers and operational guides when a new integration or recovery path is introduced.

## Git And Git LFS Failures

### GitHub Rejects a Large File

Check file size before retrying. GitHub rejects ordinary Git blobs larger than 100 MB. Use Git LFS for deliberate large generated artifacts, or keep nonessential/generated bulk output outside Git. Do not rewrite/reset unrelated local work to make a push succeed.

### LFS Transfer Is Interrupted

The local commit and LFS pointer remain intact. Confirm `git status`, `git lfs status`, and remote tracking state, then resume `git push origin main` only when the transfer is intentional. A clean local worktree can still be ahead of `origin/main`.

### Dirty Worktree Before Recovery

Inspect `git status --short`, then preserve unrelated user changes. Stage/commit only deliberate work. Use `git diff --check` before committing. Never use destructive reset/checkout commands as a routine recovery mechanism.

## Escalation Record

When a problem cannot be repaired locally, capture:

1. Command and exact arguments.
2. Environment category, not secret values.
3. Current Git commit and migration revision.
4. Source/case/job/run identifiers.
5. Error output and relevant log path.
6. Before/after table counts if a write was attempted.
7. Whether the process remains active.
8. The smallest reproducing fixture or route request.

This record is sufficient for a later developer or agent to continue without repeating an unsafe broad operation.