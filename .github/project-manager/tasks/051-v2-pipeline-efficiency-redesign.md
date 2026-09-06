# Task: V2 Pipeline efficiency redesign

Status: complete
Created: 2026-09-05
Updated: 2026-09-05

Task: Redesign V2 Pipeline execution to complete the approved cohort in approximately one overnight window without sacrificing checkpoints, quarantine, or evidence safety.
Why now: The first live run processed 1,786 cases in roughly 12 hours, projecting many days for the cohort.
Owner surface: V2 runner orchestration and performance architecture.
Evidence: Current runner launches a fresh isolated Python worker for every stage of every case, writes a full comparison JSON for nearly every case, performs source fetches serially, and commits each stage/case separately. The paused run preserved `state.json`, 1,784 comparison reports, and 243 quarantine records. A compact batched baseline for all 61,241 cases now exists at `data/eval/reports/v2-pipeline-before-all.jsonl`. Source acquisition now has a polite bounded-concurrency design: 2 workers and a 2-second per-host delay by default. Citation rebuild is now extraction-only with same-document short-form anchors; target resolution is a later pass.
Final extraction-only benchmark: 50 cases after ID 1832 completed in 23.0
seconds with zero quarantines; 1,688 citation occurrences were all unresolved
as required, 1,139 same-document anchors were retained, 452 statutes, 1,569
V3 tags, and 50 outcomes were persisted.
Target: Move from approximately 242 cases/hour to a measured throughput suitable for a 10-hour window; establish a benchmark before claiming the target.
Root cause found: citation extraction resolves each neutral citation occurrence with a separate database query through `resolve_neutral_to_case_id_local`. Citation-heavy cases therefore create an N+1 query storm; pure regex timings omit this cost. A diagnostic run reached `KeyboardInterrupt` inside that resolver while processing a citation stage.
Resolution: removed target-case lookup from V2 extraction; same-document anchors are retained as local provenance, and target resolution is deferred to a later corpus pass.
Recommended design:
1. Separate source acquisition from local enrichment. Use a bounded concurrent HTTP acquisition pool with per-host limits, timeout, retries, and append-only source quarantine; commit HTML in batches.
2. Replace seven process spawns per case with persistent worker processes or bounded process-pool batches. Keep hard watchdogs at batch/case boundaries, not every normal stage.
3. Run metadata, outcome, citations, statutes, and V3 tags in one case transaction after rechunking, reusing one session and loaded case/chunks.
4. Generate full before/after snapshots only for a stratified QA sample and aggregate counters for the rest. Preserve detailed quarantine evidence for failures.
5. Batch commits and checkpoint case IDs; resume only incomplete cases/stages.
6. Keep large-document HTML mapping on the bounded path and isolate very-large cases into a slower queue without blocking normal cases.
Risk boundary: No embeddings. No silent source skips. No browser-side offsets. No deletion of canonical/source rows. Existing V1/V2 rows remain untouched; V3/outcome versions remain isolated.
Smallest falsifiable check: A 500-case benchmark using the persistent/batched design reports throughput, p50/p95 case time, source-fetch rate, error/quarantine rate, and exact-span regression results against the current runner.
Acceptance criteria: Benchmark meets a documented throughput target or exposes the remaining bottleneck; state/resume/quarantine semantics remain valid; focused citation/statute/tag/outcome tests pass; docs and Swimm record the chosen execution architecture.
Rollback/recovery: Keep the paused run at `data/overnight_runs/v2-pipeline-20260904`; compare new runner outputs on a fresh bounded sample; resume old checkpoints only for audit, never concurrently.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`.
Status: complete
Commit allowed: yes
Push allowed: yes
