# Task: Split reader Info and Advanced tabs

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

Task: Give the inline reader a concise user-facing Info tab and a separate Advanced tab.
Why now: The reader's metadata surface mixed normalized case facts with raw extraction and operational detail.
Owner surface: `backend/pages/data_explorer.py` reader information tabs.
Dependencies: Existing reader payload fields, tag/citation/statute tabs, focused UI tests.
Risk boundary: Reader presentation only. Preserve evidence layers, backend offsets, routes, and payload schemas.
Smallest falsifiable check: Generated reader HTML exposes Info and Advanced tabs with normalized case fields, and the focused feature-tab test passes.
Acceptance criteria:
- Info is the default reader tab and presents case name, citation, court, date, outcome, judge, minister/government party, jurisdiction, language, source, and evidence counts.
- Advanced presents record identity, processing/source details, counts, extracted metadata, and provenance.
- Citations, Tags, Acts / Regs, and Precedents remain separate tabs.
- Focused tests, compilation, and diff validation pass.
- Canonical UI, system, and Swimm documentation describe the split.
Docs/generated references: `SYSTEM_REFERENCE.md`; `docs/RESEARCH_UI_GUIDE.md`; `.swm/8.upryk5h6.sw.md`.
Rollback/recovery: Revert the final reader tab override, focused assertions, documentation, and this task record.
Evidence:
- `pytest tests/test_feature_tabs.py -q`: 14 passed.
- `py_compile backend/pages/data_explorer.py`: passed with existing SyntaxWarning.
- `git diff --check`: passed.
- Note: task 117's independent chunk/full-text highlight parity issue remains in progress and is outside this task.
Commit allowed: yes
Push allowed: yes
