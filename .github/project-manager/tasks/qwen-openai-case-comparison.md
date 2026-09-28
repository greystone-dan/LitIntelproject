# Task: Qwen/OpenAI case comparison

Status: complete
Created: 2026-09-25
Updated: 2026-09-25

## Task Record

Task: Run the existing Case 35868 discussion-unit request through local Qwen3 and compare it with the prior OpenAI result.

Why now: The project has a documented single-case OpenAI artifact and a callable local model; a matched replay will measure output-shape, coverage, latency, and qualitative differences.

Owner surface: bounded case-intelligence request runner and report-only evaluation artifact

Commit allowed: yes

Push allowed: yes

Dependencies: Ollama qwen3:4b; existing Case 35868 request; prior OpenAI raw response; local provider factory

Risk boundary: No OpenAI call, database writes, canonical enrichment, citation mutation, or bulk processing.

Smallest falsifiable check: The local replay produces a parseable response artifact for the exact existing request and records timing and model identity.

Acceptance criteria:

- The same Case 35868 windowed request is sent to Qwen3 locally.
- The local artifact preserves raw and parsed response, timing, and model metadata.
- A comparison report identifies unit coverage and schema differences against the prior OpenAI response.
- No canonical or database writes occur.

Docs/generated references: SYSTEM_REFERENCE.md; .swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md

Rollback/recovery: Delete only the new local replay and comparison artifacts; runner changes are additive behind `--provider local`.

Evidence: The existing Case 35868 historical request envelope was replayed through native Ollama Qwen3 using `scripts/run_case_intelligence_request.py`. The full 71-paragraph payload timed out after 120 seconds, so a bounded first-10-paragraph replay completed in 106.995 seconds with 2,050 prompt and 689 completion tokens. The Qwen output parsed but did not follow the `discussion_units[]` contract: it returned a case-summary object and identified the matter as `R. v. Febles`, 2013 SCC 5, instead of the supplied 2014 SCC 68 case. Comparison report: `data/eval/llm_discussion_units_pilot/case_35868_openai_qwen_comparison.md`. No database or canonical writes occurred.

Status: complete
