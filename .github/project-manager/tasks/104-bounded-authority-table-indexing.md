# Task: Bounded authority-table indexing

Status: complete
Created: 2026-09-17
Updated: 2026-09-17

## Task Record

Task: Index the reviewed Canadian Charter, Refugee Convention, and 1967 Protocol non-XML authority snapshots into the existing legislation authority tables with provenance intact.

Why now: The source snapshots and format-neutral parsers have passed bounded dry-run review; indexing them makes the reviewed authorities queryable without expanding into legislation versioning.

Owner surface: scripts/index_legislation.py and its focused tests

Commit allowed: yes

Push allowed: yes

Dependencies: backend.database legislation tables; backend.citations.LEGISLATION_REGISTRY; reviewed reference-library snapshots

Risk boundary: Only the three reviewed non-XML authority sources may be indexed. Do not change versioning, overwrite unrelated authority records, run bulk case changes, or perform unbounded database writes.

Smallest falsifiable check: .\\venv\\Scripts\\python.exe -m pytest tests/test_index_legislation.py -q

Acceptance criteria:

- The CLI can select and index the Charter, Refugee Convention, and 1967 Protocol using their correct source formats.
- Indexing stores source URL, local path, and SHA-256 while producing non-empty, duplicate-free authority sections.
- Existing XML indexing behavior remains covered and unchanged.
- The focused indexing tests pass.
- Canonical source-register and Swimm documentation record the indexed authority surface.

Docs/generated references: docs/DATA_SOURCE_REGISTER.md; SYSTEM_REFERENCE.md; relevant Swimm walkthrough under .swm/

Rollback/recovery: Re-run the bounded source selection after correcting the parser or remove only the three newly indexed authority documents and sections; no versioning or case-data rollback is in scope.

Evidence: Worker implementation updated scripts/index_legislation.py and tests/test_index_legislation.py. The first bounded write exposed an incorrect repository-relative path; the path was corrected and the focused test rerun passed. The three sequential bounded writes then succeeded: Charter 35 sections, Refugee Convention 44 sections, and 1967 Protocol 11 sections. Canonical documentation and the Swimm walkthrough were updated below.

## Hypothesis

If the CLI routes each reviewed source through its declared format and the existing provenance fields, the focused indexing tests will demonstrate correct non-XML parsing without changing XML behavior.

## Plan

1. Add the three reviewed source definitions and route indexing through parse_source_sections.
2. Add focused source-selection and persistence-contract tests without requiring a live bulk run.
3. Run the focused test suite, then update the source register and Swimm walkthrough.

## Execution Checkpoints

- Delegation: AI CaseLibrary Project Manager worker implemented source definitions, format routing, and focused tests; structured result returned.
- Implementation: scripts/index_legislation.py and tests/test_index_legislation.py; focused pytest passed with 7 tests.
- Documentation: docs/DATA_SOURCE_REGISTER.md and .swm/4.9nn3id9f.sw.md updated.
- Recovery: no bulk run; bounded source selection only

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-17 | Keep legislation versioning out of scope | User explicitly deferred versions | Current task request |

## Completion

Completion recorded: yes

Summary: Indexed the three reviewed non-XML authority snapshots into the legislation tables with declared format routing and preserved source provenance.

Validation: .\\venv\\Scripts\\python.exe -m pytest tests/test_index_legislation.py -q -> 7 passed; bounded indexing commands returned 35, 44, and 11 sections respectively.

Residual risk: The indexed source snapshots remain fixed reviewed snapshots; legislation versioning and broader extraction improvements remain out of scope.

Next recommended task: Improve legislation extraction coverage and resolution after this indexing checkpoint.
