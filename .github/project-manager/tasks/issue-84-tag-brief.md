# Task: Add printable legal issue/tag brief

Status: blocked
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Implement `GET /issue-brief?tag=<tag>` JSON and `/issue-brief-ui` printable one-page brief for a legal tag.

Why now: Issue #84 requests a compact, traceable view of decisions and authorities associated with a legal issue tag.

Owner surface: API and research UI (`backend/routes.py`, its existing analytics/page-builder boundaries, and focused API tests).

Commit allowed: no

Push allowed: no

Dependencies: Existing case/tag/outcome/citation data and reusable analytics queries; no schema change or database-only feature.

Risk boundary: Read-only aggregation only. Preserve separate tag, outcome, and citation layers; keep per-case links traceable; do not let percentages obscure unclassified records or their denominator; support an empty tag without failure.

Smallest falsifiable check: `python -m pytest -q tests/test_issue_brief.py`

Acceptance criteria:

- JSON route returns decisions per year, outcome splits, top 10 cited authorities, courts, and links to tagged cases; an empty tag has a valid empty response.
- Each outcome percentage is visibly paired with the unclassified count and denominator.
- Printable UI route uses compact print CSS, shows at most 12 tagged decision links with a shown/total disclosure, and leaves the complete decision list in JSON; no new dependencies or database-only features.
- SQLite fixture tests cover the API/UI contracts and empty-tag behavior.
- Focused tests pass; canonical repository documentation and the relevant Swimm walkthrough are updated.

Harness criteria:
- `issue_brief_json_contract`
- `issue_brief_printable_ui`
- `issue_brief_empty_tag`
- `issue_brief_docs_and_swimm`

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `CHANGELOG.md`, and generated `docs/API_REFERENCE.generated.md`; Swimm walkthroughs `.swm/1.oi7rhqp2.sw.md` and `.swm/6.maiixtsw.sw.md`.

Rollback/recovery: Remove the additive routes/page builder/tests and revert only the related documentation changes; no persistent data or schema is modified.

Evidence: The managed worker added the JSON/UI routes, analytics aggregation, SQLite contract tests, and documentation. The printable page is bounded to 12 links with a shown/total disclosure; its JSON payload remains complete. The worker updated `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, and `.swm/6.maiixtsw.sw.md`. Manager checks reported that `python -m py_compile backend/analytics_service.py backend/pages/issue_brief.py backend/routes.py tests/test_issue_brief.py && git diff --check` and standalone printable renderer assertions passed. Coordinator review found no Code Review findings and CodeQL reported zero alerts. The API reference was regenerated successfully with `python scripts/generate_api_reference.py` after installing existing runtime packages in the sandbox. Focused pytest execution was not performed; pytest remains unavailable.

Files changed: `.github/project-manager/tasks/issue-84-tag-brief.md`, `backend/routes.py`, `backend/analytics_service.py`, `backend/pages/issue_brief.py`, `tests/test_issue_brief.py`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `docs/API_REFERENCE.generated.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/6.maiixtsw.sw.md`.
Delegated work: `managed-worker` implemented routes, reusable analytics-service aggregation, page builder, SQLite tests, and docs; a bounded managed-worker follow-up capped printed case links at 12 and added shown/total disclosure. Both returned the required structured reports. Neither committed or pushed.
Focused validation: `python -m pytest -q tests/test_issue_brief.py` — not run (`pytest` unavailable); manager-reported `python -m py_compile backend/analytics_service.py backend/pages/issue_brief.py backend/routes.py tests/test_issue_brief.py && git diff --check` — passed; manager-reported standalone print-renderer assertions for 12-link cap, disclosure, and print CSS — passed; `python scripts/generate_api_reference.py` — passed and updated the generated route reference.
Residual risk: SQLite/API behavior has not been executed. No browser or physical-print validation was performed.
Next bounded task: Run the focused SQLite tests and CI test command in a test-enabled environment, then perform browser/print acceptance.

## Hypothesis

If the additive issue-brief routes reuse existing read-only analytics over tagged cases, the focused SQLite API tests will demonstrate complete, traceable year/outcome/court/authority results—including explicit unclassified counts and denominators—and a safe empty-tag state.

## Plan

1. Assign one bounded API/research-UI implementation slice to a managed worker.
2. Review the returned implementation and verify its focused tests and documentation checkpoint.
3. Record manager-owned acceptance evidence; do not commit or push.

## Execution Checkpoints

- Delegation: Managed worker implementation and bounded print-layout follow-up completed; exact structured summaries are recorded in Evidence.
- Implementation: Worker changed the stated API/research-UI owner slice; coordinator made no implementation edits.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, generated `docs/API_REFERENCE.generated.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, and `.swm/6.maiixtsw.sw.md` updated.
- Recovery: No database or long-running operation expected.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Select API/research UI as the sole owner surface | Both requested routes are additive research-facing contracts and should share existing analytics | `SYSTEM_REFERENCE.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/6.maiixtsw.sw.md` |
| 2026-10-03 | Block completion pending focused behavioral tests | SQLite API behavior still needs test execution; generated reference is now current | Focused pytest was not run; `scripts/generate_api_reference.py` passed |

## Completion

Completion recorded: no

Summary: Implementation, canonical/Swimm docs, and generated API reference are present, but completion remains blocked pending behavioral tests.

Validation: Manager-reported Python compilation, `git diff --check`, and standalone renderer assertions passed. API-reference generation passed after installing declared runtime dependencies; focused pytest was not run because pytest is unavailable.

Residual risk: API/SQLite runtime behavior remains unverified; no browser or physical-print validation occurred.

Next recommended task: Run focused and CI tests plus browser/print acceptance in an environment with pytest installed, then complete final acceptance.
