# Task: Review Data Explorer visual and access quality

Status: complete
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Review the active Data Explorer website for visual defects, accessibility issues, responsive behavior, loading/error states, and current-data presentation; produce a prioritized improvement backlog.

Why now: The main reader/search workflow is functional after the V2 regression fixes, and the next product risk is usability and trust across desktop/mobile/research workflows before statutes and tagging work expands.

Owner surface: `backend/pages/data_explorer.py` active Data Explorer UI and its existing browser/API smoke contract

Commit allowed: yes

Push allowed: yes

Dependencies: Local refreshed site, PostgreSQL-backed current API, `scripts/browser_smoke.py`, `tests/test_feature_tabs.py`, `tests/test_api.py`, and UI guide.

Risk boundary: Review-first. Do not alter canonical data, citation/statute/tag processing, access/security posture, or unrelated legacy pages. Any immediate fix must be a clearly demonstrated critical UI/accessibility defect.

Smallest falsifiable check: Bounded browser review at desktop `1440x1000`, mobile `390x844`, and keyboard/semantic checks against the active Data Explorer; run existing browser smoke and focused UI/API tests.

Acceptance criteria:

- Desktop, mobile, keyboard, loading, empty, and error states are reviewed.
- Visual/accessibility findings are grounded in concrete routes/selectors/behaviors.
- Findings are ranked by severity, user impact, confidence, and implementation effort.
- Current-data/staleness risks are distinguished from cosmetic issues.
- A bounded backlog with acceptance checks is recorded in task evidence and canonical/Swimm docs.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Review-only by default. Revert any critical UI fix independently; no database recovery required.

Evidence: Delegated read-only review inspected the active Data Explorer page, routes, browser smoke, focused tests, and UI guide. No files changed and no database writes ran. Existing acceptance remained green: focused UI/API suite `56 passed`; browser smoke passed for Vavilov search, case opening, reader tabs, tags, layer legend, and mobile Themes.

Ranked findings:

- P1 accessibility: top-level `[data-tab]` buttons do not expose `aria-selected`; add active-state semantics and keyboard tab behavior.
- P1 accessibility: reader pane splitters have `role=separator` and `tabindex` but lack a visible focus style and keyboard resize behavior.
- P1 accessibility: search focus outline uses low-opacity color and needs a stronger contrast-verified focus treatment.
- P2 responsive: reader info tabs use dense five-column desktop and two-column mobile grids; measure 44px touch targets and label fit at 390px.
- P2 responsive: top-level tab overflow behavior needs explicit screenshot acceptance at desktop widths.
- P2 interaction: evidence detail positioning and Citation Intelligence chart sizing need runtime overlap/reflow checks.
- P3 maintainability: generated page still contains historical reader render wrappers; task 089 added a dispatcher boundary, but full consolidation should follow visual regression coverage.

Uncertainty: the P1/P2 visual/accessibility findings were static review findings; no assistive-technology run or screenshot pixel audit was completed in this checkpoint. No critical functional failure was found in the bounded smoke path.

## Hypothesis

If the active Data Explorer is reviewed across its primary desktop/mobile journeys and states, the highest-value next work will cluster around a small number of concrete accessibility, responsive, loading, and evidence-presentation defects rather than broad redesign.

## Plan

1. Delegate bounded browser/accessibility/visual inventory.
2. Consume structured findings and rank improvements by severity, value, effort, and risk.
3. Implement only an urgent defect if acceptance is clear; otherwise record backlog.
4. Validate and update canonical/Swimm documentation.

## Execution Checkpoints

- Delegation: pending read-only visual/accessibility review.
- Implementation: manager-owned only if an urgent defect is confirmed.
- Documentation: canonical UI guide/system reference and Swimm walkthrough.
- Recovery: local server/browser only; no database writer.

## Completion

Completion recorded: yes

Summary: Completed a bounded visual/accessibility review of the active Data Explorer and recorded a ranked backlog. Functional browser smoke and focused tests remain green.

Validation: `pytest tests/test_feature_tabs.py tests/test_api.py -q` -> `56 passed`; browser smoke passed. Static review findings recorded above.

Residual risk: Automated browser checks cannot fully replace human visual judgment or assistive-technology testing. Accessibility fixes need keyboard/screenshot acceptance before broad UI claims.

Next recommended task: Fix P1 keyboard semantics/focus treatment, then add desktop/mobile screenshot and keyboard checks before further visual redesign.
