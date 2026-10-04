# Task: Offline read-endpoint performance pass

Status: blocked
Created: 2026-10-04
Updated: 2026-10-04

Task: Implement issue #138 with offline statement-count and response-parity evidence.
Why now: Remove avoidable research-read round trips without changing evidence or JSON.
Owner surface: Backend research read services and their offline regression tests.
Commit allowed: yes
Push allowed: no
Dependencies: Existing PR108 analytics cache, isolated SQLite fixtures, CI exclusions.
Risk boundary: No application/external DB, dotenv files, credentials, deployment, other branches, new dependencies, or migrations. Preserve response contracts and ordering.
Smallest falsifiable check: Offline pytest of endpoint-performance tests with 5/50-row fixtures and cold sessions; constant query ceilings and equality must pass.
Acceptance criteria:
- Measure requested endpoint families before/after on current code only.
- Reduce evidenced N+1 queries without truncating existing responses.
- Add reusable SQLAlchemy statement counter and exact equality regressions.
- Update requested reports, canonical SYSTEM_REFERENCE.md and existing Swimm.
- Run focused tests, CI-equivalent full suite, generated docs check, and precommit secret scan; report limitations honestly.
Docs/generated references: docs/reports/query-performance-review.md; docs/reports/endpoint-performance-pass.md; docs/proposed-migrations/indexes.py.txt; SYSTEM_REFERENCE.md; .swm/1.oi7rhqp2.sw.md; .swm/5.b49ftjal.sw.md; generated references only through their generators.
Rollback/recovery: Revert this task's local commit only; no data/schema changes.
Evidence: Required references and exact CI exclusions read; initially clean worktree. Report docs/reports/endpoint-performance-pass.md contains 5/50-row before/after counts, successful JSON parity and explicit pre-existing failure exceptions. Updated canonical SYSTEM_REFERENCE.md, query-performance-review.md, index draft and .swm/1.oi7rhqp2.sw.md, .swm/5.b49ftjal.sw.md, .swm/6.maiixtsw.sw.md, .swm/7.7le8istr.sw.md in this checkpoint. Generated catalog regenerated from source; checker passes all 3 references. Compilation and git diff --check passed. gh issue retrieval unavailable without authentication; no credentials accessed. report_progress/parallel_validation tools unavailable; chat checklists and independent postcommit validation are substitutes.
Delegated work: managed-worker read-endpoint-inventory (20-file read-only inventory), analytics-read-performance, reader-read-performance, citation-read-performance, fc-read-performance, fc-summary-measurements; all returned required structured evidence. code-review performance-diff-review found no backend parity issue, but guard bypass; manager fixed raw/direct connection paths and added rejection tests.
Focused validation: /tmp/caselibrary-tests/bin/python scripts/run_offline_tests.py -q tests/test_offline_test_runner.py tests/test_endpoint_performance_analytics.py tests/test_endpoint_performance_citations.py tests/test_endpoint_performance_fc.py tests/test_endpoint_performance_fc_summaries.py tests/test_endpoint_performance_reader.py tests/test_analytics_cache.py tests/test_issue_brief.py tests/test_fc_activity_insights.py tests/test_fc_activity_motions.py tests/test_reader_service.py tests/test_reader_tag_occurrences.py tests/test_search_matching.py tests/test_judge_profiles.py tests/test_judge_influence.py — 508 passed, 2 warnings in 46.97s.
Residual risk: Full CI-deselect suite: 1590 passed, 3 failed, 2 skipped, 3 deselected, 1 xfailed, 7 warnings in 143.49s; 74% coverage. Unmocked model-provider test requires unavailable sentence-transformers; two tokenizer tests require unavailable cached tokenizer data (DNS fetch failed). Not hidden with extra deselects. PostgreSQL plans/latency and many advanced map routes unmeasured.
Next bounded task: Repair model-provider test mocking and offline tokenizer resources, rerun full CI-deselect suite.
Files changed: Five backend read modules; reusable counter and five performance test modules; offline runner/guard tests; generated-doc checker/catalog generator and generated catalog; requested reports/index draft; canonical SYSTEM_REFERENCE.md; four existing Swimm walkthroughs; this task record. See git commit for exact paths.

## Hypothesis

Batching repeated read lookups and narrowing unused selected columns will preserve JSON while keeping SQL statement counts constant between 5 and 50 related rows.

## Execution checkpoints

- Planning: User requested no extra planning documents; this single required manager task record contains working state, not a separate plan.
- Safety: Block dotenv loading and non-offline connections before importing application modules in validation.
- Implementation: Query batching/projections and bounded FC cache; focused 508 tests passed.
- Recovery: Installed existing requirements in /tmp/caselibrary-tests; fixed guard coverage/read-only disposable URI handling; no app DB access.
- Full validation: Exact CI deselects, no extras; 3 unrelated external-resource/mocking failures block green acceptance.
- Improvement loop: Added evidence-backed offline-preflight recommendation to the existing improvements/README.md; no extra planning document or instruction edit. Whole-document link review found two pre-existing canonical links; introduced-link validation required before commit.
- Commit decision: Local qualified implementation/report commit allowed; no push. Precommit fresh validation and scoped secret scan required. Independent postcommit results returned to caller.
- Precommit scan/link evidence: 26 staged files, zero secret-pattern flags; 18 introduced local links, zero missing. Final edit followed by fresh focused/generated/whitespace validation and repeat scan before commit.
- Status: blocked, not claimed complete.

## Completion

Completion recorded: no
Summary: Implementation and offline measurements delivered; full-suite acceptance blocked.
Decision required: Separate test-owner repair/offline tokenizer provision, not model downloads or additional deselects concealed as success.
Safe options: Accept the measured bounded changes with explicit blocker, or hold merge until the exact full-suite run passes.
