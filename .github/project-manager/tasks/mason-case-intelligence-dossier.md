# Task: Mason case-level intelligence dossier request

Status: complete
Created: 2026-09-23
Updated: 2026-09-23

## Task Record

Task: Build a report-only, one-call Mason dossier that gives a stronger external model the deterministic case record, identified citations, tags, statute references, outcomes, discussion units, and source text, then requests argument-level and advanced citation-treatment intelligence rather than a whole-case summary.

Why now: The per-citation contract produced 65 rejected labels because it required fragile exact spans for many model outputs. A case-level evidence packet may let a stronger model reason over the complete deterministic record and return richer treatment analysis with fewer artificial rejection points.

Owner surface: New `scripts/build_mason_case_intelligence_request.py` request builder and `data/eval/llm_discussion_units_pilot/` report-only artifacts.

Commit allowed: yes

Push allowed: yes

Dependencies: Mason case 53164, existing deterministic database records, Mason discussion-unit artifacts, and existing external-AI configuration.

Risk boundary: No canonical database writes, runtime publication, source replacement, or unbounded paid calls. Deterministic IDs, offsets, hashes, and provenance remain authoritative. The model must distinguish evidence from inference and must not summarize the whole case as its primary output.

Smallest falsifiable check: Build the request without network access and assert it contains the case metadata, all identified citation records, all statute references, tags, outcomes, discussion units, source text, provenance fields, and explicit output tasks.

Acceptance criteria:

- A deterministic, no-network builder creates one complete Mason case dossier request.
- The request includes already identified citations and enough surrounding source text for the model to verify treatment.
- The prompt requests argument/discussion-unit intelligence and advanced citation treatment, not a generic case summary.
- The payload has bounded size and passes structural completeness checks.
- Focused tests or assertions and `git diff --check` pass.

Docs/generated references: `SYSTEM_REFERENCE.md`; `.swm/8.upryk5h6.sw.md`; generated references are not hand-edited.

Rollback/recovery: Delete or ignore the new request builder and report-only request artifact; no database rollback is applicable. Any paid run must use a distinct result path and an explicit budget cap.

Evidence: Explore inspected the existing Mason fixture, runner, contract, and deterministic artifacts. The no-network builder produced a report-only dossier with 97 identified citations, 254 citation records, 336 statute references, 386 tags, and source paragraphs. The initial `gpt-4.1` call cost `$0.413526` but selected three representative treatments. The corrected compact contract completed at 187,066 prompt tokens and 7,262 completion tokens for `$0.432228`; JSON parsing succeeded and all 97/97 identified citation IDs were covered, with 85 supportive and 12 neutral treatments. Post-run cross-reference review found a strong supportive-label skew, repetitive rationales, and one missing authority mapping: argument `A2` names citation ID `7658423`, absent from `citation_treatment`. No canonical or runtime writes occurred.

## Hypothesis

If the model receives a complete, source-preserving Mason dossier and a narrowly specified intelligence contract, it will produce more useful argument-level and citation-treatment analysis than isolated span-label calls, while deterministic provenance remains auditable.

## Plan

1. Inventory the existing deterministic Mason artifacts and local ORM fields.
2. Implement a no-network dossier request builder with explicit output tasks and provenance.
3. Validate completeness, size, and JSON structure before any paid call.
4. Run a separately approved bounded strong-model call and review the returned intelligence.
5. Update canonical and Swimm documentation with observed quality and limits.

## Execution Checkpoints

- Delegation: Explore inspected the existing fixture, runner, contract, and Mason artifacts; report stored in the session tool result.
- Implementation: Added `scripts/build_mason_case_intelligence_request.py` and `scripts/run_case_intelligence_request.py`; preflight and `git diff --check` passed.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md` with the case-level report-only boundary and result artifact.
- Recovery: Paid request/result artifacts must use distinct Mason dossier names under `data/eval/llm_discussion_units_pilot/`.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-23 | Use one case-level dossier call as a separate experiment | User wants the model to see Mason as a database printout and perform advanced treatment analysis | Existing 65 rejected per-event labels and complete deterministic artifacts |

## Completion

Completion recorded: yes

Summary: Built and exercised a report-only Mason case dossier path for stronger-model argument and citation-treatment intelligence.

Validation: No-network build, structural counts, Python compilation, `git diff --check`, and one successful bounded `gpt-4.1` call.

Residual risk: A larger context may improve semantic reasoning but can still produce unsupported conclusions. The 85/97 supportive distribution, repetitive rationales, and missing `7658423` authority mapping require human review and prevent canonical publication.

Next recommended task: Repair the case-level output contract or add a report-only adjudication layer that separates citation relevance from support for the final holding, validates authority cross-references, and reviews the 85 supportive classifications before any derived treatment rows.
