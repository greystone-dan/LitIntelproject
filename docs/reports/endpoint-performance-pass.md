# Read-endpoint performance pass — issue #138

Reviewed: 2026-10-04. Base checkout: `28b86c9`, current main-derived code only.

Before: several research reads issued another SQL statement for every judge,
linked decision, authority or candidate; FC insights scanned duration data six
times, and its process-local cache could grow without an entry limit.

After: batched reads preserve successful response JSON, sorting and evidence
offsets; FC insights performs one duration scan and uses a 256-entry LRU bound.
The existing PR108 analytics cache keys, TTL policy and `X-Cache` behavior are
retained. Only disposable test databases were used; no application database,
migration or deployment operation was performed.

## Method and measurement boundary

Started from [the source-only review](query-performance-review.md), existing
offline fixtures and current cache code, not another branch. New fixtures use
SQLAlchemy SQLite `:memory:` engines with 5 and 50 related rows/distinct targets
and fresh Sessions. `tests/performance_helpers.py` attaches a reusable
`before_cursor_execute` listener only around each request; setup is excluded and
the listener is removed in `finally`. The counter records every executed
statement, not just SELECTs. Regressions enforce fixed statement ceilings
(some assert exact equality), rather than elapsed-time thresholds.

Workers recorded counts before editing their owned services, then used complete
decoded JSON equality against pre-edit/independent fixture oracles. Edge coverage
includes repeated/unresolved references, missing metrics, ties, pre-limit context
deduplication, Minister/filter variants, cache expiry, empty slices, statute
versions and unchanged source offsets. Projection assertions detect unused
body/HTML/vector columns. Fixtures and oracles live in
`tests/test_endpoint_performance_{analytics,citations,fc,fc_summaries,reader}.py`.

Citation-family counts below include HTTP/router existence checks. Other
families measure the named route's service call, not HTTP serialization/startup.
Existing cache-header/API regression tests were also run. Cold and disabled
cache requests are measured independently of warm hits.

The active analytics search uses PostgreSQL textual SQL: its **empty-query**
fixture adapts SUBSTRING syntax and the empty-query label for SQLite. This
checks limits/projection/JSON, not native PostgreSQL ranking or query plans.
After merging PR #127's query syntax, the independent search oracle includes
the real `query_echo` field (including `(empty query)`); it does not discard
response fields. Empty search and `court:FC` / `NOT court:FC` still execute
exactly **1 / 1** statements with 5 / 50 related rows, at both tested pages
(`limit=3, offset=1` and `limit=100, offset=0`). These court predicates execute
without adaptation; only the existing SUBSTRING adapter is needed for operator
search, which supplies its own bound match label. Other PostgreSQL operators
remain covered by SQL-contract tests, not claimed as native SQLite execution.
The single SELECT retains its projected columns and real SQL LIMIT/OFFSET.
Its correlated citation COUNT/COUNT(DISTINCT) subqueries are server-side work
within that statement, not separate client round trips: mentions count all
source occurrences, authorities deduplicate normalized text (falling back to
citation text), resolved targets deduplicate non-null target IDs, and inbound
cases deduplicate source IDs while excluding self-citations. Constant statement
counts do not establish constant database work or latency.
Other measured SQL executes natively on SQLite without PostgreSQL-function
emulation. FC summary source was unchanged: its before=after numbers are a
current-code measurement, not a historical speedup.

## Measured statements per request

Each cell is **5 rows / 50 rows**. Constant ceilings apply to these fixture
sizes, not arbitrary corpus sizes or unlimited SQL parameter lists.

| Endpoint | Before | After | Scope/change |
| --- | ---: | ---: | --- |
| `/analytics/search/cases` | 1 / 1 | 1 / 1 | Already SQL-limited/projected; empty-query SQLite adapter |
| `/cases/{id}/reader-data` | 13 / 13 | 13 / 13 | Targets already joined; real evidence inspector included |
| `/cases/{id}/statute-references` | 12 / 102 | 4 / 4 | Separate reader evidence endpoint; batch resolver lookups |
| `/api/judge-profiles` | 6 / 51 | 2 / 2 | Select-in links; Python order/ties and filters preserved |
| `/api/judge-profiles/{slug}` | 8 / 53 | 3 / 3 | Linked decisions loaded together, narrow projection |
| `/analytics/search/cases/{id}` | 8 / 53 | 3 / 3 | Joined citation targets; narrow chunk projection |
| `/api/citation-intelligence/search` | 1 / 1 | 1 / 1 | Narrow Case projection |
| `/api/citation-intelligence/cases` | 1 / 1 | 1 / 1 | Narrow Case projection |
| `/api/citation-intelligence/{id}/overview` | 9 / 9 | 9 / 9 | Unchanged |
| `…/{id}/timeline` | 2 / 2 | 2 / 2 | Unchanged |
| `…/{id}/outcomes` | 2 / 2 | 2 / 2 | Unchanged |
| `…/{id}/courts` | 2 / 2 | 2 / 2 | Unchanged |
| `…/{id}/judges` | 2 / 2 | 2 / 2 | Unchanged |
| `…/{id}/statutes` | 2 / 2 | 2 / 2 | Unchanged |
| `…/{id}/companions` | 2 / 2 | 2 / 2 | Unchanged |
| `…/{id}/table` | 3 / 3 | 3 / 3 | Narrow Case/Chunk projection, pagination retained |
| `/api/fc-activity/timeline` | 2 / 2 | 2 / 2 | Current-code summary/filter parity |
| `/api/fc-activity/breakdowns` | 3 / 3 | 3 / 3 | Current-code summary/filter parity |
| `/api/fc-activity/flow` | 1 / 1 | 1 / 1 | Current-code summary/filter parity |
| `/api/fc-activity/analytics` | 3 / 3, then error | 3 / 3 | Grouped counts; pre-existing failure repaired |
| `/api/fc-activity/insights` | 29 / 29 | 24 / 24 | Six duration reads combined |
| `/api/fc-activity/judges` | 3 / 3 | 3 / 3 | Remove redundant intermediate list |
| `/api/fc-activity/counsel` | 1 / 1 | 1 / 1 | Unchanged |
| `/api/fc-activity/motions` | 1 / 1 | 1 / 1 | Remove redundant intermediate list |
| `/api/fc-activity/dashboard` | 2 / 2 | 2 / 2 | Narrow columns/simplify equivalent motion subquery |
| `/api/fc-activity/case` | 1 / 1 | 1 / 1 | Narrow classification projection |
| `/issue-brief` | 2 / 2 | 2 / 2 | Narrow Case projection; full decision list retained |
| `/citation-map/summary` | 6 / 6 | 6 / 6 | Unchanged |
| `/citation-map/cases` | 1 / 1 | 1 / 1 | Narrow node projection |
| `/citation-map/cases/{id}/neighborhood` | 3 / 3 | 3 / 3 | Unchanged |
| `/citation-map/cases/{id}/authority-signals` | 12 / 102 | 4 / 4 | Batch statistics and ordered per-authority contexts |
| `/citation-map/surprises` | 21 / 201 | 2 / 2 | Batch missing/null/zero metrics |
| `/citation-map/cases/{id}/tags` (ranked display) | NameError / NameError | 4 / 4 | Grouped tag frequencies; missing import repaired |

Warm judge-list and FC analytics PR108-cache requests execute **0** SQL and
equal cold/disabled payloads. Warm FC insights/judges/counsel/motions/dashboard
also execute **0** SQL; FC case lookup remains uncached. Empty dashboard is
**1 → 1** statement. Cache tests cover keys, expiry, no hit-based TTL refresh,
eviction and failed builds.

### Explicit equality exceptions

FC analytics previously selected no `source_type` but accessed it after three
statements, raising `AttributeError`. Its aggregation oracle models intended
raw-row counts; selecting/grouping source, mapping `city` to `city_filed`, and
sorting numeric years alongside `Unknown` repair failures, not successful
legacy-response equality.

Ranked tags previously used an unimported `distinct`, raising `NameError`.
An import-repaired diagnostic legacy oracle used **8 / 53** statements; this
is **not** claimed as a successful original-endpoint baseline. Successful
payloads elsewhere are compared completely. The unchanged FC timeline's
NULL/empty-city `Unknown` alias overwrite behavior is deliberately characterized,
not silently corrected.

## Unbounded work, payloads and deferred opportunities

- Constant statement count does **not** imply bounded fetched rows or bytes.
  Judge listing still loads matching profiles/links before Python sorting;
  select-in loader batches can add statements above its batch size.
- Judge detail and issue brief still return complete decision lists. Reader
  full text/chunks remain necessary evidence. No JSON field was dropped or
  pagination/candidate cap silently introduced.
- FC analytics now transfers grouped rows rather than the entire raw cohort.
  Exact medians/quantiles still consume uncapped duration values; FC dashboard,
  judge merits and motion processing remain cohort-size dependent.
- Narrow projections avoid unused large columns but do not quantify bytes,
  peak memory or CPU savings. The reader evidence inspector still performs its
  existing analysis; no persistent evidence cache/invalidation was introduced.
- Legislation uses 400-key batches; ambiguous duplicate-section scalar fallbacks
  can increase counts. Existing resolver logic remains the status/JSON authority.
- Active analytics search is limited; the separate general lexical/hybrid
  service still has unbounded candidate scoring. An arbitrary early limit would
  change ranking and requires a separate product decision.
- Unmeasured citation-map routes: authorities, FC-priority review, topics, issue
  graph, authority-map, common-citers, paths/contextual/hidden, missing-authorities,
  position-profiles, completion-suggestions, replacement, lifecycle, court flow,
  landmarks, issue shifts/dashboard, inheritance, edge summaries/HTTP contexts,
  similar/co-cited cases, and all CSV/UI routes. Repeated path-context queries and
  unbounded path-frontier/doctrine groups remain deferred; helper equality does
  not establish whole-path request performance.
- FC's LRU bounds **entries**, not bytes, and is process-local. No distributed
  invalidation, freshness change, new dependency or cache expansion is included.

Index proposals extend the existing
[`docs/proposed-migrations/indexes.py.txt`](../proposed-migrations/indexes.py.txt)
draft only: document/section pairs and FC city/year pairs. Existing citation
source/target and tag-posting indexes are not duplicated. No deployed index
absence, selectivity, size, planner benefit or latency improvement is claimed.

## Validation and isolation

`scripts/run_offline_tests.py` disables dotenv loading **before** backend imports,
blocks application engines, SQLAlchemy raw PostgreSQL and direct psycopg2
connections, and permits SQLite files only inside that run's disposable pytest
directory. The new performance fixtures are all in memory. Guard tests reject
outside files and URI bypasses; an existing staging fixture's read-only URI is
allowed only inside that directory. Coverage's own SQLite file is disposable too.
`scripts/check_generated_docs.py` applies import/database isolation independently
inside each generator subprocess. The script catalog is regenerated from its
generator, never hand-edited.

Commands use `/tmp/caselibrary-tests/bin/python` (existing manifest requirements
installed in a disposable environment; no dependency manifest changes):

```text
python scripts/run_offline_tests.py -q tests/test_analytics_cache.py tests/test_issue_brief.py tests/test_fc_activity_insights.py
python scripts/run_offline_tests.py -q tests/test_offline_test_runner.py tests/test_endpoint_performance_analytics.py tests/test_endpoint_performance_citations.py tests/test_endpoint_performance_fc.py tests/test_endpoint_performance_reader.py
python scripts/run_offline_tests.py -q tests/test_endpoint_performance_fc_summaries.py
python scripts/run_offline_tests.py -q --deselect tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence --deselect tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes --deselect tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint --cov=backend --cov-report=term-missing:skip-covered
python scripts/check_generated_docs.py
git diff --check
```

Early focused baseline: **37 passed**. Combined performance/isolation check:
**290 passed**; additional unchanged FC summaries: **48 passed**.
Focused worker suites: analytics **248 passed**, reader **48 passed** plus two
existing fake-session checks, citations **107 passed**, FC **59 passed**.
Generated-document check: **3 references current**, after catalog regeneration.
Full-suite final result and pre/postcommit acceptance are recorded below.

Initial full-suite collection lacked installed `pyarrow`; installing the existing
manifest requirement resolved five collection errors. First completed suite:
**1541 passed, 4 failed, 2 skipped, 3 deselected, 1 xfailed**; coverage teardown
was rejected by the first hardened guard. The guard was corrected to place
coverage inside its temporary root and permit only the disposable read-only
staging URI. Remaining failures concern an unrelated unmocked local model and
uncached tokenizer data. They must not be hidden with extra deselects.

No live/external database, dotenv file, credential, deployment script, other
branch or migration was accessed. GitHub issue retrieval was unavailable
without authentication; scope comes from the user's detailed request.
The delegated implementation used independent postcommit validation. The parent
session also scans changed files for secrets, publishes progress, and requests
automated PR review and security validation with the available tools.

### Final precommit acceptance

- Comprehensive focused endpoint and adjacent regressions: **508 passed,
  2 warnings in 46.97s**. This command includes all five new performance modules,
  the guard, analytics-cache, issue-brief, FC-insights/motions, reader, search
  matching and judge tests.
- Full CI-deselect suite with coverage and `--tb=short`: **1590 passed,
  3 failed, 2 skipped, 3 deselected, 1 xfailed, 7 warnings in 143.49s**;
  backend coverage **74%**. Exact failures:
  - `tests/test_api.py::test_local_chunk_search_uses_requested_model`:
    reached an unmocked provider; `sentence-transformers` unavailable in the
    disposable environment. Installing/downloading a model is not substituted
    for repairing the test's mock, and that unrelated owner was not modified.
  - `tests/test_openai_chunk_embeddings.py::test_count_embedding_tokens_uses_model_tokenizer`
  - `tests/test_openai_chunk_embeddings.py::test_count_embedding_tokens_treats_special_token_text_as_literal`
    — tokenizer cache absent; attempted public tokenizer fetch failed DNS.
    No extra deselects or fake tokenizer were used.
- Generated references: **3 current**; changed Python compilation and
  `git diff --check`: **passed**. Whole-document local-link review found two
  pre-existing missing targets in `SYSTEM_REFERENCE.md`
  (`ANALYST_QUICK_START.md`, `reports/test-coverage.md`); they were not introduced
  or changed here. Introduced links: **18 checked, 0 missing**. Scoped added-content
  secret-pattern scan: **26 staged files, 0 flagged files** (values never printed;
  not an exhaustive security audit). Final delivery carries the independent
  postcommit check, which cannot be measured before commit.

Independent postcommit validation of `6a9f304`: **338 passed, 2 warnings in
45.85s**, all **3 generated references current**, clean worktree and commit
whitespace check passed. The validator found an overstatement that every budget
assertion was exact equality; this report now distinguishes measured counts
from ceiling assertions. No backend regression finding was reported.

**PR acceptance blocker:** full-suite green cannot be claimed in this
environment. Safe follow-up is to repair the embedding test's provider mock and
provide a verified offline tokenizer fixture/cache in that test owner surface,
then rerun the exact same three CI deselects. Changes are published through the
PR progress tool, not GitHub CLI authentication or direct pushes.

Acceptance status: **blocked on full-suite validation**, with the implementation
and focused checks delivered. No production latency,
PostgreSQL plans, browser validation or complete citation-map-family measurement
is claimed. The best next task is full-suite model/tokenizer test isolation in
its owner surface; authorized PostgreSQL plan validation follows that acceptance
repair.

Parent-session automated validation: CodeQL analyzed Python and found **0 alerts**.
The automated code-review service could not run because its configured model was
unavailable; its empty comment list is not evidence of a completed review.
The parent secret-scanning tool found no secrets in the delivered changed files.

### PR #144 merged-main validation

Merge `622d21d` retains both the performance branch and main `38f9e3b`.
The four empty-search failures reproduced as an added `query_echo` field, not
increased statement counts. Updating the independent oracle and adding eight
court-operator cases gives **12 passed**; the analytics performance, parser and
search-matching modules together give **365 passed, 2 warnings in 7.61s**.
Regenerating the script catalog fixes merged drift; all **3 references current**.

The guarded full suite used exactly the three CI deselections and CI coverage
options: **1877 passed, 4 failed, 1 skipped, 3 deselected, 1 xfailed, 7 warnings
in 374.96s**, backend coverage **79%**. The existing model/tokenizer tests listed
above fail because Hugging Face and tokenizer assets are uncached and their
download hosts cannot resolve. The additional failure is
`tests/test_paragraph_similarity.py::test_active_reader_feature_and_mock_browser`:
headless Chromium exceeds its 30-second timeout. No additional tests were
deselected or unrelated failures repaired; full-suite acceptance remains blocked.
