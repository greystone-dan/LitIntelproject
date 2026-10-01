# Task: Probe A2AJ FC/FCA/SCC refresh

Status: complete
Created: 2026-09-30
Updated: 2026-09-30

## Task Record

Task: Determine whether A2AJ currently offers additional Federal Court, Federal Court of Appeal, and Supreme Court of Canada cases beyond the local July 24, 2026 parquet population.

Why now: The corpus is incomplete and the user authorized continuing the bounded A2AJ expansion work, limited to FC, FCA, and SCC.

Owner surface: A2AJ court-scoped freshness and delta probing under `scripts/` and `canlaw/`.

Commit allowed: yes

Push allowed: yes

Dependencies: Current A2AJ public data/API contract, existing court partitions, local staging metadata, canonical source baseline, and explicit approval before any canonical write.

Risk boundary: Read-only source inspection and bounded delta measurement only. Exclude RPD and other courts. No bulk download, paid API, credential use, production write, canonical merge, deletion, or unbounded acquisition.

Smallest falsifiable check: Verify the FC/FCA/SCC filter path and run a bounded non-mutating freshness/dry-run probe that reports available/new candidate records without posting to `/ingest`.

Acceptance criteria:

- Scope is enforced to FC, FCA, and SCC only.
- Current local baseline and source freshness are measured with concrete counts/dates.
- Any newly available candidate records are reported without canonical writes.
- Existing deduplication, provenance, licence, and merge safeguards are preserved.
- Focused validation passes and canonical source documentation plus the relevant Swimm walkthrough are updated.

Harness criteria: Court scope is FC/FCA/SCC only; Baseline and freshness evidence are recorded; Probe is non-mutating; Focused validation passes; Canonical document and Swimm walkthrough are updated.

Docs/generated references: `docs/DATA_SOURCE_REGISTER.md`, `OVERNIGHT.md`, relevant A2AJ scripts, and `.swm/canlaw-staging-and-models.sw.md`.

Rollback/recovery: No source or database writes in this probe. Remove only probe artifacts if necessary; preserve logs and reports. Any future import must use a fresh bounded run directory and explicit approval.

Evidence: The delegated scoped inventory, FC dry-run, staging baseline, remote partition metadata, and documentation checkpoint were verified directly in this task. No bulk download or canonical write was performed.

Files changed: `.github/project-manager/tasks/a2aj-fc-fca-scc-refresh-probe.md`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/canlaw-staging-and-models.sw.md`
Delegated work: Explore agent assigned a read-only review of court filters, source paths, deduplication, provenance, tests, and the smallest safe probe; structured result required.
Focused validation: `python -m scripts.ingest_a2aj_parquet data/raw/a2aj/FC/train.parquet --court FC --limit 5 --dry-run` passed with `selected=35814 imported=0 skipped=35814 invalid=0`. Read-only staging query found FC `35814` newest `2026-07-24`, FCA `7785` newest `2026-07-22`, SCC `10889` newest `2026-07-24`. Remote HEAD checks returned HTTP 200 for all three current Hugging Face partitions. Focused A2AJ tests remain `3 passed` from the prior checkpoint.
Residual risk: Remote partition metadata proves current files exist but does not establish their decision-date ceiling or exact delta. A full refresh would download about 1.36 GB and requires a bounded acquisition/dry-run checkpoint, storage review, and explicit approval before any canonical PostgreSQL write.
Next bounded task: Acquire the current FC/FCA/SCC Parquet partitions into a fresh, logged staging run, inspect row/schema/date metadata, and run a 50-100-record dedup dry-run; stop before canonical import unless separately approved.

## Hypothesis

If A2AJ exposes refreshed FC/FCA/SCC data through an existing filtered source path, then a bounded non-mutating probe will identify candidate post-2026-07-24 records without changing canonical PostgreSQL state.

## Plan

1. Read authoritative source/operations guidance and consume the delegated scoped inventory.
2. Run a court-filtered, non-mutating probe and focused fixtures.
3. Record the result, update canonical and Swimm documentation, and stop before any write.

## Execution Checkpoints

- Delegation: Explore agent, read-only scoped A2AJ inventory; structured result consumed before implementation.
- Implementation: Completed read-only FC/FCA/SCC source and freshness probe; no acquisition or canonical write.
- Documentation: `docs/DATA_SOURCE_REGISTER.md` and `.swm/canlaw-staging-and-models.sw.md` updated.
- Recovery: No long-running operation planned; no bulk or paid operation allowed.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-30 | Task created | User authorized the next bounded A2AJ expansion step for FC/FCA/SCC only. | Managed-task request and prior A2AJ assessment |

## Completion

Completion recorded: yes

Summary: Current FC/FCA/SCC A2AJ Parquet partitions are available remotely, the local FC partition is stale, and local staging has an older three-court snapshot. The next step is bounded partition acquisition and dry-run comparison.

Validation: FC dry-run passed with zero new records; staging queries and remote HTTP HEAD checks were read-only; focused A2AJ tests passed 3 tests.

Residual risk: Remote date coverage and exact new-case delta remain unverified; no bulk download/import was run.

Next recommended task: Run the bounded 1.36 GB partition acquisition and 50-100-record dry-run comparison, stopping before canonical write.
