# Task: Stabilize demo reader highlight smoke check

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Make the Data Explorer reader smoke check validate highlight presence across chunk and full-text modes without assuming identical DOM mark counts.

Why now: The management-demo audit exposed a browser smoke failure because the two reader renderers legitimately apply overlap precedence differently.

Owner surface: `scripts/browser_smoke.py` and the active Data Explorer reader contract.

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/pages/data_explorer.py`, `scripts/browser_smoke.py`, `docs/RESEARCH_UI_GUIDE.md`, and the active UI Swimm walkthrough.

Risk boundary: No database writes, parser changes, or changes to backend-owned offsets. Keep validation bounded to the reader smoke path and UI documentation.

Smallest falsifiable check: A bounded browser smoke run opens a case and confirms at least one evidence highlight in both reader modes, while reporting each mode's count.

Acceptance criteria:

- The smoke check no longer fails solely because chunk and full-text mark counts differ.
- Both modes still require visible tag evidence.
- The reader documentation records that overlap precedence can make DOM mark counts differ by mode.
- Focused UI validation passes, or the exact environment blocker is recorded.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, and this task record. No generated references are hand-edited.

Rollback/recovery: Revert the focused smoke assertion and documentation if the renderer contract is later changed to guarantee identical mark counts.

Evidence: Static inspection shows full text resolves citations and tags together, while chunk mode renders citations first and then applies tags to remaining text nodes. Focused validation passed: `py_compile` for `scripts/browser_smoke.py`, `15 passed` in `tests/test_feature_tabs.py`, and browser smoke passed for the populated Vavilov workflow. Updated `docs/RESEARCH_UI_GUIDE.md` and `.swm/6.maiixtsw.sw.md` with the overlap contract and validation rule.

## Hypothesis

If smoke validation checks evidence presence rather than exact mark-count equality, the test will remain sensitive to missing reader evidence without rejecting valid overlap differences between renderers.

## Completion

Completion recorded: yes

Validation: `python -B -m py_compile scripts/browser_smoke.py` passed; `python -m pytest tests/test_feature_tabs.py -q` passed (`15 passed`); `python scripts/browser_smoke.py --base-url http://127.0.0.1:8000 --query Vavilov` passed.

Residual risk: Exact DOM mark counts remain representation-dependent when evidence spans overlap; backend-owned offsets and evidence integrity were not changed by this task.

TODO / next task: Add the remaining management-demo journeys and issue-first discovery scenarios; keep judge backfill gated on the separate 95% evaluation task.
