# Task: FC Activity stay outcomes

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Improve deterministic Federal Court Activity stay-of-removal statistics using explicit removal-cancellation signals.

Why now: The bounded dataset contains removal-cancellation wording, but the prior report captured stay references without resolving these signals as granted stays.

Owner surface: `scripts/classify_fc_activity.py` and focused Activity tests/report

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `fc_activity_documents` source text, deterministic Activity classifier, focused tests, bounded evaluation report.

Risk boundary: Read-only derived observations only. Do not modify the collector, raw Activity rows, canonical cases, citations, statutes, judgment text, embeddings, database schema, or API/UI. No network or paid operation.

Smallest falsifiable check: A fixture containing `removal has been cancelled` produces a `stay` event with `outcome == granted` and aggregate `stay_decision.status == yes`, while the focused Activity suite remains green.

Acceptance criteria:

- Explicit removal-cancellation wording is recognized as an implicit granted stay.
- Source evidence and rule names remain attached to derived events.
- Existing Activity tests and evaluation tests remain green.
- The deterministic report is regenerated if the bounded evaluator completes.
- Canonical documentation and the relevant Swimm walkthrough record the rule and its uncertainty.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; deterministic evaluation JSON if regeneration completes.

Rollback/recovery: Revert only the classifier/test/documentation changes from this task. Do not touch collector checkpoints or raw Activity tables.

Evidence: Delegated read-only review identified removal-cancellation signals as the highest-value next improvement and reported zero prior granted-stay outcomes despite matching dataset text. The classifier now recognizes explicit English removal-cancellation wording as an implicit granted stay under `stay_cancellation` in both procedural events and aggregate `stay_decision` evidence. Focused validation passed with `1 passed, 17 deselected`; the full Activity-focused suite passed with `22 passed`. The deterministic report was regenerated read-only at `data/eval/fc_activity_deterministic_evaluation_20260925.json` for 100 records with seven-year weighting: `stay` events increased to 24, with `database_written: false`. Documentation was updated in `SYSTEM_REFERENCE.md`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, and `.swm/fc-ingest-source-pipeline.sw.md`.

## Hypothesis

If explicit removal-cancellation wording is treated as an evidence-backed implicit granted stay, then stay grant statistics will better reflect procedural outcomes without interpreting source `DOC_DT` or writing canonical data.

## Completion

Completion recorded: 2026-09-25

Summary: Complete for the bounded implicit granted-stay rule and refreshed evaluation artifact.

Validation: `python -m pytest tests/test_classify_fc_activity.py -k stay -q` passed; the full Activity-focused suite passed with 22 tests; the deterministic report command completed with no database writes.

Residual risk: Cancellation can reflect an administrative change rather than a judicial stay in some registry contexts; the derived rule remains an explicit signal and should be audited against broader bilingual/ambiguous wording before production statistics are exposed.

Next recommended task: Add source-backed bilingual cancellation fixtures and distinguish administrative cancellation from judicial stay orders before exposing granted-stay statistics through the API/UI.
