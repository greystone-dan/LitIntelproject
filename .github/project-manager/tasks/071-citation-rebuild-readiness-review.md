# Citation Rebuild Readiness Review

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Review deterministic citation extraction and the citation-layer processing path; verify pinpoint preservation and decide whether evidence supports readiness for a clean extraction rebuild followed by separate target resolution.

Why now: The direct full-anchor invariant is now covered by focused tests. Before authorizing a destructive citation-layer rebuild, the extraction and replacement paths must be reviewed for correctness, scope isolation, exact offsets, pinpoint behavior, and recovery controls.

Owner surface: `backend/citations.py`

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/case_processing.py`, citation ORM contract, focused citation tests, and an approved bounded rebuild runner.

Risk boundary: Review and tests only. Do not delete or write citation rows, run target resolution, modify statutes/metadata/tags/chunks/cases/source text, or run an unbounded database operation. Treat target resolution and metric recomputation as later phases.

Smallest falsifiable check: Focused pinpoint and exact-span tests prove full, neutral, reported, and short citation matches preserve pinpoint text and source offsets; a rebuild-style in-memory persistence check confirms `resolve_targets=False` leaves target IDs unset while preserving direct full anchors.

Acceptance criteria:

- Review identifies whether the extractor can preserve case citation text, pinpoints, offsets, and direct same-decision anchor provenance.
- Review confirms the ordered processing path can isolate citation replacement from statutes and other derived layers.
- Relevant pinpoint, exact-span, and persistence tests pass.
- Findings distinguish code-proven facts from future operational prerequisites.
- Canonical and Swimm documentation state the readiness decision and remaining approval gate.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`.

Rollback/recovery: No data mutation in this task. Any later rebuild requires a pre-run export, bounded cohort, checkpoint/resume state, operation log, post-run comparison, and explicit approval before deletion.

Evidence: Read-only extractor review inspected `backend/citations.py` and pinpoint/anchor tests. It found no extractor defect: raw matches retain exact spans; pinpoints are normalized and persisted in `citation_text` and `normalized_citation`; duplicate short forms retain separate offsets and direct full anchors; `resolve_targets=False` leaves all target IDs unset. Read-only processing review inspected `backend/case_processing.py` and citation scripts. `rebuild_citations_for_case` deletes only `Citation` rows for one source case and does not resolve targets; `case_citations` can be selected as an isolated stage. Existing bulk writers are unsuitable because they combine other stages or lack bounded-cohort, baseline, lock, checkpoint, dry-run, and comparator controls. Focused delegated test run: `tests/test_citations.py tests/test_case_processing.py -q` -> `132 passed, 1 warning`. Manager validation: `tests/test_citations.py -q -k "rebuild_style_extraction or rebuild_stores_each_inline_case_name_with_chunk_location"` -> `2 passed, 126 deselected, 1 warning`; earlier final focused run -> `128 passed, 1 warning`. Documentation checkpoint: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`; deferred runner recorded in `.github/project-manager/improvements/2026-09-07-citation-only-rebuild-runner.md`.

## Hypothesis

If deterministic extraction continues to preserve exact citation spans and pinpoints while its persistence helper accepts `resolve_targets=False`, and the processing path replaces only the case-citation layer, then the code is ready for a separately approved bounded extraction rebuild followed by target resolution.

## Plan

1. Audit extractor branches, pinpoint propagation, and short-form anchor admission.
2. Audit the citation processing and replacement boundary without running a writer.
3. Run targeted pinpoint/persistence checks and the focused citation suite. Complete.
4. Record readiness decision, operational prerequisites, and documentation checkpoint. Complete.

## Execution Checkpoints

- Delegation: Completed two read-only audits of extraction and processing/rebuild path.
- Implementation: Added regression assertions for persisted normalized pinpoints and the chunk-relative occurrence/document-relative anchor coordinate contract.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/system-map.ovnldklv.sw.md`.
- Recovery: No database operation is authorized in this task.

## Completion

Completion recorded: yes.

Summary: Extractor readiness is accepted; operational rebuild readiness is deferred pending a dedicated citation-only runner.

Validation: Focused manager checks passed: `2 passed, 126 deselected, 1 warning`; focused citation suite passed: `128 passed, 1 warning`; delegated combined citation/processing suite passed: `132 passed, 1 warning`. Warnings were third-party `CryptographyDeprecationWarning`s. No database mutation ran.

Residual risk: A clean citation-layer rebuild remains unapproved. Current bulk tools cannot provide the required controlled cohort and recovery evidence. Pinpoints are not independently queryable because the schema has no pinpoint field; their text is retained in citation and normalized fields.

Next recommended task: Implement and validate the bounded citation-only rebuild runner described in `.github/project-manager/improvements/2026-09-07-citation-only-rebuild-runner.md`; then seek explicit approval for a small cohort before any full deletion/rebuild.
