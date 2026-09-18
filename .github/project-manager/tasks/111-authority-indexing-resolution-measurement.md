# Task: Authority indexing and resolution measurement

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Verify indexed legislation coverage and measure read-time statute resolution before considering any extraction rerun.

Why now: Newly indexed authority sections can improve resolution automatically, but the current system does not persist resolution status. The next safe step is to measure the live coverage and index only approved local sources that are already available.

Owner surface: legislation authority indexing and read-time resolution measurement

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/database.py`; `backend/citations.py`; `scripts/index_legislation.py`; local reviewed authority files; task 099 coverage inventory

Risk boundary: Read-only measurement first. Index only already-reviewed local sources with explicit bounded commands. No external downloads, extraction reruns, corpus backfills, case-row writes, schema changes, or production jobs.

Smallest falsifiable check: A read-only report can identify indexed documents and classify a bounded sample of stored statute references by read-time resolution status.

Acceptance criteria:

- Verify the current indexed document and section set from the configured database.
- Produce a bounded resolution-status report for stored statute references.
- Identify local reviewed sources that are present but not indexed.
- Index only those sources if the existing script and provenance checks support a bounded operation.
- Re-measure resolution impact and document the result.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/4.9nn3id9f.sw.md`; `ROADMAP.md`

Rollback/recovery: Do not alter case or statute-reference rows. If authority indexing is performed, remove only the task-created authority document/section rows using the existing script's documented replacement path; preserve source files and logs. Stop before any source acquisition or schema change.

Evidence: Delegated read-only inspection confirmed deterministic replace-on-index behavior and the available resolution statuses. Direct read-only ORM inventory found all 14 approved authority documents already indexed with 4,522 sections; no reviewed local source was pending indexing. The database contains 751,944 statute references. A bounded sample of 1,000 non-null-instrument references produced 561 `resolved_section`, 389 `missing_section`, 24 `section_not_indexed`, 22 `document_not_indexed`, and 4 `range_or_list_not_resolved` results. The missing-document population in the sample was `canada.immigration_act`, which requires a separate source decision. No database writes, extraction rerun, source acquisition, or corpus backfill ran. Canonical documentation: `SYSTEM_REFERENCE.md`; Swimm walkthrough: `.swm/4.9nn3id9f.sw.md`; roadmap: `ROADMAP.md`.

## Hypothesis

If approved local authority sources are indexed and existing stored references are resolved at read time, then resolution coverage will improve without re-extracting or rewriting statute references.

## Plan

1. Delegate a read-only inspection of indexing inputs and resolution/reporting seams.
2. Run bounded read-only document and resolution inventory.
3. Index only approved local sources that are present and not already indexed.
4. Re-measure resolution and update canonical/Swimm documentation.
5. Run focused tests, review task-owned diff, commit, and push.

## Completion

Completion recorded: yes

Summary: Completed authority indexing verification and bounded read-time resolution measurement; no pending local indexing job was found.

Validation: Read-only document inventory and 1,000-reference resolution sample completed; focused authority/parser tests remain green from task 110.

Residual risk: Read-time resolution metrics may reflect parser identity gaps and range/list limitations rather than authority-source absence.

Next recommended task: Build a resolution metrics/reporting surface or classify the `missing_section` and `document_not_indexed` populations before changing resolver behavior.
