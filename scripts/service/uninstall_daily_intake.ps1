# Removes the "iLitDailyIntake" scheduled task. Data already imported is left alone.
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$taskName = "iLitDailyIntake"
Stop-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
Write-Host "Removed scheduled task '$taskName' (if it existed)."
