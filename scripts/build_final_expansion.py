#!/usr/bin/env python3
"""Build final V3 expansion proposal with measured coverage.

Takes mined concepts, combines with existing proposal, and generates
a comprehensive expansion JSON and coverage report.
"""

import json
from pathlib import Path
from collections import defaultdict

def load_json(path: Path) -> dict:
    """Load JSON file safely."""
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)


def build_final_proposal():
    """Build the final expansion proposal."""

    output_dir = Path("/mnt/project-files/tagging")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load the original V3 proposal
    original_path = Path("data/eval/reports/tagging-v3-core-whitelist-proposal.json")
    original = load_json(original_path)

    print("Building final expansion proposal...")
    print(f"Original: {len(original.get('categories', {}))} categories")

    # Load mined concepts if available
    mined_path = output_dir / "v3-expansion-a2aj-mined.json"
    mined = load_json(mined_path)

    # Merge proposals
    final_proposal = {
        "taxonomy_version": "ca_legal_v3_core",
        "review_status": "proposed",
        "purpose": "Expanded V3 core layer with high-frequency legal concepts from Canadian immigration case law",
        "source": "Mined from A2AJ dataset + domain expertise",
        "matching_policy": "Exact alias matching produces mention evidence only. It does not infer an outcome, legal finding, or case topic.",
        "expansion_note": "These concepts are candidates for V3 expansion. Each requires human review, negative examples, and regression fixtures before activation.",
        "categories": {}
    }

    # Copy original categories
    if "categories" in original:
        for cat, values in original["categories"].items():
            final_proposal["categories"][cat] = values.copy()

    # Merge mined categories
    if "categories" in mined:
        for cat, values in mined["categories"].items():
            if cat in final_proposal["categories"]:
                # Merge - add new mined terms
                existing = final_proposal["categories"][cat]
                for value, aliases in values.items():
                    if value not in existing:
                        existing[value] = aliases
            else:
                # New category
                final_proposal["categories"][cat] = values

    # Calculate stats
    total_values = sum(len(vals) for vals in final_proposal["categories"].values())
    total_aliases = sum(
        sum(len(aliases) for aliases in vals.values())
        for vals in final_proposal["categories"].values()
    )

    final_proposal["coverage_statistics"] = {
        "total_concept_values": total_values,
        "total_aliases": total_aliases,
        "categories": len(final_proposal["categories"]),
    }

    # Save final proposal
    final_path = output_dir / "v3-expansion-final-proposal.json"
    with open(final_path, "w") as f:
        json.dump(final_proposal, f, indent=2)

    print(f"\nFinal proposal statistics:")
    print(f"  Total categories: {len(final_proposal['categories'])}")
    print(f"  Total concept values: {total_values}")
    print(f"  Total aliases: {total_aliases}")

    # Generate human-readable inventory
    inventory = "# V3 Final Expansion Proposal\n\n"
    inventory += f"**Statistics:**\n- Total categories: {len(final_proposal['categories'])}\n"
    inventory += f"- Total concept values: {total_values}\n"
    inventory += f"- Total aliases: {total_aliases}\n\n"

    for category in sorted(final_proposal["categories"].keys()):
        values = final_proposal["categories"][category]
        inventory += f"## {category.upper().replace('_', ' ')}\n\n"

        for value in sorted(values.keys()):
            aliases = values[value]
            if len(aliases) > 1:
                alias_str = " | ".join(aliases)
                inventory += f"- **{value}**: {alias_str}\n"
            else:
                inventory += f"- **{value}**\n"

        inventory += "\n"

    inventory_path = output_dir / "v3-expansion-final-inventory.md"
    with open(inventory_path, "w") as f:
        f.write(inventory)

    print(f"\n✓ Final proposal saved to: {final_path}")
    print(f"✓ Inventory saved to: {inventory_path}")

    return final_path, inventory_path


if __name__ == "__main__":
    build_final_proposal()
