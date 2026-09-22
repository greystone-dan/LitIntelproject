# AI CaseLibrary Product Roadmap

Last updated: 2026-09-22

## Current Direction

The near-term goal is a compelling demo product for Canadian immigration
litigation research. The system already has a substantial deterministic
foundation, so delivery now prioritizes showing its value clearly over broad
corpus expansion or exhaustive quality work.

The demo journey is: start with a legal issue or case type, find useful
decisions, understand why they matter, inspect source-grounded evidence, and
move through linked authorities without losing context.

Data quality remains important, but is now a deferred track. We will fix only
quality problems that could make the demo misleading or unusable until the demo
workflow has a stable audience and acceptance baseline.

The long-term architecture for the deferred intelligence track is maintained in
[docs/LONG_TERM_INTELLIGENCE_VISION.md](docs/LONG_TERM_INTELLIGENCE_VISION.md).
It preserves the intended direction for citation treatment, Decision Units,
Argument Packets, and cross-case comparison without changing the current
demo-first delivery commitment.

## Demo Audience And Jobs

The primary audience is immigration lawyers, legal researchers, supervisors,
and technical or institutional stakeholders evaluating the product. A user must
be able to:

1. Begin with an issue, doctrine, statute, or case type rather than a case name.
2. Narrow results by court, year, judge, outcome, government party, statute, or
	 cited authority.
3. See why a case was returned and whether useful evidence is available.
4. Read the decision, inspect citations/statutes/tags, and follow authorities.
5. Return to the result set without losing the research thread.

## Priority 0: Issue And Type Discovery

Case identification must work from how researchers think about a problem, not
only from title or citation.

Deliverables:

- Create curated issue and case-type entry points for a small demo corpus,
	beginning with procedural fairness, humanitarian and compassionate
	applications, inadmissibility/security, refugee protection, and judicial
	review.
- Add a visible issue/type discovery surface to `/data-explorer`.
- Map entry points to existing themes, statutes, tags, outcomes, and cohorts.
- Allow refinement by court, year, judge, outcome, government party, statute,
	cited authority, and source availability.
- Improve result cards with case identity, issue/type, court/date, outcome,
	citation signals, source status, and a concise reason for inclusion.
- Preserve a clear path from discovery to reader and back to results.

Acceptance check: a new user can select an issue/type, reach useful results,
and open a relevant case in under two minutes without knowing a case name or
touching the database.

## Priority 1: Demo Research Journey

Make `/data-explorer` feel like one product rather than a collection of
internal tools.

Deliverables:

- Lead with Case Search and issue/type discovery; demote architecture,
	inventory, and experimental surfaces from the main demo path.
- Add a curated “start here” set and a scripted golden-path scenario.
- Preserve search state, filters, selected result, and return navigation.
- Make empty, loading, unresolved, and incomplete-evidence states plain.
- Make citation intelligence, precedents, statutes, and related cases follow-up
	actions from the reader.
- Add a compact case-at-a-glance view with issue/type, outcome, provisions,
	source, citation signals, and the deterministic case summary.

Acceptance check: discovery, case reading, evidence inspection, linked-authority
navigation, and return-to-results work as one uninterrupted workflow.

## Priority 2: Usability And Reader Polish

Improve the parts users touch repeatedly before adding more intelligence.

Deliverables:

- Improve hierarchy, labels, spacing, loading states, empty states, and error
	recovery in search and the inline reader.
- Keep the technical structure and researcher-facing summary toggles distinct,
	with clear purpose and source verification cues.
- Add accessible tab semantics, keyboard navigation, focus states, and usable
	reader pane controls.
- Verify touch targets, text fit, tab overflow, and evidence panels at 390px
	and desktop widths.
- Keep the source decision primary and derived signals visibly separate.
- Add lightweight bookmarks or a temporary case set only if they directly
	support the demo; defer a full workbench.

Acceptance check: researchers can complete the primary workflow on desktop and
mobile without losing context or confusing derived evidence with source text.

## Priority 3: Evidence-Led Demo Package

Make the working product repeatable and easy to present.

Deliverables:

- Define a bounded demo corpus manifest with representative issue/type scenarios
	across Federal Court, FCA, and SCC decisions where available.
- Add browser checks for discovery, reader tabs, summary/structure toggles,
	citations, statutes, linked authorities, and return navigation.
- Add a short demo script with the research question, expected path, and
	evidence to inspect.
- Document incomplete enrichment, unresolved references, and non-authoritative
	derived signals.
- Provide a simple local startup and recovery path for demonstrations.

Demo release criteria:

- At least three curated issue/type scenarios produce useful results.
- A new user reaches a relevant reader in under two minutes.
- The discovery-to-evidence-to-authority journey needs no manual database work.
- Every displayed derived signal is traceable or explicitly labeled unavailable.
- No broken links, misleading blank states, or uncaught browser errors occur.
- Desktop and 390px mobile layouts remain usable.
- The demo does not imply complete legal coverage from the curated corpus.

## Deferred Track: Corpus Quality And Research Depth

The following work remains planned, but follows the demo milestone:

- Citation anchor and unresolved-reference backfills.
- Paragraph-chunk rebuild measurement and application.
- Corpus-wide quality gates for orphan links, malformed references, missing
	metadata, duplicate edges, and embedding coverage.
- Broader statute identity and provenance-aware authority-bank expansion.
- Corpus-wide Discussion Unit/sub-theme coverage and evaluation.
- Retrieval benchmarks, performance baselines, and release thresholds.
- Citation context, citation-purpose classification, distinguishing treatment,
	research-gap detection, and authority recommendations.
- Saved research workbench, evidence exports, and collaboration features.
- Novel-reasoning detection, monitoring, forecasting, and advanced intelligence.

Only demo-safety fixes are active before this track resumes. A demo-safety fix
prevents a broken link, false source claim, misleading empty state, or
untraceable displayed proposition; it does not attempt to make the whole corpus
complete.

## Product Boundaries

- `/data-explorer` remains the active product workflow.
- `/case-reader` remains a compatibility redirect.
- `/citation-pass` remains an internal extraction QA surface.
- Source text and backend-owned offsets remain authoritative.
- Citations, statutes, tags, metadata, outcomes, and embeddings remain separate
	evidence layers.
- Structure and summary views are research aids, not legal conclusions or
	AI-generated advice.
- Curated scenarios must be labeled curated and must not imply full coverage.

## Success Measures

Track time from issue/type selection to first relevant case, completion of the
discovery-to-reader-to-authority path, curated scenarios completed without
manual intervention, browser errors and broken links, desktop/mobile usability
issues, and evidence traceability for visible derived signals. After the demo
milestone is stable, resume the deferred quality track with explicit baselines
and release gates.

## Objective

This roadmap converts the long-term backlog in `MASTER_IDEAS.md` into a practical delivery plan focused on:

1. Research quality and trust.
2. Product usability for legal workflows.
3. QA maturity and release safety.

## Active Corpus Rebuild Sequence

The current delivery priority is to establish trustworthy, explainable data
layers across the full corpus before investing in interface polish or semantic
features. This sequence supersedes the older feature-first ordering below for
the duration of the rebuild.

### Stage 1: Deterministic evidence layers

1. Finish statute and legal-instrument extraction, authority coverage, current
	resolution, and UI-ready evidence fields.
2. Replace the legacy tagging target with a narrow, non-contextual `ca_legal_v3_core`
	whitelist. Preserve V1/V2 rows for comparison and rollback, and require
	reviewed acronym/full-name, spelling, spacing, hyphenation, and explicitly
	tested plural aliases with exact-span regression fixtures. Do not activate
	 contextual tags in the first V3 release; defer actor, proximity, evidence-role,
	 negation, and procedural-context rules until the core canary passes.
3. Add a focused outcome/case-result layer. Outcomes are foundational derived
	intelligence, but remain separate from source metadata and tags.

### Stage 2: Corpus processing

4. Run the complete deterministic pipeline across the bounded 60K-case corpus:
	case text, full/section/paragraph chunks, metadata, citations, statutes,
	tags, and outcomes.
5. Run statute and authority resolution against the populated current library.
	Preserve unresolved and ambiguous references for later incremental passes.
6. Harden and run case-citation resolution and pinpointing across the corpus.

The extraction pass must finish before broad resolution passes. Resolution may
run against the authorities already available and be repeated incrementally as
the authority library expands; it must not rewrite raw occurrence text or
offsets.

### Deferred quality backlog

	repair in task 096, run a bounded dry-run rebuild for affected cases. Compare
	paragraph coverage, duplicate ranges, inflated numeric markers, and newly
	linkable citation pinpoints before authorizing any stored-chunk rewrite.

	statute extraction and IRPA/IRPR nested-provision coverage toward a populated
	authority bank. Keep extraction, structured provision identity, authoritative
	source text/provenance, and reader evidence links as separate contracts. The
	first implementation slice should add structured provision identity and a
	read-only resolution report before any broad source acquisition or corpus
	writer. See task 097 for the evidence-backed review and phased plan.

#### Legal authority evidence plan

The current extraction layer is not the authority bank. It identifies statute
references and preserves occurrence spans, while `statute_references.pinpoint`
stores the provision as an opaque string. `LegislationDocument` and
`LegislationSection` provide a schema direction but are not yet populated by a
versioned, provenance-aware source pipeline.

Architecture options considered:

1. **Keep live parsing only:** lowest immediate cost, but repeated parsing,
	weak cross-case queries, and no durable authoritative section evidence.
2. **Structured provision identity only:** add parsed instrument/provision
	components and queryable ranges while keeping source text separate. This is
	a useful low-risk first slice, but cannot by itself prove the linked text is
	authoritative or current.
3. **Structured identity plus a provenance-aware authority bank:** version
	source documents and sections, retain terms/licence/hash/effective dates,
	resolve references deterministically, and expose section evidence. This has
	the highest setup cost but best accuracy, explainability, maintenance, and
	reader trust. It is the recommended direction, delivered incrementally.

Phased delivery and gates:

1. **Provision identity and measurement:** owner `backend/citations.py`,
	`backend/database.py`, and focused statute tests. Add structured fields or a
	child provision table for instrument, section/subsection/paragraph,
	nesting, lists, and ranges without removing raw text. Gate: IRPA/IRPR gold
	fixtures including `34(1)(f)`, positive/negative/exact-span tests, and a
	read-only corpus report of parseability and ambiguity.
2. **Authority source contract:** owner legislation ingestion/source register.
	Define source authority, version, effective dates, licence/terms, retrieval
	hash, and update cadence before importing a broad bank. Gate: a small
	approved IRPA/IRPR source set with reproducible section extraction and
	provenance checks. External acquisition and licensing decisions require
	explicit approval.
3. **Reference resolution:** owner legislation resolution service. Resolve a
	structured statute reference to one or more versioned authority sections,
	preserving unresolved/ambiguous states and match evidence. Gate: bounded
	precision/recall and no silent resolution when versions or provisions are
	ambiguous.
4. **Reader evidence:** owner `backend/reader_service.py`, routes, and active
	Data Explorer UI. Link the occurrence to the exact authority section text,
	show source/version/provenance, and retain the case-text occurrence link.
	Gate: API contract and browser checks for nested, range, and unresolved
	references.
5. **Coverage expansion:** owner source adapters and evaluation. Add other
	Canadian instruments and international materials only after the IRPA/IRPR
	gate is green; track extraction pickup separately from cleanliness.

The smallest experiment that could disconfirm the recommended direction is a
bounded IRPA/IRPR slice: parse ten representative cases, resolve structured
provisions against an approved section fixture, and verify that each reader
link opens the exact section text with source version and provenance. Failure to
maintain exact-span precision or source traceability blocks expansion.

### Stage 3: Usable research product

7. Repair the current UI around the stabilized data contracts: search, reader,
	statute/citation highlights, authority links, tags, outcomes, unresolved
	states, and evidence inspection.
8. Add browser/API workflow checks for the primary Data Explorer research path.

### Stage 4: Retrieval and intelligence

9. Add semantic embeddings only after deterministic data and UI evidence are
	stable, measured, and searchable. Embed both paragraph and section chunks so
	retrieval can capture precise local reasoning and broader doctrinal context.
	Keep text/reasoning, authority-signature, and metadata/outcome signals
	separable rather than forcing all information into one undifferentiated
	vector.
10. Continue with semantic retrieval, authority recommendations, clustering,
	 research-gap features, and other intelligence capabilities. This is the
	 first stage where the project can safely turn the completed evidence layers
	 into higher-level research intelligence.

### Rebuild exit criteria

  repeatable layers with bounded rerun commands.
  deterministic legal evidence.

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

2. Why-Is-This-Cited Classifier

3. Research Gap Detection

4. Distinguishing Citation Detection

### P1: Product Workflow And Research UX

1. Research Workbench

2. Citation Heat Maps

3. Related Case Discovery (Citation-Only Mode)

4. Authority Recommendation Engine

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

## New QA Streams To Add

1. Data quality audits

2. Retrieval quality benchmarks

3. Performance and scale tests

4. Safety and governance checks
5. External citation audits

## Suggested Quality Gates

1. Required for merge:

2. Required for release:

## Success Metrics

By end of Phase 4, target:

1. Research quality:

2. Trust and explainability:

3. Reliability:

4. Usability:

## Immediate Next Actions (This Week)

1. Use the completed live statute/source coverage audit and resolution sample
	to classify missing-section, unindexed-section, range/list, and unidentified
	references before changing resolver behavior; keep the 10,107-reference
	Immigration Act gap as a separate source-approval decision.
2. Expand law regressions for French forms, Parts/Schedules, additional treaties,
	and safe short-form anchor boundaries.
3. Repair the unrelated FC document-scraper test collection error and establish
	a new full-suite baseline.
4. Define endpoint SLO budgets for `/search/chunks/grouped` and top
	`/citation-map/*` surfaces.
5. Add CI stages for extraction quality, performance smoke, and API/export
	contract checks.
