# Task: Add evidence-backed extractive case summary card

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #232 as a new, additive extractive case summary-card module, endpoint, and conditional formatted-reader card with traceable key-paragraph selections.

Why now: Provide a concise, verifiable overview without changing the existing quick-summary contract or mixing citations, statutes, and legal tags.

Owner surface: Read-only case summary-card projection and its reader integration (`backend/case_summary_card.py`, route/page call sites).

Commit allowed: yes

Push allowed: yes

Dependencies: Existing reader service/formatter, stored citations/outcomes/tags/statutes/judges, discussion-unit evidence rules, current quick-summary implementation, and fixture-backed reader/API tests.

Risk boundary: No database, `.env`, live data, deployment, or invented evidence; preserve source offsets and distinguish citations, statutes, and tags. Keep the existing summary endpoint unchanged and make the new endpoint additive.

Smallest falsifiable check: `PYTHON_DOTENV_DISABLED=1 /tmp/litintel-summary-card-venv/bin/python -m pytest -q tests/test_case_summary_card.py`

Acceptance criteria:

- Add `backend/case_summary_card.py` and independently named `GET /api/cases/{case_id}/summary-card`, returning citation, court, date, judge, outcome and its determination source, statutes, top tags, and up to three key paragraphs.
- Select key paragraphs by transparent rules: disposition/conclusion; highest stored later pinpoint citation counts; standard-of-review statement. Every selection has paragraph number, exact text, and its rule.
- Add a compact collapsible formatted-reader “Quick summary” card, with the notice “Selected passages, not a summary written by AI”; omit missing data rather than infer it.
- Fixture tests cover each selection rule, missing data, long paragraphs truncated at a sentence with ellipsis/link to full paragraph, and reader rendering only when data exists.
- Inventory the new backend module and update the canonical document plus relevant Swimm walkthrough.
- Focused tests, generated-document check, diff check, secret scan, and applicable parallel validations pass or are explicitly recorded as blocked.
- Branch synchronization with the latest `origin/main` is complete through the available approved workflow.

Harness criteria: summary-card selection and missing-data fixtures pass; truncated evidence and links are preserved; reader conditionally renders the card; generated references are current.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, `.swm/6.maiixtsw.sw.md`; generated API reference from its source.

Rollback/recovery: Revert the additive module/route/page/test changes and corresponding documentation; no schema or stored data changes.

Evidence: Public issue #232 was retrieved from its GitHub HTML structured-data body after `gh issue view` failed (missing `GH_TOKEN`) and the unauthenticated API returned 403. Exact requirements are recorded above. The delegated worker's first API reused the existing projection and did not meet issue #232's rules; manager recovery replaced it with the independent stored-evidence projection and reader card. Canonical documentation, architecture inventory, relevant Swimm walkthrough, generated API reference, and changelog are updated. Fresh `origin/main` fetch discovered commit `ef9939bb3eff3bf94858e4bc45276347cdb8ca97` (#240) after task start: current branch HEAD is `cb5b2eb4a549f11e2a4d2b0992bec78f77f29fdc`, merge-base remains `473508851d600b74e0cd29bbbdf92c6118954aa3`. Changes overlap `CHANGELOG.md` and `docs/ARCHITECTURE.md`; synchronizing requires history integration, and this environment has no `report_progress` workflow. No merge/rebase/commit/push was performed.

Files changed: `.github/project-manager/tasks/232-extractive-case-summary-card.md`, `.swm/6.maiixtsw.sw.md`, `CHANGELOG.md`, `SYSTEM_REFERENCE.md`, `backend/case_summary_card.py`, `backend/pages/case_summary_card.py`, `backend/pages/data_explorer.py`, `backend/routes.py`, `docs/API_REFERENCE.generated.md` (generated), `docs/ARCHITECTURE.md`, `tests/test_case_summary_card.py`, `tests/test_inline_js_syntax.py`.
Delegated work: `summary-card-api` inspected the reader/projection/legal tag/discussion-unit/API tests and added an initial API slice; its structured return identified pytest unavailable and issue-specific citation uncertainty. Manager retrieved the exact public issue body, replaced the placeholder selection implementation, added UI/docs/tests, and independently validated the final work.
Focused validation: `PYTHON_DOTENV_DISABLED=1 /tmp/litintel-summary-card-venv/bin/python -m pytest -q tests/test_case_summary_card.py` passed (10, including Chromium at 1280×900 and 390×900); `tests/test_case_quick_summary_ui.py` passed (10, including its browser fixtures); adjacent summary/API filters passed (2); reader keyboard/print filters passed (2); inline-JS syntax filters passed (2); `tests/test_documentation_contracts.py` passed (2); `scripts/check_generated_docs.py` reported all three generated references current. `compileall`, changed-file secret-pattern scan, and `git diff --check` passed. All fixture tests used `PYTHON_DOTENV_DISABLED=1`; no database, `.env`, live data, or deployment operation was used.
Residual risk: Feature work is complete, but the branch is behind newly fetched `origin/main` (#240). No synchronization commit/rebase can be made through the requested `report_progress` workflow because that tool is unavailable; upstream additions to `CHANGELOG.md` and `docs/ARCHITECTURE.md` have not been integrated.
Next bounded task: Synchronize this feature branch with `origin/main` through the authorized progress workflow, then rerun generated-document and focused summary-card checks.

## Hypothesis

If the card selects only existing stored evidence according to the issue’s three stated rules, focused fixtures will prove exact traceability, missing-data omission, and conditional reader presentation without changing existing quick-summary behavior.

## Plan

1. Record the issue’s exact selection contract and inspect source/tag/citation/outcome/judge evidence contracts.
2. Replace the interim API projection and implement the collapsible conditional reader card with source links.
3. Run focused tests, generated-document check, secret scan, diff check, and final acceptance validation.

## Execution Checkpoints

- Delegation: `summary-card-api`; structured return received; placeholder endpoint replaced against the retrieved issue body.
- Implementation: Independent read-only response and conditional reader card implemented; focused API/selection/browser fixtures pass.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/ARCHITECTURE.md`, `CHANGELOG.md`, generated `docs/API_REFERENCE.generated.md`, and `.swm/6.maiixtsw.sw.md` updated and verified.
- Recovery: Not applicable; fixture-only, no persisted data changes.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Created task record before implementation | Multi-step additive API/UI feature requires auditable acceptance criteria | User request; current `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, repository invariants |
| 2026-10-04 | Adopt issue body’s explicit holding/statute card contract | Existing stored quick-summary projection is not a substitute: it omits judge and citation-ranked key paragraphs | Public issue #232 body retrieved from GitHub HTML; user provided issue #112 Rules interpretation |
| 2026-10-04 | Block final completion on concurrent main advance | Fresh fetch moved `origin/main` to #240; branch integration requires history synchronization unavailable through the requested reporting workflow | `git fetch origin main:refs/remotes/origin/main`; HEAD/merge-base/origin SHAs in Evidence |

## Completion

Completion recorded: no

Summary: Feature implementation and focused validation are complete; repository task remains blocked on synchronizing the branch with concurrently advanced `origin/main`.

Validation: Focused summary-card API/selection/UI/browser, existing quick-summary browser, adjacent summary/API, keyboard/print, inline-JS, documentation-inventory, generated-reference, compile, changed-file secret scan, and diff checks passed. Full-suite tests and live-data/database operations were not run.

Residual risk: Latest `origin/main` is not integrated; no merge/rebase/commit/push was performed.

Next recommended task: Synchronize branch with `origin/main` using the authorized progress workflow, then rerun focused validation.
