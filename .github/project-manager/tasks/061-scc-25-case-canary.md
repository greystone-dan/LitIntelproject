# SCC 50-case canary

Status: complete
Created: 2026-09-06

Task: Run and review a representative 50-case SCC text-only enrichment canary dated 1980 or later, iterating SCC-specific chunking until the remaining cohort is ready for bounded full execution.
Why now: The SCC-specific chunker and runner passed fixture/sample validation but have not yet written all layers for a representative live cohort.
Owner surface: `scripts/run_scc_text_only.py`, SCC branch in `scripts/chunk_cases.py`, and canary evidence.
Dependencies: Canonical SCC full text, completed SCC-specific readiness checkpoint, seven-stage processing contract.
Risk boundary: Exactly 50 SCC cases dated 1980 or later selected by documented strata; no HTML acquisition; no embeddings; no target-resolution pass; no non-SCC changes; checkpointed reversible database writes only. Earlier interrupted work wrote 15 preliminary cases, including pre-1980 records; those remain untouched and are not part of this acceptance sample.
Smallest falsifiable check: The 25-case canary completes without quarantine and all generated chunk/citation/statute/tag offsets remain valid against canonical text/chunk text.
Acceptance criteria: Representative 50-case 1980-present canary, stage/output review, read-only integrity audit, focused tests, documentation/Swimm update, and explicit go/no-go recommendation for remaining SCC cases.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `.swm/system-map.ovnldklv.sw.md`.
Rollback/recovery: Use the canary run state and case IDs for review; do not delete or rewrite rows outside the selected 25 cases; stop before full cohort if any integrity gate fails.
Evidence: Fresh 50-case 1980-present cohort completed in `data/overnight_runs/scc-text-only-canary-50-20260906`: 50/50 completed, 0 quarantined, 530.3 seconds. Outputs: 2,545 chunks, 16,329 citations, 8,117 statutes, 351 V3 tags. Read-only audit found 0 malformed citation/statute offsets, 0 missing tag offsets, and all 16,329 citations explicitly unresolved as designed. Focused SCC/chunking/V2 tests passed; canonical docs and Swimm walkthroughs updated. Earlier interrupted 25-case state remains as separate historical canary evidence.
Commit allowed: yes
Push allowed: yes
