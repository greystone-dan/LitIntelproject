# Task: Move About content to Site Architecture

Status: complete
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Move the existing About tab content into Site Architecture and leave About blank for a future task.

Why now: The current About narrative belongs with the site's architecture explanation; the About tab should be available as a clean placeholder.

Owner surface: `backend/pages/data_explorer.py` and its focused UI tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing Data Explorer tab markup, shared About stats loader, and feature-tab tests.

Risk boundary: Preserve existing dynamic metric IDs, tab IDs, API behavior, styling, and unrelated worktree changes. Do not change database or route contracts.

Smallest falsifiable check: Rendered HTML contains the moved prose only under `siteArchitecturePanel`, while `aboutPanel` remains present and contains no About story content.

Acceptance criteria:

- Existing About prose appears in Site Architecture.
- About remains selectable and blank of prose, ready for a future feature.
- Shared metrics and inventory controls continue to render.
- Focused UI tests and whitespace validation pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`

Rollback/recovery: Restore the moved HTML block and test assertions; no database or migration rollback is required.

Evidence: `backend/pages/data_explorer.py` now leaves `aboutPanel` with its live inventory shell and explicit future-content placeholder, while the former six-section overview is rendered under `siteArchitecturePanel`. Added a focused boundary test in `tests/test_feature_tabs.py`. `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 19 tests. Canonical documentation updated in `SYSTEM_REFERENCE.md` and `docs/RESEARCH_UI_GUIDE.md`; Swimm walkthrough updated in `.swm/6.maiixtsw.sw.md`. `git diff --check` passed. Commit/push evidence is recorded below.

## Hypothesis

If the six About prose sections are moved into the existing Site Architecture story container while About's panel shell remains intact, then the rendered page will preserve the information and expose a blank About tab without changing runtime data loading.

## Plan

1. Read the local page builder and focused feature-tab tests.
2. Move the six prose sections and add structural regression assertions.
3. Run the focused tests immediately, then update canonical and Swimm documentation.
4. Re-run validation and commit/push the completed checkpoint.

## Execution Checkpoints

- Delegation: Explore agent inspected the page builder and focused tests; no files changed.
- Implementation: `backend/pages/data_explorer.py` and `tests/test_feature_tabs.py`; focused suite passed.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md` describe the new tab ownership.
- Recovery: No long-running operation; standard Git rollback is sufficient.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-24 | Move prose into Site Architecture and retain About shell | Keeps architecture explanation together while reserving About for future content | Delegated inspection found six About prose sections and an existing Site Architecture narrative |

## Completion

Completion recorded: yes

Summary: Moved the About overview into Site Architecture and left About ready for future content.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 19 tests; `git diff --check` passed; VS Code diagnostics reported no errors in the touched Python files.

Residual risk: The About tab will intentionally be sparse until a future feature populates it.

Next recommended task: Define the future About-tab content or remove the placeholder after product review.
