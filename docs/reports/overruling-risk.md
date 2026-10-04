# Overruling-risk indicators

## Purpose and limits

This feature surfaces a small, editable seed list of selected legal developments
as research prompts. It is not a treatment classifier, an exhaustive citator, or
a legal conclusion. A flag means only that a listed development may affect the
case and warrants independent review. Do not characterize a decision's continuing
legal force from this indicator.

Every seed entry and returned flag carries the exact notice **“seed list, needs
lawyer review.”** The reader uses “may be affected” language. The date comparison
helps identify chronology; it does not decide which legal framework governs a
case.

## Current seed

The initial seed contains one event:

- **Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65**
  (decision date: 2019-12-19), source:
  [CanLII](https://canlii.ca/t/j46kb).
- Rationale: The Supreme Court of Canada established a revised
  standard-of-review framework, displacing the pre-Vavilov framework. The seed
  identifies that framework event only; it does not determine whether or how
  the framework applies to any particular decision.

This entry was selected as a certain, expressly requested event. The list
intentionally does not infer additional overrulings or treatment events.

## Assignment and response

`GET /api/overruling-risk/{case_id}` is read-only:

- A **direct** flag is assigned when the requested case's citation or full case
  name matches a seed entry after case/punctuation normalization. When the case
  is itself the listed development authority, the response says that other
  cases may be affected; it does not misstate the authority as affected by
  itself.
- An **indirect** flag is assigned for each stored, resolved
  `Citation.source_case_id -> Citation.target_case_id` row from the requested
  case to a seeded authority. Each returned indirect flag includes the citation
  row identity and text where stored. A citation edge records a reference, not
  necessarily the reasoning, treatment, or legal effect of that reference.
- `counts.direct`, `counts.indirect`, and `counts.total` count returned flags;
  indirect counts are citation occurrences, not unique authorities.
- Dates include the requested decision date, the seed event date, and (for an
  indirect match) the authority decision date. Dates support chronology only.
- Each flag returns its source, rationale, literal review notice, cautious
  assessment, and `how_assigned` explanation. Missing cases return 404.

The active `/data-explorer` reader adds a non-blocking banner only when the API
returns at least one flag. For an indirect flag it says that the case may be
affected; for a direct match to the development authority, it identifies the
case as the listed authority and says other cases may be affected. Lookup
failure or an empty response does not create a warning. No memo output is
changed.

## Extending the seed list

Edit `OVERRULING_RISK_SEEDS` in
[`backend/overruling_risk.py`](../../backend/overruling_risk.py). For each new,
carefully verified event:

1. Add one entry with a stable `event`, canonical `case_name` and `citation`,
   conservative `match_case_names` and `match_citations`, ISO `date`, a
   traceable `source`, and a narrowly stated `rationale`.
2. Set that entry's `notice` to exactly **“seed list, needs lawyer review.”**
   The notice is part of the response contract; do not weaken it.
3. Prefer a primary/official decision source. Confirm that the source supports
   the stated event and rationale before adding it; do not seed a prediction,
   disputed treatment, or a broad doctrinal category.
4. Add fixture coverage for direct matching, citation-derived indirect
   matching, source/rationale/notice, counts and dates (including chronology),
   and the no-match case. Preserve the distinction between case citations and
   other legal-reference layers.
5. Keep the API assignment explanation synchronized with the matching rule.
   Do not interpret a stored citation as proof that a later case adopted,
   followed, distinguished, or was controlled by the authority.
6. Run the focused risk tests, relevant reader tests, generated-document check,
   and `git diff --check`; update this report, `SYSTEM_REFERENCE.md`, and the
   linked Swimm API and reader walkthroughs together.

Do not add a database table or migration for this list without a separately
approved design. The seed list is deliberately small, code-editable, and
reviewable.
