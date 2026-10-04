# Served HTML dead-ends audit — Issue #142

## Scope and method

The new `scripts/check_site_links.py` enumerates registered GET HTML pages and
FastAPI documentation pages. It renders HTTP-safe routes through `TestClient`
without starting application lifespan; the two pages that need database-backed
rows use deterministic page-builder fixtures instead. The audit does not load
`.env`, connect to a database, or make network requests. It checks local anchor
`href`, form `action`, and statically literal inline `fetch` and
`XMLHttpRequest.open` URLs against registered route paths and methods.
Parameterized route segments and FastAPI's ordinary trailing-slash redirect
behavior are recognized. Pytest coverage is in `tests/test_check_site_links.py`.

The checker intentionally skips external/protocol URLs, fragments, existing
files served by registered static mounts, and runtime-computed JavaScript URLs.
It cannot validate fetched external scripts, values generated only at runtime,
database-dependent page content, or browser behavior.

## Findings

1. **HTML not-found responses were not HTML.** The default FastAPI handler
   returned JSON for an HTTP 404 even when the browser requested a page. The
   registered HTML error handler now returns a safe, minimal HTML 404 with the
   correct status and Home and Search links. Non-HTML HTTP exceptions continue
   through FastAPI's existing handler.
2. **Unhandled browser failures had no HTML page.** Starlette's default generic
   server-error response is plain text. Requests accepting HTML now receive a
   generic HTML 500 without exception details; non-HTML requests retain the
   generic plain-text 500.
3. **Retired Judge Outcomes endpoint remained in dormant client code.** The
   audit found `/analytics/judge-outcomes?min_decisions=100` in the Data
   Explorer builder; its sandbox page reuses that builder. The old tab and
   panel had already been retired, so the fetch had no registered endpoint.
   Removed the unused loader/renderer and kept old `?tab=judge-outcomes`
   bookmarks useful by redirecting them to Judge Profile.

## Changes and validation

- Added route/method-aware URL checking and actionable findings in
  `scripts/check_site_links.py`.
- Added generic, content-negotiated HTML error responses in
  `backend/html_errors.py`, registered by `backend/main.py`; JSON API exceptions
  and plain-text non-HTML 500 behavior remain unchanged. HTML errors link to
  both Home and Search.
- Added a pytest smoke test that runs the route-backed page snapshot audit, in
  addition to focused unit coverage for URL resolution, method mismatches,
  intentional URLs, HTML 404/500 behavior, and preservation of non-HTML errors.
- Updated the UI guide, system reference, and active UI walkthrough.

Observed checks:

| Command | Result |
| --- | --- |
| `python scripts/check_site_links.py` | Passed: 23 TestClient/fixture snapshots checked against 175 registered routes; zero local URL findings. |
| `python -m pytest -q --noconftest tests/test_feature_tabs.py tests/test_check_site_links.py tests/test_html_error_responses.py tests/test_documentation_contracts.py` | Passed: 71 passed, 1 skipped. `--noconftest` avoids the repository's PostgreSQL availability probe. |
| `python -m py_compile` on changed Python modules | Passed. |
| All four `scripts/generate_*.py` generators | Passed in the isolated validation environment. |
| `python scripts/check_generated_docs.py` | Passed: all 3 checked generated references are current. |
| Full CI-deselected `python -m pytest -q` suite | Not run; pytest collection probes PostgreSQL, which this task must not access. |

The full test suite remains unverified because its shared `tests/conftest.py`
probes PostgreSQL during collection, and this task cannot access a database.
The full-suite CI exclusions are
`tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence`,
`tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes`,
and
`tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint`.
An earlier focused pytest invocation did run the repository's PostgreSQL
availability probe (`SELECT 1`); it made no writes. The final focused run
disabled conftest loading to avoid further database access. No deployment,
`.env`, credential, dependency-file, or migration changes were made.
