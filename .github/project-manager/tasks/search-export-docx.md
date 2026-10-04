# Task: Add DOCX export for case search

Status: blocked
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Complete `GET /search/export.docx` and the active Data Explorer Download Word control using the actual analytics case-search contract.

Why now: Issue #89's initial implementation did not preserve the active Data Explorer filters: the UI calls `/analytics/search/cases` with query parameters, while the export bound the unrelated `CaseSearchRequest` contract. PR #74 has since added the CSV export route and button.

Owner surface: Active case-search API/UI in `backend/routes.py` and `backend/pages/data_explorer.py`, with focused API and UI contract tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `/analytics/search/cases` and `fetch_analytics_search_cases` semantics; `backend/deidentify.py` DOCX support; no new dependency.

Risk boundary: Preserve the active UI's `query,cites,government_outcome,decision_outcome,minister,judge,court,year,search_full_text,sort_by,limit` filters; paginate bounded offsets through the existing analytics service, whose per-call cap is 100; cap export at 200; keep DOCX and CSV exports separate in the shared actions group.

Smallest falsifiable check: focused DOCX API tests plus the Data Explorer UI contract assertion in `tests/test_api.py` and `tests/test_feature_tabs.py`.

Acceptance criteria:

- `GET /search/export.docx` accepts the active analytics UI filter names, preserves their `fetch_analytics_search_cases` semantics, and exports no more than 200 cases through bounded offset pagination.
- DOCX contains query/filter/generated-date/count header information and a citation/title/court/date/outcome table.
- Response uses a sanitized attachment filename and `Cache-Control: no-store`.
- Focused route tests verify active filter forwarding, two-page 200-result cap, DOCX contents/headers/safe filename/no-store.
- Data Explorer has a visible Download Word control beside Download CSV in the shared search-actions group, builds a GET link from active search values, is handled appropriately before results, and ignores stale asynchronous search responses.
- Preserve the existing CSV export endpoint and control from PR #74; do not conflate its behavior with the DOCX endpoint.
- Canonical repository documentation and the relevant Swimm walkthrough are updated.

Harness criteria: Focused DOCX route and UI contract checks pass; required docs paths and validation evidence are recorded.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/5.b49ftjal.sw.md`, and generated `docs/API_REFERENCE.generated.md` (refresh via `scripts/generate_api_reference.py`).

Rollback/recovery: Revert only the new route, test, and associated docs/task changes; no persisted data or schema changes.

Evidence: The route preserves active analytics filters, exports at most 200 cases, and has DOCX response-safety/content tests. The Word link is now statically rendered in the same case-search `.search-actions` group beside PR #74's CSV button, with distinct IDs and independent handlers. Latest `main` (`109a9f3`) was merged; conflict resolution retained both export controls and both routes. API, schema, and script-catalog references were regenerated with their generators, then `python scripts/check_generated_docs.py` passed. The three focused API/UI tests passed. The configured CI suite ran 1,038 passed, 3 failed, 1 skipped, 1 xfailed, and 3 intentionally deselected; the only failures require unavailable Hugging Face model downloads or OpenAI tokenizer network downloads. Python compilation passed with a pre-existing `SyntaxWarning` for `\s` in the page HTML literal. Generated references were not manually edited.

Files changed: `backend/routes.py`, `backend/pages/data_explorer.py`, `tests/test_api.py`, `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `CHANGELOG.md`, `.swm/5.b49ftjal.sw.md`, `.github/project-manager/tasks/search-export-docx.md`, `.github/project-manager/tasks/issue-89-search-export-control-recovery.md`.
Delegated work: Managed worker owned the bounded route/UI/test recovery slice. A read-only review flagged the late-response race; manager verified the current search-generation guard and RAG-mode hiding. Commit/push: `eadcfc5`.
Focused validation: `python -m pytest -q tests/test_api.py::test_case_search_ui_has_download_action_using_current_search_values tests/test_api.py::test_search_export_uses_analytics_filters_and_caps_docx_at_two_pages tests/test_feature_tabs.py::test_data_explorer_word_export_shares_search_actions_with_csv` — 3 passed. The exact CI command reported 1,038 passed and 3 offline external-resource failures (plus 1 skipped, 1 xfailed, and 3 configured deselections). `python scripts/check_generated_docs.py` passed after running all three reference generators. `python -m py_compile backend/routes.py backend/pages/data_explorer.py tests/test_api.py tests/test_feature_tabs.py` passed.
Residual risk: Three CI-suite tests still require Hugging Face or OpenAI tokenizer downloads that this environment cannot access; full CI therefore does not pass here. Browser behavior was not exercised.
Next bounded task: Re-run the focused API/UI tests and documentation-sync CI check in a dependency-enabled project environment, then review any generated-reference diff.

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

Residual risk: API/test runtime behavior, rendered/browser control behavior, and generated OpenAPI/schema output have not been verified. The changes are committed and pushed as `eadcfc5`.

Next recommended task: Re-run the CI suite in a network-enabled environment to validate the three model/tokenizer-dependent tests.
