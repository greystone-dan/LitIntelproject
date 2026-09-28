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
