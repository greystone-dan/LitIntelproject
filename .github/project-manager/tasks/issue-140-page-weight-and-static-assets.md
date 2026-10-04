# Task: Complete issue #140 page-weight coverage and static asset caching

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Finish issue #140's explicit page-weight requirement for every HTML page builder and safely cache mounted static assets.

Why now: The existing issue record says the prior offline baseline remains at `docs/page_weight_baseline.json`, while the requested deliverable is `docs/reports/page-weight-baseline.md`; the current script omits page builders and asset/request metrics.

Owner surface: Offline page-builder weight measurement and FastAPI static-asset delivery/cache policy.

Commit allowed: yes

Push allowed: yes

Dependencies: Current builders and deterministic fixture inputs; no database/server required.

Risk boundary: No DB, server, deployment, `.env`, credentials, or data changes. Preserve dynamic API, no-store, export, streaming, and download cache/compression behavior. Any builder not safely fixture-runnable must be identified and represented as skipped with reason.

Smallest falsifiable check: `PYTHON_DOTENV_DISABLED=1 python -m pytest -q --noconftest tests/test_page_weight.py tests/test_gzip_middleware.py`

Acceptance criteria:

- The script measures every HTML page builder, using deterministic safe fixtures when arguments are required and explicit skip records where invocation is unsafe or unsupported.
- Report records raw and gzip sizes, inline script/style bytes, and external request count for each measured HTML output.
- Fixture-runnable tests prove builder coverage and metric/report behavior without DB or server access.
- Generate the Markdown baseline exactly at `docs/reports/page-weight-baseline.md`.
- Explorer CSS/JS/static assets receive `Cache-Control: public, max-age=3600` and cheap validators; dynamic/no-store/export behavior remains unchanged.
- Relevant canonical documentation and Swimm walkthrough are updated; generated docs check, compilation, and `git diff --check` pass.

Harness criteria:

- Focused measurement and cache tests pass.
- Generated documentation check and `git diff --check` pass.
- Canonical repository document and relevant Swimm walkthrough are both updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/reports/page-weight-baseline.md`, `.swm/6.maiixtsw.sw.md`; regenerate script catalog through its generator and verify `python scripts/check_generated_docs.py`.

Rollback/recovery: Revert only this continuation's code, report, tests, and documentation changes; no external state is changed.

Evidence: The former JSON snapshot covered three page builders and only HTML/gzip totals; the new Markdown baseline measures all 24 named HTML builders with deterministic fixtures and no skips. The measured Data Explorer page now references two separately cacheable static assets. Real mounted-asset tests confirm `public, max-age=3600`, ETag/Last-Modified, and conditional 304 responses. Canonical docs: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`; Swimm walkthrough: `.swm/6.maiixtsw.sw.md`.

Files changed: `.github/project-manager/tasks/issue-140-page-weight-and-static-assets.md`; `.swm/6.maiixtsw.sw.md`; `CHANGELOG.md`; `SYSTEM_REFERENCE.md`; `backend/cache_headers.py`; `backend/main.py`; `backend/pages/data_explorer.py`; moved `backend/pages/explorer_snapshots.css` and `backend/pages/explorer_snapshots.js` to `backend/static/`; `scripts/measure_page_weight.py`; `docs/reports/page-weight-baseline.md`; generated `docs/SCRIPT_CATALOG.generated.md`; `tests/test_gzip_middleware.py`; `tests/test_page_weight.py`.
Delegated work: Managed worker `issue-140-weight-assets` inspected active page builders, routing, cache helpers, and tests; implemented the initial metric inventory, report, and static-response cache helper. Its structured return reported 24 builder measurements, 17 focused tests passing, compilation and diff-check success, and no DB/server use. Manager review found that the assets remained inline and no mount existed; the manager moved the two assets to a dedicated static directory, mounted them, externalized the Data Explorer references, added real mounted-response and inventory-completeness tests, and regenerated the report/catalog.
Focused validation: `PYTHON_DOTENV_DISABLED=1 python -m pytest -q --noconftest tests/test_page_weight.py tests/test_gzip_middleware.py tests/test_feature_tabs.py tests/test_api.py::test_search_export_uses_analytics_filters_and_caps_docx_at_two_pages` — 79 passed, 1 skipped. `PYTHON_DOTENV_DISABLED=1 python scripts/measure_page_weight.py` — 24 measured, 0 skipped, output at `docs/reports/page-weight-baseline.md`. `PYTHON_DOTENV_DISABLED=1 python scripts/generate_script_catalog.py` — generated the catalog; `PYTHON_DOTENV_DISABLED=1 python scripts/check_generated_docs.py` — all 3 references current. Python compilation, `node --check backend/static/explorer_snapshots.js`, and `git diff --check` passed.
Residual risk: The full suite was not run because normal repository pytest setup probes PostgreSQL, and this task forbids database access. No browser or deployment check was run. Tests emitted existing Python/dependency deprecation warnings but passed.
Next bounded task: Add a browser smoke check for the static asset loading path without requiring database startup.

## Hypothesis

If the fixture-driven measurement enumerates the page builders and records all requested metrics, the focused test will verify offline coverage and the generated baseline will include each measurable builder with explicit skips; static-asset cache tests will confirm public one-hour validators do not change protected dynamic routes.

## Plan

1. Delegate bounded inspection and implementation of the measuring script, tests, and static-asset cache behavior.
2. Review the worker result and run the recorded focused check.
3. Generate the requested Markdown baseline, update canonical and Swimm documentation, and run final checks.

## Execution Checkpoints

- Delegation: Managed worker returned structured findings; manager reviewed code and verified no prior production mount.
- Implementation: `/static/` serves Explorer snapshot CSS/JS; the builder inventory records raw/gzip, inline script/style, and resource-request metrics. The focused UI/cache/export suite passed.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`, and the generated script catalog; generated the report at `docs/reports/page-weight-baseline.md`.
- Recovery: No long-running or external operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Open a continuation rather than rewriting the completed task | User identified an explicit unmet deliverable in issue #140's prior completion record. | `.github/project-manager/tasks/issue-140-page-performance.md` lines 29, 92; current request |

## Completion

Completion recorded: yes

Summary: Issue #140's remaining page-weight and static asset caching requirements are implemented and validated offline.

Validation: 79 focused tests passed, 1 skipped; all three generated references current; Python and JavaScript checks and diff hygiene passed. Full suite omitted to avoid PostgreSQL access.

Residual risk: No browser smoke or full database-backed test suite.

Next recommended task: Add a browser smoke check for the static asset loading path without requiring database startup.
