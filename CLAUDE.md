# Project guide for Claude

iLit (Litigation Intelligence) is a FastAPI app over a Postgres/pgvector database of Canadian immigration case law. Live at https://www.ilit.ca.

The owner (Daniel) does not code. Explain things in plain words, do merges and deploys yourself, but only merge when he says to. Keep replies short and avoid wasting tokens: no repeated full-repo reviews, and use a lighter model for simple tasks.

## Where things run
- The live site runs on Daniel's Windows workstation, not in the cloud. Cloud sessions cannot reach the database or the live site's machine; anything that touches the database or deploys goes through a Remote Control session on his computer.
- `scripts\refresh_site.ps1` stops the old app and tunnel, then starts uvicorn (`backend.main:app`, port 8001) and the Cloudflare tunnel. It does not `git pull`.
- Cloudflare "Workers Builds" is unused. Ignore its failure emails.
- Password gate (`CASELIBRARY_ACCESS_PASSWORD`) is deliberately off for now (Daniel's decision, 2026-10-02). Do not enable it unasked.

## Run and test
- Windows: `./venv/Scripts/python.exe -m pytest -q`. Linux/CI: `pip install -r requirements.txt` then `python -m pytest -q`.
- Three tests are known to fail without local services and are deselected in CI (`.github/workflows/tests.yml`): two need Postgres on localhost:5432 and one expects an Ollama client config. Run them on Daniel's machine when relevant.
- `scripts/check_generated_docs.py` must pass (the Documentation Sync workflow runs it). If you change generated docs sources, regenerate them.

## Deploy
Use the `deploy` skill (`.claude/skills/deploy/SKILL.md`). Never restart the site while another session is mid-task on his machine without checking.

## Conventions
- Branch from `main`, one small PR per change, PR body starts with the attribution block the session gives you.
- Never commit `.env`, `.cloudflared/` credentials or database dumps.
