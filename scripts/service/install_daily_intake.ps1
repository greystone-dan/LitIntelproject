# Registers the "iLitDailyIntake" scheduled task: once a day (default 03:30) it pulls new decisions
# and new Federal Court IMM activity records. Runs hidden at low priority, no admin rights needed.
# If the PC was off at the scheduled time, it runs when the PC is next available.
# Run once:  powershell -ExecutionPolicy Bypass -File scripts\service\install_daily_intake.ps1 [-At "03:30"]
# To remove: powershell -ExecutionPolicy Bypass -File scripts\service\uninstall_daily_intake.ps1
param([string]$At = "03:30")
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$taskName = "iLitDailyIntake"
$script = (Resolve-Path (Join-Path $PSScriptRoot "run_daily_intake.ps1")).Path
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$script`"" `
    -WorkingDirectory $repoRoot
$trigger = New-ScheduledTaskTrigger -Daily -At $At
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
    -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 3) -MultipleInstances IgnoreNew
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger `
    -Settings $settings -Principal $principal -Force | Out-Null
Write-Host "Installed scheduled task '$taskName' (daily at $At). It has NOT been run yet."
Write-Host "Try it first:  powershell -File `"$script`" --dry-run"
Write-Host "Logs: $repoRoot\logs\intake\daily-YYYYMMDD.log"
