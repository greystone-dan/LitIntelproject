# Task: Statute and law authority resolution strategy

Status: in-progress
Created: 2026-09-04
Updated: 2026-09-04

Why now: Statute extraction has a small exact-span fixture gate but lacks a
versioned authority library and measured corpus-level resolution quality.

Owner surface: `backend/statutes.py`, `backend/citations.py`, legislation
authority staging, `statute_references`, and statute evaluation fixtures.

Dependencies: official Justice Laws source material, existing legislation
tables, current deterministic extraction rules, and human-reviewed gold
fixtures.

Risk boundary: Do not mix statutes with case citations or tags, lose offsets,
silently resolve ambiguous provisions, overwrite existing occurrence evidence,
or run an unbounded authority/corpus refresh.

Commit allowed: yes

Push allowed: yes

## Product outcome

When a decision mentions a statute or law, the system should preserve the exact
mention, identify the instrument and provision intended, resolve it to an
authoritative section in a versioned legal library when possible, and expose the
source-backed target for highlighting and inspection. A reference must remain
useful even when it is abbreviated, nested, ambiguous, historical, or unresolved.

## Goals

1. Extract every statute/instrument occurrence with backend-owned exact offsets,
   raw text, normalized identity, kind, and source context.
2. Resolve unambiguous references such as `34(1)(f) of the IRPA`, `IRPA s.
   34(1)(f)`, `IRPR 245(1)(c)`, and `Criminal Code, s. 36` to canonical
   provision identities.
3. Preserve hierarchical legal identity: instrument -> section -> subsection ->
   paragraph -> subparagraph, without flattening `34(1)(f)` into `34`.
4. Preserve authority provenance: official source URL, source family, retrieval
   date, publication/version date, content hash, language, and licence/terms.
5. Make ambiguity explicit. Never guess between instruments, versions, or
   provisions when the text does not distinguish them.
6. Support source-backed highlighting and a provision inspector after extraction
   and resolution quality gates pass.

7. Expand authority coverage from observed corpus demand. The detector remains 
   broad and source-independent; the authority library is added in priority
   order based on reference frequency, research value, and source quality.

## Non-goals for the first release

- Do not use an LLM as the authority of record or automatic resolver.
- Do not silently rewrite existing statute-reference rows.
- Do not merge statutes with case citations, tags, or embeddings.
- Do not ingest every Canadian statute before the IRPA/IRPR path is reliable.
- Do not treat a section number alone as sufficient evidence of an instrument.

## Recommended architecture

### 1. Authority library

Create a versioned, provenance-aware authority layer separate from case text:

- `statute_instruments`: canonical key, title, jurisdiction, language, source
  family, official URL, version/effective dates, retrieval timestamp, hash, and
  licence/terms.
- `statute_provisions`: instrument version, hierarchical parent, section label,
  normalized path, display label, provision text, source offsets or anchors, and
  source URL.
- `statute_aliases`: abbreviations and title variants such as IRPA, IRPR,
  Immigration and Refugee Protection Act, Regulations, Criminal Code, and
  bilingual forms.

The existing `statute_references` table remains the occurrence layer. Extend it 
only after the pilot proves the identity contract, with nullable resolution
status, target provision/version, resolver method, confidence, and ambiguity
reason. Existing raw text and offsets remain authoritative.

### 2. Deterministic extraction

Keep extraction separate from resolution. Recognize explicit instrument names,
accepted abbreviations, section markers, nested forms, lists, ranges, French
forms, and common legal shorthand. Emit one occurrence per source span and keep
duplicates. Negative fixtures must cover unanchored numbers, exhibit numbers,
case paragraph references, and ordinary prose.

### 3. Deterministic resolution

Resolve in ordered passes:

1. Explicit title/abbreviation plus provision.
2. Explicit instrument plus section list/range expansion.
3. Named instrument without provision.
4. Contextual alias only when a bounded document context establishes the
   instrument.
5. Unresolved/ambiguous outcome when evidence is insufficient.

Resolution should return a structured result, not replace the extracted text: 
`resolved`, `ambiguous`, `unresolved`, or `not_a_provision`, with candidate
provisions and reasons where applicable.

Detection does not depend on an instrument already being in the authority
library. Resolution runs immediately against the authorities currently loaded
for current-version research. Once historical versioning is implemented, a
case occurrence must resolve against the instrument version in force for the
case's relevant date; later source updates must create new authority versions,
not retarget existing historical occurrences. A recognized reference with no
loaded authority remains preserved and highlightable as `unresolved` until an
appropriate version is available.

### 4. Evidence and UI

The reader should highlight the extracted source span, display normalized
identity and resolution status, and link to the authority-library provision.
The provision view should show source/version/provenance and the hierarchical
path. Browser code must consume backend offsets and must never calculate them.

## Delivery phases and gates

### Phase 0: Contract and gold set

Expand the current four-fixture baseline into a human-reviewed statute set with
positive, negative, nested, list/range, bilingual, historical, and ambiguous
examples. Start with at least 100 occurrences across IRPA/IRPR and a meaningful
negative set. Record expected exact spans, instrument identity, provision path,
resolution status, and ambiguity rationale.

Gate: extraction precision, recall, and exact-span accuracy are reported 
separately. No corpus rebuild.

### Phase 1: IRPA/IRPR authority library

Acquire official Justice Laws source material through a bounded, reproducible
importer. Parse section hierarchy, preserve language and version metadata, hash
source files, and produce a read-only manifest before writing canonical rows.

Gate: every pilot target such as `34(1)(f)`, `34(1)`, `72(1)`, `96`, `97(1)`,
`112`, and `245(1)(c)` resolves to the correct hierarchical provision, with
historical/version behavior explicit.

### Phase 2: IRPA/IRPR resolution

Add resolver indexes for aliases and normalized provision paths. Evaluate exact
reference resolution independently from mention extraction. Keep unresolved and
ambiguous cases visible for review.

Gate: target resolution >=95% on unambiguous human-reviewed references, with 
silent wrong target; ambiguous references must not be promoted as resolved.

### Phase 3: Bounded corpus evaluation

Run extraction and resolution on progressively larger, read-only samples across
FC, FCA, SCC, and immigration tribunal material. Report occurrence counts,
precision, recall, exact spans, resolution accuracy, unresolved rate, ambiguity
rate, and coverage by instrument/provision form.

Gate: no regression in IRPA/IRPR fixture metrics, no offset failures, and no
corpus writes until the report is reviewed.

### Phase 4: Criminal Code and adjacent instruments

Add Criminal Code as the next authority family using the same importer,
provision hierarchy, alias table, resolver contract, and gold-set gates. After
that, rank additional instruments by bounded corpus frequency, unresolved
occurrence count, research importance, source availability, and version risk.
Extend only when IRPA/IRPR remains stable.

### Expansion policy

At each evaluation checkpoint, produce a ranked authority-demand report:

- normalized instrument mentions and aliases;
- unresolved occurrence count and case/court distribution;
- provision-shape distribution, including nested and list forms;
- estimated research value and source/provenance readiness;
- proposed next authority family and a bounded gold-set size.

Add a source family only after its demand is visible and an authoritative,
versioned source can be staged. Never let library breadth force silent changes to
the detector or convert unresolved mentions into discarded data.

### Phase 5: Highlighting and research workflow

Expose statute highlights, provision links, authority previews, and filters in
`/data-explorer` and live analysis. Add browser checks only after backend spans
and resolution contracts are stable.

## Quality metrics

Report these separately; never use exact-span validity as a substitute for legal
resolution accuracy:

- Mention precision: emitted mentions that are true statute references.
- Mention recall: gold references detected.
- Exact-span accuracy: expected source span preserved exactly.
- Instrument accuracy: correct Act/Regulation/Code identity.
- Provision accuracy: correct hierarchical target, including nested forms.
- Resolution precision: resolved targets that are correct.
- Ambiguity discipline: ambiguous inputs not incorrectly auto-resolved.
- Provenance completeness: resolved targets with source/version/hash metadata.

Initial release gates: 100% exact spans on the gold set; at least 95% mention
precision/recall and unambiguous provision resolution on the reviewed pilot;
zero silent wrong-target promotions; complete provenance for every authority
source and resolved provision.

## Alternatives considered

1. **Deterministic extractor plus canonical authority library (recommended).**
   Highest explainability, strongest exact-span behavior, bounded operating cost,
   and compatible with existing citation architecture. Requires source parsing
   and version management.
2. **External legal API as the primary resolver.** Faster initial breadth, but
   introduces availability, licensing, version, and provenance risk. It can be
   an optional comparison or enrichment source, never the sole authority.
3. **LLM/RAG resolution first.** Useful for candidate generation and difficult
   language, but weak for deterministic offsets, repeatability, legal version
   identity, and auditability. It should remain suggestion-only for adjudication.

## Smallest falsifiable pilot

Build a read-only IRPA/IRPR authority manifest and a 100-occurrence gold set.
Require exact extraction for `34(1)(f)` and related nested/list forms, then resolve
only explicit instrument references to provision paths. The pilot fails if it
cannot distinguish `34(1)(f)` from `34(1)`, loses source spans, or resolves an
ambiguous reference without recording ambiguity.

## Owner and validation

Owner surface: `backend/citations.py`, a new authority-library importer/resolver
module, `statute_references`, and statute evaluation fixtures.

Focused validation: `.\venv\Scripts\python.exe scripts\evaluate_statute_extraction.py` plus resolver-specific tests and a bounded read-only authority import. No database refresh or migration until the pilot contract is accepted.

Docs/generated references: update `SYSTEM_REFERENCE.md`, the statute section of
the Swimm processing/evaluation walkthrough, and generated script/schema
references only through their generators.

Rollback/recovery: keep authority imports staged and versioned; do not replace
existing occurrence rows during pilot work. Remove or roll back the new resolver
and staged authority snapshot without altering canonical case text or existing
case/statute occurrence evidence.

## Current checkpoint

Capability assessment: deterministic extraction already covers IRPA/IRPR nested
forms, Charter, Criminal Code, international instruments, exact offsets, and
separate statute persistence. Existing authority storage includes
`legislation_documents` and `legislation_sections`; current resolution is still
primarily a URL/identity parser rather than a versioned provision resolver.

Implemented slice: created `backend/statutes.py` as the modular legislation
identity boundary, moved the registry/parser behind it, centralized canonical
instrument names, and added `canada.criminal_code` identity support. The
existing `backend.citations` imports remain compatible. Extraction, offsets,
statute occurrence persistence, and case-citation behavior were not rewritten.

Evidence: statute/citation/evaluator tests passed (`107 passed`); adjacent
pipeline, live-analysis, and API tests passed (`50 passed`); baseline evaluator
passed 4 fixtures, 5 expected matches, 100% precision, 100% recall, 100% exact
spans, and zero false positives/negatives. The baseline remains a small fixture
gate, not a corpus-wide accuracy claim.

Next gate: run a bounded resolution pass against the currently indexed
authorities, preserving unresolved status for instruments not yet catalogued.
The 100-occurrence IRPA/IRPR gold set and versioned authority manifest remain
quality improvements, not prerequisites for current-library resolution.

## Larger subset checkpoint

The gold-set step is intentionally deferred by user direction. A read-only
250-case scan was run across FC=125, FCA=62, and SCC=63, producing 8,142
statute/instrument occurrences and 2,522 distinct normalized references. Every
occurrence retained a UI-ready raw span, normalized identity, source hash,
instrument candidate, pinpoint, line/paragraph offsets, context excerpt, and
explicit resolution status; exact spans were valid for 8,142/8,142 records.

Registry expansion identified 6,095 occurrences (74.9%) across the current
authority catalogue, reducing unidentified instrument occurrences from 4,490
to 2,047 without changing extraction spans. Added high-demand catalogue entries
include Immigration Act, Citizenship Act, Federal Courts Act/Rules, Income Tax
Act, Marine Liability Act, Commercial Arbitration Act, Coastal Fisheries
Protection Act, and the Refugee Convention.

The next demand-ranked candidates are Immigration Regulations (37), Canada Act
(35), Indian Act (25), Constitution Act (23), Bankruptcy Act (17), Federal
Court Rules (16), RPD Rules (16), and IRP Regulations (16). Residual phrases
such as `Statutes and Regulations` and `Judicial Review of Administrative Act`
must be adjudicated as likely extraction noise before being added to the
authority library.

## Current-version provision resolution checkpoint

Implemented the current-version UI resolution path in `backend/live_analysis.py`.
An explicit reference such as `Criminal Code, s. 361(1)` now returns the
instrument key, pinpoint, containing section number, exact Justice Laws section
URL, full indexed section text, a subsection excerpt when the flattened source
text permits it, and a resolution status of `resolved_provision` or
`resolved_section`. Unresolved references retain their extracted identity and
return `unresolved` rather than being discarded.

The source library currently contains 10 official Justice Laws XML documents and
4,432 indexed sections. The live database-backed smoke check resolved Criminal
Code `361(1)` to section `361` and returned the subsection text. Focused live
analysis and citation tests passed (`113 passed`). Historical-version handling
remains intentionally deferred to the versioning backlog item.
