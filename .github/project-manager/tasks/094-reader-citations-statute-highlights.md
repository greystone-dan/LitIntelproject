# Task: Repair reader citations subtab and statute highlights

Status: in-progress
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Fix the active reader's Citations subtab and statute/law highlighting for Suresh v Canada in Full text mode.

Why now: User reports that the Citations subtab renders no content and laws are not highlighted when viewing Suresh v Canada, despite persisted citation/statute data.

Owner surface: `backend/pages/data_explorer.py` reader renderers plus persisted reader-data contract

Commit allowed: yes

Push allowed: yes

Dependencies: Tasks 085, 087, 088, 092, 093; active API/UI tests and browser smoke.

Risk boundary: Display/API contract only. Do not change extraction, resolution, statute rows, tags, offsets, or database data. Preserve persisted-only reader behavior and explicit search.

Smallest falsifiable check: Live Suresh reader probe counts stored citation/statute rows and DOM highlights/tabs in Full text mode; focused UI/API tests and browser smoke must pass.

Acceptance criteria:

- Citations subtab displays persisted case-citation rows for a selected case.
- Full text mode highlights persisted citation/statute rows using backend-owned offsets.
- Suresh v Canada displays law/statute highlights when persisted statute rows exist.
- No reader-time extraction or HTML source rescanning returns.
- Tests/browser smoke pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Revert only reader renderer/API projection changes if focused/browser validation fails. No database rollback required.

Evidence: Live Suresh inventory found persisted case citations and statute-reference rows with backend offsets. The real browser journey initially showed an empty Citations tab and no law marks because lazy statute rows were not merged into `readerData.citations` used by the renderer. Fixed the reader state merge and rerender path. Final Playwright probe: Suresh Full text shows `61` law highlights and `180` total marks; Citations tab shows `35` citation groups. Focused API/UI suite passed (`56 passed`). The selected chunk-mode renderer still needs a separate projection cleanup; persisted rows and Full text behavior are correct.

## Hypothesis

If the Citations tab is wired to the final active reader renderer and Full text uses the persisted reader-data citation/statute arrays with valid document offsets, the Suresh reader will show citations and law highlights without extraction.

## Plan

1. Delegate bounded live Suresh DOM/API diagnosis.
2. Fix the active renderer/projection path.
3. Run focused tests and browser smoke, then document and commit.

## Completion

Completion recorded: yes

Summary: Fixed empty Citations tab and missing Suresh law highlights by merging lazy persisted statute rows into the canonical reader state and renderer payload.

Validation: `pytest tests/test_feature_tabs.py tests/test_api.py -q` -> `56 passed`; Playwright Suresh probe -> `61` law marks, `180` full-text marks, `35` citation groups.

Residual risk: Chunk mode still reports zero visible citation/law marks for this Suresh case despite API rows being projected to paragraph chunks; this is a separate renderer issue for the next task. Full text and Citations tab are fixed.

Next recommended task: Refactor/test the active chunk renderer so projected paragraph-layer rows render visibly, then add a Suresh browser fixture.
