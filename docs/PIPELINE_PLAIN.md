# How a case becomes searchable

This is a plain-language map of the usual path from a public decision to a
search result. The active working court scope is FC, SCC, and FCA. A whole-site
decision total can also include RPD and RAD tribunal decisions, so it is not a
count of just those three courts.

## The steps

1. **Find and collect decisions.** Source-specific collectors discover a
   decision and capture its text or document. For Federal Court collection,
   `fc_ingest/` handles discovery, retrieval, and staging; A2AJ dataset imports
   use `scripts/ingest_a2aj_parquet.py` or `scripts/ingest_a2aj_api.py`. These
   are examples, not a claim that one collector covers every court or source.
   Collection and a successful capture are separate: an identifier alone does
   not prove that decision text was obtained.

2. **Keep the source record and bring it into the case library.** A collector
   first keeps source identity and capture details with its staged record.
   `scripts/import_fc_decisions.py` is one bridge for validated Federal Court
   captures; `backend/ingestion.py` applies the shared canonical create/merge
   rules and preserves source provenance. Staged records are not automatically
   canonical decisions.

3. **Prepare the text for reading and processing.** `scripts/chunk_cases.py`
   can split a decision into a full-text segment, heading/section segments, and
   paragraph segments. `backend/case_processing.py` coordinates the current
   full-case and heading/paragraph chunk stages. The original stored text
   remains the source for evidence and offsets.

4. **Find case citations and legislation references.**
   `backend/citations.py`, called by the citation and statute stages in
   `backend/case_processing.py`, looks for case-law citations and separately
   looks for Acts, regulations, and other instruments. Finding a citation is
   not the same as deciding which local case it points to: case-target
   resolution is a later local step, with batch support in
   `scripts/resolve_citation_targets.py`. An unresolved citation can remain
   stored as unresolved.

5. **Label decision outcomes.** The `outcome` stage in
   `backend/case_processing.py` calls `backend/metadata_outcomes.py` and stores
   a versioned result with evidence. This outcome classifier uses deterministic
   rules; a label is a research signal, not a substitute for checking the
   decision.

6. **Add legal-topic tags.** The V3 tag stage in
   `backend/case_processing.py` uses `scripts/tag_cases_v3.py` and
   `backend/legal_tagger_v3.py` to store taxonomy tags separately from
   citations, statutes, and outcome labels. The batch entry point is also
   available through `scripts/backfill_case_tags_v3.py`.

7. **Make the stored material searchable.** Ordinary Case Search is served by
   `backend/search_service.py`, which searches stored case text and metadata
   using PostgreSQL queries. `alembic/versions/0038_search_indexes.py` supplies
   database search indexes. Optional chunk-vector work uses
   `scripts/embed_local_chunks.py`; vectors are a separate search signal, not
   source text or legal evidence. There is no claim here that every case has an
   embedding.

## AI and ordinary use

Normal site use—searching, opening decisions, and inspecting stored citations
and labels—does not need AI. AI helped label public case law ahead of time; that
work is stored as data for the site to read, rather than generated for each
ordinary search. The described outcome and V3 tag stages use deterministic
rules. Separate, explicitly enabled model features are described in the
[AI-use statement](government-readiness/ai-use-statement.md).

## Keep the layers distinct

- A captured source, a canonical case, and a processed case are different
  states.
- Case citations, statute references, outcome labels, tags, and embeddings are
  separate kinds of stored information.
- Citation extraction records what appears in the source; target resolution
  separately attempts to match that citation to a local decision.
- Search results and labels help research; they do not establish completeness
  or replace checking the underlying decision and authoritative source.

For schema-level table and column explanations, see the
[main database data dictionary](DATA_DICTIONARY.md). For detailed ownership and
implementation boundaries, see the
[canonical ingestion walkthrough](../.swm/3.sl0qpkcv.sw.md), the
[citation and tagging walkthrough](../.swm/4.9nn3id9f.sw.md), and the
[search walkthrough](../.swm/5.b49ftjal.sw.md).
