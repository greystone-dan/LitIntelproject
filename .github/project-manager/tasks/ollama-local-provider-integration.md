# Task: Ollama local provider integration

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Make Ollama available as a callable local AI provider for the project without changing the default hosted provider or downloading a model yet.

Why now: The user wants to test a local AI workflow from this project before choosing and downloading a model.

Owner surface: backend/embedding_providers.py and the adjacent runtime configuration boundary

Commit allowed: yes

Push allowed: yes

Dependencies: Installed Ollama CLI/service; existing provider configuration; focused provider tests

Risk boundary: Do not change the default provider, expose secrets, mutate canonical legal data, or download a model during this task.

Smallest falsifiable check: Provider configuration and a bounded Ollama availability check pass without requiring a model download.

Acceptance criteria:

- Ollama can be selected through project configuration using the existing provider boundary.
- The application can report a clear unavailable/model-not-installed error rather than failing opaquely.
- Existing default provider behavior and imports remain unchanged.
- Focused provider/config validation passes.

Docs/generated references: SYSTEM_REFERENCE.md; docs/CONFIGURATION_REFERENCE.md; .swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md

Rollback/recovery: Remove the Ollama provider branch/config entries and restore the prior default; no database or canonical-data changes are permitted.

Evidence: Explore agent inventory confirmed existing script-level Ollama support and the hardcoded /research OpenAI boundary. Added provider factory and route regression coverage. Focused pytest passed 7 tests; Python compilation passed; git diff --check passed. Ollama local API check returned HTTP 200, but the CLI is not on the current PowerShell PATH and no model was downloaded. Canonical documentation updated at SYSTEM_REFERENCE.md and docs/CONFIGURATION_REFERENCE.md; Swimm walkthrough updated at .swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md.

## Hypothesis

If Ollama is implemented behind the existing provider boundary, a focused configuration/provider check will select it and distinguish a reachable service from a missing model without affecting the default path.

## Plan

1. Inspect the existing provider, configuration, and focused tests.
2. Add the smallest Ollama adapter and configuration wiring.
3. Run focused validation, then update canonical documentation and the relevant Swimm walkthrough.

## Execution Checkpoints

- Delegation: Explore agent inspected provider/config/script/test surfaces and recommended an opt-in backend factory.
- Implementation: Added backend/text_generation_providers.py, refactored /research, and added focused provider tests.
- Documentation: Updated SYSTEM_REFERENCE.md, docs/CONFIGURATION_REFERENCE.md, and .swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md.
- Recovery: No long-running data operation; installer/model download remains outside this task.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-25 | Task created | Local model testing requires a project-callable provider without changing hosted defaults. | SYSTEM_REFERENCE.md provider ownership map |

## Completion

Completion recorded: yes

Summary: Added an opt-in Ollama/OpenAI-compatible text-generation provider for /research with OpenAI retained as the default.

Validation: .\venv\Scripts\python.exe -m pytest tests/test_text_generation_providers.py tests/test_run_case_intelligence_request.py -q passed 7 tests; py_compile passed; git diff --check passed.

Residual risk: Ollama CLI PATH integration is unresolved in the current shell, and no local model is installed; the next model-download task must select and pull one before an end-to-end generation call.

Next recommended task: Select and download a bounded local model, then run a project-level smoke call through /research.
