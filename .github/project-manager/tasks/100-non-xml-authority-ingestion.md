# Task: Ingest non-XML Charter and Convention sources

Status: complete
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Support authoritative HTML/plain-text source documents for the Canadian Charter/Constitution Act and Refugee Convention/Protocol while preserving source provenance and section/article identity.

Why now: High-demand authorities do not currently have XML-backed local sections, but authoritative source material may be available as HTML or PDF/text.

Owner surface: reference-library authority indexing

Commit allowed: yes

Push allowed: yes

Dependencies: legislation_documents, legislation_sections, scripts/index_legislation.py, authoritative source URLs

Risk boundary: No case-table writes, statute backfill, external paid service, or authority claim without source hash and URL. Do not treat PDF extraction as valid until text output is checked.

Smallest falsifiable check: Parse a fixture HTML document with section/article headings and verify stable addressable units, labels, text, order, and source hash without database writes.

Acceptance criteria:

- HTML and plain-text sources can be parsed into the existing section model.
- Source URL, local path, and hash remain preserved.
- Charter and Convention/Protocol can use distinct instrument keys and article/section numbering.
- Existing XML indexing behavior remains unchanged.
- Tests cover heading parsing and malformed/empty input behavior.

Docs/generated references: SYSTEM_REFERENCE.md; docs/DATA_SOURCE_REGISTER.md; .swm/4.9nn3id9f.sw.md

Rollback/recovery: Revert the parser/test changes; no live authority rows are written in this slice.

Evidence: Added source-format-neutral HTML and plain-text parsing to `scripts/index_legislation.py`, preserving the existing XML path. The parser handles ordinary `Section`/`Article` headings and the official Justice Laws Charter structure (`p.Section`, `a.sectionLabel`, `h3.Subheading`, and provision lists). Official Charter HTML was inspected successfully; the automated UNHCR page probe returned 403, so no Convention source was acquired. Focused tests passed: `4 passed`; `py_compile` passed. No downloads, database writes, or external paid services ran.

## Hypothesis

If authoritative HTML or extracted text is normalized into the same addressable unit contract as XML, then section/article lookup can work without requiring XML-specific parsing.

## Plan

1. Add source-format-neutral parsing helpers to the legislation indexer.
2. Add fixture tests for Charter-style sections and Convention-style articles.
3. Validate parser behavior without database writes.
4. Acquire and index bounded official sources only after source review.

## Completion

Completion recorded: yes

Summary: The existing legislation section contract can accept authoritative HTML or extracted text as well as XML. Charter HTML has a stable section-anchor structure that can be parsed; Convention source acquisition remains a separate bounded step.

Validation: `tests/test_index_legislation.py -q` -> `4 passed`; `py_compile scripts/index_legislation.py` passed.

Residual risk: HTML/PDF layouts may require source-specific selectors; article/subparagraph hierarchy is not yet modeled separately.

Next recommended task: Acquire and hash a reviewed Charter HTML snapshot and a reviewed Refugee Convention/Protocol text or PDF, then run a dry-run parse report before any authority-table write.
