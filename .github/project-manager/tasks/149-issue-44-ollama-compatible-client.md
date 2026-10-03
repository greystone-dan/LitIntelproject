# Task: Restore the Ollama-compatible client test in CI

Status: complete
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Fix the bounded case-intelligence runner's local client construction and remove the test's CI deselection.

Why now: Issue #44 identifies a clean-checkout regression hidden by CI deselection; restoring this test makes the documented local client contract continuously verifiable.

Owner surface: `scripts/run_case_intelligence_request.py` and its focused test/CI invocation.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing `OpenAI` Python client and Ollama's OpenAI-compatible `/v1` endpoint; no live endpoint needed for the focused unit test.

Risk boundary: Preserve the hosted default, local model/endpoint configuration, request/output contract, and separate `/research` provider behavior. Do not skip or disable the test.

Smallest falsifiable check: `python -m pytest -q tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint`

Acceptance criteria:

- The local runner constructs `OpenAI` with the configured `base_url` and local placeholder `api_key`.
- The issue #44 test runs and passes on a clean checkout; its deselection/comment is removed from the test workflow.
- Relevant canonical documentation and Swimm architecture walkthrough describe the runner's client boundary accurately.
- Secret scan and final focused validation complete before commit; no commit or push is made without a user-visible decision after reporting.

Harness criteria: Not used; this task does not create a harness run.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`; no generated references.

Rollback/recovery: Revert the runner/workflow/documentation edits together; hosted behavior remains unchanged.

Evidence: Managed worker `issue44-test-trace` inspected the test, runner, provider implementation, and nearby provider tests. Its structured report found that `build_client("local", ...)` returned `OllamaChatProvider` before calling the monkeypatched `OpenAI`; this contract mismatch left captured kwargs empty. Worker could not run pytest because its environment lacked pytest. In the manager environment, the first focused attempt also found pytest absent; installed the repository-pinned `pytest==8.2.2`, `openai==1.30.1`, and `httpx==0.27.0`. After the fix, the issue test passed (`1 passed`) and the full runner module passed (`2 passed`). `python -m py_compile scripts/run_case_intelligence_request.py`, `git diff --check`, and the check confirming the test name is absent from `.github/workflows/tests.yml` passed. A common credential-pattern scan over every changed file found no matches. Updated canonical `SYSTEM_REFERENCE.md` and Swimm `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md` in this checkpoint.

Files changed: `.github/workflows/tests.yml`, `.github/project-manager/tasks/149-issue-44-ollama-compatible-client.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `SYSTEM_REFERENCE.md`, `scripts/run_case_intelligence_request.py`.
Delegated work: Managed worker `issue44-test-trace`; bounded read-only trace of the failing test and direct provider call sites. Structured report returned; no files changed.
Focused validation: `python -m pytest -q tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint` (`1 passed`) and `python -m pytest -q tests/test_run_case_intelligence_request.py` (`2 passed`).
Residual risk: No live Ollama call was made; endpoint availability and model behavior remain outside this mocked client-construction fix. The separate `/research` API provider remains on native `/api/chat`.
Next bounded task: None required for issue #44.

## Hypothesis

If the runner's `local` branch constructs `OpenAI(base_url=ollama_base_url, api_key="ollama-local")`, the focused test will observe both expected kwargs and the local request/output contract will continue to pass.

## Plan

1. Construct the OpenAI-compatible client for the local runner path.
2. Remove only the issue #44 deselection/comment from CI.
3. Run focused tests, update canonical and Swimm documentation, scan for secrets, and perform final validation.

## Execution Checkpoints

- Delegation: Managed worker `issue44-test-trace` returned a structured root-cause report; no implementation delegated.
- Implementation: `scripts/run_case_intelligence_request.py` now creates the OpenAI-compatible local client; the issue #44 workflow deselection was removed.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md` updated to distinguish the script's `/v1` client from the API's `/api/chat` transport.
- Recovery: No long-running operation or external model call.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Use the OpenAI-compatible client in the script's local branch | Existing test, documented endpoint, and prior provider task specify the `/v1` client contract; current branch returns a different native adapter | Worker report; `tests/test_run_case_intelligence_request.py`; prior local-provider task |

## Completion

Completion recorded: yes

Summary: Fixed the local runner's client-construction root cause and restored the focused regression test to CI.

Validation: Issue #44 test (`1 passed`), full focused module (`2 passed`), Python compilation, workflow deselection check, `git diff --check`, and changed-file common credential-pattern scan passed.

Residual risk: Live Ollama/model connectivity was not exercised.

Next recommended task: None required; CI now executes the regression test.
