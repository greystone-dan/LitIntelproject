"""Configuration and execution for search-query embeddings."""

from __future__ import annotations

import os
from functools import lru_cache

from fastapi import HTTPException, status
from openai import OpenAI, OpenAIError

from .embedding_providers import (
    DEFAULT_LOCAL_EMBEDDING_DIMENSIONS,
    DEFAULT_LOCAL_EMBEDDING_MODEL,
    SentenceTransformerEmbeddingProvider,
)

DEFAULT_QUERY_EMBEDDING_PROVIDER = "none"
DEFAULT_OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
OPENAI_EMBEDDING_DIMENSIONS = 1536


class QueryEmbeddingConfigurationError(ValueError):
    """Raised when the selected query-embedding configuration is invalid."""


def _query_embedding_settings() -> tuple[str, str | None, int | None]:
    provider = os.getenv("QUERY_EMBEDDING_PROVIDER", DEFAULT_QUERY_EMBEDDING_PROVIDER)
    provider = provider.strip().lower()
    if provider == "none":
        return provider, None, None
    if provider == "openai":
        return (
            provider,
            os.getenv(
                "QUERY_EMBEDDING_MODEL",
                os.getenv("OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL),
            ),
            OPENAI_EMBEDDING_DIMENSIONS,
        )
    if provider == "local":
        dimensions_text = os.getenv(
            "QUERY_EMBEDDING_DIMENSIONS", str(DEFAULT_LOCAL_EMBEDDING_DIMENSIONS)
        )
        try:
            dimensions = int(dimensions_text)
        except ValueError as exc:
            raise QueryEmbeddingConfigurationError(
                "QUERY_EMBEDDING_DIMENSIONS must be a positive integer"
            ) from exc
        if dimensions < 1:
            raise QueryEmbeddingConfigurationError(
                "QUERY_EMBEDDING_DIMENSIONS must be a positive integer"
            )
        return (
            provider,
            os.getenv(
                "QUERY_EMBEDDING_MODEL",
                os.getenv("LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL),
            ),
            dimensions,
        )
    raise QueryEmbeddingConfigurationError(
        "QUERY_EMBEDDING_PROVIDER must be 'none', 'openai', or 'local'"
    )


def query_embeddings_enabled() -> bool:
    return _query_embedding_settings()[0] != "none"


@lru_cache(maxsize=2)
def _local_provider(model_name: str, dimensions: int) -> SentenceTransformerEmbeddingProvider:
    return SentenceTransformerEmbeddingProvider(model_name=model_name, dimensions=dimensions)


def embed_query(text: str, *, indexed_dimensions: int | None = None) -> list[float]:
    provider, model_name, dimensions = _query_embedding_settings()
    if provider == "none":
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Query embeddings are disabled; use lexical search or enable a provider",
        )
    assert model_name is not None and dimensions is not None
    if provider == "local":
        if indexed_dimensions is not None and dimensions != indexed_dimensions:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=(
                    f"Configured local query embedding dimension ({dimensions}) does not "
                    f"match the searched vector dimension ({indexed_dimensions}); "
                    f"re-embedding the indexed vectors to {dimensions} dimensions is "
                    "required before using this local model."
                ),
            )
        try:
            embedding = _local_provider(model_name, dimensions).embed_query(text)
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=(
                    f"{exc}. Searched vectors are {indexed_dimensions or dimensions}-"
                    "dimensional; re-embedding is required before using a local model "
                    "with a different output dimension."
                ),
            ) from exc
        except RuntimeError as exc:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=str(exc),
            ) from exc
    else:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="OPENAI_API_KEY is not configured",
            )
        try:
            organization = os.environ.pop("OPENAI_ORG_ID", None)
            try:
                client = OpenAI(api_key=api_key)
            finally:
                if organization is not None:
                    os.environ["OPENAI_ORG_ID"] = organization
            response = client.embeddings.create(input=text, model=model_name)
        except OpenAIError as exc:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="The embedding service is unavailable",
            ) from exc
        embedding = response.data[0].embedding

    if len(embedding) != dimensions:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=(
                f"The embedding provider returned {len(embedding)} dimensions; "
                f"configured query embeddings require {dimensions}."
            ),
        )
    return embedding


def embed_case_summary(text: str) -> list[float]:
    """Keep case-ingestion embeddings on their existing OpenAI provider path."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="OPENAI_API_KEY is not configured",
        )
    model_name = os.getenv("OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL)
    try:
        organization = os.environ.pop("OPENAI_ORG_ID", None)
        try:
            client = OpenAI(api_key=api_key)
        finally:
            if organization is not None:
                os.environ["OPENAI_ORG_ID"] = organization
        response = client.embeddings.create(input=text, model=model_name)
    except OpenAIError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The embedding service is unavailable",
        ) from exc
    embedding = response.data[0].embedding
    if len(embedding) != OPENAI_EMBEDDING_DIMENSIONS:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The embedding service returned an unexpected vector size",
        )
    return embedding


def get_search_embedding_status() -> dict[str, str | int | bool | None]:
    provider, model_name, dimensions = _query_embedding_settings()
    return {
        "query_provider": provider,
        "model": model_name,
        "dimensions": dimensions,
        "indexed_dimensions": OPENAI_EMBEDDING_DIMENSIONS,
        "query_data_leaves_machine": provider == "openai",
        "text_generation_provider": os.getenv("TEXT_GENERATION_PROVIDER", "openai").strip().lower(),
    }
