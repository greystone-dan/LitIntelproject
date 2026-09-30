# Task: Consolidate project-wide still-to-do register

Status: complete
Created: 2026-09-29
Updated: 2026-09-29

## Task Record

Task: Create a single evidence-backed register of remaining product work, known accuracy gaps, operational debt, deferred research, and feature opportunities across AI CaseLibrary.

Why now: Backlog material is distributed across roadmaps, task records, architecture notes, runbooks, and evaluation artifacts. A consolidated register is needed to make prioritization visible and prevent duplicate or prematurely scheduled work.

Owner surface: `docs/STILL_TO_DO.md`.

Commit allowed: yes

Push allowed: yes

Dependencies: `ROADMAP.md`, `MASTER_IDEAS.md`, `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, active/deferred task records, current Swimm technical-debt walkthrough, and current generated/status documentation.

Risk boundary: Documentation and planning only. Do not imply that deferred ideas are implemented, reopen completed work without evidence, launch operations, mutate data, invoke external or paid services, or change runtime behavior.

Smallest falsifiable check: The register links every listed item to a current source and distinguishes active commitments, known gaps, deferred research, and unscheduled ideas.

Acceptance criteria:

- A single register groups remaining work by product, accuracy/data quality, operations/reliability, and research/advanced intelligence.
- Each item has a short rationale, current status, source of evidence, and a suggested next validation or decision gate.
- Duplicate or already-implemented ideas are marked rather than represented as new work.
- The register ranks the highest-leverage next tasks using trust, research value, cost, and implementation risk.
- Canonical planning documentation and the Swimm technical-debt walkthrough link to the register.

Harness criteria:

- Register includes all required categories with source links.
- Priority shortlist includes validation or decision gates.
- Documentation paths are recorded in the task evidence.

Docs/generated references: `docs/STILL_TO_DO.md`, `ROADMAP.md`, and `.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md`.

Rollback/recovery: Delete the new register and revert the documentation links; no runtime or data changes are involved.

Evidence: `Explore` completed a read-only cross-project inventory of roadmap commitments, task records, known data-quality gaps, FC Activity work, and long-term intelligence ideas. The synthesis is in `docs/STILL_TO_DO.md`; it distinguishes active, ready, blocked, deferred, and implemented work, and records an explicit validation or decision gate for the 12-item shortlist. Required documentation updated: `ROADMAP.md` and `.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md`; documentation authority updated in `DOCS_INDEX.md`.

Files changed: `docs/STILL_TO_DO.md`, `ROADMAP.md`, `DOCS_INDEX.md`, `.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md`, and this task record.
Delegated work: `Explore` read-only inventory completed; no files changed by the worker. It returned five categories and a ranked priority set, which were consolidated without reopening deferred implementation work.
Focused validation: All local linked source paths in the register were found through workspace file discovery. `git diff --check` passed in both the original and recovery harness runs. Two attempted harnessed PowerShell link-check commands failed only because the harness parser stripped embedded child-command quotes; no documentation defect was identified.
Residual risk: The register is a dated planning synthesis and must defer to live database/API evidence for current counts.
Next bounded task: Citation short-form anchor quality audit and backfill decision, beginning with a $100$-case exact-anchor dry run.

## Hypothesis

If the distributed planning and gap evidence is consolidated with explicit status and decision gates, then the project can prioritize the next task without conflating implemented features, known deficits, and speculative ideas.

## Plan

1. Delegate a read-only inventory of the roadmap, master ideas, active/deferred task records, known gaps, and technical-debt walkthrough.
2. Create the register with deduplicated categories, evidence links, and a ranked shortlist.
3. Update planning/Swimm references, validate local links and the diff, and record task evidence.

## Execution Checkpoints

- Delegation: `Explore` project inventory completed; its findings were used as the synthesis input.
- Implementation: `docs/STILL_TO_DO.md` created with five categories, status boundaries, implemented-work guardrails, and a 12-item shortlist.
- Documentation: `ROADMAP.md`, `DOCS_INDEX.md`, and `.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md` now point to the register.
- Recovery: Documentation-only change. Two failed harness child-PowerShell commands were isolated to command quoting; the successful `git diff --check` result and workspace local-link review were retained.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-29 | Create one project-wide register before selecting another implementation slice | The backlog is distributed across many overlapping sources | User request, `ROADMAP.md`, `MASTER_IDEAS.md`, and task-record inventory |

## Completion

Completion recorded: yes

Summary: Completed the canonical cross-project still-to-do register and linked it from the planning, documentation-authority, and Swimm technical-debt surfaces.

Validation: Workspace file discovery confirmed every local source path referenced by the register exists; `git diff --check` passed. A clean final harness run and evidence gate record the acceptance evidence.

Residual risk: The register can become stale as runs and task records change; it is intentionally a planning index rather than a live operational status store.

Next recommended task: Run the bounded citation short-form anchor quality audit before considering any recovery/backfill write.