# Deployment And Remote Control Reference

Use this guide for interactive Remote Control setup and the Git-to-main
deployment workflow. For the exact site restart, health, log, and port-safety
procedures, use the [Operational Recovery Guide](OPERATIONAL_RECOVERY_GUIDE.md).

The production site is managed by the Windows scheduled task `iLitSite`; keep
its worktree on `main`. After pulling a merged change, follow the recovery
guide's Windows Site Recovery procedure to restart and verify the service.
That guide also documents the `scripts\refresh_site.ps1` fallback boundary.

## CLI prerequisite

Install and authenticate the Claude CLI using its supported vendor instructions.
Check availability with `claude --version` and
`claude remote-control --help`; do not use the retired local setup note's
unverified installation suggestions.

## Start a Remote Control session

The interactive Remote Control session is separate from the persistent
`iLitSite` scheduled task. With the Claude CLI installed and authenticated, run
the repository helper from the repository root:

```powershell
.\scripts\start_remote_control.ps1
```

Keep the terminal window open while Claude is connected. The helper checks for
the CLI and reports whether `iLitSite` is running; it does not deploy or restart
the site.

---

## Deployment Commands

### Site Deployment

**Pull latest and deploy:**
> "Pull the latest main branch and restart the site"

Claude will:
1. Run `git pull origin main`
2. Follow the Operational Recovery Guide's Windows Site Recovery procedure
3. Report the deployment status

**Deploy a change from a branch:**
> "Merge claude/feature-name into main and deploy"

Merge the change to `main`, pull `origin main` in the site worktree, then
follow the Operational Recovery Guide to restart and verify the site. Do not
check out a feature branch in the site worktree.

**Check deployment status:**
> "Is the site running? What version?"

Claude will:
1. Use the Operational Recovery Guide's health checks
2. Check recent Git history
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

**Check application or tunnel logs:**
> "Show the last 30 lines of application logs"

For service, application, or tunnel logs and health diagnostics, follow the
Operational Recovery Guide.

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
2. Follow the Operational Recovery Guide to restart and verify the site

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
- **Restart duration and verification:** follow the Windows Site Recovery procedure in the Operational Recovery Guide
- **All changes go through Git** — if something breaks, it can always be reverted
- **The PC must stay plugged in** — if it goes to sleep, Claude can't connect until you wake it
- **Remote Control is secure** — connections are encrypted, and Claude only sees your project

---

Last updated: 2026-10-03
