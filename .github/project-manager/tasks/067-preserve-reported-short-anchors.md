# Preserve Reported Short Anchors

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Preserve preferred full-form anchors when short citations are anchored to reported case citations such as `[2004] 3 F.C.R. 323`.

Why now: Unresolved `Singh` rows from older tribunal decisions have full reported authority text earlier in the same source, but stored `anchor_citation_text` is null because the extractor only promotes neutral-form full case rows to anchors.

Owner surface: `backend/citations.py` and focused citation extraction tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing case extraction regexes, stored source text, citation offset contract, and local citation-resolution tests.

Risk boundary: Preserve backend-owned offsets and source text. Add anchors only from a full case citation with a recognized reported citation; do not infer targets or change existing target links in this task.

Smallest falsifiable check: Run extraction on source case `40074` and confirm the full `[2004] 3 F.C.R. 323` authority becomes an anchor for later `Singh` rows with exact anchor offsets.

Acceptance criteria:

- Reported full case citations produce short-form anchors under the same rules as neutral citations.
- Existing neutral-anchor behavior remains unchanged.
- A focused regression test covers the reported Singh pattern and exact offsets.
- No database write is needed for validation; any later backfill is a separate bounded task.
- Canonical and Swimm documentation record the extraction fix and backfill boundary.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/blank.dudtv9pz.sw.md`, `.swm/system-map.ovnldklv.sw.md`.

Rollback/recovery: Revert only the code/test/documentation changes. Do not rewrite stored citation rows in this task; a future anchor backfill must be separately bounded and preserve offsets.

Evidence: `tests/test_citations.py -k "reported_case_anchor_for_short_form"` passed (`1 passed`); full `tests/test_citations.py` passed (`121 passed`, one existing `pypdf` ARC4 deprecation warning). Direct extraction against source cases `40074` and `45114` preserved `Singh v. Canada (Minister of Citizenship and Immigration), [2004] 3 F.C.R. 323` with exact anchor offsets. Updated `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/blank.dudtv9pz.sw.md`, and `.swm/system-map.ovnldklv.sw.md`.

## Hypothesis

If `_extract_short_form_case_candidates` treats recognized reported case rows as full anchors, then the source-40074 Singh extraction will preserve `[2004] 3 F.C.R. 323` as the preferred anchor without changing unrelated offsets.

## Plan

1. Extend reported case anchor construction using the existing reported-case parser.
2. Add an exact-offset regression test and run the focused citation suite.
3. Document the extraction rule and defer stored-row backfill to a separate read-only inventory/write decision.

## Completion

Completion recorded: yes

Summary: Reported full-form case citations now participate in preferred short-form anchor propagation, including the reported Singh authority.

Validation: Focused reported-anchor test and full citation suite passed; direct source-case extraction verified both affected Singh documents.

Residual risk: Existing stored rows remain unmodified; historical extraction rows may require a separate bounded re-extraction or anchor backfill.

Next recommended task: After the code fix passes, inventory stored short rows whose source text contains recoverable reported anchors.
