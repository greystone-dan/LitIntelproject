# Cloudflare Tunnel Setup (Local Machine Hosting)

This setup publishes your local AI CaseLibrary app to your domain via Cloudflare Tunnel.

## Prerequisites

- Domain is active in Cloudflare DNS
- Cloudflare Zero Trust access for your account
- Local project already runs on this machine
- Windows PowerShell

## One-Time Setup

Run from repo root:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup_cloudflare_tunnel.ps1 -Hostname your.domain.com -TunnelName aicaselibrary-local -LocalPort 8070
```

What this does:

1. Installs cloudflared with winget if missing.
2. Opens Cloudflare login if needed.
3. Creates (or reuses) a named tunnel.
4. Creates DNS route from hostname to the tunnel.
5. Writes local tunnel config to `.cloudflared/config.yml`.

## Run App + Tunnel

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_local_with_tunnel.ps1
```

Then open:

- `https://your.domain.com`

## If API Is Already Running Elsewhere

Use:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\run_local_with_tunnel.ps1 -SkipApiStart -LocalPort 8070
```

## Notes

- `.cloudflared/` is ignored by Git to avoid committing local tunnel config.
- Tunnel credentials are stored by cloudflared under your user profile.
- If you change local app port, re-run setup with `-LocalPort` so config stays aligned.
