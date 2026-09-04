# System Focus Mode (Master 300)

This project is currently in stabilization mode.

Current execution priority is extractor reliability for case-to-case citations.
Do not run broad 300-case rebuild/re-ingest loops until citation-pass QA gates are green.

## Active Scope

- Active case scope is the master-300 review cohort from `data/eval/fc_priority_seed_case_map.csv` (`status=matched`).
- Scope is enabled by default with:
  - `CASELIBRARY_FOCUS_MASTER_300=true`

## Five-Stage Processing Contract

Every ingested case is processed in this ordered pipeline:

1. `full_case`
2. `heading_chunks`
3. `metadata`
4. `case_citations`
5. `statutes`

Implementation: `backend/case_processing.py`

## Citation Separation

- Case-to-case references are stored in `citations`.
- Statute/instrument references are stored in `statute_references`.

## Legacy Isolation

- Legacy UI/workbench code is moved to `backend/legacy/`.
- Keep legacy modules out of active imports while stabilization is underway.

## Expanding Later

To expand beyond the master-300 cohort:

1. Set `CASELIBRARY_FOCUS_MASTER_300=false`
2. Run validation suites on full-corpus paths.
3. Re-enable broader routes only after reliability gates pass.
