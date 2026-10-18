# Next Steps (Historical Snapshot)

> Archived on 2026-10-17. The current Discussion Unit review status and approval
> gate are maintained in [`STILL_TO_DO.md`](../STILL_TO_DO.md#contextual-and-advanced-intelligence).
> The detailed run guidance below is retained for history, not as current
> authorization to run additional cases.

## Discussion Unit labeling

The bounded case lists are ready:

- `data/eval/llm_discussion_units_pilot/discussion_unit_core_300.csv`
- `data/eval/llm_discussion_units_pilot/discussion_unit_priority_2500.csv`

Before any paid run, build a manifest with one row per case containing:
`case_id`, `input_json`, `output_request`, and `output_markdown`. Run the
cohort through `scripts/run_discussion_units_cohort.py` with a durable
`--ledger-path`.

The runner skips cases whose ledger status is `complete` or `failed`; failed
cases are retried only when `--retry-failed` is supplied. It never automatically
resends a completed case. Each case retains its request/result JSON, rendered
Markdown review, and `.raw_response.txt` when the model response is malformed.

At the time of the 2026-10-17 archive, the checked-in ledger for the 300-case
core cohort under `data/eval/llm_discussion_units_pilot/core_300_run` recorded
20 cases: 17 `complete` and 3 `failed` (`677`, `2044`, and
`2220`). This is artifact evidence; operational provenance has not been
independently verified. Review the ledger and available report/error artifacts
before treating labels as useful metadata or deciding whether to continue. Keep
model outputs report-only and separate from canonical citations, statutes,
tags, outcomes, and source offsets. Do not run additional cases or the
2,500-case layer until the available results are accepted and continuation is
explicitly approved.

At archive time, the sandbox loader expected paragraph-assessment files under
`data/eval/llm_discussion_units_pilot/paragraph_level_300_run/reviews`, but that
directory was absent in the checkout. When a per-case file is missing,
`backend/discussion_units_sandbox.py` returns `available: false`; those
assessments were unavailable in that checkout, not retained artifacts. The prepared
Discussion Unit artifacts remain under `core_300_run`. Earlier five-case,
20-case, single-case, and request-only paragraph pilots were removed on
2026-09-24 as obsolete.

Future improvement: evaluate a separate model-led paragraph discovery pass on
the approved sample. The model would receive source text without deterministic
paragraph metadata, return intro/body/outro and paragraph boundaries as
zero-based character offsets, and then feed those validated spans into the
Discussion Unit labeler. Keep this deferred until the current deterministic
path is accepted; preserve exact source-text reconstruction, offset checks,
and a side-by-side boundary comparison before considering it for production.

## Recommended sequence

1. Produce deterministic input reports and a manifest for the 300 core cases.
2. Run a no-network preparation pass and inspect the manifest and ledger.
3. Review the first-10 hybrid Markdown and raw-error artifacts.
4. With explicit approval, run the remaining 290 cases through the same ledger.
5. Measure cost, malformed-response rate, coverage, and label usefulness.
6. Design database-owned persistence as a separate layer and task; do not add
	schema or canonical writes during this report-only preflight.
7. Expand to the 2,500-case list only after the core layer is accepted.
