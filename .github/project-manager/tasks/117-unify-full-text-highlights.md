# Task: Unify full-text and chunk highlights

Status: in-progress
Created: 2026-09-18
Updated: 2026-09-18

Task: Make stored tag highlights apply consistently in chunk and full-text reader modes.
Why now: Full-text mode currently misses basic tag highlights that appear in chunk mode, reducing evidence visibility when readers switch views.
Owner surface: `backend/pages/data_explorer.py` reader highlight rendering and focused browser/test coverage.
Dependencies: Existing chunk offset helper, `highlightedDecision()`, `tests/test_feature_tabs.py`, `scripts/browser_smoke.py`.
Risk boundary: Reader presentation only. Preserve backend-owned offsets, stored evidence rows, citation/statute layers, payload schemas, and extraction behavior.
Smallest falsifiable check: The same case shows tag highlights in both modes, with no loss of citation/statute highlights and no evidence row filtering.
Acceptance criteria:
- Full-text mode applies the same stored tag evidence as chunk mode.
- Chunk mode behavior remains unchanged.
- Citation and statute highlights remain present and distinct.
- Focused tests and browser validation pass in both modes.
- Canonical documentation and relevant Swimm walkthrough record the fix.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`.
Rollback/recovery: Revert only task-owned reader renderer, tests, documentation, and task record changes.
Commit allowed: yes
Push allowed: yes
Evidence:
Hypothesis: Full-text mode misses tags because `highlightedDecision()` uses a separate range renderer; routing both modes through the same backend-offset tag projection will restore parity.
Delegated work: pending bounded renderer comparison.
Focused validation: pending; baseline `pytest tests/test_feature_tabs.py -q`.
