# Task: Metadata as standalone post-chunking stage

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Split metadata extraction into its own clean stage that runs after chunk
layers (full_case, heading_chunks) and before case citation and statute layers;
modularize `backend/metadata.py` internals without changing the public API.

Why now: Metadata fields usually appear at the beginning and end of a decision,
so chunk structure exists first and citation/statute extraction downstream
should see the normalized case state. The module had grown into a 500-line
monolith mixing outcome detection, government-role inference, subject
derivation, and span matching.

Owner surface: `backend/case_processing.py` stage order plus
`backend/metadata*.py` module split.

Dependencies: `fc_ingest.document_scraper` extractor, `backend.legal_tagger`,
`tests/test_metadata.py`, `tests/test_case_processing.py`.

Risk boundary: Public API (`extract_case_metadata`, `extract_metadata_observations`,
`extract_metadata_matches`, `MetadataMatch`, `MetadataObservation`,
`METADATA_FIELDS`) must keep working from `backend.metadata`. No extraction-rule
behavior changes; this is ordering + structure only.

Smallest falsifiable check: `pytest tests/test_metadata.py tests/test_case_processing.py -q`

Acceptance criteria:

- STAGE_ORDER is (`full_case`, `heading_chunks`, `metadata`, `case_citations`, `statutes`)
- Outcome/role helpers live in a focused module; subject-field derivation in another
- Existing metadata and processing tests pass unchanged in behavior

Docs/generated references: SYSTEM_REFERENCE.md pipeline description if order is
documented there; no generated docs touched.

Rollback/recovery: `git checkout backend/case_processing.py backend/metadata*.py tests/test_case_processing.py`

Evidence: `pytest tests/test_metadata.py tests/test_case_processing.py -q` -> 10 passed in 1.86s. `py_compile` on backend/metadata.py, metadata_outcomes.py, metadata_subjects.py, case_processing.py, reader_service.py, routes.py, scripts/backfill_case_metadata_outcomes.py -> compile-ok. Grep confirmed all consumers import only the public API from `backend.metadata`.

## Hypothesis

If the stage order and module split are correct, the focused metadata and
processing tests pass with the new order asserted and all extraction behavior
unchanged.

## Plan

1. Update stage order and its test assertion.
2. Split private helpers into `backend/metadata_outcomes.py` and
   `backend/metadata_subjects.py`; keep `backend/metadata.py` as public facade.
3. Run `pytest tests/test_metadata.py tests/test_case_processing.py -q`.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-04 | Task created | User confirmed metadata should run after chunking, before citations; module needs modularization | user request |

## Completion

Status: complete

Summary: Stage order changed to (full_case, heading_chunks, metadata, case_citations, statutes). `backend/metadata.py` is now a public facade; outcome/role helpers moved to `backend/metadata_outcomes.py` and subject-field derivation to `backend/metadata_subjects.py`. No extraction-rule behavior changed.

Validation: 10 focused tests passed; compile check passed on all touched modules and consumers.

Residual risk: Metadata field quality itself (weak title/judge/date coverage on some source families) is unchanged by this refactor and remains the known limitation to QA next.

Next recommended task: Bounded metadata QA sample across courts (title, judge, date, citation, docket) before expanding citation-extraction work.
