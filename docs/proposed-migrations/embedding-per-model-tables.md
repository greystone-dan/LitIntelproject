# Proposed design: per-model embedding tables

**Status: design and compile-only scaffold. No database was inspected or
changed.** There is currently no `backend/embedding_registry.py`; the proposed
helper accepts a mapping representing a future registry entry. No application
runtime calls it, and the existing embedding tables and migrations are
unchanged.

## Goal and boundary

Give each registered embedding model a stable vector table whose pgvector
dimension and ANN index are explicit schema contracts. Preserve the association
to the source `case_chunks` row so an embedding remains traceable to its
canonical text, offsets, and chunk identity. Keep embeddings as a derived layer;
do not treat vector data as citation, statute, metadata, tag, or source
provenance.

This proposal covers table/index definition scaffolding only. It does not choose
a provider, backfill vectors, route retrieval, alter existing tables, create an
Alembic revision, or recommend running DDL.

## Options considered

| Approach | Accuracy and traceability | Runtime / operational cost | Maintenance and scale | Assessment |
| --- | --- | --- | --- | --- |
| One shared vector table with a model discriminator | A single fixed-dimension `Vector(n)` column cannot safely hold models with different dimensions; separating dimensions still needs validation and model filters on every query. | Few tables, but mixed-model indexes and filters can increase query cost and operational ambiguity. | Simple while there is one model/dimension; complexity grows with dimension families and index tuning. | Keep only for compatible models where dimensions and retrieval contract are deliberately shared. |
| One vector table per model registry entry | Fixed table and vector dimensions make model-to-vector compatibility explicit; chunk FK preserves source traceability. | Adds one relation/index per registered model; each requires a bounded migration and index build. | Clear ownership and independent index tuning; registry/table lifecycle needs governance to avoid unbounded table growth. | Recommended for this issue's proposed per-model design, gated on registry and query integration review. |
| One table per dimension family | Fixed dimensions are explicit, while same-dimension model versions share storage. Model identity still needs a discriminator and query filter. | Fewer tables/indexes than per-model; shared indexes may be less selective. | Lower catalog growth but weaker model isolation and more filtering rules. | Viable if model count grows materially and benchmarks show per-model tables are operationally expensive. |

The per-model design best matches the requirement to make model identity and
dimension explicit without requiring runtime query code to reason across
incompatible vector widths. Its main tradeoff is schema/index growth, so the
registry must be bounded and table retirement governed rather than inferred
from provider availability.

## Proposed contract

`backend/vector_tables.py` accepts a mapping with:

- `model_name`: non-empty descriptive model identity;
- `model_version`: non-empty version identity recorded with each vector row;
- `table_name`: an explicit name matching `chunk_embeddings_<slug>` (lowercase
  ASCII letters/digits separated by underscores), never derived directly from
  an untrusted provider/model string; arbitrary names and legacy
  `case_chunk_embeddings_*` names are rejected;
- `dimensions`: positive integer, materialized as `Vector(dimensions)`;
- optional table/schema, local `chunk_id`, and source chunk-key names; and
- optional ANN method, distance operator class, and method-specific parameters.

It returns SQLAlchemy table/index metadata. `compile_vector_table_ddl` compiles
the `CREATE TABLE` and `CREATE INDEX` statements for PostgreSQL without making
a connection. Names are restricted to simple identifiers; unsupported methods,
metrics, or parameters are rejected. The helper is not a migration generator
and is not wired into startup, ingestion, embedding, or retrieval.

A production registry should pin the model identifier/version, dimensions,
provider contract, and table/index names as reviewed metadata. A table row
retains `chunk_id` as its primary/foreign key, stores the model-specific vector,
and has non-null `model_name` and `model_version` columns for per-row
attribution. SQLAlchemy inserts made through this helper default those identity
columns from the registry entry; the out-of-chain template shows the explicit
columns but requires any future writer to supply their values. The table comment
is descriptive only and is not the model-identity record. `case_chunks` remains
authoritative for source text, hash, and offsets; the vector table must not copy
or redefine that evidence.

## Future search and bulk-load flow

There is no `backend/embedding_registry.py` on the current main branch, so
existing search behavior is unchanged. Once a registry exists, search should
resolve the requested model name/version to its reviewed registry entry, select
that entry's table and dimensions, and validate the query vector width before
searching only that model's table. Unknown models or width mismatches should fail
closed rather than fall back to an incompatible vector table.

A separately authorized one-time bulk job could run on rented compute: read
approved chunk IDs and text in bounded batches, embed with the registry-pinned
model/version, then bulk-load each `(chunk_id, embedding, model_name,
model_version)` row into its provisioned model table. Validate vector widths,
row counts, and chunk identities before making that table searchable; build or
refresh its ANN index after loading. The compute and transfer plan must meet
source licence, privacy, and retention requirements. This scaffold provides
neither that job nor its table, transfer, or index operations.

## Migration template and validation gate

[`embedding-per-model-tables.py.txt`](embedding-per-model-tables.py.txt) is an
illustrative migration template stored outside `alembic/versions/`. It contains
placeholder revision ancestry and must not be copied or run as-is. A future
proposal must freeze the accepted model, exact dimensions, index method,
parameters, source table, and rollback before creating a real migration linked
to the then-current single Alembic head.

The smallest falsifiable experiment for this scaffold is
`python -m pytest -q tests/test_vector_tables.py`: compiled table DDL must
include the registry dimensions and chunk relationship, and compiled index DDL
must include the chosen pgvector method and operator class. This check must not
create an engine or connect to a database. It does not establish index
performance or migration safety.

Before adoption, separately review at least:

1. a representative retrieval-accuracy and latency benchmark for each model;
2. index-build duration, disk use, write/read impact, and recovery on a
   disposable representative database copy; and
3. the model-retirement, re-embedding, and migration rollback policy.

No such benchmark or database check is part of this proposal.
