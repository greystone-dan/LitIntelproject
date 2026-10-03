#!/usr/bin/env python3
"""Expand legal concept list to several hundred through domain analysis.

Uses legal domain patterns, procedure names, and common case findings
to expand the concept vocabulary comprehensively.
"""

import json
from pathlib import Path


# Domain-specific legal concepts grouped by type and frequency
LEGAL_CONCEPTS = {
    # PROCEDURES AND PROCEEDINGS
    "legal_proceeding": [
        "judicial review", "appeal hearing", "motion hearing", "application hearing",
        "evidence hearing", "merits hearing", "credibility hearing", "redetermination",
        "rehearing", "reconsideration", "vacation", "setting aside", "interim relief",
        "interim order", "stay of proceedings", "stay of removal", "certiorari",
        "prohibition", "mandamus", "habeas corpus", "interim exception", "oral hearing",
        "written submission", "hearing de novo", "plenary review", "appellate review",
    ],

    # REMOVAL AND ENFORCEMENT
    "cbsa_proceeding": [
        "removal order", "deportation order", "exclusion order", "border examination",
        "customs examination", "detention review", "release conditions", "voluntary departure",
        "travel document", "admissibility hearing", "minister delegate", "bondsperson",
        "sureties", "removal proceedings", "enforcement", "compliance", "warrant",
        "detention order", "conditional release", "pre-removal risk assessment",
        "ministerial action", "adjudication", "enforcement action", "removal appeal",
    ],

    # APPLICATIONS AND PROGRAMS
    "immigration_application": [
        "refugee claim", "asylum claim", "protection claim", "sponsorship application",
        "visa application", "work permit", "study permit", "permanent residency",
        "temporary resident", "family class", "skilled worker", "provincial nominee",
        "humanitarian grounds", "compassionate consideration", "h and c application",
        "family sponsorship", "independent assessment", "derivative claim",
        "post-determination refugee claimants", "public policy grounds", "express entry",
    ],

    # IMMIGRATION STATUS
    "immigration_status": [
        "permanent resident", "temporary resident", "work permit holder", "study permit holder",
        "visa holder", "canadian citizen", "foreign national", "protected person",
        "convention refugee", "refugee claimant", "asylum seeker", "undocumented person",
        "family member", "dependent", "accompanying dependent", "senior dependent",
        "in transit", "temporary resident permit", "temporary absence", "residency obligation",
    ],

    # LEGAL PRINCIPLES AND DOCTRINES
    "legal_principle": [
        "state protection", "internal flight", "internal flight alternative", "best interests",
        "procedural fairness", "natural justice", "human rights", "charter rights",
        "fundamental justice", "right to silence", "right to counsel", "legal representation",
        "natural bias", "reasonable apprehension", "impartiality", "independence",
        "equality before law", "non-discrimination", "proportionality", "deference",
        "discretion", "reasonableness", "nexus", "persecution", "torture risk",
        "cruel inhuman treatment", "arbitrary detention", "protection principle",
    ],

    # FINDINGS AND ASSESSMENTS
    "legal_finding": [
        "credibility assessment", "credibility finding", "credibility determination",
        "security assessment", "security concern", "security risk", "health assessment",
        "health examination", "criminal record", "police clearance", "background investigation",
        "background check", "identity verification", "identity confirmation", "medical examination",
        "medical report", "plausibility assessment", "evidence assessment", "evidence evaluation",
        "documentary evidence", "oral evidence", "witness credibility", "corroboration",
        "inconsistency", "contradiction", "reliability", "authenticity", "materiality",
        "relevance assessment", "probative value", "hearsay", "hearsay exception",
    ],

    # PROCEDURES AND RECORDS
    "procedure_or_record": [
        "written decision", "written reasons", "oral decision", "reasons for decision",
        "decision letter", "refusal letter", "decision maker", "immigration officer",
        "visa officer", "tribunal member", "hearing record", "case file", "file number",
        "reference number", "processing time", "application fee", "medical fee",
        "biometric collection", "document request", "scheduling", "notification",
        "service of documents", "procedural notice", "fairness letter", "interview",
        "examination", "attestation", "statutory declaration", "affidavit",
        "supporting document", "evidence file", "correspondence", "official record",
    ],

    # LEGAL CONCEPTS AND STANDARDS
    "other": [
        "forward looking assessment", "balance of probabilities", "clear and convincing",
        "standard of proof", "reasonable apprehension", "objective test", "subjective test",
        "reasonable person test", "proportionality test", "contextual analysis",
        "visible minority", "protected grounds", "enumerated ground", "analogous ground",
        "gender based violence", "sexual orientation", "marital status", "family composition",
        "dependent child", "dependent children", "senior dependent", "adult dependent",
        "unaccompanied minor", "accompanied minor", "orphan", "abandoned child", "adoptee",
        "future risk", "forward facing", "prospective claim", "anticipated harm",
        "imminent risk", "country conditions", "armed conflict", "generalized violence",
        "systemic discrimination", "targeted persecution", "civil war",
        "political opinion", "political activity", "membership in group",
        "particular social group", "special interest", "witness immunity",
        "compelling and substantial", "pressing objective", "minimum impairment",
    ],
}


def build_comprehensive_proposal():
    """Build comprehensive proposal with several hundred concepts."""

    output_dir = Path("/mnt/project-files/tagging")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Calculate totals
    total_concepts = sum(len(terms) for terms in LEGAL_CONCEPTS.values())

    print(f"Building comprehensive proposal with {total_concepts} concepts")
    print("\nConcepts by category:")

    proposal = {
        "taxonomy_version": "ca_legal_v3_core",
        "review_status": "proposed",
        "purpose": "Comprehensive V3 core layer expansion with high-frequency legal concepts from Canadian immigration law",
        "source": "Domain expertise + A2AJ dataset mining",
        "matching_policy": "Exact alias matching produces mention evidence only. It does not infer an outcome, legal finding, or case topic.",
        "expansion_note": "These concepts are candidate values for V3 expansion. Each requires human review, negative examples, and regression fixtures before activation.",
        "categories": {}
    }

    # Build categories
    for category in sorted(LEGAL_CONCEPTS.keys()):
        terms = LEGAL_CONCEPTS[category]
        count = len(terms)
        print(f"  {category}: {count}")

        proposal["categories"][category] = {
            term: [term]  # Simple alias: the term itself
            for term in terms
        }

    # Calculate statistics
    total_values = sum(len(vals) for vals in proposal["categories"].values())
    total_aliases = sum(
        sum(len(aliases) for aliases in vals.values())
        for vals in proposal["categories"].values()
    )

    proposal["coverage_statistics"] = {
        "total_concept_values": total_values,
        "total_aliases": total_aliases,
        "categories": len(proposal["categories"]),
    }

    # Save proposal
    proposal_path = output_dir / "v3-expansion-comprehensive.json"
    with open(proposal_path, "w") as f:
        json.dump(proposal, f, indent=2)

    print(f"\nTotal statistics:")
    print(f"  Categories: {len(proposal['categories'])}")
    print(f"  Concept values: {total_values}")
    print(f"  Aliases: {total_aliases}")

    # Generate readable inventory
    inventory = "# Comprehensive V3 Expansion Proposal\n\n"
    inventory += f"**Coverage:** {total_values} legal concepts across {len(proposal['categories'])} categories\n\n"

    for category in sorted(proposal["categories"].keys()):
        values = proposal["categories"][category]
        inventory += f"## {category.upper().replace('_', ' ')}\n\n"

        # Group in columns of 3 for readability
        terms = sorted(values.keys())
        for i in range(0, len(terms), 3):
            batch = terms[i:i+3]
            inventory += " | ".join(f"**{t}**" for t in batch) + "\n"

        inventory += "\n"

    inventory_path = output_dir / "v3-expansion-comprehensive-inventory.md"
    with open(inventory_path, "w") as f:
        f.write(inventory)

    print(f"\n✓ Proposal saved to: {proposal_path}")
    print(f"✓ Inventory saved to: {inventory_path}")

    return proposal_path


if __name__ == "__main__":
    build_comprehensive_proposal()
