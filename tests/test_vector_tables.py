"""Pure SQL-compilation tests; these tests never create an engine or connect."""

import pytest

from backend.vector_tables import build_vector_table, compile_vector_table_ddl


def _entry(**overrides):
    entry = {
        "model_name": "example/embed-v1",
        "model_version": "v1",
        "table_name": "chunk_embeddings_example_v1",
        "dimensions": 1536,
        "index": {
            "name": "ix_example_v1_embedding_hnsw",
            "method": "hnsw",
            "metric": "cosine",
            "parameters": {"m": 16, "ef_construction": 64},
        },
    }
    entry.update(overrides)
    return entry


def test_registry_entry_builds_dimensioned_table_and_compilable_index_ddl():
    table, index = build_vector_table(_entry())
    assert table.name == "chunk_embeddings_example_v1"
    assert table.c.embedding.type.dim == 1536
    assert table.c.chunk_id.primary_key
    assert table.c.model_name.nullable is False
    assert table.c.model_version.nullable is False
    assert table.c.model_name.default.arg == "example/embed-v1"
    assert table.c.model_version.default.arg == "v1"
    assert index.name == "ix_example_v1_embedding_hnsw"

    create_table_sql, create_index_sql = compile_vector_table_ddl(_entry())
    assert "chunk_embeddings_example_v1" in create_table_sql
    assert "VECTOR(1536)" in create_table_sql
    assert "REFERENCES case_chunks (id)" in create_table_sql
    assert "model_name VARCHAR NOT NULL" in create_table_sql
    assert "model_version VARCHAR NOT NULL" in create_table_sql
    assert "USING hnsw" in create_index_sql
    assert "vector_cosine_ops" in create_index_sql
    assert "WITH (m = 16, ef_construction = 64)" in create_index_sql


def test_schema_and_metric_are_compiled_from_the_registry_entry():
    table_sql, index_sql = compile_vector_table_ddl(
        _entry(
            schema="embeddings",
            chunk_schema="public",
            dimensions=1024,
            index={
                "method": "ivfflat",
                "metric": "l2",
                "parameters": {"lists": 100},
            },
        )
    )
    assert "embeddings.chunk_embeddings_example_v1" in table_sql
    assert "VECTOR(1024)" in table_sql
    assert "REFERENCES public.case_chunks (id)" in table_sql
    assert "USING ivfflat" in index_sql
    assert "vector_l2_ops" in index_sql
    assert "WITH (lists = 100)" in index_sql


@pytest.mark.parametrize(
    ("entry", "message"),
    [
        (_entry(dimensions=True), "dimensions"),
        (_entry(dimensions=0), "dimensions"),
        (_entry(table_name="not-a-safe-name"), "table_name"),
        (_entry(table_name="arbitrary_embeddings"), "chunk_embeddings"),
        (_entry(table_name="case_chunk_embeddings_example_v1"), "chunk_embeddings"),
        (
            _entry(
                table_name="chunk_embeddings_example_v1",
                chunk_table="chunk_embeddings_example_v1",
            ),
            "distinct",
        ),
        (_entry(model_version=""), "model_version"),
        (_entry(index={"method": "unknown"}), "index.method"),
        (
            _entry(index={"method": "hnsw", "parameters": {"lists": 8}}),
            "unsupported hnsw",
        ),
    ],
)
def test_invalid_registry_entries_are_rejected(entry, message):
    with pytest.raises(ValueError, match=message):
        build_vector_table(entry)
