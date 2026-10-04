# Operations and Request Observability Logging

This document describes operational logging and observability features for AI CaseLibrary.

## Request Observability Overview

AI CaseLibrary provides two complementary observability layers:

1. **Audit Logging** (`backend/audit.py`) — optional, when configured via `CASELIBRARY_AUDIT_LOG`
   - Request/response metadata, timestamps, addresses (optionally hashed)
   - Sensitive routes do not log request content
   - Persisted to a rotating file with backups

2. **Request Observability** (`backend/request_context.py`) — always-on request ID header, optional slow-request logging
   - X-Request-ID header on every response
   - Optional structured slow-request logging when threshold is configured

## Request ID Management

### Overview
Every HTTP response includes an `X-Request-ID` response header. This header contains either:
- A validated incoming request ID (if the client provided one and it matched validation rules)
- A generated request ID (if no incoming ID, or the incoming ID was invalid)

### Validation Rules
Incoming `X-Request-ID` header values must be:
- ASCII text (no UTF-8 or extended characters)
- Between 8 and 64 characters long
- Containing only: letters (a-z, A-Z), digits (0-9), underscores (_), and hyphens (-)

Examples of valid IDs:
- `my-request-id-12345678`
- `Request_ID_001`
- `abc12345`

Examples of invalid IDs (will be replaced):
- Empty string
- `id@client` (contains `@`)
- `test/request` (contains `/`)
- `a` (too short, only 1 character)
- `a` * 100 (too long)
- `\x00\x01` (control characters)

### ID Generation
When a request ID must be generated (either no incoming ID, or invalid incoming ID), the backend:
1. Generates a 24-character random string
2. Uses only ASCII letters, digits, underscores, and hyphens
3. Uses cryptographically secure randomization (Python's `secrets` module)
4. Ensures uniqueness with overwhelming probability

## Slow-Request Logging

### Configuration
Enable optional structured logging of slow requests:

```bash
export SLOW_REQUEST_LOG_MS=500
```

This logs any request where elapsed time is **strictly greater than** 500 milliseconds.

### Threshold Behavior
- **Disabled by default**: If `SLOW_REQUEST_LOG_MS` is not set or is empty, slow-request logging does not run
- **Strictly greater than**: A request taking exactly 500ms is NOT logged (must exceed the threshold)
- **Ignored if invalid**: Non-numeric values or values ≤ 0 disable logging

### Log Fields
When a request exceeds the threshold, the log entry includes:

| Field | Example | Remarks |
| --- | --- | --- |
| `request_id` | `abc123def456ghi789jkl012` | The request ID (validated or generated) |
| `method` | `GET`, `POST` | HTTP method |
| `route_template` | `/api/search`, `/cases/{id}` | Resolved route template (never raw URL) |
| `status` | `200`, `404`, `500` | HTTP status code |
| `duration_ms` | `750.5` | Elapsed time in milliseconds |

### What is Never Logged
To preserve privacy and security, the following information is **never** included in slow-request logs:

- Request body
- Uploaded text or file content
- Query string parameters
- Raw request path with query string
- Request headers (except indirectly via route detection)
- Hostnames or IP addresses
- Credentials or secrets
- User-provided text or input

### Route Template Handling
The log entry attempts to resolve the matched route template (e.g., `/cases/{id}`) rather than the raw request path (e.g., `/cases/12345`). If the route template cannot be resolved, the log uses the fixed safe marker `<unknown>`.

### Log Format
Slow-request events use Uvicorn's `uvicorn.error` logger at INFO level. In the
default Uvicorn logging configuration used by `scripts/service/run_site.ps1`,
that logger propagates to Uvicorn's default stderr handler. The log message is
a compact, single-line JSON object containing exactly `request_id`, `method`,
`route_template`, `status`, and `duration_ms`; it does not create or rotate a
separate log file. The service redirects stderr to `logs/app.err.log` and
stdout to `logs/app.out.log`. If a custom Uvicorn logging configuration is
introduced, keep `uvicorn.error` at INFO and connected to the intended handler.

On the PC, the existing site service redirects the app's stdout and stderr to
`logs/app.out.log` and `logs/app.err.log` under the repository root. From
PowerShell, follow the app logs with:

```powershell
Get-Content .\logs\app.err.log -Tail 100 -Wait
```

To find one request in either app log, replace the example ID with the value
from the response's `X-Request-ID` header:

```powershell
Select-String -Path .\logs\app.out.log, .\logs\app.err.log -Pattern '"request_id":"abc123def456ghi789jkl012"'
```

The separate `logs/site-service.log` records supervisor start, stop, and
restart messages. It does not contain the app's structured slow-request records.

## Audit Logging (Separate Feature)

Audit logging is a separate, optional feature configured via `CASELIBRARY_AUDIT_LOG` environment variable. See `backend/audit.py` for details. Audit logs are persisted to a file and include request/response metadata with sanitized sensitive routes.

## Health and Readiness Endpoints

### /health/live
- Endpoint: `GET /health/live`
- Response: `{"status": "ok"}`
- Purpose: liveness probe, checks only that the process is running
- No dependencies checked
- Public, always accessible

### /health/ready
- Endpoint: `GET /health/ready`
- Response (ready): `{"status": "ok", "checks": {...}, "version": {...}}` (HTTP 200)
- Response (not ready): `{"status": "error", "checks": {...}, "version": {...}}` (HTTP 503)
- Version fields: `commit` (sanitized `APP_COMMIT` or guarded Git short hash, otherwise `unknown`), `started_at` (Unix timestamp), `python_version` (interpreter version)
- Checks:
  - Database connectivity and timeout
  - pgvector extension availability
  - Required tables present
  - Configured model endpoints (if configured)
- Public, always accessible
- Includes safe version information

### /api/version
- Endpoint: `GET /api/version`
- Response: `{"commit": "...", "started_at": ..., "python_version": "..."}`
- Purpose: Retrieve safe application runtime version metadata
- Fields:
  - `commit`: sanitized `APP_COMMIT`, or Git short commit hash only when the repository `.git` directory exists; otherwise `unknown`
  - `started_at`: Unix timestamp when the process started
  - `python_version`: Running Python interpreter version
- Never exposes: environment variables, deployment details, hostnames, secrets, `.env` contents
- Follows the existing optional application password-gate configuration

## Debugging with Request IDs

When troubleshooting an issue:

1. Note the `X-Request-ID` from the response header
2. Check slow-request logs for that ID (if enabled and request was slow)
3. Check audit logs for that ID (if enabled)
4. Correlate with application logs using the request ID

Example:
```bash
# Client receives response with header
X-Request-ID: req-abc123def456ghi789jkl012

# Look for request ID in the configured application log destination
grep '"request_id":"req-abc123def456ghi789jkl012"' /path/to/application-log

# Look for request ID in audit logs (if enabled)
grep "req-abc123def456ghi789jkl012" /path/to/audit.log
```

## Configuration Precedence

- Audit logging configuration: `CASELIBRARY_AUDIT_LOG` (file path)
- Audit address hashing: `CASELIBRARY_AUDIT_LOG_RAW_ADDRESS` (default: hashed)
- Slow-request threshold: `SLOW_REQUEST_LOG_MS` (default: disabled)
- App version commit: sanitized 7-40 hex `APP_COMMIT`; invalid values are ignored. Git is queried only when the repository `.git` directory exists; otherwise commit is `unknown`.

Refer to `docs/CONFIGURATION_REFERENCE.md` for a complete configuration guide.
