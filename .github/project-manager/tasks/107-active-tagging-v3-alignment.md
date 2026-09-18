# Task: Align active tagging with V3

Status: complete
Created: 2026-09-17
Updated: 2026-09-17

## Task Record

Task: Improve only the most recent active tagging process and align overnight tagging with the V3 pipeline used by case processing.

Why now: The active case-processing path uses V3, but the overnight tag selector still points to the older tagging wrapper, creating inconsistent tags between workflows.

Owner surface: scripts/run_overnight.py and active V3 tagging tests

Commit allowed: yes

Push allowed: yes

Dependencies: backend/case_processing.py; scripts/tag_cases_v3.py; backend/legal_tagger_v3.py; existing overnight orchestration tests

Risk boundary: Do not modify legacy backend/legal_tagger.py, backend/legal_tagger_v2.py, scripts/tag_cases.py, or their tests except to verify they remain excluded. Do not run tagging writes, overnight jobs, corpus backfills, or production operations.

Smallest falsifiable check: .\\venv\\Scripts\\python.exe -m pytest tests/test_tagging_v3_proposal.py -q

Acceptance criteria:

- The active overnight tag selector resolves to the V3 tagging entry point.
- A regression test prevents drift back to the legacy wrapper.
- Existing V3 tagging behavior remains green.
- The active tagging documentation and Swimm walkthrough identify V3 as the current path and legacy taggers as excluded.

Docs/generated references: SYSTEM_REFERENCE.md; OVERNIGHT.md; docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md; relevant .swm/ walkthrough

Rollback/recovery: Revert the selector and regression-test changes. No data rollback is required because no tagging operation is run.

Evidence: Delegated audit confirmed `ca_legal_v3_core` is the active case-processing tagger and identified the overnight selector drift. Workers aligned the overnight selector with the V3 wrapper, made failed V3 statuses retryable, and aligned batch text selection with case processing (`full_text or summary`). Legacy taggers were not modified. Validation passed: 13 V3 tests, 4 case-processing tests, 1 overnight selector regression with 8 deselected, and git diff --check.

## Hypothesis

If the overnight `tag_cases` selector invokes the same V3 wrapper consumed by case processing, the focused V3 test and selector regression will show one consistent active tagging path without touching legacy code.

## Plan

1. Confirm the overnight selector and active V3 entry point.
2. Change only the selector and add a drift-prevention test.
3. Run focused tests and update canonical/Swimm documentation.
4. Inspect for another high-return V3-only issue before closing.

## Execution Checkpoints

- Delegation: AI CaseLibrary Project Manager workers completed bounded active-path audit and three V3-only implementation slices with structured reports.
- Implementation: scripts/run_overnight.py, scripts/tag_cases_v3.py, tests/test_run_overnight.py, tests/test_tagging_v3_proposal.py, and active tagging documentation; legacy taggers untouched.
- Documentation: OVERNIGHT.md, LEGAL_TAGGING.md, and .swm/8.upryk5h6.sw.md updated.
- Recovery: no writer or overnight run authorized

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-17 | Exclude legacy taggers | User explicitly requested the most recent active process only | Managed-task request |

## Completion

Completion recorded: yes

Summary: Aligned overnight tagging with active V3, made failed statuses retryable, and unified V3 input text behavior with case processing.

Validation: .\\venv\\Scripts\\python.exe -m pytest tests/test_tagging_v3_proposal.py -q -> 13 passed; .\\venv\\Scripts\\python.exe -m pytest tests/test_case_processing.py -q -> 4 passed; overnight selector regression -> 1 passed, 8 deselected; git diff --check passed.

Residual risk: No corpus-wide tagging precision/recall claim was made. Further V3 rule changes should be driven by a bounded labeled fixture or sampled evaluation; legacy tagging paths remain intentionally excluded.

Next recommended task: Measure V3 tag precision/recall on a bounded fixture set and address the highest-confidence rule gap.
