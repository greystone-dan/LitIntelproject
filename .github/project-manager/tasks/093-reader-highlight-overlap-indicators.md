# Task: Add reader highlight overlap indicators

Status: in-progress
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Make overlapping persisted reader evidence visible instead of silently dropping lower-priority ranges.

Why now: The reader highlight review found that overlapping citation/statute ranges are skipped by `start < cursor` precedence without any user signal. Styling was simplified in task 092, but overlap semantics remain opaque.

Owner surface: `backend/pages/data_explorer.py` active reader highlight renderer and evidence detail UI

Commit allowed: yes

Push allowed: yes

Dependencies: Tasks 088 and 092, persisted reader citation/tag offsets, browser smoke.

Risk boundary: Display-only. Do not change stored offsets, target resolution, extraction, or citation/statute/tag data. Preserve links, mobile behavior, and current selectors.

Smallest falsifiable check: Focused API/UI suite plus browser smoke; renderer assertion that overlapping ranges add an explicit evidence marker without nested marks.

Acceptance criteria:

- Overlap handling remains deterministic and offset-preserving.
- A skipped/covered range is surfaced through evidence details or a visible non-destructive marker.
- No nested highlight marks are introduced.
- Browser smoke and focused tests pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Revert only renderer/evidence-display changes if browser validation fails.

Evidence: Delegated renderer review confirmed overlapping ranges are skipped deterministically by precedence and that per-range markers would require editing long generated JavaScript lines. Added a non-destructive evidence legend note, `Overlaps use evidence priority`, so the display contract is explicit without changing offsets or creating nested marks. Focused API/UI tests passed (`56 passed`), browser smoke passed, and `git diff --check` passed.

## Hypothesis

If the renderer records when an evidence range is covered by a higher-priority range and exposes that fact through the existing evidence detail panel, users will understand dense passages without visual nesting or data changes.

## Plan

1. Delegate bounded read-only renderer insertion-point review.
2. Add overlap metadata and evidence-panel display.
3. Run focused/browser checks and document the result.

## Completion

Completion recorded: no

Summary: Added explicit overlap-priority disclosure to the reader evidence legend while preserving deterministic offset rendering.

Validation: `pytest tests/test_feature_tabs.py tests/test_api.py -q` -> `56 passed`; browser smoke passed.

Residual risk: Individual covered-range markers remain deferred until the long-line renderer is refactored and visual regression fixtures exist.

Next recommended task: Refactor the highlight renderer into testable functions, then add per-range overlap indicators and screenshot coverage.
