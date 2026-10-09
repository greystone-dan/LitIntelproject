# Deployment Commands Reference

Once you have a Remote Control session running, use these commands to talk to Claude.

**Current site deployment:** The Windows scheduled task `iLitSite` is the primary
site and tunnel process. After `git pull origin main`, restart it with
`Stop-ScheduledTask iLitSite; Start-ScheduledTask iLitSite`. Keep the site
worktree on `main`. `scripts\refresh_site.ps1` is a fallback only if the task
has been removed; never run it while `iLitSite` is installed.

## Setup (One-time)

**Install Claude CLI:**
```powershell
# Windows - check if installed
claude --version
```

**Start a Remote Control session:**
```powershell
.\scripts\start_remote_control.ps1
```

Keep this terminal window open. Claude will connect through it.

---

## Deployment Commands

### Site Deployment

**Pull latest and deploy:**
> "Pull the latest main branch and restart the site"

Claude will:
1. Run `git pull origin main`
2. Run `Stop-ScheduledTask iLitSite; Start-ScheduledTask iLitSite` (about 45 seconds down)
3. Verify the site is running
4. Report status

**Deploy a change from a branch:**
> "Merge claude/feature-name into main and deploy"

Merge the change to `main`, pull `origin main` in the site worktree, then
restart the `iLitSite` task as above. Do not check out a feature branch in the
site worktree.

**Check deployment status:**
> "Is the site running? What version?"

Claude will:
1. Test http://127.0.0.1:8001/health
2. Check recent git log
3. Report what's currently deployed

---

## Database Commands

### Backups & Queries

**Backup the database:**
> "Back up the Postgres database"

Claude will:
1. Run `pg_dump` to create a SQL file
2. Save it with a timestamp
3. Report the file location

**Run a SQL query:**
> "Query the database: SELECT COUNT(*) FROM cases;"

Claude will:
1. Execute the query via `psql`
2. Return the results

**Check database health:**
> "Is the database running? Show me connection stats"

Claude will:
1. Test the connection
2. Show table counts and sizes
3. Report any issues

---

## Troubleshooting Commands

### Logs & Status

**Check application logs:**
> "Show the last 30 lines of application logs"

Claude will:
1. Read logs/app.out.log
2. Show recent errors or activity
3. Suggest fixes if needed

**Check Cloudflare tunnel status:**
> "Is the tunnel running? Show tunnel logs"

Claude will:
1. Check tunnel process status
2. Show recent tunnel events
3. Verify internet connectivity

**Full PC status check:**
> "Give me a full status report on the PC and site"

Claude will:
1. Check power settings
2. Verify all services are running
3. Test connectivity
4. Report any issues

---

## Advanced Commands

### Git Operations

**Revert a deployment:**
> "Revert to the previous commit and deploy"

Claude will:
1. Run `git revert HEAD`
2. Restart the `iLitSite` task with `Stop-ScheduledTask iLitSite; Start-ScheduledTask iLitSite`
3. Verify it's running

**Merge a branch to main:**
> "Merge claude/feature-name into main and deploy"

**View commit history:**
> "Show the last 5 commits on main"

### Database Migrations

**Run migrations:**
> "Run database migrations"

Claude will:
1. Check for pending migrations
2. Run them
3. Verify the schema

---

## Common Scenarios

### "The site is broken, fix it"
1. Start Remote Control: `.\scripts\start_remote_control.ps1`
2. Tell Claude: *"The site is broken. Check the logs and fix it."*
3. Claude will investigate and either:
   - Revert the last deployment
   - Fix the issue if it's known
   - Report what needs manual attention

### "Deploy my changes"
1. Commit and push your changes to a branch
2. Start Remote Control: `.\scripts\start_remote_control.ps1`
3. Tell Claude: *"Deploy the branch claude/my-feature"*
4. Claude pulls, deploys, and verifies

### "Scheduled daily backup"
1. You can ask Claude to back up the database
2. Ask me (Claude) to set up an automated backup if you want that

### "Maintenance window"
1. Start Remote Control
2. Tell Claude: *"Take the site down for maintenance"*
3. Make your changes
4. Tell Claude: *"Bring the site back online"*

---

## Getting Help

If something goes wrong:

1. **Check the logs:**
   > "Show me the application and tunnel logs"

2. **Get diagnostics:**
   > "Run diagnostics on the site and PC"

3. **Manual recovery:**
   > "Restart iLitSite" or "Rebuild the site from scratch"

---

## Notes

- **You don't need to type exact commands** — describe what you want and Claude will figure it out
- **Deployments take ~45 seconds** — the site will be offline briefly while iLitSite restarts
- **Fallback only:** run `scripts\refresh_site.ps1` only if the `iLitSite` task has been removed; do not run it while the task is installed
- **All changes go through Git** — if something breaks, it can always be reverted
- **The PC must stay plugged in** — if it goes to sleep, Claude can't connect until you wake it
- **Remote Control is secure** — connections are encrypted, and Claude only sees your project

---

Last updated: 2026-10-03
