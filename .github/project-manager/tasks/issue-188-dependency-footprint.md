# Task: Reduce unnecessary required Python dependencies

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Remove only dependencies proven unused and move sentence-transformers or spaCy/model to optional ML requirements only if base imports and CI/tests remain supported.

Why now: Issue #188 asks to reduce the required install footprint without changing application defaults or hiding test/CI dependencies.

Owner surface: Python dependency manifests and their install/runtime documentation.

Commit allowed: yes

Push allowed: yes

Dependencies: Requirements import/use inventory; issue #112 Rules block; relevant dependency-audit walkthrough.

Risk boundary: Do not upgrade `openai`, alter pip-audit blocking behavior, touch database, `.env`, or deploy configuration, change defaults, or remove working features. Preserve the three CI pytest deselects.

Smallest falsifiable check: Search tracked code/tests/workflows for direct and transitive uses of candidate packages, then validate a clean base install and `backend.main` import.

Acceptance criteria:

- Remove `langchain-openai` only if source, tests, scripts, and CI provide no required use; remove transitive-only requirements only with evidence.
- Keep sentence-transformers and spaCy/model required if base imports or CI/tests need them; otherwise isolate optional ML extras without changing base behavior.
- Document optional installation in `SETUP.md` only if an actual optional requirements file is introduced.
- Required focused, clean-install/import, and pytest validations are run and outcomes are recorded honestly.
- Canonical documentation and the relevant Swimm walkthrough are updated.

Harness criteria:

- `python -m pip install -r requirements.txt` succeeds in a fresh virtual environment.
- `python -c "import backend.main"` succeeds in that environment.
- `python -m pytest -q --deselect=tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence --deselect=tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes --deselect=tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint` completes and result is recorded.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/12.ci-quality-workflow.sw.md`; `SETUP.md` only if optional ML requirements are created. No generated docs expected.

Rollback/recovery: Restore the narrowly changed requirement entries and matching documentation from this task's diff; do not change runtime defaults or deployed environments.

Evidence: The managed worker searched source/tests/scripts/CI and reported zero direct `langchain_openai`/`ChatOpenAI`/`LLMChain` references. It found lazy imports for sentence-transformers and spaCy in `backend/embedding_providers.py` and `backend/deidentify_names.py`. A first clean base install/import without ML packages passed, but the CI-equivalent suite failed `tests/test_api.py::test_local_chunk_search_uses_requested_model` with the missing sentence-transformers dependency; sentence-transformers therefore remains in `requirements.txt`. With it installed, that test attempted to download `BAAI/bge-m3` from Hugging Face and failed because network DNS is unavailable in this environment. Two tokenizer tests likewise failed fetching `cl100k_base.tiktoken` from `openaipublic.blob.core.windows.net`. The spaCy-dependent test uses `pytest.importorskip("spacy")`, and its model test is skipped when the model is absent; spaCy/model therefore remain optional. Final full-suite result: 1,524 passed, 2 skipped, 3 deselected, 1 xfailed, 3 failed; all three failures are blocked external downloads. Corrected fresh install/import passed with sentence-transformers present and spaCy/`langchain_openai` absent. `scripts/check_generated_docs.py` passed; `git diff --check` passed; test workflow remained unchanged. A whole-file secret-pattern scan found only the pre-existing masked `DATABASE_URL` setup example; no secret material was added.

Files changed: `requirements.txt`; `requirements-ml.txt`; `SETUP.md`; `SYSTEM_REFERENCE.md`; `.swm/12.ci-quality-workflow.sw.md`; this task record.

Delegated work: `managed-worker` (manifest owner slice); structured findings received. No tests or CI/workflow files changed.

Focused validation: In a new `/tmp/issue-188-final-venv`, `python -m pip install -r requirements.txt` succeeded; `python -c "import backend.main"` succeeded and confirmed sentence-transformers present while spaCy and `langchain_openai` were absent. Full CI-equivalent pytest ran with the exact three deselects and coverage flags: 1,524 passed, 2 skipped, 3 deselected, 1 xfailed, 3 failed due to unavailable Hugging Face/OpenAI tokenizer downloads. `python scripts/check_generated_docs.py` reported 3 references current; `git diff --check` passed; relevant local documentation targets exist and `.github/workflows/tests.yml` is unchanged.

Residual risk: The local embedding and tiktoken tests require external model/tokenizer downloads and could not pass without DNS access; those tests must be rerun in a network-enabled CI environment. No requirement removal should be inferred from these environment-only failures.

Next bounded task: Make the local embedding and tokenizer tests deterministic without external downloads, then rerun the exact CI test command.

## Hypothesis

If dependencies are removed or made optional only when source and CI/test evidence permits, a fresh base install and `backend.main` import will pass while test results identify packages that must remain required.

## Plan

1. Inventory candidate imports and requirements dependency relationships against issue #112 rules.
2. Make only evidence-supported manifest/documentation changes and run a focused check.
3. Verify a fresh base install/import, then run the exact pytest command with the three CI deselects.

## Execution Checkpoints

- Delegation: `managed-worker` inventoried candidate uses and proposed moving three ML requirements; manager retained sentence-transformers as required after the CI-equivalent test failed without it.
- Implementation: `requirements.txt` no longer includes `langchain-openai`; sentence-transformers remains required because a CI test exercises it. spaCy and `en_core_web_md` are optional.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `.swm/12.ci-quality-workflow.sw.md`, and `SETUP.md` to document the optional install path.
- Recovery: No data or operational run recovery expected.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #188 requests evidence-driven reduction of required dependencies under issue #112 rules. | User issue statement; `.github/project-manager/tasks/issue-171-dependency-audit-task.md` records the issue #112 Rules block. |

## Completion

Completion recorded: yes

Summary: Removed unused `langchain-openai`; retained sentence-transformers because the suite invokes the local embedding path; moved only spaCy and `en_core_web_md` to optional `requirements-ml.txt`, with installation guidance in SETUP.

Validation: Fresh base install and `backend.main` import passed. Generated-doc and diff checks passed. The full suite ran with all three CI deselects: 1,524 passed, 2 skipped, 3 deselected, 1 xfailed, 3 failures caused by unavailable external model/tokenizer downloads.

Residual risk: Repeat the three network-dependent test failures in an environment with Hugging Face and OpenAI tokenizer asset access.

Next recommended task: Make the local embedding and tokenizer tests deterministic without external downloads, then rerun CI.
