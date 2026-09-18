# Task: External review of Discussion Unit V1.2 cohort

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Obtain bounded external feedback on the expanded 16-case Discussion Unit V1.2 and V1.3 sub-theme evaluation cohort.

Why now: Local validation established write-free, source-preserving behavior across 16 cases, but human/external review has covered only the original four fixtures.

Owner surface: `data/eval` review packet and response artifacts

Commit allowed: yes

Push allowed: yes

Dependencies: V1.2 cohort packets, existing review prompt, approved bounded OpenAI spend.

Risk boundary: Read-only packet inputs and response metadata only. Do not edit source code, canonical packets, database rows, or runtime activation. External output is non-authoritative review feedback.

Smallest falsifiable check: The external reviewer must identify whether the 50+ paragraph gate improves boundary quality without source/hash drift, and must name exact sampled case/unit evidence for any concrete finding.

Acceptance criteria:

- Review all 16 case IDs through a bounded digest, sampling evidence for larger packets.
- Preserve packet IDs, versions, hashes, offsets, and zero-write metadata in the digest.
- Keep the original V4 review artifacts unchanged and write separate V1.2 response artifacts.
- Record provider usage/cost and any rate-limit or truncation uncertainty.
- Update canonical/Swimm documentation only after the response is inspected.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/8.upryk5h6.sw.md`, `data/eval/discussion_units_external_review_prompt.txt`.

Rollback/recovery: Delete only new V1.2 review response artifacts and revert this task/documentation checkpoint; preserve all source packets and implementation.

Evidence: The first two bounded requests were blocked before output by provider/local limits, so the digest was reduced while retaining all 16 case IDs, 130 unit records, and 391 sub-theme records with one evidence anchor per sub-theme. The final external review completed with `gpt-4o-mini`, 35,482 prompt tokens, 1,363 completion tokens, total cost `$0.0061401`, `database_writes=false`, and `external_api_used=true`. It confirmed improved large-case boundaries, smaller-case preservation, and trustworthy provenance. It recommended a separate deterministic role-cue and governing-rule context refinement for exact sub-themes `677:3`, `1093:1`, `1171:2`, and `18674:72`. Outputs: `data/eval/discussion_units_external_review_v1_2_api_response.md` and `.json`. Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`.

## Hypothesis

If V1.2 improves reliability without introducing integrity regressions, external review will confirm that 53518 and 18674 have more usable boundaries while all sampled evidence remains source-reconstructable and smaller cases remain understandable.

## Completion

Completion recorded: yes

Summary: Completed bounded external review of the expanded V1.2 cohort.

Validation: Local V1.2 packet invariants and the focused 23-test suite passed; external review completed and produced separate response artifacts.

Residual risk: The external digest sampled one evidence record per sub-theme and truncated explanations/context; unsampled evidence remains unreviewed.

Next recommended task: Implement a bounded role-cue/context refinement for the exact sub-themes identified by the review.
