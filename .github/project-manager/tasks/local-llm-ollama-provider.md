# Task: Add local Ollama LLM provider

Status: complete
Created: 2026-09-23
Updated: 2026-09-23

## Task Record

Task: Allow bounded case-intelligence requests to run against a local Ollama model.

Why now: The project has local embeddings but no local generative provider; the user wants to run an LLM locally and use it for case-intelligence work.

Owner surface: `scripts/run_case_intelligence_request.py` and its provider configuration.

Commit allowed: yes

Push allowed: yes

Dependencies: Ollama installed locally with a pulled instruct model; existing OpenAI Python client.

Risk boundary: Local generation is optional and additive. It must not replace deterministic extraction, alter hosted defaults, or imply legal authority without source evidence.

Smallest falsifiable check: `venv\\Scripts\\python.exe -m pytest tests/test_run_case_intelligence_request.py -q`

Acceptance criteria:

- The existing hosted OpenAI path remains the default.
- A local Ollama path uses an OpenAI-compatible local endpoint without requiring `OPENAI_API_KEY`.
- Local model name and endpoint are configurable through CLI/environment values.
- Provider behavior is covered without requiring a live model server.
- Configuration and architecture rationale are documented.

Docs/generated references: `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`

Rollback/recovery: Revert the provider-selection and documentation changes; existing hosted invocation remains unchanged.

Evidence: Explore agent confirmed no existing generative provider. Added local Ollama selection to `scripts/run_case_intelligence_request.py`, focused tests passed with `venv\\Scripts\\python.exe -m pytest tests/test_run_case_intelligence_request.py -q` (`2 passed`), CLI help and Python compilation passed, and diagnostics reported no errors. Canonical documentation updated in `docs/CONFIGURATION_REFERENCE.md` and `SYSTEM_REFERENCE.md`; rationale updated in `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`. Ollama was not installed in the current environment, so no live model request or download was claimed.

## Hypothesis

If the script constructs an OpenAI-compatible client with Ollama's local `/v1` endpoint and a non-secret placeholder key, a bounded request can use a local model without an OpenAI credential while preserving the existing output contract.

## Plan

1. Add explicit hosted/local provider selection and configuration.
2. Add mocked provider tests for client construction and local request execution.
3. Update canonical configuration and architecture rationale, then validate.

## Execution Checkpoints

- Delegation: Explore agent inspected the current provider surface and returned a structured report.
- Implementation: `scripts/run_case_intelligence_request.py` and `tests/test_run_case_intelligence_request.py`; focused tests passed.
- Documentation: `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, and `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md` updated.
- Recovery: No long-running operation; local model download is user/runtime scoped.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-23 | Use Ollama's OpenAI-compatible endpoint | Reuses the existing OpenAI client and request contract with minimal change | `scripts/run_case_intelligence_request.py` |

## Completion

Completion recorded: yes

Summary: Added an optional Ollama/OpenAI-compatible local provider for bounded case-intelligence requests while preserving the hosted default.

Validation: Focused pytest (`2 passed`), CLI help, py_compile, and editor diagnostics all passed. Live Ollama validation remains pending installation.

Residual risk: Model quality, memory use, and latency depend on the user's hardware and chosen local model.

Next recommended task: Install Ollama, pull `qwen2.5:7b`, and run one bounded local request against a copied dry-run payload.
