# Served HTML dead-ends audit — Issue #142

## Scope and method

The new `scripts/check_site_links.py` snapshots the registered GET HTML pages
and FastAPI documentation pages without starting application lifespan, reading
`.env` or database credentials, connecting to a database, or making network
requests. It checks local anchor `href`, form `action`, and statically literal
inline `fetch` and `XMLHttpRequest.open` URLs against registered route paths and
methods. Parameterized route segments and FastAPI's ordinary trailing-slash
redirect behavior are recognized. Pytest coverage is in
`tests/test_check_site_links.py`.

The checker intentionally skips external/protocol URLs, fragments, recognized
static assets, and runtime-computed JavaScript URLs. It cannot validate fetched
external scripts, values generated only at runtime, database-dependent page
content, or browser behavior.

## Findings

1. **HTML not-found responses were not HTML.** The default FastAPI handler
   returned JSON for an HTTP 404 even when the browser requested a page. The
   registered HTML error handler now returns a safe, minimal HTML 404 with the
   correct status and a link back to Data Explorer. Non-HTML HTTP exceptions
   continue through FastAPI's existing handler.
2. **Unhandled browser failures had no HTML page.** Starlette's default generic
   server-error response is plain text. Requests accepting HTML now receive a
   generic HTML 500 without exception details; non-HTML requests retain the
   generic plain-text 500.
3. **Local page-link audit results are pending.** The repository checkout used
   for this change lacks `python-dotenv`, FastAPI, SQLAlchemy, and pytest.
   Therefore the route-backed page snapshots and pytest suite could not execute
   here, and no claim that all rendered page URLs are clean is made. Checker
   behavior was exercised directly against its five deterministic test
   functions. The four HTML-error handler tests were compiled but could not be
   run without Starlette/FastAPI.

## Changes and validation

- Added route/method-aware URL checking and actionable findings in
  `scripts/check_site_links.py`.
- Added generic, content-negotiated HTML error responses in
  `backend/html_errors.py`, registered by `backend/main.py`; JSON API exceptions
  and plain-text non-HTML 500 behavior remain unchanged.
- Added focused tests for local URL resolution, method mismatches, intentional
  URLs, HTML 404/500 behavior, and preservation of non-HTML errors.
- Updated the UI guide, system reference, and active UI walkthrough.

Observed checks:

| Command | Result |
| --- | --- |
| `python -m pytest -q tests/test_check_site_links.py` | Blocked: `pytest` is not installed. |
| `python -m pytest -q tests/test_check_site_links.py tests/test_html_error_responses.py` | Blocked before collection: `pytest` is not installed. |
| Direct invocation of the five checker test functions | Passed. |
| `python -m py_compile backend/main.py backend/html_errors.py scripts/check_site_links.py tests/test_check_site_links.py tests/test_html_error_responses.py` | Passed. |
| `python scripts/check_site_links.py --help` | Passed. |
| `python scripts/check_site_links.py` | Blocked: `python-dotenv` is not installed; FastAPI is also absent. |
| `python scripts/generate_script_catalog.py` | Passed; generated the new script's catalog entry. |
| `python scripts/check_generated_docs.py` | Blocked: API and schema generators cannot import missing FastAPI and SQLAlchemy; the script catalog generator is current. |
| `python -m pytest -q` | Blocked before collection: `pytest` is not installed; the three repository CI deselects were not reached. |

The complete rendered-page audit, focused error-response tests, full suite, and
generated-document check must be rerun in the dependency-equipped project
environment. The full-suite CI exclusions are
`tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence`,
`tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes`,
and
`tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint`;
collection failed before any selection. No database, deployment, `.env`,
credential, dependency, or migration action was performed.
