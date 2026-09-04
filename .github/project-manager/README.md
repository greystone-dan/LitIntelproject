# Project Manager Agent Workflow

Use the workspace-level **AI CaseLibrary Project Manager** agent for a bounded
outcome that should be planned, implemented, validated, documented, and handed
off with less conversational steering.

## Start A Task

1. Select the project-manager agent in VS Code chat, or invoke the
   `managed-task` prompt.
2. State the desired outcome, priority, constraints, and whether the agent may
   commit or push after validation.
3. The agent creates a task record in `.github/project-manager/tasks/` from
   `TASK_TEMPLATE.md` when the work has multiple steps or must survive a
   session boundary.
4. The agent chooses one owning surface, records a falsifiable hypothesis, and
   runs the narrowest relevant check before expanding work.

Task files are working records. Keep completed records for traceability; do not
use them as a replacement for `CHANGELOG.md`, generated references, or source
provenance.

## Statuses

| Status | Meaning |
| --- | --- |
| `planned` | Outcome is recorded but implementation has not started |
| `in-progress` | One owned slice is actively being changed and validated |
| `blocked` | A concrete dependency, failed check, or approval decision prevents safe progress |
| `deferred` | Work is intentionally postponed with a recorded reason and next trigger |
| `complete` | Acceptance criteria are met and evidence is recorded |

## Authority And Handoff

The agent reads `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`,
`.github/copilot-instructions.md`, `OVERNIGHT.md`, and the relevant Swimm map
before changing an owned surface. Use `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`
for the transition contract and [Product North Star and Future State](../../.swm/future-state.north-star.sw.md)
for future direction.

Update the canonical system document and linked Swimm walkthrough when a change
alters behavior, ownership, operations, or workflow. Generated API, schema,
script-catalog, and work-history documents must be regenerated from their
sources, never hand-edited.

## Autonomy Boundary

The agent may complete a clear, reversible change inside one owner surface after
recording acceptance criteria and validation. It must ask before unbounded or
paid operations, security/access/data-retention decisions, production or
Government of Canada/CBSA integrations, destructive operations, non-reversible
migrations, or movement into a new owner surface.

## Completion Standard

A task is complete only when it names the files changed, the focused validation
that actually ran, the result, residual risk, and the next bounded task. A
preflight, static review, or documentation check does not prove a bulk job,
browser journey, migration, or deployment succeeded.
