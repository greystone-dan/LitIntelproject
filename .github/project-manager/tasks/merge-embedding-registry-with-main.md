# Task: Integrate embedding registry with latest main

Status: blocked
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

Evidence: Starting HEAD `20d2026` was a merge commit whose first parent was `473508851d600b74e0cd29bbbdf92c6118954aa3`; freshly fetched `origin/main` is `6687f6b954f383ef431a7e4ac9c2e112f2ca4841`, with the same merge base. Initial worktree was clean. The final true merge commit is `2a11a20fe50b41db22794ccd364b3e5872b67ee6` with parents `aa1c9704de7f4e9d4aebe3a90d5a3558c3875b97` and `6687f6b954f383ef431a7e4ac9c2e112f2ca4841`. Conflicts were confined to `SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`, and generated API/schema references. Shared docs retain main's provider additions and explain the registry without schema changes; latest-main provider and documentation changes remain integrated. CI evidence supplied by the user confirms main-tip Tests and Documentation Sync runs `37267856978` and `37267856996` succeeded; earlier run `37266673439` failed only on an unrelated 30-second Chromium timeout in `tests/test_paragraph_similarity.py::test_active_reader_feature_and_mock_browser`, superseded by the passing latest tip. These runs validate main, not the merged feature branch. Generated references were recreated with all three source scripts; final `scripts/check_generated_docs.py` passed. Canonical docs and both relevant Swimm walkthroughs were corrected; local-link review checked 59 links and found four known pre-existing broken `SYSTEM_REFERENCE.md` links. A first focused/full pytest attempt with `PYTHON_DOTENV_DISABLED=1` did not block `tests/conftest.py`'s implicit `SessionLocal().execute("SELECT 1")` probe; whether that connection succeeded was not captured, and no writes were intended. Subsequent focused and full runs used a temporary startup guard blocking project `engine.connect` and `raw_connection`, plus offline model/network settings; a self-check confirmed the probe is intercepted. The guarded full suite produced `2805 passed, 2 failed, 5 skipped, 3 deselected, 1 xfailed`; both failures are tokenizer tests trying to retrieve `cl100k_base.tiktoken` from `openaipublic.blob.core.windows.net`, blocked by the offline proxy. Final focused tests passed (55); registry fields were programmatically verified unchanged; secret-pattern scan found no matches in 108 changed text files. `parallel_validation` and `report_progress` are not available in this toolset; no `git push` or alternate comment method was used.

Files changed: `backend/query_embedding_providers.py`; `tests/test_embedding_providers.py`; `SYSTEM_REFERENCE.md`; `DOCS_INDEX.md`; `docs/CONFIGURATION_REFERENCE.md`; `docs/ARCHITECTURE.md`; `.swm/embedding-registry-205.sw.md`; `.swm/2.40nypbay.sw.md`; `.github/project-manager/improvements/2026-10-04-guard-database-probes-in-pytest.md`; generated API/schema/script-catalog references; plus latest-main merge changes.
Delegated work: `managed-worker` reconciled provider-stack behavior against local `origin/main`; structured return preserved registry routing and added the 1536-dimensional case-summary guard/mode-gate ordering. Its system pytest attempt was blocked by missing pytest.
Focused validation: With the project DB engine blocked in process, `tests/test_embedding_registry.py`, `tests/test_ai_mode.py`, `tests/test_embedding_providers.py`, and `tests/test_text_generation_providers.py` passed (55). A prior unguarded focus invocation passed 46 but was not accepted as no-DB evidence due to the conftest probe.
Residual risk: Two tokenizer tests require unavailable network data; the earlier unguarded conftest probe's connection outcome is unknown. No `.env` values were enabled (`PYTHON_DOTENV_DISABLED=1`). The available tool list has no `report_progress` integration, so PR comment publication is blocked; no alternative commenting or `git push` is authorized.
Next bounded task: Publish merge commit `2a11a20` to PR comment 5990921329 through `report_progress` once that reporting integration is available; do not use `git push`.

## Hypothesis

If latest-main integration is correct, provider/registry checks and generated-document validation will pass without altering registry routing contracts or removing main's provider implementation.

## Plan

1. Inspect current merge result and preserve the latest shared documentation.
2. Regenerate generated references through their generators only if source changes require it.
3. Run focused and full validation; fetch latest main immediately before the true final merge and publish only through `report_progress` if available.

## Execution Checkpoints

- Delegation: `managed-worker`, bounded provider stack reconciliation; see Evidence and delegated structured report in session.
- Implementation: Prep commit `aa1c970` gates mode before width checks and skips API-ingestion summaries that do not match the fixed 1536-dimensional case-vector contract; regression test added.
- Documentation: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `docs/CONFIGURATION_REFERENCE.md`, `docs/ARCHITECTURE.md`, `.swm/embedding-registry-205.sw.md`, `.swm/2.40nypbay.sw.md`; all three generated references regenerated and checked.
- Recovery: Not applicable.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-05 | Continue existing merge task for PR comment 5990921329 | The current branch already has an earlier merge, but latest main must be integrated and validated | `HEAD=20d2026`; reported `origin/main=6687f6b` |
| 2026-10-05 | Delegate provider integration guard/test | Preserve the fixed case-vector contract and keep mode gates authoritative | Structured `managed-worker` return; focused tests blocked by missing pytest |

## Completion

Completion recorded: no

Summary: Latest main has been merged locally with registry contracts and provider code preserved; comment publication remains blocked by the absent reporting tool.

Validation: Generated docs check passed; guarded focused tests passed (55); guarded full suite ran with exactly three CI deselections (2805 passed, 2 tokenizer-network failures, 5 skipped, 1 xfailed); local-link scan found four pre-existing missing SYSTEM_REFERENCE links.

Residual risk: The implicit database probe was attempted before a temporary guard was introduced; its connection outcome is unknown. Two tests require unreachable tokenizer data. No `report_progress` tool is available.

Next recommended task: Publish the merge short hash through the authorized reporting integration once available.
