# Task: Iterate Data Explorer usability and accessibility

Status: in-progress
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Improve the active Data Explorer website by reducing interaction friction and addressing the highest-confidence accessibility issues from the visual review.

Why now: The reader/search workflow is functional, search is idle until submission, statute loading is deferred, and highlighting is cleaner. The next improvements should make repeated research actions easier without reopening the V2 data-layer risk.

Owner surface: `backend/pages/data_explorer.py` active Data Explorer UI

Commit allowed: yes

Push allowed: yes

Dependencies: Tasks 085, 087, 088, 089, 090; current browser smoke and focused UI/API suites.

Risk boundary: UI/accessibility changes only. Preserve current routes, persisted evidence, reader tabs, explicit search behavior, mobile Themes, and all data-layer semantics.

Smallest falsifiable check: Focused UI/API tests plus browser smoke; static assertions for `aria-selected`, focus styles, and preserved reader selectors.

Acceptance criteria:

- Active tab state is exposed semantically to assistive technology.
- Keyboard users receive visible focus on interactive reader controls.
- Repeated search/reader workflow remains low-friction and browser smoke stays green.
- No data/extraction/resolution behavior changes.
- Documentation records the improved interaction contract and remaining backlog.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Revert only page-level UI changes if focused/browser validation fails. No database recovery required.

Evidence: Delegated review identified reader splitters as the highest-confidence accessibility friction: they had `tabindex` but pointer-only resizing, a 10px target, and no visible focus treatment. Added keyboard resize behavior for ArrowLeft/ArrowRight/Home/End, expanded the splitter hit target to 24px, and added a high-contrast focus outline. Focused API/UI tests passed (`56 passed`), and browser smoke passed with search, reader tabs, tags, layer legend, and mobile Themes.

## Hypothesis

If top-level/reader tab state and keyboard focus are made explicit while preserving existing click behavior, the Data Explorer will become easier to navigate without changing its data or reader contracts.

## Plan

1. Delegate a bounded usability/accessibility review of the current active page.
2. Implement the highest-confidence P1/P2 interaction improvements.
3. Run focused tests/browser smoke and document the result.

## Execution Checkpoints

- Delegation: pending bounded read-only usability/accessibility review.
- Implementation: manager-owned active page UI only.
- Documentation: canonical UI/system docs and Swimm walkthrough.
- Recovery: local server restart only.

## Completion

Completion recorded: no

Summary: First accessibility/usability slice complete; task remains open for top-level/reader `aria-selected` semantics and visual regression coverage.

Validation: `pytest tests/test_feature_tabs.py tests/test_api.py -q` -> `56 passed`; browser smoke passed.

Residual risk: Static accessibility checks cannot replace screen-reader or assistive-technology testing. Top-level tab semantics, mobile touch measurements, and screenshot regression checks remain.

Next recommended task: Add `aria-selected`/keyboard tab semantics and desktop/mobile visual regression checks.
