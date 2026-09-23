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

Review the Markdown files before treating labels as useful metadata. Keep model
outputs report-only and separate from canonical citations, statutes, tags,
outcomes, and source offsets. Do not launch the 2,500-case layer until the
300-case layer has been reviewed and the ledger shows an acceptable failure and
cost profile.

## Recommended sequence

1. Produce deterministic input reports and a manifest for the 300 core cases.
2. Run a no-network preparation pass and inspect the manifest and ledger.
3. Run the bounded 300-case hybrid labeling pass with the ledger enabled.
4. Review the generated Markdown and raw-error files; retry only failed rows.
5. Measure cost, malformed-response rate, coverage, and label usefulness.
6. Expand to the 2,500-case list only after the core layer is accepted.
