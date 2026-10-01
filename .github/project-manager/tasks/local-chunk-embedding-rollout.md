# Task: Populate OpenAI chunk embeddings for RAG

Status: deferred
Created: 2026-09-30
Updated: 2026-09-30

## Task Record

Task: Establish a bounded, resumable process to embed every eligible `CaseChunk.text` with OpenAI vectors and measure retrieval readiness for the experimental `/research` RAG workflow.

Why now: Local embedding is too slow for the inventory; the user selected the OpenAI API so chunk retrieval can be populated promptly for plain-language questions and source-grounded generation.

Owner surface: `scripts/embed_openai_chunks.py` and the existing hosted chunk retrieval boundary in `backend/search_service.py`.

Commit allowed: yes

Push allowed: yes

Dependencies: Current deterministic processing run must finish before another PostgreSQL writer starts; `OPENAI_API_KEY` and OpenAI API access must be operator-configured; PostgreSQL/pgvector must be reachable; text generation remains a separate provider choice.

Risk boundary: Do not run concurrently with the active deterministic pipeline. Do not change canonical case text, chunks, citations, statutes, tags, outcomes, source HTML, offsets, or the text-generation provider. Do not exceed an explicit API budget or run beyond an explicitly frozen cohort during the first run. Do not present similarity or generated answers as legal conclusions.

Smallest falsifiable check: After the active writer is finished, run `scripts/embed_openai_chunks.py --dry-run --max-chunks 5`, then embed at most 2 chunks under a $0.01 cap and verify 1,536-dimensional rows plus focused hosted-search coverage.

Acceptance criteria:

- Freeze and record the intended case/chunk cohort before writing vectors.
- Populate `CaseChunk.embedding` idempotently for the selected cohort using `text-embedding-3-small`, dimensions 1536, without changing source or deterministic evidence layers.
- Verify vector counts, model name, dimensions, missing-embedding count, and no duplicate chunk writes.
- Verify hosted semantic retrieval returns bounded, source-identifiable chunks for a representative query; record retrieval quality as unmeasured until a judged query set exists.
- Keep text generation and retrieval configuration separate, with `/research` still returning retrieved source cases and excerpts.
- Focused validation passes and the canonical documentation plus relevant Swimm walkthrough are updated before completion.

Harness criteria:
Inventory identifies the existing local vector table/provider/runner and current coverage.
A frozen cohort and no-competing-writer preflight are recorded.
A bounded embedding canary passes with correct model and dimensions.
Retrieval returns source-identifiable chunks with bounded results.
Canonical repository documentation and Swimm walkthrough are updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `OVERNIGHT.md`, `.swm/5.b49ftjal.sw.md`, and the completed discovery record `.github/project-manager/tasks/local-rag-model-integration-discovery.md`. Generated schema/API references must be regenerated only if contracts change; do not hand-edit generated outputs.

Rollback/recovery: The runner was stopped on user request; committed vectors remain intact and null-vector filtering makes a later run resumable. Full resumed output is preserved at `data/overnight_runs/openai-embedding-frozen-20260930/resume-20260930.log`. Never delete other model versions or canonical rows.

Evidence: The delegated inventory found the resumable `scripts/embed_openai_chunks.py` runner, `CaseChunk.embedding` (`Vector(1536)`), token-aware batching, retries, budget enforcement, configurable progress output, and the experimental `/research` context-generation path. The runner now accepts a frozen `--case-ids-csv` allowlist, deterministic modulo partitioning with `--max-workers`, per-worker sessions/clients, and stale organization-header cleanup. `--progress-every 500` emits labeled worker progress to the terminal. `data/overnight_runs/openai-embedding-frozen-20260930/case_ids.csv` contains 61,257 cases and excludes the active 200-case deterministic cohort plus oversized cases `28926`, `13681`, `31518`, and `30537`. The allowlisted dry-run passed with `pending_sample=5`, `sample_tokens=178`, and `model=text-embedding-3-small`. The corrected 4-worker live canary embedded 77 chunks across four non-active cases for approximately `$0.0004`; verification found 79 total OpenAI vectors and 0 vectors for the active 200 cases. The first full run committed substantial partial progress but exited on an unhandled OpenAI 8,192-token input-limit error (`input[34]`); recovery now uses exact `tiktoken` preflight, records oversized chunk exclusions, and preserves successful worker commits. Focused recovery tests pass 4/4 and the allowlisted dry-run still passes.

Stop checkpoint: User-requested stop completed. Final counts: worker 1 `112,962/554,104`, worker 2 `27,114/554,072`, worker 3 `531,753/554,181`, worker 4 `117,009/554,102`; aggregate `788,838/2,216,459`. No embedding process remained. Relaunch used a `$17.90` estimated remaining budget and wrote stdout/stderr to `resume-20260930.log`; recovery tests passed 5/5.

Files changed: `scripts/embed_openai_chunks.py`, `tests/test_openai_chunk_embeddings.py`, `.github/project-manager/tasks/local-chunk-embedding-rollout.md`, `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/5.b49ftjal.sw.md`, and run artifacts under `data/overnight_runs/openai-embedding-frozen-20260930/`.
Delegated work: Explore agent performed a read-only inventory of embedding, retrieval, provider, script, test, and documentation surfaces; structured report consumed in this record.
Focused validation: `python -m pytest tests/test_openai_chunk_embeddings.py -q` passed with 5 tests; the allowlisted dry-run passed; editor diagnostics were clean; final process check confirmed the writer stopped; final per-worker vector count query completed.
Residual risk: 1,427,621 cohort chunks remain unembedded; hosted spend, retrieval quality, and oversized evidence-chunk coverage are incomplete. Oversized full-case rows are expected, while long section/paragraph chunks need a separate chunking decision. The active 200-case exclusion remains intact.
Next bounded task: Decide whether to exclude `full_case` rows and how to handle oversized paragraph/section chunks before any later embedding run.

## Hypothesis

If the existing resumable OpenAI embedding runner is used against a frozen cohort after the current writer is complete, then it will add idempotent 1,536-dimensional `text-embedding-3-small` vectors without changing canonical evidence layers and will make hosted chunk retrieval testable.

## Plan

1. Wait for and verify the active deterministic pipeline terminal checkpoint; do not compete for PostgreSQL writes.
2. Select and freeze a bounded representative case/chunk cohort; run the OpenAI embedding dry-run and preflight.
3. Run a 2-chunk OpenAI canary under a $0.01 cap, verify rows and model dimensions, and run focused provider/retrieval tests.
4. Expand only after the canary and retrieval quality gate pass; keep the run resumable and cohort-scoped.
5. Update `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `OVERNIGHT.md`, and `.swm/5.b49ftjal.sw.md` with the operational contract and evidence.

## Execution Checkpoints

- Delegation: Explore agent, read-only inventory; structured result stored in session output and summarized above.
- Implementation: Added an explicit `--case-ids-csv` allowlist, deterministic `--max-workers` partitioning, per-worker sessions, proportional budgets, and stale-organization-header cleanup to `scripts/embed_openai_chunks.py`; the active 200 cases are excluded from the frozen cohort.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `OVERNIGHT.md`, and `.swm/5.b49ftjal.sw.md` updated with the hosted contract and safety gate.
- Recovery: Frozen cohort identity is preserved under `data/overnight_runs/openai-embedding-frozen-20260930`; canary rows are committed only for the four test cases; active deterministic run remains the current writer.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-30 | Task created | User requested API-backed chunk embeddings as the foundation for plain-language RAG questions. | Existing hosted vector/retrieval infrastructure and delegated inventory |
| 2026-09-30 | Use existing OpenAI runner first | It is resumable, budget-capped, retrying, and writes the existing 1536-dimensional chunk contract. | `scripts/embed_openai_chunks.py`, `backend/database.py`, `backend/search_service.py` |
| 2026-09-30 | Defer automatic ingest embedding | Automatic model work during canonical ingest would increase latency and compete with deterministic processing before coverage and quality are measured. | Active deterministic writer; current local RAG discovery task |
| 2026-09-30 | Prefer OpenAI over local embeddings for inventory | Local embedding throughput is too slow for the current inventory; hosted API work is bounded by explicit spend and batch limits. | User decision; existing separate local 1024-dimensional contract |

## Completion

Completion recorded: no

Summary: Frozen non-overlapping cohort and allowlisted embedding path are ready; the 2-chunk live canary passed after removing the stale organization header.

Validation: Allowlisted dry-run completed; focused helper tests passed (3/3); live canary committed 2 vectors at 1536 dimensions under the `$0.01` cap; active 200-case vector count remained 0.

Residual risk: See the task-record residual-risk field.

Next recommended task: Choose the full-run budget and start the resumable allowlisted embedding run, keeping the active 200-case exclusion until its deterministic pipeline completes.
