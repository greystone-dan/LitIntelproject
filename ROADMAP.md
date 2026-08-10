# AI CaseLibrary Forward Roadmap

Last updated: 2026-08-07

## Objective

This roadmap converts the long-term backlog in `MASTER_IDEAS.md` into a practical delivery plan focused on:

1. Research quality and trust.
2. Product usability for legal workflows.
3. QA maturity and release safety.

## Current Baseline

Already delivered from the master ideas set:

1. Missing Authority Detection.
2. Citation Completion suggestions.
3. Citation Position Profiles.
4. Hidden Authority Paths and inheritance chains.
5. Jurisprudential Shift Detection.
6. Citation Surprise scoring and feeds.
7. Authority Lifecycle tracking.
8. Cross-Court Authority Flow.

Current known strength:

1. Rich citation analytics endpoints and CSV exports.
2. Good route-level test coverage in the existing suite.
3. The stored citation graph is now large enough for external QA sampling at scale.

Current known gap:

1. The roadmap-heavy features below are not yet implemented end to end.
2. QA is strong at unit/route level, but still light on dataset quality gates, performance baselines, and end-to-end regression workflows.
3. The 1000-case external audit surfaced likely truncation patterns in some stored case-to-case citations, so extraction hardening remains a priority.

## Missing Features (Prioritized)

### P0: Trust, Explainability, And Research Completion

1. Citation Context Extraction
- Persist citation windows around each authority mention and expose queryable context fields.

2. Why-Is-This-Cited Classifier
- Classify citation purpose (framework, analytical, supporting, distinguishing, outcome-adjacent).

3. Research Gap Detection
- Surface likely missing lines of authority at issue/statute/topic level, not just case-level completion.

4. Distinguishing Citation Detection
- Detect language that narrows or distinguishes precedent and flag potential negative treatment.

### P1: Product Workflow And Research UX

1. Research Workbench
- Save case sets, authorities, notes, and exported evidence bundles per research question.

2. Citation Heat Maps
- Visualize where key authorities appear within decision structure.

3. Related Case Discovery (Citation-Only Mode)
- Add citation-graph-first discovery independent of text embeddings.

4. Authority Recommendation Engine
- Suggest authorities by issue profile, jurisdiction, era, and court level.

### P2: Advanced Intelligence And Monitoring

1. Boilerplate vs Novel Reasoning detection.
2. Citation Replacement timelines and trend forecasting.
3. Authority network health and anomaly monitoring.

## Forward Delivery Plan

## Phase 1 (Weeks 1-2): QA Foundation And Reliability Gates

Scope:

1. Create gold-standard evaluation sets for at least 5 core immigration issue families.
2. Add contract tests for all `/citation-map/*` analytics and CSV routes.
3. Add performance baselines for top endpoints (p50/p95 latency, SQL row scan ceilings).
4. Add nightly data-quality checks (null metadata, orphan links, malformed citations, duplicate edges).

Exit criteria:

1. Green automated suite with stable baseline counts.
2. Failing quality gate blocks releases.
3. Performance regression budget defined and enforced.

## Phase 2 (Weeks 3-5): Citation Context Intelligence MVP

Scope:

1. Implement citation context extraction and storage.
2. Add initial rule-based citation purpose labeling.
3. Expose context and purpose in API responses and CSV exports.
4. Add UI drilldown from authority node to citation-context evidence.

Exit criteria:

1. At least 80% context extraction success on sampled FC decisions.
2. Purpose labels available in reader/map workflows.
3. QA includes context accuracy checks on labeled fixtures.

## Phase 3 (Weeks 6-8): Research Completion And Workbench MVP

Scope:

1. Implement research gap detection at case and issue level.
2. Build workbench entities: saved sessions, notes, pinned authorities, export packet.
3. Add citation-only related-case discovery and recommendation ranking.

Exit criteria:

1. Users can save and resume a research thread.
2. Gap suggestions include evidence references and confidence labels.
3. Retrieval quality improves on benchmark questions (MRR and hit@k targets).

## Phase 4 (Weeks 9-12): Explainability, Monitoring, And Launch Readiness

Scope:

1. Add distinguishing citation detection and confidence flags.
2. Add boilerplate/novel reasoning signals.
3. Add trend monitoring dashboards and alert thresholds.
4. Add release checklist for model/config/database migrations.

Exit criteria:

1. Explainability panel in UI for top recommendations.
2. Weekly trend report generated automatically.
3. Launch checklist required for production release candidate.

## QA Roadmap

## Test Pyramid Targets

1. Unit tests: keep broad deterministic coverage of extractors, scoring, and validators.
2. Integration tests: DB + API route tests for all new analytics and workbench flows.
3. End-to-end tests: browser/API tests for core user journeys:
- case search to evidence review
- missing-authority follow-up
- workbench save/resume/export

## New QA Streams To Add

1. Data quality audits
- Citation parse validity rate
- Metadata completeness rate
- Graph integrity checks

2. Retrieval quality benchmarks
- Fixed benchmark set with expected authorities
- MRR, recall@k, and precision@k tracked per release

3. Performance and scale tests
- Representative corpus-size query tests
- Endpoint latency SLO checks

4. Safety and governance checks
- Response disclaimer presence where required
- Provenance traceability for every recommendation
5. External citation audits
- Cheap-model audit passes over stored case-to-case citations
- Filter duplicate-only flags before turning findings into fixes
- Track truncation, partial party-style citations, and reporter-style citations separately

## Suggested Quality Gates

1. Required for merge:
- All tests pass
- No new critical diagnostics
- API contract snapshots unchanged or intentionally updated

2. Required for release:
- Retrieval benchmark non-regression
- Performance budget non-regression
- Data-quality thresholds met

## Success Metrics

By end of Phase 4, target:

1. Research quality:
- +20% improvement in benchmark hit@5 over current baseline.

2. Trust and explainability:
- 100% of top-N recommendations include source citations and context snippets.

3. Reliability:
- 0 unresolved critical regressions in two consecutive release cycles.

4. Usability:
- Workbench flow usable end to end without manual DB intervention.

## Immediate Next Actions (This Week)

1. Run a deterministic statute/instrument coverage audit over the priority
	review cohort and group remaining misses by format before reprocessing.
2. Expand law regressions for French forms, Parts/Schedules, additional treaties,
	and safe short-form anchor boundaries.
3. Repair the unrelated FC document-scraper test collection error and establish
	a new full-suite baseline.
4. Define endpoint SLO budgets for `/search/chunks/grouped` and top
	`/citation-map/*` surfaces.
5. Add CI stages for extraction quality, performance smoke, and API/export
	contract checks.
