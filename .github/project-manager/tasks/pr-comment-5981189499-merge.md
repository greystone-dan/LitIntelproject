Task: Integrate origin/main and complete PR comment 5981189499.
Why now: Onboarding branch must retain main search operators and complete architecture coverage.
Owner surface: Research UI integration and architecture documentation.
Dependencies: Existing requirements-dev.txt environment; runtime secret scanner.
Risk boundary: No database, dotenv files, deployment, new dependencies, migration edits, or push.
Smallest falsifiable check: PYTHON_DOTENV_DISABLED=1 python -m pytest --noconftest -q tests/test_documentation_contracts.py tests/test_onboarding.py tests/test_query_syntax.py tests/test_search_matching.py tests/test_feature_tabs.py tests/test_database_config.py
Acceptance criteria: Resolve merge preserving both features; generated checks and focused tests pass; report full CI suite honestly; scan every changed file before merge commit with two expected parents.
Docs/generated references: docs/ARCHITECTURE.md; SYSTEM_REFERENCE.md; .swm/6.maiixtsw.sw.md; generate_* references.
Rollback/recovery: Repair only integration conflicts; leave merge uncommitted if secret scanning is unavailable.
Evidence: Snapshot conflict retains URL judge prefill and lazy issue request state; API conflict regenerated. All four generate_* scripts ran; check_generated_docs.py passed (3 references). Updated docs/ARCHITECTURE.md, docs/RESEARCH_UI_GUIDE.md, docs/CONFIGURATION_REFERENCE.md, SYSTEM_REFERENCE.md, .swm/6.maiixtsw.sw.md, and .swm/system-map.ovnldklv.sw.md. Focused command passed 268 tests, skipped 1 (Playwright absent); offline Chrome onboarding passed. Python compilation, 36 local links, and git diff --check passed. Runtime secret_scanning certified all 69 PR/merge changed paths clean before the final record update; repeat immediately before commit.
Delegation: managed-worker ui-merge owned snapshot conflict, inventory/test, onboarding coexistence regressions, UI guide and walkthrough; returned structured evidence. managed-worker suite-safety performed read-only offline test safety inspection.
Full validation: PYTHON_DOTENV_DISABLED=1 python -m pytest --noconftest -q --ignore=test_statute_integration.py --deselect tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence --deselect tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes --deselect tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint --cov=backend --cov-report=term-missing:skip-covered
Results: 1465 passed, 3 failed, 1 skipped, 3 deselected, 1 xfailed; backend coverage 78%. Failures: test_api local chunk model needs uncached Hugging Face model; two test_openai_chunk_embeddings tokenizer tests need cl100k_base download. Both hosts fail DNS. No unrelated repairs or tokenizer substitutions.
Residual risk: Exact CI command cannot run within the no-DB boundary: conftest eagerly probes PostgreSQL and root statute integration queries it. Standard --noconftest and explicit file ignore avoid both; only consumers of its fixture are already CI-deselected. No database/lifespan, deployment, new dependencies, or migration modifications beyond incoming main merge. Existing requirements-dev.txt installation succeeded; installed dotenv lacks standard disable support, so a guarded database import and mock-loader regressions supply it.
Next recommended task: Re-run the three download-dependent failures in an environment with legitimate model/tokenizer availability; separately guard eager DB collection in CI.
Status: complete
Commit allowed: yes
Push allowed: no
