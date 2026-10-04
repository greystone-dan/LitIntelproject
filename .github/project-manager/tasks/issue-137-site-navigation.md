# Task: Issue 137 shared site navigation and home

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

Task: Add shared accessible HTML navigation and a real tool-directory home.
Why now: Make research tools discoverable without replacing the active reader.
Owner surface: Backend HTML presentation (`backend/pages/site_nav.py`, runtime integration).
Commit allowed: no
Push allowed: no
Dependencies: Existing HTML routes and analyst quick-start descriptions.
Risk boundary: No DB, dotenv, deployment, dependencies, migrations, access-policy changes, or agent-directory reads. Preserve streaming, exports, APIs, password gate and source offsets. Parent owns parallel_validation.
Smallest falsifiable check: `python -m pytest -q tests/test_site_nav.py`
Acceptance criteria:
- Actual HTML route inventory is statically tested without database calls.
- Navigation, query-aware current state, deep breadcrumbs, keyboard-safe quick search, responsive menu, home descriptions and opt-outs work.
- Streaming/non-200/health/API/export/login and non-HTML responses remain unchanged.
- Focused tests, generated docs and full suite with the three CI deselections pass.
Docs/generated references: Existing `SYSTEM_REFERENCE.md`, `.swm/system-map.ovnldklv.sw.md`; generated references via their generators if needed.
Rollback/recovery: Remove middleware registration and restore former root response; no data changes.
Evidence: Initial worktree clean at `1ad33ef`. CI memory verified in `.github/workflows/tests.yml:23-37` and `requirements-dev.txt:1-4`. Issue retrieval blocked by absent GH authentication; user supplied detailed requirements. Progress tool unavailable; full pre-edit checklist provided in chat. Canonical document updated: `SYSTEM_REFERENCE.md`. Swimm updated: `.swm/system-map.ovnldklv.sw.md`. API reference regenerated with `python scripts/generate_api_reference.py`; `python scripts/check_generated_docs.py` passed (3 references). `git diff --check` and Python compilation passed.
Secret scan: Six credential/private-key patterns checked all tracked additions and three new files; zero matches. This is a bounded pattern scan, not a comprehensive security audit. No commit or push performed.
Files changed: `backend/pages/site_nav.py`, `backend/main.py`, `tests/test_site_nav.py`, `tests/test_security.py`, `SYSTEM_REFERENCE.md`, `.swm/system-map.ovnldklv.sw.md`, `docs/API_REFERENCE.generated.md`, this task record.
Delegated work: managed-worker `site-nav-owner` implemented the bounded presentation slice and returned all seven required headings. Its pytest attempts failed because system Python lacked tooling. Manager installed only existing declared pins into `/tmp/caselibrary-issue137-venv`, corrected test Accept headers and stale root expectations, and repaired LF-based body offsets, tab-state observation and citation-map deep context.
Focused validation: `python -m pytest -q tests/test_site_nav.py tests/test_feature_tabs.py tests/test_security.py` passed: 150 passed, 1 skipped. `python -m pytest -q tests/test_site_nav.py` initially exposed one test-client Accept-header mismatch (61 passed, 1 failed), corrected without changing access policy.
Residual risk: Full-suite acceptance blocked by three failures outside the owned implementation; browser validation explicitly waived. Static tests cannot prove visual layout. No commits/pushes or parent parallel_validation finalization.
Next bounded task: Parent-owned parallel_validation.

## Hypothesis

If a single guarded ASGI HTML decorator owns navigation, actual page builders retain their behavior while successful finite HTML gets exactly one accessible navigation shell.

## Plan

1. Delegate route inventory, presentation implementation and focused tests.
2. Accept or repair the bounded slice; update existing canonical and Swimm docs.
3. Validate generated references and full suite with CI deselections; scan final diff for secrets.

## Validation environment and final suite

Commands used `PATH=/tmp/caselibrary-issue137-venv/bin:$PATH` and
`PYTHONPATH=/tmp/caselibrary-issue137-safety:$PWD`. The external `sitecustomize.py`
disables dotenv loading and raises before any PostgreSQL connection; repository
configuration and dependency files are unchanged. Pytest's existing conftest
otherwise probes PostgreSQL during collection.

Final broad command:

```sh
python -m pytest -q \
  --deselect tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence \
  --deselect tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes \
  --deselect tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint \
  --cov=backend --cov-report=term-missing:skip-covered
```

Result: **3 failed, 1317 passed, 2 skipped, 3 deselected, 1 xfailed**;
backend coverage 75%. Earlier collection attempts lacked pyarrow and
huggingface-hub; installing their existing declared pins allowed full collection.
Earlier broad execution also found two stale root-redirect expectations in
`tests/test_security.py`, now updated and passing.

Remaining failures:

- `tests/test_api.py::test_local_chunk_search_uses_requested_model`: test patches
  `routes._local_embedding_provider`, but unchanged `backend/search_service.py`
  owns the called provider. The unmocked path requires sentence-transformers
  (not installed in the bounded validation environment) and potentially a model.
- `tests/test_openai_chunk_embeddings.py::test_count_embedding_tokens_uses_model_tokenizer`
  and `::test_count_embedding_tokens_treats_special_token_text_as_literal`:
  public tokenizer download hostname could not resolve.

Safe recovery: parent decides whether to run with a provisioned tokenizer/model
cache or assign a separate test-isolation repair. Do not download models or
change unrelated search/tokenizer implementations as part of this issue.
Workflow improvement: provision offline test tooling/cache before delegation;
the existing unconditional conftest DB probe needs an explicit offline mode in
a separate task. Parent owns `parallel_validation`; this record does not finalize it.
