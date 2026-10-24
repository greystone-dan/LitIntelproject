# Main application database data dictionary

This is a schema-oriented guide to the main application database, not a record-level inventory. Table and column definitions are based on `backend/database.py` and the applicable revisions in `alembic/versions/`; where a migration creates a table that has no ORM model, its columns and purpose are taken from that migration. `backend/models.py` contains API/Pydantic models, not additional persisted tables. The “Pipeline fill” column names the local writer or stage where one is known; `not determined` means the inspected local code did not establish a fill step.

Layers: **canonical** is the main case record; **staging/activity** holds source-specific or procedural inputs apart from that record; **reference** contains authorities or provenance; **derived** contains generated/search-oriented data; **user activity** contains saved searches or workspace state.

## Canonical case records and provenance

### `cases`

Layer: **canonical**

Meaning: One deduplicated decision record used as the central case entity.

Pipeline fill: Source/API ingestion and deduplicating merge in `backend/ingestion.py` (called by `backend/routes.py`); source loaders include `scripts/ingest_a2aj_api.py`, `scripts/ingest_a2aj_parquet.py`, `scripts/ingest_canlii_seed_cases.py`, and `scripts/ingest_synthetic_cases.py`.

| Column | Meaning |
|---|---|
| `id` | record key |
| `title`, `court`, `date` | decision identity |
| `citation`, `docket_number` | citations/filing identifier |
| `summary`, `full_text`, `source_html` | decision content |
| `source_*`, `dataset_version`, `upstream_license`, `scraped_at` | provenance |
| `full_text_hash` | content fingerprint |
| `processing_status` | pipeline state |
| `cases_cited`, `cases_citing`, `citing_cases_count` | citation-list metadata |
| `embedding` | case vector. |

### `case_sources`

Layer: **provenance**

Meaning: One source-specific provenance record associated with a canonical case.

Pipeline fill: Created/updated alongside case merges by `_upsert_source` in `backend/ingestion.py`; migration `alembic/versions/0008_case_provenance_tables.py` backfills legacy provenance from `cases`.

| Column | Meaning |
|---|---|
| `id` | record key |
| `case_id` | canonical case |
| `source_type`, `source_name`, `source_id`, `source_url` | source identity |
| `dataset_version`, `upstream_license`, `scraped_at` | source context |
| `is_primary` | preferred source flag |
| `raw_hash` | source text fingerprint |
| `metadata_json` | source metadata. |

### `ingestion_runs`

Layer: **pipeline activity**

Meaning: A log of one ingestion attempt and its aggregate result counts.

Pipeline fill: Written by ingestion/API flows in `backend/ingestion.py` and `backend/routes.py` (`_build_ingestion_run`).

| Column | Meaning |
|---|---|
| `id` | run key |
| `source_type`, `source_name`, `run_type` | run identity |
| `status`, `started_at`, `finished_at` | lifecycle |
| `records_seen`, `records_ingested`, `records_updated`, `records_failed` | counts |
| `metadata_json` | run details. |


## Case text and derived analysis

### `case_chunks`

Layer: **derived**

Meaning: Text segments prepared for reading, search, citations, and embeddings.

Pipeline fill: `full_case` and heading/paragraph sets are replaced by stages in `backend/case_processing.py`; chunking helpers are in `scripts/chunk_cases.py`.

| Column | Meaning |
|---|---|
| `id` | chunk key |
| `case_id` | parent case |
| `chunk_set` | segmentation type |
| `chunk_index` | order |
| `chunk_label` | heading/label |
| `paragraph_start`, `paragraph_end` | covered paragraph range |
| `text`, `text_hash`, `token_estimate` | content and size |
| `embedding`, `embedding_model` | optional vector and model. |

### `case_chunk_embeddings`

Layer: **derived**

Meaning: Local-model vectors stored separately from the chunk text.

Pipeline fill: `scripts/embed_local_chunks.py`.

| Column | Meaning |
|---|---|
| `id` | vector row key |
| `chunk_id` | source chunk |
| `model_name`, `dimensions` | model identity and vector size |
| `embedding` | vector. |

### `recent_case_chunk_embeddings`

Layer: **derived/index artifact**

Meaning: A refreshed subset of paragraph vectors for the most recent cases.

Pipeline fill: Refresh SQL is part of `alembic/versions/0029_recent_5000_ivfflat_artifact.py`; a separate ongoing refresh step was not determined.

| Column | Meaning |
|---|---|
| `chunk_id` | source chunk and row key |
| `case_id`, `chunk_index`, `paragraph_start`, `paragraph_end`, `chunk_set` | case and paragraph location |
| `text`, `embedding`, `embedding_model` | indexed content/vector |
| `refreshed_at` | refresh time. |

### `case_tags`

Layer: **derived**

Meaning: Occurrences of categorized legal-topic tags with evidence and taxonomy provenance.

Pipeline fill: `tags_v3` stage in `backend/case_processing.py`; the batch backfill is `scripts/backfill_case_tags_v3.py`.

| Column | Meaning |
|---|---|
| `id` | occurrence key |
| `case_id`, `chunk_id` | case and optional chunk |
| `category`, `value` | tag |
| `score`, `evidence`, `offset_start`, `offset_end` | confidence and source text location |
| `rule_id`, `source`, `language`, `evidence_role`, `taxonomy_version` | tagging provenance. |

### `case_tagging_status`

Layer: **derived/status**

Meaning: Records completion and count for one case under a tagging taxonomy version.

Pipeline fill: Written with V3 tag occurrences by `backend/case_processing.py` or the batch backfill `scripts/backfill_case_tags_v3.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `case_id` | case |
| `taxonomy_version` | tagger version |
| `tags_count` | number of tags |
| `tagged_at` | completion time. |

### `case_outcomes`

Layer: **derived**

Meaning: Versioned, evidence-linked classification of a case’s outcome.

Pipeline fill: `outcome` stage in `backend/case_processing.py`; batch generation in `scripts/backfill_case_outcomes.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `case_id` | case |
| `classifier_version` | classifier version |
| `decision_outcome`, `outcome_status` | result and determination state |
| `winner_side`, `loser_side`, `government_role`, `government_outcome` | parties/outcomes |
| `challenged_issue`, `challenged_issues` | issue labels |
| `disposition_evidence`, `evidence_offset_start`, `evidence_offset_end` | evidence |
| `confidence`, `source` | provenance. |

### `case_type_labels`

Layer: **derived**

Meaning: Versioned deterministic label for the type and subtype of a decision.

Pipeline fill: `scripts/classify_case_types.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `case_id` | case |
| `taxonomy_version`, `status` | classifier version and state |
| `primary_type`, `primary_detail`, `secondary_types`, `proceeding` | labels |
| `issues`, `scores`, `evidence`, `confidence` | supporting result. |

### `case_fingerprints`

Layer: **derived**

Meaning: A versioned compact fingerprint of a decision’s terms, authorities, and text shape.

Pipeline fill: `scripts/build_case_fingerprints.py` calls `backend/case_fingerprint_store.py` to compute and store missing or outdated fingerprints.

| Column | Meaning |
|---|---|
| `case_id` | case and row key |
| `version` | fingerprint version |
| `terms`, `authorities`, `role_chars` | feature summaries |
| `text_length` | analyzed text length |
| `computed_at` | build time. |

### `discussion_unit_cache`

Layer: **derived/cache**

Meaning: Versioned cached discussion-unit output and its aggregate counts for a case.

Pipeline fill: Cached results are built and refreshed by `backend/batch_jobs.py`.

| Column | Meaning |
|---|---|
| `id` | cache row key |
| `case_id` | case |
| `method_version` | algorithm version |
| `units_json` | serialized units |
| `total_units`, `total_subthemes` | counts |
| `computed_at`, `updated_at` | cache times. |

### `paragraph_positions`

Layer: **derived**

Meaning: Stores a position-holder label and probability for each numbered paragraph in a decision.

Pipeline fill: `scripts/load_position_tags.py` (paragraph positions may be prepared by `scripts/build_position_tags.py`).

| Column | Meaning |
|---|---|
| `id` | row key |
| `case_id` | case |
| `tagger` | tagging method |
| `paragraph_count` | number of paragraphs |
| `paragraphs` | paragraph-number-to-holder/probability map. |

### `paragraph_notes`

Layer: **derived/editorial layer**

Meaning: A versioned short note attached to one paragraph of a case.

Pipeline fill: `scripts/load_core150_layers.py`.

| Column | Meaning |
|---|---|
| `id` | note key |
| `case_id`, `para` | case and paragraph |
| `version` | note version |
| `note` | text |
| `source` | note provenance. |

### `paragraph_note_links`

Layer: **derived**

Meaning: A scored link between notes on paragraphs considered to address the same point.

Pipeline fill: `scripts/load_note_links.py`.

| Column | Meaning |
|---|---|
| `id` | link key |
| `case_id`, `para` | first case/paragraph |
| `other_case_id`, `other_para` | linked case/paragraph |
| `score` | link score |
| `source` | provenance. |

### `case_frames`

Layer: **derived/editorial layer**

Meaning: A versioned structured summary frame of parties, issues, arguments, and challenged decision elements.

Pipeline fill: `scripts/load_case_frames.py` and `scripts/load_core150_layers.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `case_id` | case |
| `version` | frame version |
| `frame` | structured content |
| `source` | provenance. |

### `issue_maps`

Layer: **derived/editorial layer**

Meaning: A stored issue-level account of an argument and its disposition in a decision.

Pipeline fill: `scripts/load_issue_maps.py` and `scripts/load_core150_layers.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `source_key`, `issue_no` | source identity and issue order |
| `case_id`, `citation`, `court` | linked case details |
| `issue`, `text` | issue and account |
| `result`, `result_para`, `result_paragraph` | disposition and location |
| `applicant_position`, `respondent_position`, `review_flags` | reader additions. |

### `issue_map_questions`

Layer: **derived/editorial layer**

Meaning: A plain-language question associated with one stored issue-map item.

Pipeline fill: `scripts/load_issue_maps.py`.

| Column | Meaning |
|---|---|
| `id` | question key |
| `issue_map_id` | parent issue |
| `position` | display order |
| `question` | question text. |


## Citation and statute references

### `citations`

Layer: **derived/reference links**

Meaning: Extracted citation occurrences from one case, optionally resolved to another case.

Pipeline fill: Citation extraction/rebuild stages in `backend/case_processing.py` and `backend/citations.py`; `scripts/rebuild_citations_controlled.py` provides a batch rebuild.

| Column | Meaning |
|---|---|
| `id` | occurrence key |
| `source_case_id`, `target_case_id` | citing and cited cases |
| `citation_kind` | case/statute/etc. kind |
| `citation_text`, `normalized_citation` | written and normalized reference |
| `anchor_citation_text`, `anchor_offset_start`, `anchor_offset_end` | citation anchor |
| `target_paragraph`, `target_chunk_id` | pinpoint/link location |
| `provenance`, `unresolved` | source and resolution state |
| `chunk_id`, `offset_start`, `offset_end` | occurrence location. |

### `citation_metrics`

Layer: **derived**

Meaning: Per-case aggregate citation-network measures.

Pipeline fill: `scripts/recompute_citation_metrics.py` / `backend/citations.py`.

| Column | Meaning |
|---|---|
| `case_id` | case and row key |
| `in_degree` | incoming citation count |
| `out_degree` | outgoing citation count |
| `pagerank` | network score. |

### `paragraph_citation_edges`

Layer: **derived**

Meaning: Aggregated links from a citing case to a particular paragraph of a cited case.

Pipeline fill: `scripts/build_paragraph_cited_by.py`.

| Column | Meaning |
|---|---|
| `id` | edge key |
| `source_case_id`, `target_case_id` | citing and cited cases |
| `target_paragraph` | cited paragraph |
| `mentions`, `purpose`, `purpose_counts`, `signal` | occurrence and citation-purpose summary |
| `algo_version` | builder version. |

### `paragraph_citation_status`

Layer: **derived/status**

Meaning: Marks a citing case as processed by the paragraph citation aggregation batch.

Pipeline fill: `scripts/build_paragraph_cited_by.py`.

| Column | Meaning |
|---|---|
| `source_case_id` | processed case and row key |
| `algo_version` | builder version |
| `edges` | generated edge count |
| `computed_at` | completion time. |

### `citations_refined`

Layer: **derived**

Meaning: Versioned cleaned/normalized citation occurrences produced by a refinement pass.

Pipeline fill: `scripts/build_refined_citations.py`; target linking is handled by `scripts/link_refined_citations.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `source_case_id`, `target_case_id` | source and optional resolved target |
| `citation_kind`, `citation_text`, `normalized_citation` | citation form |
| `target_paragraph`, `pinpoint`, `pinpoint_kind`, `pinpoint_values` | pinpoint |
| `provenance`, `refine_step`, `refine_version`, `confidence` | refinement metadata |
| `chunk_id`, `offset_start`, `offset_end`, `unresolved` | source location and resolution state. |

### `citation_paragraph_links`

Layer: **derived**

Meaning: Maps a refined citation to a target paragraph and records the link outcome.

Pipeline fill: `not determined` from the inspected local code.

| Column | Meaning |
|---|---|
| `id` | row key |
| `refined_citation_id` | refined citation |
| `target_case_id`, `target_paragraph` | proposed target location |
| `link_status` | link result. |

### `citation_refine_status`

Layer: **derived/status**

Meaning: Records the completion and row counts for refining one case’s citations.

Pipeline fill: `scripts/build_refined_citations.py`.

| Column | Meaning |
|---|---|
| `source_case_id` | processed case and row key |
| `refine_version` | refinement version |
| `status`, `processed_at` | result and time |
| `case_rows`, `statute_rows` | output counts. |

### `statute_references`

Layer: **derived/reference links**

Meaning: Extracted legislation occurrences in a case, with optional pinpoint and statute-version resolution.

Pipeline fill: `statutes` stage in `backend/case_processing.py` using `backend/citations.py`; batch re-extraction in `scripts/reextract_statute_references.py`.

| Column | Meaning |
|---|---|
| `id` | occurrence key |
| `source_case_id`, `chunk_id` | source case and optional chunk |
| `statute_version_id` | linked version |
| `reference_text`, `normalized_reference` | written and normalized citation |
| `instrument_key`, `pinpoint` | instrument and pinpoint |
| `provision_section`, `provision_subsection`, `provision_paragraph` | structured provision |
| `offset_start`, `offset_end`, `reference_kind`, `section_text` | occurrence evidence/type. |

### `statute_references_refined`

Layer: **derived**

Meaning: Versioned refined form of extracted legislation references.

Pipeline fill: `scripts/build_refined_citations.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `source_case_id`, `chunk_id`, `statute_version_id` | source and optional links |
| `reference_text`, `normalized_reference`, `instrument_key`, `pinpoint` | reference identity |
| `provision_section`, `provision_subsection`, `provision_paragraph` | provision parts |
| `refine_step`, `confidence`, `group_start`, `group_end`, `group_index`, `refine_version` | refinement grouping and version. |

### `legislation_documents`

Layer: **reference library**

Meaning: A locally indexed legislation instrument and its source identity.

Pipeline fill: `scripts/index_legislation.py`.

| Column | Meaning |
|---|---|
| `id` | document key |
| `instrument_key` | stable instrument identifier |
| `title`, `citation` | display identity |
| `source_url`, `local_path`, `source_hash` | source and local-copy metadata. |

### `legislation_sections`

Layer: **reference library**

Meaning: A section-level indexed text passage belonging to a legislation document.

Pipeline fill: `scripts/index_legislation.py`.

| Column | Meaning |
|---|---|
| `id` | section key |
| `document_id` | parent instrument |
| `section_number`, `label` | section identity |
| `text` | section text |
| `display_order` | source order. |

### `statutes`

Layer: **reference library**

Meaning: Identity and source metadata for a statute or regulation.

Pipeline fill: `scripts/import_statutes.py` (historical source loader: `scripts/import_historical_statutes.py`).

| Column | Meaning |
|---|---|
| `id` | statute key |
| `instrument_key` | stable identifier |
| `title`, `short_title` | names |
| `jurisdiction`, `statute_type` | legal scope/type |
| `consolidated_year` | consolidation year |
| `source`, `source_url`, `license` | provenance. |

### `statute_versions`

Layer: **reference library**

Meaning: A dated in-force text version of a statute.

Pipeline fill: `scripts/import_statutes.py` and `scripts/import_historical_statutes.py`.

| Column | Meaning |
|---|---|
| `id` | version key |
| `statute_id` | parent instrument |
| `version_number` | source version label |
| `in_force_date`, `end_date` | effective period |
| `full_text`, `text_compressed` | text representations |
| `source_url`, `fetched_at` | retrieval provenance. |

### `statute_sections`

Layer: **reference library**

Meaning: A parsed section, subsection, or paragraph of one statute version.

Pipeline fill: `scripts/import_statutes.py` (and historical imports in `scripts/import_historical_statutes.py`).

| Column | Meaning |
|---|---|
| `id` | section key |
| `statute_version_id` | parent version |
| `section_number`, `subsection`, `paragraph` | provision address |
| `heading`, `text` | content |
| `offset_start`, `offset_end` | source-text range. |


## Source-specific staging and court activity

### `a2aj_cases`

Layer: **staging/reference**

Meaning: A2AJ-sourced case identity and citation-network metadata kept apart from canonical cases.

Pipeline fill: `scripts/ingest_a2aj_parquet.py` and `scripts/ingest_a2aj_api.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `a2aj_case_id` | upstream identity |
| `neutral_citation`, `court`, `decision_date` | case details |
| `cases_cited`, `cases_citing`, `citing_cases_count` | upstream citation summary. |

### `a2aj_citation_edges`

Layer: **staging/derived**

Meaning: An upstream A2AJ citation edge before or alongside local case resolution.

Pipeline fill: `scripts/ingest_a2aj_citation_network.py`.

| Column | Meaning |
|---|---|
| `id` | edge key |
| `source_a2aj_case_id`, `target_a2aj_case_id` | upstream cases |
| `normalized_citation` | normalized target reference. |

### `a2aj_case_map`

Layer: **staging/link**

Meaning: Links an upstream A2AJ case identity to its canonical local case.

Pipeline fill: A2AJ matching/linking in `backend/citations.py`; the importers are `scripts/ingest_a2aj_parquet.py` and `scripts/ingest_a2aj_api.py`.

| Column | Meaning |
|---|---|
| `a2aj_case_id` | upstream case and row key |
| `local_case_id` | canonical `cases.id`. |

### `fc_procedural_history`

Layer: **court activity**

Meaning: Stored Federal Court immigration procedural history keyed by immigration file number.

Pipeline fill: `scripts/fetch_fc_procedural_history.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `imm_number` | file identity |
| `style_of_cause`, `judge` | case/judge details |
| `leave_decision`, `leave_date`, `jr_decision`, `jr_decision_date` | procedural results |
| `case_status`, `latest_activity_date`, `full_activity_text`, `entries_json` | activity state and record |
| `conflict_flag`, `fetched_at` | data quality and fetch time. |

### `fc_activity_cases`

Layer: **court activity staging**

Meaning: One source-specific Federal Court activity file record, independent of the canonical decision record.

Pipeline fill: Imported by `scripts/ingest_hf_fc_activity.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `source_key` | stable source identity |
| `citation`, `year`, `case_name`, `date_filed` | file details |
| `nature`, `case_class`, `track` | case descriptors |
| `source_url`, `source_type`, `source_name`, `source_id`, `scraped_timestamp` | provenance |
| `raw_payload` | source record. |

### `fc_activity_documents`

Layer: **court activity staging**

Meaning: One source activity/document entry attached to an activity file.

Pipeline fill: Imported by `scripts/ingest_hf_fc_activity.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `case_id` | parent activity case |
| `re_no`, `docno` | entry identifiers |
| `doc_dt`, `recorded_entry` | date and text |
| `entry_hash`, `raw_document` | deduplication and source payload. |

### `fc_activity_classifications`

Layer: **court activity derived**

Meaning: Versioned classification output for a Federal Court activity file.

Pipeline fill: `scripts/classify_fc_activity.py`.

| Column | Meaning |
|---|---|
| `id` | row key |
| `source_case_id`, `source_key`, `imm_number` | source identifiers |
| `classification_json` | structured classification |
| `classifier_version`, `classified_at`, `updated_at` | generation provenance. |

### `fc_activity_motions`

Layer: **court activity derived**

Meaning: One classified motion with its filing party, ruling, and timing details.

Pipeline fill: `scripts/classify_fc_activity.py`.

| Column | Meaning |
|---|---|
| `id` | motion key |
| `source_case_id` | parent file |
| `position`, `motion_type`, `filer`, `outcome` | motion identity/result |
| `judge_key`, `judge_name` | deciding judge |
| `filed_date`, `decision_date`, `days_to_decision` | timing |
| `in_writing`, `relief` | decision details. |

### `fc_activity_summaries`

Layer: **court activity derived**

Meaning: A flattened classification summary for one activity file for aggregate queries.

Pipeline fill: `scripts/classify_fc_activity.py`.

| Column | Meaning |
|---|---|
| `source_case_id` | parent file and row key |
| `imm_number`, `classifier_version`, `year`, `city_filed` | identity/version |
| `resolution`, `lifecycle`, `leave_result`, `review_result` | outcomes |
| judge/counsel fields | people involved |
| timing, hearing, representation, motion, and filing fields | derived case characteristics |
| `updated_at` | refresh time. |

### `fc_activity_alerts`

Layer: **court activity/user activity**

Meaning: Records that a saved-search alert matched a Federal Court activity file.

Pipeline fill: `not determined` from the inspected local code.

| Column | Meaning |
|---|---|
| `id` | alert key |
| `search_id` | saved search |
| `case_id` | activity file |
| `entry_type` | matched event type |
| `discovered_at`, `created_at` | alert times. |


## Judges and additional authority links

### `judge_profiles`

Layer: **reference**

Meaning: A normalized judge identity used to associate decisions and name variants.

Pipeline fill: `scripts/backfill_judge_profiles.py`.

| Column | Meaning |
|---|---|
| `id` | profile key |
| `slug`, `display_name`, `normalized_name` | profile identity |
| `primary_court` | main court |
| `aliases` | known names |
| `created_at`, `updated_at` | record times. |

### `case_judge_profiles`

Layer: **derived/link**

Meaning: Links a canonical case to a judge profile while retaining the name found in the source.

Pipeline fill: `scripts/backfill_judge_profiles.py`.

| Column | Meaning |
|---|---|
| `id` | link key |
| `case_id` | decision |
| `judge_profile_id` | judge |
| `raw_name` | original extracted name. |

### `judge_profile_aliases`

Layer: **reference/link**

Meaning: Maps a duplicate judge profile to the selected canonical profile.

Pipeline fill: `scripts/apply_judge_aliases.py`.

| Column | Meaning |
|---|---|
| `id` | mapping key |
| `alias_profile_id` | duplicate profile |
| `canonical_profile_id` | retained profile |
| `source` | mapping method |
| `created_at` | mapping time. |


## Search and user workspace

### `saved_searches`

Layer: **user activity**

Meaning: A user-saved query, search mode, and filters.

Pipeline fill: Created/updated through the saved-search API in `backend/routes.py`.

| Column | Meaning |
|---|---|
| `id` | search key |
| `name`, `description` | display text |
| `query`, `search_mode`, `filters` | saved criteria |
| `created_at`, `updated_at`, `last_alert_check` | lifecycle. |

### `search_alerts`

Layer: **user activity/derived**

Meaning: A case or chunk discovered as a match for a saved search.

Pipeline fill: `scripts/check_saved_searches.py` writes matches; `backend/routes.py` provides saved-search management and reads alerts.

| Column | Meaning |
|---|---|
| `id` | alert key |
| `search_id` | saved query |
| `case_id`, `chunk_id` | matched record/location |
| `match_type`, `relevance_score` | match details |
| `discovered_at`, `created_at` | alert times. |

### `workbench_cases`

Layer: **user activity**

Meaning: A demo analyst’s tracked Federal Court immigration file and last-seen activity snapshot.

Pipeline fill: Workbench API flows in `backend/workbench.py`.

| Column | Meaning |
|---|---|
| `id` | workspace row |
| `owner`, `imm_number` | user/file identity |
| `label`, `notes`, `tags`, `folder` | analyst organization |
| `deadline`, `deadline_label` | reminder |
| `last_seen_entries`, `last_seen_activity_date`, `last_seen_status`, `last_viewed_at` | tracked snapshot. |

### `workbench_pins`

Layer: **user activity**

Meaning: A canonical library decision saved to a demo analyst’s workspace.

Pipeline fill: Workbench API flows in `backend/workbench.py`.

| Column | Meaning |
|---|---|
| `id` | pin key |
| `owner`, `case_id` | user and canonical case |
| `notes`, `tags`, `folder` | analyst organization |
| `pinned_at` | save time. |


## Contextual authority experiment tables

These tables are declared by `alembic/versions/0026_contextual_authority_phase0.py` but have no mapped ORM classes in `backend/database.py`; they remain part of the migrated application database schema. Their runtime writers were not found in the inspected `backend/` or `scripts/` Python sources.

### `contextual_snapshot`

Layer: **derived/experiment control**

Meaning: Identifies a run and configuration for a contextual-authority snapshot.

Created by `alembic/versions/0026_contextual_authority_phase0.py`. Runtime fill: `not determined`.

| Column | Meaning |
|---|---|
| `id` | snapshot key |
| `status` | lifecycle |
| `code_sha`, `method_set_version` | code/method versions |
| `config`, `cohort_hash` | settings and input cohort identity |
| `started_at`, `completed_at` | run times. |

### `contextual_active_snapshot`

Layer: **derived/experiment control**

Meaning: Selects the active contextual snapshot through a singleton row.

Created by `alembic/versions/0026_contextual_authority_phase0.py`. Runtime fill: `not determined`.

| Column | Meaning |
|---|---|
| `singleton` | fixed singleton key |
| `snapshot_id` | selected snapshot. |

### `contextual_unit`

Layer: **derived/experiment**

Meaning: Represents one method/version-specific analysis unit for one case in a snapshot.

Created by `alembic/versions/0026_contextual_authority_phase0.py`. Runtime fill: `not determined`.

| Column | Meaning |
|---|---|
| `id` | unit key |
| `snapshot_id`, `case_id` | run and case |
| `method`, `method_version` | analysis identity |
| `config_hash`, `variant_key`, `text_sha256` | configuration, variant, and input identity. |

### `contextual_unit_segment`

Layer: **derived/experiment**

Meaning: Locates an ordered text segment within a contextual analysis unit.

Created by `alembic/versions/0026_contextual_authority_phase0.py`. Runtime fill: `not determined`.

| Column | Meaning |
|---|---|
| `unit_id`, `ordinal` | unit and segment order |
| `chunk_id` | source chunk |
| `start_offset`, `end_offset` | text range |
| `text_sha256` | segment fingerprint. |

### `contextual_unit_citation`

Layer: **derived/experiment link**

Meaning: Associates citation occurrences with a contextual analysis unit.

Created by `alembic/versions/0026_contextual_authority_phase0.py`. Runtime fill: `not determined`.

| Column | Meaning |
|---|---|
| `unit_id`, `citation_occurrence_id` | unit and citation |
| `membership_role` | relationship. |

### `contextual_observation`

Layer: **derived/experiment**

Meaning: Stores a contextual-authority label or observation and its confidence/provenance.

Created by `alembic/versions/0026_contextual_authority_phase0.py`. Runtime fill: `not determined`.

| Column | Meaning |
|---|---|
| `id` | observation key |
| `snapshot_id`, `unit_id`, `citation_occurrence_id`, `target_authority_id` | run, unit, citation, and optional target |
| `kind`, `label`, `provenance_class`, `method_version` | result identity |
| `evidence_strength`, `rule_agreement`, `model_score`, `confidence_tier`, `review_status` | support and review state. |

### `contextual_evidence_span`

Layer: **derived/experiment evidence**

Meaning: Points to the source text supporting a contextual observation.

Created by `alembic/versions/0026_contextual_authority_phase0.py`. Runtime fill: `not determined`.

| Column | Meaning |
|---|---|
| `observation_id`, `ordinal` | observation and evidence order |
| `chunk_id` | source chunk |
| `start_offset`, `end_offset` | evidence range |
| `text_sha256`, `quoted` | integrity and quote flag. |

### `contextual_review`

Layer: **review activity**

Meaning: Records a reviewer’s decision and rationale for an observation.

Created by `alembic/versions/0026_contextual_authority_phase0.py`. Runtime fill: `not determined`.

| Column | Meaning |
|---|---|
| `id` | review key |
| `observation_id` | reviewed observation |
| `reviewer_id` | reviewer identifier |
| `decision`, `corrected_label`, `rationale` | review result |
| `reviewed_at` | review time. |
