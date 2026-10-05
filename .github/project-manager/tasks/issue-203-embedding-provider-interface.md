# Task: Shared embedding provider interface

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #203's common embedding provider interface and route
search/query and ingestion embedding calls through policy-aware configured
providers.

Why now: Search and ingestion need one consistent provider boundary so
off-by-default operation cannot construct models or send user text externally.

Owner surface: `backend` embedding-provider orchestration and its search,
query, and ingestion call sites.

Commit allowed: yes, through the requested `report_progress` workflow only.

Push allowed: yes, through the requested `report_progress` workflow only.

Dependencies: Existing `backend/ai_mode.py` policy, search/query paths, local and
hosted embedding configurations, and available embedding packages.

Risk boundary: Preserve zero outbound calls and no model construction in
`ENHANCED_AI_MODE=off`; `local` may use only local providers; `hosted` permits
any configured provider. Do not pass user text to a model unless enhanced mode
is enabled. Preserve 503 missing-key and 502 provider-failure API behavior and
provider-specific vector dimensions. Respect issue #112's shared safeguards:
no database, deployment, or `.env` operations. Its reader-specific file scope
does not apply to this embedding task. Use fake clients and do not download
models.

Smallest falsifiable check: Focused fake-client tests prove off-mode does not
construct/call a provider, local mode stays local, hosted selection works, and
API failure/dimension contracts remain stable.

Acceptance criteria:

- A common abstract `EmbeddingProvider` is implemented with OpenAI, cached
  SentenceTransformer, and default `NoneEmbeddingProvider` implementations.
- Search/query and ingestion embedding calls use the configured provider and
  comply with `backend/ai_mode.py`.
- Off mode constructs no model and makes no outbound embedding calls; local mode
  uses local providers only; hosted mode permits hosted providers.
- No user text reaches a model when enhanced mode is disabled.
- Missing OpenAI key remains HTTP 503, provider errors remain HTTP 502, and
  embedding dimensions are sized/reported by the selected provider.
- Focused fake-client tests pass without model downloads or DB access.
- Update the architecture inventory, relevant canonical docs and Swimm
  walkthrough; regenerate generated documentation and run required checks.

Harness criteria: Off mode produces no provider construction or invocation.
Local mode cannot select hosted embedding providers. Hosted mode permits the
configured OpenAI provider. Provider dimensions and existing 503/502 API
contracts are preserved.

Docs/generated references: `docs/ARCHITECTURE.md`,
`SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`,
`.swm/5.b49ftjal.sw.md`, `.swm/3.sl0qpkcv.sw.md`,
`.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`,
`.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md`, generated
API reference via `scripts/check_generated_docs.py`.

Rollback/recovery: Revert the provider abstraction, call-site wiring, tests,
and documentation; no schema, data, or model artifact changes are planned.

Evidence: Fetched `origin/main` at `ab0b6f5` (#201) before implementation; it
was an ancestor of starting HEAD `7dd24c4`. The current remote main tip is
`144efa1` (#195), parent `ed83bb7` (#213), and is not an ancestor of this branch.
Its changes overlap this work in `backend/routes.py`, `CHANGELOG.md`,
`SYSTEM_REFERENCE.md`, and `docs/ARCHITECTURE.md`; the complete main-to-branch
delta also includes other unrelated files. The merge-branch skill is not
available, and merging would create a commit outside the requested
`report_progress` workflow, so integration and publication remain blocked. The
`report_progress` and `parallel_validation` commands/tools are unavailable; sent
the pre-edit checklist in chat. User
clarified that issue #112 is a closed reader-specific task: only its shared
no-database/deploy/`.env` safeguards apply here, not its reader-only file scope.
GitHub CLI issue lookup is unavailable without `GH_TOKEN`; implementation
follows the user-supplied issue requirements. User reports the latest Actions
run is `action_required` with zero jobs and no failed logs, so there is no
actionable CI failure. `requirements-dev.txt` includes `pytest-cov==5.0.0` and
inherits `requirements.txt`; the quality workflow's dependency audit is
non-blocking.

Files changed: `backend/embedding_providers.py`,
`backend/query_embedding_providers.py`, `backend/routes.py`,
`tests/test_embedding_providers.py`, `docs/ARCHITECTURE.md`,
`docs/CONFIGURATION_REFERENCE.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`,
`.github/project-manager/improvements/2026-10-04-isolated-focused-test-environment.md`,
`.swm/3.sl0qpkcv.sw.md`, `.swm/5.b49ftjal.sw.md`,
`.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`,
`.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md`, and this
task record.
Delegated work: `managed-worker` implemented backend provider/query/ingestion
wiring and fake-client/model tests in the first four files; returned the
required structured report. Worker compilation and diff checks passed; worker
pytest was blocked by missing pytest. Manager reviewed the changed code and
performed final acceptance checks.
Focused validation: In an isolated `/tmp/issue203-embedding-venv` with selected
existing pinned dependencies (no model packages), passed
`PYTHON_DOTENV_DISABLED=1 /tmp/issue203-embedding-venv/bin/python -m pytest -q
tests/test_embedding_providers.py` (7 passed) and
`PYTHON_DOTENV_DISABLED=1 /tmp/issue203-embedding-venv/bin/python -m pytest -q
tests/test_api.py -k 'search_embedding_status_reports_no_embedding_default or
default_semantic_search_falls_back_without_constructing_model_client or
local_query_embedding_with_matching_indexed_dimensions or
local_query_embedding_mismatch_fails_before_provider_use or
query_embedding_provider_supports_explicit_openai_opt_in_without_live_client or
search_lexical_mode_skips_embedding_call or ingest_stores_metadata_and_embedding
or ingest_skips_embedding_when_rollout_embed_disabled or
raw_ingest_skips_embedding'` (9 passed, 57 deselected). Passed
`PYTHON_DOTENV_DISABLED=1 /tmp/issue203-embedding-venv/bin/python
scripts/check_generated_docs.py` (three generated references current),
`python -m py_compile backend/embedding_providers.py
backend/query_embedding_providers.py backend/search_service.py backend/routes.py
tests/test_embedding_providers.py`, `git diff --check`, direct architecture/API
documentation contracts, Swimm local-link checks, and changed-file secret-pattern
scan (0 matches). Tests use fake providers and a fake DB; dotenv loading was
disabled. No database connection/query, `.env` access, or model download
occurred.
Residual risk: Current branch is behind newer #213/#195 main changes, including
overlapping route and documentation files. The
requested merge-branch and `report_progress`/`parallel_validation` tools remain
unavailable, so merge/commit/push was not performed. User reports the latest
Actions run is `action_required` with zero jobs and no failed logs; there is no
actionable CI failure.
Next bounded task: Merge current main `144efa1` through the repository workflow,
resolve/review the overlapping route and documentation changes, rerun focused
tests and generated-doc checks, and publish through `report_progress`.

## Hypothesis

If all embedding requests cross a shared provider boundary gated by
`backend/ai_mode.py`, fake-client checks will prove disabled mode creates no
model or outbound call while local and hosted modes retain their provider,
dimension, and API failure contracts.

## Plan

1. Delegate the provider/search/ingestion implementation and fake-client tests.
2. Update architecture inventory, canonical docs, and mapped Swimm walkthroughs.
3. Regenerate references and run focused tests, secret scan, and final checks.

## Execution Checkpoints

- Delegation: `managed-worker` changed the backend provider, query/ingestion
  integration, and fake-client test slice; a second managed worker installed a
  bounded temporary validation environment and passed the fake-only provider
  tests with no DB/.env/model access. Manager independently passed nine targeted
  API/search/ingestion tests and generated-reference validation.
- Implementation: Provider interface/adapters and `backend/ai_mode.py`-gated
  query and case-ingestion paths added; Python compilation passed.
- Documentation: Updated `docs/ARCHITECTURE.md`, `docs/CONFIGURATION_REFERENCE.md`,
  `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, a manager improvement record, and Swimm walkthroughs
  `.swm/3.sl0qpkcv.sw.md`, `.swm/5.b49ftjal.sw.md`, and
  `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md` plus
  `.swm/technical-debt-register-and-improvement-queue.tlm730zr.sw.md`.
- Recovery: No persistent state or database operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use one shared provider interface with adapters | Compared per-call-site wrappers, a generic registry in the query-only module, and a shared provider module. The shared module centralizes lifecycle/dimensions while preserving call-site contracts; per-call-site wrappers duplicate behavior, and a query-owned registry does not cleanly serve ingestion. | Issue #203 requirements and existing mode policy |

## Completion

Completion recorded: no

Summary: Implementation, documentation, focused fake-provider/API checks, and
generated-reference validation passed on the task branch. Final status remains
blocked because current main advanced and overlaps this change, and the required
merge/publication workflow is unavailable.

Validation: Seven new provider tests and nine targeted API/search/ingestion tests
passed; generated docs (three references), Python compilation, diff check,
architecture/API documentation contracts, Swimm local links, and the final
secret-pattern scan passed. No model or database operations were performed.

Residual risk: Latest main is not integrated; main changes overlap
`backend/routes.py` and three canonical docs. The issue branch is not
committed/pushed because the required workflow tools are unavailable. The
dependency-environment workflow recommendation is deferred under
`.github/project-manager/improvements/`.

Next recommended task: Finish merge/publication through the requested tools.
