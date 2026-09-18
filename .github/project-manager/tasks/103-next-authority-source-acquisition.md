# Task: Acquire next demand-ranked authority sources

Status: in-progress
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Acquire and dry-run the next high-frequency authority gaps: Civil Code, NOC Regulations, and a corrected Patent Act source.

Why now: Demand diagnosis ranked these authorities among the largest repeated unidentified statute forms after the accepted Indian Act, Privacy Act, and Canadian Human Rights Act checkpoint.

Owner surface: reference-library authority source snapshots and dry-run parsing

Commit allowed: yes

Push allowed: yes

Dependencies: scripts/index_legislation.py; official source endpoint verification; task 102 source-identity guard

Risk boundary: Snapshot files and read-only reports only. No PostgreSQL writes, statute backfill, authority-table indexing, or bulk case changes.

Smallest falsifiable check: Every retained source must pass title/identity validation and parse into non-empty, duplicate-free addressable units.

Acceptance criteria:

- Official source identity, URL, local path, and SHA-256 are recorded.
- Retained sources parse through the source-format-neutral parser with counts and samples.
- Wrong or ambiguous endpoints are rejected and documented rather than indexed.
- No live database writes occur.

Docs/generated references: SYSTEM_REFERENCE.md; docs/DATA_SOURCE_REGISTER.md; .swm/4.9nn3id9f.sw.md

Rollback/recovery: Delete only newly rejected snapshots/report entries; no database rollback required.

Evidence: Pending bounded acquisition and dry run.
