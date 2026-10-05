from types import ModuleType, SimpleNamespace
from datetime import date

import numpy as np
import pytest
from fastapi import HTTPException

from backend import embedding_providers, query_embedding_providers, routes
from backend.embedding_providers import (
    NoneEmbeddingProvider,
    OpenAIEmbeddingProvider,
    SentenceTransformerEmbeddingProvider,
)
from backend.models import CaseIngestRequest


def test_embedding_provider_contract_and_none_provider():
    provider = NoneEmbeddingProvider()
    assert isinstance(provider, embedding_providers.EmbeddingProvider)
    assert provider.embed_documents([]) == []
    with pytest.raises(RuntimeError, match="disabled"):
        provider.embed_query("private query")


def test_openai_embedding_provider_uses_fake_client_for_documents_and_queries():
    calls = []

    class FakeClient:
        embeddings = SimpleNamespace(
            create=lambda **kwargs: calls.append(kwargs)
            or SimpleNamespace(
                data=[
                    SimpleNamespace(embedding=[0.25, 0.5]),
                    SimpleNamespace(embedding=[0.75, 1.0]),
                ]
            )
        )

    provider = OpenAIEmbeddingProvider(
        "fake-embedding-model", dimensions=2, client=FakeClient()
    )
    assert provider.embed_documents(["first", "second"]) == [
        [0.25, 0.5],
        [0.75, 1.0],
    ]
    assert provider.embed_query("query") == [0.25, 0.5]
    assert calls == [
        {"input": ["first", "second"], "model": "fake-embedding-model"},
        {"input": ["query"], "model": "fake-embedding-model"},
    ]


def test_sentence_transformer_model_is_shared_per_model_and_device(monkeypatch):
    constructions = []

    class FakeModel:
        def __init__(self, name, device):
            constructions.append((name, device))

        def encode(self, texts, **kwargs):
            return np.ones((len(texts), 2), dtype=np.float32)

    fake_module = ModuleType("sentence_transformers")
    fake_module.SentenceTransformer = FakeModel
    monkeypatch.setitem(__import__("sys").modules, "sentence_transformers", fake_module)
    with SentenceTransformerEmbeddingProvider._models_lock:
        SentenceTransformerEmbeddingProvider._models.clear()

    left = SentenceTransformerEmbeddingProvider("fake/model", dimensions=2, device="cpu")
    right = SentenceTransformerEmbeddingProvider("fake/model", dimensions=2, device="cpu")
    other_device = SentenceTransformerEmbeddingProvider(
        "fake/model", dimensions=2, device="other"
    )
    assert len(left.embed_documents(["one"])) == 1
    assert right.embed_query("two") == [1.0, 1.0]
    assert other_device.embed_query("three") == [1.0, 1.0]
    assert constructions == [("fake/model", "cpu"), ("fake/model", "other")]


def test_query_embedding_never_uses_remote_provider_in_local_or_off_mode(monkeypatch):
    monkeypatch.setenv("QUERY_EMBEDDING_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    monkeypatch.setattr(
        query_embedding_providers,
        "OpenAIEmbeddingProvider",
        lambda *_args, **_kwargs: pytest.fail("remote provider constructed"),
    )
    monkeypatch.setenv("ENHANCED_AI_MODE", "local")
    with pytest.raises(HTTPException) as local_error:
        query_embedding_providers.embed_query("private query")
    assert local_error.value.status_code == 503

    monkeypatch.setenv("ENHANCED_AI_MODE", "off")
    with pytest.raises(HTTPException) as off_error:
        query_embedding_providers.embed_query("private query")
    assert off_error.value.status_code == 503


def test_ingestion_embeddings_are_disabled_by_default_mode_and_none_provider(monkeypatch):
    monkeypatch.delenv("ENHANCED_AI_MODE", raising=False)
    monkeypatch.setenv("QUERY_EMBEDDING_PROVIDER", "openai")
    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")
    monkeypatch.setattr(
        query_embedding_providers,
        "OpenAIEmbeddingProvider",
        lambda *_args, **_kwargs: pytest.fail("embedding provider constructed"),
    )
    assert query_embedding_providers.embed_case_summary("private summary") is None

    monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
    monkeypatch.setenv("QUERY_EMBEDDING_PROVIDER", "none")
    assert query_embedding_providers.embed_case_summary("private summary") is None


def test_case_summary_embedding_preserves_fixed_1536_dimension_contract(monkeypatch):
    model = SimpleNamespace(table="case_chunks", dimensions=768)
    monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
    monkeypatch.setattr(
        query_embedding_providers, "_ingest_rollout_enabled", lambda: True
    )
    monkeypatch.setattr(
        query_embedding_providers,
        "_case_embedding_settings",
        lambda: ("openai", "custom-hosted-model", 768),
    )
    monkeypatch.setattr(
        query_embedding_providers, "get_embedding_model", lambda _name: model
    )
    monkeypatch.setattr(
        query_embedding_providers,
        "get_indexed_embedding_model",
        lambda: model,
    )
    monkeypatch.setattr(
        query_embedding_providers,
        "_configured_provider",
        lambda *_args: pytest.fail("non-1536 case embedding provider must not run"),
    )

    assert query_embedding_providers.embed_case_summary("summary") is None


def test_ingest_route_does_not_call_provider_when_enhanced_mode_is_off(monkeypatch):
    class FakeDatabase:
        def add(self, _row):
            pass

        def commit(self):
            pass

        def refresh(self, _row):
            pass

    monkeypatch.setenv("ENHANCED_AI_MODE", "off")
    monkeypatch.setitem(routes.AI_ROLLOUT, "embed_on_ingest_enabled", True)
    monkeypatch.setattr(
        routes,
        "embed_case_summary",
        lambda _text: pytest.fail("off mode must not invoke the embedding provider"),
    )
    request = CaseIngestRequest(
        title="Example case",
        court="Federal Court",
        date=date(2025, 1, 1),
        summary="Private summary text",
    )

    result = routes.ingest_case(request, FakeDatabase())

    assert result.embedding is None
    assert result.processing_status == "raw"


def test_missing_openai_key_and_provider_failure_keep_http_contract(monkeypatch):
    monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
    monkeypatch.setenv("QUERY_EMBEDDING_PROVIDER", "openai")
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(HTTPException) as missing_key:
        query_embedding_providers.embed_query("query")
    assert missing_key.value.status_code == 503
    assert "OPENAI_API_KEY" in missing_key.value.detail

    monkeypatch.setenv("OPENAI_API_KEY", "fake-key")

    class FailedProvider:
        def embed_query(self, _text):
            raise RuntimeError("fake provider failure")

    monkeypatch.setattr(
        query_embedding_providers, "_configured_provider", lambda *_args: FailedProvider()
    )
    with pytest.raises(HTTPException) as failed:
        query_embedding_providers.embed_query("query")
    assert failed.value.status_code == 502
