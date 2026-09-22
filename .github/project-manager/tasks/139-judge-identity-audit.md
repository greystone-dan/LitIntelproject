# Task: Audit judge identity and outcome alignment

Status: complete
Created: 2026-09-22
Updated: 2026-09-22

## Task Record

Task: Audit how judge identities are extracted, stored, joined, and displayed in Judge Outcomes and Judge Profile, and report suspicious identities and missing-judge coverage.

Why now: Judge Outcomes is showing false judge IDs such as `Ottawa Ontario` and `Certified true translation`, suggesting metadata extraction or downstream grouping is accepting non-person text. Judge Outcomes and Judge Profile also appear not to align.

Owner surface: Judge metadata lineage and its read-only audit/reporting path across `backend/metadata.py`, `backend/routes.py`, `backend/database.py`, and related tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Current database, judge-related routes and models, metadata extraction rules, source/provenance fields, and active Data Explorer contracts.

Risk boundary: Audit only. No judge backfill, canonical data mutation, schema change, or UI behavior change until the identity rule and counts are reviewed. Do not delete or rewrite existing metadata.

Smallest falsifiable check: A read-only corpus query/report that counts total cases, cases with no judge, distinct stored judge values, and suspicious non-person values including the reported examples.

Acceptance criteria:

- Trace the complete judge identification path from source/metadata extraction through stored fields, Judge Outcomes, and Judge Profile.
- Quantify total cases, cases with no judge, cases with one or multiple judge values where applicable, and suspicious values with reproducible criteria.
- Explain why `Ottawa Ontario` and `Certified true translation` can be treated as judges, if they are present in the live data.
- Identify the specific alignment gap between Judge Outcomes and Judge Profile and separate extraction defects from query/join defects.
- Update canonical documentation and the relevant Swimm walkthrough with the audit findings, without changing runtime behavior.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md` if applicable, `.swm/` judge/research walkthrough if present, and this task record. Generated API/schema documents are not hand-edited.

Rollback/recovery: No data recovery required. Revert only audit documentation or report artifacts if explicitly requested; preserve existing database values.

Evidence: Explore delegation traced the extraction and consumer paths in `fc_ingest/document_scraper.py`, `backend/analytics_service.py`, `backend/database.py`, `scripts/backfill_judge_profiles.py`, and related tests. Read-only audits completed against 61,261 live cases: 52,484 non-empty raw judges, 8,777 missing/blank, 31,324 profile links across 406 profiles, and 21,160 raw-judge cases without a profile link. Reported contamination is present: normalized exact `Certified true translation` occurs in 2,993 cases; values containing Ontario occur in 2,013 cases and Ottawa in 1,848. Missing judges are concentrated in A2AJ Canadian Legal Data (8,732 cases), with older RPD/FC cohorts prominent. Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` with the audit and read-only boundary. No files or database records were changed by the audit commands.

## Hypothesis

If judge identity is populated by permissive source-field extraction and the two judge views use different grouping/join paths, then non-person metadata values will appear in the stored judge population and the views will disagree even when they start from the same cases.

## Plan

1. Inventory judge extraction, storage, route, profile, and outcome paths.
2. Run a bounded/read-only corpus report with suspicious-value diagnostics and missing-judge counts.
3. Document findings, gaps, and the smallest safe remediation boundary without applying it.

## Execution Checkpoints

- Delegation: Explore agent inspected the judge extraction, profile, outcome, route, model, backfill, and test paths; returned the required structured report with no files changed.
- Implementation: No runtime implementation planned for this audit.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` with current counts, ownership boundaries, and remediation constraints.
- Recovery: Not applicable; read-only audit.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-22 | Task created | User reports false judge IDs and mismatch between Judge Outcomes and Judge Profile | Reported values `Ottawa Ontario` and `Certified true translation` |

## Completion

Completion recorded: yes

Summary: Completed a read-only audit of judge identity extraction, Judge Outcomes, Judge Profile, profile links, contamination, and missing-judge coverage. The views use different populations and the raw field contains confirmed false values.

Validation: Read-only SQLAlchemy audits completed: full population counts, exact reported-value checks, profile-link comparison, contamination diagnostics, and missing-judge court/year/source breakdown. No writes or schema changes.

Residual risk: Existing false raw judge values continue to affect Judge Outcomes, and profile links remain incomplete. The audit did not determine the correct replacement judge for each contaminated case.

Next recommended task: Design a read-only judge identity quality report and then a bounded, reversible normalization/backfill if the findings support it.
