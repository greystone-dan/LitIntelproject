Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$localPort = 8000

Get-CimInstance Win32_Process -Filter "Name = 'python.exe'" |
    Where-Object {
        $_.CommandLine -match "uvicorn\s+backend\.main:app"
    } |
    ForEach-Object {
        Write-Host "Stopping existing AI CaseLibrary server (PID: $($_.ProcessId))..."
        Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
    }

Get-NetTCPConnection -LocalPort $localPort -State Listen -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty OwningProcess -Unique |
    ForEach-Object {
        Write-Host "Stopping existing site process (PID: $_)..."
        Stop-Process -Id $_ -Force -ErrorAction SilentlyContinue
    }

Get-Process -Name cloudflared -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host "Stopping existing Cloudflare Tunnel (PID: $($_.Id))..."
    Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue
}

Push-Location $repoRoot
try {
    & (Join-Path $repoRoot "scripts\run_local_with_tunnel.ps1") -LocalPort $localPort
}
finally {
    Pop-Location
}