# Task: Establish Statute Extraction Baseline

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Create a dedicated IRPA/IRPR statute fixture set and deterministic exact-span baseline evaluator.
Why now: The quality gate reports only 12.74% statute pinpoint coverage, but the project lacks a focused fixture-level baseline separating precision from corpus coverage.
Owner surface: `backend/citations.py` extraction behavior and `scripts/evaluate_statute_extraction.py`
Dependencies: Existing `extract_statute_reference_matches`, nested IRPA/IRPR tests, `data/eval/`
Risk boundary: Evaluation-only first; do not change extraction rules or bulk-refresh statute rows until the baseline identifies a reproducible failure.
Smallest falsifiable check: Run the baseline evaluator against positive, negative, nested, and exact-span fixtures and require exact expected matches.
Acceptance criteria: Fixture report includes precision, recall, exact-span accuracy, false positives, false negatives, and per-fixture results; CLI returns nonzero on mismatch.
Docs/generated references: Swimm Evaluation Framework and Quality Metrics; Swimm Citation/Statute walkthrough; generated script catalog.
Rollback/recovery: Remove the baseline script and fixture set; no corpus data changes are made.
Evidence: Added `data/eval/statute_extraction_fixtures.json` and `scripts/evaluate_statute_extraction.py` covering nested IRPA/IRPR forms, exact offsets, section lists, and a negative unanchored-section case. Baseline passed 4 fixtures and 5 expected matches with 100% precision, 100% recall, 100% exact-span accuracy, and zero false positives/negatives. Focused tests passed (`81 passed`); generated script catalog refreshed; full suite passed (`320 passed`); `git diff --check` passed.
