"""Configuration and execution for search-query embeddings."""

from __future__ import annotations

import os
from functools import lru_cache

from fastapi import HTTPException, status
from openai import OpenAI, OpenAIError

from .embedding_providers import (
    SentenceTransformerEmbeddingProvider,
)
from .embedding_registry import (
    DEFAULT_LOCAL_EMBEDDING_MODEL,
    DEFAULT_OPENAI_EMBEDDING_MODEL,
    get_embedding_model,
)

DEFAULT_QUERY_EMBEDDING_PROVIDER = "none"


class QueryEmbeddingConfigurationError(ValueError):
    """Raised when the selected query-embedding configuration is invalid."""


def _query_embedding_settings() -> tuple[str, str | None, int | None]:
    provider = os.getenv("QUERY_EMBEDDING_PROVIDER", DEFAULT_QUERY_EMBEDDING_PROVIDER)
    provider = provider.strip().lower()
    if provider == "none":
        return provider, None, None
    if provider == "openai":
        model_id = os.getenv(
            "QUERY_EMBEDDING_MODEL",
            os.getenv("OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL),
        )
        model_config = get_embedding_model(model_id)
        if model_config.provider != provider:
            raise QueryEmbeddingConfigurationError(
                f"Embedding model {model_id!r} is not configured for provider {provider!r}"
            )
        return (
            provider,
            model_id,
            model_config.output_dimensions,
        )
    if provider == "local":
        model_id = os.getenv(
            "QUERY_EMBEDDING_MODEL",
            os.getenv("LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL),
        )
        model_config = get_embedding_model(model_id)
        if model_config.provider != provider:
            raise QueryEmbeddingConfigurationError(
                f"Embedding model {model_id!r} is not configured for provider {provider!r}"
            )
        dimensions_text = os.getenv("QUERY_EMBEDDING_DIMENSIONS")
        dimensions = model_config.output_dimensions
        if dimensions_text is not None:
            try:
                dimensions = int(dimensions_text)
            except ValueError as exc:
                raise QueryEmbeddingConfigurationError(
                    "QUERY_EMBEDDING_DIMENSIONS must be a positive integer"
                ) from exc
            if dimensions != model_config.output_dimensions:
                raise QueryEmbeddingConfigurationError(
                    f"QUERY_EMBEDDING_DIMENSIONS must match the registered model "
                    f"dimension ({model_config.output_dimensions})"
                )
        return (
            provider,
            model_id,
            dimensions,
        )
    raise QueryEmbeddingConfigurationError(
        "QUERY_EMBEDDING_PROVIDER must be 'none', 'openai', or 'local'"
    )


def query_embeddings_enabled() -> bool:
    return _query_embedding_settings()[0] != "none"


def query_embedding_provider() -> str:
    return _query_embedding_settings()[0]


def get_indexed_embedding_model():
    """Return the configured hosted model used by the indexed-vector contract."""
    model_id = os.getenv("OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL)
    model_config = get_embedding_model(model_id)
    if model_config.provider != "openai":
        raise QueryEmbeddingConfigurationError(
            f"Indexed embedding model {model_id!r} must use provider 'openai'"
        )
    return model_config


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
    model_config = get_embedding_model(model_name)
    if model_config.provider != "openai":
        raise QueryEmbeddingConfigurationError(
            f"Embedding model {model_name!r} is not configured for provider 'openai'"
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
    if len(embedding) != model_config.output_dimensions:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The embedding service returned an unexpected vector size",
        )
    return embedding


def get_search_embedding_status() -> dict[str, str | int | bool | None]:
    provider, model_name, dimensions = _query_embedding_settings()
    model_config = get_indexed_embedding_model()
    return {
        "query_provider": provider,
        "model": model_name,
        "dimensions": dimensions,
        "indexed_dimensions": model_config.output_dimensions,
        "query_data_leaves_machine": provider == "openai",
        "text_generation_provider": os.getenv("TEXT_GENERATION_PROVIDER", "openai").strip().lower(),
    }
