# Generated Script Catalog

This file is generated from active `scripts/*.py` modules by `scripts/generate_script_catalog.py`. Do not edit it manually.

Run every script from the repository root with the project virtual environment. For database/network writers, read `--help`, use dry-run/preflight/limit options where available, and confirm no other bulk PostgreSQL writer is active.

Active scripts documented: 196

## Catalog

| Script | Class | Risk | Safe first command |
| --- | --- | --- | --- |
| `a2aj_case_importer.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\a2aj_case_importer.py --help` |
| `a2aj_diagnostic.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\a2aj_diagnostic.py --help` |
| `acquire_case_html.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\acquire_case_html.py --list-jobs` |
| `adjudicate_fc_metadata.py` | Metadata adjudication | OpenAI and database writer | `.\venv\Scripts\python.exe scripts\adjudicate_fc_metadata.py --help` |
| `agent_harness.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\agent_harness.py --help` |
| `agent_policy.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\agent_policy.py --help` |
| `aggregate_recorded_costs.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\aggregate_recorded_costs.py --list-jobs` |
| `ai_triage_citation_candidate.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\ai_triage_citation_candidate.py --help` |
| `analyze_themes_before_after.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\analyze_themes_before_after.py --help` |
| `apply_judge_aliases.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\apply_judge_aliases.py --help` |
| `audit_discussion_unit_structure.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_discussion_unit_structure.py --help` |
| `audit_fc_activity_motion_unknowns_openai.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_fc_activity_motion_unknowns_openai.py --help` |
| `audit_fc_activity_openai.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_fc_activity_openai.py --help` |
| `audit_fc_metadata_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_fc_metadata_extraction.py --help` |
| `audit_self_citations.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_self_citations.py --help` |
| `backfill_case_metadata_outcomes.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_case_metadata_outcomes.py --help` |
| `backfill_case_outcomes.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_case_outcomes.py --help` |
| `backfill_case_tags_v3.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_case_tags_v3.py --help` |
| `backfill_fc_case_metadata.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_fc_case_metadata.py --help` |
| `backfill_judge_profiles.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_judge_profiles.py --help` |
| `backfill_panel_judges.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_panel_judges.py --help` |
| `backfill_rpd_header.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_rpd_header.py --help` |
| `backfill_statute_instrument_keys.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_statute_instrument_keys.py --help` |
| `backfill_statute_provisions.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_statute_provisions.py --help` |
| `batch_compute_units.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\batch_compute_units.py --help` |
| `benchmark_case_citations.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\benchmark_case_citations.py --help` |
| `benchmark_citation_resolution.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\benchmark_citation_resolution.py --help` |
| `browser_smoke.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\browser_smoke.py --help` |
| `build_alert_digest.py` | Saved-search digest rendering | offline JSON input; filesystem output only; no database, network or sending | `.\venv\Scripts\python.exe scripts\build_alert_digest.py --help` |
| `build_case_fingerprints.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_case_fingerprints.py --help` |
| `build_changelog.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_changelog.py --help` |
| `build_citation_sample_candidate.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_citation_sample_candidate.py --help` |
| `build_core_immigration_set.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_core_immigration_set.py --help` |
| `build_discussion_unit_priority_lists.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_discussion_unit_priority_lists.py --help` |
| `build_expansion_proposal.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_expansion_proposal.py --help` |
| `build_fc_activity_audit_report.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_activity_audit_report.py --help` |
| `build_fc_activity_gold_template.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_activity_gold_template.py --help` |
| `build_fc_batch_from_party.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_batch_from_party.py --help` |
| `build_fc_citation_gold_template.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_citation_gold_template.py --help` |
| `build_fc_citation_seed.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_citation_seed.py --help` |
| `build_fc_metadata_gold_set.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_metadata_gold_set.py --help` |
| `build_final_expansion.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_final_expansion.py --help` |
| `build_five_case_citation_gold_candidate.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_five_case_citation_gold_candidate.py --help` |
| `build_mason_argument_citation_fixture.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_mason_argument_citation_fixture.py --help` |
| `build_mason_case_intelligence_request.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_mason_case_intelligence_request.py --help` |
| `build_mason_citation_review_ledger.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_mason_citation_review_ledger.py --help` |
| `build_paragraph_cited_by.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_paragraph_cited_by.py --help` |
| `build_prototype_cohort.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_prototype_cohort.py --help` |
| `build_refined_citations.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_refined_citations.py --help` |
| `build_statute_demand_report.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_statute_demand_report.py --help` |
| `build_tagging_v2_core_candidates.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_tagging_v2_core_candidates.py --help` |
| `build_treatment_distillation.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_treatment_distillation.py --help` |
| `build_treatment_review_packet.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_treatment_review_packet.py --help` |
| `build_treatment_teacher_fixture.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_treatment_teacher_fixture.py --help` |
| `case_types_eval.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\case_types_eval.py --help` |
| `check_generated_docs.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\check_generated_docs.py --help` |
| `check_saved_searches.py` | Saved-search alert check | bounded database reader; --apply writes unseen case alerts; dry-run is default | `.\venv\Scripts\python.exe scripts\check_saved_searches.py --help` |
| `check_site_tour.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\check_site_tour.py --help` |
| `chunk_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\chunk_cases.py --help` |
| `classify_case_types.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\classify_case_types.py --help` |
| `classify_fc_activity.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\classify_fc_activity.py --help` |
| `clean_llm_tag_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\clean_llm_tag_report.py --help` |
| `clean_tag_candidate_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\clean_tag_candidate_report.py --help` |
| `compare_eval_runs.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\compare_eval_runs.py --help` |
| `compare_pipeline_case.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\compare_pipeline_case.py --help` |
| `crawl_canlii.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\crawl_canlii.py --help` |
| `cross_reference_seed_cases.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\cross_reference_seed_cases.py --help` |
| `curate_a2aj_cases.py` | A2AJ curation and canonical import | database writer | `.\venv\Scripts\python.exe scripts\curate_a2aj_cases.py --help` |
| `curate_a2aj_immigration_cases.py` | A2AJ curation and canonical import | database writer | `.\venv\Scripts\python.exe scripts\curate_a2aj_immigration_cases.py --help` |
| `daily_intake.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\daily_intake.py --help` |
| `deduplicate_a2aj.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\deduplicate_a2aj.py --help` |
| `discover_recent_case_themes.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\discover_recent_case_themes.py --help` |
| `discussion_units_ledger.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\discussion_units_ledger.py --help` |
| `download_reference_library.py` | Reference acquisition | network and filesystem writer | `.\venv\Scripts\python.exe scripts\download_reference_library.py --help` |
| `dry_run_paragraph_evidence_bridge.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\dry_run_paragraph_evidence_bridge.py --help` |
| `embed_a2aj_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_a2aj_cases.py --help` |
| `embed_documentation_appendices.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_documentation_appendices.py --help` |
| `embed_local_chunks.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_local_chunks.py --help` |
| `embed_openai_chunks.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_openai_chunks.py --help` |
| `eval_models.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\eval_models.py --help` |
| `evaluate_case_structure.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_case_structure.py --help` |
| `evaluate_chunk_parity.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_chunk_parity.py --help` |
| `evaluate_citation_refinement.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_citation_refinement.py --help` |
| `evaluate_data_quality.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_data_quality.py --help` |
| `evaluate_discussion_unit_boundaries.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_discussion_unit_boundaries.py --help` |
| `evaluate_fc_activity_deterministic.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_fc_activity_deterministic.py --help` |
| `evaluate_fc_citation_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_fc_citation_extraction.py --help` |
| `evaluate_retrieval.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_retrieval.py --help` |
| `evaluate_retrieval_benchmark.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_retrieval_benchmark.py --help` |
| `evaluate_statute_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_statute_extraction.py --help` |
| `evaluate_statute_sections.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_statute_sections.py --help` |
| `evidence_gate.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\evidence_gate.py --help` |
| `expand_legal_concepts.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\expand_legal_concepts.py --help` |
| `export_fc_activity_package.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\export_fc_activity_package.py --help` |
| `export_tagging_v3_canary_review.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\export_tagging_v3_canary_review.py --help` |
| `extract_a2aj_case_citations_resumable.py` | Citation extraction maintenance | database writer | `.\venv\Scripts\python.exe scripts\extract_a2aj_case_citations_resumable.py --help` |
| `extract_a2aj_provincial_acts.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\extract_a2aj_provincial_acts.py --help` |
| `extract_citation_network.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\extract_citation_network.py --help` |
| `extract_fc_citation_evidence.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\extract_fc_citation_evidence.py --help` |
| `extract_irpa_irpr_references.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\extract_irpa_irpr_references.py --help` |
| `extract_seed_cases_from_transcript.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\extract_seed_cases_from_transcript.py --help` |
| `fc_activity_extractors.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\fc_activity_extractors.py --help` |
| `fc_portal_collector.py` | Federal Court source acquisition | network and filesystem writer | `.\venv\Scripts\python.exe scripts\fc_portal_collector.py --help` |
| `fetch_fc_procedural_history.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\fetch_fc_procedural_history.py --help` |
| `fingerprint_pilot.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\fingerprint_pilot.py --help` |
| `flag_weak_short_form_links.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\flag_weak_short_form_links.py --help` |
| `generate_api_reference.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_api_reference.py` |
| `generate_schema_reference.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_schema_reference.py` |
| `generate_script_catalog.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_script_catalog.py` |
| `generate_work_history.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_work_history.py` |
| `import_a2aj_decisions.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_a2aj_decisions.py --help` |
| `import_a2aj_full.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_a2aj_full.py --help` |
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
| `judge_alias_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\judge_alias_report.py --help` |
| `judge_reconciliation_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\judge_reconciliation_report.py --help` |
| `link_citation_pinpoints.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\link_citation_pinpoints.py --help` |
| `link_refined_citations.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\link_refined_citations.py --help` |
| `llm_tag_candidate_review.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\llm_tag_candidate_review.py --help` |
| `map_fc_seed_to_local_cases.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\map_fc_seed_to_local_cases.py --help` |
| `measure_precision.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\measure_precision.py --help` |
| `measure_real_coverage.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\measure_real_coverage.py --help` |
| `measure_tagging_coverage.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\measure_tagging_coverage.py --help` |
| `mine_a2aj_concepts.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\mine_a2aj_concepts.py --help` |
| `mine_legal_concepts.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\mine_legal_concepts.py --help` |
| `monitor_vector_index.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\monitor_vector_index.py --help` |
| `normalize_fc_activity_openai_outputs.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\normalize_fc_activity_openai_outputs.py --help` |
| `package_discussion_units_llm.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\package_discussion_units_llm.py --help` |
| `plan_self_citation_cleanup.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\plan_self_citation_cleanup.py --help` |
| `populate_fc_gold_case_ids.py` | Evaluation artifact maintenance | filesystem writer | `.\venv\Scripts\python.exe scripts\populate_fc_gold_case_ids.py --help` |
| `prepare_discussion_units_cohort.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\prepare_discussion_units_cohort.py --help` |
| `prepare_treatment_teacher_batch.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\prepare_treatment_teacher_batch.py --help` |
| `profile_reader.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\profile_reader.py --help` |
| `quick_search_engine.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\quick_search_engine.py --help` |
| `reacquire_source_html.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\reacquire_source_html.py --help` |
| `rebuild_citations_controlled.py` | Citation-only rebuild | database writer; dry-run is default and --apply requires explicit confirmation | `.\venv\Scripts\python.exe scripts\rebuild_citations_controlled.py --help` |
| `recompute_citation_metrics.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\recompute_citation_metrics.py --help` |
| `reextract_statute_references.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\reextract_statute_references.py --help` |
| `refresh_recent_5000_artifact.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\refresh_recent_5000_artifact.py --help` |
| `regenerate_docs.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\regenerate_docs.py --help` |
| `remove_self_case_citations.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\remove_self_case_citations.py --help` |
| `remove_self_citations.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\remove_self_citations.py --help` |
| `remove_test_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\remove_test_cases.py --help` |
| `repair_glued_word_sections.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\repair_glued_word_sections.py --help` |
| `repair_range_word_sections.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\repair_range_word_sections.py --help` |
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
| `run_jobs.py` | Standalone interval orchestration | DB-free scheduler; opt-in child commands may write or use network; defaults disabled | `.\venv\Scripts\python.exe scripts\run_jobs.py --list` |
| `run_live_analysis_mocks.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_live_analysis_mocks.py --help` |
| `run_local_paragraph_summary_baseline.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_local_paragraph_summary_baseline.py --help` |
| `run_model_paragraph_experiment.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_model_paragraph_experiment.py --help` |
| `run_outcome_checker.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_outcome_checker.py --help` |
| `run_overnight.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\run_overnight.py --list-jobs` |
| `run_paragraph_assessment_batches.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_paragraph_assessment_batches.py --help` |
| `run_scc_text_only.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\run_scc_text_only.py --list-jobs` |
| `run_treatment_teacher_batch.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_treatment_teacher_batch.py --help` |
| `run_v2_pipeline.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\run_v2_pipeline.py --list-jobs` |
| `run_v2_pipeline_case.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_v2_pipeline_case.py --help` |
| `run_v2_text_only_fast.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\run_v2_text_only_fast.py --help` |
| `sample_pinpoint_forms.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\sample_pinpoint_forms.py --help` |
| `sample_statute_extraction.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\sample_statute_extraction.py --help` |
| `scheduled_intake_daemon.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\scheduled_intake_daemon.py --help` |
| `score_search_gold.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\score_search_gold.py --help` |
| `select_discussion_unit_cohort.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\select_discussion_unit_cohort.py --help` |
| `snapshot_v2_pipeline_baseline.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\snapshot_v2_pipeline_baseline.py --help` |
| `tag_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_cases.py --help` |
| `tag_cases_v2.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_cases_v2.py --help` |
| `tag_cases_v3.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_cases_v3.py --help` |
| `tag_prototype_topics.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_prototype_topics.py --help` |
| `test_citation_intelligence_prompts.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\test_citation_intelligence_prompts.py --help` |
| `validate_precision.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\validate_precision.py --help` |
| `verify_citation_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\verify_citation_extraction.py --help` |
| `verify_fc_case_existence.py` | Source verification | network and filesystem output | `.\venv\Scripts\python.exe scripts\verify_fc_case_existence.py --help` |

## `scripts/a2aj_case_importer.py`

**Purpose:** A2AJ case law importer for Federal courts (FC, FCA, SCC, RAD, RPD). Loads A2AJ Canadian case law dataset, deduplicates against existing iLit cases, and reports how many new decisions per court would be added. This enables expansion of case database with 100k+ academic dataset cases.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\a2aj_case_importer.py --help
```

## `scripts/a2aj_diagnostic.py`

**Purpose:** Diagnostic tool to understand why A2AJ parsing is failing. Samples rows and reports what's missing/invalid.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\a2aj_diagnostic.py --help
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

## `scripts/analyze_themes_before_after.py`

**Purpose:** Analyze theme discovery before and after stopword filtering. Run this on the PC with access to the caselibrary database: python scripts/analyze_themes_before_after.py Outputs: logs/theme_analysis_before_after.txt

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\analyze_themes_before_after.py --help
```

## `scripts/apply_judge_aliases.py`

**Purpose:** Propose, apply or revert judge profile aliases (reversible; dry-run by default). Duplicate judge profiles (same person under different strings) are mapped onto one canonical profile in `judge_profile_aliases`. No profile or case link is rewritten or deleted. python scripts/apply_judge_aliases.py # dry run: print proposed merges python scripts/apply_judge_aliases.py --apply # write alias rows (needs Daniel's go) python scripts/apply_judge_aliases.py --prune # dry run: rule rows the current rules no longer propose python scripts/apply_judge_aliases.py --prune --apply # delete those rows (e.g. Marc/Simon Noël) python scripts/apply_judge_aliases.py --revert # delete every source='rule' alias row

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\apply_judge_aliases.py --help
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

## `scripts/backfill_case_tags_v3.py`

**Purpose:** Backfill all cases with V3 legal tags. Resumable and idempotent.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_case_tags_v3.py --help
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

## `scripts/backfill_panel_judges.py`

**Purpose:** Create one judge profile per panel member for multi-judge cases (SCC) and link them (dry-run by default). SCC cases store the whole panel in one field ("Wagner, Richard; Abella, Rosalie; ..."). The first profile backfill turned each distinct panel string into a single fake judge. This script splits the panel, finds or creates one profile per judge, and links each case to every panel member. Existing profiles and links are never edited or deleted; reruns add nothing new. python scripts/backfill_panel_judges.py # dry run, SCC python scripts/backfill_panel_judges.py --apply # write (needs Daniel's go) python scripts/backfill_panel_judges.py --courts FCA # panel = the "present" lines ("STRATAS J.A.") FCA decisions store the authoring judge in `judge` (already linked) and the full bench in `present`, one judge per line. Panel members reuse the profile of the same raw string ("NOËL J.A."), so no duplicates appear, and only "J.A." / "C.J." lines count (assessment officers and clerks are skipped).

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_panel_judges.py --help
```

## `scripts/backfill_rpd_header.py`

**Purpose:** Fix the panel member and place of hearing stored for Refugee Protection Division decisions. Dry run by default. The old extractor left RPD decision makers blank and let "place of hearing" run on through the cover page. This re-reads those two fields from the cover page (`backend.metadata._rpd_header_fields`) and updates only `metadata_json -> reader_extracted -> judge` and `-> place of hearing` on RPD cases. python scripts/backfill_rpd_header.py --limit 20 # dry run: print before/after for 20 cases python scripts/backfill_rpd_header.py --apply # write (needs Daniel's go for the live database) python scripts/backfill_rpd_header.py --revert-file undo.json # put the old values back

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_rpd_header.py --help
```

## `scripts/backfill_statute_instrument_keys.py`

**Purpose:** Fill statute_references.instrument_key for rows that name a registered act but were stored without a key. About 59% of statute_references have no instrument_key, and most of those name an act the registry already knows ("Patent Act", "Federal Court Rules", "Immigration and Refugee Protection Act, S.C. 2001, c. 27"). This resolves the act name with backend/instrument_resolver.py (exact normalized names only, court-aware for names shared with provincial acts) and writes only the instrument_key column, only where it is still NULL. Dry run by default (counts per instrument and samples). --apply first writes an undo file of every id and key it is about to set; --undo FILE puts those rows back to NULL, only where the key is still the one written.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_statute_instrument_keys.py --help
```

## `scripts/backfill_statute_provisions.py`

**Purpose:** Fill statute_references.provision_section/subsection/paragraph from the stored pinpoint. The provision_* columns were added after most references were stored, so about 99.9% of rows have a pinpoint such as "36(1)(a)" but an empty provision_section. Statute-consideration queries filter on provision_section and so find almost nothing. This derives the columns from the pinpoint with the same parser the extractor uses. It never changes the pinpoint, the instrument or any other column, and only touches rows whose provision_section is still NULL. Dry run by default (counts and samples only). Use --apply to write.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_statute_provisions.py --help
```

## `scripts/batch_compute_units.py`

**Purpose:** Resumable batch job CLI for computing discussion units across the case corpus. Usage: python scripts/batch_compute_units.py [--start CASE_ID] [--end CASE_ID] [--clear] Examples: # Compute all cases from start (default: case 1) python scripts/batch_compute_units.py # Compute specific range python scripts/batch_compute_units.py --start 1 --end 500 # Clear all cached units and recompute python scripts/batch_compute_units.py --clear # Resume from case 501 after a previous run python scripts/batch_compute_units.py --start 501

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\batch_compute_units.py --help
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

## `scripts/build_alert_digest.py`

**Purpose:** Build an offline saved-search digest from enriched JSON on stdin or --input.

**Operational class:** Saved-search digest rendering

**Write/network risk:** offline JSON input; filesystem output only; no database, network or sending

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_alert_digest.py --help
```

## `scripts/build_case_fingerprints.py`

**Purpose:** Compute stored case fingerprints for cases that have none (batch job; not run by the live site). Dry run by default: it reports how many cases would be fingerprinted. Use --apply to write. Cheap and read-mostly: it reads cases.full_text and writes only case_fingerprints.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_case_fingerprints.py --help
```

## `scripts/build_changelog.py`

**Purpose:** Build the About-page changelog from GitHub records plus hand-written entries. Inputs (all committed under data/changelog/): entries.json hand-written, plain-language entries. Each one lists the merged PRs ("#216"), commits (short sha) or work-history days it summarises. An entry that cites merged PRs takes the date of the latest one, so dates always match GitHub. skip.json merged PRs deliberately left out (docs-only, CI tweaks, reverts, scratch work), with a reason. github_records.json cache of merged PRs and commits, written by --refresh. Output: data/changelog/changelog.json, which the About page embeds. Nothing is fetched when the page is viewed. python scripts/build_changelog.py rebuild changelog.json from the committed inputs python scripts/build_changelog.py --refresh first pull merged PRs and commits from GitHub (GITHUB_TOKEN, or the gh CLI) python scripts/build_changelog.py --check exit 1 if changelog.json is out of date (used by tests) python scripts/build_changelog.py --uncovered list merged PRs that have no entry and are not skipped Merged PRs that have no entry and are not skipped still appear, as short "auto" entries built from the PR title, so a refresh never loses work; write a proper entry for them in entries.json when convenient.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_changelog.py --help
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

## `scripts/build_expansion_proposal.py`

**Purpose:** Build comprehensive V3 expansion proposal with categorized legal terms. Mines 1-2 word legal concepts from immigration case law and organizes them into V3 taxonomy categories for deterministic tagging expansion.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_expansion_proposal.py --help
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

## `scripts/build_final_expansion.py`

**Purpose:** Build final V3 expansion proposal with measured coverage. Takes mined concepts, combines with existing proposal, and generates a comprehensive expansion JSON and coverage report.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_final_expansion.py --help
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

## `scripts/build_paragraph_cited_by.py`

**Purpose:** Build the paragraph-level "cited by" tables from stored citation occurrences. For every case that cites another library case by paragraph, store which paragraph it cites, how often, and the signal phrase written next to the citation ("see also", "followed in", "distinguished", ...). The reader's Markup view reads these rows. Safe by default: with no flags it only reports what it would do. Nothing is written without --apply. No AI. It is built so it cannot slow the live site down (lowest process priority, one database connection, short time limits, rests between small batches, optional site health check, stop file). python scripts/build_paragraph_cited_by.py # plan only python scripts/build_paragraph_cited_by.py --apply --max-minutes 30 --health-url http://127.0.0.1:8001/health/ready python scripts/build_paragraph_cited_by.py --report-cited 1292 # show what is stored for a case Resumable: a citing case counts as done once its status row is written, so stopping (Ctrl+C, the stop file, --max-minutes) and running the same command again carries on. To redo everything after changing the classifier, raise ALGO_VERSION in backend/paragraph_cited_by.py. Read docs/PARAGRAPH_CITED_BY.md before running.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_paragraph_cited_by.py --help
```

## `scripts/build_prototype_cohort.py`

**Purpose:** Build and operationalize prototype cohort for immigration case research. Pipeline: 1) Combine the 300-case core list with exact-matched seed/canon cases. 2) Embed cohort cases that are not yet embedded. 3) Export citation map edges restricted to cohort-internal citations.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_prototype_cohort.py --help
```

## `scripts/build_refined_citations.py`

**Purpose:** Build side-by-side refined case citations (second-pass extraction) for decisions. Writes only to the new tables `citations_refined` and `citation_refine_status`; the live `citations` table is never touched, so the site keeps reading pass-one data. DRY RUN BY DEFAULT: nothing is written without `--apply`. python scripts/build_refined_citations.py --limit 500 # dry run: counts and a compare to pass one python scripts/build_refined_citations.py --limit 500 --apply # write the first 500 decisions python scripts/build_refined_citations.py --language fr --random-seed 1 --limit 500 # random French sample, dry run python scripts/build_refined_citations.py --apply --court FC # continue (resumable; skips done decisions) python scripts/build_refined_citations.py --revert --yes # delete all refined rows and status rows for this version One decision per transaction, resumable (decisions with a status row for the same refine version are skipped), capped by --limit, with an optional stop file checked between decisions. Docket rows are not stored (no column for them yet). Statute references and paragraph links are a later step.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_refined_citations.py --help
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

## `scripts/case_types_eval.py`

**Purpose:** Run the case-type classifier over a stratified sample of A2AJ parquet files (read-only, no database). Example: python scripts/case_types_eval.py --parquet-dir /path/to/parquets --per-stratum 40 --out out.jsonl

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\case_types_eval.py --help
```

## `scripts/check_generated_docs.py`

**Purpose:** Check that checked-in generated documentation matches its generators.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\check_generated_docs.py --help
```

## `scripts/check_saved_searches.py`

**Purpose:** Check saved case searches and optionally persist previously unseen matches.

**Operational class:** Saved-search alert check

**Write/network risk:** bounded database reader; --apply writes unseen case alerts; dry-run is default

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\check_saved_searches.py --help
```

## `scripts/check_site_tour.py`

**Purpose:** Check the site tour in a real browser: every step's target must resolve, and the controls must work. Needs Playwright with Chromium and a running copy of the site. python scripts/check_site_tour.py --base-url http://localhost:8001 --walk --shots /tmp/tour-shots python scripts/check_site_tour.py --base-url https://www.ilit.ca --walk --require-data python scripts/check_site_tour.py --steps-only # only validate site_tour_steps.json (no browser) --walk takes the tour as a visitor does (start on About, press only Next) and prints, for each step, the milliseconds from pressing Next to the card being ready, any step that was skipped, and any highlight that is off screen or hidden behind the card. Like a visitor's tour it signs in to the Workbench demo and pins the example decisions. Without --walk (or with --each) every step is also opened on its own, as after a refresh; that mode is read-only unless --demo-sign-in is given. A step marked optional, or one that names a feature in "needs", may be skipped without failing the check; every other step must show its card on the page it names. Exit code 1 if any required step failed, a highlight was off screen, or the page raised an error.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\check_site_tour.py --help
```

## `scripts/chunk_cases.py`

**Purpose:** Create resumable text chunks for canonical cases without embedding calls.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\chunk_cases.py --help
```

## `scripts/classify_case_types.py`

**Purpose:** Label every decision with its case type (deterministic rules, no AI). Dry run by default. python scripts/classify_case_types.py --limit 200 # dry run: print counts only python scripts/classify_case_types.py --court FC --apply # write rows to case_type_labels python scripts/classify_case_types.py --revert # delete rows of this taxonomy version Only reads `cases` and writes `case_type_labels`. Resumable: decisions that already have a row for the current taxonomy version are skipped.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\classify_case_types.py --help
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

## `scripts/compare_eval_runs.py`

**Purpose:** Compare two model-evaluation runs using paired bootstrap confidence intervals.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\compare_eval_runs.py --help
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

## `scripts/daily_intake.py`

**Purpose:** Daily intake: new decisions from A2AJ, then new Federal Court (IMM) activity records. One run does, in order: 1. Cases. For each court (default FC, FCA, SCC) it asks Hugging Face whether the A2AJ partition has changed since the last completed run (one HEAD request, no download). Only if it changed does it download the partition, import decisions newer than what the library holds (minus a small overlap), skip anything already present, and run the deterministic processing layers (chunks, metadata, outcome, citations, statutes, tags) on each new case. 2. FC activity. New IMM files are found by walking forward from the highest IMM number already stored for the current year, fetching each from the Federal Court registry until several numbers in a row do not exist. A few recently active files are also re-fetched so their newest docket entries arrive. Touched files are re-classified with the existing rule classifier. Everything is deterministic: no AI or model calls. Each run writes one row to ingestion_runs (started, then finished with finished_at and counts). Caps keep a run small: --max-cases, --max-fc-requests, --max-minutes. Re-running is safe: existing cases and docket entries are never duplicated. Usage: python scripts/daily_intake.py --dry-run # report only, writes nothing python scripts/daily_intake.py # the real daily run python scripts/daily_intake.py --skip-activity # cases only python scripts/daily_intake.py --skip-cases # FC activity only

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\daily_intake.py --help
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

## `scripts/eval_models.py`

**Purpose:** Evaluate local embedding and JSON-generation models on frozen datasets.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\eval_models.py --help
```

## `scripts/evaluate_case_structure.py`

**Purpose:** Score deterministic case-structure labelling against hand-labelled decisions. Gold: 22 Federal Court decisions from 2001-2004 (data/eval/case_structure/gold_fc_2001_2004_v2.json, paragraphs from the stored reports), 30 more hand-labelled FC / FCA / SCC decisions (gold_new_cases.json) and 18 RPD decisions (gold_rpd_labels.json, text read from an extract that is not in the repository). Each case has a 'dev', 'holdout' or 'holdout2' split. Only dev cases may be used for tuning; the holdouts are scored at declared checkpoints. Approaches (all offline, no database, network or AI): main the segmentation on main (continuity + boundary rules) with deterministic unit role labels structure paragraph role labelling by cues + ordered skeleton, units from role changes structure+h the same plus a split at each major heading inside the analysis Run: python scripts/evaluate_case_structure.py [--per-case] [--splits dev holdout holdout2]

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_case_structure.py --help
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

## `scripts/evaluate_discussion_unit_boundaries.py`

**Purpose:** Score discussion-unit boundaries against hand-read gold labels. One evaluator for every version of ``backend/contextual_authority/discussion_units.py``. Everything runs offline from the stored deterministic case reports (``data/eval/llm_discussion_units_pilot/core_300_run/reports``); no database, network or model calls. Counting is per boundary (a boundary is a unit start paragraph index): * hits = gold starts that the algorithm also predicts (exact) * missed = gold starts not predicted * spurious = predicted starts not in gold * within-1 = gold starts matched one-to-one to a predicted start at most one paragraph away (exact matches are paired first, so one predicted start can never satisfy two gold starts) Paragraph 0 is a boundary in every gold label and every prediction, so the "interior" columns repeat the counts without it. Usage: python scripts/evaluate_discussion_unit_boundaries.py # working tree python scripts/evaluate_discussion_unit_boundaries.py --rev origin/main --rev ded7069 python scripts/evaluate_discussion_unit_boundaries.py --stored # units saved in the reports

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_discussion_unit_boundaries.py --help
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

## `scripts/evaluate_statute_sections.py`

**Purpose:** Measure section-level statute extraction against the frozen gold set. Gold file: data/eval/statute_section_gold.json (synthetic CBSA-style sentences with the instrument and pinpoint a careful reader would extract; lists are expected one pair per section). Cases with "holdout": true are frozen for before/after comparison: never tune extraction rules on them. Pure measurement, no database, no network. Usage: python scripts/evaluate_statute_sections.py [--split dev|holdout|all] [--misses] [--json out.json]

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_statute_sections.py --help
```

## `scripts/evidence_gate.py`

**Purpose:** Validate manager-owned completion evidence for a task run.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evidence_gate.py --help
```

## `scripts/expand_legal_concepts.py`

**Purpose:** Expand legal concept list to several hundred through domain analysis. Uses legal domain patterns, procedure names, and common case findings to expand the concept vocabulary comprehensively.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\expand_legal_concepts.py --help
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

## `scripts/extract_a2aj_provincial_acts.py`

**Purpose:** Cut a few provincial acts out of the A2AJ canadian-laws parquet files into small JSON snapshots. Source: https://huggingface.co/datasets/a2aj/canadian-laws (one LEGISLATION-<PROVINCE>.parquet per jurisdiction). Only the acts listed in ACTS are taken, never whole provinces. Each snapshot carries the upstream licence text and is indexed by scripts/index_legislation.py (source format "json_sections"). Tier "open": the dataset's licence note permits reproduction with attribution (Ontario, Alberta, Manitoba). Tier "held": British Columbia (licence field blank), Quebec (CC BY-NC-ND 4.0, non-commercial, no derivatives) and Saskatchewan (non-commercial use by permission). Held acts are only counted unless --include-held is given; do not commit their snapshots until the licence question is settled. Usage: python scripts/extract_a2aj_provincial_acts.py --parquet-dir DIR [--write] [--include-held] Without --write it only prints section counts.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\extract_a2aj_provincial_acts.py --help
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

## `scripts/fingerprint_pilot.py`

**Purpose:** Read-only pilot: fingerprint a random sample of real cases and see whether the sample conclusions hold. Reads cases.full_text (SELECT only, in a read-only transaction, one connection, lowest process priority, throttled), computes case fingerprints in memory, and writes everything to files. It writes nothing to the database. Output (default ``data/eval/case_fingerprints/pilot/``): * ``fingerprints.jsonl`` one fingerprint per sampled case (terms, authorities, seconds) * ``pilot-report.md`` timing, neighbours for the landmark cases and 20 random cases, and the 150 hand-labelled pairs re-scored on this library * ``pilot-results.json`` the same numbers, machine readable Run it from the repo folder, for example:: ./venv/Scripts/python.exe scripts/fingerprint_pilot.py --fc 1200 --fca 500 --scc 300

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\fingerprint_pilot.py --help
```

## `scripts/flag_weak_short_form_links.py`

**Purpose:** PARKED 2026-10-06: Daniel asked to leave the live cleanup for later; do not run --apply. Evidence note: /mnt/project-files/citation-refinement/wrong-short-form-links-evidence-2026-10-06.md Find (and optionally unlink) live short-form citations that point at the wrong case. Pass one anchored many capitalised common words ("Lake", "Bank", "Council", "Quebec") to a nearby full citation, and the resolver then linked those rows to the anchored case, so cited-by counts on the live site include links that are not citations of that case. This script re-judges every LINKED short-form row with the same rules the refinement uses (`backend/citation_refine/short_forms.py`) plus one more: the alias must appear as whole words in the linked case's own title. DRY RUN BY DEFAULT: it only reads, prints counts by reason, and writes the suspect rows to a CSV for review. python scripts/flag_weak_short_form_links.py --backup logs/weak_links.csv # dry run python scripts/flag_weak_short_form_links.py --backup logs/weak_links.csv --apply # unlink the suspects python scripts/flag_weak_short_form_links.py --revert-from logs/weak_links.csv --apply # put the links back `--apply` sets `target_case_id` to NULL and `unresolved` to true on the suspect rows only (the backup CSV holds each row's id and previous target and is written BEFORE any change). Cited-by counts and paragraph cited-by data derive from these links and need their usual recompute afterwards; nothing here recomputes them.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\flag_weak_short_form_links.py --help
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

## `scripts/import_a2aj_full.py`

**Purpose:** Full A2AJ Canadian case law importer with deduplication and database writes. Loads A2AJ dataset (226,147 decisions from 29 courts), deduplicates against existing iLit corpus, and imports non-duplicate cases from target courts: - Federal Court (FC): 35,990 decisions - Federal Court of Appeal (FCA): 7,813 decisions - Supreme Court of Canada (SCC): 10,893 decisions - Refugee Appeal Division (RAD): 14,216 decisions - Refugee Protection Division (RPD): 6,729 decisions Total target: 75,641 new cases available for import.

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\import_a2aj_full.py --help
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

## `scripts/judge_alias_report.py`

**Purpose:** Read-only report of proposed same-person judge merge groups (no writes).

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\judge_alias_report.py --help
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

## `scripts/link_refined_citations.py`

**Purpose:** Link refined citation rows (side table ``citations_refined``) to library cases. Dry run by default: reports how many refined rows would link, by kind, and prints examples. ``--apply`` sets ``target_case_id`` on refined rows that resolve to exactly one case (never on the live ``citations`` table) and marks unmatched formal citations ``unresolved``. Resumable: only rows still without a target are looked at. ``--revert --yes`` clears every link this script wrote for the refine version. Nothing on the site reads these rows unless ``CITATIONS_SOURCE=refined`` is set.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\link_refined_citations.py --help
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

## `scripts/measure_precision.py`

**Purpose:** Measure precision of V3 expansion concepts on real case data. Tags a sample of real cases, checks for false positives, and adjusts concept definitions as needed.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\measure_precision.py --help
```

## `scripts/measure_real_coverage.py`

**Purpose:** Measure real coverage on A2AJ dataset with precision validation. Loads 200+ real FC/RAD decisions, tags them before and after expansion, and reports actual precision on new concept matches.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\measure_real_coverage.py --help
```

## `scripts/measure_tagging_coverage.py`

**Purpose:** Measure V3 tagging coverage before and after expansion. Uses the CoreLegalTaggerV3 to tag a sample of real cases and computes: - Percentage of cases with at least one tag - Tag frequency distribution - Coverage improvement from expansion

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\measure_tagging_coverage.py --help
```

## `scripts/mine_a2aj_concepts.py`

**Purpose:** Mine 1-2 word legal concepts from A2AJ Canadian case law dataset. Downloads FC and RAD decisions from Hugging Face A2AJ dataset, extracts high-frequency legal concepts, and measures coverage impact.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\mine_a2aj_concepts.py --help
```

## `scripts/mine_legal_concepts.py`

**Purpose:** Mine 1-2 word legal concepts from case text for V3 tagging expansion. Sources: - A2AJ dataset (Hugging Face, MIT-licensed) - Local case samples - Statute references and headings Outputs: - Candidate terms grouped by category - Frequency and document frequency metrics - Coverage analysis (before/after)

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\mine_legal_concepts.py --help
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

## `scripts/profile_reader.py`

**Purpose:** Time where a decision's reader payload spends its time (read-only). Runs build_case_reader_data for one case with per-stage wall times, SQL statement count and the slowest statements, then the real FastAPI route through TestClient (validation, JSON encoding, middleware) so any gap between the function and the HTTP response is visible. Only SELECTs are issued; the session is rolled back. python scripts/profile_reader.py 35874 python scripts/profile_reader.py 35874 28926 --profile-file logs/profile_reader.txt

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\profile_reader.py --help
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

## `scripts/recompute_citation_metrics.py`

**Purpose:** Refresh the stored "cited by" numbers (citation_metrics). Dry run by default. The stored in_degree was last computed before many citation links were added or cleaned (Baker showed 0 with about 2,900 citing cases), and counted citation rows. It now counts distinct citing cases, as search does. python scripts/recompute_citation_metrics.py # dry run: stored vs live for sample cases and totals python scripts/recompute_citation_metrics.py --apply # recompute and write all rows (needs Daniel's go)

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\recompute_citation_metrics.py --help
```

## `scripts/reextract_statute_references.py`

**Purpose:** Re-extract statute references with the current rules; dry run compares, apply replaces. Why: older extraction dropped decimal sections ("18.1" stored as "18") and mis-handled lists. This reads the same text the original build used (the preferred chunk set, else full text), runs the current extractor, and compares with the stored rows of the same cases. Dry run (default) writes nothing: it reports counts before and after (rows, rows with an instrument, decimal sections, list rows, rows per instrument) and sample changes. --apply with --confirm-statute-reextract first writes every old row of each case to a JSONL backup file, then replaces that case's rows (one transaction per batch). --restore BACKUP puts the backed-up rows back (every column, original ids): for each case in the file it deletes the case's current rows and re-inserts the saved ones. If a case appears more than once in the file (re-runs append), the first entry, the oldest rows, is used. --restore-dry-run reports what it would do. Cases are chosen by --case-id, or by a seeded random sample (--sample N --seed S), or --all; --skip-cases-in BACKUP drops cases a previous apply already backed up (the rest after a first tranche).

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\reextract_statute_references.py --help
```

## `scripts/refresh_recent_5000_artifact.py`

**Purpose:** Refresh the derived recent-5000 paragraph retrieval artifact.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\refresh_recent_5000_artifact.py --help
```

## `scripts/regenerate_docs.py`

**Purpose:** Regenerate every checked-in generated doc and sync the backend file inventory. Run this before pushing any change that adds, renames or removes a script or a file under backend/, or changes routes or tables: python scripts/regenerate_docs.py It rewrites docs/API_REFERENCE.generated.md, docs/SCHEMA_REFERENCE.generated.md and docs/SCRIPT_CATALOG.generated.md, then adds a row to the backend inventory in docs/ARCHITECTURE.md for each new backend file (description taken from the module docstring; edit it afterwards if you like) and drops rows for files that no longer exist. Finally it runs scripts/check_generated_docs.py.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\regenerate_docs.py --help
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

## `scripts/remove_test_cases.py`

**Purpose:** List or delete the 20 placeholder "TEST CASE" decisions (ids 61264 to 61283) from the library. Dry run by default. python scripts/remove_test_cases.py # dry run: show the exact rows and what hangs off them python scripts/remove_test_cases.py --apply # delete them (needs Daniel's go for the live database) Only ids 61264-61283 can ever be touched, and only if every one still looks like a test row (title starts with "TEST CASE", citation contains "TEST" and a number). The script refuses to delete anything if another decision cites one of them, or if a row does not look like a test row.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\remove_test_cases.py --help
```

## `scripts/repair_glued_word_sections.py`

**Purpose:** Repair statute_references.provision_section values like "25s" or "2d" that came from a word glued to the number. The stored pinpoint has its spaces removed, so "s. 25 ss. 3" or "S. 2(d)" read as section "25s" or "2d" in the first backfill. Real lettered sections are uppercase ("224A", "83A", "1F", "39B") or lowercase before a bracket ("224a(1)"), so this touches only rows whose stored pinpoint has LOWERCASE letters straight after the digits and no bracket, never rows of the Criminal Code or Income Tax Act (old lettered sections), and only when the section can be read again from the cited text itself (reference_text: "section 20.1" -> 20.1, "S. 2d" -> 2). Rows where the text gives no section are left alone. Dry run by default; --apply first writes an undo CSV (id, old section, new section); --undo FILE restores the old values where the row still holds the new one.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\repair_glued_word_sections.py --help
```

## `scripts/repair_range_word_sections.py`

**Purpose:** Repair statute_references.provision_section values like "34t" (from "34 to 37") or "25s" (from "25 s. 3"). The first backfill read the "t" of "to" (or the "a" of "and") as a section suffix, so a range or list pinpoint such as "34 to 37" was stored with provision_section "34t". This re-derives only the rows whose section ends in a letter and whose pinpoint runs the section straight into "to", "and" or "th"; it changes a row only when the corrected section is the old one minus that letter. Dry run by default; --apply writes. Safe to run twice.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\repair_range_word_sections.py --help
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

## `scripts/run_jobs.py`

**Purpose:** Run opt-in interval jobs in a separate process, without database or dotenv imports.

**Operational class:** Standalone interval orchestration

**Write/network risk:** DB-free scheduler; opt-in child commands may write or use network; defaults disabled

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_jobs.py --list
```

## `scripts/run_live_analysis_mocks.py`

**Purpose:** Run the synthetic Live Analysis documents and score them against expected.json (read-only, nothing stored). Usage: python scripts/run_live_analysis_mocks.py [folder] [--no-library] The default folder is tests/live_analysis_mocks; the long speed document (03) lives in /mnt/project-files/live-analysis/mock-docs and is only scored when it is in the folder given.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_live_analysis_mocks.py --help
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

## `scripts/run_outcome_checker.py`

**Purpose:** Second-opinion outcome reader for cases the rules leave "unclear" (advisory data, never overwrites). Dry run by default: counts the cases, estimates tokens and cost, calls nothing. A real run needs --confirm-spend and OPENAI_API_KEY, stops at --max-usd (never above 1.00), and writes JSONL files to --out. Only open case law is sent. Use --source gold to measure the checker against the hand-read gold set (class-by-class agreement).

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_outcome_checker.py --help
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

## `scripts/sample_pinpoint_forms.py`

**Purpose:** Count the pinpoint forms that really occur in decisions (read-only sampling aid). Usage: python scripts/sample_pinpoint_forms.py FCA.parquet RPD.parquet [--limit N] [--verify-target FCA.parquet] Input is any parquet with an ``unofficial_text_en`` column (A2AJ dataset shards). Classifies each paragraph/page pinpoint into a shape such as ``N``, ``N-N``, ``N,N and N``, ``N ff``, then reports how much of each shape the repo parser (``backend.citation_refine.pinpoints``) turns into the right set of numbers.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\sample_pinpoint_forms.py --help
```

## `scripts/sample_statute_extraction.py`

**Purpose:** Draw a random sample of real decisions and write the statute references the extractor finds, for hand-checking. READ-ONLY: SELECTs from cases and runs the extractor in memory; writes nothing to the database. For each sampled decision it records every extracted statute reference (text, instrument, pinpoint, context) and every "loose" provision mention (s. 12, subsection 5(1), paragraph 3(b) ...) that no extracted reference covers, so both precision and recall can be hand-checked. Sampling is deterministic for a given --seed (md5 order), per court, so a second run reproduces it. Usage: python scripts/sample_statute_extraction.py --cases-per-court 40 --seed 20261006 --out sample.jsonl

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\sample_statute_extraction.py --help
```

## `scripts/scheduled_intake_daemon.py`

**Purpose:** Low-priority scheduled intake of new decisions from A2AJ and court sources. Runs continuously on Daniel's PC, checking for new decisions every 6 hours (A2AJ) or 24 hours (court sources), deduplicating, and importing without interfering with the live site. Designed to be pausable, resume-able, and disable-able. Disable by: - Setting SCHEDULED_INTAKE_ENABLED=false in .env - Renaming script to .disabled

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\scheduled_intake_daemon.py --help
```

## `scripts/score_search_gold.py`

**Purpose:** Score the case search box against a gold query set (read-only; run on the PC). Modes: legacy (exact-phrase only, the behaviour before the sentence fix), words (most-of-the-words ILIKE), paragraph (paragraph index; needs the paragraph_search table). Example: python scripts/score_search_gold.py --mode paragraph --out scores_paragraph.json python scripts/score_search_gold.py --compare scores_legacy.json scores_paragraph.json Nothing is written to the database. Landmark and citation queries count a hit when an expected citation is in the top 10; topic and French queries count a hit when a top-10 case text matches every oracle regex (a weak, loose check), and the top 3 titles are printed so a person can read them.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\score_search_gold.py --help
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

## `scripts/test_citation_intelligence_prompts.py`

**Purpose:** Test improved citation intelligence assessment prompts against real database cases. This script fetches real cases from the database, runs both current and improved paragraph assessment prompts, and compares output quality and cost. Run on: PC thread (has live database access) Usage: python scripts/test_citation_intelligence_prompts.py --case-ids 123,456,789 --max-paragraphs 300 --budget-usd 20.0 --output-dir /path/to/output

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\test_citation_intelligence_prompts.py --help
```

## `scripts/validate_precision.py`

**Purpose:** Validate precision of V3 expansion on representative case law text. Uses representative FC and RAD case law snippets to measure precision.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\validate_precision.py --help
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
