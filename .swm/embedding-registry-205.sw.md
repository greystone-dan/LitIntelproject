---
title: "Embedding model configuration and selection"
---

# Embedding model configuration and selection

## Entry points and ownership

- [`config.yaml`](../config.yaml) owns the configured model registry, provider
  defaults, and each model's expected output width.
- [`backend/embedding_registry.py`](../backend/embedding_registry.py) loads and
  validates that static configuration; it does not construct model clients.
- [`backend/query_embedding_providers.py`](../backend/query_embedding_providers.py)
  selects registered metadata and invokes the explicitly selected query
  provider.
- [`backend/embedding_providers.py`](../backend/embedding_providers.py) owns
  local SentenceTransformer execution and verifies output against registry
  metadata.
- [`backend/search_service.py`](../backend/search_service.py) keeps the
  indexed-vector compatibility gate. The existing database vector schema is
  fixed; a registry change does not migrate or re-embed stored vectors.

## Request and data flow

1. `ENHANCED_AI_MODE` remains the outer gate (`off`, `local`, or `hosted`).
2. `QUERY_EMBEDDING_PROVIDER` explicitly selects `local` or `openai`; the
   configured model ID is resolved to provider and output dimensions from the
   registry.
3. Search-status reporting reads metadata without loading a model or making a
   provider request.
4. Only an enabled semantic/hybrid request reaches embedding execution. Local
   generation remains separate from the query-embedding provider.

## Invariants and failure modes

- Unknown model IDs and provider/model mismatches fail configuration selection.
- An explicit local dimension must equal that model's registry width.
- The query vector must also match the width of the indexed vectors; the
  configured local BGE-M3 width does not match the current hosted case-vector
  schema.
- Do not combine model selection with database schema changes, re-embedding,
  or stored-vector rewrites in this owner surface.
- Offline tests replace provider construction; they must never contact OpenAI
  or download SentenceTransformer weights.

## Focused validation

Run `python -m pytest -q tests/test_embedding_registry.py tests/test_ai_mode.py`
for registry selection, local/hosted enhanced-mode behavior, and off-mode
boundaries. The configuration reference and current system contract are
maintained in [`docs/CONFIGURATION_REFERENCE.md`](../docs/CONFIGURATION_REFERENCE.md)
and [`SYSTEM_REFERENCE.md`](../SYSTEM_REFERENCE.md).
