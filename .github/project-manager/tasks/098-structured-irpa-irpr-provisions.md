# Task: Structured IRPA/IRPR provision identity

Status: complete
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Add structured provision identity for IRPA/IRPR statute references while preserving raw text, exact offsets, and existing statute/case separation.

Why now: The legal-authority review found that nested provisions such as `34(1)(f)` are extracted, but `StatuteReference.pinpoint` is opaque and cannot support reliable provision queries or later authority-section resolution.

Owner surface: backend statute extraction and StatuteReference persistence contract

Commit allowed: yes

Push allowed: yes

Dependencies: backend/citations.py, backend/database.py, backend/case_processing.py, backend/models.py, Alembic, focused statute tests

Risk boundary: Do not rerun corpus extraction, populate an authority bank, acquire external sources, alter case citations, or change raw reference text/offsets. New fields must be nullable and additive; existing API behavior must remain compatible.

Smallest falsifiable check: Unit-test structured parsing for IRPA/IRPR forms including `34(1)(f)`, then compile and run the focused statute/citation tests.

Acceptance criteria:

- IRPA/IRPR references expose instrument identity and structured provision components without losing raw pinpoint text.
- Nested provisions, ranges, and lists have deterministic structured output or an explicit unresolved state.
- Migration is additive and inspected before any optional backfill.
- Existing focused statute/citation tests pass.
- No database backfill or authority-source acquisition runs in this task.

Docs/generated references: SYSTEM_REFERENCE.md; ROADMAP.md; .swm/4.9nn3id9f.sw.md; docs/TESTING_MATRIX.md

Rollback/recovery: Revert the additive migration and parser changes. Do not delete or rewrite existing statute rows; no data writer is authorized in this task.

Evidence: Explore completed the read-only contract inventory. Added structured provision parsing and persistence fields, migration `0025_structured_statute_prov`, and focused fixtures. `py_compile` passed; statute-focused tests passed `25 passed, 119 deselected, 1 warning`. Migration initially exposed the repository's 32-character Alembic version limit; the revision was shortened and migration then applied successfully from `0024_citation_target_paragraph` to `0025_structured_statute_prov`.

## Hypothesis

If structured provision identity is derived from the existing normalized IRPA/IRPR reference without changing its raw text or offsets, then fixture tests will show reliable queries for sections and nested provisions while existing extraction contracts remain green.

## Plan

1. Delegate a bounded read-only inventory of the StatuteReference model, parser return shape, persistence path, and migration numbering.
2. Implement the smallest additive structured fields/parser contract.
3. Run focused tests and inspect the migration without applying a corpus backfill.
4. Update canonical and Swimm documentation.

## Execution Checkpoints

- Delegation: Explore completed the bounded schema/parser inventory; no files changed.
- Implementation: Updated `backend/statutes.py`, `backend/database.py`, `backend/citations.py`, `tests/test_citations.py`, and added the additive migration.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `.swm/4.9nn3id9f.sw.md`.
- Recovery: No database writer or external source operation authorized.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-15 | Task created | User approved continuation from the legal authority review | Task 097 recommended this as the smallest next implementation slice |

## Completion

Completion recorded: yes

Summary: Added structured IRPA/IRPR provision identity while preserving raw pinpoint text and offsets. The live schema now supports section, subsection, paragraph, nesting depth, and range/list status.

Validation: `py_compile` passed; `tests/test_citations.py -q -k "statute or IRPA or IRPR"` -> `25 passed, 119 deselected, 1 warning`; Alembic current is `0025_structured_statute_prov (head)`.

Residual risk: Structured fields alone do not establish authoritative section text; the authority-bank source contract remains a later gated phase.

Next recommended task: Add a read-only IRPA/IRPR provision resolution report and verify structured fields against a bounded case sample; do not backfill or acquire authority sources until the report is reviewed.
