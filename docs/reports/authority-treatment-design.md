# Citation authority-treatment design

**Status:** Proposal only. This document describes a future, evidence-linked
research signal; it does not describe a production classifier or current UI
behavior.

## Product outcome

Help a researcher see how a citing court used a particular authority for a
particular proposition, with the source language and its location one click
away. The unit of analysis is a citation event (and potentially several
treatment events for that occurrence), not a case-to-case edge or a permanent
property of the cited authority.

The core distinction is:

> A citation is not proof of treatment; treatment is not the citing case's
> disposition.

Current citation extraction records occurrence text, offsets, pinpoints and
optional target resolution. `citation_contexts()` returns the citation text and
offsets, chunk identity, and bounded nearby text (up to 500 characters on each
side, with newline boundaries); these are source-navigation inputs, not
treatment labels
([`backend/citation_map.py`](../../backend/citation_map.py#L261-L322)). The
refinement design likewise separates extraction, resolution and pinpoints, and
does not define a treatment classifier
([`backend/citations.py`](../../backend/citations.py#L338-L349);
[`docs/CITATION_REFINEMENT.md`](../CITATION_REFINEMENT.md#L1-L6),
[#L44-L48)).

## Proposed label set

Use the treatment-teacher contract's existing provisional vocabulary as a
starting point (`supportive`, `distinguishing`, `negative`, `neutral`, `absent`,
`ambiguous`); validate the definitions with legal reviewers before use. The
contract is a non-production LLM teacher-label schema, including exact treatment
phrase offsets and separate exact-span context fields for actor, reason raised,
argument supported/addressed, court response and argument conclusion. It is not
the requested rule-based classifier and does not provide that classifier's
rules. Reuse its enum only as a vocabulary candidate, subject to legal review
([`teacher_contract.py`](../../backend/contextual_authority/teacher_contract.py#L72-L107);
the [long-term vision](../LONG_TERM_INTELLIGENCE_VISION.md#L204-L227)
also requires legal review of treatment vocabulary).

| Label | Proposed meaning | Important boundary |
|---|---|---|
| **Supportive** | The citing court expressly adopts, follows, applies, confirms, or relies on the cited authority for an identifiable proposition. | A citation in the same paragraph as a proposition is not enough; identify the court's own use. |
| **Distinguishing** | The court explains that the cited authority does not govern, or is materially different, on a stated basis. | A distinction is not automatically criticism or rejection of the authority. |
| **Negative** | The court expressly questions, rejects, disapproves of, overrules, or declines to follow the cited authority or the relevant proposition. | Do not assign this because a party attacks the authority or because the citing party loses. |
| **Neutral** | The authority is described or mentioned, but the court's language does not show a directional endorsement, distinction, or rejection. | This is a substantive “descriptive mention” label, not a low-confidence guess. |
| **Absent** | The citation occurrence is present, but the inspected source context contains no supported treatment evidence. | Means “no treatment evidence found in this context,” not “the case never treated the authority.” |
| **Ambiguous** | The source supports multiple plausible readings, conflicting treatment, or unclear attribution. | Preserve the competing evidence; do not force a single polarity. |

Keep **unresolved / not reviewed / insufficient context** as workflow states,
not extra treatment labels. A low-confidence candidate, missing paragraph,
unresolved target or failed span check should abstain. One authority can be
supported for one proposition and distinguished for another in the same
decision; do not collapse those events into one case-level label. This matches
the vision's event-level model and its instruction to retain conflicting
candidates ([`LONG_TERM_INTELLIGENCE_VISION.md`](../LONG_TERM_INTELLIGENCE_VISION.md#L343-L397)).

## Evidence signals and decision rules

Each candidate should identify the *court's treatment of the cited proposition*,
not merely detect a nearby phrase. Retain a source-reconstructible treatment
phrase, actor/speaker, rationale where explicit, citation event ID, source
paragraph/chunk, offsets, method/version, confidence and alternatives.

1. **Signal phrases.** Treatment verbs and comparison clauses (for example,
   “followed,” “applied,” “distinguished,” “questioned,” or “rejected”) can
   nominate candidates. Require the relevant clause and an attributable actor;
   phrases alone are not a decision rule. Exact phrase offsets must reconstruct
   against source text. The teacher contract distinguishes treatment-phrase
   offsets from citation offsets and requires exact spans.
2. **Quotation and attribution.** Quoted holdings, party submissions and
   descriptions of another court are not automatically the current judge's
   position. Track who said the words and whether the citing court adopts,
   limits, or rejects them. A quoted positive phrase without judicial adoption
   must not become a supportive flag; a party's criticism must not become a
   court's negative treatment.
3. **Local context and Discussion Unit position.** Start with the citation
   paragraph and a bounded neighboring-sentence window; use its reviewed
   Discussion Unit as context for whether it is stating a rule, recounting a
   party position, assessing evidence, applying a test, or giving a disposition.
   Unit role and position (including early/late placement) are context, never
   standalone proof of treatment. Discussion Units group coherent legal work
   while preserving source identity; the weekly review says a citation's
   presence in a unit does not itself prove why it was cited
   ([`DISCUSSION_UNITS_WEEKLY_REVIEW.md`](../DISCUSSION_UNITS_WEEKLY_REVIEW.md#L16-L49),
   [#L212-L236)).
4. **Citing-case outcome.** Keep the case disposition and government outcome
   separate from treatment. The overall outcome may be shown as a filter or
   descriptive cohort field, but must not determine the treatment label or the
   result of an individual argument. An application can be dismissed while a
   cited authority is followed on one issue; a successful case can distinguish
   another authority. The long-term design explicitly separates argument
   outcome and case disposition ([`LONG_TERM_INTELLIGENCE_VISION.md`](../LONG_TERM_INTELLIGENCE_VISION.md#L217-L227)).
5. **Conflict and abstention.** Preserve mixed signals and multiple
   proposition-specific events. When quotation, attribution, unit boundaries,
   or the available source text leave a real ambiguity, return `ambiguous` or
   an unresolved workflow state; do not average competing labels into a
   confident flag.

The current `contextual_authority` package has useful but narrower primitives:
Discussion Unit segmentation uses headings, citation/statute/tag continuity
and text continuity; observations retain exact cue spans and hashes; and rule
agreement can report conflict or abstention without generating a pseudo-label
([`discussion_units.py`](../../backend/contextual_authority/discussion_units.py#L20-L35),
[#L147-L171); [`observations.py`](../../backend/contextual_authority/observations.py#L23-L40),
[#L71-L129); [`voting.py`](../../backend/contextual_authority/voting.py#L82-L124)).
Those cues do not establish citation treatment or attribution.

## Precision target and first hand-check

**Proposed expectation, not a measured result:** before any confident,
researcher-facing supportive, distinguishing or negative flag is enabled, target
at least **95% event-level precision per displayed label** on a held-out,
hand-adjudicated sample. Report precision separately by label, plus coverage,
abstention and confusion counts; never let a large neutral class hide errors in
an adverse label. A UI threshold should favor abstention over unsupported
certainty.

No treatment precision or calibrated confidence is established by the sources
reviewed here. The Discussion Unit review reports a small segmentation pilot,
not a citation-treatment gold set, and explicitly says that unit membership
does not prove citation function ([`DISCUSSION_UNITS_WEEKLY_REVIEW.md`](../DISCUSSION_UNITS_WEEKLY_REVIEW.md#L283-L295)).
The 95% figure is therefore a proposed release target, not an observed baseline
or guarantee. A small pilot can expose obvious failure modes but cannot by
itself establish that target.

**Smallest useful manual screen:** sample 48 citation events from at least 12
decisions. Include candidate positive and negative language, quoted/party
language, neutral mentions, no-treatment cases, and more than one Discussion
Unit position; split by decision so no decision appears in both calibration and
held-out examples. Two legal reviewers independently label each event and
record the exact evidence phrase, speaker, label, and abstention reason; adjudicate
disagreements before scoring. Report per-label exact counts and denominators,
false-positive examples, reviewer agreement, abstention/coverage, and a
confidence interval. If a label has too few candidate examples for a meaningful
precision read, report it as **not evaluated**, not as passing. Expand the
cohort before release; this screen is diagnostic, not a production-readiness
claim.

## Research display

### Citation Intelligence

Add a treatment-evidence view only after reviewed labels exist. Keep the selected
authority identity and each citing case distinct. A row should show the proposed
label and review status, citation occurrence, exact treatment phrase with
source-linked highlight, citing paragraph and Discussion Unit role, speaker or
actor where known, confidence/method, and a one-click route to the full decision
context. Put the citing case's outcome in a separate field, never inside the
treatment badge. Show conflicting, ambiguous, absent and unreviewed events
rather than filtering them away by default.

Citation Intelligence authority signals currently summarize frequency,
occurrences, chunk spread, context and navigation; they are not treatment
scores. Its guide explicitly cautions that an outcome association does not show
that an authority caused an outcome. Treatment would be a separate,
source-linked interpretation layer, not a replacement for existing occurrence
rows, target resolution, graph metrics, or outcome signals
([`RESEARCH_UI_GUIDE.md`](../RESEARCH_UI_GUIDE.md#L407-L447);
[`backend/citation_map.py`](../../backend/citation_map.py#L626-L710)).

### Memo check

**Runtime/field interpretation caveat:** `backend/memo_citation_check.py`
contains `analyze_memo_citations()` and `_get_treatment_status()`. The latter
labels `Citation.citation_kind` values such as `overruled`, `reversed`, or
`applied` as treatment flags. However, the inspected extractor defines case
citation kinds as `neutral`, `case`, `case_short`, and `case_name`
([`memo_citation_check.py`](../../backend/memo_citation_check.py#L24-L55);
[`citations.py`](../../backend/citations.py#L34-L36)). This apparent field/value
mismatch means those returned flags must **not** be represented as verified
treatment classifications. This design note has not validated their runtime
behavior or UI exposure. The repository's UI guide does not document a Memo
Check surface, so the exact user-facing workflow remains unverified.

If/when that workflow is defined, show independently reviewed treatment as a
*verification prompt* for citations used in the memo: compare the memo's
proposition with the source passage and expose supportive,
limiting/distinguishing, negative, neutral, ambiguous and unreviewed evidence
side by side. Require the researcher to open and verify the judgment. Never
present the existing `citation_kind` flags as that review, auto-approve a
proposition, mark a memo legally correct, or silently omit contrary evidence.
Keep every displayed label traceable to exact source text and make uncertainty
conspicuous.

## Risks of wrong flags in litigation research

- A false **negative** or **distinguishing** flag can make counsel wrongly
  discount controlling or favorable authority; a false **supportive** flag can
  make a proposition appear safer than the reasons support.
- A wrong **case outcome** association can be mistaken for authority strength or
  argument success. Keep case disposition, argument result and treatment as
  distinct fields.
- A quotation, counsel's submission, procedural history or headnote-like
  description can be misattributed to the judge. Speaker errors are substantive
  errors, not cosmetic model mistakes.
- A citation may receive different treatment for different propositions. A
  single case-level badge erases qualifications and conflicts.
- Citation target resolution, citation offsets and treatment are separate
  layers. Never repair an unresolved citation or alter backend-owned offsets to
  make a label look complete.
- A polished badge can be over-trusted under time pressure. Keep labels
  provisional until reviewed, show the source phrase and context beside them,
  display “not reviewed” clearly, and provide a direct way to inspect the
  decision.

The design must therefore be recall-tolerant and precision-first for prominent
flags, with explicit unknown states, provenance and a review gate. A wrong
displayed flag risks researcher reliance; a missing candidate is less harmful
when the interface makes its incomplete coverage clear.

## Phased plan

1. **Evidence-only review slice (smallest first slice).** Select a bounded set
   of existing, resolved citation occurrences; build no classifier, database
   write, or UI change. Present each occurrence with backend-owned citation
   offsets, bounded source context, and its Discussion Unit/paragraph identity
   where available. Have reviewers apply the labels above and save the exact
   source phrase, actor, disagreement and unresolved reason. This tests whether
   the taxonomy is usable and whether the needed context is available.
2. **Candidate generation, still report-only.** Add deterministic phrase and
   quote/attribution cues as candidate selectors only. Preserve source spans,
   candidate alternatives, method/version and `review_required`; compare against
   the manual slice and abstain on attribution gaps. Do not alter citation
   extraction, target resolution, or canonical records. This is a separate
   rule-based design, not an activation or reinterpretation of the LLM teacher
   contract. The long-term vision likewise calls for a bounded treatment
   vocabulary, supporting spans and alternatives, a reviewed cohort, and
   separation from target resolution and graph metrics
   ([`LONG_TERM_INTELLIGENCE_VISION.md`](../LONG_TERM_INTELLIGENCE_VISION.md#L559-L565)).
3. **Held-out precision check.** Expand and stratify the manually reviewed set;
   evaluate per-label precision, coverage, abstentions, quote/speaker errors,
   and outcome leakage. Require the proposed precision gate for each promoted
   label, with enough examples to support interpretation.
4. **Read-only Citation Intelligence.** Add source-linked, reviewed
   treatment-event rows and conflicts. Keep raw citation evidence, labels,
   outcomes and graph counts separate. Gate default visibility by reviewed
   status and confidence; do not reuse existing authority-signal scores as
   treatment scores.
5. **Memo-check integration.** Only after that workflow's contract is confirmed,
   expose reviewed treatment as a citation-audit aid with a mandatory source
   check and no legal-correctness verdict. Re-evaluate after real user review.

Do not move candidate treatment into canonical citation rows or use it in graph
metrics until a separately approved persistence and evaluation design exists.

## Evidence and verification notes

- Discussion-unit documents found in this checkout and cited above are
  `docs/DISCUSSION_UNITS_WEEKLY_REVIEW.md` and
  `docs/LONG_TERM_INTELLIGENCE_VISION.md`. The weekly review says the Discussion
  Unit output is report-only and has not changed canonical citations, statutes,
  tags, outcomes, offsets, or database records (lines 6-14). No local
  `origin/main` ref was available, so these are cited as checkout evidence, not
  attributed to a verified main-branch revision.
- Code and document evidence cited above establishes citation spans/context,
  provisional treatment contracts, and report-only Discussion Unit status. It
  does **not** establish production treatment accuracy, a treatment gold set,
  calibrated confidence, or that the existing memo `citation_kind` flags
  represent verified treatment.
- The existing [Swimm Discussion Unit walkthrough](../../.swm/8.upryk5h6.sw.md#L226-L295)
  records that current treatment outputs remain provisional and runtime-disabled;
  this design note is a proposal, not a change to that behavior.
