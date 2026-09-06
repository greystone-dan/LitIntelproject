# V2 run review and release

Status: complete
Created: 2026-09-06
Updated: 2026-09-06

Task: Review the completed optimized V2 text-only enrichment run, document results and residual risk, regenerate references, and save the reviewed repository state to Git.
Why now: The run completed and needs evidence-backed acceptance before the separate citation resolution pass.
Owner surface: V2 enrichment operations, citation extraction contract, and canonical/Swimm documentation.
Dependencies: `data/overnight_runs/v2-text-only-full-20260905/state.json`, compact baseline, PostgreSQL read-only audit, focused tests, generated documentation.
Risk boundary: Review and documentation only after run completion; no rerun, no concurrent writer, no source acquisition, no data deletion, and no target-resolution write pass in this task.
Smallest falsifiable check: Focused V2/citation tests pass, generated references are current, and read-only offset audit reports no malformed evidence spans.
Acceptance criteria: Report completion/exclusion/error rates, before/after cohort deltas, stage coverage, HTML/provenance and resolution limitations; update canonical docs and relevant Swimm walkthroughs; commit and push the reviewed worktree.
Docs/generated references: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `.swm/system-map.ovnldklv.sw.md`, generated schema/script references.
Rollback/recovery: Revert only the review/documentation commit if needed; preserve completed run state and database rows.
Evidence: Run completed with 50,327 processed, 43,598 completed, 6,729 excluded, 0 quarantined. Completed cohort deltas versus baseline: chunks +188,272 (1.12x), citations +360,105 (1.30x), statutes +180,443 (1.65x), V3 tags +842,658 (23.10x). All completed rows had valid citation/statute offsets and tag offsets in the read-only audit. Focused suite passed 116 tests; generated documentation check passed. Canonical docs updated: `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`. Swimm walkthroughs updated: `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`, `.swm/system-map.ovnldklv.sw.md`.
Commit allowed: yes
Push allowed: yes
