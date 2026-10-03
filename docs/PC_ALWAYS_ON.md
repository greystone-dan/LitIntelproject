# Keeping the iLit PC Always On and Ready for Claude

This PC runs the iLit website (https://www.ilit.ca) and the Postgres database that powers it. It must stay on and accessible at all times so Claude can deploy updates and run database tasks. This guide explains what runs on the PC and how to verify everything is working.

## What Runs on the PC

1. **iLitSite Scheduled Task** (`scripts\service\run_site.ps1`): Starts automatically at login and keeps both the FastAPI app (on port 8001) and the Cloudflare tunnel running. Restarts either one if it crashes. Health checks run every 30 seconds.

2. **FastAPI Backend**: The web application serving https://www.ilit.ca. Logs to `logs/app.out.log` and `logs/app.err.log`.

3. **Cloudflare Tunnel**: Routes traffic from the internet to the FastAPI app on localhost:8001. Configured in `.cloudflared/config.yml`. Logs to `logs/tunnel.out.log` and `logs/tunnel.err.log`.

4. **Postgres Database**: Runs as a local service (installed separately). The FastAPI app connects via `localhost:5432`.

## Power and Sleep Settings

The PC is configured to **never sleep or hibernate while plugged in to AC power**:

- **Sleep timeout on AC**: 0 seconds (disabled)
- **Hibernate timeout on AC**: 0 seconds (disabled)
- **Power plan**: High Performance
- **Active hours**: 4 AM to 10 PM (Windows won't force reboots during these hours)

All these settings are locked in via Windows power schemes.

## Checking if Everything is Working

### Quick Status Check

Open PowerShell and run:

```powershell
# Check if the iLitSite task is running
Get-ScheduledTask -TaskName "iLitSite" | Select-Object TaskName, State

# Check if the FastAPI app is listening
netstat -ano | Select-String ":8001.*LISTENING"

# Check the app is healthy
Invoke-WebRequest -Uri "http://127.0.0.1:8001/health" -UseBasicParsing
```

Expected output:
- iLitSite State: `Running`
- netstat shows `127.0.0.1:8001` in LISTEN state
- Health check returns HTTP 200

### Checking the Logs

If something isn't working, check these logs in the repo folder:

- `logs/site-service.log` — The supervisor script's activity log (starts/stops, errors)
- `logs/app.out.log` / `logs/app.err.log` — FastAPI app output and errors
- `logs/tunnel.out.log` / `logs/tunnel.err.log` — Cloudflare tunnel logs

## After a Power Cut or Reboot

When the PC restarts, Windows will:

1. Boot up (no login needed; the scheduled task will run at the system logon prompt)
2. Start the iLitSite task automatically
3. Start the FastAPI app and Cloudflare tunnel

**The website should be back online within 1-2 minutes.** Claude will be able to reach it and deploy changes.

If the site doesn't come back online within a few minutes, check the task status:

```powershell
Get-ScheduledTask -TaskName "iLitSite" | Select-Object TaskName, State
```

If the state is not `Running`, manually restart it:

```powershell
Start-ScheduledTask -TaskName "iLitSite"
```

## Windows Update and Reboots

The PC is configured with two safeguards:

1. **Active Hours (4 AM to 10 PM)**: Windows will not force a restart during normal hours.
2. **Windows Update**: Set to notify before installing updates. Restarts are configured to happen at 3 AM (outside active hours) and **only if no one is logged in**.

## If Claude Cannot Reach the PC

1. Check that the PC is plugged into power and powered on
2. Verify iLitSite is running (see "Quick Status Check" above)
3. Check the health endpoint: `http://127.0.0.1:8001/health`
4. Restart the task manually: `Start-ScheduledTask -TaskName "iLitSite"`
5. Check the log files for error messages

If you restart the PC or uninstall the scheduled task, reinstall it:

```powershell
& "scripts\service\install_site_service.ps1"
```

## Manual Deployment (if Claude is unavailable)

If Claude cannot reach the PC to deploy, you can deploy manually:

1. Open PowerShell as Administrator in the repo folder
2. Fetch the latest code: `git pull origin main`
3. Restart the site service:
   ```powershell
   Stop-ScheduledTask -TaskName "iLitSite"
   Start-ScheduledTask -TaskName "iLitSite"
   ```
   (This takes ~45 seconds; you'll see the website go offline briefly)
4. Verify the deployment: Visit https://www.ilit.ca or check `logs/app.out.log`

---

Last updated: 2026-10-03  
Maintained by: Claude (via Remote Control on Daniel's PC)
