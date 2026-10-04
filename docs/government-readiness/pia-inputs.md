# PIA fact sheet inputs

This sheet records facts that can be gathered from the repository and questions
for the assessment owner. It makes no legal conclusion about whether a PIA is
required, which law or policy applies, or whether any use is approved.

## System and purpose

| Fact-sheet field | Repository evidence or open question |
| --- | --- |
| System | FastAPI legal research application with PostgreSQL/pgvector storage and browser interfaces. Database connection settings are environment-configured. [SYSTEM_REFERENCE.md:71-83](../../SYSTEM_REFERENCE.md#L71-L83) [backend/database.py:61-78](../../backend/database.py#L61-L78) |
| Purpose described in code | Search and research over stored Canadian decisions and statutes; memo-citation-check compares citations in an uploaded draft with stored local authorities. [backend/search_service.py:1-4](../../backend/search_service.py#L1-L4) [backend/memo_citation_check.py:102-119](../../backend/memo_citation_check.py#L102-L119) |
| Intended departmental use | **To be supplied by the department.** The repository does not establish the sponsor's purpose, authority, user population, or approval. |
| Deployment | The repository contains a local-workstation/tunnel deployment path; this does not prove the live PC's location, configuration, or actual network path. [scripts/service/run_site.ps1:22-27](../../scripts/service/run_site.ps1#L22-L27) [docs/LOCAL_DEPLOYMENT_SETUP.md:101-117](../LOCAL_DEPLOYMENT_SETUP.md#L101-L117) |

## Personal information and data subjects

| Data or person | Repository fact | Assessment input still needed |
| --- | --- | --- |
| People named or described in decisions | Stored decisions can include full text, source HTML, docket number, summaries, and metadata. [backend/database.py:85-109](../../backend/database.py#L85-L109) | Identify the categories of personal information actually present in the corpus, whether minors or vulnerable persons occur, and whether records are redacted or restricted at source. |
| People whose matters are searched | Search queries can contain names, case details, or matter context. API search defaults to lexical; query embeddings are disabled by default. OpenAI receives search query text only when an operator explicitly enables `ENHANCED_AI_MODE=hosted` and `QUERY_EMBEDDING_PROVIDER=openai`; local mode permits only local inference. [backend/ai_mode.py](../../backend/ai_mode.py) [backend/query_embedding_providers.py](../../backend/query_embedding_providers.py) [backend/search_service.py](../../backend/search_service.py) | Determine what users are instructed to enter, whether queries can identify clients or third parties, and whether a department-specific prohibition or notice is needed. |
| People mentioned in uploaded memos | The memo-check endpoint accepts a document and analyzes citations; the upload is not written as an application-managed record by the inspected handler. [backend/routes.py:1040-1054](../../backend/routes.py#L1040-L1054) | Determine whether the service will receive client, employee, witness, or other personal information and whether the route is in scope for departmental use. |
| User/request information | Optional audit events contain request metadata and a client-address hash; raw address is opt-in. [backend/audit.py:64-83](../../backend/audit.py#L64-L83) | Identify the live log configuration, access, purposes, and any linkability across other operational records. |

## Collection

- Decision and statute content is ingested through separate source workflows and
  persisted in the configured database. [backend/database.py:85-119](../../backend/database.py#L85-L119)
  [backend/database.py:489-515](../../backend/database.py#L489-L515)
- Users provide search text to application routes. Query embeddings are disabled
  by default, so semantic/hybrid requests use lexical ranking. OpenAI query
  embeddings require explicit provider configuration.
  [backend/query_embedding_providers.py](../../backend/query_embedding_providers.py)
  [backend/search_service.py](../../backend/search_service.py)
- The memo-check page submits a selected DOCX/PDF file to the application's
  `/memo-citation-check` endpoint. [backend/pages/memo_citation_check.py:17-19](../../backend/pages/memo_citation_check.py#L17-L19)
  [backend/routes.py:1040-1047](../../backend/routes.py#L1040-L1047)

**Questions for the sponsor:** Which fields will users enter? Will uploads or
queries include personal/confidential information? What notice, consent,
authority, minimization, and user instructions are required? What is the
approved upload-size and transport boundary?

## Use and access

- Application access can be password-gated when `CASELIBRARY_ACCESS_PASSWORD`
  is non-empty. The code reference does not prove whether this gate or an
  external access control is enabled on the live PC. [backend/main.py:85-105](../../backend/main.py#L85-L105)
  [docs/CONFIGURATION_REFERENCE.md:41-48](../CONFIGURATION_REFERENCE.md#L41-L48)
- Uploaded memo analysis performs deterministic citation extraction and local
  database lookups; it is distinct from AI-generated paragraph assessment.
  [backend/memo_citation_check.py:102-129](../../backend/memo_citation_check.py#L102-L129)
- A separate `/research` feature can send a question and retrieved decision
  excerpts to a hosted or configured local generation provider.
  [backend/routes.py:3851-3903](../../backend/routes.py#L3851-L3903)

**Questions for the sponsor:** Define authorized users, role separation,
administrator access, training, access reviews, use limits, human review, and
whether generated material may be copied into departmental files or decisions.

## Storage, retention, and disposal

| Information | Code-visible storage | Open fact |
| --- | --- | --- |
| Decisions, statutes, derived records, and embeddings | Configured PostgreSQL database. [backend/database.py:75-119](../../backend/database.py#L75-L119) [backend/database.py:489-535](../../backend/database.py#L489-L535) | Live host/region, encryption, backups, retention, deletion, and restoration are unverified. |
| Ordinary request audit events | Optional configured JSON-lines file, 5 MiB rotation and three backups. [backend/audit.py:26-43](../../backend/audit.py#L26-L43) | Live path, activation, permissions, backup, and retention are unverified. |
| Memo uploads and results | No application-managed upload record is created in the inspected handler; the response returns analysis. [backend/routes.py:1040-1054](../../backend/routes.py#L1040-L1054) | Framework temporary storage and deployment/browser copies are not proven absent; deletion and response caching need verification. |
| AI paragraph assessment outputs | Request/response and Markdown files are written to supplied output paths. [scripts/package_discussion_units_llm.py:527-552](../../scripts/package_discussion_units_llm.py#L527-L552) | Operator-selected paths, ACLs, backups, and retention are unverified. |

**Questions for the sponsor:** Set retention and deletion periods for each
source, output, operational log, backup, and temporary copy; identify the
records owner; establish hold/export requirements; and verify deletion and
restore procedures in the actual deployment.

## Disclosure and external processing

- OpenAI receives query text for embeddings only when the operator explicitly
  sets `QUERY_EMBEDDING_PROVIDER=openai`. Optional `/research` generation sends
  the question and retrieved excerpts to the configured provider, which
  defaults to OpenAI.
  [backend/query_embedding_providers.py](../../backend/query_embedding_providers.py)
  [backend/routes.py:3851-3903](../../backend/routes.py#L3851-L3903)
- Build-time paragraph assessment sends selected decision paragraph text to
  OpenAI only when the script is invoked in send mode.
  [scripts/package_discussion_units_llm.py:137-160](../../scripts/package_discussion_units_llm.py#L137-L160)
  [scripts/package_discussion_units_llm.py:391-405](../../scripts/package_discussion_units_llm.py#L391-L405)
- Cloudflare Tunnel relays traffic when configured. Google Fonts and unpkg are
  browser asset providers. GitHub receives repository contents and workflow
  activity when repository workflows run.
  [scripts/service/run_site.ps1:48-54](../../scripts/service/run_site.ps1#L48-L54)
  [backend/pages/memo_citation_check.py:10-11](../../backend/pages/memo_citation_check.py#L10-L11)
  [backend/pages/citation_map.py:10-12](../../backend/pages/citation_map.py#L10-L12)
  [.github/workflows/tests.yml:3-5](../../.github/workflows/tests.yml#L3-L5)

**Questions for the sponsor:** Confirm which flows are in scope, the actual
providers and endpoints, regions, contractual terms, support access, provider
logs/retention, and any required notice or approval. The code does not determine
any of those provider facts.

## Safeguards and assessment follow-up

The application has an optional password gate, bounded upload/parser limits,
and an optional request-audit log. These are implementation facts, not a
conclusion that the full system is secure or fit for a particular information
class. [backend/main.py:85-105](../../backend/main.py#L85-L105)
[backend/resource_limits.py:25-36](../../backend/resource_limits.py#L25-L36)
[backend/audit.py:20-43](../../backend/audit.py#L20-L43)

Before a departmental assessment, identify the accountable privacy/security
owners, confirm data categories and purpose, validate each disclosure/storage
path, assess access and retention controls, and document decisions and residual
questions. This list is not a legal checklist and does not replace departmental
direction.
