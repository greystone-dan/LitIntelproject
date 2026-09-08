# Task: Full controlled case-citation extraction replacement

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Run the full extraction-only case-citation replacement with the controlled runner and keep it isolated from stale partial state.

Why now: The corrected extractor and runner are validated, but the prior dry-run and bulk-run attempt left a stale state boundary. A fresh all-case replacement is needed to establish a clean citation layer without reusing the failed run or broadening scope into metric/target resolution.

Owner surface: `scripts/rebuild_citations_controlled.py`

Commit allowed: yes

Push allowed: yes

Dependencies: PostgreSQL availability, current project venv, no concurrent bulk writer, active case text corpus, existing dry-run evidence, and a clean run directory.

Risk boundary: This task must not resolve targets, recompute metrics, or reuse the stale partial run state. It must preserve case-citation provenance and only replace the `case_citations` layer in the selected cohort.

Smallest falsifiable check: `./venv/Scripts/python.exe scripts/rebuild_citations_controlled.py --case-id 615 --limit 1 --run-dir data/overnight_runs/citation-rebuild-full-run-ready-20260907 --dry-run`

Acceptance criteria:

- The fresh runner completes a bounded dry run without invoking any writes.
- A fully explicit all-case apply run is started in a new directory and writes only controlled run artifacts.
- The run state remains in `case_citations` stage with `target_resolution=deferred` and `metrics=deferred`.
- No stale partial state or previous run directory is resumed.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`, `scripts/rebuild_citations_controlled.py`

Rollback/recovery: Use the dedicated run directory and lock file in `data/overnight_runs/citation-extraction-all-final-20260907`; stop the process if it stalls, retain the baseline/comparison JSONL, and do not resume the previous run. Recovery is to rerun in a fresh run directory if the current one fails validation.

Evidence: Verified the bounded dry run command succeeded: `status=dry_run cases=1 stage=case_citations resolution=deferred metrics=deferred`. The 500-case gate completed with `500` cases, `7,700` citations, and zero failures. After the first operator pause, resume progressed cleanly through roughly 29,000 more cases before stalling again on case `53722`, which held ~100% CPU with zero checkpoint progress for 12+ minutes; a soft interrupt did not reach the child process, so it was force-terminated and confirmed rolled back to its exact pre-run baseline. A second recovery defect was found during that pause: the resume walk stopped at the first case lacking comparison/checkpoint evidence even when later cases had journal evidence and the gap case already had an operator-recorded terminal status; fixed so a recorded terminal status passes through instead of halting recovery, preventing a ~29,000-case redundant re-extraction. Regression test added and passing: `tests/test_rebuild_citations_controlled.py`: `8 passed in 1.57s`. Verified cursor after the fix: `53,757` committed, case `53,758` next, two cases (`24480`, `53722`) explicitly skipped with recorded reasons. Canonical documentation updated: `OVERNIGHT.md` and `SYSTEM_REFERENCE.md`.

Final evidence: `data/overnight_runs/citation-extraction-all-live-20260907/state.json` records `status=completed`, `completed=61212`, and `skipped=4`. The skipped case IDs are `24480`, `53722`, `56686`, and `56973`. This terminal checkpoint supersedes the earlier in-progress cursor. Future full-pipeline runs must use the controlled runner and preserve separate resolution and metrics phases.

## Hypothesis

If the corrected controlled runner and extractor are valid, a bounded dry run will report a clean state and the fresh all-case apply run will progress under a new directory without touching stale run state.

## Plan

1. Validate the runner with a one-case dry run using the same explicit cohort pattern.
2. Start the fresh all-case `case_citations` rebuild in a new directory with the required lock and directional guardrails.
3. Confirm the state file and outputs reflect the fresh run and defer target resolution and metrics.

## Execution Checkpoints

- Delegation: none; direct validation and run execution are bounded to the controlled runner.
- Implementation: run the bounded dry-run and the full all-case apply command in a new run directory.
- Documentation: canonical repository path `OVERNIGHT.md`; Swimm path `.swm/4.9nn3id9f.sw.md`.
- Recovery: `data/overnight_runs/citation-extraction-all-final-20260907` and its lock/state files.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Task created | Fresh extraction-only rebuild required after validation and stale-run risk | Extractor and runner had passing canary checks before the full run |
| 2026-09-07 | 10-case batches with skip logging | Compact output requested; timed-out batches must not hang the run | 25-case validation printed `Cases Processed [10] - [225]`, `[20] - [330]`, `[25] - [347]` |
| 2026-09-07 | 500-case validation launched | Gate before all-case replacement | Fresh dir `citation-progress-500-case-20260907`, 50 batches of 10, 240s per-batch timeout |
| 2026-09-07 | Full run paused at user request | Terminal appeared frozen at its last ten-case progress line | Reconciled cursor: 24,433 committed cases, 509,213 citations, next case ID 24,480; no active writer |

## Completion

Completion recorded: yes

Summary: The controlled full replacement completed for the frozen 61,216-case cohort, with 61,212 commits and four explicit skips.

Validation: Final state reconciliation -> `status=completed`, `completed=61212`, `skipped=4`; interrupted-case rollback -> `exact_snapshot_match=True`; focused runner tests passed.

Residual risk: Four cases remain explicitly skipped. Future full-pipeline runs must use the controlled runner and retain separate target-resolution and metrics phases.

Next recommended task: Preserve the controlled runner as the required full-pipeline citation extraction path.
