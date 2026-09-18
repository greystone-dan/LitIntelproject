# Task: Reader highlight code cleanup

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

Task: Remove duplicate and stale active-reader highlighting code while preserving backend-owned evidence rows, offsets, colors, hover behavior, and reader contracts.
Why now: The active Data Explorer page accumulated layered renderer overrides and an obsolete text-search tag overlay, making highlight behavior difficult to reason about and regress.
Owner surface: `backend/pages/data_explorer.py` active reader highlighting path.
Dependencies: `tests/test_feature_tabs.py`, `scripts/browser_smoke.py`, live local API for Mason browser validation.
Risk boundary: Active reader highlighting only. Do not alter extraction, stored evidence, payload schemas, tab semantics, or legacy routes.
Smallest falsifiable check: Mason renders the same stored citation/statute/tag rows after cleanup, with exact span text and unchanged colors.
Acceptance criteria:
- One active chunk renderer remains.
- Chunk tags use the offset-based helper only; stale text-search overlay is removed.
- Stored citation/statute/tag rows and backend offsets remain unchanged.
- Focused reader tests and Mason Playwright validation pass.
- Canonical documentation and relevant Swimm walkthrough record the cleanup.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`.
Rollback/recovery: Revert only the task-owned reader source, tests, documentation, and task record changes.
Commit allowed: yes
Push allowed: yes
Evidence: Read-only Explore audit identified duplicate chunk renderer definitions and a stale text-search tag helper still called from chunk mode. Removed the duplicate renderer, redundant alias assignment, and stale text-search overlay; retained the single offset-based tag helper and all stored evidence rows/contracts. Focused validation passed: `py_compile backend/pages/data_explorer.py` and `pytest tests/test_feature_tabs.py -q` (14 passed). Browser smoke passed against refreshed `http://127.0.0.1:8000` with query `B010`: 96 tag highlights, 111 citations, 155 statutes, distinct citation/statute colors, hover text, and mobile Themes loading. Canonical docs updated: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`; Swimm walkthrough updated: `.swm/8.upryk5h6.sw.md`.
