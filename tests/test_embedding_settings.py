from __future__ import annotations

import importlib
import os
import sys
from types import ModuleType, SimpleNamespace


def _reload_settings(monkeypatch):
    import dotenv

    monkeypatch.setattr(dotenv, "load_dotenv", lambda *args, **kwargs: True)
    import backend.settings as settings_module

    return importlib.reload(settings_module)


def _install_stub_numpy(monkeypatch):
    monkeypatch.setitem(sys.modules, "numpy", ModuleType("numpy"))


def _install_stub_openai(monkeypatch):
    fake_openai = ModuleType("openai")
    fake_openai.OpenAI = object
    fake_openai.OpenAIError = Exception
    monkeypatch.setitem(sys.modules, "openai", fake_openai)


def test_embedding_settings_reads_organization_and_device(monkeypatch):
    monkeypatch.setenv("OPENAI_ORG_ID", "org-test")
    monkeypatch.setenv("LOCAL_EMBEDDING_DEVICE", "cuda:0")

    settings_module = _reload_settings(monkeypatch)

    assert settings_module.settings.embedding.organization == "org-test"
    assert settings_module.settings.embedding.device == "cuda:0"


def test_search_service_suppresses_openai_org_and_restores_env(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    monkeypatch.setenv("OPENAI_ORG_ID", "org-test")

    settings_module = _reload_settings(monkeypatch)
    _install_stub_numpy(monkeypatch)
    _install_stub_openai(monkeypatch)
    import backend.search_service as search_service

    importlib.reload(search_service)

    captured = {}

    class FakeEmbeddings:
        def create(self, *, input, model):
            return SimpleNamespace(
                data=[SimpleNamespace(embedding=[0.0] * search_service.EMBEDDING_DIMENSIONS)]
            )

    class FakeOpenAI:
        def __init__(self, **kwargs):
            captured.update(kwargs)
            self.embeddings = FakeEmbeddings()

    monkeypatch.setattr(search_service, "OpenAI", FakeOpenAI)

    embedding = search_service._embed("hello")

    assert captured == {"api_key": "sk-test"}
    assert embedding == [0.0] * settings_module.settings.embedding.dimensions
    assert os.getenv("OPENAI_ORG_ID") == "org-test"


def test_search_service_restores_openai_org_when_constructor_fails(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    monkeypatch.setenv("OPENAI_ORG_ID", "org-test")

    _reload_settings(monkeypatch)
    _install_stub_numpy(monkeypatch)
    _install_stub_openai(monkeypatch)
    import backend.search_service as search_service

    importlib.reload(search_service)

    class FailingOpenAI:
    	def __init__(self, **kwargs):
    		assert kwargs == {"api_key": "sk-test"}
    		raise search_service.OpenAIError("boom")

    monkeypatch.setattr(search_service, "OpenAI", FailingOpenAI)

    try:
    	search_service._embed("hello")
    except search_service.HTTPException as exc:
    	assert exc.status_code == search_service.status.HTTP_502_BAD_GATEWAY
    else:
    	raise AssertionError("Expected HTTPException")

    assert os.getenv("OPENAI_ORG_ID") == "org-test"


def test_sentence_transformer_provider_uses_grouped_embedding_device(monkeypatch):
    monkeypatch.setenv("LOCAL_EMBEDDING_DEVICE", "mps")

    _reload_settings(monkeypatch)
    _install_stub_numpy(monkeypatch)
    import backend.embedding_providers as embedding_providers

    importlib.reload(embedding_providers)

    provider = embedding_providers.SentenceTransformerEmbeddingProvider(model={})

    assert provider.device == "mps"
