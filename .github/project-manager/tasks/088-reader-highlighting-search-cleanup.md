# Task: Clean up reader highlighting and search

Status: complete
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Review and simplify the main Data Explorer case reader and search experience, with emphasis on broken/overlapping highlighting and unnecessary frontend complexity.

Why now: The reader now correctly serves persisted evidence only, but its highlighting/rendering code has accumulated layered overrides and duplicate render functions. The user reports decision highlighting is messy, and search should remain fast and clean.

Owner surface: `backend/pages/data_explorer.py` active Data Explorer reader/search page

Commit allowed: yes

Push allowed: yes

Dependencies: Task 085/087 persisted-only reader contract, current API/UI tests, browser smoke, and no database changes.

Risk boundary: Do not change citation extraction, statute/tag persistence, target resolution, or source offsets. Preserve explicit search behavior, stored evidence semantics, reader tabs, and mobile Themes. UI-only/API projection changes require browser validation.

Smallest falsifiable check: `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_feature_tabs.py tests\\test_api.py -q` plus browser smoke with Vavilov.

Acceptance criteria:

- Main reader highlighting does not overlap or produce confusing duplicate marks/buttons.
- Search remains idle until explicit submission and returns current case data.
- Reader tabs, tags, citation layers, and mobile Themes remain functional.
- Duplicate/overriding frontend render paths are reduced or clearly isolated.
- A ranked follow-up list identifies remaining UI improvements.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Revert only page-level UI changes if browser/API acceptance fails. No database rollback is authorized.

Evidence: Delegated read-only review found the active reader applied citation/statute highlights from backend offsets, then ran `applyTagHighlights()` text-search over rendered chunk DOM, causing nested/overlapping marks and repeated-text false positives. It also identified a layered reader renderer chain. Manager cleanup disabled the post-render text-search tag overlay in chunk mode, preserving clean offset-based citation/statute marks; tags remain available in the Tags panel and offset-based Full text path. Explicit search remains idle on page load after the prior `184c030` checkpoint. Focused API/UI tests passed (`56 passed`), and browser smoke passed with reader tabs, tags, layer legend, and mobile Themes.

## Hypothesis

If the active reader uses one canonical highlight renderer with explicit precedence for citations, statutes, and tags, the main decision view will become visually coherent without changing persisted evidence; removing duplicate initialization/render overrides will reduce regressions.

## Plan

1. Delegate bounded read-only review of reader highlighting/search code and browser symptoms.
2. Choose one cleanup slice and implement it without touching data layers.
3. Run focused tests and browser smoke, measure visible behavior, and update docs.

## Execution Checkpoints

- Delegation: pending bounded read-only reader/search review.
- Implementation: manager-owned `backend/pages/data_explorer.py` changes only unless API contract evidence requires a one-hop route change.
- Documentation: canonical system/UI docs and `.swm/4.9nn3id9f.sw.md`.
- Recovery: local server restart only; no database writer.

## Completion

Completion recorded: yes

Summary: Removed the overlapping chunk tag overlay that made decision highlighting visually messy while preserving stored citation/statute highlighting and tag inspection.

Validation: `pytest tests/test_feature_tabs.py tests/test_api.py -q` -> `56 passed`; browser smoke passed.

Residual risk: The generated page still has historical renderer wrappers that should be consolidated in a future UI refactor. Chunk-mode tag highlights are intentionally not overlaid on citation/statute marks to preserve non-overlapping evidence display.

Next recommended task: Consolidate the layered `renderCaseReaderPane` wrappers into one dispatcher after adding visual regression coverage for citation/statute/tag precedence.
