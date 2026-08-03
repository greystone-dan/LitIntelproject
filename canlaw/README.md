# Hugging Face case-law staging

The `canlaw` package downloads court datasets from `a2aj/canadian-case-law` into a local SQLite staging archive. It does not replace the project's primary PostgreSQL database.

## Verified snapshot

The 2026-08-01 staging run completed with SQLite integrity status `ok`:

| Court | Decisions |
|---|---:|
| FC | 35,814 |
| RPD | 6,729 |
| FCA | 7,785 |
| SCC | 10,889 |
| Total | 61,217 |

The resulting ignored local artifact is `canlaw.db` (approximately 6.24 GiB).

## Storage model

Each `cases` row stores normalized columns for court, bilingual citations, names, dates, URLs, decision text, citation counts, and merged cited/citing lists. It also stores:

- `raw_payload`: the complete source row, including both language text fields.
- `metadata_json`: all source fields except the two full-text fields.
- `source_key`: a stable hash used to make future ingestion runs idempotent.

The `case_embeddings` table stores one vector per case and model. Its unique `(case_id, model)` index prevents duplicate vectors.

## Commands

Download or refresh all configured courts:

```powershell
python -m canlaw.cli ingest_courts --courts FC RPD FCA SCC
```

After all live data pulls finish, backfill source keys and normalized bilingual citation lists for rows created by the initial loader version:

```powershell
python -m canlaw.cli repair_staging --batch-size 100
```

Create local staging vectors in bounded batches:

```powershell
python -m canlaw.cli embed_courts --courts FC RPD FCA SCC --batch-size 16
```

Dry-run the bridge into the primary PostgreSQL corpus:

```powershell
python -m scripts.import_canlaw_staging --dry-run --limit 25
```

After a stopped run, resume after the last reported staging ID:

```powershell
python -m scripts.import_canlaw_staging --start-after-id 12345
```

Do not run the PostgreSQL bridge concurrently with another bulk database pull. The bridge deduplicates by citation and full-text hash and routes records through the established ingestion API so provenance rows and ingestion runs are created consistently.

## Embedding limitation

The local staging vector is a single model-limited representation of each full decision. Production retrieval should continue to use the primary database's chunking and pgvector workflow, which preserves passage-level recall for long legal decisions.
