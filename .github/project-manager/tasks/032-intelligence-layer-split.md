# 032 — Intelligence layer split from metadata facade

Task: Split derived outcome/subject derivation out of `backend/metadata.py` into a new `backend/intelligence.py` module, keeping `extract_case_metadata` output byte-identical and all stored JSON paths unchanged.
Why now: User-requested code-level separation of the deterministic source-metadata layer from the derived intelligence layer; concept clarity without behavior or storage change.
Owner surface: `backend/metadata.py` (+ new `backend/intelligence.py`).
Dependencies: `backend/metadata_outcomes.py` and `backend/metadata_subjects.py` unchanged (no renames); downstream consumers (`analytics_service.py`, `citation_map.py`, `contextual_intelligence.py`) keep reading `metadata_json->'reader_extracted'`.
Risk boundary: Only the two files above. No extraction rule, regex, confidence score, storage path, UI, or consumer changes. No commit.
Smallest falsifiable check: `tests/test_metadata.py` passes and a fixed-sample `extract_case_metadata` output hash is identical before/after the edit.
Acceptance criteria:
- `pytest tests/test_metadata.py tests/test_fc_document_scraper.py tests/test_case_processing.py tests/test_contextual_intelligence.py -q` all pass.
- Import check prints `metadata_fields 12` and `intelligence_fields 7`.
- Full suite reports 341 passed.
- Sample payload hash identical before/after.
Docs/generated references: none (no generated docs touched; docstrings updated in the two modules).
Rollback/recovery: revert `backend/metadata.py`; delete `backend/intelligence.py` and this task file.
Evidence:
- Byte-identity: fixed-sample `extract_case_metadata` SHA256 before = `840a5ccf0fc44fd7d2ee9b02d014dfe0d4907e032f60e1a853d7664e222337f5`, after = same; `byte_identical True`.
- Focused: `pytest tests/test_metadata.py tests/test_fc_document_scraper.py tests/test_case_processing.py tests/test_contextual_intelligence.py -q` -> 30 passed.
- Import check -> `metadata_fields 12`, `intelligence_fields 7`.
- Full suite: `pytest -q` -> 341 passed, 1 warning (pre-existing pypdf ARC4 deprecation).
- No editor diagnostics in `backend/metadata.py` or `backend/intelligence.py`.
Status: complete.
