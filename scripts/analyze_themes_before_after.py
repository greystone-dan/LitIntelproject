#!/usr/bin/env python3
"""
Analyze theme discovery before and after stopword filtering.

Run this on the PC with access to the caselibrary database:
    python scripts/analyze_themes_before_after.py

Outputs: logs/theme_analysis_before_after.txt
"""
import sys
from pathlib import Path
from collections import Counter

# Ensure we can import backend modules
repo_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo_root))

from backend.database import SessionLocal
from backend.reader_service import build_case_reader_data

def discover_themes_without_filter(case_evidence_summaries):
    """Original theme discovery without stopword filtering."""
    all_occurrences = []

    for case_id, evidence_summary in case_evidence_summaries.items():
        if not evidence_summary.units:
            continue
        for unit in evidence_summary.units:
            for subtheme in unit.subthemes:
                all_occurrences.append((subtheme, case_id, unit.unit_index))

    if not all_occurrences:
        return []

    themes = {}
    processed = set()

    for idx, (subtheme, case_id, unit_index) in enumerate(all_occurrences):
        if idx in processed:
            continue

        theme_key = frozenset(term.lower() for term in subtheme.key_terms)
        theme_occurrences = [(case_id, unit_index, subtheme.key_terms)]
        processed.add(idx)

        for other_idx, (other_subtheme, other_case_id, other_unit_index) in enumerate(all_occurrences):
            if other_idx in processed or other_idx <= idx:
                continue
            other_key = frozenset(term.lower() for term in other_subtheme.key_terms)

            # Jaccard similarity
            intersection = len(theme_key & other_key)
            union = len(theme_key | other_key)
            similarity = intersection / union if union else 0

            if similarity >= 0.4:
                theme_occurrences.append((other_case_id, other_unit_index, other_subtheme.key_terms))
                processed.add(other_idx)

        if len(theme_occurrences) >= 2:
            themes[theme_key] = theme_occurrences

    results = []
    for theme_key, occurrences in themes.items():
        all_terms = []
        for _, _, key_terms in occurrences:
            all_terms.extend(key_terms)

        term_counts = Counter(term.lower() for term in all_terms)
        top_terms = [t for t, _ in term_counts.most_common(5)]
        theme_name = " + ".join(top_terms[:3]) if top_terms else "Unnamed"

        results.append({
            "theme_name": theme_name,
            "key_terms": top_terms,
            "occurrence_count": len(occurrences),
        })

    return sorted(results, key=lambda x: x["occurrence_count"], reverse=True)


def discover_themes_with_filter(case_evidence_summaries):
    """Theme discovery WITH stopword filtering (from claude/theme-discovery)."""
    STOPWORDS = {
        "appearances", "applicant", "attorney", "order", "canada",
        "dated", "style", "cause", "case", "court", "judge",
        "federal", "decision", "reasons", "find", "hold", "conclude",
        "agreement", "application", "motion", "petition", "request",
        "pursuant", "section", "article", "act", "law", "regulation",
        "citizenship", "immigration", "department", "minister",
    }

    all_occurrences = []

    for case_id, evidence_summary in case_evidence_summaries.items():
        if not evidence_summary.units:
            continue
        for unit in evidence_summary.units:
            for subtheme in unit.subthemes:
                all_occurrences.append((subtheme, case_id, unit.unit_index))

    if not all_occurrences:
        return []

    themes = {}
    processed = set()

    for idx, (subtheme, case_id, unit_index) in enumerate(all_occurrences):
        if idx in processed:
            continue

        theme_key = frozenset(term.lower() for term in subtheme.key_terms)
        theme_occurrences = [(case_id, unit_index, subtheme.key_terms)]
        processed.add(idx)

        for other_idx, (other_subtheme, other_case_id, other_unit_index) in enumerate(all_occurrences):
            if other_idx in processed or other_idx <= idx:
                continue
            other_key = frozenset(term.lower() for term in other_subtheme.key_terms)

            intersection = len(theme_key & other_key)
            union = len(theme_key | other_key)
            similarity = intersection / union if union else 0

            if similarity >= 0.4:
                theme_occurrences.append((other_case_id, other_unit_index, other_subtheme.key_terms))
                processed.add(other_idx)

        if len(theme_occurrences) >= 2:
            themes[theme_key] = theme_occurrences

    results = []
    for theme_key, occurrences in themes.items():
        all_terms = []
        for _, _, key_terms in occurrences:
            all_terms.extend(key_terms)

        # FILTER stopwords here
        term_counts = Counter(term.lower() for term in all_terms if term.lower() not in STOPWORDS)
        top_terms = [t for t, _ in term_counts.most_common(5)]

        # Skip if no meaningful terms
        if not top_terms:
            continue

        theme_name = " + ".join(top_terms[:3]) if top_terms else "Unnamed"

        results.append({
            "theme_name": theme_name,
            "key_terms": top_terms,
            "occurrence_count": len(occurrences),
        })

    return sorted(results, key=lambda x: x["occurrence_count"], reverse=True)


def main():
    print("Loading evidence summaries for 50 real FC cases (IDs 6-55)...")
    case_evidence_summaries = {}

    with SessionLocal() as db:
        for case_id in range(6, 56):
            try:
                reader_data = build_case_reader_data(case_id, db)
                if reader_data and reader_data.evidence_summary:
                    case_evidence_summaries[case_id] = reader_data.evidence_summary
            except Exception as e:
                print(f"  Skipped case {case_id}: {e}")

    if not case_evidence_summaries:
        print("✗ Failed to load any case evidence summaries")
        return False

    print(f"✓ Loaded {len(case_evidence_summaries)} cases\n")

    # Analyze before
    print("Computing themes WITHOUT stopword filter...")
    themes_before = discover_themes_without_filter(case_evidence_summaries)
    print(f"✓ Found {len(themes_before)} themes\n")

    # Analyze after
    print("Computing themes WITH stopword filter...")
    themes_after = discover_themes_with_filter(case_evidence_summaries)
    print(f"✓ Found {len(themes_after)} themes\n")

    # Generate report
    output = []
    output.append("THEME DISCOVERY: BEFORE vs AFTER STOPWORD FILTERING\n")
    output.append("=" * 70)
    output.append(f"\nAnalyzed: 50 real FC immigration cases (IDs 6-55)\n")

    output.append("\n" + "=" * 70)
    output.append("BEFORE FILTERING (procedural noise included)")
    output.append("=" * 70 + "\n")
    output.append(f"Total themes: {len(themes_before)}\n")
    for i, theme in enumerate(themes_before[:10], 1):
        output.append(f"{i}. {theme['theme_name']}")
        output.append(f"   Occurrences: {theme['occurrence_count']}")
        output.append(f"   Key terms: {', '.join(theme['key_terms'][:5])}\n")

    output.append("\n" + "=" * 70)
    output.append("AFTER FILTERING (meaningful themes only)")
    output.append("=" * 70 + "\n")
    output.append(f"Total themes: {len(themes_after)}\n")
    for i, theme in enumerate(themes_after[:10], 1):
        output.append(f"{i}. {theme['theme_name']}")
        output.append(f"   Occurrences: {theme['occurrence_count']}")
        output.append(f"   Key terms: {', '.join(theme['key_terms'][:5])}\n")

    # Summary
    output.append("\n" + "=" * 70)
    output.append("SUMMARY")
    output.append("=" * 70)
    if len(themes_before) > 0:
        reduction = 100 * (len(themes_before) - len(themes_after)) / len(themes_before)
    else:
        reduction = 0
    output.append(f"Reduction: {len(themes_before)} → {len(themes_after)} themes ({reduction:.1f}% filtered)")
    output.append("\nStopwords removed:")
    output.append("  appearances, applicant, attorney, order, canada, dated, style, cause,")
    output.append("  case, court, judge, federal, decision, reasons, citizenship, immigration,")
    output.append("  and 16 more procedural/boilerplate terms")

    text = "\n".join(output)
    print(text)

    # Write to file
    out_path = Path("logs") / "theme_analysis_before_after.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text)
    print(f"\n✓ Results saved to {out_path}")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
