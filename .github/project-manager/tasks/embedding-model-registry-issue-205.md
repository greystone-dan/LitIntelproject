# Task: Configuration-driven embedding model registry

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #205's configuration-driven embedding model registry without hard-coded model names or vector widths.

Why now: Provider/model selection and vector compatibility must be explicit and testable for hosted OpenAI and local BGE-M3 embedding paths.

Owner surface: Embedding provider configuration and selection (`backend/embedding_providers.py` and its direct config/test call sites).

Commit allowed: yes

Push allowed: no

Dependencies: Existing enhanced AI mode configuration and embedding provider contracts. Issue #205's full text is unavailable (GitHub API/web return 403); implementation follows the detailed requirements supplied in the user request.

Risk boundary: No database access or schema changes, no `.env` reads/writes, no deployment scripts, no provider/network calls, and no bulk re-embedding. Preserve distinct hosted/local model and dimension contracts. The local issue #112 Rules evidence also prohibits feature deletion, adding dependencies, and enabling a password gate; none occurred.

Smallest falsifiable check: Focused offline tests for both `text-embedding-3-small` and `BAAI/bge-m3` selections in hosted/local enhanced modes, asserting configured model/dimension metadata and no external calls.

Acceptance criteria:

- Model identifiers and embedding widths come from a configuration-driven registry rather than provider/model-specific literals in runtime selection.
- Hosted and local enhanced-mode selection remains explicit and returns the correct registered model/dimension metadata.
- Focused tests cover `text-embedding-3-small` and `BAAI/bge-m3` without external calls.
- Canonical repository documentation and the relevant Swimm walkthrough describe the registry and fixed schema boundary.
- Generated-document sources are run; any environment or drift blocker is explicitly recorded.
- Issue #112 Rules-block requirements are verified locally and honored.

Harness criteria:

Registry-driven hosted and local embedding model metadata passes offline focused tests.
Canonical and Swimm docs describe the registry; generated-document limitations are recorded.

Docs/generated references: `SYSTEM_REFERENCE.md`, relevant `.swm/` embedding walkthrough, and generated API/schema/script references via their generator/check; `DOCS_INDEX.md` ownership guidance if needed.

Rollback/recovery: Revert the isolated provider/config/tests/docs change; no persisted vectors or schema are modified.

Evidence: Initial `main` fetch was `ab0b6f59ad228b8de1007d4a32bc48ab27362d33` (#201). Final fetch was `144efa172615b3061e27db49db00b8aa1460900e` (#195), merged by `999be64`; implementation commit is `db71b5e`. A clean `git merge-tree --write-tree` preview preceded integration. The issue #112 Rules block was verified from `.github/project-manager/tasks/issue-171-dependency-audit-task.md`: no database/deploy-script/`.env` changes, feature deletion, added dependencies, or password-gate activation. Post-merge focused tests passed: `python -m pytest -q tests/test_embedding_registry.py tests/test_local_embeddings.py tests/test_canlaw_embeddings.py` (27 passed). Python compilation, `git diff --check`, changed-file credential-pattern scan, and the focused Swimm link check passed. `python scripts/check_generated_docs.py` is blocked by missing `httpx`; the API generator's output omitted 58 hidden routes in this environment and was not retained. Post-merge AI/API test collection is likewise blocked by missing `httpx`. A wider link scan found four pre-existing unresolved links elsewhere in `SYSTEM_REFERENCE.md`; no new walkthrough links are broken.

Files changed: `.github/project-manager/tasks/embedding-model-registry-issue-205.md`; `.swm/embedding-registry-205.sw.md`; `SYSTEM_REFERENCE.md`; `docs/CONFIGURATION_REFERENCE.md`; `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`; `config.yaml`; `backend/embedding_registry.py`; `backend/embedding_providers.py`; `backend/query_embedding_providers.py`; `backend/search_service.py`; `backend/models.py`; `backend/unit_search.py`; `tests/test_embedding_registry.py`; `tests/test_local_embeddings.py`; `tests/test_ai_mode.py`; `tests/test_api.py`.
Delegated work: `managed-worker` implemented an initial registry/provider/test/doc slice. Manager review found and corrected remaining Python defaults, missing enhanced-mode assertions, a noncanonical standalone guide, and runtime search literals. Manager validated final claims independently.
Focused validation: `python -m pytest -q tests/test_embedding_registry.py tests/test_local_embeddings.py tests/test_canlaw_embeddings.py` passed (27 tests); `python -m py_compile backend/embedding_registry.py backend/embedding_providers.py backend/query_embedding_providers.py backend/search_service.py backend/models.py backend/unit_search.py tests/test_embedding_registry.py tests/test_local_embeddings.py tests/test_ai_mode.py tests/test_api.py`, `git diff --check`, credential scan, and focused Swimm local-link check passed. `python scripts/check_generated_docs.py` and focused `tests/test_api.py` collection failed because `httpx` is not installed.
Residual risk: Issue #205 full text remains inaccessible. API/generated-document verification needs an environment with the existing `httpx` dependency. The standard fixed case-vector schema remains 1536-dimensional; configuration does not migrate or re-embed vectors. The full documentation-link scan found four pre-existing broken links outside the new walkthrough.
Next bounded task: Use a dependency-complete environment to rerun API/generated-doc checks and compare acceptance against issue #205's full owner text.

## Hypothesis

If embedding model identity and output width are supplied by a registry-backed configuration, the focused offline provider tests will select compatible hosted and local model metadata without embedding-specific hard-coded widths or making external calls.

## Plan

1. Inspect embedding provider/config/test ownership and find local evidence for issue #112's Rules block.
2. Implement registry-backed selection and focused offline hosted/local tests.
3. Update canonical and Swimm docs, attempt generated-reference validation, and run focused checks and a secret scan.

## Execution Checkpoints

- Delegation: Managed worker implemented initial provider/registry/tests and proposed docs; manager corrected the slice after acceptance review.
- Implementation: Registry loaded from `config.yaml`; runtime selection/status and provider dimensions use registered metadata.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, and `.swm/embedding-registry-205.sw.md`.
- Main integration: Committed the validated slice as `db71b5e`; merged fetched #195 (`144efa1`) as `999be64`. Auto-merge completed without conflicts.
- Recovery: No database or persistent run artifacts involved.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Record task and avoid main merge | Feature branch already descends from fetched latest main | `git merge-base HEAD FETCH_HEAD` returned the fetched main SHA; `git diff --stat HEAD..FETCH_HEAD` was empty |
| 2026-10-04 | Keep issue-access uncertainty visible | GitHub CLI and unauthenticated API access returned 403 | `gh issue view 205/112`; `curl` GitHub issue API |
| 2026-10-04 | Use repository-local issue #112 Rules evidence | Public issue access returned 403, but the completed issue #171 record preserves the exact Rules block | `.github/project-manager/tasks/issue-171-dependency-audit-task.md` |
| 2026-10-04 | Keep generated/API output unchanged after unsafe drift | The missing-`httpx` environment's API generator output removed 58 hidden routes; schema/script generator changes were timestamp-only | `python scripts/check_generated_docs.py`; generated API diff review |
| 2026-10-04 | Preserve latest-main integration safely | Merge preview is conflict-free; Git refused because local edits overlap two main-updated files | `git merge-tree --write-tree HEAD FETCH_HEAD`; `git merge --no-edit FETCH_HEAD` |
| 2026-10-04 | Integrate fetched main after preserving local work | Committed the validated slice, then merged #195 cleanly; no push | `db71b5e`; `999be64`; post-merge focused validation |

## Completion

Completion recorded: no

Summary: Implementation and canonical/Swimm documentation are in place and latest fetched main is merged; task remains blocked on dependency-complete generated/API validation.

Validation: Focused registry/local/CanLaw tests passed (27); compilation, diff, secret, and focused Swimm link checks passed. Generated-doc/API validation could not complete because `httpx` is not installed.

Residual risk: Issue #205 full text remains unavailable. No generated reference output with unrelated route omissions was retained.

Next recommended task: Rerun generated-doc/API validation in a dependency-complete environment and compare against the full issue #205 owner text.
