# Task: Audit Discussion Unit structural failures

Status: complete
Created: 2026-09-29
Updated: 2026-09-29

## Task Record

Task: Produce a reproducible, read-only Core-300 audit that measures collapsed and oversized deterministic Discussion Unit and sub-theme spans, without publishing or changing the experimental UI.

Why now: A ten-case human read found that coarse Discussion Unit boundaries often collapse substantive reasoning, while sub-themes remain promising. The project needs cohort-wide evidence before changing the algorithm or representing structural units as legal sections.

Owner surface: `scripts/audit_discussion_unit_structure.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: `data/eval/llm_discussion_units_pilot/core_300_run/reports/`, `backend/contextual_authority/discussion_units.py`, focused discussion-unit tests, `SYSTEM_REFERENCE.md`, and `.swm/8.upryk5h6.sw.md`.

Risk boundary: Read existing report artifacts only. Do not write canonical or contextual database rows, alter source text, change active UI behavior, launch external or paid model work, or publish treatment labels.

Smallest falsifiable check: Run the audit against the retained Core-300 deterministic artifacts and verify that it emits a machine-readable report containing per-case and cohort collapse/oversize counts.

Acceptance criteria:

- The audit reads the retained deterministic Core-300 artifacts without a database connection or network call.
- It reports per-case unit/sub-theme counts, maximum span size, and explicit flags for collapsed or oversized structures.
- The report supplies cohort-level counts for review, not a legal-quality claim or automatic segmentation change.
- A focused test covers a collapsed fixture and an ordinary multi-unit fixture.
- The canonical architecture reference and contextual-authority Swimm walkthrough document the audit and its review-only boundary.

Harness criteria:

- Audit test passes.
- Bounded Core-300 audit command produces the required JSON report.
- Documentation paths are recorded in the task evidence.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, and this task record. No generated reference requires manual editing.

Rollback/recovery: Delete the new read-only audit script, focused test, and generated audit artifact; no database, source, or runtime state changes are involved.

Evidence: `Explore` inspected the prior retained review cohort and report schema; the manager reconciled that result with the actual `core_300_run/reports` directory containing 300 deterministic reports. The new artifact audit completed without database, network, canonical, or contextual writes. It found 11 collapsed top-level cases, 1 collapsed-subtheme case, 231 cases with an oversized top-level unit, and 74 with an oversized sub-theme under the recorded thresholds.

Files changed: `scripts/audit_discussion_unit_structure.py`, `tests/test_audit_discussion_unit_structure.py`, `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, and this task record. Generated evidence: `data/eval/llm_discussion_units_pilot/core_300_run/discussion_unit_structural_audit.json`.
Delegated work: `Explore` performed a read-only artifact-schema and test-convention inventory; no files changed. Its initial 16-case path was corrected before implementation by inspecting the full `core_300_run/reports` artifact directory.
Focused validation: `./venv/Scripts/python.exe -m pytest tests/test_audit_discussion_unit_structure.py -q` passed through the task harness. The bounded audit command completed with 300 reports and wrote the JSON artifact.
Residual risk: Structural flags identify cases for review but cannot establish substantive legal correctness. The thresholds are review heuristics, and hybrid labeling remains approval-gated and unpublished.
Next bounded task: Select a stratified human-review cohort from the 231 oversized-unit and 11 collapsed-top-level cases, then decide whether to build a fine-subtheme-first segmentation prototype.

## Hypothesis

If the retained Core-300 deterministic reports are audited for one-unit, one-sub-theme, and oversized-span structures, then the project can quantify the observed collapse failure without introducing model inference or changing canonical evidence.

## Plan

1. Delegate a read-only inventory of artifact schema, existing report scripts, and focused test conventions.
2. Add a pure artifact audit and fixtures for collapsed and non-collapsed structures.
3. Run the bounded cohort audit, update the current architecture/Swimm documentation, and record evidence.

## Execution Checkpoints

- Delegation: `Explore` completed a read-only artifact inventory. Its initial review-cohort path was reconciled against the actual 300-report pilot directory before implementation.
- Implementation: Pending validation of the read-only audit script and focused test.
- Documentation: `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` updated with the baseline, thresholds, and review-only boundary.
- Recovery: Generated report is disposable and reproducible from retained artifacts.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-29 | Measure the structural failure before changing segmentation or UI | The ten-case read identifies collapse but is not cohort-wide evidence | User evaluation and `docs/DISCUSSION_UNITS_WEEKLY_REVIEW.md` |

## Completion

Completion recorded: yes. The managed harness recorded all three criteria as passed, and `scripts/evidence_gate.py` passed against the completed run state and this task record.

Summary: Added a pure report-artifact audit for the Core-300 deterministic Discussion Unit run. It quantifies structural collapse and oversized spans without changing source, database, runtime, or model state.

Validation: Focused audit test passed; bounded 300-report audit command completed and wrote its JSON report.

Residual risk: The audit cannot validate legal-quality boundaries; human review remains required before an algorithm or UI change.

Next recommended task: Review a stratified flagged cohort and decide whether to prototype fine-subtheme-first segmentation.