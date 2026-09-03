# Research UI Guide

Last reviewed: 2026-09-01

This guide explains the active iLIT research interfaces, their controls, and how to interpret what they display. The application is a research aid. Source text, source status, and legal propositions must be verified independently.

## Start Here: Data Explorer

Open `/data-explorer`. This is the active research workspace. It has eight top-level tabs:

| Tab | Primary purpose | Main data layer |
| --- | --- | --- |
| About | Live system inventory and coverage | `/api/about/stats`, outcome series |
| Case search | Find and read decisions | `cases`, citations, chunks, metadata |
| Site Architecture | Explain live tables and derived views | Documentation/UI explanation |
| Citation Intelligence | Examine authority use for a selected case | citations, metrics, tags |
| Judge outcomes | Compare recorded outcome classifications by judge | cases, judge profiles, metadata |
| Judge Profile | Inspect canonical judge identity and linked decisions | judge profiles/links |
| Data explorer | Inspect source/case inventory views | cases, sources, metadata |
| FC History | Look up procedural/activity context by IMM number | FC procedural/activity tables |

The tab labels are navigation, not proof that every data layer is complete for every case. Empty states mean the relevant source, enrichment, or linkage is absent from the current database.

## About

About shows live counts rather than hard-coded documentation figures. It describes cases, chunks, citation rows, resolved case links, judge profiles, Federal Court activity records/documents, and coverage-style status labels.

Use it to understand available inventory, not legal relevance. A populated layer means records exist; it does not establish extraction precision, source authority, or complete corpus coverage. The outcome chart uses classified decisions only. Hover a point to see the classified count behind a rate before comparing years.

## Case Search

### Basic Search

Enter a case name or citation, for example `Vavilov` or `2019 SCC 65`. The default path favors title/citation matching. This is intentional: it keeps the common authority-lookup workflow fast and avoids broad full-text matches unless requested.

Choose a result count and sort order:

- **Newest decision**: date-first ordering.
- **Most cited / newest**: relevance-oriented ordering with citation context and recency behavior.
- **Oldest decision**: date-first ascending ordering.
- **Minister / government party (A-Z)**: alphabetical government-actor ordering where recorded.

### Advanced Controls

Open Advanced options to narrow the candidate set. Available filters include cited authority, government outcome, decision outcome, judge, court, date/year, minister/government party, source type, and other metadata-oriented constraints. Court abbreviations such as `FC`, `FCA`, and `SCC` expand to their canonical court names.

Enable **Search full decision text** only when the research question requires text passages rather than named authorities. Full-text matching broadens results and can be slower or noisier than title/citation lookup.

### Reading Result Metadata

Search result cards can show case identity, court/date, source context, outcome labels, and citation counts. A citation count is an occurrence count, not a count of legally controlling authorities. A resolved link means the system matched the citation to a case in the local library; it does not verify the proposition for which it was cited.

## Inline Decision Reader

Open a result to enter the reader. The reader replaces the search panel until closed, preserving an explicit return to search.

### Reader Layout

| Pane | Content | Research use |
| --- | --- | --- |
| Case information | Canonical fields, extracted metadata, tags, citation metrics, source/provenance, and related panels | Confirm identity, source, and enrichment state |
| Decision text | Chunk breakdown or full formatted text | Read the decision and inspect evidence spans |
| Case context | Selected linked authority and related context | Compare cited authority without losing the source decision |

The side panes are resizable on larger screens and can stack on smaller displays. Case information can be collapsed. Reader panes scroll independently so linked authority context does not force the decision text away from its current position.

### Reader Modes

- **Chunk breakdown**: displays stored decision chunks with labels/paragraph context. This is the evidence-oriented mode for inspecting citation and statute spans.
- **Full text**: uses sanitized source HTML when available to preserve source formatting; otherwise uses stored normalized decision text with citation highlights.

Source formatting supports reading, while stored chunk text and offsets remain the evidence location of record. A visual source paragraph is not a substitute for the persisted chunk/offset reference.

## Live Analysis

Open `/live-analysis` to inspect a document without adding it to the case library.
The temporary reader displays extracted source text, highlights case citations and
statute references in place, and provides an evidence inspector with paragraph or
PDF page, offsets, context, and resolution status.

Accepted formats are `.docx` and text-based `.pdf`, up to 10 MB. Scanned PDFs are
not OCR'd by this prototype. Enable **Resolve local matches** when neutral
citations should be checked against existing local case metadata. Resolution is
batched and read-only; it does not save the upload or create derived database
records.

### Highlight Types And Linked Authorities

- Case-citation highlights identify stored case-law references.
- Statute/instrument highlights identify independently stored law references.
- A citation with a resolved target is interactive. Selecting it loads the matched authority into the context pane.
- Hover text can show a target-authority preview. It is deliberately viewport-positioned so it does not get clipped by the chunk containing the citation.

No highlight means one of several things: the case may have no stored rows, its relevant enrichment may not have been run, its offsets may not validate against the displayed text, or the source formatting mode may not map directly to chunk evidence. Use Citation Pass before changing extraction logic.

### Case Information Panels

Reader panels can expose case details, citation rows, evidence/provenance, quality/QA context, citation intelligence, Federal Court activity, legal tags, and Acts/Regulations. The Acts/Regulations panel is backed by the separate statute-reference layer; it is not a case-citation graph view.

## Citation Intelligence

Citation Intelligence starts with a title search or a case selected from Case Search. It provides bounded views over resolved case-citation data:

- **Overview**: citing decisions, total mentions, average/max mentions, and related high-level authority signals.
- **Timeline**: year-based use over time.
- **Outcomes**: classifications among citing decisions where available.
- **Courts/Judges**: attributed citation use by court or canonical judge data where available.
- **Statutes**: statute references appearing alongside authority use.
- **Evidence/table views**: stored citation rows, offsets, and target context.

Interpret these views as navigation and prioritization aids. A citation increase can reflect corpus coverage, extraction changes, or genuine usage change. An outcome association does not show that an authority caused an outcome.

## Judge Outcomes And Profiles

Judge Outcomes aggregates stored classifications. It shows decisions, government wins, individual wins, unclassified rows, and a government-win percentage among classified decisions. Use minimum-decision thresholds before making comparisons; unclassified cases and source/classification gaps matter.

Judge Profile resolves a canonical judge identity, aliases, primary court, linked cases, and available outcome/year information. It is intended to reduce name variation, not to claim a complete judicial record or infer individual bias.

## Data Explorer And FC History

Data Explorer is an inventory-oriented research tool. It supports inspection of case/source records and aggregate group/split views. Use it to understand coverage, source composition, processing state, and structured field availability.

FC History accepts an IMM number such as `IMM-1234-19` and presents stored/proxied Federal Court procedural history and available activity context. Treat it as procedural/activity context, not official judgment reasons. A matching IMM number alone does not prove all linked records are the same proceeding.

## Supporting Interfaces

| Route | When to use it | Caution |
| --- | --- | --- |
| `/case-reader` | Compatibility redirect for legacy bookmarks | Redirects to the active Data Explorer case reader |
| `/citation-map` | Explore maps, paths, authority relationships, and CSV exports | Graph relationships are derived from resolved rows and bounded queries |
| `/citation-pass` | QA extraction spans, normalization, and stored-versus-live results | QA interface, not normal legal research workflow |
| `/quick-search` | Lightweight search experimentation | Not the full advanced research workspace |
| `/testing`, `/prototype` | Testing/legacy exploration | Do not treat their UI copy or behavior as the active product contract |

## Research Workflow

1. Start with Case Search using a citation or authority name.
2. Add court/date/source/outcome/judge filters only when they answer a real inclusion question.
3. Open a decision and confirm title, court, date, citation, source, and available text.
4. Read chunks/full text and inspect highlighted citations/statutes in context.
5. Open linked authorities only after checking that the link is resolved and the target identity is plausible.
6. Use Citation Intelligence/Citation Map to find relationships, context, and potential follow-up authorities.
7. Verify critical propositions against authoritative sources before relying on them in legal work.

## Common Interpretation Errors

1. Do not treat a similarity score as a legal relevance judgment.
2. Do not treat a citation link as confirmation of a legal proposition or treatment status.
3. Do not compare outcome rates without checking classified counts and source coverage.
4. Do not mix statute-reference counts with case-citation counts.
5. Do not assume a missing highlight proves a source text lacks a citation.
6. Do not call a staged/discovered record an official captured decision.
7. Do not use generated labels, tags, or analytics as legal advice.