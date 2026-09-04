# Task: Build Cross-Court HTML Structure Matrix

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Test source-preserving HTML acquisition and structural mapping across FC, FCA, and SCC decision sources.
Why now: The clean rebuild must account for court-specific HTML wrappers, metadata layouts, headings, and decision-body structures.
Owner surface: `scripts/reacquire_source_html.py` and `backend/document_structure.py`
Dependencies: Curated FC core subset, representative FCA/SCC canonical cases, official decision iframe content URLs
Risk boundary: Bounded two-case cross-court canary; preserve original source URLs and canonical text; do not lower global confidence thresholds or bulk reacquire the inventory based on this sample.
Smallest falsifiable check: Preflight and apply one FCA and one SCC snapshot, rechunk them, and compare mapping confidence, block kinds, section labels, and exact source containment against FC canaries.
Acceptance criteria: Official FC/FCA/SCC iframe patterns are supported; source-specific differences are measured; all canary chunks remain exact canonical-text substrings; weak mappings remain fallback-only.
Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, Swimm architecture and evaluation walkthroughs, generated script catalog.
Rollback/recovery: Remove only the two cross-court canary snapshots/source records and revert the bounded acquisition changes; no bulk rollback required.
Evidence: Curated core cohort is 300 FC cases, all with canonical IDs/source URLs and initially 0 HTML snapshots. FC, FCA, and SCC official item pages return public shells while `?iframe=true` returns decision HTML containing the expected citation. Applied snapshots for FCA 2004 FCA 427 (case 35875) and SCC 2002 SCC 1 (case 35860), then added source-specific SCC parsing for `.documentcontent`, nested `SectionN` containers, numbered paragraph elements, and Roman-numeral divisions. FCA mapping confidence was 0.9961 with 91 blocks, 2 sections, and 77 paragraphs. SCC now produces 1 full-case, 5 sections, and 176 paragraphs at the `0.85` SCC gate, with 212 of 235 structural blocks mapping strongly and exact canonical-text containment for all generated rows. FC remains variable under the stricter `0.98` gate. Full regression validation follows.
