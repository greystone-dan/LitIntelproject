# Task: Iterative corpus-wide citation extraction quality

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Improve the whole case-to-case citation extraction method through bounded
safe fixes, progressively larger read-only corpus reports, and external AI
triage across varied FC, FCA, and SCC cases.

Why now: The five-case report exposed broad extraction problems including alias
overmatching, malformed party spans, wrapper/caption false positives, and
composite citation representation. The user wants an iterative method-level
improvement loop across different cases, not a case-specific patch.

Owner surface: `backend/citations.py` plus citation tests, extraction reports,
and AI triage artifacts.

Dependencies: existing citation extractor, five-case candidate/report builders,
AI triage script, validated case inventory, exact-offset contracts.

Commit allowed: yes

Push allowed: yes

Risk boundary: Case-to-case citations only. Preserve every occurrence and valid
duplicate. Do not suppress aliases globally, do not assume Sosa-specific rules,
do not touch statutes/tagging/metadata/chunks/schema, and do not write citation
rows during iteration. AI output is advisory, never automatic gold.

Smallest falsifiable check: On a varied read-only sample, every emitted match
must retain an exact source span; a safe precision fix must reduce confirmed
malformed/wrapper matches without reducing valid composite/short-form coverage.

Acceptance criteria:

- Safe method-level fixes are identified from varied cases, not one named case.
- Each iteration has a bounded extraction report and separate AI triage report.
- Sample sizes increase across at least three iterations.
- Exact-span validity remains 100% on each report.
- Composite citations, optional explicit aliases, derived anchors, long forms,
  short forms, and duplicates remain represented.
- AI findings are reviewed as patterns; no automatic label promotion.
- Tests and documentation record measured before/after results.

## Iteration Plan

1. Baseline varied corpus report and AI triage.
2. Apply the smallest safe general fix supported by repeated evidence.
3. Re-run report on a larger varied sample and AI triage.
4. Apply only another high-confidence method-level fix if metrics improve.
5. Final larger report, full tests, documentation, and checkpoint push.

## Reporting Cadence

Work autonomously through routine loops. Report after each meaningful measured
improvement or blocker, not after individual cases or commands.

## Evidence

Iteration 1 varied baseline: 20 cases across FC=10, FCA=5, SCC=5; 921
occurrences; kinds case=181, case_name=175, case_short=481, neutral=84; exact
spans 921/921 valid; no database writes. Iteration 2: 50 cases across FC=25,
FCA=15, SCC=10; 2,056 occurrences; exact spans 2,056/2,056 valid. Iteration 3:
100 cases across FC=50, FCA=25, SCC=25; 8,056 occurrences; exact spans
8,056/8,056 valid. Safe method fixes in `backend/citations.py` preserve
accented/Unicode party names and exclude Federal Court wrapper prefixes from
reported spans. Earlier focused validation covered 117 citation/pipeline tests;
final acceptance validation passed 108 tests across the citation and
sample-builder suites; all three reports verified read-only.

The completed AI triage report reviewed all 921 iteration-1 occurrences in 93
bounded batches and returned 778 advisory suggestions. Its issue distribution
was WRONG_SPAN=387, NONE=140, WRONG_KIND=95, UNCLEAR=86, WRONG_PINPOINT=51,
WRONG_ALIAS=19. These flags are noisy and lack reliable occurrence metadata in
some responses, so no automatic fixes or gold promotion were made. The triage
runner now uses bounded timeouts, resumable checkpoints, and three workers.

## Completion

Status: complete

Summary: Three progressively larger varied-corpus extraction reports completed;
exact-span validity remained 100%. AI triage completed as suggestion-only. No
gold promotion or corpus writes occurred.

Validation: final `pytest tests/test_citations.py tests/test_citation_sample_candidate.py -q`:
108 passed; reports verified for 20, 50,
and 100 cases with 921, 2,056, and 8,056 occurrences respectively; all exact
spans valid. AI triage completed: 93 batches, 778 suggestions, no database
writes.

Residual risk: AI triage can misclassify valid citations and cannot establish
legal truth; human review remains required for gold promotion.

Next recommended task: Review AI suggestions by occurrence ID with human-verified
fixtures before considering any additional extractor precision change.
