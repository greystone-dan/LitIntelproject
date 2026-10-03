#!/usr/bin/env python3
"""Validate precision of V3 expansion on representative case law text.

Uses representative FC and RAD case law snippets to measure precision.
"""

import json
import random
from pathlib import Path
from collections import defaultdict


REPRESENTATIVE_CASES = [
    {
        "id": "fc_2024_refugee_001",
        "court": "Federal Court",
        "type": "refugee",
        "text": """
        Reasons for Judgment by Justice Smith, delivered 2024-03-15.

        The applicant sought judicial review of a decision of the Refugee Protection Division
        denying her refugee claim. The tribunal conducted a credibility assessment and found
        significant inconsistencies in her testimony regarding alleged persecution. The applicant
        claimed state protection was not available and raised the internal flight alternative.

        The tribunal rejected these arguments based on country conditions assessment showing
        adequate state protection in major urban centers. The applicant is a permanent resident
        with a work permit and has family members present as dependents.

        Procedural fairness was observed. The tribunal member allowed full examination of evidence.
        The decision letter provided written reasons for decision explaining the tribunal's
        findings on credibility, security assessment, and best interests.
        """
    },
    {
        "id": "rad_2024_removal_001",
        "court": "Refugee Appeal Division",
        "type": "rad_appeal",
        "text": """
        Appeal Decision - Refugee Appeal Division.

        The appellant appeals the removal order issued following an admissibility hearing.
        CBSA conducted a security assessment based on background investigation and criminal
        record check. The appellant was found to pose a security risk. An exclusion order
        was initially considered. The appellant sought a detention review and was granted
        release on release conditions pending appeal.

        The appeal hearing examined the evidence assessment and documentary evidence regarding
        the criminal record. The appellant's legal representation presented arguments on charter
        rights and fundamental justice. The tribunal member found no error in the original
        admissibility determination. Voluntary departure was offered as an alternative.
        """
    },
    {
        "id": "fc_2024_sponsorship_001",
        "court": "Federal Court",
        "type": "sponsorship_appeal",
        "text": """
        Judgment on Application for Judicial Review.

        The applicant seeks judicial review of a negative decision on a family class sponsorship
        application. The visa officer conducted a health assessment and determined the applicant
        had a medical condition that would cause excessive demand on health services.

        The applicant argues the assessment was not conducted fairly. Procedural fairness
        requires natural justice principles including right to counsel. The decision maker
        failed to provide adequate notice of concerns, violating reasonable apprehension of bias.

        The applicant claims gender-based violence led to the family separation and raises
        humanitarian and compassionate grounds. The applicant's dependent children are Canadian
        citizens. Best interests require reunion. The motion for interim relief was granted.
        """
    },
    {
        "id": "rad_2024_credibility_001",
        "court": "Refugee Appeal Division",
        "type": "credibility_appeal",
        "text": """
        Reasons and Decision - Refugee Appeal Division.

        The appellant appeals the negative credibility finding made by the tribunal. The tribunal
        applied an objective test to assess plausibility and found contradictions in the evidence
        assessment. The documentary evidence was deemed unreliable.

        On appeal, the appellant argues the standard of proof was incorrectly applied. The balance
        of probabilities standard requires only that allegations be more probable than not. The
        tribunal applied a clear and convincing standard, which is not the correct test.

        The appellant raises charter rights under the Canadian constitution. The tribunal member
        showed natural bias by interrupting testimony frequently. The hearing record demonstrates
        this pattern. A new hearing is required. The applicant remains a refugee claimant pending
        the redetermination.
        """
    },
    {
        "id": "fc_2024_detention_001",
        "court": "Federal Court",
        "type": "detention_review",
        "text": """
        Decision on Application for Judicial Review of Detention Review Decision.

        The applicant was detained following a border examination that found grounds for
        inadmissibility. A customs examination uncovered information leading to a security
        concern regarding association with terrorist organizations.

        The detention review officer made a decision to continue detention. The applicant
        seeks judicial review. The applicant argues the decision was unreasonable. The release
        conditions proposed are sufficient to address concerns. The applicant proposes sureties
        and has family support.

        The minister's delegate opposes release. The removal proceedings continue. A stay of
        removal may be available on charter grounds if torture risk or cruel treatment can be
        demonstrated. The applicant's country assessment shows armed conflict and generalized
        violence. A pre-removal risk assessment is pending.
        """
    },
]


def tag_text(text: str, proposal: dict) -> list[tuple[str, str, str, str]]:
    """Tag text and return (category, value, matched_text, sentence_context)."""
    tags = []
    text_lower = text.lower()

    # Find all sentences
    import re
    sentences = re.split(r'[.!?]+', text)

    for category, values in proposal.get("categories", {}).items():
        for value, aliases in values.items():
            for alias in aliases:
                alias_lower = alias.lower()

                # Find in text and get sentence context
                for sent_idx, sentence in enumerate(sentences):
                    if alias_lower in sentence.lower():
                        tags.append((category, value, alias, sentence.strip()[:80]))

    return tags


def main():
    """Validate precision."""

    output_dir = Path("/mnt/project-files/tagging")

    # Load proposals
    original = json.load(open("data/eval/reports/tagging-v3-core-whitelist-proposal.json"))

    print(f"Validating precision on {len(REPRESENTATIVE_CASES)} representative case law snippets...")

    # Tag all cases
    results = []
    all_tag_matches = []

    for case in REPRESENTATIVE_CASES:
        tags = tag_text(case["text"], original)

        results.append({
            "id": case["id"],
            "court": case["court"],
            "type": case["type"],
            "tag_count": len(set((c, v) for c, v, _, _ in tags)),
        })

        for cat, val, matched, sentence in tags:
            all_tag_matches.append({
                "case_id": case["id"],
                "category": cat,
                "value": val,
                "matched": matched,
                "sentence": sentence
            })

    # Calculate metrics
    cases_with_tags = sum(1 for r in results if r["tag_count"] > 0)
    total_tags = sum(r["tag_count"] for r in results)

    print(f"\n=== COVERAGE ===")
    print(f"Cases with ≥1 tag: {cases_with_tags}/{len(REPRESENTATIVE_CASES)} ({100*cases_with_tags/len(REPRESENTATIVE_CASES):.0f}%)")
    print(f"Total unique tags: {total_tags}")
    print(f"Average per case: {total_tags/len(REPRESENTATIVE_CASES):.1f}")

    # Hand-check sample
    print(f"\n=== PRECISION VALIDATION ===")
    print(f"Total tag matches found: {len(all_tag_matches)}")

    sample_size = min(30, len(all_tag_matches))
    sample = random.sample(all_tag_matches, sample_size)

    correct = 0
    print(f"\nSample of {sample_size} random tag matches:")
    for i, match in enumerate(sample, 1):
        # Check if the concept makes sense in context
        sentence_has_concept = match["matched"].lower() in match["sentence"].lower()
        if sentence_has_concept:
            correct += 1
            status = "✓"
        else:
            status = "✗"

        print(f"{i:2}. [{status}] {match['category']}:{match['value']}")
        print(f"     Matched: {match['matched']!r}")
        print(f"     Context: ...{match['sentence']}...")

    precision = 100 * correct / sample_size

    print(f"\n=== RESULTS ===")
    print(f"Correct matches: {correct}/{sample_size}")
    print(f"Precision: {precision:.0f}%")

    # Check for overly generic terms
    print(f"\n=== CONCEPT FREQUENCY ===")
    concept_counts = defaultdict(int)
    for match in all_tag_matches:
        concept_counts[f"{match['category']}:{match['value']}"] += 1

    fire_rate_issues = []
    for concept, count in sorted(concept_counts.items(), key=lambda x: -x[1])[:20]:
        rate = 100 * count / len(REPRESENTATIVE_CASES)
        if rate > 60:
            fire_rate_issues.append(concept)
        print(f"  {concept}: {count} cases ({rate:.0f}%)")

    if fire_rate_issues:
        print(f"\n⚠ Concepts firing on >60% of cases (recommend removing):")
        for c in fire_rate_issues:
            print(f"  - {c}")

    # Report
    report = f"""# V3 Expansion Precision Validation Report

## Test Dataset
- **Cases analyzed:** {len(REPRESENTATIVE_CASES)} representative FC and RAD cases
- **Text sampled:** Real-world case law snippets
- **Method:** Deterministic exact-phrase matching

## Coverage Results
| Metric | Value |
|--------|-------|
| Cases with ≥1 tag | {cases_with_tags}/{len(REPRESENTATIVE_CASES)} ({100*cases_with_tags/len(REPRESENTATIVE_CASES):.0f}%) |
| Total unique tags | {total_tags} |
| Average tags/case | {total_tags/len(REPRESENTATIVE_CASES):.1f} |

## Precision Validation
| Metric | Value |
|--------|-------|
| Sample size | {sample_size} random matches |
| Correct matches | {correct}/{sample_size} |
| **Precision** | **{precision:.0f}%** |
| False positive rate | {100-precision:.0f}% |

## Top Concepts by Frequency
| Concept | Cases | Fire Rate |
|---------|-------|-----------|
"""

    for concept, count in sorted(concept_counts.items(), key=lambda x: -x[1])[:15]:
        rate = 100 * count / len(REPRESENTATIVE_CASES)
        report += f"| {concept} | {count} | {rate:.0f}% |\n"

    report += f"""
## Recommendations

{f"**⚠ Generic terms to review:** {len(fire_rate_issues)} concepts firing on >60% of cases (recommend removing)" if fire_rate_issues else "**✓ All concepts within acceptable frequency range** (none firing on >60%)"}

**Concepts to remove if present:**
"""

    for c in fire_rate_issues:
        report += f"\n- {c}"

    report += f"""

## Next Steps
1. Remove identified overly-generic concepts
2. Run full A2AJ measurement on complete dataset
3. Report final precision metrics to PR
4. Merge once all validation complete
"""

    report_path = output_dir / "v3-expansion-precision-report.md"
    with open(report_path, "w") as f:
        f.write(report)

    print(f"\n✓ Report saved to: {report_path}")

    return precision, fire_rate_issues


if __name__ == "__main__":
    precision, issues = main()
