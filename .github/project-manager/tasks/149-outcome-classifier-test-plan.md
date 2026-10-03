# Task: Outcome classifier test plan

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Add synthetic outcome-classifier fixtures/tests and a report for issue #45 without changing classifier behavior.

Why now: The deterministic outcome classifier has known wording edge categories that need documented test coverage and an explicit testability plan before any future behavior work.

Owner surface: `backend/metadata_outcomes.py` test coverage, `tests/test_metadata.py`, `docs/reports/outcome-classifier-test-plan.md`, `CHANGELOG.md`, and `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`

Commit allowed: yes

Push allowed: yes

Dependencies: Existing deterministic outcome classifier, current metadata/case-processing tests, managed-worker inventory, Swimm evaluation walkthrough

Risk boundary: No classifier behavior changes, no production data writes, no schema changes, no broad test expansion outside the outcome slice

Smallest falsifiable check: `python3 -m pytest tests/test_metadata.py -q`

Acceptance criteria:

- Synthetic tests cover the decidable outcome rules already in code and xfail unsupported expected cases with reasons.
- The report documents wording, expected/current behavior, risk, and Minister win-rate impact notes.
- Focused validation passes without classifier behavior changes.

Docs/generated references: `CHANGELOG.md`, `docs/reports/outcome-classifier-test-plan.md`, `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`

Rollback/recovery: Remove the new fixture tests and report; no data migration or runtime rollback needed

Evidence: Managed-worker inventory completed; added synthetic outcome fixtures/tests in `tests/test_metadata.py`; wrote `docs/reports/outcome-classifier-test-plan.md`; updated canonical doc `CHANGELOG.md`; updated Swimm walkthrough `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`; focused validation `python3 -m pytest tests/test_metadata.py -q` passed with `35 passed, 3 xfailed`; `git diff --check` passed; secret scan over changed files found only preexisting generic password/secret/token wording in history text, no secrets added.

Files changed: `.github/project-manager/tasks/149-outcome-classifier-test-plan.md`, `tests/test_metadata.py`, `docs/reports/outcome-classifier-test-plan.md`, `CHANGELOG.md`, `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`
Delegated work: managed-worker inventory of existing deterministic_outcome_v2 wording coverage and gaps
Focused validation: `python3 -m pytest tests/test_metadata.py -q` -> `35 passed, 3 xfailed`
Residual risk: Unsupported wording categories remain xfailed/documented rather than behavior-changed
Next bounded task: None

## Hypothesis

If the current classifier behavior is correctly understood, focused synthetic tests will pass for supported wording and xfail the unsupported edge cases with documented reasons.

## Plan

1. Add bounded synthetic outcome fixtures for supported/unsupported wording categories.
2. Write `docs/reports/outcome-classifier-test-plan.md` with wording, expected/current, and risk columns.
3. Run the focused metadata test slice and refresh canonical docs and Swimm.

## Execution Checkpoints

- Delegation: managed-worker inventory for deterministic_outcome_v2 rules and missing testability cases
- Implementation: `tests/test_metadata.py` and `docs/reports/outcome-classifier-test-plan.md`
- Documentation: `CHANGELOG.md` and `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`
- Recovery: none

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created | Need bounded test/report coverage for issue #45 without behavior changes | Managed-worker inventory request |

## Completion

Completion recorded: yes

Summary: Added issue #45 synthetic outcome-classifier fixtures, xfailed unsupported wording cases, and the outcome test-plan report without changing classifier behavior.

Validation: `python3 -m pytest tests/test_metadata.py -q` -> `35 passed, 3 xfailed`; `git diff --check` passed

Residual risk: Unsupported wording categories remain explicitly documented and xfailed until a future behavior change is approved

Next recommended task: Use the report as the reference if outcome behavior work is proposed later
