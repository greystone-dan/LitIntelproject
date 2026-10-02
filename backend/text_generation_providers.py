from __future__ import annotations

import os
from types import SimpleNamespace
from typing import Any

import httpx
from openai import OpenAI


DEFAULT_OLLAMA_BASE_URL = "http://127.0.0.1:11434/v1"
DEFAULT_OLLAMA_MODEL = "qwen3:4b"


class TextGenerationConfigurationError(ValueError):
	"""Raised when the selected text-generation provider is not configured."""


class ChatGenerationProvider:
	model_name: str

	def create_chat_completion(self, **kwargs: Any) -> Any:
		raise NotImplementedError


class OpenAIChatProvider(ChatGenerationProvider):
	def __init__(self, *, api_key: str, model_name: str) -> None:
		organization = os.environ.pop("OPENAI_ORG_ID", None)
		try:
			self.client = OpenAI(api_key=api_key)
		finally:
			if organization is not None:
				os.environ["OPENAI_ORG_ID"] = organization
		self.model_name = model_name

	def create_chat_completion(self, **kwargs: Any) -> Any:
		return self.client.chat.completions.create(**kwargs)


class OllamaChatProvider(ChatGenerationProvider):
	def __init__(self, *, base_url: str, model_name: str) -> None:
		self.base_url = base_url.rstrip("/")
		self.model_name = model_name

	def create_chat_completion(self, **kwargs: Any) -> Any:
		messages = kwargs.get("messages")
		if isinstance(messages, list):
			messages = [dict(message) for message in messages]
		else:
			messages = []
		payload: dict[str, Any] = {
			"model": kwargs.get("model", self.model_name),
			"messages": messages,
			"stream": False,
			"think": False,
			"options": {"temperature": kwargs.get("temperature", 0.0)},
		}
		if "max_tokens" in kwargs:
			payload["options"]["num_predict"] = kwargs["max_tokens"]
		if kwargs.get("response_format") == {"type": "json_object"}:
			payload["format"] = "json"

		api_url = self.base_url.removesuffix("/v1") + "/api/chat"
		response = httpx.post(api_url, json=payload, timeout=120.0)
		response.raise_for_status()
		data = response.json()
		message = data.get("message", {})
		return SimpleNamespace(
			choices=[SimpleNamespace(message=SimpleNamespace(content=message.get("content", "")))],
			usage=SimpleNamespace(
				prompt_tokens=data.get("prompt_eval_count", 0),
				completion_tokens=data.get("eval_count", 0),
			),
		)


def get_text_generation_provider() -> ChatGenerationProvider:
	provider_name = os.getenv("TEXT_GENERATION_PROVIDER", "openai").strip().lower()
	if provider_name == "local":
		return OllamaChatProvider(
			base_url=os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL),
			model_name=os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL),
		)
	if provider_name != "openai":
		raise TextGenerationConfigurationError(
			"TEXT_GENERATION_PROVIDER must be 'openai' or 'local'"
		)

	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		raise TextGenerationConfigurationError("OPENAI_API_KEY is not configured")
	return OpenAIChatProvider(
		api_key=api_key,
		model_name=os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini"),
	)
