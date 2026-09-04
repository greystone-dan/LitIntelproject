# Generated Script Catalog

This file is generated from active `scripts/*.py` modules by `scripts/generate_script_catalog.py`. Do not edit it manually.

Run every script from the repository root with the project virtual environment. For database/network writers, read `--help`, use dry-run/preflight/limit options where available, and confirm no other bulk PostgreSQL writer is active.

Active scripts documented: 66

## Catalog

| Script | Class | Risk | Safe first command |
| --- | --- | --- | --- |
| `adjudicate_fc_metadata.py` | Metadata adjudication | OpenAI and database writer | `.\venv\Scripts\python.exe scripts\adjudicate_fc_metadata.py --help` |
| `audit_fc_metadata_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\audit_fc_metadata_extraction.py --help` |
| `backfill_case_metadata_outcomes.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_case_metadata_outcomes.py --help` |
| `backfill_fc_case_metadata.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_fc_case_metadata.py --help` |
| `backfill_judge_profiles.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\backfill_judge_profiles.py --help` |
| `build_core_immigration_set.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_core_immigration_set.py --help` |
| `build_fc_activity_gold_template.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_activity_gold_template.py --help` |
| `build_fc_batch_from_party.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_batch_from_party.py --help` |
| `build_fc_citation_gold_template.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_citation_gold_template.py --help` |
| `build_fc_citation_seed.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_citation_seed.py --help` |
| `build_fc_metadata_gold_set.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_fc_metadata_gold_set.py --help` |
| `build_prototype_cohort.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_prototype_cohort.py --help` |
| `build_tagging_v2_core_candidates.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\build_tagging_v2_core_candidates.py --help` |
| `chunk_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\chunk_cases.py --help` |
| `classify_fc_activity.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\classify_fc_activity.py --help` |
| `clean_llm_tag_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\clean_llm_tag_report.py --help` |
| `clean_tag_candidate_report.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\clean_tag_candidate_report.py --help` |
| `crawl_canlii.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\crawl_canlii.py --help` |
| `cross_reference_seed_cases.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\cross_reference_seed_cases.py --help` |
| `curate_a2aj_cases.py` | A2AJ curation and canonical import | database writer | `.\venv\Scripts\python.exe scripts\curate_a2aj_cases.py --help` |
| `curate_a2aj_immigration_cases.py` | A2AJ curation and canonical import | database writer | `.\venv\Scripts\python.exe scripts\curate_a2aj_immigration_cases.py --help` |
| `download_reference_library.py` | Reference acquisition | network and filesystem writer | `.\venv\Scripts\python.exe scripts\download_reference_library.py --help` |
| `embed_a2aj_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_a2aj_cases.py --help` |
| `embed_documentation_appendices.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_documentation_appendices.py --help` |
| `embed_local_chunks.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_local_chunks.py --help` |
| `embed_openai_chunks.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\embed_openai_chunks.py --help` |
| `evaluate_data_quality.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_data_quality.py --help` |
| `evaluate_fc_citation_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_fc_citation_extraction.py --help` |
| `evaluate_retrieval.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\evaluate_retrieval.py --help` |
| `extract_a2aj_case_citations_resumable.py` | Citation extraction maintenance | database writer | `.\venv\Scripts\python.exe scripts\extract_a2aj_case_citations_resumable.py --help` |
| `extract_citation_network.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\extract_citation_network.py --help` |
| `extract_fc_citation_evidence.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\extract_fc_citation_evidence.py --help` |
| `extract_irpa_irpr_references.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\extract_irpa_irpr_references.py --help` |
| `extract_seed_cases_from_transcript.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\extract_seed_cases_from_transcript.py --help` |
| `fc_portal_collector.py` | Federal Court source acquisition | network and filesystem writer | `.\venv\Scripts\python.exe scripts\fc_portal_collector.py --help` |
| `fetch_fc_procedural_history.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\fetch_fc_procedural_history.py --help` |
| `generate_api_reference.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_api_reference.py` |
| `generate_schema_reference.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_schema_reference.py` |
| `generate_script_catalog.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_script_catalog.py` |
| `generate_work_history.py` | Documentation generation | read-only | `.\venv\Scripts\python.exe scripts\generate_work_history.py` |
| `import_canlaw_staging.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_canlaw_staging.py --help` |
| `import_fc_decisions.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_fc_decisions.py --help` |
| `import_seed_cases_from_a2aj_api.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\import_seed_cases_from_a2aj_api.py --help` |
| `index_legislation.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\index_legislation.py --help` |
| `ingest_a2aj_api.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_a2aj_api.py --help` |
| `ingest_a2aj_citation_network.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_a2aj_citation_network.py --help` |
| `ingest_a2aj_parquet.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_a2aj_parquet.py --help` |
| `ingest_canlii_seed_cases.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_canlii_seed_cases.py --help` |
| `ingest_hf_fc_activity.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_hf_fc_activity.py --help` |
| `ingest_synthetic_cases.py` | Source acquisition or canonical import | network and/or database writer | `.\venv\Scripts\python.exe scripts\ingest_synthetic_cases.py --help` |
| `llm_tag_candidate_review.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\llm_tag_candidate_review.py --help` |
| `map_fc_seed_to_local_cases.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\map_fc_seed_to_local_cases.py --help` |
| `populate_fc_gold_case_ids.py` | Evaluation artifact maintenance | filesystem writer | `.\venv\Scripts\python.exe scripts\populate_fc_gold_case_ids.py --help` |
| `quick_search_engine.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\quick_search_engine.py --help` |
| `remove_self_case_citations.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\remove_self_case_citations.py --help` |
| `report_a2aj_immigration_selection.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\report_a2aj_immigration_selection.py --help` |
| `resolve_citation_targets.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\resolve_citation_targets.py --help` |
| `resolve_short_citation_targets.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\resolve_short_citation_targets.py --help` |
| `review_tag_candidates.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\review_tag_candidates.py --help` |
| `run_overnight.py` | Orchestration | database/network job runner | `.\venv\Scripts\python.exe scripts\run_overnight.py --list-jobs` |
| `tag_cases.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_cases.py --help` |
| `tag_cases_v2.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_cases_v2.py --help` |
| `tag_prototype_topics.py` | Canonical enrichment or maintenance | database writer unless dry-run is documented | `.\venv\Scripts\python.exe scripts\tag_prototype_topics.py --help` |
| `test_tag_matrix.py` | Utility | inspect implementation before execution | `.\venv\Scripts\python.exe scripts\test_tag_matrix.py --help` |
| `verify_citation_extraction.py` | Evaluation, audit, or build artifact | usually read-only/filesystem output | `.\venv\Scripts\python.exe scripts\verify_citation_extraction.py --help` |
| `verify_fc_case_existence.py` | Source verification | network and filesystem output | `.\venv\Scripts\python.exe scripts\verify_fc_case_existence.py --help` |

## `scripts/adjudicate_fc_metadata.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Metadata adjudication

**Write/network risk:** OpenAI and database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\adjudicate_fc_metadata.py --help
```

## `scripts/audit_fc_metadata_extraction.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\audit_fc_metadata_extraction.py --help
```

## `scripts/backfill_case_metadata_outcomes.py`

**Purpose:** Apply the current metadata and outcome extractor to every case with full text.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\backfill_case_metadata_outcomes.py --help
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

## `scripts/build_core_immigration_set.py`

**Purpose:** Build a deterministic ~300-case immigration prototype set from A2AJ data. This script reads the local A2AJ Federal Court parquet source, applies transparent ranking rules, maps selected citations to local case IDs, and exports a CSV for prototype testing and embedding workflows.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_core_immigration_set.py --help
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

## `scripts/build_prototype_cohort.py`

**Purpose:** Build and operationalize prototype cohort for immigration case research. Pipeline: 1) Combine the 300-case core list with exact-matched seed/canon cases. 2) Embed cohort cases that are not yet embedded. 3) Export citation map edges restricted to cohort-internal citations.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_prototype_cohort.py --help
```

## `scripts/build_tagging_v2_core_candidates.py`

**Purpose:** Build a conservative Tagging V2 core candidate file from the brainstorming draft.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\build_tagging_v2_core_candidates.py --help
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

## `scripts/download_reference_library.py`

**Purpose:** Download a provenance-preserving reference corpus kept separate from cases.

**Operational class:** Reference acquisition

**Write/network risk:** network and filesystem writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\download_reference_library.py --help
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

## `scripts/evaluate_data_quality.py`

**Purpose:** Automated data quality and corpus integrity evaluation script. Audits canonical cases, chunk distributions, citation resolution, statute references, metadata completeness, and graph consistency. Emits structured JSON reports and console markdown summaries.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\evaluate_data_quality.py --help
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

## `scripts/fc_portal_collector.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Federal Court source acquisition

**Write/network risk:** network and filesystem writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\fc_portal_collector.py --help
```

## `scripts/fetch_fc_procedural_history.py`

**Purpose:** Fetch Federal Court procedural history for a list of IMM numbers. Hits two FC API endpoints per IMM number: - proceedingQueriesCourtNumberList → style of cause - proceedingQueriesRE → all DOC_DT / RECORDED_ENTRY events Parses leave decision, JR decision, case status, judge, and full activity text using the same priority-based logic as the VBA original. Results are upserted into the fc_procedural_history table, tagged by IMM number. Input sources (choose one or more): --imm-numbers IMM-1234-19 IMM-5678-20 (space-separated on command line) --imm-file FILE CSV/text file, one IMM per line or 'imm_number' column --from-prototype Pull IMM numbers from prototype cohort (source_id field) Options: --update Re-fetch and overwrite entries that already exist --delay-ms Milliseconds between requests (default 1000) --dry-run Parse and print without writing to DB

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

## `scripts/import_seed_cases_from_a2aj_api.py`

**Purpose:** Import missing seed cases via A2AJ REST API /fetch. Designed for targeted backfill of known citations (not bulk scraping).

**Operational class:** Source acquisition or canonical import

**Write/network risk:** network and/or database writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\import_seed_cases_from_a2aj_api.py --help
```

## `scripts/index_legislation.py`

**Purpose:** Index authoritative Justice Laws XML into section-addressable references.

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

## `scripts/populate_fc_gold_case_ids.py`

**Purpose:** Populate local_case_id in FC gold template from seed-to-case mapping.

**Operational class:** Evaluation artifact maintenance

**Write/network risk:** filesystem writer

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\populate_fc_gold_case_ids.py --help
```

## `scripts/quick_search_engine.py`

**Purpose:** Quick semantic search tester over chunk embeddings. Usage: python -m scripts.quick_search_engine "non-refoulement risk evidence"

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\quick_search_engine.py --help
```

## `scripts/remove_self_case_citations.py`

**Purpose:** Remove false-positive self-case short-form citation rows. Dry-run is the default. Use --apply only after reviewing the reported count.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\remove_self_case_citations.py --help
```

## `scripts/report_a2aj_immigration_selection.py`

**Purpose:** Create a QA report for the immigration-core A2AJ selector output.

**Operational class:** Evaluation, audit, or build artifact

**Write/network risk:** usually read-only/filesystem output

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\report_a2aj_immigration_selection.py --help
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

## `scripts/review_tag_candidates.py`

**Purpose:** Review candidate tags mined from stored decision text without writing to the database.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\review_tag_candidates.py --help
```

## `scripts/run_overnight.py`

**Purpose:** Run resumable case acquisition and corpus maintenance jobs overnight.

**Operational class:** Orchestration

**Write/network risk:** database/network job runner

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\run_overnight.py --list-jobs
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

## `scripts/tag_prototype_topics.py`

**Purpose:** Tag prototype cohort cases with topic-keyword metadata. Writes `topic_keywords` and `topic_scores` into each case metadata_json.

**Operational class:** Canonical enrichment or maintenance

**Write/network risk:** database writer unless dry-run is documented

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\tag_prototype_topics.py --help
```

## `scripts/test_tag_matrix.py`

**Purpose:** No module docstring; inspect this script before use.

**Operational class:** Utility

**Write/network risk:** inspect implementation before execution

**Safe first command**

```powershell
.\venv\Scripts\python.exe scripts\test_tag_matrix.py --help
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
