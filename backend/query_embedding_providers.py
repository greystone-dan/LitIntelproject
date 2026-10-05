"""Configuration and execution for query and case-ingestion embeddings."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from fastapi import HTTPException, status

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
from .embedding_registry import (
    EmbeddingModel,
    get_embedding_model,
)

DEFAULT_QUERY_EMBEDDING_PROVIDER = "none"
OPENAI_EMBEDDING_DIMENSIONS = DEFAULT_OPENAI_EMBEDDING_DIMENSIONS


def OpenAI(**kwargs: Any) -> Any:
    """Construct an OpenAI client only after a hosted provider is selected."""
    from openai import OpenAI as OpenAIClient

    return OpenAIClient(**kwargs)


class QueryEmbeddingConfigurationError(ValueError):
    """Raised when the selected query-embedding configuration is invalid."""


def _registered_settings(
    provider: str, model_name: str
) -> tuple[EmbeddingModel, int]:
    try:
        model_config = get_embedding_model(model_name)
    except ValueError as exc:
        raise QueryEmbeddingConfigurationError(str(exc)) from exc
    if model_config.provider != provider:
        raise QueryEmbeddingConfigurationError(
            f"Embedding model {model_name!r} is not configured for provider {provider!r}"
        )
    return model_config, model_config.output_dimensions


def _provider_model_setting(provider: str) -> tuple[str, str]:
    if provider == "local":
        return "LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL
    return "OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL


def _query_embedding_settings() -> tuple[str, str | None, int | None]:
    configured_provider = os.getenv("QUERY_EMBEDDING_PROVIDER")
    selected_model = os.getenv("EMBEDDING_MODEL")

    if configured_provider is None:
        mode = enhanced_mode()
        if mode in {"hosted", "local"}:
            if selected_model is None:
                model_setting, default_model = _provider_model_setting(
                    mode if mode == "local" else "openai"
                )
                selected_model = os.getenv(model_setting, default_model)
            try:
                configured_provider = get_embedding_model(selected_model).provider
            except ValueError as exc:
                raise QueryEmbeddingConfigurationError(str(exc)) from exc

    provider = (
        configured_provider or DEFAULT_QUERY_EMBEDDING_PROVIDER
    ).strip().lower()
    if provider == "none":
        return provider, None, None
    if provider not in {"openai", "local"}:
        raise QueryEmbeddingConfigurationError(
            "QUERY_EMBEDDING_PROVIDER must be 'none', 'openai', or 'local'"
        )

    provider_model_setting, default_model = _provider_model_setting(provider)
    model_name = os.getenv(
        "QUERY_EMBEDDING_MODEL",
        selected_model or os.getenv(provider_model_setting, default_model),
    )
    model_config, dimensions = _registered_settings(provider, model_name)
    dimensions_setting = os.getenv("QUERY_EMBEDDING_DIMENSIONS")
    if dimensions_setting is not None:
        try:
            configured_dimensions = int(dimensions_setting)
        except ValueError as exc:
            raise QueryEmbeddingConfigurationError(
                "QUERY_EMBEDDING_DIMENSIONS must be a positive integer"
            ) from exc
        if configured_dimensions < 1:
            raise QueryEmbeddingConfigurationError(
                "QUERY_EMBEDDING_DIMENSIONS must be a positive integer"
            )
        if configured_dimensions != dimensions:
            raise QueryEmbeddingConfigurationError(
                "QUERY_EMBEDDING_DIMENSIONS must match the registered model dimension "
                f"({dimensions})"
            )
    return provider, model_config.name, dimensions


def query_embeddings_enabled() -> bool:
    return _query_embedding_settings()[0] != "none"


def query_embedding_provider() -> str:
    return _query_embedding_settings()[0]


def get_indexed_embedding_model() -> EmbeddingModel:
    """Return the registered model selected for indexed vectors."""
    model_id = os.getenv("EMBEDDING_MODEL")
    if model_id is None:
        if enhanced_mode() == "local":
            model_id = os.getenv("LOCAL_EMBEDDING_MODEL", DEFAULT_LOCAL_EMBEDDING_MODEL)
        else:
            model_id = os.getenv(
                "OPENAI_EMBEDDING_MODEL", DEFAULT_OPENAI_EMBEDDING_MODEL
            )
    try:
        return get_embedding_model(model_id)
    except ValueError as exc:
        raise QueryEmbeddingConfigurationError(str(exc)) from exc


@lru_cache(maxsize=8)
def _local_provider(
    model_name: str, dimensions: int
) -> SentenceTransformerEmbeddingProvider:
    return SentenceTransformerEmbeddingProvider(
        model_name=model_name, dimensions=dimensions
    )


def _configured_provider(
    provider: str, model_name: str | None, dimensions: int | None
) -> EmbeddingProvider:
    if provider == "none":
        return NoneEmbeddingProvider()
    assert model_name is not None and dimensions is not None
    if provider == "local":
        return _local_provider(model_name, dimensions)
    return OpenAIEmbeddingProvider(
        model_name,
        dimensions=dimensions,
        client_factory=OpenAI,
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
    try:
        from openai import OpenAIError
    except ImportError:  # pragma: no cover - OpenAI is an application dependency
        OpenAIError = ()  # type: ignore[assignment,misc]
    if isinstance(exc, OpenAIError):
        return HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="The embedding service is unavailable",
        )
    return HTTPException(
        status_code=status.HTTP_502_BAD_GATEWAY,
        detail="The embedding provider failed",
    )


def embed_query(
    text: str,
    *,
    indexed_dimensions: int | None = None,
    model_id: str | None = None,
) -> list[float]:
    provider_name, model_name, dimensions = _query_embedding_settings()
    if model_id is not None:
        try:
            model_config = get_embedding_model(model_id)
        except ValueError as exc:
            raise QueryEmbeddingConfigurationError(str(exc)) from exc
        provider_name = model_config.provider
        model_name = model_config.name
        dimensions = model_config.output_dimensions

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
        vector = _configured_provider(
            provider_name, model_name, dimensions
        ).embed_query(text)
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
    # Ingestion remains explicitly opt-in even though enabled search can infer
    # its provider from the configured model registry.
    configured_provider = os.getenv(
        "CASE_EMBEDDING_PROVIDER",
        os.getenv("QUERY_EMBEDDING_PROVIDER", "none"),
    )
    provider = configured_provider.strip().lower()
    if provider == "none":
        return provider, None, None
    if provider not in {"openai", "local"}:
        raise QueryEmbeddingConfigurationError(
            "CASE_EMBEDDING_PROVIDER must be 'none', 'openai', or 'local'"
        )
    provider_model_setting, default_model = _provider_model_setting(provider)
    model_name = os.getenv(
        "CASE_EMBEDDING_MODEL",
        os.getenv(
            "QUERY_EMBEDDING_MODEL",
            os.getenv(provider_model_setting, default_model),
        ),
    )
    model_config, dimensions = _registered_settings(provider, model_name)
    dimensions_setting = os.getenv("CASE_EMBEDDING_DIMENSIONS")
    if dimensions_setting is not None:
        try:
            configured_dimensions = int(dimensions_setting)
        except ValueError as exc:
            raise QueryEmbeddingConfigurationError(
                "CASE_EMBEDDING_DIMENSIONS must be a positive integer"
            ) from exc
        if configured_dimensions != dimensions or configured_dimensions < 1:
            raise QueryEmbeddingConfigurationError(
                "CASE_EMBEDDING_DIMENSIONS must match the registered model dimension "
                f"({dimensions})"
            )
    return provider, model_config.name, dimensions


def _ingest_rollout_enabled() -> bool:
    override = os.getenv("CASELIBRARY_EMBED_ON_INGEST_ENABLED")
    if override is not None:
        return override.strip().lower() in {"1", "true", "yes", "on"}
    config_path = Path(__file__).resolve().parent.parent / "config.yaml"
    try:
        payload = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
        rollout = (payload.get("ai") or {}).get("rollout") or {}
        return bool(rollout.get("embed_on_ingest_enabled", False))
    except (OSError, TypeError, AttributeError, yaml.YAMLError):
        return False


def embed_case_summary(text: str) -> list[float] | None:
    """Embed ingestion text only with rollout, mode, and provider opt-in."""
    if enhanced_mode() == "off" or not _ingest_rollout_enabled():
        return None
    provider_name, model_name, dimensions = _case_embedding_settings()
    if provider_name == "none":
        return None
    _check_mode(provider_name)
    assert model_name is not None and dimensions is not None

    # Case.embedding is the hosted case_chunks vector. Local models use a
    # separate registered table and cannot be stored in this column safely.
    try:
        model_config = get_embedding_model(model_name)
    except ValueError as exc:
        raise QueryEmbeddingConfigurationError(str(exc)) from exc
    indexed_model = get_indexed_embedding_model()
    if (
        model_config.table != "case_chunks"
        or model_config.dimensions != indexed_model.dimensions
        or model_config.dimensions != OPENAI_EMBEDDING_DIMENSIONS
    ):
        return None
    try:
        provider = _configured_provider(provider_name, model_name, dimensions)
        vector = provider.embed_documents([text])[0]
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
    return vector


def get_search_embedding_status() -> dict[str, str | int | bool | None]:
    provider, model_name, dimensions = _query_embedding_settings()
    if enhanced_mode() == "local" and provider != "local":
        provider, model_name, dimensions = "none", None, None
    indexed_model = get_indexed_embedding_model()
    return {
        "query_provider": provider,
        "model": model_name,
        "dimensions": dimensions,
        "indexed_dimensions": indexed_model.output_dimensions,
        "query_data_leaves_machine": provider == "openai",
        "text_generation_provider": os.getenv(
            "TEXT_GENERATION_PROVIDER", "openai"
        ).strip().lower(),
    }
