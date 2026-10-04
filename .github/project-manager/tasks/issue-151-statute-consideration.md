# Task: Add statute consideration analytics

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add descriptive decision-level statistics and a research page for cases that reference an act section.

Why now: Issue #151 adds a traceable way to assess how an identified statutory provision appears in reported decisions without presenting the counts as legal advice.

Owner surface: Statute consideration analytics and its dedicated API/UI entry points.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing statute canonicalization/versioning, statute reference rows, case outcomes, reader routes, and statute viewer.

Risk boundary: Read-only descriptive analytics only; no schema/database/deployment changes, no external calls, preserve statute/case-reference separation, and keep route registration minimal.

Smallest falsifiable check: `python -m pytest -q tests/test_statute_consideration.py`

Acceptance criteria:

- The API reports distinct decisions referencing a provision, court/year counts, outcome counts with unclassified and denominator, and a paginated relevance-ranked list capped at 50 per page.
- Unknown sections return a clear 404 with a useful hint; the dedicated page accepts act and section and links results to the reader.
- The statute viewer links to consideration; fixture tests and concise feature documentation cover the behavior.
- Focused tests, generated-document check, and the CI-configured full test suite pass; generated API references are regenerated where needed.

Harness criteria: API analytics and pagination fixtures pass; UI/form/link fixtures pass; generated docs are current; CI-configured full suite passes.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/6.maiixtsw.sw.md` (active UI); generated API/schema/script references via documented generators.

Rollback/recovery: Revert the isolated new service/page and minimal route/viewer registrations; no persisted data or schema changes require recovery.

Evidence: Managed-worker implemented the feature, fixtures, and docs; manager review corrected the endpoint path to `/api/statutes/{act}/{section}/consideration`. The focused command `PYTHON_DOTENV_DISABLED=1 DATABASE_URL=sqlite:///:memory: /tmp/caselibrary-validation-venv/bin/python -m pytest -q --noconftest tests/test_statute_consideration.py` passed (5 tests) without loading repository conftest or connecting to a database. In the same isolated environment, the API, schema, and script-catalog generators ran; `PYTHON_DOTENV_DISABLED=1 DATABASE_URL=sqlite:///:memory: /tmp/caselibrary-validation-venv/bin/python scripts/check_generated_docs.py` passed (3 references). Python compilation, endpoint/UI path and page-cap source assertions, and `git diff --check` passed. CI-configured full pytest was not run: `tests/conftest.py` probes the configured database at collection, outside the issue's no-database boundary. Canonical docs updated at `SYSTEM_REFERENCE.md`; Swimm walkthrough updated at `.swm/6.maiixtsw.sw.md`. `origin/main` was refreshed and verified as an ancestor of feature HEAD (`2c89913`).

Files changed: `backend/statute_consideration.py`; `backend/routes.py`; `backend/pages/statute_viewer.py`; `tests/test_statute_consideration.py`; `SYSTEM_REFERENCE.md`; `.swm/6.maiixtsw.sw.md`; generated `docs/API_REFERENCE.generated.md` and `docs/SCHEMA_REFERENCE.generated.md`; this task record.
Delegated work: Managed-worker inspected its assigned code/docs, implemented the service/router, viewer link, fixtures, and documentation, and returned a structured report. Bounded manager recovery fixed the specified API route mismatch after review; delegated agent handle was unavailable for follow-up.
Focused validation: `PYTHON_DOTENV_DISABLED=1 DATABASE_URL=sqlite:///:memory: /tmp/caselibrary-validation-venv/bin/python -m pytest -q --noconftest tests/test_statute_consideration.py` passed (5 tests). Python compilation, endpoint/UI path and page-cap assertions, and `git diff --check` passed. API/schema/script-catalog generators ran; the generated-doc check passed.
Residual risk: The CI-configured full suite was not run because its `tests/conftest.py` performs a database availability probe, disallowed by this task's boundary. Database population completeness was not assessed. No application database was accessed.
Next bounded task: Obtain an approved no-database strategy for the CI-configured full suite, then run it with the specified CI deselections.

## Hypothesis

If decision-level aggregation is correctly derived from stored statute references and canonical cases, fixture/API tests will show correct distinct decision, court/year, outcome-denominator, stable ranking, pagination, and unknown-section behavior without schema changes.

## Plan

1. Assign bounded implementation and focused fixture checks to a managed worker.
2. Review the returned change against the API/UI and descriptive-statistics requirements.
3. Regenerate generated references, run focused and CI-configured full tests, and update canonical and Swimm documentation.

## Execution Checkpoints

- Delegation: Managed-worker returned a structured implementation report; endpoint path mismatch required bounded manager recovery.
- Implementation: Worker implementation reviewed; manager corrected API path.
- Documentation: `SYSTEM_REFERENCE.md`; `.swm/6.maiixtsw.sw.md`.
- Recovery: No database or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Scope to read-only statute-reference analytics with no schema change | Issue requires descriptive statistics and existing statute storage | User request; `SYSTEM_REFERENCE.md`; `DOCS_INDEX.md` |

## Completion

Completion recorded: no

Summary: Implementation, focused fixtures, and documentation are present; task remains blocked because the requested full-suite run would probe a database, outside the explicit boundary.

Validation: Isolated focused pytest passed (5 tests); compilation/source assertions and `git diff --check` passed; all three generators ran and generated-doc check passed. Full pytest was not run because the repository conftest probes the database.

Residual risk: Full-suite compatibility remains unverified; no live or test database was accessed.

Next recommended task: Agree on a safe no-database method for the CI-configured full suite.
