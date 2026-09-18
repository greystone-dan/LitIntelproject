# Task: Copilot review handoff protocol pilot

Status: in-progress
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Set up a simple OneDrive-visible folder protocol for external Copilot review work.

Why now: Replace manual copy/paste of large review packets with a durable shared-file handoff.

Owner surface: `data/copilot_review/` and its bounded task-folder protocol.

Dependencies: V1.1 case 677 review packet and OneDrive synchronization.

Risk boundary: No code, canonical data, database rows, or source evaluation packets are modified by the external reviewer. The external reviewer writes only the response file in its numbered task folder.

Smallest falsifiable check: An external reviewer can read `REQUEST.md` and `SOURCES.md`, open the complete V1.1 case 677 packet, and write a complete `RESPONSE.md` without requiring pasted chat content.

Acceptance criteria:

- A shared review-root README defines the handoff protocol.
- Task `001-discussion-units-677` has a request, source manifest, and status marker.
- The request identifies the complete V1.1 packet and response contract.
- The source manifest points to Markdown and JSON artifacts without duplicating or altering them.
- The external reviewer is instructed to write only `RESPONSE.md`.

Docs/generated references: `data/copilot_review/README.md`; task folder `data/copilot_review/001-discussion-units-677/`; no generated references.

Rollback/recovery: Delete only this staged handoff folder and task record. Preserve all source evaluation artifacts.

Commit allowed: yes

Push allowed: yes

Evidence: Setup files created. External response and local validation are pending.

## Completion

Completion recorded: no

Residual risk: OneDrive sync delay, Copilot 365 path/permission limitations, and response quality remain untested until the external reviewer returns `RESPONSE.md`.

Next recommended task: Ask external Copilot to process `data/copilot_review/001-discussion-units-677/REQUEST.md` and save its response as `RESPONSE.md`.
