# Task: Add an evidence-based case summary layer

Status: complete
Created: 2026-09-19
Updated: 2026-09-19

## Task Record

Task: Add an optional, evidence-based case summary layer on top of Discussion Units and sub-themes so researchers can toggle a compact case structure view without changing canonical data or presenting unsupported legal conclusions.

Why now: The deterministic Discussion Unit and sub-theme artifacts are useful but currently require researchers to inspect JSON/Markdown packets. A toggleable reader layer can expose the existing evidence as a navigational summary.

Owner surface: `backend/routes.py`, the active `/data-explorer` reader page, and the existing contextual-authority projection; no new persistence in the first slice.

Commit allowed: yes

Push allowed: yes

Dependencies: Discussion Unit V1.2, sub-theme V1.4, existing reader data contracts, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and the relevant Swimm walkthrough.

Risk boundary: Read-only and additive. Do not invent legal conclusions, semantic theme labels, embeddings, external AI calls, browser-owned offsets, or canonical/contextual database writes. Every displayed summary item must retain source paragraph/chunk identity and evidence context. The layer must be user-toggleable and default-safe.

Smallest falsifiable check: For case `1093`, a toggleable summary projection exposes the existing four Discussion Units and eleven sub-themes, and every displayed role/evidence item maps back to its source paragraph and canonical hash without changing reader data or database rows.

Acceptance criteria:

- Define a deterministic summary projection over existing Discussion Units and sub-themes.
- Expose it through the active case-reader workflow without changing canonical records.
- Add an explicit toggle so the current reader remains available unchanged.
- Show source-linked unit/sub-theme boundaries, roles, explanations, and evidence contexts.
- Add focused contract tests for case `1093` and a large-case bounded response.
- Update `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and the relevant Swimm walkthrough.

Docs or generated references to refresh: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`, `CHANGELOG.md`, and generated API references if an endpoint is added.

Rollback/recovery: Remove the projection route/UI toggle and its tests; preserve the existing reader, contextual-authority artifacts, source hashes, and canonical rows. No migration is expected for the first slice.

Evidence: Authority docs confirm Discussion Units and sub-themes are immutable staged outputs with source hashes, offsets, method/version, and zero-write behavior. Delegated integration review recommended extending `CaseReaderDataResponse`, projecting in the reader service, and rendering a separate lazy toggle; that recommendation was followed. The reader payload now exposes optional `evidence_summary`, generated on demand from paragraph CaseChunk rows and existing memberships. The live module inspector for case `1093` passed with 4 Discussion Units, 11 sub-themes, and zero canonical/contextual writes. Focused validation passed: `tests/test_feature_tabs.py` (14 passed) and Python compilation for the touched modules. API reference generation passed. Generated-doc checking remains blocked by the pre-existing BOM syntax error in `scripts/run_treatment_teacher_batch.py` and reports generated-doc drift. The 1093 report currently contains no argument-evidence items, so the UI preserves that absence rather than inventing spans.

## Hypothesis

If the existing deterministic evidence can be projected into a compact reader view, researchers will be able to locate argument positions, governing rules, reasoning, and outcomes faster while retaining direct source verification and the ability to return to the unchanged reader.

## Delegation

Delegated slice: inspect the active reader/API owner surfaces and recommend the smallest integration point, response contract, and focused test seam. Worker must not edit files or task records.

## Completion

Completion recorded: yes

Validation: Focused UI tests passed (14); touched Python modules compiled; live 1093 inspector passed with 4 units, 11 sub-themes, and zero writes; API reference regenerated; full suite passed (558 tests); `git diff --check` passed. Browser automation was not available in this environment. Generated-doc checking remains blocked by the pre-existing BOM syntax error in `scripts/run_treatment_teacher_batch.py`.

Residual risk: Deterministic role cues can be incomplete or mechanically broad; the feature must label itself as evidence-based review assistance and preserve raw source access.

Next bounded task: Run the full suite and browser smoke, then assess whether cue-free 1093 sub-themes need a separate extraction-quality task before broader reader rollout.
