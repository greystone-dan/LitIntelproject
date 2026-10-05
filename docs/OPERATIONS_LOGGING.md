# Operations Logging

## Request IDs and slow requests

Every HTTP response includes `X-Request-ID`. A valid incoming ID is preserved;
otherwise, the app generates one. Valid IDs are 8–64 ASCII letters, digits,
underscores, or hyphens.

Slow-request logging is off unless `SLOW_REQUEST_LOG_MS` is set to a positive
integer. Requests are logged only when their duration is strictly greater than
the threshold. Each log line is JSON with `request_id`, `method`,
`route_template`, `status`, and `duration_ms`. It contains no request body,
uploaded text, query string, raw path, host, or secret.

## Reading app logs on the PC

The site service redirects app stdout and stderr to `logs/app.out.log` and
`logs/app.err.log` under the repository root. Slow-request lines use Uvicorn's
INFO-level `uvicorn.error` logger and are written to stderr. In PowerShell,
from the repository root, follow the app log:

```powershell
Get-Content .\logs\app.err.log -Tail 100 -Wait
```

To find a request in either app log, search using the ID from its response:

```powershell
Select-String -Path .\logs\app.out.log, .\logs\app.err.log -Pattern '"request_id":"abc123def456ghi789jkl012"'
```

`logs/site-service.log` records service start and restart messages, not app
requests. The app does not create a separate slow-request log file.

## Version and health

`GET /health/ready` includes a `version` object while preserving its existing
readiness checks and 503 behavior. `GET /api/version` returns the same fields:

- `commit`: sanitized `APP_COMMIT`, or the short Git commit when the repository
  `.git` directory exists; otherwise `unknown`.
- `started_at`: process start time as a Unix timestamp.
- `python_version`: Python interpreter version.

The version responses do not include environment dumps, hostnames, or secrets.
`/api/version` follows the existing optional password gate.

## Separate audit log

The optional `CASELIBRARY_AUDIT_LOG` feature writes rotating request metadata
logs to its configured file. It is separate from slow-request logging; see
[Configuration Reference](CONFIGURATION_REFERENCE.md) for its settings.
