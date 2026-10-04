# Task: Judge issue-first outcome table

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Complete issue #116 by adding a judge issue-first outcome table and Federal Court baseline, exposed through `GET /api/judge-profiles/{slug}/issues` and a lazy-loaded Judge Profile section.

Why now: The judge profile workflow needs transparent issue-level outcome evidence without turning sparse data into misleading percentages or comparative rankings.

Owner surface: Judge Profile workflow (`backend/routes.py`, analytics service, and `backend/pages/`).

Commit allowed: yes

Push allowed: yes

Dependencies: Existing issue brief and judge comparison aggregation precedents; stored judge and issue/outcome metadata.

Risk boundary: No database access, schema/migration changes, new dependencies, `.env`/secret access, deployment, rankings, or harshness inference. Preserve existing profile metrics and distinguish the denominator from unclassified outcomes.

Smallest falsifiable check: `python -m pytest -q tests/test_api.py -k judge_profile_issues`

Acceptance criteria:

- API returns issue-first four-category outcomes (Minister win, applicant win, other, unclassified) and a matching Federal Court-wide baseline with explicit safe denominators.
- Suppress issue rows below 10 observations and disclose the hidden issue count; unknown judge slugs return 404.
- Judge Profile lazily loads the section and displays one-line outcome-method and unclassified-denominator disclosures without changing existing profile metrics.
- Focused checks and generated-document consistency pass; the exact full-suite CI command is run and any environment-limited failures are recorded.

Harness criteria:

- `python -m pytest -q tests/test_api.py -k judge_profile_issues`
- `python -m pytest -q tests/test_feature_tabs.py`
- Full pytest with the three documented CI deselections is run; environment-limited failures are recorded.
- `python scripts/check_generated_docs.py`
- Secret scan and parallel validation complete without exposing secrets or accessing a database.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, relevant Judge Profile Swimm walkthrough, and generated API reference if its source contract changes.

Rollback/recovery: Revert only the feature-specific route, query, UI, tests, and documentation edits; no data or schema state is changed.

Evidence: Managed-worker returned the required structured API implementation findings. Its initial tests were blocked by missing packages. Manager prepared `/tmp/litintel-issue116-venv` using existing pinned requirements only; focused failures exposed incorrect category expectations and a SQLite cross-thread fixture, both repaired. Canonical outcomes are `won`/`lost`/`mixed`; undetermined and unrecognized outcomes are unclassified. Canonical documentation: `SYSTEM_REFERENCE.md` and `CHANGELOG.md`; Swimm walkthrough: `.swm/6.maiixtsw.sw.md`; generated API contract regenerated from `scripts/generate_api_reference.py`.

Files changed: `.github/project-manager/tasks/issue-116-judge-issue-outcomes.md`, `.swm/6.maiixtsw.sw.md`, `CHANGELOG.md`, `SYSTEM_REFERENCE.md`, `backend/analytics_service.py`, `backend/pages/explorer_snapshots.css`, `backend/pages/explorer_snapshots.js`, `backend/routes.py`, `docs/API_REFERENCE.generated.md`, `tests/test_feature_tabs.py`, `tests/test_judge_comparison.py`.
Delegated work: `judge-issues-api` managed-worker; changed only the API/query/tests surface and returned the exact structured fields requested. Initial test environment lacked pytest and runtime packages; no DB, secret, deployment, or dependency-manifest access occurred.
Focused validation: `PYTHON_DOTENV_DISABLED=true /tmp/litintel-issue116-venv/bin/python -m pytest -q tests/test_judge_comparison.py tests/test_issue_brief.py tests/test_judge_profiles.py tests/test_feature_tabs.py` — 83 passed, 1 skipped. `scripts/check_generated_docs.py` passed (3 references); `py_compile`, `node --check`, `git diff --check`, diff-only secret-pattern scan (no dedicated scanner installed), and fixture-only headless Chromium interaction all passed.
Residual risk: The exact full suite ran 1,254 passed, 2 skipped, 1 xfailed, and 3 deselected, with 3 failures in unrelated embedding/token accounting tests because `sentence-transformers` and `tiktoken` are absent from the temporary environment. No model/tokenizer assets were downloaded. Federal Court matching is limited to stored court labels `FC`, `Federal Court`, and `Federal Court of Canada`; no corpus/live database was accessed.
Next bounded task: None required for #116; revisit court-label variants only if source-backed fixtures establish additional Federal Court labels.

## Hypothesis

If issue outcomes use a shared judge/Federal Court issue population with explicit all-outcome denominators, suppressing groups below ten, then focused API tests will prove that percentages cannot silently exclude unclassified decisions.

## Plan

1. Confirm local issue-brief, comparison, Judge Profile, and Swimm precedents without database access.
2. Implement and test the issue outcome endpoint, then add the lazy-loaded section and focused UI coverage.
3. Update canonical documentation and Swimm, regenerate generated references if needed, and run focused, full-suite, and documentation checks.

## Execution Checkpoints

- Delegation: `judge-issues-api` managed-worker returned structured findings and implemented the API slice; manager repaired fixture/mapping failures and verified it.
- Implementation: API, tests, and lazy UI implemented; focused judge/profile/UI set passed.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and `.swm/6.maiixtsw.sw.md`; regenerated `docs/API_REFERENCE.generated.md` from its generator and verified all generated references.
- Recovery: No database or long-running data operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | User requested a bounded implementation of issue #116 with explicit denominator, privacy, and scope constraints. | User-provided issue acceptance criteria; repo task template |

## Completion

Completion recorded: yes

Summary: Issue #116 completed with an issue-first table, minimum-threshold privacy, safe category denominators, Federal Court baseline, unknown-judge 404, and click-to-load Judge Profile section. Existing profile metrics remain unchanged.

Validation: Focused set 83 passed/1 skipped; generated-doc check passed; fixture-only Chromium check passed; exact full-suite CI command ran with 1,254 passed, 2 skipped, 1 xfailed, 3 deselected, and 3 unrelated missing-dependency failures. No database access, secrets, deployments, migrations, or dependency-manifest changes.

Residual risk: The three full-suite failures require local embedding/tokenizer packages/assets; no download was attempted. Federal Court label scope is explicit and corpus coverage was not inspected.

Next recommended task: None required for #116.
