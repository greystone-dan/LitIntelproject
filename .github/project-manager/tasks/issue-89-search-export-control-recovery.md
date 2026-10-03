# Task: Restore Data Explorer DOCX search export control

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Implement the missing visible Download Word control adjacent to Data Explorer search status, with correct active-search URL and visibility lifecycle.

Why now: Recovery verification found the task-record claim does not match source: the anchor is absent, while a focused UI test expects it.

Owner surface: `backend/pages/data_explorer.py` search UI and its focused feature-tab test.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `/search/export.docx` route and `searchValues()` query field contract.

Risk boundary: Keep the existing export route and exact user filter field names; no CSV route or unrelated search behavior changes. Avoid stale results with the existing generation check.

Smallest falsifiable check: `python -m pytest -q tests/test_feature_tabs.py`

Acceptance criteria:

- An initially hidden Download Word anchor is adjacent to search results status.
- Successful nonempty active case search exposes `/search/export.docx` with the current query and exact `searchValues()` filters; RAG, empty, loading, error, or post-edit states hide it.
- Focused UI source/test assertion passes.

Harness criteria: Source/test contract verifies the anchor, route, filter field names, and state visibility requirements.

Docs/generated references: Update `docs/RESEARCH_UI_GUIDE.md` and the relevant Data Explorer walkthrough in `.swm/`; generated references: none.

Rollback/recovery: Revert only the search-export control and corresponding test/docs changes; preserve unrelated worktree state.

Evidence: Verified the actual page source and found the control had only been injected in the `backend/routes.py` rendering wrapper; the owning `backend/pages/data_explorer.py` template still lacked it. Moved the initially hidden anchor and control script into the page source, made the route helper delegate to the page builder, and aligned the focused test with that rendered-page source. The controller uses `Object.entries(searchValues())` so it preserves the exact existing filter names, hides the link except for a nonempty successful ordinary search, hides it on edits and RAG mode, and retains the generation guard against stale responses. Reviewed the DOCX route and focused API test for matching filter names and bounded export behavior. Updated canonical docs `SYSTEM_REFERENCE.md` and `docs/RESEARCH_UI_GUIDE.md` and Swimm walkthrough `.swm/5.b49ftjal.sw.md`.

Files changed: `backend/pages/data_explorer.py`, `backend/routes.py`, `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/5.b49ftjal.sw.md`, `.github/project-manager/tasks/issue-89-search-export-control-recovery.md`, `.github/project-manager/tasks/search-export-docx.md`.
Delegated work: Managed worker inspected the route/page/API contract and strengthened `tests/test_feature_tabs.py`; it did not implement the page anchor because it found the pre-existing route-wrapper injection. Manager independently checked the source and recovered by moving the control into the owning page module. Worker returned structured findings: syntax/whitespace checks passed; pytest unavailable.
Focused validation: `python -m pytest -q tests/test_feature_tabs.py` — blocked, `No module named pytest`. `python -m py_compile backend/pages/data_explorer.py backend/routes.py tests/test_feature_tabs.py && git diff --check` — passed, with a pre-existing `SyntaxWarning` for invalid escape `\s` in the page HTML literal. Generated the page HTML in memory, asserted the initially hidden link is adjacent to `searchMeta`, and passed its export-control script to `node --check -` — passed. Re-read `tests/test_api.py::test_search_export_uses_analytics_filters_and_caps_docx_at_two_pages` and the DOCX route; no route/test mismatch found.
Residual risk: The focused pytest could not execute because pytest is absent; route/runtime behavior and browser visibility were not exercised. Existing issue #89 changes remain uncommitted; no commit or push was performed.
Next bounded task: Re-run the focused UI and API tests in a pytest-enabled environment.

## Hypothesis

If the missing search export control is restored and its state transitions remain synchronized with the active search generation, the focused feature-tab test will verify the generated HTML/script link-control contract.

## Plan

1. Implement the anchor and minimal UI test in the Data Explorer owner surface.
2. Inspect the exact diff and route/query contract.
3. Update canonical UI guide and Swimm active-UI walkthrough; run focused validation.

## Execution Checkpoints

- Delegation: Managed-worker test-contract inspection completed; manager completed the source recovery after the worker left page source unchanged.
- Implementation: Added the anchor/controller to the page source and removed duplicate route-level HTML injection; focused UI assertion now checks exact `searchValues()` field names and state contract.
- Documentation: Updated canonical `SYSTEM_REFERENCE.md`, workflow guide `docs/RESEARCH_UI_GUIDE.md`, and Swimm Search and Retrieval walkthrough `.swm/5.b49ftjal.sw.md`.
- Recovery: No long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Recovery task opened for actual source/test mismatch | User identified missing anchor in source despite existing test expectation | User-provided source locations and contract |
| 2026-10-03 | Render the control in the owning Data Explorer page module | A route wrapper made returned HTML contain the anchor but left page source without the actual control | Generated page HTML statically verified; focused source/test contract aligned |

## Completion

Completion recorded: yes

Summary: Restored the Download Word control in the owning page source, aligned the focused test to the exact search contract, and updated canonical/Swimm guidance.

Validation: Page compilation, route/test compilation, generated-HTML adjacency assertion, embedded JavaScript syntax check, and `git diff --check` passed. Focused pytest was attempted but is unavailable in the environment.

Residual risk: Runtime test execution and browser behavior remain unverified because pytest is not installed; see evidence above.

Next recommended task: Re-run the focused UI and DOCX API tests where pytest is available.
