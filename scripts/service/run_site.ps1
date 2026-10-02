# Supervisor: keeps the iLit app (uvicorn) and the Cloudflare tunnel running.
# Restarts either one if it exits, and restarts the app if /health stops answering.
# Normally launched by the "iLitSite" scheduled task (see install_site_service.ps1).
param(
    [int]$LocalPort = 8001,
    [string]$ConfigPath = ".cloudflared/config.yml"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$logDir = Join-Path $repoRoot "logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "site-service.log"

function Write-Log([string]$msg) {
    $line = "{0}  {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $msg
    Add-Content -Path $logFile -Value $line
}

$pythonExe = Join-Path $repoRoot "venv\Scripts\python.exe"
$configFull = Join-Path $repoRoot $ConfigPath
$cloudflared = (Get-Command cloudflared -ErrorAction SilentlyContinue).Source
if (-not $cloudflared) { $cloudflared = "C:\Program Files (x86)\cloudflared\cloudflared.exe" }
foreach ($p in @($pythonExe, $configFull, $cloudflared)) {
    if (-not (Test-Path $p)) { Write-Log "Missing required file: $p"; throw "Missing required file: $p" }
}

function Stop-Stale {
    Get-CimInstance Win32_Process -Filter "Name = 'python.exe'" |
        Where-Object { $_.CommandLine -match "uvicorn\s+backend\.main:app" } |
        ForEach-Object { Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
    Get-Process -Name cloudflared -ErrorAction SilentlyContinue |
        Stop-Process -Force -ErrorAction SilentlyContinue
}

function Test-Health {
    try {
        $r = Invoke-WebRequest -Uri "http://127.0.0.1:$LocalPort/health" -UseBasicParsing -TimeoutSec 10
        return ($r.StatusCode -eq 200)
    } catch { return $false }
}

Set-Location $repoRoot
while ($true) {
    Stop-Stale
    Write-Log "Starting app on port $LocalPort and tunnel"
    $app = Start-Process -FilePath $pythonExe -WindowStyle Hidden -PassThru -WorkingDirectory $repoRoot `
        -ArgumentList "-m", "uvicorn", "backend.main:app", "--host", "127.0.0.1", "--port", $LocalPort `
        -RedirectStandardOutput (Join-Path $logDir "app.out.log") -RedirectStandardError (Join-Path $logDir "app.err.log")
    $tunnel = Start-Process -FilePath $cloudflared -WindowStyle Hidden -PassThru -WorkingDirectory $repoRoot `
        -ArgumentList "tunnel", "--config", $configFull, "run" `
        -RedirectStandardOutput (Join-Path $logDir "tunnel.out.log") -RedirectStandardError (Join-Path $logDir "tunnel.err.log")

    $failures = 0
    Start-Sleep -Seconds 45   # startup grace period before health checks begin
    while ($true) {
        if ($app.HasExited) { Write-Log "App exited (code $($app.ExitCode))"; break }
        if ($tunnel.HasExited) { Write-Log "Tunnel exited (code $($tunnel.ExitCode))"; break }
        if (Test-Health) { $failures = 0 } else { $failures++ }
        if ($failures -ge 3) { Write-Log "Health check failed 3 times in a row"; break }
        Start-Sleep -Seconds 30
    }
    Write-Log "Restarting in 10 seconds"
    Start-Sleep -Seconds 10
}
