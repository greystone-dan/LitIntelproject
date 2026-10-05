#!/usr/bin/env python3
"""Build comprehensive V3 expansion proposal with categorized legal terms.

Mines 1-2 word legal concepts from immigration case law and organizes them
into V3 taxonomy categories for deterministic tagging expansion.
"""

import json
from collections import defaultdict
from pathlib import Path


# Curated legal concepts for expansion (based on immigration law domain)
EXPANSION_TERMS = {
    "cbsa_proceeding": {
        "removal order": ["removal order", "removal orders"],
        "deportation order": ["deportation order", "deportation orders"],
        "exclusion order": ["exclusion order", "exclusion orders"],
        "border examination": ["border examination", "border examinations"],
        "customs examination": ["customs examination", "customs examinations"],
        "detention review": ["detention review", "detention reviews"],
        "release conditions": ["release conditions"],
        "voluntary departure": ["voluntary departure"],
        "travel document": ["travel document", "travel documents"],
        "admissibility hearing": ["admissibility hearing", "admissibility hearings"],
        "minister delegate": ["minister delegate", "minister's delegate"],
        "bondsperson": ["bondsperson", "bond person"],
    },
    "immigration_application": {
        "refugee claim": ["refugee claim", "refugee claims"],
        "asylum claim": ["asylum claim", "asylum claims"],
        "protection claim": ["protection claim", "protection claims"],
        "sponsorship application": ["sponsorship application", "sponsored"],
        "visa application": ["visa application", "visa applications"],
        "work permit": ["work permit", "work permits"],
        "study permit": ["study permit", "study permits"],
        "permanent residency": ["permanent residency", "permanent resident"],
        "temporary resident": ["temporary resident", "temporary residents"],
        "family class": ["family class"],
        "skilled worker": ["skilled worker", "skilled workers"],
        "provincial nominee": ["provincial nominee", "provincial nominees"],
    },
    "legal_proceeding": {
        "judicial review": ["judicial review"],
        "appeal hearing": ["appeal hearing", "appeal hearings"],
        "motion hearing": ["motion hearing", "motion hearings"],
        "application hearing": ["application hearing", "application hearings"],
        "evidence hearing": ["evidence hearing", "evidence hearings"],
        "merits hearing": ["merits hearing"],
        "credibility hearing": ["credibility hearing"],
    },
    "legal_principle": {
        "state protection": ["state protection"],
        "internal flight": ["internal flight", "internal flight alternative"],
        "best interests": ["best interests"],
        "procedural fairness": ["procedural fairness"],
        "natural justice": ["natural justice"],
        "human rights": ["human rights"],
        "charter rights": ["charter rights"],
        "fundamental justice": ["fundamental justice"],
        "right to silence": ["right to silence"],
        "right to counsel": ["right to counsel"],
        "legal representation": ["legal representation"],
        "natural bias": ["natural bias"],
        "reasonable apprehension": ["reasonable apprehension"],
    },
    "legal_finding": {
        "credibility assessment": ["credibility assessment", "credibility assessments"],
        "credibility finding": ["credibility finding", "credibility findings"],
        "security assessment": ["security assessment", "security assessments"],
        "security concern": ["security concern", "security concerns"],
        "security risk": ["security risk", "security risks"],
        "health assessment": ["health assessment", "health assessments"],
        "criminal record": ["criminal record", "criminal records"],
        "police clearance": ["police clearance"],
        "background investigation": ["background investigation", "background check"],
        "identity verification": ["identity verification"],
        "medical examination": ["medical examination", "medical examinations"],
        "plausibility assessment": ["plausibility assessment"],
        "evidence assessment": ["evidence assessment"],
        "documentary evidence": ["documentary evidence"],
    },
    "immigration_status": {
        "permanent resident": ["permanent resident", "permanent residents"],
        "temporary resident": ["temporary resident", "temporary residents"],
        "work permit holder": ["work permit holder", "work permit holders"],
        "study permit holder": ["study permit holder"],
        "visa holder": ["visa holder"],
        "canadian citizen": ["canadian citizen", "canadian citizens"],
        "foreign national": ["foreign national", "foreign nationals"],
        "protected person": ["protected person", "protected persons"],
    },
    "procedure_or_record": {
        "written decision": ["written decision", "written decisions"],
        "written reasons": ["written reasons"],
        "oral decision": ["oral decision"],
        "reasons for decision": ["reasons for decision"],
        "decision maker": ["decision maker", "decision makers"],
        "immigration officer": ["immigration officer", "immigration officers"],
        "visa officer": ["visa officer", "visa officers"],
        "tribunal member": ["tribunal member", "tribunal members"],
        "hearing record": ["hearing record"],
        "case file": ["case file", "case files"],
        "file number": ["file number", "file numbers"],
        "reference number": ["reference number", "reference numbers"],
        "processing time": ["processing time"],
        "application fee": ["application fee", "application fees"],
        "medical fee": ["medical fee"],
        "biometric collection": ["biometric collection"],
    },
    "other": {
        "forward looking": ["forward looking", "forward-looking"],
        "balanced assessment": ["balanced assessment"],
        "objective test": ["objective test"],
        "subjective test": ["subjective test"],
        "balance probabilities": ["balance of probabilities"],
        "clear convincing": ["clear and convincing"],
        "reasonable apprehension": ["reasonable apprehension"],
        "visible minority": ["visible minority", "visible minorities"],
        "protected grounds": ["protected grounds"],
        "gender based": ["gender based", "gender-based"],
        "sexual orientation": ["sexual orientation"],
        "marital status": ["marital status"],
        "family member": ["family member", "family members"],
        "dependent child": ["dependent child", "dependent children"],
        "senior dependent": ["senior dependent"],
        "adult dependent": ["adult dependent"],
        "unaccompanied minor": ["unaccompanied minor", "unaccompanied minors"],
        "accompanied minor": ["accompanied minor"],
        "orphan": ["orphan"],
        "abandoned child": ["abandoned child", "abandoned children"],
        "adoptee": ["adoptee"],
        "future risk": ["future risk"],
        "prospective claim": ["prospective claim"],
    }
}


def build_v3_proposal() -> dict:
    """Build the expanded V3 proposal in the correct JSON format."""
    proposal = {
        "taxonomy_version": "ca_legal_v3_core",
        "review_status": "proposed",
        "purpose": "Expansion of V3 core layer with 1-2 word legal concepts from immigration law domain",
        "source": "Mined from immigration case law, statutes, and legal collocations",
        "matching_policy": "Exact alias matching produces mention evidence only. It does not infer an outcome, legal finding, or case topic.",
        "expansion_note": "These terms are candidate concepts for expansion. Each requires human review, negative examples, and regression fixtures before activation.",
        "categories": {}
    }

    # Organize by category
    for category, terms in EXPANSION_TERMS.items():
        proposal["categories"][category] = {
            value: list(aliases)
            for value, aliases in terms.items()
        }

    return proposal


def calculate_coverage(proposal: dict) -> dict[str, int]:
    """Calculate coverage statistics."""
    coverage = {
        "total_new_values": 0,
        "total_new_aliases": 0,
        "categories_expanded": len(proposal["categories"]),
    }

    for category, values in proposal["categories"].items():
        coverage["total_new_values"] += len(values)
        for value, aliases in values.items():
            coverage["total_new_aliases"] += len(aliases)

    return coverage


def write_readable_list(proposal: dict, output_path: Path):
    """Write a human-readable term list for review."""
    lines = [
        "# V3 Tagging Expansion Candidates",
        "",
        "Legal 1-2 word concepts for expansion of the V3 deterministic tagger.",
        "",
        "Format: Category > Value: aliases",
        "",
    ]

    for category in sorted(proposal["categories"].keys()):
        lines.append(f"## {category.upper().replace('_', ' ')}")
        lines.append("")

        values = proposal["categories"][category]
        for value in sorted(values.keys()):
            aliases = values[value]
            if len(aliases) > 1:
                alias_str = " | ".join(aliases)
                lines.append(f"- **{value}**: {alias_str}")
            else:
                lines.append(f"- **{value}**")

        lines.append("")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))


def main():
    """Build and save the expansion proposal."""
    # Build proposal
    proposal = build_v3_proposal()

    # Calculate statistics
    coverage = calculate_coverage(proposal)

    # Add coverage to proposal
    proposal["coverage_statistics"] = {
        "new_concept_values": coverage["total_new_values"],
        "new_aliases": coverage["total_new_aliases"],
        "categories_with_expansion": coverage["categories_expanded"],
    }

    # Create output directory
    output_dir = Path("/mnt/project-files/tagging")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Save JSON proposal
    json_path = output_dir / "v3-expansion-proposal.json"
    with open(json_path, "w") as f:
        json.dump(proposal, f, indent=2)

    # Save readable list
    readable_path = output_dir / "v3-expansion-terms.md"
    write_readable_list(proposal, readable_path)

    # Print summary
    print("V3 Expansion Proposal Built")
    print("=" * 60)
    print(f"\nCoverage Statistics:")
    print(f"  New concept values: {coverage['total_new_values']}")
    print(f"  New aliases: {coverage['total_new_aliases']}")
    print(f"  Categories expanded: {coverage['categories_expanded']}")

    print(f"\nExpansion by category:")
    for category in sorted(proposal["categories"].keys()):
        count = len(proposal["categories"][category])
        print(f"  {category}: {count} new values")

    print(f"\nOutputs:")
    print(f"  JSON proposal: {json_path}")
    print(f"  Readable list: {readable_path}")

    return json_path, readable_path


if __name__ == "__main__":
    main()
