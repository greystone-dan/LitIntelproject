# FC Citation Rebuild Implementation Notes

## Current scope

This track is limited to citation-system rebuild for Federal Court cases.

Included:
- seed intake normalization
- citation extraction and resolution quality
- deterministic evaluation harness and reports

Excluded:
- tagging
- embedding
- retrieval/ranking tuning
- broad UI redesign

## Implemented now

- Added `scripts/build_fc_citation_seed.py`.
- Purpose: normalize user-provided case links into canonical FC item URLs and produce deterministic artifacts.
- Added `scripts/build_fc_citation_gold_template.py`.
- Purpose: generate a gold-annotation template from normalized FC seeds.
- Added `scripts/extract_fc_citation_evidence.py`.
- Purpose: produce read-only extraction evidence rows and resolution outcomes for QA.

### Inputs

- `.docx`
- `.csv`
- `.txt`
- `.md`

### Outputs

- `data/eval/fc_priority_seed_links.csv`
- `data/eval/fc_priority_seed_rejects.csv`
- `data/eval/fc_priority_seed_summary.json`

### Reject reason codes

- `invalid_url`
- `not_fc_domain`
- `not_item_url`
- `missing_item_id`
- `duplicate_normalized_url`
- `duplicate_item_id`

## Run command

```powershell
& "./venv/Scripts/python.exe" scripts/build_fc_citation_seed.py --input "<path-to-user-case-list.docx>"
```

```powershell
& "./venv/Scripts/python.exe" scripts/build_fc_citation_gold_template.py --seed-csv data/eval/fc_priority_seed_links.csv
```

```powershell
& "./venv/Scripts/python.exe" scripts/extract_fc_citation_evidence.py --case-id 32335 --out-csv data/eval/reports/fc_citation_evidence_case_32335.csv
```

## Next implementation slice

1. FC citation eval script with precision/recall/span checks against gold fixtures.
2. Per-type regression gate runner and baseline-vs-rebuild delta report.
3. Resolver reason-code expansion for ambiguous party-style citations.
