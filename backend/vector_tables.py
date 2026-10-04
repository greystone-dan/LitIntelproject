"""Scaffold SQLAlchemy vector tables from explicit embedding-registry entries.

This module only constructs SQLAlchemy metadata and compiles DDL. It has no
database engine/session dependency and does not execute DDL. A future registry
can provide mappings with ``model_name``, ``model_version``, a
``chunk_embeddings_<slug>`` table name, ``dimensions`` and optional schema,
chunk-reference, vector-column, and index settings.
"""

from __future__ import annotations

import re
from collections.abc import Mapping
from typing import Any

from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, ForeignKey, Index, Integer, MetaData, String, Table
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateIndex, CreateTable

_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_VECTOR_TABLE_NAME = re.compile(r"^chunk_embeddings_[a-z0-9]+(?:_[a-z0-9]+)*$")
_INDEX_METHODS = {"hnsw", "ivfflat"}
_OPERATOR_CLASSES = {
    "cosine": "vector_cosine_ops",
    "l2": "vector_l2_ops",
    "inner_product": "vector_ip_ops",
}
_INDEX_PARAMETERS = {
    "hnsw": {"m", "ef_construction"},
    "ivfflat": {"lists"},
}


def _identifier(value: Any, field: str) -> str:
    if not isinstance(value, str) or not _IDENTIFIER.fullmatch(value):
        raise ValueError(f"{field} must be a simple SQL identifier")
    return value


def build_vector_table(entry: Mapping[str, Any]) -> tuple[Table, Index]:
    """Build one model-specific vector table and its PostgreSQL ANN index.

    Registry entries are mappings; the model name is descriptive while
    ``table_name`` is an explicit, stable SQL identifier. Dimensions are fixed
    in the resulting ``Vector`` type. The chunk foreign key is represented in
    metadata but is never resolved against or applied to a database.
    """
    if not isinstance(entry, Mapping):
        raise ValueError("registry entry must be a mapping")

    model_name = entry.get("model_name")
    if not isinstance(model_name, str) or not model_name.strip():
        raise ValueError("model_name must be a non-empty string")
    model_version = entry.get("model_version")
    if not isinstance(model_version, str) or not model_version.strip():
        raise ValueError("model_version must be a non-empty string")

    table_name = _identifier(entry.get("table_name"), "table_name")
    if not _VECTOR_TABLE_NAME.fullmatch(table_name):
        raise ValueError("table_name must match 'chunk_embeddings_<slug>'")
    vector_column = _identifier(entry.get("vector_column", "embedding"), "vector_column")
    chunk_table = _identifier(entry.get("chunk_table", "case_chunks"), "chunk_table")
    chunk_id_column = _identifier(
        entry.get("chunk_id_column", "chunk_id"), "chunk_id_column"
    )
    source_chunk_id_column = _identifier(
        entry.get("source_chunk_id_column", "id"), "source_chunk_id_column"
    )
    schema = entry.get("schema")
    if schema is not None:
        schema = _identifier(schema, "schema")
    chunk_schema = entry.get("chunk_schema", schema)
    if chunk_schema is not None:
        chunk_schema = _identifier(chunk_schema, "chunk_schema")
    if table_name == chunk_table and schema == chunk_schema:
        raise ValueError("vector table must be distinct from its chunk source table")

    dimensions = entry.get("dimensions")
    if isinstance(dimensions, bool) or not isinstance(dimensions, int) or dimensions <= 0:
        raise ValueError("dimensions must be a positive integer")

    index_options = entry.get("index", {})
    if not isinstance(index_options, Mapping):
        raise ValueError("index must be a mapping")
    method = index_options.get("method", "hnsw")
    if not isinstance(method, str) or method not in _INDEX_METHODS:
        raise ValueError("index.method must be 'hnsw' or 'ivfflat'")
    metric = index_options.get("metric", "cosine")
    if not isinstance(metric, str) or metric not in _OPERATOR_CLASSES:
        raise ValueError("index.metric must be cosine, l2, or inner_product")

    parameters = index_options.get("parameters", {})
    if not isinstance(parameters, Mapping):
        raise ValueError("index.parameters must be a mapping")
    allowed_parameters = _INDEX_PARAMETERS[method]
    unsupported_parameters = set(parameters) - allowed_parameters
    if any(not isinstance(key, str) for key in parameters) or unsupported_parameters:
        raise ValueError(
            f"unsupported {method} index parameters: "
            f"{', '.join(sorted(str(key) for key in unsupported_parameters))}"
        )
    for key, value in parameters.items():
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"index.parameters.{key} must be a positive integer")

    parent = f"{chunk_schema}.{chunk_table}" if chunk_schema else chunk_table
    metadata = MetaData()
    # Register a metadata-only parent so the foreign key compiles without
    # importing application ORM models or opening a database connection.
    Table(
        chunk_table,
        metadata,
        Column(source_chunk_id_column, Integer, primary_key=True),
        schema=chunk_schema,
    )
    table = Table(
        table_name,
        metadata,
        Column(
            chunk_id_column,
            Integer,
            ForeignKey(f"{parent}.{source_chunk_id_column}", ondelete="CASCADE"),
            primary_key=True,
        ),
        Column(vector_column, Vector(dimensions), nullable=False),
        Column("model_name", String, nullable=False, default=model_name.strip()),
        Column("model_version", String, nullable=False, default=model_version.strip()),
        schema=schema,
        comment=f"Embedding vectors for {model_name.strip()}",
    )

    index_name = _identifier(
        index_options.get(
            "name", f"ix_{table_name}_{vector_column}_{method}"
        ),
        "index.name",
    )
    index = Index(
        index_name,
        table.c[vector_column],
        postgresql_using=method,
        postgresql_ops={vector_column: _OPERATOR_CLASSES[metric]},
        postgresql_with=dict(parameters) or None,
    )
    return table, index


def compile_vector_table_ddl(
    entry: Mapping[str, Any], dialect: Any | None = None
) -> tuple[str, str]:
    """Compile ``CREATE TABLE`` and ``CREATE INDEX`` strings without execution."""
    table, index = build_vector_table(entry)
    dialect = dialect or postgresql.dialect()
    return (
        str(CreateTable(table).compile(dialect=dialect)),
        str(CreateIndex(index).compile(dialect=dialect)),
    )
