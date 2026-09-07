# Short-Form Anchor Provenance Backfill

Status: deferred follow-up

## Observation

The V2 invariant is `case_short exists => full same-decision anchor exists`, but the live `citations` table currently contains `78,372` short-form rows missing anchor text and offsets. The corpus has `1,408,402` `case_short` rows total and `1,330,030` fully anchored. Of the `78,372` anchor-gap rows, `60,399` are unresolved.

## Why It Matters

This is a provenance and auditability defect, not primarily a target-resolution defect. A bare source mention such as `Singh` may retain a normalized label while losing the full authority and exact anchor offsets that explain why it was extracted. The gap is material but is not the majority of unresolved citations: `78,372` anchor-gap rows versus `744,708` unresolved citation rows at the current checkpoint.

## Recommended Slice

Run a read-only, checkpointed dry-run that re-extracts each affected source case, matches the stored short-form offset, and reconstructs the full same-decision anchor. Partition exact recoveries, source-span conflicts, and missing evidence. Only after review should a bounded writer update anchor fields alone.

## Guardrails

- Do not use global alias matching or fuzzy matching.
- Do not alter citation text, normalized citation, target links, unresolved state, statute references, chunks, or source offsets.
- Preserve the distinction between local anchor provenance and canonical target resolution.
- Treat any row that cannot be reconstructed as a backfill failure requiring investigation, not as a valid unanchored short citation.

## Evidence

The count came from a direct read-only SQLAlchemy query on 2026-09-07. No data was modified.
