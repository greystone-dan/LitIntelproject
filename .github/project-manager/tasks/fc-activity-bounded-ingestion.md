# Task: Bounded FC Activity discovery and ingestion

Status: in-progress
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Execute a bounded Federal Court Activity discovery, classification, and FC Activity-table ingestion sequence.

Why now: The FC Activity collector and schema are prepared; a small live run will prove the complete activity-only path before any independent worker deployment.

Owner surface: `scripts/fetch_fc_procedural_history.py` endpoint adapter and FC Activity persistence only.

Dependencies: Federal Court public source availability, configured FC Activity database connection, existing schema, and exclusive writer ownership.

Risk boundary: FC Activity tables only (`fc_activity_cases`, `fc_activity_documents`, and separately `fc_activity_classifications`). Do not write canonical `cases`, judgment text, citations, statutes, embeddings, or other case-ingestion tables. Use bounded limits, delays, checkpoints, and preserved staging artifacts. Do not inspect or print `.env`.

Smallest falsifiable check: Run a five-candidate sequential endpoint fetch with `--write-activity`, then verify stable rerun deduplication and unchanged canonical case counts.

Acceptance criteria:

- Bounded sequential endpoint collection completes or leaves an explicit failure.
- Activity records contain IMM source identity/provenance and are not described as captured judgments.
- Endpoint-to-Activity mapping preserves stable case/document hashes.
- A controlled write, if database connectivity and exclusive ownership are confirmed, changes only FC Activity tables.
- Post-write counts and deduplication are verified.
- Canonical documentation and the FC Swimm walkthrough record the actual run evidence.

Docs/generated references: `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, `OVERNIGHT.md`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/fc-ingest-source-pipeline.sw.md`. Generated references unchanged.

Rollback/recovery: Preserve staging/checkpoint artifacts. If an FC Activity write must be undone, use an explicit reviewed database recovery procedure; do not delete or alter canonical case data. Stop on source blocks, malformed payloads, uncertain checkpoint state, database contention, or missing writer ownership.

Evidence: Delegated Explore worker inspected the decision collector but could not execute commands in its environment. The decision-portal attempts were not used as FC Activity evidence: both exited 0 with `Scanned=0 Written=0` and created no artifacts. The correct FC Activity endpoint test then ran sequentially in dry-run mode: 5 candidate file numbers attempted, 63 activity records returned, exit code 0, endpoint reached, no database writes, and no output/checkpoint paths supported by the fetcher. The adapter was added behind `--write-activity`; focused tests passed, Python compilation passed, help exposed the flag, and `git diff --check` passed. Safety hardening uses a 2,000 ms default delay plus jitter and a hard API-attempt budget; the explicit `--diagnostic-allow-sub-2000ms-delay` override is reserved for tiny dry-run speed probes and does not change routine collection. The Court does not publish a robots policy, so the collector does not require one. The earlier 10-candidate dry-run stopped at the removed robots preflight with HTTP 404; that result is no longer a collection blocker. The live Activity-only write remains pending until the bounded operational checks and writer ownership are confirmed.

2025 upper-range probe evidence: sparse probes at 5,000, 10,000, 15,000, 20,000, and 25,000 all returned activity (6-9 entries each). Probes at 30,000 through 50,000 returned normally with zero entries, so these were empty source responses rather than transport failures. Bracket-and-refine probes found 27,500 active (8 entries), 28,125 active (6), 28,437 active (5), 28,750 empty, and no HTTP/retry failures. This establishes a sampled transition between 28,437 and 28,750 for activity-bearing 2025 IMM numbers; it is not a proof of a contiguous case count or a universal maximum IMM number.

Prior-year bracket-and-refine evidence: coarse 5,000-step probes and midpoint refinements returned no transport/retry failures. The sampled active-to-empty transitions are 2022 between 13,437 (9 entries) and 13,750 (empty); 2023 between 16,562 (8 entries) and 16,875 (empty); and 2024 between 24,687 (12 entries) and 25,000 (empty). These are activity-response transition intervals, not exact counts: IMM numbering may contain gaps, and an empty response does not prove that the number was never assigned.

Final 2023-2026 midpoint refinement, read-only and sequential, narrowed the sampled active-to-empty brackets to 2023: IMM-16,742-23 active / IMM-16,747-23 empty; 2024: IMM-24,784-24 active / IMM-24,789-24 empty; 2025: IMM-28,705-25 active / IMM-28,710-25 empty; and 2026: IMM-28,051-26 active / IMM-28,054-26 empty. No files or database records were changed and no transport/retry failures were reported.

Status: in-progress
Commit allowed: yes
Push allowed: yes

## Hypothesis

The existing FC Activity path can discover a bounded batch, classify it deterministically, and persist only FC Activity records without touching canonical case-ingestion tables.

## Delegated Work

Delegated Explore report: inspected `scripts/fc_portal_collector.py`, identified the bounded command contract, but could not execute it. Manager recovery executed the bounded commands directly after that limitation.

## Validation Log

Decision-portal discovery was inconclusive and is out of scope for FC Activity. Commands run:

- `venv\\Scripts\\python.exe scripts\\fc_portal_collector.py --prefixes IMM --max-records 5 --max-pages 1 --output-jsonl data\\raw\\fc\\portal_bounded_20260925.jsonl --checkpoint-json data\\raw\\fc\\portal_bounded_20260925_checkpoint.json`
- Same bounded command with default prefixes and retry-specific output/checkpoint paths.

Both returned exit code 0 but reported zero scanned/written records and created no artifacts. No classifier or writer command ran from those attempts.

FC Activity endpoint validation then passed with a bounded sequential dry-run: help exited 0; the generated/sequential endpoint run exited 0 after attempting 5 candidates and returning 63 activity records. No database write occurred.

Adapter validation passed:

- `venv\Scripts\python.exe -m pytest tests\test_fetch_fc_procedural_history_cli.py tests\test_classify_fc_activity.py tests\test_hf_fc_activity_ingest.py -q` -> 21 passed.
- `venv\Scripts\python.exe -m py_compile scripts\fetch_fc_procedural_history.py` -> exit 0.
- `venv\Scripts\python.exe scripts\fetch_fc_procedural_history.py --help` -> exit 0; `--write-activity` present.
- `git diff --check` -> exit 0.
- `venv\Scripts\python.exe -m pytest tests\test_fetch_fc_safety.py tests\test_fetch_fc_procedural_history_cli.py -q` -> 5 passed.
- `venv\Scripts\python.exe scripts\fetch_fc_procedural_history.py --imm-numbers IMM-5000-26 IMM-10000-26 IMM-15000-26 --delay-ms 2000 --jitter-ms 0 --max-requests 10 --dry-run` -> 3 processed, 0 HTTP/retry failures, 6 API attempts, entries 7/3/18.
- `--delay-ms 1500` without the diagnostic switch -> rejected locally before any endpoint attempt, preserving the routine 2,000 ms floor.
- With explicit `--diagnostic-allow-sub-2000ms-delay`, the same three-candidate dry-run was tested at 1,500 ms, 1,000 ms, and 500 ms with zero jitter and a 10-attempt cap. Each run exited 0, processed all 3 candidates, returned entries 7/3/18, used 6 API attempts, and produced 0 HTTP/retry failures. No 429, 403, 5xx, timeout, connection, or other rate-limit signal appeared. These are short diagnostic probes only and do not establish a safe unrestricted collection rate.
- A larger 20-candidate 2026 slice was then run at each of 1,500 ms, 1,000 ms, and 500 ms, with zero jitter, a 50-attempt cap, and dry-run mode. Every run exited 0, processed 20/20 candidates, returned 83 total activity entries, used 40 API attempts, and produced no HTTP/retry, 403, 429, 5xx, timeout, connection, or rate-limit signal. This supports the faster diagnostic observations for this sample, but does not authorize unrestricted collection or database writes.
- Adaptive speed control was added behind `--adaptive-delay`: the operator supplies the starting `--delay-ms`, checkpoints every `--batch-size` cases (default 20), pauses after fetch issues, and increases delay by `--backoff-factor` up to `--max-delay-ms`. The default issue pause is 5,000 ms and the default backoff factor is 2.0. A 20-case dry-run at 100 ms processed 20/20 candidates, returned 148 activity entries, used 40 API attempts, and reported no failures or rate-limit signals. Focused safety/CLI tests passed with 6 tests.
- Live monitoring is available through `--log-file`; output is mirrored to a line-buffered UTF-8 file, including candidate progress, warnings, adaptive pauses, checkpoints, and final request totals. A one-case dry-run smoke check confirmed start, fetch, and done lines in the log. The focused safety/CLI suite then passed with 6 tests.

## Documentation Checkpoint

Updated runbook, data-source register, and Swimm walkthrough with the distinction between decision discovery and FC Activity endpoint harvesting. Adapter and safety hardening are complete; the live FC Activity-only database write and post-write count verification remain pending behind bounded local throttling and writer-ownership checks. Canonical tables remain unchanged.
