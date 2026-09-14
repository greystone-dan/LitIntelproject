# Task: Improve case reader highlight display

Status: in-progress
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Review and improve the visual display of persisted citation, statute, and tag highlights in the main Data Explorer case reader.

Why now: The reader no longer extracts or rescans HTML at request time, and chunk tag overlays were removed because they nested with citation/statute marks. The remaining priority is making stored evidence visually clear across chunk and full-text modes without losing offsets or target links.

Owner surface: `backend/pages/data_explorer.py` active reader highlight renderers/CSS

Commit allowed: yes

Push allowed: yes

Dependencies: Tasks 085, 088, 089, 091; persisted reader payload; browser smoke and focused UI/API tests.

Risk boundary: Display-only. Do not change citation/statute/tag rows, offsets, resolution, extraction, or database data. Preserve target-case links, evidence toggle, reader tabs, mobile layout, and current smoke selectors.

Smallest falsifiable check: Focused UI/API suite plus browser smoke with Vavilov; static/runtime check that chunk and full-text highlight spans render without nested duplicate marks.

Acceptance criteria:

- Citation, statute, and tag visual treatments are distinct and readable.
- Chunk mode avoids nested/overlapping display marks.
- Full-text mode preserves persisted offsets and target links.
- Evidence details/hover behavior remains usable and mobile-safe.
- Browser smoke and focused tests pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Revert only CSS/renderer changes if visual/browser acceptance fails. No database recovery required.

Evidence: Delegated review found that chunk/full-text evidence uses distinct citation, statute, and tag classes, but borders and inset shadows compound visually in dense passages; overlapping ranges are currently skipped by offset precedence. The manager applied a display-only cleanup: citation/statute/tag highlights now use flatter fills, smaller radii, no borders, and restrained underlines instead of stacked borders/shadows. No offsets, data rows, links, or extraction behavior changed. Focused API/UI tests passed (`56 passed`), browser smoke passed, and `git diff --check` passed.

## Hypothesis

If highlights use one explicit precedence model and restrained CSS rather than layered borders/shadows, the reader will show persisted evidence clearly without visual collisions or ambiguous colors.

## Plan

1. Delegate bounded review of chunk/full-text highlight renderers and CSS.
2. Implement one display-only improvement slice.
3. Run focused tests/browser smoke and document the result.

## Execution Checkpoints

- Delegation: pending read-only highlight review.
- Implementation: manager-owned active page CSS/JS only.
- Documentation: canonical UI guide/system reference and Swimm walkthrough.
- Recovery: local server restart only.

## Completion

Completion recorded: no

Summary: First display-only highlight slice complete; task remains open for explicit overlap indicators and visual regression coverage.

Validation: `pytest tests/test_feature_tabs.py tests/test_api.py -q` -> `56 passed`; browser smoke passed.

Residual risk: Overlapping ranges can still be dropped by precedence in the renderer, and no pixel-level visual regression baseline exists yet.

Next recommended task: Add overlap-aware evidence indicators and desktop/mobile screenshot coverage before changing range precedence.
