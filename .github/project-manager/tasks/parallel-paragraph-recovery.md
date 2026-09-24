# Task: Parallel paragraph recovery

Status: in_progress
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Replay the recoverable paragraph-assessment failures with three bounded workers.
Why now: The paused run has valid partial model responses, and sequential recovery is unnecessarily slow.
Owner surface: `scripts/run_paragraph_assessment_batches.py`.
Dependencies: Existing paragraph ledger, deterministic reports, raw responses, and parser salvage behavior.
Risk boundary: Process only the explicitly selected recoverable case IDs; exclude truncated cases 2044 and 7567; no database writes.
Smallest falsifiable check: Focused runner test or bounded dry-run showing the selected IDs and worker count without network calls.
Acceptance criteria:
- Runner supports `--workers` with a bounded positive value.
- Runner supports an explicit `--case-ids` allowlist.
- Runner supports explicit exclusions for protected cases.
- Concurrent children do not write the shared ledger directly.
- Ledger and progress output record per-case elapsed time alongside cost.
- Truncated or partial responses are completed with explicit `Not found` rows.
- A bounded recovery command can target the 12 expected-recoverable failures and exclude 2044/7567.
Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`.
Rollback/recovery: Stop the recovery process; the ledger remains parent-owned and completed cases are skipped on rerun.
Evidence: Parser tests passed with 14 tests; scripts compiled; offline replay
of case 2044 recovered 243 assessment objects from a truncated response. The
earlier bounded
three-worker recovery completed cases 1147, 5465, and 9900; case 10047 failed;
cases 9342, 9411, 9448, 9501, 9697, 9903, and 9928 failed again; case 10091
was interrupted while active. Cases 2044 and 7567 remained excluded. Existing
case 10121 remains started from the earlier interruption. The process was
stopped after the monitoring window to avoid an unobserved run.
Commit allowed: yes
Push allowed: yes
