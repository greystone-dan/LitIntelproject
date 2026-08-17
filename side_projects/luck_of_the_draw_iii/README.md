# Luck of the Draw III

Standalone importer and Excel exporter for the public Hugging Face dataset
`refugee-law-lab/luck-of-the-draw-iii`.

Run from the repository root:

```powershell
.\venv\Scripts\python.exe side_projects\luck_of_the_draw_iii\build_lotd_excel.py
```

It stores only its data in the PostgreSQL schema `lotd` (`lotd.cases` and
`lotd.dockets`) and writes the workbook to `side_projects/luck_of_the_draw_iii/output/`.
Neither table is used by the case-library application or its APIs.

Use `--skip-download` to rebuild from cached parquet files, or `--skip-excel`
to import data without writing the workbook.

## Access Recommendation

Access is a better front-end than Excel for this dataset, but only if Access
links to PostgreSQL instead of importing all `2.6M+` docket rows into a local
`.accdb` file.

After running the importer, the isolated `lotd` schema provides three
Access-friendly views:

- `lotd.access_cases`: one row per IMM file
- `lotd.access_docket_summary`: one row per IMM file with docket counts and date ranges
- `lotd.access_dockets`: full docket entries when you need drill-down

Recommended Access workflow:

1. Use an ODBC PostgreSQL connection.
2. Link `lotd.access_cases` and `lotd.access_docket_summary` first.
3. Link `lotd.access_dockets` only for detailed lookups or filtered forms.
4. Keep PostgreSQL as the source of truth; do not import the full dockets table into Access.

If you only want the SQL objects refreshed on an existing import, run:

```powershell
.\venv\Scripts\python.exe side_projects\luck_of_the_draw_iii\build_lotd_excel.py --skip-download --skip-excel
```

## Access Front-End Builder

If you want a real `.accdb` file rather than a huge Excel workbook, build the
Access front-end from the Access-sized LotD views:

```powershell
.\venv\Scripts\python.exe side_projects\luck_of_the_draw_iii\export_lotd_access_sources.py
powershell -ExecutionPolicy Bypass -File side_projects\luck_of_the_draw_iii\build_lotd_access_frontend.ps1
```

This creates `side_projects/luck_of_the_draw_iii/output/luck_of_the_draw_iii_frontend.accdb`
with:

- `Cases` table
- `DocketSummary` table
- Saved queries sorted by `IMM_NUMBER`
- Lookup queries for partial IMM number search
- Docket-count ranking queries

This Access file is designed for working analysis. The full `2.6M` docket rows
remain in PostgreSQL.