# Citation Extraction Canary

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Run an explicitly approved one-case citation-extraction apply canary, inspect its baseline and pre-commit comparison, then run a five-case bounded extraction-only cohort if the canary is clean.

Why now: The controlled citation-only runner is implemented and validated through mocks. The user approved a one-case test followed by a bounded run, while requiring resolution to remain separate.

Owner surface: `scripts/rebuild_citations_controlled.py`

Commit allowed: yes

Push allowed: yes

Dependencies: PostgreSQL connectivity, selected canonical cases, `scripts/rebuild_citations_controlled.py`, and exclusive writer access.

Risk boundary: This task may replace only `Citation` rows for explicitly selected source cases. It must not run generic resolution, short-form resolution, metrics, statutes, metadata, tags, chunks, case/source writes, external lookups, or concurrent writers. Stop before the five-case cohort if the one-case baseline/comparison shows invalid short anchors, an error, or unexpected evidence.

Smallest falsifiable check: One apply canary creates baseline/state/comparison artifacts, reports only the `case_citations` stage, has zero invalid rebuilt short anchors, and contains no target-resolution or metric operation.

Acceptance criteria:

- A selected one-case apply canary completes with preserved recovery artifacts and a clean comparison.
- A five-case explicit apply cohort completes only after canary acceptance.
- Every run state records `target_resolution=deferred` and `metrics=deferred`.
- No non-citation derived layer is selected or changed by the runner.
- Evidence names exact run directories, commands, statuses, and comparison results.
- Canonical and Swimm documentation record actual results and the deferred-resolution boundary.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/4.9nn3id9f.sw.md`.

Rollback/recovery: Each run directory contains a source-case citation baseline before replacement. On any failed or unacceptable run, stop further cohorts, preserve state/baseline/comparison, and restore only affected citations through a separately reviewed recovery command. Do not resolve targets or metrics.

Evidence: Confirmed from `scripts/rebuild_citations_controlled.py` and completed run states that the runner selected only `case_citations` with `target_resolution=deferred` and `metrics=deferred`. The initial case-22 comparison showed `9 -> 0` despite `case_citations=1`; root cause was `SessionLocal(autoflush=False)`, so the runner queried comparison rows before pending inserts were flushed. The runner now calls `session.flush()` before its comparison. Focused validation: `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_rebuild_citations_controlled.py -q` -> `5 passed`; combined extraction/runner validation -> `134 passed, 1 warning`. Corrected canary: `--case-id 22 --limit 1 --run-dir data\\overnight_runs\\citation-extraction-canary-20260907-recheck --apply --confirm-citation-rebuild` -> completed, `1 -> 1`, zero invalid short anchors. Five-case cohort: `--case-id 22 --case-id 23 --case-id 24 --case-id 25 --case-id 26 --limit 5 --run-dir data\\overnight_runs\\citation-extraction-cohort-20260907 --apply --confirm-citation-rebuild` -> completed with zero invalid short anchors. Case 23 gained four valid short forms; case 25 removed four historical self-resolved `RAMADANI` rows and retained its external Siloch short form. The database has `61,216` text-bearing cases. Documentation checkpoint: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

Because the controlled runner selects only `case_citations` and enforces direct short-form anchors before commit, a one-case canary and then five explicit cases can rebuild citation occurrences without invoking resolution, metrics, or other derived layers.

## Plan

1. Select one citation-bearing canonical case using a bounded read-only query.
2. Run and inspect the one-case apply canary.
3. Select four additional explicit cases and run a five-case apply cohort only if the canary passes. Complete.
4. Record artifacts and deferred resolution/metrics boundary. Complete.

## Execution Checkpoints

- Delegation: None; live write evidence must be directly verified by the manager.
- Implementation: Added the required pre-comparison flush, a nonempty-to-empty rollback guard, and bounded all-case cohort selection.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, and `.swm/4.9nn3id9f.sw.md`.
- Recovery: Baselines and state are retained before each source-case replacement.

## Completion

Completion recorded: yes.

Summary: Corrected extraction-only canary and five-case cohort passed. The all-case extraction command is prepared and intentionally not run.

Validation: Runner safety test `5 passed`; combined focused citation/runner suites `134 passed, 1 warning`; generated documentation check passed. Corrected canary and five-case cohort states/comparisons inspected directly. No target resolution, short-form resolution, metrics, statute, metadata, tag, chunk, or source write ran.

Residual risk: The all-case operation is destructive and has not run. It must remain the only database writer in its run window. Target resolution, short-form resolution, and metric recomputation remain intentionally deferred until after an accepted extraction run.

Next recommended task: Run the prepared all-case extraction-only command in a reserved writer window, inspect its durable state/baseline/comparison artifacts, then separately authorize bounded generic target resolution, short-form target resolution, and metrics.
