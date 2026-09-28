# Task: FC Activity intelligence stages 1-4

Status: complete
Created: 2026-09-27
Updated: 2026-09-27

## Task Record

Task: Complete the first four deterministic FC Activity intelligence stages: milestone rollups, challenged-decision taxonomy, hearing semantics, and seeded evaluation analytics.

Why now: The prior bounded evaluation established the Activity-only classifier boundary, but its stabilized fields are not yet consistently structured for review and queryable reporting.

Owner surface: `scripts/classify_fc_activity.py`, `scripts/evaluate_fc_activity_deterministic.py`, and focused Activity tests

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FC Activity source tables, `classification_json`, deterministic evaluation report, and optional local text-generation provider.

Risk boundary: Do not alter raw Activity records, canonical judgments/citations/statutes/embeddings, routes, database schema, collector checkpoints, or the old Claude smoke artifact. Do not infer closure from age or invent procedural dates. No unbounded writes or network/paid operation.

Smallest falsifiable check: Focused classifier/evaluator tests prove explicit milestone, hearing, challenged-decision, gold-set, and analytics outputs while all derived rows retain source evidence.

Acceptance criteria:

- Stage-aware milestone rollups expose structured, evidence-linked application, leave, motion, hearing, final-decision, and closure signals.
- Challenged decisions expose decision-maker, underlying tribunal, and subject taxonomy with conservative unknowns.
- Hearing semantics distinguish scheduled, held, reserved, and not-held wording in English and French, including negation.
- Seeded evaluation reports gold-set metrics and structured analytics without database writes.
- Local LLM review is attempted only as a bounded offline/local, abstaining, non-writing experiment; unavailable providers are recorded as a blocker.
- Canonical documentation and the FC Activity Swimm walkthrough describe the stabilized boundary.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.swm/fc-ingest-source-pipeline.sw.md`; no schema migration or generated reference change.

Rollback/recovery: Revert only this task's classifier/evaluator/tests/docs/task changes. Delete bounded evaluation artifacts if needed. Do not touch collector state or raw Activity tables.

Evidence: Deterministic classifier/evaluator/local-review tests and compilation
passed. Ollama metadata showed installed model `qwen3:4b`; the local provider
default was corrected from the unavailable `qwen2.5:7b`, and a synthetic
one-record probe returned valid source-linked JSON. No database or production
fact was written. No delegation was used because no delegated worker tool was
available in this session. A real five-record smoke classification completed
read-only, and the seeded 100-record report completed read-only after fixing an
O(N²) sampling bottleneck. The report found 84 closed/16 active, 32% final-
decision judge-stage coverage, 88% unknown decision subjects, and 2% valid
removal-delay coverage. A real captured Activity entry also produced valid
local-review JSON with exact source evidence and no write.

## Hypothesis

If the stabilized Activity observations are emitted as explicit stage, taxonomy, hearing-status, and seeded metric fields, then focused fixtures and a bounded report can distinguish known signals from unknowns without changing source or canonical data.

## Plan

1. Add additive classifier rollups, challenged-decision fields, and hearing-status semantics.
2. Add seeded gold-set comparison and structured analytics to the read-only evaluator.
3. Run focused tests after each implementation slice, then regenerate the bounded report and validate compilation/diff hygiene.
4. Probe the configured local provider only with a bounded redacted review prompt; record evidence or the exact availability blocker.
5. Update canonical documentation and the Activity Swimm walkthrough.

## Execution Checkpoints

- Delegation: Not used; no delegated worker tool is available in this session, so the manager retained the bounded owner surface and validation.
- Implementation: Complete for additive milestone rollups, challenged-decision taxonomy, hearing semantics, lifecycle/judge evidence, evaluator analytics, and bounded local-review validation.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`, and `.swm/fc-ingest-source-pipeline.sw.md`.
- Recovery: No long-running operation; only bounded read-only report generation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-27 | Keep stages 1-4 inside nested classification JSON and report analytics | Existing schema already stores derived JSON and semantics are not stable enough for migration/API exposure | `alembic/versions/0015_fc_activity_classifications.py`; user request |
| 2026-09-27 | Treat local LLM output as review-only and abstaining | Deterministic fields remain the production evidence layer | User request; local provider abstraction |

## Completion

Completion recorded: 2026-09-27

Summary: First four deterministic intelligence stages and the bounded local
review experiment are implemented and validated. Local output remains
review-only, source-linked, abstaining-capable, and non-writing.

Validation: `pytest tests/test_classify_fc_activity.py tests/test_evaluate_fc_activity_deterministic.py tests/test_review_fc_activity_local.py -q` -> 35 passed; `py_compile` passed; `git diff --check` passed earlier in the checkpoint.

Residual risk: Judge assignment and taxonomy remain deterministic candidates
requiring source review; 88% of the bounded sample has unknown decision subject
and removal-delay coverage is only 2%. No bulk reclassification, schema
migration, API exposure, or LLM promotion was performed.

Next recommended task: Build a bounded gold set from reviewed Activity rows,
prioritize subject extraction and removal-date coverage, and measure
field-level precision/recall before any bulk reclassification.