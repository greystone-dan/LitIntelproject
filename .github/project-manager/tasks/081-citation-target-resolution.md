# Task: Citation target resolution after full extraction replacement

Status: in-progress
Created: 2026-09-07
Updated: 2026-09-08

## Task Record

Task: Run the deferred case-to-case target resolution pass (`scripts/resolve_citation_targets.py` then `scripts/resolve_short_citation_targets.py`) over the citation layer produced by the completed full extraction replacement (task 080).

Why now: The extraction-only replacement in task 080 completed (61,212 cases rebuilt, 4 explicitly skipped) with `target_resolution=deferred`. Resolution is the next required layer before citation metrics.

Owner surface: `scripts/resolve_citation_targets.py`, `scripts/resolve_short_citation_targets.py`, `backend/citations.py` (read-only use of `build_local_case_resolution_index`)

Commit allowed: yes

Push allowed: yes

Dependencies: Completed citation extraction (task 080), PostgreSQL availability, no concurrent bulk writer.

Risk boundary: Must only set `Citation.target_case_id`/`unresolved`; must not re-extract citations, must not touch statute references or metadata, and must not run concurrently with another bulk writer.

Smallest falsifiable check: Formal/neutral resolver's own summary line (`finished inspected=... resolved=...`) and short-form resolver's final summary; spot-check a handful of newly resolved rows against `Case.title`/`citation`.

Acceptance criteria:

- `resolve_citation_targets.py` completes over all unresolved rows and reports final counts.
- `resolve_short_citation_targets.py` completes over all `case`/`case_short`/`case_name`/`neutral` rows and reports final counts.
- No citation extraction or statute rows are modified.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Both scripts only ever move a row from `unresolved=true`/`target_case_id=NULL` to a resolved state; recovery is to inspect `Citation.target_case_id` history is not versioned, so a bad resolution class would need a targeted re-null of affected rows by rule, not a full re-run.

Evidence: `resolve_citation_targets.py` completed in apply mode after task 080. The current database contains `1,444,546` citation rows, with `919,781` linked and `524,765` unresolved. The read-only report command
`.\venv\Scripts\python.exe scripts\report_unresolved_citation_shapes.py --top 50 --output data\eval\reports\unresolved_citation_shapes_post_resolution_20260907.json`
completed successfully. Its pre-short-form breakdown is `350,119 case_name`, `117,905 case_short`, `53,078 case`, and `3,663 neutral` unresolved rows; `477,627` (`91.02%`) have no exact local signal, while `16,656` have a unique case-alias signal and `1,258` have an ambiguous title/year signal. The short/name resolver has not run yet; metrics recomputation is also pending.
Documentation checkpoint: updated `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/4.9nn3id9f.sw.md`. The report arithmetic validation passed, and `git diff --check` passed for all edited task and documentation files.
Implementation correction: the short resolver now treats `case_short` rows as anchor-exclusive. Formal identifiers preserved in `normalized_citation` constrain candidates, and the short name only disambiguates compound anchors; it never triggers a corpus-wide short-name lookup. Focused tests passed (`3 passed`), and a read-only live audit found `484,705` of `655,842` `case_short` rows anchor-resolvable, including `153,262` of `157,786` compound-anchor rows. No database writer was run after this correction.

The later cancelled short/name apply process had already committed bounded batches. It linked `3,019` rows (`501 case_short`, `2,518 case_name`) before cancellation. The accepted remaining short-form inventory gap is `117,074` anchored unresolved occurrences across `10,889` source cases and `16,495` distinct exact anchors; all have zero local candidates from their stored citation identifiers. Another `330` unresolved short rows lack anchors and remain provenance defects. Task 082 subsequently resolved `14,051` exact canonical-title `case_name` rows, leaving `507,695` unresolved rows overall and `390,291` when `case_short` is excluded.

## Hypothesis

If the extraction layer is complete and consistent, both resolution passes will complete cleanly and report a large, plausible resolved fraction without needing the extractor to re-run.

## Plan

1. Run `scripts/resolve_citation_targets.py` (neutral/formal exact + canonical-title resolution) to completion.
2. Run `scripts/resolve_short_citation_targets.py` (short/name alias resolution) to completion.
3. Record final summary counts and update documentation/Swimm.

## Execution Checkpoints

- Delegation: none; direct execution of the two prepared resolver scripts.
- Implementation: run both scripts to completion in the visible terminal.
- Documentation: canonical repository path `SYSTEM_REFERENCE.md`/`OVERNIGHT.md`; Swimm path `.swm/4.9nn3id9f.sw.md`.
- Recovery: none required; both scripts are additive (only fill `NULL` targets).

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Task created, apply mode approved without dry run | Extraction replacement completed; operator explicitly approved a direct apply run | Task 080 completion: `completed=61212 skipped=4 pending=0` |

## Completion

Completion recorded: no

Summary: Pending.

Validation: The unresolved-shape report completed successfully and matches the database unresolved count of `524,765`. The report is intentionally pre-short-form resolution.

Residual risk: The unique-alias and title/year buckets are candidates, not accepted resolutions; ambiguity gates must remain in place. The report is not the final unresolved baseline until `resolve_short_citation_targets.py` completes.

Next recommended task: Recompute citation metrics (`compute_citation_metrics()`) once both resolution passes complete.
