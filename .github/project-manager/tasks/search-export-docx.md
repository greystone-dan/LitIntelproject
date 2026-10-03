# Task: Add DOCX export for case search

Status: blocked
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Complete `GET /search/export.docx` and the active Data Explorer Download Word control using the actual analytics case-search contract.

Why now: Issue #89's initial implementation does not preserve the active Data Explorer filters: the UI calls `/analytics/search/cases` with query parameters, while the export currently binds the unrelated `CaseSearchRequest` contract. There is no CSV export route in this codebase; do not add one.

Owner surface: Active case-search API/UI in `backend/routes.py` and `backend/pages/data_explorer.py`, with focused API and UI contract tests.

Commit allowed: no

Push allowed: no

Dependencies: Existing `/analytics/search/cases` and `fetch_analytics_search_cases` semantics; `backend/deidentify.py` DOCX support; no new dependency.

Risk boundary: Preserve the active UI's `query,cites,government_outcome,decision_outcome,minister,judge,court,year,search_full_text,sort_by,limit` filters; paginate bounded offsets through the existing analytics service, whose per-call cap is 100; cap export at 200; do not change search behavior or invent a CSV endpoint.

Smallest falsifiable check: focused DOCX API tests plus the Data Explorer UI contract assertion in `tests/test_api.py` and `tests/test_feature_tabs.py`.

Acceptance criteria:

- `GET /search/export.docx` accepts the active analytics UI filter names, preserves their `fetch_analytics_search_cases` semantics, and exports no more than 200 cases through bounded offset pagination.
- DOCX contains query/filter/generated-date/count header information and a citation/title/court/date/outcome table.
- Response uses a sanitized attachment filename and `Cache-Control: no-store`.
- Focused route tests verify active filter forwarding, two-page 200-result cap, DOCX contents/headers/safe filename/no-store.
- Data Explorer has a visible Download Word control next to result/status controls, builds a GET link from active search values, is handled appropriately before results, and ignores stale asynchronous search responses.
- Do not create a CSV endpoint; none exists in this codebase.
- Canonical repository documentation and the relevant Swimm walkthrough are updated.

Harness criteria: Focused DOCX route and UI contract checks pass; required docs paths and validation evidence are recorded.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/5.b49ftjal.sw.md`, and generated `docs/API_REFERENCE.generated.md` (refresh via `scripts/generate_api_reference.py`).

Rollback/recovery: Revert only the new route, test, and associated docs/task changes; no persisted data or schema changes.

Evidence: Manager reviewed the initial uncommitted implementation and confirmed both acceptance gaps: it bound `CaseSearchRequest`/`execute_search_cases` instead of the active analytics parameters/service, and no Download Word control existed. Recovery implementation accepts the active parameter names, pages offsets 0 and 100 with 100 rows per service call, caps at 200, and tests DOCX contents/response safety and UI contract. Manager review caught and corrected a status-marker mismatch that would have prevented control insertion. An independent read-only review found a stale-response race; the Data Explorer now ignores earlier asynchronous case-search results. Follow-up source verification found the control was being injected by the route wrapper rather than rendered by the owning page module; the anchor and controller now live in `backend/pages/data_explorer.py`, while the route helper delegates to that page builder. The UI test checks the rendered adjacent hidden anchor, exact `searchValues()` keys, visibility conditions, and generation guard. `python -m py_compile backend/routes.py backend/pages/data_explorer.py tests/test_api.py tests/test_feature_tabs.py`, `git diff --check`, and `node --check -` on the generated page's export-control script passed. The page HTML was rendered in memory and statically checked for the adjacent control. Compilation emitted a `SyntaxWarning` for an unchanged `\s` sequence at line 8 of the existing HTML literal. Focused pytest is blocked (`No module named pytest`); `python scripts/check_generated_docs.py` is blocked because FastAPI and SQLAlchemy are absent. Generated docs were not hand-edited. Task remains blocked because runtime tests and generated-doc CI validation could not run.

Files changed: `backend/routes.py`, `backend/pages/data_explorer.py`, `tests/test_api.py`, `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `CHANGELOG.md`, `.swm/5.b49ftjal.sw.md`, `.github/project-manager/tasks/search-export-docx.md`, `.github/project-manager/tasks/issue-89-search-export-control-recovery.md`.
Delegated work: Managed worker owned the bounded route/UI/test recovery slice and returned the required structured report. A read-only code-review agent flagged the late-response race; manager independently checked and fixed it in the Data Explorer request generation, also keeping export hidden in RAG mode. Manager fixed the status-marker mismatch, updated docs/task record, and owns final validation and commit/push.
Focused validation: `python -m pytest -q tests/test_api.py::test_search_export_uses_analytics_filters_and_caps_docx_at_two_pages tests/test_feature_tabs.py::test_data_explorer_word_export_uses_active_case_search_filters` — blocked (`No module named pytest`). `python -m py_compile backend/routes.py backend/pages/data_explorer.py tests/test_api.py tests/test_feature_tabs.py && git diff --check` — passed. The generated Data Explorer HTML was rendered in memory, its direct-page anchor adjacency was asserted, and the export-control script passed `node --check -`. `python scripts/check_generated_docs.py` — blocked (FastAPI and SQLAlchemy absent).
Residual risk: Runtime route/test behavior, browser visibility, stale-response behavior, and generated API/schema docs are not verified in this dependency-free environment. The rendered source, status adjacency, state conditions, and filter-key contract are statically checked; no broad suite was run.
Next bounded task: Re-run the focused API/UI tests and documentation-sync CI check in a dependency-enabled project environment, review generated-reference diff, then complete and commit/push.

## Hypothesis

If the export forwards the active Data Explorer's analytics query parameters to `fetch_analytics_search_cases` using bounded offsets, the focused tests will demonstrate preserved UI filters, at most 200 rows, valid DOCX metadata/headers, and a visible current-filter Download Word control.

## Plan

1. Replace the incorrect route contract with active analytics filters and bounded offset pagination; add the Download Word control and stale-response protection in the active Data Explorer.
2. Add focused route coverage for forwarded UI filter names, two pages/200 cap, DOCX contents and response safety, plus a UI contract assertion.
3. Run focused validation, update canonical and Swimm docs, refresh generated API docs if dependencies permit, secret-scan, review final diff, then commit/push only after completion.

## Execution Checkpoints

- Delegation: Managed worker completed the bounded route/UI/test recovery assignment. It reported syntax and whitespace checks passed and focused pytest blocked by missing pytest; files owned were `backend/routes.py`, `tests/test_api.py`, and `tests/test_feature_tabs.py`.
- Implementation: Route now delegates to `fetch_analytics_search_cases` with active analytics query names and bounded two-page offset pagination; Data Explorer control builds a current-filter GET link and is hidden before nonempty successful results or when filters become dirty; older asynchronous searches cannot overwrite newer ones.
- Documentation: Updated canonical `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and Swimm walkthrough `.swm/5.b49ftjal.sw.md`. CI generator `scripts/check_generated_docs.py` failed because FastAPI and SQLAlchemy are absent; generated output remains untouched.
- Recovery: No stateful operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created | Bounded issue #89 API enhancement; one search-export owner and falsifiable test | `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, and `.swm/5.b49ftjal.sw.md` reviewed |
| 2026-10-03 | Recovery plan updated | Review found export/API contract mismatch and missing active UI control; preserve the existing incomplete changes while correcting the same owner surface | User-provided acceptance gaps and current route/UI diff |
| 2026-10-03 | Race-guard scope added | Read-only review found late responses can replace current results and mismatch the export link; prevent stale case-search responses at the active search owner | Code-review report on `backend/routes.py` UI status observer |

## Completion

Completion recorded: no

Summary: Route/UI implementation and documentation recovery are present, but runtime-focused tests and generated-reference CI could not execute because required dependencies are missing.

Validation: `python -m py_compile backend/routes.py backend/pages/data_explorer.py tests/test_api.py tests/test_feature_tabs.py && git diff --check` passed; `node --check -` passed for the Data Explorer search and injected export scripts; the common-secret-pattern scan found no matches. The exact focused pytest invocation failed with `No module named pytest`. `python scripts/check_generated_docs.py` reported missing FastAPI and SQLAlchemy and generated-doc drift because the generators could not run.

Residual risk: API/test runtime behavior, rendered/browser control behavior, and generated OpenAPI/schema output have not been verified. No commit or push was made while task is blocked.

Next recommended task: Run the exact focused tests and documentation-sync CI check in a dependency-enabled environment; do not add a CSV endpoint.
