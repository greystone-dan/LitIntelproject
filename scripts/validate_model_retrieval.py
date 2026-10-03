#!/usr/bin/env python3
"""
Validate that embedding models actually retrieve relevant paragraphs for legal queries.

This is a small check to verify semantic search works correctly, not just that
embeddings have high cosine similarity in the abstract.

Runs on sample legal paragraphs extracted from actual case law, testing whether
known-relevant paragraphs rank high for targeted queries.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))

from embedding_providers import SentenceTransformerEmbeddingProvider
import numpy as np


# Real legal paragraphs from iLit cases (sample)
LEGAL_PARAGRAPHS = {
    "refugee_determination_1": "The claimant must establish a credible basis for fear of persecution on return to the country of origin.",
    "refugee_determination_2": "To succeed, the applicant needs to show a reasonable possibility that they would face persecution based on a Convention ground.",
    "border_authority_1": "Border Services officers have authority to conduct secondary inspections at the port of entry under the Immigration Act.",
    "border_authority_2": "The officer was authorized to examine baggage and interview the traveller pursuant to section 38 of the Customs Act.",
    "humanitarian_1": "Humanitarian and compassionate factors must be considered in light of the best interests of any children.",
    "humanitarian_2": "The applicant's personal circumstances, including family ties and establishment, are relevant H&C considerations.",
    "judicial_review_1": "The applicant bears the onus of demonstrating that the decision was unreasonable.",
    "judicial_review_2": "A decision is unreasonable if the reasons do not justify the result or if the reasoning is incoherent.",
    "citizenship_1": "Misrepresentation in citizenship applications may lead to revocation proceedings.",
    "citizenship_2": "The applicant must have satisfied the requirements of the Citizenship Act at the time of grant.",
}

# Test queries with expected relevant paragraphs
TEST_QUERIES = [
    {
        "query": "What must a refugee claimant prove?",
        "expected_relevant": ["refugee_determination_1", "refugee_determination_2"],
    },
    {
        "query": "What authority do border officers have?",
        "expected_relevant": ["border_authority_1", "border_authority_2"],
    },
    {
        "query": "How are humanitarian factors considered?",
        "expected_relevant": ["humanitarian_1", "humanitarian_2"],
    },
    {
        "query": "When can a decision be overturned on judicial review?",
        "expected_relevant": ["judicial_review_1", "judicial_review_2"],
    },
    {
        "query": "What happens if someone lies on their citizenship application?",
        "expected_relevant": ["citizenship_1", "citizenship_2"],
    },
]

MODELS_TO_TEST = [
    ("BAAI/bge-m3", 1024),
    ("sentence-transformers/all-MiniLM-L6-v2", 384),
]


def rank_paragraphs(query: str, paragraphs: dict, provider: SentenceTransformerEmbeddingProvider) -> list:
    """Rank paragraphs by cosine similarity to query."""
    query_embedding = provider.embed_query(query)
    paragraph_embeddings = provider.embed_documents(list(paragraphs.values()))

    # Compute cosine similarities (embeddings are normalized)
    rankings = []
    for (key, text), para_embedding in zip(paragraphs.items(), paragraph_embeddings):
        similarity = np.dot(query_embedding, para_embedding)
        rankings.append((key, text, similarity))

    # Sort by similarity descending
    rankings.sort(key=lambda x: x[2], reverse=True)
    return rankings


def test_model_retrieval(model_name: str, dimensions: int) -> dict:
    """Test if model retrieves relevant paragraphs for legal queries."""
    print(f"\n{'='*70}")
    print(f"Testing {model_name} ({dimensions} dims)")
    print(f"{'='*70}")

    try:
        provider = SentenceTransformerEmbeddingProvider(
            model_name=model_name,
            dimensions=dimensions,
            device="cpu",
        )
    except Exception as e:
        print(f"✗ Failed to load: {e}")
        return {"success": False, "error": str(e)}

    results = {
        "model": model_name,
        "dimensions": dimensions,
        "total_queries": len(TEST_QUERIES),
        "queries_with_relevant_in_top_2": 0,
        "queries_with_relevant_in_top_5": 0,
        "average_rank_of_first_relevant": 0,
        "details": [],
    }

    first_relevant_ranks = []

    for test_case in TEST_QUERIES:
        query = test_case["query"]
        expected_relevant = set(test_case["expected_relevant"])

        print(f"\nQuery: {query}")

        rankings = rank_paragraphs(query, LEGAL_PARAGRAPHS, provider)

        # Find rank of first relevant paragraph
        first_relevant_rank = None
        for rank, (key, text, similarity) in enumerate(rankings, 1):
            if key in expected_relevant:
                first_relevant_rank = rank
                break

        if first_relevant_rank is not None:
            first_relevant_ranks.append(first_relevant_rank)
            if first_relevant_rank <= 2:
                results["queries_with_relevant_in_top_2"] += 1
                status = "✓ TOP 2"
            elif first_relevant_rank <= 5:
                results["queries_with_relevant_in_top_5"] += 1
                status = "✓ TOP 5"
            else:
                status = f"✗ RANK {first_relevant_rank}"
        else:
            status = "✗ NOT FOUND"
            first_relevant_rank = len(rankings) + 1
            first_relevant_ranks.append(first_relevant_rank)

        print(f"  {status}")
        print(f"  Top 3 results:")
        for rank, (key, text, similarity) in enumerate(rankings[:3], 1):
            marker = "→ " if key in expected_relevant else "  "
            print(f"    {rank}. {marker}{text[:60]}... (sim: {similarity:.3f})")

        results["details"].append({
            "query": query,
            "first_relevant_rank": first_relevant_rank,
            "found": first_relevant_rank <= len(rankings),
        })

    if first_relevant_ranks:
        results["average_rank_of_first_relevant"] = sum(first_relevant_ranks) / len(first_relevant_ranks)

    # Print summary
    print(f"\nSummary for {model_name}:")
    print(f"  Queries with relevant in top 2: {results['queries_with_relevant_in_top_2']}/{results['total_queries']}")
    print(f"  Queries with relevant in top 5: {results['queries_with_relevant_in_top_5']}/{results['total_queries']}")
    print(f"  Average rank of first relevant: {results['average_rank_of_first_relevant']:.1f}")

    results["success"] = True
    return results


def main():
    print("\n" + "="*70)
    print("MODEL RETRIEVAL VALIDATION FOR LEGAL DOMAIN")
    print("="*70)
    print("\nTesting whether embedding models actually retrieve relevant legal")
    print("paragraphs for immigration law queries (not just abstract similarity).")

    all_results = []
    for model_name, dimensions in MODELS_TO_TEST:
        result = test_model_retrieval(model_name, dimensions)
        all_results.append(result)

    # Final recommendation
    print("\n" + "="*70)
    print("RECOMMENDATION")
    print("="*70)

    successful = [r for r in all_results if r["success"]]
    if not successful:
        print("✗ No models loaded successfully")
        return

    # Compare by top-2 retrieval rate
    successful.sort(
        key=lambda r: (
            -r["queries_with_relevant_in_top_2"],
            r["average_rank_of_first_relevant"],
        )
    )

    best = successful[0]
    print(f"\n✓ BEST MODEL: {best['model']}")
    print(f"  - Relevant paragraphs in top 2: {best['queries_with_relevant_in_top_2']}/{best['total_queries']}")
    print(f"  - Average first-relevant rank: {best['average_rank_of_first_relevant']:.1f}")

    if len(successful) > 1:
        second = successful[1]
        print(f"\n✓ ALTERNATIVE: {second['model']}")
        print(f"  - Relevant paragraphs in top 2: {second['queries_with_relevant_in_top_2']}/{second['total_queries']}")
        print(f"  - Average first-relevant rank: {second['average_rank_of_first_relevant']:.1f}")


if __name__ == "__main__":
    main()
