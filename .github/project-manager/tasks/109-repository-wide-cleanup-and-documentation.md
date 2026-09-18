# Task: Repository-wide cleanup and documentation alignment

Status: complete
Created: 2026-09-17
Updated: 2026-09-17

## Task Record

Task: Review the repository end to end, separate active and legacy code clearly, improve and simplify evidenced defects, align documentation with current behavior, and finish with verified green checks plus an explicit commit/push checkpoint.

Why now: The system has accumulated multiple active, comparison, generated, side-project, and historical surfaces. The user wants the repository organized around the current system rather than silently carrying stale paths.

Owner surface: repository architecture and documentation governance, coordinated through bounded owner slices

Commit allowed: yes

Push allowed: yes

Dependencies: SYSTEM_REFERENCE.md; DOCS_INDEX.md; OVERNIGHT.md; generated documentation workflow; active test suite; existing project-manager tasks and Swimm walkthroughs

Risk boundary: Do not delete or rewrite history, remove potentially active code without evidence, alter production/security/source-access posture without explicit approval, run unbounded writers, or overwrite unrelated user changes. Generated docs must be regenerated, not hand-edited. Side projects and historical artifacts remain isolated.

Smallest falsifiable check: bounded repository inventory plus the narrowest failing test for the first confirmed issue; final validation must include the relevant focused tests, documentation checks, and the broadest feasible suite.

Acceptance criteria:

- Active, legacy/comparison, generated, historical, and side-project surfaces are inventoried and clearly documented.
- High-value confirmed defects and simplifications are fixed in bounded owner slices with tests.
- Current canonical documentation, Swimm walkthroughs, and generated references agree with active behavior.
- Focused checks pass after each slice; the broadest feasible test suite is run and failures are resolved or honestly recorded.
- Worktree changes are reviewed, committed, and pushed only after fresh final validation and explicit evidence.

Docs/generated references: SYSTEM_REFERENCE.md; DOCS_INDEX.md; OVERNIGHT.md; docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md; relevant .swm/ walkthroughs; generated docs via their generators

Rollback/recovery: Revert only this task's commit if necessary; do not use destructive Git operations. Preserve run state/logs and avoid database rollback because no bulk writer is authorized by this task. Push recovery requires a follow-up corrective commit.

Evidence: Delegated read-only inventory classified active owner surfaces, legacy/comparison boundaries, generated references, historical docs, and isolated side projects. Fixed the confirmed full-suite collection defect in the browser-game harness import path, regenerated schema/script references, and aligned the canonical V2 pipeline documentation with the explicit overnight `pipeline` profile. Focused and full validation passed: generated-doc checker passed 3 references; full pytest passed 507 tests with 0 failures and 0 skips; browser-game harness passed 5 tests; diff checks passed. Commit `a48ee7b4441ea645b171aa6ba9e5894ff2002afe` was pushed successfully to `origin/main`.

## Hypothesis

If the repository is classified by active ownership and each confirmed cleanup issue is fixed in its owning surface with focused validation, then the final suite and documentation checks will show a coherent current system without requiring risky broad deletion.

## Plan

1. Delegate a read-only repository inventory and baseline assessment.
2. Create a ranked cleanup backlog with explicit active/legacy/generated boundaries.
3. Delegate and implement bounded fixes one owner surface at a time, validating after each edit.
4. Regenerate/check documentation and update canonical/Swimm explanations.
5. Run the broadest feasible validation, review the diff, commit, and push.

## Execution Checkpoints

- Delegation: AI CaseLibrary Project Manager worker completed the bounded repository inventory with the required structured report.
- Inventory: Active backend/orchestration surfaces, legacy/comparison code, generated docs, historical docs, and side projects classified; unrelated dirty worktree changes preserved.
- Implementation: side_projects/browser_game/tests/test_game_harness.py import portability fix; generated schema/script references regenerated.
- Documentation: SYSTEM_REFERENCE.md, OVERNIGHT.md, and .swm/8.upryk5h6.sw.md updated; generated references current.
- Validation: full pytest and generated-document checker passed.
- Commit/push: completed with the bounded cleanup commit `a48ee7b4441ea645b171aa6ba9e5894ff2002afe` pushed to `origin/main`; unrelated worktree changes remain unstaged.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-17 | Preserve legacy and historical code unless evidence proves safe separation/removal | User requested clear separation, not destructive deletion | Managed-task request and repository safety rules |
| 2026-09-17 | Use staged owner slices instead of one broad rewrite | Large cross-surface scope needs falsifiable checks | Project-manager workflow |

## Completion

Completion recorded: yes

Summary: Completed the bounded repository cleanup checkpoint: active/legacy boundaries documented, the confirmed full-suite collection defect fixed, generated docs synchronized, and the full test suite green.

Validation: `scripts/check_generated_docs.py` passed; `pytest -q` -> 507 passed, 0 failed, 0 skipped; browser-game harness -> 5 passed; `git diff --check` passed.

Residual risk: The worktree contains pre-existing unrelated changes and untracked artifacts, so only task-owned files may be committed. A repository-wide semantic review cannot prove every future cleanup opportunity; current high-value validation is green.

Next recommended task: Review the staged task-owned diff and push the dedicated cleanup commit only after confirming the intended remote and branch.
