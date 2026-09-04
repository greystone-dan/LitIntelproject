# Task: Accept SCC numeric dockets in docket shape validation

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Broaden `_has_docket_shape` in fc_ingest/document_scraper.py to accept bare
4-6 digit SCC docket file numbers (e.g. `31516`) without weakening FC/FCA
`LETTERS-DIGITS-DIGITS` validation or admitting 1-3 digit numbers.

Why now: Cross-court audit showed 39/40 SCCmodern cases drop docket confidence
from 0.92 to 0.72 with `invalid_shape:docket` + `critical_below_threshold:docket`
flags even though the extracted value is correct. This depresses a critical-field
confidence signal for the whole SCC modern slice.

Owner surface: fc_ingest/document_scraper.py (`_has_docket_shape` only) +
tests/test_metadata.py (focused tests via `extract_case_metadata`).

Dependencies: backend/metadata.py re-exports `_extract_metadata_with_quality`;
scripts/_tmp_crosscourt_audit.py re-runs the SCCmodern/FCA slices (read-only DB).

Risk boundary: Do not change confidence math, `_text_label_present`, extraction
logic, `_normalize_docket_value`, or any other field's validator. Numeric
acceptance limited to `\d{4,6}` full-match (optionally `;`/`,` separated list).
No commit.

Smallest falsifiable check:
`& ".\venv\Scripts\python.exe" -m pytest tests/test_metadata.py tests/test_fc_document_scraper.py -q`

Acceptance criteria:

- `extract_case_metadata` on a realistic SCC title page ("2008 SCC 48",
  "Docket: 31516") yields docket confidence >= 0.9 and no `invalid_shape:docket`.
- Existing FC shape (`IMM-13884-24`) still passes with confidence >= 0.9.
- A 2-digit docket value still fails shape validation (`invalid_shape:docket`).
- SCCmodern audit: docket invalid_shape count -> 0, avg confidence ~0.96-0.97.
- FCA audit unchanged (no regression).
- Full suite: 341 baseline + 3 new = 344 passed.

Docs/generated references: none (throwaway audit script is the measurement;
no generated docs affected).

Rollback/recovery: revert the single-function edit and the three appended tests.

Evidence: Focused validation `pytest tests/test_metadata.py tests/test_fc_document_scraper.py tests/test_case_processing.py tests/test_contextual_intelligence.py -q` -> 33 passed, 1 pre-existing pypdf warning. Full suite `pytest -q` -> 344 passed, 1 warning. `git diff --check` clean. Cross-court audit `scripts/_tmp_crosscourt_audit.py --court all --limit 40 --low-samples 5` wrote `data/eval/metadata_audit_crosscourt_after_numeric_docket.json`: FCA docket 40/40, 1 below-threshold legacy value; SCCmodern docket 39/40 with 1 missing docket; SCCmodern numeric docket shape no longer produces invalid_shape flags. FCA critical fields otherwise 100% coverage/confidence ~0.97. Historical SCC/SCR sample remains a separate parser/access gap: docket, citation, and style metadata are absent because the legacy documents have a different unlabelled CanLII layout.

## Hypothesis

If `_has_docket_shape` also full-matches a bare 4-6 digit number, then SCC modern
cases whose docket values come from docket-labeled captures will pass shape
validation (0.92 + 0.05 = 0.97) while FC/FCA shapes and short numbers are unchanged.

## Plan

1. Edit `_has_docket_shape` only: keep existing search regex, add conservative
   fullmatch for `\d{4,6}` (allowing `;`/`,`-separated lists from normalize).
2. Append three focused tests to tests/test_metadata.py (SCC numeric pass,
   FC shape still valid, 2-digit rejected).
3. Run focused pytest, SCCmodern + FCA audits, then full suite; record outputs.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-04 | Task created | User-reported audit finding: SCC numeric dockets wrongly flagged | scripts/_tmp_crosscourt_audit.py SCCmodern slice |
| 2026-09-04 | Fullmatch-only numeric acceptance | Docket values reach the validator only from docket-labeled captures, so a bare 4-6 digit value is reliable; fullmatch keeps trailing/leading garbage invalid | fc_ingest/document_scraper.py `_extract_metadata` docket fallback + `_parse_labeled_sections` |

## Completion

Status: complete

Summary: Accepted conservative 4-6 digit numeric SCC docket values while preserving FC/FCA docket shapes and rejecting short numeric values. Added focused SCC, FC, and short-number regression tests. Cross-court audit confirms no FCA regression and the modern SCC docket problem is resolved.

Validation: 33 focused tests passed; 344 full-suite tests passed; audit report JSON validated; `git diff --check` clean.

Residual risk: Historical SCR-era SCC records remain outside this fix because their source layout lacks the modern labeled metadata blocks. One modern SCC record has no docket available in the extracted source.

Next recommended task: Move to citation extraction on the validated modern FC/FCA/SCC corpus; keep SCR-era metadata/source access as a bounded backlog item.
