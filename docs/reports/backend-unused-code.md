# Backend Unused-Code and Dependency Cleanup

Evidence report for issue #548 Cleanup 7. This updates the earlier read-only
inventory for issue #46 with the removals that passed repository-use checks.
Source, route, startup, and dependency-install contracts were kept in scope.

## Method and limits

Candidate symbol/module names and their import forms were searched across
`backend/`, `scripts/`, `fc_ingest/`, `canlaw/`, and `tests/`; route declarations,
dynamic module-loading patterns, `scripts/service/`, Dockerfiles/Compose, CI
workflows, and documented install instructions were reviewed. Package-name
checks used Python import spellings (for example, `langchain_community` for the
`langchain-community` distribution). AST/import and exact-name inspection were
used in addition to text searches.

These checks establish repository-local use only. They cannot rule out
undocumented external imports. No public route, database table, migration, or
`scripts/service/` startup import was changed.

## Removed backend code

| Removal | Evidence on the pre-cleanup tree | Decision |
| --- | --- | --- |
| `backend/routes.py::_normalize_whitespace` | `backend/routes.py` contained only its definition; there was no route/helper call or import of `routes._normalize_whitespace`. The similarly named helpers in `backend/reader_service.py` and `backend/citations.py` have in-module callers and remain. | Removed the unused route-local private helper only. |
| `backend/contextual_intelligence.py::ProximityCluster` | Exact-name/reference search found only the class declaration; no backend, script, ingestion, CanLaw, or test consumer was found. The containing service remains in use. | Removed the unreferenced class only. |
| `backend/unit_search.py` | Pre-cleanup imports were confined to `tests/test_unit_search_e2e.py` and `tests/test_unit_search_model.py`; no non-test import, route, script, service-startup, or dynamic-loader reference was found. The active `/unit-search` route uses `backend.unit_keyword_search`; that module and `tests/test_unit_keyword_search.py` remain. | Removed the deprecated module and its two directly coupled tests. |
| `backend/vector_tables.py` | Its only import consumer was `tests/test_vector_tables.py`; no runtime, route, script, service-startup, or dynamic-loader reference was found. The module only compiled a future registry scaffold and did not execute DDL. | Removed the unused scaffold and its directly coupled test. |

The pre-cleanup symbol scan was:

```text
git grep -nE 'unit_search|vector_tables|routes\._normalize_whitespace|ProximityCluster|merge_local_and_a2aj_graph' HEAD -- backend scripts fc_ingest canlaw tests
```

Among the broad `unit_search` text hits, the imports from the deleted module
were `tests/test_unit_search_e2e.py:20` and
`tests/test_unit_search_model.py:3`; their remaining hits refer to that imported
object. The live route is `backend/routes.py:960-967` and imports
`backend.unit_keyword_search` instead. The only `vector_tables` consumer was
`tests/test_vector_tables.py:5`. The only `ProximityCluster` hit was its
declaration at `backend/contextual_intelligence.py:97`; no
`routes._normalize_whitespace` or `merge_local_and_a2aj_graph` hit existed in
the cleanup base. Dynamic import/loading and `scripts/service/` searches found
no references to the deleted module names.

The issue candidate `backend/citations.py::merge_local_and_a2aj_graph` was
already absent from both the cleanup base and the resulting tree. It was not
removed by this change; the earlier inventory row was stale.

The removed test files were the direct unit tests for the deleted modules. No
live route test was removed. The live route's implementation remains in
`backend/unit_keyword_search.py`.

## Dependencies removed

For each distribution below, import-name searches found no use in the issue
scope (`backend/`, `scripts/`, `fc_ingest/`, `canlaw/`, or `tests/`), and no
Dockerfile/workflow installed it separately or documented an explicit
package-specific install purpose.

| Removed distribution | Import name checked |
| --- | --- |
| `anthropic` | `anthropic` |
| `langchain` | `langchain` |
| `langchain-community` | `langchain_community` |
| `pydantic-settings` | `pydantic_settings` |
| `aiohttp` | `aiohttp` |
| `python-jose` | `jose` |
| `passlib` | `passlib` |
| `pytest-asyncio` | `pytest_asyncio` |
| `isort` | `isort` |
| `flake8` | `flake8` |
| `mypy` | `mypy` |
| `pre-commit` | `pre_commit` |
| `loguru` | `loguru` |
| `rich` | `rich` |

The package import scan was:

```text
git grep -nE '^[[:space:]]*(from|import)[[:space:]]+(anthropic|langchain|langchain_community|pydantic_settings|aiohttp|jose|passlib|pytest_asyncio|isort|flake8|mypy|pre_commit|loguru|rich)(\.|[[:space:],]|$)' HEAD -- backend scripts fc_ingest canlaw tests
```

It returned no matching Python imports. Distribution-to-import spellings are
listed in the table above; the explicit Docker/workflow/install-purpose review
found no package-specific consumer for these removals.

The Dockerfile installs `requirements.txt`; CI installs `requirements-dev.txt`
for tests and quality checks and runs the dependency audit against the base
requirements. `pytest-cov`, `pytest-xdist`, `ruff`, and `pip-audit` remain in
`requirements-dev.txt` for those explicit workflows. `black` remains in
`requirements.txt` because it is documented as a formatting tool in `SETUP.md`.
The optional `spacy` package and model in `requirements-ml.txt` remain for the
lazy-loaded name-detection workflow. Other packages with active source or
workflow consumers (including `cloudscraper`, `datasets`, `pyarrow`,
`huggingface-hub`, `hf-xet`, and `tqdm`) were retained.

The Compose file and Docker deployment guide still contain legacy
`ANTHROPIC_API_KEY`/`ANTHROPIC_MODEL` settings. No Python Anthropic SDK import
or provider implementation consumes them; the settings were left untouched to
avoid changing the Compose environment contract. Their status is a separate
documentation/configuration follow-up, not evidence that the SDK is currently
used by the application.

## Candidates intentionally retained

| Candidate | Evidence | Decision |
| --- | --- | --- |
| `backend/case_compare.py` and `backend/case_comparison.py` | `backend/routes.py` imports input-resolution helpers from the former and `fetch_case_comparison` from the latter. `/cases/compare`, `/case-compare`, `/api/compare`, and `/compare` continue to use these paths; `tests/test_case_comparison.py` exercises both modules. The responsibilities differ. | Keep both. |
| `backend/legal_tagger.py` | Imported by `backend/metadata_subjects.py` and legacy tagging scripts; it also has tests. | Keep V1. |
| `backend/legal_tagger_v2.py` | Imported by `scripts/clean_llm_tag_report.py` and `scripts/tag_cases_v2.py`, with its own tests. | Keep V2. |
| `backend/legal_tagger_v3.py` | Used by the active `backend/case_processing.py` stage and services including reader/search/comparison, with tests and scripts. | Keep active V3; do not change tagging behavior. |
| `backend/pages/judge_outcomes.py` | Exported from `backend/pages/__init__.py`; its page JavaScript calls the judge-outcomes analytics endpoint, and `tests/test_inline_js_syntax.py` covers it. | Keep; the retired tab did not make this exported page safe to remove. |
| Similar whitespace, citation-variant, and sentence-boundary helpers | Each retained instance has local callers and, in some cases, different input/offset semantics. | Keep; do not deduplicate based on name or superficial similarity. |

`scripts/service/run_site.ps1` starts `uvicorn backend.main:app`. The deleted
module names were not referenced by the service startup scripts. The route
module, application startup, live search route, API paths, database schema, and
tagging behavior were not changed.

## Tool and validation limits

`ruff --select F401,F841` and vulture-style checks could not run because neither
tool is installed in this environment. No broad import cleanup was performed
without that evidence.

The base interpreter lacks `pytest`, SQLAlchemy, and FastAPI. In addition,
`tests/conftest.py` imports `backend.database` and probes PostgreSQL at module
collection. Pytest was therefore not run because the explicit task boundary
forbids database access. Focused/full pytest and generated-document validation
results are recorded in the issue task record.
