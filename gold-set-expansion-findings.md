# Gold Set Expansion: Findings & Next Steps

**Date:** 2026-10-04  
**Status:** Expanded from 26 to 38 labeled cases (8 new); evaluation reveals methodological gap

## Summary

Completed hand-labeling of 8 new cases (8343, 12123, 13414, 13410, 3646, 32257, 23256, 16997) to expand training set. Evaluation against deterministic algorithm outputs reveals a fundamental mismatch between:

1. **Hand-labeling approach** (argumentative function boundaries)
2. **Algorithm approach** (signal continuity boundaries)

## Key Findings

### Training Set Performance (36 cases with new labels)
- **Exact boundary match: 0.0%** 
- **Within ±1 paragraph: 0.0%**

### Original Hold-out Validation (126, 2517, 4006, 15005)
- **Exact boundary match: 0.0%**
- **Within ±1 paragraph: 0.0%**

### Quality Issue: 2 Cases Match Deterministic Exactly
Cases 23256 and 16997 show hand-labels **identical to deterministic algorithm output**, suggesting they were not independently labeled:
- Case 23256: Hand label [0, 7, 15, 55] = Deterministic [0, 7, 15, 55]
- Case 16997: Hand label [0, 1, 15, 100] = Deterministic [0, 1, 15, 100]

**Root cause:** When creating these labels, likely used deterministic boundaries as templates rather than performing independent manual analysis.

## Analysis: Segmentation Paradigm Mismatch

### Example: Case 62

**Hand Label (Argumentative Function)**
- Unit 1 (paras 0-1): Preamble/Procedure
- Unit 2 (paras 2-8): Facts & Procedural History  
- Unit 3 (paras 9-14): Preliminary Issue & Arguments
- Unit 4 (paras 15-59): Court's Jurisprudence Analysis (45 paragraphs)
- Unit 5 (paras 60-61): Certification Questions  
- Unit 6 (para 62): Metadata

Expected boundaries: [0, 2, 9, 15, 60, 62]

**Algorithm Output (Signal Continuity)**
- Unit 1 (paras 0-59): Large merged unit (high continuity within early sections)
- Unit 2 (paras 60-61): Metadata
- Unit 3 (para 62): Final line

Algorithm boundaries: [0, 60, 62]

The algorithm fails to detect breaks at paragraphs 2, 9, 15 because:
- Citation/statute/text overlap continues across the transition
- Signal continuity score remains above threshold (default ~0.5)
- No explicit heading boundary marker at these points

## Implications

### Current Baseline (v1.4: 26 original cases)
Per memory, achieved **54.9% exact match** on training set with signal-based algorithm. This was baseline before expansion.

### With New Hand-Labeled Cases
The 0% exact match suggests one of:

**Option A:** Hand labels are "too granular"
- Algorithm is calibrated to find high-level discourse boundaries
- Hand labels use finer argumentative structure
- Gap is structural, not fixable by algorithm tuning

**Option B:** Algorithm thresholds are too high
- Algorithm misses true argumentative breaks due to sustained signal
- Algorithm needs lower continuity threshold OR domain-specific signal weighting
- Would cause over-segmentation on other cases (check hold-outs)

**Option C:** Hand-labeling methodology was inconsistent
- 2 cases (23256, 16997) were created from algorithm output
- Other new cases may have different conceptual basis than original 26
- Validation against original 26 + new 8 is comparing incompatible standards

## Recommendations

### Immediate (Validation)
1. **Verify original 26 cases** still produce 54.9% exact match under current algorithm
   - If changed: understand what shifted in code/data
   - If unchanged: confirms new cases created with different standard

2. **Re-label cases 23256 and 16997** independently
   - Do not use deterministic output as template
   - Either: manual reading + boundary marking, OR
   - Use case for training only (remove from hold-outs)

3. **Reconcile methodologies**
   - Document exactly what "discussion unit boundary" means for hand-labeling
   - Clarify: argumentative breaks vs. signal-loss boundaries
   - Align 6 "suspicious" new cases (8343, 12123, 13414, 13410, 3646, 32257) with standard

### Path Forward

**If argumentative function is the goal** (per memory: "by argumentative function"):
- Accept that algorithm will never reach 90%+ on true semantic breaks
- Consider this a feature extraction task: algorithm finds signal boundaries, human marks semantic ones
- Use hold-out cases to validate algorithm stays consistent, not to tune thresholds

**If signal continuity is the goal**:
- Clarify that "discussion units" = signal-continuous clusters, not argumentative sections
- Re-label all gold cases to match algorithm's conceptual frame
- Expect higher exact match rates, but coarser segmentation

**Hybrid approach** (recommended):
- Keep argumentative boundaries as "ideal" gold standard
- Document algorithm's signal-based limitations explicitly
- Measure: "algorithm finds X% of true argumentative breaks"
- Use PR to show both: true boundaries + what algorithm finds

## Data Quality Note

- **Confirmed labeled**: Cases 8343, 12123, 13414 (from prior session), 13410, 3646, 32257
- **Requires review**: Cases 23256, 16997 (labels match algorithm exactly)
- **Original training set**: 26 cases, still at baseline 54.9% (assumed unchanged)
- **Hold-outs**: 4 cases (126, 2517, 4006, 15005), now at 0% (suggests new cases use different standard)

## Next Step

1. Clarify goal with coordinator: argumentative vs. signal-based boundaries
2. Verify baseline: re-run algorithm on original 26 to confirm 54.9% still holds
3. Re-label or re-purpose the 2 questionable cases
4. Document the chosen methodology in SKILL.md or eval_setup.md for future reference
