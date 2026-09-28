# FC Activity Beta VBA Comparison

Status: analysis checkpoint, no extraction behavior changed
Date: 2026-09-28

## Scope

The Beta workbook was inspected read-only from `data/reference_library/JRU Personal Inventory Tool Beta.xlsm` with `olevba 0.60.2`. The comparison covers the workbook's VBA modules and the active Python FC Activity classifier and procedural-history fetcher. The workbook was not executed and no remote or database operation was performed.

## Verified Beta Surface

Beta contains these relevant modules and procedures:

| Module | Verified procedures | Practical output |
| --- | --- | --- |
| `ModMain.bas` | `RefreshInventory`, `BuildCasesToReview` | Orchestration, worksheet population, review queue |
| `ModMotions.bas` | `NormalizeMotionType`, `NormalizeMotionResult`, `ExtractMotionHistory`, `ExtractMotionHistoryFromArrays` | Motion labels and motion history columns |
| `ModCourtData.bas` | `HttpGet`, `GetJsonValue`, `CleanDateTime`, `ParseAllEntries`, `BuildFullActivityAndLatest` | API retrieval, docket parsing, dates, reverse chronology |
| `ModDecisionMaker.bas` | `ExtractJudge`, `ExtractDecisionMaker` | One judge and one underlying decision-maker label |
| `ModDecisionPoints.bas` | `NormalizeEntry`, `ExtractLeaveInfoFromArrays`, `ExtractJRInfoFromArrays`, `ResolveLeaveAndNormalizeDates`, `DetermineCaseStatus` | Leave/JR outcome precedence and case status |
| `ModValidation.bas` | `ValidateInventory`, `AddValidationIssue`, `WriteValidationReport` | Row-level QA report |

The verified workbook sheets are `Inventory`, `FullActivity`, `Cases to Review`, and `ValidationReport`. `Inventory` has fields for tribunal number, case name, latest activity date, judge, decision maker, proceeding type, motions, motion results, hearings, leave/JR decisions and dates, case status, and full activity text.

## Where Beta Improves The Current Pipeline

### 1. A dedicated motion taxonomy

Beta explicitly names motion categories that the current Python event layer does not preserve as a structured subtype: stay of removal, stay of deportation, stay of release, stay of admissibility hearing, stay of proceedings, stay of execution, abeyance, s.37 CEA, s.87 IRPA, anonymity, amendment of ALJR, extension of time, consent judgment, confidentiality, production, intervention, and a generic stay/other fallback.

The current Python classifier detects `motion_filed` and `motion_decision` and preserves source evidence, but it does not normalize these motion types into a stable taxonomy. This is the highest-value Beta contribution because it supports motion-level filtering and procedural-delay analysis without collapsing motions into general tags.

### 2. A useful validation contract

Beta validates contradictions and missing values after refresh, including:

- leave still pending while a JR result exists;
- a JR result without a JR date;
- leave date after JR date;
- leave date after latest activity date;
- missing latest activity date;
- leave marked `N/A` while a substantive JR result exists.

The Python pipeline has evidence gates and evaluation reports, but these exact cross-field integrity checks are not yet represented as a reusable per-case validation result. Beta's validation ideas should be adapted to structured JSON findings, not copied as worksheet logic.

### 3. A human review queue

`BuildCasesToReview` selects terminal and unresolved statuses into a dedicated review sheet. The current Python evaluation produces coverage and audit-gap reports, but it does not yet expose a simple case-level queue driven by status contradictions, missing dates, unknown subject, unknown motion type, or low evidence completeness.

### 4. A clear raw-versus-derived presentation split

`FullActivity` retains the reverse-chronological raw activity string while `Inventory` presents derived fields. The current Python architecture already preserves source documents and evidence more rigorously, but the Beta layout is a useful operator-facing presentation pattern for a compact review export.

## Where Current Python Is Stronger

### Provenance and repeatable evidence

Python emits event-level `doc_id`, `re_no`, `docno`, source document date, semantic event date, filing date, date kind, source text, and rule. Beta reduces most outputs to worksheet strings and does not retain field-level evidence links.

### Event granularity

Python emits repeatable procedural events for application filing/perfection, appearances, leave, motions, hearings, decisions, stays, and judge observations. Beta primarily produces one aggregate motion string and one aggregate judge/decision-maker value.

### Dates and chronology

Python distinguishes rendered/event dates, filing dates, and source registry dates, and handles more explicit date forms. Beta uses locale-sensitive `IsDate` and simple string parsing. Beta's reverse chronology and latest-date check are useful, but its date parser should not replace the existing typed date path.

### Judge and decision-maker handling

Python records stage-specific judge observations and evidence. Beta's `ExtractJudge` takes the first `Justice ` occurrence and only returns a short name; `ExtractDecisionMaker` exits on the first matching application entry and returns one coarse label. Python is safer for multiple procedural stages and auditability.

### Leave/JR semantics

The two implementations share the same broad precedence model, including leave-dismissed overriding an apparent JR grant and inferring leave from a later JR result. Python has broader bilingual and evidence-aware handling. Beta remains valuable as a source of additional exact phrases and QA invariants, not as the authority to replace current precedence without fixture comparison.

## Important Beta Limitations And Bugs

1. `NormalizeMotionResult` is defined, but `ExtractMotionHistoryFromArrays` never calls it and never appends `MotionResults`. The `Motion Results` column is therefore unfinished in the inspected Beta source.
2. Motion detection is limited to `notice of motion` and French `avis de requete/requête`; a motion order or result without that phrase may be missed.
3. The motion extractor drops `Other Motion` rather than preserving an evidence-backed unknown category.
4. `GetJsonValue` is a string search, not a JSON parser; escaped quotes, nulls, field ordering, and nested values are unsafe.
5. `ParseAllEntries` searches raw JSON text and stops when a matching recorded-entry field is absent; it does not expose parse failures as structured source-quality findings.
6. `ExtractJudge` returns only the first `Justice` match and can truncate names.
7. `ExtractDecisionMaker` is restricted to entries containing application wording and returns the first match, so later clarifying evidence is not aggregated.
8. Excel `IsDate` is locale-sensitive, while the Python path should remain the canonical normalized-date implementation.

## Recommended Next Steps

### Phase 1: fixture extraction and alignment

1. Create a small Beta-derived rule inventory from the extracted VBA source, preserving exact phrase examples and intended normalized labels.
2. Add a field-alignment matrix: Beta field/rule, Python field/rule, evidence source, expected behavior, and test fixture.
3. Build 20-30 bounded Activity fixtures covering each motion category, partial grant, discontinuance, French wording, unknown motion, and motion result without a notice phrase.
4. Do not execute macros against production data; use copied source text and a bounded workbook sample only.

### Phase 2: motion subtype and result layer

1. Add `motion_subtype` and a normalized motion-result vocabulary to the Python procedural event schema.
2. Preserve `unknown` motion subtype and exact evidence instead of dropping unmatched motions.
3. Add explicit partial-grant, abandoned, discontinued, and French result rules.
4. Keep one event per source document and retain all source identifiers; do not replace the current event model with aggregate strings.

### Phase 3: validation and review outputs

1. Implement a pure `validate_fc_activity_classification()` function returning structured findings with severity, rule, affected fields, and evidence document ids.
2. Port the Beta cross-field checks first, then add Python-specific checks for missing evidence, date-kind conflicts, duplicate event claims, unknown subject, and unknown motion subtype.
3. Generate a bounded `Cases to Review` report from those findings, with status categories and source links.
4. Measure validation yield on the existing 1,000-record evaluation before considering any bulk run.

## Acceptance Signals

The next implementation should be considered successful only if:

- motion subtype and result extraction improves coverage on the new fixtures without changing raw Activity rows;
- every promoted motion event retains source text and document identifiers;
- Beta cross-field contradictions are surfaced as structured findings;
- unknowns remain visible rather than being coerced into a category;
- focused classifier tests and the bounded evaluator pass with before/after coverage counts.

The Beta workbook is therefore best treated as a rule and QA reference, not as a replacement extraction engine. Its highest-return additions are motion subtype normalization, structured validation findings, and a reproducible review queue.

## Implementation Checkpoint

The first bounded implementation slice is complete in
`scripts/classify_fc_activity.py`:

- Motion events now retain stable subtypes for Beta categories such as
	removal stays, s.87 IRPA, intervention, production, and unknown categories.
- Explicit results now distinguish `granted`, `granted_in_part`, `refused`,
	`abandoned`, and `discontinued` without changing the existing
	`motion_filed`/`motion_decision` event types.
- `validate_fc_activity_classification()` returns deterministic, read-only
	findings for Beta-derived leave/JR and activity-date contradictions.

The focused fixture suite passed 4 tests and the existing FC Activity
classifier suite passed 49 tests. Source document identifiers and text remain
on every promoted motion event; raw Activity rows and canonical case records
were not changed.

The fixed seeded coverage measurement used 100 cases (`seed=20260925`,
seven-year recent weighting, 70% recent share) and produced 8 motion cases,
22 motion events, and complete evidence on all 22 events. Subtype coverage was
22.73% (5 classified, 17 unknown); result coverage was 18.18% (4 classified,
18 unknown). The artifact is
`data/eval/fc_activity_motion_coverage_20260928.json`; it records
`network_called=false` and `database_written=false`. This is extraction
coverage, not gold-set accuracy, and the unknown majority is the next fixture
and rule-review signal.

## Corpus Pattern Checkpoint

The seeded 1,000-record corpus evaluation (`seed=20260925`, seven-year recent
weighting, 70% recent share) produced 139 motion cases and 950 motion events.
Subtype coverage was 250/950 (26.32%), with 700 unknown subtypes. Result
coverage was 127/950 (13.37%); observed results included 78 granted, 37
refused, 6 abandoned, 5 discontinued, and 1 granted in part, with 818 unknown
results. The artifact is
`data/eval/fc_activity_motion_patterns_20260928.json`; it recorded no network
call and no database write.

A bounded 10-case OpenAI audit completed with `gpt-4.1-nano` at an estimated
cost of `$0.0014555`, with no database write. It returned three advisory
findings concerning originating-application capture, a French leave decision,
and a judge/date signal. These are review signals only; no classifier rule was
promoted. The audit artifact is
`data/eval/fc_activity_openai_motion_review_20260928.json`.

## Unknown Motion Review Matrix

The 700 unknown-subtype events in the fixed 1,000-record artifact were
independently grouped using conservative source-language families:

- `motion_record_reference`: 441
- `unresolved_motion`: 242
- `motion_order_without_subject`: 12
- `hearing_motion_reference`: 5

The bounded review artifact
`data/eval/fc_activity_motion_unknowns_20260928.json` preserves 30 candidate
rows with activity case IDs, document IDs, event types, outcomes, source dates,
and bounded evidence text. Every row remains `review_status=unknown` with no
suggested subtype, and `rules_promoted=false`. These are triage families, not
legal or procedural classifications; the next fixture work must review linked
documents before proposing any rule.

## Full Unknown-Motion OpenAI Enrichment

All 700 unknown-subtype motion events from the fixed corpus were sent through
the event-level `gpt-4.1-nano` adapter in 70 bounded batches. The run completed
normally within the hard `$5.00` budget: projected cost was `$0.041059` and
actual spend was `$0.0316852`. It used 93,796 prompt tokens and 44,434
completion tokens across the initial pass and the bounded retry of responses
that omitted structured suggestions.

The review artifact is
`data/eval/fc_activity_motion_unknowns_openai_20260928.json`. It records
`network_called=true`, `database_written=false`, and `rules_promoted=false`.
698 events have structured advisory suggestions; 2 remain unresolved after the
retry and remain eligible for later source-backed review. The suggestions are
not a gold set, classifier truth, or automatic rule input. The initial API
failure was traced to stale organization/project environment variables loaded
from `.env`; the adapter now removes those optional variables before client
construction.

## Advisory-Derived Deterministic Improvements

The advisory output was used as a bounded rule-discovery signal, not as a gold
set or automatic promotion source. The deterministic classifier now recognizes
explicit removal-stay gerunds, French sursis and consent-judgment wording, and
`extend time` variants. It also links a motion filing description to later
entries through explicit `Doc. N`, `Motion Doc. N`, or `Requête Doc. N` text
references. A primary `Notice of Motion` may use its source `docno` as the
filing reference when the text has no reference; `re_no` is only a fallback.
The activity row/document identity is not treated as a logical motion. Bare
`stay` is excluded from propagation, conflicting subtype anchors remain
unknown, and propagated events retain `subtype_source_doc_id` and source text.

The classifier version is now `fc_activity_v5`. On the same seeded 1,000-case
read-only evaluation, subtype coverage increased from 250/950 (26.32%) to
264/952 (27.73%), with evidence complete on all 952 motion events. Result
coverage remains a separate metric at 13.45%; the rerun recorded
`network_called=false` and `database_written=false`.

The OpenAI adapter now preserves cumulative usage, spend, pass history, and
explicit unresolved event keys across retries. No advisory suggestion was
promoted automatically.

## Progression-Aware Applicability

Field coverage must distinguish absent evidence from fields that cannot exist
for a case's procedural path. The classifier now preserves the raw evidence
fields and emits `field_applicability` statuses of `known`, `pending`,
`not_applicable`, or `not_observed` for leave, judicial-review result,
judicial-review final decision, and the generic final-decision marker.

The progression rules are directional: a case discontinued or withdrawn before
leave has no applicable leave decision; leave refusal makes the substantive
judicial-review result and final decision not applicable; and withdrawal or
discontinuance after leave grant makes the substantive final decision not
applicable. Leave non-applicability now includes an explicit reason and
explanation: direct judicial review does not require leave, an application
that was never perfected cannot reach leave, and terminal closure after
perfection but before a leave decision is recorded is reported separately.
A generic final-decision marker may still be the leave dismissal and is kept
separate from `judicial_review_final_decision`. Substantive judicial-review
results infer that leave was granted. A granted production order is retained
as a lower-confidence supporting signal for inferred leave grant, with its
source event preserved.

In the bounded 1,000-case evaluation, leave was known in 466 cases, pending in
252, and not applicable in 278. The leave N/A reasons were 152 cases not
perfected before discontinuance, 121 discontinued after perfection but before
leave, 4 administratively terminated before perfection, and 1 direct judicial
review. Judicial-review result was known in 52 cases, pending in 20, and not
applicable in 672; judicial-review final decision was known in 50, pending in
22, and not applicable in 672. These denominators are more meaningful than
treating all 1,000 cases as eligible for every field.

The same applicability model now covers application perfection and hearings.
Application perfection was known in 529 cases, pending in 185, and not
applicable in 286: 124 followed leave refusal, 152 were not perfected before
discontinuance, 4 before administrative termination, 5 had no originating
application, and 1 was direct judicial review. Hearing status was known in 516
cases, pending in 220, not observed in 6, and not applicable in 258. The
hearing N/A reasons were
249 discontinued before leave, 4 administratively terminated before leave, and
5 leave refusals. Explicit hearing evidence remains authoritative, including
484 known not-held outcomes and 15 reserved outcomes.

## Pending Applicability Review

A bounded read-only review of the 185 pending perfection cases and 220 pending
hearing cases found no safe deterministic inference to promote. Pending
perfection cases are now limited to unresolved or unknown leave paths and
leave-pending paths. Treating a downstream leave outcome as proof of perfection
would conflate missing docket evidence with a procedural fact.

Leave refusal is now handled separately: when no explicit perfection evidence
exists, perfection is `not_applicable` with reason `leave_refused`, because the
case can no longer be pending perfection. Its human-readable explanation is
`Not applicable: leave refused.` Explicit perfection evidence remains `known`
even when leave was refused.

Pending hearing cases were concentrated in unresolved or unknown leave paths:
89 had no resolved leave status, 79 remained leave-pending, 28 had no leave
resolution despite a perfected application, and 24 were leave-pending with a
perfected application. The correct current result is `pending`, not
`not_held` or `not_applicable`. No classifier rule was promoted and no source
or database write was performed. Future improvement should revalidate source
completeness for a bounded sample before changing these states.

## Document Versus Unique-Motion Coverage

The evaluation now reports two denominators. Document-level metrics retain one
row per extracted motion event for regression continuity. A separate grouped
metric connects activity entries using the motion-document number in filing,
support, opposition, hearing, or decision text. It uses the primary filing's
`docno` only when that entry is a `Notice of Motion`, then falls back to
case-scoped `re_no` and finally a singleton document when no stable link exists.
The FC Activity row/document identity is only an entry identifier, not a
logical motion identity. Conflicting subtype or outcome evidence is reported as
`conflict`, not resolved by majority vote.

On the seeded 1,000-case evaluation, 952 document events produced 568 grouped
motion candidates. 202 groups used explicit motion-document references and 366
used the conservative `re_no` fallback. Filing-context propagation raised event
subtype coverage to 521/952 (54.83%). Grouped subtype coverage was 218/568
(38.38%), with 10 subtype conflicts. These are coverage-of-extracted-signals
measures, not accuracy estimates; unresolved groups remain visible.
