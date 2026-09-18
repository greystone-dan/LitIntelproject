# Task: Build managed roadmap handoff for next platform phase

Status: in-progress
Created: 2026-09-14
Updated: 2026-09-14

## Task Record

Task: Review current AI CaseLibrary position and produce an evidence-backed execution roadmap for a stronger implementation agent covering pinpoint resolution, statute resolution, tagging, and website evolution.

Why now: Citation extraction/resolution and the Data Explorer reader have recently changed. The next agent needs a dependency-ordered handoff that avoids repeating completed work and protects the extraction/resolution/data-layer boundaries.

Owner surface: Project-manager roadmap and task handoff documentation

Commit allowed: yes

Push allowed: yes

Dependencies: Current task records, SYSTEM_REFERENCE.md, ROADMAP.md, MASTER_IDEAS.md, OVERNIGHT.md, active Swimm maps, live inventory, and recent committed checkpoints.

Risk boundary: Review and roadmap only. No database writers, production changes, destructive operations, or broad implementation in this task.

Smallest falsifiable check: A bounded delegated inventory plus live read-only counts must reconcile current completed work, open tasks, unresolved citation classes, and website acceptance state.

Acceptance criteria:

- Completed work and remaining work are separated clearly.
- Pinpoint resolution, statute resolution, tagging, and website work are ordered by dependencies.
- Each phase has an owner surface, acceptance gate, rollback boundary, and recommended worker assignment.
- The handoff explicitly prevents repeating exact case-name resolution, full extraction, and reader extraction work already completed/fixed.
- Canonical and Swimm roadmap documentation are updated, with task evidence naming actual commands and uncertainties.

Docs/generated references: `ROADMAP.md`, `MASTER_IDEAS.md`, `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/future-state.north-star.sw.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Documentation-only changes; revert the roadmap checkpoint without touching application or database state.

Evidence: Pending delegated inventory and manager synthesis.

## Hypothesis

If current task records, live counts, and active UI acceptance are reconciled before planning the next phase, a stronger agent can execute pinpoint/statute/tag/site work in dependency order without repeating completed extraction or reader fixes.

## Plan

1. Delegate bounded repository/task/live-inventory review.
2. Synthesize phases, gates, owners, dependencies, and explicit exclusions.
3. Update roadmap, canonical system reference, and Swimm direction.
4. Validate documentation links/format and deliver the handoff.

## Completion

Completion recorded: no

Summary: Roadmap handoff started.

Validation: Pending.

Residual risk: Some prioritization depends on product choices about accuracy versus coverage and whether external authority inventory expansion is allowed.

Next recommended task: Pending delegated inventory.
