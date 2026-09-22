# Long-Term Intelligence Vision

Last updated: 2026-09-22
Status: Strategic direction; not an implementation commitment

## Purpose

AI CaseLibrary should eventually help a researcher answer not only **which
cases are related**, but also:

- what legal issue or decision was being considered;
- what each party argued and what evidence or authority supported the argument;
- how an authority was used in context;
- how the judge responded to the argument and authority;
- whether the argument succeeded, failed, was limited, or was left unresolved;
- how those findings relate to the final disposition; and
- whether the same argument appears, changes, or receives different treatment
  across cases.

This document preserves that direction as a long-term architecture. It does
not claim that the proposed intelligence exists today. The active system is a
provenance-first research aid, not legal advice. Source decisions and stored
backend evidence remain authoritative; derived signals must remain traceable,
versioned, reviewable, and explicitly uncertain.

## Product Outcome

The long-term product outcome is a researcher-facing evidence graph that makes
reasoning comparable without pretending that legal reasoning is a flat list of
tags or a single case outcome.

The intended chain is:

```text
Case
  -> proceeding and decision under challenge
  -> Decision Units
  -> issues, propositions, arguments, evidence, and authorities
  -> citation events and citation treatment candidates
  -> judicial response
  -> argument outcome
  -> case disposition
```

The chain is deliberately layered. A citation is not a treatment. A treatment
is not an argument outcome. An argument outcome is not the same as the case
disposition. Each relation must point back to source text and preserve the
uncertainty introduced by extraction, normalization, or inference.

## Current Baseline

The recent implementation establishes a credible deterministic foundation:

- source records, decision text, hashes, provenance, and backend-owned offsets;
- paragraph and section chunks with stable source identity;
- deterministic case citations, target resolution, statute references, tags,
  metadata, outcomes, and embeddings as separate layers;
- Discussion Units and sub-theme roles as read-only contextual evidence;
- a deterministic seven-section case summary with explicit unavailable states;
- report-only recent-case theme discovery with explainable classification factors;
- an active `/data-explorer` research workflow and compatibility redirect for
  `/case-reader`.

Tasks 134-137 demonstrate the intended operating pattern: derive a useful
research projection, retain evidence and limitations, validate it on a bounded
cohort, and avoid canonical writes until its quality is understood. The current
Discussion Unit and sub-theme work is a foundation for the vision, not proof
that corpus-wide argument extraction is solved.

Known baseline limitations include citation anchor gaps, unresolved references,
statute identity gaps, uncertain sub-theme role context, segmentation edge
cases, and theme thresholds that have not yet received corpus-wide legal review.
These limitations are inputs to the roadmap below, not reasons to hide the
future model.

## Scope And Non-Goals

### In scope

- citation use and treatment in decision context;
- dynamic multi-paragraph Decision Units;
- issues, legal propositions, party positions, evidence, authorities, and
  judicial response;
- Argument Packets as a traceable comparison projection;
- retrieval and comparison by argument, authority, issue, and response;
- deterministic and probabilistic boundaries;
- evaluation, human review, versioning, and rollback.

### Not an immediate commitment

- a local generative LLM deployment;
- automatic legal advice or a conclusion that an argument is legally correct;
- opaque semantic clustering as a replacement for evidence extraction;
- canonical persistence of themes, Decision Units, or Argument Packets before
  quality gates pass;
- a complete authority bank or complete citation graph;
- automatic prediction of future outcomes;
- a claim that cross-case comparison is exhaustive.

## The Two Intelligence Systems

The long-term design has two related systems with separate ownership and
validation needs.

### 1. Citation-treatment intelligence

This system explains how a decision uses an authority. It starts from a stored
citation occurrence and reconstructs its local context. It may eventually
classify a citation as, for example, following, distinguishing, limiting,
criticizing, applying, quoting, relying on, contrasting, or merely mentioning
an authority. These are treatment candidates until supported by evidence and
review.

The same case can cite the same authority several times for different purposes.
Treatment therefore belongs to a citation event or a small event group, not to
the case-to-case edge alone.

### 2. Dynamic Decision Unit intelligence

This system identifies coherent reasoning episodes that may span several
paragraphs and may not align with headings or fixed chunk windows. A unit can
contain an issue, a party position, evidence, a governing rule, application,
a counterargument, and a conclusion. It may contain one main argument, several
closely related arguments, or an explicit transition to another issue.

Decision Units are not a new source layer. They are versioned projections over
source paragraphs, sections, citation events, statute references, tags, and
metadata. Every unit must be reconstructible from those underlying records.

### Composition

The systems should remain independently useful:

- citation treatment can be reviewed without accepting an argument extraction;
- Decision Units can organize reader evidence without classifying treatment;
- an Argument Packet can join them only through explicit source-backed links;
- a failed treatment classifier must not invalidate citation extraction;
- a changed segmentation version must not silently rewrite source identity or
  citation offsets.

## Core Vocabulary

### Case

A canonical judgment or decision with source identity, text, metadata, and
provenance. A case may include several source representations, but the source
ledger and canonical merge rules remain authoritative.

### Proceeding type

The procedural setting or kind of proceeding, such as an application for
judicial review, appeal, detention review, or an immigration decision review.
It describes the proceeding, not necessarily the administrative decision being
challenged.

### Decision under challenge

The administrative, tribunal, or procedural decision under review, such as a
cessation decision, refugee protection decision, inadmissibility decision,
removal decision, or humanitarian and compassionate decision. This field must
remain distinct from broad proceeding labels and broad themes.

### Theme

A controlled, broad research grouping such as credibility and evidence,
procedural fairness, or removal and stays. Themes support discovery but do not
replace an issue or argument. Theme matches should retain evidence kinds and
classification factors.

### Issue

A narrower legal or factual question actually addressed in a decision. An
issue can be derived from metadata, explicit issue language, argument roles,
statutes, or reviewed semantic normalization. It must remain linked to the
Decision Units that support it.

### Legal proposition

A claim that can be stated as a proposition and checked against a span of
text, authority, statute, or reasoning. A proposition is not simply a tag. It
should record its source spans, role, speaker or owner where known, and
normalization status.

### Argument

A structured position or reasoning claim concerning an issue. An argument may
include a party position, evidence, legal rule, application, counterargument,
and conclusion. The system should allow arguments to be incomplete when the
source does not expose every role.

### Decision Unit

A contiguous or explicitly linked set of source paragraphs that forms a
coherent reasoning episode. The primary representation should preserve ordered
paragraph IDs, source hashes, document offsets, section context, and the
signals used to choose the boundary.

### Citation event

One occurrence of a case-law citation, including its source span, normalized
form, target if resolved, pinpoint, anchor provenance, and containing
paragraph or Decision Unit. A case may have many events for the same target.

### Citation treatment

A contextual relationship between a citation event and the proposition or
reasoning episode in which the authority is used. Treatment is an observed or
candidate use, not a property of the target authority itself.

### Judicial response

The judge's treatment of a party position, proposition, evidence, or cited
authority. Possible states may include accepted, rejected, limited,
distinguished, unresolved, or not detected, but the vocabulary must be
validated against legal review and source evidence.

### Argument outcome

The result for a particular argument or proposition, such as succeeded,
failed, partly accepted, not reached, or unresolved. It is narrower than the
case disposition.

### Case disposition

The final result of the proceeding, such as application allowed, dismissed,
remitted, or withdrawn. It must not be back-propagated as proof that every
argument succeeded or failed.

### Argument Packet

A traceable projection that bundles one issue or argument across its Decision
Units, propositions, evidence, authorities, citation events, treatment
candidates, judicial response, argument outcome, and source links. It is a
research object for comparison, not a replacement for the source decision.

## Proposed Data Model

The future model should be additive and versioned. Exact table names are an
implementation decision for a later schema task.

```text
SourceRecord
  -> CanonicalCase
    -> DecisionDocument
      -> Section
        -> Paragraph
          -> DecisionUnit
            -> Issue / Proposition / Argument
              -> EvidenceLink
              -> CitationEvent -> CitationTreatmentCandidate
              -> StatuteReference
              -> JudicialResponse
              -> ArgumentOutcome
    -> CaseDisposition
```

Each projected record should carry at least:

- stable source or entity identifier;
- source paragraph/chunk IDs and exact offsets where applicable;
- source hash and processing version;
- extraction method and rule/model version;
- confidence or evidence level;
- review state and reviewer provenance;
- creation and supersession metadata;
- links to the original text and related records.

The model should support many-to-many relationships. A proposition may be
supported by several paragraphs and authorities. One citation event may
support more than one proposition. A Decision Unit may contain more than one
argument, and an argument may continue across adjacent units when the text
makes the relationship explicit.

## Decision Unit Architecture

### Boundary signals

Segmentation should combine signals rather than rely on one heuristic:

1. document structure, headings, numbered grounds, and section transitions;
2. paragraph continuity and content-word overlap;
3. connective language such as however, therefore, alternatively, and in any
   event;
4. changes in speaker, party position, or argument role;
5. citation and statute continuity;
6. repeated issue terms and legal proposition continuity;
7. evidence and fact references that remain active across paragraphs;
8. paragraph density, short transition paragraphs, and enumerated lists;
9. source-specific formatting and paragraph identity.

Signals should explain both why a boundary was introduced and why adjacent
paragraphs were kept together. A unit without a clear evidence trail should
remain a review candidate rather than silently becoming authoritative.

### Segmentation strategy

The first durable strategy should be a deterministic candidate generator:

- start with ordered paragraph identity and structural anchors;
- generate candidate boundaries at strong structural or role transitions;
- suppress boundaries when continuity, authority, and issue signals remain
  strong;
- use bounded low-continuity runs as a vacuum boundary only after a minimum
  paragraph gate;
- retain alternative candidate boundaries when scores are close;
- emit diagnostics rather than forcing every paragraph into a confident unit.

Later probabilistic models may rank candidate boundaries or normalize similar
units, but they should not erase the underlying paragraph sequence or invent
unsupported roles.

### Technical challenges

- **Under-segmentation:** unrelated issues or arguments become one unit,
  making treatment and outcome attribution unreliable.
- **Over-segmentation:** one reasoning episode is split at a heading, citation,
  short transition, or change in role, losing its logic.
- **Mixed units:** a judge may address several arguments in one paragraph or
  return to an earlier issue after an interruption.
- **Argument continuation:** an argument may cross sections, quotations,
  footnotes, or procedural history.
- **Role ambiguity:** words such as claim, under, or issue can describe
  metadata or procedural facts rather than an argument role.
- **Sparse decisions:** short decisions may not expose all roles and must not
  be penalized for missing evidence.
- **Source reconstruction:** paragraph IDs, offsets, hashes, HTML/text
  variants, and repeated markers must remain consistent.
- **Cross-unit references:** a conclusion may refer to facts or authorities
  introduced much earlier.
- **Version drift:** changing a segmentation rule can change unit identity;
  old projections must remain inspectable and comparable.
- **Legal validation:** a technically coherent unit may still be legally
  misleading if it assigns the wrong speaker, issue, or response.

### Quality gates

Before runtime activation, a representative benchmark should measure boundary
precision, boundary recall, unit purity, role precision, source reconstruction,
and reviewer agreement. The benchmark must include short decisions, long
reasons, headings, lists, quotations, multiple issues, cessation, refugee,
procedural fairness, credibility, and mixed outcome examples.

## Citation-Treatment Architecture

The intended processing path is:

```text
Citation occurrence
  -> local sentence and paragraph context
  -> containing Decision Unit
  -> nearby proposition or argument
  -> treatment candidate
  -> judicial response evidence
  -> reviewed treatment label or unresolved state
```

### Citation event requirements

The event layer must preserve the existing extraction contract:

- exact citation text and backend-owned offsets;
- normalized citation and citation kind;
- source case and optional resolved target case;
- pinpoint and target chunk where uniquely resolved;
- short-form anchor text and anchor offsets when present;
- unresolved state and resolution provenance;
- containing paragraph or Decision Unit only as additive context.

The treatment layer must never repair a missing citation anchor by guessing and
must never turn an unresolved citation into a resolved target merely because a
semantic model found a similar name.

### Treatment candidates

A candidate may use:

- verbs and phrases around the citation;
- quotation and block-quote structure;
- explicit comparison language;
- treatment verbs such as followed, distinguished, applied, rejected, or
  confirmed;
- proposition similarity within the Decision Unit;
- whether the cited authority is used for a rule, factual analogy, standard of
  review, procedural test, or disposition;
- the judge's later conclusion and limiting language.

The output should include the candidate label, supporting spans, counter-signals,
method/version, confidence, and unresolved alternatives. A candidate is not a
legal conclusion until it passes the appropriate review gate.

### Multiple uses and conflicting signals

One authority may be followed for one proposition and distinguished for another
in the same decision. The model must represent multiple treatment events and
avoid reducing them to one case-level edge. Conflicting candidates should be
visible, not averaged away. Citation graph metrics may consume reviewed
relations later, but raw occurrence and treatment records remain separate.

## Argument Packets

An Argument Packet is the principal long-term comparison object. It should be
assembled from existing evidence rather than generated as an unsupported
summary.

### Packet contents

A packet may contain:

- case identity, court, date, proceeding type, and decision under challenge;
- issue and controlled theme links;
- one or more Decision Units;
- party, judge, or source role for each proposition where detected;
- argument statement and normalization status;
- evidence and fact references;
- governing rules and statute references;
- cited authorities and citation events;
- treatment candidates and supporting spans;
- judicial response and response evidence;
- argument outcome and separate case disposition;
- unresolved questions, alternate interpretations, and review state.

### Projection rules

Packets should be materialized only after the underlying evidence layers are
stable enough to support them. Initially they should be read-only projections
or report artifacts. Canonical persistence requires versioned schemas,
rebuildability, supersession, and a rollback plan.

A packet should be allowed to say:

- not detected;
- source text available but role unresolved;
- multiple candidate interpretations;
- evidence insufficient to classify;
- argument outcome not reached;
- case disposition known but argument outcome unknown.

These states are essential for trust. Absence of a detected role is not proof
that the role did not exist in the decision.

### Cross-case comparison

Future retrieval should support questions such as:

- Which cases considered the same issue under the same decision type?
- Which authorities were cited for the same proposition?
- Where was an authority distinguished rather than followed?
- How did judicial response differ by court, date, judge, or outcome?
- Which arguments recur with different evidence or procedural settings?
- Which cases contain a potentially relevant authority but no detected use?

Results must show the comparison basis, cohort filters, evidence links, and
coverage limitations. Similarity or embedding rank may discover candidates,
but it must not be presented as proof of legal equivalence.

## Deterministic And Probabilistic Responsibilities

### Deterministic responsibilities

The deterministic layer owns facts and reproducibility:

- source identity, provenance, terms, hashes, and text;
- paragraph and section identity and offsets;
- citation and statute extraction;
- target resolution and resolution status;
- controlled tags and metadata fields;
- explicit structural and lexical segmentation signals;
- evidence links, versions, and diagnostics.

These layers should remain testable with exact spans, positive and negative
fixtures, bounded reports, and repeatable outputs.

### Embedding responsibilities

Embeddings can support retrieval, candidate grouping, near-duplicate detection,
and proposition similarity. They should remain model-versioned and optional.
The existing local BGE-M3 provider is suitable for private repeatable
embeddings, while external embeddings remain an optional integration. An
embedding match is a search signal, not an evidence claim.

### Local generative model responsibilities

A local generative model may eventually assist with:

- issue and proposition normalization;
- grouping equivalent candidate arguments;
- ranking segmentation alternatives;
- drafting a bounded explanation from retrieved evidence;
- identifying possible counterarguments for human review.

It must not be the sole source of citation identity, offsets, statute identity,
argument outcome, or legal advice. Every generated statement must link to
retrieved source spans, disclose model/version and uncertainty, and remain
replaceable by a deterministic or human-reviewed result. The repository
currently has no local generative LLM; introducing one is a later operational,
privacy, quality, and resource decision.

## Evaluation And Human Review

The architecture needs evaluation before scale, not after a UI release.

### Benchmark layers

1. **Source fidelity:** text, offsets, paragraph identity, hashes, and citation
   anchors reconstruct correctly.
2. **Extraction:** citation, statute, tag, metadata, and role precision/recall
   on reviewed spans.
3. **Segmentation:** Decision Unit boundary and coherence measures.
4. **Linking:** proposition-to-evidence, citation-to-unit, and authority links.
5. **Treatment:** treatment candidate precision and unresolved-state accuracy.
6. **Argument:** issue, role, response, and argument-outcome agreement.
7. **Retrieval:** relevant-case and relevant-packet recall, ranking quality,
   explanation traceability, and latency.
8. **Product trust:** researchers can reach source evidence and understand what
   is inferred, unavailable, or unresolved.

### Review protocol

Use a stratified, versioned sample rather than only easy cases. Include courts,
years, languages where supported, case types, decision lengths, citation
shapes, and difficult mixed-issue decisions. Record reviewer instructions,
independent labels, disagreements, adjudication, and changes to the taxonomy.
Legal-domain review is required before promoting low-trust role or treatment
signals to default product behavior.

### Release gates

A new layer should remain report-only until it has:

- a bounded benchmark and known failure classes;
- exact source links for every displayed result;
- explicit unavailable and unresolved states;
- a reproducible versioned run;
- a rollback or supersession path;
- acceptable reviewer precision for its intended use;
- documentation of residual risk and coverage.

## Sequenced Roadmap

### Phase 0: Preserve the foundation

Maintain the deterministic source, citation, statute, metadata, tag, outcome,
chunk, embedding, Discussion Unit, sub-theme, summary, and theme layers. Keep
the current demo journey moving independently of advanced intelligence.

### Phase 1: Benchmark Decision Units

Create a reviewed cohort from the existing read-only Discussion Unit work. Measure
boundary quality, identify role and continuity failures, and define a stable
versioned unit representation. No corpus-wide canonical write is required.

### Phase 2: Build evidence-linked Argument Packets

Project issues, propositions, roles, evidence, authorities, and outcomes into
read-only packets. Start with cases where deterministic evidence is strongest.
Expose missing roles and unresolved links rather than filling them with model
claims.

### Phase 3: Add citation context and treatment candidates

Attach citation events to units and propositions. Implement a bounded treatment
vocabulary, emit supporting spans and alternatives, and evaluate on a reviewed
citation-use cohort. Keep target resolution, treatment, and graph metrics
separate.

### Phase 4: Compare packets across cases

Add controlled retrieval and comparison by decision under challenge, issue,
argument, authority, court, judge, date, and outcome. Show the cohort and
coverage basis for every comparison.

### Phase 5: Add embeddings and optional local assistance

Use embeddings to improve candidate retrieval and grouping after deterministic
links are trustworthy. Evaluate an optional local generative model only against
privacy, cost, latency, reproducibility, and evidence-grounding requirements.

### Phase 6: Productize reviewed intelligence

Promote only reviewed capabilities into the Data Explorer and reader. Add
saved comparisons, evidence bundles, exports, monitoring, and feedback loops
when the core projections are stable enough to support them.

## Risks And Open Decisions

### Principal risks

- A fluent explanation may conceal a wrong boundary or attribution.
- Case disposition may be incorrectly used as a proxy for argument success.
- Broad themes may override the more specific decision under challenge.
- Citation graphs may overstate authority relationships when treatment is not
  modeled per event.
- Semantic similarity may group legally distinct propositions.
- Long decisions may produce unstable units across parser or chunk versions.
- A local model may create privacy, resource, or reproducibility burdens.
- Corpus gaps may be mistaken for legal absence.

### Open decisions

- What is the minimum stable Decision Unit identity across segmentation versions?
- Which treatment vocabulary is useful and reviewable for Canadian immigration
  decisions?
- Should a packet represent one argument, one issue episode, or both?
- How should split or competing interpretations be displayed?
- Which roles require human review before any runtime exposure?
- What precision threshold is acceptable for a research-discovery signal versus
  a displayed explanation?
- When should projected units and packets become canonical records?
- What source and model versions must be retained for reproducibility?
- Which legal-domain reviewers and adjudication process will govern taxonomy
  changes?

## Architectural Invariants

1. Source evidence comes first; derived intelligence points back to it.
2. Citations, statutes, tags, metadata, outcomes, embeddings, treatments, and
   arguments remain distinct layers.
3. Backend-owned offsets and paragraph identity are authoritative.
4. Case-to-case target resolution remains separate from citation extraction.
5. A citation event is not a treatment, a treatment is not an argument outcome,
   and an argument outcome is not a case disposition.
6. Proceeding type, decision under challenge, theme, issue, and argument remain
   distinct concepts.
7. Unresolved and unavailable states are valid outputs.
8. Probabilistic systems assist discovery and normalization but do not replace
   provenance or source review.
9. Read-only reports and bounded cohorts precede canonical persistence.
10. Every promoted layer has evaluation evidence, versioning, documentation,
    and a recovery path.

## Relationship To Current Planning

The immediate roadmap remains demo-first: issue/type discovery, a coherent
Data Explorer journey, reader usability, and evidence-led demo scenarios.
Advanced citation treatment, corpus-wide contextual authority, argument
comparison, and local generative models remain deferred work. This document
keeps those goals visible without changing the current delivery commitment.

Current architecture and implementation details belong in
[SYSTEM_REFERENCE.md](../SYSTEM_REFERENCE.md). Near-term priorities belong in
[ROADMAP.md](../ROADMAP.md). The existing future-state map remains in
[`.swm/future-state.north-star.sw.md`](../.swm/future-state.north-star.sw.md),
while contextual-authority operations and bounded validation are described in
[`.swm/8.upryk5h6.sw.md`](../.swm/8.upryk5h6.sw.md).
