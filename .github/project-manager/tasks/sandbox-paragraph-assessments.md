# Task: Sandbox paragraph assessment overlay

Status: complete
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Add a toggleable inline paragraph-assessment display to the Discussion Units sandbox.
Why now: The paragraph-level analysis is available as report-only artifacts and needs a usable review surface beside source paragraphs.
Owner surface: `backend/discussion_units_sandbox.py`, sandbox route in `backend/routes.py`, and `backend/pages/discussion_units_sandbox.py`.
Dependencies: Paragraph assessment Markdown artifacts under `data/eval/llm_discussion_units_pilot/paragraph_level_300_run/reviews`.
Risk boundary: Sandbox-only read-only endpoint and page behavior; do not change production reader routes, payloads, or renderers.
Smallest falsifiable check: `venv\\Scripts\\python.exe -m pytest tests/test_discussion_units_sandbox.py -q`.
Acceptance criteria:
- Toggle is off by default and does not alter source paragraph rendering when off.
- Toggle loads assessments only for cohort cases.
- Assessments display beside matching paragraphs with topic, role, confidence, and explanation.
- Missing report artifacts degrade to an unavailable state.
- Production functionality is unchanged.
Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`.
Rollback/recovery: Remove the sandbox helper, route, page controls, tests, and documentation; no data rollback is required.
Evidence: `venv\\Scripts\\python.exe -m pytest tests/test_discussion_units_sandbox.py -q` passed (6 tests); `venv\\Scripts\\python.exe -m py_compile backend/discussion_units_sandbox.py backend/pages/discussion_units_sandbox.py backend/routes.py` passed; `git diff --check` passed. Swimm walkthrough updated at `.swm/6.maiixtsw.sw.md`; canonical repository reference updated at `SYSTEM_REFERENCE.md`.
Commit allowed: yes
Push allowed: yes
