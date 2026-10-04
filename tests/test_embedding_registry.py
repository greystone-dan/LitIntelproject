"""Test configured embedding registry and offline provider selection."""

from types import SimpleNamespace

import numpy as np
import pytest

from backend import query_embedding_providers, search_service
from backend.embedding_registry import (
    EMBEDDING_MODELS,
    _registry_from_config,
    get_embedding_model,
    validate_embedding_dimensions,
)
from backend.embedding_providers import SentenceTransformerEmbeddingProvider


class TestEmbeddingRegistry:
    """Tests for the embedding model registry."""

    def test_registry_contains_expected_models(self):
        """Verify registry includes text-embedding-3-small and BAAI/bge-m3."""
        assert "text-embedding-3-small" in EMBEDDING_MODELS
        assert "BAAI/bge-m3" in EMBEDDING_MODELS

    def test_registry_models_are_immutable(self):
        """Verify EmbeddingModel dataclass is frozen."""
        model = EMBEDDING_MODELS["text-embedding-3-small"]
        with pytest.raises(AttributeError):
            model.output_dimensions = 999
        with pytest.raises(TypeError):
            EMBEDDING_MODELS["test-model"] = model

    def test_registry_is_built_from_configuration(self):
        registry, defaults = _registry_from_config(
            {
                "model": "configured-hosted-model",
                "local_model": "configured-local-model",
                "registry": {
                    "configured-hosted-model": {
                        "provider": "openai",
                        "output_dimensions": 768,
                    },
                    "configured-local-model": {
                        "provider": "local",
                        "output_dimensions": 384,
                    },
                },
            }
        )
        assert registry["configured-hosted-model"].output_dimensions == 768
        assert registry["configured-local-model"].provider == "local"
        assert defaults == {
            "openai": "configured-hosted-model",
            "local": "configured-local-model",
        }

    def test_text_embedding_3_small_metadata(self):
        """Verify text-embedding-3-small has correct metadata."""
        model = get_embedding_model("text-embedding-3-small")
        assert model.model_id == "text-embedding-3-small"
        assert model.provider == "openai"
        assert model.output_dimensions == 1536

    def test_baai_bge_m3_metadata(self):
        """Verify BAAI/bge-m3 has correct metadata."""
        model = get_embedding_model("BAAI/bge-m3")
        assert model.model_id == "BAAI/bge-m3"
        assert model.provider == "local"
        assert model.output_dimensions == 1024

    def test_all_miniml_l6_v2_metadata(self):
        """Verify all-MiniLM-L6-v2 fallback model metadata."""
        model = get_embedding_model("sentence-transformers/all-MiniLM-L6-v2")
        assert model.model_id == "sentence-transformers/all-MiniLM-L6-v2"
        assert model.provider == "local"
        assert model.output_dimensions == 384

    def test_get_embedding_model_raises_for_unknown_model(self):
        """Verify unknown model raises ValueError with helpful message."""
        with pytest.raises(ValueError, match="Unknown embedding model 'unknown-model'"):
            get_embedding_model("unknown-model")

    def test_validate_embedding_dimensions_accepts_correct_dimensions(self):
        """Verify validation passes for correct dimensions."""
        # Should not raise
        validate_embedding_dimensions("text-embedding-3-small", 1536)
        validate_embedding_dimensions("BAAI/bge-m3", 1024)

    def test_validate_embedding_dimensions_rejects_wrong_dimensions(self):
        """Verify validation rejects incorrect dimensions."""
        with pytest.raises(ValueError, match="expected 1536"):
            validate_embedding_dimensions("text-embedding-3-small", 1024)

        with pytest.raises(ValueError, match="expected 1024"):
            validate_embedding_dimensions("BAAI/bge-m3", 1536)


class FakeSentenceModel:
    """Mock SentenceTransformer for testing without actual model loading."""

    def __init__(self, dimensions=1024):
        self.dimensions = dimensions
        self.calls = []

    def encode(self, texts, **kwargs):
        self.calls.append((list(texts), kwargs))
        return np.ones((len(texts), self.dimensions), dtype=np.float32)


class TestEmbeddingProviderWithRegistry:
    """Test SentenceTransformerEmbeddingProvider uses registry validation."""

    def test_provider_validates_baai_bge_m3_dimensions(self):
        """Verify provider validates BAAI/bge-m3 returns correct 1024 dimensions."""
        model = FakeSentenceModel(dimensions=1024)
        provider = SentenceTransformerEmbeddingProvider(
            model_name="BAAI/bge-m3",
            dimensions=1024,
            model=model,
        )

        vectors = provider.embed_documents(["test text"])

        assert len(vectors) == 1
        assert len(vectors[0]) == 1024

    def test_provider_uses_registered_local_dimensions(self):
        """Verify local model dimensions are selected from the registry."""
        model = FakeSentenceModel(dimensions=384)
        provider = SentenceTransformerEmbeddingProvider(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model=model,
        )

        vectors = provider.embed_documents(["test text"])

        assert len(vectors) == 1
        assert len(vectors[0]) == 384

    def test_local_provider_rejects_hosted_model(self):
        with pytest.raises(ValueError, match="not a local model"):
            SentenceTransformerEmbeddingProvider(model_name="text-embedding-3-small")

    def test_provider_rejects_baai_wrong_dimensions(self):
        """Verify provider rejects BAAI/bge-m3 with wrong dimensions."""
        model = FakeSentenceModel(dimensions=384)  # Wrong: should be 1024
        provider = SentenceTransformerEmbeddingProvider(
            model_name="BAAI/bge-m3",
            dimensions=1024,
            model=model,
        )

        with pytest.raises(ValueError, match="expected 1024"):
            provider.embed_query("test query")

    def test_provider_normalizes_embeddings_and_validates(self):
        """Verify provider normalizes embeddings and validates dimensions."""
        model = FakeSentenceModel(dimensions=1024)
        provider = SentenceTransformerEmbeddingProvider(
            model_name="BAAI/bge-m3",
            dimensions=1024,
            model=model,
        )

        vectors = provider.embed_documents(["English text", "French text"])

        assert len(vectors) == 2
        assert all(len(v) == 1024 for v in vectors)
        assert model.calls[0][1]["normalize_embeddings"] is True
        assert model.calls[0][1]["show_progress_bar"] is False

    def test_provider_empty_texts_returns_empty_list(self):
        """Verify provider handles empty text list gracefully."""
        model = FakeSentenceModel(dimensions=1024)
        provider = SentenceTransformerEmbeddingProvider(
            model_name="BAAI/bge-m3",
            dimensions=1024,
            model=model,
        )

        vectors = provider.embed_documents([])

        assert vectors == []


class TestOfflineEmbeddingConfiguration:
    """Test configuration-driven model selection without external calls."""

    def test_registry_provides_all_model_metadata(self):
        """Verify registry can populate UI/config without external API calls."""
        # This test proves the registry is self-contained
        for model_id, model_config in EMBEDDING_MODELS.items():
            assert model_config.model_id is not None
            assert model_config.provider in ("openai", "local")
            assert model_config.output_dimensions > 0

    def test_dimensions_derivable_from_registry(self):
        """Verify dimensions come from registry, not provider constants."""
        baai_model = get_embedding_model("BAAI/bge-m3")
        openai_model = get_embedding_model("text-embedding-3-small")

        # Dimensions should come from registry, not from provider-specific constants
        assert baai_model.output_dimensions == 1024
        assert openai_model.output_dimensions == 1536

    def test_multiple_local_models_with_different_dimensions(self):
        """Verify registry supports multiple local models with different dimensions."""
        bge_model = get_embedding_model("BAAI/bge-m3")
        miniml_model = get_embedding_model("sentence-transformers/all-MiniLM-L6-v2")

        assert bge_model.output_dimensions == 1024
        assert miniml_model.output_dimensions == 384
        assert bge_model.model_id != miniml_model.model_id


@pytest.mark.parametrize(
    ("mode", "provider", "model_id", "expected_dimensions"),
    [
        ("hosted", "openai", "text-embedding-3-small", 1536),
        ("local", "local", "BAAI/bge-m3", 1024),
    ],
)
def test_enhanced_mode_selects_registered_model_without_external_calls(
    monkeypatch, mode, provider, model_id, expected_dimensions
):
    """Hosted/local enhanced modes use configured model metadata offline."""
    monkeypatch.setenv("ENHANCED_AI_MODE", mode)
    monkeypatch.setenv("QUERY_EMBEDDING_PROVIDER", provider)
    monkeypatch.setenv("QUERY_EMBEDDING_MODEL", model_id)
    monkeypatch.delenv("QUERY_EMBEDDING_DIMENSIONS", raising=False)
    monkeypatch.delenv("OPENAI_EMBEDDING_MODEL", raising=False)

    assert search_service._effective_search_mode("semantic") == "semantic"
    assert query_embedding_providers._query_embedding_settings() == (
        provider,
        model_id,
        expected_dimensions,
    )
    assert query_embedding_providers.get_search_embedding_status()["model"] == model_id

    observed = {}
    if provider == "openai":
        monkeypatch.setenv("OPENAI_API_KEY", "test-only")

        class FakeOpenAI:
            def __init__(self, **kwargs):
                observed["client"] = kwargs
                self.embeddings = SimpleNamespace(
                    create=lambda **params: observed.update(params)
                    or SimpleNamespace(
                        data=[
                            SimpleNamespace(
                                embedding=[0.25] * expected_dimensions
                            )
                        ]
                    )
                )

        monkeypatch.setattr(query_embedding_providers, "OpenAI", FakeOpenAI)
    else:
        monkeypatch.setattr(
            query_embedding_providers,
            "_local_provider",
            lambda model, dimensions: observed.update(
                {"model": model, "dimensions": dimensions}
            )
            or SimpleNamespace(
                embed_query=lambda _text: [0.25] * dimensions
            ),
        )

    vector = query_embedding_providers.embed_query("offline test query")
    assert len(vector) == expected_dimensions
    assert observed.get("model", observed.get("model_id", model_id)) == model_id
    if provider == "openai":
        assert observed["client"] == {"api_key": "test-only"}
        assert observed["model"] == model_id
    else:
        assert observed == {"model": model_id, "dimensions": expected_dimensions}


def test_local_query_dimensions_cannot_override_registered_model_width(monkeypatch):
    monkeypatch.setenv("QUERY_EMBEDDING_PROVIDER", "local")
    monkeypatch.setenv("QUERY_EMBEDDING_MODEL", "BAAI/bge-m3")
    monkeypatch.setenv("QUERY_EMBEDDING_DIMENSIONS", "1536")
    with pytest.raises(
        query_embedding_providers.QueryEmbeddingConfigurationError,
        match="must match the registered model dimension",
    ):
        query_embedding_providers._query_embedding_settings()
