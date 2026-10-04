# Task: Issue #102 in-process analytics TTL cache

Status: complete
Created: 2026-10-04
Updated: 2026-10-04

## Task Record

Task: Add a configurable, disableable in-process TTL cache for the expensive read-only analytics endpoints identified in the Issue #56 performance review.

Why now: Repeated analytics reads repeat costly aggregation queries; a short freshness window may improve research response time without schema or dependency changes.

Owner surface: Analytics read API (`backend/analytics_service.py`, `backend/routes.py`, and focused API/cache tests).

Commit allowed: yes

Push allowed: yes

Dependencies: Issue #56 query-performance review; existing analytics handlers; no schema or package changes.

Risk boundary: Cache only successful results from the reviewed read-only analytics endpoints; include every normalized query parameter in keys; never alter uncached response behavior; do not access `.env`, a database, or deployment.

Smallest falsifiable check: Focused tests demonstrate distinct normalized-parameter keys, hit/miss, injected-clock expiry, disabled mode, error non-caching, and response parity when disabled.

Acceptance criteria:

- In-process cache defaults to 600 seconds and supports configuration and explicit disablement without a dependency.
- The selected reviewed analytics endpoints return `X-Cache: hit|miss`; errors are not cached.
- Tests cover cache hit/miss, injected-clock expiry, disabled mode, error non-caching, complete parameter keys, and identical disabled-cache behavior.
- Relevant canonical documentation and Swimm walkthrough are updated in the same checkpoint.
- Focused tests, full `python -m pytest -q`, generated-doc check, modified-line secret scan, and parallel validation run when available; report failures honestly.

Harness criteria:

- Focused cache/API acceptance tests pass without database access.
- Full suite and generated-doc check outcomes are recorded.
- Documentation, modified-file secret scan, and final validation evidence are recorded.

Docs/generated references: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/7.7le8istr.sw.md`, and regenerated `docs/API_REFERENCE.generated.md`.

Rollback/recovery: Revert only this task's cache, tests, docs, and task-record edits. No database, schema, or external state changes.

Evidence: The manager delegated the service/routes/tests implementation and a bounded repair to managed workers. The first worker pass reported a post-computation cache probe and no reproducible pytest command; its report also recorded `git checkout` use while undoing its work. The initial worktree was clean before delegation. The manager reviewed and repaired cache status reporting, parameter-key safety, route compatibility, test isolation, bounded capacity, and documentation. Focused cache/API and existing direct-route tests passed (27 passed). The unfiltered `python -m pytest -q` run produced 8 failures, 1,055 passed, 1 skipped, and 1 xfailed: two local PostgreSQL connection attempts were refused, three tests required unavailable network model/tokenizer downloads, one Ollama endpoint expectation differed, and two direct route-call regressions from the initial signature were repaired afterward. No database connection succeeded. The broad offline-safe run passed with 1,057 passed, 1 skipped, 6 deselected, and 1 xfailed. `python scripts/generate_api_reference.py` regenerated the hidden-route reference; `python scripts/check_generated_docs.py` passed (3 references current). `git diff --check`, Python compilation, modified-line secret scan, and new Markdown local-link checks passed. The named `parallel_validation` tool was not exposed; independent validation commands were run concurrently with the available parallel tool. Canonical documentation updated: `SYSTEM_REFERENCE.md` and `CHANGELOG.md`; Swimm walkthroughs updated: `.swm/1.oi7rhqp2.sw.md` and `.swm/7.7le8istr.sw.md`.

Files changed: `.github/project-manager/tasks/issue-102-analytics-ttl-cache.md`, `.github/project-manager/improvements/2026-10-04-delegated-cache-validation-evidence.md`, `backend/analytics_service.py`, `backend/routes.py`, `tests/test_analytics_cache.py`, `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/7.7le8istr.sw.md`, and regenerated `docs/API_REFERENCE.generated.md`.
Delegated work: Managed worker `issue-102-cache` implemented initial cache/tests; `issue-102-cache-repair` addressed the review findings. The manager independently reviewed, corrected, and validated the final slice. No commit or push was made.
Focused validation: `python -m pytest -q tests/test_analytics_cache.py tests/test_feature_tabs.py::test_about_stats_returns_library_counts tests/test_feature_tabs.py::test_judge_profiles_default_to_most_linked_profiles` — 27 passed.
Residual risk: The unfiltered suite remains environment-blocked by failed local DB connection attempts, unavailable external model/tokenizer downloads, and one existing Ollama config expectation. Cache freshness and latency benefit were not measured against a live database. Cache state is process-local by design.
Next bounded task: Measure cache hit rate and endpoint latency against an approved read-only representative environment before claiming a runtime speedup.

## Hypothesis

If caching is correct, focused endpoint tests will demonstrate that identical successful normalized requests hit within 600 seconds, distinct parameter sets miss, expiry/disablement/errors preserve correct behavior, and every response exposes `X-Cache`.

## Plan

1. Delegate the bounded analytics cache implementation and focused tests.
2. Review returned implementation and test evidence; repair only this owner slice if needed.
3. Update canonical docs and Swimm; regenerate API reference from its generator.
4. Run focused tests, broad offline-safe tests, full suite, generated-doc check, secret scan, and final scope review.

## Execution Checkpoints

- Delegation: Two managed-worker slices completed; manager review found and repaired first-miss reporting, env configuration/test gaps, parameter normalization collisions, and legacy direct-route signature compatibility.
- Implementation: `backend/analytics_service.py`, `backend/routes.py`, and `tests/test_analytics_cache.py`; focused acceptance and direct-call compatibility tests passed.
- Documentation: `SYSTEM_REFERENCE.md`, `CHANGELOG.md`, `.swm/1.oi7rhqp2.sw.md`, `.swm/7.7le8istr.sw.md`; `docs/API_REFERENCE.generated.md` regenerated from `scripts/generate_api_reference.py`.
- Recovery: No external state changed. Initial worktree was clean; no user changes were present to recover.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-04 | Task created | User requested issue #102; performance review identifies expensive read-only analytics aggregations | `docs/reports/query-performance-review.md`; worktree initially clean |
| 2026-10-04 | Cache only the three review-backed endpoint reads | Keep scope tied to measured review candidates; preserve original payload shape and add explicit cache status | Focused tests and source review |

## Completion

Completion recorded: yes

Summary: Added bounded process-local TTL caching for About statistics, FC activity analytics, and the Judge Profile list with environment configuration, complete request parameter keys, expiry, clear helper, and `X-Cache` response status.

Validation: Focused test slice passed (27 passed); broad offline-safe suite passed (1,057 passed, 1 skipped, 6 deselected, 1 xfailed); generated-doc check and modified-line secret scan passed. The unfiltered full suite was attempted and its environment-dependent failures are recorded above. `python scripts/generate_api_reference.py`, `git diff --check`, and Python compilation passed.

Residual risk: No live latency/freshness measurements; unfiltered test failures require database/network/configuration support.

Next recommended task: Measure cache hit rate and endpoint latency in an approved read-only representative environment.
