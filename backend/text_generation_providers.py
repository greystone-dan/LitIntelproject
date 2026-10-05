from __future__ import annotations

import ipaddress
import os
from types import SimpleNamespace
from urllib.parse import urlsplit
from typing import Any

import httpx
from openai import OpenAI

from .ai_mode import enhanced_mode

DEFAULT_OLLAMA_BASE_URL = "http://127.0.0.1:11434/v1"
DEFAULT_OLLAMA_MODEL = "qwen3:4b"
_DEFAULT_CHAT_TIMEOUT_SECONDS = 60.0


class TextGenerationConfigurationError(ValueError):
	"""Raised when the selected text-generation provider is not configured."""


class ChatGenerationProvider:
	model_name: str
	max_context_chars: int
	default_max_tokens: int | None
	supports_json_mode: bool

	def create_chat_completion(self, **kwargs: Any) -> Any:
		raise NotImplementedError


class OpenAIChatProvider(ChatGenerationProvider):
	max_context_chars = 12_000
	default_max_tokens = None
	supports_json_mode = True

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


class OpenAICompatibleChatProvider(ChatGenerationProvider):
	max_context_chars = 12_000
	default_max_tokens = None
	supports_json_mode = True

	def __init__(
		self, *, base_url: str, api_key: str | None, model_name: str, timeout_seconds: float
	) -> None:
		self.base_url = base_url.rstrip("/")
		self.model_name = model_name
		# The SDK requires a key even when a compatible local endpoint does not.
		self.client = OpenAI(
			api_key=api_key or "not-needed",
			base_url=self.base_url,
			timeout=timeout_seconds,
		)

	def create_chat_completion(self, **kwargs: Any) -> Any:
		return self.client.chat.completions.create(**kwargs)


class OllamaChatProvider(ChatGenerationProvider):
	max_context_chars = 4_000
	default_max_tokens = 256
	supports_json_mode = True

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


def _is_local_or_private_url(url: str) -> bool:
	try:
		host = urlsplit(url).hostname
	except ValueError:
		return False
	if not host:
		return False
	host = host.rstrip(".").lower()
	if host == "localhost" or host.endswith((".localhost", ".local")):
		return True
	try:
		address = ipaddress.ip_address(host)
	except ValueError:
		return False
	return address.is_private or address.is_loopback or address.is_link_local


def _compatible_provider(mode: str) -> OpenAICompatibleChatProvider:
	base_url = os.getenv("CHAT_BASE_URL", "").strip()
	if not base_url:
		raise TextGenerationConfigurationError("CHAT_BASE_URL is not configured")
	local_endpoint = _is_local_or_private_url(base_url)
	if local_endpoint != (mode == "local"):
		expected = "localhost/private" if mode == "local" else "hosted"
		raise TextGenerationConfigurationError(
			f"CHAT_BASE_URL must identify a {expected} endpoint in enhanced {mode} mode"
		)
	try:
		timeout_seconds = float(
			os.getenv("CHAT_TIMEOUT_SECONDS", str(_DEFAULT_CHAT_TIMEOUT_SECONDS))
		)
		if timeout_seconds <= 0:
			raise ValueError
	except ValueError as exc:
		raise TextGenerationConfigurationError(
			"CHAT_TIMEOUT_SECONDS must be a positive number"
		) from exc
	return OpenAICompatibleChatProvider(
		base_url=base_url,
		api_key=os.getenv("CHAT_API_KEY"),
		model_name=os.getenv("CHAT_MODEL", "gpt-4o-mini"),
		timeout_seconds=timeout_seconds,
	)


def get_text_generation_provider() -> ChatGenerationProvider:
	mode = enhanced_mode()
	if mode == "off":
		raise TextGenerationConfigurationError("AI answers are disabled in this deployment")
	provider_name = os.getenv("TEXT_GENERATION_PROVIDER", "openai").strip().lower()
	valid_names = ("openai", "local", "openai_compatible")
	if provider_name not in valid_names:
		raise TextGenerationConfigurationError(
			"TEXT_GENERATION_PROVIDER must be one of: " + ", ".join(valid_names)
		)
	if mode == "local":
		if provider_name == "openai_compatible":
			return _compatible_provider(mode)
		return OllamaChatProvider(
			base_url=os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL),
			model_name=os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL),
		)
	if provider_name == "local":
		return OllamaChatProvider(
			base_url=os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL),
			model_name=os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL),
		)
	if provider_name == "openai_compatible":
		return _compatible_provider(mode)

	api_key = os.getenv("OPENAI_API_KEY")
	if not api_key:
		raise TextGenerationConfigurationError("OPENAI_API_KEY is not configured")
	return OpenAIChatProvider(
		api_key=api_key,
		model_name=os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini"),
	)
