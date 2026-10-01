# Task: Local RAG and model integration discovery

Status: complete
Created: 2026-09-30
Updated: 2026-09-30

## Task Record

Task: Establish an evidence-backed path for retrieval-augmented generation (RAG) over the existing CaseLibrary data and local model use through the site.

Why now: The repository has substantial legal data and model-related components, but the current retrieval, embeddings, generation, provenance, and UI boundaries need to be made understandable before implementation.

Owner surface: Retrieval and local-generation integration design centered on `backend/search_service.py`, `backend/embedding_providers.py`, `backend/text_generation_providers.py`, and their existing API boundary.

Commit allowed: yes

Push allowed: yes

Dependencies: Existing database/schema, search and embedding providers, current API/UI workflow, local model runtime availability, and authoritative architecture documentation.

Risk boundary: Discovery and a bounded local experiment only. Do not change production access, source terms, canonical citation/offset ownership, database schema, bulk data, Government of Canada/CBSA integrations, or paid/external inference without explicit approval.

Smallest falsifiable check: Run the narrowest existing retrieval/provider tests identified by the inventory, plus a bounded provider/configuration check that demonstrates whether a local model can be selected without changing canonical data.

Acceptance criteria:

- Map the existing retrieval, embedding/vector, generation-provider, provenance, and site entry points with concrete file references.
- Identify the smallest safe local-model/RAG experiment and its required configuration, data boundary, and rollback.
- Implement only a bounded integration slice if the existing seams support it, otherwise document the exact blocker and next task.
- Focused validation passes for the touched slice; no unsupported claims about full-suite, browser, bulk, or production behavior.
- Update one canonical repository document and the relevant Swimm walkthrough with the resulting architecture and next step.

Harness criteria: Inventory identifies existing retrieval/vector/provider/site seams; Smallest experiment and risk boundary are documented; Focused validation result is recorded; Canonical document and Swimm walkthrough are named and updated.

Docs/generated references: `SYSTEM_REFERENCE.md`, `DOCS_INDEX.md`, `OVERNIGHT.md`, `docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md`, relevant `.swm/` walkthrough, and the canonical RAG/model integration document selected after inventory.

Rollback/recovery: Revert only the bounded code/documentation changes from this task; do not delete or rewrite existing data. Any experiment must use read-only or isolated data and leave a command/state artifact.

Evidence: Managed run `\.github/project-manager/runs/local-rag-model-integration-discovery-20260930-122236-c0fdfd9c` recorded the delegated inventory, focused provider test command, four passing criteria, and required documentation paths. The generated-document check was also run and reported pre-existing drift in `docs/API_REFERENCE.generated.md` and `docs/SCRIPT_CATALOG.generated.md`; those generated outputs were not edited because this slice changed no API or script contracts.

Files changed: `.github/project-manager/tasks/local-rag-model-integration-discovery.md`, `SYSTEM_REFERENCE.md`, `docs/CONFIGURATION_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md`
Delegated work: Explore agent performed a read-only inventory and returned exactly: `Files inspected:` SYSTEM_REFERENCE.md, DOCS_INDEX.md, OVERNIGHT.md, docs/SWIMM_AND_PROJECT_MANAGER_TRANSITION.md, backend/search_service.py, backend/embedding_providers.py, backend/text_generation_providers.py, backend/routes.py, backend/models.py, backend/database.py, config.yaml, .env template, docs/CONFIGURATION_REFERENCE.md, backend/pages/research.py, tests/test_text_generation_providers.py; `Files changed:` none; `Commands run:` none; `Results:` existing `/research` RAG route, grouped chunk retrieval, local BGE-M3 embeddings, Ollama provider, rollout flags, and source-returning contracts; `Failures:` none; `Uncertainty:` local vector coverage, Ollama model availability, context truncation semantics, and lack of browser/evaluation coverage; `Recommendation:` configure Ollama locally, select `TEXT_GENERATION_PROVIDER=local`, validate provider/API paths, and address retrieval evaluation/context assembly before production use.
Focused validation: `& .\venv\Scripts\python.exe -m pytest tests/test_text_generation_providers.py -q` passed: 6 passed, 1 warning. `git diff --check` passed. `tests/test_api.py -k research -q` found no matching tests (48 deselected), so no API behavior claim is made. `scripts/check_generated_docs.py` was run and failed on pre-existing drift in `docs/API_REFERENCE.generated.md` and `docs/SCRIPT_CATALOG.generated.md`.
Residual risk: Ollama installation/model availability, local hardware/latency, populated local chunk-vector coverage, retrieval quality, 12,000-character context truncation, browser behavior, model license/terms, and citation-grounded answer evaluation remain unverified. `/research` remains experimental and is not an authoritative legal-answer workflow. The generated-doc drift remains unresolved outside this slice.
Next bounded task: Build a read-only retrieval evaluation over a fixed, explicitly bounded question/case set, measuring chunk recall and evidence-span completeness before changing context assembly or making `/research` production-facing.

## Hypothesis

If the existing search and provider abstractions expose stable retrieval, embedding, and generation seams, then a bounded read-only local RAG path can be added or demonstrated without changing canonical records, source offsets, or production access controls.

## Plan

1. Read authoritative architecture and ownership documentation and consume the delegated inventory.
2. Select one owner surface and the smallest implementation or documentation slice supported by evidence.
3. Run focused validation immediately after the first edit, then update canonical and Swimm documentation.

## Execution Checkpoints

- Delegation: Explore agent, read-only architecture inventory; structured result consumed before implementation.
- Implementation: Updated the local-generation/RAG explanation and corrected the documented Ollama default; no database, API, or canonical evidence writes.
- Documentation: `SYSTEM_REFERENCE.md`, `docs/RESEARCH_UI_GUIDE.md`, `docs/CONFIGURATION_REFERENCE.md`, and `.swm/architecture-decisions-and-design-rationale.gwtegcrn.sw.md` updated.
- Recovery: No long-running operation planned; no bulk writer or external paid operation allowed.

## Decision Log

| Date | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| 2026-09-30 | Task created | User requested an understandable, actionable RAG and local-model setup path. | Managed-task request and repository structure |

## Completion

Completion recorded: yes

Summary: The repository already supports an experimental, read-only RAG path at `/research`. Local generation is enabled by selecting the Ollama provider; local embeddings are a separate BGE-M3 chunk-vector path. Documentation now explains setup, data flow, evidence boundaries, and production gaps.

Validation: Managed run completed its four declared criteria after the validating/documenting phases. Focused provider tests passed; patch whitespace passed. Generated-doc drift was detected and recorded without modifying generated outputs.

Residual risk: See the task-record residual-risk field; no live Ollama request, database retrieval measurement, browser check, or production deployment was run.

Next recommended task: Run the bounded retrieval-quality evaluation described in `Next bounded task`.
