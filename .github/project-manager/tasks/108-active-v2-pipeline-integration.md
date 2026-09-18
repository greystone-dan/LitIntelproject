# Task: Verify active V2 pipeline integration

Status: complete
Created: 2026-09-17
Updated: 2026-09-17

## Task Record

Task: Ensure the active V2 case-processing pipeline includes all completed system improvements and does not silently route work through stale or legacy stages.

Why now: The system has accumulated improvements across extraction, tagging, provenance, chunks, citations, statutes, metadata, and reader contracts; active orchestration must be checked against those completed paths.

Owner surface: backend/case_processing.py and active orchestration entry points

Commit allowed: yes

Push allowed: yes

Dependencies: scripts/run_overnight.py; active case-processing stages; focused orchestration tests; current system and Swimm documentation

Risk boundary: Do not run production/bulk writers, alter legacy modules unless active wiring proves they are still authoritative, change schema/versioning, or modify unrelated feature behavior. Preserve stage ordering, locks, checkpoints, and dry-run boundaries.

Smallest falsifiable check: .\\venv\\Scripts\\python.exe -m pytest tests/test_case_processing.py tests/test_run_overnight.py -q

Acceptance criteria:

- Active pipeline entry points and stage lists are inventoried with ownership identified.
- Completed active improvements are present in the actual pipeline, not only in isolated helpers/tests.
- Stale or legacy stage wiring is either corrected or explicitly documented as excluded.
- Focused orchestration and stage-order tests pass.
- Canonical and Swimm documentation record the active pipeline contract and residual gaps.

Docs/generated references: SYSTEM_REFERENCE.md; OVERNIGHT.md; docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md; relevant .swm/ walkthrough

Rollback/recovery: Revert only confirmed active wiring changes and regression tests. No production or bulk run is authorized, so no data rollback is required.

Evidence: Delegated inventory confirmed the active V2 stage order as `source_html -> chunks -> metadata -> outcome -> citations -> statutes -> tags_v3`, with citations mapped to the separate `case_citations` stage. It also confirmed completed chunk, metadata, outcome, statute, V3 tagging, provenance, and reader integrations, while identifying that the main overnight coordinator did not expose the full V2 runner. Added a bounded `v2_pipeline` job and dedicated `pipeline` profile without changing `safe` or `enrich`; added drift-prevention tests and updated OVERNIGHT.md plus the Swimm operations walkthrough.

## Hypothesis

If the active V2 pipeline stage list and overnight selectors point to the completed owner modules in the documented order, focused orchestration tests will catch any missing or stale integration without requiring a data run.

## Plan

1. Delegate a read-only inventory of active entry points, stage composition, and completed-feature call sites.
2. Fix the smallest confirmed active integration gaps and add drift-prevention tests.
3. Run focused case-processing and overnight orchestration tests immediately after edits.
4. Update canonical and Swimm pipeline documentation and record any intentionally deferred stages.

## Execution Checkpoints

- Delegation: AI CaseLibrary Project Manager worker completed the bounded active-pipeline inventory and profile integration slice with a structured report.
- Implementation: scripts/run_overnight.py, tests/test_run_overnight.py, and active orchestration documentation; no production or bulk run.
- Documentation: OVERNIGHT.md and .swm/8.upryk5h6.sw.md updated; SYSTEM_REFERENCE.md remains the owner/stage reference.
- Recovery: no production, bulk, or database writer run authorized

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-17 | Audit active V2 path only | User requested current pipeline integration, not legacy cleanup | Managed-task request |

## Completion

Completion recorded: yes

Summary: Exposed the complete improved V2 runner through an explicit overnight `pipeline` profile while preserving existing `safe` and `enrich` profile behavior.

Validation: .\\venv\\Scripts\\python.exe -m pytest tests/test_run_overnight.py tests/test_v2_pipeline_runner.py -q -> 17 passed; .\\venv\\Scripts\\python.exe -m pytest tests/test_case_processing.py -q -> 4 passed; git diff --check passed.

Residual risk: The new profile was not executed and no database writer was run. Existing `safe`/`enrich` profiles intentionally remain separate; operators must select `pipeline` when the full V2 sequence is desired.

Next recommended task: Address the highest-confidence missing active stage or stale selector found by the inventory.
