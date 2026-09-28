# Task: Upgrade About system map into an interactive graph

Status: in-progress
Created: 2026-09-24
Updated: 2026-09-24

## Task Record

Task: Turn the About system map from a six-node linear route into an interactive graph and map with expandable local neighborhoods and contextual panels.

Why now: The current visual canvas is readable but still behaves like a simple line of squares; selecting a station only swaps one detail card and does not reveal the system's connected structure.

Owner surface: `backend/pages/data_explorer.py` and focused UI/browser tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing About visual canvas, Swimm runtime flow charts, active Data Explorer tab behavior, and browser validation.

Risk boundary: UI-only. Preserve live inventory metrics, routes, API contracts, backend-owned evidence/provenance language, unrelated worktree changes, and the six-stage conceptual model. No database, API, or production/security changes.

Smallest falsifiable check: Browser interaction shows a selected station expanding into connected child nodes and multiple contextual panels, with a reset path and no horizontal overflow on desktop or mobile.

Acceptance criteria:

- The About surface reads as an interactive graph/map, not a six-item sequence.
- Selecting a station reveals a connected local neighborhood with directional or labeled relationships.
- Expanded content includes more than one contextual panel or node group and can be collapsed/reset.
- Graph nodes remain keyboard-accessible with clear active state and live detail updates.
- The visual language follows existing Swimm/runtime flow concepts without exposing misleading implementation claims.
- Responsive layout, reduced-motion behavior, live metrics, and other tabs remain intact.
- Focused tests, diagnostics, whitespace validation, and browser interaction checks pass.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/6.maiixtsw.sw.md`

Rollback/recovery: Restore the prior committed visual canvas implementation and focused assertions; no data rollback is needed.

Evidence: Pending delegated inspection and implementation.

## Hypothesis

If each primary station opens a connected subgraph with named relationships and multiple contextual panels, then visitors will understand how the library moves from source material to reviewable research evidence better than they do from a single linear route and one replacement detail card.

## Plan

1. Delegate a bounded inspection of existing Swimm charts and the current About graph surface.
2. Implement the smallest graph interaction slice with expandable neighborhoods, contextual panels, and reset behavior.
3. Run focused tests immediately, then browser-check desktop/mobile interaction and reduced-motion behavior.
4. Update canonical UI documentation and the Active UI Swimm walkthrough.
5. Finalize evidence and commit/push the completed checkpoint.

## Execution Checkpoints

- Authority review: pending.
- Delegation: pending.
- Implementation: pending.
- Documentation: pending.
- Recovery: no long-running or destructive operation planned.

## Completion

Completion recorded: no

Summary: In progress.

Validation: Pending.

Residual risk: A richer graph can become visually dense or imply relationships that are not backed by the documented runtime flow; labels and source boundaries must remain explicit.

Next recommended task: Have a general visitor review the expanded graph and identify the least understandable relationship.
