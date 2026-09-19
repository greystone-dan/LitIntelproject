# Task: Add deterministic case summary projection

Status: complete
Created: 2026-09-19
Updated: 2026-09-19

Task: Add a researcher-friendly Case summary layer derived from the existing deterministic Discussion Unit and sub-theme evidence.
Why now: The current Case structure view exposes technical units and roles, but researchers need a concise case brief that remains source-verifiable and explicitly avoids unsupported conclusions.
Owner surface: `backend/reader_service.py`, `backend/models.py`, and the active `/data-explorer` reader UI.
Dependencies: Existing `evidence_summary` payload, Discussion Unit V1.2, sub-theme V1.4, current reader toggle, source-linked chunk evidence.
Risk boundary: No AI calls, embeddings, semantic legal conclusions, canonical writes, migrations, or browser-invented offsets. Missing roles must render as `Not detected in available evidence`.
Smallest falsifiable check: Case 1093 receives a deterministic summary payload with stable section order, explicit unavailable states, and every populated section linked to existing evidence or source paragraph metadata.
Acceptance criteria:
- Add an optional `case_summary` payload distinct from `evidence_summary`.
- Use controlled deterministic templates for issue, positions, facts/evidence, governing law, reasoning, limitations, and disposition.
- Preserve source evidence references and disclose that the output is coded research assistance, not a legal conclusion.
- Add a separate `Show case summary` reader toggle while preserving the existing structure toggle.
- Validate case 1093 and a case with missing evidence roles; run focused UI/API tests and the full suite.
- Update `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`, `CHANGELOG.md`, and generated API docs.
Docs/generated references: Canonical docs and Swimm walkthrough are required; regenerate API reference rather than editing it manually.
Rollback/recovery: Remove the optional payload, summary builder, UI toggle, tests, and documentation additions. Existing reader and structure layer remain intact.
Commit allowed: yes
Push allowed: yes
Evidence: Delegated read-only integration review completed and recommended a separate `case_summary` field, fixed seven-section role aggregation, explicit unavailable states, and an independent reader toggle. Implemented the response models and deterministic projection in `backend/models.py` and `backend/reader_service.py`, the `Show case summary` control in `backend/pages/data_explorer.py`, and focused tests in `tests/test_case_summary.py`. Pure projection validation passed; combined summary and reader tests passed (16 tests); the live `/cases/1093/reader-data` endpoint returned all seven sections with totals 7 available and 0 unavailable; the full suite passed (561 tests); the rendered `openDecision(1093)` browser smoke displayed all seven headings and reported no console or request errors; API reference regeneration completed; `git diff --check` passed.
Residual risk: Template quality depends on deterministic cue coverage; the summary must never imply that an undetected role was absent from the underlying decision. The generated-doc checker still has the pre-existing BOM issue in `scripts/run_treatment_teacher_batch.py`.
Next bounded task: Commit and push the completed Task 134 change set.
