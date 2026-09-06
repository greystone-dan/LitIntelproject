# Task: Text-only V2 run with SCC HTML later

Status: in-progress
Created: 2026-09-05
Updated: 2026-09-05

Task: Run the V2 Pipeline with text-only section/paragraph chunking for non-SCC cases, while excluding SCC from the main run and preparing a slower SCC-only HTML acquisition path.
Why now: Most canonical text preserves usable headings and paragraph markers; SCC has distinct structure and remains the main text-only parity risk. HTML acquisition is the network bottleneck.
Owner surface: V2 runner court policy, text-only chunk selection, and SCC acquisition configuration.
Dependencies: canonical full text, existing chunk builder, source-link inventory, parity reports.
Risk boundary: Do not process SCC in the main text-only run. Do not use existing HTML for non-SCC chunking in this mode. Preserve canonical text and offsets. SCC HTML acquisition is separate, slow, resumable, and not part of the main enrichment writer.
Smallest falsifiable check: A bounded non-SCC sample produces full_case/section/paragraph chunks with `source_html` ignored; an SCC case is excluded; SCC acquisition dry-run selects only SCC rows.
Acceptance criteria: Runner supports court exclusion/text-only mode; main V2 configuration excludes SCC and uses text-only chunking for all other cases; SCC-only acquisition supports conservative delay and quarantine; docs and Swimm are updated; focused tests pass.
Rollback/recovery: Keep the paused prior run untouched; resume or restart the new policy run with a new run directory. SCC acquisition remains a separate source refresh.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/future-state.north-star.sw.md`.
Evidence:
- Parity sample shows FC/FCA text-only structure is strong; SCC remains the main structural exception.
- Runner now excludes SCC by default, ignores HTML for non-SCC chunking, and
	disables detailed snapshots during bulk mode. SCC acquisition remains a
	separate future slow path.
- Full-policy dry run completed without writes: 50,327 non-SCC full-text cases
	were examined; SCC and malformed/unsupported source-link cases were excluded;
	embeddings were excluded.
- Text-only runner tests pass: `6 passed` in the final policy check.
- Full optimized non-SCC run launched under
	`data/overnight_runs/v2-text-only-full-20260905` with batch size 50; SCC,
	malformed/unsupported sources, HTML acquisition, embeddings, and detailed
	snapshots are excluded. SCC HTML acquisition is deferred until the main
	PostgreSQL writer completes.
Status: in-progress
Commit allowed: yes
Push allowed: yes
