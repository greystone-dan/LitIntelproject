# Task: Improve case-citation extraction quality

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Improve deterministic case-to-case citation extraction for long forms,
neutral citations, reporter forms, short references, pinpoints, and false-positive
handling using reviewed evidence and bounded read-only benchmarks.

Why now: Extraction currently preserves exact spans, duplicates, pinpoints, and
short-name anchor provenance, but the benchmark shows high duplicate/self-citation
volume and lacks a reviewed gold set to distinguish valid repeated references
from extraction noise.

Owner surface: `backend/citations.py` and citation-specific fixtures/tests/benchmark
artifacts only.

Dependencies: existing citation benchmark reports, `tests/test_citations.py`,
`tests/test_citation_baseline.py`, `tests/test_citation_resolution_benchmark.py`,
validated FC/FCA text inventory.

Commit allowed: yes

Push allowed: yes

Risk boundary: Case-to-case citations only. Every occurrence, including valid
duplicates, must remain stored/countable. Do not touch statute extraction,
tagging, metadata, chunk generation, schema, bulk row rebuilds, or production
writes. Never infer citations or pinpoints from proximity/chunk positions.

Smallest falsifiable check: A focused fixture reproduces one measured false
positive or missed valid citation, and the smallest extraction change improves
that case without invalidating exact source spans or reducing valid duplicate
occurrences.

Acceptance criteria:

- A small reviewed fixture/gold set records expected citation spans/kinds and excluded false positives.
- One or more extraction improvements are supported by before/after metrics.
- Long, neutral, reporter, short-form, and anchored standalone-name paths remain covered.
- Exact offsets remain valid for every emitted occurrence.
- Duplicate occurrences remain preserved and separately measurable.
- Focused and full tests pass; no database rows are rewritten.

Docs/generated references: `docs/METRICS_DICTIONARY.md` only if benchmark
metrics become a durable public contract; this task record otherwise.

Rollback/recovery: Revert only citation extraction, focused fixtures/tests,
and benchmark artifacts. No database recovery required.

Evidence: Delegated review identified a concrete multi-word anchored-alias
failure: `Rexx Management` was split/truncated and `Galindo Camayo` became
`Camayo`. The extraction fix preserves full alias text, explicit pinpoints, and
anchor citation text/offsets; duplicate short-name occurrences remain separate.
Direct fixtures validated `Rexx Management` span 55:82 with anchor 0:53,
`Galindo Camayo` span 69:109 with anchor 0:67, and duplicate Rexx occurrences
as two distinct rows. Focused citation suite: 112 passed, 1 warning. Bounded
read-only benchmark after fix: 1,234 occurrences, 770 duplicates, 1,234 exact
spans, 780/780 anchored short-name spans valid, 717 unique resolutions, 420
ambiguous, 97 unresolved, and explicit pinpoints 97 -> 98; `database_writes=false`.
The aggregate sample did not contain the two motivating aliases, so its total
occurrence count was unchanged; fixture evidence is the direct proof of recall
improvement. Full regression pending.

## Hypothesis

A reviewed sample of the highest-volume extraction categories will expose one
high-value false-positive or missed-form rule that can be fixed without reducing
valid occurrence recall or exact-offset validity.

## Managed Execution Plan

1. Delegate bounded review of current citation matches and test gaps.
2. Create a compact reviewed fixture and select one extraction improvement.
3. Implement and validate the improvement against fixtures and bounded corpus.
4. Compare metrics, document residual uncertainty, and push the checkpoint.

## Reporting Cadence

Work autonomously through routine review, tests, and one coherent extraction
iteration. Report after the reviewed fixture/baseline and after each significant
measured improvement, not after routine commands.

## Completion

Status: in-progress

Summary: Fixed multi-word anchored short-name extraction without broadening to
unanchored capitalized phrases or removing duplicate occurrences. Full aliases
now retain exact source spans, explicit pinpoints, and anchor provenance.

Validation: 112 citation-focused tests passed; bounded benchmark completed with
no database writes; final full-suite validation pending.

Residual risk: Existing persisted citation rows remain pre-rebuild until the
separate approved full-pipeline rebuild task.

Next recommended task: Build a compact reviewed citation gold set containing the
motivating multi-word aliases and representative false positives before another
extraction iteration.
