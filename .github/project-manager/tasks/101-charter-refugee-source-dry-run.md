# Task: Dry-run Charter and Refugee Convention sources

Status: complete
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Acquire bounded authoritative source snapshots for the Charter/Constitution Act and Refugee Convention/1967 Protocol, then parse them into addressable units for review without writing authority tables.

Why now: The source-format-neutral parser is ready, and these high-demand instruments lack local indexed authority text.

Owner surface: reference-library authority source acquisition and dry-run parsing

Commit allowed: yes

Push allowed: yes

Dependencies: scripts/index_legislation.py; official Justice Laws and UNHCR/UN treaty source material

Risk boundary: Snapshot/report only. No live database writes, statute backfill, reader links, or paid APIs. Preserve source URLs, retrieval metadata, hashes, and source terms.

Smallest falsifiable check: A dry-run parse produces non-empty, correctly numbered Charter sections and Convention/Protocol articles with valid text and source hashes.

Acceptance criteria:

- Charter source snapshot is official and produces addressable section units.
- Refugee Convention and Protocol source snapshot is authoritative and produces addressable article units.
- Counts, examples, empty/duplicate units, source URLs, and hashes are recorded.
- No authority-table or case-table writes occur.
- User can review the report before indexing.

Docs/generated references: SYSTEM_REFERENCE.md; docs/DATA_SOURCE_REGISTER.md; .swm/4.9nn3id9f.sw.md

Rollback/recovery: Delete only the new snapshots/report if source review rejects them; no database rollback required.

Evidence: Saved the official Justice Laws Charter HTML snapshot and official UN Treaty Series PDFs for the 1951 Convention and 1967 Protocol. Derived UTF-8 text snapshots from both PDFs. The dry-run report `data/eval/non_xml_authority_dry_run.json` records source URLs, hashes, sizes, and sample units. Results: Charter 35 units (`1` through `34`, including `16.1`); Convention 44 articles (`1` through `46`); Protocol 11 Roman-numbered articles (`I` through `XI`). All have zero duplicate identifiers, zero empty texts, and no parse errors. No database writes or statute backfill ran.

## Hypothesis

If the official Charter HTML and an authoritative Convention/Protocol text can be normalized into the parser contract, then section/article lookup can be added without requiring XML or changing statute extraction.

## Completion

Completion recorded: yes

Summary: The Charter, 1951 Refugee Convention, and 1967 Protocol can all be represented as addressable non-XML authority units. The report is ready for review before live authority-table indexing.

Validation: `tests/test_index_legislation.py -q` -> `5 passed`; `py_compile scripts/index_legislation.py` passed; dry-run report has no duplicate or empty units.

Residual risk: Source access, page layout, treaty language/version, and article/subparagraph hierarchy require review before indexing.

Next recommended task: Review `data/eval/non_xml_authority_dry_run.json`, then approve a bounded authority-table indexing pass with distinct instrument keys for the Charter, Convention, and Protocol.
