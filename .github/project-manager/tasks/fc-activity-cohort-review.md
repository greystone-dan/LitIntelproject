# Task: Build FC Activity review cohorts

Status: in-progress
Created: 2026-09-26
Updated: 2026-09-26

## Task Record

Task: Add reproducible read-only cohort filters, generate targeted FC Activity review packages, and produce coverage/code-answer artifacts.

Why now: A design reviewer needs focused evidence cohorts and verified repository facts before designing the next Activity transformation layer.

Owner surface: scripts/export_fc_activity_package.py and its focused tests

Commit allowed: yes

Push allowed: yes

Dependencies: PostgreSQL Activity tables, existing classifier and normalization code, read-only export directory

Risk boundary: No writes to PostgreSQL or fc_activity_* tables; no classifier changes; raw source fields remain byte-for-byte represented in JSON serialization; never overwrite output directories; no secrets or .env access.

Smallest falsifiable check: `python -m pytest tests/test_export_fc_activity_package.py -q` and `python -m py_compile scripts/export_fc_activity_package.py` using fixture-backed tests.

Acceptance criteria:

- Exporter supports the requested reproducible filters and manifest metadata.
- Fixture-backed tests cover every filter and deterministic sampling.
- Fifteen cohort packages, a counts-only coverage report, repository answers, and a zip are generated without database writes.
- Zip size is checked against the 30 MB threshold and any reductions are documented.
- Documentation/task evidence records actual commands, counts, and residual limitations.

Docs/generated references: docs/CLAUDE_ACTIVITY_PROJECT_SETUP.md, SYSTEM_REFERENCE.md, docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md, .swm/fc-ingest-source-pipeline.sw.md

Rollback/recovery: Delete only the newly created cohort output directory and zip; database is read-only and unchanged.

Evidence: Pending.

## Hypothesis

If candidate selection is performed from read-only source rows using explicit normalized predicates and deterministic SHA-256 ordering, repeated runs with the same arguments and seed will produce identical case IDs and linked raw rows.

## Plan

1. Inspect exporter, schema helpers, classifier, and source-key code.
2. Implement filter selection and manifest metadata without changing classifier logic.
3. Add fixture-backed tests and run focused validation.
4. Generate cohorts and counts-only reports in new output directories.
5. Write code answers with file/line references, zip, and final evidence.

## Execution Checkpoints

- Delegation: Pending bounded code-fact and filter review.
- Implementation: Pending.
- Validation: Pending.
- Artifacts: Pending.

## Completion

Completion recorded: no

Summary: Pending.

Validation: Pending.

Residual risk: Cohort counts depend on the current database snapshot; regex semantics and source limitations remain documented in manifests.

Next recommended task: Review cohort design with the external AI before implementing new production-derived tables.
