#!/usr/bin/env python3
"""
Evaluate discussion units algorithm across versions on verified and hold-out cases.

Produces unified metrics table:
- Boundary agreement: exact, within-1, missed, spurious
- Separated by verified set (22 cases, can tune) and hold-out set (4 cases, locked)
- Can compare multiple parameter configurations or versions

Usage:
    python scripts/evaluate_discussion_units.py
    python scripts/evaluate_discussion_units.py --require-corroboration
"""

import json
import argparse
from pathlib import Path
from collections import defaultdict
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.contextual_authority.discussion_units import (
    ParagraphFeatures, ContinuityComponents, segment_discussion_units
)


def dict_to_paragraph_features(para_dict):
    return ParagraphFeatures(
        case_id=para_dict.get('case_id', 0),
        chunk_id=para_dict['chunk_id'],
        paragraph_index=para_dict['paragraph_index'],
        start_offset=para_dict['start_offset'],
        end_offset=para_dict['end_offset'],
        text=para_dict['text'],
        source_text_hash=para_dict.get('source_text_sha256', ''),
        source_paragraph_index=para_dict.get('source_paragraph_index', -1),
        citation_ids=tuple(para_dict.get('citation_ids', [])),
        statute_ids=tuple(para_dict.get('statute_ids', [])),
        tag_ids=tuple(para_dict.get('tag_ids', [])),
        is_heading=para_dict.get('is_heading', False),
    )


def dict_to_continuity_components(cont_dict):
    return ContinuityComponents(
        left_paragraph_index=cont_dict['left_paragraph_index'],
        right_paragraph_index=cont_dict['right_paragraph_index'],
        authority_overlap=cont_dict['authority_overlap'],
        statute_overlap=cont_dict['statute_overlap'],
        tag_overlap=cont_dict['tag_overlap'],
        text_overlap=cont_dict['text_overlap'],
        heading_boundary_penalty=cont_dict['heading_boundary_penalty'],
        signal_density_shift=cont_dict['signal_density_shift'],
        continuity_score=cont_dict['continuity_score'],
    )


def get_gold_boundaries(case_id, gold_meta, verified_gold):
    """Extract gold boundaries from either prior verified or new independent cases."""
    case_id_str = str(case_id)

    if case_id in gold_meta.get('prior_verified_cases', []):
        if case_id_str in verified_gold.get('gold_labels', {}):
            units = verified_gold['gold_labels'][case_id_str]['gold_unit_boundaries']
            boundaries = [0]
            for unit in units:
                start = unit['start']
                if start > 0 and start not in boundaries:
                    boundaries.append(start)
            return sorted(boundaries)

    if case_id in gold_meta.get('new_independent_cases', []):
        merged = gold_meta.get('merged_gold_labels', {})
        key = f'new_cases_{case_id}'
        if key in merged:
            return sorted(merged[key]['gold_unit_boundaries'])

    return None


def evaluate_set(case_list, set_name, gold_meta, verified_gold, require_corroboration=False):
    """Evaluate algorithm on a set of cases."""
    results = {
        'name': set_name,
        'total_cases': len(case_list),
        'exact': 0,
        'within_1': 0,
        'missed_total': 0,
        'spurious_total': 0,
        'cases_analyzed': 0,
        'cases': []
    }

    for case_id in sorted(case_list):
        gold = get_gold_boundaries(case_id, gold_meta, verified_gold)
        if not gold:
            continue

        det_path = Path(
            f'data/eval/llm_discussion_units_pilot/core_300_run/reports/'
            f'case_{case_id}_deterministic.json'
        )
        if not det_path.exists():
            continue

        with open(det_path) as f:
            det_data = json.load(f)

        paragraphs = [dict_to_paragraph_features(p) for p in det_data['paragraphs']]
        continuity = [dict_to_continuity_components(c) for c in det_data['continuity']]

        # Segment with specified parameters
        units = segment_discussion_units(
            paragraphs,
            continuity,
            require_corroboration_for_signal_vacuum=require_corroboration
        )
        predicted = sorted(set(u.start_paragraph for u in units))

        # Calculate metrics
        gold_set = set(gold)
        pred_set = set(predicted)

        exact_match = (gold_set == pred_set)
        within_1_match = all(
            abs(min([abs(p - g) for p in predicted], default=float('inf'))) <= 1
            for g in gold
        )
        missed = gold_set - pred_set
        spurious = pred_set - gold_set

        results['exact'] += 1 if exact_match else 0
        results['within_1'] += 1 if within_1_match else 0
        results['missed_total'] += len(missed)
        results['spurious_total'] += len(spurious)
        results['cases_analyzed'] += 1

        results['cases'].append({
            'case_id': case_id,
            'exact': exact_match,
            'within_1': within_1_match,
            'gold_count': len(gold),
            'pred_count': len(predicted),
            'missed': len(missed),
            'spurious': len(spurious),
        })

    return results


def main():
    parser = argparse.ArgumentParser(
        description='Evaluate discussion units algorithm on verified and hold-out cases'
    )
    parser.add_argument(
        '--require-corroboration',
        action='store_true',
        help='Require corroboration for signal vacuum boundaries (v1.5 improvement)'
    )
    args = parser.parse_args()

    # Load gold labels
    with open('/mnt/project-files/discussion-units/gold_set_labels_verified_22cases.json') as f:
        gold_meta = json.load(f)

    with open('/mnt/project-files/discussion-units/gold_set_labels_verified.json') as f:
        verified_gold = json.load(f)

    verified_cases = (
        gold_meta['prior_verified_cases'] + gold_meta['new_independent_cases']
    )
    hold_out_cases = gold_meta['hold_out_cases']

    version_label = "v1.5 (corroboration)" if args.require_corroboration else "v1.4 (baseline)"

    print("=" * 100)
    print(f"DISCUSSION UNITS EVALUATION: {version_label}")
    print("=" * 100)
    print()

    # Evaluate both sets
    verified_results = evaluate_set(
        verified_cases, "VERIFIED (22 cases, can tune)",
        gold_meta, verified_gold,
        require_corroboration=args.require_corroboration
    )
    holdout_results = evaluate_set(
        hold_out_cases, "HOLD-OUT (4 cases, locked)",
        gold_meta, verified_gold,
        require_corroboration=args.require_corroboration
    )

    # Print results table
    print(f"{'Set':<30} {'Cases':<8} {'Exact':<8} {'Within-1':<10} {'Missed':<10} {'Spurious':<10}")
    print("-" * 100)

    for results in [verified_results, holdout_results]:
        if results['cases_analyzed'] == 0:
            continue

        exact_pct = 100 * results['exact'] / results['cases_analyzed']
        within1_pct = 100 * results['within_1'] / results['cases_analyzed']

        print(
            f"{results['name']:<30} "
            f"{results['cases_analyzed']:<8} "
            f"{results['exact']}/{results['cases_analyzed']} ({exact_pct:5.1f}%)   "
            f"{results['within_1']}/{results['cases_analyzed']} ({within1_pct:5.1f}%)   "
            f"{results['missed_total']:<10} "
            f"{results['spurious_total']:<10}"
        )

    print()
    print("=" * 100)
    print("DETAILED RESULTS")
    print("=" * 100)

    for results in [verified_results, holdout_results]:
        if results['cases_analyzed'] == 0:
            continue

        print()
        print(f"{results['name']}")
        print("-" * 100)
        print(
            f"{'Case':<8} {'Status':<8} {'Gold':<6} {'Pred':<6} {'Missed':<8} {'Spurious':<10}"
        )
        print("-" * 100)

        for case in results['cases']:
            status = "✓" if case['exact'] else ("~" if case['within_1'] else "✗")
            print(
                f"{case['case_id']:<8} {status:<8} "
                f"{case['gold_count']:<6} {case['pred_count']:<6} "
                f"{case['missed']:<8} {case['spurious']:<10}"
            )

    # Save results to JSON
    output_file = Path(
        f'/mnt/project-files/discussion-units/evaluation_results_'
        f"{'v15_corroboration' if args.require_corroboration else 'v14_baseline'}.json"
    )
    with open(output_file, 'w') as f:
        json.dump({
            'version': version_label,
            'verified': verified_results,
            'holdout': holdout_results,
        }, f, indent=2)

    print()
    print(f"Results saved to {output_file}")


if __name__ == '__main__':
    main()
