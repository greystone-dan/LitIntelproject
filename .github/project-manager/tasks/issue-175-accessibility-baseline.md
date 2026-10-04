# Task: Implement issue #175 accessibility baseline

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Complete issue #175 by adding shared skip links and a narrow all-builder static contract alongside the accessibility statement, Citation Map alternative, optional axe coverage, and manual test plan; preserve existing title styling where heading levels changed.

Why now: Issue #175 closes known accessibility explanation and test-coverage gaps without making unsupported conformance claims.

Owner surface: Generated HTML/UI page-builder accessibility and title styling.

Commit allowed: via parent `engine-tools-report_progress` only

Push allowed: via parent `engine-tools-report_progress` only

Dependencies: Current branch is based on latest merged main. PR #136 is an open draft and is not a substitute for this task; implement only its exact requested skip-link/image-alt overlap, then document the later convergence point. Do not merge/cherry-pick it. PR #146 is responsive-only. No database, deployment, or environment-file access.

Risk boundary: Follow issue #112: no database, deployment, `.env`, new dependencies/password gates, or deleted features. Preserve the Citation Map's visual graph. Do not claim WCAG conformance or testing that did not occur.

Smallest falsifiable check: directly run the focused accessibility assertion functions and assert the About title CSS and case-reader title margin in rendered/source output; also attempt `python -m pytest -q tests/test_accessibility_page.py tests/test_page_builder_shell.py`.

Acceptance criteria:

- `/accessibility` and a footer/About link provide plain-language WCAG 2.1 AA target, actual static-check scope, known gaps, no conformance claim, and an owner-placeholder contact line; heading-semantic fixes preserve prior visible title size and spacing.
- Citation Map SVG has `title`/`aria-labelledby`, a text equivalent, and additive “View as table” node/link list; visual graph is unchanged.
- Every standalone generated page has one focusable skip-to-content target via one shared new module and minimal builder integrations; fragment injectors/pass-through routes are identified and documented.
- A static regression checks `lang`, title, viewport, exactly one `h1`, and image `alt` presence across every standalone builder. Any exceptions are narrowly documented.
- Optional axe test skips cleanly when Playwright/Chromium is unavailable; manual keyboard, NVDA, VoiceOver, 200% zoom, and contrast test plan exists.
- Canonical documentation and a relevant Swimm walkthrough are updated.
- Focused checks, generated-doc check, feasible CI-deselected full suite, secret scan, and fresh-main check are recorded honestly.
- PR #136 overlap and a post-merge convergence point are documented; do not import or duplicate its unrelated live-region/table/focus enhancements.

Harness criteria:

- Accessibility builder regressions pass.
- Documentation and Swimm checkpoints exist.
- Required broader validation is recorded with results or limitations.

Docs/generated references: `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`, `docs/reports/accessibility-manual-test-plan.md`; `scripts/check_generated_docs.py` verifies generated references.

Rollback/recovery: Revert only issue #175 changes; no data or schema changes.

Evidence: At assignment start, branch `copilot/accessibility-statement-page` was at merge commit `c0b8126`, whose parent includes `origin/main` `95dd903`. Managed worker inspected actual public diffs for PR #136/#146: PR #136 head `4dbe86f` adds `backend/pages/accessibility.py`, shared skip-link behavior and a generic regression that already asserts image-alt presence, but it does not add `/accessibility`, statement/contact/manual-test documentation, the Citation Map graph alternative, or document-shell assertions. PR #146 head `beecc1d` changes responsive layouts/tests only. User clarified that issue #175 must not wait for either draft; this branch implements the requested exact skip-link/alt overlap, excludes PR #136's unrelated enhancements, and records a later consolidation point. Final review correction adds a dedicated About-title class with the former `h1` typography and preserves the case-reader `h3` top margin on its new `h1`; focused regressions verify both.

Files changed: `backend/pages/access_gate.py`, `backend/pages/skip_link.py`, `backend/pages/accessibility_statement.py`, `backend/pages/case_compare.py` (main's new complete builder now receives the helper), `backend/pages/discussion_units_sandbox_route.py`, all complete HTML builders in `backend/pages/`, `backend/case_reader_ui.py`, `backend/main.py`, `backend/discussion_units_sandbox.py`, `backend/routes.py`, `backend/pages/about_content.html`, `tests/test_page_builder_shell.py`, `tests/test_accessibility_page.py`, `tests/test_accessibility_builders.py`, `tests/test_accessibility_axe.py`, `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `CHANGELOG.md`, `docs/reports/accessibility-audit.md`, `docs/reports/accessibility-manual-test-plan.md`, `.swm/6.maiixtsw.sw.md`, and this task record. Added follow-up recommendation `.github/project-manager/improvements/2026-10-04-inline-script-syntax-check.md`.
Delegated work: Managed worker reviewed PR #136/#146 diffs and implemented the shared primitive, minimal builder decorators, and shell/alt/skip test across 20 builders. Manager review found the separate Discussion Units route builder and private access page; these were added to the shared inventory without importing routes or reading `.env`/using the database. The worker's exact structured report is reflected in the inventory/validation checkpoint.
Focused validation after the final main refresh: direct execution of every `test_*` function in `tests/test_page_builder_shell.py`, `tests/test_accessibility_page.py`, and `tests/test_accessibility_builders.py` passed (7 functions); all 23 full-page outputs passed shell, skip-target, and image-alt assertions. `python -m compileall -q backend/pages backend/main.py backend/discussion_units_sandbox.py backend/case_reader_ui.py` passed (existing invalid-escape `SyntaxWarning`s in Data Explorer and Theme Explorer remain). Both rendered Citation Map inline scripts passed `node --check`. Secret scan of 39 changed files found zero high-confidence credential patterns; staged and unstaged `git diff --check` passed. Local Markdown link review found two missing `SYSTEM_REFERENCE.md` targets (`ANALYST_QUICK_START.md`, `reports/test-coverage.md`); both already occur in the merged baseline, are unrelated, and no new local link was broken. `python -m pytest -q` with the three documented CI deselections could not start (`No module named pytest`). `python scripts/check_generated_docs.py` could not finish because `fastapi` and `sqlalchemy` are unavailable. No browser/axe, screen-reader, or 200% zoom tests ran. Main's latest commit `3720556` (#180) was merged as local merge commit `f87dfa7`; final `git fetch origin main` confirmed `HEAD` is four commits ahead and zero behind.

Final design review correction: `backend/pages/about_content.html` keeps the About title as an `h2` while its `.about-title` rule duplicates the former `h1` typography and spacing; the case-reader `h1` retains a `1em` top margin from its previous `h3`. The new assertions in `tests/test_accessibility_page.py` initially exposed that the shared skip helper appends focus attributes to the heading; the assertion was corrected to account for that rendered contract. The final direct run passed all 8 focused functions, including the 23-builder shell contract and both visual-preservation assertions. `python -m compileall -q backend/case_reader_ui.py tests/test_accessibility_page.py`, `git diff --check`, and a final 39-file secret scan passed (zero matches). Focused pytest was attempted but remains unavailable (`No module named pytest`). The visual correction is documentation-linked in `SYSTEM_REFERENCE.md` and `.swm/6.maiixtsw.sw.md`.
Residual risk: The environment lacks pytest and generator dependencies; axe/browser, screen-reader, and 200% zoom checks have not run. PR #136 has exact helper/alt overlap, requiring later consolidation if it merges. No WCAG conformance claim.
Next bounded task: Run focused pytest and the documented manual accessibility checks when the required test/browser/assistive-technology tools are available.

## Hypothesis

If one shared helper and one complete builder inventory provide the precise skip-link and shell/alt contracts, focused rendered-output checks will verify every standalone page without importing PR #136's unrelated enhancements.

## Plan

1. Inspect PR #136/#146 overlap and document boundaries/convergence.
2. Inventory all standalone builders; add one shared skip-link helper and shell/alt/skip regression.
3. Include complete route/access pages, update statement/canonical docs/Swimm, and validate without database access.

## Execution Checkpoints

- Delegation: Managed worker reviewed PR #136/#146 actual diffs and returned structured output. It implemented the shared helper and 20-builder regression; manager added complete access/discussion route pages to that inventory.
- Implementation: `backend/pages/skip_link.py` supplies the sole shared skip-link primitive; `tests/test_page_builder_shell.py` now checks shell fields, focusable skip target, and image-alt presence across 23 complete page documents, including main's `/case-compare`. No unrelated PR #136 semantics were adopted.
- Documentation: Canonical repository sources `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `CHANGELOG.md`, and accessibility reports `docs/reports/accessibility-audit.md`, `docs/reports/accessibility-manual-test-plan.md`; Swimm walkthrough `.swm/6.maiixtsw.sw.md`.
- Recovery: No long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | User supplied bounded issue requirements and merge boundary | Worktree at `c0b8126`; `origin/main` at `95dd903` |
| 2026-10-04 | Resumed exact issue acceptance criteria | Open PR #136 is not in main and does not satisfy issue #175's route, statement, graph, or shell contract; user authorized only the exact skip/alt overlap | Updated task record and manager-owned minimal integration |
| 2026-10-04 | Added shared skip-link + complete static inventory | Every full generated page must satisfy the user contract in this branch; avoid importing or copying unrelated PR #136 behavior | Managed worker: 20 builders; manager-added access gate and Discussion Units route make 22 |
| 2026-10-04 | Refreshed main | Check whether the shared helper became available | `git fetch origin main`; `HEAD=c0b8126`, `origin/main=95dd903`, `2 0`; no merge required |
| 2026-10-04 | Removed duplicate generic implementation after user review | Keep this branch additive and avoid publishing overlapping unstaged builder edits | `git status` contains no helper or generic all-builder test; final diff check passed |
| 2026-10-04 | Final main refresh after shell-test scope correction | Confirm latest main still does not contain PR #136 | `git fetch origin main`; `HEAD=c0b8126`, `origin/main=95dd903`, `2 0`; no merge required |
| 2026-10-04 | Refreshed and merged newly advanced main | User required final refresh; `main` gained five commits after task start | `git fetch origin main`; fetched `38f9e3b`, `HEAD=c0b8126`; merged `FETCH_HEAD`; preserved main changes to Data Explorer and Memo Citation Check while resolving the shared-helper imports |
| 2026-10-04 | Final post-merge acceptance | Ensure all complete documents, including newly merged case comparison, retain the issue contract | Direct 7-function run passed across 23 builders; compileall, both Citation Map `node --check`s, secret scan, and `git diff --check` passed; pytest/generator dependencies unavailable |
| 2026-10-04 | Refreshed and merged latest main once more | Main advanced by a documentation-only commit after first final refresh | `git fetch origin main`; fetched `3720556` (#180); merge commit `f87dfa7`; final ancestry `4 0`; no accessibility conflicts |
| 2026-10-04 | Preserve visible title design after semantic heading corrections | User identified typography and top-spacing regressions from changing heading levels | `.about-title` duplicates former `h1` declarations; rendered case-reader `h1` retains `margin-top: 1em`; 8 direct test functions pass; pytest unavailable; commit/push prohibited |

## Completion

Completion recorded: yes

Summary: Implemented the issue #175 feature set locally, including shared skip links and static contracts for all 23 full-page builders, including `/case-compare` added by refreshed main. PR #136's requested overlap is limited to the exact skip-link/alt contract and documented for future convergence.

Validation: Post-merge direct rendered-output assertions (7 functions over 23 pages), compilation, Citation Map JavaScript syntax, secret scan, and staged/unstaged diff checks passed. Pytest and generated-doc verification were attempted and blocked by missing dependencies; see Evidence.

Residual risk: Browser/axe, screen-reader, and zoom checks remain unverified. No conformance claim.

Next recommended task: Execute manual keyboard/screen-reader/zoom/contrast checks in a suitable environment; if PR #136 merges, reconcile the duplicate helper and overlapping image-alt test.
