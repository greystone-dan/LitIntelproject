# Task: Establish Source-Preserving HTML Structure

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Add a deterministic source-HTML structural mapper for future intelligent chunking and pretty Case Reader rendering.
Why now: Source HTML is already preserved, but the active pipeline currently consumes plain text without retaining structural blocks or source mappings.
Owner surface: `backend/document_structure.py`
Dependencies: `bs4`, `Case.source_html`, existing chunk and reader contracts
Risk boundary: Pure foundation only; do not change existing chunks, citations, statutes, tags, or database rows until mappings are integrated end to end.
Smallest falsifiable check: Parse fixtures and verify block kinds, canonical text, exact ranges, sanitization, fallback behavior, and unchanged source input.
Acceptance criteria: Produce sanitized display HTML, canonical plain text, structural blocks, HTML paths, parser version, and exact canonical-text ranges.
Docs/generated references: Swimm Architecture Decisions, Swimm Active Research UI, `docs/RESEARCH_UI_GUIDE.md`.
Rollback/recovery: Remove the new mapper and tests; no data rollback is required.
Evidence: Added `backend/document_structure.py` with deterministic HTML sanitization, structural block extraction, canonical plain-text generation, HTML paths, exact text ranges, and sequence-aligned canonical ranges with per-block confidence. Added four parser/mapping fixtures. On Roghangar v. Canada, all 115 HTML blocks mapped with document confidence `0.991`, while the HTML-derived text remained distinct from canonical metadata text. Recorded the durable requirement that inventory HTML and live DOCX/PDF adapters converge on this shared structural contract. Focused structure tests passed (`4 passed`); full suite passed (`329 passed`); `git diff --check` passed. Existing chunk, citation, statute, tag, and database behavior remains unchanged pending mapped integration.
