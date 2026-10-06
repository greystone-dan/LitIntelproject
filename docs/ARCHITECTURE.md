# iLit architecture overview

This document is a plain-language map for contributors and technical reviewers.
The implementation and generated references remain authoritative; the
[system reference](../SYSTEM_REFERENCE.md) explains current behavior in more
depth.

## At a glance

```mermaid
flowchart LR
    Sources["Court and secondary sources"]
    Collectors["Collectors and staging<br/>scripts/ · fc_ingest/ · canlaw/"]
    Ingest["Validate and merge<br/>backend/ingestion.py"]
    API["FastAPI<br/>backend/main.py · backend/routes.py"]
    DB[("PostgreSQL + pgvector<br/>canonical and derived tables")]
    Process["Deterministic processing<br/>chunks · metadata · citations · statutes · tags"]
    Services["Search and analytics services"]
    Pages["Research pages<br/>Data Explorer · Citation Map · Statute Library · QA tools"]
    Vectors["Optional embeddings"]
    Uploads["Live Analysis upload<br/>memory only"]
    Reference["Separate reference library"]
    Side["Isolated side projects"]

    Sources --> Collectors --> Ingest --> DB
    API --> Ingest
    DB --> Process --> DB
    DB --> Services --> API --> Pages
    Services -. "when configured and available" .-> Vectors
    Pages --> Uploads
    Collectors -. "separate, non-canonical data" .-> Reference
    Side -. "independent storage boundary" .-> DB
```

Collectors acquire or stage source material; validated case records enter
canonical ingestion and merge policy. PostgreSQL stores cases, source history,
and separate derived products. Deterministic processing creates chunks,
metadata, case citations, statute references, tags, and outcomes. Search and
analytics services read those records for API responses and pages. The Statute
Library serves imported legislation sections and point-in-time statute versions
where the versioned source data is available. Embeddings are an optional
retrieval aid, not a replacement for source text or evidence.

Live Analysis is a distinct path: the supplied DOCX or text-based PDF is read
in memory for analysis and is not written to the case database. Legislation and
other reference-library documents, staging collections, Federal Court activity
data, test data, and isolated side-project data remain distinct from canonical
judgment records.

## Where it runs

The live application and PostgreSQL/pgvector database run together on one
workstation. There is no cloud-hosted production database. GitHub stores the
source repository and runs CI; cloud development sessions do not connect to the
live database. A local contributor can run the API against their own configured
PostgreSQL/pgvector instance.

The application password gate and request audit log are disabled unless
explicitly configured. Upload and parsing limits are active by default and can
be adjusted with the `LITINTEL_MAX_*` environment variables. See
[README.md](../README.md) for the short setup/test instructions and
[SYSTEM_REFERENCE.md](../SYSTEM_REFERENCE.md) for configuration details.

## Engine limits and request failure policy

[`backend/db_limits.py`](../backend/db_limits.py) owns opt-in, validated engine
kwargs and precise timeout classification. `database.py` keeps URL precedence,
sessions and ORM ownership; `main.py` only registers the handlers. Unset limits
preserve SQLAlchemy defaults. PostgreSQL timeout options apply per connection;
SQLite keeps its dialect pool and ignores unsupported QueuePool kwargs.
Diagnosed statement/lock timeouts and QueuePool exhaustion return a safe 503
with `Retry-After: 5`; unrelated errors retain their previous handling.

Scripts may opt into a separate `engine_without_timeout()` and must close their
sessions and dispose it; application limits are neither global database changes
nor implicit changes to other processes. This helper does not erase server/role
defaults. See [configuration and accepted ranges](CONFIGURATION_REFERENCE.md#opt-in-database-limits)
and the [database walkthrough](../.swm/2.40nypbay.sw.md#connection-rules).

## Main data tables

The generated [schema reference](SCHEMA_REFERENCE.generated.md) lists every
column, index, and relationship. These are the main groups in plain language:

| Table or group | What it represents |
| --- | --- |
| `cases` | Canonical decision records, including citation identity, text, and normalized metadata |
| `case_sources`, `ingestion_runs` | Source identity, provenance, hashes, merge history, and ingestion-run counts |
| `case_chunks` | Stored passages or structural chunks linked to a case |
| `case_chunk_embeddings`, `recent_case_chunk_embeddings` | Optional vector representations used for similarity retrieval |
| `citations`, `citation_metrics` | Case-citation occurrences, their evidence locations and resolution state, plus case-level metrics |
| `statute_references` | Separate statute or instrument mentions and their evidence locations |
| `statutes`, `statute_versions`, `statute_sections` | Imported federal statutes, their in-force versions, and the sections for each version |
| `legislation_documents`, `legislation_sections` | Separate reference-library authorities and indexed sections |
| `case_tags`, `case_tagging_status` | Evidence-backed legal tags and the processing status for tag layers |
| `case_outcomes` | Versioned outcome classifications with confidence and source evidence |
| `judge_profiles`, `case_judge_profiles` | Normalized judges and links from judges to decisions |
| `saved_searches`, `search_alerts` | User-configured searches and recorded alert state |
| `fc_activity_cases`, `fc_activity_documents`, `fc_activity_classifications`, `fc_activity_motions`, `fc_activity_summaries`, `fc_activity_alerts` | Federal Court procedural/activity data and derived classifications, separate from judgments |
| `fc_procedural_history` | Separate Federal Court docket/procedural-history records |
| `a2aj_cases`, `a2aj_citation_edges`, `a2aj_case_map` | External A2AJ citation-network records and explicit mappings to canonical cases |

Treat citations, statute references, metadata, tags, outcomes, source records,
and embeddings as distinct layers. A source record or activity event is not
itself a judgment.

## Data sources and use

The project preserves source identity and applicable terms as data is staged
and ingested. Broad source categories include official court material,
secondary legal services, third-party datasets such as A2AJ, government
legislation and guidance used as reference material, and synthetic test data.
Unofficial copies must not be treated as authoritative legal text, and
reference-library documents do not enter canonical case tables. Source
priority supports merge decisions; it is not proof of accuracy or permission
to reuse.

For the source-by-source status, known limits, source handling rules, and
licence/terms notes, see the
[Data Source Register](DATA_SOURCE_REGISTER.md). Verify critical legal
propositions against authoritative records and follow upstream terms.

## Repository map

| Location | Responsibility |
| --- | --- |
| `backend/` | Application, API, persistence, processing, retrieval, and page builders; full inventory below |
| `alembic/` | Deployable schema migrations |
| `scripts/` | Source acquisition, import, enrichment, evaluation, documentation generation, and operations |
| `fc_ingest/` | Federal Court source-specific staging and collection |
| `canlaw/` | Local source archive and staging tools |
| `data/` | Local source, evaluation, reference-library, and runtime artifacts |
| `docs/` | Architecture, source governance, setup, and generated references |
| `tests/` | Automated behavior and contract tests |
| `side_projects/` | Independent utilities and datasets outside the canonical case workflow |
| `legacy/` | Archived or reference-only materials |
| `.swm/` | Connected walkthroughs for system architecture and workflows |
| `.github/` | CI and repository automation |

## Backend file inventory

Optional [background jobs](BACKGROUND_JOBS.md) run only through
`scripts/run_jobs.py` in a separate process. Their standard-library scheduler
does not import database configuration or start with the web application.

Each file currently under `backend/` is listed once. The documentation contract
test checks that these paths continue to exist.

| File | Responsibility |
| --- | --- |
| `backend/ai_mode.py` | Central off/local/hosted gate for enhanced API search and research |
| `backend/alert_digest.py` | Pure saved-search digest construction and offline HTML/text rendering, with Minister-loss flags and counted shift notes |
| `backend/analytics_service.py` | Analytics, judge profiles, and Federal Court activity service |
| `backend/audit.py` | Optional metadata-only request audit middleware |
| `backend/batch_jobs.py` | Batch calculations and cache handling for discussion-unit work |
| `backend/batch_safety.py` | Safety rails for batch jobs next to the live site: low priority, one connection, time limits, throttling, site health gate, stop file |
| `backend/case_compare.py` | Stored ID/citation input resolution and comparison of stored cross-citations and pinpoints |
| `backend/case_comparison.py` | Read-only case facts, outcome provenance, and distinct shared/unique legal signals |
| `backend/case_formatter.py` | Deterministic formatting of stored decision text for the reader |
| `backend/case_processing.py` | Coordinates ordered case-processing stages |
| `backend/case_reader_ui.py` | Builds the case reader with statute-reference integration |
| `backend/case_summary.py` | Read-only stored quick-summary API projection with exact paragraph evidence |
| `backend/case_summary_card.py` | Read-only extractive case-summary card projection with stored outcome, authority, and paragraph-pick evidence |
| `backend/case_types/__init__.py` | Deterministic case-type labels ("what kind of case is this"). No AI at any point |
| `backend/case_types/claim_issues.py` | Deterministic "what was the claim decided on" labels for refugee-protection decisions |
| `backend/case_types/classifier.py` | Deterministic "what type of case is this" classifier |
| `backend/case_types/display.py` | Turn a stored case_type_labels row into what the site shows. Reads stored data only; no classification, no AI |
| `backend/case_types/taxonomy.py` | Case-type taxonomy for Canadian immigration and refugee decisions |
| `backend/citation_intelligence_prompts.py` | Improved LLM prompts for citation intelligence analysis (unit-level issue assessment) |
| `backend/citation_map.py` | Citation graph and authority analytics |
| `backend/citation_pipeline/__init__.py` | Citation-extraction package exports |
| `backend/citation_pipeline/canlii.py` | CanLII source adapter for citation extraction |
| `backend/citation_pipeline/models.py` | Citation candidate and extraction data shapes |
| `backend/citation_pipeline/pipeline.py` | Runs citation rules, ranks, and filters overlaps |
| `backend/citation_pipeline/rules.py` | Deterministic citation extraction rules |
| `backend/citation_refine/__init__.py` | Second-pass citation and statute refinement package |
| `backend/citation_refine/cases.py` | Refines case-citation candidates |
| `backend/citation_refine/context.py` | Shared whole-document context for refinement |
| `backend/citation_refine/instruments.py` | Instrument registry for law-reference refinement |
| `backend/citation_refine/laws.py` | Refines statute and treaty references |
| `backend/citation_refine/models.py` | Shared refinement data shapes |
| `backend/citation_refine/pinpoints.py` | Parses structured citation pinpoints |
| `backend/citation_refine/resolution.py` | Links refined references to cases, paragraphs, and provisions |
| `backend/citation_treatment.py` | Pure rules that label how a decision treats a cited authority |
| `backend/citation_treatment_service.py` | Loads stored citations and verifies treatment labels against source text |
| `backend/citations.py` | Extracts, validates, resolves, and measures citation evidence |
| `backend/contextual_authority/__init__.py` | Contextual-authority analysis package |
| `backend/contextual_authority/context_units.py` | Builds contextual text units for analysis |
| `backend/contextual_authority/discussion_units.py` | Deterministic paragraph features and discussion-unit boundaries |
| `backend/contextual_authority/models.py` | Contextual-authority data models and text hashing |
| `backend/contextual_authority/observations.py` | Observation and evidence structures for contextual analysis |
| `backend/contextual_authority/subthemes.py` | Groups discussion-unit subthemes |
| `backend/contextual_authority/teacher_contract.py` | Validates report-only teacher/evaluation outputs |
| `backend/contextual_authority/unit_roles.py` | Deterministic coarse role labels (facts, issues, analysis, disposition...) for discussion units |
| `backend/contextual_authority/voting.py` | Voting helpers for contextual review |
| `backend/contextual_intelligence.py` | Contextual tag, statute, and citation intelligence service |
| `backend/database.py` | SQLAlchemy engine, sessions, ORM schema, and database setup |
| `backend/db_limits.py` | Opt-in engine limits, script engine helper, and precise safe timeout responses |
| `backend/degraded_mode.py` | Narrow database-connection outage classification, safe HTML/JSON 503 responses, and opt-in retryable panel script |
| `backend/deidentify.py` | Reversible document de-identification |
| `backend/deidentify_names.py` | Finds personal names for the de-identification tool |
| `backend/discussion_units_sandbox.py` | Read-only cohort search for the discussion-unit experiment |
| `backend/document_structure.py` | Maps source HTML structure to plain text |
| `backend/embedding_providers.py` | Shared `EmbeddingProvider` interface; disabled, lazy OpenAI, and process-cached SentenceTransformer implementations |
| `backend/fc_activity.py` | Normalizes Federal Court activity source records |
| `backend/fc_activity_insights.py` | Aggregates Federal Court activity summaries for display |
| `backend/health.py` | Bounded liveness and dependency-readiness probes |
| `backend/ingestion.py` | Canonical create/merge policy and source provenance |
| `backend/intelligence.py` | Derives case outcomes, roles, issues, and related metadata |
| `backend/job_runner.py` | Standalone opt-in interval scheduler, DB-free per-job locks, subprocess timeouts and signal cleanup |
| `backend/judge_aliases.py` | Read-side helpers for the reversible judge alias layer |
| `backend/judge_fc_activity.py` | Attach Federal Court docket activity (leave, JR, motions, stays) to a canonical judge profile |
| `backend/judge_issue_record.py` | Aggregates judge-linked issue outcomes with explicit denominators |
| `backend/judge_normalization.py` | Deterministic judge-name normalization (no database, no AI) |
| `backend/legal_tagger.py` | Deterministic evidence-bearing legal tags |
| `backend/legal_tagger_v2.py` | High-precision whitelist tagging comparison layer |
| `backend/legal_tagger_v3.py` | V3 deterministic legal-tag matching layer |
| `backend/live_analysis.py` | In-memory uploaded-document analysis and citation resolution |
| `backend/live_reader.py` | Reader-shaped payload for an uploaded or pasted document (Live Analysis markup view); in memory, no model |
| `backend/load_shedding.py` | Opt-in per-process concurrency buckets and debug-only load status |
| `backend/main.py` | FastAPI app, startup, health, access middleware, and router inclusion |
| `backend/markup_export.py` | Word export of a case with Markup margin notes as real Word comments (pure; standard-library OOXML) |
| `backend/memo_authority_suggestions.py` | Bounded distinct-citation and stored-outcome suggestions for ephemeral memos |
| `backend/memo_citation_check.py` | Checks uploaded legal memos for citation completeness |
| `backend/memo_gap_check.py` | Bounded per-tag missing and possible-contrary authority suggestions for ephemeral memos |
| `backend/memo_suggestion_models.py` | Additive descriptive memo-authority response contracts |
| `backend/metadata.py` | Facade for deterministic source-metadata extraction |
| `backend/metadata_outcomes.py` | Derives outcome and government-role metadata |
| `backend/metadata_subjects.py` | Derives subject metadata |
| `backend/models.py` | Pydantic request and response contracts |
| `backend/outcome_checker.py` | Advisory second reader for rule-unclear outcomes (batch, open case law only) |
| `backend/overruling_risk.py` | Editable source-backed seeds and cautious direct/indirect indicator response shaping |
| `backend/overruling_risk_routes.py` | Read-only route for direct seed matches and stored resolved citation indicators |
| `backend/pages/__init__.py` | HTML page-builder package |
| `backend/pages/about_content.html` | Content template for the About and architecture surface |
| `backend/pages/case_compare.py` | Searchable side-by-side decision comparison page for `/case-compare` and `/compare` |
| `backend/pages/case_quick_summary.py` | Additive formatted-reader Quick summary renderer and verified paragraph links |
| `backend/pages/case_summary_card.py` | Conditional formatted-reader card for exact selected passages and source-paragraph links |
| `backend/pages/changelog_tab.py` | About page views: overview text plus the changelog tab rendered from `data/changelog/changelog.json` |
| `backend/pages/citation_map.py` | Citation Map page builder |
| `backend/pages/citation_pass.py` | Citation Pass QA page builder |
| `backend/pages/data_explorer.py` | Primary Data Explorer interface builder |
| `backend/pages/deidentify.py` | De-identification page builder |
| `backend/pages/discussion_units_sandbox.py` | Experimental discussion-unit page builder |
| `backend/pages/explorer_snapshots.css` | Styles for Explorer snapshot views |
| `backend/pages/explorer_snapshots.js` | Browser behavior for Explorer snapshot views |
| `backend/pages/fc_analytics.py` | Federal Court activity analytics page |
| `backend/pages/issue_brief.py` | Printable source-linked issue brief page |
| `backend/pages/judge_outcomes.py` | Judge outcomes page builder |
| `backend/pages/live_analysis.py` | Live Analysis page: the research page with a view that opens your own document in the reader's markup mode |
| `backend/pages/markup_mode.css` | Styles for the Markup mode case-reader view |
| `backend/pages/markup_mode.js` | Browser behavior for Markup mode: margin notes built from the loaded reader payload |
| `backend/pages/memo_authority_suggestions.py` | Escaped descriptive renderer for additive memo suggestions |
| `backend/pages/memo_citation_check.py` | Memo citation-check page builder |
| `backend/pages/memo_gap_check.py` | Escaped renderer for rule-based memo gap suggestions |
| `backend/pages/mobile_layout.css` | Phone-width layout rules for the search page and case reader, injected last |
| `backend/pages/overruling_risk_reader.js` | Additive, escaped overruling-risk banner for the active case reader |
| `backend/pages/pitch_nav.py` | Pitch navigation: four top-level tabs on the main explorer page |
| `backend/pages/precedent_finder.py` | Ephemeral proposition-to-authority research page builder |
| `backend/pages/prototype.py` | Prototype explorer page builder |
| `backend/pages/quick_search.py` | Lightweight search page builder |
| `backend/pages/reader_v6.css` | TODO: describe this file |
| `backend/pages/reader_v6.js` | TODO: describe this file |
| `backend/pages/research.py` | Experimental research page builder |
| `backend/pages/saved_searches.py` | Saved-search and alert page builder |
| `backend/pages/search_v6.css` | TODO: describe this file |
| `backend/pages/search_v6.js` | TODO: describe this file |
| `backend/pages/statute_library.py` | Browser page for the section-level statute library |
| `backend/pages/statute_viewer.py` | Statute Library page builder for statute versions and sections |
| `backend/pages/tag_analytics.py` | Legal-tag analytics page builder |
| `backend/pages/tag_finder.py` | Tag-based case similarity page builder |
| `backend/pages/testing.py` | API and search testing page builder |
| `backend/pages/theme_explorer.py` | Theme discovery page builder |
| `backend/paragraph_cited_by.py` | Paragraph cited-by logic: signal phrases and per-paragraph aggregation (pure, no database) |
| `backend/paragraph_cited_by_db.py` | Paragraph cited-by storage and reader loaders (batch job writes, reader reads) |
| `backend/paragraph_cited_by_runner.py` | Paragraph cited-by batch loop (small rested batches, resumable) behind `scripts/build_paragraph_cited_by.py` |
| `backend/paragraph_similarity.py` | Bounded paragraph matching using stored evidence |
| `backend/precedent_finder.py` | Bounded V3 tag matching and resolved-authority ranking without storing propositions |
| `backend/prompt_registry.py` | Loads versioned prompt text and header-declared versions |
| `backend/prompts/citation_aware_assessment.txt` | Citation-aware issue-assessment prompt, versioned independently |
| `backend/prompts/citation_issue_focused_assessment.txt` | Issue-focused paragraph-assessment prompt |
| `backend/prompts/citation_lightweight_issue_extraction.txt` | Lightweight issue-extraction prompt |
| `backend/prompts/citation_unit_context_assessment.txt` | Discussion-unit assessment prompt with optional context placeholders |
| `backend/prompts/contextual_authority_teacher.txt` | Contextual-authority treatment teacher prompt |
| `backend/prompts/discussion_paragraph_assessment.txt` | Paragraph-level discussion assessment prompt |
| `backend/prompts/discussion_units.txt` | Discussion-unit grouping prompt |
| `backend/prompts/model_paragraph_segmentation.txt` | Model paragraph segmentation prompt |
| `backend/prompts/research_system.txt` | Experimental `/research` system prompt |
| `backend/query_embedding_providers.py` | Applies enhanced-mode policy to query and case-ingestion provider selection, errors, and vector dimensions |
| `backend/query_syntax.py` | Parses Case Search query operators and builds the interpretation echo |
| `backend/reader_service.py` | Case-reader, citation-pass, and metadata formatting services |
| `backend/request_context.py` | Request ID generation, validation, and optional slow-request logging for observability |
| `backend/resource_limits.py` | Upload and parsed-document size limits and validation |
| `backend/routes.py` | API contracts, request orchestration, and page integration |
| `backend/search_matching.py` | Whole-token identity matching shared by search queries |
| `backend/search_service.py` | Case and passage search/retrieval |
| `backend/security_headers.py` | Opt-in pure-ASGI response security headers |
| `backend/statute_consideration.py` | Aggregates descriptive decision statistics for statutory sections |
| `backend/statute_sections.py` | Section-level statute library: table of contents with case counts and a per-section view |
| `backend/statute_versioning.py` | Selects statute versions by decision date and links references to versions |
| `backend/statutes.py` | Statute identity and citation parsing |
| `backend/text_generation_providers.py` | Experimental `/research` generation providers: OpenAI, native Ollama, and OpenAI-SDK compatible endpoints with explicit context/token/JSON capabilities |
| `backend/theme_discovery.py` | Groups discussion-unit subthemes for theme discovery |
| `backend/unit_search.py` | Deprecated discussion-unit search helper; matches stored BAAI/bge-m3 embeddings and falls back to keywords |
| `backend/vector_tables.py` | Builds `chunk_embeddings_<slug>` pgvector table metadata with per-row model name/version columns and PostgreSQL index DDL from a registry entry; compiles only and never connects or executes DDL |

The test suite validates this inventory and the README route list against the
generated API reference. The generated references are rebuilt from code and
must not be edited by hand.

Query and case-ingestion embeddings share the provider interface but retain
separate configuration and vector contracts. `backend/ai_mode.py` gates use
before provider construction: `off` makes no embedding call, `local` permits
only local inference, and `hosted` permits the selected provider. The default
provider is disabled; OpenAI clients and SentenceTransformer models are created
lazily, and local models are cached across provider instances by model and
device. Search query dimensions are checked against the indexed-vector contract;
case embeddings must also match the existing stored-vector dimension.

The vector-table helper is design scaffolding only: the embedding registry does
not yet exist, no runtime path calls the helper, and no table is created. Its
exact `chunk_embeddings_<slug>` naming rule, per-row model identity columns,
proposed schema, future registry-based search and bulk-load flow, and out-of-chain
migration template are under
[`docs/proposed-migrations/`](proposed-migrations/embedding-per-model-tables.md).
