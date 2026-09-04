# Task: Separate legacy tag surfaces

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

Task: Make active tag readers and analytics V3-only by default while preserving V1/V2 code and rows for comparison and rollback.
Why now: V3 is wired into deterministic processing, but runtime queries can still mix legacy taxonomy rows with active V3 evidence.
Owner surface: Runtime tag visibility in reader, search, citation-map, analytics, and contextual-intelligence services.
Dependencies: `ca_legal_v3_core` taxonomy and existing CaseTag taxonomy_version column.
Risk boundary: No deletion, archival migration, file moves, or changes to V1/V2 rows. Preserve evaluation access separately.
Smallest falsifiable check: Focused reader/search/analytics tests confirm active responses exclude legacy taxonomy rows.
Acceptance criteria: Active runtime tag queries explicitly filter `ca_legal_v3_core`; V1/V2 remain queryable only through explicit legacy/evaluation paths; focused tests and compilation pass.
Docs/generated references: SYSTEM_REFERENCE.md, LEGAL_TAGGING.md, OVERNIGHT.md; generated references are not hand-edited.
Rollback/recovery: Revert query-filter changes; taxonomy rows remain intact.
Evidence:
- Added `ACTIVE_TAG_TAXONOMY_VERSION` and filtered active reader, tag-search,
	citation-map, contextual-intelligence, and inventory queries to
	`ca_legal_v3_core`.
- Preserved V1/V2 rows and implementations; no archive or deletion operation
	was performed.
- Focused validation passed: 19 tests across contextual intelligence, case
	processing, and V3 tagging.
- Python compilation and `git diff --check` passed.
Status: complete
Commit allowed: yes
Push allowed: yes
