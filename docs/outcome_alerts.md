# Outcome-aware saved-search alerts

`GET /saved-searches/{search_id}/alerts?since=<ISO datetime>` returns previously
recorded `SearchAlert` matches for an existing saved search. When `since` is
provided, only alerts with a later `discovered_at` are returned. Each decision
includes its stored outcome, if available, and a concise match reason from the
stored `match_type` and optional relevance score. This read does not perform a
search, discover new alerts, or advance `last_alert_check`; an unknown saved
search returns 404.

The `authority_watch` starts with resolved case authorities cited by those
matching results. For each authority, it counts distinct decisions citing that
authority in the latest and preceding calendar 12-month windows. The numerator
is the number whose stored `CaseOutcome.government_outcome` is `lost` (against
the Minister); the denominator is all citing decisions in that period, including
decisions without a stored outcome. Both counts and denominators are returned.
If either denominator is under 8, `comparison_suppressed` is true and
proportions are omitted. These descriptive comparisons do not establish
causation or corpus completeness.

`GET /saved-searches/{search_id}/alerts-ui` is a plain HTML page that fetches
and displays the JSON response.

## Offline input and execution

`scripts/build_outcome_alerts.py` calls the same pure calculation without
importing the database layer or connecting to services. Its JSON input has:

- `saved_search`: an object with `id` and an `alerts` array. Alert items contain
  `case_id`, `match_type`, optional `relevance_score`, and ISO `discovered_at`.
- `cases`: result decisions and corpus decisions, each with `id`, `date`, and
  `citations` items. A citation uses `target_case_id` for a resolved case
  authority; unresolved and statute rows are excluded.
- `outcomes`: stored outcomes with `case_id`, `government_outcome`, and
  `source`; optional evidence and timestamps are retained for matches.
- Optional top-level `since`: ISO datetime used to filter recorded alerts.

Run `python scripts/build_outcome_alerts.py --help` for CLI options. The script
writes JSON to stdout by default or to a path supplied with `--output`; `--as-of`
sets a deterministic reference time for the 12-month windows. Windows are
calendar-based, not fixed 365-day approximations.

The script does not read live saved-search records or prepare/export input.
Windows scheduling guidance is in
[`docs/operators/schedule_outcome_alerts.md`](operators/schedule_outcome_alerts.md).
