# Task: Establish Three-Level Case Chunking

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Make every processed case produce full-case, section, and paragraph chunk layers.
Why now: The processor already emits section and paragraph layers, but its overall layer is legacy overlapping windows rather than one complete case representation.
Owner surface: `backend/case_processing.py`
Dependencies: `scripts/chunk_cases.py`, `backend/reader_service.py`, `backend/database.py`
Risk boundary: Additive naming and processing change; preserve section/paragraph content, backend offsets, existing reader fallback behavior, and legacy standalone chunk script compatibility.
Smallest falsifiable check: Process a fixture case and verify exactly one `full_case` row plus section and paragraph rows with stable hashes and labels.
Acceptance criteria: The canonical processor has explicit full-case, section, and paragraph outputs; reader can prefer paragraph evidence while retaining all three layers; tests cover the contract.
Docs/generated references: Swimm architecture and active UI walkthroughs; `OVERNIGHT.md`; `SYSTEM_REFERENCE.md`.
Rollback/recovery: Revert the processing/reader changes; existing legacy chunk rows are not bulk rewritten by this task.
Evidence: Added the canonical `full_case` one-row layer to `backend/case_processing.py`, preserved section/paragraph processing, and switched the operational `scripts/chunk_cases.py` pending/rebuild/estimate paths to create all three layers. Reader selection prefers paragraph, then section, then full_case, with legacy compatibility retained. Rechunked only Roghangar v. Canada (case 32097) and Ou v. Canada (case 32120): Roghangar produced 1 full-case, 5 HTML-informed section, and 105 paragraph rows; OU produced 1 full-case, 6 text-fallback section, and 19 paragraph rows. Every generated row was an exact substring of canonical `full_text`. Roghangar's 115 HTML blocks mapped with document confidence `0.991`; OU had no stored HTML and correctly used fallback. Added reader `layer_spans` metadata and verified live OU citations expose full-case, section, and paragraph coordinates. Focused tests passed (`9 passed`); final full-suite validation follows.
