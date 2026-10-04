# Optional Security Response Headers

Security response headers are defense-in-depth controls. They do not provide
authentication, prevent a caller from reaching the service, or replace a
trusted reverse-proxy/tunnel access policy. The feature is disabled unless
explicitly enabled.

## Enable and configure

Set `CASELIBRARY_SECURITY_HEADERS=1` in the server process environment and
restart the application. The middleware reads its settings when the application
is initialized.

| Variable | Default | Behavior |
| --- | --- | --- |
| `CASELIBRARY_SECURITY_HEADERS` | `0` (disabled) | Enables the response headers only when set to `1`. |
| `CASELIBRARY_HSTS_MAX_AGE` | `31536000` seconds | HSTS max age; invalid values fall back to the default and negative values are clamped to zero. |
| `CASELIBRARY_HSTS_SUBDOMAINS` | `0` | Adds `includeSubDomains` only when set to `1`. |
| `CASELIBRARY_CSP_ENFORCE` | `0` | Uses `Content-Security-Policy` instead of report-only mode only when set to `1`. |

When enabled, responses receive `X-Content-Type-Options: nosniff`,
`Referrer-Policy: strict-origin-when-cross-origin`,
`X-Frame-Options: SAMEORIGIN`, and a `Permissions-Policy` that denies camera,
microphone, and geolocation. The middleware does not replace a response header
already set by a route. It does not buffer or consume request or response
bodies.

HSTS is added only when the ASGI request scheme is HTTPS or the first
`X-Forwarded-Proto` value is `https`. Behind a proxy, configure the trusted
proxy to overwrite forwarded-protocol headers; do not trust client-supplied
forwarding headers at an untrusted boundary. HSTS is not added to ordinary
HTTP requests. `includeSubDomains` affects every subdomain, so enable it only
when all subdomains are HTTPS-capable.

The middleware preserves the app's existing no-index, access/password,
no-cache, and audit behavior. `X-Robots-Tag` remains an indexing directive,
not authentication. See [configuration reference](CONFIGURATION_REFERENCE.md)
for the complete environment-variable inventory.

## Review Content-Security-Policy-Report-Only findings

The default CSP response is `Content-Security-Policy-Report-Only`. It asks the
browser to report policy violations without blocking the resource. The current
middleware does not configure a server-side CSP report-collection endpoint;
inspect the browser's developer-tools Console (and Network panel as needed)
while exercising the active research pages. Review each violation's directive,
blocked URL, and page before deciding whether the resource is intentional.
Do not broadly allow an origin just to silence a warning.

The initial policy is based on a scan of generated page output under
`backend/pages/`: current pages use inline scripts and styles, Google Fonts
stylesheets from `fonts.googleapis.com`, font files from `fonts.gstatic.com`,
Lucide scripts from `unpkg.com`, and data-URL images. These uses are reflected
in `script-src`, `style-src`, `font-src`, and `img-src`. Re-scan generated HTML
and review report-only findings whenever page output or third-party resources
change; this inventory is not a guarantee that every future page is covered.
The policy allows `'unsafe-inline'` scripts and styles for current generated
pages, which limits CSP's protection against injected inline code.

`CASELIBRARY_CSP_ENFORCE=1` switches to the enforcing
`Content-Security-Policy` header. Enforcement has not been tested and may block
page functionality; keep report-only mode while reviewing all affected pages
and do not enable enforcement without a separate browser validation.

## Validation

Focused middleware coverage is in `tests/test_security_headers.py`:

```sh
python -m pytest -q tests/test_security_headers.py
```

The tests cover default passthrough, enabled headers, HSTS scheme and forwarded
protocol handling, preservation of existing response headers, streaming bodies,
and application middleware registration/order.
