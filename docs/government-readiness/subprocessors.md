# Third-party services and subprocessors

This is an inventory of services directly indicated by the requested runtime,
page, and workflow sources. It is not a contract or complete supplier
assessment. “Data sent” describes the code path, not provider-side handling.
All locations are **to verify** because the inspected code does not pin a
processing region.

| Service | Purpose | Data sent or exposed | Location |
| --- | --- | --- | --- |
| OpenAI API | Explicitly enabled query embeddings; `/research` answer generation when hosted generation is selected; explicitly invoked paragraph assessment/segmentation and other evaluation scripts. | Search query text for embeddings only if `QUERY_EMBEDDING_PROVIDER=openai`; for `/research`, question and retrieved case excerpts; for build-time calls, selected case paragraph text and prompt metadata. | **To verify.** The code uses the SDK default endpoint and configures no region or data residency setting. |
| Cloudflare Tunnel | Relays external application traffic to the loopback-hosted application when the tunnel is used. | Application requests and responses routed through the configured tunnel, potentially including uploaded memo content submitted to that app. The checked-in script does not establish provider-side inspection, logging, or retention. | **To verify.** Tunnel configuration is local and the code does not select a region. |
| Google Fonts | Supplies font CSS/assets directly to the browser on pages that include the external stylesheet. | Browser asset request and associated network metadata. No application code appends search queries or uploaded content to the font URL. | **To verify.** No region is pinned in the page code. |
| unpkg | Supplies the Lucide JavaScript asset requested by the citation-map page. | Browser asset request and associated network metadata. No application payload is included in the static asset URL. | **To verify.** No region is pinned in the page code. |
| GitHub repository and Actions | Stores repository changes and runs CI workflows on pushes and pull requests. | Repository contents and commit metadata; Actions checks out the repository and emits workflow output/logs. Do not put case records, memo files, generated assessment files, secrets, or other sensitive material into the repository or workflow artifacts. | **To verify.** Workflow source does not establish repository region or log/artifact retention settings. |

## Local/optional model endpoint

Ollama is an optional text-generation provider. The default base URL is
`http://127.0.0.1:11434/v1`, and the application transforms this to Ollama's
local `/api/chat` endpoint. An operator can configure a different URL, so
confirm the actual endpoint before treating the path as local. [backend/text_generation_providers.py:11-12](../../backend/text_generation_providers.py#L11-L12)
[backend/text_generation_providers.py:40-65](../../backend/text_generation_providers.py#L40-L65)
[backend/text_generation_providers.py:77-95](../../backend/text_generation_providers.py#L77-L95)

## Scope notes

- These paths do not prove the live PC uses any particular service or
  configuration.
- External source-acquisition and other one-off evaluation scripts may contact
  additional services when run. Review their specific command and data inputs
  before use; this table does not inventory every external website or dataset.
- Confirm provider contracts, processing location, logging, retention, support
  access, and any departmental approval with the relevant provider and service
  owner.
- Live machine checks are listed in the
  [verification register](README.md#live-pc-verification-register).
