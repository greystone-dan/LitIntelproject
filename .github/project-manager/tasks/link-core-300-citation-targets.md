# Task: Link Core 300 citations to target evidence

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

Task: Enrich Core 300 assessment and comparison citation hits with canonical target-case metadata and paragraph-local evidence where the stored citation row supports it.

Why now: The comparison workflow preserves source paragraph identity, but citation chips currently open only the originating case. Researchers need a direct, traceable path from assessment key term to the cited authority and stored evidence offsets.

Owner surface: Core 300 report-only assessment search and existing canonical citation/reader contracts.

Dependencies: `Citation` rows, target `Case` relationships, canonical reader data, paragraph evidence bridge, existing Core 300 comparison endpoint.

Risk boundary: Read-only enrichment only. Preserve citation IDs, source/target chunk IDs, backend-owned offsets, cohort scoping, and separate statute/citation layers. Do not infer treatment or create new citation rows.

Commit allowed: yes
Push allowed: yes

Smallest falsifiable check: A mocked Core 300 assessment citation with a canonical target case returns target case metadata and preserved source/target offsets without changing its case/paragraph identity.

Acceptance criteria:
- Core 300 assessment and comparison citations include canonical target-case metadata when resolved.
- Stored source chunk offsets and target paragraph/chunk identifiers remain visible.
- UI can open the cited target authority separately from the originating case.
- Unresolved citations remain explicitly unresolved and do not receive guessed targets.
- Focused API/helper/UI tests pass.
- Canonical documentation and Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/8.upryk5h6.sw.md`.

Rollback/recovery: Remove citation enrichment and target-authority controls; preserve the existing paragraph-anchored comparison behavior.

Evidence:
- Existing `Citation` rows contain `target_case_id`, `target_paragraph`, `target_chunk_id`, `chunk_id`, and source offsets.
- Current bridge response intentionally exposes only citation ID, source chunk ID, and normalized citation.
- Regenerated the bounded 300-case bridge into `paragraph_level_300_run/citation_evidence_bridge.json`: 13,424 records, 3,241 with citation links.
- Exposed stored source and paragraph offsets, target case IDs, link method/status, and assessment key terms in Core 300 citation objects.
- Citation chips now open the cited target case when resolved, with source-case fallback when unresolved.
- Topic/role comparison now scans the full loaded Core 300 assessment cohort when filters are supplied, rather than being limited to the first 100 search hits.
- Live smoke check: `search_cohort_assessments('mootness', limit=25)` returned 25 results, 33 citations, 21 resolved target links, and 33 paragraph-offset links.
- Focused comparison validation: `venv\Scripts\python.exe -m pytest tests/test_discussion_units_sandbox.py -k 'comparison' -q` passed with 2 tests.
- Browser validation: Core 300 search returned 25 hits and 33 citation buttons; a resolved citation opened the reader for target case `35881` with no page errors or failed responses. The selected first topic/role comparison returned one eligible case and zero citations because that assessment key is unique in the eligible bridge records; the comparison API returned one group successfully.
- Final focused validation: 75 tests passed; `get_errors` found no errors; `git diff --check` passed.
- Documentation checkpoint updated in `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/8.upryk5h6.sw.md`.
