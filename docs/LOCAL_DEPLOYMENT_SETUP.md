# Local Deployment Sessions Setup

Your laptop is now configured as an always-on deployment hub. Claude can connect via Remote Control to deploy changes, run database operations, and manage the site.

## What You Need

### 1. Claude CLI (If Not Installed)

The Claude CLI enables Remote Control connections. Check if it's installed:

```powershell
claude --version
```

If not found, install it:
- **macOS**: `brew install anthropics/claude-cli/claude-cli`
- **Windows**: Download from https://github.com/anthropics/claude-cli or use installer if available
- **Linux**: `pip install claude-cli` or download binary

### 2. Verify Remote Control is Available

Once Claude CLI is installed:

```powershell
claude remote-control --help
```

This should show help text if available.

## Starting an Idle Local Session

To keep a session ready for Claude to use, start one with Remote Control listening:

```powershell
cd "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary"
claude remote-control
```

This will:
1. Start a Remote Control server on your laptop
2. Print a code or URL you can share
3. Wait for Claude to connect

**Keep this window open.** Once Claude connects, you can run commands through this session.

### Optional: Run in Background (Advanced)

If you want the session to persist even after closing the terminal, you could:

```powershell
# Start PowerShell in background
Start-Process powershell -NoNewWindow -ArgumentList `
  "-NoExit", `
  "-Command", `
  "cd 'C:\Users\danny\OneDrive\Desktop\AI CaseLibrary'; claude remote-control"
```

Or create a scheduled task (similar to iLitSite) to auto-start a Remote Control session at login.

## Deployment Workflow

### Quick Deployment (No Questions)

1. Start the idle Remote Control session (see above)
2. Tell Claude: *"Deploy the latest main to production"* or *"Pull the latest changes"*
3. Claude connects to your PC via Remote Control
4. Claude pulls latest code, restarts the site, verifies it's running
5. Done — site is live

### Database Work

1. Start the idle Remote Control session
2. Tell Claude: *"Run a database query..."* or *"Backup the database"*
3. Claude connects and executes via `psql` on your PC (where the DB runs locally)

### Testing/Verification

1. Start the idle Remote Control session
2. Tell Claude: *"Check if the site is running"* or *"Verify the health endpoint"*
3. Claude connects and tests http://127.0.0.1:8001/health

## Deployment Quick Reference

Once a Remote Control session is running, tell Claude:

| Goal | Example |
|------|---------|
| **Deploy latest** | "Deploy the latest main to production" |
| **Pull + restart** | "Pull origin/main and restart the site" |
| **Check site status** | "Is the site running? Check the health endpoint" |
| **Database backup** | "Backup the Postgres database to a SQL file" |
| **View logs** | "Show me the last 50 lines of the app logs" |
| **Manual restart** | "Restart the iLitSite task" |

Claude will:
1. Connect to your PC via Remote Control
2. Run the necessary commands
3. Report what happened
4. Disconnect (the session stays idle for next time)

## Architecture

```
Your Laptop (Home Network)
├── iLitSite (Scheduled Task)
│   ├── FastAPI app on :8001
│   ├── Postgres database
│   └── Cloudflare tunnel → https://www.ilit.ca
├── Remote Control session (idle, waiting for Claude)
└── Power: Always plugged in, never sleeps on AC

Claude (Cloud)
└── Connects to your PC via Remote Control
    ├── Runs deployments
    ├── Queries database
    └── Manages the site
```

## Troubleshooting

### "Claude CLI not found"
- Reinstall Claude CLI
- Make sure it's in your PATH: `command -v claude` (PowerShell: `Get-Command claude`)

### "Remote Control connection failed"
- Verify the PC is plugged in and hasn't slept
- Check that iLitSite is running: `Get-ScheduledTask -TaskName iLitSite | Select-Object State`
- Restart the Remote Control session

### "Port 8001 is in use"
- Another process is using the port
- Run: `netstat -ano | Select-String ":8001"`
- Kill the process if it's not the FastAPI app

### Site doesn't respond after deployment
- Check the logs: `Get-Content "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\logs\app.out.log" -Tail 20`
- Restart iLitSite: `Stop-ScheduledTask iLitSite; Start-ScheduledTask iLitSite`
- Wait ~45 seconds for it to come back online

## Security Notes

- Remote Control connects over a secure tunnel; your credentials are never shared
- Claude only has access to your project folder and the database (which is local)
- The site runs on localhost:8001; only Cloudflare tunnel exposes it to the internet
- `.cloudflared/` credentials are kept secure and not committed to git

## Next Steps

1. **Install Claude CLI** if not already done
2. **Test a connection**: Start a Remote Control session and tell Claude to check the site status
3. **Automate (optional)**: Set up a scheduled task to auto-start Remote Control at login (ask Claude if you want this)

---

**Key Principle**: Keep your laptop plugged in at home, start a Remote Control session when you're ready for Claude to deploy, and Claude handles the rest. Simple and clear.
