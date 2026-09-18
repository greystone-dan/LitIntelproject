# Task: Case-insensitive provision continuity

Status: complete
Created: 2026-09-17
Updated: 2026-09-17

## Task Record

Task: Preserve statute identity when a provision is first named as `34(1)(A) of IRPA` and later appears as `section 34(1)(a)` without repeating the instrument name.

Why now: The user identified a trust-relevant extraction loss where repeated, abbreviated, or case-varied provisions are not consistently identified as the same IRPA/IRPR authority.

Owner surface: backend/citations.py statute extraction and tests/test_citations.py

Commit allowed: yes

Push allowed: yes

Dependencies: existing anchored-provision extraction; structured provision parsing; no database or authority-bank changes

Risk boundary: Preserve raw text and exact offsets, keep case citations separate, do not backfill corpus rows, and do not broaden into legislation versioning or authority resolution.

Smallest falsifiable check: .\\venv\\Scripts\\python.exe -m pytest tests/test_citations.py -k statute_reference -q

Acceptance criteria:

- The exact mixed-case sequence produces both provision references with correct source spans.
- The later standalone provision inherits the prior IRPA identity only when the existing bounded anchoring rules permit it.
- Normalized provision identity is case-insensitive for section-letter variants without changing raw reference text.
- Existing nested, negative, and exact-span statute tests remain green.
- Canonical and Swimm documentation record the extraction continuity behavior.

Docs/generated references: SYSTEM_REFERENCE.md; docs/TESTING_MATRIX.md; .swm/4.9nn3id9f.sw.md

Rollback/recovery: Revert the focused matcher/normalization change and regression tests; no database recovery is required because no writer or backfill is authorized.

Evidence: The legislation extraction worker updated backend/statutes.py and backend/citations.py to canonicalize nested provision casing while preserving raw source spans, and added mixed-case/repeated-abbreviation regressions in tests/test_citations.py. Focused validation passed with 24 tests passed and 122 deselected. SYSTEM_REFERENCE.md, docs/TESTING_MATRIX.md, and .swm/4.9nn3id9f.sw.md record the behavior.

## Hypothesis

If provision suffix matching and normalization treat section letters case-insensitively while retaining original match text and offsets, the focused mixed-case sequence test will return both references with the later one anchored to IRPA.

## Plan

1. Add a regression fixture for the exact mixed-case repeated-provision sequence.
2. Make the smallest matcher/normalization adjustment needed for the fixture.
3. Run focused statute tests and update canonical/Swimm documentation.

## Execution Checkpoints

- Delegation: Completed within managed task 106 by the AI CaseLibrary Project Manager worker.
- Implementation: backend/citations.py, backend/statutes.py, and tests/test_citations.py.
- Documentation: SYSTEM_REFERENCE.md, docs/TESTING_MATRIX.md, and .swm/4.9nn3id9f.sw.md updated.
- Recovery: no corpus writer or backfill authorized

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-17 | Keep authority resolution and versioning out of scope | User requested extraction improvement only | Current task request |

## Completion

Completion recorded: yes

Summary: Case-insensitive provision continuity is implemented and tested.

Validation: .\\venv\\Scripts\\python.exe -m pytest tests/test_citations.py -k "statute_reference or legislation" -q -> 24 passed, 122 deselected; git diff --check passed.

Residual risk: Other abbreviated references may require separate alias rules; repeated shorthand lists and ranges remain the next bounded recall shape.

Next recommended task: Measure additional unresolved statute-reference shapes after the focused fix.
