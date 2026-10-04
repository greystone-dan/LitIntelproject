# Task: Measure pytest coverage and strengthen pure-logic tests

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Measure coverage using the test selection and deselects used in CI, add `pytest-cov` only to development requirements, publish a risk-ranked module report, and add focused database-free tests for the three weakest pure-logic modules.

Why now: The repository needs an actionable, reproducible view of untested logic and focused regression tests without changing production behavior.

Owner surface: Python test quality and coverage reporting (`tests/`, development requirements, and `docs/reports/test-coverage.md`).

Commit allowed: yes

Push allowed: yes

Dependencies: Existing pytest configuration, CI test selection, and pure-logic module boundaries.

Risk boundary: Test/development/documentation changes only; no runtime behavior, database access, CI selection, or production dependencies may change. Any test exposing an existing defect must be an explicitly reasoned xfail and included in the PR summary.

Smallest falsifiable check: `python -m pytest -q tests/test_citation_refine_context.py tests/test_fc_activity_pure_logic.py tests/test_metadata_subjects.py`.

Acceptance criteria:

- `pytest-cov` is added only to development requirements.
- A reproducible coverage report ranks modules by risk and records selection, denominator, and limitations.
- Three lowest-coverage pure-logic modules receive focused tests without database setup.
- Existing bugs are xfailed with a reason and explicitly listed in the PR summary.
- Relevant canonical documentation and Swimm walkthrough are updated and their paths plus validation are recorded here.

Harness criteria: CI deselects are identified and reflected in measurement; report is reproducible and risk-ranked; focused tests are database-free and pass or contain documented xfails; docs and Swimm checkpoint is complete.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/reports/test-coverage.md`, `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`; no generated references.

Rollback/recovery: Revert only this task's test, development dependency, report, and documentation edits; no data or runtime recovery is needed.

Evidence: The managed worker confirmed CI runs `python -m pytest -q` with `tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence`, `tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes`, and `tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint` explicitly deselected. After installing the pinned requirements locally, the coverage run using those exclusions completed with `987 passed, 3 failed, 3 deselected`; the failures require uncached Hugging Face/OpenAI tokenizer downloads and network DNS is unavailable. Backend coverage was 77.5% (8,413/10,859 statements across 66 modules). Baseline pure, database-free targets were `backend/citation_refine/context.py` 77.7% (112 statements), `backend/fc_activity.py` 81.6% (125), and `backend/metadata_subjects.py` 85.2% (88); post-test coverage is 79.5%, 91.2%, and 88.6%. Lower baseline figures for `backend/citation_pipeline/canlii.py` and `backend/memo_citation_check.py` are excluded from pure-logic selection because they own network/rate-limit or database orchestration behavior, respectively. No existing bug was revealed, so no xfails were added. Canonical docs updated: `docs/TESTING_MATRIX.md`, `SYSTEM_REFERENCE.md`, and `docs/reports/test-coverage.md`; Swimm updated: `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`. Documentation correction: risk order now explicitly prioritizes CBSA-visible outcome, citation, analytics, minister, and judge handling, ahead of general coverage gaps; measured values and the original three-module test selection are unchanged. Per user request, no tests, builds, or linters were run for this correction.

Files changed: `.github/workflows/tests.yml`, `.github/project-manager/tasks/test-coverage-and-pure-logic-tests.md`, `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`, `SYSTEM_REFERENCE.md`, `docs/TESTING_MATRIX.md`, `docs/reports/test-coverage.md`, `requirements-dev.txt`, `requirements.txt`, `tests/test_citation_refine_context.py`, `tests/test_fc_activity_pure_logic.py`, `tests/test_metadata_subjects.py`.
Delegated work: `coverage-inventory` (managed-worker), read-only discovery of CI deselects, candidate modules, and coverage availability; structured result returned, no files changed. Its first measurement attempt was blocked because pytest was absent; manager installed the pinned requirements and measured coverage.
Focused validation: `python -m pytest -q tests/test_citation_refine_context.py tests/test_fc_activity_pure_logic.py tests/test_metadata_subjects.py` — 8 passed; `python scripts/check_generated_docs.py` — 3 references current; local-link check — no broken links; `git diff --check` — passed. Full CI-selected coverage run — 987 passed, 3 network-dependent failures, 3 deselected; 77.5% backend statement coverage.
Residual risk: The full suite remains non-green in this network-restricted environment because Hugging Face model files and OpenAI tokenizer assets could not be fetched. Coverage is a measured snapshot, not a release gate.
Next bounded task: Isolate a database-free test surface for high-impact `backend/citation_map.py` logic, or document why route-level behavior prevents safe pure tests.

## Hypothesis

If coverage is measured with CI's actual collection/exclusion rules, focused database-free tests for `backend/citation_refine/context.py`, `backend/fc_activity.py`, and `backend/metadata_subjects.py` will exercise their uncovered deterministic branches without changing runtime behavior.

## Plan

1. Delegate read-only discovery of CI pytest selection, baseline coverage, and candidate pure-logic modules.
2. Add `pytest-cov` to dev-only requirements, measure/report module risk, and add focused tests for the three lowest-coverage pure modules.
3. Run focused validation and update the canonical reference plus evaluation walkthrough.

## Execution Checkpoints

- Delegation: `coverage-inventory`; CI deselect list and unranked pure-logic candidates reported; baseline blocked by missing pytest.
- Implementation: Added dev-only pytest-cov installation, CI coverage output, and focused database-free tests; the recorded focused command passed.
- Documentation: Updated `docs/reports/test-coverage.md`, `docs/TESTING_MATRIX.md`, `SYSTEM_REFERENCE.md`, and `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`; the risk-order correction is recorded in the report and this task record.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created | User requested measurable coverage and safe, behavior-preserving logic tests | `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, and evaluation walkthrough reviewed |
| 2026-10-03 | Reordered report risks around CBSA-visible numbers | User clarified risk order must prioritize outcomes, citations, analytics, minister, and judge handling before raw coverage gaps | Updated report and Swimm explanation; coverage values and three tested modules retained; no tests/builds/linters run per request |

## Completion

Completion recorded: yes

Summary: Measured backend pytest coverage with CI's three explicit deselects, moved pytest-cov to development requirements, documented risk-ranked module results, and added eight deterministic tests across the three lowest-coverage pure-logic modules selected from the baseline. No production behavior changed; no xfail was required.

Validation: Focused tests: 8 passed. Generated-document check: 3 references current. Local links and `git diff --check`: passed. Full selected suite: 987 passed, 3 network-dependent failures, 3 deselected; 77.5% statement coverage.

Residual risk: The full run requires external Hugging Face/OpenAI tokenizer assets unavailable in this environment; details are in the coverage report.

Next recommended task: Design an isolated no-database coverage slice for high-impact citation-map logic without coupling it to API/database orchestration.
