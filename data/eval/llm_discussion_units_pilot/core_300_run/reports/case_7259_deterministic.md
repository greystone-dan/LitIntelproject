# Discussion Units: case 7259

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **16**
- Continuity pairs: **15**
- Discussion Units: **2**
- Paragraph source hashes: **16**
- Sub-themes: **5**

## 7259:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ef125121136e4242c54285ee3c28d76130ce04f37e4a629b2886181b675153e5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7259:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, canada, convention, crdd, decision, fear, hands, immigration`
- Display key terms: `convention, crdd, fear, hands`
- Argument roles: `reasoning_application`
- Explanation: Observed roles: reasoning_application Display terms: convention, crdd, fear, hands Application context: On the advice of his father, the applicant went into hiding for fear that MQM-Haqiqi members would try to implicate him in the carnage because of his affiliation with the PML. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4388194` offsets `699-706`; context: On the advice of his father, the applicant went into hiding for fear that MQM-Haqiqi members would try to implicate him in the carnage because of his affiliation with the PML.

#### 7259:1:subtheme:2 · paragraphs 5-6

- Raw key terms: `applicant, crdd, fear, hands, persecution, regarding, above, allegation`
- Display key terms: `crdd, fear, hands, persecution, regarding, above, allegation`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: crdd, fear, hands, persecution, regarding, above, allegation Application context: However, it went on to conclude that, in relation to his fear of persecution at the hands of the MQM-Haqiqi, the applicant had an internal flight alternative to the city of Lahore. | It concludes that they are fraudulent and were provided to embellish the claimant's claim. Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4388196` offsets `51-56`; context: [5] The CRDD, in its decision, essentially took no issue with the credibility of the applicant's testimony regarding his difficulties at the hands of the MQM-Haqiqi.
- Evidence: `evidence_fact` cue `testimony` at chunk `4388196` offsets `97-106`; context: [5] The CRDD, in its decision, essentially took no issue with the credibility of the applicant's testimony regarding his difficulties at the hands of the MQM-Haqiqi.
- Evidence: `reasoning_application` cue `conclude` at chunk `4388196` offsets `189-197`; context: However, it went on to conclude that, in relation to his fear of persecution at the hands of the MQM-Haqiqi, the applicant had an internal flight alternative to the city of Lahore.
- Evidence: `counterargument_limitation` cue `However` at chunk `4388196` offsets `166-173`; context: However, it went on to conclude that, in relation to his fear of persecution at the hands of the MQM-Haqiqi, the applicant had an internal flight alternative to the city of Lahore.
- Evidence: `evidence_fact` cue `evidence` at chunk `4388197` offsets `208-216`; context: [6] In support of his allegation of a well-founded fear of persecution at the hands of authorities in Pakistan, the applicant provided to the CRDD, very shortly before the hearing into his claim, documentary evidence in the form of Arrest Warrants, a Proclamation and a First Information Report.
- Evidence: `reasoning_application` cue `concludes` at chunk `4388197` offsets `987-996`; context: It concludes that they are fraudulent and were provided to embellish the claimant's claim.

#### 7259:1:subtheme:3 · paragraphs 7-11

- Raw key terms: `crdd, evidence, applicant, circumstances, fraudulent, applicant's, application, arrest`
- Display key terms: `crdd, circumstances, fraudulent, applicant's, arrest`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue Display terms: crdd, circumstances, fraudulent, applicant's, arrest Rule/authority context: In the result, the CRDD concluded: In light of the panel's findings regarding the trustworthiness of the documents presented to corroborate the alleged charges against the claimant, and its findings of implausibility reg Operative outcome context: [11] In the result, this application for judicial review will be dismissed. Evidence spans paragraphs 7-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4388198` offsets `392-397`; context: It determined against the reliability of that Report based in part on its conclusion that the Arrest Warrants and Proclamation presented by the applicant were fraudulent and further on the basis that it considered the applicant's testimony regarding the circumstances leading to the issue of
the First Information Report to be implausible.
- Evidence: `evidence_fact` cue `testimony` at chunk `4388198` offsets `339-348`; context: It determined against the reliability of that Report based in part on its conclusion that the Arrest Warrants and Proclamation presented by the applicant were fraudulent and further on the basis that it considered the applicant's testimony regarding the circumstances leading to the issue of
the First Information Report to be implausible.
- Evidence: `governing_rule` cue `under` at chunk `4388198` offsets `702-707`; context: In the result, the CRDD concluded:
In light of the panel's findings regarding the trustworthiness of the documents presented to corroborate the alleged charges against the claimant, and its findings of implausibility regarding the alleged circumstances under which those charges came to be laid, the panel finds that the credible evidence before it has not established, on a balance of probabilities, that there are any charges outstanding against the claimant in Pakistan today.
- Evidence: `issue` cue `issue` at chunk `4388199` offsets `13-18`; context: [8] The only issue raised on behalf of the applicant on this application for judicial review was whether or not the CRDD erred in determining the Arrest Warrants that were before it to be fraudulent on the basis of documentary evidence that, it was urged, was at best ambivalent and unauthoritative.
- Evidence: `evidence_fact` cue `evidence` at chunk `4388199` offsets `227-235`; context: [8] The only issue raised on behalf of the applicant on this application for judicial review was whether or not the CRDD erred in determining the Arrest Warrants that were before it to be fraudulent on the basis of documentary evidence that, it was urged, was at best ambivalent and unauthoritative.
- Evidence: `evidence_fact` cue `evidence` at chunk `4388200` offsets `50-58`; context: [9] The CRDD has wide discretion in the choice of evidence before it on which it chooses to rely.
- Evidence: `evidence_fact` cue `evidence` at chunk `4388201` offsets `64-72`; context: [10] It was not in dispute before me that extensive documentary evidence discloses that fraudulent documentary evidence is reasonably readily available in support of refugee claims and other immigration proceedings originating from Pakistan.
- Evidence: `counterargument_limitation` cue `Notwithstanding` at chunk `4388201` offsets `756-771`; context: Notwithstanding that certain of the independent documentary evidence before the CRDD was perhaps less authoritative than it might have been, in the absence of any evidence on behalf of the applicant to support the authenticity of the documentation that he produced, I am satisfied that the factual finding by the CRDD that the applicant's documentation was not reliable, was reasonably open to it.
- Evidence: `disposition` cue `dismissed` at chunk `4388202` offsets `65-74`; context: [11] In the result, this application for judicial review will be dismissed.

#### 7259:1:subtheme:4 · paragraphs 12-14

- Raw key terms: `april, agreement, alberta, applicant, application, calgary, canada, cause`
- Display key terms: `april, agreement, alberta, calgary`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: april, agreement, alberta, calgary Rule/authority context: Counsel for the respondent urged that the decision under review was fact-driven and raised no question for certification. Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4388203` offsets `73-80`; context: [12] While counsel for the applicant was somewhat equivocal before me on whether or not this application for judicial review raised a serious question of general importance that warranted certifying, he produced no question for certification.
- Evidence: `governing_rule` cue `under` at chunk `4388203` offsets `294-299`; context: Counsel for the respondent urged that the decision under review was fact-driven and raised no question for certification.
- Evidence: `evidence_fact` cue `RECORD` at chunk `4388204` offsets `106-112`; context: FEDERAL COURT OF CANADA TRIAL DIVISION
NAMES OF SOLICITORS AND SOLICITORS ON THE RECORD
COURT FILE NO.

#### Section text

Uddin v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2002-04-26
Neutral citation
2002 FCT 451
File numbers
IMM-895-01
Decision Content
Date: 20020426
Docket: IMM-895-01
Neutral citation: 2002 FCT 451
BETWEEN:
NIZAM UDDIN
Applicant
and
THE MINISTER OF CITIZENSHIP & IMMIGRATION
Respondent
REASONS FOR ORDER
GIBSON, J.:

[1] The applicant seeks judicial review of a decision of the Convention Determination Refugee Division (the "CRDD") of the Immigration and Refugee Board wherein the CRDD determined the applicant not to be a Convention refugee within the meaning given to that expression in subsection 2 (1) of the Immigration Act[1]. The decision of the CRDD is dated the 1st of February, 2001.

[2] The applicant is a mohajir and a citizen of Pakistan from the Shah Faisal Colony in Karachi. He joined the Pakistan Muslim League (the "PML") in 1990. He alleged a fear of persecution if he is required to return to Pakistan at the hands of members of a mohajir political party, the MQM-Haqiqi, which at all relevant times exercised a significant degree of influence and control in the Shah Faisal Colony, and at the hands of Pakistani authorities, by reason of his political opinion and activities as a member of the PML.

[3] Before the CRDD, the applicant testified to a history from approximately 1992 onwards of harassment, extortion, assault, abduction and torture at the hands of the MQM-Haqiqi by reason of his membership in the PML and his political activity on behalf of that party. The applicant testified that, on the 1st of October, 1999, he witnessed the aftermath of what the CRDD described in its reasons as a "scene of brutal carnage" allegedly inflicted on others by members or representatives of the MQM-Haqiqi, some of whom, he testified, recognized him at the scene. On the advice of his father, the applicant went into hiding for fear that MQM-Haqiqi members would try to implicate him in the carnage because of his affiliation with the PML. The applicant testified that, the next day, the claimant learned from his father that the police had come to his home to interrogate him. Some seven days later, a coup resulted in the demise of the PML government and the installation of a military administration in Pakistan. The applicant learned that many PML workers were being rounded up by police. Arrangements were made for the applicant to leave Pakistan.

[4] The applicant arrived in Canada on the 26th of November, 1999 and stated his intention to make a Convention refugee claim on the 6th of December, 1999.

[5] The CRDD, in its decision, essentially took no issue with the credibility of the applicant's testimony regarding his difficulties at the hands of the MQM-Haqiqi. However, it went on to conclude that, in relation to his fear of persecution at the hands of the MQM-Haqiqi, the applicant had an internal flight alternative to the city of Lahore. On this application for judicial review, the applicant took no issue with that conclusion by the CRDD.

[6] In support of his allegation of a well-founded fear of persecution at the hands of authorities in Pakistan, the applicant provided to the CRDD, very shortly before the hearing into his claim, documentary evidence in the form of Arrest Warrants, a Proclamation and a First Information Report. The CRDD noted discrepancies between the Arrest Warrants and the Proclamation presented by the applicant and documentary evidence that was before it regarding the form and content of such documentation. The CRDD chose to prefer the documentation that was before it that it considered to have been provided by reliable and independent sources. It concluded:
The panel prefers the documentary evidence for the reasons, cited above, that it emanates from independent sources with no interest in the outcome of this particular claim. It finds that the discrepancies, particularly when taken together, provide valid reason to doubt the trustworthiness of the Arrest Warrants and Proclamation. It concludes that they are fraudulent and were provided to embellish the claimant's claim.

[7] The CRDD went on to consider the reliability of the First Information Report presented by the applicant. It determined against the reliability of that Report based in part on its conclusion that the Arrest Warrants and Proclamation presented by the applicant were fraudulent and further on the basis that it considered the applicant's testimony regarding the circumstances leading to the issue of
the First Information Report to be implausible. In the result, the CRDD concluded:
In light of the panel's findings regarding the trustworthiness of the documents presented to corroborate the alleged charges against the claimant, and its findings of implausibility regarding the alleged circumstances under which those charges came to be laid, the panel finds that the credible evidence before it has not established, on a balance of probabilities, that there are any charges outstanding against the claimant in Pakistan today.

[8] The only issue raised on behalf of the applicant on this application for judicial review was whether or not the CRDD erred in determining the Arrest Warrants that were before it to be fraudulent on the basis of documentary evidence that, it was urged, was at best ambivalent and unauthoritative.

[9] The CRDD has wide discretion in the choice of evidence before it on which it chooses to rely. Subsection 68 (3) of the Immigration Act reads as follows:
(3) The Refugee Division is not bound by any legal or technical rules of evidence and, in any proceedings before it, it may receive and base a decision on evidence adduced in the proceedings and considered credible or trustworthy in the circumstances of the case.
(3) La section du statut n'est pas liée par les règles légales ou techniques de présentation de la preuve. Elle peut recevoir les éléments qu'elle juge crédibles ou dignes de foi en l'occurrence et fonder sur eux sa décision.

[10] It was not in dispute before me that extensive documentary evidence discloses that fraudulent documentary evidence is reasonably readily available in support of refugee claims and other immigration proceedings originating from Pakistan. Indeed, in all circumstances, the onus lies on persons, such as the applicant herein, who rely on documentary evidence originating in Pakistan in support of their claims, to be prepared to demonstrate the authenticity of the documentation presented. Here, the applicant was unable to demonstrate the authenticity of his documentation. The CRDD had before it independent documentary evidence which it was entitled to consider that supported a conclusion that the applicant's documentary evidence was not authentic. Notwithstanding that certain of the independent documentary evidence before the CRDD was perhaps less authoritative than it might have been, in the absence of any evidence on behalf of the applicant to support the authenticity of the documentation that he produced, I am satisfied that the factual finding by the CRDD that the applicant's documentation was not reliable, was reasonably open to it.

[11] In the result, this application for judicial review will be dismissed.

[12] While counsel for the applicant was somewhat equivocal before me on whether or not this application for judicial review raised a serious question of general importance that warranted certifying, he produced no question for certification. Counsel for the respondent urged that the decision under review was fact-driven and raised no question for certification. I am in agreement with the position of counsel for the respondent. No question will be certified.
_______________________
J. F.C.C.
Ottawa, Ontario
April 26, 2002

[1] R.S.C. 1985, c. I-2.
FEDERAL COURT OF CANADA TRIAL DIVISION
NAMES OF SOLICITORS AND SOLICITORS ON THE RECORD
COURT FILE NO.: IMM-895-01

STYLE OF CAUSE: NIZAM UDDIN v.
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: CALGARY, ALBERTA
DATE OF HEARING: APRIL 17, 2002
REASONS FOR 

## 7259:2 · paragraphs 15-15

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4cf27526f46a0fdf54526f97405b80c191fb6b74d1cba60505fff907d975dd88`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 7259:2:subtheme:1 · paragraphs 15-15

- Raw key terms: `alberta, appearances, applicant, april, attorney, brad, calgary, canada`
- Display key terms: `alberta, april, brad, calgary`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alberta, april, brad, calgary No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 15-15. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER OF THE HONOURABLE MR. JUSTICE GIBSON DATED: APRIL 26"', 2002
APPEARANCES:
MR G. MICHAEL SHERRITT FOR THE APPLICANT
MR. W. BRAD HARDSTAFF FOR THE RESPONDENT
SOLICITORS ON THE RECORD:
MR G. MICHAEL SHERRITT FOR THE APPLICANT CALGARY, ALBERTA
MR. MORRIS ROSENBERG FOR THE RESPONDENT DEPUTY ATTORNEY GENERAL OF CANADA
