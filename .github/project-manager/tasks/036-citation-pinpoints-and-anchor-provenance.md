# Task: Improve citation pinpoints and short-name anchor provenance

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Increase explicit pinpoint capture and preserve the full-citation anchor
for standalone short-name citations so each occurrence can be verified against
its source context.

Why now: The initial benchmark found only 97 explicit pinpoints across 1,234
occurrences. Short-name citations such as `Vavilov` are identified when they can
be anchored to a full citation elsewhere, but the created match did not retain
which full citation anchored it, making verification difficult.

Owner surface: `backend/citations.py` and citation-specific tests/benchmark
metrics only.

Dependencies: `RawCitationMatch`, short-alias anchor extraction, exact source
spans, existing citation resolution benchmark, `tests/test_citations.py`.

Commit allowed: yes

Push allowed: yes

Risk boundary: Case-to-case citations only. Preserve every occurrence,
including duplicates. Do not change statute extraction, tagging, metadata,
chunk generation, database schema, citation row persistence, or target
resolution policy except adding non-breaking provenance fields to in-memory
matches. Never invent pinpoints from paragraph markers or chunk positions.

Smallest falsifiable check: Focused tests prove a standalone short-name match
retains its anchor citation text/offset and explicit pinpoint extraction
increases only when source text contains an explicit pinpoint phrase.

Acceptance criteria:

- Long, neutral, reporter, and short-form citation paths preserve explicit pinpoint text where present.
- Standalone short-name matches retain anchor citation text and anchor offsets when anchored.
- Anchor provenance is optional and backward-compatible for existing constructors/callers.
- Every occurrence remains emitted and benchmark counts do not deduplicate.
- Tests cover anchored and unanchored short names, duplicate occurrences, exact spans, and pinpoint variants.
- A bounded benchmark reports before/after pinpoint and anchor coverage without database writes.

Docs/generated references: `SYSTEM_REFERENCE.md` or `docs/METRICS_DICTIONARY.md`
only if the public evidence/metric contract changes; update this task evidence.

Rollback/recovery: Revert only `backend/citations.py`, citation tests,
benchmark metric changes, and this task record. No database recovery required.

Evidence: Delegated and independently verified. `RawCitationMatch` now carries
optional `pinpoint`, `anchor_citation_text`, `anchor_offset_start`, and
`anchor_offset_end` fields. Explicit forms supported include `at para 100`,
`at paragraph 102`, `at paras 10-12`, `at paragraphs 20 to 22`, and `at pp.
100-102`; no inference from `[n]`, chunks, or proximity. Focused citation
regression: 108 passed, 1 pre-existing pypdf warning. Anchor benchmark update:
FC 175/175 and FCA 605/605 short-form occurrences retained valid anchor spans;
SCCmodern 0/0 due to no sampled source rows; total 780/780. Duplicate
occurrences remain individually counted. Full suite: 360 passed, 1 warning;
`git diff --check` clean. Database writes: false.

## Hypothesis

If citation matches retain explicit pinpoint phrases and anchored short-name
provenance, pinpoint/verification coverage will increase without changing
citation occurrence counts, offsets, or resolution behavior.

## Managed Execution Plan

1. Inspect current pinpoint regexes and short-name anchor data flow.
2. Add the smallest optional anchor-provenance fields and improve missed explicit pinpoint forms.
3. Add focused tests and rerun the bounded read-only benchmark.
4. Compare occurrence counts, exact spans, pinpoints, and anchor coverage.

## Reporting Cadence

Work through routine investigation and tests autonomously. Report after the
first measured improvement, any scope blocker, and final validation, not after
every file edit.

## Completion

Status: complete

Summary: Increased explicit pinpoint coverage and preserved the full-citation
anchor text and exact offsets for anchored standalone short-name citations.
Benchmark metrics now measure anchor coverage and anchor-span validity without
deduplicating occurrences.

Validation: Focused 108 passed; full suite 360 passed; bounded read-only
benchmark written to `data/eval/citation_resolution_after_anchor_036.json`;
all sampled anchor spans valid; no database rows changed.

Residual risk: SCCmodern has no source cases in the current bounded inventory.
Bracket pinpoints, undotted `p 100`, and `at page 100` remain intentionally
unsupported. Existing persisted citation rows remain pre-rebuild.

Next recommended task: Build a small reviewed citation gold set to distinguish
true ambiguous aliases from false positives before further resolver changes.
