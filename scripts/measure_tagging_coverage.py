#!/usr/bin/env python3
"""Measure V3 tagging coverage before and after expansion.

Uses the CoreLegalTaggerV3 to tag a sample of real cases and computes:
- Percentage of cases with at least one tag
- Tag frequency distribution
- Coverage improvement from expansion
"""

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

# Import the tagging system
try:
    from backend.tagging.core_legal_tagger_v3 import CoreLegalTaggerV3
except ImportError:
    print("Error: Could not import CoreLegalTaggerV3. Running in demo mode.")
    CoreLegalTaggerV3 = None


def load_proposal(path: Path) -> dict[str, Any]:
    """Load a V3 proposal JSON."""
    with open(path) as f:
        return json.load(f)


def measure_coverage(
    cases: list[dict[str, str]],
    proposal: dict[str, Any],
    tagger: CoreLegalTaggerV3 | None = None
) -> dict[str, Any]:
    """Measure tagging coverage on a set of cases."""

    if not tagger:
        # Demo mode: simple regex-based matching
        return measure_coverage_demo(cases, proposal)

    results = {
        "total_cases": len(cases),
        "cases_with_tags": 0,
        "total_tags_applied": 0,
        "tag_frequency": Counter(),
        "case_tag_counts": [],
        "categories_used": set(),
    }

    for case in cases:
        text = case.get("text", "")
        if not text:
            continue

        tags = tagger.tag(text)

        if tags:
            results["cases_with_tags"] += 1

        results["total_tags_applied"] += len(tags)

        for tag in tags:
            tag_key = f"{tag.category}:{tag.value}"
            results["tag_frequency"][tag_key] += 1
            results["categories_used"].add(tag.category)

        results["case_tag_counts"].append(len(tags))

    results["categories_used"] = sorted(list(results["categories_used"]))

    # Compute coverage percentage
    coverage_pct = (results["cases_with_tags"] / results["total_cases"] * 100) if results["total_cases"] > 0 else 0
    results["coverage_percentage"] = coverage_pct

    # Top tags
    results["top_tags"] = dict(results["tag_frequency"].most_common(20))

    return results


def measure_coverage_demo(
    cases: list[dict[str, str]],
    proposal: dict[str, Any]
) -> dict[str, Any]:
    """Demo coverage measurement using simple regex matching."""

    # Build a simple matcher from the proposal
    matcher = {}
    for category, values in proposal.get("categories", {}).items():
        for value, aliases in values.items():
            for alias in aliases:
                if alias not in matcher:
                    matcher[alias.lower()] = []
                matcher[alias.lower()].append((category, value))

    results = {
        "total_cases": len(cases),
        "cases_with_tags": 0,
        "total_tags_applied": 0,
        "tag_frequency": Counter(),
        "case_tag_counts": [],
        "categories_used": set(),
    }

    for case in cases:
        text = (case.get("text", "") or "").lower()
        if not text:
            continue

        case_tags = set()
        for alias, tags in matcher.items():
            if alias in text:
                for category, value in tags:
                    tag_key = f"{category}:{value}"
                    case_tags.add(tag_key)
                    results["tag_frequency"][tag_key] += 1
                    results["categories_used"].add(category)

        if case_tags:
            results["cases_with_tags"] += 1

        results["total_tags_applied"] += len(case_tags)
        results["case_tag_counts"].append(len(case_tags))

    results["categories_used"] = sorted(list(results["categories_used"]))

    # Compute coverage percentage
    coverage_pct = (results["cases_with_tags"] / results["total_cases"] * 100) if results["total_cases"] > 0 else 0
    results["coverage_percentage"] = coverage_pct

    # Top tags
    results["top_tags"] = dict(results["tag_frequency"].most_common(20))

    return results


def main():
    """Main measurement pipeline."""
    output_dir = Path("/mnt/project-files/tagging")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Try to load sample cases from A2AJ mining output or other source
    sample_cases = []

    # Look for cached A2AJ cases
    a2aj_cache = Path("/tmp/a2aj_sample_cases.json")
    if a2aj_cache.exists():
        with open(a2aj_cache) as f:
            sample_cases = json.load(f)
        print(f"Loaded {len(sample_cases)} cases from cache")

    if not sample_cases:
        print("No sample cases available for measurement")
        print("Continuing with proposal generation...")
        return

    # Load the original V3 proposal
    original_proposal_path = Path("data/eval/reports/tagging-v3-core-whitelist-proposal.json")
    if not original_proposal_path.exists():
        print(f"Warning: Original proposal not found at {original_proposal_path}")
        original_proposal = {"categories": {}}
    else:
        original_proposal = load_proposal(original_proposal_path)

    # Load the expanded A2AJ proposal if it exists
    expanded_proposal_path = output_dir / "v3-expansion-a2aj-mined.json"
    if expanded_proposal_path.exists():
        expanded_proposal = load_proposal(expanded_proposal_path)
    else:
        print("Warning: Expanded proposal not yet available")
        expanded_proposal = {"categories": {}}

    print(f"Measuring coverage on {len(sample_cases)} cases...")
    print("\n=== BEFORE EXPANSION ===")
    before = measure_coverage(sample_cases, original_proposal)

    print(f"Cases with ≥1 tag: {before['cases_with_tags']}/{before['total_cases']} ({before['coverage_percentage']:.1f}%)")
    print(f"Total tags applied: {before['total_tags_applied']}")
    print(f"Categories used: {len(before['categories_used'])}")
    print(f"Top 5 tags:")
    for i, (tag, count) in enumerate(list(before['tag_frequency'].most_common(5)), 1):
        print(f"  {i}. {tag}: {count}")

    print("\n=== AFTER EXPANSION ===")
    after = measure_coverage(sample_cases, expanded_proposal)

    print(f"Cases with ≥1 tag: {after['cases_with_tags']}/{after['total_cases']} ({after['coverage_percentage']:.1f}%)")
    print(f"Total tags applied: {after['total_tags_applied']}")
    print(f"Categories used: {len(after['categories_used'])}")
    print(f"Top 5 tags:")
    for i, (tag, count) in enumerate(list(after['tag_frequency'].most_common(5)), 1):
        print(f"  {i}. {tag}: {count}")

    # Generate report
    improvement_pct = after['coverage_percentage'] - before['coverage_percentage']

    report = f"""# V3 Tagging Coverage Measurement Report

## Dataset
- **Test cases**: {len(sample_cases)} FC and RAD decisions
- **Measurement date**: Real case data

## Results

### Before Expansion
- **Cases with ≥1 tag**: {before['cases_with_tags']}/{before['total_cases']} ({before['coverage_percentage']:.1f}%)
- **Total tags applied**: {before['total_tags_applied']}
- **Average tags per case**: {before['total_tags_applied']/before['total_cases']:.2f}
- **Categories used**: {len(before['categories_used'])}

### After Expansion
- **Cases with ≥1 tag**: {after['cases_with_tags']}/{after['total_cases']} ({after['coverage_percentage']:.1f}%)
- **Total tags applied**: {after['total_tags_applied']}
- **Average tags per case**: {after['total_tags_applied']/after['total_cases']:.2f}
- **Categories used**: {len(after['categories_used'])}

### Coverage Improvement
- **Absolute improvement**: {improvement_pct:.1f} percentage points
- **Relative improvement**: {(after['coverage_percentage']/before['coverage_percentage']-1)*100:.1f}% increase
- **New tags applied**: {after['total_tags_applied'] - before['total_tags_applied']}

## Top 10 Tags Before Expansion
"""
    for i, (tag, count) in enumerate(list(before['tag_frequency'].most_common(10)), 1):
        report += f"{i}. {tag}: {count} cases\n"

    report += "\n## Top 10 Tags After Expansion\n"
    for i, (tag, count) in enumerate(list(after['tag_frequency'].most_common(10)), 1):
        report += f"{i}. {tag}: {count} cases\n"

    # Save report
    report_path = output_dir / "v3-expansion-coverage-measurement.md"
    with open(report_path, "w") as f:
        f.write(report)

    # Save JSON results
    results_path = output_dir / "v3-expansion-coverage-results.json"
    with open(results_path, "w") as f:
        json.dump({
            "before": {k: v for k, v in before.items() if k != "tag_frequency"},
            "after": {k: v for k, v in after.items() if k != "tag_frequency"},
            "improvement": {
                "absolute_percentage_points": improvement_pct,
                "relative_percentage": (after['coverage_percentage']/before['coverage_percentage']-1)*100 if before['coverage_percentage'] > 0 else 0,
            }
        }, f, indent=2)

    print(f"\nReport saved to: {report_path}")
    print(f"Results saved to: {results_path}")


if __name__ == "__main__":
    main()
