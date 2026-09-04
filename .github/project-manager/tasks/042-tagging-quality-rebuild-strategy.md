# Task: Tagging quality rebuild strategy

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Product outcome

Researchers can filter and understand cases through trustworthy, evidence-backed
legal tags. Every tag has one clear meaning, exact source evidence, an explicit
taxonomy version, and a confidence/resolution state. Tags describe a mention or
supported legal feature; they never present an inferred legal conclusion as fact.

## Why now

The current live tag layer is large but not sufficiently discriminating for
research use. A read-only database audit found 2,664,768 `ca_legal_v2_core` tag
occurrences across 28,454 of 61,241 cases. Coverage is incomplete, and generic
terms dominate: `canada`=555,848, `evidence`=372,152, and `citizenship`=197,990.
These terms can be useful as textual evidence but are too broad to lead a legal
research taxonomy without contextual qualification.

## Owner surface

`backend/legal_tagger_v3.py`, `backend/case_processing.py`,
`scripts/tag_cases_v3.py`, the V3 proposal/evaluation reports, and the additive
tag evidence contract. Contextual tagging and outcome-derived intelligence are
separate follow-up surfaces.

Dependencies: canonical case text and chunks; statute/citation occurrence layers;
current V2 tag tables and status rows; existing country/organization inventories.

Risk boundary: preserve existing tag rows and exact offsets. Do not mix tags with
statute or citation rows. Do not bulk-retag or delete V2 data until a new taxonomy
version, fixtures, dry-run, and bounded canary pass. AI proposals remain discovery
only and never write confirmed tags.

Commit allowed: yes

Push allowed: yes

## Capability assessment

- V1 (`ca_legal_v2`) is a broad, monolithic regex rule catalogue that mixes legal
  issues, procedures, entities, statutory signals, outcomes, and metadata. It is
  retained as a legacy comparison layer and is no longer the runtime target.
- V2 core (`ca_legal_v2_core`) is an independent exact-match occurrence matcher
  with exact offsets and resumable batches, but its whitelist includes generic
  terms whose frequency overwhelms discriminating legal concepts. It is a legacy
  comparison/rollback layer, not a production runtime default.
- The database has 28,511 completed V2 status rows and no skipped batches, but
  only 28,454 cases currently contain V2 tag rows. The remaining corpus is not
  covered.
- V2 stores occurrences with offsets; the reader can retain repeated evidence.
- Existing tests are strong for curated positive examples (27 focused tests pass)
  but lack a stratified precision/recall benchmark and negative/context fixtures.

## Recommended architecture

### Layer A: stable mention entities

High-precision, source-exact entities: statutes/instruments, tribunals, agencies,
ministers, reviewed organizations, countries/territories, case-procedure labels,
and known document types. Maintain canonical aliases in versioned configuration.
These tags answer "what is mentioned?" and preserve every valid occurrence.

The first V3 release is intentionally narrower than the final taxonomy. It will
prioritize useful, high-confidence categories:

- countries/territories relevant to a case, excluding Canada by default because
  it is ubiquitous and rarely discriminating;
- reviewed immigration and legal-process acronyms such as IRPA, IRPR, PRRA,
  H&C, IFA, RPD, RAD, IAD, ID, CBSA, IRCC, GCMS, and PFL;
- named external organizations and groups with reviewed aliases, such as IPOB,
  Falun Gong, LTTE, PKK, FARC, Taliban, Hamas, Hezbollah, and ISIS/ISIL;
- high-signal, explicit legal issue terms such as cessation, reavailment,
  terrorism, exclusion, inadmissibility, state protection, IFA, non-refoulement,
  and procedural fairness.

Generic standalone words such as `Canada`, `evidence`, `citizenship`, `notice`,
and `testimony` are excluded from the high-confidence research filter layer.
They can remain available later as contextual evidence only when a focused rule
establishes a legally useful meaning.

### Layer B: contextual legal features

Rule modules for issues, legal tests, procedural errors, risk, credibility,
inadmissibility, remedies, and immigration programs. A contextual rule requires
specific phrases, nearby statutory/citation evidence, or an explicit legal
predicate. It must distinguish discussion, allegation, party submission, finding,
and disposition where that distinction affects meaning.

### Layer C: derived research signals

Case-level summaries assembled from Layers A/B plus statute/citation/outcome
records. These are not raw text tags and must retain links to their underlying
evidence. Examples: primary issue, proceeding type, decision-maker, and dominant
statutory framework.

### Shared contracts

Each occurrence must retain: case ID, chunk ID where known, category, canonical
value, taxonomy version, rule ID, score/confidence, raw evidence, exact offsets,
language, and evidence role (`mention`, `allegation`, `submission`, `finding`,
`disposition`, or `unknown`). Do not collapse repeated occurrences. Case-level
summaries can deduplicate only as derived views.

## Delivery plan

1. Create `ca_legal_v3` rather than altering current V2 rows. Split the taxonomy
   into entity and contextual modules with small versioned configurations.
2. Build a stratified, read-only tagging candidate report across FC, FCA, SCC,
   RPD, RAD, ID, and IAD. Include positives, negatives, generic-term traps,
   heading/caption noise, French forms, and line-wrapped text.
3. Build the narrow V3 core from countries excluding Canada, reviewed acronyms,
   named organizations/groups, and explicit high-signal legal issues. Exclude
   generic standalone terms (`Canada`, `evidence`, `citizenship`, `notice`, and
   similar) from high-confidence research filters.
4. Align statute tags to extracted/resolved statute references rather than
   independently re-matching broad statute names in tag rules.
5. Defer contextual modules until the non-contextual V3 core passes its gates.
  Later, add contextual modules one legal family at a time, starting with immigration
   refugee protection, inadmissibility, removal/enforcement, procedural fairness,
   credibility/evidence, and H&C/family matters.
6. Run a bounded canary with a new taxonomy version; compare category counts,
   per-case density, exact-span validity, and human-reviewed precision/recall.
7. Only after gates pass, run checkpointed/resumable corpus tagging. Preserve V2
   rows for comparison and rollback.
8. Build reader/search filters from v3 evidence and derived summaries, not from
   raw high-frequency mentions alone.

## Alternatives considered

1. **Modular deterministic v3 with evaluation gates (recommended):** highest
   auditability, repeatability, and fit with existing offset evidence. It is
   incremental and requires curated fixtures.
2. **Expand the current V2 whitelist:** low initial cost but worsens generic-term
   noise and keeps incompatible concepts in one layer.
3. **LLM-first tagging:** useful for discovery/adjudication samples, but expensive
   and less repeatable for corpus-scale tags; unsuitable as the source of record.

## Success criteria

The tagging rebuild succeeds when all of the following are true:

- Every stored v3 tag is source-backed with valid offsets and a stable rule ID.
- Taxonomy categories are orthogonal: entity mention, legal issue, procedural
  posture, outcome, and derived summary are not conflated.
- Generic-word false positives no longer dominate the searchable legal taxonomy.
- Canada is excluded from the default country filter, and every retained country,
  acronym, organization, or issue has a reviewed canonical value and alias set.
- The first V3 pass prefers precision over breadth: it may leave nuanced or
  weakly contextual concepts untagged rather than assign a speculative label.
- V1 and V2 remain preserved but are explicitly non-target layers: V1 is not
  replaced in runtime until V3 is approved, and V2 is not reactivated as the
  production default.
- Contextual tags are deferred backlog work with separate actor, proximity,
  evidence-role, and negation tests.
- A stratified human-reviewed evaluation reports at least 95% precision for
  Layer-A entities and at least 90% precision for Layer-B high-confidence legal
  features; recall targets are measured separately by legal family and may not
  be claimed without fixtures.
- At least 95% of v3 occurrences have exact valid spans, with any exception
  explicitly documented and excluded from UI highlights.
- The system distinguishes a mere mention from an allegation/finding/disposition
  whenever a tag can be mistaken for a legal conclusion.
- Statute, citation, and outcome links are evidence-backed rather than duplicate
  regex claims.
- A bounded canary across FC/FCA/SCC/RPD/RAD/ID/IAD passes before full-corpus
  processing; jobs are resumable and use no competing writers.
- The UI exposes a tag's evidence, category, confidence, and scope so a
  researcher can verify it without trusting a label blindly.

## Smallest falsifiable next check

Build a read-only, stratified tag candidate report and measure how many current
V2 matches are generic standalone terms versus discriminating legal concepts. The
plan is falsified if generic tags do not materially dominate the current layer or
if their removal reduces explicit high-confidence concept coverage.

## Evidence

- Focused current tagger/reader tests: `27 passed`.
- Current V2 status coverage: 28,511 completed cases, zero skipped batches.
- Current V2 occurrence coverage: 2,664,768 tags across 28,454 cases.
- Existing LLM candidate report covers 500 cases but is discovery-only.
- A delegated read-only inventory reviewed the V2 whitelist, matcher, candidate
  report, draft guidance, and focused tests; no files were changed by the
  delegate.
- Added inactive proposal at
  `data/eval/reports/tagging-v3-core-whitelist-proposal.json` with seven narrow
  categories, 92 aliases, explicit generic-term exclusions, and a required
  regression/canary gate before activation.
- Expanded the inactive proposal with IRCC and CBSA research facets: named
  records, programs, formal proceedings, and enforcement/review signals are
  candidate core terms; generic words such as `application`, `decision`,
  `removal`, `detention`, and `hearing` remain contextual-only. The proposal
  now contains nine categories and 121 aliases, with 29 agency core signals
  mapped to canonical aliases.
- Recorded the lifecycle boundary: V1 remains only as a temporary runtime
  fallback, V2 is comparison/rollback only, and neither is the V3 target. Added
  a reviewed alias policy covering acronym/full-name, punctuation, spacing,
  hyphenation, and explicitly tested plural variants; automatic pluralization,
  adjectival expansion, substring fragments, and ambiguous short acronyms remain
  excluded.
- Added inactive `backend/legal_tagger_v3.py`, which reads the review-only V3
  proposal and emits exact mention evidence with backend-owned offsets. It is
  not wired into runtime ingestion or any bulk writer.
- Added eight focused V3 proposal/matcher tests covering proposal status, agency
  signal coverage, contextual separation, safe alias variants, generic-term
  exclusions, exact offsets, and non-inference behavior.
- Added additive migration `0021_case_tag_evidence_contract` and extended
  `CaseTag` with optional chunk/rule provenance plus language and evidence role.
  Added opt-in `scripts/tag_cases_v3.py`; it is bounded, resumable, taxonomy
  isolated, and persists every occurrence without a set/deduplication step.
- Added a focused repeated-occurrence contract test: two IRCC matches remain
  two rows with distinct offsets and complete rule/source/taxonomy metadata.
- Proposal JSON validation passed on 2026-09-04.
- Focused V3 tests passed: `8 passed` on 2026-09-04.
- Focused V3 tests now pass: `9 passed` on 2026-09-04.
- Applied additive Alembic migration `0021_case_tag_evidence_contract` to the
  configured PostgreSQL database on 2026-09-04.
- Ran the bounded read-only preview
  `scripts/tag_cases_v3.py --dry-run --limit 25`: 25 pending cases and 156
  preview occurrences; no V3 tag or status rows were written.
- Applied a one-case-per-available-cohort V3 canary for FC, FCA, Federal Court,
  RPD, and SCC. The five cases completed with 35, 13, 0, 7, and 60 occurrence
  rows respectively; no batches were skipped. RAD and IAD had no pending cases
  in the available database cohort query, so they were not claimed as tested.
- Verified the five canary statuses and persisted rows: all non-empty rows had
  rule IDs, `mention` evidence roles, valid positive spans, and complete V3
  taxonomy/source metadata. Repeated canonical values were present at separate
  offsets, confirming no occurrence deduplication.
- Generated the review snapshot
  `data/eval/reports/tagging-v3-canary-review.md` with all 115 persisted
  occurrences and their case, court, category, value, evidence, offsets, rule,
  language, role, and source fields.
- Wired `tags_v3` into `process_case_in_five_layers` as the final deterministic
  stage. The stage replaces only the case's V3 rows/status and does not alter
  V1 subject derivation, V2 comparison rows, citations, statutes, or outcomes.
- Updated `LEGAL_TAGGING.md`, `SYSTEM_REFERENCE.md`, and `OVERNIGHT.md` to
  identify V3 as the active deterministic core, preserve V1/V2 boundaries, and
  defer contextual tags and outcome-derived intelligence.

Status: complete
