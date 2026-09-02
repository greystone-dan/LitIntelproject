# Metrics Dictionary

Last reviewed: 2026-09-01

This dictionary defines the research metrics shown or computed by the active system. Metrics are evidence-navigation signals. They do not determine legal authority, correctness, outcome causation, or legal advice.

## Inventory Metrics

| Metric | Definition | Source | Interpretation |
| --- | --- | --- | --- |
| Decision cases | Count of canonical `cases` rows | `/api/about/stats` | Library inventory, not official-source or full-text completeness |
| Cases with full text | Canonical cases with non-empty `full_text` | `/api/about/stats` | Text availability; text may still be unofficial or incomplete |
| Searchable chunks | Count of `case_chunks` rows | `/api/about/stats` | Segmented text inventory; chunk sets can represent the same decision at different granularities |
| Citation records | Count of `citations` rows | `/api/about/stats` | Case-law citation occurrences, not unique authorities |
| Resolved citations | Citation rows with a non-null `target_case_id` | `/api/about/stats` | Local target match count; not legal proposition validation |
| Unique linked authorities | Distinct local target-case IDs among resolved citations | search/reader analytics | Breadth of local resolved authority use |
| Statute references | Count of `statute_references` rows | inventory/statute APIs | Independent law/instrument occurrences; never add directly to case-citation totals |
| Judge profiles | Count of canonical `judge_profiles` | `/api/about/stats` | Known normalized judge identities, not complete judicial coverage |
| FC activity cases/documents | Counts in `fc_activity_cases` and `fc_activity_documents` | `/api/about/stats` | Separate procedural/activity dataset inventory |

## Search And Retrieval Metrics

| Metric | Definition | Formula/behavior | Caution |
| --- | --- | --- | --- |
| Semantic similarity | Vector similarity displayed for semantic/hybrid search | $\max(0, \min(1, 1-d))$ from pgvector cosine distance $d$ | Model- and corpus-dependent; not a probability of relevance |
| Lexical similarity | Relative lexical match score | Raw lexical score divided by maximum candidate score | Relative to returned candidate set; not comparable across unrelated searches |
| Hybrid similarity | Combined semantic and lexical score | $w_sS+w_lL$ using request weights | Meaning changes with weights and candidate pool |
| Graph boost | Small popularity tie-breaker | $\min(0.05, \log(1+in\_degree)/100)$ | At most 0.05; should not dominate text relevance |
| Best chunk similarity | Highest final matching chunk score for a grouped case | Greatest grouped chunk score | One strong passage can rank a case highly |
| Candidate pool | Pre-pagination candidates before hybrid reranking | Request-bounded, normally 10-500 | Affects rank quality and work performed |

## Citation Occurrence And Graph Metrics

| Metric | Definition | Source | Caution |
| --- | --- | --- | --- |
| Citation mention / occurrence | One stored case-law reference in a source case | `citations` row | Multiple mentions of one authority count separately |
| Total occurrences | Number of citation rows/mentions in scope | citation table/analytics | Do not confuse with distinct citing cases or edges |
| Unique cited authorities | Distinct normalized/resolved target authorities cited by one case | reader/search analytics | Unresolved forms and normalization affect the count |
| Unique citing cases | Distinct source cases citing an authority | citation-intelligence overview | Breadth signal; depends on corpus coverage |
| Max mentions in one decision | Largest occurrences from one source case to one authority | citation-intelligence overview | Repeated discussion, not necessarily authority weight |
| Average mentions per decision | Total occurrences divided by distinct citing cases | citation-intelligence overview | Sparse denominators can exaggerate values |
| Resolved occurrence | Citation row mapped to a canonical target | `target_case_id IS NOT NULL` | Matching is local-library dependent |
| Unresolved occurrence | Valid extracted citation with no local match | `unresolved=true` | Could indicate absence, naming variation, or resolution gap |
| Aggregated edge | Resolved occurrences grouped by source/target case | `(source_case_id, target_case_id)` | Edge strength is occurrence count, not doctrinal strength |
| In-degree | Resolved occurrences targeting a case | `citation_metrics.in_degree` | Counts occurrences, not necessarily distinct citing cases |
| Out-degree | Resolved occurrences made by a case | `citation_metrics.out_degree` | Counts resolved outgoing occurrences only |
| PageRank | Resolved-graph centrality value | `citation_metrics.pagerank` | Relative signal; changes with corpus/resolution coverage |

## Citation Intelligence Scores

| Metric | Definition | Interpretation limit |
| --- | --- | --- |
| Gravity share | Local citation intensity relative to a source case's citation distribution | Relative attention within one decision, not legal force |
| Surprise score | Signal balancing local intensity against global authority ubiquity | Review aid; sparse coverage can distort it |
| Originality score | Signal emphasizing less ubiquitous authorities in a case's citations | Not novelty of legal reasoning |
| Rarity-weighted score | Shared-authority similarity inversely weighted by authority frequency | Depends on resolved graph completeness |
| Missing-authority priority | Peer coverage, occurrences, rarity boost, and priority for an absent authority | Suggestion to investigate, not a required citation |
| Completion recommendation score | Peer-derived authority signal for a focus case | Not an automated filing recommendation |
| Replacement score | Time-series overlap/transition signal between authorities | Not proof of overruling/replacement |
| Lifecycle velocity/decay | Recent versus prior citing-case change | Time-window/corpus sensitive |
| Lifecycle stage | Emerging, dominant, declining, foundational, or transitional label | Heuristic categorization only |
| Hidden-bridge support | Frequency/weight of intermediate case on citation paths | Network navigation, not legal mediation |
| Inheritance chain depth | Downstream hops in authority-adoption path | Graph path length, not causal influence |
| Cross-court flow | Citing case count/occurrences grouped by source/target court | Court/source coverage matters |

## Outcome, Metadata, And Quality Metrics

| Metric | Definition | Formula/behavior | Caution |
| --- | --- | --- | --- |
| Classified decisions | Decisions with recognized stored outcome classification | count of classified rows | Coverage varies by source/text quality |
| Government wins | Classified rows labelled government won | count | Not a merits or judge-bias finding |
| Individual wins | Classified rows labelled individual won | count | May not capture mixed/remittal nuances |
| Unclassified | Decisions lacking usable classification | total minus classified | Inspect before comparing rates |
| Government win rate | Government-won share among classified decisions | $100 \times government\_wins/classified$ | Low denominators and excluded rows matter |
| Individual win rate | Individual-won share among classified decisions | $100 \times individual\_wins/classified$ | Use only with classification coverage context |
| Metadata confidence | Deterministic field extraction confidence | Source/extraction agreement signal | Not legal certainty |
| Quality flag | Missing, malformed, conflicting, or low-confidence field signal | Review-queue indicator | Not necessarily a source error |
| Needs review | Critical metadata needs verification | case-level flag | Does not invalidate all fields |
| Tag score | Rule-defined strength for legal tag/evidence match | deterministic tag rule | Not issue dispositiveness |
| Citation pickup | Audit-derived share of expected citations found | Report expected/matched/missing/unexpected/span errors | Always report cohort and source scope |

## Work-History Metrics

| Metric | Definition | Caution |
| --- | --- | --- |
| Recorded turns | Stored local VS Code project turns | Excludes offline/terminal/browser work |
| Five-minute-capped active time | Sum of inter-turn gaps capped at five minutes | Reproducible proxy, not payroll time |
| Session-level cross-check | Same capped logic grouped by session | May differ slightly from day grouping across midnight |

## Reporting Rules

1. Name the metric scope: case, chunk, source, cohort, date range, court, tag, or full corpus.
2. State whether values are occurrences, distinct cases, distinct authorities, or aggregated edges.
3. For rates, report the denominator and unclassified/missing population.
4. For extraction quality, report precision/recall-style counts and exact-span errors, not only total rows.
5. For graph signals, state that they derive from resolved local citations and can change as coverage improves.
6. Preserve source links and avoid presenting a score as legal advice or legal conclusion.