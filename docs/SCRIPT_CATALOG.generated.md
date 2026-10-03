# Generated Script Catalog

This file is generated from active `scripts/*.py` modules by `scripts/generate_script_catalog.py`. Do not edit it manually.

Run every script from the repository root with the project virtual environment. For database/network writers, read `--help`, use dry-run/preflight/limit options where available, and confirm no other bulk PostgreSQL writer is active.

Active scripts documented: 142

## Catalog

| Script | Class | Risk | Safe first command |
| --- | --- | --- | --- |
| `_tmp_crosscourt_audit.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\_tmp_crosscourt_audit.py --help` |
| `acquire_case_html.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\acquire_case_html.py --list-jobs` |
| `adjudicate_fc_metadata.py` | Metadata adjudication | OpenAI and database writer | `.\venv\Scripts\python.exe scripts\adjudicate_fc_metadata.py --help` |
| `agent_harness.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\agent_harness.py --help` |
| `agent_policy.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\agent_policy.py --help` |
| `aggregate_recorded_costs.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\aggregate_recorded_costs.py --list-jobs` |
| `ai_triage_citation_candidate.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\ai_triage_citation_candidate.py --help` |
| `audit_discussion_unit_structure.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_discussion_unit_structure.py --help` |
| `audit_fc_activity_motion_unknowns_openai.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_fc_activity_motion_unknowns_openai.py --help` |
| `audit_fc_activity_openai.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_fc_activity_openai.py --help` |
| `audit_fc_metadata_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_fc_metadata_extraction.py --help` |
| `audit_self_citations.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_self_citations.py --help` |
| `backfill_case_metadata_outcomes.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_case_metadata_outcomes.py --help` |
| `backfill_case_outcomes.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_case_outcomes.py --help` |
| `backfill_fc_case_metadata.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_fc_case_metadata.py --help` |
| `backfill_judge_profiles.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_judge_profiles.py --help` |
| `benchmark_case_citations.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\benchmark_case_citations.py --help` |
| `benchmark_citation_resolution.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\benchmark_citation_resolution.py --help` |
| `browser_smoke.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\browser_smoke.py --help` |
| `build_citation_sample_candidate.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_citation_sample_candidate.py --help` |
| `build_core_immigration_set.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_core_immigration_set.py --help` |
| `build_discussion_unit_priority_lists.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_discussion_unit_priority_lists.py --help` |
| `build_fc_activity_audit_report.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_activity_audit_report.py --help` |
| `build_fc_activity_gold_template.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_activity_gold_template.py --help` |
| `build_fc_batch_from_party.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_batch_from_party.py --help` |
| `build_fc_citation_gold_template.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_citation_gold_template.py --help` |
| `build_fc_citation_seed.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_citation_seed.py --help` |
| `build_fc_metadata_gold_set.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_metadata_gold_set.py --help` |
| `build_five_case_citation_gold_candidate.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_five_case_citation_gold_candidate.py --help` |
| `build_mason_argument_citation_fixture.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_mason_argument_citation_fixture.py --help` |
| `build_mason_case_intelligence_request.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_mason_case_intelligence_request.py --help` |
| `build_mason_citation_review_ledger.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_mason_citation_review_ledger.py --help` |
| `build_prototype_cohort.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_prototype_cohort.py --help` |
| `build_statute_demand_report.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_statute_demand_report.py --help` |
| `build_tagging_v2_core_candidates.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_tagging_v2_core_candidates.py --help` |
| `build_treatment_distillation.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_treatment_distillation.py --help` |
| `build_treatment_review_packet.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_treatment_review_packet.py --help` |
| `build_treatment_teacher_fixture.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_treatment_teacher_fixture.py --help` |
| `check_generated_docs.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\check_generated_docs.py --help` |
| `chunk_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\chunk_cases.py --help` |
| `classify_fc_activity.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\classify_fc_activity.py --help` |
| `clean_llm_tag_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\clean_llm_tag_report.py --help` |
| `clean_tag_candidate_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\clean_tag_candidate_report.py --help` |
| `compare_pipeline_case.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\compare_pipeline_case.py --help` |
| `crawl_canlii.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\crawl_canlii.py --help` |
| `cross_reference_seed_cases.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\cross_reference_seed_cases.py --help` |
| `curate_a2aj_cases.py` | A2AJ curation and canonical import | database writer | `.\venv\Scripts\python.exe scripts\curate_a2aj_cases.py --help` |
| `curate_a2aj_immigration_cases.py` | A2AJ curation and canonical import | database writer | `.\venv\Scripts\python.exe scripts\curate_a2aj_immigration_cases.py --help` |
| `deduplicate_a2aj.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\deduplicate_a2aj.py --help` |
| `discover_recent_case_themes.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\discover_recent_case_themes.py --help` |
| `discussion_units_ledger.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\discussion_units_ledger.py --help` |
| `download_reference_library.py` | Reference acquisition | network and filesystem writer | `.\venv\Scripts\python.exe scripts\download_reference_library.py --help` |
| `dry_run_paragraph_evidence_bridge.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\dry_run_paragraph_evidence_bridge.py --help` |
| `embed_a2aj_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_a2aj_cases.py --help` |
| `embed_documentation_appendices.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_documentation_appendices.py --help` |
| `embed_local_chunks.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_local_chunks.py --help` |
| `embed_openai_chunks.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_openai_chunks.py --help` |
| `evaluate_chunk_parity.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_chunk_parity.py --help` |
| `evaluate_citation_refinement.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_citation_refinement.py --help` |
| `evaluate_data_quality.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_data_quality.py --help` |
| `evaluate_fc_activity_deterministic.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_fc_activity_deterministic.py --help` |
| `evaluate_fc_citation_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_fc_citation_extraction.py --help` |
| `evaluate_retrieval.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_retrieval.py --help` |
| `evaluate_retrieval_benchmark.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_retrieval_benchmark.py --help` |
| `evaluate_statute_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_statute_extraction.py --help` |
| `evidence_gate.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\evidence_gate.py --help` |
| `export_fc_activity_package.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\export_fc_activity_package.py --help` |
| `export_tagging_v3_canary_review.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\export_tagging_v3_canary_review.py --help` |
| `extract_a2aj_case_citations_resumable.py` | Citation extraction maintenance | database writer | `.\venv\Scripts\python.exe scripts\extract_a2aj_case_citations_resumable.py --help` |
| `extract_citation_network.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\extract_citation_network.py --help` |
| `extract_fc_citation_evidence.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\extract_fc_citation_evidence.py --help` |
| `extract_irpa_irpr_references.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\extract_irpa_irpr_references.py --help` |
| `extract_seed_cases_from_transcript.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\extract_seed_cases_from_transcript.py --help` |
| `fc_activity_extractors.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\fc_activity_extractors.py --help` |
| `fc_portal_collector.py` | Federal Court source acquisition | network and filesystem writer | `.\venv\Scripts\python.exe scripts\fc_portal_collector.py --help` |
| `fetch_fc_procedural_history.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\fetch_fc_procedural_history.py --help` |
| `generate_api_reference.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_api_reference.py` |
| `generate_schema_reference.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_schema_reference.py` |
| `generate_script_catalog.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_script_catalog.py` |
| `generate_work_history.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_work_history.py` |
| `import_a2aj_decisions.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_a2aj_decisions.py --help` |
| `import_canlaw_staging.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_canlaw_staging.py --help` |
| `import_fc_decisions.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_fc_decisions.py --help` |
| `import_historical_statutes.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_historical_statutes.py --help` |
| `import_seed_cases_from_a2aj_api.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_seed_cases_from_a2aj_api.py --help` |
| `import_statutes.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_statutes.py --help` |
| `index_legislation.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\index_legislation.py --help` |
| `ingest_a2aj_api.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_a2aj_api.py --help` |
| `ingest_a2aj_citation_network.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_a2aj_citation_network.py --help` |
| `ingest_a2aj_parquet.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_a2aj_parquet.py --help` |
| `ingest_canlii_seed_cases.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_canlii_seed_cases.py --help` |
| `ingest_hf_fc_activity.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_hf_fc_activity.py --help` |
| `ingest_synthetic_cases.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_synthetic_cases.py --help` |
| `inspect_context_variants.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\inspect_context_variants.py --help` |
| `inspect_discussion_units.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\inspect_discussion_units.py --help` |
| `judge_reconciliation_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\judge_reconciliation_report.py --help` |
| `link_citation_pinpoints.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\link_citation_pinpoints.py --help` |
| `llm_tag_candidate_review.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\llm_tag_candidate_review.py --help` |
| `map_fc_seed_to_local_cases.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\map_fc_seed_to_local_cases.py --help` |
| `monitor_vector_index.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\monitor_vector_index.py --help` |
| `normalize_fc_activity_openai_outputs.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\normalize_fc_activity_openai_outputs.py --help` |
| `package_discussion_units_llm.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\package_discussion_units_llm.py --help` |
| `plan_self_citation_cleanup.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\plan_self_citation_cleanup.py --help` |
| `populate_fc_gold_case_ids.py` | Evaluation artifact maintenance | filesystem writer | `.\venv\Scripts\python.exe scripts\populate_fc_gold_case_ids.py --help` |
| `prepare_discussion_units_cohort.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\prepare_discussion_units_cohort.py --help` |
| `prepare_treatment_teacher_batch.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\prepare_treatment_teacher_batch.py --help` |
| `quick_search_engine.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\quick_search_engine.py --help` |
| `reacquire_source_html.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\reacquire_source_html.py --help` |
| `rebuild_citations_controlled.py` | Citation-only rebuild | database writer; dry-run is default and --apply requires explicit confirmation | `.\venv\Scripts\python.exe scripts\rebuild_citations_controlled.py --help` |
| `refresh_recent_5000_artifact.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\refresh_recent_5000_artifact.py --help` |
| `remove_self_case_citations.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\remove_self_case_citations.py --help` |
| `remove_self_citations.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\remove_self_citations.py --help` |
| `report_a2aj_immigration_selection.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\report_a2aj_immigration_selection.py --help` |
| `report_fc_activity_coverage.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\report_fc_activity_coverage.py --help` |
| `report_fc_activity_motion_unknowns.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\report_fc_activity_motion_unknowns.py --help` |
| `report_incomplete_short_form_anchors.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\report_incomplete_short_form_anchors.py --help` |
| `report_unresolved_citation_shapes.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\report_unresolved_citation_shapes.py --help` |
| `resolve_citation_targets.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\resolve_citation_targets.py --help` |
| `resolve_short_citation_targets.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\resolve_short_citation_targets.py --help` |
| `review_fc_activity_local.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\review_fc_activity_local.py --help` |
| `review_tag_candidates.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\review_tag_candidates.py --help` |
| `run_case_intelligence_request.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_case_intelligence_request.py --help` |
| `run_citation_rebuild_progress.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\run_citation_rebuild_progress.py --list-jobs` |
| `run_discussion_units_cohort.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_discussion_units_cohort.py --help` |
| `run_fc_activity_openai_structured_pilot.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_fc_activity_openai_structured_pilot.py --help` |
| `run_local_paragraph_summary_baseline.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_local_paragraph_summary_baseline.py --help` |
| `run_model_paragraph_experiment.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_model_paragraph_experiment.py --help` |
| `run_overnight.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\run_overnight.py --list-jobs` |
| `run_paragraph_assessment_batches.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_paragraph_assessment_batches.py --help` |
| `run_scc_text_only.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\run_scc_text_only.py --list-jobs` |
| `run_treatment_teacher_batch.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_treatment_teacher_batch.py --help` |
| `run_v2_pipeline.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\run_v2_pipeline.py --list-jobs` |
| `run_v2_pipeline_case.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_v2_pipeline_case.py --help` |
| `run_v2_text_only_fast.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_v2_text_only_fast.py --help` |
| `select_discussion_unit_cohort.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\select_discussion_unit_cohort.py --help` |
| `snapshot_v2_pipeline_baseline.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\snapshot_v2_pipeline_baseline.py --help` |
| `tag_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_cases.py --help` |
| `tag_cases_v2.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_cases_v2.py --help` |
| `tag_cases_v3.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_cases_v3.py --help` |
| `tag_prototype_topics.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_prototype_topics.py --help` |
| `verify_citation_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\verify_citation_extraction.py --help` |
| `verify_fc_case_existence.py` | Source verification | network and filesystem output | `.\venv\Scripts\python.exe scripts\verify_fc_case_existence.py --help` |

## `scripts/_tmp_crosscourt_audit.py`

**Purpose:** THROWAWAY cross-court metadata-extraction audit (read-only). Patterns on scripts/audit_fc_metadata_extraction.py but audits a court selected via --court (FCA | SCC | both). Reuses fc_ingest.document_scraper._extract_metadata_with_quality and backend.database. Purpose: measure whether the recent FC metadata-extraction fixes generalize to FCA and SCC without court-specific handling. Usage: & ".\venv\Scripts\python.exe" scripts\_tmp_crosscourt_audit.py --court both

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\_tmp_crosscourt_audit.py --help
```

## `scripts/acquire_case_html.py`

**Purpose:** Bounded, resumable source-HTML acquisition for canonical cases.

**Operational class:** Orchestration

**Write/network risk:** database/network job runner

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\acquire_case_html.py --list-jobs
```

## `scripts/adjudicate_fc_metadata.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Metadata adjudication

**Write/network risk:** OpenAI and database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\adjudicate_fc_metadata.py --help
```

## `scripts/agent_harness.py`

**Purpose:** Small repo-local control plane for managed agent task runs.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\agent_harness.py --help
```

## `scripts/agent_policy.py`

**Purpose:** Fail-closed policy checks for managed-task command requests.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\agent_policy.py --help
```

## `scripts/aggregate_recorded_costs.py`

**Purpose:** Aggregate report-level estimated costs from evaluation artifacts.

**Operational class:** Orchestration

**Write/network risk:** database/network job runner

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\aggregate_recorded_costs.py --list-jobs
```

## `scripts/ai_triage_citation_candidate.py`

**Purpose:** Bounded AI triage for proposed case-citation review candidates. This script produces suggestions only. It never modifies the candidate fixture, database rows, or confirmed gold data. Use --dry-run first.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\ai_triage_citation_candidate.py --help
```

## `scripts/audit_discussion_unit_structure.py`

**Purpose:** Audit retained Discussion Unit reports for review-only structural risks.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\audit_discussion_unit_structure.py --help
```

## `scripts/audit_fc_activity_motion_unknowns_openai.py`

**Purpose:** Send all unknown FC Activity motions for bounded OpenAI subtype suggestions.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\audit_fc_activity_motion_unknowns_openai.py --help
```

## `scripts/audit_fc_activity_openai.py`

**Purpose:** Audit deterministic FC Activity events with a bounded OpenAI sample.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\audit_fc_activity_openai.py --help
```

## `scripts/audit_fc_metadata_extraction.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\audit_fc_metadata_extraction.py --help
```

## `scripts/audit_self_citations.py`

**Purpose:** Bounded, read-only audit of existing citation self-links.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\audit_self_citations.py --help
```

## `scripts/backfill_case_metadata_outcomes.py`

**Purpose:** Apply the current metadata and outcome extractor to every case with full text.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_case_metadata_outcomes.py --help
```

## `scripts/backfill_case_outcomes.py`

**Purpose:** Backfill the dedicated deterministic outcome table in bounded batches.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_case_outcomes.py --help
```

## `scripts/backfill_fc_case_metadata.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_fc_case_metadata.py --help
```

## `scripts/backfill_judge_profiles.py`

**Purpose:** Create canonical judge profiles from existing extracted case metadata.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_judge_profiles.py --help
```

## `scripts/benchmark_case_citations.py`

**Purpose:** Bounded, read-only baseline for case-to-case citation extraction.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\benchmark_case_citations.py --help
```

## `scripts/benchmark_citation_resolution.py`

**Purpose:** Bounded, read-only benchmark for citation occurrence resolution.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\benchmark_citation_resolution.py --help
```

## `scripts/browser_smoke.py`

**Purpose:** Bounded browser smoke checks for the active Data Explorer workflow.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\browser_smoke.py --help
```

## `scripts/build_citation_sample_candidate.py`

**Purpose:** Build a deterministic, read-only citation extraction candidate report.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_citation_sample_candidate.py --help
```

## `scripts/build_core_immigration_set.py`

**Purpose:** Build a deterministic ~300-case immigration prototype set from A2AJ data. This script reads the local A2AJ Federal Court parquet source, applies transparent ranking rules, maps selected citations to local case IDs, and exports a CSV for prototype testing and embedding workflows.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_core_immigration_set.py --help
```

## `scripts/build_discussion_unit_priority_lists.py`

**Purpose:** Build the bounded Discussion Unit priority lists without database writes.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_discussion_unit_priority_lists.py --help
```

## `scripts/build_fc_activity_audit_report.py`

**Purpose:** Build a readable, source-backed audit report from an FC Activity package.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_fc_activity_audit_report.py --help
```

## `scripts/build_fc_activity_gold_template.py`

**Purpose:** Build a stratified manual-adjudication template from an FC classification report.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_fc_activity_gold_template.py --help
```

## `scripts/build_fc_batch_from_party.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_fc_batch_from_party.py --help
```

## `scripts/build_fc_citation_gold_template.py`

**Purpose:** Generate a gold-annotation template from normalized FC seed links. This is a fixture-construction helper for citation QA. It does not perform extraction.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_fc_citation_gold_template.py --help
```

## `scripts/build_fc_citation_seed.py`

**Purpose:** Build a normalized Federal Court seed list for citation-system rebuild. This script is intentionally extraction-only infrastructure. It normalizes a user-provided case list into canonical FC item URLs and produces deterministic artifacts: - accepted seeds - rejects with reason codes - summary stats Supported input formats: - .txt / .md: plain text with links - .csv: scans common URL columns and any cell text - .docx: extracts hyperlink targets and plain-text links

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_fc_citation_seed.py --help
```

## `scripts/build_fc_metadata_gold_set.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_fc_metadata_gold_set.py --help
```

## `scripts/build_five_case_citation_gold_candidate.py`

**Purpose:** Build a deterministic, proposed five-case citation review fixture.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_five_case_citation_gold_candidate.py --help
```

## `scripts/build_mason_argument_citation_fixture.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_mason_argument_citation_fixture.py --help
```

## `scripts/build_mason_case_intelligence_request.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_mason_case_intelligence_request.py --help
```

## `scripts/build_mason_citation_review_ledger.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_mason_citation_review_ledger.py --help
```

## `scripts/build_prototype_cohort.py`

**Purpose:** Build and operationalize prototype cohort for immigration case research. Pipeline: 1) Combine the 300-case core list with exact-matched seed/canon cases. 2) Embed cohort cases that are not yet embedded. 3) Export citation map edges restricted to cohort-internal citations.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_prototype_cohort.py --help
```

## `scripts/build_statute_demand_report.py`

**Purpose:** Build a read-only statute and legal-instrument demand catalogue.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_statute_demand_report.py --help
```

## `scripts/build_tagging_v2_core_candidates.py`

**Purpose:** Build a conservative Tagging V2 core candidate file from the brainstorming draft.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_tagging_v2_core_candidates.py --help
```

## `scripts/build_treatment_distillation.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_treatment_distillation.py --help
```

## `scripts/build_treatment_review_packet.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_treatment_review_packet.py --help
```

## `scripts/build_treatment_teacher_fixture.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_treatment_teacher_fixture.py --help
```

## `scripts/check_generated_docs.py`

**Purpose:** Check that checked-in generated documentation matches its generators.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\check_generated_docs.py --help
```

## `scripts/chunk_cases.py`

**Purpose:** Create resumable text chunks for canonical cases without embedding calls.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\chunk_cases.py --help
```

## `scripts/classify_fc_activity.py`

**Purpose:** Deterministically classify Federal Court activity milestones without writing to the database.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\classify_fc_activity.py --help
```

## `scripts/clean_llm_tag_report.py`

**Purpose:** Create a conservative review shortlist from an LLM tag report.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\clean_llm_tag_report.py --help
```

## `scripts/clean_tag_candidate_report.py`

**Purpose:** Create a conservative, review-ready list from a tag candidate report.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\clean_tag_candidate_report.py --help
```

## `scripts/compare_pipeline_case.py`

**Purpose:** Snapshot and compare one case across V2 Pipeline derived layers.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\compare_pipeline_case.py --help
```

## `scripts/crawl_canlii.py`

**Purpose:** Slowly crawl CanLII case pages for a configurable set of citations. Seed sources (choose one or both): --from-prototype Pull cases_cited from the local prototype cohort in the DB, ranked by citation frequency and filtered to exclude cases already present in the DB. --citations-file FILE CSV or JSONL file with a 'citation' column. Citation following: --depth 1 Hops of citation expansion beyond seeds (0 = seeds only). Expanded citations are also ranked by how often they appear. Rate / scale limits: --limit 50 Max total cases to attempt (across seeds + expanded). --delay-ms 5000 Base milliseconds to wait between HTTP requests. --jitter 0.3 Fractional random jitter applied to each delay (±30% default). --rest-every 10 After every N fetches, pause for --rest-seconds. --rest-seconds 45 Duration of the periodic rest pause. Persistence: --checkpoint FILE JSON file tracking already-fetched/failed citations (for resume). --output FILE JSONL output; records are appended so partial runs are safe. Dry run: --dry-run Resolve URLs and print plan without fetching anything.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\crawl_canlii.py --help
```

## `scripts/cross_reference_seed_cases.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\cross_reference_seed_cases.py --help
```

## `scripts/curate_a2aj_cases.py`

**Purpose:** Select and import 25 transparent A2AJ refugee-risk evaluation cases.

**Operational class:** A2AJ curation and canonical import

**Write/network risk:** database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\curate_a2aj_cases.py --help
```

## `scripts/curate_a2aj_immigration_cases.py`

**Purpose:** Select and import a core A2AJ immigration dataset. This script builds a balanced immigration-focused seed set from the full A2AJ Federal Court parquet source. It prioritizes cases with immigration-party signals, immigration issue keywords, and case patterns commonly seen in Federal Court immigration review work.

**Operational class:** A2AJ curation and canonical import

**Write/network risk:** database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\curate_a2aj_immigration_cases.py --help
```

## `scripts/deduplicate_a2aj.py`

**Purpose:** Deduplication logic for A2AJ decisions against existing iLit corpus. Matches A2AJ decisions to existing decisions using: 1. Neutral citation (normalized) + decision date 2. Case name + date (fallback) This prevents duplicate storage and enables citation linking. Note: This is a dry-run proof-of-concept showing dedup logic. Actual implementation requires database access and citation normalization rules.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\deduplicate_a2aj.py --help
```

## `scripts/discover_recent_case_themes.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\discover_recent_case_themes.py --help
```

## `scripts/discussion_units_ledger.py`

**Purpose:** Atomic, report-only ledger for resumable Discussion Unit runs.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\discussion_units_ledger.py --help
```

## `scripts/download_reference_library.py`

**Purpose:** Download a provenance-preserving reference corpus kept separate from cases.

**Operational class:** Reference acquisition

**Write/network risk:** network and filesystem writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\download_reference_library.py --help
```

## `scripts/dry_run_paragraph_evidence_bridge.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\dry_run_paragraph_evidence_bridge.py --help
```

## `scripts/embed_a2aj_cases.py`

**Purpose:** Chunk and embed raw A2AJ cases. This is the first paid API operation.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\embed_a2aj_cases.py --help
```

## `scripts/embed_documentation_appendices.py`

**Purpose:** Embed linked documentation appendices into the canonical system reference.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\embed_documentation_appendices.py --help
```

## `scripts/embed_local_chunks.py`

**Purpose:** Generate resumable local BGE-M3 embeddings for existing case chunks.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\embed_local_chunks.py --help
```

## `scripts/embed_openai_chunks.py`

**Purpose:** Generate resumable OpenAI embeddings for existing case chunks with a hard budget cap.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\embed_openai_chunks.py --help
```

## `scripts/evaluate_chunk_parity.py`

**Purpose:** Compare HTML-enabled and text-only chunking on a bounded sample.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_chunk_parity.py --help
```

## `scripts/evaluate_citation_refinement.py`

**Purpose:** Shadow-mode comparison of pass-one citation extraction and the step-2 refinement layers. Never writes to the database. Two input modes: --text-file PATH a decision as .txt or .html (no database needed) --case-id N / --limit N decisions from the database (read-only) With --resolve (database mode) it also links rows to cases, paragraphs and statute provisions, and reports how many more reach each level than pass one. Outputs go to --output-dir (default data/eval/reports/citation_refinement): rows.csv every refined/dropped row with its step, action and notes summary.json counts by step/action and, with --resolve, linking statuses

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_citation_refinement.py --help
```

## `scripts/evaluate_data_quality.py`

**Purpose:** Automated data quality and corpus integrity evaluation script. Audits canonical cases, chunk distributions, citation resolution, statute references, metadata completeness, and graph consistency. Emits structured JSON reports and console markdown summaries.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_data_quality.py --help
```

## `scripts/evaluate_fc_activity_deterministic.py`

**Purpose:** Build a seeded, read-only evaluation report for FC Activity extraction.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_fc_activity_deterministic.py --help
```

## `scripts/evaluate_fc_citation_extraction.py`

**Purpose:** Evaluate citation extraction output against gold annotations. The gold file can be partially complete. Only rows with sufficient annotation fields are scored.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_fc_citation_extraction.py --help
```

## `scripts/evaluate_retrieval.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_retrieval.py --help
```

## `scripts/evaluate_retrieval_benchmark.py`

**Purpose:** Evaluate the Data Explorer case-search ranking against a fixed benchmark.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_retrieval_benchmark.py --help
```

## `scripts/evaluate_statute_extraction.py`

**Purpose:** Evaluate deterministic statute extraction against exact-span fixtures.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_statute_extraction.py --help
```

## `scripts/evidence_gate.py`

**Purpose:** Validate manager-owned completion evidence for a task run.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evidence_gate.py --help
```

## `scripts/export_fc_activity_package.py`

**Purpose:** Export reproducible Federal Court Activity source and derived cohorts.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\export_fc_activity_package.py --help
```

## `scripts/export_tagging_v3_canary_review.py`

**Purpose:** Export the current bounded V3 canary rows as a human-review snapshot.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\export_tagging_v3_canary_review.py --help
```

## `scripts/extract_a2aj_case_citations_resumable.py`

**Purpose:** Extract case-to-case citations for RPD/SCC A2AJ cases with per-case timeouts.

**Operational class:** Citation extraction maintenance

**Write/network risk:** database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\extract_a2aj_case_citations_resumable.py --help
```

## `scripts/extract_citation_network.py`

**Purpose:** Backfill the citation network from case texts and/or stored chunks.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\extract_citation_network.py --help
```

## `scripts/extract_fc_citation_evidence.py`

**Purpose:** Extract citation evidence rows for FC-focused evaluation. This script is read-only against the main case DB. It does not write citation rows. Use it to produce transparent extraction evidence before pipeline integration changes.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\extract_fc_citation_evidence.py --help
```

## `scripts/extract_irpa_irpr_references.py`

**Purpose:** Extract recognized statute and legal-instrument references into the statute-reference layer.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\extract_irpa_irpr_references.py --help
```

## `scripts/extract_seed_cases_from_transcript.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\extract_seed_cases_from_transcript.py --help
```

## `scripts/fc_activity_extractors.py`

**Purpose:** Additional evidence-backed fields extracted from Federal Court docket entries. Each extractor reads the docket entries of one IMM file (``ActivityEvent`` objects from ``scripts.classify_fc_activity``) and returns a JSON-ready dict. Every value carries the entry it came from so a reviewer can check it, and a field is left ``unknown`` rather than guessed when the registry text does not say.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\fc_activity_extractors.py --help
```

## `scripts/fc_portal_collector.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Federal Court source acquisition

**Write/network risk:** network and filesystem writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\fc_portal_collector.py --help
```

## `scripts/fetch_fc_procedural_history.py`

**Purpose:** Fetch Federal Court procedural history for a list of IMM numbers. Hits two FC API endpoints per IMM number: - proceedingQueriesCourtNumberList → style of cause - proceedingQueriesRE → all DOC_DT / RECORDED_ENTRY events Parses leave decision, JR decision, case status, judge, and full activity text using the same priority-based logic as the VBA original. Results are upserted into the fc_procedural_history table, tagged by IMM number. Input sources (choose one or more): --imm-numbers IMM-1234-19 IMM-5678-20 (space-separated on command line) --imm-file FILE CSV/text file, one IMM per line or 'imm_number' column --from-prototype Pull IMM numbers from prototype cohort (source_id field) Options: --update Re-fetch and overwrite entries that already exist --delay-ms Milliseconds between requests (default 2000) --diagnostic-allow-sub-2000ms-delay Explicitly allow a faster diagnostic probe; never use for routine collection --dry-run Parse and print without writing to DB

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\fetch_fc_procedural_history.py --help
```

## `scripts/generate_api_reference.py`

**Purpose:** Generate the checked-in API appendix from the FastAPI OpenAPI schema.

**Operational class:** Documentation generation

**Write/network risk:** read-only

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\generate_api_reference.py
```

## `scripts/generate_schema_reference.py`

**Purpose:** Generate the checked-in schema reference and ERD from SQLAlchemy metadata.

**Operational class:** Documentation generation

**Write/network risk:** read-only

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\generate_schema_reference.py
```

## `scripts/generate_script_catalog.py`

**Purpose:** Generate an operational script catalog from active script modules.

**Operational class:** Documentation generation

**Write/network risk:** read-only

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\generate_script_catalog.py
```

## `scripts/generate_work_history.py`

**Purpose:** Generate the project work-history ledger from an exported session snapshot.

**Operational class:** Documentation generation

**Write/network risk:** read-only

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\generate_work_history.py
```

## `scripts/import_a2aj_decisions.py`

**Purpose:** Dry-run importer for A2AJ Canadian case law decisions. Demonstrates mapping from A2AJ HuggingFace dataset to iLit decision schema. Supports: RPD (Refugee Protection Division), RAD (Refugee Appeal Division), FC (Federal Court), FCA (Federal Court of Appeal), and other Canadian courts. Note: This is a dry-run proof-of-concept. Actual import would require: 1. Database write permissions 2. Deduplication against existing iLit decisions 3. Citation linking setup 4. Embedding generation

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\import_a2aj_decisions.py --help
```

## `scripts/import_canlaw_staging.py`

**Purpose:** Import Hugging Face staging records into the primary CaseLibrary database.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\import_canlaw_staging.py --help
```

## `scripts/import_fc_decisions.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\import_fc_decisions.py --help
```

## `scripts/import_historical_statutes.py`

**Purpose:** Importer for historical point-in-time statute versions from justice.gc.ca. Fetches statute versions from PITIndex.html and extracts text from point-in-time HTML pages. Stores multiple versions with their in-force dates to enable decision-date matching (core of Phase 1 requirement). Example: IRPA had 12+ versions between 2017-2026; this importer stores them with their effective dates so a decision from 2019-06-15 can be matched to the IRPA version that was in force on that date.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\import_historical_statutes.py --help
```

## `scripts/import_seed_cases_from_a2aj_api.py`

**Purpose:** Import missing seed cases via A2AJ REST API /fetch. Designed for targeted backfill of known citations (not bulk scraping).

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\import_seed_cases_from_a2aj_api.py --help
```

## `scripts/import_statutes.py`

**Purpose:** Importer for Canadian federal statutes from Justice Laws XML (justice.gc.ca). Imports statute text with versioning information (in-force dates) for: - Immigration and Refugee Protection Act (IRPA) - Immigration and Refugee Protection Regulations (IRPR) - Citizenship Act - Customs Act - Federal Courts Act - Federal Courts Rules - Canadian Charter of Rights and Freedoms Uses: justice.gc.ca REST API for statute versions and text. License: Open Government License (Canada)

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\import_statutes.py --help
```

## `scripts/index_legislation.py`

**Purpose:** Index authoritative legal sources into section-addressable references.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\index_legislation.py --help
```

## `scripts/ingest_a2aj_api.py`

**Purpose:** Ingest A2AJ records from a paginated API into local /ingest. This complements parquet ingestion by allowing direct sync from a live A2AJ API.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\ingest_a2aj_api.py --help
```

## `scripts/ingest_a2aj_citation_network.py`

**Purpose:** Ingest A2AJ citation-network data into local provenance tables and graph edges.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\ingest_a2aj_citation_network.py --help
```

## `scripts/ingest_a2aj_parquet.py`

**Purpose:** Raw-ingest A2AJ case-law Parquet records without OpenAI calls.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\ingest_a2aj_parquet.py --help
```

## `scripts/ingest_canlii_seed_cases.py`

**Purpose:** Ingest seed immigration cases from CanLII by citation. Mode A: direct HTML fetch + parse from CanLII case pages. Notes: - CanLII may return anti-bot 403 pages for some requests. This script logs those failures and continues so you can still ingest whatever is accessible. - The script posts normalized payloads to the existing local /ingest endpoint.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\ingest_canlii_seed_cases.py --help
```

## `scripts/ingest_hf_fc_activity.py`

**Purpose:** Load the Hugging Face FC activity dataset into the canonical database tables.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\ingest_hf_fc_activity.py --help
```

## `scripts/ingest_synthetic_cases.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\ingest_synthetic_cases.py --help
```

## `scripts/inspect_context_variants.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\inspect_context_variants.py --help
```

## `scripts/inspect_discussion_units.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\inspect_discussion_units.py --help
```

## `scripts/judge_reconciliation_report.py`

**Purpose:** Report stored judge metadata and canonical profile-link mismatches without writes.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\judge_reconciliation_report.py --help
```

## `scripts/link_citation_pinpoints.py`

**Purpose:** Persist resolved case-citation paragraph links from stored paragraph chunks.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\link_citation_pinpoints.py --help
```

## `scripts/llm_tag_candidate_review.py`

**Purpose:** Propose immigration research tags with an external OpenAI pass. This script is read-only: it reads stored decision text and writes only a review report.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\llm_tag_candidate_review.py --help
```

## `scripts/map_fc_seed_to_local_cases.py`

**Purpose:** Map normalized FC/CanLII seed links to local case IDs. This creates a deterministic bridge from seed links to local DB cases so citation evidence extraction can run on a concrete case set.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\map_fc_seed_to_local_cases.py --help
```

## `scripts/monitor_vector_index.py`

**Purpose:** Report PostgreSQL progress for the hosted paragraph vector index build.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\monitor_vector_index.py --help
```

## `scripts/normalize_fc_activity_openai_outputs.py`

**Purpose:** Normalize open-ended FC Activity model outputs for evaluation only.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\normalize_fc_activity_openai_outputs.py --help
```

## `scripts/package_discussion_units_llm.py`

**Purpose:** Prepare and optionally run a bounded LLM Discussion Unit review.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\package_discussion_units_llm.py --help
```

## `scripts/plan_self_citation_cleanup.py`

**Purpose:** Plan self-citation cleanup candidates without modifying the database.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\plan_self_citation_cleanup.py --help
```

## `scripts/populate_fc_gold_case_ids.py`

**Purpose:** Populate local_case_id in FC gold template from seed-to-case mapping.

**Operational class:** Evaluation artifact maintenance

**Write/network risk:** filesystem writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\populate_fc_gold_case_ids.py --help
```

## `scripts/prepare_discussion_units_cohort.py`

**Purpose:** Prepare deterministic reports and no-network requests for a Discussion Unit cohort.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\prepare_discussion_units_cohort.py --help
```

## `scripts/prepare_treatment_teacher_batch.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\prepare_treatment_teacher_batch.py --help
```

## `scripts/quick_search_engine.py`

**Purpose:** Quick semantic search tester over chunk embeddings. Usage: python -m scripts.quick_search_engine "non-refoulement risk evidence"

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\quick_search_engine.py --help
```

## `scripts/reacquire_source_html.py`

**Purpose:** Bounded HTML snapshot reacquisition for the curated core case subset.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\reacquire_source_html.py --help
```

## `scripts/rebuild_citations_controlled.py`

**Purpose:** Run a bounded, citation-only rebuild with baseline and recovery evidence.

**Operational class:** Citation-only rebuild

**Write/network risk:** database writer; dry-run is default and --apply requires explicit confirmation

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\rebuild_citations_controlled.py --help
```

## `scripts/refresh_recent_5000_artifact.py`

**Purpose:** Refresh the derived recent-5000 paragraph retrieval artifact.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\refresh_recent_5000_artifact.py --help
```

## `scripts/remove_self_case_citations.py`

**Purpose:** Remove false-positive self-case short-form citation rows. Dry-run is the default. Use --apply only after reviewing the reported count.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\remove_self_case_citations.py --help
```

## `scripts/remove_self_citations.py`

**Purpose:** Guarded removal of exact citation self-links.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\remove_self_citations.py --help
```

## `scripts/report_a2aj_immigration_selection.py`

**Purpose:** Create a QA report for the immigration-core A2AJ selector output.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\report_a2aj_immigration_selection.py --help
```

## `scripts/report_fc_activity_coverage.py`

**Purpose:** Produce counts-only coverage metrics for the Federal Court Activity tables.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\report_fc_activity_coverage.py --help
```

## `scripts/report_fc_activity_motion_unknowns.py`

**Purpose:** Report recurring evidence patterns among unknown FC Activity motions.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\report_fc_activity_motion_unknowns.py --help
```

## `scripts/report_incomplete_short_form_anchors.py`

**Purpose:** Report stored short-form anchors that can be lengthened from source text.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\report_incomplete_short_form_anchors.py --help
```

## `scripts/report_unresolved_citation_shapes.py`

**Purpose:** Report unresolved citation shapes and exact local recovery signals. The database query is read-only. The report distinguishes exact citation, canonical-title, alias, self-case, and ambiguous signals so a later writer can be limited to a measured, precision-safe family.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\report_unresolved_citation_shapes.py --help
```

## `scripts/resolve_citation_targets.py`

**Purpose:** Resolve stored citation rows to locally available target cases. This intentionally does not extract citations again or call external services.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\resolve_citation_targets.py --help
```

## `scripts/resolve_short_citation_targets.py`

**Purpose:** Link stored case names and shortened citations to unambiguous authorities.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\resolve_short_citation_targets.py --help
```

## `scripts/review_fc_activity_local.py`

**Purpose:** Run one bounded, evidence-constrained FC Activity review through the local provider.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\review_fc_activity_local.py --help
```

## `scripts/review_tag_candidates.py`

**Purpose:** Review candidate tags mined from stored decision text without writing to the database.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\review_tag_candidates.py --help
```

## `scripts/run_case_intelligence_request.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_case_intelligence_request.py --help
```

## `scripts/run_citation_rebuild_progress.py`

**Purpose:** Run a bounded citation rebuild in 10-case progress batches and print compact extraction counts.

**Operational class:** Orchestration

**Write/network risk:** database/network job runner

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_citation_rebuild_progress.py --list-jobs
```

## `scripts/run_discussion_units_cohort.py`

**Purpose:** Run a manifest of Discussion Unit cases with durable skip/retry state.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_discussion_units_cohort.py --help
```

## `scripts/run_fc_activity_openai_structured_pilot.py`

**Purpose:** Run a bounded, review-only structured FC Activity extraction pilot.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_fc_activity_openai_structured_pilot.py --help
```

## `scripts/run_local_paragraph_summary_baseline.py`

**Purpose:** Generate a bounded, report-only local paragraph-summary baseline.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_local_paragraph_summary_baseline.py --help
```

## `scripts/run_model_paragraph_experiment.py`

**Purpose:** Run a bounded model-paragraph versus deterministic-paragraph experiment.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_model_paragraph_experiment.py --help
```

## `scripts/run_overnight.py`

**Purpose:** Run resumable case acquisition and corpus maintenance jobs overnight.

**Operational class:** Orchestration

**Write/network risk:** database/network job runner

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --list-jobs
```

## `scripts/run_paragraph_assessment_batches.py`

**Purpose:** Run paragraph-level assessments in visible, resumable batches.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_paragraph_assessment_batches.py --help
```

## `scripts/run_scc_text_only.py`

**Purpose:** Run the SCC-specific text-only enrichment pipeline.

**Operational class:** Orchestration

**Write/network risk:** database/network job runner

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_scc_text_only.py --list-jobs
```

## `scripts/run_treatment_teacher_batch.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_treatment_teacher_batch.py --help
```

## `scripts/run_v2_pipeline.py`

**Purpose:** Run the complete V2 Pipeline with durable state and per-case quarantine.

**Operational class:** Orchestration

**Write/network risk:** database/network job runner

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_v2_pipeline.py --list-jobs
```

## `scripts/run_v2_pipeline_case.py`

**Purpose:** Run and compare the complete V2 Pipeline for one canonical case.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_v2_pipeline_case.py --help
```

## `scripts/run_v2_text_only_fast.py`

**Purpose:** Fast text-only V2 Pipeline runner for non-SCC cases.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_v2_text_only_fast.py --help
```

## `scripts/select_discussion_unit_cohort.py`

**Purpose:** Select a bounded, report-only cohort for Discussion Unit labeling.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\select_discussion_unit_cohort.py --help
```

## `scripts/snapshot_v2_pipeline_baseline.py`

**Purpose:** Create a compact before-snapshot for every canonical case.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\snapshot_v2_pipeline_baseline.py --help
```

## `scripts/tag_cases.py`

**Purpose:** Build deterministic text and metadata tags for canonical cases.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\tag_cases.py --help
```

## `scripts/tag_cases_v2.py`

**Purpose:** Apply the independent Tagging V2 core whitelist to canonical cases.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\tag_cases_v2.py --help
```

## `scripts/tag_cases_v3.py`

**Purpose:** Apply the inactive Tagging V3 core whitelist to canonical cases.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\tag_cases_v3.py --help
```

## `scripts/tag_prototype_topics.py`

**Purpose:** Tag prototype cohort cases with topic-keyword metadata. Writes `topic_keywords` and `topic_scores` into each case metadata_json.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\tag_prototype_topics.py --help
```

## `scripts/verify_citation_extraction.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\verify_citation_extraction.py --help
```

## `scripts/verify_fc_case_existence.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Source verification

**Write/network risk:** network and filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\verify_fc_case_existence.py --help
```
