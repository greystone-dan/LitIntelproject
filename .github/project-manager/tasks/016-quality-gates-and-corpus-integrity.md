# Task: Add Quality Gates and Corpus Integrity Reporting

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Add explicit pass/warn/fail quality gates to the existing corpus evaluator.
Why now: The project needs measurable release signals for citation trust, corpus integrity, and statute coverage before more intelligence work is layered on.
Owner surface: `scripts/evaluate_data_quality.py`
Dependencies: `tests/test_evaluate_data_quality.py`, `data/eval/`, PostgreSQL read-only evaluation access
Risk boundary: Read-only reporting only; do not modify corpus rows, delete self-citations, or establish arbitrary coverage thresholds without sampled evidence.
Smallest falsifiable check: Run the evaluator and verify critical integrity defects fail while unbaselined coverage reports advisory warnings.
Acceptance criteria: Reports include explicit gate status and checks; `--quality-gate` can return a blocking exit code; critical defects are not hidden.
Docs/generated references: Swimm Evaluation Framework and Quality Metrics; Swimm Technical Debt Register and Improvement Queue.
Rollback/recovery: Revert evaluator and focused test changes; no data rollback is required because the run is read-only.
Evidence: Extended `scripts/evaluate_data_quality.py` with explicit pass/warn/fail gates and an opt-in `--quality-gate` exit mode. Added regression tests for critical failures and advisory baselines (`3 passed`). The read-only live run reported `status=fail`: 241,272 self-citation rows, with 0 orphan targets, 0 invalid offsets, 62.0% citation resolution, and 12.74% statute pinpoint coverage. The failure was recorded in the Swimm debt register; no corpus rows were modified. Full regression validation remains required before release.
