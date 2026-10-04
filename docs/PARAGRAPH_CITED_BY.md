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

Run it when the PC is plugged in and nobody needs the site (evening or overnight). The site can stay up;
the job runs at lower priority, in small batches, with a pause between them.

1. Deploy first (the migration must be applied: `alembic upgrade head`). The site works before and
   after; without the tables it simply shows the old counts.
2. Preview, which writes nothing:
   `.\venv\Scripts\python.exe scripts\build_paragraph_cited_by.py`
3. Run for real, in a window of an hour at a time:
   `.\venv\Scripts\python.exe scripts\build_paragraph_cited_by.py --apply --max-minutes 60`
4. Run the same command again to carry on. It skips finished citing cases, so stopping (Ctrl+C or the time
   limit) loses nothing.
5. Check one case: `.\venv\Scripts\python.exe scripts\build_paragraph_cited_by.py --report-cited <case id>`

Useful flags: `--batch-size 25`, `--sleep 0.5` (seconds between batches; raise it to be gentler),
`--limit N` (stop after N citing cases), `--case-ids 12 34` (just these), `--statement-timeout-ms 60000`.
A citing case that errors is skipped and reported; it stays pending and is retried on the next run.

On Windows, to lower the priority further, start it with `start /low` from a normal Command Prompt.

## Changing the rules later

Raise `ALGO_VERSION` in `backend/paragraph_cited_by.py`. Every citing case then counts as pending again and
the next `--apply` run rewrites it. Rows from the old version are replaced per citing case, so the data is
never half old and half new for one citing case.

## Tested

On 300 real decisions loaded into a scratch database: 197 citing cases, 569 paragraph edges; a plain run,
a `--limit 40` run and a resume run gave the same 569 edges with no duplicates, and a re-run did nothing.
Signal-phrase precision was checked by hand on 200 real decisions; the rule set is deliberately cautious, so
most citations stay "mentioned" when the text gives no clear signal.
