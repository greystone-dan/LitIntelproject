# Discussion Units: Weekly Review

**Date:** 2026-09-24  
**Status:** Core-300 preparation complete; 20 of 300 API cases attempted; full run not yet authorized or complete.

## Executive Summary

This week the project moved Discussion Units from a deterministic inspection concept into a bounded hybrid analytical workflow.

The work now produces a structured, reviewable representation of what a legal decision is doing across its paragraphs. The deterministic layer identifies paragraph boundaries and preserves existing legal signals. The hybrid layer asks `gpt-4.1-nano` to refine those spans into plain-language labels and explanations. Every output remains linked to the source paragraph range and remains report-only; canonical citations, statutes, tags, outcomes, offsets, and database records have not been changed.

The full core cohort of 300 cases has been prepared without network calls. Twenty API attempts have been run in two approved 10-case slices. Seventeen cases completed successfully and three were rejected by the coverage validator because the model did not cover every supplied paragraph exactly once. The sampled API spend was approximately $0.024 USD in total.

The next product step is human review of the Discussion Unit spans and labels. After that review, the core-300 run can be completed with the ledger and the accepted units can become a foundation for citation-context analysis, unit-level embeddings, cross-case comparison, and more explainable legal research workflows.

## What A Discussion Unit Is

A Discussion Unit is a contiguous span of legal paragraphs that performs one coherent task in the decision. Examples include:

- Procedural history
- Factual background
- Party submissions
- Legal test or governing framework
- Evidence assessment
- Analysis or application
- Treatment of an authority
- Disposition or remedy

The unit is not a replacement for a paragraph, citation, statute reference, tag, or source chunk. It is an additive analytical layer that groups related paragraphs while retaining the underlying source identity and offsets.

## Deterministic Foundation

The first stage is local and deterministic. The inspector reads the existing paragraph-level case data and builds a report containing the paragraph text, paragraph identity, and available legal signals.

For each paragraph or source span, the report can retain:

- Case and chunk identity
- Paragraph index and source paragraph index
- Canonical chunk hash and source provenance
- Heading status
- Citation memberships
- Statute or instrument memberships
- Legal tag memberships
- Signal density and continuity information
- Deterministic Discussion Unit ranges

The deterministic segmentation uses local continuity signals rather than a model making unsupported claims. It can identify changes in heading structure, citation or statute density, tag overlap, authority continuity, and paragraph-to-paragraph text continuity. The result is a reproducible baseline that can be compared with the hybrid output.

The deterministic layer is important even when the final labels are model-assisted. It gives the model a bounded paragraph window, supplies an initial segmentation for comparison, and preserves a source-grounded fallback. It also ensures that the workflow does not ask a model to invent paragraph identity or replacement offsets.

## Hybrid Method

The current hybrid method has four stages.

### 1. Inspect

`scripts/inspect_discussion_units.py` reads the existing paragraph data and writes a deterministic JSON report. This stage makes no external API calls and does not write canonical database records.

### 2. Prepare

`scripts/prepare_discussion_units_cohort.py` runs the deterministic inspector for the core list and creates the dedicated run structure. Each manifest row maps one case to:

- A deterministic input report
- An LLM request JSON path
- A rendered Markdown review path

The prepared request contains the numbered paragraph window and, unless text-only mode is selected, the deterministic baseline and legal signal metadata. The model is instructed to group contiguous paragraphs, use only the supplied indices, and cover the entire supplied window exactly once.

### 3. Refine With The Model

`scripts/package_discussion_units_llm.py` sends the bounded request to `gpt-4.1-nano`. The model returns JSON units with:

- Start paragraph
- End paragraph
- Plain-language label
- Short explanation
- Transition from the previous unit
- Confidence value

The model is not allowed to replace source paragraphs or create new source offsets. Its role is to refine the explanation and semantic grouping of the supplied paragraph window.

### 4. Validate And Render

The response parser requires contiguous, complete coverage. It rejects responses with gaps, overlaps, invalid paragraph indices, or omitted trailing paragraphs. Successful responses are rendered into Markdown for human review. Raw rejected responses are retained for diagnosis.

The Markdown output now begins with:

- Model name
- Prompt token count
- Completion token count
- Total token count
- Estimated billing in USD

The request JSON retains the original request and the response, including the complete usage object. The ledger records terminal case status, unit count, and usage or cost information for resumable execution.

## Resumable And Bounded Execution

The workflow uses a manifest and an atomic per-case ledger. The runner:

- Selects cases from an explicit manifest
- Skips terminal cases by default
- Does not resend completed cases
- Retries failed cases only when explicitly requested
- Records `started`, `complete`, or `failed` state
- Preserves standard output and error text for failed subprocesses
- Retains raw model responses when validation fails

This prevents accidental duplicate API spending and makes the run recoverable. The full 300-case preparation is complete, but the API boundary remains separate: only approved slices have been sent.

## Current Core-300 Status

### No-network preparation

The preparation pass completed for all 300 core cases:

- 300 deterministic input reports created
- 300 request payloads created
- One 300-row manifest created
- Dedicated reports, requests, and reviews directories created
- Ledger initialized for resumable execution
- No canonical database writes made

The primary run directory is [core_300_run](../data/eval/llm_discussion_units_pilot/core_300_run/).

### First approved 10-case slice

The first ten cases were sent before billing metadata was added to the text output. Nine completed successfully and one failed validation.

Successful cases:

`62`, `126`, `356`, `853`, `1046`, `1147`, `1292`, `1439`, `1540`

Failed case:

`677`

The successful cases produced Markdown reviews and response JSON. Case `677` retained a raw response and a validator error stating that the response did not cover every paragraph exactly once.

The first slice cost approximately `$0.0118017` in recorded model spend, or approximately `$0.001311` per completed case. This slice is retained as an early calibration sample; its text files do not all contain the later billing header, but its request and ledger artifacts preserve the recorded cost information available at that stage.

### Second approved 10-case slice

The next ten manifest rows were isolated into [next_10_manifest.csv](../data/eval/llm_discussion_units_pilot/core_300_run/next_10_manifest.csv) so that earlier failed cases were not accidentally retried.

Cases attempted:

`1748`, `1866`, `1901`, `1978`, `2044`, `2220`, `2517`, `2660`, `2788`, `2828`

Successful cases:

`1748`, `1866`, `1901`, `1978`, `2517`, `2660`, `2788`, `2828`

Failed cases:

`2044`, `2220`

The second slice cost `$0.0076567` in total. The average cost per completed case was `$0.0009570875`. The two failed API responses also incurred recorded costs:

- Case `2044`: `$0.0060967`
- Case `2220`: `$0.0004574`

The complete second-slice attempt cost, including the two rejected responses, was therefore `$0.0076567`.

Each successful Markdown review and each failed raw-response text artifact begins with model, token, and billing metadata. For example, see [case 1292](../data/eval/llm_discussion_units_pilot/core_300_run/reviews/case_1292_hybrid.md) and the failed [case 2044 raw response](../data/eval/llm_discussion_units_pilot/core_300_run/reviews/case_2044_hybrid.raw_response.txt).

### Combined status

Across the two approved slices:

- 20 API attempts
- 17 completed cases
- 3 rejected responses
- 85% completion rate in the observed sample
- Approximately `$0.0194584` recorded cost across the two slices
- Approximately `$0.00097292` per attempted case
- Approximately `$0.0011446` per completed case when using the reported slice totals and the 17 completed cases

The cost estimate is preliminary. The sample is small, and document length and paragraph count materially affect token usage. The remaining 280 cases have not been sent.

## What Failed And What We Learned

The three failures were not transport failures, authentication failures, or billing failures. The model returned structurally readable content, but the content did not satisfy the source-coverage contract.

The observed pattern was incomplete trailing coverage:

- Case `2044` was supplied a window through paragraph `243`, but the model stopped its final unit at paragraph `237`.
- Case `2220` was supplied a window through paragraph `19`, but the model stopped its final unit at paragraph `12`.
- Case `677` was rejected by the same exact-coverage validator in the first slice.

The raw JSON was retained for review, and the validator correctly prevented partial labels from being accepted as complete analytical output. The model prompt has since been strengthened to require an explicit final-unit check: the first unit must start at `first_allowed`, the final unit must end at `last_allowed`, and there must be no gaps or overlaps.

That prompt change is a mitigation, not proof that the issue is solved. Before the full 300-case run, we should measure whether the failure rate improves. A bounded retry or smaller-window continuation strategy remains available if incomplete coverage continues.

## Human Review Gate

Human review is the next substantive gate. The review should assess:

1. Whether the boundaries group paragraphs that perform one coherent legal task.
2. Whether labels are plain-language and useful to a legal researcher.
3. Whether explanations accurately describe the supplied paragraphs.
4. Whether transitions identify meaningful changes in legal task.
5. Whether confidence values are informative or merely clustered near the high end.
6. Whether citations and statutes appearing in a unit support the unit's interpretation.
7. Whether the deterministic baseline and hybrid result disagree in useful or problematic ways.

The review should preserve accepted, rejected, and needs-retry status. It should not silently edit source paragraph indices or overwrite authoritative citation and statute records.

## Intelligence Applications

Discussion Units create a useful intermediate representation between raw case text and higher-level intelligence. They make the decision's legal work observable at a meaningful scale while preserving exact source grounding.

### Citation context

A citation can be attached to the Discussion Unit containing its source paragraph. This changes the question from:

> Where is Mason cited?

To:

> What kind of legal work is being performed in the unit that cites Mason?

The unit can provide context for classifying the citation as support for a legal test, evidence assessment, factual comparison, analogy, distinction, procedural proposition, or disposition.

This remains a separate interpretation layer. The presence of Mason inside a unit does not by itself prove why Mason was cited. It supplies the bounded context needed for a reviewable citation-role analysis.

### Pinpoint authority pathways

When Case A cites Mason at a pinpoint paragraph, the citation can connect two analytical units:

- Source unit: the unit in Case A containing the citing paragraph
- Pinpoint: the citation's exact target paragraph in Mason
- Target unit: the reviewed unit in Mason containing that target paragraph

This enables unit-to-unit authority analysis. We can compare whether the source unit and target unit address the same legal task, whether the source case appears to follow or distinguish the authority, and whether multiple cases cite the same target unit for similar reasons.

The ordinary citation record, pinpoint resolution, source offsets, and target resolution should remain separate layers. The unit-to-unit link should be derived from those authoritative relationships rather than replacing them.

### Theme discovery

Plain-language labels and explanations can be normalized into candidate research themes. For example, several units may discuss variations of:

> RAD evidence evaluation and corroboration requirements

The system can group those units by label, legal tags, statutes, cited authorities, and paragraph-level evidence. Human review can then promote a recurring candidate into a stable research theme.

### Embedding units

Once Discussion Units have passed review, they are natural embedding inputs. Instead of embedding arbitrary fixed-size text chunks, the system can embed a meaningful legal span together with a controlled context package:

- Unit label and explanation
- Paragraph text
- Case metadata
- Citations and statutes within the span
- Legal tags and normalized topics
- Case ID, chunk identity, paragraph range, and source offsets
- Generation and review metadata

Embeddings can then find semantically similar units across cases. The embedding supports retrieval and clustering; the Discussion Unit and provenance metadata make the result explainable.

### Citation-aware similarity

A useful later experiment is to compare three similarity modes:

1. Text-only unit embeddings
2. Unit text plus legal metadata
3. Unit text plus citation and statute context

The first may find broad semantic similarity. The second may improve legal-topic grouping. The third may distinguish units that use similar language for different authorities or identify units that use different wording to perform the same legal task.

These modes should be evaluated against human-reviewed examples rather than assumed to be interchangeable.

### Research workflows

The combined layer could support queries such as:

- Show units that cite Mason for evidence evaluation.
- Find units discussing RAD corroboration requirements and compare their cited authorities.
- Show cases that distinguish a target authority at the unit level.
- Find the most similar units to a selected reader passage.
- Identify recurring legal tasks that are not captured by existing metadata subjects or tags.
- Compare how different courts structure analysis of the same statutory provision.

## What This Does Not Yet Claim

The current work does not yet establish that:

- All 300 cases have successful hybrid labels.
- The observed 15% failure rate generalizes to the full cohort.
- Model confidence is calibrated.
- A unit label proves the legal holding of a case.
- A citation appearing in a unit proves the citation's legal function.
- Embedding similarity proves doctrinal similarity.
- Discussion Units should be written into canonical database tables.

Those claims require human review, broader evaluation, and a separately designed persistence layer.

## Current Artifacts And Code

- [Deterministic inspector](../scripts/inspect_discussion_units.py)
- [Core-300 preparation script](../scripts/prepare_discussion_units_cohort.py)
- [LLM packager and validator](../scripts/package_discussion_units_llm.py)
- [Resumable cohort runner](../scripts/run_discussion_units_cohort.py)
- [Atomic ledger](../scripts/discussion_units_ledger.py)
- [Focused tests](../tests/test_package_discussion_units_llm.py)
- [Core-300 manifest](../data/eval/llm_discussion_units_pilot/core_300_run/manifest.csv)
- [Preparation summary](../data/eval/llm_discussion_units_pilot/core_300_run/preparation_summary.json)
- [Run ledger](../data/eval/llm_discussion_units_pilot/core_300_run/ledger.json)
- [Markdown review directory](../data/eval/llm_discussion_units_pilot/core_300_run/reviews/)
- [Next-steps runbook](NEXT_STEPS.md)
- [Discussion Unit task record](../.github/project-manager/tasks/discussion-unit-core-300-preflight.md)

## Recommended Next Steps

1. Human-review the available successful Markdown reviews and failed raw responses.
2. Record whether the boundaries and explanations are acceptable.
3. Decide whether the strengthened coverage prompt is sufficient or whether bounded continuation retries are needed.
4. Complete the remaining core-300 API run only after explicit approval.
5. Build the experimental Core-300 search and inline Case Reader scope using the existing UI and server-side cohort restriction.
6. Design database-owned persistence as a separate layer after the report-only workflow is accepted.
7. Add citation-to-unit and pinpoint-to-target-unit projections after the unit review gate.
8. Evaluate unit-level embeddings only after reviewed units and provenance are stable.

## References

- [System reference](../SYSTEM_REFERENCE.md)
- [Swimm Discussion Unit walkthrough](../.swm/8.upryk5h6.sw.md)
- [Next steps](NEXT_STEPS.md)
- [Project task record](../.github/project-manager/tasks/discussion-unit-core-300-preflight.md)
