# AI CaseLibrary - Long-Term System Guidance

Document role: long-term architecture and product north star.
This is not the live operations snapshot.
For current state and overnight run posture, see `SYSTEM_OVERVIEW.txt` and `OVERNIGHT.md`.

This document is the technical north star for AI CaseLibrary. It describes the intended product direction, architecture, data model, retrieval behavior, and operating principles. It is deliberately separate from `CHANGELOG.md`, which records what has already happened.

## 1. Vision and objectives

AI CaseLibrary is a litigation-focused legal knowledge system for ingesting judicial decisions and related documents, normalizing their metadata, creating semantic representations, and retrieving useful authorities for litigation research and strategy.

The system should make case-law work:

- Faster by reducing manual searching across official court websites and preserved datasets.
- Smarter through semantic, issue-based, and hybrid retrieval.
- Repeatable through consistent ingestion, summarization, tagging, and ranking pipelines.

The system is a research aid. It must not present generated output as legal advice, and every explanation should remain traceable to source cases.

## 1.1 Current stage checkpoint (prototype)

The project has now moved beyond backend-only validation into a prototype interaction stage for immigration litigation research.

Current practical milestone:

- The canonical PostgreSQL corpus now contains 35,902 cases, 168,282 chunks,
	303,816 citations, and 5,808 chunk embeddings.
- A lock-protected overnight pipeline remains ready to tag, chunk, extract
	citations, and locally embed new corpus additions with resumable commits.
- A prototype explorer page can show cohort summary metrics, topic-keyword
	distributions, case-level browsing/filtering, and an interactive citation map
	with topic filters.

Near-term strategy should prioritize product trust and operator reliability:

- Keep prototype views consistent with the active data source (database or regenerated exports).
- Add explicit indicators when map data is artifact-backed rather than computed live.
- Continue hardening map usability (selection details, export, and path tracing) before full RAG generation work.

## 2. Long-term capabilities

The platform should evolve to:

- Ingest cases from official court websites, preserved datasets, uploaded PDFs, HTML, local files, and manual entry.
- Normalize court, jurisdiction, date, parties, citation, and other metadata.
- Generate configurable short and long summaries.
- Embed summaries, issues, and optionally full text.
- Store structured records and vectors in PostgreSQL with pgvector.
- Search semantically, lexically, and through metadata filters.
- Explain results through retrieval-augmented generation (RAG) with citations.
- Automate ingestion, tagging, alerts, and recurring research workflows.

## 3. Target architecture

### Core components

- **FastAPI backend:** API boundary and orchestration for ingestion, search, analysis, and future chat.
- **PostgreSQL + pgvector:** Durable structured storage and vector similarity search.
- **OpenAI or equivalent provider:** Embeddings, optional summarization, and future RAG responses.
- **Configuration layer:** `.env` for secrets and environment-specific values; non-secret defaults belong in code or static configuration.

### Data flow

#### Ingestion

1. Receive raw text or a structured case record.
2. Extract and normalize metadata.
3. Generate a configurable summary when needed.
4. Generate one or more embeddings.
5. Store the case, metadata, source information, and vectors.
6. Return a stable record identifier and processing status.

#### Search

1. Receive a natural-language, issue-based, citation-based, or keyword query.
2. Generate a query embedding.
3. Run semantic, keyword, and metadata filtering as appropriate.
4. Rank candidates using transparent scoring.
5. Return cases with relevance information and source metadata.

#### RAG

1. Receive a research question.
2. Retrieve the most relevant cases and excerpts.
3. Build a context containing the question and source metadata.
4. Generate a cautious explanation grounded in those sources.
5. Return the answer together with cited cases, excerpts, and any uncertainty flags.

## 4. Data model direction

The current `cases` table is intentionally small. It should grow toward a model such as:

- `id`: primary key, eventually UUID or another stable external identifier.
- `title`: normalized case name.
- `court`: canonical court name.
- `jurisdiction`: province, territory, federal, or other jurisdiction.
- `date`: decision date.
- `citation`: official citation string.
- `summary`: consistent short summary.
- `full_text`: optional source text, subject to storage and privacy decisions.
- `issues`: structured issue tags or JSON.
- `embedding`: pgvector representation for semantic retrieval.
- `metadata_json`: flexible source-specific metadata.
- `source_url`, `source_name`, and ingestion timestamps for traceability.

Future related tables may include parties, judges, citations, documents, chunks, ingestion jobs, and saved research queries.

### Indexing and performance

- Add B-tree indexes for court, jurisdiction, date, and citation.
- Add a pgvector index such as HNSW or IVFFlat once the corpus justifies it.
- Use partial indexes for high-value subsets when query patterns are known.
- Prefer measured query plans and corpus benchmarks over premature tuning.

## 5. Ingestion roadmap

The current endpoint accepts `title`, `court`, `date`, and `summary`, embeds the summary, and stores the result. The long-term pipeline should accept raw PDF, HTML, or text input and then:

1. Extract title, court, date, citation, parties, jurisdiction, and issues.
2. Normalize court names, dates, jurisdictions, and citation formats.
3. Generate short and optional long summaries with a configurable legal or plain-language style.
4. Chunk full text when full-text retrieval is enabled.
5. Generate embeddings for summaries, issues, and selected chunks.
6. Store provenance, model information, and processing status.
7. Support retries, idempotency, deduplication, and batch ingestion.

Important product decisions include which courts and jurisdictions to cover, which date ranges matter, how often to ingest, and what summary style is useful in actual litigation work.

## 6. Search and retrieval roadmap

Search should eventually support:

- Semantic similarity for conceptual matches.
- PostgreSQL full-text search for exact terms and names.
- Hybrid ranking that combines semantic and keyword scores.
- Filters for court, jurisdiction, date range, citation, issue, judge, and source.
- Transparent secondary ranking using recency and court hierarchy.
- Pagination and stable ordering for large result sets.
- Result scores and short explanations of why a case matched.

A future scoring model may use a weighted combination such as semantic relevance, keyword relevance, recency, and court authority. The weights should be configurable and evaluated against real research examples.

The definition of a good result must be guided by litigation workflow: conceptual similarity, same cause of action, court level, authority, recency, or some deliberate combination.

## 7. RAG and explanation layer

The future chat layer should answer questions such as which cases address a legal issue while showing the authorities used. Responses should include:

- A concise answer.
- Cited case names and citations.
- Relevant excerpts or summarized holdings.
- Structured legal tests or issues where appropriate.
- Clear uncertainty when the retrieved material is incomplete or conflicting.
- A reminder that the output is a research aid, not legal advice.

Answer style, citation format, depth, and whether to include strategy-oriented analysis are product decisions that should remain configurable. The system should never invent a citation or imply that a generated conclusion was directly stated by a court when it was synthesized.

## 8. Extensibility

Potential future features include:

- Automatic issue tagging and outcome classification.
- Judge and court analytics.
- Citation graphs and authority relationships.
- Doctrine and trend analysis over time.
- Saved searches, alerts, and daily ingestion jobs.
- A web dashboard for browsing and filtering.
- A CLI such as `caselib search "fiduciary duty"`.
- VS Code integration and mobile shortcut workflows.

## 9. Operational principles

- Keep secrets in `.env` and out of version control.
- Track source provenance and model versions for every generated artifact.
- Log ingestion events, search latency, external API failures, and database errors without logging sensitive document content by default.
- Use request IDs and structured logs as the service grows.
- Mock embedding calls in unit tests and use a dedicated database for integration tests.
- Add migrations before making schema changes in shared or production environments.
- Treat client or confidential case material as sensitive data and define retention and access policies before accepting it.
- Design for retryable, idempotent ingestion rather than assuming every external call succeeds.

## 10. Decision points requiring user guidance

The following choices should be made from actual litigation research needs:

- Which jurisdictions, courts, case types, and date ranges to ingest.
- Whether to store full text or only summaries and excerpts.
- Summary length, tone, and level of legal analysis.
- Whether semantic, keyword, recency, or court authority should dominate ranking.
- Required filters and metadata fields.
- Citation style and answer format for RAG responses.
- Ingestion frequency, source permissions, retention, and privacy controls.

## 11. Recommended implementation order

Completed foundation:

- Added Alembic migrations and a stable schema evolution process.
- Added focused mocked API tests for ingest and search validation.
- Added source URLs, citations, jurisdictions, and provenance fields.
- Added filtered, paginated semantic search with normalized similarity scores.
- Tested chunked embeddings on 25 A2AJ cases; chunk-level retrieval evaluation remains before corpus scaling.
- Added a separate curated refugee-risk evaluation group and chunk-level passage retrieval.

Next implementation order:

1. Add PostgreSQL integration tests and relevance evaluation fixtures.
2. Add full-text storage and chunk-level retrieval when the corpus requires it.
3. Add hybrid keyword and semantic ranking.
4. Build the RAG endpoint with citations and grounded-response tests.
5. Add ingestion jobs, deduplication, tagging, authentication, observability, and a user-facing interface.

Current execution point: chunk storage is proven and the broader 35,902-case
corpus is ready for resumable chunking and local BGE-M3 embedding. Retrieval still
needs citation-based benchmarks and grouped parent-case results before RAG output
should be treated as reliable.

Updated immediate implementation order:

1. Run and monitor the resumable overnight tagging, chunking, citation, and local-embedding pipeline.
2. Import staged official-source records only through an explicit, provenance-preserving canonical merge.
3. Measure local retrieval coverage and quality after the embedding backlog completes.
4. Group chunk results by parent case and expand citation-based evaluation fixtures.
5. Align prototype graph data with live database state and add reproducible exports.
6. Proceed to grounded RAG only after retrieval and citation reliability pass measured gates.
CANLII_API_KEY should never be committed or stored in docs; set it only in local environment variables.