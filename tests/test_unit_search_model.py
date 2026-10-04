from types import SimpleNamespace

from backend import embedding_providers, unit_search
from backend.embedding_providers import DEFAULT_LOCAL_EMBEDDING_MODEL


class FakeResult:
    def __init__(self, rows):
        self.rows = rows

    def all(self):
        return self.rows


class FakeSession:
    def __init__(self, rows):
        self.rows = rows
        self.statements = []

    def execute(self, statement):
        self.statements.append(statement)
        return FakeResult(self.rows)


def install_fake_embedding_provider(monkeypatch):
    model_names = []

    class FakeEmbeddingProvider:
        def __init__(self, model_name):
            model_names.append(model_name)

        def embed_query(self, query):
            return [0.1, 0.2]

    monkeypatch.setattr(
        embedding_providers,
        "SentenceTransformerEmbeddingProvider",
        FakeEmbeddingProvider,
    )
    return model_names


def test_semantic_search_uses_stored_model_name_and_skips_keyword_fallback(
    monkeypatch,
):
    model_names = install_fake_embedding_provider(monkeypatch)
    session = FakeSession(
        [SimpleNamespace(case_id=1, text="Procedural fairness", distance=0.2)]
    )
    monkeypatch.setattr(
        unit_search,
        "get_unit_judge_analytics",
        lambda case_id, unit_index, db: {"judges": [], "disposition": None},
    )
    monkeypatch.setattr(
        unit_search, "_map_chunk_to_unit", lambda case_id, indices, db: (0, 0, 0, "")
    )
    def unexpected_fallback(*args):
        raise AssertionError("unexpected keyword fallback")

    monkeypatch.setattr(unit_search, "_keyword_search", unexpected_fallback)

    results = unit_search.search_units_by_embedding("fairness", session)

    assert model_names == [DEFAULT_LOCAL_EMBEDDING_MODEL]
    statement = session.statements[0]
    compiled = statement.compile()
    assert "model_name =" in str(compiled)
    assert DEFAULT_LOCAL_EMBEDDING_MODEL in compiled.params.values()
    assert len(results) == 1
    assert results[0].match_type == "semantic"


def test_semantic_search_uses_keyword_fallback_only_when_no_matches(monkeypatch):
    model_names = install_fake_embedding_provider(monkeypatch)
    session = FakeSession([])
    fallback_result = [object()]
    fallback_calls = []

    def keyword_search(query, db, limit):
        fallback_calls.append((query, db, limit))
        return fallback_result

    monkeypatch.setattr(unit_search, "_keyword_search", keyword_search)

    results = unit_search.search_units_by_embedding("fairness", session, limit=3)

    assert model_names == [DEFAULT_LOCAL_EMBEDDING_MODEL]
    assert fallback_calls == [("fairness", session, 3)]
    assert results is fallback_result
