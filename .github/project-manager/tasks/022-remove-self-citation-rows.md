# Task: Remove Confirmed Self-Citation Rows

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Delete all existing citation rows where source and target case IDs are identical, then refresh citation metrics.
Why now: The user explicitly authorized removal after the bounded audit classified the population as source-header and self-link artifacts; the quality gate is blocked by these rows.
Owner surface: `citations` table and citation metrics refresh
Dependencies: `scripts/evaluate_data_quality.py`, `backend/citations.py`, `backend/database.py`
Risk boundary: Delete only exact `source_case_id = target_case_id` rows; do not alter unresolved non-self citations, statutes, tags, cases, chunks, or sources. Stop if the pre-delete count is unexpectedly different from the measured 241,272 without confirmation.
Smallest falsifiable check: Pre-count exact self-citation rows, delete within one transaction, recompute metrics, and verify exact self-citation count is zero.
Acceptance criteria: Exact self-citation count reaches zero; citation metrics are recomputed; quality gate no longer fails on self-citations; full tests pass.
Docs/generated references: Swimm Technical Debt Register and Improvement Queue; Swimm Evaluation Framework and Quality Metrics; `OVERNIGHT.md`.
Rollback/recovery: Database backup/restore is the recovery path for this destructive operation; no application rollback can restore deleted rows.
Evidence: Pre-count matched the guarded expected count of 241,272. The cleanup exported all targeted citation rows to `C:\Users\danny\AppData\Local\Temp\ai-caselibrary-self-citations-20260904.csv` (25,110,170 bytes), deleted only rows where `source_case_id = target_case_id`, recomputed citation metrics, and verified zero remaining self-citations. Post-cleanup quality gate is `WARN` with 0 self-citations, 0 orphan targets, 0 invalid offsets, and 12.74% advisory statute pinpoint coverage. Full suite passed (`319 passed`); `git diff --check` passed.
