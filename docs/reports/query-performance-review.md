# Query Performance Review — Issue #56

Reviewed: 2026-10-03

## Scope and method

Read-only source review of `backend/search_service.py`, `backend/reader_service.py`,
`backend/routes.py`, `backend/analytics_service.py`, and the Alembic migration
files. No database connection, query plan, deployed schema, benchmark, or runtime
measurement was used. Findings below distinguish source-observed behavior from
performance hypotheses; expected impacts are directional, not measured.

“Missing index” means no matching index was found in the inspected migration
definitions, not that a deployed database was inspected. In particular,
`case_tags` already has a unique index on `(case_id, category, value,
taxonomy_version)` from `0010_case_legal_tags.py`, matching the correlated tag
filter; an additional copy is not proposed.

## Findings

| Query | File / line | Problem | Proposed fix | Expected impact |
| --- | --- | --- | --- | --- |
| Case lexical/semantic/hybrid search | [`backend/search_service.py:443-458`](../../backend/search_service.py#L443), [`:462-507`](../../backend/search_service.py#L462) | The SQL statement fetches every matching row. Scoring, sorting and page slicing happen in Python afterward. The response is page-sized, but the candidate query and intermediate lists are not bounded by `page_size`. | Design a bounded candidate strategy that preserves the documented ranking semantics (including lexical normalization and graph boost), then apply a stable database-side ordering/limit where valid. Compare result parity on representative queries before adoption; a simple early `LIMIT` may change rankings. | Lower result transfer and Python memory/CPU for broad matches if candidate selection is bounded without unacceptable recall or ranking changes. Runtime benefit and safe candidate cap are unknown. |
| Case substring filters and search query | [`backend/search_service.py:214-237`](../../backend/search_service.py#L214), [`:281-294`](../../backend/search_service.py#L281), ranking expression [`:344-351`](../../backend/search_service.py#L344); initial case indexes [`alembic/versions/0001_case_metadata.py:39-40`](../../alembic/versions/0001_case_metadata.py#L39) | Several filters use leading-wildcard `ILIKE` (`title`, `court`, `source_name`, citations, and related fields). Migration-defined B-tree indexes on some fields do not generally accelerate `%term%` matching. The lexical rank builds `to_tsvector` from a dynamic multi-column expression; no corresponding GIN search-vector index was found in the inspected migrations. | Benchmark representative plans. For selective substring filters, evaluate `pg_trgm` GIN indexes on frequently used columns. For lexical ranking, consider a stored/generated search vector only as a separate design, ensuring the indexed expression exactly matches search semantics. | Trigram indexes can reduce scans for supported, selective substring patterns; a stored search vector could accelerate text matching/ranking. Index size, write cost, short-term behavior, and actual planner use are unmeasured. |
| Exact `source_type` and `language` filters | [`backend/search_service.py:244-253`](../../backend/search_service.py#L244); migration indexes in [`0001_case_metadata.py`](../../alembic/versions/0001_case_metadata.py) and [`0002_raw_ingestion.py:42-43`](../../alembic/versions/0002_raw_ingestion.py#L42) | These exact-match filters are present, but no B-tree indexes for `cases.source_type` or `cases.language` were found in those migration definitions. `processing_status` does have an index. This is an index candidate, not evidence that these filters are currently slow. | Check selectivity and `EXPLAIN (ANALYZE, BUFFERS)` on a representative database before adding either index; use only indexes justified by common, selective request patterns. | Could reduce reads for selective exact-match filters; low-cardinality or infrequent filters may not benefit enough to offset storage and write overhead. |
| Inventory and per-case sources | [`backend/routes.py:610-620`](../../backend/routes.py#L610), response assembly [`:651-656`](../../backend/routes.py#L651); existing source index [`alembic/versions/0008_case_provenance_tables.py:31`](../../alembic/versions/0008_case_provenance_tables.py#L31) | `/inventory` materializes every case, then runs one `case_sources` query per case, and returns the complete collection. The existing `case_sources.case_id` index helps each lookup but does not remove the N+1 round trips or bound payload size. | Introduce a reviewed, explicit page/cursor contract; fetch one page of cases and batch-fetch sources for its IDs, then group sources in memory. Review existing callers before changing the response contract. | Changes source reads from one per case to a small fixed number per page; pagination bounds database and application memory, transfer, and response size. |
| Legislation case occurrences | [`backend/routes.py:764-798`](../../backend/routes.py#L764); related section lookup [`:824-845`](../../backend/routes.py#L824) | An `OR` combines indexed `instrument_key` equality with leading-wildcard pinpoint matching, then all candidate rows are materialized, parsed, post-filtered, and returned without a result limit. A B-tree on `instrument_key` exists (`0017_structured_legislation_citations.py`); it does not cover the substring branch. | Filter by canonical instrument key first if equivalent for all supported inputs, or evaluate a trigram index for the pinpoint branch and move exact predicates into SQL where semantics permit. Add an explicit bound/pagination only with contract review. | May reduce candidate scans and Python work for pinpoint lookups. Current plans, input sizes, and compatibility of query rewrites are unknown. |
| Stored citation detail target lookup | [`backend/reader_service.py:941-966`](../../backend/reader_service.py#L941) | For each source citation, the code may call `db.get(Case, target_case_id)`. If target cases are not already in the session identity map, this can issue per-citation lookups. The number of distinct targets/session state was not measured. | Collect distinct target IDs and load them in one query, or include target fields in a join; preserve the current citation-to-target mapping. | Avoids repeated round trips when multiple targets are uncached; query-count reduction depends on citation and target counts. |
| Statute-reference resolution in reader helper | [`backend/reader_service.py:506-513`](../../backend/reader_service.py#L506), per-reference resolution [`:528-530`](../../backend/reader_service.py#L528), response construction [`:567-570`](../../backend/reader_service.py#L567) | Each reference is passed to `resolve_legislation_reference`. That helper is outside this review’s source scope, so additional SQL per row is a possible but unverified N+1. | Inspect the resolver’s query behavior in a follow-up; if it performs repeated document/section lookups, batch or memoize lookups by normalized instrument/pinpoint within the request. | Could reduce repeated resolution queries; benefit is conditional on the helper implementation and repeated keys. |
| Reader evidence summary | [`backend/reader_service.py:734-741`](../../backend/reader_service.py#L734), [`:81-85`](../../backend/reader_service.py#L81) | Each reader build with paragraph chunks calls `inspect_case` to build the evidence summary. Its query count and CPU cost were not inspected or measured; the output appears derived from case/chunk data and algorithm parameters. | Measure the helper first. If materially expensive and stable, cache/precompute by case/chunk content version plus analysis version, with explicit invalidation when inputs or rules change. | Could avoid repeated analysis work on unchanged evidence; cache cost, freshness guarantees, and actual latency gain are unknown. |
| FC activity analytics aggregation | [`backend/analytics_service.py:509-526`](../../backend/analytics_service.py#L509), Python aggregation [`:549-563`](../../backend/analytics_service.py#L549) | The query selects all matching classification rows and Python aggregates counts and source distributions. Result rows are not capped; filters may narrow them but can be omitted. | Group by the requested dimensions in SQL and return the already-aggregated counts. Preserve the current unknown-value handling and coverage totals. | Reduces rows transferred and Python memory/CPU for large cohorts; database aggregation cost and group cardinality remain workload-dependent. |
| Judge profile list | [`backend/analytics_service.py:593-624`](../../backend/analytics_service.py#L593) | Both branches load all profiles, sort, and only then apply a maximum limit of 100. Sorting accesses `case_links`; if that ORM relationship is lazy-loaded, it may also cause N+1 queries. Relationship loading behavior was not verified. | Aggregate decision counts and order/limit in SQL, or explicitly eager-load the relationship in one bounded query. Inspect the relationship mapping and verify query count before selecting a fix. | Bounds profile rows and may eliminate relationship round trips; exact impact depends on profile count and ORM loading configuration. |
| About-page statistics | [`backend/analytics_service.py:256-283`](../../backend/analytics_service.py#L256) | Each call executes 15 separate scalar count statements, including counts over large tables. These are repeated whenever the endpoint is requested. | Consider a single statement containing scalar subqueries or a short-lived cache/snapshot with a documented freshness policy. Measure database cost first; some tables may be small. | Fewer round trips and potentially less repeated counting; total table-scan work may remain similar unless counts are cached or precomputed. |

## Draft migration (report text only — not added to `alembic/`)

The leading-wildcard filters above are the clearest schema-level index candidate.
The following is a **non-deployable draft** for four likely search fields only;
the review did not establish that these are the most selective or frequent
filters. Confirm PostgreSQL/`pg_trgm` availability, current Alembic head,
index sizes, representative query plans, and maintenance window before turning
this into a migration. Creating an extension may require elevated database
privileges. Concurrent index creation takes longer and consumes additional
resources; `IF NOT EXISTS` does not verify an existing index’s definition.

```python
"""DRAFT ONLY: trigram support for case substring filters."""

from alembic import op

revision = "TBD"
down_revision = "CONFIRM_CURRENT_ALEMBIC_HEAD"
branch_labels = None
depends_on = None

INDEXES = (
    ("ix_cases_title_trgm", "title"),
    ("ix_cases_court_trgm", "court"),
    ("ix_cases_citation_trgm", "citation"),
    ("ix_cases_secondary_citation_trgm", "secondary_citation"),
)


def upgrade() -> None:
    # Verify extension policy/privileges before deployment.
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    with op.get_context().autocommit_block():
        for index_name, column_name in INDEXES:
            op.execute(
                f"CREATE INDEX CONCURRENTLY IF NOT EXISTS {index_name} "
                f"ON cases USING gin ({column_name} gin_trgm_ops)"
            )


def downgrade() -> None:
    with op.get_context().autocommit_block():
        for index_name, _column_name in reversed(INDEXES):
            op.execute(f"DROP INDEX CONCURRENTLY IF EXISTS {index_name}")
    # Deliberately retain pg_trgm: it may be shared by other indexes/features.
```

This does not address the dynamic full-text rank expression or exact-match
`source_type`/`language` candidates. For this draft, the smallest disconfirming
experiment is to compare representative `EXPLAIN (ANALYZE, BUFFERS)` plans and
latencies with/without the candidate indexes on a controlled database snapshot,
including short and selective search strings. No such experiment was run.

## Evidence boundaries

- Reviewed source and migration definitions only; no database, production system,
  secrets, query plans, performance metrics, or migration execution were used.
- No application source or Alembic file was modified.
- Recommendations are review candidates, not proof of deployed index absence or
  a claim that a query currently violates a latency target.
- Related Swimm walkthrough: [Search and Retrieval Architecture](../../.swm/5.b49ftjal.sw.md).
