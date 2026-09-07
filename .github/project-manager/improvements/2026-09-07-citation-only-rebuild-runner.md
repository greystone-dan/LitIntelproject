# Citation-Only Rebuild Runner

Status: deferred follow-up

## Observation

The extractor is ready for an extraction-only citation rebuild, but no current bulk writer provides the operational controls required for a destructive citation-layer replacement. `scripts/extract_citation_network.py --cases` has batch commits and an ID resume point, but no explicit case-ID cohort, dry run, baseline export, durable checkpoint, exclusive writer lock, or post-run comparator. `scripts/run_overnight.py` and the V2 runners combine citation work with other derived layers; the A2AJ resumable extractor also updates case metadata markers.

## Why It Matters

A clean citation rebuild must replace only `citations`, preserve source text and all non-citation derived layers, remain recoverable if a cohort shows unexpected count or span deltas, and defer both target resolution and metrics to later bounded phases. Existing runners do not provide sufficient evidence or recovery controls for that operation.

## Recommended Slice

Add a citation-only runner with explicit case IDs and a small limit, an exclusive writer lock, pre-delete per-case citation baseline exports, durable per-case checkpoints, dry-run/preflight mode, extraction using `resolve_targets=False`, and post-run count/span/anchor comparisons. Keep generic target resolution, short-form target resolution, and citation-metric recomputation as separate bounded commands after accepted extraction evidence.

## Coordinate Contract

For chunk-linked citations, occurrence `offset_start`/`offset_end` are relative to the linked chunk; short-form anchor offsets are document-relative and are verified against the source case text. Pinpoints are retained in `citation_text` and `normalized_citation`; the current `Citation` schema has no separate pinpoint column.

## Evidence

On 2026-09-07, focused `tests/test_citations.py` passed with `128 passed, 1 warning`; targeted rebuild persistence and coordinate checks passed with `2 passed, 126 deselected, 1 warning`. A read-only processing audit confirmed `rebuild_citations_for_case` deletes only citations for its source case and defers target resolution. No database operation was run.
