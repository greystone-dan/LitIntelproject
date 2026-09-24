# Task: Main core cases and paragraph assessments

Status: complete
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Add a main search preset for the 300 Discussion Unit core cases and a main reader toggle for their paragraph assessments.
Why now: The 297 completed report-only assessments need to be usable against their corresponding cases in the active research workflow.
Owner surface: `backend/routes.py`, `backend/pages/data_explorer.py`, and focused API/UI tests.
Dependencies: Core manifest and paragraph assessment reports under `data/eval/llm_discussion_units_pilot`.
Risk boundary: Read-only UI/API additions; default search and reader behavior must remain unchanged; no database writes or schema changes.
Smallest falsifiable check: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py tests/test_api.py -q` with focused test selection if needed.
Acceptance criteria:
- Main search has a `Display core cases` button.
- Clicking it loads the 300 core cases through the ordinary search result contract.
- Main reader has an assessment toggle that is off by default.
- Toggle displays matching topic, role, confidence, and explanation beside source paragraphs when a report exists.
- Cases without a report remain usable and show no assessment overlay.
- Sandbox functionality is not required for this change.
Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`.
Rollback/recovery: Remove the named search parameter, endpoint, UI hooks, tests, and documentation; no data rollback required.
Evidence: `venv\\Scripts\\python.exe -m py_compile backend/pages/data_explorer.py backend/routes.py backend/discussion_units_sandbox.py backend/analytics_service.py` passed. `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py tests/test_discussion_units_sandbox.py -q` passed (23 tests). `venv\\Scripts\\python.exe -m pytest tests/test_api.py -q` passed (44 tests). Final focused `venv\\Scripts\\python.exe -m pytest tests/test_api.py tests/test_feature_tabs.py -q` passed (64 tests). `git diff --check` passed; Git reported only LF/CRLF normalization warnings for the two documentation files. Canonical documentation updated in `SYSTEM_REFERENCE.md` and Swimm walkthrough `.swm/6.maiixtsw.sw.md`.
Commit allowed: yes
Push allowed: yes
