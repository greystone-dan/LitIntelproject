# Task: Improve search interface clarity

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

Task: Improve the active Data Explorer case-search bar and advanced-search presentation while preserving the existing visual language and search behavior.
Why now: The current search entry point and advanced controls are dense and do not make the primary query, filter state, or submission path easy to scan.
Owner surface: `backend/pages/data_explorer.py` search shell, styles, and client-side search controls.
Dependencies: `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, current search API contract.
Risk boundary: UI-only. Preserve search parameter names, endpoint behavior, reader navigation, active seven-tab shell, and backend-owned evidence behavior. No data, schema, ingestion, or external paid operation.
Smallest falsifiable check: Render the page and assert the primary search input, clear/submit controls, advanced disclosure, and existing filter IDs remain present; run the focused feature-tab test.
Acceptance criteria:
- Primary search intent and submit action are visually clear at desktop and mobile widths.
- Advanced filters are grouped and labeled with readable spacing and a clear open/close state.
- Existing search controls and parameter IDs remain compatible with the current client logic.
- Empty, active-filter, and responsive states remain legible without changing search semantics.
- Focused UI tests, Python compilation, and a browser smoke check pass.
- Canonical UI guide and active Swimm walkthrough describe the improved search workflow.
Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`; no generated reference changes expected.
Rollback/recovery: Revert only the search markup/style/client changes and associated focused tests/docs; no database recovery required.
Commit allowed: yes
Push allowed: yes

Hypothesis: If the search surface establishes one dominant query row, a clear primary action, and grouped advanced filters with explicit state, researchers will be able to discover and operate the existing search capabilities more reliably without API or query changes.

Delegated work: Bounded Explore inventory completed for the current search markup, local design patterns, test contract, and applicable search usability principles. The implementation remained on the single `backend/pages/data_explorer.py` owner surface.

Evidence:
- Files changed: `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and this task record.
- Focused test: `& '.\\venv\\Scripts\\python.exe' -m pytest tests/test_feature_tabs.py -q` -> 16 passed, 2 warnings.
- Compilation: `& '.\\venv\\Scripts\\python.exe' -m py_compile backend/pages/data_explorer.py` -> passed with an existing SyntaxWarning.
- Browser validation: bounded Playwright desktop/mobile workflow passed. Advanced options opened, `#judgeFilter` became usable, the summary changed to `1 active filter`, Clear reset the form and collapsed advanced controls, Vavilov returned 6 result cards, mobile controls fit without overlap, and no console/page/request errors were observed.
- Server check: `/health` returned HTTP 200 after refreshing Uvicorn with the current source.
- Canonical documentation updated: `SYSTEM_REFERENCE.md` and `CHANGELOG.md`.
- Swimm walkthrough updated: `.swm/6.maiixtsw.sw.md`.
- Residual risk: browser validation covered the active search workflow and responsive control layout, not every filter combination or every result-card navigation path.
- Next bounded task: none for this request; keep broader search-quality improvements separate from this UI change.
