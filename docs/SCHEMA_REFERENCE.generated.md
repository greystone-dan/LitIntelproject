# Generated Database Schema Reference

This file is generated from `backend.database.Base.metadata` by `scripts/generate_schema_reference.py`. Do not edit it manually.

Generated: 2026-10-07T08:58:58.080664+00:00
Tables: 43

The reference documents the ORM schema declared in this repository. Apply Alembic migrations for deployment changes; use database inspection as the final authority for an already-running environment.

## Entity Relationship Diagram

```mermaid
erDiagram
    a2aj_case_map {
        TEXT a2aj_case_id PK FK
        Integer local_case_id  FK
    }
    a2aj_cases {
        Integer id PK
        TEXT a2aj_case_id
        TEXT neutral_citation
        TEXT court
        DATE decision_date
        JSON cases_cited
        JSON cases_citing
        Integer citing_cases_count
    }
    a2aj_citation_edges {
        Integer id PK
        TEXT source_a2aj_case_id
        TEXT target_a2aj_case_id
        TEXT normalized_citation
    }
    case_chunk_embeddings {
        Integer id PK
        Integer chunk_id  FK
        String(255) model_name
        Integer dimensions
        VECTOR(1024) embedding
        DATETIME created_at
    }
    case_chunks {
        Integer id PK
        Integer case_id  FK
        String(50) chunk_set
        Integer chunk_index
        String(255) chunk_label
        Integer paragraph_start
        Integer paragraph_end
        TEXT text
        String(64) text_hash
        Integer token_estimate
        VECTOR(1536) embedding
        String(100) embedding_model
        DATETIME created_at
    }
    case_fingerprints {
        Integer case_id PK FK
        String(20) version
        JSON terms
        JSON authorities
        JSON role_chars
        Integer text_length
        DATETIME computed_at
    }
    case_judge_profiles {
        Integer id PK
        Integer case_id  FK
        Integer judge_profile_id  FK
        String(255) raw_name
        DATETIME created_at
    }
    case_outcomes {
        Integer id PK
        Integer case_id  FK
        String(100) classifier_version
        String(50) decision_outcome
        String(30) outcome_status
        String(30) winner_side
        String(30) loser_side
        String(30) government_role
        String(30) government_outcome
        String(100) challenged_issue
        JSON challenged_issues
        TEXT disposition_evidence
        Integer evidence_offset_start
        Integer evidence_offset_end
        FLOAT confidence
        String(50) source
        DATETIME created_at
        DATETIME updated_at
    }
    case_sources {
        Integer id PK
        Integer case_id  FK
        String(100) source_type
        String(255) source_name
        String(255) source_id
        String(2048) source_url
        String(100) dataset_version
        TEXT upstream_license
        DATETIME scraped_at
        BOOLEAN is_primary
        String(64) raw_hash
        JSON metadata_json
        DATETIME created_at
        DATETIME updated_at
    }
    case_tagging_status {
        Integer id PK
        Integer case_id  FK
        String(100) taxonomy_version
        Integer tags_count
        DATETIME tagged_at
    }
    case_tags {
        Integer id PK
        Integer case_id  FK
        Integer chunk_id  FK
        String(100) category
        String(255) value
        FLOAT score
        TEXT evidence
        Integer offset_start
        Integer offset_end
        String(150) rule_id
        String(16) language
        String(30) evidence_role
        String(50) source
        String(100) taxonomy_version
        DATETIME created_at
    }
    case_type_labels {
        Integer id PK
        Integer case_id  FK
        String(50) taxonomy_version
        String(30) status
        String(80) primary_type
        String(80) primary_detail
        JSON secondary_types
        String(80) second_type
        String(80) second_detail
        String(60) proceeding
        JSON issues
        FLOAT confidence
        JSON scores
        JSON evidence
        DATETIME created_at
    }
    cases {
        Integer id PK
        String(255) title
        String(255) court
        String(100) jurisdiction
        DATE date
        String(255) citation
        String(255) docket_number
        String(255) secondary_citation
        TEXT summary
        TEXT full_text
        TEXT source_html
        JSON issues
        JSON metadata_json
        String(2048) source_url
        String(255) source_name
        String(255) source_id
        String(100) source_type
        String(100) dataset_version
        TEXT upstream_license
        DATETIME scraped_at
        String(10) language
        String(64) full_text_hash
        String(30) processing_status
        JSON cases_cited
        JSON cases_citing
        Integer citing_cases_count
        VECTOR(1536) embedding
        DATETIME created_at
    }
    citation_metrics {
        Integer case_id PK FK
        Integer in_degree
        Integer out_degree
        FLOAT pagerank
    }
    citation_paragraph_links {
        Integer id PK
        Integer refined_citation_id  FK
        Integer target_case_id
        Integer target_paragraph
        String(50) link_status
    }
    citation_refine_status {
        Integer source_case_id PK
        Integer refine_version
        String(50) status
        DATETIME processed_at
        Integer case_rows
        Integer statute_rows
    }
    citations {
        Integer id PK
        Integer source_case_id  FK
        Integer target_case_id  FK
        String(20) citation_kind
        TEXT citation_text
        TEXT normalized_citation
        TEXT anchor_citation_text
        Integer anchor_offset_start
        Integer anchor_offset_end
        String(255) declared_alias
        Integer target_paragraph
        Integer target_chunk_id  FK
        String(20) provenance
        Integer chunk_id  FK
        Integer offset_start
        Integer offset_end
        BOOLEAN unresolved
    }
    citations_refined {
        Integer id PK
        Integer source_case_id  FK
        Integer target_case_id  FK
        String(20) citation_kind
        TEXT citation_text
        TEXT normalized_citation
        TEXT anchor_citation_text
        Integer anchor_offset_start
        Integer anchor_offset_end
        String(255) declared_alias
        Integer target_paragraph
        Integer target_chunk_id  FK
        String(20) provenance
        Integer chunk_id  FK
        Integer offset_start
        Integer offset_end
        BOOLEAN unresolved
        String(50) refine_step
        FLOAT confidence
        Integer refine_version
        Integer source_citation_id
    }
    discussion_unit_cache {
        Integer id PK
        Integer case_id  FK
        String(100) method_version
        TEXT units_json
        Integer total_units
        Integer total_subthemes
        DATETIME computed_at
        DATETIME updated_at
    }
    fc_activity_alerts {
        Integer id PK
        Integer search_id  FK
        Integer case_id  FK
        String(100) entry_type
        DATETIME discovered_at
        DATETIME created_at
    }
    fc_activity_cases {
        Integer id PK
        String(255) source_key
        String(255) citation
        Integer year
        TEXT case_name
        DATE date_filed
        String(255) city_filed
        TEXT nature
        String(120) case_class
        String(120) track
        String(2048) source_url
        String(100) source_type
        String(255) source_name
        String(255) source_id
        DATETIME scraped_timestamp
        JSON raw_payload
        DATETIME created_at
        DATETIME updated_at
    }
    fc_activity_classifications {
        Integer id PK
        Integer source_case_id  FK
        String(255) source_key
        String(255) imm_number
        Integer year
        TEXT case_name
        DATE date_filed
        String(255) city_filed
        TEXT nature
        String(120) case_class
        String(120) track
        String(2048) source_url
        String(100) source_type
        String(255) source_name
        String(255) source_id
        DATETIME scraped_timestamp
        JSON classification_json
        String(80) classifier_version
        DATETIME classified_at
        DATETIME updated_at
    }
    fc_activity_documents {
        Integer id PK
        Integer case_id  FK
        String(50) re_no
        String(120) docno
        DATE doc_dt
        TEXT recorded_entry
        String(64) entry_hash
        JSON raw_document
        DATETIME created_at
    }
    fc_activity_motions {
        Integer id PK
        Integer source_case_id  FK
        String(255) imm_number
        Integer year
        String(255) city_filed
        Integer position
        String(60) motion_type
        String(40) filer
        String(60) outcome
        String(60) link
        String(120) judge_key
        String(255) judge_name
        DATE filed_date
        DATE decision_date
        Integer days_to_decision
        BOOLEAN in_writing
        TEXT relief
    }
    fc_activity_summaries {
        Integer source_case_id PK FK
        String(255) imm_number
        String(80) classifier_version
        Integer year
        String(255) city_filed
        String(80) resolution
        String(40) lifecycle
        String(40) leave_result
        String(40) review_result
        String(40) decision_body
        String(120) leave_judge_key
        String(255) leave_judge_name
        String(120) merits_judge_key
        String(255) merits_judge_name
        String(160) applicant_counsel_key
        String(255) applicant_counsel_name
        String(40) representation
        String(40) respondent_position
        String(40) leave_refusal_reason
        String(40) stay_status
        String(40) hearing_mode
        Integer hearing_minutes
        String(40) appeal_status
        String(60) certified_question
        String(40) consent_status
        String(40) reasons_at_filing
        String(20) proceeding_language
        String(40) lead_file
        String(80) lead_resolution
        String(80) application_type
        String(80) office_location
        BOOLEAN joint_applicants
        Integer motions_filed
        String(40) extension_of_time
        BOOLEAN dormant
        Integer days_decision_to_filing
        String(40) filing_timeliness
        String(40) record_timeliness
        String(40) memorandum_timeliness
        String(40) hearing_window
        Integer days_filing_to_perfection
        Integer days_filing_to_leave_decision
        Integer days_leave_grant_to_hearing
        Integer days_hearing_to_judgment
        Integer days_filing_to_final_disposition
        BOOLEAN judgment_from_bench
        DATETIME updated_at
    }
    fc_procedural_history {
        Integer id PK
        String(50) imm_number
        TEXT style_of_cause
        String(120) judge
        String(30) leave_decision
        DATE leave_date
        String(40) jr_decision
        DATE jr_decision_date
        String(40) case_status
        DATE latest_activity_date
        TEXT full_activity_text
        JSON entries_json
        BOOLEAN conflict_flag
        DATETIME fetched_at
    }
    ingestion_runs {
        Integer id PK
        String(100) source_type
        String(255) source_name
        String(50) run_type
        String(30) status
        DATETIME started_at
        DATETIME finished_at
        Integer records_seen
        Integer records_ingested
        Integer records_updated
        Integer records_failed
        JSON metadata_json
    }
    judge_profile_aliases {
        Integer id PK
        Integer alias_profile_id  FK
        Integer canonical_profile_id  FK
        String(30) source
        DATETIME created_at
    }
    judge_profiles {
        Integer id PK
        String(255) slug
        String(255) display_name
        String(255) normalized_name
        String(255) primary_court
        JSON aliases
        DATETIME created_at
        DATETIME updated_at
    }
    legislation_documents {
        Integer id PK
        String(100) instrument_key
        TEXT title
        TEXT citation
        TEXT source_url
        TEXT local_path
        String(64) source_hash
    }
    legislation_sections {
        Integer id PK
        Integer document_id  FK
        String(100) section_number
        TEXT label
        TEXT text
        Integer display_order
    }
    paragraph_citation_edges {
        Integer id PK
        Integer source_case_id  FK
        Integer target_case_id  FK
        Integer target_paragraph
        Integer mentions
        String(20) purpose
        JSON purpose_counts
        String(60) signal
        Integer algo_version
    }
    paragraph_citation_status {
        Integer source_case_id PK FK
        Integer algo_version
        Integer edges
        DATETIME computed_at
    }
    recent_case_chunk_embeddings {
        Integer chunk_id PK FK
        Integer case_id  FK
        Integer chunk_index
        Integer paragraph_start
        Integer paragraph_end
        String(50) chunk_set
        TEXT text
        VECTOR(1536) embedding
        String(100) embedding_model
        DATETIME refreshed_at
    }
    saved_searches {
        Integer id PK
        String(255) name
        TEXT description
        TEXT query
        String(20) search_mode
        JSON filters
        DATETIME created_at
        DATETIME updated_at
        DATETIME last_alert_check
    }
    search_alerts {
        Integer id PK
        Integer search_id  FK
        Integer case_id  FK
        Integer chunk_id  FK
        String(50) match_type
        FLOAT relevance_score
        DATETIME discovered_at
        DATETIME created_at
    }
    statute_references {
        Integer id PK
        Integer source_case_id  FK
        Integer chunk_id  FK
        Integer statute_version_id  FK
        Integer offset_start
        Integer offset_end
        TEXT reference_text
        TEXT normalized_reference
        String(100) instrument_key
        String(255) pinpoint
        String(50) provision_section
        String(50) provision_subsection
        String(50) provision_paragraph
        Integer provision_nested_depth
        BOOLEAN provision_is_range_or_list
        TEXT legislation_url
        TEXT section_text
        String(20) reference_kind
    }
    statute_references_refined {
        Integer id PK
        Integer source_case_id  FK
        Integer chunk_id  FK
        Integer statute_version_id  FK
        Integer offset_start
        Integer offset_end
        TEXT reference_text
        TEXT normalized_reference
        String(100) instrument_key
        String(255) pinpoint
        String(50) provision_section
        String(50) provision_subsection
        String(50) provision_paragraph
        Integer provision_nested_depth
        BOOLEAN provision_is_range_or_list
        TEXT legislation_url
        TEXT section_text
        String(20) reference_kind
        String(50) refine_step
        FLOAT confidence
        Integer group_start
        Integer group_end
        Integer group_index
        Integer refine_version
    }
    statute_sections {
        Integer id PK
        Integer statute_version_id  FK
        String(50) section_number
        String(50) subsection
        String(50) paragraph
        TEXT heading
        TEXT text
        Integer offset_start
        Integer offset_end
        DATETIME created_at
    }
    statute_versions {
        Integer id PK
        Integer statute_id  FK
        String(50) version_number
        DATE in_force_date
        DATE end_date
        TEXT full_text
        BLOB text_compressed
        TEXT source_url
        DATETIME fetched_at
        DATETIME created_at
    }
    statutes {
        Integer id PK
        String(100) instrument_key
        TEXT title
        String(255) short_title
        String(100) jurisdiction
        String(50) statute_type
        Integer consolidated_year
        String(100) source
        TEXT source_url
        String(100) license
        DATETIME created_at
        DATETIME updated_at
    }
    workbench_cases {
        Integer id PK
        String(80) owner
        String(50) imm_number
        String(255) label
        TEXT notes
        JSON tags
        String(80) folder
        DATE deadline
        String(120) deadline_label
        Integer last_seen_entries
        DATE last_seen_activity_date
        String(80) last_seen_status
        DATETIME last_viewed_at
        DATETIME added_at
    }
    workbench_pins {
        Integer id PK
        String(80) owner
        Integer case_id  FK
        TEXT notes
        JSON tags
        String(80) folder
        DATETIME pinned_at
    }
    a2aj_cases ||--o{ a2aj_case_map : "a2aj_case_id"
    cases ||--o{ a2aj_case_map : "local_case_id"
    case_chunks ||--o{ case_chunk_embeddings : "chunk_id"
    cases ||--o{ case_chunks : "case_id"
    cases ||--o{ case_fingerprints : "case_id"
    cases ||--o{ case_judge_profiles : "case_id"
    judge_profiles ||--o{ case_judge_profiles : "judge_profile_id"
    cases ||--o{ case_outcomes : "case_id"
    cases ||--o{ case_sources : "case_id"
    cases ||--o{ case_tagging_status : "case_id"
    cases ||--o{ case_tags : "case_id"
    case_chunks ||--o{ case_tags : "chunk_id"
    cases ||--o{ case_type_labels : "case_id"
    cases ||--o{ citation_metrics : "case_id"
    citations_refined ||--o{ citation_paragraph_links : "refined_citation_id"
    case_chunks ||--o{ citations : "chunk_id"
    cases ||--o{ citations : "source_case_id"
    cases ||--o{ citations : "target_case_id"
    case_chunks ||--o{ citations : "target_chunk_id"
    case_chunks ||--o{ citations_refined : "chunk_id"
    cases ||--o{ citations_refined : "source_case_id"
    cases ||--o{ citations_refined : "target_case_id"
    case_chunks ||--o{ citations_refined : "target_chunk_id"
    cases ||--o{ discussion_unit_cache : "case_id"
    fc_activity_cases ||--o{ fc_activity_alerts : "case_id"
    saved_searches ||--o{ fc_activity_alerts : "search_id"
    fc_activity_cases ||--o{ fc_activity_classifications : "source_case_id"
    fc_activity_cases ||--o{ fc_activity_documents : "case_id"
    fc_activity_cases ||--o{ fc_activity_motions : "source_case_id"
    fc_activity_cases ||--o{ fc_activity_summaries : "source_case_id"
    judge_profiles ||--o{ judge_profile_aliases : "alias_profile_id"
    judge_profiles ||--o{ judge_profile_aliases : "canonical_profile_id"
    legislation_documents ||--o{ legislation_sections : "document_id"
    cases ||--o{ paragraph_citation_edges : "source_case_id"
    cases ||--o{ paragraph_citation_edges : "target_case_id"
    cases ||--o{ paragraph_citation_status : "source_case_id"
    cases ||--o{ recent_case_chunk_embeddings : "case_id"
    case_chunks ||--o{ recent_case_chunk_embeddings : "chunk_id"
    cases ||--o{ search_alerts : "case_id"
    case_chunks ||--o{ search_alerts : "chunk_id"
    saved_searches ||--o{ search_alerts : "search_id"
    case_chunks ||--o{ statute_references : "chunk_id"
    cases ||--o{ statute_references : "source_case_id"
    statute_versions ||--o{ statute_references : "statute_version_id"
    case_chunks ||--o{ statute_references_refined : "chunk_id"
    cases ||--o{ statute_references_refined : "source_case_id"
    statute_versions ||--o{ statute_references_refined : "statute_version_id"
    statute_versions ||--o{ statute_sections : "statute_version_id"
    statutes ||--o{ statute_versions : "statute_id"
    cases ||--o{ workbench_pins : "case_id"
```

## Table Summary

| Table | Columns | Primary key |
| --- | ---: | --- |
| `a2aj_case_map` | 2 | `a2aj_case_id` |
| `a2aj_cases` | 8 | `id` |
| `a2aj_citation_edges` | 4 | `id` |
| `case_chunk_embeddings` | 6 | `id` |
| `case_chunks` | 13 | `id` |
| `case_fingerprints` | 7 | `case_id` |
| `case_judge_profiles` | 5 | `id` |
| `case_outcomes` | 18 | `id` |
| `case_sources` | 14 | `id` |
| `case_tagging_status` | 5 | `id` |
| `case_tags` | 15 | `id` |
| `case_type_labels` | 15 | `id` |
| `cases` | 28 | `id` |
| `citation_metrics` | 4 | `case_id` |
| `citation_paragraph_links` | 5 | `id` |
| `citation_refine_status` | 6 | `source_case_id` |
| `citations` | 17 | `id` |
| `citations_refined` | 21 | `id` |
| `discussion_unit_cache` | 8 | `id` |
| `fc_activity_alerts` | 6 | `id` |
| `fc_activity_cases` | 18 | `id` |
| `fc_activity_classifications` | 20 | `id` |
| `fc_activity_documents` | 9 | `id` |
| `fc_activity_motions` | 17 | `id` |
| `fc_activity_summaries` | 47 | `source_case_id` |
| `fc_procedural_history` | 14 | `id` |
| `ingestion_runs` | 12 | `id` |
| `judge_profile_aliases` | 5 | `id` |
| `judge_profiles` | 8 | `id` |
| `legislation_documents` | 7 | `id` |
| `legislation_sections` | 6 | `id` |
| `paragraph_citation_edges` | 9 | `id` |
| `paragraph_citation_status` | 4 | `source_case_id` |
| `recent_case_chunk_embeddings` | 10 | `chunk_id` |
| `saved_searches` | 9 | `id` |
| `search_alerts` | 8 | `id` |
| `statute_references` | 18 | `id` |
| `statute_references_refined` | 24 | `id` |
| `statute_sections` | 10 | `id` |
| `statute_versions` | 10 | `id` |
| `statutes` | 12 | `id` |
| `workbench_cases` | 14 | `id` |
| `workbench_pins` | 7 | `id` |

## `a2aj_case_map`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `a2aj_case_id` | `TEXT` | no | PK; FK -> a2aj_cases.a2aj_case_id; NOT NULL |
| `local_case_id` | `Integer` | no | FK -> cases.id; NOT NULL |

### Indexes

- `ix_a2aj_case_map_local_case_id`: index on `local_case_id`

### Foreign Keys

- `a2aj_case_id` -> `a2aj_cases.a2aj_case_id`; on delete `CASCADE`
- `local_case_id` -> `cases.id`; on delete `CASCADE`

## `a2aj_cases`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `a2aj_case_id` | `TEXT` | no | NOT NULL |
| `neutral_citation` | `TEXT` | yes | - |
| `court` | `TEXT` | yes | - |
| `decision_date` | `DATE` | yes | - |
| `cases_cited` | `JSON` | yes | - |
| `cases_citing` | `JSON` | yes | - |
| `citing_cases_count` | `Integer` | yes | - |

### Indexes

- `ix_a2aj_cases_a2aj_case_id`: unique index on `a2aj_case_id`
- `ix_a2aj_cases_decision_date`: index on `decision_date`
- `ix_a2aj_cases_neutral_citation`: index on `neutral_citation`

## `a2aj_citation_edges`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_a2aj_case_id` | `TEXT` | no | NOT NULL |
| `target_a2aj_case_id` | `TEXT` | yes | - |
| `normalized_citation` | `TEXT` | yes | - |

### Indexes

- `ix_a2aj_citation_edges_normalized_citation`: index on `normalized_citation`
- `ix_a2aj_citation_edges_source_a2aj_case_id`: index on `source_a2aj_case_id`
- `ix_a2aj_citation_edges_target_a2aj_case_id`: index on `target_a2aj_case_id`

## `case_chunk_embeddings`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `chunk_id` | `Integer` | no | FK -> case_chunks.id; NOT NULL |
| `model_name` | `String(255)` | no | NOT NULL |
| `dimensions` | `Integer` | no | NOT NULL |
| `embedding` | `VECTOR(1024)` | no | NOT NULL |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_chunk_embeddings_chunk_id`: index on `chunk_id`
- `ix_case_chunk_embeddings_model_name`: index on `model_name`

### Unique Constraints

- `uq_chunk_embedding_model`: `chunk_id`, `model_name`

### Foreign Keys

- `chunk_id` -> `case_chunks.id`; on delete `CASCADE`

## `case_chunks`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `chunk_set` | `String(50)` | no | NOT NULL; default=legacy |
| `chunk_index` | `Integer` | no | NOT NULL |
| `chunk_label` | `String(255)` | yes | - |
| `paragraph_start` | `Integer` | yes | - |
| `paragraph_end` | `Integer` | yes | - |
| `text` | `TEXT` | no | NOT NULL |
| `text_hash` | `String(64)` | no | NOT NULL |
| `token_estimate` | `Integer` | no | NOT NULL |
| `embedding` | `VECTOR(1536)` | yes | - |
| `embedding_model` | `String(100)` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_chunks_case_id`: index on `case_id`
- `ix_case_chunks_chunk_set`: index on `chunk_set`
- `ix_case_chunks_text_hash`: index on `text_hash`
- `ix_similarity_paragraph`: index on `case_id`, `chunk_set`, `paragraph_start`, `id`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`

## `case_fingerprints`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `case_id` | `Integer` | no | PK; FK -> cases.id; NOT NULL |
| `version` | `String(20)` | no | NOT NULL |
| `terms` | `JSON` | no | NOT NULL |
| `authorities` | `JSON` | no | NOT NULL |
| `role_chars` | `JSON` | yes | - |
| `text_length` | `Integer` | no | NOT NULL; default=0 |
| `computed_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_fingerprints_version`: index on `version`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`

## `case_judge_profiles`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `judge_profile_id` | `Integer` | no | FK -> judge_profiles.id; NOT NULL |
| `raw_name` | `String(255)` | no | NOT NULL |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_judge_profiles_case_id`: index on `case_id`
- `ix_case_judge_profiles_judge_profile_id`: index on `judge_profile_id`

### Unique Constraints

- `uq_case_judge_profile`: `case_id`, `judge_profile_id`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`
- `judge_profile_id` -> `judge_profiles.id`; on delete `CASCADE`

## `case_outcomes`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `classifier_version` | `String(100)` | no | NOT NULL |
| `decision_outcome` | `String(50)` | yes | - |
| `outcome_status` | `String(30)` | no | NOT NULL; default=undetermined |
| `winner_side` | `String(30)` | yes | - |
| `loser_side` | `String(30)` | yes | - |
| `government_role` | `String(30)` | yes | - |
| `government_outcome` | `String(30)` | yes | - |
| `challenged_issue` | `String(100)` | yes | - |
| `challenged_issues` | `JSON` | yes | - |
| `disposition_evidence` | `TEXT` | yes | - |
| `evidence_offset_start` | `Integer` | yes | - |
| `evidence_offset_end` | `Integer` | yes | - |
| `confidence` | `FLOAT` | no | NOT NULL; default=0 |
| `source` | `String(50)` | no | NOT NULL; default=deterministic_outcome |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_outcomes_case_id`: index on `case_id`
- `ix_case_outcomes_challenged_issue`: index on `challenged_issue`
- `ix_case_outcomes_classifier_version`: index on `classifier_version`
- `ix_case_outcomes_decision_outcome`: index on `decision_outcome`
- `ix_case_outcomes_government_outcome`: index on `government_outcome`
- `ix_case_outcomes_government_role`: index on `government_role`
- `ix_case_outcomes_loser_side`: index on `loser_side`
- `ix_case_outcomes_outcome_status`: index on `outcome_status`
- `ix_case_outcomes_winner_side`: index on `winner_side`

### Unique Constraints

- `uq_case_outcome_version`: `case_id`, `classifier_version`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`

## `case_sources`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `source_type` | `String(100)` | no | NOT NULL |
| `source_name` | `String(255)` | yes | - |
| `source_id` | `String(255)` | yes | - |
| `source_url` | `String(2048)` | yes | - |
| `dataset_version` | `String(100)` | yes | - |
| `upstream_license` | `TEXT` | yes | - |
| `scraped_at` | `DATETIME` | yes | - |
| `is_primary` | `BOOLEAN` | no | NOT NULL; default=False |
| `raw_hash` | `String(64)` | yes | - |
| `metadata_json` | `JSON` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_sources_case_id`: index on `case_id`
- `ix_case_sources_raw_hash`: index on `raw_hash`
- `ix_case_sources_source_type`: index on `source_type`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`

## `case_tagging_status`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `taxonomy_version` | `String(100)` | no | NOT NULL |
| `tags_count` | `Integer` | no | NOT NULL |
| `tagged_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_tagging_status_case_id`: index on `case_id`
- `ix_case_tagging_status_taxonomy_version`: index on `taxonomy_version`

### Unique Constraints

- `uq_case_tagging_status`: `case_id`, `taxonomy_version`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`

## `case_tags`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `category` | `String(100)` | no | NOT NULL |
| `value` | `String(255)` | no | NOT NULL |
| `score` | `FLOAT` | no | NOT NULL |
| `evidence` | `TEXT` | no | NOT NULL |
| `offset_start` | `Integer` | yes | - |
| `offset_end` | `Integer` | yes | - |
| `rule_id` | `String(150)` | yes | - |
| `language` | `String(16)` | no | NOT NULL; default=unknown |
| `evidence_role` | `String(30)` | no | NOT NULL; default=mention |
| `source` | `String(50)` | no | NOT NULL |
| `taxonomy_version` | `String(100)` | no | NOT NULL |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_tags_case_id`: index on `case_id`
- `ix_case_tags_category`: index on `category`
- `ix_case_tags_chunk_id`: index on `chunk_id`
- `ix_case_tags_evidence_role`: index on `evidence_role`
- `ix_case_tags_language`: index on `language`
- `ix_case_tags_rule_id`: index on `rule_id`
- `ix_case_tags_source`: index on `source`
- `ix_case_tags_taxonomy_version`: index on `taxonomy_version`
- `ix_case_tags_value`: index on `value`
- `ix_similarity_tag_posting`: index on `taxonomy_version`, `category`, `value`, `case_id`, `id`
- `ix_similarity_tag_source`: index on `case_id`, `taxonomy_version`, `id`

### Unique Constraints

- `uq_case_tag_taxonomy`: `case_id`, `category`, `value`, `offset_start`, `offset_end`, `taxonomy_version`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`
- `chunk_id` -> `case_chunks.id`; on delete `SET NULL`

## `case_type_labels`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `taxonomy_version` | `String(50)` | no | NOT NULL |
| `status` | `String(30)` | no | NOT NULL |
| `primary_type` | `String(80)` | yes | - |
| `primary_detail` | `String(80)` | yes | - |
| `secondary_types` | `JSON` | yes | - |
| `second_type` | `String(80)` | yes | - |
| `second_detail` | `String(80)` | yes | - |
| `proceeding` | `String(60)` | yes | - |
| `issues` | `JSON` | yes | - |
| `confidence` | `FLOAT` | no | NOT NULL; default=0 |
| `scores` | `JSON` | yes | - |
| `evidence` | `JSON` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_case_type_labels_case_id`: index on `case_id`
- `ix_case_type_labels_primary_type`: index on `primary_type`
- `ix_case_type_labels_status`: index on `status`
- `ix_case_type_labels_taxonomy_version`: index on `taxonomy_version`

### Unique Constraints

- `uq_case_type_label_version`: `case_id`, `taxonomy_version`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`

## `cases`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `title` | `String(255)` | no | NOT NULL |
| `court` | `String(255)` | no | NOT NULL |
| `jurisdiction` | `String(100)` | yes | - |
| `date` | `DATE` | no | NOT NULL |
| `citation` | `String(255)` | yes | - |
| `docket_number` | `String(255)` | yes | - |
| `secondary_citation` | `String(255)` | yes | - |
| `summary` | `TEXT` | yes | - |
| `full_text` | `TEXT` | yes | - |
| `source_html` | `TEXT` | yes | - |
| `issues` | `JSON` | yes | - |
| `metadata_json` | `JSON` | yes | - |
| `source_url` | `String(2048)` | yes | - |
| `source_name` | `String(255)` | yes | - |
| `source_id` | `String(255)` | yes | - |
| `source_type` | `String(100)` | yes | - |
| `dataset_version` | `String(100)` | yes | - |
| `upstream_license` | `TEXT` | yes | - |
| `scraped_at` | `DATETIME` | yes | - |
| `language` | `String(10)` | yes | - |
| `full_text_hash` | `String(64)` | yes | - |
| `processing_status` | `String(30)` | no | NOT NULL; default=raw |
| `cases_cited` | `JSON` | yes | - |
| `cases_citing` | `JSON` | yes | - |
| `citing_cases_count` | `Integer` | yes | - |
| `embedding` | `VECTOR(1536)` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_cases_citation`: index on `citation`
- `ix_cases_court`: index on `court`
- `ix_cases_date`: index on `date`
- `ix_cases_docket_number`: index on `docket_number`
- `ix_cases_full_text_hash`: index on `full_text_hash`
- `ix_cases_jurisdiction`: index on `jurisdiction`
- `ix_cases_processing_status`: index on `processing_status`
- `ix_cases_source_id`: index on `source_id`
- `ix_cases_title`: index on `title`

## `citation_metrics`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `case_id` | `Integer` | no | PK; FK -> cases.id; NOT NULL |
| `in_degree` | `Integer` | yes | - |
| `out_degree` | `Integer` | yes | - |
| `pagerank` | `FLOAT` | yes | - |

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`

## `citation_paragraph_links`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `refined_citation_id` | `Integer` | no | FK -> citations_refined.id; NOT NULL |
| `target_case_id` | `Integer` | yes | - |
| `target_paragraph` | `Integer` | no | NOT NULL |
| `link_status` | `String(50)` | no | NOT NULL |

### Foreign Keys

- `refined_citation_id` -> `citations_refined.id`; on delete `CASCADE`

## `citation_refine_status`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `source_case_id` | `Integer` | no | PK; NOT NULL |
| `refine_version` | `Integer` | no | NOT NULL |
| `status` | `String(50)` | no | NOT NULL |
| `processed_at` | `DATETIME` | yes | - |
| `case_rows` | `Integer` | no | NOT NULL |
| `statute_rows` | `Integer` | no | NOT NULL |

## `citations`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `target_case_id` | `Integer` | yes | FK -> cases.id |
| `citation_kind` | `String(20)` | no | NOT NULL; default=unknown |
| `citation_text` | `TEXT` | yes | - |
| `normalized_citation` | `TEXT` | yes | - |
| `anchor_citation_text` | `TEXT` | yes | - |
| `anchor_offset_start` | `Integer` | yes | - |
| `anchor_offset_end` | `Integer` | yes | - |
| `declared_alias` | `String(255)` | yes | - |
| `target_paragraph` | `Integer` | yes | - |
| `target_chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `provenance` | `String(20)` | no | NOT NULL; default=local |
| `chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `offset_start` | `Integer` | yes | - |
| `offset_end` | `Integer` | yes | - |
| `unresolved` | `BOOLEAN` | no | NOT NULL; default=False |

### Indexes

- `ix_citations_chunk_id`: index on `chunk_id`
- `ix_citations_citation_kind`: index on `citation_kind`
- `ix_citations_normalized_citation`: index on `normalized_citation`
- `ix_citations_provenance`: index on `provenance`
- `ix_citations_source_case_id`: index on `source_case_id`
- `ix_citations_target_case_id`: index on `target_case_id`
- `ix_citations_target_chunk_id`: index on `target_chunk_id`
- `ix_citations_target_paragraph`: index on `target_paragraph`
- `ix_similarity_authority_posting`: index on `target_case_id`, `source_case_id`, `id`
- `ix_similarity_citation_source`: index on `source_case_id`, `id`
- `ix_similarity_unresolved_posting`: index on `normalized_citation`, `source_case_id`, `id`

### Foreign Keys

- `chunk_id` -> `case_chunks.id`; on delete `SET NULL`
- `source_case_id` -> `cases.id`; on delete `CASCADE`
- `target_case_id` -> `cases.id`; on delete `CASCADE`
- `target_chunk_id` -> `case_chunks.id`; on delete `SET NULL`

## `citations_refined`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `target_case_id` | `Integer` | yes | FK -> cases.id |
| `citation_kind` | `String(20)` | no | NOT NULL; default=unknown |
| `citation_text` | `TEXT` | yes | - |
| `normalized_citation` | `TEXT` | yes | - |
| `anchor_citation_text` | `TEXT` | yes | - |
| `anchor_offset_start` | `Integer` | yes | - |
| `anchor_offset_end` | `Integer` | yes | - |
| `declared_alias` | `String(255)` | yes | - |
| `target_paragraph` | `Integer` | yes | - |
| `target_chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `provenance` | `String(20)` | no | NOT NULL; default=local |
| `chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `offset_start` | `Integer` | yes | - |
| `offset_end` | `Integer` | yes | - |
| `unresolved` | `BOOLEAN` | no | NOT NULL; default=False |
| `refine_step` | `String(50)` | yes | - |
| `confidence` | `FLOAT` | yes | - |
| `refine_version` | `Integer` | no | NOT NULL |
| `source_citation_id` | `Integer` | yes | - |

### Indexes

- `ix_citations_refined_source_case_id`: index on `source_case_id`

### Foreign Keys

- `chunk_id` -> `case_chunks.id`; on delete `SET NULL`
- `source_case_id` -> `cases.id`; on delete `CASCADE`
- `target_case_id` -> `cases.id`; on delete `CASCADE`
- `target_chunk_id` -> `case_chunks.id`; on delete `SET NULL`

## `discussion_unit_cache`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `method_version` | `String(100)` | no | NOT NULL |
| `units_json` | `TEXT` | no | NOT NULL |
| `total_units` | `Integer` | no | NOT NULL; default=0 |
| `total_subthemes` | `Integer` | no | NOT NULL; default=0 |
| `computed_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_discussion_unit_cache_case_id`: index on `case_id`
- `ix_discussion_unit_cache_method_version`: index on `method_version`

### Unique Constraints

- `uq_discussion_unit_cache_version`: `case_id`, `method_version`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`

## `fc_activity_alerts`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `search_id` | `Integer` | no | FK -> saved_searches.id; NOT NULL |
| `case_id` | `Integer` | no | FK -> fc_activity_cases.id; NOT NULL |
| `entry_type` | `String(100)` | no | NOT NULL |
| `discovered_at` | `DATETIME` | no | NOT NULL; default=now() |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_fc_activity_alerts_case_id`: index on `case_id`
- `ix_fc_activity_alerts_discovered_at`: index on `discovered_at`
- `ix_fc_activity_alerts_search_id`: index on `search_id`

### Foreign Keys

- `case_id` -> `fc_activity_cases.id`; on delete `CASCADE`
- `search_id` -> `saved_searches.id`; on delete `CASCADE`

## `fc_activity_cases`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_key` | `String(255)` | no | NOT NULL |
| `citation` | `String(255)` | yes | - |
| `year` | `Integer` | yes | - |
| `case_name` | `TEXT` | yes | - |
| `date_filed` | `DATE` | yes | - |
| `city_filed` | `String(255)` | yes | - |
| `nature` | `TEXT` | yes | - |
| `case_class` | `String(120)` | yes | - |
| `track` | `String(120)` | yes | - |
| `source_url` | `String(2048)` | yes | - |
| `source_type` | `String(100)` | yes | - |
| `source_name` | `String(255)` | yes | - |
| `source_id` | `String(255)` | yes | - |
| `scraped_timestamp` | `DATETIME` | yes | - |
| `raw_payload` | `JSON` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_fc_activity_cases_citation`: index on `citation`
- `ix_fc_activity_cases_date_filed`: index on `date_filed`
- `ix_fc_activity_cases_source_id`: index on `source_id`
- `ix_fc_activity_cases_source_key`: unique index on `source_key`
- `ix_fc_activity_cases_source_name`: index on `source_name`
- `ix_fc_activity_cases_source_type`: index on `source_type`
- `ix_fc_activity_cases_year`: index on `year`

### Unique Constraints

- `uq_fc_activity_case_citation`: `citation`
- `uq_fc_activity_case_source_key`: `source_key`

## `fc_activity_classifications`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_case_id` | `Integer` | no | FK -> fc_activity_cases.id; NOT NULL |
| `source_key` | `String(255)` | no | NOT NULL |
| `imm_number` | `String(255)` | yes | - |
| `year` | `Integer` | yes | - |
| `case_name` | `TEXT` | yes | - |
| `date_filed` | `DATE` | yes | - |
| `city_filed` | `String(255)` | yes | - |
| `nature` | `TEXT` | yes | - |
| `case_class` | `String(120)` | yes | - |
| `track` | `String(120)` | yes | - |
| `source_url` | `String(2048)` | yes | - |
| `source_type` | `String(100)` | yes | - |
| `source_name` | `String(255)` | yes | - |
| `source_id` | `String(255)` | yes | - |
| `scraped_timestamp` | `DATETIME` | yes | - |
| `classification_json` | `JSON` | no | NOT NULL |
| `classifier_version` | `String(80)` | no | NOT NULL |
| `classified_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_fc_activity_classifications_date_filed`: index on `date_filed`
- `ix_fc_activity_classifications_imm_number`: index on `imm_number`
- `ix_fc_activity_classifications_source_case_id`: unique index on `source_case_id`
- `ix_fc_activity_classifications_source_id`: index on `source_id`
- `ix_fc_activity_classifications_source_key`: index on `source_key`
- `ix_fc_activity_classifications_source_name`: index on `source_name`
- `ix_fc_activity_classifications_source_type`: index on `source_type`
- `ix_fc_activity_classifications_year`: index on `year`

### Foreign Keys

- `source_case_id` -> `fc_activity_cases.id`; on delete `CASCADE`

## `fc_activity_documents`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `case_id` | `Integer` | no | FK -> fc_activity_cases.id; NOT NULL |
| `re_no` | `String(50)` | yes | - |
| `docno` | `String(120)` | yes | - |
| `doc_dt` | `DATE` | yes | - |
| `recorded_entry` | `TEXT` | yes | - |
| `entry_hash` | `String(64)` | yes | - |
| `raw_document` | `JSON` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_fc_activity_documents_case_id`: index on `case_id`
- `ix_fc_activity_documents_doc_dt`: index on `doc_dt`
- `ix_fc_activity_documents_docno`: index on `docno`
- `ix_fc_activity_documents_entry_hash`: index on `entry_hash`
- `ix_fc_activity_documents_re_no`: index on `re_no`

### Unique Constraints

- `uq_fc_activity_document_fallback`: `case_id`, `re_no`, `docno`, `entry_hash`
- `uq_fc_activity_document_identity`: `case_id`, `re_no`, `docno`

### Foreign Keys

- `case_id` -> `fc_activity_cases.id`; on delete `CASCADE`

## `fc_activity_motions`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_case_id` | `Integer` | no | FK -> fc_activity_cases.id; NOT NULL |
| `imm_number` | `String(255)` | yes | - |
| `year` | `Integer` | yes | - |
| `city_filed` | `String(255)` | yes | - |
| `position` | `Integer` | no | NOT NULL |
| `motion_type` | `String(60)` | no | NOT NULL |
| `filer` | `String(40)` | yes | - |
| `outcome` | `String(60)` | no | NOT NULL |
| `link` | `String(60)` | yes | - |
| `judge_key` | `String(120)` | yes | - |
| `judge_name` | `String(255)` | yes | - |
| `filed_date` | `DATE` | yes | - |
| `decision_date` | `DATE` | yes | - |
| `days_to_decision` | `Integer` | yes | - |
| `in_writing` | `BOOLEAN` | yes | - |
| `relief` | `TEXT` | yes | - |

### Indexes

- `ix_fc_activity_motions_imm_number`: index on `imm_number`
- `ix_fc_activity_motions_judge_key`: index on `judge_key`
- `ix_fc_activity_motions_motion_type`: index on `motion_type`
- `ix_fc_activity_motions_outcome`: index on `outcome`
- `ix_fc_activity_motions_source_case_id`: index on `source_case_id`
- `ix_fc_activity_motions_year`: index on `year`

### Foreign Keys

- `source_case_id` -> `fc_activity_cases.id`; on delete `CASCADE`

## `fc_activity_summaries`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `source_case_id` | `Integer` | no | PK; FK -> fc_activity_cases.id; NOT NULL |
| `imm_number` | `String(255)` | yes | - |
| `classifier_version` | `String(80)` | no | NOT NULL |
| `year` | `Integer` | yes | - |
| `city_filed` | `String(255)` | yes | - |
| `resolution` | `String(80)` | yes | - |
| `lifecycle` | `String(40)` | yes | - |
| `leave_result` | `String(40)` | yes | - |
| `review_result` | `String(40)` | yes | - |
| `decision_body` | `String(40)` | yes | - |
| `leave_judge_key` | `String(120)` | yes | - |
| `leave_judge_name` | `String(255)` | yes | - |
| `merits_judge_key` | `String(120)` | yes | - |
| `merits_judge_name` | `String(255)` | yes | - |
| `applicant_counsel_key` | `String(160)` | yes | - |
| `applicant_counsel_name` | `String(255)` | yes | - |
| `representation` | `String(40)` | yes | - |
| `respondent_position` | `String(40)` | yes | - |
| `leave_refusal_reason` | `String(40)` | yes | - |
| `stay_status` | `String(40)` | yes | - |
| `hearing_mode` | `String(40)` | yes | - |
| `hearing_minutes` | `Integer` | yes | - |
| `appeal_status` | `String(40)` | yes | - |
| `certified_question` | `String(60)` | yes | - |
| `consent_status` | `String(40)` | yes | - |
| `reasons_at_filing` | `String(40)` | yes | - |
| `proceeding_language` | `String(20)` | yes | - |
| `lead_file` | `String(40)` | yes | - |
| `lead_resolution` | `String(80)` | yes | - |
| `application_type` | `String(80)` | yes | - |
| `office_location` | `String(80)` | yes | - |
| `joint_applicants` | `BOOLEAN` | yes | - |
| `motions_filed` | `Integer` | yes | - |
| `extension_of_time` | `String(40)` | yes | - |
| `dormant` | `BOOLEAN` | yes | - |
| `days_decision_to_filing` | `Integer` | yes | - |
| `filing_timeliness` | `String(40)` | yes | - |
| `record_timeliness` | `String(40)` | yes | - |
| `memorandum_timeliness` | `String(40)` | yes | - |
| `hearing_window` | `String(40)` | yes | - |
| `days_filing_to_perfection` | `Integer` | yes | - |
| `days_filing_to_leave_decision` | `Integer` | yes | - |
| `days_leave_grant_to_hearing` | `Integer` | yes | - |
| `days_hearing_to_judgment` | `Integer` | yes | - |
| `days_filing_to_final_disposition` | `Integer` | yes | - |
| `judgment_from_bench` | `BOOLEAN` | yes | - |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_fc_activity_summaries_applicant_counsel_key`: index on `applicant_counsel_key`
- `ix_fc_activity_summaries_city_filed`: index on `city_filed`
- `ix_fc_activity_summaries_decision_body`: index on `decision_body`
- `ix_fc_activity_summaries_imm_number`: index on `imm_number`
- `ix_fc_activity_summaries_leave_judge_key`: index on `leave_judge_key`
- `ix_fc_activity_summaries_merits_judge_key`: index on `merits_judge_key`
- `ix_fc_activity_summaries_office_location`: index on `office_location`
- `ix_fc_activity_summaries_resolution`: index on `resolution`
- `ix_fc_activity_summaries_year`: index on `year`

### Foreign Keys

- `source_case_id` -> `fc_activity_cases.id`; on delete `CASCADE`

## `fc_procedural_history`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `imm_number` | `String(50)` | no | NOT NULL |
| `style_of_cause` | `TEXT` | yes | - |
| `judge` | `String(120)` | yes | - |
| `leave_decision` | `String(30)` | yes | - |
| `leave_date` | `DATE` | yes | - |
| `jr_decision` | `String(40)` | yes | - |
| `jr_decision_date` | `DATE` | yes | - |
| `case_status` | `String(40)` | yes | - |
| `latest_activity_date` | `DATE` | yes | - |
| `full_activity_text` | `TEXT` | yes | - |
| `entries_json` | `JSON` | yes | - |
| `conflict_flag` | `BOOLEAN` | no | NOT NULL; default=False |
| `fetched_at` | `DATETIME` | yes | - |

### Indexes

- `ix_fc_procedural_history_case_status`: index on `case_status`
- `ix_fc_procedural_history_imm_number`: unique index on `imm_number`
- `ix_fc_procedural_history_leave_decision`: index on `leave_decision`

## `ingestion_runs`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_type` | `String(100)` | no | NOT NULL |
| `source_name` | `String(255)` | yes | - |
| `run_type` | `String(50)` | no | NOT NULL |
| `status` | `String(30)` | no | NOT NULL; default=started |
| `started_at` | `DATETIME` | no | NOT NULL; default=now() |
| `finished_at` | `DATETIME` | yes | - |
| `records_seen` | `Integer` | yes | - |
| `records_ingested` | `Integer` | yes | - |
| `records_updated` | `Integer` | yes | - |
| `records_failed` | `Integer` | yes | - |
| `metadata_json` | `JSON` | yes | - |

### Indexes

- `ix_ingestion_runs_run_type`: index on `run_type`
- `ix_ingestion_runs_source_type`: index on `source_type`
- `ix_ingestion_runs_status`: index on `status`

## `judge_profile_aliases`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `alias_profile_id` | `Integer` | no | FK -> judge_profiles.id; NOT NULL |
| `canonical_profile_id` | `Integer` | no | FK -> judge_profiles.id; NOT NULL |
| `source` | `String(30)` | no | NOT NULL; default=rule |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_judge_profile_aliases_canonical_profile_id`: index on `canonical_profile_id`

### Unique Constraints

- `unnamed`: `alias_profile_id`

### Foreign Keys

- `alias_profile_id` -> `judge_profiles.id`; on delete `CASCADE`
- `canonical_profile_id` -> `judge_profiles.id`; on delete `CASCADE`

## `judge_profiles`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `slug` | `String(255)` | no | NOT NULL |
| `display_name` | `String(255)` | no | NOT NULL |
| `normalized_name` | `String(255)` | no | NOT NULL |
| `primary_court` | `String(255)` | yes | - |
| `aliases` | `JSON` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_judge_profiles_normalized_name`: unique index on `normalized_name`
- `ix_judge_profiles_primary_court`: index on `primary_court`
- `ix_judge_profiles_slug`: unique index on `slug`

## `legislation_documents`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `instrument_key` | `String(100)` | no | NOT NULL |
| `title` | `TEXT` | no | NOT NULL |
| `citation` | `TEXT` | yes | - |
| `source_url` | `TEXT` | yes | - |
| `local_path` | `TEXT` | yes | - |
| `source_hash` | `String(64)` | yes | - |

### Indexes

- `ix_legislation_documents_instrument_key`: unique index on `instrument_key`

## `legislation_sections`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `document_id` | `Integer` | no | FK -> legislation_documents.id; NOT NULL |
| `section_number` | `String(100)` | no | NOT NULL |
| `label` | `TEXT` | yes | - |
| `text` | `TEXT` | no | NOT NULL |
| `display_order` | `Integer` | no | NOT NULL |

### Indexes

- `ix_legislation_sections_document_id`: index on `document_id`
- `ix_legislation_sections_section_number`: index on `section_number`

### Foreign Keys

- `document_id` -> `legislation_documents.id`; on delete `CASCADE`

## `paragraph_citation_edges`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `target_case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `target_paragraph` | `Integer` | no | NOT NULL |
| `mentions` | `Integer` | no | NOT NULL; default=1 |
| `purpose` | `String(20)` | no | NOT NULL; default=mentioned |
| `purpose_counts` | `JSON` | yes | - |
| `signal` | `String(60)` | yes | - |
| `algo_version` | `Integer` | no | NOT NULL; default=1 |

### Indexes

- `ix_paragraph_citation_target`: index on `target_case_id`, `target_paragraph`

### Unique Constraints

- `uq_paragraph_citation_edge`: `source_case_id`, `target_case_id`, `target_paragraph`

### Foreign Keys

- `source_case_id` -> `cases.id`; on delete `CASCADE`
- `target_case_id` -> `cases.id`; on delete `CASCADE`

## `paragraph_citation_status`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `source_case_id` | `Integer` | no | PK; FK -> cases.id; NOT NULL |
| `algo_version` | `Integer` | no | NOT NULL |
| `edges` | `Integer` | no | NOT NULL; default=0 |
| `computed_at` | `DATETIME` | no | NOT NULL; default=now() |

### Foreign Keys

- `source_case_id` -> `cases.id`; on delete `CASCADE`

## `recent_case_chunk_embeddings`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `chunk_id` | `Integer` | no | PK; FK -> case_chunks.id; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `chunk_index` | `Integer` | no | NOT NULL |
| `paragraph_start` | `Integer` | yes | - |
| `paragraph_end` | `Integer` | yes | - |
| `chunk_set` | `String(50)` | no | NOT NULL; default=paragraph |
| `text` | `TEXT` | no | NOT NULL |
| `embedding` | `VECTOR(1536)` | no | NOT NULL |
| `embedding_model` | `String(100)` | no | NOT NULL |
| `refreshed_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_recent_case_chunk_embeddings_case_id`: index on `case_id`
- `ix_recent_case_chunk_embeddings_embedding_model`: index on `embedding_model`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`
- `chunk_id` -> `case_chunks.id`; on delete `CASCADE`

## `saved_searches`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `name` | `String(255)` | no | NOT NULL |
| `description` | `TEXT` | yes | - |
| `query` | `TEXT` | no | NOT NULL |
| `search_mode` | `String(20)` | no | NOT NULL; default=semantic |
| `filters` | `JSON` | no | NOT NULL |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |
| `last_alert_check` | `DATETIME` | yes | - |

### Indexes

- `ix_saved_searches_created_at`: index on `created_at`
- `ix_saved_searches_name`: index on `name`

## `search_alerts`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `search_id` | `Integer` | no | FK -> saved_searches.id; NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `match_type` | `String(50)` | no | NOT NULL |
| `relevance_score` | `FLOAT` | yes | - |
| `discovered_at` | `DATETIME` | no | NOT NULL; default=now() |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_search_alerts_case_id`: index on `case_id`
- `ix_search_alerts_discovered_at`: index on `discovered_at`
- `ix_search_alerts_search_id`: index on `search_id`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`
- `chunk_id` -> `case_chunks.id`; on delete `CASCADE`
- `search_id` -> `saved_searches.id`; on delete `CASCADE`

## `statute_references`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `statute_version_id` | `Integer` | yes | FK -> statute_versions.id |
| `offset_start` | `Integer` | yes | - |
| `offset_end` | `Integer` | yes | - |
| `reference_text` | `TEXT` | yes | - |
| `normalized_reference` | `TEXT` | yes | - |
| `instrument_key` | `String(100)` | yes | - |
| `pinpoint` | `String(255)` | yes | - |
| `provision_section` | `String(50)` | yes | - |
| `provision_subsection` | `String(50)` | yes | - |
| `provision_paragraph` | `String(50)` | yes | - |
| `provision_nested_depth` | `Integer` | yes | - |
| `provision_is_range_or_list` | `BOOLEAN` | no | NOT NULL; default=False |
| `legislation_url` | `TEXT` | yes | - |
| `section_text` | `TEXT` | yes | - |
| `reference_kind` | `String(20)` | no | NOT NULL |

### Indexes

- `ix_statute_references_chunk_id`: index on `chunk_id`
- `ix_statute_references_instrument_key`: index on `instrument_key`
- `ix_statute_references_normalized_reference`: index on `normalized_reference`
- `ix_statute_references_pinpoint`: index on `pinpoint`
- `ix_statute_references_provision_is_range_or_list`: index on `provision_is_range_or_list`
- `ix_statute_references_provision_paragraph`: index on `provision_paragraph`
- `ix_statute_references_provision_section`: index on `provision_section`
- `ix_statute_references_provision_subsection`: index on `provision_subsection`
- `ix_statute_references_reference_kind`: index on `reference_kind`
- `ix_statute_references_source_case_id`: index on `source_case_id`
- `ix_statute_references_statute_version_id`: index on `statute_version_id`

### Foreign Keys

- `chunk_id` -> `case_chunks.id`; on delete `SET NULL`
- `source_case_id` -> `cases.id`; on delete `CASCADE`
- `statute_version_id` -> `statute_versions.id`; on delete `SET NULL`

## `statute_references_refined`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `statute_version_id` | `Integer` | yes | FK -> statute_versions.id |
| `offset_start` | `Integer` | yes | - |
| `offset_end` | `Integer` | yes | - |
| `reference_text` | `TEXT` | yes | - |
| `normalized_reference` | `TEXT` | yes | - |
| `instrument_key` | `String(100)` | yes | - |
| `pinpoint` | `String(255)` | yes | - |
| `provision_section` | `String(50)` | yes | - |
| `provision_subsection` | `String(50)` | yes | - |
| `provision_paragraph` | `String(50)` | yes | - |
| `provision_nested_depth` | `Integer` | yes | - |
| `provision_is_range_or_list` | `BOOLEAN` | no | NOT NULL; default=False |
| `legislation_url` | `TEXT` | yes | - |
| `section_text` | `TEXT` | yes | - |
| `reference_kind` | `String(20)` | no | NOT NULL |
| `refine_step` | `String(50)` | yes | - |
| `confidence` | `FLOAT` | yes | - |
| `group_start` | `Integer` | yes | - |
| `group_end` | `Integer` | yes | - |
| `group_index` | `Integer` | yes | - |
| `refine_version` | `Integer` | no | NOT NULL |

### Indexes

- `ix_statute_references_refined_source_case_id`: index on `source_case_id`

### Foreign Keys

- `chunk_id` -> `case_chunks.id`; on delete `SET NULL`
- `source_case_id` -> `cases.id`; on delete `CASCADE`
- `statute_version_id` -> `statute_versions.id`; on delete `SET NULL`

## `statute_sections`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `statute_version_id` | `Integer` | no | FK -> statute_versions.id; NOT NULL |
| `section_number` | `String(50)` | no | NOT NULL |
| `subsection` | `String(50)` | yes | - |
| `paragraph` | `String(50)` | yes | - |
| `heading` | `TEXT` | yes | - |
| `text` | `TEXT` | yes | - |
| `offset_start` | `Integer` | yes | - |
| `offset_end` | `Integer` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_statute_sections_statute_version_id`: index on `statute_version_id`

### Foreign Keys

- `statute_version_id` -> `statute_versions.id`; on delete `CASCADE`

## `statute_versions`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `statute_id` | `Integer` | no | FK -> statutes.id; NOT NULL |
| `version_number` | `String(50)` | no | NOT NULL |
| `in_force_date` | `DATE` | no | NOT NULL |
| `end_date` | `DATE` | yes | - |
| `full_text` | `TEXT` | yes | - |
| `text_compressed` | `BLOB` | yes | - |
| `source_url` | `TEXT` | yes | - |
| `fetched_at` | `DATETIME` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_statute_versions_in_force_date`: index on `in_force_date`
- `ix_statute_versions_statute_id`: index on `statute_id`

### Unique Constraints

- `uq_statute_version_date`: `statute_id`, `in_force_date`

### Foreign Keys

- `statute_id` -> `statutes.id`; on delete `CASCADE`

## `statutes`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `instrument_key` | `String(100)` | no | NOT NULL |
| `title` | `TEXT` | no | NOT NULL |
| `short_title` | `String(255)` | yes | - |
| `jurisdiction` | `String(100)` | no | NOT NULL |
| `statute_type` | `String(50)` | no | NOT NULL |
| `consolidated_year` | `Integer` | yes | - |
| `source` | `String(100)` | no | NOT NULL |
| `source_url` | `TEXT` | yes | - |
| `license` | `String(100)` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_statutes_instrument_key`: unique index on `instrument_key`
- `ix_statutes_jurisdiction`: index on `jurisdiction`
- `ix_statutes_source`: index on `source`

## `workbench_cases`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `owner` | `String(80)` | no | NOT NULL |
| `imm_number` | `String(50)` | no | NOT NULL |
| `label` | `String(255)` | yes | - |
| `notes` | `TEXT` | yes | - |
| `tags` | `JSON` | yes | - |
| `folder` | `String(80)` | yes | - |
| `deadline` | `DATE` | yes | - |
| `deadline_label` | `String(120)` | yes | - |
| `last_seen_entries` | `Integer` | no | NOT NULL; default=0 |
| `last_seen_activity_date` | `DATE` | yes | - |
| `last_seen_status` | `String(80)` | yes | - |
| `last_viewed_at` | `DATETIME` | yes | - |
| `added_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_workbench_cases_owner`: index on `owner`

### Unique Constraints

- `uq_workbench_case_owner_imm`: `owner`, `imm_number`

## `workbench_pins`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `owner` | `String(80)` | no | NOT NULL |
| `case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `notes` | `TEXT` | yes | - |
| `tags` | `JSON` | yes | - |
| `folder` | `String(80)` | yes | - |
| `pinned_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_workbench_pins_case_id`: index on `case_id`
- `ix_workbench_pins_owner`: index on `owner`

### Unique Constraints

- `uq_workbench_pin_owner_case`: `owner`, `case_id`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`
