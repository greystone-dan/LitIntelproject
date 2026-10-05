# Registers the "iLitSite" scheduled task: starts the site and tunnel when you log in
# to Windows, runs hidden, and restarts itself if it ever stops. No admin rights needed.
# Run once:  powershell -ExecutionPolicy Bypass -File scripts\service\install_site_service.ps1
# To remove: powershell -ExecutionPolicy Bypass -File scripts\service\uninstall_site_service.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$taskName = "iLitSite"
$script = (Resolve-Path (Join-Path $PSScriptRoot "run_site.ps1")).Path
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path

$action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$script`"" `
    -WorkingDirectory $repoRoot
$trigger = New-ScheduledTaskTrigger -AtLogOn -User "$env:USERDOMAIN\$env:USERNAME"
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries `
    -StartWhenAvailable -RestartCount 999 -RestartInterval (New-TimeSpan -Minutes 1) `
    -ExecutionTimeLimit ([TimeSpan]::Zero) -MultipleInstances IgnoreNew
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger `
    -Settings $settings -Principal $principal -Force | Out-Null
Write-Host "Installed scheduled task '$taskName'. Starting it now..."
Stop-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
Start-ScheduledTask -TaskName $taskName
Write-Host "Done. Logs: $repoRoot\logs\site-service.log"
