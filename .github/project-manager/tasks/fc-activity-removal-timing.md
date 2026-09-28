# Task: FC Activity removal timing

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Preserve explicit scheduled-removal dates and destinations on deterministic Activity stay events for procedural delay statistics.

Why now: The evaluation corpus contains repeated stay-motion entries with removal dates and destinations, but derived events currently retain only the source document date.

Owner surface: `scripts/classify_fc_activity.py` and focused Activity tests

Commit allowed: yes

Push allowed: yes

Dependencies: Existing Activity source text, `_DATE_TOKEN` normalization, stay event extraction.

Risk boundary: Derived fields only; no raw/canonical/database/API changes, no collector changes, no network or paid operation.

Smallest falsifiable check: A stay-motion fixture containing `removal order scheduled for 26-FEB-2007` emits `removal_scheduled_date == 2007-02-26` while preserving source document date semantics.

Acceptance criteria:

- Extract explicit scheduled-removal dates from stay/removal wording.
- Preserve an explicit removal destination when present without inventing one.
- Add focused tests and keep the full Activity suite green.
- Document the field and its source-only semantics in the required Activity docs.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`.

Rollback/recovery: Revert only the classifier/test/documentation changes from this task; do not touch collector checkpoints or source rows.

Evidence: The delegated Activity review identified repeated scheduled-removal date/destination patterns as a concrete extension point. Corpus search found examples in the deterministic report, including removal dates scheduled for 26-FEB-2007 and 03-DEC-2019 with destination Nigeria. The classifier now preserves normalized `removal_scheduled_date` and bounded `removal_destination` on stay events, while generalizing explicit `filed on` semantics to all procedural events. No French cancellation rule was added because available matches were administrative/file cancellation or decision-annulment language, not a repeatable removal-cancellation outcome. Focused timing validation passed with 2 tests; the full Activity-focused suite passed with 23 tests. The deterministic report was regenerated read-only with 100 records, seven-year weighting, 24 stay events, and `database_written: false`. Documentation was updated in `SYSTEM_REFERENCE.md`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, and `.swm/fc-ingest-source-pipeline.sw.md`.

## Hypothesis

If explicit scheduled-removal metadata is preserved on stay events, then filing-to-removal and motion-to-removal delay statistics can be computed later without treating `DOC_DT` as the removal date.

## Completion

Completion recorded: 2026-09-25

Summary: Complete for explicit scheduled-removal metadata and filing-date semantics.

Validation: `python -m pytest tests/test_classify_fc_activity.py -k "stay or removal_schedule" -q` passed with 2 tests; the full Activity-focused suite passed with 23 tests; the report command completed without database writes.

Residual risk: Registry wording and destination phrasing vary; this slice captures only explicit scheduled dates and bounded destination text.

Next recommended task: Add report-level counts for scheduled-removal metadata and compute bounded filing-to-removal and motion-to-removal delay distributions with explicit missing/ambiguous states.
