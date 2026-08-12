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