---
title: GOC Network principles/future considerations
---
# Technical Readiness Report: Migrating an External Intelligence-Gathering Website into CBSA / Government of Canada Infrastructure

## 1\. Executive determination and immediate blockers

**The site is not presently ready for protected, personal, authenticated or transactional use.** Enterprise material associated with the project explicitly says that the current prototype has no authentication or application-level access control and is not ready for deployment involving protected or sensitive material; it also calls for formal security, privacy, information-management, legal, accessibility and technology reviews before broader use. The related deployment package describes a FastAPI/React/PostgreSQL/Azure-oriented implementation and CI/CD configuration, but that package is project evidence—not proof that those technologies are CBSA-approved standards.

The decisive GoC acceptance sequence is:

1. **Define mandate and business use.**

2. **Categorize confidentiality, integrity and availability (CIA)** using the highest injury level across all information and business processes.

3. **Select and tailor the applicable control profile.**

4. **Complete privacy, architecture, accessibility, legal and security design reviews.**

5. **Implement and independently assess controls.**

6. **Produce a remediation plan for deficiencies.**

7. **Obtain an explicit authorization decision before operation.**

8. **Continuously monitor and maintain the authorization state.**

This sequence is directly reflected in the GC cloud security risk-management process and in the Cyber Centre’s current medium-impact control profile.

### Mandatory migration blockers

| Blocker                                                 | Why it blocks acceptance                                                                              | Required disposition                                                              |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| No accepted security categorization                     | Hosting and control requirements cannot be selected without CIA injury ratings                        | Business-owner-approved categorization report                                     |
| Unconfirmed legal authority for intelligence collection | “Publicly available” does not eliminate Privacy Act, platform-terms, copyright or mandate constraints | Legal/privacy collection authority and source register                            |
| No verified CBSA authorization package                  | Deployment does not equal authorization                                                               | Security plan, assessment report, residual-risk decision and signed authorization |
| No approved hosting/network pattern                     | Public cloud, GC cloud, SSC-hosted and departmental platforms have different control inheritance      | CBSA/SSC hosting decision and responsibility matrix                               |
| No proven IAM model                                     | Current prototype lacks authentication/access control                                                 | Workforce/public identity architecture, MFA and authorization model               |
| No evidence of operational controls                     | Logging, incident response, patching, recovery and support must operate after launch                  | SIEM onboarding, runbooks, monitoring, backup/restore and support evidence        |
| Accessibility and bilingual design not demonstrated     | CBSA is in scope for [Canada.ca](http://Canada.ca) design and accessibility obligations               | EN/WCAG testing, bilingual content and accessibility acceptance                   |
| Public-source data not governed                         | Collection can create personal-information holdings and intelligence-derived records                  | Privacy protocol/PIA, PIB decision, provenance and retention rules                |

**Do not build one undifferentiated platform intended to “turn on Protected B later.”** Build reusable components, but isolate trust zones, identities, data stores, keys, pipelines and environments so that a future protected/transactional capability can be separately categorized, assessed and authorized.

---

## 2\. Authoritative hierarchy and applicability

| Level                               | Instrument                                                                                                                                                                                                                     | Status and relevance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Statutes/regulations                | Privacy Act and Regulations; Official Languages Act and Regulations; Accessible Canada Act and Regulations; Copyright Act; Library and Archives of Canada Act; Financial Administration Act; CBSA enabling/program legislation | **Binding**, subject to exact program and information use. The Privacy Act limits collection to information directly related to an operating program/activity and regulates administrative use, accuracy, retention and access rights. [\[](https://justice.canada.ca/eng/csj-sjc/pa-lprp/pa-lprp.html)[justice.canada.ca](http://justice.canada.ca)[\]](https://justice.canada.ca/eng/csj-sjc/pa-lprp/pa-lprp.html), [\[](https://www.canlii.org/en/ca/laws/stat/rsc-1985-c-p-21/latest/rsc-1985-c-p-21.html)[canlii.org](http://canlii.org)[\]](https://www.canlii.org/en/ca/laws/stat/rsc-1985-c-p-21/latest/rsc-1985-c-p-21.html) No government record may be disposed of without the required LAC authority. [\[laws-lois....](https://laws-lois.justice.gc.ca/eng/acts/L-7.7/section-12.html)[tice.gc.ca](http://tice.gc.ca)[\]](https://laws-lois.justice.gc.ca/eng/acts/L-7.7/section-12.html) |
| Treasury Board policies             | Policy on Government Security; Policy on Service and Digital; Policy on Privacy Protection; communications/federal-identity policy                                                                                             | **Mandatory for in-scope federal institutions.** The Policy on Service and Digital integrates service, data, IT and cyber-security management; the current policy and directive were modified August 29, 2025.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Directives and mandatory procedures | Directive on Security Management; Directive on Service and Digital; Directive on Privacy Practices; Directive on Automated Decision-Making; communications/web procedures                                                      | **Mandatory where applicable.** Security Management includes mandatory IT-security, event-management, information-security, contract-security, categorization and continuity procedures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Standards                           | Security Categorization; Systems that Manage Information and Data; Metadata; Web Accessibility; [Canada.ca](http://Canada.ca) external-web specifications; APIs; cloud guardrails                                              | **Mandatory within stated scope.** Systems managing information/data must support auditable retention/disposition, metadata, taxonomies, interoperability, open-format export and secure management.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Cyber Centre profiles/guidance      | ITSG-33 and successor lifecycle material; ITSP.10.033 catalogue; medium-impact profile; cloud, authentication, zoning, cryptography and website guidance                                                                       | Generally **authoritative security guidance used to implement policy**, then tailored by departmental authorities. The April 2, 2026 medium-impact profile supersedes the old ITSG-33 Annex 4A Profile 1 PBMM profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Industry specifications             | CAN/ASC–EN 301 549:2024, WCAG, OWASP ASVS/WSTG/API guidance, SBOM formats                                                                                                                                                      | Mandatory only when incorporated by law/policy/contract; otherwise strong implementation evidence. OWASP ASVS 5.0 provides testable application-security requirements. [\[](https://owasp.org/www-project-application-security-verification-standard/)[owasp.org](http://owasp.org)[\]](https://owasp.org/www-project-application-security-verification-standard/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Currency warning

Do not use the legacy ITSG-33 **Protected B / Medium Integrity / Medium Availability Annex 4A Profile 1** as the sole baseline. The Cyber Centre’s April 2026 medium-impact profile expressly supersedes it and requires organizational tailoring; it does not automatically cover sophisticated state actors. ITSG-33 concepts and control families remain relevant, but the project should ask CBSA which current departmental profile, overlays and assurance level apply.

---

## 3\. Verified CBSA-specific findings versus unresolved internal requirements

### Verified from public CBSA sources

- CBSA states that its websites and applications are being aligned with the Accessible Canada Act, its regulations and **CAN/ASC–EN 301 549:2024**, alongside the TBS web-accessibility standard and accessible-IT guidance. [\[](https://www.cbsa-asfc.gc.ca/accessibility-accessibilite/statement-enonce-eng.html)[cbsa-asfc.gc.ca](http://cbsa-asfc.gc.ca)[\]](https://www.cbsa-asfc.gc.ca/accessibility-accessibilite/statement-enonce-eng.html)

- CBSA publicly publishes PIAs for applications and intelligence-related programs. Recent CBSA PIA material identifies controls such as secure transmission/storage, role-based profiles, accuracy measures and updated PIBs as mitigations for automated information exchange. [\[](https://www.cbsa-asfc.gc.ca/agency-agence/reports-rapports/pia-efvp/atip-aiprp/pias-sefp-eng.html)[cbsa-asfc.gc.ca](http://cbsa-asfc.gc.ca)[\]](https://www.cbsa-asfc.gc.ca/agency-agence/reports-rapports/pia-efvp/atip-aiprp/pias-sefp-eng.html), [\[](https://www.cbsa-asfc.gc.ca/agency-agence/reports-rapports/pia-efvp/atip-aiprp/inssp-pfsni-eng.html)[cbsa-asfc.gc.ca](http://cbsa-asfc.gc.ca)[\]](https://www.cbsa-asfc.gc.ca/agency-agence/reports-rapports/pia-efvp/atip-aiprp/inssp-pfsni-eng.html)

- CBSA’s public terms treat IP addresses as personal information in context, require personal-information collection statements for submitted information, document analytics/retention practices, and recognize official-language, accessibility and copyright obligations.

- CBSA has a departmental cloud migration strategy and action plan supporting transition to end-state data centres and cloud computing. [\[](https://www.cbsa-asfc.gc.ca/agency-agence/reports-rapports/fs-ef/2025/it-ti-proj-eng.html)[cbsa-asfc.gc.ca](http://cbsa-asfc.gc.ca)[\]](https://www.cbsa-asfc.gc.ca/agency-agence/reports-rapports/fs-ef/2025/it-ti-proj-eng.html)

- Public CBSA systems demonstrate use of cloud-hosted domains and external identity services, but these examples **do not establish a mandatory product or architecture for this application**. [\[ccp-pcc.cb....](https://ccp-pcc.cbsa-asfc.cloud-nuage.canada.ca/en/cbsa-homepage)[canada.ca](http://canada.ca)[\]](https://ccp-pcc.cbsa-asfc.cloud-nuage.canada.ca/en/cbsa-homepage), [\[](https://www.canada.ca/en/border-services-agency/services/carm-portal-help.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/border-services-agency/services/carm-portal-help.html)

### Enterprise evidence

[Canadian Immigration Knowledge Repository.docx](https://onedrive.live.com/personal/f25d9e6d04142053/_layouts/15/doc.aspx?resid=aa8c8196-573d-45d2-94b7-821fba708d14&cid=f25d9e6d04142053&EntityRepresentationId=f651e212-6a43-4dc6-b8f0-cee35594c4c9) is primarily a source-collection design and does not establish official CBSA platform standards. It is useful only insofar as it recognizes security/operational constraints around external APIs, protected information and CBSA internal material.

Technical Implementation Design Document.docx is relevant to readiness because it records the prototype’s present limitations and required review areas, but it is not an approved CBSA security standard. CBSA MVP Deployment Package – Local & Azure (Container Apps) PDF provides implementation detail for a candidate stack and deployment automation; it must not be interpreted as CBSA platform approval.

**No authoritative internal CBSA onboarding standard, approved technology catalogue, network-zone diagram, ATO workflow, SIEM schema, vulnerability SLA or release procedure was verified from the available enterprise material.** Those items are therefore explicitly open below.

---

## 4\. Target architecture and trust model

!

### Recommended technology-neutral structure

1. **Public edge**

   - Authoritative DNS, approved certificates and TLS configuration.

   - DDoS protection, reverse proxy, WAF and load balancing.

   - Deny direct Internet access to application nodes and data services.

   - API gateway for Internet-facing APIs; GC guidance states that Internet-facing APIs must use gateways/proxies and retain API-level defence in depth.

2. **Presentation tier**

   - Stateless public UI or backend-for-frontend.

   - No database credentials in browsers; strict CSP, HSTS, secure headers, secure/HttpOnly/SameSite cookies and CSRF protections.

   - Separate public and administrative routes; no administrative console on the normal public entry path.

3. **API/business-services tier**

   - Central authorization enforcement plus object/function-level checks in each service.

   - Contract-first APIs, schema validation, bounded payloads, idempotency for transactions and explicit version/deprecation policy.

   - API gateway performs throttling, initial authentication, payload screening and request logging; backend services remain responsible for fine-grained authorization.

4. **Acquisition/ingestion tier**

   - Separate outbound acquisition workers and queues.

   - Approved source allow-list; forward proxy or controlled egress; DNS and IP validation to prevent SSRF.

   - Fetch-size/time limits, content-type verification, decompression limits, malware scanning, quarantine and parser sandboxing.

   - Store source URL, retrieval time, licence/terms status, content hash, collector version and transformation lineage.

5. **Data tier**

   - Separate raw evidence, normalized records, derived indexes and operational metadata.

   - Encrypt in transit and at rest; use managed keys/secrets with rotation and access auditing.

   - Classification and retention attributes travel with records.

   - Do not mix public-source raw data, protected operational data and production audit logs in a single undifferentiated store.

6. **Management/security plane**

   - Workforce SSO/MFA, privileged-access controls, managed administrative devices and dedicated management entry.

   - Centralized logs/SIEM, vulnerability/configuration monitoring and trusted time.

   - Immutable deployment artefacts and configuration-controlled infrastructure as code.

   - Encrypted backups, geographically appropriate separation and tested restoration.

**CBSA/SSC must determine the actual products, network zones, ingress/egress services, certificate authority, DNS domain, identity provider, key service, log destination and hosting platform.**

---

## 5\. Cybersecurity engineering baseline

### Categorization, assessment and authorization

Prepare a categorization report covering every business process and information type. Apply the **high-watermark** rule independently to confidentiality, integrity and availability; adding personal information, enforcement intelligence or transactions can raise one or more dimensions even if public content remains unchanged. Select CBSA’s current control profile and document every inherited, shared, implemented, tailored and not-applicable control. [\[](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/cloud-security-risk-management-approach-procedures.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/cloud-security-risk-management-approach-procedures.html)

The minimum authorization evidence should include:

- system boundary and context/data-flow diagrams;

- asset, software, API, dependency and external-connection inventories;

- security categorization and threat/risk assessment;

- system security/privacy plan and control traceability matrix;

- assessment plan and security assessment report;

- penetration-test and vulnerability results;

- PIA/privacy protocol and PIB decision;

- remediation **Plan of Action and Milestones**;

- residual-risk statement and authorization letter;

- continuous-monitoring strategy and authorization-maintenance triggers.

The current medium-impact profile selects independent control assessment, authorization before operation, PoAM management and continuous monitoring; penetration testing remains a control to select based on organizational tailoring rather than an automatic universal frequency.

### Secure SDLC and supply chain

Implement protected branches, mandatory peer review, signed and immutable releases, isolated build identities, short-lived CI credentials, least-privilege runners and separation between code approval and production deployment. Pipeline gates should include secret scanning, SAST, SCA/licence checking, container/IaC scanning, DAST against a representative environment and manual testing for authorization and business logic.

Generate an SBOM for each releasable artefact, retain dependency hashes and build provenance, and sign release artefacts where the approved CBSA toolchain supports it. Cyber Centre guidance recommends SBOMs for software producers, purchasers and operators and identifies them as a means to understand components, vulnerabilities and supply-chain risk. These are **recommended unless CBSA’s profile or procurement terms make them mandatory**.

Use OWASP ASVS as the application-verification matrix, supplemented by the WSTG and API testing. Specifically test injection, XSS, broken object/function authorization, authentication recovery, session fixation, CSRF, unsafe deserialization, SSRF, path traversal, file handling, template injection, request smuggling, cache confusion, mass assignment, GraphQL/API abuse and business-process bypass. [\[](https://owasp.org/www-project-application-security-verification-standard/)[owasp.org](http://owasp.org)[\]](https://owasp.org/www-project-application-security-verification-standard/), [\[](https://wstg.owasp.org/)[wstg.owasp.org](http://wstg.owasp.org)[\]](https://wstg.owasp.org/)

### Vulnerability and operations controls

Maintain complete asset/component inventories, hardened baselines, patch and exception records, authenticated infrastructure scanning and unauthenticated external scanning. The Cyber Centre describes patching as a top security action and requires testing, change management, deployment and verification rather than merely receiving vendor advisories.

Centralize authentication, authorization, administrative, configuration, data-export, ingestion, security and transaction events. Logs should identify event type, UTC time, source, outcome and relevant actor/object without unnecessarily duplicating personal or secret data. The medium profile requires protected audit information, central review/correlation, logging-failure alerts and retention aligned to records policy.

---

## 6\. Public-information intelligence collection

**Public availability is not blanket permission to collect or operationalize information.** TBS’s implementation notice, effective May 28, 2025, says publicly available personal information should generally be treated like other personal information; collection still requires legal authority and direct relationship to an operating program/activity. [\[](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/privacy-implementation-notice-2023-03.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/privacy-implementation-notice-2023-03.html)

Before enabling each source:

1. Record owner, URL/API, terms, licence, authentication method, robots indication, collection method, rate limits and permitted purpose.

2. Prefer an official API or licensed data feed over scraping.

3. Obtain legal review for terms that prohibit automated collection, government use, surveillance or intelligence gathering.

4. Do not treat leaked, hacked or inadvertently disclosed data as legitimately public.

5. Minimize collection parameters and dispose of overcollected data.

6. Preserve source/date/hash and confidence; corroborate consequential information.

7. Segregate raw acquisition from analyst-curated or decision-support records.

8. Establish correction, deletion, retention and source-removal procedures.

TBS specifically warns that platform terms may prohibit government intelligence collection, that copyright and technological-protection-measure issues may arise, and that public-source personal information generally should not be the sole basis for an administrative decision. The Open Government Licence permits broad reuse with attribution but excludes personal information, third-party rights, official symbols and other protected IP. [\[](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/privacy-implementation-notice-2023-03.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/privacy-implementation-notice-2023-03.html) [\[](https://open.canada.ca/en/open-government-licence-canada)[open.canada.ca](http://open.canada.ca)[\]](https://open.canada.ca/en/open-government-licence-canada)

For non-administrative trend/research use involving personal information, create a **privacy protocol**. For administrative use or decisions affecting individuals, a PIA is required; a PIB may also be required where information is used administratively or retrieved by personal identifier.

---

## 7\. Privacy, identity and future transactions

### Privacy transition model

| Evolution stage                         | Privacy/security consequence                                                                                               |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Public factual content only             | Still govern source terms, copyright, integrity, retention and security logs                                               |
| Publicly available personal information | Privacy protocol or PIA analysis; minimization, access restriction, provenance and safeguards                              |
| Protected/personal operational data     | Re-categorization, PIB/PIA, protected hosting, stronger access/audit/retention and breach controls                         |
| Administrative decision support         | Accuracy, direct-collection exceptions, review/correction opportunities and potentially automated-decision requirements    |
| Transactions                            | Identity assurance, authorization, non-repudiation, fraud controls, transaction recovery and financial/legal recordkeeping |

The current privacy standard requires a documented Privacy Checklist before a new or substantially modified activity involving personal information. It requires a PIA before administrative use, major IT/process changes, third-party involvement or covered automated decision systems; approved PIAs go to TBS and OPC, receive a public summary, and have mitigation measures reviewed annually.

### IAM

Maintain distinct identity realms and policies for:

- **Workforce users:** departmental federation/SSO, MFA, managed-device and screening requirements, RBAC/ABAC, joiner-mover-leaver automation and periodic access review.

- **Privileged administrators:** separate named admin accounts, phishing-resistant/strong MFA, dedicated admin path/device, just-in-time elevation, session logging and break-glass governance.

- **Public/external users:** identity assurance proportionate to the transaction, minimal attributes, secure recovery, anti-enumeration and step-up authentication for sensitive actions.

- **Workloads:** unique service identities, mutual authentication where appropriate, short-lived credentials, scoped permissions and no static secrets in source or images.

The 2026 medium profile selects MFA for privileged and non-privileged organizational accounts, SSO, replay-resistant authentication and identity-proofing controls, but exact CBSA technologies remain to be confirmed. Cloud direction requires privileged MFA and alignment with GC identity/authentication services. [\[](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/direction-secure-use-commercial-cloud-services-spin.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/direction-secure-use-commercial-cloud-services-spin.html)

---

## 8\. Web, accessibility, languages and information management

CBSA is listed as subject to the [Canada.ca](http://Canada.ca) design requirements for all public-facing websites and digital services, regardless of domain, technology or publishing platform. Use the [Canada.ca](http://Canada.ca) Content and Information Architecture Specification, content style guide, federal identity elements and required global/contextual notices. WET is encouraged and helps with responsive and accessible implementation, but use of WET does not by itself prove conformance. [\[](https://design.canada.ca/specifications/usage-canadaca-design/institutions-list.html)[design.canada.ca](http://design.canada.ca)[\]](https://design.canada.ca/specifications/usage-canadaca-design/institutions-list.html)

For public pages, test complete user processes against the currently applicable TBS accessibility standard and CBSA’s stated EN 301 549 direction. The existing TBS standard requires WCAG 2.0 Level AA for in-scope public pages; newer Accessible Canada Regulations establish December 5, 2027 requirements for new/updated public-sector employee- and non-employee-facing web pages to meet specified EN 301 549 clauses. Design to the newer requirement now rather than planning a later retrofit.

Provide English and French of equal quality where official-language obligations apply, including navigation, errors, notifications, help, privacy statements and transactional correspondence. Internal applications may be out of scope for [Canada.ca](http://Canada.ca) visual design, but accessibility, language-of-work/service and security/privacy duties can still apply.

Information systems must support auditable retention/disposition, metadata, enterprise taxonomies, interoperability and open-format export. Do not delete scraped records, logs or derived intelligence solely because an application retention timer expires; disposition must align with an approved records-disposition authority and the Library and Archives of Canada Act. [\[laws-lois....](https://laws-lois.justice.gc.ca/eng/acts/L-7.7/section-12.html)[tice.gc.ca](http://tice.gc.ca)[\]](https://laws-lois.justice.gc.ca/eng/acts/L-7.7/section-12.html)

---

## 9\. Phased migration and acceptance roadmap

| Phase                               | Engineering and evidence                                                                                         | Gate / likely reviewers                                                  |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| 1\. Scope and triage                | Mandate, source inventory, data flows, information types, current security scan, dependency inventory            | Business owner; CBSA legal/privacy/security                              |
| 2\. Categorization and architecture | CIA report, BIA, target architecture, hosting decision, control-profile tailoring, threat model                  | Business owner; departmental security/architecture; SSC where applicable |
| 3\. Privacy/content design          | Privacy Checklist, protocol/PIA, PIB analysis, source terms/licences, retention schedule, bilingual content plan | CBSA ATIP/privacy, legal, IM and communications                          |
| 4\. Platform onboarding             | Landing zone/account, network flows, DNS/TLS, IAM, keys, logging, backups, guardrails and IaC                    | CBSA platform/network/security; SSC                                      |
| 5\. Secure implementation           | CI/CD controls, SAST/SCA/DAST, SBOM, API/WAF controls, hardening, test environments                              | Development, platform and security assessors                             |
| 6\. Verification                    | Functional, accessibility, bilingual, load, recovery, penetration and incident-response testing                  | Independent security assessor; accessibility/content reviewers           |
| 7\. Authorization                   | Security assessment report, PoAM, residual risk, operating procedures and signed authorization                   | Named CBSA authorizing official—confirm internally                       |
| 8\. Production readiness            | Support model, SLOs, alert routing, service desk, runbooks, rollback, change calendar                            | Service owner, operations, SOC/SIEM and change authority                 |
| 9\. Continuous operation            | Patching, access recertification, control monitoring, PIA updates, restore tests and authorization maintenance   | Service owner, security/privacy/IM/platform functions                    |

For cloud, GC guardrails are required controls. SSC states that applicable Azure, AWS and GCP environments must use its Compliance-as-Code package, while new cloud accounts must achieve guardrail compliance within 30 business days. [\[hosting-se....](https://hosting-services-hebergement.canada.ca/s/security-compliance?language=en_US)[canada.ca](http://canada.ca)[\]](https://hosting-services-hebergement.canada.ca/s/security-compliance?language=en_US)

---

## 10\. Implementation checklist

| Area                   | Implement / retain as evidence                                          | Source and classification                                                                                                                                                                                                                                                                                                                                                                                              | Trigger                  | Status |
| ---------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------ |
| Mandate                | Approved purpose, legal authorities, permitted intelligence uses        | Privacy Act/TBS; **GoC mandatory** [\[](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/privacy-implementation-notice-2023-03.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/privacy-implementation-notice-2023-03.html) | Any collection           | ☐      |
| Categorization         | CIA injury assessment and signed high-watermark report                  | TBS/Cyber; **mandatory** [\[](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/cloud-security-risk-management-approach-procedures.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/cloud-security-risk-management-approach-procedures.html)               | Before hosting selection | ☐      |
| Control profile        | Current CBSA profile, tailoring rationale, inheritance matrix           | Cyber; **mandatory process**                                                                                                                                                                                                                                                                                                                                                                                           | All GC operation         | ☐      |
| Authorization          | Assessment report, PoAM, residual-risk acceptance, authorization letter | TBS/Cyber; **mandatory** [\[](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/direction-secure-use-commercial-cloud-services-spin.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/direction-secure-use-commercial-cloud-services-spin.html)             | Before production        | ☐      |
| Privacy                | Privacy Checklist; protocol/PIA; mitigation tracking                    | TBS; **conditional mandatory**                                                                                                                                                                                                                                                                                                                                                                                         | Personal information     |        |
| PIB                    | Create/update PIB where administratively used or identifier-retrievable | TBS; **conditional mandatory**                                                                                                                                                                                                                                                                                                                                                                                         | Applicable holdings      |        |
| Public sources         | Source/terms/licence register, legal review, provenance                 | TBS; **mandatory/strong guidance** [\[](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/privacy-implementation-notice-2023-03.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/treasury-board-secretariat/services/access-information-privacy/access-information-privacy-notices/privacy-implementation-notice-2023-03.html) | Automated collection     |        |
| Architecture           | Boundaries, flows, zones, external interfaces, admin path               | Cyber; **control evidence**                                                                                                                                                                                                                                                                                                                                                                                            | All deployments          |        |
| Cloud                  | Guardrails, Compliance-as-Code, responsibility matrix                   | TBS/SSC; **conditional mandatory**                                                                                                                                                                                                                                                                                                                                                                                     | Cloud                    |        |
| IAM                    | SSO/federation, MFA, least privilege, lifecycle and reviews             | Cyber/TBS; **profile-dependent**                                                                                                                                                                                                                                                                                                                                                                                       | Authentication           |        |
| APIs                   | Gateway, schema validation, rate limiting, auth and audit               | GC API guidance; **Internet-facing mandatory gateway**                                                                                                                                                                                                                                                                                                                                                                 | Exposed API              |        |
| SDLC                   | Reviews, scans, release evidence, separation of duties                  | Cyber/OWASP; **recommended/profile-tailored**                                                                                                                                                                                                                                                                                                                                                                          | Code changes             |        |
| Supply chain           | Dependency inventory, SBOM, provenance/signing                          | Cyber; **recommended unless mandated**                                                                                                                                                                                                                                                                                                                                                                                 | Built/procured software  |        |
| Logging                | UTC event logs, SIEM export, access controls and alert tests            | Cyber; **profile control**                                                                                                                                                                                                                                                                                                                                                                                             | Operational system       |        |
| Vulnerabilities        | Scan, patch, exception and remediation records                          | Cyber; **profile/operational control**                                                                                                                                                                                                                                                                                                                                                                                 | Continuous               |        |
| Recovery               | BIA-derived RTO/RPO, encrypted backups and restore evidence             | Cyber; **profile control**                                                                                                                                                                                                                                                                                                                                                                                             | Stateful/critical        |        |
| Accessibility          | EN/WCAG conformance report, manual assistive-tech tests                 | GoC/CBSA; **mandatory/dated trigger**                                                                                                                                                                                                                                                                                                                                                                                  | Web/app update           |        |
| Languages/design       | EN/FR parity, [Canada.ca](http://Canada.ca) templates/notices           | GoC; **public-facing mandatory**                                                                                                                                                                                                                                                                                                                                                                                       | Public service           |        |
| Information management | Metadata, retention/disposition, export and deletion audit              | GoC; **mandatory**                                                                                                                                                                                                                                                                                                                                                                                                     | Government records       |        |
| Operations             | Runbooks, ownership, SLOs, escalation, change and decommission plan     | Cyber/TBS; **profile-tailored** [\[](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/cloud-security-risk-management-approach-procedures.html)[canada.ca](http://canada.ca)[\]](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/cloud-services/cloud-security-risk-management-approach-procedures.html)        | Production               |        |

---

## 11\. Questions requiring authoritative CBSA/SSC answers

 1. What is the official **application intake/onboarding process**, system of record and required gates?

 2. Which CBSA security categorization methodology and current control profile/overlays must be used?

 3. Who is the business risk owner, security assessor and authorizing official?

 4. Is the required outcome called SA&A, authorization to operate, interim authorization or another CBSA term?

 5. Which hosting patterns are approved: SSC data centre, departmental cloud, GC cloud marketplace, or a specific platform?

 6. What are the approved regions and data-location, replication, backup and support-location constraints?

 7. Which network zones, ingress/WAF/DDoS, egress proxy and private-connectivity services are mandatory?

 8. Which domains, DNS, certificate authority and TLS baselines apply?

 9. Which workforce and public identity providers, assurance levels and MFA methods are approved?

10. What secrets/key-management and cryptographic-module requirements apply?

11. Which SIEM, log schema, retention periods and alert-routing rules are mandatory?

12. What vulnerability-remediation SLAs, scanning tools and penetration-test independence/frequency apply?

13. Which source repositories, CI/CD runners, artifact registries, container platforms and IaC tools are approved?

14. What branch protections, SBOM, code-signing and provenance requirements are mandatory?

15. What are the release/change records, emergency-change process and production-access restrictions?

16. Which accessibility test standard and acceptance authority will CBSA use before December 5, 2027?

17. What privacy protocol/PIA/PIB applies to this public-source intelligence activity and its future uses?

18. What approved source-collection policy governs attributable/non-attributable accounts, scraping and intelligence mandates?

19. What records-disposition authority and retention periods apply to raw captures, derived records and audit logs?

20. What SLO, DR tier, RTO/RPO, service-desk and operational-ownership model will CBSA require?

## Overall readiness conclusion

The project can be engineered for a smooth migration, but **“CBSA-ready” is an evidence and authorization state, not a hosting location**. The strongest design is a modular, API-based, zone-separated platform with a dedicated acquisition boundary, explicit information lineage, externalized identity, centralized controls and independently deployable public versus protected capabilities. Migration should begin with the current public-information function, but the target design must prevent that low-sensitivity authorization from being silently reused for personal, protected, intelligence-decision or transactional workloads.

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBTGl0SW50ZWxwcm9qZWN0JTNBJTNBZ3JleXN0b25lLWRhbg==" repo-name="LitIntelproject"><sup>Powered by [Swimm](https://app.swimm.io/)</sup></SwmMeta>
