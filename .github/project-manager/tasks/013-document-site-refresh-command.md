# Task: Document Site Refresh Command

Status: complete
Created: 2026-09-04
Updated: 2026-09-04

## Task Record

Task: Make the approved local site refresh command easy to find in the primary documentation.
Why now: The refresh workflow exists but is buried across operational references, making it easy to miss when restarting the website.
Owner surface: Repository startup and operations documentation
Dependencies: `scripts/refresh_site.ps1`, `scripts/run_local_with_tunnel.ps1`
Risk boundary: Documentation-only change; do not alter server, tunnel, process, or database behavior.
Smallest falsifiable check: Confirm the canonical command appears in the README and operational guide with the local and public URLs described.
Acceptance criteria: A developer can find and run the refresh command from the README, with operational details available in `OVERNIGHT.md` and `SYSTEM_REFERENCE.md`.
Docs/generated references: `README.md`, `OVERNIGHT.md`, `SYSTEM_REFERENCE.md`.
Rollback/recovery: Revert the documentation-only additions.
Evidence: Added the canonical `.\scripts\refresh_site.ps1` command and local/public URL guidance to `README.md`, `OVERNIGHT.md`, and `SYSTEM_REFERENCE.md`. Validation confirmed the command appears in all three files and `git diff --check` passed. No runtime code was changed.
