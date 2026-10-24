# Citation Extraction, Linking, and Treatment Review

## Summary

The active citation path handles many neutral, reporter, pinpoint, and short-form
variants, and the treatment and risk modules generally label their results as
experimental or indicative. This static review found concrete defects in tag
ranking, French citation extraction, API authentication, pinpoint expansion, and
memo treatment reporting, plus risks around ambiguous links, outcome-based
“contrary” suggestions, and unbounded database work.

All 51 source files listed in the issue were read. None were unread. The review
was limited to FC, SCC, and FCA decisions; no database, external API, or live
service was queried. Findings based on unverified corpus conditions are marked
**possible**.

## Bugs

- **`backend/citation_map.py:383` — medium.** `_rank_tags_by_rarity_and_frequency`
  calls `distinct(...)`, but the module imports neither `distinct` nor a name
  that defines it. The default tag-ranking path therefore raises `NameError`
  when it counts cases with a tag. Use `func.count(func.distinct(...))` or
  import SQLAlchemy's `distinct`.

- **`backend/citations.py:58-65`; `backend/citation_pipeline/rules.py:28,37-40` —
  medium.** The active extractor does not recognize French-neutral court codes
  or French case-name separators: the neutral regexes accept FC/FCA/SCC, while
  the case-name rules require `v.` and ASCII party-name letters. For example,
  `Canada (Ministre de la Citoyenneté et de l'Immigration) c. Vavilov, 2019 CSC
  65, au para 23.` should produce a case citation normalized to `2019 SCC 65`
  with its pinpoint; the active extraction path produces no case candidate.
  The separate refinement code has French fixtures, but it is not invoked by
  this extraction entry point. Extend and test the active rules for `c.` and
  accented names, and map CSC/CAF/CF before resolution.

- **`backend/citation_pipeline/canlii.py:66-75` — medium.** The client places
  the literal `******` in the `Authorization` header and never uses its
  `api_key` field in the request. Authenticated lookups therefore cannot work;
  the broad exception handler also silently turns request failures into no
  result. Send the key using CanLII's documented mechanism and handle failures
  without exposing the key.

- **`backend/citation_refine/pinpoints.py:62-70` — medium.** Abbreviated
  endpoints crossing a hundred boundary are expanded incorrectly. For example,
  `paras 199-02` calls `_expand_range(199, 2)`, constructs 192, and returns
  `[199]`; expected values are 199 through 202. Preserve the endpoint's written
  digits and roll the abbreviated endpoint into the next hundred when required.

- **`backend/memo_citation_check.py:43-51` — medium.** Treatment is inferred
  from `Citation.citation_kind` values such as `"overruled"` and `"applied"`,
  but the extraction layer defines case kinds as `neutral`, `case`,
  `case_short`, and `case_name` (`backend/citations.py:36-37`). Normal stored
  citation rows therefore cannot express these treatment labels, so this
  feature reports no treatment even when citations exist. Use a separately
  sourced treatment-evidence layer and do not treat extraction kind as treatment.

## Data-correctness risks

- **`backend/overruling_risk.py:143-155` — medium.** Every resolved citation to
  the Vavilov seed creates an indirect “may be affected” flag, without checking
  whether the requested case predates the 2019 event. A post-Vavilov decision
  citing Vavilov can consequently appear to be at risk from a later development.
  Use the decision/event chronology to distinguish later-development risk from
  ordinary citation to the framework, and keep unknown dates explicitly cautious.

- **`backend/memo_authority_suggestions.py:124-133` — medium.** The `contrary`
  list is selected solely because a majority of the authority's citing decisions
  have a government-lost outcome. That does not show that those decisions
  criticized, distinguished, or rejected the authority. The output can be read
  as a treatment label despite having only outcome evidence. Rename it as an
  outcome association or require verified, authority-specific treatment evidence
  before calling an authority contrary.

- **`backend/memo_citation_check.py:53-56` — medium.** `citing_cases_count` is
  the number of citation rows, not distinct citing decisions. Repeated mentions
  by one source decision inflate the displayed count. Count distinct
  `Citation.source_case_id` values; expose occurrence count separately if useful.

- **`backend/memo_citation_check.py:73-80,156-170` — low.** Both suggestion
  paths limit cases by citation count before checking issue overlap in Python.
  A case sharing the relevant issues but outside the preselected top
  `limit * 3` (or 20) can never be returned, and the response does not identify
  that omission. Filter for issue overlap before limiting, or paginate and
  disclose truncation.

- **Possible — `backend/citations.py:2833-2848` — medium.** Local neutral
  resolution uses `session.scalar()` for citation equality and returns one
  matching case without checking for duplicates. The model's citation field is
  indexed but not unique, and another local index builder explicitly marks
  collisions ambiguous (`backend/citations.py:2870-2883`). If duplicate
  canonical values exist, the chosen target may be arbitrary. Resolve only a
  unique matching case and leave collisions unresolved.

- **Possible — `backend/citation_map.py:62-77`; `backend/citation_source.py:1-5,
  35-51` — medium.** Citation-map graph aggregation reads `Citation` directly
  rather than using the `CITATIONS_SOURCE` selector. If that setting is intended
  to switch all read paths, enabling `refined` still leaves graph analytics on
  legacy rows. Make this read path source-aware, or document its explicit
  legacy-only behavior.

- **`backend/paragraph_cited_by_db.py:91-100,103-116`;
  `backend/paragraph_cited_by_runner.py:319-324` — low.** The CLI's processed
  count includes every current-version status, including no-citation cases
  handled in incremental mode, while the default-mode total includes only
  citing cases with resolved citations. After incremental processing, default
  mode can overstate completed work and understate “to do.” Count processed
  sources using the same eligibility criteria as the selected mode.

- **`backend/contextual_authority/outline_v2.py:939-951` — low.** Section and
  point membership use `start <= offset <= end`, although the stored character
  spans are half-open. A citation at the exact end boundary can be assigned to
  the preceding section or point. Use `start <= offset < end` consistently.

## Security risks

No concrete security vulnerability was identified in the reviewed files. The
CanLII request-key defect is reported above as a functional issue; no secret or
credential value was found in the reviewed source.

## Performance

- **`backend/memo_citation_check.py:31-34,128-133` — medium.** For each
  resolved memo citation, `_get_treatment_status` loads every incoming citation
  row for that target. Repeated citations to the same authority repeat the
  query, and the result is unbounded. Batch distinct target IDs and aggregate
  treatment evidence/counts in bounded database queries.

- **`backend/contextual_intelligence.py:596-600` — medium.** Up to 100
  candidate IDs are scored by calling `compute_case_thematic_signature` once
  per candidate; that function separately loads the case, tags, statutes, and
  citations (`:463-482`). This creates roughly four candidate-related reads per
  candidate. Batch-load the signature inputs, then score in memory.

- **Possible — `backend/citation_pipeline/pipeline.py:18-25` — low.**
  `_select_non_overlapping` compares each candidate with every already accepted
  candidate, so a citation-dense document can require quadratic overlap checks.
  Consider an interval-based selection structure if profiling confirms this is
  material.

## Dead code / cleanup

- **`backend/paragraph_cited_by.py:158-162` — low.** `citer_sort_key` says
  “Strongest signal” first, and `PURPOSES` orders stronger signals first, but
  the returned key sorts by descending mentions before signal strength. A
  high-volume “mentioned” citer can outrank a stronger treatment signal. Put
  purpose strength before mention count, or correct the stated/display order.

No other high-confidence dead-code or misleading-name findings were identified.

## Suggestions

- Add focused regression fixtures for French neutral captions and abbreviated
  cross-hundred paragraph ranges through the public extraction/linking paths,
  not only their helper regexes.
- Keep extraction kind, citation relationship, treatment evidence, and decision
  outcome as distinct data; UI labels should state which evidence supports each
  heuristic.
- Verify duplicate neutral-citation handling and source-selection behavior
  against fixtures that include collisions and partially refined source cases.

## Review and validation limits

The focused pytest command could not start because `pytest` is not installed.
`python scripts/check_generated_docs.py` also could not complete: its API and
schema generators lack the installed `fastapi` and `sqlalchemy` packages.
`git diff --check` passed before this report was added. No code or tests were
changed, and no database or external service was used.
