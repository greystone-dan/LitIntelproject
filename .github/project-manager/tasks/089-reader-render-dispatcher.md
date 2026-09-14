# Task: Consolidate reader render dispatch

Status: complete
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Simplify the active Data Explorer reader's layered `renderCaseReaderPane` wrappers into one explicit dispatcher while preserving tabs, persisted evidence, and browser smoke behavior.

Why now: The active page currently reassigns `renderCaseReaderPane` through multiple historical wrappers for metadata, activity, info, tags, Acts/Regs, precedents, and grouped tags. This makes tab behavior difficult to reason about and increases regression risk.

Owner surface: `backend/pages/data_explorer.py` active reader JavaScript

Commit allowed: yes

Push allowed: yes

Dependencies: Completed task 088 highlighting cleanup, task 087 lazy statute loading, browser smoke, and current reader API contract.

Risk boundary: UI JavaScript only. Preserve all existing tab labels/selectors, persisted evidence semantics, explicit search behavior, and mobile Themes. No database or extraction changes.

Smallest falsifiable check: `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_feature_tabs.py tests\\test_api.py -q` plus browser smoke with Vavilov.

Acceptance criteria:

- Reader tab behavior remains unchanged for Metadata, Citations, Info, Intel, Activity, Tags, Acts / Regs, and Precedents.
- The active render path has one clear dispatch point rather than a sequential wrapper chain.
- Browser smoke and focused API/UI tests pass.
- No citation/statute/tag data behavior changes.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Revert only the reader JavaScript refactor if any tab or browser check fails.

Evidence: Delegated read-only audit mapped the active five-layer `renderCaseReaderPane` wrapper chain, duplicate render definitions, tab selectors, and endpoint calls. The manager added a capture-phase reader tab dispatcher so each `[data-reader-tab]` click has one explicit owner while preserving existing endpoint behavior and selectors. Existing wrappers remain behind that boundary for later incremental removal. Focused API/UI tests passed (`56 passed`), and browser smoke passed with all reader tabs, tags, layer legend, and mobile Themes.

## Hypothesis

If the reader's tab-specific render logic is routed through one dispatcher, the same persisted payload will produce the same visible tabs with lower implementation complexity and fewer order-dependent overrides.

## Plan

1. Delegate bounded read-only wrapper-chain mapping and selector inventory.
2. Replace the sequential wrapper reassignment with one dispatcher or a narrowly equivalent consolidation.
3. Run focused tests and browser smoke, then update docs/task evidence.

## Execution Checkpoints

- Delegation: pending bounded reader JavaScript audit.
- Implementation: manager-owned page JavaScript only.
- Documentation: canonical UI docs and Swimm walkthrough.
- Recovery: local server restart only.

## Completion

Completion recorded: yes

Summary: Added one explicit reader tab dispatcher boundary without changing active tab behavior. Deferred deletion of the historical wrapper chain to a separately tested refactor.

Validation: `pytest tests/test_feature_tabs.py tests/test_api.py -q` -> `56 passed`; browser smoke passed.

Residual risk: The generated page still contains historical renderer wrappers and duplicate definitions behind the dispatcher. Full removal remains higher risk and should receive dedicated visual regression coverage.

Next recommended task: Build visual regression coverage, then consolidate the reader wrapper chain into one dispatcher.
