# SCC text chunking readiness

Status: complete
Created: 2026-09-06

Task: Prepare SCC cases for text-only enrichment by adding an SCC-specific chunking path that recovers accurate paragraph and section boundaries without changing other court chunking.
Why now: SCC HTML acquisition is blocked for many older records by access redirects, so canonical text must provide the structural fallback.
Owner surface: `scripts/chunk_cases.py`, SCC structure tests, and the V2 processing contract.
Dependencies: Canonical SCC full text, 27 stored SCC HTML snapshots, existing `backend.document_structure` SCC rules, citation/statute/tag offset contracts.
Risk boundary: No SCC corpus import or bulk enrichment in this task; no changes to FC/FCA fallback rules; no source HTML bypass or access-control changes.
Smallest falsifiable check: Stored SCC HTML/text fixtures show a stable paragraph-marker and Roman-heading pattern that the new SCC builder reproduces with exact canonical-text containment.
Acceptance criteria: SCC-specific section and paragraph chunk builder, positive/negative fixture tests, exact substring containment, stable paragraph numbering, and V2 stage compatibility; existing non-SCC chunk tests remain passing.
Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `.swm/system-map.ovnldklv.sw.md`.
Rollback/recovery: Revert only the SCC-specific chunking/test/docs changes; do not delete existing case chunks or run bulk writers until the focused check passes.
Evidence: Added SCC-only numbered/bracketed/Roman-section and unnumbered body-line fallback in `scripts/chunk_cases.py`, plus `scripts/run_scc_text_only.py`. Stored 27-case SCC sample produced exact canonical-text containment for 27/27 cases, with 2,633 paragraph chunks and 194 section chunks. Focused chunk/SCC/V2 tests passed (`15 passed`); compilation, CLI help, and a five-case no-write dry run passed. No SCC corpus import was performed.
Commit allowed: yes
Push allowed: yes
