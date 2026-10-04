from __future__ import annotations

import os
from typing import Any

import numpy as np

from .embedding_registry import (
    DEFAULT_LOCAL_EMBEDDING_DIMENSIONS,
    DEFAULT_LOCAL_EMBEDDING_MODEL,
    get_embedding_model,
    validate_embedding_dimensions,
)

__all__ = [
    "DEFAULT_LOCAL_EMBEDDING_DIMENSIONS",
    "DEFAULT_LOCAL_EMBEDDING_MODEL",
    "SentenceTransformerEmbeddingProvider",
]


class SentenceTransformerEmbeddingProvider:
    def __init__(
        self,
        model_name: str = DEFAULT_LOCAL_EMBEDDING_MODEL,
        *,
        dimensions: int | None = None,
        device: str | None = None,
        model: Any | None = None,
    ) -> None:
        model_config = get_embedding_model(model_name)
        if model_config.provider != "local":
            raise ValueError(f"Embedding model {model_name!r} is not a local model")
        self.model_name = model_name
        self.dimensions = (
            model_config.output_dimensions if dimensions is None else dimensions
        )
        if self.dimensions != model_config.output_dimensions:
            raise ValueError(
                f"Embedding model {model_name} is configured for "
                f"{model_config.output_dimensions} dimensions"
            )
        self.device = device or os.getenv("LOCAL_EMBEDDING_DEVICE", "cpu")
        self._model = model

    def _get_model(self):
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError as exc:
                raise RuntimeError(
                    "sentence-transformers is required for local embeddings"
                ) from exc
            self._model = SentenceTransformer(self.model_name, device=self.device)
        return self._model

    def _encode(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        vectors = self._get_model().encode(
            texts,
            normalize_embeddings=True,
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
        # Validate against registry
        validate_embedding_dimensions(self.model_name, array.shape[1])
        return array.tolist()

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self._encode(texts)

    def embed_query(self, text: str) -> list[float]:
        return self._encode([text])[0]
