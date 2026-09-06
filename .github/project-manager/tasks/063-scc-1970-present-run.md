# SCC 1970-present enrichment run

Status: in-progress
Created: 2026-09-06

Task: Run the SCC text-only enrichment pipeline for cases dated 1970-01-01 through the present.
Why now: The SCC chunking and citation performance path passed representative canaries; the user requested excluding the oldest historical tail.
Owner surface: `scripts/run_scc_text_only.py` and SCC canonical enrichment stages.
Dependencies: SCC-specific chunker, safe citation optimization, PostgreSQL writer availability.
Risk boundary: SCC only, date-filtered, no HTML acquisition, no embeddings, no target resolution, checkpointed batch writes, resumable state, no concurrent writer.
Smallest falsifiable check: The runner reports the exact date-filtered cohort and a five-case dry run selects only records dated 1970 or later.
Acceptance criteria: Start the bounded 1970-present SCC run with durable state and resume support; do not claim completion until state is terminal and outputs are audited.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `.swm/system-map.ovnldklv.sw.md`.
Rollback/recovery: Stop and resume from the same state directory; no destructive rollback or source deletion.
Evidence: Prior 50-case 1980-present canary passed with 0 quarantines and safe citation optimization committed in `bea7bea`. Exact cohort confirmed at 4,928 full-text SCC cases dated 1970-01-01 or later. Five-case dry run passed. Initial launch used the runner's old default limit and completed the first 100 cases with 0 quarantines. Resume reached 1,225 completed before case 53722 hung; the worker was terminated and its transaction released. The runner now has an isolated per-case process watchdog with a 600-second default timeout, so the next resume will quarantine pathological cases and continue.
Commit allowed: yes
Push allowed: yes
