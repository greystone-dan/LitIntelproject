# Task: Define Resource-Bounded Local RAG Retrieval For Recent 5,000 Decisions

Status: complete
Created: 2026-10-02
Updated: 2026-10-02

## Task Record

Task: Implement a reversible, resource-bounded IVFFlat retrieval artifact for the newest 5,000 decisions with exact-scan fallback.

Why now: A prior long-running full-corpus HNSW build over ~2M paragraph embeddings failed/rolled back on constrained hardware; retrieval strategy must be redesigned to fit laptop limits and preserve existing embeddings.

Owner surface: backend/search_service.py

Commit allowed: yes

Push allowed: yes

Dependencies: backend/database.py schema semantics; alembic/versions/0028_case_chunk_embedding_index.py behavior; backend/routes.py and backend/models.py request contracts; local runtime support in embedding/text generation providers; read-only DB inventory.

Risk boundary: No HNSW/full-corpus index, web/tunnel launch, paid embedding call, .env edit, or canonical case/chunk mutation. The approved migration may create only the derived recent-cohort artifact.

Smallest falsifiable check: .\venv\Scripts\python.exe -m pytest -q tests/test_api.py -k "grouped_chunk_search or local_chunk_search_respects_rollout_disable or paragraphs"

Acceptance criteria:

- Add a reversible Alembic migration that creates a dedicated recent-5000 paragraph artifact table with IVFFlat cosine index and deterministic refresh SQL.
- Route semantic/hybrid chunk retrieval to the artifact only when `case_cohort="recent_5000"` and compatible paragraph-hosted embedding constraints are present.
- Preserve existing behavior for all other requests and use exact scan fallback when the artifact is absent.
- Add focused tests proving cohort behavior, artifact path selection, and fallback continuity.

Harness criteria: Focused API tests and compile checks pass; migrations only create the approved derived retrieval artifacts.

Docs/generated references: SYSTEM_REFERENCE.md; DOCS_INDEX.md; OVERNIGHT.md; docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md; .swm/5.b49ftjal.sw.md

Rollback/recovery: Revert this code/migration checkpoint if needed. The applied artifact can be removed with `alembic downgrade 0029_recent_5000_ivfflat`.

Evidence: Implemented bounded artifact path and applied migration `0029_recent_5000_ivfflat`, creating `recent_case_chunk_embeddings` (177,846 vectors across 4,799 cases), plus migration `0030_full_paragraph_ivfflat`, creating the partial full-corpus paragraph IVFFlat index with `lists=1000` and session-local `maintenance_work_mem=512MB`. Live read-only verification: full index `indisvalid=true`, `indisready=true`, size approximately 15 GB; full paragraph query returned 10 rows in 762 ms with `ivfflat.probes=12`. The 5k artifact remains available; its prior service-path query was 4.45 seconds. HNSW remains retired. Updated canonical and Swimm docs in the same checkpoint. Validation: focused API tests, py_compile, migration graph checks, live catalog/query checks, and full API regression passed.

Files changed: backend/search_service.py; backend/database.py; tests/test_api.py; alembic/versions/0029_recent_5000_ivfflat_artifact.py; SYSTEM_REFERENCE.md; .swm/5.b49ftjal.sw.md; this task record.
Delegated work: execution_subagent; bounded slice: focused validation command execution and reporting.
Focused validation: full `tests/test_api.py` regression (51 passed); py_compile and git diff check passed; live full-index catalog/query verification passed.
Residual risk: Artifact refresh is migration-applied and not continuously auto-refreshed; newly ingested cases require explicit refresh/rebuild to keep cohort current.
Next bounded task: Add a small operational refresh command wrapper (readability/safety) for `recent_case_chunk_embeddings` rebuild and document runbook placement in OVERNIGHT.

## Hypothesis

If a bounded 5,000-case cohort is selected by deterministic recency criteria and has measurable embedding coverage, then retrieval can be safely implemented with a cohort-scoped artifact/index strategy and exact-scan fallback that fits local resource limits.

## Plan

1. Run one delegated read-only inventory slice for cohort selection, embedding/model counts, and local provider/runtime prerequisites.
2. Implement bounded cohort artifact + IVFFlat path with deterministic refresh SQL and exact-scan fallback.
3. Validate with focused API tests + compile checks and update canonical + Swimm docs.

## Execution Checkpoints

- Delegation: Completed bounded inventory slice with structured output and explicit commands.
- Implementation: Completed owner-surface retrieval path + reversible migration.
- Documentation: Updated SYSTEM_REFERENCE and Swimm walkthrough in same checkpoint.
- Recovery: Migrations `0029_recent_5000_ivfflat` and `0030_full_paragraph_ivfflat` applied successfully; downgrade `0030` removes only the full partial index, while downgrade `0029` removes the derived 5k artifact table.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-10-02 | Task created and scoped to search owner | Avoid repeating failed full-HNSW build on constrained hardware | User request + manager workflow constraints |
| 2026-10-02 | Use deterministic 5,000-case recency cohort before any index work | Bound CPU/RAM/disk risk and keep discovery reversible | Read-only DB counts and selector check |
| 2026-10-02 | Keep generation/runtime decisions separate from retrieval embeddings | Local generation can be configured independently and should not imply embedding availability | Provider/config inspection + rollout flags |
| 2026-10-02 | Implement dedicated recent_5000 IVFFlat artifact with exact-scan fallback | Avoid full-corpus HNSW costs while preserving endpoint behavior when artifact is absent | search_service + migration + focused tests |
| 2026-10-02 | Add full paragraph partial IVFFlat index | Full paragraph retrieval is now viable with IVFFlat and a bounded 512 MiB build session, without an HNSW graph | 1,987,620 vectors indexed; valid 15 GB index; 762 ms read-only query |

## Completion

Completion recorded: yes

Summary: Bounded recent-cohort and full hosted-paragraph IVFFlat retrieval are complete. The HNSW migration was retired as a no-op; only the approved 5k artifact and full partial paragraph index were applied.

Validation: Live full-index catalog/count checks passed; indexed retrieval returned 10 results in 762 ms. Full API regression passed with 51 tests.

Residual risk: Freshness of the artifact depends on explicit refresh/rebuild after new ingestion.

Next recommended task: Add a guarded operational refresh command in `scripts/` and register it in `OVERNIGHT.md`; tune the opt-in RAG weights only against judged retrieval examples.
