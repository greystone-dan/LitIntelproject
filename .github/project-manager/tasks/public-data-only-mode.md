# Task: Add opt-in public-data-only mode

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add an opt-in `CASELIBRARY_PUBLIC_DATA_ONLY` deployment profile that blocks document/free-text analysis inputs, explains disabled UI functions, and exposes its status.

Why now: Deployment operators need a clear, independently observable mode that preserves public-data browsing and search while rejecting private document/analysis inputs.

Owner surface: FastAPI public-data-only deployment profile and its route/UI policy.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FastAPI routes, page builders, focused route/UI tests, generated API reference, and API/route-flow Swimm walkthrough.

Risk boundary: Do not access the database, deploy/restart, read or modify `.env`, add dependencies, change the password gate, block non-analysis browse/search/read/statute paths, or remove existing features. No database or deployment scripts.

Smallest falsifiable check: `python -m pytest -q tests/test_public_data_only_mode.py`

Acceptance criteria:

- `CASELIBRARY_PUBLIC_DATA_ONLY` defaults off; when on, every classified document/free-text analysis input path is rejected while public read/search/statute workflows continue.
- The mode is reported by `/health` and `GET /api/deployment-profile`; affected UI entry points explain the restriction.
- A regression test detects new POST routes accepting upload/file/free-text inputs unless they are explicitly classified.
- Focused on/off/read-path tests pass, generated API documentation is checked/regenerated when appropriate, and documentation and walkthrough updates are recorded.

Harness criteria: Not using a managed run harness; validate each acceptance item with focused tests and generated-doc check.

Docs/generated references: `docs/PUBLIC_DATA_ONLY_MODE.md`, `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, and generated API reference if route API changes.

Rollback/recovery: Revert the additive profile module, route guards, response/UI changes, tests, and docs together; no data or schema changes.

Evidence: Manager delegated an initial implementation/inventory slice; the worker returned structured evidence, and manager repaired the incomplete route classification, focused tests, and missing UI surfaces. `python -m py_compile backend/deployment_profile.py backend/main.py backend/routes.py backend/pages/live_analysis.py tests/test_deployment_profile.py` passed. An isolated local harness executed all 8 focused test functions using minimal FastAPI/pytest API stubs (no application/database/.env import); all passed. The local documentation-path review and `git diff --check` passed. `python -m pytest -q tests/test_deployment_profile.py` could not run because pytest is not installed. `python scripts/check_generated_docs.py` could not complete because FastAPI and SQLAlchemy are not installed; API/schema generators therefore failed before importing application/database modules. Do not hand-edit generated API references.

Files changed: `.swm/1.oi7rhqp2.sw.md`; `CHANGELOG.md`; `SYSTEM_REFERENCE.md`; `backend/deployment_profile.py`; `backend/main.py`; `backend/routes.py`; `docs/CONFIGURATION_REFERENCE.md`; `docs/PUBLIC_DATA_ONLY_MODE.md`; `tests/test_deployment_profile.py`; this task record.
Delegated work: Managed-worker `public-data-mode-worker` inventoried route inputs and prepared the initial code/tests/docs; structured handoff identified unavailable runtime dependencies. Manager independently corrected scope/test/UI coverage and performed final checks.
Focused validation: `python -m py_compile backend/deployment_profile.py backend/main.py backend/routes.py backend/pages/live_analysis.py tests/test_deployment_profile.py` (passed); isolated focused harness (8 checks passed); `git diff --check` (passed); local documentation-path review (passed). Standard pytest and generated-doc checks are blocked by missing packages.
Residual risk: No FastAPI TestClient/browser run; API generator did not refresh `docs/API_REFERENCE.generated.md` because FastAPI/SQLAlchemy are unavailable. The API reference is stale for the new `GET /api/deployment-profile` endpoint until generated in a dependency-complete, no-`.env`-access environment.
Next bounded task: In a dependency-complete isolated CI/test environment with no readable `.env` files, run `python -m pytest -q tests/test_deployment_profile.py`, regenerate/check API/schema references with the existing generators, and add a browser smoke check for the four affected analysis pages.

## Hypothesis

If the mode is correctly centralized and enforced at the HTTP boundary, the focused tests will show that analysis/document inputs fail only when enabled, while health/profile status and ordinary public read/search/statute paths remain available.

## Plan

1. Inventory request routes, UI entry points, and existing focused tests; classify only document/free-text analysis paths.
2. Implement centralized profile/path classification, guards, status surfaces, UI messaging, and explicit classification coverage.
3. Run focused tests, regenerate/check generated route docs, update canonical documentation and Swimm walkthrough, reconcile `main`, and perform final safety checks.

## Execution Checkpoints

- Delegation: Pending.
- Implementation: Pending.
- Documentation: Pending.
- Recovery: No database, migration, or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #112 constraints supplied by requester; worktree is on feature branch with a prior main merge commit | Git status/branch inspected; GitHub issue lookup unavailable because `GH_TOKEN` is not configured |

## Completion

Completion recorded: no

Summary: Implementation, focused source tests, documentation, and route/UI policy are present. The task remains blocked from completion because standard pytest and generated-reference validation cannot run in this environment.

Validation: Python compilation and 8 isolated focused test functions passed; standard pytest and generated-doc checks failed at dependency import due missing pytest, FastAPI, and SQLAlchemy.

Residual risk: Generated API/schema references and browser/runtime behavior remain unverified.

Next recommended task: Run focused tests and generated-reference validation in an isolated environment with required project dependencies and no `.env` access.
