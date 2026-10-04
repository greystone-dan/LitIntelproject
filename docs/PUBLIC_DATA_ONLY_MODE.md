# Public-data-only deployment mode

`CASELIBRARY_PUBLIC_DATA_ONLY` is an opt-in deployment profile for installations
that should support public case-law research without accepting document or
free-text analysis submissions. It defaults to off; existing behavior is
unchanged unless the setting is enabled.

Set it in the server process environment:

```dotenv
CASELIBRARY_PUBLIC_DATA_ONLY=on
```

The server reads the value for each request. Empty, `0`, `false`, and `off`
(case-insensitive) mean off; other non-empty values mean on. There is no
`.env` change or deployment script required. This profile is an application
feature restriction, not authentication, source verification, or a data
redaction guarantee. The optional `CASELIBRARY_ACCESS_PASSWORD` gate is
independent and remains disabled unless separately configured.

## Blocked analysis inputs

When enabled, these POST paths return HTTP 403 with an explanatory response:

- `/ingest` and `/ingest/merge` (case/document content submission)
- `/live-analysis/analyze` and `/live-analysis/resolve` (uploaded documents)
- `/memo-citation-check` (uploaded memo or brief)
- `/api/deidentify`, `/api/reidentify`, and `/api/deidentify/docx` (uploaded or
  pasted text)
- `/research` (free-text research question)

The `/live-analysis`, `/memo-citation-check`, `/deidentify`, and `/research`
pages remain reachable, show a public-data-only explanation, and disable their
analysis controls. Server-side route guards remain authoritative if client-side
profile lookup fails. Page scripts can read the additive profile value from
`window.CASELIBRARY_DEPLOYMENT_PROFILE` after the profile request completes.

Public research remains available, including `/data-explorer`, case browsing
and reading, statute lookup, and the `/search` and `/search/chunks*` routes.
Other POST operations not accepting document or free-text analysis inputs,
including citation-metric recomputation and saved-search operations, are not
disabled by this profile.

## Profile status

`GET /api/deployment-profile` returns:

```json
{
  "public_data_only": true,
  "public_data_only_env": "CASELIBRARY_PUBLIC_DATA_ONLY"
}
```

`GET /health` preserves its existing `message` field and adds the same object
under `deployment_profile`. Treat this as an operational status signal, not an
access-control boundary. The deployment profile is centralized in
[`backend/deployment_profile.py`](../backend/deployment_profile.py); route
classification and guard coverage are exercised by
[`tests/test_deployment_profile.py`](../tests/test_deployment_profile.py).
