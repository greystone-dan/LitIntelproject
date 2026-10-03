# Pytest Coverage Baseline

Measured: 2026-10-03. This is Python statement coverage for `backend/`, not a
measure of legal accuracy, corpus completeness, or end-to-end workflow quality.
The denominator is 10,859 executable statements across 66 backend modules.

## Reproduction

CI installs test tooling with:

```bash
python -m pip install -r requirements-dev.txt
```

The coverage invocation uses the exact three test deselects in
`.github/workflows/tests.yml`:

```bash
python -m pytest -q \
  --deselect tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence \
  --deselect tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes \
  --deselect tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint \
  --cov=backend \
  --cov-report=term-missing:skip-covered
```

## Result And Limitations

The measured run covered 8,413 of 10,859 statements (77.5%); 2,446 statements
were missed. It completed with **987 passed, 3 failed, and 3 deselected**. The
failures are environment-dependent network fetches, not newly introduced test
failures:

- `tests/test_api.py::test_local_chunk_search_uses_requested_model` could not
  fetch the Hugging Face model because the runner could not resolve
  `huggingface.co`.
- `tests/test_openai_chunk_embeddings.py::test_count_embedding_tokens_uses_model_tokenizer`
  and
  `tests/test_openai_chunk_embeddings.py::test_count_embedding_tokens_treats_special_token_text_as_literal`
  could not fetch the `cl100k_base.tiktoken` encoding because the runner could
  not resolve `openaipublic.blob.core.windows.net`.

Coverage is still useful as a measured snapshot, but the suite is not green and
the values should not be treated as a release gate. The CI deselects are
intentional and remain visible in both the workflow and this command.

## Risk-Ranked Follow-Up

Risk priority is not a raw sort by uncovered lines. First protect pure logic whose
misclassification can change CBSA-visible counts or rates, in the required order
below; then prioritize remaining gaps by coverage, statement volume, and owner
impact. SQL/session-backed modules are included where they publish these numbers,
but should be tested separately from pure calculations. Very small page-import
wrappers can have low percentages without representing comparable behavioral risk.

| Rank | CBSA-visible risk | Module coverage | Risk rationale |
| ---: | --- | --- | --- |
| 1 | Outcomes | `backend/metadata_outcomes.py` 91.2% (15 / 171 missed); `backend/metadata.py` 95.7% (4 / 93) | Allowed/dismissed/mixed/undetermined derivation feeds winner/loser and outcome counts; preserve operative disposition evidence. |
| 2 | Citations | `backend/citations.py` 80.9% (283 / 1,481); `backend/citation_refine/context.py` 79.5% (23 / 112) | Extraction, target evidence, and context/short-form handling affect authority counts; keep extraction distinct from resolution. |
| 3 | Analytics | `backend/analytics_service.py` 25.5% (246 / 330); `backend/fc_activity_insights.py` 92.8% (22 / 307); `backend/citation_map.py` 10.0% (705 / 783) | Published aggregates and rates have high exposure. Separate deterministic aggregation/formula tests from SQL, graph-query, and route integration. |
| 4 | Minister handling | `backend/metadata_outcomes.py` 91.2% (15 / 171); `backend/metadata_subjects.py` 88.6% (10 / 88) | Applicant/respondent role and government win/loss derivation can reverse visible party-level numbers. |
| 5 | Judge handling | `backend/metadata.py` 95.7% (4 / 93); `backend/analytics_service.py` 25.5% (246 / 330); `backend/fc_activity_insights.py` 92.8% (22 / 307) | Judge extraction/identity feeds profile and outcome aggregates; cover deterministic identity/aggregation rules separately from database queries. |

The remaining follow-up gaps, ordered by coverage and owner exposure:

| Rank | Module | Coverage | Missed / statements | Risk rationale |
| ---: | --- | ---: | ---: | --- |
| 6 | `backend/citation_pipeline/canlii.py` | 37.7% | 43 / 69 | External authority-source client, quotas, and response failures need isolated mock coverage. |
| 7 | `backend/memo_citation_check.py` | 54.1% | 28 / 61 | Citation treatment and missing-authority workflow; current untested paths are session-backed. |
| 8 | `backend/ingestion.py` | 56.5% | 77 / 177 | Canonical merge and source-provenance policy; requires careful fake-session/integration tests. |
| 9 | `backend/reader_service.py` | 58.8% | 160 / 388 | Reader evidence assembly affects source traceability and has substantial untested branches. |
| 10 | `backend/main.py` | 58.1% | 31 / 74 | Startup, middleware, and route registration have moderate coverage and broad operational impact. |
| 11 | `backend/case_processing.py` | 68.2% | 28 / 88 | Ordered metadata/chunk/citation/statute processing stages need additional isolated coverage. |
| 12 | `backend/routes.py` | 70.9% | 321 / 1,102 | Large API/UI owner; many response and fallback branches remain uncovered. |
| 13 | `backend/contextual_intelligence.py` | 73.2% | 38 / 142 | Contextual authority signals should retain transparent, deterministic fallbacks. |
| 14 | `backend/search_service.py` | 78.2% | 88 / 403 | Retrieval and result-ranking branches merit query-contract tests. |
| 15 | `backend/text_generation_providers.py` | 79.2% | 11 / 53 | Provider configuration/failure handling; external-provider behavior needs mocks. |

The remaining pure-logic test targets were selected using the pre-change
coverage run: `backend/fc_activity.py` (81.6%, 23 missed of 125) and
`backend/metadata_subjects.py` (85.2%, 13 missed of 88). Focused tests raised
their measured coverage to 91.2% and 88.6%, respectively; the focused context
tests raised `backend/citation_refine/context.py` from 77.7% to 79.5%. These
three modules have deterministic transformations/classification and do not
require a database. Their tests live in
`tests/test_citation_refine_context.py`,
`tests/test_fc_activity_pure_logic.py`, and
`tests/test_metadata_subjects.py`.

## Complete Backend Module Coverage

Percentages below are from the measured run after adding the focused tests.
Rows are sorted by coverage to make low-coverage modules visible; interpret
them with the risk criteria above rather than as a severity ranking by
percentage alone.

| Module | Coverage | Missed / statements |
| --- | ---: | ---: |
| `backend/pages/discussion_units_sandbox.py` | 0.0% | 2 / 2 |
| `backend/citation_map.py` | 10.0% | 705 / 783 |
| `backend/analytics_service.py` | 25.5% | 246 / 330 |
| `backend/citation_pipeline/canlii.py` | 37.7% | 43 / 69 |
| `backend/pages/citation_pass.py` | 50.0% | 1 / 2 |
| `backend/pages/judge_outcomes.py` | 50.0% | 1 / 2 |
| `backend/pages/prototype.py` | 50.0% | 1 / 2 |
| `backend/pages/quick_search.py` | 50.0% | 1 / 2 |
| `backend/pages/research.py` | 50.0% | 1 / 2 |
| `backend/memo_citation_check.py` | 54.1% | 28 / 61 |
| `backend/ingestion.py` | 56.5% | 77 / 177 |
| `backend/main.py` | 58.1% | 31 / 74 |
| `backend/reader_service.py` | 58.8% | 160 / 388 |
| `backend/pages/citation_map.py` | 66.7% | 1 / 3 |
| `backend/pages/memo_citation_check.py` | 66.7% | 1 / 3 |
| `backend/case_processing.py` | 68.2% | 28 / 88 |
| `backend/routes.py` | 70.9% | 321 / 1,102 |
| `backend/contextual_intelligence.py` | 73.2% | 38 / 142 |
| `backend/search_service.py` | 78.2% | 88 / 403 |
| `backend/text_generation_providers.py` | 79.2% | 11 / 53 |
| `backend/citation_refine/context.py` | 79.5% | 23 / 112 |
| `backend/citations.py` | 80.9% | 283 / 1,481 |
| `backend/live_analysis.py` | 84.1% | 27 / 170 |
| `backend/citation_refine/resolution.py` | 85.8% | 34 / 239 |
| `backend/citation_refine/__init__.py` | 86.0% | 8 / 57 |
| `backend/metadata_subjects.py` | 88.6% | 10 / 88 |
| `backend/contextual_authority/teacher_contract.py` | 88.7% | 8 / 71 |
| `backend/discussion_units_sandbox.py` | 88.8% | 14 / 125 |
| `backend/citation_pipeline/pipeline.py` | 89.5% | 4 / 38 |
| `backend/document_structure.py` | 89.8% | 21 / 205 |
| `backend/citation_refine/pinpoints.py` | 90.9% | 8 / 88 |
| `backend/embedding_providers.py` | 90.9% | 3 / 33 |
| `backend/fc_activity.py` | 91.2% | 11 / 125 |
| `backend/metadata_outcomes.py` | 91.2% | 15 / 171 |
| `backend/citation_refine/cases.py` | 91.3% | 42 / 483 |
| `backend/statutes.py` | 92.1% | 5 / 63 |
| `backend/contextual_authority/subthemes.py` | 92.5% | 15 / 199 |
| `backend/deidentify.py` | 92.5% | 21 / 281 |
| `backend/contextual_authority/discussion_units.py` | 92.6% | 12 / 162 |
| `backend/fc_activity_insights.py` | 92.8% | 22 / 307 |
| `backend/case_formatter.py` | 92.9% | 11 / 154 |
| `backend/citation_refine/models.py` | 93.3% | 6 / 90 |
| `backend/contextual_authority/voting.py` | 93.4% | 5 / 76 |
| `backend/citation_refine/laws.py` | 93.5% | 19 / 291 |
| `backend/citation_pipeline/models.py` | 94.1% | 1 / 17 |
| `backend/legal_tagger_v2.py` | 94.2% | 3 / 52 |
| `backend/contextual_authority/context_units.py` | 95.6% | 3 / 68 |
| `backend/metadata.py` | 95.7% | 4 / 93 |
| `backend/legal_tagger_v3.py` | 95.7% | 3 / 70 |
| `backend/contextual_authority/models.py` | 96.6% | 2 / 58 |
| `backend/deidentify_names.py` | 96.6% | 7 / 206 |
| `backend/legal_tagger.py` | 96.8% | 3 / 93 |
| `backend/contextual_authority/observations.py` | 97.9% | 1 / 48 |
| `backend/citation_refine/instruments.py` | 98.4% | 1 / 64 |
| `backend/database.py` | 99.1% | 4 / 458 |
| `backend/models.py` | 99.7% | 2 / 671 |
| `backend/citation_pipeline/__init__.py` | 100.0% | 0 / 4 |
| `backend/citation_pipeline/rules.py` | 100.0% | 0 / 88 |
| `backend/contextual_authority/__init__.py` | 100.0% | 0 / 8 |
| `backend/intelligence.py` | 100.0% | 0 / 10 |
| `backend/pages/__init__.py` | 100.0% | 0 / 11 |
| `backend/pages/data_explorer.py` | 100.0% | 0 / 21 |
| `backend/pages/deidentify.py` | 100.0% | 0 / 3 |
| `backend/pages/fc_analytics.py` | 100.0% | 0 / 13 |
| `backend/pages/live_analysis.py` | 100.0% | 0 / 3 |
| `backend/pages/testing.py` | 100.0% | 0 / 3 |

Coverage gaps should be addressed by targeted tests against documented
ownership boundaries. Do not increase a percentage by coupling pure logic to
the database or changing runtime behavior solely to make it easier to measure.
