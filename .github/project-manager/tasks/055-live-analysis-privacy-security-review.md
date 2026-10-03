# Task: Live Analysis Privacy And Security Review

Status: completed
Created: 2026-10-03
Updated: 2026-10-03

## Task Record

Task: Deliver issue #55's privacy/security review of live-analysis uploads and de-identification, and fix only clear, small issues.

Why now: Uploaded legal text can contain sensitive personal information; users need an evidence-backed account of storage, caching, external processing, parser limits, and redaction limitations.

Owner surface: Live Analysis uploaded-document privacy boundary (`/live-analysis` and its in-memory parsing/resolution path).

Commit allowed: yes

Push allowed: yes

Dependencies: Existing live-analysis and de-identification handlers, focused API tests, and the backend/system-map walkthrough.

Risk boundary: Preserve ephemeral processing, local read-only resolution, existing API payloads, parser/de-identification behavior, source offsets, and all unrelated worktree changes. No broad redesign or unsupported security claims.

Smallest falsifiable check: `python -m pytest -q tests/test_live_analysis.py tests/test_deidentify.py`

Acceptance criteria:

- Publish `docs/reports/privacy-security-review.md` covering the requested data-flow, hostile-file, limits, and de-identification questions with evidence and residual risks.
- Add focused cache-control hardening only if evidence confirms a clear gap, without changing response payloads or parsing behavior.
- Update `SYSTEM_REFERENCE.md` and the relevant Swimm walkthrough in the same checkpoint.
- Run the focused tests and documentation/link/diff checks; scan changed files for secrets before commit.

Harness criteria:
- Review and documentation accurately distinguish observed behavior from unverified deployment controls.
- The live-analysis response is not cacheable by HTTP caches.
- Focused tests pass and required repository documentation paths are updated.

Docs/generated references: `docs/reports/privacy-security-review.md`, `SYSTEM_REFERENCE.md`, `.swm/1.oi7rhqp2.sw.md`; no generated documents.

Rollback/recovery: Revert only the small cache-header/test edits if they cause a regression; documentation can be corrected independently. No data migration or persistent upload artifact is involved.

Evidence: Security-review specialist found missing no-store response headers on Live Analysis and no other newly exploitable in-scope issue; it also flagged the pre-existing unenforced login middleware as a deployment caveat. Managed worker added route headers and a focused test. Manager restored the explicit `LiveAnalysisResponse` OpenAPI contract and expanded coverage to both upload POST routes. Focused tests passed: `python -m pytest -q tests/test_live_analysis.py tests/test_deidentify.py` (22 passed, one upstream deprecation warning). `python scripts/check_generated_docs.py` passed (3 references checked); local documentation links passed; `python -m py_compile backend/routes.py`, `git diff --check`, and the changed-file secret scan passed. The published review includes severity, file/line references, and suggested remediation for each finding. Canonical report: `docs/reports/privacy-security-review.md`; system reference: `SYSTEM_REFERENCE.md`; Swimm walkthrough: `.swm/1.oi7rhqp2.sw.md`.

Files changed: `backend/routes.py`, `tests/test_live_analysis.py`, `docs/reports/privacy-security-review.md`, `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `.swm/1.oi7rhqp2.sw.md`, this task record.
Delegated work: Security-review specialist completed a read-only scoped assessment; managed worker added no-store headers and initial API coverage. Both returned the required structured report. Manager reviewed and retained response-model schema validation.
Focused validation: `python -m pytest -q tests/test_live_analysis.py tests/test_deidentify.py` — 22 passed, one upstream Starlette deprecation warning.
Residual risk: Multipart reads precede the 10 MiB check; expanded DOCX/PDF processing and pasted text are not comprehensively resource-bounded. App middleware does not enforce its apparent login; deployment access control requires separate verification. No hostile-file fuzzing, browser/proxy retention audit, or full suite run.
Next bounded task: Separately verify deployment access control and scope a resource-limit hardening task.

## Hypothesis

If live-analysis responses carry `Cache-Control: no-store` and the review is accurate, focused API tests will demonstrate non-cacheable upload results while source inspection documents ephemeral handling and parser/de-identification limits without changing extraction or response data.

## Plan

1. Read the authoritative behavior and relevant walkthrough; consume both specialist reports.
2. Accept the bounded cache-header/test change and synthesize the audit report.
3. Update the canonical documentation and Swimm walkthrough, then run focused validation and final safety checks.

## Execution Checkpoints

- Delegation: Security-review specialist completed read-only exploitability pass; managed worker changed only the Live Analysis routes and focused test.
- Implementation: `backend/routes.py` adds response cache headers while retaining response-model validation; `tests/test_live_analysis.py` verifies both POST routes.
- Documentation: `docs/reports/privacy-security-review.md`, `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, and `.swm/1.oi7rhqp2.sw.md`.
- Recovery: No long-running operation or persistent run state.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Selected Live Analysis uploaded-document privacy boundary | It owns ephemeral uploaded-text parsing and local resolution, and directly addresses issue #55 | `SYSTEM_REFERENCE.md` route table and `.swm/1.oi7rhqp2.sw.md` Live Analysis boundary |
| 2026-10-03 | Limit implementation to response no-store headers | Clear fix does not require changing parsing, storage, or access-control policy | Security-review finding; focused route test |

## Completion

Completion recorded: yes

Summary: Scoped privacy/security report delivered; Live Analysis success responses made non-cacheable without changing their validated payload contract.

Validation: `python -m pytest -q tests/test_live_analysis.py tests/test_deidentify.py` passed 22 tests with one upstream deprecation warning.

Residual risk: See the report and task evidence; hostile-file fuzzing, full-suite validation, and deployment access-control verification were not run.

Next recommended task: Separately investigate deployed access controls before exposing these routes.
