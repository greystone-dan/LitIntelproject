"""Provider implementations for text embeddings."""

from __future__ import annotations

import os
from abc import ABC, abstractmethod
from threading import RLock
from typing import Any

import numpy as np

from .settings import settings

DEFAULT_LOCAL_EMBEDDING_MODEL = "BAAI/bge-m3"
DEFAULT_LOCAL_EMBEDDING_DIMENSIONS = 1024
DEFAULT_OPENAI_EMBEDDING_MODEL = "text-embedding-3-small"
DEFAULT_OPENAI_EMBEDDING_DIMENSIONS = 1536


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
		dimensions: int = DEFAULT_OPENAI_EMBEDDING_DIMENSIONS,
		client: Any | None = None,
		client_factory: Any | None = None,
	) -> None:
		self.model_name = model_name
		self.dimensions = dimensions
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

		# The SDK reads this variable during client initialization. Avoid applying a
		# process-wide organization override, then restore it immediately.
		organization = os.environ.pop("OPENAI_ORG_ID", None)
		try:
			self._client = client_factory(api_key=api_key)
		finally:
			if organization is not None:
				os.environ["OPENAI_ORG_ID"] = organization
		return self._client

	def embed_documents(self, texts: list[str]) -> list[list[float]]:
		if not texts:
			return []
		response = self._get_client().embeddings.create(
			input=texts, model=self.model_name
		)
		vectors = [item.embedding for item in response.data]
		_validate_dimensions(vectors, self.model_name, self.dimensions)
		return vectors

	def embed_query(self, text: str) -> list[float]:
		return self.embed_documents([text])[0]


class SentenceTransformerEmbeddingProvider(EmbeddingProvider):
	"""Lazy local sentence-transformer with a process-wide model cache."""

	_models: dict[tuple[str, str], Any] = {}
	_models_lock = RLock()

	def __init__(
		self,
		model_name: str = DEFAULT_LOCAL_EMBEDDING_MODEL,
		*,
		dimensions: int = DEFAULT_LOCAL_EMBEDDING_DIMENSIONS,
		device: str | None = None,
		model: Any | None = None,
	) -> None:
		self.model_name = model_name
		self.dimensions = dimensions
		self.device = device or settings.embedding.device
		self._model = model

	def _get_model(self) -> Any:
		if self._model is None:
			key = (self.model_name, self.device)
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
		return array.tolist()

	def embed_documents(self, texts: list[str]) -> list[list[float]]:
		return self._encode(texts)

	def embed_query(self, text: str) -> list[float]:
		return self._encode([text])[0]


def _validate_dimensions(
	vectors: list[list[float]], model_name: str, dimensions: int
) -> None:
	for vector in vectors:
		if len(vector) != dimensions:
			raise ValueError(
				f"Embedding model {model_name} returned {len(vector)} dimensions; "
				f"expected {dimensions}"
			)
