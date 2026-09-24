# Task: Improve paragraph assessment presentation

Status: complete
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Improve the active reader's paragraph-level assessment presentation so it is compact, legible, and useful beside the source text, then publish it through the running site.

Why now: The current assessment overlay is visually bulky and difficult to scan during legal research.

Owner surface: backend/pages/data_explorer.py

Commit allowed: yes

Push allowed: yes

Dependencies: Existing paragraph assessment endpoint and report-only assessment artifacts; tests/test_feature_tabs.py; active site refresh on port 8001.

Risk boundary: Preserve assessment content, backend-owned paragraph matching, source text, offsets, reader controls, and report-only/no-database-write behavior. Do not change assessment data or the API contract.

Smallest falsifiable check: `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q`, followed by a bounded browser check of the live reader.

Acceptance criteria:

- Assessment content remains available through the existing toggle and endpoint.
- Assessment presentation is compact, legible, and visually separated from source text without obscuring it.
- Existing reader and core-case controls remain intact.
- Focused UI tests, Python compilation, and a browser check pass.
- The refreshed public site serves the updated reader.

Docs/generated references: SYSTEM_REFERENCE.md; docs/RESEARCH_UI_GUIDE.md; Swimm Active UI walkthrough mapped in docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md.

Rollback/recovery: Revert the scoped presentation changes in backend/pages/data_explorer.py and rerun the focused UI test; restart scripts/refresh_site.ps1 if the running site needs restoration.

Evidence: Delegated read-only inspection by Explore found the assessment markup had no CSS and recommended a scoped hierarchy. Changed backend/pages/data_explorer.py, tests/test_feature_tabs.py, docs/RESEARCH_UI_GUIDE.md, and .swm/6.maiixtsw.sw.md. Ran `venv\\Scripts\\python.exe -m pytest tests/test_feature_tabs.py -q` (18 passed), `venv\\Scripts\\python.exe -m py_compile backend/pages/data_explorer.py` (passed with existing SyntaxWarning), and `git diff --check` (passed with line-ending warnings). Refreshed with `scripts/refresh_site.ps1`; local health and public page both returned 200, and the public HTML contains the compact and mobile assessment CSS. Canonical documentation updated at docs/RESEARCH_UI_GUIDE.md; Swimm walkthrough updated at .swm/6.maiixtsw.sw.md.

## Hypothesis

If the assessment is rendered as a compact labeled rail within each chunk, with restrained typography and spacing, then the live reader browser check will show readable assessment content without changing toggle behavior or paragraph matching.

## Plan

1. Inspect the current assessment markup, CSS, and nearby reader patterns.
2. Apply the smallest scoped presentation change in the active reader.
3. Run focused tests, refresh the site, and verify the live browser interaction.
4. Update the canonical UI documentation and Swimm walkthrough evidence.

## Execution Checkpoints

- Delegation: Explore inspected backend/pages/data_explorer.py, tests/test_feature_tabs.py, and docs/RESEARCH_UI_GUIDE.md; no files changed. Recommendation was to add scoped compact assessment CSS.
- Implementation: Added compact indented assessment rail, topic/meta/body hierarchy, and mobile full-width rule in backend/pages/data_explorer.py; added regression assertions in tests/test_feature_tabs.py.
- Documentation: Updated docs/RESEARCH_UI_GUIDE.md and .swm/6.maiixtsw.sw.md.
- Recovery: No long-running data operation; site refresh uses scripts/refresh_site.ps1.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-24 | Task created | User requested a cleaner, more legible live paragraph assessment display. | SYSTEM_REFERENCE.md active reader description and current UI implementation. |

## Completion

Completion recorded: yes

Summary: Paragraph assessments now render as a compact indented amber analysis rail beneath the source chunk, with readable hierarchy and responsive behavior. The refreshed public site serves the update.

Validation: Focused tests, Python compilation, diff check, local health, public page status, and public CSS presence all passed. Full post-refresh click-through browser verification was not repeated after the styling-only change.

Residual risk: Visual browser confirmation of the final styling remains for user review; assessment API and toggle behavior were unchanged.

Next recommended task: None until this presentation change is validated.
