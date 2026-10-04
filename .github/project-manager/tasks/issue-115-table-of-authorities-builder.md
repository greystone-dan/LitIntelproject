# Task: Build ephemeral DOCX Table of Authorities

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Close the acceptance gap where nonblank, unrecognized paste lines were
silently omitted from the Table of Authorities DOCX.

Why now: Let researchers turn draft legal submissions into a traceable,
court-grouped authority list without adding private draft text to the case
library.

Owner surface: Ephemeral Table of Authorities feature under `backend/`,
including its route/page integration and focused tests.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing local case metadata/citation resolution, page builders,
and `python-docx`; no schema, database writes, deployment, or dependency changes.

Risk boundary: Accept at most 200 nonblank input lines and clearly reject
overflow; never persist or log pasted content; only resolve against local
records and emit external CanLII links for known authorities; preserve existing
routes and UI.

Smallest falsifiable check: `python -m pytest tests/test_table_of_authorities.py -q`

Acceptance criteria:

- `POST /table-of-authorities` accepts JSON with one case ID or citation per
  line and returns a DOCX.
- Existing `GET /table-of-authorities` UI and
  `POST /table-of-authorities/build` form contract remain unchanged.
- Numeric case-ID lines resolve against local records; citation lines continue
  to resolve independently, and missing IDs/citations remain explicit.
- Every nonblank line that is neither a positive case ID nor an extracted
  citation appears as an unresolved item; blank lines are ignored.
- Parser extracts citations and paragraph references, groups by court in a
  documented order, and alphabetizes authorities within each court.
- Resolver reports unmatched authorities explicitly and provides CanLII-style
  links only when a known identifier supports the link.
- The DOCX and UI make resolution, not-found entries, citations, and paragraph
  references clear; input is never persisted or logged.
- Focused parser/resolver/API/DOCX tests and requested repository validations
  pass, or limitations are recorded with evidence.

Harness criteria: `Unparseable authority text` appears in the DOCX not-found
section; blank-only lines do not create entries; existing ID/citation and
200-line behavior remains.

Docs/generated references: Updated `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and
`.swm/6.maiixtsw.sw.md` to clarify that unrecognized nonblank lines are retained;
`scripts/check_generated_docs.py` confirms no API/schema regeneration was needed.

Rollback/recovery: Revert the feature module, route/page integration, tests, and
the two documentation updates together; no stored data or migration requires
recovery.

Evidence: Original JSON/ID implementation and this follow-up are complete. The
parser now retains any nonblank line with no extracted case citation or positive
case ID, so the existing resolver places it in the DOCX not-found section.
Blank-only input creates no item. The prior implementation added the
parser/resolver, GET page, POST DOCX route, and fixture-backed tests. Manager
verification found and fixed a CanLII URL path
pattern mismatch, then made the route query citation-matched metadata instead of
loading every case row. The focused suite passed 10 tests; UI feature-tab tests
passed 56 with one skipped. Headless Chromium confirmed that a 201-line paste is
rejected in the UI before a fetch. Generated references are current. Canonical
documentation updated at `SYSTEM_REFERENCE.md` and `CHANGELOG.md`; Swimm
walkthrough updated at `.swm/6.maiixtsw.sw.md`.

Files changed: `.github/project-manager/tasks/issue-115-table-of-authorities-builder.md`,
`backend/models.py`, `backend/routes.py`, `backend/table_of_authorities.py`,
`backend/pages/table_of_authorities.py`, `tests/test_table_of_authorities.py`,
`SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/6.maiixtsw.sw.md`, and regenerated
`docs/API_REFERENCE.generated.md`.
Delegated work: Managed-worker `toa-backend` implemented the original builder,
parser/resolver, routes, and tests. Managed-worker `toa-json-ids` added the JSON
request contract, numeric ID extraction/resolution, filtered ID query, and
compatibility tests. Both returned the required structured reports; neither
accessed a database or edited documentation. Manager review added an explicit
binary DOCX OpenAPI response and contract assertion, and normalized indentation
in the parser module.
Focused validation: `/tmp/caselibrary-issue115-venv/bin/python -m pytest tests/test_table_of_authorities.py -q` — 17 passed. The focused DOCX regression confirms `Unparseable authority text` is under the not-found heading and blank lines are ignored. `scripts/check_generated_docs.py` — 3 references current. Python compilation, `git diff --check`, and modified-file secret-pattern scan passed. The local-link scan found only the two previously recorded, unchanged broken links in `SYSTEM_REFERENCE.md`; the updated Swimm/changelog links passed. Earlier Chromium smoke confirmed the 201-line UI rejection.
Residual risk: The CI-deselected full suite collected and ran but ended with
1,261 passed, 3 failed, 2 skipped, 1 xfailed, and 3 deselected. Failures were
`tests/test_api.py::test_local_chunk_search_uses_requested_model` (missing
`sentence_transformers`) and two `tests/test_openai_chunk_embeddings.py` tests
(missing `tiktoken`) in the isolated temporary environment. No production
database or live API was accessed. The browser check used Chromium with the
generated page rather than a live server. A repository-wide local-link check
also found two existing, unchanged `SYSTEM_REFERENCE.md` links with wrong
relative paths (`ANALYST_QUICK_START.md` and `reports/test-coverage.md`); the
feature documentation links are valid. `engine-tools-report_progress` and
`parallel_validation` were not available in this session; progress was reported
in chat and independent checks were run with `multi_tool_use.parallel`.
Next bounded task: Run required PR validation in the fully provisioned CI
environment.

## Hypothesis

If an unrecognized nonblank line is preserved, the focused DOCX test will find
its exact text in the not-found section while blank-only input creates no
not-found entry.

## Plan

1. Preserve original text as an unresolved citation-like row when a nonblank
   line yields no citation and is not a positive case ID.
2. Add a fixture-backed DOCX test for unknown text and blank-line handling.
3. Update canonical docs and Swimm, then rerun the focused tests and safety checks.

## Execution Checkpoints

- Delegation: Managed-workers `toa-backend` and `toa-json-ids` returned required
  structured reports.
- Implementation: Complete; unrecognized nonblank lines are retained in the
  not-found section and blank lines are ignored.
- Documentation: Updated `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, and
  `.swm/6.maiixtsw.sw.md`; generated-reference check passed.
- Recovery: None required; no database or long-running operation.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Require a stateless POST-to-DOCX flow and a GET UI route | Avoid retaining pasted draft submissions while satisfying the requested routes | Issue request; system reference and Swimm walkthrough establish ephemeral analysis precedent |

## Completion

Completion recorded: yes

Summary: Shipped ephemeral form and JSON DOCX builders. Inputs accept one
positive local case ID or citation per line; all unrecognized nonblank lines are
preserved in the not-found section. Resolved authorities are grouped and
alphabetized, with citations, paragraph references, and validated CanLII links
represented in the DOCX.

Validation: Focused TOA tests (17 passed), UI regression tests (56 passed, 1
skipped), generated-doc check, Python compilation, diff check, and modified-file
secret scan passed. OpenAPI tests confirm JSON input and DOCX response media
types. Full-suite limitations from the initial checkpoint are recorded above;
the full suite was not rerun for the review follow-ups.

Residual risk: Full-suite failures from the earlier run are attributable to
declared embedding packages missing from the isolated environment. No live
database was accessed; required PR validation remains with the reviewer.

Next recommended task: Run the documented CI-deselected suite in the fully
provisioned CI environment.
