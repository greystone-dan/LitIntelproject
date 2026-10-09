# Task: Audit About and Research mobile accessibility

Status: blocked
Created: 2026-10-09
Updated: 2026-10-09

## Task Record

Task: Audit and surgically improve About and Research views at 360px and 390px, covering responsive layout and accessibility.

Why now: Issue #431 identifies narrow-screen and accessibility defects in active research views.

Owner surface: active About and Case Search builder/styles plus the standalone Research and Quick Search builders; focused UI contract tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing Data Explorer navigation and About/Research page builder.

Risk boundary: Preserve tab-click resets-page behavior. Do not access a database or live site. Do not touch `site_tour*` or `coming_soon_*` files.

Smallest falsifiable check: `python -m pytest tests/test_feature_tabs.py -q`

Acceptance criteria:

- Focused tests cover the identified mobile/accessibility behavior for About and Research.
- Fixes are surgical and do not alter the established tab activation/reset behavior.
- Generated-document check and secret scan pass before commit.
- Canonical Research UI guidance and Active Research UI Swimm walkthrough are updated.

Harness criteria:
- About and Research affordances/layout have static contracts for narrow 360px and 390px widths; browser-rendered overflow remains unverified.
- Focused UI contract tests pass and continue to assert tab-click reset behavior.
- Required documentation and final requested checks are recorded.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`; `.swm/6.maiixtsw.sw.md`; run `python scripts/check_generated_docs.py` without hand-editing generated references.

Rollback/recovery: Revert only this task's page-builder, test, and documentation hunks; no data or external state is involved.

Evidence: Required docs read before changes: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.swm/6.maiixtsw.sw.md`, and `docs/RESEARCH_UI_GUIDE.md`. Managed worker returned structured evidence; manager removed first-pass Site Architecture/Research Bench changes as outside active About/Research. Static inspection found mobile Research tabs forced into a horizontal row and multiple search/changelog controls below 44px. The current change wraps tabs, raises the relevant touch targets, adds visible focus and landmarks to standalone search builders, and makes Quick Search status changes a polite live status. About diagrams have accessible labels and local scroll wrappers; no defects found in their static markup. Updated canonical `docs/RESEARCH_UI_GUIDE.md` and Swimm walkthrough `.swm/6.maiixtsw.sw.md`. The initial builder compile and `git diff --check` passed; initial secret scan passed. `python -m pytest tests/test_feature_tabs.py -q` could not start (`No module named pytest`). `python scripts/check_generated_docs.py` failed because required `fastapi` and `sqlalchemy` modules are unavailable. No browser test, live site, or database was used. Current focused checks and generated-doc check remain unrun in this environment.

Files changed: `backend/pages/data_explorer.py`, `backend/pages/about_how.html`, `backend/pages/changelog_tab.py`, `backend/pages/mobile_layout.css`, `backend/pages/quick_search.py`, `backend/pages/research.py`, `tests/test_feature_tabs.py`, `tests/test_accessibility_builders.py`, `tests/test_changelog.py`, `tests/test_mobile_layout.py`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, this task record.
Delegated work: Managed worker `about-research-ui` inspected the builder/tests and supplied a static audit/fix pass; out-of-scope Research Bench/Site Architecture edits were removed. Manager owns final scope refinement, docs, and validation.
Focused validation: The initial builder compilation passed with the noted warning; focused pytest and generated-doc checks are blocked by missing `pytest`, `fastapi`, and `sqlalchemy`. Static inspection and `git diff --check` are complete; the new code/test edits have not been executed.
Residual risk: Focused tests and generated-doc consistency remain unverified until dependencies are installed; viewport assertions are static CSS/markup contracts, not browser/device or screen-reader validation. No live site/database was used.
Next bounded task: Rerun the focused UI test and generated-document check in an environment with project dependencies.

## Hypothesis

If About and Research layout/semantics are corrected without changing navigation state transitions, the focused feature-tab tests will prove the narrow UI contracts and preserve tab-click resets-page behavior.

## Plan

1. Delegate bounded inspection and implementation of About/Research page markup/styles and tests.
2. Manager reviews the diff, updates canonical UI guidance and the linked Swimm walkthrough.
3. Run focused UI tests, generated-document check, secret scan, and diff checks before deciding on commit.

## Execution Checkpoints

- Delegation: Managed worker `about-research-ui`; structured response received.
- Implementation: About summary inventory now has polite atomic status semantics; feature tests target the About and Case Search surfaces. Unrelated Site Architecture/Research Bench changes removed.
- Documentation: Updated `docs/RESEARCH_UI_GUIDE.md` and `.swm/6.maiixtsw.sw.md`.
- Recovery: No external or persistent operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-09 | Selected embedded Data Explorer page builder as owner | `SYSTEM_REFERENCE.md`, UI guide, tests, and Swimm map identify this as the active About/Research surface | Read `SYSTEM_REFERENCE.md` lines 68-95; `DOCS_INDEX.md`; `.swm/6.maiixtsw.sw.md`; `docs/RESEARCH_UI_GUIDE.md` |
| 2026-10-09 | Kept Research Bench and Site Architecture work out of scope | System documentation defines Case Search as the default Research view; the worker's first pass targeted Testing and a separate architecture panel | Reviewed delegated diff against `SYSTEM_REFERENCE.md` lines 72-85 and `docs/RESEARCH_UI_GUIDE.md` lines 61-86 |

## Completion

Completion recorded: no

Summary: Code/test/documentation changes implement the static mobile/accessibility fixes. Completion remains blocked on focused tests and generated-document verification in an environment missing project dependencies, and on browser-rendered checks.

Validation: An initial `py_compile`, changed-file secret scan, and `git diff --check` passed. Pytest and generated-doc check were attempted and failed to start due to missing `pytest`, `fastapi`, and `sqlalchemy`; later edits have not been run through those checks.

Residual risk: No browser/device reflow, no-horizontal-scroll, touch-size, keyboard-only, screen-reader, or comprehensive contrast measurement was performed. The CSS tests are static contracts only.

Next recommended task: Rerun the exact blocked checks with project dependencies installed.
