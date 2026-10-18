# AI CaseLibrary Product Roadmap

Last updated: 2026-10-17

## Current Direction

The near-term goal is a compelling demo product for Canadian immigration
litigation research. The system already has a substantial deterministic
foundation, so delivery now prioritizes showing its value clearly over broad
corpus expansion or exhaustive quality work.

The consolidated cross-project backlog, accuracy gaps, deferred research, and
implemented-feature guardrails are maintained in
[docs/STILL_TO_DO.md](docs/STILL_TO_DO.md). Use it to select a bounded next
task; this roadmap remains authoritative for product direction and sequencing.

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
	support the demo; defer further full-workbench workflow expansion. Existing
	Workbench and prototype surfaces remain part of the current interface.

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
