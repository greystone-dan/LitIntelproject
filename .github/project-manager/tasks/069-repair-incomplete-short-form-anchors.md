# Backfill Incomplete Short-Form Anchors

Status: deferred
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Run the second short-form anchor provenance backfill for stored `case_short` rows whose anchor text and offsets exist but are incomplete.

Why now: This is a separate backfill from task 068: approximately `383,608` unresolved stored short-form rows already have anchor fields but may omit adjacent neutral or reporter citation text. The Zazai row is a confirmed example.

Owner surface: `backend/citations.py` extraction and an anchor-only citation backfill.

Commit allowed: yes

Push allowed: yes

Dependencies: Source case text, stored short-form citation offsets, current V2 extractor, focused citation tests, and a read-only before/after inventory.

Risk boundary: Include only rows with existing anchor text and complete anchor offsets. The inventory separates pure right-edge extensions from start-correction candidates and rows with no local extension evidence. Exclude rows with no anchor text or offsets. Do not alter citation text, normalized citations, target links, unresolved state, statute references, chunks, or source offsets. Do not use global aliases or fuzzy matching.

Smallest falsifiable check: The representative Zazai, Siloch, and Mugesera texts must produce one full case citation span and a later short row whose anchor offsets equal that full span.

Acceptance criteria:

- Dotted neutral forms such as `2004 F.C. 1356` are included in the full same-decision anchor.
- Parenthesized reporter forms such as `(1993), 151 N.R. 76 (F.C.A.)` are included in the full same-decision anchor.
- The focused citation suite passes with exact source and anchor offsets.
- A read-only inventory reports the exact anchored unresolved population, pure right-edge candidates, start-correction candidates, no-local-evidence rows, and source-span conflicts.
- The resulting backfill plan updates anchor fields only; no database writer runs in this task.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/blank.dudtv9pz.sw.md`, and sibling task `.github/project-manager/tasks/068-backfill-short-form-anchor-provenance.md`.

Rollback/recovery: No database write is run here. A later writer must export affected anchor fields, use checkpointed commits, and restore only prior anchor columns for affected citation IDs if post-write validation fails.

Evidence: `125` focused citation tests passed after the final regression was added. The read-only inventory processed `33,963` source decisions and reported `383,608` unresolved anchored rows, `9,130` pure right-edge extension candidates, `14,235` start-correction candidates, `360,243` rows with no local extension evidence, and `78,372` excluded no-anchor rows. No database writer, target-resolution run, or full-document extraction was run.

## Hypothesis

If the extractor recognizes dotted neutral and parenthesized reporter citation shapes as full case rows, bounded inspection of an existing short-form row's stored source span will identify a safe right-edge anchor extension without changing any citation or target fields. Start corrections require a separate review gate.

## Plan

1. Add focused citation patterns and regression tests for composite full-anchor spans.
2. Run the focused citation suite immediately after the parser edit.
3. Run a read-only stored-row comparison limited to rows with existing anchor text and offsets; report exact recoveries, conflicts, and excluded no-anchor rows.
4. Update canonical and Swimm documentation with the scope, count, and backfill guardrails.

## Execution Checkpoints

- Delegation: None; bounded local parser/test/inventory work is smaller than delegation overhead.
- Implementation: Complete in `backend/citations.py`, `tests/test_citations.py`, and `scripts/report_incomplete_short_form_anchors.py`; the script remains read-only.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, and `.swm/blank.dudtv9pz.sw.md`.
- Recovery: No writer or database mutation in this task.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Separate incomplete-anchor repair from the no-anchor gap | User clarified that the target is the approximately 400k rows with anchor text present but incomplete | Zazai row 4408593 has anchor offsets `5576-5591` containing only `Zazai v. Canada` while the source contains the adjacent full citation |
| 2026-09-07 | Separate safe suffix repair from start correction | Existing historical anchors can include narrative or header text before the authority; only pure right-edge extensions are writer candidates without an additional semantic gate | Inventory: `9,130` pure right-edge candidates, `14,235` start-correction candidates, `360,243` with no local extension evidence |

## Completion

Completion recorded: 2026-09-07

Summary: This second backfill is scoped and inventoried but deferred before writing. The `9,130` pure right-edge rows are one directly recoverable class within the `383,608`-row backfill; the remaining classes require additional bounded reconstruction or review.

Validation: `pytest tests\\test_citations.py -q` -> `125 passed, 1 warning`; `py_compile backend\\citations.py scripts\\report_incomplete_short_form_anchors.py` passed; read-only inventory completed with the counts recorded above.

Residual risk: The `14,235` start-correction candidates may contain metadata/header or narrative contamination and remain unchanged pending review. The `360,243` no-local-evidence rows are not proven complete. No target resolution was changed.

Next recommended task: Prepare the second backfill's checkpointed, anchor-only dry-run, covering all `383,608` in-scope rows and partitioning direct repairs, start corrections, no-local-evidence rows, and conflicts before any write.

Status: deferred
