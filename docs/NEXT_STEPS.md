# Next Steps

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

The no-network preparation pass completed for all 300 core cases in
`data/eval/llm_discussion_units_pilot/core_300_run`, including 300 deterministic
reports, 300 request payloads, a manifest, and a ledger. The approved first-10
API validation completed 9 cases and retained one raw response for failed case
`677`; no cases after the first 10 were attempted. Review the nine Markdown
files and the raw-error file before treating labels as useful metadata. Keep
model outputs report-only and separate from canonical citations, statutes,
tags, outcomes, and source offsets. Do not launch the remaining 290 cases or
the 2,500-case layer until the first-10 result is accepted and explicitly
approved.

## Recommended sequence

1. Produce deterministic input reports and a manifest for the 300 core cases.
2. Run a no-network preparation pass and inspect the manifest and ledger.
3. Review the first-10 hybrid Markdown and raw-error artifacts.
4. With explicit approval, run the remaining 290 cases through the same ledger.
5. Measure cost, malformed-response rate, coverage, and label usefulness.
6. Design database-owned persistence as a separate layer and task; do not add
	schema or canonical writes during this report-only preflight.
7. Expand to the 2,500-case list only after the core layer is accepted.
