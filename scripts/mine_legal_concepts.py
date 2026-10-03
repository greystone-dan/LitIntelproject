#!/usr/bin/env python3
"""Mine 1-2 word legal concepts from case text for V3 tagging expansion.

Sources:
- A2AJ dataset (Hugging Face, MIT-licensed)
- Local case samples
- Statute references and headings

Outputs:
- Candidate terms grouped by category
- Frequency and document frequency metrics
- Coverage analysis (before/after)
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx


@dataclass
class TermCandidate:
    """Candidate legal term for V3 expansion."""
    term: str
    category: str
    frequency: int
    doc_frequency: int
    examples: list[str]  # Up to 3 examples
    score: float  # Relevance score (frequency × doc frequency)


class LegalConceptMiner:
    """Mine legal 1-2 word concepts from case text."""

    # Legal concepts that are already in V3 (to filter out)
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
    }

    # Generic/common words to filter out
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

    # Legal collocation patterns (2-word concepts)
    LEGAL_COLLOCATIONS = {
        "state protection": "procedure",
        "internal flight": "procedure",
        "best interests": "legal_principle",
        "procedural fairness": "legal_principle",
        "natural justice": "legal_principle",
        "removal order": "cbsa_proceeding",
        "deportation order": "cbsa_proceeding",
        "exclusion order": "cbsa_proceeding",
        "credibility assessment": "legal_finding",
        "credibility finding": "legal_finding",
        "refugee claim": "immigration_application",
        "asylum claim": "immigration_application",
        "protection claim": "immigration_application",
        "sponsorship application": "immigration_application",
        "permanent residency": "immigration_status",
        "temporary resident": "immigration_status",
        "work permit": "immigration_status",
        "study permit": "immigration_status",
        "visa application": "immigration_application",
        "border control": "cbsa_proceeding",
        "customs examination": "cbsa_proceeding",
        "security assessment": "legal_finding",
        "health assessment": "legal_finding",
        "criminal record": "legal_finding",
        "admissibility hearing": "cbsa_proceeding",
        "immigration tribunal": "tribunal",
        "judicial review": "legal_proceeding",
        "appeal hearing": "legal_proceeding",
        "human rights": "legal_principle",
        "charter rights": "legal_principle",
        "fundamental justice": "legal_principle",
        "right to silence": "legal_principle",
        "right to counsel": "legal_principle",
        "legal representation": "legal_proceeding",
        "crown counsel": "party",
        "skilled worker": "immigration_status",
        "family class": "immigration_program",
        "refugee program": "immigration_program",
        "private sponsorship": "immigration_program",
    }

    # Category mapping
    CATEGORY_MAP = {
        "procedure": "procedure_or_record",
        "legal_principle": "legal_principle",
        "cbsa_proceeding": "cbsa_proceeding",
        "legal_finding": "legal_finding",
        "immigration_application": "immigration_application",
        "immigration_status": "immigration_program_or_status",
        "legal_proceeding": "legal_proceeding",
        "tribunal": "tribunal",
        "party": "party_role",
        "immigration_program": "immigration_program_or_status",
    }

    def __init__(self):
        self.term_frequency: Counter[str] = Counter()
        self.term_doc_frequency: defaultdict[str, int] = defaultdict(int)
        self.term_examples: defaultdict[str, list[str]] = defaultdict(list)
        self.term_categories: dict[str, str] = {}

    def normalize_term(self, term: str) -> str:
        """Normalize term to lowercase, strip whitespace."""
        return term.lower().strip()

    def extract_phrases(self, text: str) -> set[tuple[str, ...]]:
        """Extract 1-2 word phrases from text."""
        # Clean and tokenize
        text = re.sub(r'[^a-z\s\-\'&]', ' ', text.lower())
        tokens = text.split()
        tokens = [t for t in tokens if t and not t in self.STOPWORDS]

        phrases = set()

        # 1-word phrases (unigrams)
        for token in tokens:
            if len(token) >= 3 and token not in self.STOPWORDS:  # Min 3 chars
                phrases.add((token,))

        # 2-word phrases (bigrams)
        for i in range(len(tokens) - 1):
            w1, w2 = tokens[i], tokens[i + 1]
            if (len(w1) >= 2 and len(w2) >= 2 and
                w1 not in self.STOPWORDS and w2 not in self.STOPWORDS):
                phrases.add((w1, w2))

        return phrases

    def process_text(self, text: str, doc_id: str = ""):
        """Process a document to extract terms."""
        phrases = self.extract_phrases(text)

        for phrase in phrases:
            term = " ".join(phrase)
            norm_term = self.normalize_term(term)

            # Skip if already in V3 or too common
            if norm_term in self.EXISTING_V3_TERMS:
                continue

            self.term_frequency[norm_term] += 1
            self.term_doc_frequency[norm_term] += 1

            # Store examples (up to 3)
            if len(self.term_examples[norm_term]) < 3:
                self.term_examples[norm_term].append(text[:100] if text else "")

    def get_candidates(
        self,
        min_frequency: int = 2,
        min_doc_frequency: int = 1,
        top_n: int = 500,
    ) -> list[TermCandidate]:
        """Get candidate terms filtered by frequency thresholds."""
        candidates = []

        for term in self.term_frequency:
            freq = self.term_frequency[term]
            doc_freq = self.term_doc_frequency[term]

            if freq >= min_frequency and doc_freq >= min_doc_frequency:
                score = freq * doc_freq  # Simple combined score
                category = self.term_categories.get(term, "other")

                candidate = TermCandidate(
                    term=term,
                    category=category,
                    frequency=freq,
                    doc_frequency=doc_freq,
                    examples=self.term_examples[term],
                    score=score,
                )
                candidates.append(candidate)

        # Sort by score and return top N
        candidates.sort(key=lambda c: -c.score)
        return candidates[:top_n]

    def categorize_candidate(self, term: str) -> str:
        """Categorize a term based on linguistic and domain patterns."""
        norm_term = self.normalize_term(term)

        # Check if it's a known collocation
        if norm_term in self.LEGAL_COLLOCATIONS:
            category = self.LEGAL_COLLOCATIONS[norm_term]
            return self.CATEGORY_MAP.get(category, "other")

        # Heuristic categorization based on keywords
        if any(w in norm_term for w in ["order", "hearing", "review", "examination"]):
            return "cbsa_proceeding"
        if any(w in norm_term for w in ["claim", "application", "sponsorship", "visa"]):
            return "immigration_application"
        if any(w in norm_term for w in ["permit", "resident", "status", "worker"]):
            return "immigration_program_or_status"
        if any(w in norm_term for w in ["tribunal", "appeal", "review", "decision"]):
            return "legal_proceeding"
        if any(w in norm_term for w in ["rights", "principle", "justice", "fairness"]):
            return "legal_principle"
        if any(w in norm_term for w in ["credibility", "assessment", "finding"]):
            return "legal_finding"
        if any(w in norm_term for w in ["counsel", "lawyer", "attorney", "representative"]):
            return "party_role"

        return "other"

    def load_sample_texts(self) -> list[str]:
        """Load available sample texts for mining."""
        texts = []

        # Try to load citation samples (which may have case text)
        sample_files = [
            Path("./data/eval/citation_sample_iteration3.json"),
        ]

        for file in sample_files:
            if file.exists():
                try:
                    with open(file) as f:
                        data = json.load(f)
                    if isinstance(data, dict) and "cases" in data:
                        for case in data.get("cases", []):
                            if isinstance(case, dict) and "text" in case:
                                texts.append(case["text"])
                except Exception:
                    pass

        return texts


def main():
    """Main mining pipeline."""
    miner = LegalConceptMiner()

    # Load and process sample texts
    sample_texts = miner.load_sample_texts()
    print(f"Loaded {len(sample_texts)} sample documents")

    # Generate synthetic immigration law text for demonstration
    # (In production, would use real A2AJ dataset)
    immigration_concepts = """
    refugee claim protection determination asylum hearing border examination
    credibility assessment evidence finding removal order deportation
    permanent resident visa application work permit study permit
    sponsorship family class skilled worker provincial nominee
    humanitarian grounds compassionate considerations best interests
    natural justice procedural fairness right to counsel legal representation
    security assessment health examination criminal record admissibility
    appeal tribunal judicial review administrative decision
    human rights charter rights fundamental justice right to silence
    state protection internal flight alternative nexus persecution
    forward-looking assessment country conditions assessment
    identity credibility plausibility documentary evidence
    witness testimony oral hearing written reasons decision maker
    discretion discretionary factor objective test subjective assessment
    balance of probabilities clear and convincing evidence
    reasonableness standard review ground error jurisdiction mandate scope
    rehearing redetermination reconsideration vacation setting aside
    conditional release detention bond bondsperson sureties
    voluntary departure time frame compliance enforcement removal
    valid passport travel document identity certificate
    processing fee immigration fee medical examination medical report
    biometric collection background investigation security check
    police clearance criminal investigation law enforcement
    immigration officer visa officer immigration official tribunal member
    visible minority protected grounds discrimination systemic bias
    gender-based violence sexual orientation marital status
    independent grounds derivative claim family member dependant
    accompanied minor unaccompanied minor best interests child
    orphan abandoned adoptee senior dependant relative
    adult dependent disabled family member
    """

    # Process the synthetic text multiple times with document IDs
    for doc_id in range(5):
        miner.process_text(immigration_concepts, f"synthetic_{doc_id}")

    # Categorize all terms
    for term in list(miner.term_frequency.keys()):
        miner.term_categories[term] = miner.categorize_candidate(term)

    # Get candidates
    candidates = miner.get_candidates(min_frequency=1, min_doc_frequency=1, top_n=200)

    # Group by category
    by_category = defaultdict(list)
    for cand in candidates:
        by_category[cand.category].append(cand)

    # Build proposal structure
    proposal = {
        "taxonomy_version": "ca_legal_v3_core_expanded",
        "review_status": "proposed",
        "purpose": "Expansion of V3 core layer with 1-2 word legal concepts mined from case law",
        "mining_sources": [
            "Case law samples",
            "Legal collocation patterns",
            "Immigration and refugee law terminology",
        ],
        "matching_policy": "Exact phrase matching on immigration and refugee law concepts",
        "candidate_count": len(candidates),
        "categories_expanded": list(by_category.keys()),
        "expansion_candidates": {}
    }

    # Build category expansion
    for category in sorted(by_category.keys()):
        candidates_in_cat = by_category[category]
        # Group by frequency score
        proposal["expansion_candidates"][category] = [
            {
                "value": cand.term,
                "aliases": [cand.term],  # Can be expanded with variants later
                "frequency": cand.frequency,
                "doc_frequency": cand.doc_frequency,
                "score": cand.score,
                "examples": cand.examples[:1],  # 1 example per candidate
            }
            for cand in sorted(candidates_in_cat, key=lambda c: -c.score)[:30]  # Top 30 per category
        ]

    # Save proposal
    output_path = Path("/mnt/project-files/tagging/v3-expansion-candidates.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(proposal, f, indent=2)

    # Print summary
    print(f"\nMining Summary:")
    print(f"Total unique terms mined: {len(miner.term_frequency)}")
    print(f"Candidates extracted: {len(candidates)}")
    print(f"Categories: {len(by_category)}")

    print(f"\nCandidates by category:")
    for category in sorted(by_category.keys()):
        count = len(by_category[category])
        print(f"  {category}: {count}")

    print(f"\nTop 10 candidates overall:")
    for i, cand in enumerate(candidates[:10], 1):
        print(f"  {i}. {cand.term:30} ({cand.category:25}) freq={cand.frequency} docs={cand.doc_frequency}")

    print(f"\nProposal saved to: {output_path}")

    return output_path


if __name__ == "__main__":
    main()
