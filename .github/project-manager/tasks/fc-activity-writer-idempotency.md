# Task: FC Activity writer idempotency

Status: complete
Created: 2026-09-26
Updated: 2026-09-26

## Task Record

Task: Repair the FC Activity-only writer after a duplicate document identity stopped collection.

Why now: The collector failed at IMM-23145-25 with a PostgreSQL unique violation on `(case_id, re_no, docno) = (283392, 10, 7)`.

Owner surface: `scripts/fetch_fc_procedural_history.py` Activity writer

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `fc_activity_documents` identity constraints and Activity-only resume command.

Risk boundary: Activity tables only. No canonical cases, citations, statutes, embeddings, collector input deletion, or destructive database operation.

Smallest falsifiable check: Duplicate complete registry identities in one response or already persisted rows are skipped without an insert, while entries missing either registry key retain entry-hash deduplication.

Acceptance criteria:

- Prevent the observed duplicate `(case_id, re_no, docno)` failure.
- Preserve Activity-only writes and existing hash fallback.
- Add focused regression coverage.
- Document the rerun behavior and residual risk.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`; `.github/project-manager/tasks/fc-activity-writer-idempotency.md`.

Rollback/recovery: Stop the collector, preserve the current Activity rows, and revert only the writer/test/documentation change if needed. Resume from the existing IMM input; do not delete rows or reset checkpoints.

Evidence: The traceback showed the writer checked only `entry_hash` while the database enforced `(case_id, re_no, docno)`. The writer now deduplicates complete identities within each response and against persisted rows, retaining hash fallback for incomplete identities. Focused validation passed with 2 tests. Broader validation and compile checks are recorded below.

## Hypothesis

If the writer uses the database-enforced registry identity before hash fallback, then repeated endpoint entries cannot crash an Activity-only resume run with the observed unique violation.

## Completion

Completion recorded: 2026-09-26

Summary: Complete for the observed duplicate-identity failure.

Validation: `python -m pytest tests/test_fetch_fc_procedural_history_cli.py -q` passed with 2 tests; the broader collector/Activity suite passed with 32 tests; `py_compile` passed for the three touched Activity scripts; and `git diff --check` passed.

Residual risk: If the endpoint changes identity semantics or returns conflicting complete identities with meaningful revisions, the current policy preserves the first row and skips later conflicting content; such cases require an explicit merge policy.

Next recommended task: Resume from the failed IMM input with `--log-file`, confirm IMM-23145-25 is idempotent, and monitor the next adaptive checkpoints.
