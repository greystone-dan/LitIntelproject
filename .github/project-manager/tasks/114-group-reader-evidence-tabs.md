# Task: Group reader evidence tabs

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

Task: Make the Acts / Regs and Tags reader tabs group unique entries like Citations, with Acts / Regs drilling from source to section to occurrences.
Why now: The reader currently exposes evidence rows without the same compact unique-entry navigation used by Citations.
Owner surface: `backend/pages/data_explorer.py` reader evidence-tab rendering and its focused feature-tab tests.
Dependencies: Existing citation grouping behavior, stored statute/tag payload rows, `tests/test_feature_tabs.py`.
Risk boundary: Reader tab presentation only. Preserve stored evidence rows, offsets, extraction, payload schemas, and highlight behavior.
Smallest falsifiable check: A focused test proves unique tags and statute sources are shown once, source expansion reveals unique sections, and section expansion reveals every occurrence.
Acceptance criteria:
- Tags group by unique tag entry and expose its occurrences.
- Acts / Regs group by unique source, then section, then all stored occurrences.
- Existing Citations grouping and reader highlighting remain unchanged.
- Focused tests and browser validation pass.
- Canonical documentation and relevant Swimm walkthrough record the interaction.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`.
Rollback/recovery: Revert only task-owned reader tab source, tests, documentation, and task record changes.
Commit allowed: yes
Push allowed: yes
Evidence:
Hypothesis: The existing Citations tab grouping can be generalized locally to Tags and Acts / Regs without changing evidence payload semantics.
Smallest validation command: `pytest tests/test_feature_tabs.py -q`.
Implementation: Tags retained its unique category/value grouping and occurrence details. Added `groupedStatuteHtml()` for source -> section -> occurrence rendering and routed the active Acts / Regs dispatcher through it; payloads and stored rows remain unchanged.
Validation: `pytest tests/test_feature_tabs.py -q` passed (14 tests); `py_compile backend/pages/data_explorer.py` passed with the existing `\s` SyntaxWarning. Direct Playwright validation against refreshed `http://127.0.0.1:8000/data-explorer?case_id=53516` passed with 7 statute sources, 7 sections, 41 occurrences, 2 tag groups, and 3 tag occurrences, with no page errors or timeouts. Canonical docs updated: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`; Swimm walkthrough updated: `.swm/8.upryk5h6.sw.md`.
