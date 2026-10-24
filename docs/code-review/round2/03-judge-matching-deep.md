# Judge matching review — deeper pass

Scope: judge normalization, aliases, Federal Court activity matching, issue
records, and judge-specific analytics. FC, SCC and FCA only. No database rows
were queried. Current stored alias names and the example corpus counts in the
issue therefore remain unverified.

## Merge rules, thresholds, and aliases

- `parse_judge_name` repairs common mojibake, removes listed titles/suffixes,
  folds accents, and drops leading surname particles. A profile with an
  `assessor` title is rejected. Prothonotary role is retained for display, but
  role is deliberately ignored when merging
  ([`judge_normalization.py:16-32,50-130,144-151`](../../../backend/judge_normalization.py)).
- Full-name grouping requires equal normalized surnames, no explicit gender
  clash, and compatible given-name initials. Given-name token comparison is
  prefix-like because it zips the token tuples without requiring equal lengths.
  Candidates are greedily grouped by descending case count
  ([`judge_normalization.py:133-151,237-247`](../../../backend/judge_normalization.py)).
- Surname-only strings: one existing cluster receives compatible bare names;
  with no clusters, bare names are placed together except where explicit male
  and female titles split them; with multiple clusters, a bare name attaches to
  the dominant cluster if all other cluster counts total no more than
  `max(3, dominant // 50)`, otherwise it is left for review
  ([`judge_normalization.py:185-213`](../../../backend/judge_normalization.py)).
- `J.A.` forms are separated and attach to a full-name cluster only when date
  spans identify exactly one fit, with a 366-day tolerance. Otherwise they form
  their own group ([`judge_normalization.py:171-177,249-271`](../../../backend/judge_normalization.py)).
- FC activity rows match on normalized surname and compatible initials. A
  same-surname competing profile blocks ambiguous rows
  ([`judge_fc_activity.py:18-57`](../../../backend/judge_fc_activity.py)).
- There is no hardcoded name-alias dictionary in `judge_aliases.py`; aliases are
  stored as profile-ID to canonical-ID rows. `member_ids` follows one alias
  hop and returns direct members
  ([`judge_aliases.py:16-25`](../../../backend/judge_aliases.py)). The current
  database alias rows cannot be listed without querying the database.
- Other judge-analysis thresholds: issue visibility is 10 decisions
  ([`judge_issue_record.py:42,122-125`](../../../backend/judge_issue_record.py));
  shared comparison issues require five decisions per judge
  ([`analytics_service.py:1087-1089`](../../../backend/analytics_service.py));
  the profile-list cap is 2,000
  ([`analytics_service.py:870-908`](../../../backend/analytics_service.py)).

## Findings (ranked)

### 1. Medium — Alias chains lose earlier aliases from the canonical profile

**Location:** [`judge_aliases.py:21-25`](../../../backend/judge_aliases.py);
alias creation/reconciliation: [`scripts/apply_judge_aliases.py:79-92,158-175`](../../../scripts/apply_judge_aliases.py)

`member_ids` resolves only one level. With stored rows `A → B` and `B → C`,
requesting canonical profile C returns C and direct alias B, but omits A.
Requesting A resolves to B rather than C. The alias application script can
preserve an old canonical row while adding a new alias for that former
canonical, so a chain is possible. Expected: all members resolve to the final
canonical profile; actual: earlier links/cases can disappear from list and
profile totals.

**Suggested fix:** Flatten alias rows to direct canonical IDs when changing a
canonical profile, or resolve transitively with cycle detection; add a
three-profile regression test.

### 2. Medium — Panel parsing drops different co-judges with the same surname and first initial

**Location:** [`judge_normalization.py:312-324`](../../../backend/judge_normalization.py)

`parse_panel` deduplicates by `(surname, parsed.initials[:1])`. For
`Brown, Russell; Brown, Robert`, it retains Russell Brown and drops Robert
Brown. Expected: both panel members; actual: one. This affects SCC panel
backfills and any profile counts built from those parsed panels.

**Suggested fix:** Deduplicate only when full parsed names are compatible as
the same person, not merely when surname and first initial match.

### 3. Medium — Dominance threshold silently assigns ambiguous bare names

**Location:** [`judge_normalization.py:201-212`](../../../backend/judge_normalization.py)

The count threshold is treated as identity evidence. With
`Russell Brown: 100`, `Robert Brown: 1`, and `Brown J.: 2`, the current
normalizer attaches `Brown J.` to Russell and emits no review note. Expected:
the surname-only identity remains ambiguous; actual: it is merged with the
dominant candidate.

**Suggested fix:** Use the dominance calculation to prioritize review, not to
automatically assign identity without corroborating evidence.

### 4. Medium — Bare-only variants merge even when court context distinguishes them

**Location:** [`judge_normalization.py:192-200,251-259`](../../../backend/judge_normalization.py)

When there are no full-name clusters, `_attach_bare` groups all bare strings
without consulting the supplied court sets. For example, `Justice Brown` from
FC and `Brown J.` from SCC produce one group even if `courts` maps them to
different courts. Expected: leave unproven identities separate or flagged;
actual: one proposed merge. This edge case is not covered by the test that
scopes bare strings when a full-name cluster exists.

**Suggested fix:** Apply court scoping before the no-cluster branch and leave
cross-court surname-only cases for review.

### 5. Low — Given-name prefixes can merge distinct full names

**Location:** [`judge_normalization.py:133-141,241-247`](../../../backend/judge_normalization.py)

The zipped token comparison treats a missing middle token as compatible:
`John Smith` and `John A. Smith` are grouped. These might be the same person
with incomplete extraction, but could be two judges with the same first and
last names. Expected under conservative identity matching: flag the
abbreviation as ambiguous absent corroboration; actual: automatic merge.

**Suggested fix:** Require compatible token counts or mark prefix-only matches
for review unless separate court/date or approved-alias evidence supports them.

### 6. Possible, Low — Full-name grouping ignores available court and date conflicts

**Location:** [`judge_normalization.py:237-247`](../../../backend/judge_normalization.py)

Full-name clusters call `same_person` without using the optional `courts` or
`spans` evidence. Two distinct `John Brown` profiles in FC and SCC with
overlapping service dates would therefore merge if their parsed names match.
The identities may instead be one judge serving both courts; this is a
possible false merge, not a corpus-confirmed case.

**Suggested fix:** At minimum flag same-name, cross-court, overlapping spans
for review before applying an alias.

## Reported count / alias examples

- The list's `decision_count` is based on profile links
  ([`analytics_service.py:901-908`](../../../backend/analytics_service.py));
  profile detail deduplicates case IDs and excludes cases explicitly labelled
  `not_immigration` ([`analytics_service.py:1123-1128`](../../../backend/analytics_service.py)).
  Thus list/profile values such as Zinn `850` versus `590`, or McLachlin
  `2,011` versus `55`, can represent different denominators; these supplied
  counts were not independently checked. The profile response reports excluded
  cases, but the list's count does not identify its broader denominator.
- The issue's FCA Marc Noël → FC Simon Noël example is not verifiable without
  inspecting stored alias rows. The current helper consumes aliases as given;
  it does not recheck court or service dates. The alias script has an explicit
  prune path for stale rule rows, and its usage text names Marc/Simon Noël
  ([`scripts/apply_judge_aliases.py:6-15,79-92`](../../../scripts/apply_judge_aliases.py)).
  Therefore a corrected grouping rule alone does not establish that a prior
  stored alias has been removed.

## Limits

The examples of bad merges/splits above were reproduced with the pure
normalizer; no judge aliases, linked cases, or live count totals were read.
Current alias membership and the exact causes of the supplied Zinn/McLachlin
count differences could not be confirmed. The already-known second FCA date
branch finding is not repeated.
