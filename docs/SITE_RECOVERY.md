# iLit Site Recovery Runbook

## Quick Recovery: Site Down

If https://www.ilit.ca/ is unreachable or localhost:8001 is not responding:

### 1. Restart the iLitSite scheduled task

The scheduled task is the primary site and tunnel process. Restart it first:

```powershell
Stop-ScheduledTask iLitSite; Start-ScheduledTask iLitSite
Start-Sleep -Seconds 50  # Wait for startup grace period
```

After `git pull origin main`, use the same restart command. Keep the site worktree on `main`.
`scripts\refresh_site.ps1` is a fallback only if the task has been removed; do
not run it while the task is installed.

### 2. Verify recovery

```powershell
# Test localhost
$r = Invoke-WebRequest -Uri "http://localhost:8001/health/live" -TimeoutSec 3 -ErrorAction Stop
Write-Host "Local site: $($r.StatusCode)"

# Test public URL
$r = Invoke-WebRequest -Uri "https://www.ilit.ca/data-explorer" -TimeoutSec 5 -ErrorAction Stop
Write-Host "Public tunnel: $($r.StatusCode)"
```

Both should return 200.

### 3. If recovery fails, check for competing processes

Only troubleshoot process conflicts if the scheduled-task restart and health
checks above do not restore service.

Check for a process holding port 8001:

```powershell
netstat -ano | findstr "127.0.0.1:8001.*LISTENING"
```

If a process is holding the port but the site isn't responding, confirm it is
not managed by `iLitSite` before stopping it:

```powershell
# Kill only a confirmed stale process (replace NNNN with its PID)
Stop-Process -Id NNNN -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2
```

If the listener is a manually started Uvicorn process, stop only its confirmed
PID using the command above. Do not bulk-stop Python processes managed by the
scheduled task.

## Root Causes

- **Stale process on port 8001**: Uvicorn or another process crashed but didn't release the port. The scheduled task's new process cannot bind and exits. Identify the process and stop it only if it is confirmed not to be managed by `iLitSite`.
- **Manual uvicorn running**: A manually started process is holding port 8001, blocking the scheduled task. Stop only confirmed manual processes, then restart the task.
- **Task startup delay**: The scheduled task waits 45 seconds for processes to start before health checks begin. Allow at least 50 seconds before testing.
- **Tunnel connectivity**: If the public URL fails but localhost works, the Cloudflare tunnel may need to restart. Restart the task (it manages both the app and tunnel).

## Site Architecture

- **Deployment**: iLitSite scheduled task (Windows) manages both the FastAPI app (uvicorn) and Cloudflare tunnel
- **App**: `scripts\service\run_site.ps1` supervises and restarts both processes
- **Database**: PostgreSQL on localhost:5432
- **Monitoring**: Task health checks /health every 30s; 3 consecutive failures trigger a restart

## If Recovery Steps Don't Work

1. Check task logs:
   ```powershell
   Get-Content "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\logs\site-service.log" -Tail 20
   ```

2. Check app error log:
   ```powershell
   Get-Content "C:\Users\danny\OneDrive\Desktop\AI CaseLibrary\logs\app.err.log" -Tail 20
   ```

3. Verify Postgres is running and responding:
   ```bash
   psql -h localhost -U postgres -d caselibrary -c "SELECT version();"
   ```

4. Check .env is correct (password gate OFF, semantic search OFF):
   ```bash
   grep "CASELIBRARY_ACCESS_PASSWORD\|CASELIBRARY_SEMANTIC_ENABLED" .env | tail -2
   ```
