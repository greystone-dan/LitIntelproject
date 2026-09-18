# Task: Case reader evidence highlights and hover behavior

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Ensure the active case reader renders tags, case citations, and statute/instrument references as distinct evidence highlights with hover details and pinpoint text where available, then validate search and reader workflows in a browser.

Why now: The deterministic pipeline and reader evidence contracts are present, but the user needs confirmation that the basic search/reader experience is fully wired in the active interface.

Owner surface: active Data Explorer reader UI and evidence projection

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/reader_service.py`; `backend/routes.py`; `backend/pages/data_explorer.py`; `backend/pages/quick_search.py`; `tests/test_feature_tabs.py`; browser automation setup

Risk boundary: Active UI only. Preserve backend-owned offsets and existing citation/statute/tag contracts. Do not alter legacy reader surfaces, production data, source acquisition, schema, or broad pipeline jobs.

Smallest falsifiable check: A browser-loaded case reader exposes search results and renders tag, citation, and statute highlight elements with hoverable evidence details; case pinpoints show stored pinpoint text when available.

Acceptance criteria:

- Search workflow opens a case in the active Data Explorer reader.
- Tags highlight single-word occurrences without replacing backend offsets.
- Case citations highlight the citation span and expose hover details.
- Citation pinpoints expose stored pinpoint text when available.
- Laws and regulations behave like citations with a distinct color/evidence type.
- Playwright/browser validation covers search, reader loading, highlight counts, colors/types, and hover behavior.
- Update canonical documentation, relevant Swimm walkthrough, and task evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`

Rollback/recovery: Revert only task-owned UI/test/documentation changes. Do not modify data or legacy reader code.

Evidence: Delegated inspection confirmed the active Data Explorer reader path. Updated `backend/pages/data_explorer.py` to restore tag highlighting, use backend reader citations for chunk-local spans, map absolute statute offsets to chunks, and retain hover authority previews. Updated `scripts/browser_smoke.py` to assert search-to-reader navigation, tag/citation/statute highlight counts, hover text, and distinct computed colors. Focused validation passed: `pytest tests/test_feature_tabs.py -q` (14 passed); Python compilation passed. Playwright passed against `http://127.0.0.1:8000` with query `B010`: 95 tag highlights, 110 case citations, 153 statute highlights, citation `rgb(248, 230, 167)`, statute `rgb(238, 228, 247)`, non-empty hover tooltip, and mobile Themes load. Canonical docs updated: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`; Swimm walkthrough updated: `.swm/8.upryk5h6.sw.md`.

## Hypothesis

If the active Data Explorer reader projects backend-owned evidence spans into typed highlight elements and the browser binds hover details from the same payload, then search-to-reader navigation will expose tags, citations, statutes, and citation pinpoint text without inventing offsets.

## Plan

1. Delegate read-only inspection of active reader markup, payload contracts, and browser-test tooling.
2. Implement the smallest active-reader fix if a wiring gap is confirmed.
3. Run narrow Python tests immediately after edits.
4. Run Playwright/browser validation for search and reader hover behavior.
5. Update canonical/Swimm documentation, validate, commit, and push.

## Completion

Completion recorded: yes

Summary: Active Data Explorer search-to-reader evidence behavior is wired and browser-validated. Tags, case citations, and statutes/regulations render through the supported reader modes with hover evidence details and distinct colors.

Validation: `pytest tests/test_feature_tabs.py -q`; `py_compile` for the touched Python files; Playwright `scripts/browser_smoke.py --base-url http://127.0.0.1:8000 --query B010`.

Residual risk: Pinpoint hover text is present only where the backend stores target paragraph/chunk context. Tag highlights are offset-driven in full-text mode and word-bounded in chunk mode; the browser acceptance fixture validates the former and the citation/statute chunk spans.

Next recommended task: Add accessibility keyboard/ARIA coverage for the reader tabsets and evidence tooltip.
