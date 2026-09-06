# SCC performance optimization

Status: complete
Created: 2026-09-06

Task: Identify and reduce SCC text-only enrichment bottlenecks without reducing extraction capability, evidence offsets, or stage separation.
Why now: The 50-case SCC canary completed safely but required 530.3 seconds, materially slower than the non-SCC benchmark.
Owner surface: SCC text-only processing, citation/statute/tag extraction, and bounded runner performance.
Dependencies: Completed SCC canary state, canonical full text, existing extraction tests and V2 stage contract.
Risk boundary: Read-only profiling first; optimization must preserve exact spans, row counts, unresolved citation contract, and non-SCC behavior. No full-corpus run during optimization.
Smallest falsifiable check: In-memory stage profiling identifies the dominant SCC stage, and an optimized implementation preserves representative output counts and offset invariants.
Acceptance criteria: Profile representative SCC sizes, implement the smallest safe speedup, compare before/after counts and timings, run focused tests, update canonical/Swimm docs, and record the bounded next canary.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `.swm/system-map.ovnldklv.sw.md`.
Rollback/recovery: Revert the optimization commit; do not rewrite existing corpus rows outside a bounded benchmark.
Evidence: Baseline canary: 50 cases, 7.14M characters, 530.3 seconds, 16,329 citations, 8,117 statutes, 351 tags, zero offset failures. In-memory profiling identified `_extract_short_form_case_candidates` as the dominant SCC cost: about 85 seconds in an isolated 680k-character profile, while chunks/statutes/tags were approximately 1-2 seconds each. The retained safe optimization uses indexed nearest-anchor lookup and avoids copying the full prefix for each metadata check; it preserves the benchmark citation count (`3,684`) and passed the full citation suite (`109 passed`). A repeated 680k-character benchmark measured 23.9 seconds after the safe change. A more aggressive combined-regex experiment changed output counts and was rejected. No corpus run was launched.
Commit allowed: yes
Push allowed: yes
