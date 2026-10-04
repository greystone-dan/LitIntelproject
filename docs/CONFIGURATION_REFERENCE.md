# Configuration Reference

Last reviewed: 2026-10-04

This document describes configuration discovered from active Python environment-variable reads, the checked-in `.env.example`, and `config.yaml`. It contains no credential values. `SYSTEM_REFERENCE.md` is the broader system handbook.

## Configuration Sources And Precedence

1. `backend/database.py` loads repository-root `.env` and then `backend/.env`, both with `override=True`. Values in the latter file therefore win when both exist.
2. Process environment variables are present before those files are loaded, but the project `.env` files may override them because of `override=True`.
3. For database connection selection, explicit `POSTGRES_*` values take precedence over `DATABASE_URL` whenever any `POSTGRES_*` setting is set.
4. Command-line arguments generally override environment-backed defaults for scripts that expose both.
5. `backend/ai_mode.py` reads `ENHANCED_AI_MODE` at runtime (after the database module has loaded the repository and backend `.env` files). The mode defaults to `off`; only `off`, `local`, and `hosted` are accepted. The four search rollout flags under `ai.rollout` are separate controls.

Never commit `.env`, `backend/.env`, database passwords, API keys, access passwords, tunnel credentials, or generated secret files. `.env.example` must contain placeholders only.

## Required Baseline

| Setting | Required for | Notes |
| --- | --- | --- |
| `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` or `DATABASE_URL` | Canonical database routes and write scripts | Prefer complete `POSTGRES_*` local configuration; see precedence above. |
| `OPENAI_API_KEY` | OpenAI embedding, research-answer, and OpenAI audit/adjudication paths | Not required for deterministic extraction, tag, chunk, or most local read paths. |
| `CASELIBRARY_ACCESS_PASSWORD` and preferably a separate `CASELIBRARY_SESSION_SECRET` | Optional private-site login | The gate is off by default and enforced when the password is non-empty. Use a separate strong signing secret and a verified perimeter policy where needed. |

## Application And Database Settings

| Variable | Default | Consumer | Purpose and validation |
| --- | --- | --- | --- |
| `POSTGRES_HOST` | `localhost` | `backend/database.py` | PostgreSQL host when building a connection URL. |
| `POSTGRES_PORT` | `5432` | `backend/database.py` | PostgreSQL TCP port; must parse as an integer. |
| `POSTGRES_DB` | `caselibrary` | `backend/database.py` | PostgreSQL database name. |
| `POSTGRES_USER` | `postgres` | `backend/database.py` | PostgreSQL user. |
| `POSTGRES_PASSWORD` | `postgres` fallback in URL construction | `backend/database.py` | PostgreSQL password. Use a real secret outside local throwaway environments. |
| `DATABASE_URL` | none | `backend/database.py` | Alternative complete SQLAlchemy URL. Ignored when any explicit `POSTGRES_*` variable is present. |
| `OVERNIGHT_PYTHON` | `venv/Scripts/python.exe`, else current interpreter | `scripts/run_overnight.py` | Interpreter used by scheduled jobs. Must point to an executable with project dependencies. |

The SQLAlchemy engine currently uses `pool_pre_ping=True`; pool size, timeout, recycle, and SQL echo values in `config.yaml` are not presently consumed by `create_engine()`. `backend/search_service.py` loads the four AI rollout flags from `config.yaml` and then applies any `CASELIBRARY_*_ENABLED` environment overrides. The independent `ENHANCED_AI_MODE` setting gates enhanced API search and `/research`.

## Access, Session, And Indexing Settings

| Variable | Default | Consumer | Purpose and safety notes |
| --- | --- | --- | --- |
| `CASELIBRARY_ACCESS_PASSWORD` | none (gate disabled) | `backend/main.py` | Enables signed-cookie checks for protected routes when non-empty. The access page returns `503` when unset. |
| `CASELIBRARY_SESSION_SECRET` | `SECRET_KEY`, then access password | `backend/main.py` | HMAC signing secret for access cookies. Configure a separate strong random value rather than relying on either fallback. |
| `SECRET_KEY` | none | `backend/main.py` | Fallback session signing secret only. It is not otherwise a general JWT/application-secret implementation. |
| `CASELIBRARY_SESSION_SECONDS` | `86400`, minimum `300` | `backend/main.py` | Cookie lifetime in seconds. Invalid values fall back to `86400`. |

The application adds `X-Robots-Tag: noindex, nofollow, noarchive` and serves a restrictive `robots.txt`. This is an indexing directive, not authentication. Configure tunnel/reverse-proxy access control before exposing restricted material.

## Optional Security Response Headers

| Variable | Default | Consumer | Purpose and safety notes |
| --- | --- | --- | --- |
| `CASELIBRARY_SECURITY_HEADERS` | `0` (disabled) | `backend/main.py`, `backend/security_headers.py` | Enable response security headers only when set to `1`. |
| `CASELIBRARY_HSTS_MAX_AGE` | `31536000` seconds | `backend/security_headers.py` | HSTS max age; invalid values fall back to the default and negative values are clamped to zero. |
| `CASELIBRARY_HSTS_SUBDOMAINS` | `0` | `backend/security_headers.py` | Adds `includeSubDomains` only when set to `1`; enable only if all subdomains support HTTPS. |
| `CASELIBRARY_CSP_ENFORCE` | `0` | `backend/security_headers.py` | Selects enforcing CSP only when set to `1`; report-only is the default, and enforcement is untested. |

Configuration is read when the application/middleware is initialized; restart
the server after changing these settings. HSTS is emitted only for HTTPS requests
according to the ASGI scheme or the first `X-Forwarded-Proto` value. Only trust
forwarded-protocol headers when a trusted proxy overwrites them. The middleware
preserves existing response headers and does not consume response bodies. See
[Optional Security Response Headers](SECURITY_HEADERS.md) for activation,
report-only review, CSP policy scope, and limitations.

## Optional Request Audit Log

| Variable | Default | Consumer | Purpose and safety notes |
| --- | --- | --- | --- |
| `CASELIBRARY_AUDIT_LOG` | none (disabled) | `backend/audit.py` | JSON-lines file path; 5 MiB rotation, three backups. Parent directory must exist. Use one process per file. |
| `CASELIBRARY_AUDIT_LOG_RAW_ADDRESS` | `false` | `backend/audit.py` | Only `true` (case-insensitive) permits recording the raw client address alongside its hash. |

Configuration is read when the middleware is initialized; restart the server
after changing it. Records contain UTC time, generated request ID, method,
matched route template (`<unmatched>` for unknown paths), status, duration in
milliseconds, and an HMAC-SHA256 client-address hash with a random process-local
key. Hashes are not stable across workers or restarts. Bodies, filenames, query
strings, headers, and cookies are never logged, including on the live-analysis,
memo-citation-check, de-identification, and re-identification routes. Logging
errors do not break requests and do not print records or exception details.
Protect the log directory and review separate server/proxy access logging.
See the optional request audit log section of `SETUP.md` for operator instructions.

## OpenAI And External Model Settings

| Variable | Default | Consumer | Purpose |
| --- | --- | --- | --- |
| `ENHANCED_AI_MODE` | `off` | `backend/ai_mode.py`, API search/research routes, generation provider factory | Selects `off`, `local`, or `hosted`; invalid values are rejected. Off disables `/research` with HTTP 503 and downgrades explicit semantic/hybrid API search to lexical without invoking embeddings. Local selects local generation and permits only local query embeddings. Hosted permits the configured generation and query providers; hosted query embeddings still require explicit `QUERY_EMBEDDING_PROVIDER` selection. |
| `QUERY_EMBEDDING_PROVIDER` | `none` | `backend/query_embedding_providers.py` | Query embeddings are disabled by default; semantic/hybrid requests use lexical ranking. Explicitly select `openai` or `local` query embeddings and enable enhanced mode; OpenAI additionally requires hosted mode. |
| `QUERY_EMBEDDING_MODEL` | Provider default | `backend/query_embedding_providers.py` | Optional explicit query embedding model. Defaults to `OPENAI_EMBEDDING_MODEL`/`text-embedding-3-small` for OpenAI or `LOCAL_EMBEDDING_MODEL`/`BAAI/bge-m3` for local. |
| `QUERY_EMBEDDING_DIMENSIONS` | `1024` for local | `backend/query_embedding_providers.py` | Expected local query-vector size. The selected model's actual output and the target indexed vectors must match; standard hosted semantic search currently requires 1536 dimensions. |
| `TEXT_GENERATION_PROVIDER` | `openai` when `ENHANCED_AI_MODE=hosted` | `backend/text_generation_providers.py` | Selects the `/research` answer-generation provider in enabled modes. `ENHANCED_AI_MODE=local` selects Ollama regardless of this value; hosted mode preserves the configured provider. |
| `OPENAI_API_KEY` | none | `backend/routes.py`, embedding scripts, audit/adjudication scripts | Required wherever an OpenAI client is constructed. Missing keys should produce a controlled failure rather than a silent fallback. |
| `OPENAI_EMBEDDING_MODEL` | `text-embedding-3-small` | `backend/routes.py`, `scripts/embed_a2aj_cases.py`, `scripts/embed_openai_chunks.py`, cohort builders | Case/chunk embedding model name. The common vector dimension is 1536; change model and schema/index assumptions together. |
| `OPENAI_CHAT_MODEL` | `gpt-4o-mini` | `backend/routes.py` | Experimental `/research` answer-generation model. This route is not a production legal-answer system. |
| `OPENAI_EMBED_COST_PER_1M` | `0.02` | `scripts/embed_openai_chunks.py` | Planning estimate for embedding cost per million tokens; does not alter provider billing. |
| `OPENAI_METADATA_AUDIT_MODEL` | `gpt-4.1-nano` | `scripts/adjudicate_fc_metadata.py` | Model for optional low-confidence metadata adjudication. |
| `OPENAI_AUDIT_MODEL` | `gpt-4.1-nano` | `scripts/verify_citation_extraction.py` | Model for optional citation audit sampling. |
| `OPENAI_AUDIT_BUDGET_USD` | `0.10` | `scripts/verify_citation_extraction.py` | Audit budget ceiling used by the script. |
| `OPENAI_AUDIT_INPUT_COST_PER_1M` | `0.10` | `scripts/verify_citation_extraction.py` | Input-token cost estimate used for budget calculation. |
| `OPENAI_AUDIT_OUTPUT_COST_PER_1M` | `0.40` | `scripts/verify_citation_extraction.py` | Output-token cost estimate used for budget calculation. |
| `OPENAI_AUDIT_MAX_OUTPUT_TOKENS` | `300` | `scripts/verify_citation_extraction.py` | Maximum requested completion tokens per audit call. |
| `OPENAI_AUDIT_MAX_CHARS` | `5000` | `scripts/verify_citation_extraction.py` | Maximum source characters included in an audit prompt. |
| `OLLAMA_BASE_URL` | `http://127.0.0.1:11434/v1` | `backend/text_generation_providers.py`, `scripts/run_case_intelligence_request.py` | Local Ollama endpoint base used when the local provider is selected. The application provider uses Ollama's native `/api/chat` endpoint; the bounded script runner uses the compatible `/v1` endpoint. |
| `OLLAMA_MODEL` | `qwen3:4b` | `backend/text_generation_providers.py`, `scripts/run_case_intelligence_request.py` | Local instruct model used when the local provider is selected. The model must be pulled into Ollama separately; set this explicitly if using another pulled model such as `qwen2.5:7b`. |

The case-intelligence runner defaults to the hosted OpenAI provider. Use
`--provider local` to keep prompts and JSON result artifacts on the local
machine through Ollama. Local generation is optional enrichment; deterministic
citations, statutes, offsets, and source provenance remain authoritative.

The experimental `/research` route is disabled unless `ENHANCED_AI_MODE` is
explicitly set to `local` or `hosted`. Off mode returns HTTP 503 with
`AI answers are disabled in this deployment` before retrieval or generation.
Use `ENHANCED_AI_MODE=local` for Ollama; this mode does not construct an OpenAI
generation client. Use `ENHANCED_AI_MODE=hosted` to opt into the existing
provider selection; `TEXT_GENERATION_PROVIDER` may still select Ollama there.
The local provider's code-default model is `qwen3:4b`. An enabled route reports
a controlled `503` when the selected provider is not configured or reachable.
Setting these values does not download a model.

Query embedding is a separate provider decision and is disabled by default.
Semantic/hybrid search uses lexical ranking until an operator explicitly sets
`QUERY_EMBEDDING_PROVIDER=openai` or `local` and enables enhanced AI mode. OpenAI
query inference additionally requires `ENHANCED_AI_MODE=hosted`; local query
inference is permitted in `local` or `hosted` mode. The default off mode never
constructs a query embedding provider. Only the OpenAI setting sends query text
off-machine. Case-ingestion summary embeddings retain their existing,
separately controlled provider path. The read-only
`GET /api/search-embedding-status` endpoint reports both selected providers,
the query model and dimensions (`null` when embeddings are disabled), the
indexed-vector dimension, and whether query text is sent off-machine. It does
not instantiate the embedding model. With the local BGE-M3 model,
query vectors are 1024-dimensional while the standard hosted semantic index is
1536-dimensional; the search dimension guard rejects that incompatible vector
rather than submitting it. Local model inference may fetch model artifacts on
first use if they are not already cached; this is separate from whether query
text leaves the machine. See `docs/reports/local-query-embeddings.md`.

The checked-in template also names `OPENAI_ORG_ID` and `OPENAI_MODEL`, but current application code does not read them. Do not assume setting them changes runtime behavior.

## Local Embedding Settings

| Variable | Default | Consumer | Purpose |
| --- | --- | --- | --- |
| `LOCAL_EMBEDDING_MODEL` | `BAAI/bge-m3` | `backend/query_embedding_providers.py`, `scripts/embed_local_chunks.py` | Local SentenceTransformer model used for model-versioned chunk vectors and the local query-provider fallback. |
| `LOCAL_EMBEDDING_DEVICE` | `cpu` | `backend/embedding_providers.py`, `backend/query_embedding_providers.py`, `scripts/embed_local_chunks.py` | SentenceTransformer device. Use a supported device string such as `cpu` or an intentionally configured accelerator. |
| `A2AJ_EMBED_LIMIT` | `25` | `scripts/embed_a2aj_cases.py` | Limits A2AJ embedding work for bounded pilot runs. |
| `A2AJ_EMBED_SOURCE_TYPE` | `a2aj_curated` | `scripts/embed_a2aj_cases.py` | Selects the canonical source type targeted by that embedding script. |

Local BGE-M3 vectors are expected to have 1024 dimensions. The provider validates returned dimension shape before storage. Do not point a 768- or 1536-dimensional model at the local chunk embedding workflow without an explicit schema/model change.

## Citation, Cohort, And Source Settings

| Variable | Default | Consumer | Purpose |
| --- | --- | --- | --- |
| `CASELIBRARY_CITATION_PIPELINE` | `v2` | `backend/citations.py` | Selects the citation pipeline implementation. Use supported values only; deterministic extraction remains the active expectation. |
| `CASELIBRARY_FOCUS_MASTER_300` | `false` | `backend/citation_map.py` | Restricts applicable citation-map operations to matched IDs in `data/eval/fc_priority_seed_case_map.csv` when true. Default behavior is full corpus. |
| `CANLII_API_KEY` | none | `backend/citation_pipeline/canlii.py` | Optional CanLII API bearer credential. Without it, the client factory returns `None`. |
| `CANLII_API_BASE_URL` | `https://api.canlii.org` | `backend/citation_pipeline/canlii.py` | CanLII API base URL. |
| `CANLII_API_USER_AGENT` | `AI-CaseLibrary/1.0` | `backend/citation_pipeline/canlii.py` | User-Agent for CanLII API requests. |
| `A2AJ_SOURCE_API_URL` | none | `scripts/ingest_a2aj_api.py` | Required unless supplied as `--api-url`. |
| `A2AJ_API_KEY` or value named by `--api-key-env` | none | `scripts/ingest_a2aj_api.py` | Optional API credential for direct A2AJ API ingestion. |
| `CASELIBRARY_INGEST_URL` | `http://127.0.0.1:8000/ingest` | A2AJ/CanLII seed import scripts | Destination for HTTP-based case ingestion. |
| `CASELIBRARY_MERGE_URL` | `http://127.0.0.1:8000/ingest/merge` | `scripts/import_canlaw_staging.py` | Destination for Canlaw staging merge. |
| `CANLAW_DB_PATH` | `canlaw.db` | `canlaw/config.py` | Separate Canlaw staging SQLite path. |
| `CANLAW_HF_DATASET` | `a2aj/canadian-case-law` | `canlaw/config.py` | Hugging Face dataset name for Canlaw tooling. |
| `CANLAW_HF_FC_DATA_DIR` | `FC` | `canlaw/config.py` | Federal Court dataset subset/directory. |
| `CANLAW_HF_RPD_DATA_DIR` | `RPD` | `canlaw/config.py` | RPD dataset subset/directory. |
| `CANLAW_HF_FCA_DATA_DIR` | `FCA` | `canlaw/config.py` | FCA dataset subset/directory. |
| `CANLAW_HF_SCC_DATA_DIR` | `SCC` | `canlaw/config.py` | SCC dataset subset/directory. |
| `CANLAW_EMBEDDING_MODEL` | `sentence-transformers/all-MiniLM-L6-v2` | `canlaw/config.py` | Separate Canlaw embedding model. |
| `CANLAW_SUMMARIZATION_MODEL` | `facebook/bart-large-cnn` | `canlaw/config.py` | Separate Canlaw summarization model. |

The CanLII API client enforces an in-process default ceiling of two requests per second and 1,000 requests per UTC day. Those values are currently dataclass defaults, not environment variables.

## Partially Consumed Template Settings

`config.yaml` records defaults for application, server, database, vector, AI,
logging, security, and path settings. Only the four `ai.rollout` flags read by
`backend/search_service.py` currently affect application behavior.

Changing `server.host`, `server.port`, database-pool, vector, logging, security,
or path values in that file does not alter runtime behavior. The four rollout
flags are `semantic_enabled`, `hybrid_enabled`, `local_semantic_enabled`, and
`embed_on_ingest_enabled`; matching `CASELIBRARY_*_ENABLED` environment values
override them. Use the consuming module's environment settings or explicit
server flags for other runtime configuration.

## Example Local Development Setup

Create a local ignored `.env` with placeholders replaced by actual local values:

```dotenv
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=caselibrary
POSTGRES_USER=your_local_user
POSTGRES_PASSWORD=your_local_password
OPENAI_API_KEY=your_key_only_if_openai_workflows_are_required
LOCAL_EMBEDDING_DEVICE=cpu
OLLAMA_BASE_URL=http://127.0.0.1:11434/v1
OLLAMA_MODEL=qwen2.5:7b
CASELIBRARY_FOCUS_MASTER_300=false
```

For a local-only deterministic extraction/tagging/chunking session, omit `OPENAI_API_KEY` and do not start OpenAI-dependent scripts. For any tunnel or public deployment, configure access control outside the app until the access middleware is repaired and tested.

## Configuration Change Rules

1. Add a variable only when an active code path reads it or a documented deployment system consumes it.
2. State the default, consuming module, required condition, and safety/cost impact.
3. Add a placeholder to `.env.example` only for settings users are expected to configure.
4. Never add a literal token, password, DSN containing a password, or private endpoint to a tracked example or generated artifact.
5. When changing embedding models or dimensions, update the model contract, storage schema, index assumptions, and retrieval tests together.
6. When changing database settings, test both explicit `POSTGRES_*` and `DATABASE_URL` precedence.
7. When changing access settings, test anonymous, authenticated, local, HTTPS, and tunnel/reverse-proxy paths.

## Known Configuration Gaps

1. Only the search-service AI rollout flags in `config.yaml` are loaded; other template values can drift from code.
2. Private access is disabled by default and enforced only when `CASELIBRARY_ACCESS_PASSWORD` is non-empty.
3. The `.env.example` includes several legacy/aspirational names not read by active code.
4. There is no central typed settings object or startup validation report for all required configuration.
5. Cloudflare tunnel configuration is intentionally local and should be documented without committing credentials.