# Discussion Unit priority cohort

Status: blocked
Created: 2026-09-24
Updated: 2026-09-24

Task: Build a report-only cohort selector for general Discussion Unit labeling: include an explicit priority-case list, then up to 2,500 other cases ranked by inbound citation count, excluding non-priority cases dated before 2005.

Why now: A bounded, relevant corpus avoids the cost and noise of labeling the full inventory while preserving the cases the project has explicitly prioritized.

Owner surface: `scripts/select_discussion_unit_cohort.py` and its focused tests.

Dependencies: authoritative local `Case.date`, `CitationMetrics.in_degree` or citation-table counts, and a priority CSV containing local case IDs. The existing curated core-case CSV is the default reproducible priority input, but callers may provide the user’s final flagged list.

Risk boundary: Selection is report-only. It must not call an external model, mutate the database, embed cases, or publish model output. Priority inclusion and ranked inclusion remain separately labeled.

Smallest falsifiable check: Given synthetic cases, every explicit priority ID is present including pre-2005 cases; no non-priority case before 2005 is present; ranked additions are ordered by descending inbound count with deterministic tie-breaking; additions are capped at 2,500.

Acceptance criteria: deterministic JSON/CSV-ready cohort records; explicit priority union; 2005 cutoff for ranked additions; up to 2,500 ranked additions; duplicate suppression; inbound counts and inclusion reasons recorded; bounded projected-cost summary available from the selected count.

Docs/generated references: `SYSTEM_REFERENCE.md`; relevant Swimm walkthrough under `.swm/`; this task record. No generated reference document is edited directly.

Rollback/recovery: Delete the report artifact and revert the selector/test/documentation changes; no database state is changed.

Commit allowed: yes

Push allowed: yes

Evidence: Added `scripts/select_discussion_unit_cohort.py` and
`tests/test_select_discussion_unit_cohort.py`. Focused validation passed with
`venv\Scripts\python.exe -m pytest tests/test_select_discussion_unit_cohort.py -q`
(`2 passed`). `git diff --check` passed. The database-backed selector was run
twice after local fixes; the final optimized read-only run exceeded the
30-second bound without a summary or report artifact and was terminated. The
canonical reference and Swimm walkthrough were updated. No external model call
or database write occurred.

Blocker: The current database-backed inventory read does not complete within
the bounded execution window, so the exact selected count and projected cost
remain unverified. Resume with a database-side bounded query or an exported
candidate ledger; do not launch labeling until the cohort report exists.
