# Task: Make AI search modes explicitly opt-in

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Gate enhanced search and research behavior behind `ENHANCED_AI_MODE`, default off, while retaining explicitly enabled local/hosted behavior.

Why now: Normal search should not unexpectedly invoke embeddings or external providers in deployments that have not opted into enhanced AI.

Owner surface: Backend search/research API mode boundary (`backend/ai_mode.py`, routes, providers, and focused API tests).

Commit allowed: yes

Push allowed: yes

Dependencies: Existing search mode contracts, embedding and text-generation provider factories, and current route/UI behavior.

Risk boundary: Do not change `/analytics/search/cases`, SQL Case Search UI, unrelated analytics, database/schema, `.env`, deployment scripts, dependency declarations, or password/access gates. Do not construct or invoke providers when mode is off.

Smallest falsifiable check: `python -m pytest -q tests/test_ai_mode.py tests/test_api.py` with offline fakes and assertions that disabled requests make zero provider calls.

Acceptance criteria:

- `ENHANCED_AI_MODE` accepts only `off`, `local`, or `hosted`; default is `off`, and status reports effective mode.
- With mode off, search defaults are lexical; explicit semantic/hybrid requests become lexical and explain the effective mode and disabled reason, with no embeddings or provider calls.
- `/research` returns a clear disabled JSON response; local selection does not construct an OpenAI client; hosted behavior is available only when explicitly enabled.
- Focused tests pass, generated references are current, and canonical docs plus the relevant Swimm walkthrough are updated.

Harness criteria: Not declared; repository harness run was not started.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, root `CHANGELOG.md` (there is no `docs/CHANGELOG.md`), `docs/RESEARCH_UI_GUIDE.md`, the government-readiness AI use/data flow/PIA input documents, `.swm/5.b49ftjal.sw.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, generated API reference via existing generator/check.

Rollback/recovery: Revert the mode-gate code and tests together; there are no schema or data changes.

Evidence: Reviewed `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.github/copilot-instructions.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.swm/5.b49ftjal.sw.md`, and `.swm/1.oi7rhqp2.sw.md`. The managed worker implemented the backend boundary and focused fake-based tests. `python -m compileall -q ...` passed for changed Python files; `git diff --check` passed. `python -m pytest -q tests/test_ai_mode.py tests/test_api.py tests/test_search_matching.py tests/test_text_generation_providers.py tests/test_feature_tabs.py` was attempted but could not collect because `pytest` is not installed. `python scripts/check_generated_docs.py` was attempted; API/schema generators failed because FastAPI and SQLAlchemy are unavailable. `python scripts/embed_documentation_appendices.py` passed and synchronized source-owned appendices; generated API reference remains stale because its generator could not run. No database, external model, deployment, or live provider was used. There is no `docs/CHANGELOG.md`; updated the repository's canonical root `CHANGELOG.md`.

Files changed: `.github/project-manager/tasks/200-default-search-non-ai.md`; `backend/ai_mode.py`; `backend/models.py`; `backend/routes.py`; `backend/search_service.py`; `backend/text_generation_providers.py`; `backend/pages/quick_search.py`; `tests/test_ai_mode.py`; `tests/test_api.py`; `tests/test_search_matching.py`; `tests/test_text_generation_providers.py`; `SYSTEM_REFERENCE.md`; `docs/CONFIGURATION_REFERENCE.md`; `docs/ARCHITECTURE.md`; `docs/RESEARCH_UI_GUIDE.md`; `docs/government-readiness/ai-use-statement.md`; `docs/government-readiness/data-flow.md`; `docs/government-readiness/pia-inputs.md`; `CHANGELOG.md`; `.swm/5.b49ftjal.sw.md`; `.swm/1.oi7rhqp2.sw.md`; `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`.
Delegated work: `managed-worker` implemented backend mode handling and fake tests; returned the required structured report. Its pytest invocation was blocked because pytest was unavailable. Manager updated user-facing and external-processing documentation, added an explicit hosted-mode fixture for existing semantic characterization tests, regenerated synchronized appendices, and performed final acceptance checks.
Focused validation: `python -m compileall -q backend/ai_mode.py backend/models.py backend/routes.py backend/search_service.py backend/text_generation_providers.py backend/pages/quick_search.py tests/test_ai_mode.py tests/test_api.py tests/test_search_matching.py tests/test_text_generation_providers.py` passed; `git diff --check` passed. Focused pytest and generated-doc check remain blocked by unavailable dependencies as stated above.
Residual risk: Focused tests were not executed and generated API/schema references could not be refreshed; do not treat this as fully validated. `git fetch origin main` refreshed `FETCH_HEAD`, which still resolves to `d5efc31 (#176)`; this checkout remains on `copilot/make-normal-search-non-ai` at `a08537c (Initial plan)`, so the stated merged-main state is not reflected and no commit/push was made. `search_mode_effective`/`ai_disabled_reason` are per returned item in list contracts, so an empty list cannot carry those fields without changing the established response shape.
Next bounded task: In a dependency-enabled project environment, run the focused tests and generated-reference generators, review their output, reconcile actual main/issue branch state, then decide commit/push.

## Hypothesis

If `ENHANCED_AI_MODE=off` is enforced at API boundaries, offline tests will show lexical search defaults, lexical downgrade metadata for semantic/hybrid requests, clear `/research` disablement, and zero embedding/provider calls.

## Plan

1. Add the mode configuration and API behavior with focused offline tests.
2. Verify local and hosted provider-selection behavior without live providers.
3. Refresh generated references and canonical/Swimm documentation, then validate.

## Execution Checkpoints

- Delegation: Managed worker completed backend code/tests; pytest unavailable.
- Implementation: Backend API mode boundary added; Python compilation passed.
- Documentation: Updated root `SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `docs/RESEARCH_UI_GUIDE.md`, government-readiness AI/data-flow/PIA documents, root `CHANGELOG.md`, and Swimm walkthroughs `.swm/5.b49ftjal.sw.md`, `.swm/1.oi7rhqp2.sw.md`, and `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`; source-owned appendices regenerated.
- Recovery: Not applicable; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | One backend API mode-boundary owner | The setting must consistently govern search and research without changing analytics Case Search | Search/retrieval walkthrough and route ownership map |

## Completion

Completion recorded: no

Summary: Implementation and documentation are present, but task is blocked on test execution and generated API/schema verification in an environment with FastAPI, SQLAlchemy, and pytest.

Validation: Python compilation and `git diff --check` passed. Focused pytest failed to start (`No module named pytest`); generated-doc check failed because API/schema generators cannot import FastAPI/SQLAlchemy.

Residual risk: API/schema generated refs remain unrefreshed; behavior is not test-validated.

Next recommended task: Run the focused suite and generated-reference check in the project dependency environment; then reconcile branch ancestry and finalize commit/push separately.
