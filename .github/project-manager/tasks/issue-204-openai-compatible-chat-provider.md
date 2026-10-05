# Task: Add OpenAI-compatible chat provider

Status: blocked
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
- Apply the issue #112 CI-deselected full-suite check without accessing PostgreSQL or dotenv; record its result or exact environment blocker.

Harness criteria:

The compatible provider contract, mode boundary, tests, and required docs are present and validated.

Docs/generated references: `docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md` (backend module inventory), `.swm/5.b49ftjal.sw.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, and generated references refreshed via their generator if affected. Government-readiness AI-use, data-flow, and subprocessor summaries were aligned with endpoint selection/locality.

Rollback/recovery: Revert only this issue's code, tests, docs, and task record; no data or schema changes are permitted.

Evidence: Fetched/merged `origin/main` before edits (`ab0b6f5`, #201) and again before final validation (`ed83bb7`, #213); both merges completed without conflict. Issue #112 Rules block evidence from `.github/project-manager/tasks/issue-171-dependency-audit-task.md`: no database, deploy-script, `.env`, feature-deletion, added-dependency, or password-gate changes. `gh issue view 112` could not authenticate in this environment; use the recorded Rules block and supplied issue #204 requirements. Requested `engine-tools-report_progress` and `parallel_validation` tools are unavailable; progress was reported in chat and final checks were run concurrently. Full-suite validation used a temporary `/tmp/caselibrary-issue204-venv`, `PYTHON_DOTENV_DISABLED=1`, and a process-local SQLAlchemy guard blocking non-SQLite connections because `tests/conftest.py` otherwise probes PostgreSQL at collection. No DB was accessed and no `.env` was read. Only packages already pinned in repository requirements were installed in `/tmp`; project dependency files were unchanged.

Files changed: `.github/project-manager/tasks/issue-204-openai-compatible-chat-provider.md`, `.github/project-manager/improvements/2026-10-04-guard-database-probes-in-pytest.md`, `backend/text_generation_providers.py`, `backend/routes.py`, `tests/test_text_generation_providers.py`, `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `SYSTEM_REFERENCE.md`, `.swm/5.b49ftjal.sw.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `docs/government-readiness/ai-use-statement.md`, `docs/government-readiness/data-flow.md`, `docs/government-readiness/subprocessors.md`, `CHANGELOG.md`.
Delegated work: `managed-worker` implemented only the provider/route/test slice and returned the required structured report. It added the compatible SDK provider, endpoint mode classification, route capability limits, and mocked HTTP/mode tests. Its initial compile/diff checks passed; its initial pytest attempt was blocked by missing system dependencies. Manager reviewed the diff and independently ran the focused tests.
Focused validation: The final focused run used a process-local SQLAlchemy guard rejecting non-SQLite connections, with `PYTHON_DOTENV_DISABLED=1`: 22 tests passed, 1 third-party deprecation warning. `PYTHON_DOTENV_DISABLED=1 /tmp/caselibrary-issue204-venv/bin/python scripts/check_generated_docs.py` — passed; 3 references current. Compilation, route/provider static contract, changed-line Markdown links, changed-file secret scan, and `git diff --check` passed. Earlier focused pytest invocations occurred before discovering the conftest behavior below; `tests/conftest.py` attempted its import-time localhost `SELECT 1` probe. That probe is read-only by source, but its connection outcome was not captured, so I cannot certify those earlier invocations made no DB connection. All later test runs used the connection guard.
Full-suite validation: CI's three `--deselect` filters and coverage flags were run under the process-local non-SQLite DB guard. Result: 1,651 passed, 4 failed, 4 skipped, 3 deselected, 1 xfailed. Two Chromium timeout failures passed when retried alone. The two remaining failures are tokenizer tests: `tiktoken` cannot download `cl100k_base.tiktoken` because `openaipublic.blob.core.windows.net` does not resolve. No project dependency files were changed to work around this.
Residual risk: Full CI-deselected suite is not green in this environment because tokenizer data is unavailable; initial browser subprocess timeouts passed on isolated retry. The configured compatible service's retention/processing location remain unverified. Live issue #112 could not be queried because `GH_TOKEN` is unavailable; the recorded Rules block was followed. A process recommendation was recorded to prevent pytest's import-time database probe from violating no-DB validation boundaries.
Next bounded task: Re-run the full CI-deselected suite with the `cl100k_base` asset available locally or in network-enabled CI, retaining the non-SQLite connection guard; then continue `/research` grounding evaluation.

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

Completion recorded: no

Summary: Implementation and focused acceptance checks are complete. The requested additional CI-deselected suite ran with non-SQLite DB connections blocked and dotenv disabled, but cannot be green here because the offline environment lacks the tokenizer vocabulary asset. Earlier unguarded focused pytest runs invoked conftest's read-only PostgreSQL availability probe; whether it connected is not known.

Validation: 22 focused tests passed; generated-doc, documentation-contract, changed-link, secret, compilation, static-contract, and diff checks passed. Guarded full suite: 1,651 passed, 4 failed, 4 skipped, 3 deselected, 1 xfailed. Two browser failures passed alone; two tokenizer tests fail on unavailable external vocabulary asset.

Residual risk: CI-deselected suite is not green in this network-restricted environment. The earlier unguarded conftest probe's connection outcome is unknown; all later tests blocked non-SQLite connections, and dotenv loading was disabled. External compatible endpoint behavior and retention remain operator/provider-specific.

Next recommended task: Add retrieval/context-grounding evaluation for experimental `/research` before treating it as production-facing.
