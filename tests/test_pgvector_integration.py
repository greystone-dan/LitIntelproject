"""Real cosine SQL checks, opt-in on a disposable pgvector_ci database only.

The workflow migrates a fresh database first. Local runs skip by default;
CASELIBRARY_PGVECTOR_TESTS=1 enables checks against the isolated CI database.
Temporary tables and a rolled-back transaction keep synthetic vectors separate
from canonical chunks. No embedding model download or hosted API is needed.
"""

import os

import pytest
from sqlalchemy import Column, Integer, MetaData, Table, create_engine, select, text
from sqlalchemy.exc import OperationalError

from backend.database import CaseChunk, CaseChunkEmbedding, engine


@pytest.fixture
def vector_connection():
    if os.getenv("CASELIBRARY_PGVECTOR_TESTS") != "1":
        pytest.skip("Real pgvector tests require explicit disposable-database opt-in")
    url = engine.url
    if url.database != "pgvector_ci" or url.host not in {"localhost", "127.0.0.1"}:
        pytest.skip(
            "Real pgvector tests only use the local disposable pgvector_ci database"
        )

    test_engine = create_engine(url, connect_args={"connect_timeout": 3})
    try:
        try:
            connection = test_engine.connect()
        except OperationalError:
            pytest.skip("Disposable pgvector database is not reachable")
        with connection:
            transaction = connection.begin()
            try:
                connection.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
                yield connection
            finally:
                transaction.rollback()
    finally:
        test_engine.dispose()


@pytest.mark.parametrize("model", [CaseChunk, CaseChunkEmbedding])
def test_chunk_vectors_nearest_neighbour_order(vector_connection, model):
    vector_type = model.__table__.c.embedding.type
    width = vector_type.dim
    chunks = Table(
        "pgvector_test_chunks",
        MetaData(),
        Column("id", Integer, primary_key=True),
        Column("embedding", vector_type, nullable=False),
        prefixes=["TEMPORARY"],
    )
    chunks.create(vector_connection)
    query = [1.0, 0.0] + [0.0] * (width - 2)
    vector_connection.execute(
        chunks.insert(),
        [
            {"id": 3, "embedding": [0.0, 1.0] + [0.0] * (width - 2)},
            {"id": 2, "embedding": [1.0, 1.0] + [0.0] * (width - 2)},
            {"id": 1, "embedding": query},
        ],
    )

    # Same pgvector SQLAlchemy helper used by search_service's chunk searches.
    distance = chunks.c.embedding.cosine_distance(query).label("distance")
    rows = vector_connection.execute(
        select(chunks.c.id, distance).order_by(distance).limit(3)
    ).all()
    assert [row.id for row in rows] == [1, 2, 3]
    assert [row.distance for row in rows] == pytest.approx(
        [0.0, 1.0 - 2.0**-0.5, 1.0]
    )
