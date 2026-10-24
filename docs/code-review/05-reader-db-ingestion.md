# Code review 05: reader, database, ingestion, and tour

Reviewed against `main` at `d2bcb41` (2026-10-24). Scope is FC, SCC, and FCA only. All listed files were read; `backend/analytics_service.py` was skipped as directed. The related CanLaw and FC ingestion walkthroughs and the relevant ORM migrations were consulted.

The main risks are unsafe HTML rendering in the legacy reader, unbounded or insufficiently restricted source fetches, and a few reader/ingestion paths that can lose evidence or fail to report their state accurately.

## Bugs

- `backend/batch_jobs.py:97-99,139-147` — **medium**. `compute_case_units` catches every exception and returns without rolling back the caller's session. If a database operation fails, SQLAlchemy can leave that transaction unusable; the outer loop then continues with the same session and subsequent cases can fail as well. Roll back after a failed computation (and make the failure visible to the batch result).
- `backend/batch_jobs.py:170-179` — **medium**. The case-specific `clear_cache` path reads `.rowcount` from a `SELECT` result before issuing its delete. A SELECT result does not provide a portable affected-row count and may raise or return an unusable value, preventing the delete or misreporting its count. Count explicitly or use the delete statement's result.

## Security risks

- `backend/case_reader_ui.py:14-21,197-214,245-256,285-298,323-359,535-559` — **medium, possible**. Case fields and statute API values are interpolated into HTML and inline JavaScript, and some API-derived values are assigned through `innerHTML`. If an untrusted or compromised record contains markup/script, opening this reader can execute it in a visitor's browser. Escape server-rendered text, render API values with DOM `textContent`, and remove inline event handlers.
- `fc_ingest/index_scraper.py:87-104`, `fc_ingest/item_scraper.py:66-78,86-111`, `fc_ingest/document_scraper.py:857-869`, `fc_ingest/ingest_pipeline.py:261-305` — **medium, possible**. Index links are accepted whenever they have a scheme and host; document and PDF links are resolved and fetched without an official-host check. A compromised or unexpected source response could therefore make the collector request an unrelated or private-network URL. Require HTTPS and an exact source-host allowlist for every fetched URL and redirect.
- `fc_ingest/index_scraper.py:58-66`, `fc_ingest/item_scraper.py:66-78`, `fc_ingest/document_scraper.py:872-890`, `fc_ingest/pdf_downloader.py:11-25` — **medium**. Requests have timeouts, but response bodies are read fully into memory with `.text` or `.content`; no response-size limit is enforced. The PDF downloader also stores the response without checking its signature. Stream with a byte cap and validate the PDF before staging it.

## Data-correctness risks

- `backend/reader_service.py:1122-1125,1329-1336` — **medium, possible**. Chunk offsets are rebased with `case_text.find(chunk.text)`, which always selects the first matching occurrence. If identical chunk text occurs more than once in a decision, a later citation or statute reference can be highlighted at the wrong location. Reuse the ordered chunk locations already computed by `locate_chunk_layers`.
- `backend/reader_service.py:594-615` — **medium**. The paragraph continuation set omits the formatter's `quote` block type. `paragraph_text_from_decision` therefore stops at a quoted block that belongs to a numbered paragraph and returns incomplete pinpoint text. Include quote continuations and cover them with a regression test.
- `backend/ingestion.py:140-175` — **medium**. Conflicting canonical fields from an equal- or lower-priority source are silently left unchanged; only metadata conflicts are added to `_source_conflicts`. The source row retains identity/metadata and a text hash, but not the losing field values or text, so those conflicts cannot be reviewed. Record canonical-field conflicts with their source provenance or preserve a reviewable source snapshot.
- `canlaw/embeddings.py:37-51` — **low**. `COALESCE(unofficial_text_en, unofficial_text_fr)` treats an empty English string as present, so it skips available French text and can embed an empty value. Use `NULLIF(..., '')` for the English value and exclude blank text.
- `canlaw/db.py:137-177` — **low, possible**. On a repeat load, a matching `source_key` returns immediately; a natural-identity match only refreshes the key and cited/citing lists. Changed text or metadata in a refreshed source snapshot is not applied. Clarify whether staging is intentionally immutable; otherwise compare a content hash and update the row under an explicit refresh policy.
- `fc_ingest/index_scraper.py:79-84`, `fc_ingest/ingest_pipeline.py:151-173,412-430` — **medium, possible**. An unrecognized result-count page is treated as zero, and the discovery loop can then finish without identifying a failed window. A changed response or an unrecognized challenge page could silently omit decisions. Distinguish a confirmed zero-result page from a parse failure and stop or report the latter.
- `fc_ingest/ingest_pipeline.py:151-173` — **low, possible**. Date windows stop splitting at monthly granularity without checking whether a month still exceeds the source's 500-result cap. If that assumption ceases to hold, results past the cap may be omitted. Verify the monthly count or split oversized windows further.

## Performance

- `backend/reader_service.py:1221-1257` — **medium**. Matching each fetched paragraph chunk against every pinpoint makes this work proportional to chunks × pinpoints. The existing `_match_pinpoint_chunks` helper groups by case and is tested for bounded performance, but this path does not use it. Reuse the helper or otherwise index pinpoints by case and range.
- `backend/tour_cache.py:26-27,135-148` — **low**. `_MAX_BODY` limits what is stored, but the middleware buffers every response chunk before calling `put`; oversized responses can still consume unbounded memory. Stop buffering once the cap is exceeded while continuing to stream the response.

## Dead code / cleanup

- `backend/models.py:865-888` — **low**. `ResearchRequest` declares `max_chunks_per_case` and `page_size` twice. The later declarations replace the earlier defaults; keep one declaration of each to make the effective contract clear.
- `fc_ingest/index_scraper.py:23` — **low**. `MAX_SAFE_RESULTS` is declared but the date-window splitter uses a separate literal `500`. Use the named constant in the check or remove it.

## Suggestions

- Keep paragraph/source offsets owned by the backend; test repeated identical chunks and quoted paragraph continuations explicitly.
- Make batch failures and source-window parse failures fail visibly, and preserve enough provenance to review discarded canonical-field conflicts.
- The sampled ORM/migration comparisons did not establish a schema mismatch. This was a static source review only; no database or migration was run.
- No tests were run. The formatter-only check confirmed the quote-block classification; importing the full reader for a runtime check was unavailable because FastAPI is not installed. `scripts/check_generated_docs.py` was attempted but could not run its generators because FastAPI and SQLAlchemy are not installed in this environment.
