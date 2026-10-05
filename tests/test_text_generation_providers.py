from types import SimpleNamespace

import httpx
import pytest
from openai import OpenAI

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

	with pytest.raises(
		providers.TextGenerationConfigurationError,
		match="openai.*local.*openai_compatible",
	):
		providers.get_text_generation_provider()


def test_off_mode_does_not_construct_a_generation_provider(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "off")
	monkeypatch.setattr(
		providers, "OpenAI",
		lambda **_kwargs: pytest.fail("generation provider must not be constructed"),
	)

	with pytest.raises(providers.TextGenerationConfigurationError, match="disabled"):
		providers.get_text_generation_provider()


def test_compatible_provider_uses_mocked_http_endpoint(monkeypatch):
	requests = []
	client_options = {}

	def respond(request):
		requests.append(request)
		return httpx.Response(
			200,
			json={
				"id": "chatcmpl-test",
				"object": "chat.completion",
				"created": 0,
				"model": "fixture-model",
				"choices": [
					{
						"index": 0,
						"message": {"role": "assistant", "content": "compatible answer"},
						"finish_reason": "stop",
					}
				],
				"usage": {"prompt_tokens": 2, "completion_tokens": 2, "total_tokens": 4},
			},
		)

	def mocked_client(**kwargs):
		client_options.update({key: value for key, value in kwargs.items() if key != "http_client"})
		kwargs["http_client"] = httpx.Client(transport=httpx.MockTransport(respond))
		return OpenAI(**kwargs)

	monkeypatch.setattr(providers, "OpenAI", mocked_client)
	monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "openai_compatible")
	monkeypatch.setenv("CHAT_BASE_URL", "https://chat.example.test/v1")
	monkeypatch.delenv("CHAT_API_KEY", raising=False)
	monkeypatch.setenv("CHAT_MODEL", "fixture-model")
	monkeypatch.setenv("CHAT_TIMEOUT_SECONDS", "17")

	provider = providers.get_text_generation_provider()
	result = provider.create_chat_completion(
		model=provider.model_name,
		messages=[{"role": "user", "content": "test"}],
	)

	assert isinstance(provider, providers.OpenAICompatibleChatProvider)
	assert provider.max_context_chars == routes._CONTEXT_CHAR_LIMIT
	assert provider.default_max_tokens is None
	assert provider.supports_json_mode is True
	assert result.choices[0].message.content == "compatible answer"
	assert requests[0].url.path == "/v1/chat/completions"
	assert client_options == {
		"api_key": "not-needed",
		"base_url": "https://chat.example.test/v1",
		"timeout": 17.0,
	}
	assert requests[0].read()
	provider.client.close()


def test_compatible_provider_is_local_only_for_private_urls(monkeypatch):
	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "openai_compatible")
	monkeypatch.setenv("ENHANCED_AI_MODE", "local")
	monkeypatch.setenv("CHAT_BASE_URL", "http://192.168.1.20:8080/v1")

	provider = providers.get_text_generation_provider()
	assert isinstance(provider, providers.OpenAICompatibleChatProvider)

	monkeypatch.setenv("CHAT_BASE_URL", "https://chat.example.test/v1")
	with pytest.raises(providers.TextGenerationConfigurationError, match="localhost/private"):
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

	class FakeProvider:
		model_name = "qwen2.5:7b"
		max_context_chars = 20
		default_max_tokens = routes._LOCAL_RAG_MAX_TOKENS
		supports_json_mode = True

		def create_chat_completion(self, **kwargs):
			calls.update(kwargs)
			return SimpleNamespace(
				choices=[SimpleNamespace(message=SimpleNamespace(content="local answer"))],
				usage=SimpleNamespace(prompt_tokens=3, completion_tokens=2),
			)

	monkeypatch.setattr(routes, "_grouped_chunk_search", lambda search, db: search_result)
	monkeypatch.setattr(routes, "get_text_generation_provider", lambda: FakeProvider())

	response = routes.research(ResearchRequest(query="reasonableness"), db=object())

	assert response.model_used == "qwen2.5:7b"
	assert response.prompt_version == "v1"
	assert response.answer == "local answer"
	assert calls["model"] == "qwen2.5:7b"
	assert calls["max_tokens"] == routes._LOCAL_RAG_MAX_TOKENS
	assert "[Context truncated" in calls["messages"][1]["content"]
