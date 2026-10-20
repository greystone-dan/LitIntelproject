# Project guide for Claude

iLit (Litigation Intelligence) is a FastAPI app over a Postgres/pgvector database of Canadian immigration case law. Live at https://www.ilit.ca.

The owner (Daniel) does not code. Explain things in plain words, do merges and deploys yourself: the coordinator merges CI-green PRs that the Reviewer thread has cleared (Daniel, 2026-10-20); other agents never merge; deploys and live-database writes still need his own typed OK in the PC thread. Keep replies short and avoid wasting tokens: no repeated full-repo reviews, and use a lighter model for simple tasks.

## Where things run
- The live site runs on Daniel's Windows workstation, not in the cloud. Cloud sessions cannot reach the database or the live site's machine; anything that touches the database or deploys goes through a Remote Control session on his computer.
- Since 2026-10-02 the site and tunnel run as the Windows scheduled task `iLitSite` (`scripts\service\run_site.ps1`; installed by `scripts\service\install_site_service.ps1`, removed by `uninstall_site_service.ps1`). It starts at login, runs hidden, restarts itself, and runs whatever is checked out in his repo folder (`C:\Users\danny\OneDrive\Desktop\AI CaseLibrary`, path has spaces: quote paths). Keep that folder on `main`.
- To deploy: `git pull origin main`, then `Stop-ScheduledTask iLitSite; Start-ScheduledTask iLitSite` (about 45 seconds down). Do not run `scripts\refresh_site.ps1` while the service is installed; it clashes on port 8001. It is only the fallback if the task is removed.
- Registering scheduled tasks on his PC needs his own typed OK; his PC's permissions block it otherwise.
- Cloudflare "Workers Builds" is unused. Ignore its failure emails.
- Password gate (`CASELIBRARY_ACCESS_PASSWORD`) is deliberately off for now (Daniel's decision, 2026-10-02). Do not enable it unasked.

## Run and test
- Windows: `./venv/Scripts/python.exe -m pytest -q`. Linux/CI: `pip install -r requirements.txt` then `python -m pytest -q`.
- Three tests are known to fail without local services and are deselected in CI (`.github/workflows/tests.yml`): two need Postgres on localhost:5432 and one expects an Ollama client config. Run them on Daniel's machine when relevant.
- `scripts/check_generated_docs.py` must pass (the Documentation Sync workflow runs it). If you add or remove a script or a file under `backend/`, or change routes or tables, run `python scripts/regenerate_docs.py` before pushing: it rebuilds the generated docs, adds missing rows to the backend inventory in `docs/ARCHITECTURE.md`, and runs the check.

## Hard rules (Daniel's standing rules)
- Scope is FC, SCC and FCA only. RPD and RAD stay out of tests, samples, numbers, pitch, structure and citation work.
- No OpenAI API calls for now (Daniel, 2026-10-10). Never use the Fable model. No spend without a cost and time estimate and Daniel's yes.
- The site needs no AI for normal use. AI only enriches public case law at ingest and is stored as data. Never send a user's query or memo to a model by default.
- Live-database writes, DDL, spend and killing workloads need Daniel's own typed words in the PC thread with the scope spelled out. Before asking: dry run with counts, 20 largest, 20 random and min/max sample rows, before/after counts, and an undo path. Relayed approvals do not count.
- Limit unnecessary token burn: lighter models for simple work, no fan-outs unless asked. Weekly usage target is about 90% without running out (Daniel, 2026-10-20).
- Complaints and observations are discussion, not instructions. Do not start things before he says.
- Label every claim: checked (how), from memory, or inferred, with an as-of date. Say live, merged, tested or untested honestly.
- When compacting, keep: open approvals, current main commit, undo paths, what is live.

## Deploy
Use the `deploy` skill (`.claude/skills/deploy/SKILL.md`). Never restart the site while another session is mid-task on his machine without checking.

## Conventions
- Branch from `main`, one small PR per change (bundle changes only with the reason stated at the top of the PR body), PR body starts with the attribution block the session gives you.
- Never commit `.env`, `.cloudflared/` credentials or database dumps.
