# Task: Improve Citation Intelligence evidence navigation

Status: deferred
Created: 2026-09-29
Updated: 2026-09-29

## Task Record

Task: Make the active Citation Intelligence tab more useful by reducing the steps from a selected authority to the stored citation evidence and its surrounding case context.

Why now: The current workspace exposes substantial citation analytics, but research value depends on quickly reaching reviewable source evidence rather than adding more derived metrics or unverified treatment claims.

Owner surface: `backend/pages/data_explorer.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing citation-intelligence routes, `backend/citation_map.py`, active inline reader, `tests/test_feature_tabs.py`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`.

Risk boundary: Preserve backend-owned citation offsets, resolved/unresolved status, active `/data-explorer` workflow, and existing API contracts. Do not infer citation treatment, controlling authority, legal similarity, or case outcome; do not mutate citation data or add paid/runtime model calls.

Smallest falsifiable check: A selected Citation Intelligence authority exposes a clear route from its overview to stored citation evidence, and a browser check can follow that route without stale or ambiguous state.

Acceptance criteria:

- The selected-authority workspace exposes the most useful existing stored-evidence path without adding a legal inference.
- The evidence route preserves the source case, citation identity, and reader navigation already owned by the backend.
- Loading, empty, and failure states remain clear and existing Citation Intelligence subviews stay reachable.
- Focused UI tests and a bounded browser check pass.
- The research UI guide and Citation Intelligence Swimm walkthrough explain the new evidence path and boundary.

Harness criteria:

- Focused Citation Intelligence UI test passes.
- Browser check verifies the evidence path for a selected authority.
- Documentation paths are recorded in the task evidence.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`, and this task record. No generated reference requires manual editing.

Rollback/recovery: Revert the scoped generated-UI/test/documentation changes; no data, migration, or API contract rollback is required.

Evidence: Superseded before delegation or implementation by the 2026-09-29 project-wide "still to do" inventory request. No product, API, UI, data, or documentation changes were made for this task.

Files changed: This task record only.
Delegated work: None; superseded before the planned inventory began.
Focused validation: Not run; no implementation occurred.
Residual risk: The Citation Intelligence evidence-navigation opportunity remains unassessed.
Next bounded task: Reconsider the evidence-navigation slice after the project-wide backlog register identifies its relative priority.

## Hypothesis

If Citation Intelligence promotes an existing source-grounded evidence path at the selected-authority level, then researchers can inspect how an authority appears in citing decisions with less navigation while preserving the boundary between evidence and treatment inference.

## Options Considered

1. Add more graph scores and rankings: low implementation risk but limited research value without immediate passage evidence.
2. Add citation treatment or semantic-purpose inference: potentially high value but high review, explainability, and publication risk; outside current approved constraints.
3. Improve direct evidence navigation from the current overview: high evidence fidelity, modest implementation cost, and strong fit for the active research workflow. Selected.

## Plan

1. Delegate a read-only inventory of the current overview, evidence table, reader navigation, and focused tests.
2. Implement the smallest evidence-first UI enhancement and focused contract test.
3. Validate in the browser, update the research guide and Swimm walkthrough, then record evidence.

## Execution Checkpoints

- Delegation: Pending `Explore` evidence-path inventory.
- Implementation: Pending owner-surface UI change and focused validation.
- Documentation: Pending `docs/RESEARCH_UI_GUIDE.md` and `.swm/8.upryk5h6.sw.md` updates.
- Recovery: No long-running operation or persisted state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-29 | Prioritize evidence navigation over new scores or treatment inference | It increases immediate research utility without weakening citation-evidence boundaries | `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and existing Citation Intelligence workspace task |

## Completion

Completion recorded: deferred before implementation.

Summary: Deferred in favor of a managed project-wide inventory of backlog items, known accuracy gaps, operations debt, and feature opportunities.

Validation: Not applicable; no behavior changed.

Residual risk: The deferred citation-evidence path has not been evaluated in the active UI.

Next recommended task: Consolidate the repository-wide still-to-do register and rank the Citation Intelligence slice against trust, research value, cost, and implementation risk.