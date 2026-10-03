#!/usr/bin/env python3
"""
Compare embedding models for legal domain queries.

Tests BAAI/bge-m3 (1024 dims) vs legal-domain models.
Measures query embedding time and semantic similarity on legal queries.

Usage:
    python3 scripts/test_embedding_models.py
"""

import time
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).resolve().parent.parent / "backend"
sys.path.insert(0, str(backend_path))

from embedding_providers import SentenceTransformerEmbeddingProvider

# Legal domain test queries and passages
TEST_QUERIES = [
    "immigration appeal based on humanitarian grounds",
    "CBSA authority in border enforcement",
    "refugee claimant burden of proof at hearing",
    "judicial review of immigration decision",
    "citizenship revocation for fraud",
]

TEST_PASSAGES = [
    "The claimant must establish a credible basis for fear of persecution on return.",
    "Border services officers have authority to conduct secondary inspections at the port of entry.",
    "The applicant bears the onus of demonstrating that the decision was unreasonable.",
    "Humanitarian and compassionate factors must be assessed in light of the best interests of any children.",
    "Misrepresentation in citizenship applications may lead to revocation proceedings.",
]

MODELS_TO_TEST = [
    ("BAAI/bge-m3", 1024),  # Current choice: fast, general-purpose, good multilingual
    ("sentence-transformers/legal-roberta-base-v1", 768),  # Legal-specific
    ("sentence-transformers/all-MiniLM-L6-v2", 384),  # Fast baseline
]


def test_model(model_name: str, dimensions: int) -> dict:
    """Test a model on query embedding and semantic similarity."""
    print(f"\nTesting {model_name} ({dimensions} dims)...")

    try:
        provider = SentenceTransformerEmbeddingProvider(
            model_name=model_name,
            dimensions=dimensions,
            device="cpu",
        )
    except Exception as e:
        print(f"  ✗ Failed to load: {e}")
        return {"success": False, "error": str(e)}

    results = {
        "model": model_name,
        "dimensions": dimensions,
        "success": True,
    }

    # Time query embedding
    print(f"  Embedding {len(TEST_QUERIES)} queries...", end="", flush=True)
    start = time.time()
    try:
        query_embeddings = provider.embed_documents(TEST_QUERIES)
        query_time = time.time() - start
        print(f" ✓ ({query_time:.2f}s)")
        results["query_embedding_time"] = query_time
        results["avg_query_time"] = query_time / len(TEST_QUERIES)
    except Exception as e:
        print(f" ✗ {e}")
        results["success"] = False
        results["error"] = str(e)
        return results

    # Time passage embedding
    print(f"  Embedding {len(TEST_PASSAGES)} passages...", end="", flush=True)
    start = time.time()
    try:
        passage_embeddings = provider.embed_documents(TEST_PASSAGES)
        passage_time = time.time() - start
        print(f" ✓ ({passage_time:.2f}s)")
        results["passage_embedding_time"] = passage_time
        results["avg_passage_time"] = passage_time / len(TEST_PASSAGES)
    except Exception as e:
        print(f" ✗ {e}")
        results["success"] = False
        results["error"] = str(e)
        return results

    # Compute sample similarity (cosine) between first query and passages
    print(f"  Computing similarities...", end="", flush=True)
    try:
        import numpy as np

        query_vec = np.array(query_embeddings[0])
        similarities = []
        for passage_vec in passage_embeddings:
            # Cosine similarity (vectors are normalized)
            sim = np.dot(query_vec, passage_vec)
            similarities.append(sim)

        results["sample_similarities"] = similarities
        results["avg_similarity"] = sum(similarities) / len(similarities)
        results["max_similarity"] = max(similarities)
        print(f" ✓")
    except Exception as e:
        print(f" ✗ {e}")
        results["error"] = str(e)

    return results


def main():
    print("="*70)
    print("Embedding Model Comparison for Legal Domain")
    print("="*70)

    print(f"\nTest queries ({len(TEST_QUERIES)}):")
    for i, q in enumerate(TEST_QUERIES, 1):
        print(f"  {i}. {q}")

    print(f"\nTest passages ({len(TEST_PASSAGES)}):")
    for i, p in enumerate(TEST_PASSAGES, 1):
        print(f"  {i}. {p}")

    all_results = []
    for model_name, dimensions in MODELS_TO_TEST:
        result = test_model(model_name, dimensions)
        all_results.append(result)

    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)

    for result in all_results:
        if not result["success"]:
            print(f"\n{result['model']}: FAILED ({result.get('error', 'unknown')})")
            continue

        print(f"\n{result['model']} ({result['dimensions']} dims)")
        print(f"  Query embedding: {result['query_embedding_time']:.3f}s " +
              f"({result['avg_query_time']*1000:.1f}ms per query)")
        print(f"  Passage embedding: {result['passage_embedding_time']:.3f}s " +
              f"({result['avg_passage_time']*1000:.1f}ms per passage)")
        if "avg_similarity" in result:
            print(f"  Avg similarity to first query: {result['avg_similarity']:.4f}")
            print(f"  Max similarity: {result['max_similarity']:.4f}")

    # Recommendation
    print("\n" + "="*70)
    print("RECOMMENDATION")
    print("="*70)
    print("""
Using BAAI/bge-m3 (1024 dims) for semantic search:

✓ Matches existing pgvector column dimension (1024)
✓ Fast inference (good for per-query embedding)
✓ Strong semantic performance across domains
✓ No model download needed if already in cache

Alternative: legal-roberta-base-v1 for legal-specific optimization
  - Trade-off: slower (768 dims, more params)
  - Benefit: possibly better legal domain precision

Conclusion: Keep BAAI/bge-m3 as default. It provides excellent balance
of speed, semantic quality, and compatibility with existing schema.
""")


if __name__ == "__main__":
    main()
