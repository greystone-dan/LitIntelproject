# Outcome review — deeper pass

Scope: outcome derivation and storage, case summaries/frames, and other
winner/outcome displays. This review is limited to FC, SCC and FCA. No database
rows were queried; examples are synthetic source-level traces.

## Label and assignment map

| Value | Labels / rule | Where it is set or consumed |
| --- | --- | --- |
| `decision_outcome` | `allowed`, `granted`, `dismissed`, `set_aside`, `remitted`, `withdrawn`, `mixed`, `procedural`, `unclear`; missing extraction can remain `None`. Synonyms (including `denied`, `refused`, `rejected`, `upheld`, and `accepted`) normalize through `_VERB_LABELS`. | `_decide` and `_derive_outcome_fields` in [`metadata_outcomes.py:175-183,595-649,836-872`](../../../backend/metadata_outcomes.py). The dedicated `CaseOutcome` builder stores it at `:916-938`; the compatibility metadata layer also stores a headline field. |
| Government result | `won`, `lost`, `mixed`, `undetermined`, derived by combining the disposition with government role. | Compatibility `government outcome` and `outcome status` are set at [`metadata_outcomes.py:848-870`](../../../backend/metadata_outcomes.py); the dedicated row's `government_outcome` is assigned at `:916-930`. |
| Winner / loser | `applicant`, `respondent`, `mixed`, or null. The compatibility fields derive sides from government role/result; the structured detail derives them from applicant-relative disposition. | Compatibility `case winner`/`case loser`: [`metadata_outcomes.py:862-867`](../../../backend/metadata_outcomes.py). Structured `winner`/`loser`: `:897-904`, then row `winner_side`/`loser_side`: `:925-927`. |
| Checker labels | `allowed`, `dismissed`, `mixed`, `procedural`, `unclear`; it maps `granted`, `set_aside`, and `remitted` into the allowed comparison class. | [`outcome_checker.py:23,82-99`](../../../backend/outcome_checker.py). This is an advisory second opinion, not a write to the deterministic result. |
| Frame wording | Prior-level outcomes use the separate `_OUTCOME_WORDS` vocabulary; the current decision result line maps the stored `decision_outcome` through a fixed display map. | [`case_frame_plus.py:203-216`](../../../backend/case_frame_plus.py), [`case_frame_store.py:23-32,56-66`](../../../backend/case_frame_store.py). These values are not a second normalized `CaseOutcome`. |

The ordered case-processing path runs metadata before the outcome stage
([`case_processing.py:22,42-55,148-156`](../../../backend/case_processing.py)).
Both derive from the same classifier, but separately stored compatibility
metadata and versioned `case_outcomes` can diverge when a backfill or a later
assignment updates only one. Comparison and summary-card readers prefer the
latest table row; search and judge analytics read the metadata mirror.

## Values that can disagree

1. **Same name, different perspective (confirmed by code):** the compatibility
   `reader_extracted["outcome status"]` is the government result
   ([`metadata_outcomes.py:855-868`](../../../backend/metadata_outcomes.py));
   `case_outcomes.outcome_status` is applicant-relative
   ([`metadata_outcomes.py:897-925`](../../../backend/metadata_outcomes.py)).
   With an individual applicant, Minister respondent, and an allowed
   application, the legacy status is `lost`, while the table status is `won`;
   the table's separate `government_outcome` is `lost`. These are different
   perspectives under the same unqualified field name.
2. **Compatibility headline versus table row (possible):** the versioned
   backfill reads the metadata but inserts only `CaseOutcome`
   ([`scripts/backfill_case_outcomes.py:31-49`](../../../scripts/backfill_case_outcomes.py)).
   Conversely, the FCA headline filler updates only a blank metadata value and
   leaves nonblank values untouched
   ([`scripts/fill_fca_headline_outcomes.py:55-60,104-120`](../../../scripts/fill_fca_headline_outcomes.py)).
   An old `dismissed` headline can therefore coexist with a newly derived
   `allowed` table row. The summary-card/comparison path can show the table
   result while metadata-backed search/analytics show the headline.
3. **Other independent projections:** `FramePlus.disposition` and its earlier
   `levels[].outcome` are regex extractions, not normalized table fields
   ([`case_frame_plus.py:203-216,419-440`](../../../backend/case_frame_plus.py)).
   `outcome_checker` is separately labelled advisory data. Either may disagree
   with the canonical table without changing that row.
4. **Different row-selection rules (possible):** summary, summary card, and
   frame result select the greatest `updated_at` and ID, without filtering to
   the current classifier version ([`case_summary.py:294-296`](../../../backend/case_summary.py),
   [`case_summary_card.py:338-342`](../../../backend/case_summary_card.py),
   [`case_frame_store.py:79-82`](../../../backend/case_frame_store.py)).
   If an older-version assignment is updated later than the current row, those
   surfaces can display the older classifier's answer. No such rows were
   inspected.
5. **Mixed versus unclassified in judge summaries (confirmed):** the overall
   judge outcome counter treats every value other than `won`/`lost` as
   `unclassified` ([`analytics_service.py:325-340`](../../../backend/analytics_service.py)).
   For a stored `government outcome="mixed"`, it increments that bucket. The
   judge-issue path instead preserves `mixed` as `other`
   ([`judge_issue_record.py:57-71`](../../../backend/judge_issue_record.py)).
   The same known result can thus be presented as unclassified overall but
   other in issue results.
6. **Display labels differ:** a stored `unclear` becomes “unclassified” in Quick
   Summary, remains `unclear` in the summary card, and produces no frame result
   line ([`pages/case_quick_summary.py:45`](../../../backend/pages/case_quick_summary.py),
   [`case_summary_card.py:312-319`](../../../backend/case_summary_card.py),
   [`case_frame_store.py:56-66`](../../../backend/case_frame_store.py)).

## Findings (ranked)

### 1. Medium — French merits review petition can be labelled procedural

**Location:** [`metadata_outcomes.py:579-585`](../../../backend/metadata_outcomes.py)

`_decide_french` puts every match whose subject begins `la requête` into
`motions`; if no other ruling remains, it returns `procedural`. For an FC/FCA
merits order ending `LA COUR ORDONNE que la requête de contrôle judiciaire soit
accueillie`, the expected label is `allowed`; the current branch returns
`procedural`. The result then has `outcome_status="undetermined"` and no winner
([`metadata_outcomes.py:841-844,892-904`](../../../backend/metadata_outcomes.py)).

**Suggested fix:** Distinguish a merits `requête de contrôle judiciaire` from a
motion/leave request and add French FC/FCA positive and negative fixtures.

### 2. Medium — `outcome status` has opposite orientations in the two records

**Location:** [`metadata_outcomes.py:855-868,897-925`](../../../backend/metadata_outcomes.py)

For an individual applicant and the Minister as respondent, an allowed
application gives compatibility `outcome status="lost"` (government lost) and
table `outcome_status="won"` (applicant won). The distinct table
`government_outcome="lost"` makes the intended perspective recoverable, but
consumers of the identically named status fields can report opposite answers.

**Suggested fix:** Give the fields explicit perspectives or make the mirror
orientation consistent; keep government-relative and applicant-relative
outcomes separately named and documented.

### 3. Low — Explicit mixed results disappear into “unclassified” in overall judge statistics

**Location:** [`analytics_service.py:325-340`](../../../backend/analytics_service.py);
contrast: [`judge_issue_record.py:57-71`](../../../backend/judge_issue_record.py)

A case with `reader_extracted["government outcome"]="mixed"` is counted as
unclassified in profile and comparison outcome totals, even though the issue
summary recognizes it as `other`. Expected: a known mixed result remains
distinguishable from absent/unrecognized data; actual: it is included in the
unclassified bucket.

**Suggested fix:** Add a separate mixed/other count to overall profile outcomes;
continue excluding it from binary win-rate denominators.

### 4. Low — Stored headline/table disagreement is possible after one-sided updates

**Location:** [`scripts/backfill_case_outcomes.py:31-49`](../../../scripts/backfill_case_outcomes.py);
[`scripts/fill_fca_headline_outcomes.py:55-60,104-120`](../../../scripts/fill_fca_headline_outcomes.py)

The two update paths do not reconcile the other stored representation. If a
case's text now yields `allowed` but its compatibility headline remains
`dismissed`, table-preferred readers and metadata-backed analytics can disagree.
This is a possible stale-row condition; no corpus rows were examined.

**Suggested fix:** Reconcile the mirror during outcome reprocessing, or make all
outcome consumers use the documented table source of truth.

### 5. Low — Current-version status is not part of “latest assignment” selection

**Location:** [`case_summary.py:294-296`](../../../backend/case_summary.py),
[`case_summary_card.py:338-342`](../../../backend/case_summary_card.py),
[`case_frame_store.py:79-82`](../../../backend/case_frame_store.py)

These readers select by timestamp/ID only. If a row from an older classifier
version is updated after the current-version row, it becomes the displayed
answer. This is conditional on multiple rows and their update order; no
database rows were inspected.

**Suggested fix:** Explicitly define latest-assignment precedence or filter to
the active classifier version, with a migration/backfill policy for older rows.

## Limits

I did not inspect corpus values, run outcome tests, or verify the reported
frequency of stale rows or version conflicts. The French example is a synthetic
FC/FCA input traced through the rules. The excluded withdrawn-winner and
`balanced_rag` NameError findings are not repeated here.
