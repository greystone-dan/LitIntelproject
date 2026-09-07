# Citation-Only Rebuild Runner

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Implement and validate a bounded, citation-only rebuild runner that preserves a recovery baseline and keeps extraction, target resolution, and metric recomputation as separate phases.

Why now: Deterministic extraction, direct short-form anchors, and alias/pinpoint preservation are covered. Existing writers cannot safely authorize a clean citation-layer replacement because they lack a complete bounded operational contract.

Owner surface: `scripts/rebuild_citations_controlled.py`

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/citations.py`, `backend/database.py`, `backend/case_processing.py`, `tests/`, and file-system run state under `data/overnight_runs/`.

Risk boundary: Do not execute a database delete/rebuild in this task. The runner must default to dry run and require an explicit write flag. It must not run target resolution or citation metrics, alter statutes/metadata/tags/chunks/cases/source records, call external services, or accept an unbounded cohort.

Smallest falsifiable check: Runner `--help` exposes explicit case IDs, a positive bounded limit, run directory, dry-run default, and explicit write mode; a mocked dry run writes a baseline and checkpoint but does not invoke the citation replacement helper.

Acceptance criteria:

- Default execution is non-mutating and requires explicit case IDs plus a positive limit.
- A dry run produces an inspectable baseline and durable per-case checkpoint/state.
- Write mode requires an explicit confirmation flag and calls only the `case_citations` stage or its citation-only helper.
- The runner prevents concurrent execution through a file lock and has a documented recovery command.
- Target resolution and metrics remain separate, uninvoked phases.
- Focused runner tests and `--help` pass.
- Canonical and Swimm documentation describe the runner and approval boundary.

Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/4.9nn3id9f.sw.md`.

Rollback/recovery: Dry-run artifacts are non-mutating. Before any future write cohort, retain the JSONL baseline and state file. On a failed write run, stop, use the completed-case checkpoint, restore source-case citation rows from baseline only through a separately validated recovery command, and do not resolve targets/metrics until replacement evidence is accepted.

Evidence: Selected a dedicated runner over extending `extract_citation_network.py` or using the multi-stage V2 runner because it makes the destructive boundary, recovery artifacts, and deferred phases explicit. Added `scripts/rebuild_citations_controlled.py` and `tests/test_rebuild_citations_controlled.py`. The runner requires explicit case IDs and a positive limit; defaults to dry run; writes `citation-baseline.jsonl` and `state.json`; uses `RunLock`; requires both `--apply` and `--confirm-citation-rebuild`; invokes only `process_case_in_five_layers(..., stage_order=("case_citations",))`; writes `citation-comparison.jsonl` before commit; and rejects invalid rebuilt short-form anchor fields. It does not call target resolution or metrics. Focused test command `& .\\venv\\Scripts\\python.exe -m pytest tests\\test_rebuild_citations_controlled.py -q` passed (`3 passed`). CLI validation `& .\\venv\\Scripts\\python.exe scripts\\rebuild_citations_controlled.py --help` passed. Generated catalog was regenerated through `scripts/generate_script_catalog.py`. Documentation checkpoint: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

A dedicated runner that accepts an explicit bounded case cohort, writes before-state JSONL and durable checkpoints, defaults to dry-run, and invokes only citation replacement under an exclusive file lock can make a future rebuild auditable and recoverable without coupling extraction to resolution or other derived layers.

## Options

1. Extend `scripts/extract_citation_network.py`: lowest initial code cost, but unsafe defaults and its broad legacy role make the destructive boundary less visible.
2. Use `scripts/run_v2_pipeline.py --stage citations`: fits current orchestration, but the V2 pipeline is designed around multi-stage cohorts and does not provide a dedicated citation baseline/recovery contract.
3. Add `scripts/rebuild_citations_controlled.py`: modest new code and tests, but the clearest explicit contract for a destructive citation-only operation. Selected for auditability, isolation, and recovery.

## Plan

1. Inspect existing run-state, lock, checkpoint, and script-test conventions.
2. Add the dry-run-first controlled runner and focused mocked tests.
3. Run help and focused tests; document the command, recovery, and unresolved approval boundary. Complete.
4. Do not run write mode or a real cohort without explicit user approval.

## Execution Checkpoints

- Delegation: Completed read-only inventory of reusable lock, state, dry-run, and baseline conventions.
- Implementation: Completed dedicated runner, focused tests, and generated script-catalog registration.
- Documentation: Completed in `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, and `.swm/4.9nn3id9f.sw.md`.
- Recovery: No database operation is authorized in this task.

## Completion

Completion recorded: yes.

Summary: The controlled citation-only rebuild runner is prepared and validated without any live database operation.

Validation: `tests/test_rebuild_citations_controlled.py -q` -> `3 passed`; `scripts/rebuild_citations_controlled.py --help` passed; generated script catalog regenerated. No database mutation ran.

Residual risk: The runner's write path is exercised only through mocks. A real citation replacement remains destructive and requires explicit approval after a reviewed dry-run cohort; generic resolution, short-form resolution, and metrics have not run.

Next recommended task: Run a user-approved small dry-run cohort, inspect its baseline/state output, then request explicit write-cohort approval. After accepted replacement, run generic resolution, short-form resolution, and metrics as separately bounded phases.
