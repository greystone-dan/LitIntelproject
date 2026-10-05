# Task: Integrate embedding registry with latest main

Status: in progress
Created: 2026-10-04
Updated: 2026-10-05

## Task Record

Task: Address PR comment 5990921329 by integrating the registry branch with latest main and preserving shared/provider work.

Why now: The requested current-main integration must retain PR #209 provider code and existing registry contracts while updating shared documentation and generated references.

Owner surface: Embedding model registry, shared documentation, generated references, and final Git integration.

Commit allowed: yes

Push allowed: no (`git push` is prohibited; publication is only through the requested `report_progress` workflow).

Dependencies: Latest `origin/main`, current feature tree, required repository documentation, and the embedding-registry Swimm walkthrough.

Risk boundary: Do not access databases or `.env` files, deploy, run bulk data jobs, change registry dimensions/prefixes/tables/routing, discard main provider behavior, or use `git push`. Fetch main immediately before the final true merge.

Smallest falsifiable check: `python -m pytest -q tests/test_embedding_registry.py tests/test_ai_mode.py tests/test_embedding_providers.py` and `python scripts/check_generated_docs.py`.

Acceptance criteria:

- Main provider code and registry behavior both survive; registry dimensions, prefixes, table routing, and fixed-width case-vector contract are preserved.
- Shared canonical documentation and the registry Swimm walkthrough reflect the resulting integration.
- Generated references are regenerated only from their scripts and pass `python scripts/check_generated_docs.py`.
- Focused tests and full `python -m pytest -q` with precisely the three CI deselections run; failures are reported honestly.
- A true merge commit includes freshly fetched latest main; the short hash is sent to PR comment 5990921329 only via `report_progress`, with no Git push.

Harness criteria: Focused provider/registry/API tests pass or their failures are recorded; generated documentation check passes; merge commit has latest main as second parent.

Docs/generated references: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `.swm/embedding-registry-205.sw.md`; generated API/schema/script catalog references via source generators.

Rollback/recovery: Preserve the feature-branch commit. If latest-main merge or validation reveals unsafe behavior, stop before publication and record the blocker; do not force-resolve, reset, or push.

Evidence: Starting HEAD `20d2026` is a merge commit whose first parent is `473508851d600b74e0cd29bbbdf92c6118954aa3`; the reported refreshed `origin/main` is `6687f6b954f383ef431a7e4ac9c2e112f2ca4841` with that merge base. Initial worktree was clean. Prior task evidence recorded provider conflict resolution, shared-doc updates, generators, and a full test run against an older merge base; those results do not establish acceptance against latest main. The reporting tool's availability remains to be checked at publication time.

Files changed: `backend/query_embedding_providers.py`, `tests/test_embedding_providers.py` (delegated integration guard/test); documentation, generated references, and merge changes pending.
Delegated work: `managed-worker` reconciled focused provider-stack behavior against local `origin/main`; structured return verified the 1536-dimensional case-summary guard and mode-gate order while preserving registry routing. The focused test could not run because system Python lacked pytest. Manager is preparing an isolated environment from existing `requirements-dev.txt`.
Focused validation: Worker AST syntax and `git diff --check` passed; its test attempt was blocked by missing system pytest. Manager installed only existing `requirements-dev.txt` in isolated `/tmp/caselib-merge-venv`; `PYTHON_DOTENV_DISABLED=1 HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 /tmp/caselib-merge-venv/bin/python -m pytest -q tests/test_embedding_registry.py tests/test_ai_mode.py tests/test_embedding_providers.py` passed (46 tests, three warnings).
Residual risk: Pending.
Next bounded task: Pending.

## Hypothesis

If latest-main integration is correct, provider/registry checks and generated-document validation will pass without altering registry routing contracts or removing main's provider implementation.

## Plan

1. Inspect current merge result and preserve the latest shared documentation.
2. Regenerate generated references through their generators only if source changes require it.
3. Run focused and full validation; fetch latest main immediately before the true final merge and publish only through `report_progress` if available.

## Execution Checkpoints

- Delegation: `managed-worker`, bounded provider stack reconciliation; see Evidence and delegated structured report in session.
- Implementation: `backend/query_embedding_providers.py` now gates mode before checking width and skips API-ingestion case summaries that do not match the fixed 1536-dimensional case-vector contract; regression test added.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/embedding-registry-205.sw.md`.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-05 | Continue existing merge task for PR comment 5990921329 | The current branch already has an earlier merge, but latest main must be integrated and validated | `HEAD=20d2026`; reported `origin/main=6687f6b` |
| 2026-10-05 | Delegate provider integration guard/test | Preserve the fixed case-vector contract and keep mode gates authoritative | Structured `managed-worker` return; focused tests blocked by missing pytest |

## Completion

Completion recorded: no

Summary: Pending.

Validation: Pending.

Residual risk: Pending.

Next recommended task: Pending.
