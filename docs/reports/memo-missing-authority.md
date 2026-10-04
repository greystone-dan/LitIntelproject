# Memo missing and contrary authority suggestions (#149)

## Scope

Memo Citation Check now adds descriptive suggestions based on authorities
actually cited by decisions sharing the memo's deterministic tags or statutes.
Existing citation, treatment, related-authority and missing-authority results
remain unchanged. No new dependencies, persistence, logging, external resolution,
migrations or deployment changes are introduced.

## Statistical definitions

The cohort is the union (**OR**) of canonical decisions sharing at least one
deterministic memo V3 tag or exact normalized statute reference. A tag requires
category **AND** value on the same stored row and the active V3 taxonomy.
Nested statute identities remain exact; a base section is not a substitute.

Only authorities actually targeted by resolved stored citations from cohort
decisions are candidates. Memo-resolved authority IDs, matching citation and
secondary-citation identities (including FC/FCT variants), and exact normalized
full adversarial titles are excluded. Repeated citation occurrences count once
per source decision and authority. Rank is descending distinct citing decisions,
then ascending authority ID. Each explanation unions only shared tags/statutes
from the decisions actually citing that authority.

Missing frequency is `distinct citing decisions / checked cohort decisions`,
including cohort decisions with no resolved outgoing citation.
Outcome counts partition the distinct citing decisions into Minister **won**,
**lost**, **mixed**, and **unclassified**. The source is the stored
`cases.metadata_json.reader_extracted["government outcome"]`, as used by judge
analytics; `CaseOutcome.outcome_status` is not used because it can be
applicant-relative. No disposition or party-name inference occurs.

Contrary suggestions are uncited candidates whose Minister-lost count is a
strict majority of **all** their checked citing decisions, including mixed and
unclassified decisions in the denominator, and which have at least five citing
decisions. The response reports majority-lost candidates hidden by that minimum.
Unclassified records never become wins or losses. Contrary candidates are
computed before the missing display limit.

## Limitations and interpretation

**Suggestions, not legal advice.** A citation does not establish endorsement,
relevance to a particular argument, or negative treatment of another authority.
“Contrary” describes the outcomes of citing decisions, not the holding of the
authority, and does not infer the memo's position. Users must read the decisions.

The cohort is capped at 500 decisions in ID order, with one lookahead; distinct
resolved edges are capped at 10,000 in source/target ID order, with one lookahead.
Truncation is explicitly partial coverage, not a representative sample. Counts,
outcome distributions and rankings can change with full coverage. Each list
shows at most ten authorities and separately reports pre-display totals.
Stored tagging, statute extraction, resolution, and outcome coverage determine
recall. Unresolved stored citation edges are omitted; textual exclusions are
conservative exact identities, not fuzzy party-name resolution.
Existing extraction does not fully support every provision spelling: an invented
`IRPA s. 112(2)(b.1)` fixture currently extracts only `112(2)`, while
`paragraph 112(2)(b.1) of IRPA` is not extracted. This change does not alter those
legacy rows. Suggestions omit an extracted statute signal when its source span
visibly stops before another parenthesized component, instead of matching a
broader subsection. Exact supported `34(1)(f)` and `245(1)(c)` forms are tested.
The legacy page's existing completeness wording and treatment interpretation are
unchanged; the separate suggestions section explicitly disclaims completeness.
Query result caps bound returned rows, not guaranteed database scan time;
production query plans and corpus recall remain unmeasured.

No live query, database benchmark, production upload, or deployment is performed
for this change. Existing document extraction/resource limits are reused once;
only derived lookup signals reach suggestion queries, not memo text. Existing
multipart/server retention and access-control limitations remain unchanged.

## Validation evidence

Validation uses an isolated `/tmp/caselibrary-149-venv` with existing declared
dependency pins only (no requirements changes). A temporary
`/tmp/caselibrary-offline149/sitecustomize.py` replaces `dotenv.load_dotenv`
before application imports and rejects non-SQLite SQLAlchemy connections.
This prevents the existing `tests/conftest.py` PostgreSQL availability probe from
connecting. The broad suite's invented temporary/in-memory SQLite fixtures are
allowed; no canonical/local/remote PostgreSQL or repository `.env` is accessed.
The same guard is inherited by documentation-generator subprocesses through
`PYTHONPATH=/tmp/caselibrary-offline149:$PWD`.

Passed checks:

- First focused helper/legacy run: **29 passed**. The worker's initial pytest
  attempt was blocked by missing runtime dependencies; the manager installed
  already-declared pins and independently ran its SQL/fixture tests.
- Memo, nested extraction, route/response and static UI tests plus adjacent
  live-analysis, feature-tab and citation checks: **267 passed, 1 skipped,
  1 xfailed**. An initial invented dotted-paragraph expectation exposed the
  existing extractor limitation; the same-slice guard and supported exact-span
  tests passed afterward.
- Final focused memo and documentation-inventory check:
  `python -m pytest -q tests/test_memo_authority_suggestions.py
  tests/test_memo_suggestion_integration.py tests/test_memo_citation_check.py
  tests/test_documentation_contracts.py`: **38 passed**.
- `python scripts/check_generated_docs.py`: **3 references current**, no
  generated files changed.
- `python -m py_compile` on all changed/new Python implementation and tests,
  local documentation-link existence review, and `git diff --check`: passed.
- Fixture-only Google Chrome (`/opt/google/chrome/chrome --headless=new
  --no-sandbox --disable-gpu --disable-dev-shm-usage --dump-dom` with network
  resolution disabled) rendered the actual page with an invented payload:
  numerator/cohort denominator, all outcome counts, partial warning, hidden
  threshold count, and escaped malicious-looking invented titles/tags passed.
  No server or uploaded live content was used. The installed Chromium binary
  first timed out; the installed Google Chrome retry succeeded.

The full existing suite was run with exactly the three CI deselects:

```text
python -m pytest -q
--deselect tests/test_contextual_intelligence.py::test_api_endpoints_contextual_intelligence
--deselect tests/test_v2_pipeline_runner.py::test_v2_pipeline_dry_run_records_all_stages_without_writes
--deselect tests/test_run_case_intelligence_request.py::test_build_client_uses_ollama_openai_compatible_endpoint
```

The first collection attempt lacked already-declared PyArrow; installing its
declared pin allowed collection. The subsequent run had **1288 passed, 4 failed,
2 skipped, 3 deselected, 1 xfailed**. The new modules caused one maintained
architecture-inventory failure, repaired by adding their three inventory rows
and confirmed by the focused documentation test. Three unrelated failures remain:

- `tests/test_api.py::test_local_chunk_search_uses_requested_model`: the existing
  test patches `routes._local_embedding_provider`, but execution uses the
  separate `search_service._local_embedding_provider`, attempting an unavailable
  sentence-transformers model instead. No model download or unrelated search
  repair was attempted.
- `tests/test_openai_chunk_embeddings.py::test_count_embedding_tokens_uses_model_tokenizer`
  and `::test_count_embedding_tokens_treats_special_token_text_as_literal`:
  the existing tokenizer cache is absent and its public download host cannot
  resolve. No paid operation occurred.

Final post-inventory acceptance run (same deselects, `--tb=short`):
**1289 passed, 3 failed, 2 skipped, 3 deselected, 1 xfailed** in 16.36 seconds.
These failures are outside the changed memo surface; the broad suite is
**not green**. The suite also warns that the existing
`test_statute_integration.py::test_statute_integration` returns `False` rather
than asserting; that nominal pass must not be treated as live-database evidence.
The canonical system reference and connected Swimm walkthrough were updated
in this checkpoint, as was the maintained architecture inventory.

Next bounded task: independently fix the search-service test injection point
and provision an offline tokenizer cache before demanding a green broad-suite
baseline. Separately, dotted nested statute extraction deserves its own exact-span
change rather than silently broadening this issue.
