from datetime import date
from io import BytesIO
from types import SimpleNamespace

import httpx
import openai
import pytest
import requests
from docx import Document
from fastapi import HTTPException
from fastapi.testclient import TestClient

from backend import routes, search_service, text_generation_providers
from backend import query_embedding_providers
from backend.ai_mode import AI_DISABLED_MESSAGE, enhanced_mode, mode_status
from backend.main import app
from backend.models import (
	CaseSearchRequest,
	ChunkGroupSearchRequest,
	LocalChunkSearchRequest,
	ResearchRequest,
)
from backend.pages.research import research_page_html


class FakeDatabase:
	def __init__(self, rows=()):
		self.rows = list(rows)
		self.statement = None

	def execute(self, statement, *args, **kwargs):
		self.statement = statement
		if "case_chunks" in str(statement):
			case, chunk, _score = self.rows[0]
			return [(case, chunk, 0.5)]
		case, _chunk, _score = self.rows[0]
		return [(case, 0.5, 0)]

	def scalar(self, statement):
		return None


def _case():
	return SimpleNamespace(
		id=1,
		title="Example v Canada",
		court="Federal Court",
		jurisdiction="Canada",
		date=date(2026, 1, 1),
		citation="2026 FC 1",
		summary="A summary",
		full_text=None,
		issues=None,
		metadata_json=None,
		source_url=None,
		source_name="source",
	)


def _chunk():
	return SimpleNamespace(chunk_index=0, text="A relevant passage")


def test_mode_defaults_off_and_rejects_invalid_values(monkeypatch):
	monkeypatch.delenv("ENHANCED_AI_MODE", raising=False)
	assert enhanced_mode() == "off"
	assert mode_status() == {"enhanced_ai_mode": "off"}
	assert CaseSearchRequest(query="query").search_mode == "lexical"
	assert ChunkGroupSearchRequest(query="query").search_mode == "lexical"
	assert ResearchRequest(query="query").search_mode == "hybrid"

	monkeypatch.setenv("ENHANCED_AI_MODE", "remote")
	with pytest.raises(ValueError, match="off, local, hosted"):
		enhanced_mode()


def test_off_mode_downgrades_search_endpoints_without_embedding_calls(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "off")

	def fail_embedding(_text):
		raise AssertionError("off mode must not call an embedding provider")

	monkeypatch.setattr(routes, "_embed", fail_embedding)
	case = _case()
	chunk = _chunk()
	search_database = FakeDatabase([(case, 0.5, 0)])
	case_results = routes.search_cases(
		CaseSearchRequest(query="passage", search_mode="semantic"), search_database
	)
	assert case_results[0].search_mode_effective == "lexical"
	assert case_results[0].ai_disabled_reason
	assert "lexical" in str(search_database.statement.compile()).lower()

	chunk_results = routes.search_chunks(
		CaseSearchRequest(query="passage", search_mode="hybrid"),
		FakeDatabase([(case, chunk, 0.5)]),
	)
	assert chunk_results[0].search_mode_effective == "lexical"
	assert chunk_results[0].ai_disabled_reason

	grouped = routes.search_chunks_grouped(
		ChunkGroupSearchRequest(query="passage", search_mode="semantic"),
		FakeDatabase([(case, chunk, 0.5)]),
	)
	assert grouped.search_mode_effective == "lexical"
	assert grouped.ai_disabled_reason

	paragraph_results = routes.search_paragraphs(
		CaseSearchRequest(query="passage", search_mode="hybrid"),
		FakeDatabase([(case, chunk, 0.5)]),
	)
	assert paragraph_results[0].search_mode_effective == "lexical"
	assert paragraph_results[0].ai_disabled_reason


def test_off_mode_blocks_research_before_retrieval_or_generation(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "off")
	monkeypatch.setattr(
		routes, "_grouped_chunk_search",
		lambda *_args: (_ for _ in ()).throw(AssertionError("retrieval must not run")),
	)
	monkeypatch.setattr(
		routes, "get_text_generation_provider",
		lambda: (_ for _ in ()).throw(AssertionError("generation must not run")),
	)

	with pytest.raises(HTTPException) as error:
		routes.research(ResearchRequest(query="question"), db=FakeDatabase())
	assert error.value.status_code == 503
	assert error.value.detail == AI_DISABLED_MESSAGE


def test_off_mode_blocks_explicit_local_chunk_embeddings(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "off")
	monkeypatch.setattr(
		routes, "_local_embedding_provider",
		lambda *_args: (_ for _ in ()).throw(AssertionError("local embedding provider must not be constructed")),
	)
	with pytest.raises(HTTPException) as error:
		routes.search_chunks_local(
			LocalChunkSearchRequest(query="question"),
			FakeDatabase(),
		)
	assert error.value.status_code == 503


def test_off_mode_exports_remain_sql_analytics_without_ai_calls(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "off")
	monkeypatch.setattr(
		routes, "_embed",
		lambda *_args: (_ for _ in ()).throw(AssertionError("exports must not embed")),
	)
	monkeypatch.setattr(
		routes, "get_text_generation_provider",
		lambda: (_ for _ in ()).throw(AssertionError("exports must not generate")),
	)
	monkeypatch.setattr(
		routes, "fetch_analytics_search_cases",
		lambda *_args, **_kwargs: {"results": []},
	)

	csv_response = routes.export_search_analytics_cases(db=FakeDatabase())
	docx_response = routes.export_search_docx(db=FakeDatabase())

	assert csv_response.media_type == "text/csv"
	assert docx_response.media_type == (
		"application/vnd.openxmlformats-officedocument.wordprocessingml.document"
	)


def test_local_generation_provider_never_constructs_openai(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "local")
	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "openai")
	monkeypatch.setenv("QUERY_EMBEDDING_PROVIDER", "local")
	monkeypatch.setenv("QUERY_EMBEDDING_DIMENSIONS", "1536")
	monkeypatch.delenv("OPENAI_API_KEY", raising=False)
	monkeypatch.setattr(
		query_embedding_providers,
		"_local_provider",
		lambda *_args: SimpleNamespace(embed_query=lambda _text: [0.2] * 1536),
	)
	monkeypatch.setattr(
		text_generation_providers, "OpenAI",
		lambda **_kwargs: (_ for _ in ()).throw(AssertionError("OpenAI client must not be constructed")),
	)
	monkeypatch.setattr(
		query_embedding_providers, "OpenAI",
		lambda **_kwargs: (_ for _ in ()).throw(AssertionError("OpenAI client must not be constructed")),
	)

	assert isinstance(
		text_generation_providers.get_text_generation_provider(),
		text_generation_providers.OllamaChatProvider,
	)
	assert search_service._effective_search_mode("semantic") == "semantic"
	assert len(search_service._embed("local query")) == 1536


def test_hosted_mode_preserves_configured_openai_provider_through_fake(monkeypatch):
	calls = {}
	monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
	monkeypatch.setenv("TEXT_GENERATION_PROVIDER", "openai")
	monkeypatch.setenv("OPENAI_API_KEY", "test-key")

	class FakeOpenAI:
		def __init__(self, **kwargs):
			calls["client"] = kwargs
			self.chat = SimpleNamespace(
				completions=SimpleNamespace(
					create=lambda **payload: calls.update(payload) or "fake completion"
				)
			)

	monkeypatch.setattr(text_generation_providers, "OpenAI", FakeOpenAI)
	provider = text_generation_providers.get_text_generation_provider()
	result = provider.create_chat_completion(model=provider.model_name, messages=[])

	assert isinstance(provider, text_generation_providers.OpenAIChatProvider)
	assert calls["client"] == {"api_key": "test-key"}
	assert calls["model"] == "gpt-4o-mini"
	assert result == "fake completion"


def test_mode_changes_from_environment_and_status_is_exposed(monkeypatch):
	monkeypatch.setenv("ENHANCED_AI_MODE", "hosted")
	assert routes.get_ai_mode() == {"enhanced_ai_mode": "hosted"}
	assert any(route.path == "/api/ai-mode" for route in routes.router.routes)


def test_research_page_displays_server_disabled_message():
	html = research_page_html()

	assert "if (!response.ok)" in html
	assert "body.detail || response.statusText" in html
	assert "resultSection" in html


def test_default_search_and_memo_endpoints_make_no_model_calls(monkeypatch):
	monkeypatch.delenv("ENHANCED_AI_MODE", raising=False)
	monkeypatch.delenv("QUERY_EMBEDDING_PROVIDER", raising=False)
	monkeypatch.delenv("QUERY_EMBEDDING_MODEL", raising=False)
	monkeypatch.delenv("OPENAI_API_KEY", raising=False)
	case = _case()
	chunk = _chunk()
	monkeypatch.setitem(app.dependency_overrides, routes.get_db, lambda: FakeDatabase([(case, chunk, 0.5)]))
	monkeypatch.setattr(routes, "fetch_analytics_search_cases", lambda *_args, **_kwargs: {"results": []})
	monkeypatch.setattr(routes, "get_text_generation_provider", lambda: pytest.fail("generation provider constructed"))

	def fail_model_call(*_args, **_kwargs):
		raise AssertionError("default mode must not call or construct an AI provider")

	monkeypatch.setattr(openai, "OpenAI", fail_model_call)
	monkeypatch.setattr(text_generation_providers, "OpenAI", fail_model_call)
	monkeypatch.setattr(query_embedding_providers, "OpenAI", fail_model_call)
	monkeypatch.setattr(query_embedding_providers, "embed_query", fail_model_call)
	monkeypatch.setattr(
		query_embedding_providers, "SentenceTransformerEmbeddingProvider", fail_model_call
	)
	monkeypatch.setattr(
		query_embedding_providers,
		"_local_provider",
		lambda *_args: fail_model_call(),
	)
	assert query_embedding_providers.get_search_embedding_status()["query_provider"] == "none"
	monkeypatch.setattr(search_service, "SentenceTransformerEmbeddingProvider", fail_model_call)
	monkeypatch.setattr(routes, "_local_embedding_provider", fail_model_call)
	monkeypatch.setattr(httpx, "post", fail_model_call)
	monkeypatch.setattr(requests, "post", fail_model_call)

	document = Document()
	document.add_paragraph("This private note contains no citations or legal issues.")
	uploaded = BytesIO()
	document.save(uploaded)
	client = TestClient(app)

	assert client.get("/api/ai-mode").json() == {"enhanced_ai_mode": "off"}
	assert client.get("/analytics/search/cases", params={"query": "private name"}).status_code == 200

	for mode in ("semantic", "hybrid"):
		response = client.post(
			"/search",
			json={"query": "private name", "search_mode": mode},
		)
		assert response.status_code == 200, response.text
		assert response.json()[0]["search_mode_effective"] == "lexical"
		assert response.json()[0]["ai_disabled_reason"]

		chunk_response = client.post(
			"/search/chunks",
			json={"query": "private name", "search_mode": mode},
		)
		assert chunk_response.status_code == 200, chunk_response.text
		assert chunk_response.json()[0]["search_mode_effective"] == "lexical"
		assert chunk_response.json()[0]["ai_disabled_reason"]

	assert client.post("/search", json={"query": "private name"}).json()[0][
		"search_mode_effective"
	] == "lexical"
	assert client.post("/search/chunks", json={"query": "private name"}).json()[0][
		"search_mode_effective"
	] == "lexical"
	assert client.get("/search/export.csv", params={"query": "private name"}).status_code == 200
	assert client.get("/search/export.docx", params={"query": "private name"}).status_code == 200
	research_response = client.post("/research", json={"query": "private question"})
	assert research_response.status_code == 503
	assert research_response.json()["detail"] == AI_DISABLED_MESSAGE
	memo_response = client.post(
		"/memo-citation-check",
		files={
			"file": (
				"memo.docx",
				uploaded.getvalue(),
				"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
			)
		},
	)
	assert memo_response.status_code == 200, memo_response.text
