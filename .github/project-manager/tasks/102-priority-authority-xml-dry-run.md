# Task: Dry-run priority authority XML sources

Status: complete
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Acquire and dry-run official XML sources for the next high-frequency authority gaps: Indian Act, Patent Act, Privacy Act, and Canadian Human Rights Act.

Why now: The demand diagnosis identified these instruments as recurring unidentified authorities and official Justice Laws XML endpoints are available.

Owner surface: reference-library authority source snapshots and dry-run parsing

Commit allowed: yes

Push allowed: yes

Dependencies: scripts/index_legislation.py; official Justice Laws XML endpoints

Risk boundary: New source files and report only. No PostgreSQL writes, statute backfill, authority-table indexing, case changes, or paid APIs.

Smallest falsifiable check: Each official XML parses into non-empty, non-duplicate section units with a source hash.

Acceptance criteria:

- Identity-verified official XML snapshots are saved for Indian Act, Privacy Act, and Canadian Human Rights Act with source URLs and hashes.
- The requested Patent Act endpoint is identity-checked and rejected because it returns the Payments for Community Development Act; it is not retained or indexed.
- Counts, sample units, duplicate identifiers, and empty-text counts are recorded.
- No live database writes occur.

Docs/generated references: SYSTEM_REFERENCE.md; docs/DATA_SOURCE_REGISTER.md; .swm/4.9nn3id9f.sw.md

Rollback/recovery: Delete only the new snapshots/report if source review rejects them; no database rollback required.

Evidence: `data/eval/priority_authority_dry_run.json` records 134 Indian Act units, 96 Privacy Act units, and 95 Canadian Human Rights Act units, all non-empty and duplicate-free. The report records the Patent Act endpoint rejection. The focused `priority_dry_run_guard` check passed; no PostgreSQL writer or authority-table indexing command ran.

## Completion

Completion recorded: yes

Summary: Three priority sources passed the bounded XML dry run. The nominal `P-4.6.xml` endpoint is not the Patent Act and remains blocked pending a correct authoritative source.

Validation: `priority_dry_run_guard=PASS` with three accepted snapshots; source identity inspection confirmed the rejected endpoint's title mismatch.

Residual risk: The accepted sources include appended or separately ordered section structures, so unit order and source version should be reviewed before live indexing. Patent Act coverage remains open.

Next recommended task: Review and approve bounded authority-table indexing for the three accepted sources, then acquire Patent Act from a verified official source.
