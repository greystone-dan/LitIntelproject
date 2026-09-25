# Task: Link paragraph assessments to citation evidence

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

Task: Execute the deterministic evidence bridge for the 300 paragraph-assessed cases so each paragraph assessment instance links to zero or more citation occurrences through the authoritative paragraph chunk, preserving citation IDs and offsets.

Why now: The paragraph assessments identify research concepts such as RAD intervention criteria. Linking them to citation occurrences enables future search from an assessment concept back to the underlying authorities without yet making any claim about citation treatment.

Owner surface: `scripts/` read-only evidence bridge and focused tests/artifacts.

Dependencies: `scripts/dry_run_paragraph_evidence_bridge.py`, `backend/discussion_units_sandbox.py`, `backend/database.py`, paragraph assessment artifacts, citation/chunk provenance.

Risk boundary: Read-only bridge only. No production database writes, no citation-treatment labels, no target-resolution changes, no statute/citation merging, no paid operations, and no changes to the 300 assessment source artifacts.

Commit allowed: yes
Push allowed: yes

Smallest falsifiable check: For a bounded sample, every emitted assessment link resolves through `case_id + paragraph_index -> paragraph CaseChunk -> Citation.chunk_id`; citation offsets remain within the authoritative chunk text, and ambiguous/unmatched joins are explicit rather than guessed.

Acceptance criteria:
- Inspect the 300-case assessment cohort and produce a versioned bridge artifact.
- Preserve one record per assessment instance, including assessments with zero citations.
- Link citation occurrences by authoritative paragraph chunk, including `citation_id`, `chunk_id`, offsets, text, normalized form, unresolved state, and target ID when present.
- Record exact, zero-citation, ambiguous, unmatched, and missing-assessment statuses.
- Validate chunk text hashes and citation offset bounds where source text is available.
- Add focused tests for exact, zero-citation, ambiguous, unmatched, and offset-integrity cases.
- Update canonical documentation and relevant Swimm walkthrough with the bridge contract and limitations.
- Do not proceed into citation-treatment classification.

Hypothesis: A deterministic paragraph-index-to-paragraph-chunk-to-citation join can link the 300 assessments back to citation occurrences without inventing offsets or depending on target-case resolution.

Focused validation: `venv\\Scripts\\python.exe -m pytest tests/test_dry_run_paragraph_evidence_bridge.py -q` plus the bounded 300-case bridge run and `git diff --check`.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/system-map.ovnldklv.sw.md`.

Rollback/recovery: Delete the generated bridge artifact and revert only bridge code/tests/docs; no database rollback is required.

Evidence:
- Prior read-only inspection confirmed assessments are keyed by paragraph index and paragraph chunks expose `paragraph_start`, `id`, and `text_hash`.
- Prior inspection confirmed citations carry `id`, `chunk_id`, `offset_start`, `offset_end`, normalized text, unresolved state, and optional target IDs.
- Existing `scripts/dry_run_paragraph_evidence_bridge.py` provides the local join pattern.
- Delegated Explore inspection confirmed the existing bridge CLI and its exact/ambiguous/missing-assessment behavior; no files changed by delegation.
- `venv\\Scripts\\python.exe -m pytest tests/test_dry_run_paragraph_evidence_bridge.py -q` passed: 3 tests.
- `venv\\Scripts\\python.exe scripts/dry_run_paragraph_evidence_bridge.py --limit 300` completed read-only in 5.817 seconds and wrote valid `data/eval/llm_discussion_units_pilot/paragraph_level_300_run/citation_evidence_bridge.json`.
- Final artifact: 300 cases, 13,424 records, 11,657 exact paragraph matches, 798 ambiguous mappings, 969 missing-assessment records, 6,260 translated citation links across 3,241 paragraph records, and no invalid translated offsets.
- Canonical documentation updated: `SYSTEM_REFERENCE.md`.
- Swimm walkthrough updated: `.swm/8.upryk5h6.sw.md`.
- Citation treatment inference was intentionally not performed.

Residual risk: 1,985 citation rows have no source chunk and additional section citations cannot be translated when paragraph text reconstruction is unavailable. Ambiguous paragraph matches remain explicit. The artifact is report-only and not a persistent SQL relationship.

Next bounded task: Add a read-only search/report surface that filters the 300 assessment records by topic or role and returns their linked citation IDs; do not infer citation treatment without a separate approved task.
