# iLit Site Recovery Runbook

## Quick Recovery: Site Down

If https://www.ilit.ca/ is unreachable or localhost:8001 is not responding:

### 1. Check for stale process holding port 8001

```powershell
netstat -ano | findstr "127.0.0.1:8001.*LISTENING"
```

If a process is holding the port but the site isn't responding:
```powershell
# Kill the stale process (replace NNNN with the PID from netstat output)
Stop-Process -Id NNNN -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2
```

### 2. Verify no manual uvicorn is running

```powershell
Get-Process python -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -match "uvicorn" }
```

If manual uvicorn is found, stop it:
```powershell
Get-Process python -ErrorAction SilentlyContinue | Where-Object { $_.CommandLine -match "uvicorn" } | Stop-Process -Force
```

### 3. Restart the iLitSite scheduled task

```powershell
Stop-ScheduledTask -TaskName iLitSite -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2
Start-ScheduledTask -TaskName iLitSite
Start-Sleep -Seconds 50  # Wait for startup grace period
```

### 4. Verify recovery

```powershell
# Test localhost
$r = Invoke-WebRequest -Uri "http://localhost:8001/health/live" -TimeoutSec 3 -ErrorAction Stop
Write-Host "Local site: $($r.StatusCode)"

# Test public URL
$r = Invoke-WebRequest -Uri "https://www.ilit.ca/data-explorer" -TimeoutSec 5 -ErrorAction Stop
Write-Host "Public tunnel: $($r.StatusCode)"
```

Both should return 200.

## Root Causes

- **Stale process on port 8001**: Uvicorn or another process crashed but didn't release the port. The scheduled task's new process cannot bind and exits. Kill the stale process first.
- **Manual uvicorn running**: A manual start-command process is holding port 8001, blocking the scheduled task. Stop all manual Python processes and restart the task.
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
