# Task: Separate main headings into paragraph chunks

Status: complete
Created: 2026-09-30
Updated: 2026-09-30

Task: Fix paragraph-layer chunking so recognized main headings are emitted as their own chunks instead of being absorbed into intro, numbered, or tail chunks.

Why now: Current paragraph splitting uses numbered paragraph markers, while main headings are only recognized by the section layer. This causes headings such as OVERVIEW, ANALYSIS, and CONCLUSION to contaminate paragraph chunk text and confuse downstream discussion/chunk consumers.

Owner surface: `scripts/chunk_cases.py` paragraph chunk builder and `tests/test_chunk_cases.py`.

Commit allowed: yes
Push allowed: yes

Dependencies: Existing section-heading regex, paragraph numbering rules, CaseChunk schema, discussion-unit heading detection, and processing pipeline chunk replacement.

Risk boundary: Change only paragraph-layer boundaries for recognized main headings. Preserve full-case and section layers, numbered paragraph identity, outro/footer handling, source text, offsets, and non-heading fallback behavior. No corpus rebuild or database write in this task.

Smallest falsifiable check: A focused chunk test must show a heading between numbered paragraphs becomes a standalone row and is absent from neighboring paragraph text.

Acceptance criteria:

- Main headings are standalone paragraph-layer chunks.
- Heading chunks retain exact source text and have no paragraph number.
- Numbered paragraphs remain separate and preserve mapped paragraph ranges.
- Existing intro, tail, SCC, HTML, and reporter-year tests continue to pass.
- Relevant Swimm walkthrough and canonical documentation are updated before completion.

Docs/generated references: `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.swm/4.9nn3id9f.sw.md`, `docs/TESTING_MATRIX.md`.

Rollback/recovery: Revert only the paragraph-builder change and its focused tests; no database rows are changed until a separately approved bounded rebuild.

Evidence: Paragraph and HTML chunk builders now emit recognized main headings as standalone `paragraph` rows with `chunk_label="heading"` and no paragraph range. Focused chunk tests passed with `14 passed`; the adjacent chunk, span-mapping, and SCC structure validation passed with `18 passed`.

Files changed: `.github/project-manager/tasks/paragraph-heading-chunking.md`, `scripts/chunk_cases.py`, `tests/test_chunk_cases.py`, `docs/TESTING_MATRIX.md`, `.swm/4.9nn3id9f.sw.md`.
Delegated work: None; this is a bounded owner-surface fix.
Focused validation: `python -m pytest -q tests/test_chunk_cases.py tests/test_layer_span_mapping.py tests/test_scc_document_structure.py` passed with `18 passed`; `py_compile` and `git diff --check` also passed. No database rebuild was run.
Residual risk: Existing stored chunks remain unchanged and may still contain absorbed headings until a separate measured rebuild. The heading regex remains intentionally limited to recognized main headings.
Next bounded task: Run a bounded measurement over representative FC/FCA/SCC cases before any chunk rebuild.
