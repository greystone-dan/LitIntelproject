param(
    [string]$ConfigPath = ".cloudflared/config.yml",
    [string]$LocalHost = "127.0.0.1",
    [int]$LocalPort = 8000,
    [switch]$SkipApiStart
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$configFullPath = Join-Path $repoRoot $ConfigPath

if (-not (Test-Path $configFullPath)) {
    throw "Tunnel config not found: $configFullPath. Run scripts/setup_cloudflare_tunnel.ps1 first."
}

$cloudflaredCmd = Get-Command cloudflared -ErrorAction SilentlyContinue
$cloudflaredExe = if ($cloudflaredCmd) { $cloudflaredCmd.Source } else { $null }
if (-not $cloudflaredExe) {
    $knownCloudflared = "C:\Program Files (x86)\cloudflared\cloudflared.exe"
    if (Test-Path $knownCloudflared) {
        $cloudflaredExe = $knownCloudflared
        $env:Path = "C:\Program Files (x86)\cloudflared;" + $env:Path
    }
}
if (-not $cloudflaredExe) {
    throw "cloudflared not found in PATH. Install it and retry."
}

$apiProcess = $null
Push-Location $repoRoot
try {
    if (-not $SkipApiStart) {
        $pythonExe = Join-Path $repoRoot "venv/Scripts/python.exe"
        if (-not (Test-Path $pythonExe)) {
            throw "Python executable not found at $pythonExe"
        }

        Write-Host "Starting local API on http://${LocalHost}:${LocalPort} ..."
        $apiProcess = Start-Process -FilePath $pythonExe `
            -ArgumentList "-m", "uvicorn", "backend.main:app", "--host", $LocalHost, "--port", $LocalPort `
            -WorkingDirectory $repoRoot `
            -PassThru

        if ($apiProcess.HasExited) {
            throw "Local API process exited early with code $($apiProcess.ExitCode)."
        }

        Write-Host "API process started (PID: $($apiProcess.Id))."
    }

    Write-Host "Starting Cloudflare Tunnel with config: $configFullPath"
    Write-Host "Press Ctrl+C to stop the tunnel (and local API if started by this script)."

    & $cloudflaredExe tunnel --config $configFullPath run
}
finally {
    if ($apiProcess -and -not $apiProcess.HasExited) {
        Write-Host "Stopping local API process (PID: $($apiProcess.Id))..."
        Stop-Process -Id $apiProcess.Id -Force
    }
    Pop-Location
}
