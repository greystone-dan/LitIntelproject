# Task: Case citation extraction, resolution, and pinpointing

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Make case-to-case citation intelligence trustworthy across the validated
FC, FCA, and modern SCC corpus by improving citation extraction, database-wide
target resolution, and exact pinpointing without rebuilding the corpus until
all three areas are approved.

Why now: Citation extraction is only one part of the problem. Resolution and
pinpointing depend on the full case inventory, canonical identities, citation
aliases, source text, chunk layers, and existing database relationships. The
chunking and metadata improvements are not yet applied across the inventory.

Owner surface: `backend/citations.py` plus citation-specific benchmark and test
fixtures. Database resolution contracts may be inspected and minimally adapted
only when required by the citation owner surface.

Dependencies: `backend/database.py`, `backend/case_processing.py`, persisted
case inventory, canonical `Case` identities, `CaseChunk` offsets, existing
citation rows, `tests/test_citations.py`, and bounded read-only benchmark tooling.

Commit allowed: yes

Push allowed: yes

Risk boundary: Case-to-case citations only. Statute/instrument extraction,
tagging, metadata extraction, chunk regeneration, embeddings, bulk citation
rewrites, schema migrations, and production corpus rebuilds are out of scope
until separately approved. Never replace backend-owned offsets with browser or
locally invented offsets. Keep extraction, resolution, and pinpointing as
separate measurable operations.

Smallest falsifiable check: Run a read-only bounded benchmark on existing
`Case.full_text` for FC, FCA, and modern SCC and verify extracted citation spans
are exact slices of the input text while reporting resolution and pinpoint
availability without changing database rows.

Acceptance criteria:

- A frozen case-citation fixture/gold set covers long-form, short-form, FC/FCA/SCC/SCR/CanLII citations, quoted citations, self-citations, and false positives.
- Extraction reports exact source offsets and does not emit statute references into the case-citation layer.
- Resolution is tested separately against the complete current case inventory, including neutral-citation identity, aliases, short forms, unresolved targets, and duplicate/ambiguous matches.
- Pinpointing is tested separately and preserves canonical source/chunk offsets; chunk-level evidence is not claimed when the database lacks a matching chunk.
- A bounded read-only corpus benchmark reports extraction count, exact-offset validity, duplicate rate, self-citation rate, unresolved rate, ambiguous rate, and pinpoint availability by court.
- No case, chunk, citation, statute, tag, embedding, or metadata rows are rewritten during development iterations.
- Only after extraction, resolution, and pinpointing acceptance checks pass is a separate rebuild task proposed.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/TESTING_MATRIX.md`,
`docs/METRICS_DICTIONARY.md`; update only after behavior or workflow changes.

Rollback/recovery: Revert only citation-owner code, focused fixtures, benchmark
scripts, and task documentation. Do not delete or rewrite corpus rows during
this task.

Evidence: Milestone 1 baseline: read-only
`scripts/benchmark_case_citations.py --courts FC FCA SCCmodern --limit 20`
reported FC 307 matches (178 duplicate occurrences, 89 self-citations), FCA
927 matches (592 duplicates, 258 self-citations), SCCmodern 0 sampled rows;
all 1,234/1,234 spans exact and `database_writes=false`. Milestone 2/3:
alias resolution now gathers candidate IDs, resolves only one distinct
candidate, and leaves duplicate aliases unresolved instead of selecting
`ORDER BY id LIMIT 1`. Milestone 4: `RawCitationMatch` now carries optional
explicit pinpoint text (`at para`, `at paras`) without changing citation text,
offsets, resolution, or occurrence storage. Final read-only benchmark:
1,234 occurrences, 770 duplicate occurrences, 1,234 exact spans, 717 unique
resolutions, 420 ambiguous, 97 unresolved, 97 explicit pinpoints;
`database_writes=false`, target inventory 61,241. Focused tests 103 passed;
full suite later 354 passed before benchmark-only metric correction; after the
correction 89 focused tests passed and `git diff --check` passed. No database
rows changed.

## Hypothesis

If extraction, database-wide resolution, and pinpointing are benchmarked as
separate operations on the existing inventory, the highest-impact case-citation
failure can be improved and measured without relying on stale rebuilt rows or
mixing statutes into the case-citation layer.

## Managed Execution Plan

### Milestone 1: Read-only inventory and baseline

Delegate a bounded inspection of citation entry points, database resolution
queries, chunk/offset contracts, existing tests, and current inventory counts.
Produce a baseline report without editing production rows or rebuilding anything.

### Milestone 2: Extraction quality

Improve the pure case-citation extractor against fixtures and reviewed excerpts.
Validate exact spans, citation-family coverage, false positives, and self-citation
handling. Re-run only the extraction benchmark.

### Milestone 3: Resolution quality

Test resolution against the complete current case inventory using canonical
neutral citations, aliases, short forms, duplicate candidates, and unresolved
cases. Keep resolution separate from extraction and do not silently select an
ambiguous target.

### Milestone 4: Pinpoint quality

Validate source offsets against canonical `Case.full_text` and persisted chunk
rows. Report missing/stale chunk evidence explicitly. Do not regenerate chunks
or rewrite citation rows in this task.

### Milestone 5: Acceptance checkpoint

Compare baseline and improved metrics by court. Only then create a separate,
explicitly approved rebuild task for the full ordered pipeline:
`full_case -> heading_chunks -> metadata -> case_citations -> statutes -> tags`.

## Reporting Cadence

Work autonomously through routine inspection, bounded tests, and one coherent
improvement at a time. Report after the baseline, each significant measured
improvement, any blocker or scope-boundary decision, and final acceptance. Do
not report after every file or routine command.

## Stop Conditions

Stop and record a blocker if a change requires statute/tagging work, a schema or
migration decision, unbounded database writes, corpus rebuild, production access,
new source acquisition, or a product decision about precision versus recall.
Stop after two iterations without measurable improvement and report the evidence.

## Delegation Contract

Delegated agents may inspect and edit only their assigned citation owner surface
and explicitly allowed tests/benchmark files. They must not edit task records,
commit, push, rebuild rows, or decide acceptance.

Required delegated return:

```text
Files inspected:
Files changed:
Commands run:
Results:
Failures:
Uncertainty:
Recommendation:
```

## Completion

Status: in-progress

Summary: Baseline established and first trust improvement landed: ambiguous
case-alias resolution no longer silently links to an arbitrary case. Extraction
and resolution remain separate in development; statutes and tagging remain
out of scope.

Validation: Read-only benchmark JSON at
`data/eval/citation_baseline_035.json`; focused citation tests and broader
citation verification tests passed (95); no corpus writes.

Residual risk: Existing baseline does not measure database-wide resolution or
pinpoint availability because the pure match API lacks explicit pinpoint data.
SCCmodern has no sampled rows in the current inventory. Persisted chunks,
citations, and derived metrics remain pre-rebuild.

Next recommended task: Review citation benchmark false positives and ambiguous
aliases using a small gold set, then improve resolution/pinpoint semantics only
where the measured evidence supports it. Keep statutes, tagging, and corpus
rebuild as separate later tasks.
