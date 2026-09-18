# Task: Expand Discussion Unit reliability cohort

Status: complete
Created: 2026-09-18
Updated: 2026-09-18

## Task Record

Task: Expand the read-only Discussion Unit and sub-theme evaluation from four fixtures to a representative multi-case cohort.

Why now: The V1.4 rule improved the known large case, but reliability was not established from four cases alone. More cases were needed to test size, source structure, heading boundaries, signal density, and provenance preservation before another implementation iteration.

Owner surface: `scripts/inspect_discussion_units.py` and `data/eval` evaluation packets

Commit allowed: yes

Push allowed: yes

Dependencies: Existing paragraph chunk data, V1.2 Discussion Unit implementation, V1.3 sub-theme implementation, local virtual environment.

Risk boundary: Read-only inspection only. Do not write canonical/contextual database rows, alter source packets, run bulk writers, add embeddings, or activate the layer at runtime.

Smallest falsifiable check: Run the inspector on a bounded cohort spanning short, medium, and long paragraph counts; verify deterministic packet output, source hashes, sensible unit ranges, and zero writes.

Acceptance criteria:

- Select and inspect a representative cohort beyond cases 677, 1093, 1171, and 18674.
- Preserve source identity, paragraph membership, offsets, hashes, configuration/version fields, and zero-write invariants.
- Record fragmentation and preservation metrics sufficient to decide whether V1.4 needs another local rule.
- Update the canonical Discussion Unit documentation and the relevant Swimm walkthrough with observed results.
- Focused regression and packet validation pass, with residual risk recorded honestly.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, `.swm/8.upryk5h6.sw.md`, `data/eval/discussion_units_external_review_prompt.txt` if the review cohort changes.

Rollback/recovery: Delete only newly generated evaluation artifacts and revert task/documentation edits; preserve existing V4 packets and all source/database data.

Evidence: Explore selected 12 additional cases: `53515`, `53516`, `53517`, `53518`, `62`, `853`, `1046`, `3267`, `7341`, `10047`, `12718`, and `13610`, spanning 12-172 paragraph inputs. The read-only inspector generated V1.2 JSON/Markdown packets for those cases plus the original `677`, `1093`, `1171`, and `18674` fixtures. All 16 inspections completed with `status=dry_run`, `canonical_writes=0`, `contextual_writes=0`, valid source hashes, and stable generation/configuration metadata. Initial cohort evidence found a 56-paragraph one-unit collapse in `53518`; the local refinement changed the production defaults from ten vacuum pairs and 100 paragraphs to eight pairs and 50 paragraphs. Focused `tests/test_discussion_units_v1.py` passed 7 tests after the change, and the combined Discussion Unit/sub-theme/inspector suite passed 23 tests; `git diff --check` passed. Final counts in cohort order are 1, 2, 13, 3, 3, 2, 4, 4, 2, 3, 5, 3, 3, 4, 6, and 72 units. Case `53518` is no longer collapsed, case `53517` is segmented into 13 units, and case `18674` is bounded at 72 units. Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`. Evaluation packets are under `data/eval/discussion_units_case_*_cohort_v1.{json,md}`.

## Hypothesis

If V1.4 is reliable beyond the original fixtures, a size- and structure-diverse read-only cohort will produce deterministic, source-reconstructable units with no database writes and without widespread one- or two-paragraph fragmentation or giant collapsed units.

## Plan

1. Select a bounded, diverse case cohort using existing paragraph chunk metadata.
2. Generate read-only JSON and Markdown inspection packets and compute quality metrics.
3. Repair only a demonstrated local defect, then rerun the same cohort check.
4. Update canonical and Swimm documentation and record the next bounded recommendation.

## Execution Checkpoints

- Delegation: Explore selected the 12-case expansion and identified the packet metrics; no files changed.
- Implementation: Updated `backend/contextual_authority/discussion_units.py` to version 1.2 with the eight-pair/50-paragraph signal-vacuum gate after the cohort falsified the initial hypothesis on case 53518.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `.swm/8.upryk5h6.sw.md`.
- Recovery: Evaluation artifacts under `data/eval`; no database writer or long-running operation permitted.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-18 | Task created | User requested continued expansion until the feature is reliable. | V1.4 focused suite passed 23 tests; original real-case cohort remained only four cases. |

## Completion

Completion recorded: yes

Summary: Expanded the read-only evaluation to 16 cases and applied one evidence-backed local segmentation refinement.

Validation: `tests/test_discussion_units_v1.py tests/test_subthemes_v1.py tests/test_discussion_unit_inspector.py -q` passed with 23 tests; `git diff --check` passed; all 16 inspector runs completed as dry runs with zero writes.

Residual risk: Shorter cases still contain some one- or two-paragraph units at explicit heading/order transitions; sub-theme role-cue quality remains a separate low-trust review concern. No external review was run for the expanded cohort.

Next recommended task: Run a bounded human or external review of the 16-case V1.2 cohort, focusing on heading-sized units and the weakest role explanations before runtime activation.
