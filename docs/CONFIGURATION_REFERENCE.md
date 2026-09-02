# Configuration Reference

Last reviewed: 2026-09-01

This document describes configuration discovered from active Python environment-variable reads, the checked-in `.env.example`, and `config.yaml`. It contains no credential values. `SYSTEM_REFERENCE.md` is the broader system handbook.

## Configuration Sources And Precedence

1. `backend/database.py` loads repository-root `.env` and then `backend/.env`, both with `override=True`. Values in the latter file therefore win when both exist.
2. Process environment variables are present before those files are loaded, but the project `.env` files may override them because of `override=True`.
3. For database connection selection, explicit `POSTGRES_*` values take precedence over `DATABASE_URL` whenever any `POSTGRES_*` setting is set.
4. Command-line arguments generally override environment-backed defaults for scripts that expose both.
5. `config.yaml` is currently a checked-in static reference template. No active runtime module loads it, so changing it alone does not reconfigure FastAPI, SQLAlchemy, embedding providers, logging, or security behavior.

Never commit `.env`, `backend/.env`, database passwords, API keys, access passwords, tunnel credentials, or generated secret files. `.env.example` must contain placeholders only.

## Required Baseline

| Setting | Required for | Notes |
| --- | --- | --- |
| `POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` or `DATABASE_URL` | Canonical database routes and write scripts | Prefer complete `POSTGRES_*` local configuration; see precedence above. |
| `OPENAI_API_KEY` | OpenAI embedding, research-answer, and OpenAI audit/adjudication paths | Not required for deterministic extraction, tag, chunk, or most local read paths. |
| `CASELIBRARY_ACCESS_PASSWORD` plus independent `CASELIBRARY_SESSION_SECRET` | Intended private-site login | Current middleware does not enforce this login design; do not treat merely setting these variables as access protection. |

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

The SQLAlchemy engine currently uses `pool_pre_ping=True`; pool size, timeout, recycle, and SQL echo values in `config.yaml` are not presently consumed by `create_engine()`.

## Access, Session, And Indexing Settings

| Variable | Default | Consumer | Purpose and safety notes |
| --- | --- | --- | --- |
| `CASELIBRARY_ACCESS_PASSWORD` | none | `backend/main.py` | Intended password for the private access page. A missing value makes `/access` return `503`. Current middleware does not enforce protected-route access. |
| `CASELIBRARY_SESSION_SECRET` | `SECRET_KEY`, then access password | `backend/main.py` | HMAC signing secret for access cookies. Set a separate strong random value; do not rely on the password fallback. |
| `SECRET_KEY` | none | `backend/main.py` | Fallback session signing secret only. It is not otherwise a general JWT/application-secret implementation. |
| `CASELIBRARY_SESSION_SECONDS` | `86400`, minimum `300` | `backend/main.py` | Cookie lifetime in seconds. Invalid values fall back to `86400`. |

The application adds `X-Robots-Tag: noindex, nofollow, noarchive` and serves a restrictive `robots.txt`. This is an indexing directive, not authentication. Configure tunnel/reverse-proxy access control before exposing restricted material.

## OpenAI And External Model Settings

| Variable | Default | Consumer | Purpose |
| --- | --- | --- | --- |
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

The checked-in template also names `OPENAI_ORG_ID` and `OPENAI_MODEL`, but current application code does not read them. Do not assume setting them changes runtime behavior.

## Local Embedding Settings

| Variable | Default | Consumer | Purpose |
| --- | --- | --- | --- |
| `LOCAL_EMBEDDING_MODEL` | `BAAI/bge-m3` | `scripts/embed_local_chunks.py` | Local SentenceTransformer model used for model-versioned chunk vectors. |
| `LOCAL_EMBEDDING_DEVICE` | `cpu` | `backend/embedding_providers.py`, `scripts/embed_local_chunks.py` | SentenceTransformer device. Use a supported device string such as `cpu` or an intentionally configured accelerator. |
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

## Static Template Settings

`config.yaml` records non-secret aspirational/default settings for app identity, server, database pool, pgvector, AI behavior, logging, security, Copilot indexing, and common paths. It is not currently loaded by active application code.

Treat it as a planning template until a configuration loader is implemented. In particular, changing `server.host`, `server.port`, `database.pool_size`, `pgvector.index_type`, `ai.rollout`, `logging`, `security`, or `paths` in that file will not alter runtime behavior today. Use explicit Uvicorn flags, runtime environment variables, or code changes instead.

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

1. `config.yaml` is not a live configuration source and can drift from code.
2. The private-access variables are not enforced by current middleware.
3. The `.env.example` includes several legacy/aspirational names not read by active code.
4. There is no central typed settings object or startup validation report for all required configuration.
5. Cloudflare tunnel configuration is intentionally local and should be documented without committing credentials.