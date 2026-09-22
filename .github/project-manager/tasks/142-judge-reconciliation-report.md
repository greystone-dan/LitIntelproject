# Task: Judge identity reconciliation report

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Produce a bounded, read-only reconciliation report for stored judge metadata and canonical judge profile links.

Why now: The extraction rule is improved for future processing, but existing metadata remains contaminated and profile links remain incomplete. Evidence is needed before any backfill or corpus write.

Owner surface: Judge identity reconciliation and reporting.

Commit allowed: yes

Push allowed: yes

Dependencies: `scripts/backfill_judge_profiles.py`, `fc_ingest.document_scraper._is_judge_junk`, `backend.database`, current database, and judge regression tests.

Risk boundary: Read-only only. Do not update `cases.metadata_json`, `judge_profiles`, or `case_judge_profiles`; do not run a bulk importer or external acquisition.

Smallest falsifiable check: A bounded command reports counts for total cases, non-empty raw judges, invalid stored values, raw judges without profile links, linked cases without valid raw judges, and representative review samples.

Acceptance criteria:

- Report is reproducible from the repository and uses the current shared validation rule.
- Report distinguishes invalid stored values from merely unlinked valid values.
- Report includes representative case IDs/titles/citations for manual source review.
- No database writes occur.
- Focused judge tests and report execution pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, this task record; no generated reference edits unless a generator is run.

Rollback/recovery: Delete or revert only the report implementation/documentation; no database recovery is required because the command is read-only.

Evidence: Added `scripts/judge_reconciliation_report.py` and regression coverage in `tests/test_judge_profiles.py`. The read-only report generated `data/eval/reports/judge_reconciliation_2026-09-22.json`: 61,261 total cases, 52,484 non-empty raw judges, 46,832 profileable, 5,652 invalid, 19,095 valid-unlinked, 3,587 invalid-linked, 31,324 links, 406 profiles, and 28,583 link/name mismatches. A letter-spaced location false positive was found and fixed in `fc_ingest/document_scraper.py`; `pytest tests/test_judge_profiles.py tests/test_metadata.py -q` passed with 27 tests. No database writes occurred.

## Hypothesis

If the shared profileability predicate is applied to stored metadata, the reconciliation report will separate known false-positive values from valid judge names lacking profile links and will produce a bounded review set without changing rows.

## Plan

1. Review the existing backfill and audit patterns through delegated read-only inspection.
2. Implement the smallest reusable read-only report command or script if no existing command covers the need.
3. Run the report, focused judge tests, compilation, and diff checks; document the measured result.

## Execution Checkpoints

- Delegation: Explore worker confirmed no existing committed reconciliation report and recommended a dedicated read-only script.
- Implementation: Added `scripts/judge_reconciliation_report.py`; tightened letter-spaced location rejection in `fc_ingest/document_scraper.py`; added focused test coverage.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`; report artifact recorded.
- Recovery: No data or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-22 | Task created | Extraction fix is deployed in code, but stored metadata and links have not been reconciled | Tasks 139 and 140; current judge profile backfill path |

## Completion

Completion recorded: yes

Summary: Completed a read-only reconciliation report and fixed the discovered letter-spaced location false-positive shape.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_judge_profiles.py tests/test_metadata.py -q` passed: 27 passed. Report execution completed with `read_only: true`; no database writes.

Residual risk: The report cannot determine the correct judge where source extraction is absent or ambiguous; manual/source review remains necessary.

Next recommended task: Review report samples, then plan a separate dry-run backfill with checkpointed writes.
