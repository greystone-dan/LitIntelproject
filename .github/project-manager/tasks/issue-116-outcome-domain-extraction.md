# Task: Extract judge issue outcome domain logic

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Move judge issue outcome aggregation helpers and constants from `backend/analytics_service.py` into `backend/judge_issue_record.py`, preserving existing imports and behavior, and verify the profile's unclassified-outcome denominator disclosure.

Why now: The committed issue #116 implementation put domain logic in the analytics service instead of the explicitly requested dedicated module.

Owner surface: Judge issue outcomes (`backend/judge_issue_record.py`, compatibility exports, and their focused tests)

Commit allowed: yes

Push allowed: yes

Dependencies: Existing judge profile issue API and fixtures; no database access.

Risk boundary: Preserve current judge profile metrics, response/API contracts, and read-only behavior. No database, `.env`, migrations, dependencies, deployment, or unrelated judge profile changes.

Smallest falsifiable check: `python -m pytest -q tests/test_judge_comparison.py -k judge_issue`

Acceptance criteria:

- Domain constants/helpers and aggregation logic are owned by `backend/judge_issue_record.py`.
- Existing API/import compatibility through `backend/analytics_service.py` remains intact.
- The UI explicitly explains outcome assignment and that percentages include unclassified decisions in the denominator.
- The hidden-issue count explicitly says each hidden issue has fewer than 10 decisions.
- Focused tests pass; full repository checks, generated-doc check, and secret scan are reported accurately.

Harness criteria: Not used for this bounded follow-up.

Docs/generated references: Update `SYSTEM_REFERENCE.md` and `.swm/6.maiixtsw.sw.md` to identify the module owner; run `python scripts/check_generated_docs.py` (generated references should remain unchanged).

Rollback/recovery: Revert only this follow-up's source, test, and documentation edits; no data or schema state is touched.

Evidence: Implemented the module extraction and compatibility re-exports; source now assigns aggregation to `backend/judge_issue_record.py`. The UI explains outcome assignment and the unclassified-inclusive denominator, and now explicitly says `${N(hidden)} issue(s) hidden (each has fewer than ${minimum} decisions)`; the focused assertion checks this exact source text. Canonical documentation updated at `SYSTEM_REFERENCE.md`; Swimm walkthrough updated at `.swm/6.maiixtsw.sw.md`. Static checks passed: Python compilation, `git diff --check`, exact disclosure/source-test check, `node --check`, and changed-file credential-pattern scan (0 matches). Focused and full pytest runs could not start because pytest is absent; generated-doc validation could not run because FastAPI and SQLAlchemy are absent. No database, `.env`, migration, dependency, or deployment operation was performed. No commit made.

Files changed: `.github/project-manager/tasks/issue-116-outcome-domain-extraction.md`, `backend/judge_issue_record.py`, `backend/analytics_service.py`, `backend/pages/explorer_snapshots.js`, `tests/test_judge_comparison.py`, `tests/test_feature_tabs.py`, `SYSTEM_REFERENCE.md`, `.swm/6.maiixtsw.sw.md`.
Delegated work: `managed-worker` moved the issue outcome aggregation logic/helpers/constants into the dedicated module and added compatibility assertions. Its structured report confirmed the moved block matched the original; worker focused pytest attempt failed because `pytest` is not installed.
Focused validation: `PYTHON_DOTENV_DISABLED=true python -m pytest -q tests/test_judge_comparison.py -k judge_issue`, `PYTHON_DOTENV_DISABLED=true python -m pytest -q tests/test_feature_tabs.py -k judge_issue_outcomes_are_lazy_loaded`, and `PYTHON_DOTENV_DISABLED=true python -m pytest -q` could not start (`No module named pytest`). `python scripts/check_generated_docs.py` failed because `fastapi` and `sqlalchemy` are unavailable. Python test compilation, exact disclosure/source-test check, `git diff --check`, credential-pattern scan, and `node --check backend/pages/explorer_snapshots.js` passed. An attempted `py_compile` that included the JavaScript file was inapplicable and failed; the proper Node syntax check passed.
Residual risk: Runtime test suite and generated-document drift remain unverified in this dependency-free environment.
Next bounded task: In an existing dependency-equipped environment, rerun the two focused tests, full pytest suite, and `python scripts/check_generated_docs.py`; do not add/install dependencies as part of this follow-up.

## Hypothesis

If the issue outcome domain logic is moved without behavior changes, the focused judge-issue fixture/API checks will pass while importing the existing service entry point continues to work.

## Plan

1. Move the aggregation implementation into the dedicated domain module and preserve analytics-service exports.
2. Verify/fix the single-line outcome-assignment and denominator disclosure.
3. Update the canonical architecture reference and Judge Profile Swimm walkthrough.
4. Run focused then repository-required validation and inspect the final diff.

## Execution Checkpoints

- Delegation: Managed-worker implemented the domain extraction in the bounded module/test surface; pytest unavailable.
- Implementation: `backend/judge_issue_record.py` now owns issue aggregation; `backend/analytics_service.py` re-exports existing function/helper/constant names. The hidden-count disclosure states that each issue has fewer than the displayed decision threshold.
- Documentation: Updated `SYSTEM_REFERENCE.md` and `.swm/6.maiixtsw.sw.md` to reflect module ownership and the explicit hidden-issue threshold.
- Recovery: Not applicable; no long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Keep the change a module-ownership refactor | User identified the explicit issue #116 module-location mismatch and requested no unrelated changes | Existing architecture says judge issue response uses `backend/analytics_service.py`; issue asks for a dedicated module |
| 2026-10-04 | Block pending runtime validation | Required pytest and generated-doc checks cannot run without unavailable repository dependencies; dependency installation is out of scope | `No module named pytest`; generated-doc checker reports unavailable `fastapi` and `sqlalchemy` |
| 2026-10-04 | Make hidden-count disclosure explicit | Follow-up acceptance requires each hidden issue count to state that hidden issues have fewer than the threshold decisions | UI copy and `tests/test_feature_tabs.py` assertion now include the explicit threshold |

## Completion

Completion recorded: no

Summary: Code, compatibility tests, disclosure assertion, and ownership documentation updated. Task remains blocked pending focused/full test and generated-doc validation in an existing dependency-equipped environment.

Validation: Static compilation, exact disclosure check, JavaScript syntax, diff whitespace, and changed-file credential-pattern scan passed. Focused pytest, full pytest, and generated-doc checks could not run to completion because required dependencies are absent.

Residual risk: Runtime behavior and generated references are not verified by this environment. No commit was made.

Next recommended task: Run the blocked checks in an existing dependency-equipped environment; then decide on commit.
