# Task: Fix judge identification false positives

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Tighten judge identity extraction and downstream Judge Outcomes filtering so locations, translation labels, court labels, and other metadata cannot be treated as judges.

Why now: The audit found 2,993 `Certified true translation` values, 2,013 values containing `Ontario`, 1,848 containing `Ottawa`, and 21,160 raw-judge cases without profile links. Judge Outcomes currently groups every non-empty raw value.

Owner surface: Judge identity contract: `fc_ingest/document_scraper.py`, `backend/analytics_service.py`, and focused judge metadata/profile tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing metadata extraction rules, `scripts/backfill_judge_profiles.py`, Judge Outcomes API contract, current database values, and audit task 139.

Risk boundary: Preserve source text, existing metadata, profile tables, and public response shapes. Do not run a corpus-wide write or delete judge/profile data in this task. Avoid rejecting legitimate judicial names without fixtures and review.

Smallest falsifiable check: Focused metadata tests proving known locations/document labels are rejected while valid judge forms remain accepted, plus a Judge Outcomes query test proving invalid raw values are excluded.

Acceptance criteria:

- Judge extraction rejects known non-person metadata and requires a stronger judge-name shape.
- Existing valid forms such as `Russel W. Zinn`, `Justice Brown`, and `NOËL J.A.` remain accepted.
- Judge Outcomes and profile backfill use the same validation contract.
- Focused tests pass and the touched Python files compile.
- Documentation and Swimm record the new identity rule and the fact that existing stored values require a separate backfill.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, audit task 139, and this task record. Do not hand-edit generated API/schema docs.

Rollback/recovery: Revert the code/test/documentation changes without touching database rows. Any future metadata/profile backfill must use a separate dry-run, baseline, checkpoint, and explicit approval.

Evidence: Audit task 139 established the live false-positive and missing-judge baseline. Explore delegation reviewed the bounded implementation surface with no files changed. Updated `fc_ingest/document_scraper.py` with shared junk-pattern validation, `scripts/backfill_judge_profiles.py` to reuse it, `backend/analytics_service.py` to exclude the same invalid pattern, and focused tests in `tests/test_metadata.py` and `tests/test_judge_profiles.py`. Focused suite passed: 26 tests. Compilation and `backend.analytics_service` import passed. A live read-only `fetch_judge_outcomes` check returned 100 groups / 24,657 decisions with no prohibited-term matches. Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`. No database rows were changed.

## Hypothesis

If judge validation rejects document/location vocabulary and requires a judicial name/title shape before aggregation, then the known false values will disappear from newly extracted Judge Outcomes while legitimate judge fixtures remain available.

## Plan

1. Delegate a bounded review of the existing extraction, profileability, and analytics contracts.
2. Implement the shared validation rule and focused regression tests.
3. Run focused tests and compilation, then update canonical documentation and Swimm.

## Execution Checkpoints

- Delegation: Explore agent reviewed the extraction, profileability, analytics, and test contracts; returned the required structured report with no files changed.
- Implementation: Tightened extraction/profile/outcome validation and added regression tests; no schema or data writes.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`.
- Recovery: No runtime/data recovery required; database backfill explicitly deferred.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-22 | Task created | Audit confirmed false judge values and divergent consumers | Task 139 live corpus audit |

## Completion

Completion recorded: yes

Summary: Fixed the judge identity code path for known false-positive classes and aligned Judge Outcomes with the extraction/profileability contract.

Validation: `pytest tests/test_metadata.py tests/test_judge_profiles.py -q` passed with 26 tests; all touched Python files compiled; `backend.analytics_service` imported successfully.

Residual risk: Existing stored metadata remains contaminated until a separate approved backfill; the new location list is intentionally bounded and may need additional reviewed fixtures.

Next recommended task: Run a bounded dry-run metadata/profile reconciliation report before any corpus write.
