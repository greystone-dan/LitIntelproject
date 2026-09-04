# Task: Five-case reviewed citation gold-set candidate

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Generate and run a human-reviewable candidate gold set for case-to-case
citation extraction on five real cases, preserving every occurrence and exact
source evidence.

Why now: Extraction improvements need reviewed evidence to distinguish valid
citations, valid duplicates, false positives, short-name anchors, and missed
forms. The existing benchmark is quantitative but has no adjudicated labels.

Owner surface: citation extraction benchmark/fixture files only.

Dependencies: `backend/citations.py`, current five-case corpus sample,
`tests/test_citations.py`, citation benchmark scripts.

Commit allowed: yes

Push allowed: yes

Risk boundary: Case-to-case citations only. Do not send source text to an
external API, modify database rows, or touch statutes/tagging/metadata/chunks.
Candidate labels are not gold until user review confirms them. Preserve every
occurrence, including duplicates.

Smallest falsifiable check: The generated fixture has five cases, every proposed
match has an exact valid span, and rerunning extraction from each stored source
text reproduces the proposed occurrence list.

Acceptance criteria:

- Five bounded cases selected and identified by case ID/citation/court.
- Candidate fixture includes source excerpt/context, citation text, kind, normalized citation, offsets, pinpoint, anchor provenance, and review status.
- Extractor rerun reports exact-span validity and occurrence counts for all five cases.
- Fixture clearly labels proposed versus user-confirmed gold entries.
- External API option and cost assumptions documented without transmitting legal text.

Docs/generated references: this task record and fixture README/notes only.

Rollback/recovery: Delete only the candidate fixture/report/script if rejected;
no database recovery required.

Evidence: Candidate generated and verified by delegated builder, then
regenerated after the composite-citation model fix. Five cases:
FC 2026 FC 171 (case 35859, 58 occurrences), FC 2026 FC 159 (case 35858,
350), FC 2006 FC 1160 (case 35857, 34), FCA 2013 FCA 142 (case 47497, 18),
and SCC 2008 SCC 48 (case 61037, 59). The corrected fixture has 507
occurrences; all 507 exact spans are valid. Explicit forms such as `Canada
Revenue Agency v Telfer, 2009 FCA 23 [Telfer] at para 34` are one `case`
occurrence with `declared_alias=Telfer` and the pinpoint attached; the former
false second `case_short` record is gone. The same applies to Stemijon and
Vavilov. Candidate review status remains `proposed`; no external API used and
no database writes occurred. Build and `--verify` passed. Focused tests passed
(105); full suite passed (376); `git diff --check` passed. The fixture contains
bounded context excerpts, offsets, pinpoints, alias declarations, anchor
provenance, and per-occurrence review status.

## Hypothesis

A five-case candidate set with source-grounded occurrences and explicit review
status will provide a cheaper, safer adjudication surface than asking an external
API to label full decisions before the extraction errors are understood.

## Completion

Status: in-progress

Summary: Five-case candidate review surface is ready. Composite full citations
carry optional declared aliases and attached pinpoints as single records; later
short references remain separate anchored occurrences. Labels remain `proposed`
pending user review.

Validation: Candidate build and verification passed: 5 cases, 507 occurrences,
507 exact spans; 105 focused tests and 376 full-suite tests passed; no corpus
mutation.

Residual risk: Proposed labels remain unconfirmed until user review; five cases
cannot estimate corpus-wide precision/recall.

Next recommended task: User review of
`data/eval/five_case_citation_gold_candidate.json`; confirm valid/invalid,
expected kind, and missed citations. Promote only confirmed rows into a gold
fixture/test; do not label the proposed rows as truth automatically.
