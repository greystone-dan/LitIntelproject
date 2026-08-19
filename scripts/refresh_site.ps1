Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$localPort = 8000

Get-NetTCPConnection -LocalPort $localPort -State Listen -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty OwningProcess -Unique |
    ForEach-Object {
        Write-Host "Stopping existing site process (PID: $_)..."
        Stop-Process -Id $_ -Force
    }

Get-Process -Name cloudflared -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host "Stopping existing Cloudflare Tunnel (PID: $($_.Id))..."
    Stop-Process -Id $_.Id -Force
}

Push-Location $repoRoot
try {
    & (Join-Path $repoRoot "scripts\run_local_with_tunnel.ps1") -LocalPort $localPort
}
finally {
    Pop-Location
}