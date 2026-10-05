from pathlib import Path
from types import SimpleNamespace

import pytest

from backend import routes, text_generation_providers as providers
from backend.models import ResearchRequest


def test_local_provider_uses_ollama_openai_compatible_settings(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "local")
	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "local")
	monkeypatch.setenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
	monkeypatch.setenv("OLLAMA_MODEL", "qwen2.5:7b")

	provider = providers.get_text_generation_provider()

	assert isinstance(provider, providers.OllamaChatProvider)
	assert provider.model_name == "qwen2.5:7b"
	assert provider.base_url == "http://localhost:11434/v1"


def test_local_provider_forwards_chat_completion(monkeypatch):
	calls = {}

	class FakeResponse:
		def raise_for_status(self):
			return None

		def json(self):
			return {"message": {"content": "ok"}, "prompt_eval_count": 2, "eval_count": 3}

	def fake_post(url, **kwargs):
		calls["url"] = url
		calls.update(kwargs["json"])
		return FakeResponse()

	monkeypatch.setattr(providers.httpx, "post", fake_post)
	monkeypatch.setenv("ENHANCED_AI_MODE", "local")
	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "local")
	monkeypatch.delenv("OLLAMA_MODEL", raising=False)

	provider = providers.get_text_generation_provider()
	completion = provider.create_chat_completion(model=provider.model_name, messages=[], max_tokens=10)

	assert calls["url"] == "http://127.0.0.1:11434/api/chat"
	assert calls["think"] is False
	assert calls["options"]["num_predict"] == 10
	assert completion.choices[0].message.content == "ok"


def test_local_provider_disables_qwen_thinking_for_text_output(monkeypatch):
	calls = {}

	class FakeResponse:
		def raise_for_status(self):
			return None

		def json(self):
			return {"message": {"content": "ok"}}

	def fake_post(url, **kwargs):
		calls.update(kwargs["json"])
		return FakeResponse()

	monkeypatch.setattr(providers.httpx, "post", fake_post)
	monkeypatch.setenv("ENHANCED_AI_MODE", "local")
	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "local")

	provider = providers.get_text_generation_provider()
	provider.create_chat_completion(
		model=provider.model_name,
		messages=[{"role": "user", "content": "Summarize this paragraph."}],
	)

	assert calls["think"] is False


def test_openai_remains_default_and_requires_key(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
	monkeypatch.delenv("TEXT_GENERATION_PROVIDER", raising=False)
	monkeypatch.delenv("OPENAI_API_KEY", raising=False)

	with pytest.raises(providers.TextGenerationConfigurationError, match="OPENAI_API_KEY"):
		providers.get_text_generation_provider()


def test_unknown_provider_is_rejected(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "unknown")

	with pytest.raises(providers.TextGenerationConfigurationError, match="openai.*local"):
		providers.get_text_generation_provider()


def test_research_route_uses_selected_provider(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
	search_result = SimpleNamespace(
		cases=[
			SimpleNamespace(
				id=42,
				title="Example v Canada",
				citation="2024 FC 1",
				date=None,
				court="FC",
				source_url=None,
				chunks=[SimpleNamespace(chunk_text="The court considered reasonableness.")],
			)
		]
	)
	calls = {}

	class FakeResponse:
		def raise_for_status(self):
			return None

		def json(self):
			return {"message": {"content": "local answer"}, "prompt_eval_count": 3, "eval_count": 2}

	def fake_post(url, **kwargs):
		calls["url"] = url
		calls.update(kwargs["json"])
		return FakeResponse()

	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "local")
	monkeypatch.setenv("OLLAMA_MODEL", "qwen2.5:7b")
	monkeypatch.setattr(routes, "_grouped_chunk_search", lambda search, db: search_result)
	monkeypatch.setattr(providers.httpx, "post", fake_post)

	response = routes.research(ResearchRequest(query="reasonableness"), db=object())

	assert response.model_used == "qwen2.5:7b"
	assert response.prompt_version == "v1"
	assert response.answer == "local answer"
	assert calls["model"] == "qwen2.5:7b"
	assert calls["think"] is False


def test_research_route_uses_grouped_chat_provider_setting():
	source = Path("backend/routes.py").read_text()

	assert 'settings.chat.provider.strip().lower() == "local"' in source
