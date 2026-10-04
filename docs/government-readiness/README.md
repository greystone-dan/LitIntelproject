# Government-readiness documentation pack

This pack records code-level facts for a security, privacy, and program review.
It is an evidence aid, not a security assessment, Privacy Impact Assessment,
legal opinion, compliance determination, approval, or statement about the
current live deployment.

The issue-referenced background requirements report and always-on PC runbook
were not available in this checkout/session. This pack therefore does not
claim to reconcile their findings. Unknowns are stated as unknown rather than
inferred.

## Documents

| Document | Purpose |
| --- | --- |
| [Data classification](data-classification.md) | Data types, code-visible storage and access boundaries, and proposed sensitivity labels for departmental decision. |
| [Data flow](data-flow.md) | Mermaid view and evidence table for storage, external transfers, and audit logging. |
| [Subprocessors](subprocessors.md) | Observed service providers, purpose, data flow, and location questions. |
| [Logging and retention](logging-and-retention.md) | Application audit fields, rotation, opt-ins, and retention gaps. |
| [PIA inputs](pia-inputs.md) | Fact-sheet inputs and unanswered questions for a privacy assessment. |
| [AI use statement](ai-use-statement.md) | Runtime and build-time model use, generated versus deterministic outputs, and human-review boundaries. |

The repository-based CBSA readiness checklist remains a separate evidence
screen: [readiness checklist](../reports/cbsa-readiness-checklist.md).

## Live-PC verification register

Each item below is not verified by this checkout. Confirm it on the live PC
and with the responsible service/provider owner before relying on it.

1. **LIVE-PC-01 — Current access boundary:** actual `CASELIBRARY_ACCESS_PASSWORD` setting, any proxy/Cloudflare Access policy, reachable routes, account scope, and verification evidence.
2. **LIVE-PC-02 — Database and file storage:** actual database host/path, Windows account and file ACLs, encryption, temporary multipart files, and any filesystem copies.
3. **LIVE-PC-03 — Backups and deletion:** whether backups exist, their locations/regions, access, encryption, retention, restore testing, and deletion schedule.
4. **LIVE-PC-04 — Audit and host logs:** actual audit-log path/flags, process count, directory permissions, Windows/Uvicorn/tunnel/proxy logs, forwarding/monitoring, and their rotation and retention.
5. **LIVE-PC-05 — Tunnel behavior:** current Cloudflare tunnel route and account settings, external access controls, traffic/log visibility, and provider retention.
6. **LIVE-PC-06 — Enabled model paths:** current runtime environment/flags, whether OpenAI or Ollama paths are used, and where any build-time request, response, assessment, and ledger files are written and retained.
7. **LIVE-PC-07 — Browser and GitHub use:** actual pages/clients used, browser/CDN requests, repository visibility, Actions retention, and any artifacts/log access policy.

Provider processing regions, terms, and retention are also unverified; these
require provider and departmental confirmation and are not established merely
by inspecting the PC.

## Evidence limits

Evidence links in this pack point to repository files and line ranges. A
code-level statement describes the checked-in path, not necessarily runtime
configuration, deployed behavior, service-provider practice, or organizational
policy. Sensitivity labels in the classification document are proposals for
the department to decide; they are not determinations.
