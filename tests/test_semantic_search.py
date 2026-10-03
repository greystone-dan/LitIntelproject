"""
Test semantic search embedding functionality.

Full integration tests (query execution against database) require a live Postgres database
and are deselected in CI. These tests focus on the embedding provider and output validation.
"""

import pytest

from backend.embedding_providers import SentenceTransformerEmbeddingProvider


@pytest.fixture
def embedding_provider():
    """Initialize the embedding provider for tests."""
    return SentenceTransformerEmbeddingProvider(
        model_name="BAAI/bge-m3",
        dimensions=1024,
        device="cpu",
    )


def test_embedding_provider_initialization():
    """Test that the embedding provider initializes correctly."""
    provider = SentenceTransformerEmbeddingProvider(
        model_name="BAAI/bge-m3",
        dimensions=1024,
        device="cpu",
    )
    assert provider.model_name == "BAAI/bge-m3"
    assert provider.dimensions == 1024


def test_embed_single_query(embedding_provider: SentenceTransformerEmbeddingProvider):
    """Test embedding a single query."""
    query = "What is required for a refugee claim?"
    embedding = embedding_provider.embed_query(query)

    assert isinstance(embedding, list)
    assert len(embedding) == 1024
    assert all(isinstance(x, float) for x in embedding)


def test_embed_documents(embedding_provider: SentenceTransformerEmbeddingProvider):
    """Test embedding multiple documents."""
    texts = [
        "The claimant must establish a credible basis for fear of persecution.",
        "Border services officers have authority to conduct inspections.",
        "Humanitarian factors must be considered in light of the best interests of children.",
    ]
    embeddings = embedding_provider.embed_documents(texts)

    assert len(embeddings) == 3
    assert all(len(e) == 1024 for e in embeddings)
    assert all(all(isinstance(x, float) for x in e) for e in embeddings)


def test_embeddings_normalized(embedding_provider: SentenceTransformerEmbeddingProvider):
    """Test that embeddings are normalized (unit vectors)."""
    import math

    text = "This is a test sentence."
    embedding = embedding_provider.embed_query(text)

    # Normalized vectors should have magnitude ~1.0
    magnitude = math.sqrt(sum(x**2 for x in embedding))
    assert abs(magnitude - 1.0) < 0.01


def test_similar_texts_have_similar_embeddings(
    embedding_provider: SentenceTransformerEmbeddingProvider,
):
    """Test that semantically similar texts have similar embeddings."""
    import numpy as np

    similar_texts = [
        "The claimant seeks refugee status.",
        "The applicant is seeking refuge.",
    ]

    different_texts = [
        "The claimant seeks refugee status.",
        "Border officers inspect baggage.",
    ]

    similar_embeddings = embedding_provider.embed_documents(similar_texts)
    different_embeddings = embedding_provider.embed_documents(different_texts)

    # Cosine similarity between similar texts
    sim1 = np.dot(similar_embeddings[0], similar_embeddings[1])

    # Cosine similarity between different texts
    sim2 = np.dot(different_embeddings[0], different_embeddings[1])

    # Similar texts should have higher cosine similarity
    assert sim1 > sim2


def test_dimension_mismatch_error(embedding_provider: SentenceTransformerEmbeddingProvider):
    """Test that dimension mismatch is caught."""
    # Create provider expecting wrong dimensions
    bad_provider = SentenceTransformerEmbeddingProvider(
        model_name="BAAI/bge-m3",
        dimensions=768,  # Wrong: actual model is 1024
        device="cpu",
    )

    text = "Test sentence."
    with pytest.raises(ValueError, match="returned .* dimensions; expected"):
        bad_provider.embed_query(text)


def test_legal_domain_queries(embedding_provider: SentenceTransformerEmbeddingProvider):
    """Test that the provider works with legal domain queries."""
    legal_queries = [
        "immigration appeal based on humanitarian grounds",
        "CBSA authority in border enforcement",
        "refugee claimant burden of proof at hearing",
        "judicial review of immigration decision",
        "citizenship revocation for fraud",
    ]

    embeddings = embedding_provider.embed_documents(legal_queries)

    assert len(embeddings) == len(legal_queries)
    assert all(len(e) == 1024 for e in embeddings)


def test_empty_text_handling(embedding_provider: SentenceTransformerEmbeddingProvider):
    """Test handling of empty text lists."""
    embeddings = embedding_provider.embed_documents([])
    assert embeddings == []
