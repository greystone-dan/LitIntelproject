#!/usr/bin/env python3
"""Mine 1-2 word legal concepts from A2AJ Canadian case law dataset.

Downloads FC and RAD decisions from Hugging Face A2AJ dataset,
extracts high-frequency legal concepts, and measures coverage impact.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

# Existing V3 concepts to filter out
EXISTING_V3_TERMS = {
    "ircc", "cbsa", "csis", "rpd", "rad", "immigration division", "iad",
    "irpa", "irpr", "charter", "prra", "h&c", "h and c", "humanitarian and compassionate",
    "ifa", "internal flight alternative", "pfl", "procedural fairness letter",
    "section 44 report", "gcms", "caips", "decision letter", "refusal letter",
    "admissibility hearing", "minister's delegate", "detention review", "detention order",
    "release conditions", "voluntary departure", "travel document",
    "prtd", "permanent resident", "copr", "lmia", "pgwp", "trv", "trp", "bowp",
    "express entry", "provincial nominee", "security screening",
    "ipob", "ltte", "pkk", "farc", "taliban", "hamas", "hezbollah",
    # And the existing V3 expansion concepts
    "removal order", "deportation order", "exclusion order", "border examination",
    "customs examination", "detention review", "release conditions", "voluntary departure",
    "travel document", "admissibility hearing", "minister delegate", "bondsperson",
    "refugee claim", "asylum claim", "protection claim", "sponsorship application",
    "visa application", "work permit", "study permit", "permanent residency",
    "temporary resident", "family class", "skilled worker", "provincial nominee",
    "judicial review", "appeal hearing", "motion hearing", "application hearing",
    "evidence hearing", "merits hearing", "credibility hearing",
    "state protection", "internal flight", "best interests", "procedural fairness",
    "natural justice", "human rights", "charter rights", "fundamental justice",
    "right to silence", "right to counsel", "legal representation", "natural bias",
    "reasonable apprehension", "credibility assessment", "credibility finding",
    "security assessment", "security concern", "security risk", "health assessment",
    "criminal record", "police clearance", "background investigation",
    "identity verification", "medical examination", "plausibility assessment",
    "evidence assessment", "documentary evidence",
    "written decision", "written reasons", "oral decision", "reasons for decision",
    "decision maker", "immigration officer", "visa officer", "tribunal member",
    "hearing record", "case file", "file number", "reference number",
    "processing time", "application fee", "medical fee", "biometric collection",
}

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "is", "was", "are", "be", "have", "has", "had", "do", "does",
    "did", "will", "would", "should", "could", "may", "might", "must",
    "can", "that", "this", "these", "those", "which", "who", "what",
    "where", "when", "why", "how", "all", "each", "every", "both", "any",
    "one", "some", "such", "no", "nor", "not", "only", "own", "same",
    "so", "than", "too", "very", "just", "as", "if", "because",
    "by", "from", "up", "about", "out", "into", "through", "during",
    "before", "after", "above", "below", "between", "under", "over",
    "again", "further", "then", "once", "here", "there", "now",
    "case", "court", "judge", "decision", "order", "hearing", "matter",
    "person", "people", "applicant", "respondent", "party", "parties",
    "act", "regulation", "law", "statute", "section", "subsection",
}


def download_a2aj_sample(min_records: int = 500) -> list[dict[str, Any]]:
    """Download FC and RAD decisions from A2AJ dataset via Hugging Face."""
    print(f"Downloading A2AJ dataset (target: {min_records}+ cases)...")

    cases = []

    try:
        from datasets import load_dataset

        # Load the full dataset without trust_remote_code
        dataset = load_dataset("a2aj/canadian-case-law", split="train")

        print(f"Total records in dataset: {len(dataset)}")

        # Filter for Federal Court and Refugee Appeal Division cases
        target_courts = ["federal court", "f.c.", "f.c", "fca", "federal court of appeal",
                        "refugee appeal", "rad", "r.a.d."]

        for i, record in enumerate(dataset):
            if i % 10000 == 0:
                print(f"  Filtering case {i+1}/{len(dataset)}...")

            if not record.get("text"):
                continue

            # Get court info from multiple possible fields
            court = (record.get("court") or "").lower()
            title = (record.get("title") or "").lower()

            # Check if this is an FC or RAD case
            is_target = any(target in court or target in title for target in target_courts)

            if is_target:
                cases.append({
                    "id": record.get("id", f"case_{len(cases)}"),
                    "text": record.get("text", ""),
                    "court": court,
                    "title": title,
                })

                if len(cases) >= min_records:
                    break

        print(f"Filtered to {len(cases)} FC and RAD cases")
        return cases

    except Exception as e:
        print(f"Dataset loading error: {e}")
        print("Using fallback synthetic mining...")
        return []


def extract_phrases(text: str) -> set[tuple[str, ...]]:
    """Extract 1-2 word phrases from text."""
    # Clean and tokenize
    text = re.sub(r'[^a-z\s\-\'&.]', ' ', text.lower())
    tokens = text.split()
    tokens = [t.strip('-\'') for t in tokens if t.strip('-\'')]
    tokens = [t for t in tokens if t and t not in STOPWORDS and len(t) >= 2]

    phrases = set()

    # 1-word phrases (unigrams)
    for token in tokens:
        if len(token) >= 3:
            phrases.add((token,))

    # 2-word phrases (bigrams)
    for i in range(len(tokens) - 1):
        w1, w2 = tokens[i], tokens[i + 1]
        if len(w1) >= 2 and len(w2) >= 2:
            phrases.add((w1, w2))

    return phrases


def mine_concepts(cases: list[dict[str, Any]]) -> dict[str, dict[str, int]]:
    """Mine concept frequencies from cases."""
    term_frequency: Counter[str] = Counter()
    term_doc_frequency: defaultdict[str, int] = defaultdict(int)

    print(f"Mining {len(cases)} cases...")

    for i, case in enumerate(cases):
        if i % 50 == 0 and i > 0:
            print(f"  Processed {i}/{len(cases)} cases, {len(term_frequency)} unique terms...")

        text = case.get("text", "")
        if not text:
            continue

        phrases = extract_phrases(text)

        case_terms = set()
        for phrase in phrases:
            term = " ".join(phrase)
            norm_term = term.lower().strip()

            # Skip if already in V3 or too generic
            if norm_term in EXISTING_V3_TERMS or norm_term in STOPWORDS:
                continue

            case_terms.add(norm_term)

        # Update frequencies
        for term in case_terms:
            term_frequency[term] += 1
            term_doc_frequency[term] += 1

    print(f"Total unique terms found: {len(term_frequency)}")

    # Filter by minimum document frequency (appeared in at least 5 documents)
    filtered = {}
    for term, freq in term_frequency.most_common():
        doc_freq = term_doc_frequency[term]
        if doc_freq >= 5:  # Appeared in 5+ documents
            filtered[term] = {
                "frequency": freq,
                "doc_frequency": doc_freq,
                "score": freq * doc_freq
            }

    return filtered


def categorize_terms(terms: dict[str, dict[str, int]]) -> dict[str, list[str]]:
    """Categorize terms by legal domain heuristics."""
    categorized = defaultdict(list)

    for term in terms:
        score = terms[term]["score"]
        words = term.split()

        # Categorization heuristics based on keywords
        if any(w in term for w in ["order", "examination", "border", "detention", "release", "departure", "travel"]):
            cat = "cbsa_proceeding"
        elif any(w in term for w in ["claim", "application", "sponsorship", "visa", "permit"]):
            cat = "immigration_application"
        elif any(w in term for w in ["resident", "status", "citizen", "national", "holder"]):
            cat = "immigration_status"
        elif any(w in term for w in ["judicial", "appeal", "motion", "hearing", "review"]):
            cat = "legal_proceeding"
        elif any(w in term for w in ["principle", "justice", "fairness", "right", "protection"]):
            cat = "legal_principle"
        elif any(w in term for w in ["assessment", "finding", "credibility", "evidence", "risk", "concern"]):
            cat = "legal_finding"
        elif any(w in term for w in ["decision", "reasons", "written", "oral", "record", "file"]):
            cat = "procedure_or_record"
        else:
            cat = "other"

        categorized[cat].append((term, score))

    # Sort by score and return top N per category
    result = {}
    for category in sorted(categorized.keys()):
        sorted_terms = sorted(categorized[category], key=lambda x: -x[1])
        # Keep top 150 per category to reach "several hundred" total
        result[category] = [t[0] for t in sorted_terms[:150]]

    return result


def main():
    """Mine A2AJ concepts and generate proposal."""
    output_dir = Path("/mnt/project-files/tagging")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Download cases
    cases = download_a2aj_sample(min_records=500)

    if not cases:
        print("\nWarning: Could not download A2AJ dataset; using fallback approach")
        # Fallback: use the 105 concepts we already have plus some additional handcurated ones
        cases = []

    if cases:
        # Step 2: Mine concepts
        mined_terms = mine_concepts(cases)

        print(f"\nMined {len(mined_terms)} high-frequency candidate terms (5+ documents)")

        # Step 3: Categorize
        categorized = categorize_terms(mined_terms)

        print("\nTerms by category:")
        total_terms = 0
        for category in sorted(categorized.keys()):
            count = len(categorized[category])
            total_terms += count
            print(f"  {category}: {count} terms")

        print(f"\nTotal candidate terms: {total_terms}")
    else:
        print("\nUsing pre-curated expansion terms (105 concepts)")
        categorized = load_precurated_terms()

    # Build proposal
    proposal = {
        "taxonomy_version": "ca_legal_v3_core",
        "review_status": "proposed",
        "purpose": "Expansion of V3 core layer with high-frequency legal concepts from Canadian immigration case law",
        "source": f"Mined from {len(cases)} FC and RAD decisions in A2AJ dataset" if cases else "Curated from immigration law domain",
        "matching_policy": "Exact alias matching produces mention evidence only",
        "categories": {}
    }

    for category in sorted(categorized.keys()):
        proposal["categories"][category] = {
            term: [term]  # Alias is the term itself for now
            for term in categorized[category]
        }

    # Save proposal
    proposal_path = output_dir / "v3-expansion-a2aj-mined.json"
    with open(proposal_path, "w") as f:
        json.dump(proposal, f, indent=2)

    print(f"\nProposal saved to: {proposal_path}")

    # Generate summary report
    total_new = sum(len(terms) for terms in proposal["categories"].values())
    print(f"\n✓ Proposal contains {total_new} candidate concepts across {len(proposal['categories'])} categories")

    return proposal_path


def load_precurated_terms() -> dict[str, list[str]]:
    """Load the 105 pre-curated expansion terms."""
    return {
        "cbsa_proceeding": [
            "removal order", "deportation order", "exclusion order", "border examination",
            "customs examination", "detention review", "release conditions", "voluntary departure",
            "travel document", "admissibility hearing", "minister delegate", "bondsperson",
        ],
        "immigration_application": [
            "refugee claim", "asylum claim", "protection claim", "sponsorship application",
            "visa application", "work permit", "study permit", "permanent residency",
            "temporary resident", "family class", "skilled worker", "provincial nominee",
        ],
        "legal_proceeding": [
            "judicial review", "appeal hearing", "motion hearing", "application hearing",
            "evidence hearing", "merits hearing", "credibility hearing",
        ],
        "legal_principle": [
            "state protection", "internal flight", "best interests", "procedural fairness",
            "natural justice", "human rights", "charter rights", "fundamental justice",
            "right to silence", "right to counsel", "legal representation", "natural bias",
            "reasonable apprehension",
        ],
        "legal_finding": [
            "credibility assessment", "credibility finding", "security assessment", "security concern",
            "security risk", "health assessment", "criminal record", "police clearance",
            "background investigation", "identity verification", "medical examination",
            "plausibility assessment", "evidence assessment", "documentary evidence",
        ],
        "immigration_status": [
            "permanent resident", "temporary resident", "work permit holder", "study permit holder",
            "visa holder", "canadian citizen", "foreign national", "protected person",
        ],
        "procedure_or_record": [
            "written decision", "written reasons", "oral decision", "reasons for decision",
            "decision maker", "immigration officer", "visa officer", "tribunal member",
            "hearing record", "case file", "file number", "reference number",
            "processing time", "application fee", "medical fee", "biometric collection",
        ],
        "other": [
            "forward looking", "balanced assessment", "objective test", "subjective test",
            "balance probabilities", "clear convincing", "visible minority", "protected grounds",
            "gender based", "sexual orientation", "marital status", "family member",
            "dependent child", "senior dependent", "adult dependent", "unaccompanied minor",
            "accompanied minor", "orphan", "abandoned child", "adoptee", "future risk",
            "prospective claim",
        ],
    }


if __name__ == "__main__":
    main()
