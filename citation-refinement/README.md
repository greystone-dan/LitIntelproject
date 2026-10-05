# Citation Refinement QA Sample

**Generated:** `qa-sample.json` using `scripts/evaluate_citation_refinement.py` with `--limit 500 --resolve`

**Random seed:** 42 (fixed for reproducibility)

## Contents

Stratified random sample of citation extraction differences between pass-one and the refinement layers (step 2):

- **case_citations_added** (~50 rows): New case citations found by refinement steps (C1–C5)
- **case_citations_dropped** (~30 rows): Case citations removed by refinement validation
- **statute_citations_added** (~20 rows): New statute/law citations found by refinement steps (L1–L5)

Each row includes:
- `case_id`: Source case ID
- `layer`: "cases" or "laws"
- `kind`: Citation type (e.g., "neutral", "reporter", "ibid", "statute")
- `step`: Refinement step that produced this row (e.g., "C1_gap_scan", "L3_expand")
- `action`: "added" or "dropped"
- `extracted_text`: Raw text extracted from the decision
- `normalized`: Normalized citation (e.g., "2008 SCC 9")
- `confidence`: Confidence score (0–1)
- `identifiers_or_instrument`: For cases: parallel identifiers. For laws: instrument name (e.g., "IRPA")
- `provision_or_pinpoints`: For cases: pinpoint structure. For laws: provision number or range
- `notes`: Refinement notes or validation issues

## How this was generated

```bash
./venv/Scripts/python.exe scripts/evaluate_citation_refinement.py --limit 500 --resolve --output-dir data/eval/qa_sample_raw
python generate_qa_sample.py  # Stratified sampling and formatting
```

The `rows.csv` output contains every added/dropped row from the 500-case run. This sample draws randomly from each category with fixed seed 42.

## Using this sample

- **For QA:** Review representative examples of each refinement type
- **For validation:** Cross-check against the gold sets in `scripts/evaluate_fc_citation_extraction.py`
- **For tuning:** If any step produces wrong rows, it can be disabled via `CASELIBRARY_CITATION_REFINE_STEPS`

See `docs/CITATION_REFINEMENT.md` for the full refinement pipeline documentation.
