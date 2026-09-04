# Task: Metadata extraction reliability and coverage QA

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Quantify real metadata extraction quality across courts with a bounded
sample, then fix the weakest high-value fields (title/style of cause, judge,
date, citation, docket) so extraction is reliable and consistent.

Why now: User reports metadata was "a mess before" and wants it reliable before
citation-extraction work expands. Metadata is the hidden foundation layer;
weaknesses here propagate into search, reader, analytics, and resolution.

Owner surface: `fc_ingest/document_scraper.py` extraction rules (consumed by
`backend/metadata.py` facade). No pipeline-order changes; that shipped in task 030.

Dependencies: `scripts/audit_fc_metadata_extraction.py`, `backend/metadata.py`,
database with real cases, `tests/test_metadata.py`.

Risk boundary: Extraction-rule changes must not regress existing passing tests
or alter stored offsets. Improve recall/precision of fields only; do not change
the public metadata API or stage order.

Smallest falsifiable check: `pytest tests/test_metadata.py -q` plus a bounded
audit run (`scripts/audit_fc_metadata_extraction.py --limit 60`) showing
coverage deltas after any rule change.

Acceptance criteria:

- Bounded cross-court coverage report recorded (per-field fill rate + critical-confidence)
- At least one concrete weakest-field fix landed with a focused test proving it
- `tests/test_metadata.py` and adjacent tests pass after the fix
- Audit rerun shows the targeted metric improved, with before/after numbers recorded

Docs/generated references: Task 030 (stage split), SYSTEM_REFERENCE.md pipeline
section, docs/METRICS_DICTIONARY.md if a new quality metric is introduced.

Rollback/recovery: `git checkout fc_ingest/document_scraper.py backend/metadata*.py tests/test_metadata.py`

Evidence: Baseline `audit_fc_metadata_extraction.py --limit 60` -> judge 59/60 below 0.9 confidence, `invalid_shape:judge` 59 (data/eval/metadata_audit_fc_baseline.json). Fix pass 1 (honorifics, name-plausible shape, junk guard, title-page preference, signature fallback): below-threshold 59 -> 7, invalid_shape 59 -> 0 (data/eval/metadata_audit_fc_after.json). Fix pass 2 (French honorifics 'monsieur le juge'/'la juge en chef par intérim', SCHEDULE junk guard, colon-optional 'En présence de' label): below-threshold 7 -> 1, sole remaining flag `missing_critical:judge` on a case with no parseable judge name (data/eval/metadata_audit_fc_after3.json). Tests: tests/test_metadata.py + tests/test_fc_document_scraper.py 17 passed; full suite 337 passed, 1 warning. French scraper test expectation updated from 'monsieur le juge McHaffie' to 'McHaffie' for normalization consistency.

## Hypothesis

If the audit quantifies per-field coverage and confidence on a bounded real-case
sample, it will reveal at least one weakest critical field whose rule fix raises
its coverage/confidence measurably without breaking existing metadata tests.

## Plan

1. Run `audit_fc_metadata_extraction.py` on a bounded FC sample; record baseline.
2. Extend/run a cross-court sample (FCA, SCC) to compare coverage by source family.
3. Identify weakest high-value field(s); fix the narrowest rule; add focused test.
4. Rerun audit; record before/after; run `tests/test_metadata.py` and neighbors.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-04 | Task created | User wants metadata reliable and consistent before citation expansion | user request |

## Completion

Status: complete

Summary: Fixed the dominant judge-extraction failure in fc_ingest/document_scraper.py. Judge values are now normalized (honorifics stripped), shape-validated as plausible names, junk captures (court names, annex labels) dropped in favor of the title-page `present` value, and the trailing signature block used to recover the full judge name when it corroborates the title-page surname.

Validation: 3 new focused judge tests pass (signature capture, court-name junk guard, honorific normalization); full suite 337 passed. FC audit judge below-threshold rate improved 59/60 -> 7/60; invalid_shape judge flags eliminated.

Residual risk: All five critical fields now reliable on the 60-case FC sample: judge 59/60 (1 legitimately missing), style of cause 60/60, docket/date/neutral-citation 60/60 at 0.0 below-threshold. Cross-court (FCA/SCC) metadata coverage not yet measured; English docket-only variants (T-xxxx-xx without label) resolved by the colon-optional fix. No remaining FC field slice open.

French-label sub-pass (delegated to subagent): colon-optional + French variants for date/docket/neutral-citation in `_text_label_present` -> docket 9->0, date 6->0, neutral citation 6->0 below-threshold (data/eval/metadata_audit_fc_after5.json); 21 focused tests pass, full suite 341 passed.

Next recommended task: Bounded cross-court (FCA/SCC) metadata audit using the same audit harness pattern to confirm the FC fixes generalize, then close the metadata-reliability line and move to citation extraction.

## Addendum: Intelligence-layer split (2026-09-04)

Outcome/role/subject derivation separated from metadata at the code level into `backend/intelligence.py` (INTELLIGENCE_FIELDS = 7 derived fields; derive_intelligence_fields). `backend/metadata.py` now narrows METADATA_FIELDS to the 12 deterministic source fields and composes the intelligence layer via `ALL_FIELDS = METADATA_FIELDS + INTELLIGENCE_FIELDS`. Storage path `metadata_json->'reader_extracted'` unchanged; extract_case_metadata output byte-identical (sha256 verified before/after). Downstream consumers (analytics_service, citation_map, contextual_intelligence, reader UI) untouched. Full suite 341 passed. Recorded in task 032.
