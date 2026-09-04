# Task: Reacquire HTML for Core Immigration Subset

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Validate and selectively preserve source HTML for the curated 300-case immigration core subset.
Why now: The core subset has 300/300 canonical IDs and source URLs but 0/300 stored HTML snapshots, making it the right controlled population for ingestion testing.
Owner surface: `scripts/reacquire_source_html.py`
Dependencies: `data/eval/core_immigration_cases.csv`, official Federal Court source endpoints, source terms/licence, `backend/document_structure.py`
Risk boundary: Bounded network and optional database writer; reject site shells/challenge pages; never store content without expected decision evidence; default dry-run and explicit `--apply` required.
Smallest falsifiable check: Run `--limit 5` and require valid decision HTML containing each case's expected citation before storage.
Acceptance criteria: Valid snapshots store sanitized HTML and retrieval hash/provenance, then feed confidence-gated HTML chunking; unavailable source payloads remain explicit failures.
Docs/generated references: `OVERNIGHT.md`, Swimm source/architecture walkthroughs, generated script catalog.
Rollback/recovery: Restore prior `source_html`/metadata and remove only newly created HTML source records; retain fetched artifacts outside Git when needed for review.
Evidence: Core CSV contains 300 rows, all 300 map to canonical cases, all 300 have source URLs, and none initially had source HTML. The browser showed the Federal Court decision in a same-origin `?iframe=true` content document; reacquisition now fetches that variant while preserving the original source URL. Five-case preflight passed, and five snapshots were applied with sanitized HTML, hashes, retrieval metadata, and secondary `federal_court_html` source records. Rechunked cases 1540, 1748, 4649, 16997, and 31126: each has one full-case row, exact source containment for all section/paragraph rows, and HTML mapping confidences `0.957`, `0.9939`, `0.9643`, `0.9847`, and `0.9844`. The two cases below the `0.98` gate used text fallback; the other three used HTML-informed sections. No shell snapshots remain. Full regression validation follows.
