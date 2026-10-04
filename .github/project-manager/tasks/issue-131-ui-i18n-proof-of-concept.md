# Task: UI string inventory and French i18n proof of concept

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Inventory user-facing UI strings with human-readable and JSON reports, and demonstrate French localization on one page.

Why now: Issue #131 requests an evidence-backed inventory and a deliberately narrow localization proof of concept before any broader translation effort.

Owner surface: Generated research UI localization and string-inventory tooling.

Commit allowed: yes

Push allowed: yes

Dependencies: Active UI builders in `backend/pages/` and `backend/routes.py`; current UI tests and documentation.

Risk boundary: Keep localization limited to About unless an existing `/start` page is found; preserve default English behavior, routes, stored data, and evidence offsets. No database, deployment, or `.env` access.

Smallest falsifiable check: `python -m pytest tests/test_ui_string_inventory.py tests/test_feature_tabs.py -q`

Acceptance criteria:

- A reproducible inventory reports user-facing UI strings in both a readable report and JSON, with its source scope and limitations stated.
- A single-page French proof of concept is available on About (or `/start` only if that route already exists), while English remains the default.
- Focused tests cover inventory output and localization behavior without database access.
- `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and the Active Research UI Swimm walkthrough document the implemented behavior and its limits.
- Focused validation, prescribed full tests, generated-document check, changed-file secret scan, and `parallel_validation` are reported accurately.

Harness criteria:
- UI inventory has a reproducible JSON and readable report.
- French proof of concept is restricted to one page and preserves English default behavior.
- Required documentation and Swimm walkthrough are updated.
- Required validation commands and safety checks are recorded.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`; generated inventory report/JSON must come from its generator.

Rollback/recovery: Revert the bounded UI localization and inventory-tool changes together; no database or deployment state is involved.

Evidence: The worktree was clean at task start. GitHub CLI could not retrieve issue #131 because this environment has no `GH_TOKEN`; scope is taken from the user's request. Managed worker `issue-131-ui-i18n` confirmed `/start` is absent, implemented the bounded inventory and About preview, added focused tests, and updated the canonical docs and Swimm map. Manager review corrected a documentation mismatch so the About architecture graph/pipeline and Site Architecture inventory are described according to the builder. Direct invocation of all five new test assertions passed; `python scripts/generate_ui_string_inventory.py --check`, Python compilation, JavaScript syntax checking, Chromium interaction, `git diff --check`, changed-link review, and the changed-file secret-pattern scan passed. Headless Chromium verified six About toggle assertions (French title/lang/pressed state and English restoration). `python -m pytest -q` and the focused pytest command could not run because pytest is absent. `python scripts/check_generated_docs.py` could not complete because FastAPI and SQLAlchemy are absent; after it identified the new script catalog entry as stale, `python scripts/generate_script_catalog.py` regenerated that output. The required standalone `parallel_validation` command/tool is not available; independent checks were executed through `multi_tool_use.parallel`. Canonical docs updated: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`; Swimm walkthrough updated: `.swm/6.maiixtsw.sw.md`.

Files changed: `.github/project-manager/tasks/issue-131-ui-i18n-proof-of-concept.md`, `backend/pages/about_content.html`, `scripts/generate_ui_string_inventory.py`, `tests/test_ui_string_inventory.py`, `docs/UI_STRING_INVENTORY.generated.md`, `docs/UI_STRING_INVENTORY.generated.json`, `docs/SCRIPT_CATALOG.generated.md`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`
Delegated work: Managed worker `issue-131-ui-i18n` implemented the static inventory generator/report/JSON, About language preview, focused tests, and UI documentation. It reported a direct assertion runner with five passes, inventory staleness check, compilation, Node syntax, and whitespace check; its pytest attempt was blocked by missing pytest. Manager corrected the docs to reflect the actual About graph/pipeline placement.
Focused validation: Passed direct invocation of all five tests in `tests/test_ui_string_inventory.py`; `python scripts/generate_ui_string_inventory.py --check`; `python -m py_compile scripts/generate_ui_string_inventory.py backend/pages/data_explorer.py`; `git diff --check`; and a headless Chromium check with six language-toggle assertions. `python -m pytest tests/test_ui_string_inventory.py tests/test_feature_tabs.py -q` and `python -m pytest -q` were attempted but blocked (`No module named pytest`). `python scripts/check_generated_docs.py` was attempted and blocked because FastAPI and SQLAlchemy are absent; `docs/SCRIPT_CATALOG.generated.md` was regenerated by `python scripts/generate_script_catalog.py`. Independent validation calls ran via `multi_tool_use.parallel`; no standalone `parallel_validation` tool/command was exposed.
Residual risk: Full pytest suite, feature-tab pytest coverage, and API/schema generated-doc check remain unverified because dependencies are unavailable. Browser verification covered the About toggle only, not general responsive/accessibility behavior. The string inventory is static source coverage, not runtime-complete. French preview is intentionally limited to the About overview summary and section links, not the whole app. The exact issue body could not be fetched through GitHub CLI.
Next bounded task: In an environment with pytest, FastAPI, SQLAlchemy, and browser tooling installed, run the prescribed full suite, generated-doc check, and About interaction smoke check before merge.

## Hypothesis

If the inventory and single-page language switch are implemented without changing the existing English default, focused tests will verify deterministic report/JSON output, the French About content, and unchanged navigation behavior.

## Plan

1. Inventory the active UI string sources and choose a reproducible report format.
2. Add the bounded About French localization proof of concept and focused tests.
3. Update the canonical UI docs and Swimm walkthrough, then run focused and required repository checks.

## Execution Checkpoints

- Delegation: Managed worker `issue-131-ui-i18n` implemented inventory, About language preview, and focused tests; manager accepted the bounded slice and corrected a documentation placement error.
- Implementation: Added deterministic static HTML/UI-attribute inventory generation, checked-in Markdown and JSON outputs, French/English About controls, and five focused assertion tests.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`; regenerated `docs/SCRIPT_CATALOG.generated.md`.
- Recovery: No persistent data or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use About as the proof-of-concept page | No `/start` route exists; About is the requested fallback. Translations stay limited to the overview summary and section links | `backend/routes.py`; `backend/pages/data_explorer.py` |
| 2026-10-04 | Keep task blocked pending prescribed environment checks | Test runner and generated-doc dependencies are missing, preventing the requested broad checks | `python -m pytest -q`; `python scripts/check_generated_docs.py` |

## Completion

Completion recorded: no

Summary: Implementation and required documentation are present; validation is blocked by missing test and generated-document dependencies.

Validation: Five focused assertion functions and six browser toggle assertions passed; the UI inventory generator check passed. Full pytest and API/schema generated-document checks were attempted and blocked by missing dependencies.

Residual risk: Browser interaction received a bounded check; broad pytest and API/schema generated-doc checks remain blocked; see Evidence.

Next recommended task: Run the blocked acceptance checks in a correctly provisioned test environment.
