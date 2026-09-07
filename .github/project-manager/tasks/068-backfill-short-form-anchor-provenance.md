# Backfill Short-Form Anchor Provenance

Status: deferred
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Restore missing same-decision anchor provenance for stored `case_short` rows.

Why now: The live citation table contains `78,372` `case_short` rows missing anchor text and offsets. Under the V2 contract, every `case_short` row must have a same-decision full anchor; these rows are provenance defects, not valid unanchored citations.

Owner surface: Bounded citation-data backfill using `backend/citations.py` extraction and the `citations` table.

Dependencies: Source case text, stored citation offsets, current V2 extractor, database writer lock, checkpoint/resume support, and before/after audit output.

Risk boundary: Repair anchor text and anchor offsets only. Do not change `citation_text`, normalized citations, target-case links, unresolved status, statute references, chunks, or source offsets. Do not infer anchors from global aliases.

Smallest falsifiable check: Read-only dry-run over the `78,372` rows must reconstruct one full same-decision anchor for every row, match the stored short-form source span, and report any missing or conflicting source span before a writer is permitted.

Acceptance criteria:

- Dry-run inventories all `78,372` rows and partitions exact recoveries, conflicts, and missing source evidence.
- A write pass, if approved after the dry-run, updates only anchor fields and preserves exact source/chunk offsets.
- Post-write invariant: every stored `case_short` row has complete anchor text/start/end fields.
- Target resolution remains a separate pass; this task does not promise additional `target_case_id` links.
- The distinction from the broader unresolved population is documented: `78,372` anchor-gap rows versus `744,708` unresolved citation rows, with `60,399` unresolved rows in the anchor-gap set.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/system-map.ovnldklv.sw.md`, `.swm/blank.dudtv9pz.sw.md`, `.github/project-manager/improvements/2026-09-07-short-form-anchor-provenance-backfill.md`.

Rollback/recovery: Run the writer with a checkpoint and before/after export; restore only prior anchor columns for affected citation IDs if validation fails. Never rewrite citation text or target links as rollback.

Commit allowed: yes

Push allowed: yes

Evidence: Direct read-only count on 2026-09-07: `1,408,402` total `case_short` rows, `1,330,030` fully anchored, `78,372` missing any anchor field, and `60,399` unresolved rows missing any anchor field. No backfill write has run.

Next action: Build and run the bounded read-only dry-run; do not start the writer until exact recovery coverage and conflict counts are recorded.
