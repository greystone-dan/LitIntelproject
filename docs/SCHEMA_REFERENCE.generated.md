# Generated Database Schema Reference

This file is generated from `backend.database.Base.metadata` by `scripts/generate_schema_reference.py`. Do not edit it manually.

Generated: 2026-09-05T02:07:19.218418+00:00
Tables: 22

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
    citations {
        Integer id PK
        Integer source_case_id  FK
        Integer target_case_id  FK
        String(20) citation_kind
        TEXT citation_text
        TEXT normalized_citation
        String(20) provenance
        Integer chunk_id  FK
        Integer offset_start
        Integer offset_end
        BOOLEAN unresolved
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
    statute_references {
        Integer id PK
        Integer source_case_id  FK
        Integer chunk_id  FK
        Integer offset_start
        Integer offset_end
        TEXT reference_text
        TEXT normalized_reference
        String(100) instrument_key
        String(255) pinpoint
        TEXT legislation_url
        String(20) reference_kind
    }
    a2aj_cases ||--o{ a2aj_case_map : "a2aj_case_id"
    cases ||--o{ a2aj_case_map : "local_case_id"
    case_chunks ||--o{ case_chunk_embeddings : "chunk_id"
    cases ||--o{ case_chunks : "case_id"
    cases ||--o{ case_judge_profiles : "case_id"
    judge_profiles ||--o{ case_judge_profiles : "judge_profile_id"
    cases ||--o{ case_outcomes : "case_id"
    cases ||--o{ case_sources : "case_id"
    cases ||--o{ case_tagging_status : "case_id"
    cases ||--o{ case_tags : "case_id"
    case_chunks ||--o{ case_tags : "chunk_id"
    cases ||--o{ citation_metrics : "case_id"
    case_chunks ||--o{ citations : "chunk_id"
    cases ||--o{ citations : "source_case_id"
    cases ||--o{ citations : "target_case_id"
    fc_activity_cases ||--o{ fc_activity_classifications : "source_case_id"
    fc_activity_cases ||--o{ fc_activity_documents : "case_id"
    legislation_documents ||--o{ legislation_sections : "document_id"
    case_chunks ||--o{ statute_references : "chunk_id"
    cases ||--o{ statute_references : "source_case_id"
```

## Table Summary

| Table | Columns | Primary key |
| --- | ---: | --- |
| `a2aj_case_map` | 2 | `a2aj_case_id` |
| `a2aj_cases` | 8 | `id` |
| `a2aj_citation_edges` | 4 | `id` |
| `case_chunk_embeddings` | 6 | `id` |
| `case_chunks` | 13 | `id` |
| `case_judge_profiles` | 5 | `id` |
| `case_outcomes` | 18 | `id` |
| `case_sources` | 14 | `id` |
| `case_tagging_status` | 5 | `id` |
| `case_tags` | 15 | `id` |
| `cases` | 28 | `id` |
| `citation_metrics` | 4 | `case_id` |
| `citations` | 11 | `id` |
| `fc_activity_cases` | 15 | `id` |
| `fc_activity_classifications` | 17 | `id` |
| `fc_activity_documents` | 9 | `id` |
| `fc_procedural_history` | 14 | `id` |
| `ingestion_runs` | 12 | `id` |
| `judge_profiles` | 8 | `id` |
| `legislation_documents` | 7 | `id` |
| `legislation_sections` | 6 | `id` |
| `statute_references` | 11 | `id` |

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

### Unique Constraints

- `uq_case_tag_taxonomy`: `case_id`, `category`, `value`, `offset_start`, `offset_end`, `taxonomy_version`

### Foreign Keys

- `case_id` -> `cases.id`; on delete `CASCADE`
- `chunk_id` -> `case_chunks.id`; on delete `SET NULL`

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

### Foreign Keys

- `chunk_id` -> `case_chunks.id`; on delete `SET NULL`
- `source_case_id` -> `cases.id`; on delete `CASCADE`
- `target_case_id` -> `cases.id`; on delete `CASCADE`

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
| `scraped_timestamp` | `DATETIME` | yes | - |
| `raw_payload` | `JSON` | yes | - |
| `created_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_fc_activity_cases_citation`: index on `citation`
- `ix_fc_activity_cases_date_filed`: index on `date_filed`
- `ix_fc_activity_cases_source_key`: unique index on `source_key`
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
| `scraped_timestamp` | `DATETIME` | yes | - |
| `classification_json` | `JSON` | no | NOT NULL |
| `classifier_version` | `String(80)` | no | NOT NULL |
| `classified_at` | `DATETIME` | no | NOT NULL; default=now() |
| `updated_at` | `DATETIME` | no | NOT NULL; default=now() |

### Indexes

- `ix_fc_activity_classifications_date_filed`: index on `date_filed`
- `ix_fc_activity_classifications_imm_number`: index on `imm_number`
- `ix_fc_activity_classifications_source_case_id`: unique index on `source_case_id`
- `ix_fc_activity_classifications_source_key`: index on `source_key`
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

## `statute_references`

### Columns

| Column | Type | Nullable | Constraints and defaults |
| --- | --- | --- | --- |
| `id` | `Integer` | no | PK; NOT NULL |
| `source_case_id` | `Integer` | no | FK -> cases.id; NOT NULL |
| `chunk_id` | `Integer` | yes | FK -> case_chunks.id |
| `offset_start` | `Integer` | yes | - |
| `offset_end` | `Integer` | yes | - |
| `reference_text` | `TEXT` | yes | - |
| `normalized_reference` | `TEXT` | yes | - |
| `instrument_key` | `String(100)` | yes | - |
| `pinpoint` | `String(255)` | yes | - |
| `legislation_url` | `TEXT` | yes | - |
| `reference_kind` | `String(20)` | no | NOT NULL |

### Indexes

- `ix_statute_references_chunk_id`: index on `chunk_id`
- `ix_statute_references_instrument_key`: index on `instrument_key`
- `ix_statute_references_normalized_reference`: index on `normalized_reference`
- `ix_statute_references_pinpoint`: index on `pinpoint`
- `ix_statute_references_reference_kind`: index on `reference_kind`
- `ix_statute_references_source_case_id`: index on `source_case_id`

### Foreign Keys

- `chunk_id` -> `case_chunks.id`; on delete `SET NULL`
- `source_case_id` -> `cases.id`; on delete `CASCADE`
