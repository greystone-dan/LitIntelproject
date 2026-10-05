# AI use statement

This describes code paths in the repository, not which settings or workflows
are currently enabled on a live machine. “AI” here covers embedding and
language-model calls; deterministic extraction is separately identified.

## Where models are used

| Use | Input and output | Runtime/activation | Evidence |
| --- | --- | --- | --- |
| Search query embeddings | Disabled by default. User query text reaches OpenAI embeddings only when `ENHANCED_AI_MODE=hosted` and `QUERY_EMBEDDING_PROVIDER=openai`; off mode downgrades semantic/hybrid requests to lexical. Local query inference requires the explicit local provider and an enabled enhanced mode; off mode makes no provider calls. | Lexical by default; hosted OpenAI and local query inference require explicit settings. | [backend/ai_mode.py](../../backend/ai_mode.py) [backend/query_embedding_providers.py](../../backend/query_embedding_providers.py) [backend/search_service.py](../../backend/search_service.py) |
| Experimental research answers | The question and retrieved case excerpts are submitted only when `ENHANCED_AI_MODE` is `local` or `hosted`. Hosted mode defaults to OpenAI. Local mode defaults to Ollama and may select an OpenAI-compatible endpoint only when its base URL is localhost/private; hosted compatible endpoints must be non-local. | `/research` returns a disabled response unless enhanced mode is explicitly enabled; provider-side retention and location depend on the configured endpoint and are not established by the code. | [backend/ai_mode.py](../../backend/ai_mode.py) [backend/routes.py](../../backend/routes.py) [backend/text_generation_providers.py](../../backend/text_generation_providers.py) |
| Build-time paragraph assessment/discussion units | Selected decision paragraph text is provided to a prompt. The model returns topics/roles/explanations or grouped discussion spans. The script validates and writes model output to operator-selected files. | Optional script workflow; model send requires `--send`. | [scripts/package_discussion_units_llm.py:137-160](../../scripts/package_discussion_units_llm.py#L137-L160) [scripts/package_discussion_units_llm.py:391-405](../../scripts/package_discussion_units_llm.py#L391-L405) [scripts/package_discussion_units_llm.py:472-552](../../scripts/package_discussion_units_llm.py#L472-L552) |
| Model-assisted paragraph segmentation experiment | Decision text is sent for model-proposed paragraph boundaries; returned offsets are checked against the source and text is derived locally. This is a bounded comparison, not the deterministic canonical extraction path. | Explicit experiment script run. | [scripts/run_model_paragraph_experiment.py:31-56](../../scripts/run_model_paragraph_experiment.py#L31-L56) [scripts/run_model_paragraph_experiment.py:70-102](../../scripts/run_model_paragraph_experiment.py#L70-L102) [scripts/run_model_paragraph_experiment.py:174-189](../../scripts/run_model_paragraph_experiment.py#L174-L189) |

The repository also contains optional audit, adjudication, and evaluation
scripts that call OpenAI or a local Ollama-compatible endpoint. Their inputs
and outputs depend on each script and invocation; they are not implicitly run
by the memo-citation-check request handler. Review a specific script before
running it with non-public material. Examples include
[scripts/adjudicate_fc_metadata.py](../../scripts/adjudicate_fc_metadata.py),
[scripts/verify_citation_extraction.py](../../scripts/verify_citation_extraction.py),
[scripts/run_treatment_teacher_batch.py](../../scripts/run_treatment_teacher_batch.py),
and [scripts/run_fc_activity_openai_structured_pilot.py](../../scripts/run_fc_activity_openai_structured_pilot.py).

## Generated versus deterministic

- Case/statute citation extraction and uploaded-memo citation checking use
  deterministic code and local database lookups; the inspected memo path does
  not call an LLM. [backend/memo_citation_check.py:102-129](../../backend/memo_citation_check.py#L102-L129)
  [backend/live_analysis.py:224-260](../../backend/live_analysis.py#L224-L260)
- Embeddings are model-generated numeric representations of query text; they
  are not citations, legal findings, or determinations.
- Paragraph assessments, discussion-unit labels/explanations, and `/research`
  answers are model-generated text. They are not source text and may be
  incomplete or incorrect.
- The build-time paragraph script describes results as provisional and
  read-only, keeps source paragraphs authoritative, and declares no canonical
  or contextual writes in its report. [scripts/package_discussion_units_llm.py:132-143](../../scripts/package_discussion_units_llm.py#L132-L143)
  [scripts/package_discussion_units_llm.py:263-285](../../scripts/package_discussion_units_llm.py#L263-L285)

## Labelling and human verification

The build-time assessment Markdown includes the model name, token counts, and
assessment fields. The generation response is not itself verified legal
analysis. Compare every paragraph label/explanation to the source decision;
check input identity, source offsets, missing or unmatched rows, and model
output before reuse. Do not treat a model confidence field as proof of
correctness. [scripts/package_discussion_units_llm.py:254-285](../../scripts/package_discussion_units_llm.py#L254-L285)
[scripts/package_discussion_units_llm.py:202-251](../../scripts/package_discussion_units_llm.py#L202-L251)

The `/research` prompt requests evidence labels and includes a research-aid
disclaimer; this is prompt/response behavior, not a guarantee of accuracy or
grounding. Verify any proposition and citation against the underlying decision
and an authoritative source. [backend/routes.py:3595-3601](../../backend/routes.py#L3595-L3601)
[backend/routes.py:3872-3903](../../backend/routes.py#L3872-L3903)

## Position for departmental review

**Proposed position: research support, not automated decision-making about
clients.** The described tools support search and document review; repository
code does not establish or authorize automated decisions about a person.
Whether that position is applicable to a department's intended use is for the
department to decide. Human review, use limitations, and any required
governance controls must be specified by the department.

## External processing

OpenAI receives semantic query text only when enhanced mode is explicitly
`hosted` and `QUERY_EMBEDDING_PROVIDER=openai`; `/research` question and
excerpts are sent to OpenAI only when enhanced mode is hosted and the selected
text-generation provider is OpenAI. Local mode selects Ollama for generation
and allows only the local query embedding provider. Build-time assessment
scripts remain separately and explicitly invoked. Confirm the actual Ollama
URL because it can be overridden. Provider region, retention, training/data-use
terms, and account settings are not established by application code. See
[subprocessors](subprocessors.md).
