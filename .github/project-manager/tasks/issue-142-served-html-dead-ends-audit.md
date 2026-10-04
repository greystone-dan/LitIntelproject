# Task: Audit served HTML routes and local navigation

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Audit every served HTML page for route-aware local links and browser API URLs, add reusable checking and regression coverage, repair confirmed dead ends and HTML error behavior, and publish findings.

Why now: An apparently successful HTML response can still contain broken page navigation or browser requests; route-aware checks make those dead ends observable and prevent regressions.

Owner surface: Served HTML route/navigation behavior across `backend/main.py`, `backend/routes.py`, `backend/pages/`, and the dedicated checker.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing FastAPI route registry, page builders, current UI guide and active UI walkthrough.

Risk boundary: Preserve every route and feature; no database access, deployment, `.env`/credential access, dependency changes, or migrations. Keep the checker offline and read-only.

Smallest falsifiable check: `python -m pytest -q tests/test_check_site_links.py tests/test_html_error_responses.py`

Acceptance criteria:

- A route-aware checker audits rendered served HTML for local `href`, `form action`, and inline `fetch`/XHR URLs, distinguishing intentional external/dynamic/API targets from broken local page targets.
- Pytest covers checker behavior and every served HTML page without database or network access.
- Confirmed dead ends are repaired without removing routes or features; HTML not-found and server-error responses have appropriate status and HTML behavior.
- `docs/reports/dead-ends-audit.md` records scope, methodology, findings, changes, and limitations.
- Relevant Swimm and canonical repository documentation are updated; full suite with CI deselects, generated-doc check, and diff checks are recorded.

Harness criteria: checker covers all HTML pages and required URL surfaces; regressions pass; all confirmed dead ends and HTML error responses are addressed; report and both required documentation layers are updated; full-suite and generated-document results are recorded.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `docs/reports/dead-ends-audit.md`, `.swm/6.maiixtsw.sw.md`; generated script catalog is refreshed if script inventory generation includes this tool.

Rollback/recovery: Revert only this task's checker, tests, bounded route/page fixes, audit report, and documentation. No persistent data or deployment state is involved.

Evidence: The initial worktree was clean. The managed worker returned the requested structured result and implemented the checker/test slice plus UI guide and walkthrough updates; its pytest run was blocked by missing pytest, and its application snapshot command was blocked by missing FastAPI. Manager review added HTTP-method matching, empty form-action and slash-redirect cases, FastAPI docs-page snapshots, guarded application imports, content-negotiated HTML 404/500 handling, and the audit report. Five checker test functions were directly invoked and passed. Final validation commands and blockers are recorded below.

Files changed: `.github/project-manager/tasks/issue-142-served-html-dead-ends-audit.md`, `.swm/6.maiixtsw.sw.md`, `CHANGELOG.md`, `SYSTEM_REFERENCE.md`, `backend/main.py`, `backend/html_errors.py`, `docs/RESEARCH_UI_GUIDE.md`, `docs/SCRIPT_CATALOG.generated.md`, `docs/reports/dead-ends-audit.md`, `scripts/check_site_links.py`, `scripts/generate_script_catalog.py`, `tests/test_check_site_links.py`, `tests/test_html_error_responses.py`.
Delegated work: `html-link-audit` (managed-worker), bounded checker/test implementation and UI documentation; structured response received. The worker reported three initial checker tests pass when directly invoked, but pytest and route rendering were blocked by missing packages. It changed only the checker, focused tests, UI guide, and active UI walkthrough; manager independently reviewed the changes and owns acceptance.
Focused validation: `python -m pytest -q tests/test_check_site_links.py tests/test_html_error_responses.py` — blocked before collection (`No module named pytest`). Direct invocation of five checker test functions — passed. `python -m py_compile backend/main.py backend/html_errors.py scripts/check_site_links.py scripts/generate_script_catalog.py tests/test_check_site_links.py tests/test_html_error_responses.py` — passed. `python scripts/check_site_links.py --help` — passed; full snapshot invocation — blocked (`No module named dotenv`). `python scripts/generate_script_catalog.py` — passed. `python scripts/check_generated_docs.py` — API/schema generators blocked (`fastapi`/`sqlalchemy` missing); script catalog is current. `python -m pytest -q` — blocked before collection (`No module named pytest`), so configured CI deselects were not reached. New local documentation links, `git diff --check`, and compilation passed.
Residual risk: No rendered route/page audit or pytest execution was possible in this environment; consequently page-link findings and HTML handler behavior remain unverified at runtime. The report explicitly makes no claim that page URLs are clean. No database, deployment, `.env`, credential, dependency, or migration action was performed.
Next bounded task: In the dependency-equipped repository environment, run `python scripts/check_site_links.py`, repair only confirmed findings, run the focused tests and `python -m pytest -q` with its configured CI deselects, then rerun `python scripts/check_generated_docs.py`.

## Hypothesis

If each rendered HTML page is tested against the registered local routes and API targets, the checker and focused tests will identify broken local destinations and invalid HTML route error behavior without changing page or data contracts.

## Plan

1. Delegate bounded inventory and implementation of the checker plus its focused tests.
2. Consume checker findings, repair only confirmed local dead ends and HTML error responses, and run the focused check.
3. Publish the audit report, update canonical and Swimm docs, then run the CI-selected full suite and generated-doc check.

## Execution Checkpoints

- Delegation: `html-link-audit` returned structured findings, changed the checker/test slice and UI docs; manager recovery added route method checks and complete application-error behavior.
- Implementation: Checker direct fixture calls passed; focused pytest was blocked before collection because pytest is unavailable. HTML error tests compile but were not executed.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`, and `docs/reports/dead-ends-audit.md`; regenerated `docs/SCRIPT_CATALOG.generated.md`. Local links and `git diff --check` passed.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #142 asks for a multi-part page audit, regression checker, fixes, and report | Clean initial worktree; `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, repository guidance, runbook, transition doc, and active UI walkthrough reviewed |
| 2026-10-04 | Marked blocked after implementation/documentation checkpoint | Required tests, full route rendering, and generated API/schema checks cannot run without dependencies; adding/installing dependencies is outside scope | Five checker tests invoked directly; py_compile, local docs links, `git diff --check`, and script catalog generation passed; pytest, checker rendering, and two generated references failed before executing due missing packages |

## Completion

Completion recorded: no

Summary: Implemented the route-aware local HTML checker, focused tests, HTML 404/500 handlers, generated script-catalog entry, audit report, and canonical/Swimm documentation. The task remains blocked pending a dependency-equipped full page audit and tests.

Validation: Five checker test functions, Python compilation, checker CLI help, generated script catalog, local documentation links, and `git diff --check` passed. Focused/full pytest, actual checker snapshots, and generated API/schema verification were blocked as detailed above and in `docs/reports/dead-ends-audit.md`.

Residual risk: No page snapshot findings or HTML exception tests were executed; do not infer that all rendered routes are free of dead ends.

Next recommended task: Rerun the checker, focused tests, full CI-selected suite, and generated-doc check in the project dependency-equipped environment, then fix only confirmed page dead ends.
