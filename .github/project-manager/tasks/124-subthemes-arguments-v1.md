# Task: Sub-themes and Argument Evidence V1

Status: in-progress
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Build an additive, deterministic sub-theme and argument-evidence layer inside reviewed Discussion Units.

Why now: Section boundaries alone are too coarse for legal research. Reviewers need to see the distinct issues, factual clusters, governing rules, party positions, reasoning moves, counterarguments, and disposition cues inside each section.

Owner surface: `backend/contextual_authority/`, the read-only Discussion Unit inspector, focused tests, and staged evaluation artifacts.

Dependencies: Discussion Unit V1 source spans and hashes, canonical paragraph text, citations/statute/tag memberships, existing deterministic metadata/outcome cues, and case `1093` as the bounded real fixture.

Risk boundary: No canonical database writes, migrations, UI activation, treatment inference, external AI, embeddings, or opaque semantic labels. Sub-theme names must remain inspectable term signatures or explicitly marked deterministic role labels. Every argument observation must retain source chunk identity, local offsets, source hash, cue text, rule/method version, and confidence rationale.

Approaches considered:

1. Deterministic lexical and cue evidence: argument-role regex cues plus contiguous term-signature grouping. Highest explainability and lowest operational cost; chosen for V1.
2. Local embedding similarity: likely better paraphrase grouping but adds model/version drift, runtime cost, and weaker legal auditability; deferred until V1 has reviewed boundaries.
3. External-AI theme/argument interpretation: strongest prose interpretation but violates offline runtime, introduces label instability, and is unsuitable before evidence review; deferred to non-authoritative teacher experiments only.

Smallest falsifiable check: For case `1093`, each Discussion Unit must produce one or more source-reconstructable argument observations and deterministic sub-theme records whose paragraph ranges remain within the parent unit; a reviewer can distinguish at least issue, party-position, rule, reasoning/application, and disposition cues where the source text contains them.

Acceptance criteria:

- Define immutable argument observation and sub-theme contracts.
- Detect argument roles from explicit text cues and preserve exact local evidence spans.
- Generate contiguous sub-themes from text term signatures and role continuity, without pretending a term cluster is a legal conclusion.
- Keep sub-theme ranges inside parent Discussion Unit ranges.
- Preserve source chunk IDs, local offsets, source hashes, method/version, configuration hash, evidence terms, and role rationale.
- Emit JSON and Markdown through the existing read-only inspector.
- Add focused synthetic tests for role cues, exact spans, range containment, deterministic regeneration, empty cues, and no writes.
- Validate one real decision artifact and inspect its section/sub-theme/argument alignment.
- Update `SYSTEM_REFERENCE.md`, the relevant Swimm walkthrough, and this task record.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, and this task record.

Rollback/recovery: Remove only staged code/tests/evaluation artifacts. Discussion Unit V1 and all canonical case/chunk/citation/statute/tag/treatment data remain unchanged.

Commit allowed: yes

Push allowed: yes

## Hypothesis

If each Discussion Unit is decomposed into source-backed argument-role observations and contiguous term-signature sub-themes, then a legal reviewer can inspect the internal issue/argument structure without relying on citation overlap, opaque embeddings, or generated legal conclusions.

## Plan

1. Define pure immutable argument and sub-theme contracts.
2. Implement deterministic cue extraction with exact local spans and rationale.
3. Implement contiguous term-signature sub-theme grouping within parent units.
4. Integrate JSON/Markdown inspection output without database writes.
5. Validate synthetic contracts and case `1093`, then update canonical and Swimm documentation.

## Evidence

Delegated read-only discovery identified existing document-structure, chunking, metadata/outcome, citation, statute, and tag utilities, but no existing sub-theme or argument contract suitable for direct reuse. The chosen V1 owner is the existing pure contextual-authority layer plus its inspector. Focused validation passed with `PYTHONPATH=. .\\venv\\Scripts\\python.exe -m pytest tests/test_subthemes_v1.py tests/test_discussion_units_v1.py tests/test_discussion_unit_inspector.py -q` (`14 passed` after renderer and explanation regressions). The bounded real-case packets are case `1093`: 4 units, 11 sub-themes, 62 observations; case `1171`: 6 units, 14 sub-themes, 86 observations; and case `677`: 3 units, 8 sub-themes, 91 observations. All three passed deterministic rerun, parent-range containment, source-hash linkage, cue/context offset, Markdown explanation, and zero-write assertions. Argument observations include exact cue offsets plus full sentence context and canonical source hashes. Large Markdown sections are bounded at 20,000 characters while JSON retains full evidence.

## Residual risk

Deterministic cue rules can miss implicit legal moves, broad role cues can still over-label sentences, and term signatures can over-split or merge paraphrased issues. Three cases are not corpus-level validation, and large-case Markdown is intentionally truncated while JSON remains complete. The artifact must present evidence and rationale rather than claim semantic truth. Human review remains required before embeddings, clustering, AI interpretation, or runtime activation.

## Next recommended task

Review the three generated packets for role precision, sub-theme coherence, and explanation usefulness. Record corrections before expanding to a larger bounded sample or considering statistical similarity.
