# Discussion Unit priority lists

Status: complete
Created: 2026-09-23
Updated: 2026-09-23

Task: Generate two report-only case lists for Discussion Unit feature testing: the existing 300-case core layer and a 2,500-case expanded layer containing all core cases, with 500 SCC cases, 750 FCA cases, and 1,250 FC cases.

Why now: The feature work needs a stable, representative test corpus without launching an unbounded labeling run.

Owner surface: `scripts/build_discussion_unit_priority_lists.py` and its focused tests.

Dependencies: `data/eval/core_immigration_cases.csv`, local Case metadata, decision dates, court labels, and inbound citation counts from `CitationMetrics.in_degree` with a local fallback.

Risk boundary: Report-only CSV/JSON generation. No external model calls, database writes, embeddings, canonical publication, or source acquisition. Core cases remain included even if older than 2005; non-core additions must be dated 2005 or later.

Smallest falsifiable check: Generated expanded output has 2,500 unique local IDs, contains every core ID, and has exactly 500 SCC, 750 FCA, and 1,250 FC rows; no non-core row is dated before 2005.

Acceptance criteria: deterministic core and expanded CSV artifacts; explicit layer/reason fields; court quotas; core containment; inbound-count provenance; stable tie-breaking; summary JSON with counts and ranking rule.

Docs/generated references: `SYSTEM_REFERENCE.md`; relevant Swimm walkthrough under `.swm/`; this task record. Generated CSV/JSON artifacts are outputs of the new script.

Rollback/recovery: Remove generated artifacts and revert the script/tests/documentation changes; no database state changes.

Commit allowed: yes

Push allowed: yes

Evidence: Added `scripts/build_discussion_unit_priority_lists.py` and
`tests/test_build_discussion_unit_priority_lists.py`. Generated
`data/eval/llm_discussion_units_pilot/discussion_unit_core_300.csv`,
`data/eval/llm_discussion_units_pilot/discussion_unit_priority_2500.csv`, and
`data/eval/llm_discussion_units_pilot/discussion_unit_priority_2500_summary.json`.
The generator reported `core_count=300`, `expanded_count=2500`, and exact
court totals `FC=1250`, `FCA=750`, `SCC=500`. Focused tests passed with
`venv\Scripts\python.exe -m pytest tests/test_build_discussion_unit_priority_lists.py -q`
(`1 passed`). Artifact validation passed for unique IDs, core containment,
the 2005 cutoff, and ranked-addition ordering/ranks. `git diff --check`
passed. Canonical documentation and the Swimm walkthrough were updated. No
external model call or database write occurred.
