# Task: Case Search CSV export

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Add a filtered Case Search CSV download and `GET /search/export.csv`, limited to 1,000 results, with spreadsheet-safe values and a UTF-8 BOM.

Why now: Let researchers take the same bounded, filtered search results into spreadsheet workflows without losing safety or column consistency.

Owner surface: `backend/routes.py` Case Search API and generated UI; focused API tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing Case Search query and filter contract; no new dependency.

Risk boundary: Do not alter search filtering/ranking, result evidence or persistence, and do not export more than 1,000 rows. Escape leading `=`, `+`, `-`, `@` to prevent spreadsheet formula execution.

Smallest falsifiable check: `python -m pytest tests/test_api.py -k 'search_export or csv_export' -q`

Acceptance criteria:

- `GET /search/export.csv` applies the same search query and filters as Case Search and emits at most 1,000 rows.
- CSV columns, in order: citation, title, court, date, judge, outcome, iLit URL; response is UTF-8 with BOM and formula-prefixed cells are escaped.
- Case Search offers a Download CSV action preserving the current query/filters.
- Focused route and escaping tests pass; no dependency is added.
- The exact CI test command from `.github/workflows/tests.yml` runs and its result is recorded.

Harness criteria:

- Filtered export contract, row cap, columns and encoding pass route tests.
- Spreadsheet formula escaping passes focused tests.
- Case Search download action preserves current query/filter state.
- Configured CI test command result is recorded.
- `SYSTEM_REFERENCE.md` and the active Research UI Swimm walkthrough are updated and validated.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/6.maiixtsw.sw.md`; regenerate/check `docs/API_REFERENCE.generated.md` through `scripts/generate_api_reference.py`; `CHANGELOG.md`.

Rollback/recovery: Revert the focused route/UI/test/doc edits only; preserve all pre-existing worktree changes.

Evidence: Managed worker implemented the route, UI action, and focused tests in `backend/routes.py` and `tests/test_api.py`; worker returned the required structured report. Worker-side pytest was unavailable. Manager installed repository requirements, reviewed the implementation, corrected the partial-page fixture, and used active Data Explorer links. Canonical documentation updated at `SYSTEM_REFERENCE.md` and `CHANGELOG.md`; walkthrough updated at `.swm/6.maiixtsw.sw.md`; generated `docs/API_REFERENCE.generated.md` from `scripts/generate_api_reference.py`. Focused route tests passed (3); active feature-tab tests passed (51); the generated-doc check passed (3 references); compilation, whitespace, Swimm link review, and changed-file secret scan passed. Headless Chromium confirmed the rendered download handler sent the current query and filters to `/search/export.csv`. The exact configured CI suite ran 982 passed, 3 failed, 3 deselected; all 3 failures were unrelated external model/tokenizer downloads blocked by DNS/network access.

Files changed: `.github/project-manager/tasks/case-search-csv-export.md`, `backend/routes.py`, `tests/test_api.py`, `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`, `docs/API_REFERENCE.generated.md` (generated), `CHANGELOG.md`.
Delegated work: Managed worker inspected route/UI and search helper call sites; changed only `backend/routes.py` and `tests/test_api.py`. Worker reported implementation and syntax/whitespace checks passed, but its focused pytest could not start because `pytest` and `fastapi` were unavailable. Manager installed `requirements.txt`, independently reviewed/fixed the test fixture, and owns final validation.
Focused validation: `python -m pytest tests/test_api.py::test_case_search_csv_export_reuses_search_filters_and_escapes_cells tests/test_api.py::test_case_search_csv_export_caps_results_at_1000 tests/test_api.py::test_case_search_ui_has_download_action_using_current_search_values -q` — 3 passed. Parallel validation: `python -m pytest tests/test_feature_tabs.py -q` — 51 passed; `python scripts/check_generated_docs.py` — current (3 references); `python -m py_compile backend/routes.py tests/test_api.py` and `git diff --check` passed; Swimm local links and changed-file secret scan passed (7 files). Headless Chromium executed the rendered download handler with current search values and observed the expected `/search/export.csv` query. Configured CI command from `.github/workflows/tests.yml`: `python -m pytest -q --deselect tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence --deselect tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes --deselect tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint` — 982 passed, 3 failed, 3 deselected, 5 warnings; the failures could not download Hugging Face `BAAI/bge-m3` and OpenAI tokenizer assets because DNS/network was unavailable.
Residual risk: Exact configured CI command completed with 982 passed, 3 failed, 3 deselected, and 5 warnings. The three unrelated failures need Hugging Face `BAAI/bge-m3` or OpenAI tokenizer assets unavailable because network DNS resolution failed. No live database or full-page browser session was run; the Chromium smoke exercised the rendered download handler and search-value helper on a minimal local fixture.
Next bounded task: Re-run the exact configured CI command in an environment with the Hugging Face and OpenAI tokenizer assets cached or network access available.

## Hypothesis

If CSV export uses the existing filtered Case Search query contract with an explicit 1,000-row cap and escapes spreadsheet formula prefixes, the focused route tests will verify equivalent filtering, safe output, stable columns, and a browser action carrying the current filters.

## Plan

1. Assign a managed worker to inspect and implement the bounded route, Case Search download action, and focused tests.
2. Independently run the focused validation; update canonical and Swimm documentation and regenerate/check API references.
3. Run the exact CI test command, secret scan, required `parallel_validation`, then finalize evidence.

## Execution Checkpoints

- Delegation: Managed worker completed the bounded route/UI/test slice in `backend/routes.py` and `tests/test_api.py`; worker test environment lacked dependencies.
- Implementation: CSV endpoint, current-filter download button, formula escaping, BOM, 1,000-row cap, and focused contract tests are in place; focused tests passed.
- Documentation: `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`, generated `docs/API_REFERENCE.generated.md`, and `CHANGELOG.md` updated.
- Validation: Focused route and feature-tab tests, generated-doc check, compilation, whitespace, local-link and secret checks passed; headless Chromium smoke passed. Exact configured CI command ran with 3 external-asset failures; details are recorded above.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created; owner is the Case Search route/UI in `backend/routes.py` | User-specified bounded route/UI feature; API and active UI walkthroughs identify this owner | `SYSTEM_REFERENCE.md`; `.swm/1.oi7rhqp2.sw.md`; `.swm/6.maiixtsw.sw.md`; `.github/workflows/tests.yml` |
| 2026-10-03 | Expose the export in OpenAPI and point links to `/data-explorer?case_id=...` | Keep the CSV contract discoverable and generated links on the active workflow, not the compatibility redirect | Regenerated API reference; `case_reader_page` redirects to `/data-explorer` |

## Completion

Completion recorded: yes

Summary: Added a filtered, spreadsheet-safe Case Search CSV export and a current-filter Download CSV action. Updated canonical, generated, and Swimm documentation.

Validation: Focused export tests: 3 passed; feature-tab tests: 51 passed; generated-doc check current; Chromium download-handler smoke passed. Exact CI suite: 982 passed, 3 external-network-dependent failures, 3 deselected.

Residual risk: Full CI cannot be called green because three unrelated model/tokenizer tests require network assets unavailable in this environment. No live database or full-page browser session was run; the Chromium smoke covered only download-handler query serialization.

Next recommended task: Rerun the configured CI command where the Hugging Face model and OpenAI tokenizer assets are available.
