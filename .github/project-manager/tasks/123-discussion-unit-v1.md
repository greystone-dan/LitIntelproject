# Task: Discussion Unit Detection V1

Status: in-progress
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Build a deterministic, evidence-backed Discussion Unit layer over existing decision paragraphs, citations, legislation references, tags, headings, and source text, including text-aware section continuity.

Why now: Discussion boundaries are a safer foundation for later themes, argument mapping, issue extraction, and treatment analysis than attempting theme classification first.

Owner surface: `backend/contextual_authority/`, a bounded read-only inspection script, focused tests, and staged evaluation artifacts.

Dependencies: Existing canonical chunks, citation/statute/tag occurrence offsets, Phase 0 context-unit contracts, and one representative decision fixture.

Risk boundary: No changes to cases, chunks, citations, legislation references, tags, embeddings, or runtime treatment labels. No clustering, theme labels, external AI, or database publication in V1. Text features remain deterministic and explainable; they are not semantic model judgments.

Method hierarchy: Use descending certainty. Phase 1 uses structural boundaries
and deterministic signal continuity. Phase 2 may add statistical similarity
and text-segmentation experiments. Phase 3 may explore co-occurrence,
frequent-pattern mining, graph communities, and hierarchical clustering. Phase
4 may add AI-generated labels or summaries only as non-authoritative metadata.
No later phase is a V1 dependency.

Smallest falsifiable check: For one decision, deterministic paragraph features and adjacent-pair continuity scores can be reconstructed from source evidence and produce reviewer-inspectable boundaries without modifying canonical rows.

Acceptance criteria:

- Define stable paragraph identity and source-offset contracts before unit generation.
- Build paragraph features using canonical IDs and occurrence memberships, not copied labels alone.
- Compute adjacent continuity components separately: authority overlap, statute overlap, tag overlap, heading boundary penalty, and optional semantic signal.
- Include explainable signal-density measures such as authority density, statute density, tag density, authority diversity, and authority reuse where the source data supports them.
- Segment one decision with a documented boundary policy that does not split on a single noisy low score.
- Preserve generation method/version, configuration, source hashes, paragraph memberships, and reconstructable text evidence.
- Produce a read-only Markdown/JSON inspection artifact for reviewer boundary assessment.
- Add focused tests for offsets, empty-feature paragraphs, headings, boundaries, regeneration determinism, and canonical immutability.
- Update `SYSTEM_REFERENCE.md` and the relevant Swimm walkthrough before completion.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, and this task record.

Rollback/recovery: Delete only staged Discussion Unit artifacts and implementation files; canonical cases, chunks, citations, statutes, tags, and treatment artifacts remain unchanged.

Commit allowed: yes

Push allowed: yes

Evidence: The treatment distillation task was deferred with its contracts, reports, paid evidence, and review packet preserved. Discussion Unit V1 now includes deterministic content-word overlap and embedded section-cue detection; weak lexical overlap is neutral and does not by itself split ordinary legal paragraphs. Embedded headings are split into source-preserving local spans with the original chunk identity, canonical hash, and exact offsets. Focused validation passed with `PYTHONPATH=. .\\venv\\Scripts\\python.exe -m pytest tests/test_discussion_units_v1.py tests/test_discussion_unit_inspector.py -q` (`8 passed`). The first real invocation for case `53516` and `chunk_set=heading_chunks` was a safe empty result because that chunk set is absent. A bounded read-only ORM query found the populated sets `paragraph`, `section`, and `full_case`; case `1093` with `chunk_set=paragraph` produced `data/eval/discussion_units_case_1093.json` and `data/eval/discussion_units_case_1093.md` with 43 derived spans from 40 canonical paragraph chunks, 42 continuity pairs, 3 exact heading spans, 4 deterministic units (`0-3`, `4-12`, `13-40`, `41-42`), source hashes validated against canonical chunks, and `canonical_writes=0` plus `contextual_writes=0`. The report source label was corrected to reflect the selected chunk set and the artifact was regenerated after lexical calibration and offset alignment.

## Hypothesis

If paragraphs retain stable source identity and adjacent continuity components include content-word overlap plus section/discourse cues, then a reviewer can assess text-supported discussion boundaries without relying on citation/tag coverage or theme labels alone.

## Plan

1. Inspect the existing paragraph/chunk and Phase 0 context contracts.
2. Define pure paragraph-feature and adjacent-continuity models.
3. Build a bounded single-decision inspector with JSON and Markdown output.
4. Validate exact reconstruction, determinism, and no canonical writes.
5. Add deterministic text continuity and section-cue evidence, then update canonical and Swimm documentation with the accepted boundary and deferred work.

## Completion

Completion recorded: no

Residual risk: Existing paragraph chunks are a useful source-preserving proxy but do not provide populated `heading_chunks` in this database. Derived heading spans now align boundaries to embedded cues, but a human reviewer must assess whether the selected cue vocabulary captures all relevant legal sections without missing headings or splitting quoted/order text.

Next recommended task: Review the regenerated `data/eval/discussion_units_case_1093.md` and its continuity components against the source decision, then record whether the text-supported boundaries identify useful sections. Do not add embeddings, clustering, frequent-pattern mining, community detection, or AI labels before that review.