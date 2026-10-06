# Runs one daily intake pass (new A2AJ decisions + new Federal Court IMM activity records).
# Launched by the "iLitDailyIntake" scheduled task (see install_daily_intake.ps1); safe to run by hand.
# Extra arguments are passed through, e.g.:  run_daily_intake.ps1 --dry-run
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$logDir = Join-Path $repoRoot "logs\intake"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir ("daily-{0}.log" -f (Get-Date -Format "yyyyMMdd"))
$pythonExe = Join-Path $repoRoot "venv\Scripts\python.exe"
if (-not (Test-Path $pythonExe)) { throw "Missing $pythonExe" }

Set-Location $repoRoot
# Stay out of the live site's way.
(Get-Process -Id $PID).PriorityClass = "BelowNormal"
"{0}  starting daily intake {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), ($args -join " ") | Add-Content -Path $logFile

# Python logs to stderr; merge it so the log has everything.
$env:PYTHONIOENCODING = "utf-8"
& $pythonExe "scripts\daily_intake.py" @args 2>&1 | ForEach-Object { "$_" } | Add-Content -Path $logFile
$code = $LASTEXITCODE
"{0}  finished with exit code {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $code | Add-Content -Path $logFile
exit $code
