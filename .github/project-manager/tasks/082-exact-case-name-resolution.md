# Task: Exact case-name target resolution

Status: complete
Created: 2026-09-07
Updated: 2026-09-07

## Task Record

Task: Examine the 404,342 unresolved non-short citations and recover precision-safe `case_name` targets, starting with the measured unique exact-alias class.

Why now: `case_name` rows account for 347,601 (85.97%) of unresolved non-short citations. The current formal resolver skips rows without citation variants even when one exact canonical local alias exists.

Owner surface: `scripts/resolve_citation_targets.py`

Commit allowed: yes

Push allowed: yes

Dependencies: Completed full extraction replacement, completed formal/neutral pass, current unresolved report excluding `case_short`, PostgreSQL availability, and no competing database writer.

Risk boundary: Resolve only a unique non-self local case target supported by deterministic normalized identity. Do not use fuzzy matching, modify extraction or offsets, resolve short forms, or infer an authority absent from the local inventory.

Smallest falsifiable check: `& .\venv\Scripts\python.exe -m pytest tests\test_citations.py -k "case_name_target or title_year_target" -q`

Acceptance criteria:

- Recover the unique exact-alias `case_name` class without formal citation variants.
- Leave self matches, collisions, and absent-inventory names unresolved.
- Produce a bounded dry-run count and a refreshed non-short unresolved breakdown.
- Update `SYSTEM_REFERENCE.md` and `.swm/4.9nn3id9f.sw.md` with measured evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, `.swm/4.9nn3id9f.sw.md`, `data/eval/reports/unresolved_citation_shapes_excluding_short_20260907.json`

Rollback/recovery: Before apply, record candidate citation IDs and target IDs. Any incorrect class can be reverted by setting only those recorded citation IDs back to `target_case_id=NULL, unresolved=true`. Apply requires a fresh focused test and dry-run count.

Evidence: Starting baseline was 404,342 unresolved non-short rows: 347,601 `case_name`, 53,078 `case`, and 3,663 `neutral`. The delegated read-only audit found 14,051 `case_name` rows with one exact non-self canonical-title target, 9,735 self-only rows, 1,746 self-plus-one rows, 10,207 collisions, and 311,862 absent exact title keys. It inspected `scripts/resolve_citation_targets.py`, `scripts/report_unresolved_citation_shapes.py`, `backend/citations.py`, `tests/test_citations.py`, and the filtered report; it changed no files and reported one corrected read-only probe failure.

Focused tests passed (`3 passed`), the full citation module passed (`143 passed`), and the dry run reported exactly `14,051` links. The rollback artifact `data/eval/reports/case_name_exact_resolution_mapping_20260907.jsonl` contains all proposed IDs and targets. The apply pass inspected 347,601 rows and linked 14,051. Post-apply verification found `14,051 matched`, `0 wrong`. The refreshed report records 390,291 unresolved non-short rows, including 333,550 `case_name`; only 11 unique-alias signals remain and none are `case_name`. Canonical documentation: `SYSTEM_REFERENCE.md` and `OVERNIGHT.md`; Swimm walkthrough: `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

If the resolver evaluates normalized full case-name identity independently of formal citation variants, it will uniquely resolve the measured exact-alias class while tests keep self, ambiguous, and absent-inventory names unresolved.

## Plan

1. Measure and sample exact unique-alias candidates against canonical case titles.
2. Add a narrow deterministic case-name resolver and focused tests.
3. Run a bounded dry run, apply only after validation, then regenerate the filtered report and document evidence.

## Execution Checkpoints

- Delegation: bounded read-only inventory of unresolved `case_name` normalization gaps; structured return required.
- Implementation: `scripts/resolve_citation_targets.py` and focused tests in `tests/test_citations.py`.
- Documentation: `SYSTEM_REFERENCE.md`, `OVERNIGHT.md`, and `.swm/4.9nn3id9f.sw.md`.
- Recovery: candidate mapping artifact under `data/eval/reports/` before any apply run.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-07 | Start with unique exact aliases | Highest-confidence measurable recovery class; fuzzy matching is outside the risk boundary | Filtered report identifies 14,062 rows |

## Completion

Completion recorded: yes

Summary: Added and applied strict exact canonical-title recovery for name-only `case_name` rows, with a kind filter for bounded execution and an exclusion filter for unresolved reporting.

Validation: `tests/test_citations.py` passed (`143 passed`); dry run and apply both reported `14,051` links; post-apply mapping verification reported `14,051 matched`, `0 wrong`; the refreshed non-short report totals `390,291`.

Residual risk: `365,617` non-short rows have no exact local signal. Sampled designation rewrites recover only hundreds and introduce collisions, so they were not applied. Inventory absence must not be replaced by fuzzy name matching.

Next recommended task: Review a bounded gold set for the 635 potentially unique designation-normalization candidates before adding any rewrite rule.
