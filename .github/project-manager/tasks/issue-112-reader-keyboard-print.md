# Task: Add case reader keyboard navigation and print support

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add keyboard paragraph navigation/help and print-specific case reader styling requested by issue #112.

Why now: Reader usability and printable research copies are requested without changing routes or evidence ownership.

Owner surface: Inline case reader in `backend/pages/data_explorer.py`, its styles/scripts, and focused UI tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing formatted paragraph anchors and the active UI walkthrough.

Risk boundary: Keep changes within the reader UI, CSS/JS, tests, and docs. Preserve backend paragraph identity/offsets and all existing reader features; do not read `.env`, access the database, or touch deployment scripts.

Smallest falsifiable check: Focused source-contract test `python -m pytest tests/test_feature_tabs.py -k inline_reader_keyboard_navigation_and_print_contract`; not run per the user's explicit restriction.

Acceptance criteria:

- `j`/`n` moves to the next paragraph and `k`/`p` to the previous paragraph; typing in inputs/editable fields does not trigger navigation.
- Current/focused paragraph is visibly highlighted and `?` reveals the available shortcuts.
- Print output hides navigation, side panels, and buttons; retains paragraph numbers, avoids paragraph splits, and includes citation/title header.
- Focused source-contract test added; test execution explicitly prohibited.
- Canonical UI documentation and relevant Swimm walkthrough updated.
- `scripts/check_generated_docs.py` and changed-file secret scan attempted; do not run lint/build/tests per the request.

Harness criteria: Reader behavior, print behavior, docs checkpoint, and generated-doc/secret-scan checks are recorded.

Docs/generated references: `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`; no generated references expected because routes/contracts do not change.

Rollback/recovery: Revert only the issue #112 reader, tests, and documentation changes; no data or schema changes.

Evidence: Worker added keyboard, focus, help, typing-target, and print behavior plus a focused source-contract test in `backend/pages/data_explorer.py` and `tests/test_feature_tabs.py`. Updated `docs/RESEARCH_UI_GUIDE.md`, `SYSTEM_REFERENCE.md`, and `.swm/6.maiixtsw.sw.md`. `git diff --check` passed on the final worktree. The changed-file secret-pattern scan found no matches. `python scripts/check_generated_docs.py` failed because the environment lacks `fastapi` and `sqlalchemy`, required by two reference generators. Tests were not run as explicitly instructed. `engine-tools-report_progress` is unavailable (not exposed as a tool and no command installed), so the requested tool-mediated commit/push step could not be performed; no commit or push was attempted.

Files changed: `.github/project-manager/tasks/issue-112-reader-keyboard-print.md`, `.swm/6.maiixtsw.sw.md`, `SYSTEM_REFERENCE.md`, `backend/pages/data_explorer.py`, `docs/RESEARCH_UI_GUIDE.md`, `tests/test_feature_tabs.py`.
Delegated work: `managed-worker` implemented reader keyboard/print behavior and a focused contract test; structured return received. Worker ran `git diff --check`, not tests.
Focused validation: `git diff --check` passed; `python scripts/check_generated_docs.py` failed due missing `fastapi` and `sqlalchemy`; secret-pattern scan found no matches. No tests, lint, or build were run.
Residual risk: No browser validation or test execution; generated-doc check is blocked on missing dependencies. The requested progress tool is unavailable, so no commit/push was made.
Next bounded task: Re-run `scripts/check_generated_docs.py` and the focused UI test when dependencies and the progress tool are available; then commit/push through the requested workflow.

## Hypothesis

If the inline reader adds scoped keyboard handlers, explicit paragraph-current styling, and print-only layout rules, a focused code review will show the requested navigation and print behavior without affecting other reader modes or source evidence.

## Plan

1. Delegated the inline reader markup/style/script and focused test to one owner.
2. Updated the active UI walkthrough and canonical reader documentation.
3. Reviewed the diff and ran only permitted non-test checks; recorded missing dependencies and unrun tests.

## Execution Checkpoints

- Delegation: `managed-worker` completed the inline reader implementation and focused test; tests were not run.
- Implementation: `backend/pages/data_explorer.py` and `tests/test_feature_tabs.py`.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, and `.swm/6.maiixtsw.sw.md`.
- Recovery: Not applicable; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Keep the change in the existing inline reader UI | Issue scope concerns reader interaction and printing; routes/data contracts do not need to change | Issue #112 request and active UI ownership in Swimm |

## Completion

Completion recorded: no

Summary: Implementation and documentation are present; task is blocked on unavailable generated-doc dependencies and required progress/commit workflow.

Validation: `git diff --check` passed; secret-pattern scan had no findings. Generated-doc check failed because `fastapi` and `sqlalchemy` are not installed. Tests were not run per explicit instruction.

Residual risk: Browser output and tests remain unverified; no commit/push was possible through the unavailable requested tool.

Next recommended task: Restore the required environment dependencies and progress tool, then run the generated-doc check and focused UI test and complete the commit/push workflow.
