# Language Analytics Evaluation Plan

## Scope and current limits

This is the review checklist for stage-1 phrase analysis; no corpus results are
claimed here. The feature is offline and read-only. It compares one exact
`cases.issues` label at a time, optionally restricted to one judge slug. Outcome
groups come from `metadata_json.reader_extracted["government outcome"]`:
`lost` is allowed/applicant-win, `won` is dismissed/Minister-win. `mixed`,
missing, and unrecognized values are excluded from both groups and reported as
excluded. The label `excluded_unclassified` includes every excluded
non-binary/unknown outcome.

Phrases are contiguous 2–4-token sequences, lowercased and deduplicated within
each decision. Document frequency counts decisions, not repeated occurrences.
A phrase needs at least five documents in its associated outcome group. The
score is the log2 ratio of group rates with one pseudo-observation for each
binary phrase status:

```text
log2(((allowed_phrase_docs + 1) / (allowed_decisions + 2))
     / ((dismissed_phrase_docs + 1) / (dismissed_decisions + 2)))
```

Positive scores indicate a higher allowed-group rate; negative scores indicate
a higher dismissed-group rate. A stable ascending case-ID order is used and
the hard/default query cap is 10,000 matching decisions. If `decisions_capped` is
true, this is a truncated cohort and may not represent all matching decisions.

## Required checks before interpreting a result

1. **Confirm cohort scope.** Record the exact tag label, optional canonical
   judge slug, scan cap, scanned count, and capped flag. Verify the label is the
   intended exact stored issue rather than a related label or free-text query.
2. **Audit outcome mapping.** For a review sample, compare stored
   `government outcome` values against the allowed/dismissed assignment. Confirm
   `mixed`, absent, blank, undetermined, and unfamiliar values are excluded and
   included in the reported excluded count, never silently assigned to either
   side.
3. **Check denominators.** Independently count distinct matching decisions by
   group in the same capped cohort. Confirm each phrase denominator includes
   all classified decisions in that group, not only phrase-bearing decisions.
4. **Check phrase extraction and document counts.** Manually inspect at least
   20 returned phrase/context pairs per group when available. Confirm each
   phrase has 2–4 contiguous tokens, punctuation does not join sentence words,
   repeated occurrences in one decision count once, and each returned row's
   allowed/dismissed document counts match a direct review. Check whether
   boilerplate, headings, copied submissions, or tokenization artifacts dominate.
5. **Check the threshold and ranking.** Confirm each emitted phrase occurs in
   at least five distinct decisions in its associated group. Recompute the
   smoothed group rates and log2 score for a small sample; allowed rows must
   have positive scores and dismissed rows negative scores, ordered by
   association magnitude. Confirm the endpoint returns no more than 25 rows
   per group.
6. **Check the capped-cohort caveat.** If capped, compare the result against a
   separately reviewed smaller cohort or a later approved offline evaluation.
   Record that ascending case-ID selection can reflect ingest order and do not
   generalize a capped result to the full tag population.
7. **Check judge filtering.** Compare an unfiltered result with one exact judge
   slug on a small reviewed cohort. An unknown slug must not fall back to the
   all-judge cohort.
8. **Check presentation and interpretation.** Verify that API, CLI, and page
   disclose denominators, excluded outcomes, and cap status. The caution must
   remain visible: these are associations in wording, not causes of outcomes,
   judicial characteristics, or evidence of bias.

## Record for each future evaluation

Save the exact tag and judge filter, date, cap/scanned/capped values, both group
denominators, excluded count, sampled decision IDs, phrase rows checked, score
recomputations, failures, and limitations. Do not make causal claims or
individual-judge performance claims from phrase frequencies. A capped result,
small group, or unreviewed phrase context is exploratory only.
