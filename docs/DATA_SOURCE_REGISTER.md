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

Bulk HTML refresh uses `scripts/acquire_case_html.py` with bounded concurrency,
per-host spacing, request timeouts, retries/backoff, citation validation, and
quarantine. It is intentionally polite; reuse stored `source_html` before
making a network request and do not tune it into an aggressive scraper.

HTML is also used as a calibration reference for text-only chunking. The active
corpus should not require HTML acquisition for every case when canonical text
preserves sufficient headings, paragraph markers, evidence substrings, and
offset-safe boundaries. The parity harness records where HTML exposes structure
that canonical text cannot recover; those differences remain review signals.

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
| Adapters | `backend/fc_activity.py`, `scripts/fetch_fc_procedural_history.py` (`--write-activity`), `scripts/ingest_hf_fc_activity.py`, `scripts/classify_fc_activity.py`, `scripts/backfill_case_metadata_outcomes.py` |
| Tables | `fc_activity_cases`, `fc_activity_documents`, `fc_activity_classifications` |
| Identity | Stable source key, optional citation, date/year, case name, source URL, plus deduplicated document entries; endpoint additions use stable IMM-based keys and preserve source payloads |
| Canonical relationship | Separate from canonical `cases`; can provide activity context or verified docket correlation |
| Classification | Deterministic classification JSON/version is stored separately from source activity data |
| Constraint | Activity records and classifications are research signals, not judicial reasons, outcomes, or canonical decision capture |

The dataset is particularly useful for IMM-focused procedural/activity analysis but has source-period and coverage limits. Keep date scope and correlation logic visible when presenting results.

Independent collection preparation and the approval boundary for a future
worker are documented in
`docs/FC_ACTIVITY_ORACLE_WORKER_RUNBOOK.md`. The worker may stage discovery,
procedural history, and activity classifications without the public website;
canonical PostgreSQL import remains a separate, exclusive, explicitly approved
operation. Oracle Always Free is not an approved hosting decision or a source
of access control.

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

#### Current coverage assessment (2026-09-30)

The live canonical database currently reports `60,849` cases with source type
`a2aj_parquet`, with the newest dated decision at `2026-07-24`. The smaller
`a2aj_api_seed`, `a2aj_curated`, and `a2aj_immigration_core` populations are
targeted subsets rather than a complete refresh. The local `canlaw.db` staging
archive is approximately 6.7 GB and was last modified in August 2026; its
documented snapshot is not proof of present-day A2AJ coverage.

The repository has both a bounded paginated API importer and a Hugging Face
staging bridge, but the public API contract still needs a current, non-mutating
probe. A single unauthenticated request to the documented A2AJ search endpoint
on 2026-09-30 returned HTTP 400 for the attempted query shape, so newer records
are not yet confirmed. Do not infer that the endpoint is unavailable or change
the importer based on that one response; first reconcile the current A2AJ API
request/response contract.

The next safe step is a read-only, one-page source probe or refreshed staging
metadata check, followed by a bounded dry-run comparison against the canonical
date/citation baseline. Any bulk acquisition, source-terms decision, or
canonical PostgreSQL write requires a separate approval and must retain the
existing provenance, hash, source-priority, conflict, checkpoint, and
single-writer safeguards.

The scoped FC/FCA/SCC probe confirmed that the live A2AJ Hugging Face dataset
exposes all three target Parquet partitions. Remote HEAD metadata reported
approximately 850 MB for FC, 145 MB for FCA, and 365 MB for SCC; the remote FC
object differs from the local 844 MB, 35,814-row file. Local staging contains
FC/FCA/SCC rows from the older snapshot, but only the FC Parquet file is
present under `data/raw/a2aj/`; FCA and SCC must be acquired from the current
upstream partitions before they can be dry-run through the Parquet importer.
This establishes a viable refresh source, not the date coverage or permission
to download and import it.

The bounded refresh acquisition completed on 2026-09-30 in
`data/raw/a2aj/refresh-20260930/`. FC contains 35,990 rows through
2026-09-25, FCA contains 7,813 rows through 2026-09-24, and SCC contains
10,893 rows through 2026-09-18. Court-filtered dry-runs found 206 FC, 33 FCA,
and 4 SCC candidates; 168 FC, 28 FCA, and 4 SCC are dated after the canonical
2026-07-24 baseline. The files matched their upstream linked SHA-256 values.
These are staging candidates only. Review of source terms, citation/hash
conflicts, and canonical import remains approval-gated.

SCC HTML acquisition was canaried on 2026-09-30 using
`scripts/acquire_case_html.py --court SCC --missing-html-only`. Five official
pages were inspected: one validated and was stored as a sanitized
`source_html` snapshot with a dedicated provenance row; four were quarantined
because the returned page did not contain the expected citation. The validated
case mapped to canonical text at `0.6828`, below the SCC structural threshold
of `0.85`, so broader SCC HTML acquisition is paused for source-structure
review. The canary did not replace canonical text or rebuild chunks.

The approved post-baseline import completed on 2026-09-30. It added 168 FC, 28
FCA, and 4 SCC cases through the existing `/ingest` contract, increasing the
canonical `a2aj_parquet` population from 60,849 to 61,049. The importer now
supports `--after-date YYYY-MM-DD`, and the run used `--after-date 2026-07-24`
with court filters for only FC, FCA, and SCC. Existing cases were not enriched
or replaced; refreshed relationship metadata and HTML snapshots remain a
separate task.

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

The current authority dry-run checkpoint also preserves official Justice Laws
XML snapshots under `data/reference_library/legislation_xml/` and report
evidence under `data/eval/priority_authority_dry_run.json`. Indian Act, Privacy
Act, and Canadian Human Rights Act passed non-empty, duplicate-free parsing.
The nominal `P-4.6.xml` endpoint was rejected after identity validation because
it returns the Payments for Community Development Act, not the Patent Act; it
must not be indexed under a Patent Act key.

The reviewed non-XML authority snapshots under
`data/reference_library/non_xml_authorities/` are indexed by
`scripts/index_legislation.py` using declared source formats: the Charter
snapshot routes through HTML parsing, while the 1951 Refugee Convention and
1967 Protocol route through extracted text parsing. The indexed records keep
their source URL, local path, checksum, title, citation, and duplicate-free
section rows.

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
## Added federal statute snapshots (2026-10-06)

41 more Justice Laws XML snapshots (Open Government Licence - Canada) sit in `data/reference_library/legislation_xml/`: Customs Act, CBSA Act, Customs Tariff, Excise Tax Act, Excise Acts, Patent Act, Competition Act, Bankruptcy and Insolvency Act, Food and Drugs Act and Regulations, NOC Regulations, CDSA, Canada Evidence Act, Access to Information Act, Fisheries Act, Labour Code, CCRA, CSIS Act, Extradition Act, Security of Information Act, YCJA, Canada Marine and Shipping Acts, EI Act, FPSLRA, PCMLTFA, plus the RPD, RAD, ID, IAD (2022) and Federal Courts Citizenship Immigration Rules and Citizenship Regulations. `scripts/index_legislation.py --dry-run` parses and counts them without a database; `--only-missing` indexes only instruments with no document. Not available: the repealed Immigration Act (R.S.C. 1985, c. I-2) and the pre-2022 IAD Rules, which Justice Laws no longer serves.

Second batch (2026-10-07): 37 more Justice Laws snapshots, about 6,600 sections: Canada Pension Plan, Old Age Security Act, Official Languages Act, Canada Revenue Agency Act, Canada Business Corporations Act, Copyright Act, Trademarks Act, Telecommunications Act, Canada Transportation Act, Canada Elections Act, National Defence Act, CEPA 1999, Judges Act, RCMP Act, Public Service Employment Act, Employment Equity Act, Multiculturalism Act, Divorce Act, SEMA, Magnitsky Act, SCIDA, Tax Court Act and Rules (General Procedure), SIMA, CITT Act, Export and Import Permits Act, Firearms Act, Health of Animals Act, Plant Protection Act, Quarantine Act, WAPPRIITA, Cultural Property Act, Seized Property Management Act, Government Employees Compensation Act, EI Regulations, CCR Regulations, Presentation of Persons (2003) Regulations and Reporting of Imported Goods Regulations.

Third batch (2026-10-07): Financial Administration Act, Statutory Instruments Act, Department of Citizenship and Immigration Act, Canadian Bill of Rights, PIPEDA, Prisons and Reformatories Act, Transfer of Offenders Act, Mutual Legal Assistance in Criminal Matters Act, Identification of Criminals Act, Carriage by Air Act and the Income Tax Regulations (about 970 sections).

Fourth batch (2026-10-07): Pension Act, Bank Act, Broadcasting Act, Aeronautics Act, Veterans Review and Appeal Board Act, Canada Recovery Benefits Act, CERB Act, Statistics Act, Interest Act, Bills of Exchange Act, State Immunity Act, Parliament of Canada Act, Public Service Superannuation Act, Canadian Forces Superannuation Act, Impact Assessment Act, Radiocommunication Act, Emergencies Act, Canada Post Corporation Act, CICC Act, Crimes Against Humanity and War Crimes Act, ESDC Act, Canada Student Financial Assistance Act, Security Offences Act, Public Service Employment Regulations and Patent Rules (about 4,000 sections, Bank Act alone 1,379). Same Open Government Licence - Canada source and identity guard.
