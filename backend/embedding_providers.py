"""Provider implementations for text embeddings."""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from threading import RLock
from typing import Any

import numpy as np

from .embedding_registry import (
    DEFAULT_LOCAL_EMBEDDING_DIMENSIONS,
    DEFAULT_LOCAL_EMBEDDING_MODEL,
    DEFAULT_OPENAI_EMBEDDING_DIMENSIONS,
    DEFAULT_OPENAI_EMBEDDING_MODEL,
    EmbeddingModel,
    get_embedding_model,
    validate_embedding_dimensions,
)

__all__ = [
    "DEFAULT_LOCAL_EMBEDDING_DIMENSIONS",
    "DEFAULT_LOCAL_EMBEDDING_MODEL",
    "DEFAULT_OPENAI_EMBEDDING_DIMENSIONS",
    "DEFAULT_OPENAI_EMBEDDING_MODEL",
    "EmbeddingProvider",
    "EmbeddingProviderUnavailableError",
    "NoneEmbeddingProvider",
    "OpenAIEmbeddingProvider",
    "SentenceTransformerEmbeddingProvider",
]


class EmbeddingProvider(ABC):
    """Common interface for document and query embedding providers."""

    model_name: str | None
    dimensions: int | None

    @abstractmethod
    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed multiple documents."""

    @abstractmethod
    def embed_query(self, text: str) -> list[float]:
        """Embed one search query."""


class EmbeddingProviderUnavailableError(RuntimeError):
    """Raised when an embedding provider cannot be used in this environment."""


def _normalize(vector: list[float]) -> list[float]:
    norm = float(np.linalg.norm(np.asarray(vector, dtype=np.float32)))
    return [value / norm for value in vector] if norm else vector


def _registered_model(model_name: str, provider: str) -> EmbeddingModel | None:
    try:
        model_config = get_embedding_model(model_name)
    except ValueError:
        # An explicitly injected/fake model remains useful to provider consumers.
        # Configuration entry points validate model IDs before constructing providers.
        return None
    if model_config.provider != provider:
        if provider == "local":
            raise ValueError(f"Embedding model {model_name!r} is not a local model")
        raise ValueError(f"Embedding model {model_name!r} is not an OpenAI model")
    return model_config


class NoneEmbeddingProvider(EmbeddingProvider):
    """Explicit disabled provider; construction and use never invoke a model."""

    model_name = None
    dimensions = None

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        raise EmbeddingProviderUnavailableError("Embedding provider is disabled")

    def embed_query(self, text: str) -> list[float]:
        raise EmbeddingProviderUnavailableError("Embedding provider is disabled")


class OpenAIEmbeddingProvider(EmbeddingProvider):
    """Lazy OpenAI embeddings adapter, injectable with a compatible fake client."""

    def __init__(
        self,
        model_name: str = DEFAULT_OPENAI_EMBEDDING_MODEL,
        *,
        dimensions: int | None = None,
        client: Any | None = None,
        client_factory: Any | None = None,
    ) -> None:
        self.model_config = _registered_model(model_name, "openai")
        expected_dimensions = (
            self.model_config.output_dimensions
            if self.model_config is not None
            else DEFAULT_OPENAI_EMBEDDING_DIMENSIONS
        )
        if dimensions is not None and self.model_config and dimensions != expected_dimensions:
            raise ValueError(
                f"Embedding model {model_name} is configured for "
                f"{expected_dimensions} dimensions"
            )
        self.model_name = (
            self.model_config.name if self.model_config is not None else model_name
        )
        self.dimensions = expected_dimensions if dimensions is None else dimensions
        self._client = client
        self._client_factory = client_factory

    def _get_client(self) -> Any:
        if self._client is not None:
            return self._client

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise EmbeddingProviderUnavailableError("OPENAI_API_KEY is not configured")

        client_factory = self._client_factory
        if client_factory is None:
            from openai import OpenAI

            client_factory = OpenAI

        # The SDK reads this setting at construction; do not let a process-wide
        # organization override silently affect this application client.
        organization = os.environ.pop("OPENAI_ORG_ID", None)
        try:
            self._client = client_factory(api_key=api_key)
        finally:
            if organization is not None:
                os.environ["OPENAI_ORG_ID"] = organization
        return self._client

    def _encode(self, texts: list[str], *, query: bool) -> list[list[float]]:
        if not texts:
            return []
        prefix = ""
        if self.model_config is not None:
            prefix = (
                self.model_config.query_prefix
                if query
                else self.model_config.document_prefix
            )
        prepared_texts = [f"{prefix}{text}" for text in texts]
        request_input: str | list[str] = prepared_texts
        if query and self.model_config is not None:
            request_input = prepared_texts[0]
        response = self._get_client().embeddings.create(
            input=request_input,
            model=self.model_name,
        )
        vectors = [list(item.embedding) for item in response.data]
        _validate_dimensions(vectors, self.model_name or "unknown", self.dimensions or 0)
        if self.model_config is not None:
            validate_embedding_dimensions(self.model_name or "", len(vectors[0]))
            if self.model_config.normalize:
                vectors = [_normalize(vector) for vector in vectors]
        return vectors

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self._encode(texts, query=False)

    def embed_query(self, text: str) -> list[float]:
        return self._encode([text], query=True)[0]


class SentenceTransformerEmbeddingProvider(EmbeddingProvider):
    """Lazy local sentence-transformer with a process-wide model cache."""

    _models: dict[tuple[str, str], Any] = {}
    _models_lock = RLock()

    def __init__(
        self,
        model_name: str = DEFAULT_LOCAL_EMBEDDING_MODEL,
        *,
        dimensions: int | None = None,
        device: str | None = None,
        model: Any | None = None,
    ) -> None:
        self.model_config = _registered_model(model_name, "local")
        if self.model_config is None and dimensions is None:
            raise ValueError(
                f"Unregistered local embedding model {model_name!r} requires dimensions"
            )
        expected_dimensions = (
            self.model_config.output_dimensions
            if self.model_config is not None
            else dimensions
        )
        if dimensions is not None and self.model_config and dimensions != expected_dimensions:
            raise ValueError(
                f"Embedding model {model_name} is configured for "
                f"{expected_dimensions} dimensions"
            )
        self.model_name = (
            self.model_config.name if self.model_config is not None else model_name
        )
        self.dimensions = expected_dimensions if dimensions is None else dimensions
        self.device = device or os.getenv("LOCAL_EMBEDDING_DEVICE", "cpu")
        self._model = model

    def _get_model(self) -> Any:
        if self._model is None:
            key = (self.model_name or "", self.device)
            with self._models_lock:
                if key not in self._models:
                    try:
                        from sentence_transformers import SentenceTransformer
                    except ImportError as exc:
                        raise EmbeddingProviderUnavailableError(
                            "sentence-transformers is required for local embeddings"
                        ) from exc
                    self._models[key] = SentenceTransformer(
                        self.model_name, device=self.device
                    )
                self._model = self._models[key]
        return self._model

    def _encode(self, texts: list[str], *, query: bool = False) -> list[list[float]]:
        if not texts:
            return []
        prefix = ""
        normalize = False
        if self.model_config is not None:
            prefix = (
                self.model_config.query_prefix
                if query
                else self.model_config.document_prefix
            )
            normalize = self.model_config.normalize
        vectors = self._get_model().encode(
            [f"{prefix}{text}" for text in texts],
            normalize_embeddings=normalize,
            show_progress_bar=False,
            convert_to_numpy=True,
        )
        array = np.asarray(vectors, dtype=np.float32)
        if array.ndim != 2 or array.shape[1] != self.dimensions:
            actual = array.shape[1] if array.ndim == 2 else "unknown"
            raise ValueError(
                f"Embedding model {self.model_name} returned {actual} dimensions; "
                f"expected {self.dimensions}"
            )
        if self.model_config is not None:
            validate_embedding_dimensions(self.model_name or "", array.shape[1])
        return array.tolist()

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self._encode(texts)

    def embed_query(self, text: str) -> list[float]:
        return self._encode([text], query=True)[0]


def _validate_dimensions(
    vectors: list[list[float]], model_name: str, dimensions: int
) -> None:
    for vector in vectors:
        if len(vector) != dimensions:
            raise ValueError(
                f"Embedding model {model_name} returned {len(vector)} dimensions; "
                f"expected {dimensions}"
            )
