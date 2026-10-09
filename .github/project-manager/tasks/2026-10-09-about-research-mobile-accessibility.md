# Task: Audit About and Research mobile accessibility

Status: blocked
Created: 2026-10-09
Updated: 2026-10-09

## Task Record

Task: Audit and surgically improve About and Research views at 360px and 390px, covering responsive layout and accessibility.

Why now: Issue #431 identifies narrow-screen and accessibility defects in active research views.

Owner surface: `backend/pages/data_explorer.py` and its focused UI contract tests in `tests/test_feature_tabs.py`.

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
- About and Research affordances/layout are corrected for narrow 360px and 390px widths without horizontal overflow in covered surfaces.
- Focused UI contract tests pass and continue to assert tab-click reset behavior.
- Required documentation and final requested checks are recorded.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`; `.swm/6.maiixtsw.sw.md`; run `python scripts/check_generated_docs.py` without hand-editing generated references.

Rollback/recovery: Revert only this task's page-builder, test, and documentation hunks; no data or external state is involved.

Evidence: Required docs read before changes: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.swm/6.maiixtsw.sw.md`, and `docs/RESEARCH_UI_GUIDE.md`. Managed worker returned structured evidence; manager removed first-pass Site Architecture/Research Bench changes as outside active About/Research. Updated canonical `docs/RESEARCH_UI_GUIDE.md` and Swimm walkthrough `.swm/6.maiixtsw.sw.md`. `python -m py_compile backend/pages/data_explorer.py tests/test_feature_tabs.py` passed (existing invalid-escape `SyntaxWarning` emitted at page-builder line 36); `git diff --check` passed; changed-file secret-pattern scan passed. `python -m pytest tests/test_feature_tabs.py -q` could not start (`No module named pytest`). `python scripts/check_generated_docs.py` failed because required `fastapi` and `sqlalchemy` modules are unavailable. No browser test, live site, or database was used. Blocked pending an environment with project dependencies for focused test and generated-doc check.

Files changed: `backend/pages/data_explorer.py`, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`, this task record.
Delegated work: Managed worker `about-research-ui` inspected the builder/tests and supplied a static audit/fix pass; out-of-scope Research Bench/Site Architecture edits were removed. Manager owns final scope refinement, docs, and validation.
Focused validation: `python -m py_compile backend/pages/data_explorer.py tests/test_feature_tabs.py` passed with the noted warning; focused pytest and generated-doc checks were attempted but blocked by unavailable dependencies. Secret scan and `git diff --check` passed.
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

Summary: Code/test/documentation slice implemented, but completion is blocked on focused-test and generated-document checks in an environment missing project dependencies.

Validation: `py_compile`, changed-file secret scan, and `git diff --check` passed. Pytest and generated-doc check were attempted and failed to start due to missing `pytest`, `fastapi`, and `sqlalchemy`.

Residual risk: No browser/device or screen-reader audit was performed.

Next recommended task: Rerun the exact blocked checks with project dependencies installed.
