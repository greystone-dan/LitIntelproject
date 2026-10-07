# Daily intake

`scripts/daily_intake.py` is the once-a-day job that keeps the library current. It makes no AI or model calls.

## What one run does

1. **New decisions.** For each of FC, FCA and SCC it makes one HEAD request to the A2AJ dataset on Hugging Face and compares the file fingerprint with the last completed run. Unchanged means nothing more happens. If it changed, it downloads that court's Parquet file (checked against the published SHA-256), imports decisions dated after the newest stored decision minus 30 days, skips anything already present (matched by text hash, citation or source id) and never edits existing cases. Each new case then goes through the existing deterministic processing layers (chunks, metadata, outcome, citations, statutes, tags).
2. **FC activity records.** It finds the highest IMM number stored for the current year and walks forward, fetching each file from the Federal Court registry (two requests per file, at least 2 seconds apart) until 5 numbers in a row do not exist. It also re-fetches up to 20 recently active files not fetched for 7 days so new docket entries arrive. New entries are added (never duplicated) and the touched files are re-classified with the existing rule classifier.

## Safety and limits

- One run at a time (a Postgres advisory lock), and a run is skipped if one finished in the last 20 hours unless `--force`.
- Caps per run: `--max-cases 200`, `--max-new-files 150`, `--max-fc-requests 400`, `--max-minutes 120`. Hitting a cap is a normal stop; the next run continues.
- `--dry-run` writes nothing to the database. It probes upstream and walks the registry but does not download the large Parquet files unless `--download-in-dry-run` is given.
- Each real run writes one `ingestion_runs` row (`source_type = daily_intake`): status `started`, then `completed`, `completed_with_errors` or `failed` with `finished_at`, counts and a JSON summary per court and for FC activity.
- The registry requests identify themselves as `iLit-daily-intake`. If the registry ever rejects that, set `FC_ACTIVITY_USER_AGENT` in `.env`.
- Refuses to walk from IMM-1 if no IMM files are stored for this or last year (`--allow-sweep-from-one` overrides, for a brand-new library only).

## Scheduling on Windows

`scripts\service\install_daily_intake.ps1` registers the scheduled task `iLitDailyIntake` (daily at 03:30, hidden, below-normal priority, runs when the PC next wakes if it missed the time). `uninstall_daily_intake.ps1` removes it. `run_daily_intake.ps1` is what the task runs; it appends to `logs\intake\daily-YYYYMMDD.log` and also works by hand (`run_daily_intake.ps1 --dry-run`). It is separate from the `iLitSite` task and does not restart the site.

## Not covered

Case-type labels, fingerprints, judge aliasing and SCC panel links are separate pipelines and are not run by this job. The older `scripts/scheduled_intake_daemon.py` only discovers and is superseded by this job.
