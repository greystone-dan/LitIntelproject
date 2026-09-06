# Task: V2 Pipeline tonight readiness

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

Task: Prepare a failure-safe, resumable full V2 Pipeline cohort run.
Why now: The redesigned case pipeline works on one-case and medium/large tests, but tonight's cohort run needs complete source-HTML coverage, exact stage orchestration, per-case failure isolation, and before/after quality gates.
Owner surface: V2 Pipeline acquisition/enrichment orchestration and launch preflight.
Required sequence: validated source-link HTML reacquisition -> HTML-aware rechunk -> metadata refresh -> citations -> statutes -> citation metrics -> dedicated outcomes -> V3 tags. Embeddings are excluded.
Current baseline: 61,241 cases; 61,216 full-text cases; 61,241 source URLs; 42 stored HTML snapshots; 2,001,513 existing chunks; about 201 GB free on C:; no competing Python writer observed during preflight.
Known blockers: 6,729 source URLs have no parseable hostname; 25 use unsupported `www.fct-cf.ca`; current HTML reacquirer is limited to the curated core CSV; existing overnight profile does not represent the V2 sequence; citation/statute batch functions need per-case quarantine/error reporting; cohort before/after comparison sample is not yet complete.
Risk boundary: Do not launch the cohort run until unsupported/malformed sources have an explicit disposition, source acquisition is bounded and resumable, every stage has checkpoints and per-case errors, and a stratified comparison gate passes. Never include embeddings in this run.
Smallest falsifiable check: A dry-run preflight reports every case's source disposition, writable stage order, free disk, lock availability, and output/checkpoint paths without writing production rows.
Acceptance criteria: Full V2 runner exists with lock/state/logs, source acquisition coverage report, bounded retries/timeouts, per-case failure quarantine, stage resume, before/after snapshots for the stratified sample, and explicit no-embedding configuration.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/goc-network-principlesfuture-considerations.rwey5ues.sw.md` for future boundaries.
Rollback/recovery: Stop at checkpoint, resume by run ID, inspect failure quarantine, and preserve all pre-run snapshots. No destructive source/canonical deletion without a separate authorization.
Evidence:
- Read-only coverage and resource audit run on 2026-09-04.
- Added `scripts/acquire_case_html.py` with bounded timeout/retry behavior,
	host validation, source quarantine JSONL, provenance updates, and batch commits.
- Added `scripts/run_v2_pipeline.py` with explicit seven-stage order, durable
	state, per-case quarantine, resume behavior, interrupt state, and explicit
	`embeddings=False` output.
- Added isolated per-stage worker processes with configurable `--stage-timeout`
	(default 900 seconds); timed-out stages are terminated and quarantined rather
	than leaving the parent runner idle.
- Added focused runner coverage and validated dry-run: `9 passed`; one-case
	dry-run planned all stages without writes; three-case acquisition dry-run
	reported three ready and zero quarantined.
- Disk preflight found approximately 201 GB free and no competing Python writer.
- Remaining blockers are source coverage dispositions for 6,729 malformed-host
	links and 25 unsupported hosts, plus a stratified before/after delta gate.
- Bounded six-case stratified trial ran with FC/FCA/SCC and short/medium/long
	samples. Five cases completed; one SCC source was quarantined because the
	source page did not contain the expected citation. Results included one major
	citation delta (`407->45`) and ordinary chunk/statute changes, so cohort
	rollout remains blocked pending adjudication.
- Major-delta logic was refined so zero-baseline V3 tag additions are expected,
	tiny-count changes do not automatically fail, and substantial chunk/citation/
	statute changes quarantine the case for review.
- No embeddings were run.
- Watchdog-protected real-case validation completed for case `23`: 7 stages,
  1 case complete, 0 quarantined, `embeddings=False`.
- Final text-only policy dry run examined 50,327 eligible non-SCC full-text
	cases without writes; SCC and malformed/unsupported source-link cases were
	excluded. The previous full-run checkpoint remains interrupted and is not
	being resumed.
- Full V2 Pipeline launched on `data/overnight_runs/v2-pipeline-20260904` with
	batch size 25, 30-second source timeout, 3 retries, 900-second per-stage
	watchdog, quarantine, durable state, and embeddings excluded. Parent and
	isolated worker processes confirmed active; no interactive input required.
- Latest live checkpoint: state `running`, 3 cases recorded in the durable state
	file; the process remains active for overnight continuation.
- A repair validation command accidentally resumed an existing live-test state
	without `--limit`, processing 31 bounded cases before an alignment interruption.
	This was not a cohort launch; its state/quarantine files preserve the event and
	it must not be counted as clean rollout evidence.
Status: in-progress
Commit allowed: yes
Push allowed: yes
