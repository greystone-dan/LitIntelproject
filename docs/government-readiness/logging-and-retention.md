# Logging and retention

## Optional application audit log

`RequestAuditMiddleware` creates a JSON-lines rotating file handler only when
`CASELIBRARY_AUDIT_LOG` is set. Its configured maximum is 5 MiB with three
backup files. The parent directory must exist; the handler suppresses logging
errors rather than printing record contents. [backend/audit.py:14-42](../../backend/audit.py#L14-L42)
[docs/CONFIGURATION_REFERENCE.md:50-65](../CONFIGURATION_REFERENCE.md#L50-L65)

Each recorded HTTP request contains:

- UTC timestamp and generated request ID;
- HTTP method and matched route template (`<unmatched>` for no matched route);
- response status and elapsed time in milliseconds;
- an HMAC-SHA256 hash of the client address, using a random process-local key;
- raw client address only when `CASELIBRARY_AUDIT_LOG_RAW_ADDRESS=true`.

The client-address hash is not stable across workers or restarts. The middleware
does **not** record request/response bodies, filenames, query strings, headers,
or cookies. These are statements about the application audit middleware only;
they do not establish logging behavior at Uvicorn, Windows, Cloudflare, the
browser, a reverse proxy, or an upstream hosting layer. [backend/audit.py:49-94](../../backend/audit.py#L49-L94)
[docs/CONFIGURATION_REFERENCE.md:57-65](../CONFIGURATION_REFERENCE.md#L57-L65)

The configuration reference says the audit log is disabled unless the path is
configured. Runtime values are read at middleware initialization, so changing
them requires a server restart. [backend/audit.py:20-43](../../backend/audit.py#L20-L43)
[docs/CONFIGURATION_REFERENCE.md:50-58](../CONFIGURATION_REFERENCE.md#L50-L58)

## Other logs visible in the service script

The Windows supervisor appends timestamped status messages to
`logs/site-service.log` and redirects application and tunnel stdout/stderr to
`logs/app.out.log`, `logs/app.err.log`, `logs/tunnel.out.log`, and
`logs/tunnel.err.log`. The script contains no rotation or retention policy for
these files. Actual log contents, access permissions, backup, rotation, and
deletion on the live PC are **unverified**. [scripts/service/run_site.ps1:12-20](../../scripts/service/run_site.ps1#L12-L20)
[scripts/service/run_site.ps1:48-67](../../scripts/service/run_site.ps1#L48-L67)

## Application data and retention boundaries

- The memo-citation-check route passes upload bytes to its analyzer and returns
  results; no application-managed upload record is created in that handler.
  The code does not establish cleanup behavior for multipart spooling,
  framework/server memory, browser state, proxy logs, or backups.
  [backend/routes.py:1040-1054](../../backend/routes.py#L1040-L1054)
  [backend/memo_citation_check.py:102-119](../../backend/memo_citation_check.py#L102-L119)
- The build-time paragraph assessment script writes request/response JSON and
  Markdown output to operator-selected paths, and may write a raw response on
  parse failure. It does not define retention or secure deletion for those
  outputs. [scripts/package_discussion_units_llm.py:391-405](../../scripts/package_discussion_units_llm.py#L391-L405)
  [scripts/package_discussion_units_llm.py:491-552](../../scripts/package_discussion_units_llm.py#L491-L552)
- Database backups and database-record retention are not governed by the
  inspected application code. Actual backup schedules and deletion procedures
  are not verified here.

## Items requiring live verification

See the pack's [LIVE-PC-02](README.md#live-pc-verification-register),
[LIVE-PC-03](README.md#live-pc-verification-register), and
[LIVE-PC-04](README.md#live-pc-verification-register) checks for the current
database/filesystem location, temporary storage, log paths/permissions,
rotation, forwarding, backups, and retention. Provider-side retention is
listed separately in [subprocessors](subprocessors.md).
