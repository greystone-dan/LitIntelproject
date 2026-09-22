# Task: Remove Judge Outcomes Surface

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Remove the Judge Outcomes Data Explorer tab and dedicated routes while retaining Judge Profile as the active judge workflow.

Why now: The product should present one canonical judge experience after the judge-identification audit; the separate outcomes surface duplicates and can imply a less trustworthy population.

Owner surface: Data Explorer UI and its route wiring.

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/pages/data_explorer.py`, `backend/routes.py`, feature-tab tests, canonical product documentation, and the relevant Swimm walkthrough.

Risk boundary: Do not alter Judge Profile endpoints, profile linking, stored data, analytics query behavior, or compatibility redirects other than removing the dedicated Judge Outcomes routes.

Smallest falsifiable check: Render `/data-explorer` and verify Judge Profile remains while the Judge Outcomes tab and panel are absent; run `pytest tests/test_feature_tabs.py -q`.

Acceptance criteria:

- Judge Outcomes is absent from the active Data Explorer tab list and client initialization.
- `/judge-outcomes` and `/analytics/judge-outcomes` are no longer active routes.
- Judge Profile and `/judges` compatibility redirect remain functional.
- Focused tests, compilation, and documentation checks pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.swm/8.upryk5h6.sw.md`, `.swm/blank.dudtv9pz.sw.md`; generated API reference must be regenerated if route generation is available.

Rollback/recovery: Restore the removed tab/panel/route wiring from this task's diff; no database or bulk operation is involved.

Evidence: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 15 tests; route imports and handlers were removed; `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.swm/blank.dudtv9pz.sw.md`, and `.swm/1.oi7rhqp2.sw.md` were updated. No database writes were run.

## Hypothesis

If only the independent Judge Outcomes tab, panel, loader, and dedicated routes are removed, the focused feature-tab test will show Judge Profile and all other active tabs remain available.

## Plan

1. Remove the active tab/panel/loader/route wiring without touching profile code.
2. Update focused tests and canonical product documentation.
3. Run focused tests, Python compilation, route/shell checks, and `git diff --check`.

## Execution Checkpoints

- Delegation: Explore agent traced the independent tab, panel, loader, and routes; no files changed.
- Implementation: `backend/pages/data_explorer.py`, `backend/routes.py`, and `tests/test_feature_tabs.py`; focused shell test passed.
- Documentation: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.swm/blank.dudtv9pz.sw.md`, and `.swm/1.oi7rhqp2.sw.md` updated.
- Recovery: No data or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-22 | Task created | Consolidate judge research on Judge Profile after audit | `backend/pages/data_explorer.py`, `backend/routes.py`, `tests/test_feature_tabs.py` |

## Completion

Completion recorded: yes

Summary: Judge Outcomes was removed from the active Data Explorer surface and dedicated routes; Judge Profile remains active.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed: 15 passed, 1 warning.

Residual risk: Orphaned analytics/page modules may remain until a separate dead-code cleanup is approved.

Next recommended task: Run a bounded dry-run audit/backfill for invalid or missing judge profile links.
