# Statute library count and lookup check

Date: 2026-10-03
Scope: Issue #79; Phase 1 Justice Laws XML statute reference library. This is a
repository and fixture audit, not a live database inventory.

## Phase 1 scope and fixture output

`scripts/import_statutes.py` configures seven Phase 1 entries. Six are enabled
for XML import; `Charter` is marked `skip` because that source has no Justice
Laws XML. The shared small fixture
[`tests/fixtures/statute_library/phase1_sample.xml`](../../tests/fixtures/statute_library/phase1_sample.xml)
contains exactly three namespaced `Section` elements: `34`, `35`, and `36`.
The focused tests run the actual parser/importer against isolated SQLite for
each of the six XML-enabled registry entries and compare the stored section
numbers with those three fixture expectations.

| Phase 1 key | XML importer behavior | Expected sections in the synthetic fixture | Production imported totals |
| --- | --- | ---: | --- |
| `IRPA` | imported | 3 | needs DB |
| `IRPR` | imported | 3 | needs DB |
| `CA` | imported | 3 | needs DB |
| `CustA` | imported | 3 | needs DB |
| `FCA` | imported | 3 | needs DB |
| `FCR` | imported | 3 | needs DB |
| `Charter` | skipped (`skip: True`) | 3 parser output only; not bulk-imported | needs DB |

The fixture is intentionally reused, not a sample of each law's source XML.
Thus “7 configured,” “6 XML-enabled,” and “3 fixture sections per parser run”
are code/test facts; none supplies the real count of imported statutes,
versions, or sections. No live database was accessed. Current per-law
statute/version/section totals and persisted effective-date ranges are
**needs DB**.

The importer parser returns a count from recognized XML `Section` elements.
`import_statute_from_xml` stores up to the first 100 returned sections per
version. Its bulk version summary is computed from successful import-function
calls, but it does not prove newly inserted version rows: an already-existing
version also returns its statute record. There is no configured expected
production section count per law.

## Count surfaces: computed or fixed

| Surface | Behavior | Interpretation |
| --- | --- | --- |
| `scripts/import_statutes.py` Phase 1 registry | Seven explicit dictionary entries; Charter has a fixed `skip` flag | Configured scope is hard-coded, not loaded coverage |
| Bulk importer summary | Instrument/version-call totals are accumulated while running; parsed section count is derived from the parser result and capped at 100 for storage | Computed run output, not a live-library inventory or proof of new inserts |
| `backend/pages/statute_viewer.py` | Seven statute choices are hard-coded; displayed section data is fetched from the API | Choices are not proof that those instruments are loaded; response list length is data-derived |
| `/api/statutes/{statute_code}` and `/versions/{version_id}/sections` | Details have no statute/version/section total; the sections route returns section rows | No API count contract exists |
| `docs/API_REFERENCE.generated.md` | Documents the detail and section routes without a count field | No hard-coded library total |
| `docs/SCRIPT_CATALOG.generated.md` | Previously repeated a fixed “IRPA had 12+ versions between 2017-2026” example from the importer module docstring | Unsupported fixed count removed at the source and generated catalog refreshed; it was not an observed live count |
| Existing reports | No repository report was found with production per-law statute-library section totals | Current totals are **needs DB** |
| `SYSTEM_REFERENCE.md` | Contains dated historical counts for `statute_references`, `legislation_documents`, and `legislation_sections` | Static historical observations from a separate authority-indexing surface; not this new `statutes` / `statute_versions` / `statute_sections` library |

For versions populated through this importer, at most 100 sections are stored
per version. A returned-list length therefore is not necessarily a full-law
section total.

## Parser and point-in-time behavior

The XML parser now queries the LIMS-namespaced `Section` elements. The fixture
exposed that an unprefixed ElementTree path matched none of the namespaced
sections; the importer had then fallen back to text parsing and stored only a
partial fixture result. The fixture asserts all three section identifiers are
parsed and imported.

Effective start date now prefers `inforce_start_date` over snapshot `pit_date`.
The importer also reads an XML `inforce-end-date` and carries PIT-index start/end
dates into imported historical versions. Point-in-time lookup treats start/end
as inclusive, selects the covering version with the latest start when ranges
overlap, and returns no version for a gap. An explicit API `as_of` request now
returns 404 on a gap instead of silently selecting the latest version; requests
without `as_of` still select the latest version.

The XML fixture's section 34 includes subsection 1, paragraph f. The test runs
the parsed section text through the provision-tree splitter and requires the
exact path `("34", "1", "f")`. This is fixture evidence, not verification of
current IRPA XML or stored rows.

## Validation and limits

Focused command:

```text
python -m pytest tests/test_statute_library.py -q
```

Result: **9 passed**. It uses an isolated SQLite database, not the configured
PostgreSQL database. No source downloads, database reads/writes, bulk imports,
migrations, or external Justice Laws checks were performed. Live library
counts and actual imported date boundaries remain **needs DB**.
