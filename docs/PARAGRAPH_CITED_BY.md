# Paragraph "cited by" batch job

Markup mode's margin and Peek panel can show, for each paragraph of a decision, which other
decisions cite that paragraph, how often, and the signal phrase the citing judge wrote beside it
("applied in", "see also", "distinguished", a quotation, ...). This job builds that data once, from
what is already stored. It uses no AI and no network, and it never reads anything a user typed.

The signal phrase is a reading aid: it shows how the citing case introduced the paragraph. It is not a
verdict on whether the paragraph is still good law.

## What it does

For every citing decision that has citations resolved to library cases, it reads that decision's text once,
looks at the words just before each pinpoint citation, and stores one row per
(citing case, cited case, cited paragraph) in `paragraph_citation_edges`. A second table,
`paragraph_citation_status`, marks each citing case as done. Both are additive (migration `0036`); no
existing table changes.

The reader shows "Cited by N cases" for a paragraph's own case as soon as some citing cases are done,
labelled partial until all are. In Peek, the cited paragraph's summary appears only when every citing case
of that authority has been processed, so a partly finished run never shows a wrong count.

## Run it on Daniel's PC

**Do not run it until the PC thread confirms the live site is healthy.** The first run once made the site
unresponsive. The job now has safety rails that are on by default (see below), but run it only when the
site is up, and watch the first few minutes.

1. Deploy first (the migration must be applied: `alembic upgrade head`). The site works before and
   after; without the tables it simply shows the old counts.
2. Preview, which writes nothing:
   `.\venv\Scripts\python.exe scripts\build_paragraph_cited_by.py`
3. Run for real, in a window of 30 minutes at a time, watching the site:
   `.\venv\Scripts\python.exe scripts\build_paragraph_cited_by.py --apply --max-minutes 30 --health-url http://127.0.0.1:8001/health/ready`
4. Run the same command again to carry on. It skips finished citing cases, so stopping (Ctrl+C, the stop file or
   the time limit) loses nothing.
5. Check one case: `.\venv\Scripts\python.exe scripts\build_paragraph_cited_by.py --report-cited <case id>`

**Stop it at any moment:** create an empty file named `stop_cited_by.txt` in the folder it was started from
(or press Ctrl+C). It finishes the small batch it is on and exits.

### Safety rails (all on by default)

- Lowest process priority at start (Windows background mode, else idle, else below-normal; `nice 19` elsewhere).
- At most one database connection, ever.
- Server-side limits set for the whole connection: 15 s per statement, 2 s waiting for a lock, 30 s idle in a
  transaction. A slow or locked query is skipped (the case stays pending) and the job rests longer.
- One short transaction per batch of 5 citing cases, committed at once, nothing held between batches.
- It rests after every batch for at least 4 times as long as the batch took (works at most 20% of the time),
  and never less than 2 s.
- With `--health-url` it times the site before each batch; if the answer takes over 1.5 s, or fails, it waits
  (10 s, doubling up to 2 min) and asks again, and stops after 12 waits in a row.
- It does not scan the whole citations table at start; `--count` asks for the full total (slow).
- It stops after 5 database errors in a row.

Useful flags: `--batch-size`, `--sleep-between-batches` (raise to be gentler), `--sleep-between-cases`,
`--max-duty`, `--max-minutes`, `--max-cpu-seconds`, `--limit N`, `--case-ids 12 34`, `--statement-timeout-ms`,
`--lock-timeout-ms`, `--health-slow-seconds`, `--health-max-waits`, `--stop-file`, `--max-db-errors`.
A citing case that errors is skipped and reported; it stays pending and is retried on the next run.

## Changing the rules later

Raise `ALGO_VERSION` in `backend/paragraph_cited_by.py`. Every citing case then counts as pending again and
the next `--apply` run rewrites it. Rows from the old version are replaced per citing case, so the data is
never half old and half new for one citing case.

## Tested

On 300 real decisions loaded into a scratch database: 197 citing cases, 569 paragraph edges; a plain run,
a `--limit 40` run and a resume run gave the same 569 edges with no duplicates, and a re-run did nothing.
Signal-phrase precision was checked by hand on 200 real decisions; the rule set is deliberately cautious, so
most citations stay "mentioned" when the text gives no clear signal.
