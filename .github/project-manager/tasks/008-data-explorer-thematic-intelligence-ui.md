# Task: Integrate Contextual Thematic Intelligence & Statute Matrix into Data Explorer UI

Status: complete
Created: 2026-09-03
Updated: 2026-09-03

## Task Record

Task: Expose the new contextual intelligence engine (`/analytics/themes`, `/analytics/statute-tag-matrix`, `/analytics/cases/{case_id}/thematic-cluster`) directly within the active Data Explorer research interface (`backend/pages/data_explorer.py`), allowing litigation analysts to explore legal themes, inspect statutory co-occurrence matrices, and discover thematically clustered precedents with one click.

Why now: We built the backend intelligence engine correlating 2.66M+ tags, statutory provisions, and citations. Integrating this into the primary Data Explorer UI turns these backend capabilities into a live researcher workbench feature for CBSA analysts and legal researchers.

Owner surface: `backend/pages/data_explorer.py`

Dependencies: `backend/contextual_intelligence.py`, `backend/routes.py`, `tests/test_feature_tabs.py`

Risk boundary:
- Existing 8 tabs (About, Case Search, Site Architecture, Citation Intelligence, Judge Outcomes, Judge Profile, Data Explorer, FC History) must remain 100% functional without tab breaking.
- Inline reader highlight inspection must not regress.
- All 311 unit and integration tests must continue to pass.

Smallest falsifiable check:
`.\venv\Scripts\python.exe -m pytest tests\test_feature_tabs.py tests\test_api.py -q`

Acceptance criteria:
- Data Explorer includes an interactive "Legal Themes & Statute Matrix" interface or dedicated controls in the analytics/search panels.
- Analysts can select a statutory provision (e.g. `34(1)(f)`, `25(1)`, `96`, `40(1)(a)`) and view co-occurring tag distributions, top cited precedent cases, and historical applicant relief rates.
- Inline reader / case detail allows viewing similar precedent cases by composite thematic signature.
- Tests pass cleanly and Swimm documentation is updated.

Docs/generated references:
- `SYSTEM_REFERENCE.md`
- `docs/RESEARCH_UI_GUIDE.md`
- `.swm/6.maiixtsw.sw.md` (Frontend and UI Surfaces)

Rollback/recovery: Revert `backend/pages/data_explorer.py` if regressions occur.

Evidence: `\.venv\Scripts\python.exe -m pytest tests\test_contextual_intelligence.py -q` passed (7 tests); `\.venv\Scripts\python.exe -m pytest tests\test_feature_tabs.py tests\test_api.py -q` passed (55 tests); full suite passed (311 tests). The UI uses the registered `/analytics/themes`, `/analytics/statute-tag-matrix`, and `/analytics/cases/{case_id}/thematic-cluster` contracts.

## Hypothesis
Adding dynamic statute matrix exploration and thematic clustering into Data Explorer will allow researchers to query statute-tag affinities and cluster precedents directly in the browser while maintaining full backward compatibility.

## Plan
1. Inspect `backend/pages/data_explorer.py` tabs and client JavaScript.
2. Add interactive statute-tag matrix visualizer and case thematic cluster explorer into Data Explorer.
3. Verify live browser rendering and endpoint responses.
4. Run `tests/test_feature_tabs.py` and full test suite.
5. Update Swimm documentation and mark task complete.

## Decision Log
| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-03 | Task created | Expose contextual intelligence in Data Explorer UI | This task file |
