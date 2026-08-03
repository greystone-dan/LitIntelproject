from types import SimpleNamespace

import numpy as np
import pytest

from backend.embedding_providers import SentenceTransformerEmbeddingProvider
from scripts.embed_local_chunks import encode_chunk_batch


class FakeSentenceModel:
    def __init__(self, dimensions=1024):
        self.dimensions = dimensions
        self.calls = []

    def encode(self, texts, **kwargs):
        self.calls.append((list(texts), kwargs))
        return np.ones((len(texts), self.dimensions), dtype=np.float32)


def test_sentence_transformer_provider_normalizes_and_validates_dimensions():
    model = FakeSentenceModel()
    provider = SentenceTransformerEmbeddingProvider(
        model_name="BAAI/bge-m3",
        dimensions=1024,
        model=model,
    )

    vectors = provider.embed_documents(["English reasons", "Motifs en francais"])

    assert len(vectors) == 2
    assert len(vectors[0]) == 1024
    assert model.calls[0][1]["normalize_embeddings"] is True
    assert model.calls[0][1]["show_progress_bar"] is False


def test_sentence_transformer_provider_rejects_wrong_dimensions():
    provider = SentenceTransformerEmbeddingProvider(
        model_name="wrong-model",
        dimensions=1024,
        model=FakeSentenceModel(dimensions=384),
    )

    with pytest.raises(ValueError, match="expected 1024"):
        provider.embed_query("test query")


def test_encode_chunk_batch_returns_model_versioned_rows():
    provider = SentenceTransformerEmbeddingProvider(
        model_name="BAAI/bge-m3",
        dimensions=1024,
        model=FakeSentenceModel(),
    )
    chunks = [
        SimpleNamespace(id=10, text="First passage"),
        SimpleNamespace(id=11, text="Second passage"),
    ]

    rows = encode_chunk_batch(chunks, provider)

    assert [row.chunk_id for row in rows] == [10, 11]
    assert all(row.model_name == "BAAI/bge-m3" for row in rows)
    assert all(row.dimensions == 1024 for row in rows)
    assert all(len(row.embedding) == 1024 for row in rows)
