# Task: Group the research site's primary navigation

Status: complete
Created: 2026-09-30
Updated: 2026-09-30

## Task Record

Task: Replace the right-aligned mixed header links with left-aligned Info, Research, Workbench and Testing navigation groups.
Why now: User wants predictable main navigation and separation of work-in-progress features.
Owner surface: `backend/pages/data_explorer.py`.
Commit allowed: no
Push allowed: no
Dependencies: Existing generated HTML, inline tab handlers, `tests/test_feature_tabs.py`, running local site on port 8001.
Risk boundary: Preserve existing endpoints, reader behavior, deep links, backend offsets and active embedding writer. No data changes, route/schema changes, unrelated layout overhaul or prototype promotion. No server restart that touches the embedding process.
Smallest falsifiable check: `venv/Scripts/python.exe -m pytest tests/test_feature_tabs.py -q` plus generated-script/browser checks.
Acceptance criteria:
- Four left-aligned primary groups with accessible active state and keyboard activation.
- Info owns About/Architecture; Research owns existing research views; Workbench owns stable tools; Testing owns sandbox/QA and prototype Research Bench.
- Research remains default and existing `?tab=`/reader deep links select the proper group.
- Desktop/mobile navigation has no overlap; existing features remain reachable.
- Focused tests, compilation and browser validation pass; canonical docs and Swimm updated.
Harness criteria: Group navigation; preserved reader/deep links; responsive browser validation.
Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, relevant research-interface `.swm/` walkthrough.
Rollback/recovery: Revert only this task's navigation changes if checks fail; leave all unrelated work and running processes intact.
Evidence: After two delegation failures, bounded recovery found grouped navigation, regression tests, and matching docs already present in the workspace. Preserved and validated those changes instead of replacing them. Live updated HTML served at `http://127.0.0.1:8002/data-explorer`; existing port 8001 served older HTML. The new server does not restart or touch the active embedding writer.
Files changed: This task record; acceptance evidence in `docs/RESEARCH_UI_GUIDE.md` and `.swm/6.maiixtsw.sw.md`. Existing builder, tests, and `SYSTEM_REFERENCE.md` navigation changes preserved and verified.
Delegated work: Two bounded worker attempts failed with upstream HTTP 404 download errors and no structured return. Exception: manager performed bounded recovery and final acceptance; no claim of successful worker implementation.
Focused validation: `venv/Scripts/python.exe -m pytest tests/test_feature_tabs.py -q` passed 48 tests, including the final rerun. `venv/Scripts/python.exe -m py_compile backend/pages/data_explorer.py` passed. Live Playwright passed at 1440x1000 and 390x844: group visibility, default Research, legacy deep links, arrow-key focus/Enter activation, button non-overlap, no horizontal overflow, and no uncaught page errors. Screenshots: `data/copilot_review/primary-navigation-groups/desktop-research.png` and `mobile-research.png`. Editor diagnostics found no errors in the builder or tests. Scoped `git diff --check` passed and all local checkpoint references exist. Updated canonical document: `docs/RESEARCH_UI_GUIDE.md`; updated Swimm: `.swm/6.maiixtsw.sw.md`.
Residual risk: Existing Python invalid-escape and pypdf ARC4 warnings remain. `venv/Scripts/python.exe scripts/check_generated_docs.py` failed on previously known drift in `docs/API_REFERENCE.generated.md` and `docs/SCRIPT_CATALOG.generated.md`; generated files were not edited in this task. Navigation checks do not certify research-result accuracy or every standalone tool workflow. The old server on port 8001 remains unchanged. No full suite, data migration, or embedding completion claimed.
Next bounded task: User review of group placement on the updated site; no additional implementation scope opened.

## Hypothesis

If one group-to-view map owns primary and secondary selection while reusing the current tab controller, four left-aligned groups can organize the UI without breaking existing deep links or reader workflows.

## Plan

1. Worker implements grouping in builder and extends existing feature-tab checks.
2. Manager verifies focused tests and live browser navigation on desktop/mobile.
3. Save canonical docs, Swimm and evidence checkpoint without touching the embedding writer.

## Execution Checkpoints

- Existing right-header links: Research, Sandbox, Citation Map, Live Analysis, Case Reader.
- Initial proposed grouping is conservative: prototype Research Bench remains Testing, not promoted into Workbench functionality.

## Completion

Completion recorded: yes
Summary: Four top-left groups are serving on port 8002; grouped navigation, responsive acceptance, canonical documentation, and Swimm checkpoint are complete.
Validation: 48 focused tests, compilation, live desktop/mobile checks, editor diagnostics, local-reference checks, and scoped whitespace validation passed. Generated-document drift remains unrelated and explicitly recorded.
Residual risk: See task record.
Next recommended task: Review group placement on the updated local site.