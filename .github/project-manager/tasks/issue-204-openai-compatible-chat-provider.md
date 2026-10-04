# Task: Add OpenAI-compatible chat provider

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #204: configurable OpenAI-compatible chat generation for `/research`.

Why now: Support compatible hosted chat APIs while keeping provider capability limits and the enhanced-mode locality boundary explicit.

Owner surface: Experimental `/research` answer generation (`backend/text_generation_providers.py`, its route call site, and focused tests).

Commit allowed: yes

Push allowed: yes

Dependencies: Current `ENHANCED_AI_MODE` and provider behavior; issue #112 Rules block.

Risk boundary: Do not access the database, edit `.env` or deploy scripts, add dependencies, weaken the off-mode gate, change citation/statute evidence, or discard unrelated branch changes. Preserve OpenAI and local Ollama behavior.

Smallest falsifiable check: Focused provider/research tests prove compatible mocked HTTP requests, provider capability-driven token/context limits, JSON-mode support, and that off mode constructs no provider.

Acceptance criteria:

- Add an OpenAI SDK custom-`base_url` compatible chat provider configured by `CHAT_BASE_URL`, optional `CHAT_API_KEY`, `CHAT_MODEL`, and `CHAT_TIMEOUT_SECONDS`, with advertised capabilities for context size, default output tokens, and JSON mode.
- `/research` uses provider capabilities and contains no `os.getenv("TEXT_GENERATION_PROVIDER")`; OpenAI and native local Ollama behavior remain compatible.
- Enhanced local mode accepts only localhost/private compatible endpoints; enhanced off mode never constructs a provider; invalid provider names report valid choices.
- Tests cover a mocked compatible endpoint and enhanced-mode gating.
- Update `docs/CONFIGURATION_REFERENCE.md`, the canonical system/architecture inventory, relevant Swimm walkthrough, and generated documentation from its generator.
- Focused tests, `scripts/check_generated_docs.py`, changed-file secret scan, and final validation pass.

Harness criteria:

The compatible provider contract, mode boundary, tests, and required docs are present and validated.

Docs/generated references: `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md` (backend module inventory), `.swm/5.b49ftjal.sw.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, and generated references refreshed via their generator if affected. Government-readiness AI-use, data-flow, and subprocessor summaries were aligned with endpoint selection/locality.

Rollback/recovery: Revert only this issue's code, tests, docs, and task record; no data or schema changes are permitted.

Evidence: Fetched/merged `origin/main` before edits (`ab0b6f5`, #201) and again before final validation (`ed83bb7`, #213); both merges completed without conflict. Issue #112 Rules block evidence from `.github/project-manager/tasks/issue-171-dependency-audit-task.md`: no database, deploy-script, `.env`, feature-deletion, added-dependency, or password-gate changes. `gh issue view 112` could not authenticate in this environment; use the recorded Rules block and supplied issue #204 requirements. Requested `engine-tools-report_progress` and `parallel_validation` tools are unavailable; checklist/progress were reported in chat and final checks were run concurrently. Initial system Python lacked test dependencies; used a temporary `/tmp/caselibrary-issue204-venv` with dotenv loading disabled (`PYTHON_DOTENV_DISABLED=1`) and no database connections.

Files changed: `.github/project-manager/tasks/issue-204-openai-compatible-chat-provider.md`, `backend/text_generation_providers.py`, `backend/routes.py`, `tests/test_text_generation_providers.py`, `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, `.swm/5.b49ftjal.sw.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `docs/government-readiness/ai-use-statement.md`, `docs/government-readiness/data-flow.md`, `docs/government-readiness/subprocessors.md`, `CHANGELOG.md`.
Delegated work: `managed-worker` implemented only the provider/route/test slice and returned the required structured report. It added the compatible SDK provider, endpoint mode classification, route capability limits, and mocked HTTP/mode tests. Its initial compile/diff checks passed; its initial pytest attempt was blocked by missing system dependencies. Manager reviewed the diff and independently ran the focused tests.
Focused validation: `PYTHON_DOTENV_DISABLED=1 /tmp/caselibrary-issue204-venv/bin/python -m pytest -q tests/test_text_generation_providers.py tests/test_ai_mode.py tests/test_documentation_contracts.py tests/test_government_readiness_docs.py` — 22 passed, 1 third-party deprecation warning. `PYTHON_DOTENV_DISABLED=1 /tmp/caselibrary-issue204-venv/bin/python scripts/check_generated_docs.py` — passed; 3 references current. `python -m compileall -q backend/text_generation_providers.py backend/routes.py tests/test_text_generation_providers.py`, route/provider contract assertions, changed-line Markdown link scan, changed-file secret scan, and `git diff --check` passed. An unrestricted local-link scan found four pre-existing unresolved links in `SYSTEM_REFERENCE.md` outside this change; no added links are broken.
Residual risk: The configured compatible service's retention, processing location, and API behavior are provider-specific and remain unverified; no full suite or browser test was run. Live issue #112 could not be queried because `GH_TOKEN` is unavailable; its recorded Rules block was followed. Commit/push validation is the remaining checkpoint.
Next bounded task: Add retrieval/context-grounding evaluation for experimental `/research` before treating it as production-facing.

## Hypothesis

If `/research` selects providers only after its off-mode check, uses provider context/output limits, and exposes JSON-mode capability metadata, focused tests will demonstrate compatible endpoint behavior without regressing OpenAI or local Ollama operation.

## Plan

1. Implement the bounded provider and route/test slice.
2. Update configuration, architecture inventory, and Swimm; refresh generated references if applicable.
3. Run focused validation, secret scan, latest-main merge, and final validation before commit/push.

## Execution Checkpoints

- Delegation: `managed-worker` returned structured findings for provider, route, and tests; see evidence above.
- Implementation: Code slice implemented; focused provider and mode tests pass.
- Documentation: Updated `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, both relevant Swimm walkthroughs, government-readiness AI-use/data-flow/subprocessor docs, and `CHANGELOG.md`.
- Recovery: Not applicable; no long-running operation or persistent state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | Issue #204 is a multi-step provider/API/test/documentation change. | User requirements; repository guidance and issue #112 Rules block recorded above. |

## Completion

Completion recorded: yes

Summary: Added the OpenAI-SDK compatible chat provider and capability-driven `/research` limits, preserved OpenAI/Ollama and mode gates, and updated configuration, architecture, privacy/data-flow, Swimm, and changelog documentation.

Validation: 22 focused tests passed; generated-doc, documentation-contract, changed-link, secret, compilation, static-contract, and diff checks passed after merging latest `origin/main`.

Residual risk: External compatible endpoint behavior and retention remain operator/provider-specific; full-suite and browser validation were not run.

Next recommended task: Add retrieval/context-grounding evaluation for experimental `/research` before treating it as production-facing.
