# API Search and Security Review

## Review scope and limits

- Requested scope: `backend/routes.py`, `backend/main.py`,
  `backend/search_service.py`, `backend/search_matching.py`,
  `backend/query_syntax.py`, `backend/search_thesaurus.py`,
  `backend/paragraph_search.py`, `backend/unit_keyword_search.py`,
  `backend/security_headers.py`, `backend/request_context.py`,
  `backend/resource_limits.py`, `backend/load_shedding.py`,
  `backend/degraded_mode.py`, `backend/db_limits.py`, `backend/health.py`,
  `backend/audit.py`, `backend/ai_mode.py`,
  `backend/embedding_providers.py`,
  `backend/query_embedding_providers.py`,
  `backend/text_generation_providers.py`, `backend/prompt_registry.py`,
  and every file under `backend/prompts/`.
- Court scope: Federal Court (FC), Supreme Court of Canada (SCC), and Federal
  Court of Appeal (FCA). Findings concern searches/research involving decisions
  in this scope, not claims about other corpora.
- Review basis: read-only inspection of the current checkout
  `copilot/code-review-api-search-security` at `22ebf9d` (`Initial plan`).
  The worktree was clean before this report was created.
- Base limitation: this checkout has no local `main` or `origin/main` ref and
  is shallow. Visible history ends at grafted commit `d2bcb41` (a merge of
  #629); it does not establish the current main tip or a reviewable merge base.
  No merge was attempted. GitHub issue metadata could not be retrieved because
  `gh` was unauthenticated; the user-provided scope and constraints were used.
- No tests, database, deployment, or live-site operations were performed.

## Bugs

### P2 — Case search may reference an undefined `chunk`

**Path:** `backend/search_service.py:479-481`

**Evidence:** In `execute_search_cases`, the `balanced_rag` ranking branch reads
`chunk.text`, but this function's loop handles case rows and does not assign a
`chunk`. If a request reaches this branch with results, it raises `NameError`.
The route calls this function for `/search` (`backend/routes.py:4117-4123`).
Whether the request contract permits this ranking mode was not verified because
the request-model definition is outside the requested scope.

**Suggested fix:** Remove passage scoring from case-level search, or explicitly
retrieve and pass the passage being scored. Add a focused route/service test for
the supported `balanced_rag` request contract.

### P3 — Non-finite compatible-provider timeout is accepted

**Path:** `backend/text_generation_providers.py:140-149`

**Evidence:** `CHAT_TIMEOUT_SECONDS` is parsed as a float and rejected only
when `<= 0`. `NaN` does not satisfy that comparison, and positive infinity also
passes, so either can reach client configuration.

**Suggested fix:** Require `math.isfinite(timeout_seconds)` as well as a
positive value, and reject invalid configuration with a clear error.

## Security risks

### P2 — Local mode does not constrain the Ollama endpoint to a local address

**Path:** `backend/text_generation_providers.py:168-179`

**Evidence:** In `local` mode, the Ollama provider uses configured
`OLLAMA_BASE_URL` without the locality validation applied to the
OpenAI-compatible provider (`:130-155`). The research route puts the user's
query and retrieved case excerpts into the generation message
(`backend/routes.py:4651-4654`), and the Ollama provider posts that message to
the configured URL (`backend/text_generation_providers.py:99-101`). Thus a
remote URL configured as the Ollama endpoint can receive that research
content while the application is in local mode. This is a configuration/code
path finding; no request was made during review.

**Suggested fix:** Enforce the intended local/private endpoint policy for
Ollama in local mode, and require a distinct explicit opt-in for remote
endpoints.

### User-query and memo provider-egress paths (evidence only)

These are conditional code paths, not evidence that any request or transmission
occurred during this review. Query-embedding and generation provider selection
are separate.

- **OpenAI query embeddings:** `/search` calls case search
  (`backend/routes.py:4117-4127`); `/search/chunks` calls chunk search
  (`:4235-4245`); `/search/chunks/paragraphs` invokes semantic paragraph
  search (`:4248-4258`); grouped search and `/research` invoke grouped search
  (`:4272-4280`, `:4609-4617`). When semantic/hybrid retrieval selects the
  OpenAI query provider, the query flows through `_embed`
  (`backend/search_service.py:113-124`, `:430`, `:678`) and
  `embed_query` (`backend/query_embedding_providers.py:166-186`) to
  `embeddings.create(input=texts, model=...)`
  (`backend/embedding_providers.py:91-103`). This path requires the
  configured OpenAI query provider and a mode that permits it. The local
  SentenceTransformer path encodes the query locally
  (`backend/search_service.py:624-654`;
  `backend/embedding_providers.py:141-163`).
- **Research answer generation:** `/research` includes `search.query` and
  retrieved excerpts in the provider message and calls the selected
  `create_chat_completion` (`backend/routes.py:4611-4617`, `:4644-4655`).
  Configured provider branches are OpenAI
  (`backend/text_generation_providers.py:38-48`, `:183-189`),
  OpenAI-compatible at configured `CHAT_BASE_URL` (`:62-69`, `:130-155`),
  and Ollama at configured `OLLAMA_BASE_URL` (`:77-101`, `:168-179`).
  The Ollama locality gap is the P2 finding above. These branches are
  configuration/mode dependent.
- **Memo citation check and uploaded document analysis:** the routes pass
  uploaded bytes to `analyze_memo_citations` and `analyze_document`
  (`backend/routes.py:1281-1315`, `:1402-1416`). The helper implementations
  are outside scope; these route calls do not establish whether those helpers
  invoke an outside model or provider.
- **De-identification:** `/api/deidentify` passes text and the
  `auto_names` option to `deidentify_text`
  (`backend/routes.py:1427-1436`, `:1456-1486`); the route describes
  automatic name-finding as model-based. The implementation is outside scope,
  so these lines do not establish whether it sends text to an outside provider.
- **Prompts:** `backend/prompts/research_system.txt` is loaded by the
  `/research` route (`backend/routes.py:4644`). The other prompt files contain
  prompt text, but no use or provider call for them is demonstrated in the
  scoped files. Prompt content alone does not establish that a query or memo
  was transmitted.
- **Health probes:** `backend/health.py:76-120` probes configured model
  endpoints; the scoped code does not put a user query or memo in those probe
  requests.

## Data-correctness risks

### P2 — Graph boost uses the last row's degree for every case

**Path:** `backend/search_service.py:458-483, 485-501`

**Evidence:** The preparation loop reads each row's graph in-degree but stores
only `(case, semantic_similarity, lexical_score)` at `:483`. The later scoring
loop therefore has only the final row's degree available for the graph boost
at `:498`. That same boost is applied to every row and cannot change their
relative ranking, so the intended per-case graph signal is lost.

**Suggested fix:** Retain each case's graph in-degree in the prepared tuple
and calculate that case's boost from its own value. Add a test with different
degrees and otherwise tied scores.

## Performance

### P2 — Case search materializes all matching candidates before paging

**Path:** `backend/search_service.py:439-454, 507-519`

**Evidence:** The query result is converted to a list before Python scoring
and sorting; pagination occurs after scoring/sorting. Broad FC, SCC, or FCA
searches can therefore load and process all matching case rows for one page.
The Search and Retrieval walkthrough also identifies this unbounded candidate
materialization as an existing limitation.

**Suggested fix:** Bound the candidate set and push filtering/ranking/paging
into SQL where semantics permit. Select only fields required for ranking and
the response, and validate the change with a fixed retrieval benchmark and
latency/candidate-count measurements.

## Dead code / cleanup

No separate dead-code or cleanup finding was identified in the inspected
scope. Duplicate or fragile route/UI code was not reported as a finding because
this review was limited to API search/security and no concrete defect in those
areas was established here.

## Suggestions

- Review the implementations behind `analyze_memo_citations`,
  `analyze_document`, and `deidentify_text` before making any claim about memo
  or uploaded-document provider egress; those implementations are outside this
  review's scope.
- Keep model-egress disclosures conditional on effective mode and provider
  configuration. The inspected code demonstrates provider request paths, not
  that a particular deployment enabled them or that a transmission occurred.
- After any ranking correction, run a bounded FC/SCC/FCA retrieval check that
  verifies both expected-case ranking and latency. No tests were added or run
  for this report-only issue.

## Files with nothing else worth flagging

No additional code findings were identified in:

- `backend/main.py`
- `backend/search_matching.py`
- `backend/query_syntax.py`
- `backend/search_thesaurus.py`
- `backend/paragraph_search.py`
- `backend/unit_keyword_search.py`
- `backend/security_headers.py`
- `backend/request_context.py`
- `backend/resource_limits.py`
- `backend/load_shedding.py`
- `backend/degraded_mode.py`
- `backend/db_limits.py`
- `backend/health.py`
- `backend/audit.py`
- `backend/ai_mode.py`
- `backend/embedding_providers.py`
- `backend/query_embedding_providers.py`
- `backend/prompt_registry.py`
- `backend/prompts/citation_aware_assessment.txt`
- `backend/prompts/citation_issue_focused_assessment.txt`
- `backend/prompts/citation_lightweight_issue_extraction.txt`
- `backend/prompts/citation_unit_context_assessment.txt`
- `backend/prompts/contextual_authority_teacher.txt`
- `backend/prompts/discussion_paragraph_assessment.txt`
- `backend/prompts/discussion_units.txt`
- `backend/prompts/model_paragraph_segmentation.txt`
- `backend/prompts/research_system.txt` (apart from the documented
  `/research` prompt-loading path above)

All requested files were inspected; none were unfinished.
