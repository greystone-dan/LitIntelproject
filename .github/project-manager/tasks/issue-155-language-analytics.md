# Task: Issue #155 language analytics

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add bounded, offline phrase association analysis for one tag, an API endpoint, and a research page.

Why now: Provide a transparent, fixture-testable way to inspect wording associated with allowed versus dismissed decisions without implying causation.

Owner surface: Language analytics feature (`backend/language_analytics.py`, `scripts/phrase_analysis.py`, minimal API/page registration and associated tests).

Commit allowed: yes

Push allowed: yes

Dependencies: Existing database access layer for local execution; tests must use fixtures only.

Risk boundary: No database/deployment operations, no `.env` reads or writes, no feature deletion, dependencies, or password gating. Bound scanned decisions; count and exclude unclassified cases. Describe wording associations, not causes.

Smallest falsifiable check: `PYTHON_DOTENV_DISABLED=1 python -m pytest --confcutdir=/tmp -q tests/test_language_analytics.py` (excludes the repository conftest's PostgreSQL probe)

Acceptance criteria:

- 2–4 word phrases distinguish allowed and dismissed decisions using a robust interpretable score, with minimum document frequency 5, group document counts and denominators.
- The analysis is offline/read-only, accepts one tag and optional judge, caps scanned decisions and reports whether capped, and reports excluded unclassified decisions.
- `GET /api/language-analytics?tag=...` returns the top 25 phrases per side; `/language-analytics` prominently cautions that wording associations are not causes.
- Tests use fixtures only; the CLI/API do not run during development against a database.
- Evaluation plan states exactly what to check, and canonical and Swimm docs are updated.
- Focused tests and `python scripts/check_generated_docs.py` pass.

Harness criteria:

- Fixture-only phrase scoring and bounds tests pass.
- Endpoint and page contract tests pass.
- Generated documentation check passes.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/reports/language-analytics-evaluation-plan.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/6.maiixtsw.sw.md`; generated references via their generator only if drift requires it.

Rollback/recovery: Revert only the issue-specific source, tests, and documentation changes; no database state or schema changes are involved.

Evidence: The feature and fixture tests are implemented and validated. GitHub CLI issue access was unavailable because `GH_TOKEN` is not configured; implementation scope and issue #112 rules were supplied directly by the user. **Blocked from clean acceptance:** the initial ordinary pytest invocation (also reported by the first worker) loaded `tests/conftest.py`, whose module-level availability check imports `SessionLocal` and attempts `SELECT 1`; the initial manager invocation also lacked `PYTHON_DOTENV_DISABLED`, so import-time dotenv loading may have read `.env`. No database writes, deployments, direct `.env` inspection/modification, or browser interaction were performed. This was not intentional. All subsequent validation used `PYTHON_DOTENV_DISABLED=1 --confcutdir=/tmp`, excluding dotenv loading and the repository conftest probe. Whether the initial probe connected or dotenv files were present/read is not observable from the test output. Safe options: preserve the changes and let the user decide whether to accept this disclosed process deviation, or defer acceptance; do not rerun tests with the repository conftest or without dotenv disabled.

Files changed: `.github/project-manager/tasks/issue-155-language-analytics.md`; `.github/project-manager/improvements/2026-10-04-worker-analytics-acceptance.md`; `backend/language_analytics.py`; `backend/pages/language_analytics.py`; `backend/routes.py`; `scripts/phrase_analysis.py`; `tests/test_language_analytics.py`; `docs/reports/language-analytics-evaluation-plan.md`; `SYSTEM_REFERENCE.md`; `DOCS_INDEX.md`; `CHANGELOG.md`; `.swm/1.oi7rhqp2.sw.md`; `.swm/6.maiixtsw.sw.md`; `.swm/evaluation-framework-and-quality-metrics.nftvfh5p.sw.md`; regenerated `docs/API_REFERENCE.generated.md` and `docs/SCRIPT_CATALOG.generated.md`.
Delegated work: Managed worker implemented the initial service/CLI/page/routes and fixture tests; manager review found the first report nonconforming and code still had an unbounded/N+1 tag lookup and denominator-insensitive scoring. A bounded recovery worker added tests and claimed the query issue was fixed, but manager verification found N+1 loading remained. Manager replaced it with a tag-filtered, bounded query, shared normalized scoring/result serialization, and behavior-level fixtures. Follow-up process recommendation recorded at `.github/project-manager/improvements/2026-10-04-worker-analytics-acceptance.md`.
Focused validation: `PYTHON_DOTENV_DISABLED=1 python -m pytest --confcutdir=/tmp -q tests/test_language_analytics.py` — 74 passed; `PYTHON_DOTENV_DISABLED=1 python -m pytest --confcutdir=/tmp -q tests/test_feature_tabs.py` — 58 passed, 1 skipped; `python -m py_compile backend/language_analytics.py backend/routes.py backend/pages/language_analytics.py scripts/phrase_analysis.py tests/test_language_analytics.py` — passed; `python scripts/phrase_analysis.py --help` — passed without opening a session; Node inline JavaScript syntax check — passed; `python scripts/generate_api_reference.py` and `python scripts/generate_script_catalog.py` — regenerated; `python scripts/check_generated_docs.py` — all 3 references current; `git diff --check` — passed.
Residual risk: No corpus analysis or PostgreSQL result query was deliberately run; the initial pytest conftest read-only connection probe and possible import-time dotenv read are recorded above. The PostgreSQL JSONB filter was checked by offline SQL compilation and fixtures only. The exact-tag match is case/spacing sensitive at the database boundary. A capped cohort uses ascending case IDs and may be biased by ingest order. No real browser runtime was available, so HTML/page fixtures and JavaScript syntax were checked but not interactive rendering. Phrase associations do not establish causes.
Next bounded task: User decision on accepting the implementation with the disclosed safety deviation; do not run further database or `.env` access.

## Blocker

Exact blocker: The initial ordinary `pytest` command loaded the root conftest, which attempts a PostgreSQL `SELECT 1`, and did not disable import-time dotenv loading. The test output does not establish whether the probe connected or whether `.env` was read.

Evidence: The first worker reported `python -m pytest tests/test_language_analytics.py -v`; the manager also ran an ordinary focused pytest invocation before switching to `PYTHON_DOTENV_DISABLED=1 --confcutdir=/tmp`. Final safe fixture test runs passed (74 tests); no writes, corpus query, deployment, direct `.env` inspection, or modification occurred.

Safe options: Preserve the implementation and let the user accept it with this disclosed deviation, or defer acceptance. No source rollback can undo a read-only probe; do not rerun normal pytest or any command that loads dotenv/root conftest.

Decision required: User acceptance of the implementation despite this unintentional validation-boundary deviation, or defer the task.

## Hypothesis

If phrase extraction uses capped, fixture-fed decisions and document-frequency scoring, focused tests will demonstrate group counts, class denominators, unclassified exclusion, rare-phrase filtering, ranking, and cap reporting without database access.

## Plan

1. Add the phrase analysis service, read-only CLI, API/page surface, and fixture-only tests.
2. Update the evaluation plan, canonical system reference, and API/UI Swimm walkthroughs.
3. Run focused tests, generated-document check, and `git diff --check`; inspect final status and diff.

## Execution Checkpoints

- Delegation: Initial implementation and recovery reports reviewed; manager closed gaps with implementation and tests.
- Implementation: Added bounded service, read-only CLI, page, route registration, and fixture-only test coverage.
- Documentation: Updated evaluation plan, canonical references, generated references, and three Swimm walkthroughs.
- Recovery: No external operation or persistent run state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Scope constrained to issue #155 | User supplied issue requirements and issue #112 safety rules | User task instructions |

## Completion

Completion recorded: no

Summary: Implemented fixture-tested phrase analysis with a read-only capped query, API, standalone page, CLI, required evaluation plan, canonical documentation, and Swimm walkthrough updates. Status remains blocked because the initial standard test invocation attempted the root conftest database probe and may have triggered dotenv loading.

Validation: Focused feature tests (74 passed), feature-tab tests (58 passed, 1 skipped), Python compilation, CLI help, inline JavaScript syntax, generated-document check (3 references current), and `git diff --check` passed. Commands are recorded above.

Residual risk: Clean compliance with the database/`.env` boundary cannot be established for the initial test invocation. No live corpus analysis or browser interaction test was performed.

Next recommended task: User decision on accepting the code with the disclosed safety deviation; do not run further database or `.env` access.
