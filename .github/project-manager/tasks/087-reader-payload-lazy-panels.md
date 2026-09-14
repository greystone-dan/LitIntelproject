# Task: Reduce reader payload and lazy-load secondary panels

Status: complete
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Improve the active reader after the persisted-only fix by reducing initial payload size and deferring secondary intelligence panels without changing citation/statute/tag data.

Why now: Vavilov now opens correctly, but its persisted reader payload is approximately 3 MB with 975 citation rows. The basic case view should become visible quickly; Intel, Activity, linked authority context, and large citation detail can load on demand.

Owner surface: `backend/pages/data_explorer.py`, `backend/reader_service.py`, `backend/routes.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Completed task 085, active Data Explorer reader contract, API tests, browser smoke, and current persisted citation/chunk data.

Risk boundary: No database writes, extraction, resolution, statute, or tag changes. Preserve current reader tabs and persisted evidence semantics. Do not remove data; only change initial transport/render timing or bounded endpoint payloads.

Smallest falsifiable check: Browser smoke remains green after the initial reader payload is reduced or secondary panel loading is deferred; focused API tests cover the changed contract.

Acceptance criteria:

- Initial case open remains functional and displays title, stored text/chunks, and primary persisted citation evidence.
- Secondary intelligence/activity/linked-context work is deferred or bounded.
- Browser smoke and focused API/UI tests pass.
- Payload/timing improvement is measured against the Vavilov baseline.
- Canonical and Swimm documentation record the new reader loading contract.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Revert only the reader transport/render changes if browser/API acceptance fails. No database recovery is required.

Evidence: Baseline from task 085 was approximately 3.59 seconds direct build and 2.96 MB HTTP payload for Vavilov. The delegated audit identified statute rows as safe to defer because the initial reader smoke contract only requires case metadata, chunks, case citations, and tabs; Acts/Regs already behaves as a secondary tab. Added a persisted `/cases/{case_id}/statute-references` endpoint and lazy Acts/Regs fetch, removing statute rows from the initial reader response. Final Vavilov measurements: `3.88s`, `2.07 MB` initial reader response, `101 KB` statute endpoint. API/UI suite passed (`56 passed`), and browser smoke passed with all reader tabs, tags, legend, and mobile Themes.

## Hypothesis

If secondary panels and oversized citation detail are deferred while primary persisted reader data remains, Vavilov’s initial case-open response and browser-visible reader will become materially smaller/faster without changing evidence correctness.

## Plan

1. Delegate a bounded read-only audit of reader payload fields, tab behavior, and existing endpoints suitable for lazy loading.
2. Choose and implement one compatible payload/loading slice.
3. Run focused tests and browser smoke, measure before/after, and update docs.

## Execution Checkpoints

- Delegation: pending bounded UI/API payload audit; worker cannot edit task records or commit.
- Implementation: manager-owned reader/API/page changes only.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`.
- Recovery: no database writer; local server restart only.

## Completion

Completion recorded: yes

Summary: Deferred statute references from the initial reader payload and lazy-loaded them only when Acts / Regs is opened.

Validation: `pytest tests/test_feature_tabs.py tests/test_api.py -q` -> `56 passed`; initial reader `2.07 MB / 3.88s`; statute endpoint `101 KB`; browser smoke passed.

Residual risk: Intel, Activity, and linked-authority context remain candidates for later lazy loading. The current change preserves the existing reader tabs and does not alter stored evidence.

Next recommended task: Lazy-load Intel and Activity panels with explicit per-tab endpoints while keeping the initial case reader persisted-only.
