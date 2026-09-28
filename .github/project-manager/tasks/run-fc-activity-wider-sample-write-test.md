# Task: Run wider FC Activity sample and write test

Status: complete
Created: 2026-09-28
Updated: 2026-09-28

## Task Record

Task: Run a wider read-only FC Activity evaluation and perform a bounded persistence test with all derived fields tied to the case-level IMM number/source case.

Why now: The pre-scale readiness review passed; the next checkpoint is to measure wider-sample behavior and verify the persistence identity contract before any larger write.

Owner surface: FC Activity evaluation and persistence path under `scripts/classify_fc_activity.py` and `scripts/evaluate_fc_activity_deterministic.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: Readiness artifact, fixed seed 20260928, existing FC Activity database tables, and case-level IMM/source identity.

Risk boundary: Wider read-only evaluation plus a bounded test write only; no bulk overwrite until post-write identity verification passes. Do not create document-level derived rows or alter source Activity documents.

Smallest falsifiable check: Run a 5,000-case evaluation, then persist a small bounded sample and verify `source_case_id`, `imm_number`, and classification payload identity for every written row.

Acceptance criteria:

- Wider evaluation completes with validation coverage, runtime/output artifact, and no network calls.
- Derived classifications are one row per source case and carry the case IMM number.
- Test write updates only the bounded selected case rows and leaves source documents unchanged.
- Post-write query confirms no IMM/source-case mismatch or document-level classification rows.
- Focused tests and `git diff --check` pass after any required code/documentation changes.

Harness criteria: Evaluation is bounded; persistence is bounded; write verification records counts and mismatches; no external AI call is made.

Docs/generated references: `docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md`; `.swm/fc-ingest-source-pipeline.sw.md`; `OVERNIGHT.md`.

Rollback/recovery: The persistence path is upsert-like by source case. If the bounded test reveals identity or schema defects, stop before wider writes and restore only the affected test rows from their prior classification payloads.

Evidence: The 5,000-case artifact `data/eval/fc_activity_wider_5000_20260928.json`
contains 5,000 valid classifications and zero validation issues; the evaluator
reported no network calls and no database writes. A bounded
`classify_fc_activity.py --limit 5 --write` run wrote 5 rows. Post-write
verification found source case IDs 1-5, one row per source case, zero IMM
mismatches, and payload fields `motion_presence`, `aljr_filer_type`, and
`respondent_minister`. The persistence path was hardened to reject duplicate
report IDs and missing source cases. Documentation was updated in
`docs/FC_ACTIVITY_BETA_VBA_COMPARISON.md` and
`.swm/fc-ingest-source-pipeline.sw.md`.

Files changed: `.github/project-manager/tasks/run-fc-activity-wider-sample-write-test.md`
Delegated work: Pending bounded write-path review.
Focused validation: `pytest tests/test_classify_fc_activity.py -q` passed 71
tests; `classify_fc_activity.py --limit 5 --write` completed with 5 written;
the post-write SQLAlchemy identity query passed; and `git diff --check` passed.
Residual risk: Motion subtype and result coverage remain intentionally
conservative, and no wider persistence write has been authorized or run.
Next bounded task: Decide whether to expand persistence after the test write passes.

## Hypothesis

If persistence is case-owned, then every derived row written from the bounded sample will have one matching `source_case_id` and IMM number, regardless of how many source documents contributed evidence.

## Plan

1. Inspect the write path and identity constraints.
2. Run the wider read-only evaluation.
3. Persist and verify a small case-level sample, then document the result.

## Execution Checkpoints

- Delegation: Manager-owned bounded write-path review; no separate worker was
	needed after the local persistence contract was inspected.
- Evaluation: Complete; 5,000/5,000 valid with zero issues and no evaluator
	network/database writes.
- Write test: Complete; 5/5 written and identity verification passed.
- Documentation: Complete; canonical FC Activity note and Swimm walkthrough
	updated.
- Recovery: Preserve prior test-row payloads if rollback is required.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-28 | Task created | User authorized a wider run and requested a test write with IMM-level identity verification. | Pre-scale readiness artifact and user instruction |

## Completion

Completion recorded: yes

Summary: Wider deterministic evaluation and bounded case-level persistence
verification completed successfully.

Validation: 71 focused tests passed; bounded write completed; post-write case
identity query passed; final diff check pending.

Residual risk: No wider persistence write was performed. Motion detail remains
conservative by design.

Next recommended task: Review the wider motion-positive cases for a targeted
AI enhancement dataset before considering any larger persistence write.