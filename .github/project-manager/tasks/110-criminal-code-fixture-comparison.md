# Task: Criminal Code source-backed fixture comparison

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Compare Criminal Code extraction spans and stored-section resolution against the indexed Justice Laws authority shape.

Why now: The read-only statute coverage inventory found 50,020 Criminal Code references across 3,708 cases and 1,716 indexed sections, making it the highest-value covered non-IRPA fixture surface.

Owner surface: statute extraction and legislation resolution tests

Commit allowed: yes

Push allowed: yes

Dependencies: `backend/citations.py`; `backend/statutes.py`; `tests/test_citations.py`; indexed Criminal Code section shape

Risk boundary: Test-only comparison. Do not modify canonical rows, acquire sources, run corpus backfills, or change extraction rules unless a focused fixture failure proves a local defect.

Smallest falsifiable check: A Criminal Code section/subsection/paragraph citation preserves its exact source span and resolves to the stored base section; negative and range/list forms remain explicitly unresolved where expected.

Acceptance criteria:

- Add positive exact-span and stored-section resolution fixtures for Criminal Code.
- Add negative or range/list coverage that protects unresolved behavior.
- Focused citation tests pass without database writes.
- Update the task record and relevant statute/authority walkthrough with evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/4.9nn3id9f.sw.md`

Rollback/recovery: Revert only the test and documentation commit; no data rollback is needed.

Evidence: Added positive exact-span and stored-section resolution coverage plus explicit range and missing-section safeguards in `tests/test_citations.py`. Focused validation passed: `tests/test_citations.py -q -k "criminal_code_fixture or parse_legislation_citation_supports_criminal_code"` -> 3 passed, 152 deselected, 1 warning. No database writes, source acquisition, or corpus jobs ran. Canonical documentation: `SYSTEM_REFERENCE.md`; Swimm walkthrough: `.swm/4.9nn3id9f.sw.md`.

## Hypothesis

If Criminal Code references use the same structured provision and resolution contract as IRPA/IRPR, then exact-span positive fixtures will resolve to the indexed base section while range/list and missing-section cases remain explicit rather than silently misresolved.

## Plan

1. Add bounded Criminal Code fixtures beside existing citation tests.
2. Run focused citation validation.
3. Update documentation and task evidence.
4. Commit and push only task-owned files.

## Completion

Completion recorded: yes

Summary: Completed the bounded Criminal Code fixture comparison against the indexed authority row shape.

Validation: Focused Criminal Code fixture tests passed 3 times; the pre-existing broader statute resolution slice also passed 9 tests.

Residual risk: Unit fixtures model the indexed row shape but do not prove every live Criminal Code section has complete or current source coverage.

Next recommended task: Expand the fixture set with reviewed Criminal Code section text samples before considering any source acquisition or corpus backfill.
