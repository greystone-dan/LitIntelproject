# Task: Outcome-aware saved-search alerts

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Implement issue #156 outcome-aware alerts for existing saved searches, including decision outcomes, authority-treatment comparisons, JSON and plain-page access, and offline scheduling support.

Why now: The current saved-search feature records matches but does not explain outcomes or show how cited authorities are treated over time.

Owner surface: Saved-search outcome alerts (`backend/outcome_alerts.py`, `backend/outcome_alert_routes.py`), with minimal registration in `backend/routes.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing saved-search models/routes and outcome/citation fields on `main`; no dependency on open PR #129.

Risk boundary: Use only code on `main`; do not access a database, deploy scripts, `.env`, or credentials. Do not add dependencies, migrations, deletions, or unrelated feature changes. Keep `routes.py` and `main.py` edits to minimal registration lines. Do not infer causal authority treatment or report underpowered windows.

Smallest falsifiable check: `python -m pytest tests/test_outcome_alerts.py -q`

Acceptance criteria:

- A new `backend/outcome_alerts.py` computes saved-search matches since a caller-supplied date with stored outcome and a concise, evidence-based match reason.
- The authority watch aggregates cited authorities represented in saved-search results; compares Minister outcomes in consecutive 12-month windows, returns both counts and denominators, and suppresses comparisons when either denominator is below 8.
- Adequately sized windows report signed percentage-point movement and mark `declining` when the Minister-loss share rises by at least 15 points.
- `GET /saved-searches/{id}/alerts` returns the computed JSON; a plain page exposes the same information without changing existing saved-search behavior.
- `scripts/build_outcome_alerts.py` supports bounded, offline use of the shared alert logic.
- Fixture tests cover matching, outcome/reason, both authority windows and denominators, minimum-count suppression, and route/page contract as feasible without database access.
- A short operator document explains how Daniel's PC can schedule the offline script without exposing credentials.
- Relevant canonical documentation and Swimm walkthrough are updated; generated references are refreshed from their generator.
- Focused tests, documentation check, diff/secret review are run and recorded; no deployment or database access occurs.

Harness criteria: None; no managed run is being used.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, a short outcome-alert scheduling document, `.swm/1.oi7rhqp2.sw.md`, and regenerated API/script references where the generator detects changes.

Rollback/recovery: Revert only this feature's additive module, registrations, script, tests, and documentation. No schema or canonical data changes are involved.

Evidence: The managed worker inspected the current-main `SavedSearch`, `SearchAlert`, `Citation`, and `CaseOutcome` contracts and implemented the initial feature slice; the manager reviewed and corrected the evidence paths and final route/docs. `python -m py_compile backend/outcome_alerts.py backend/outcome_alert_routes.py backend/routes.py scripts/build_outcome_alerts.py tests/test_outcome_alerts.py` passed. Direct invocation of three focused fixture/calendar/CLI test functions passed. `python scripts/build_outcome_alerts.py --help` and `python scripts/generate_script_catalog.py` passed. `python -m pytest -q tests/test_outcome_alerts.py` failed because pytest is unavailable. `python scripts/check_generated_docs.py` failed because FastAPI and SQLAlchemy are unavailable to the API/schema generators; API reference regeneration remains blocked. Focused links in `DOCS_INDEX.md`, `docs/outcome_alerts.md`, and `.swm/1.oi7rhqp2.sw.md` resolve; two unrelated broken links in `SYSTEM_REFERENCE.md` are present in the base revision. `git diff HEAD --check` passed and changed-file high-confidence secret scan found no matches. Canonical documentation updated: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`; Swimm walkthrough updated: `.swm/1.oi7rhqp2.sw.md`.

Files changed: `.github/project-manager/tasks/outcome-aware-alerts-156.md`, `.swm/1.oi7rhqp2.sw.md`, `CHANGELOG.md`, `DOCS_INDEX.md`, `SYSTEM_REFERENCE.md`, `backend/outcome_alert_routes.py`, `backend/outcome_alerts.py`, `backend/pages/saved_search_alerts.py`, `backend/routes.py`, `docs/SCRIPT_CATALOG.generated.md`, `docs/operators/schedule_outcome_alerts.md`, `docs/outcome_alerts.md`, `scripts/build_outcome_alerts.py`, and `tests/test_outcome_alerts.py`. `backend/main.py` was not changed because it already registers the parent router.
Delegated work: Managed worker completed two bounded passes over current-main contracts, feature implementation, and fixture tests. Manager review corrected the authority cohort/date semantics, kept result decisions in the citing cohorts, moved handlers behind a registered router, completed the Swimm/canonical documentation checkpoint, and performed final validation.
Focused validation before the review corrections: `python -m py_compile backend/outcome_alerts.py backend/outcome_alert_routes.py backend/routes.py scripts/build_outcome_alerts.py tests/test_outcome_alerts.py` passed; three fixture/calendar/CLI checks directly invoked from `tests/test_outcome_alerts.py` passed; `python scripts/build_outcome_alerts.py --help`, `python scripts/generate_script_catalog.py`, focused new-doc link review, `git diff HEAD --check`, and changed-file secret-pattern scan passed. Review corrections then added the 15-point signal and aligned fixture outcome/timestamp fields; those corrections were inspected but tests were not rerun. `python -m pytest -q tests/test_outcome_alerts.py` could not run (`No module named pytest`). `python scripts/check_generated_docs.py` failed because `fastapi` and `sqlalchemy` are unavailable, so the generated API reference could not be refreshed.
Residual risk: The feature routes have not received pytest/FastAPI or database-backed integration validation (database access was explicitly prohibited). `docs/API_REFERENCE.generated.md` remains unrefreshed until the generator can run. Authority comparisons are descriptive; all citing decisions form the denominator, including those without stored outcomes.
Next bounded task: In an existing project environment with the declared dependencies, run the focused pytest and generated-doc checks, regenerate `docs/API_REFERENCE.generated.md`, and review the generated diff; do not connect to a database or deploy.

## Hypothesis

If the shared alert calculation consumes existing saved-search and decision evidence without writing data, fixtures will show recent matching outcomes/reasons and correctly bounded, denominator-qualified authority comparisons, and the API and offline paths will expose the same computed contract.

## Plan

1. Verify current-main saved-search, outcome, citation, and route contracts without database access.
2. Implement a dedicated alert calculation module, minimal route/app registration, offline script, and fixture tests.
3. Update operator/canonical/Swimm documentation, regenerate derived references, and validate the focused feature plus documentation and diff safety.

## Execution Checkpoints

- Delegation: Managed worker completed initial and repair passes; manager independently accepted/repaired the final implementation and documentation.
- Implementation: Shared pure calculations, read-only DB-backed query, separate API router, plain HTML page, offline JSON builder, and fixture coverage are present. `backend/routes.py` has only a route-router import and include line; `backend/main.py` is unchanged.
- Documentation: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `DOCS_INDEX.md`, `docs/outcome_alerts.md`, `docs/operators/schedule_outcome_alerts.md`, `.swm/1.oi7rhqp2.sw.md`, and generated `docs/SCRIPT_CATALOG.generated.md` updated. API-reference regeneration is blocked by missing packages.
- Recovery: No data or run-state artifacts.

## Solution Evaluation

| Approach | Accuracy / explainability | Runtime and operations | Maintenance / ownership | Decision |
| --- | --- | --- | --- | --- |
| Put all query and aggregation logic in `backend/routes.py` and duplicate CLI logic | Could use stored evidence, but route and offline rules could drift; low explanation reuse | Fewer files initially, but each request does live citation aggregation | Couples calculation to the large route module and duplicates logic | Rejected |
| Shared pure calculation module, thin API router, and offline JSON input | Same match/outcome/denominator rules can be fixture-tested and reused; source citation targets and windows remain explicit | Bounded to recorded matches and citing decisions in the two windows; offline file preparation stays an explicit operation | Separates query orchestration and pure calculation without changing schema or startup ownership | Chosen |
| Persist periodic authority-watch snapshots with new tables | Can make later reads fast, but adds freshness/version questions and another derived layer | Requires a migration and scheduled writer | Higher operational ownership and rollback burden; prohibited for this issue | Rejected |

The smallest disconfirming experiment is a fixture with independent 8-decision
boundaries, both sides of the 15-point decline threshold, and distinct
authorities, followed by the shared offline CLI. The original fixture passed by
direct invocation; the review-correction fixture was inspected but not rerun
because pytest is unavailable and completed managed-agent changes are not
retested.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Use a dedicated shared calculation module and keep route/app changes to registration | Avoid coupling outcome logic to the large route module; reuse one calculation for API and offline scheduling | User constraint; current route walkthrough `.swm/1.oi7rhqp2.sw.md` |
| 2026-10-04 | Reject adding schema-backed alert state or depending on PR #129 | Issue permits use of existing mainline saved-search contracts only and no migrations | User constraint |
| 2026-10-04 | Treat authority trends as descriptive and suppress either window below 8 decisions | Prevent overclaiming from small denominators; keep counts and denominators visible | User acceptance criteria |
| 2026-10-04 | Require resolved citation edges from alert-result decisions to seed authority watch, then count corpus decisions citing those targets | `Case.cases_cited` plus alert-case dates does not establish who cited a watched authority and gives the wrong denominators | Manager review of `Citation`, `Case`, and `CaseOutcome` ORM contracts |
| 2026-10-04 | Choose a shared pure calculation plus thin API router and JSON-file CLI over inline route logic or persisted alert snapshots | It reuses one transparent rule set for live reads and offline snapshots without duplicating computation, while avoiding schema/deployment cost and stale persisted aggregates; query cost is bounded to matched results and two date windows | Fixture cases verify exact resolved authorities, source-decision windows, numerator/denominator, and both suppression boundaries |

## Completion

Completion recorded: no; blocked pending dependency-enabled test and generated API-reference checks

Summary: Feature code and canonical/Swimm documentation are implemented, but required pytest and generated API-reference validation could not run in this environment.

Validation: Three focused fixture/calendar/CLI checks passed by direct invocation before review corrections; changed Python compiled; offline CLI help worked; script catalog generated; focused new-document links, secret-pattern scan, and combined diff check passed. The 15-point threshold and API/offline parity corrections were inspected but not tested. Pytest and generated-doc checks could not run because the runtime packages are unavailable.

Residual risk: No FastAPI route integration or database-backed execution was tested, and the generated API reference is not refreshed. No database or deployment was used.

Next recommended task: Re-run focused pytest and `scripts/check_generated_docs.py` in an existing dependency-enabled project environment, then update generated references and re-review the diff.
