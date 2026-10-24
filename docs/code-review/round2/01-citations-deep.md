# Citation review — deeper pass

Scope: `backend/citations.py`, `citation_map.py`, `citation_refine/`,
`citation_pipeline/`, citation treatment, and paragraph cited-by. FC, SCC and
FCA behavior is in scope. This is a source review; I did not query the database
or execute extraction because the review environment lacks the citation module's
runtime dependencies. The examples below are traced through source and existing
fixtures, not reported as fresh test results.

## Input trace

- `2024 FC 639` enters the neutral-citation path in
  [`citations.py:58-66,1518-1548`](../../../backend/citations.py), where the
  court/year/number are recognized before the extraction wrapper persists the
  candidate. Resolution and refinement are separate follow-on steps.
- A parallel form such as `2015 SCC 1, [2015] 1 S.C.R. 3 at para 139` is
  processed as a chain of citation cores
  ([`citation_refine/cases.py:331-435,516`](../../../backend/citation_refine/cases.py)).
  `parse_pinpoint` handles the pinpoint
  ([`citation_refine/pinpoints.py:102`](../../../backend/citation_refine/pinpoints.py)).
- The French form `Dhillon c. Canada, 2020 CF 123, par. 12` is covered by a
  refinement fixture; French court codes are mapped in
  [`citation_refine/cases.py:70`](../../../backend/citation_refine/cases.py).
  The pinpoint parser includes ranges and lists (for example, `at paras
  85-87 and 99`), while short forms such as `Vavilov at paras 10-12` use
  their own extraction/anchor path. These are separate checks; a successful
  text match does not establish that target resolution found a local case.
- The citation issue map and the paragraph-citer list are downstream views;
  neither re-extracts citation text or changes its offsets.

## Findings (ranked)

### 1. Low — Focus mode limits the global set before filtering to the focus set

**Location:** [`backend/citation_map.py:489-512`](../../../backend/citation_map.py)

When `CASELIBRARY_FOCUS_MASTER_300` is enabled, the query orders and limits all
cases carrying a tag, then filters those rows to `focus_ids` in Python. If the
first `limit` rows are outside the focused cohort, the map can return no nodes
even when focused cases match; the separate `available_cases` count is scoped
to the focus IDs. For example, with `limit=1`, a higher-ranked non-focus case
and a lower-ranked focus case with the same tag, the result drops the selected
row after the SQL limit. Expected: one focused node; actual: zero nodes.

**Suggested fix:** Apply the focus-ID predicate in SQL before ordering and
limiting, retaining the empty-focus fast path.

### 2. Low — Citer order contradicts its stated strongest-signal priority

**Location:** [`backend/paragraph_cited_by.py:158-162`](../../../backend/paragraph_cited_by.py);
consumer: [`backend/paragraph_cited_by_db.py:258-283`](../../../backend/paragraph_cited_by_db.py)

`citer_sort_key` says “Strongest signal, then most mentions,” and
`PURPOSES` declares `disagreed` stronger than `mentioned`, but the sort tuple
puts descending mention count first. A `mentioned` citer with 12 occurrences
therefore precedes a `disagreed` citer with one occurrence. Expected from the
documented contract: the disagreed citer is first; actual: the more frequent
mention is first.

**Suggested fix:** Sort on signal strength before mention count, or explicitly
change the documented contract and UI if frequency-first is intended.

## Not repeated

This report omits the excluded `citation_map.distinct` NameError, pinpoint
`199-02`, citation-pass backslashes, and previously fixed citation findings.

## Limits

No live corpus counts, database-backed examples, browser checks, or citation
integration tests were run. The neutral, reporter, pinpoint, French, short-form,
and range paths were inspected in source and fixtures only.
