"""Configuration and execution for search-query embeddings."""

from __future__ import annotations

import os
from functools import lru_cache
from math import sqrt

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


def _normalize_embedding(embedding: list[float], normalize: bool) -> list[float]:
    if not normalize:
        return embedding
    norm = sqrt(sum(value * value for value in embedding))
    return [value / norm for value in embedding] if norm else embedding


def _query_embedding_settings() -> tuple[str, str | None, int | None]:
    configured_provider = os.getenv("QUERY_EMBEDDING_PROVIDER")
    selected_model = os.getenv("EMBEDDING_MODEL")
    enhanced_mode = os.getenv("ENHANCED_AI_MODE", "off").strip().lower()
    if configured_provider is None and enhanced_mode in {"hosted", "local"}:
        if selected_model is None:
            if enhanced_mode == "local":
                selected_model = os.getenv(
                    "LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL
                )
            else:
                selected_model = os.getenv(
                    "OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL
                )
        configured_provider = (
            "local"
            if enhanced_mode == "local"
            else get_embedding_model(selected_model).provider
        )
    provider = (configured_provider or DEFAULT_QUERY_EMBEDDING_PROVIDER).strip().lower()
    if provider == "none":
        return provider, None, None
    if provider == "openai":
        model_id = os.getenv(
            "QUERY_EMBEDDING_MODEL",
            selected_model
            or os.getenv("OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL),
        )
        model_config = get_embedding_model(model_id)
        if model_config.provider != provider:
            raise QueryEmbeddingConfigurationError(
                f"Embedding model {model_id!r} is not configured for provider {provider!r}"
            )
        return (
            provider,
            model_config.name,
            model_config.output_dimensions,
        )
    if provider == "local":
        model_id = os.getenv(
            "QUERY_EMBEDDING_MODEL",
            selected_model
            or os.getenv("LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL),
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
            model_config.name,
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
    """Return the model selected for indexed vectors, defaulting to hosted embeddings."""
    model_id = os.getenv("EMBEDDING_MODEL")
    if model_id is None and os.getenv("ENHANCED_AI_MODE", "off").strip().lower() == "local":
        model_id = os.getenv("LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL)
    if model_id is None:
        model_id = os.getenv("OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL)
    return get_embedding_model(model_id)


@lru_cache(maxsize=2)
def _local_provider(model_name: str, dimensions: int) -> SentenceTransformerEmbeddingProvider:
    return SentenceTransformerEmbeddingProvider(model_name=model_name, dimensions=dimensions)


def embed_query(
    text: str,
    *,
    indexed_dimensions: int | None = None,
    model_id: str | None = None,
) -> list[float]:
    provider, model_name, dimensions = _query_embedding_settings()
    if model_id is not None:
        model_config = get_embedding_model(model_id)
        provider, model_name, dimensions = (
            model_config.provider,
            model_config.name,
            model_config.dimensions,
        )
    if provider == "none":
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Query embeddings are disabled; use lexical search or enable a provider",
        )
    assert model_name is not None and dimensions is not None
    model_config = get_embedding_model(model_name)
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
            response = client.embeddings.create(
                input=f"{model_config.query_prefix}{text}",
                model=model_name,
            )
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
    return _normalize_embedding(embedding, model_config.normalize)


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
        response = client.embeddings.create(
            input=f"{model_config.document_prefix}{text}",
            model=model_name,
        )
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
    return _normalize_embedding(embedding, model_config.normalize)


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
