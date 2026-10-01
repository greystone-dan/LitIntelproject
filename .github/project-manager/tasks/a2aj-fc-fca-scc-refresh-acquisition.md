# Task: Acquire and dry-run A2AJ FC/FCA/SCC refresh

Status: complete
Created: 2026-09-30
Updated: 2026-09-30

## Task Record

Task: Stage the current A2AJ FC, FCA, and SCC Parquet partitions and measure the non-mutating delta beyond the July 24, 2026 canonical baseline.

Why now: The prior read-only probe confirmed current upstream partitions but could not establish their date ceiling or exact delta.

Owner surface: A2AJ source staging and court-scoped Parquet dry-run under `data/raw/a2aj/` and `scripts/`.

Commit allowed: yes

Push allowed: yes

Dependencies: Current A2AJ Hugging Face partitions, existing Parquet importer, canonical case citation/hash baseline, and source provenance rules.

Risk boundary: Download only the three approved courts into `data/raw/a2aj/refresh-20260930/`. No RPD or other courts, no paid API, no PostgreSQL write, no `/ingest` POST, no canonical merge, and no deletion.

Smallest falsifiable check: Verify each downloaded file against the upstream linked SHA-256, inspect row/date metadata, and run the existing importer with `--court` and `--dry-run`.

Acceptance criteria:

- Only FC, FCA, and SCC are acquired and scanned.
- Downloaded file hashes match upstream metadata.
- Row counts and date maxima are recorded.
- Candidates beyond the July 24 baseline are measured without canonical writes.
- Source documentation and Swimm walkthrough record the result and remaining approval boundary.

Docs/generated references: `docs/DATA_SOURCE_REGISTER.md`, `.swm/canlaw-staging-and-models.sw.md`.

Rollback/recovery: Remove only `data/raw/a2aj/refresh-20260930/` if the staged snapshot is no longer needed. No database rollback is required because no database write occurred.

Evidence: FC, FCA, and SCC partitions downloaded with resume-enabled curl. SHA-256 values matched the upstream linked ETags: FC `EC5A82247B4B337D2A1A7E58703135DC37812059224F565B0C4B6F26A3C899B5`, FCA `454709DB060FF545E5EDE7791E76CD869A864A894A5E99D14BA768EE43E22AD7`, SCC `06FC3A9969700B5EAEFD40F79F2E099B6D932CBBF2ADCEC7FAA59935CFCA2703`.

Files changed: `.github/project-manager/tasks/a2aj-fc-fca-scc-refresh-acquisition.md`, `docs/DATA_SOURCE_REGISTER.md`, `.swm/canlaw-staging-and-models.sw.md`; staged data under `data/raw/a2aj/refresh-20260930/`.

Delegated work: None; this was the user-authorized bounded acquisition and dry-run slice following the completed probe.

Focused validation: Metadata scan reported FC `35,990` rows, newest `2026-09-25`; FCA `7,813`, newest `2026-09-24`; SCC `10,893`, newest `2026-09-18`. Existing importer dry-runs reported FC `206` candidates, FCA `33`, SCC `4`, with no writes. Date classification beyond the `2026-07-24` baseline reported FC `168`, FCA `28`, SCC `4`.

Residual risk: Candidate records include 38 FC and 5 FCA records dated before the baseline, indicating source identity or canonical coverage differences that require review. No candidate has been imported or normalized into canonical records.

Next bounded task: Review the 200 post-baseline candidates in a bounded report, validate source terms and citation/hash conflicts, then request explicit approval before any canonical import.

## Completion

Completion recorded: yes

Summary: Current FC/FCA/SCC A2AJ partitions were staged, integrity-checked, measured, and dry-run against canonical deduplication. The source contains 200 post-baseline candidates through September 25, with no canonical writes.

Validation: All three file hashes matched upstream linked hashes; metadata scans and court-filtered dry-runs passed.

Residual risk: Candidate review and canonical import remain separate approval-gated steps.

Next recommended task: Generate a bounded candidate review report for the 200 post-baseline records, including citation, decision date, source URL, full-text hash, and conflict classification.
