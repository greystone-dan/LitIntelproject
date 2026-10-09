# Task: Produce scoped dead-code audit report

Status: in progress
Created: 2026-10-09
Updated: 2026-10-09

## Task Record

Task: Add a report-only dead-code audit for the issue #430 scope using current checked-out source evidence.

Why now: Identify safe removal candidates and duplication without changing working code or touching tour/Coming soon code.

Owner surface: `docs/reports/DEAD_CODE_AUDIT.md`

Commit allowed: yes

Push allowed: yes

Dependencies: Current source in `backend/`, `scripts/`, `legacy/`, and `side_projects/`; generated script catalog is status evidence only.

Risk boundary: No code deletion or modification; do not access databases, live site, or `.env`; exclude tour and Coming soon code; classify as unused only with path-specific search evidence and conservative dynamic-reference review.

Smallest falsifiable check: Verify each proposed unused item has no in-scope or repository-wide textual reference and document remaining dynamic-reference uncertainty.

Acceptance criteria:

- Report covers backend (including pages and legal_tagger/case_compare pairs), `scripts/`, top-level `test_statute_integration.py`, `legacy/`, and `side_projects/`.
- Every item has path evidence, grep/search evidence where called unused, a remove/check/keep rating, and duplicates/superseded script notes including generated-catalog documentation status.
- No working code is changed; tour and Coming soon code are not assessed.
- Documentation paths and `git diff --check` are recorded; no tests, linters, or builds are run.

Harness criteria: Not used; no task-run harness started.

Docs/generated references: Canonical report `docs/reports/DEAD_CODE_AUDIT.md`; Swimm `Technical Debt Register and Improvement Queue` walkthrough. Do not edit generated `docs/SCRIPT_CATALOG.generated.md`.

Rollback/recovery: Remove the report and this task record; any Swimm link can be reverted independently. No code or data changes.

Evidence: Pending. Record delegated inventory, evidence commands, review limits, the canonical report and Swimm walkthrough paths, and final documentation checks.

Files changed: Pending.
Delegated work: Pending bounded read-only inventory.
Focused validation: Pending report-evidence review and `git diff --check`.
Residual risk: Static reference search cannot prove absence of runtime imports, plugin/entry-point loading, or external callers.
Next bounded task: None until audit findings are reviewed.

## Hypothesis

If the audit's remove candidates are safe to consider, scoped repository-wide searches and dynamic-loading checks will show no relevant references while retaining explicit uncertainty for reflective or external references.

## Plan

1. Delegate bounded source inventory and reference searches for the requested scope.
2. Synthesize conservative findings, duplication suggestions, ratings, and script-catalog status into the report.
3. Update the relevant Swimm walkthrough, validate the report evidence and documentation diff, and record actual results.

## Execution Checkpoints

- Delegation: Pending managed-worker read-only inventory.
- Implementation: Pending report-only audit synthesis.
- Documentation: Pending canonical report and Swimm walkthrough checkpoint.
- Recovery: No long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-09 | Task created | Issue #430 requests a broad, evidence-backed report with no code changes | `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, and `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md` inspected |

## Completion

Completion recorded: no

Summary: Pending.

Validation: Pending.

Residual risk: Pending.

Next recommended task: Pending.
