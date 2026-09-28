# Task: Download Qwen3 local model

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Download `qwen3:4b` into Ollama and verify that AI CaseLibrary can call it locally.

Why now: The user approved the recommended local model for paragraph and chunk summaries.

Owner surface: Ollama local runtime and project text-generation configuration

Commit allowed: yes

Push allowed: yes

Dependencies: Ollama service at `http://127.0.0.1:11434`; network access; approximately 2.5 GB available storage

Risk boundary: Download only the approved model; do not modify canonical data, run bulk analysis, or switch hosted production behavior without explicit approval.

Smallest falsifiable check: Ollama lists `qwen3:4b` and returns a bounded local response through the project’s OpenAI-compatible provider.

Acceptance criteria:

- `qwen3:4b` is downloaded and listed by Ollama.
- The project provider can call the model locally.
- A bounded generation smoke test succeeds.
- No hosted-provider default or canonical data changes occur.

Docs/generated references: SYSTEM_REFERENCE.md; docs/CONFIGURATION_REFERENCE.md; .swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md

Rollback/recovery: Remove the model with `ollama rm qwen3:4b`; restore any temporary environment overrides. No source or database rollback is expected.

Evidence: Delegated readiness check confirmed Ollama executable at `C:\Users\danny\AppData\Local\Programs\Ollama\ollama.exe`, local API availability, and empty model inventory. Pulled `qwen3:4b` successfully at 2.5 GB. Added project `.env` settings for local provider, endpoint, and model. Updated the local adapter to use native Ollama `/api/chat` with `think=false` because the OpenAI-compatible endpoint returned Qwen3 reasoning without content. Focused tests passed 6; Python compilation passed; live project-provider smoke call returned non-empty content for `qwen3:4b`; `git diff --check` passed.

## Hypothesis

If `qwen3:4b` fits the installed Ollama runtime, `ollama list` and a one-prompt local generation call will succeed without changing the application’s hosted default.

## Plan

1. Verify current Ollama/provider configuration and delegated readiness.
2. Pull `qwen3:4b` with bounded command monitoring.
3. Run model-list, direct API, and project-provider smoke checks; update documentation evidence.

## Execution Checkpoints

- Delegation: Explore agent inspected `.env`, provider configuration, and local readiness without editing files.
- Download: `C:\Users\danny\AppData\Local\Programs\Ollama\ollama.exe pull qwen3:4b` completed successfully; downloaded size 2.5 GB.
- Validation: 6 focused tests passed; compilation passed; live project-provider call returned content and token usage; diff check passed.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `docs/CONFIGURATION_REFERENCE.md`.

## Completion

Completion recorded: yes

Summary: Downloaded qwen3:4b and made it callable through the project's local text-generation provider.

Validation: `pytest tests/test_text_generation_providers.py -q` passed 6 tests; `py_compile` passed; live qwen3:4b provider smoke call passed; `git diff --check` passed.

Residual risk: Model quality and throughput for legal summaries remain unbenchmarked. The Ollama executable is not on the current shell PATH, so use its full path or refresh PATH in new shells.

Next recommended task: Run a 10-paragraph summary pilot with JSON validation and resource measurements.
