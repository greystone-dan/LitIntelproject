# Task: V2 Pipeline quality gates

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

Task: Automate before/after evidence comparison and protect HTML-aware alignment before the V2 Pipeline cohort rollout.
Why now: Case 9237 completed the redesigned stages but citation/statute counts changed materially; a 731K-character case made monolithic SequenceMatcher alignment computationally prohibitive.
Owner surface: `backend/document_structure.py`, V2 Pipeline comparison tooling, focused tests, and rollout documentation.
Dependencies: Existing canonical case/chunk/citation/statute/tag/outcome tables and source HTML.
Risk boundary: Do not run a cohort rebuild until large deltas and alignment failures are visible and reviewable. No silent fallback may invent offsets. Preserve existing rows unless a bounded case test explicitly replaces them.
Smallest falsifiable check: Long alignment either completes within a bounded path or returns an explicit fallback/skip state; before/after snapshots produce deterministic count and item deltas.
Acceptance criteria: Snapshot/comparison tooling exists; alignment has a bounded large-document guard/fallback; seed and stratified tests cover chunk/citation/statute/tag/outcome deltas; docs and Swimm record rollout gates.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `docs/METRICS_DICTIONARY.md`, `.swm/system-map.ovnldklv.sw.md`, this task record.
Rollback/recovery: Disable the cohort runner; retain snapshots and existing rows; revert only the comparator/fallback changes if focused tests fail.
Evidence:
- Delegated audit confirmed global `SequenceMatcher` was the large-document
	bottleneck and that citation/statute count deltas require item-level review.
- Added bounded large-document block lookup in `backend/document_structure.py`;
	very large inputs bypass global diffing and leave unmatched blocks explicit.
- Added `scripts/compare_pipeline_case.py` for per-case before/after snapshots
	and deltas across chunks, citations, statutes, V3 tags, outcomes, and source
	HTML state.
- Added focused alignment/comparison tests; quality-gate suite passes: `32
	passed`.
- Generated current snapshots for cases 22, 9237, and 13681 under
	`data/eval/reports/`. Historical before snapshots were not captured before
	the earlier manual tests, so those reports are current-state snapshots only.
- Focused citation/statute regression subset passed: `107 passed`.
- Generated references are current and `git diff --check` passed.
- Automated one-case harness `scripts/run_v2_pipeline_case.py` completed for
	case `20217` (178,660 characters), producing before/after snapshots and a
	comparator report: chunks `237->247`, citations `36->40`, statutes
	`115->114`, V3 tags `0->10`, and a new explicit undetermined outcome.
- The bounded large-document path was exercised successfully on case `13681`
	(731,236 characters): HTML-aware replacement produced 709 chunks, followed
	by 133 citations, 93 statutes, and 483 V3 tags. The prior alignment failure
	no longer reproduces.
- Comparator deltas now include configurable `relative_delta` and
	`major_delta` flags, with regression coverage for the rollout threshold.
- Final quality-gate suite passes: `32 passed`; generated documentation is
	current and `git diff --check` passes.
Status: complete
Commit allowed: yes
Push allowed: yes
