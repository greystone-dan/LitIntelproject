# Task: Audit and improve accessibility in research UI HTML

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Audit search, case reader, judge profile, and citation HTML builders against WCAG 2.1 AA; write `docs/reports/accessibility-audit.md` and make only clear, small accessibility fixes with focused tests.

Why now: The active research UI review backlog explicitly calls out tab semantics, focus treatment, input contrast, mobile fit, and keyboard interaction; a traceable audit can close obvious gaps without redesign.

Owner surface: Research UI HTML generation in `backend/pages/` and `backend/case_formatter.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: Current Data Explorer behavior and UI guide; existing page/formatter tests.

Risk boundary: No interaction redesign, broad style changes, behavior changes, or claims of complete WCAG conformance; preserve active `/data-explorer` workflow, evidence offsets, and unrelated work.

Smallest falsifiable check: Focused tests for audited HTML semantics plus `git diff --check`.

Acceptance criteria:

- Audit the named search, case reader, judge profile, and citation HTML builder surfaces against WCAG 2.1 AA and document findings, severity/impact, scope, and limitations.
- Add only clear, low-risk labels, alt text, ARIA attributes, or keyboard-visible focus treatments with focused test coverage.
- Update the canonical repository documentation and the relevant Swimm walkthrough in the same checkpoint.
- Run the focused tests and documentation/link/diff checks; scan changed files for secrets.

Harness criteria:

- Accessibility audit and findings are documented.
- Focused UI tests pass.
- Canonical and Swimm docs are updated and local links validated.

Docs/generated references: `docs/reports/accessibility-audit.md`; canonical `docs/RESEARCH_UI_GUIDE.md`; generated `SYSTEM_REFERENCE.md` UI appendix; `.swm/6.maiixtsw.sw.md`. No API/schema/script catalog changes.

Rollback/recovery: Revert only the isolated accessibility attribute/style and corresponding test changes; retain audit report and findings.

Evidence: Managed worker `formatter-a11y` inspected `backend/case_formatter.py` and `tests/test_case_formatter.py`, found no HTML to change, changed no files, and could not run tests before pytest was installed. Manager-side static generated-page checks found an unnamed Citation Map search input, insufficient focus styling, and CSS-only reader/Citation Map selected states; these were fixed and covered by builder assertions. `docs/RESEARCH_UI_GUIDE.md`, the selected generated UI appendix in `SYSTEM_REFERENCE.md`, and `.swm/6.maiixtsw.sw.md` document this work. `python scripts/check_generated_docs.py` was attempted but could not import missing `fastapi` and `sqlalchemy`; `test_feature_tabs.py` collection is blocked by missing `httpx`. The focused isolated suite and documentation link/diff checks passed. `engine-tools-report_progress` and `parallel_validation` were unavailable in this session; progress was reported in chat and validations were run directly.

Files changed: `backend/pages/data_explorer.py`, `backend/pages/citation_map.py`, `tests/test_accessibility_builders.py`, `docs/reports/accessibility-audit.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, `SYSTEM_REFERENCE.md`, task record.
Delegated work: Managed worker `formatter-a11y` inspected only `backend/case_formatter.py` and `tests/test_case_formatter.py`, found no HTML rendering to fix, changed no files, and could not run pytest (not installed in system Python).
Focused validation: `python -m pytest -q tests/test_accessibility_builders.py tests/test_case_formatter.py` — 9 passed; `python -m compileall -q backend/pages/data_explorer.py backend/pages/citation_map.py backend/pages/citation_pass.py backend/pages/live_analysis.py backend/pages/quick_search.py backend/case_formatter.py tests/test_accessibility_builders.py` — passed with the pre-existing invalid-escape warning; Swimm links and `git diff --check` passed.
Residual risk: Static HTML review and automated tests do not establish WCAG 2.1 AA conformance. Browser, keyboard, contrast, and assistive-technology checks were not run. The Citation Map graph has only a generic image name; its dynamic textual equivalent is unverified.
Next bounded task: Browser keyboard and screen-reader review of Data Explorer search/reader and Citation Map at desktop and narrow viewports.

## Hypothesis

If the scoped builders expose programmatic names and selected states and provide visible keyboard focus where missing, focused HTML tests will demonstrate those semantics without changing search, reader, profile, or citation behavior.

## Plan

1. Delegate a bounded audit/implementation slice for `backend/case_formatter.py` before manager-side discovery of the same targets.
2. Audit page builders and tests; implement only clear fixes and verify each owned slice.
3. Produce the requested audit report and update canonical documentation and the active UI Swimm walkthrough; run focused validation and final acceptance checks.

## Execution Checkpoints

- Delegation: `formatter-a11y` returned the required structured report; no safe formatter fix was found.
- Implementation: `backend/pages/data_explorer.py`, `backend/pages/citation_map.py`; focused builder and formatter tests passed.
- Documentation: `docs/reports/accessibility-audit.md`, `docs/RESEARCH_UI_GUIDE.md`, selected generated `SYSTEM_REFERENCE.md` appendix, and `.swm/6.maiixtsw.sw.md` updated; local Swimm links resolve.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created | User requested a bounded WCAG 2.1 AA audit and surgical fixes across named research UI builders. | `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.swm/` UI walkthrough |

## Completion

Completion recorded: yes

Summary: Completed the static audit and surgical accessibility fixes in active search, reader, judge-profile, and citation UI markup. No HTML fix was applicable to the text/offset formatter.

Validation: `python -m pytest -q tests/test_accessibility_builders.py tests/test_case_formatter.py` — 9 passed; audited modules compiled; local links, secret-pattern scan, and `git diff --check` passed. Generic generated-doc check and broader feature-tab tests were attempted but blocked by missing `fastapi`, `sqlalchemy`, and `httpx`.

Residual risk: No browser, manual keyboard, screen-reader, contrast, responsive, or touch-target validation; full WCAG conformance is not claimed. Citation Map's graph alternative remains unverified.

Next recommended task: Browser keyboard and screen-reader review of Data Explorer search/reader and Citation Map at desktop and narrow viewports.
