# SCC 1970-present enrichment run

Status: complete
Created: 2026-09-06
Updated: 2026-09-06

Task: Complete the SCC text-only enrichment pipeline for cases dated 1970-01-01 through the present.
Why now: The SCC chunking and citation performance path passed representative canaries; the user requested excluding the oldest historical tail and the run needed a proven terminal checkpoint before closure.
Owner surface: `scripts/run_scc_text_only.py` and SCC canonical enrichment stages.
Dependencies: SCC-specific chunker, safe citation optimization, PostgreSQL writer availability.
Risk boundary: SCC only, date-filtered, no HTML acquisition, no embeddings, no target resolution, checkpointed batch writes, resumable state, no concurrent writer.
Smallest falsifiable check: The runner reports a terminal status in the state file for the exact date-filtered cohort and the final output records completed versus quarantined cases.
Acceptance criteria: The bounded 1970-present SCC run finishes with durable state and a terminal checkpoint; completion is only claimed after the state file is terminal and the run is audited.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `.swm/system-map.ovnldklv.sw.md`.
Rollback/recovery: Stop and resume from the same state directory; no destructive rollback or source deletion.
Evidence: Prior 50-case 1980-present canary passed with 0 quarantines and safe citation optimization committed in `bea7bea`. Exact cohort confirmed at 4,928 full-text SCC cases dated 1970-01-01 or later. Five-case dry run passed. Initial launch used the runner's old default limit and completed the first 100 cases with 0 quarantines. Resume reached 1,225 completed before case 53722 hung; the worker was terminated and its transaction released. The runner gained an isolated per-case process watchdog with a 600-second default timeout; the resumed run quarantined pathological cases and continued. Verified terminal status from the final run command: `status=completed processed=3703 completed=4920 quarantined=8 elapsed_seconds=26363.0` from `./venv/Scripts/python.exe scripts/run_scc_text_only.py --from-date 1970-01-01 --limit 10000 --batch-size 25 --case-timeout 600 --run-dir data/overnight_runs/scc-text-only-1970-present-20260906 --resume`.
Commit allowed: yes
Push allowed: yes

## Completion

Completion recorded: yes

Summary: The 1970-present SCC text-only enrichment run completed successfully, with 4,920 cases processed and 8 quarantined. The per-case watchdog prevented a stalled case from blocking the entire run.

Validation: `.	venv\Scripts\python.exe scripts\run_scc_text_only.py --from-date 1970-01-01 --limit 10000 --batch-size 25 --case-timeout 600 --run-dir data/overnight_runs/scc-text-only-1970-present-20260906 --resume` reported `status=completed processed=3703 completed=4920 quarantined=8 elapsed_seconds=26363.0`.

Residual risk: The quarantine list remains a review item; no expansion beyond the 1970-present boundary was attempted. The run remains bounded to the same SCC cohort with no HTML acquisition or target resolution.

Next recommended task: Audit the 8 quarantined cases and decide whether to resume any worthy follow-up, or stop at the 1970-present completion boundary.
