---
title: "Embedding model configuration and selection"
---

# Embedding model configuration and selection

## Entry points and ownership

- [`config.yaml`](../config.yaml) owns the configured model registry, provider
  defaults, dimensions, normalization, prefixes, and retrieval-table metadata.
- [`backend/embedding_registry.py`](../backend/embedding_registry.py) loads and
  validates that static configuration; it does not construct model clients.
- [`backend/query_embedding_providers.py`](../backend/query_embedding_providers.py)
  selects registered metadata, enforces enhanced-mode policy, and invokes the
  selected query or opt-in ingestion provider.
- [`backend/embedding_providers.py`](../backend/embedding_providers.py) owns
  the common `EmbeddingProvider` contract plus lazy disabled, OpenAI, and
  SentenceTransformer implementations. Local models are shared by model/device
  in-process and registered outputs are checked against registry metadata.
- [`backend/search_service.py`](../backend/search_service.py) uses each selected
  model's table and canonical name for chunk retrieval. The existing database
  vector schemas are fixed; a registry change does not migrate or re-embed
  stored vectors.

## Request and data flow

1. `ENHANCED_AI_MODE` remains the outer gate (`off`, `local`, or `hosted`).
   Off mode downgrades semantic/hybrid search to lexical and makes no embedding
   call.
2. When enhanced mode is enabled, `EMBEDDING_MODEL` selects a registry entry;
   absent an override, the current hosted model remains the default.
   `QUERY_EMBEDDING_PROVIDER` and `QUERY_EMBEDDING_MODEL` remain optional
   overrides and must agree with registered metadata.
3. Search-status reporting reads metadata without loading a model or making a
   provider request.
4. Only an enabled semantic/hybrid request reaches embedding execution.
   Hosted 1536-dimensional queries use the existing hosted chunk tables; BGE-M3
   1024-dimensional queries use `case_chunk_embeddings` and filter by exact
   canonical model tag. Local generation remains separate from query embedding.
5. API-ingestion summary vectors are opt-in and remain subject to the rollout
   flag, enhanced mode, provider selection, and the existing 1536-dimensional
   case-vector contract.

## Invariants and failure modes

- Unknown model IDs and provider/model mismatches fail configuration selection.
- Every registry entry declares its canonical name, provider, dimensions,
  normalization, query/document prefixes, and retrieval table.
- Request validation rejects unregistered models. Aliased `bge-m3` resolves to
  `BAAI/bge-m3` before embedding and table filtering.
- The 1024-dimensional local vector is never compared with 1536-dimensional
  hosted vectors; case-level semantic search remains hosted-only.
- `off` constructs no embedding provider; `local` cannot invoke a hosted
  embedding provider. Model artifact downloads are possible only on enabled
  local-provider execution and are not part of tests.
- Do not combine model selection with database schema changes, re-embedding,
  or stored-vector rewrites in this owner surface.
- Offline tests replace provider construction; they must never contact OpenAI
  or download SentenceTransformer weights.
- Offline model-quality evaluation is a separate CLI workflow with frozen
  datasets and no application-database access; see the
  [offline evaluation walkthrough](offline-model-evaluation.sw.md).

## Focused validation

Run `python -m pytest -q tests/test_embedding_registry.py tests/test_ai_mode.py tests/test_embedding_providers.py`
for registry selection, provider contracts, local/hosted enhanced-mode
behavior, and off-mode boundaries. Offline retrieval/generation evaluation is
documented in [`docs/OFFLINE_MODEL_EVALUATION.md`](../docs/OFFLINE_MODEL_EVALUATION.md).
The configuration reference and current system contract are maintained in
[`docs/CONFIGURATION_REFERENCE.md`](../docs/CONFIGURATION_REFERENCE.md) and
[`SYSTEM_REFERENCE.md`](../SYSTEM_REFERENCE.md).
