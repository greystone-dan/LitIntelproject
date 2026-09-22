# Task: Explain recent-case theme classification

Status: in_progress
Created: 2026-09-22
Updated: 2026-09-22

Task: Add report-level classification factors explaining why each recent-case theme received its status.
Why now: Human review needs to distinguish role-driven centrality from broad text, tag, statute, or subject matches.
Owner surface: `scripts/discover_recent_case_themes.py` and its focused tests.
Dependencies: Existing report-only theme classifier and controlled evidence registry.
Risk boundary: Additive JSON/report metadata only; no canonical writes, migrations, existing evidence changes, UI changes, or external calls.
Smallest falsifiable check: A focused test can assert the factor values and threshold reason for a central theme.
Acceptance criteria:
- Every matched theme reports role score, independent evidence kinds, and the threshold branch used.
- Existing status and evidence payloads remain unchanged.
- Focused tests cover role-driven and non-role-driven classification factors.
- Canonical docs, Swimm, and this task record are updated.
Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`.
Rollback/recovery: Remove the classification factor field, test assertions, and documentation additions.
Evidence:
- Files: `scripts/discover_recent_case_themes.py`, `tests/test_discover_recent_case_themes.py`, `SYSTEM_REFERENCE.md`, and `.swm/8.upryk5h6.sw.md`.
- Focused validation: `python -m pytest tests/test_discover_recent_case_themes.py::test_theme_record_preserves_evidence_and_classifies_central_signal -q` passed after confirming the fixture's existing subject evidence.
- Classification factors now report role score, sorted independent evidence kinds, and the exact status threshold branch.
- Full focused validation: `python -m pytest tests/test_discover_recent_case_themes.py -q` passed with 3 tests; `py_compile` and `git diff --check` passed.
- Bounded live validation: `python -m scripts.discover_recent_case_themes --start-date 2020-09-22 --end-date 2026-09-22 --limit 25 ...` produced 25 cases, 21 cases with themes, 79 theme matches, and classification factors on every match.
- Residual risk: factors explain deterministic classification but do not establish legal correctness; human review remains required.
Status: complete
Commit allowed: yes
Push allowed: yes
