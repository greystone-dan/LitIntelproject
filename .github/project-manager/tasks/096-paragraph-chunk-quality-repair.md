# Task: Paragraph chunk quality repair

Status: complete
Created: 2026-09-15
Updated: 2026-09-15

## Task Record

Task: Identify and repair the paragraph-chunk construction defects that prevent resolved pinpoint citations from linking to target paragraph evidence.

Why now: 86,462 of 93,854 remaining pinpoint links fall into paragraph-range gaps, 4,981 have multiple matching chunks, and 2,411 cite paragraphs outside the stored range.

Owner surface: paragraph chunk construction and its focused tests

Commit allowed: yes

Push allowed: yes

Dependencies: backend/database.py, backend/case_processing.py, backend/document_structure.py, existing paragraph-chunk tests, canonical case text

Risk boundary: Do not rerun citation extraction or target resolution, rewrite citation rows, or alter non-paragraph chunk sets. Any data repair must be dry-run first and bounded.

Smallest falsifiable check: Read-only inventory of paragraph chunk ranges and the paragraph chunk builder, followed by a focused unit test for malformed/overlapping paragraph ranges.

Acceptance criteria:

- The owning paragraph-chunk construction defect is identified with representative evidence.
- The smallest code fix prevents malformed or overlapping paragraph ranges for newly built chunks.
- Focused tests cover the repaired behavior.
- Any corpus repair is separately measured before application and does not modify citation rows.

Docs/generated references: SYSTEM_REFERENCE.md; .swm/4.9nn3id9f.sw.md

Rollback/recovery: Revert the focused chunk-builder change. Do not delete existing chunk rows or run a bulk rewrite without a bounded dry-run and explicit recovery evidence.

Evidence: Explore inventory identified `scripts/chunk_cases.py` as the owner. The HTML, fallback, and SCC builders accepted false or repeated numeric markers as paragraph IDs. The focused repair now accepts only an increasing sequence anchored at paragraph 1; rejected markers remain text chunks without paragraph identity. `tests/test_chunk_cases.py` passes `13 passed`. In-memory rebuilds of representative cases 57038, 38924, 56752, and 53295 produced no duplicate or inflated paragraph IDs. No database rows were changed.

## Hypothesis

If paragraph chunks are built from malformed HTML/text paragraph markers, then the builder is producing missing, overlapping, or inflated paragraph ranges; a focused inventory plus builder test will expose the controlling branch before any data repair.

## Plan

1. Inventory the paragraph chunk builder and representative database range anomalies.
2. Implement the smallest owning-surface repair and focused tests.
3. Run a bounded dry-run inventory and document whether a corpus rebuild is safe.

## Execution Checkpoints

- Delegation: Explore completed the bounded read-only inventory and identified `scripts/chunk_cases.py` as the owning builder.
- Implementation: Updated HTML, fallback, and SCC marker classification; focused test suite passed with `13 passed`.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `.swm/4.9nn3id9f.sw.md`, and `ROADMAP.md`.
- Recovery: No data writer authorized yet.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-15 | Task created | Residual pinpoint rows show paragraph coverage and uniqueness defects | Completed read-only linker classification: 86,462 range gaps, 4,981 multiple matches, 2,411 outside stored range |

## Completion

Completion recorded: yes

Summary: Repaired paragraph marker classification in HTML, ordinary text, and SCC text chunk builders. False citation-like years and repeated mapped markers no longer become target paragraph IDs for newly built or rebuilt chunks.

Validation: `tests/test_chunk_cases.py -q` -> `13 passed`; representative in-memory rebuild check showed empty duplicate and inflated-ID sets for four anomalous cases.

Residual risk: Existing stored paragraph chunks remain unchanged and require a separate bounded rebuild. The conservative filter assumes numbered decisions begin at paragraph 1; documents with a different numbering convention need review before broad rebuild.

Next recommended task: Run the deferred paragraph-chunk corpus rebuild from `ROADMAP.md` as a bounded dry run, compare coverage and duplicate counts, then approve or reject corpus application.
