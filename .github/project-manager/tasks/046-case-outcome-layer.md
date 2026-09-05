# Task: Case outcome layer

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

Task: Create a deterministic, evidence-backed case outcome layer that consistently identifies who won, what disposition occurred, and what decision or issue was challenged.
Why now: Existing outcome derivation recognizes several operative-tail verbs and government win/loss, but stores coarse derived fields without a structured outcome record or exact disposition/challenge evidence.
Owner surface: `backend/metadata_outcomes.py`, `backend/intelligence.py`, metadata payload integration, focused outcome tests, and the outcome Swimm walkthrough.
Dependencies: Canonical case text, caption/party metadata, existing `reader_extracted` payload contract, V3 tag evidence, citation/statute layers.
Risk boundary: Preserve existing field names and values for compatibility. Do not infer a winner when the operative disposition is ambiguous; emit explicit `unknown`/`undetermined` states with confidence and evidence status. Keep outcomes separate from tags, citations, statutes, and metadata source observations.
Smallest falsifiable check: Curated positive, negative, mixed-disposition, quoted-history, and no-disposition fixtures show final operative outcome selection, winner mapping, and challenged-issue extraction without false certainty.
Acceptance criteria: Every supported case receives an explicit outcome status; supported cases expose winner/loser side, disposition action, decision-maker/process, challenged issue, confidence, and exact evidence where available; ambiguous cases remain reviewable rather than guessed; existing tests remain green.
Docs/generated references: `SYSTEM_REFERENCE.md`, `LEGAL_TAGGING.md` only for layer boundaries, relevant `.swm/` outcome walkthrough, `docs/METRICS_DICTIONARY.md` if metric semantics change.
Rollback/recovery: Preserve old payload fields and add new fields; revert the outcome module and focused tests without touching canonical case/source/citation/tag rows.
Evidence:
- Preserved the existing operative-tail extraction and government-role inversion
	as the compatibility baseline.
- Added mixed/partial disposition handling, explicit case winner/loser and
	outcome status fields, structured outcome detail with exact evidence offsets,
	and additive challenged-issue fields.
- Focused metadata suite passed: `21 passed`.
- Updated `SYSTEM_REFERENCE.md`, `docs/METRICS_DICTIONARY.md`, and
	`.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md` in the same
	documentation checkpoint.
Status: complete
Commit allowed: yes
Push allowed: yes
