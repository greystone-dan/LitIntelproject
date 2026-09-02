# Data Source Register

Last reviewed: 2026-09-01

This register describes sources represented in the active repository, their intended role, trust/provenance status, ingestion route, storage boundary, and operating constraints. It is a source-governance record, not a claim that every listed source is continuously available or completely imported.

## Source Classification

| Class | Meaning | Can populate canonical `cases`? |
| --- | --- | --- |
| Official/first-party | Court-origin or official government/court material | Yes, after validation and provenance capture |
| Secondary legal source | Reputable third-party legal publisher/service | Yes, with explicit source type/licence/provenance |
| Dataset/staging source | Bulk research dataset or source-specific archive | Only through canonical ingestion/merge workflow |
| Reference corpus | Legislation, guidance, policy, and background documents | No; intentionally separate |
| Synthetic/test source | Demo, fixture, or test data | Only for explicit test/demo use; must not control canonical data |
| Isolated side project | Independent data product in a separate schema/path | No, unless a deliberate bridge is added |

## Canonical Source Priority

`backend/ingestion.py` determines which source can replace a non-empty canonical field during a merge.

| Source type or family | Priority | Merge behavior |
| --- | ---: | --- |
| `federal_court`, `fc_scraper`, `official_court`, source types beginning `federal_court` or `official` | 400 | Can replace lower-priority non-empty canonical fields |
| `canlii`, `canlii_html_seed`, non-fallback types beginning `canlii` | 300 | Can replace A2AJ/Hugging Face/synthetic canonical fields |
| `a2aj_parquet`, `a2aj_api_seed`, `a2aj_curated`, `a2aj_immigration_core`, `huggingface`, `canlii_html_seed_fallback`, types beginning `a2aj` or `huggingface` | 200 | Fills gaps and can replace lower-priority fields |
| Unrecognized non-empty source type | 100 | Fills gaps; replaces only lower-priority source data |
| `synthetic` | 10 | Must not supersede real-source data |
| Missing source type | 0 | Lowest confidence/precedence |

Priority is not proof of legal accuracy. Conflicting source values are recorded in metadata rather than silently discarded. The active primary source is represented by `case_sources.is_primary`; historical source records remain attached to the case.

## Register

### Federal Court Official Decisions

| Attribute | Details |
| --- | --- |
| Class | Official/first-party acquisition and staging |
| Source type | `federal_court`, `fc_scraper`, or another explicit official-family source type |
| Primary adapters | `fc_ingest/`, `scripts/fc_portal_collector.py`, `scripts/import_fc_decisions.py`, `scripts/crawl_canlii.py` where applicable |
| Staging storage | Source-specific SQLite, JSONL, raw files, and `data/raw/fc/fc_decisions.db` |
| Canonical path | Validate/normalize a record, then pass through canonical ingestion/merge with source URL, identifier, metadata, and hash |
| Provenance requirement | Preserve official URL, source identifier, retrieval/scrape time, raw/text hash, and metadata evidence |
| Known limitation | Discovery, page retrieval, document/PDF capture, and canonical import are independent states. Automated source requests can be blocked or embedded endpoints can reject a request. |

Never call a discovered Federal Court item a captured judgment merely because an identifier exists in staging. Preserve the error/discovery state and resume the supported collector rather than fabricating text or URLs.

### Federal Court Procedural History

| Attribute | Details |
| --- | --- |
| Class | Official/procedural source layer |
| Tables | `fc_procedural_history` |
| Adapter | `scripts/fetch_fc_procedural_history.py` |
| Identity | IMM/file number, with style, judge, leave/JR status/date, latest activity, raw activity text, entries, conflict flag, and fetch timestamp |
| Canonical relationship | Separate from case decisions; linked context only where a reliable docket relation exists |
| Constraint | A procedural-history record is not itself a judgment and must not be represented as a decision-text source |

### Federal Court Activity Dataset

| Attribute | Details |
| --- | --- |
| Class | Dataset/staging intelligence layer |
| Source shape | A2AJ/Hugging Face Federal Court activity rows and document-level docket entries |
| Adapters | `backend/fc_activity.py`, `scripts/ingest_hf_fc_activity.py`, `scripts/classify_fc_activity.py`, `scripts/backfill_case_metadata_outcomes.py` |
| Tables | `fc_activity_cases`, `fc_activity_documents`, `fc_activity_classifications` |
| Identity | Stable source key, optional citation, date/year, case name, source URL, plus deduplicated document entries |
| Canonical relationship | Separate from canonical `cases`; can provide activity context or verified docket correlation |
| Classification | Deterministic classification JSON/version is stored separately from source activity data |
| Constraint | Activity records and classifications are research signals, not judicial reasons, outcomes, or canonical decision capture |

The dataset is particularly useful for IMM-focused procedural/activity analysis but has source-period and coverage limits. Keep date scope and correlation logic visible when presenting results.

### A2AJ Canadian Case Law

| Attribute | Details |
| --- | --- |
| Class | Third-party dataset/staging source |
| Source types | `a2aj_parquet`, `a2aj_api_seed`, `a2aj_curated`, `a2aj_immigration_core` |
| Source name | `A2AJ Canadian Legal Data` where emitted by importers |
| Adapters | `scripts/ingest_a2aj_parquet.py`, `scripts/ingest_a2aj_api.py`, `scripts/curate_a2aj_cases.py`, `scripts/curate_a2aj_immigration_cases.py` |
| Input forms | Local Parquet, direct paginated API, curated/immigration-selected subsets |
| Canonical path | `CaseIngestRequest` to `/ingest`; citation/hash deduplication and source provenance apply |
| Stored source fields | Bilingual citations/names/text where available, URLs, scrape timestamps, cited/citing lists, source licence metadata, and source identity |
| Trust status | Unofficial copy. Verify critical propositions, dates, citations, and dispositions against authoritative material. |

Importers support bounded `--limit` and dry-run workflows. A2AJ data may be broader than immigration and should be filtered/curated rather than assumed IMM-specific.

### A2AJ Citation Network

| Attribute | Details |
| --- | --- |
| Class | Separate provenance network from an external dataset |
| Tables | `a2aj_cases`, `a2aj_citation_edges`, `a2aj_case_map` |
| Adapter | `scripts/ingest_a2aj_citation_network.py` and helpers in `backend/citations.py` |
| Purpose | Preserve A2AJ-provided cited/citing relationships, map A2AJ records to canonical cases, optionally convert matched edges to local citation rows with `provenance="a2aj"` |
| Constraint | Mapping must be explicit; unmatched A2AJ IDs must not be treated as canonical case IDs |

This network supplements locally extracted citation occurrences. It must remain distinguishable through provenance and should not conceal uncertainty in the source mapping.

### CanLII

| Attribute | Details |
| --- | --- |
| Class | Secondary legal source/API or fallback seed source |
| Source types | `canlii`, `canlii_html_seed`, `canlii_html_seed_fallback` |
| Adapters | `scripts/ingest_canlii_seed_cases.py`, `scripts/crawl_canlii.py`, `backend/citation_pipeline/canlii.py` |
| Canonical path | Normalized source record through canonical ingest; records include source URL, source type, seed identity, and CanLII terms/licensing note |
| Credential | Optional `CANLII_API_KEY`; client has bounded in-process request rate/quota defaults |
| Constraint | Direct HTML requests can encounter anti-bot restrictions. Use the documented API/fallback/staging path; do not evade site controls. |

CanLII data has higher merge priority than A2AJ but remains a secondary source. Preserve its terms/licensing metadata and verify critical information against first-party records.

### Canlaw Hugging Face Staging Archive

| Attribute | Details |
| --- | --- |
| Class | Separate local staging archive |
| Package | `canlaw/` |
| Dataset default | `a2aj/canadian-case-law` |
| Courts | FC, RPD, FCA, SCC configurable through `CANLAW_HF_*_DATA_DIR` |
| Storage | Local `canlaw.db`, including raw payload, normalized metadata, source key, and optional staging embeddings |
| Commands | `python -m canlaw.cli ingest_courts`, `repair_staging`, `embed_courts`; bridge with `scripts/import_canlaw_staging.py` |
| Canonical relationship | Does not replace PostgreSQL directly. The bridge uses the established ingestion/merge endpoint. |
| Constraint | Full-decision staging embeddings are not a replacement for canonical passage/chunk retrieval. |

The archive is intended for resilient acquisition and source preservation. It is normally ignored by Git due to size.

### Reference Library

| Attribute | Details |
| --- | --- |
| Class | Separate reference corpus |
| Contents | Legislation, tribunal guidance, court procedure, program materials, and related legal reference documents |
| Authority record | `data/reference_library/manifest.json` |
| Generated index | `data/reference_library/inventory.csv` |
| Downloader | `scripts/download_reference_library.py` |
| Storage | `data/reference_library/documents/` organized by publisher/function |
| Validation | MIME type, PDF signature or recognizable HTML, atomic write, SHA-256 checksum, retrieval/final URL, status/error tracking |
| Canonical relationship | Must never be inserted into canonical judicial/administrative case tables |

The manifest records publisher, title, source type, document date, jurisdiction, topics, original/final URL, local path, MIME type, size, checksum, status, retrieval timestamp, and failure reason. HTML remains HTML; it is never relabeled as a PDF.

### Synthetic And Fixture Data

| Attribute | Details |
| --- | --- |
| Class | Test/demo source |
| Source type | `synthetic` |
| Adapter | `scripts/ingest_synthetic_cases.py` and test fixtures |
| Merge priority | 10 |
| Use | Pipeline demonstrations, deterministic test coverage, local UI testing |
| Constraint | Exclude from meaningful research evaluation where possible; synthetic records must not outrank or overwrite authoritative/real records. |

### Isolated Luck Of The Draw III Data

| Attribute | Details |
| --- | --- |
| Class | Isolated side project |
| Location | `side_projects/luck_of_the_draw_iii/` |
| Storage | PostgreSQL schema `lotd` and side-project outputs |
| Purpose | Independent imported dataset and workbook workflow |
| Canonical relationship | No direct use by canonical case tables or active legal-research routes |
| Constraint | Keep migrations, import paths, and exports isolated unless a future explicit integration decision is made. |

## Provenance Minimums For Canonical Import

Every canonical import should preserve as many of these fields as the source provides:

1. `source_type` and `source_name`.
2. Stable `source_id` and original `source_url`.
3. Dataset/version identifier and upstream licence/terms when available.
4. `scraped_at` or another retrieval timestamp.
5. Raw/full-text hash when text exists.
6. Source-specific metadata in `metadata_json`.
7. Whether the source is currently primary after merge precedence is applied.

Missing provenance is a data-quality defect, not an invitation to fabricate values. Preserve nulls and a clear source status when data cannot be verified.

## Source Handling Rules

1. Do not represent third-party, staged, discovered, or activity data as official judgment capture.
2. Do not merge reference-library documents into `cases`.
3. Do not run competing bulk writers against the same canonical PostgreSQL database.
4. Use dry-run, bounded limits, and resume support where offered.
5. Retain licence/terms metadata and respect source access controls.
6. Use source priority only for merge conflict resolution; it does not verify a legal proposition.
7. Record source type/provenance on derived citation, tag, and activity data where the model supports it.
8. Before adding a new source, define its class, licence, stable identity, raw/staging storage, canonical bridge, precedence, deduplication key, and validation plan.

## Known Source Risks

1. A2AJ and Canlaw source texts are valuable but unofficial copies.
2. CanLII and court sites can enforce access controls or change page structures.
3. Federal Court discovery and document capture completeness are distinct metrics.
4. Docket correlation can be strong without proving that two records are identical decisions.
5. Reference-library snapshots age; checksum validity proves local-file integrity, not current legal validity.
6. Dataset-wide statistics should identify source scope and extraction date before being used for research conclusions.