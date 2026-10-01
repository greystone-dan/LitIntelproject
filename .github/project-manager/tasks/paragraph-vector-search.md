# Task: Make paragraph embeddings searchable

Status: in-progress
Created: 2026-10-01
Updated: 2026-10-01

Task: Add indexed, paragraph-only semantic retrieval for the completed OpenAI paragraph vectors.
Why now: The authorized paragraph cohort is embedded, but semantic retrieval needs an efficient PostgreSQL vector index and an explicit paragraph endpoint before relevance testing.
Owner surface: `backend/search_service.py`, `backend/routes.py`, `backend/models.py`, and the Alembic index migration.
Dependencies: PostgreSQL with pgvector, existing `text-embedding-3-small` query embedding provider, current chunk search contracts.
Risk boundary: Additive endpoint and reversible index only; preserve existing vectors, chunk rows, lexical search, local embeddings, and current endpoint behavior.
Smallest falsifiable check: Focused API test confirms the paragraph endpoint compiles a semantic query with `chunk_set='paragraph'`, non-null vectors, and the expected model.
Acceptance criteria: HNSW cosine index migration exists; paragraph semantic endpoint is exposed; existing search behavior is preserved; focused tests pass; migration and docs are recorded.
Docs/generated references: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/5.b49ftjal.sw.md`; generated references only through generators if required.
Rollback/recovery: Downgrade the additive index migration and remove only the additive endpoint/filter code; no vector data mutation.
Evidence: Historical validation: 49 API tests passed and touched modules compiled. Current read-only resource diagnosis verifies PostgreSQL is local on C:, diagnostic defaults maintenance_work_mem=64 MiB/shared_buffers=128 MiB, machine RAM 11.84 GiB/free 2.41 GiB, disk free 153.54 GiB, disk read snapshot about 102 MiB/s. Main build PID 47696 advanced from 810,994 to 811,922 tuples in about 26 seconds with no blockers; PID 44412 waits on its transaction. Other client sessions idle. Live command reports CREATE INDEX, so source migration changes do not establish that this build is concurrent. No processes or settings changed. Canonical checkpoint: `OVERNIGHT.md`; Swimm checkpoint: `.swm/5.b49ftjal.sw.md`.
Delegated work: Bounded read-only runtime diagnostic returned proposed code instead of executed evidence; manager performed bounded direct diagnostic recovery and rejected unsupported conclusions.
Residual uncertainty: Diagnostic-session settings may differ from build session; graph memory spill unproven; one disk snapshot cannot attribute all I/O. Index not yet catalog-visible or complete.
Status: in-progress
Commit allowed: no
Push allowed: no
