---
name: deploy
description: Deploy the latest main to the live site www.ilit.ca on Daniel's Windows workstation (pull, refresh, verify). Use when asked to deploy, go live, or refresh the site.
---

# Deploy iLit to www.ilit.ca

Runs only on Daniel's computer (the project's default device) through a Remote Control session in the LitIntelproject folder. A cloud session cannot do this; start the device session first.

1. Check nothing is half-done: `git status`. If there are uncommitted changes you did not make, stop and tell Daniel.
2. `git checkout main` then `git pull origin main`. Note the new commit with `git log --oneline -1`.
3. If `requirements.txt` changed in the pull, run `./venv/Scripts/python.exe -m pip install -r requirements.txt`.
4. Restart the site.
   - If the background service is installed (scheduled task `iLitSite`, see `scripts/service/`): `Stop-ScheduledTask iLitSite; Start-ScheduledTask iLitSite`.
   - Otherwise run `scripts\refresh_site.ps1` in a terminal that stays open (it blocks while the site runs; start it detached so the session is not stuck).
5. Verify, waiting up to about 30 seconds for startup:
   - `Invoke-RestMethod http://127.0.0.1:8001/health` returns ok.
   - `Invoke-WebRequest https://www.ilit.ca/health` returns 200 (proves the tunnel).
   - Open one page the change touched, e.g. https://www.ilit.ca/data-explorer, and confirm it loads.
6. Tell Daniel in one or two plain sentences: which commit is live and that the checks passed, or exactly what failed. If the new version fails to start, `git checkout` the previous commit, restart, and report.

Database changes (alembic migrations) are not part of a routine deploy. Ask Daniel before running any.
