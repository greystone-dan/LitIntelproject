# Start a Remote Control session for Claude to connect to
# Usage: .\scripts\start_remote_control.ps1

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path

Write-Host ""
Write-Host "================================" -ForegroundColor Green
Write-Host "Claude Remote Control Session" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "Checking prerequisites..."

# Check if Claude CLI is installed
$claude = Get-Command claude -ErrorAction SilentlyContinue
if (-not $claude) {
    Write-Host "ERROR: Claude CLI not found" -ForegroundColor Red
    Write-Host ""
    Write-Host "Install Claude CLI from: https://github.com/anthropics/claude-cli"
    Write-Host "Then run this script again."
    exit 1
}

Write-Host "✓ Claude CLI found at: $($claude.Source)"

# Verify iLitSite is running
$iLitTask = Get-ScheduledTask -TaskName "iLitSite" -ErrorAction SilentlyContinue
if ($iLitTask -and $iLitTask.State -eq "Running") {
    Write-Host "✓ iLitSite is running"
} else {
    Write-Host "⚠ iLitSite is not running" -ForegroundColor Yellow
    Write-Host "  Claude can still connect, but deployments may not work."
    Write-Host "  To start iLitSite: Start-ScheduledTask -TaskName iLitSite"
}

# Verify FastAPI is listening
$listening = netstat -ano 2>$null | Select-String ":8001.*LISTENING"
if ($listening) {
    Write-Host "✓ FastAPI is listening on port 8001"
} else {
    Write-Host "⚠ FastAPI is not listening on port 8001" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Starting Remote Control session..."
Write-Host "This window will stay open while Claude is connected."
Write-Host "Once Claude connects, you'll see a confirmation message."
Write-Host ""
Write-Host "To stop: press Ctrl+C"
Write-Host ""

Set-Location $repoRoot
& claude remote-control
