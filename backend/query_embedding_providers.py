"""Configuration and execution for query and case-ingestion embeddings."""

from __future__ import annotations

import os
from functools import lru_cache

from fastapi import HTTPException, status
from openai import OpenAI, OpenAIError

from .ai_mode import enhanced_mode
from .embedding_providers import (
    DEFAULT_LOCAL_EMBEDDING_DIMENSIONS,
    DEFAULT_LOCAL_EMBEDDING_MODEL,
    DEFAULT_OPENAI_EMBEDDING_DIMENSIONS,
    DEFAULT_OPENAI_EMBEDDING_MODEL,
    EmbeddingProvider,
    EmbeddingProviderUnavailableError,
    NoneEmbeddingProvider,
    OpenAIEmbeddingProvider,
    SentenceTransformerEmbeddingProvider,
)

DEFAULT_QUERY_EMBEDDING_PROVIDER = "none"
OPENAI_EMBEDDING_DIMENSIONS = DEFAULT_OPENAI_EMBEDDING_DIMENSIONS


class QueryEmbeddingConfigurationError(ValueError):
    """Raised when the selected query-embedding configuration is invalid."""


def _positive_dimensions(setting_name: str, default: int) -> int:
    try:
        dimensions = int(os.getenv(setting_name, str(default)))
    except ValueError as exc:
        raise QueryEmbeddingConfigurationError(
            f"{setting_name} must be a positive integer"
        ) from exc
    if dimensions < 1:
        raise QueryEmbeddingConfigurationError(
            f"{setting_name} must be a positive integer"
        )
    return dimensions


def _provider_settings(
    provider_setting: str,
    model_setting: str,
    dimensions_setting: str,
    *,
    provider_default: str,
    model_default_setting: str | None = None,
    dimensions_default: int = DEFAULT_OPENAI_EMBEDDING_DIMENSIONS,
) -> tuple[str, str | None, int | None]:
    provider = os.getenv(provider_setting, provider_default).strip().lower()
    if provider == "none":
        return provider, None, None
    if provider == "openai":
        return (
            provider,
            os.getenv(
                model_setting,
                os.getenv(
                    model_default_setting or "OPENAI_EMBEDDING_MODEL",
                    DEFAULT_OPENAI_EMBEDDING_MODEL,
                ),
            ),
            dimensions_default,
        )
    if provider == "local":
        default_model = (
            os.getenv(model_default_setting, DEFAULT_LOCAL_EMBEDDING_MODEL)
            if model_default_setting
            else DEFAULT_LOCAL_EMBEDDING_MODEL
        )
        return (
            provider,
            os.getenv(model_setting, default_model),
            _positive_dimensions(dimensions_setting, dimensions_default),
        )
    raise QueryEmbeddingConfigurationError(
        f"{provider_setting} must be 'none', 'openai', or 'local'"
    )


def _query_embedding_settings() -> tuple[str, str | None, int | None]:
    provider = os.getenv(
        "QUERY_EMBEDDING_PROVIDER", DEFAULT_QUERY_EMBEDDING_PROVIDER
    ).strip().lower()
    if provider == "openai":
        return (
            provider,
            os.getenv(
                "QUERY_EMBEDDING_MODEL",
                os.getenv("OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL),
            ),
            OPENAI_EMBEDDING_DIMENSIONS,
        )
    return _provider_settings(
        "QUERY_EMBEDDING_PROVIDER",
        "QUERY_EMBEDDING_MODEL",
        "QUERY_EMBEDDING_DIMENSIONS",
        provider_default=DEFAULT_QUERY_EMBEDDING_PROVIDER,
        model_default_setting="LOCAL_EMBEDDING_MODEL",
        dimensions_default=DEFAULT_LOCAL_EMBEDDING_DIMENSIONS,
    )


def query_embeddings_enabled() -> bool:
    return _query_embedding_settings()[0] != "none"


def query_embedding_provider() -> str:
    return _query_embedding_settings()[0]


@lru_cache(maxsize=8)
def _local_provider(model_name: str, dimensions: int) -> SentenceTransformerEmbeddingProvider:
    return SentenceTransformerEmbeddingProvider(model_name=model_name, dimensions=dimensions)


def _configured_provider(
    provider: str, model_name: str | None, dimensions: int | None
) -> EmbeddingProvider:
    if provider == "none":
        return NoneEmbeddingProvider()
    assert model_name is not None and dimensions is not None
    if provider == "local":
        return _local_provider(model_name, dimensions)
    return OpenAIEmbeddingProvider(
        model_name, dimensions=dimensions, client_factory=OpenAI
    )


def _check_mode(provider: str) -> None:
    mode = enhanced_mode()
    if mode == "off":
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI-powered embeddings are disabled in this deployment",
        )
    if mode == "local" and provider != "local":
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Local AI mode permits only local embedding providers",
        )


def _provider_http_error(exc: Exception) -> HTTPException:
    if isinstance(exc, EmbeddingProviderUnavailableError):
        return HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        )
    if isinstance(exc, OpenAIError):
        return HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The embedding service is unavailable",
        )
    return HTTPException(
        status_code=status.HTTP_502_BAD_GATEWAY,
        detail=f"The embedding provider failed: {exc}",
    )


def embed_query(text: str, *, indexed_dimensions: int | None = None) -> list[float]:
    provider_name, model_name, dimensions = _query_embedding_settings()
    if provider_name == "none":
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Query embeddings are disabled; use lexical search or enable a provider",
        )
    _check_mode(provider_name)
    assert model_name is not None and dimensions is not None
    if indexed_dimensions is not None and dimensions != indexed_dimensions:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=(
                f"Configured {provider_name} query embedding dimension ({dimensions}) does not "
                f"match the searched vector dimension ({indexed_dimensions}); "
                f"re-embedding the indexed vectors to {dimensions} dimensions is "
                "required before using this provider."
            ),
        )
    try:
        vector = _configured_provider(provider_name, model_name, dimensions).embed_query(text)
    except ValueError as exc:
        detail = str(exc)
        if provider_name == "local":
            detail = (
                f"{exc}. Searched vectors are {indexed_dimensions or dimensions}-"
                "dimensional; re-embedding is required before using a local model "
                "with a different output dimension."
            )
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=detail,
        ) from exc
    except Exception as exc:
        raise _provider_http_error(exc) from exc
    if len(vector) != dimensions:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=(
                f"The embedding provider returned {len(vector)} dimensions; "
                f"configured query embeddings require {dimensions}."
            ),
        )
    return vector


def _case_embedding_settings() -> tuple[str, str | None, int | None]:
    configured_provider = os.getenv("CASE_EMBEDDING_PROVIDER")
    if configured_provider is None:
        configured_provider = os.getenv(
            "QUERY_EMBEDDING_PROVIDER", DEFAULT_QUERY_EMBEDDING_PROVIDER
        )
    provider = configured_provider.strip().lower()
    if provider == "none":
        return provider, None, None
    if provider == "openai":
        return (
            provider,
            os.getenv(
                "CASE_EMBEDDING_MODEL",
                os.getenv("OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL),
            ),
            OPENAI_EMBEDDING_DIMENSIONS,
        )
    if provider == "local":
        return (
            provider,
            os.getenv(
                "CASE_EMBEDDING_MODEL",
                os.getenv("LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL),
            ),
            _positive_dimensions(
                "CASE_EMBEDDING_DIMENSIONS", DEFAULT_LOCAL_EMBEDDING_DIMENSIONS
            ),
        )
    raise QueryEmbeddingConfigurationError(
        "CASE_EMBEDDING_PROVIDER must be 'none', 'openai', or 'local'"
    )


def embed_case_summary(text: str) -> list[float] | None:
    """Embed an ingested summary only when mode and provider opt in."""
    if enhanced_mode() == "off":
        return None
    provider_name, model_name, dimensions = _case_embedding_settings()
    if provider_name == "none":
        return None
    _check_mode(provider_name)
    assert model_name is not None and dimensions is not None
    try:
        vector = _configured_provider(provider_name, model_name, dimensions).embed_query(text)
    except Exception as exc:
        raise _provider_http_error(exc) from exc
    if len(vector) != dimensions:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=(
                f"The case embedding provider returned {len(vector)} dimensions; "
                f"configured case embeddings require {dimensions}."
            ),
        )
    if len(vector) != OPENAI_EMBEDDING_DIMENSIONS:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=(
                f"The case embedding provider returned {len(vector)} dimensions; "
                f"case embeddings require {OPENAI_EMBEDDING_DIMENSIONS}."
            ),
        )
    return vector


def get_search_embedding_status() -> dict[str, str | int | bool | None]:
    provider, model_name, dimensions = _query_embedding_settings()
    if enhanced_mode() == "local" and provider != "local":
        provider, model_name, dimensions = "none", None, None
    return {
        "query_provider": provider,
        "model": model_name,
        "dimensions": dimensions,
        "indexed_dimensions": OPENAI_EMBEDDING_DIMENSIONS,
        "query_data_leaves_machine": provider == "openai",
        "text_generation_provider": os.getenv("TEXT_GENERATION_PROVIDER", "openai").strip().lower(),
    }
