# Task: Port saved searches and alerts for issue #78

Status: blocked
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Port the saved searches/alerts feature requested by issue #78 from PR #33 onto current main, including persistence, API, maintenance script, `/saved-searches-ui`, and Case Search save-current-query/filter controls.

Why now: Enable researchers to preserve and revisit bounded search criteria without changing existing search behavior for users who have no saved searches.

Owner surface: Saved-search workflow (backend persistence/API, Case Search and standalone UI, and operational checker).

Commit allowed: no

Push allowed: no

Dependencies: Current main schema head, existing case-search request/filter contract, and PR #33 implementation as reference.

Risk boundary: No canonical PostgreSQL access or writes; focused route tests use mocked sessions and the full suite uses its isolated temporary SQLite fixtures only. Preserve current search behavior when saved searches are absent; maintain one Alembic head chained from current main; do not push the PR #33 branch; preserve unrelated worktree state.

Smallest falsifiable check: Focused saved-search route and Case Search markup tests, plus static Alembic head/parent inspection without a database connection.

Acceptance criteria:

- Saved-search models, API routes, `scripts/check_saved_searches.py`, `/saved-searches-ui`, and redesigned Case Search save-current-query/filter control are implemented.
- With no saved searches, existing case-search behavior is unchanged.
- Exactly one Alembic head remains and the new revision chains from current main's latest revision.
- Tests cover saved-search routes and button markup.
- Run `python -m pytest -q` with the repository CI deselects; no database access.
- PR description explicitly says it supersedes `greystone-dan/LitIntelproject#33`; do not push the PR #33 branch.

Harness criteria:

- Focused saved-search API and UI contract tests pass.
- Migration graph has exactly one head and the saved-search revision descends from main's prior head.
- Full test command passes with CI deselects and performs no database access.
- Canonical docs and the relevant Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, relevant Swimm API/search/UI/schema walkthrough; regenerate API/schema/script-catalog references from their generators.

Rollback/recovery: Revert the saved-search migration and feature code together before deployment; no database has been accessed or mutated in this task.

Evidence: Initial worktree was clean on `copilot/claudesaved-searches-alerts`. Implemented the requested saved-search workflow. Updated canonical documents `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `OVERNIGHT.md`, and `docs/RESEARCH_UI_GUIDE.md`; updated Swimm walkthroughs `.swm/1.oi7rhqp2.sw.md`, `.swm/2.40nypbay.sw.md`, and `.swm/6.maiixtsw.sw.md`.

Files changed: `.github/project-manager/tasks/issue-78-saved-searches-alerts.md`, `backend/database.py`, `backend/models.py`, `backend/routes.py`, `backend/pages/data_explorer.py`, `backend/pages/saved_searches.py`, `alembic/versions/0031_saved_searches_alerts.py`, `scripts/check_saved_searches.py`, `scripts/generate_script_catalog.py`, `tests/test_saved_search_routes.py`, `tests/test_check_saved_searches.py`, `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `OVERNIGHT.md`, `docs/RESEARCH_UI_GUIDE.md`, `docs/API_REFERENCE.generated.md`, `docs/SCHEMA_REFERENCE.generated.md`, `docs/SCRIPT_CATALOG.generated.md`, and the three Swimm paths above.
Delegated work: `saved-search-api` managed worker ported persistence/contracts/routes/migration and updated `SYSTEM_REFERENCE.md` plus `.swm/1.oi7rhqp2.sw.md`. Structured report received. Static graph evidence: `0030_full_paragraph_ivfflat` -> `0031_saved_searches_alerts`, single head `0031_saved_searches_alerts`. No canonical database connection or migration execution.
Focused validation: `python -m pytest -q tests/test_saved_search_routes.py tests/test_check_saved_searches.py tests/test_feature_tabs.py` — 63 passed. `python scripts/check_saved_searches.py --help` passed without importing DB modules. `python -m alembic heads` reported only `0031_saved_searches_alerts`; history confirms its parent is `0030_full_paragraph_ivfflat`. `python scripts/check_generated_docs.py`, Python compileall, and `git diff --check` passed.
Full validation: Ran `python -m pytest -q --deselect tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence --deselect tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes --deselect tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint`, matching `.github/workflows/tests.yml`. Result: 991 passed, 3 failed, 3 deselected. The three failures require unavailable external model/tokenizer downloads (`huggingface.co` BGE-M3 assets and OpenAI `cl100k_base.tiktoken`); this environment has no DNS/network access or cached assets. No PostgreSQL tests were run; repository tests did use isolated temporary SQLite fixtures.
Security validation: Targeted changed-file scan for common private-key, AWS, GitHub, and OpenAI credential patterns found no matches across 22 changed paths; no dedicated secret scanner is installed.
Residual risk: Full-suite completion is blocked by three unrelated network-dependent tests. UI markup and routes were tested, but no live browser check was available. PR has not been created or published; its description must include `Supersedes greystone-dan/LitIntelproject#33.` `report_progress` is unavailable, so no commit or push was performed.
Next bounded task: Re-run the exact CI pytest command in an environment with the BGE-M3 and `cl100k_base.tiktoken` assets cached or network access available; then create the PR with the supersedes statement.

## Hypothesis

If the saved-search API and UI are ported without altering the existing search contract, the focused contract tests will show both save/list behavior and unchanged default Case Search behavior when no searches exist.

## Plan

1. Delegate a bounded reference/implementation slice before equivalent PR discovery.
2. Integrate remaining scripts and UI behavior, then run the narrow API, markup, and migration checks.
3. Regenerate references, update canonical and Swimm documentation, run secret scan and repository parallel validation, then run the full pytest command with CI deselects.

## Execution Checkpoints

- Delegation: `saved-search-api` completed the backend/migration slice; structured report received.
- Implementation: Saved-search API/schema, checker, standalone page, and Case Search save control added; 63 focused tests passed.
- Documentation: Updated canonical system, operational, changelog, and UI docs plus the relevant API, schema, and UI Swimm walkthroughs.
- Recovery: Not applicable; no database operations.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Task created; commit and push disabled | User requires publication only through unavailable `report_progress`; preserve no-push boundary | User acceptance and repository manager workflow |
| 2026-10-03 | Backend/migration slice accepted for integration | Static graph checks passed; focused mocked route tests pass after installing project requirements | Managed-worker report; `python -m pytest -q tests/test_saved_search_routes.py` |
| 2026-10-03 | Task blocked after full-suite attempt | Three non-feature tests require uncached external Hugging Face/OpenAI tokenizer assets | 991 passed, 3 failed, 3 deselected under CI command |

## Completion

Completion recorded: no

Summary: Implementation and focused checks are complete; full-suite acceptance is blocked by unavailable external test assets.

Validation: Focused checks passed (63); full CI-deselected command returned 991 passed / 3 failed / 3 deselected.

Residual risk: Full suite needs the required external assets; no PostgreSQL access or browser run occurred.

Next recommended task: Re-run the exact CI pytest command where BGE-M3 and `cl100k_base.tiktoken` assets are available; then create the PR with the required supersedes statement.
