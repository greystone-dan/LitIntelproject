# Task: Add an interactive system map to About

Status: complete
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Replace the reserved About placeholder with a polished, expandable system map that explains the full site's workflow and major research surfaces.

Why now: The About tab is reserved for new content and is the appropriate entry point for a trustworthy, navigable explanation of how the site functions.

Owner surface: `backend/pages/data_explorer.py` and its focused UI tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing Data Explorer tab markup, shared page styles/scripts, live About stats loader, Site Architecture content, and feature-tab tests.

Risk boundary: UI-only. Preserve existing tab IDs, API routes, live metrics, source/provenance wording, accessibility, and unrelated worktree changes. Do not change database, route contracts, or generated references.

Smallest falsifiable check: Rendered About HTML contains an accessible system-map control set with expandable sections, and the focused test confirms the map's key stages and detail content are present without moving or breaking other tabs.

Acceptance criteria:

- About contains a professional, clean interactive system map covering source/staging, canonical records, processing/enrichment, APIs, research workflows, and evidence/provenance boundaries.
- Sections expand and collapse through accessible controls without requiring a framework or new backend endpoint.
- The map explains the site's function rather than only listing files, and includes concise details inside each expandable section.
- Existing Site Architecture content, tab navigation, live inventory loading, and other Data Explorer surfaces remain intact.
- Focused UI tests, Python diagnostics, whitespace validation, and a browser interaction check pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`

Rollback/recovery: Restore the About panel markup, CSS, JavaScript, and focused assertions; no database or migration rollback is required.

Evidence: Authority docs reviewed. Explore delegation inspected `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`; no files changed. `backend/pages/data_explorer.py` now renders `aboutSystemMap` with a visible six-stage workflow and six native `<details>` disclosures covering sources, canonical records, enrichment, services, research views, and evidence boundaries. `tests/test_feature_tabs.py` asserts the map structure. `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 19 tests. Bounded Playwright smoke check passed at 1280x900 and 390x844: map present, six disclosures, first open, second opens on click, and no horizontal overflow. VS Code diagnostics reported no errors in the touched Python files, and `git diff --check` passed.

## Hypothesis

If the About panel uses semantic disclosure controls organized around the actual source-to-research workflow, then users can understand the site's function by expanding only the parts they need while existing Data Explorer behavior remains unchanged.

## Plan

1. Delegate a bounded inspection of the About owner surface, nearby styles/scripts, and focused tests.
2. Implement the smallest accessible map with staged reveal, clear system layers, and responsive styling.
3. Run focused tests immediately, repair local failures, then perform a browser interaction and responsive check.
4. Update canonical UI/architecture documentation and the Active UI Swimm walkthrough.
5. Re-run final validation and commit/push the completed checkpoint.

## Execution Checkpoints

- Authority review: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, and `.swm/6.maiixtsw.sw.md` reviewed.
- Delegation: Explore agent inspected the owner surface and recommended native `<details>` disclosures; no files changed.
- Implementation: `backend/pages/data_explorer.py` and `tests/test_feature_tabs.py`; focused suite passed.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md` updated to describe the interactive map.
- Recovery: No long-running or destructive operation planned.

## Completion

Completion recorded: yes

Summary: Added and validated a polished interactive system map to the About tab.

Validation: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` passed with 19 tests; bounded Playwright browser check passed at desktop and mobile viewports; VS Code diagnostics reported no errors; `git diff --check` passed.

Residual risk: The map summarizes major user-visible stages rather than every repository file or endpoint; detailed table-level explanation remains in Site Architecture.

Next recommended task: After completion, review the map wording with a researcher and add any missing domain-specific workflow branch as a bounded follow-up.
