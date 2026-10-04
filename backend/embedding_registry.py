"""Configuration-driven embedding model registry."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Literal, Mapping

import yaml


@dataclass(frozen=True)
class EmbeddingModel:
    """Immutable metadata for one configured embedding model."""

    model_id: str
    provider: Literal["openai", "local"]
    output_dimensions: int


def _registry_from_config(
    embedding_config: Mapping[str, object],
) -> tuple[Mapping[str, EmbeddingModel], dict[str, str]]:
    """Build validated model metadata and defaults from ``ai.embeddings`` config."""
    raw_registry = embedding_config.get("registry")
    if not isinstance(raw_registry, dict) or not raw_registry:
        raise ValueError("ai.embeddings.registry must define at least one model")

    registry: dict[str, EmbeddingModel] = {}
    for model_id, raw_model in raw_registry.items():
        if not isinstance(model_id, str) or not isinstance(raw_model, dict):
            raise ValueError("Embedding registry entries must map model IDs to settings")
        provider = raw_model.get("provider")
        dimensions = raw_model.get("output_dimensions")
        if provider not in {"openai", "local"}:
            raise ValueError(f"Embedding model {model_id!r} has an unsupported provider")
        if not isinstance(dimensions, int) or isinstance(dimensions, bool) or dimensions < 1:
            raise ValueError(
                f"Embedding model {model_id!r} must have positive output_dimensions"
            )
        registry[model_id] = EmbeddingModel(
            model_id=model_id,
            provider=provider,
            output_dimensions=dimensions,
        )

    default_values = {
        "openai": embedding_config.get("model"),
        "local": embedding_config.get("local_model"),
    }
    defaults: dict[str, str] = {}
    for provider, model_id in default_values.items():
        if not isinstance(model_id, str) or model_id not in registry:
            raise ValueError(
                f"ai.embeddings default for {provider} must name a registered model"
            )
        if registry[model_id].provider != provider:
            raise ValueError(
                f"ai.embeddings default {model_id!r} must use provider {provider!r}"
            )
        defaults[provider] = model_id

    return MappingProxyType(registry), defaults


def _load_registry_config() -> tuple[Mapping[str, EmbeddingModel], dict[str, str]]:
    config_path = Path(__file__).resolve().parent.parent / "config.yaml"
    payload = yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    embeddings = ((payload.get("ai") or {}).get("embeddings") or {})
    if not isinstance(embeddings, dict):
        raise ValueError("ai.embeddings must be a mapping")
    return _registry_from_config(embeddings)


EMBEDDING_MODELS, _DEFAULT_MODELS = _load_registry_config()


def get_embedding_model(model_id: str) -> EmbeddingModel:
    """Return registered metadata, rejecting model IDs absent from config."""
    try:
        return EMBEDDING_MODELS[model_id]
    except KeyError as exc:
        available = ", ".join(EMBEDDING_MODELS)
        raise ValueError(
            f"Unknown embedding model {model_id!r}. Available models: {available}"
        ) from exc


def get_default_embedding_model(provider: Literal["openai", "local"]) -> EmbeddingModel:
    """Return the configured default model for a provider."""
    return get_embedding_model(_DEFAULT_MODELS[provider])


def validate_embedding_dimensions(model_id: str, actual_dimensions: int) -> None:
    """Reject output whose width differs from its configured model metadata."""
    expected = get_embedding_model(model_id).output_dimensions
    if actual_dimensions != expected:
        raise ValueError(
            f"Embedding model {model_id} returned {actual_dimensions} dimensions; "
            f"expected {expected}"
        )


DEFAULT_OPENAI_EMBEDDING_MODEL = get_default_embedding_model("openai").model_id
DEFAULT_OPENAI_EMBEDDING_DIMENSIONS = (
    get_default_embedding_model("openai").output_dimensions
)
DEFAULT_LOCAL_EMBEDDING_MODEL = get_default_embedding_model("local").model_id
DEFAULT_LOCAL_EMBEDDING_DIMENSIONS = (
    get_default_embedding_model("local").output_dimensions
)
