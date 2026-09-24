# Discussion Units: case 15260

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **16**
- Continuity pairs: **15**
- Discussion Units: **2**
- Paragraph source hashes: **16**
- Sub-themes: **4**

## 15260:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `96ac85d8824fc0dacca48f2a3124e29dd468ed91efd7546227465e906b9c1380`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 15260:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, because, board, division, protection, refugee, claim, claimant`
- Display key terms: `because, division, protection, refugee`
- Argument roles: `evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, party_position, reasoning_application Display terms: because, division, protection, refugee Position/evidence statements: [2] The applicant is a citizen of Sri Lanka who claims a well-founded fear of returning to Sri Lanka because he is a former United National Party ("UNP") member who left the UNP to join the Sri Lankan National Front Part Rule/authority context: Therefore, after having considered the totality to the evidence, the relevant statutory provisions and jurisprudence, the Refugee Protection Division rejects the claim [. Application context: [2] The applicant is a citizen of Sri Lanka who claims a well-founded fear of returning to Sri Lanka because he is a former United National Party ("UNP") member who left the UNP to join the Sri Lankan National Front Part | [3] The Board rejected the applicant's refugee claim on grounds of credibility because the applicant was unable to produce any collaborating documentation that he was involved with the UNP. Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `4731502` offsets `181-196`; context: [1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board ("Board") dated June 4, 2003, wherein the Board determined that the applicant is not a credible Convention refugee or person in need of protection.
- Evidence: `party_position` cue `claims` at chunk `4731503` offsets `48-54`; context: [2] The applicant is a citizen of Sri Lanka who claims a well-founded fear of returning to Sri Lanka because he is a former United National Party ("UNP") member who left the UNP to join the Sri Lankan National Front Party ("SLNFP") .
- Evidence: `reasoning_application` cue `because` at chunk `4731503` offsets `101-108`; context: [2] The applicant is a citizen of Sri Lanka who claims a well-founded fear of returning to Sri Lanka because he is a former United National Party ("UNP") member who left the UNP to join the Sri Lankan National Front Party ("SLNFP") .
- Evidence: `evidence_fact` cue `evidence` at chunk `4731504` offsets `941-949`; context: ]
I find that the neglect to provide corroborating evidence in regards to his membership and the arrest, which could reasonably have been forthcoming, (he was able to show that his father and brother were involved and arrested) indicates that he invented his story in order to create a refugee claim for protection.
- Evidence: `reasoning_application` cue `because` at chunk `4731504` offsets `79-86`; context: [3] The Board rejected the applicant's refugee claim on grounds of credibility because the applicant was unable to produce any collaborating documentation that he was involved with the UNP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4731505` offsets `276-284`; context: Therefore, after having considered the totality to the evidence, the relevant statutory provisions and jurisprudence, the Refugee Protection Division rejects the claim [.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4731505` offsets `324-337`; context: Therefore, after having considered the totality to the evidence, the relevant statutory provisions and jurisprudence, the Refugee Protection Division rejects the claim [.
- Evidence: `reasoning_application` cue `concludes` at chunk `4731505` offsets `22-31`; context: [4] Finally the Board concludes at page 5:
I find that this claim has to fail because the claimant is not a credible and trustworthy witness and nothing else was presented to establish the material aspects of this claim.

#### 15260:1:subtheme:2 · paragraphs 5-12

- Raw key terms: `board, claim, documents, applicant, applicant's, credibility, provided, case`
- Display key terms: `documents, applicant's, credibility, provided, case`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: documents, applicant's, credibility, provided, case Position/evidence statements: [5] The applicant's sole issue in this case is whether or not the Board can reject a claim only for the reason that claimant failed to produce corroborative documents. | [6] The applicant submits that in the absence of any evidence to the contrary, his sworn oral and written testimony is evidence that can be properly considered to support his claim, and that the Board's rejection of this Rule/authority context: However, a reasonable explanation for the failure to provide documents under section 7 means that corroboration documents are not always necessary. Evidence spans paragraphs 5-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4731506` offsets `25-30`; context: [5] The applicant's sole issue in this case is whether or not the Board can reject a claim only for the reason that claimant failed to produce corroborative documents.
- Evidence: `party_position` cue `claim` at chunk `4731506` offsets `85-90`; context: [5] The applicant's sole issue in this case is whether or not the Board can reject a claim only for the reason that claimant failed to produce corroborative documents.
- Evidence: `party_position` cue `submits` at chunk `4731507` offsets `18-25`; context: [6] The applicant submits that in the absence of any evidence to the contrary, his sworn oral and written testimony is evidence that can be properly considered to support his claim, and that the Board's rejection of this evidence was patently unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4731507` offsets `53-61`; context: [6] The applicant submits that in the absence of any evidence to the contrary, his sworn oral and written testimony is evidence that can be properly considered to support his claim, and that the Board's rejection of this evidence was patently unreasonable.
- Evidence: `party_position` cue `submits` at chunk `4731508` offsets `19-26`; context: [7] The respondent submits that the Board is entitled to reject an applicant's claim on the basis of credibility alone, and that inconsistencies and contradictions do not form the only basis for making negative credibility findings in a refugee case.
- Evidence: `governing_rule` cue `under` at chunk `4731510` offsets `197-202`; context: However, a reasonable explanation for the failure to provide documents under section 7 means that corroboration documents are not always necessary.
- Evidence: `party_position` cue `claim` at chunk `4731511` offsets `177-182`; context: [10] It is well established that a panel cannot make negative inferences solely from the fact that a refugee claimant failed to produce any extrinsic documents to corroborate a claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4731511` offsets `425-433`; context: But where there are valid reasons to doubt a claimant's credibility, a failure to provide corroborating documentation is a proper consideration for a panel if the Board does not accept the applicant's explanation for failing to produce that evidence.
- Evidence: `party_position` cue `claim` at chunk `4731513` offsets `58-63`; context: [12] The onus is on the applicant to establish a credible claim.

#### 15260:1:subtheme:3 · paragraphs 13-14

- Raw key terms: `applicant, reasons, absence, accordingly, amarapala, application, because, case`
- Display key terms: `absence, accordingly, amarapala, because, case`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: absence, accordingly, amarapala, because, case Application context: [13] The questions for certification proposed by the applicant regarding Rule 7 and the absence of corroborative evidence would not be dispositive of this case because corroborative evidence is not necessary in every cas Operative outcome context: ORDER THIS COURT ORDERS that this application is dismissed. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4731514` offsets `329-337`; context: Accordingly, the Court will not certify any question.
- Evidence: `evidence_fact` cue `evidence` at chunk `4731514` offsets `113-121`; context: [13] The questions for certification proposed by the applicant regarding Rule 7 and the absence of corroborative evidence would not be dispositive of this case because corroborative evidence is not necessary in every case, but was necessary in this case for the reasons stated herein.
- Evidence: `reasoning_application` cue `because` at chunk `4731514` offsets `160-167`; context: [13] The questions for certification proposed by the applicant regarding Rule 7 and the absence of corroborative evidence would not be dispositive of this case because corroborative evidence is not necessary in every case, but was necessary in this case for the reasons stated herein.
- Evidence: `counterargument_limitation` cue `but` at chunk `4731514` offsets `223-226`; context: [13] The questions for certification proposed by the applicant regarding Rule 7 and the absence of corroborative evidence would not be dispositive of this case because corroborative evidence is not necessary in every case, but was necessary in this case for the reasons stated herein.
- Evidence: `disposition` cue `dismissed` at chunk `4731514` offsets `388-397`; context: ORDER
THIS COURT ORDERS that this application is dismissed.

#### Section text

Amarapala v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2004-01-07
Neutral citation
2004 FC 12
File numbers
IMM-5034-03
Decision Content
Date: 20040107
Docket: IMM-5034-03
Citation: 2004 FC 12
Toronto, Ontario, January 7th, 2004
Present: The Honourable Mr. Justice Kelen
BETWEEN:
PRIYANGA UDAYANTHA AMARAPALA
Applicant
and
THE MINISTER OF
CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] This is an application for judicial review of a decision of the Refugee Protection Division of the Immigration and Refugee Board ("Board") dated June 4, 2003, wherein the Board determined that the applicant is not a credible Convention refugee or person in need of protection.
THE FACTS

[2] The applicant is a citizen of Sri Lanka who claims a well-founded fear of returning to Sri Lanka because he is a former United National Party ("UNP") member who left the UNP to join the Sri Lankan National Front Party ("SLNFP") . He claims UNP members consider him a traitor and have threatened him.

[3] The Board rejected the applicant's refugee claim on grounds of credibility because the applicant was unable to produce any collaborating documentation that he was involved with the UNP. At page 2 of its reasons the Board states:
Here the absence of documentation which would indicate that the claimant was ever involved with the UNP created a credibility concern, and I took into account Rule 7 of the Refugee Protection Division Rules and the Commentary to that rule, when coming to this finding. I am aware that claimants do not necessarily have to submit documents in support of their claim.
And at page 3 the Board states:
Upon closer examination it became obvious that his documents relate to the political activities of his father who died in 1997, and his brother Vajira, who still lives in Sri Lanka. In regards to the claimant there is nothing to connect him with the UNP.
[...]
I find that the neglect to provide corroborating evidence in regards to his membership and the arrest, which could reasonably have been forthcoming, (he was able to show that his father and brother were involved and arrested) indicates that he invented his story in order to create a refugee claim for protection. Even though the claimant might have been in charge of the family business and his father and brother might have been involved with the UNP, there is insufficient evidence to establish that this involvement had ever impacted on him personally.

[4] Finally the Board concludes at page 5:
I find that this claim has to fail because the claimant is not a credible and trustworthy witness and nothing else was presented to establish the material aspects of this claim. Therefore, after having considered the totality to the evidence, the relevant statutory provisions and jurisprudence, the Refugee Protection Division rejects the claim [...]
ANALYSIS

[5] The applicant's sole issue in this case is whether or not the Board can reject a claim only for the reason that claimant failed to produce corroborative documents. The applicant also seeks leave to have this question certified.

[6] The applicant submits that in the absence of any evidence to the contrary, his sworn oral and written testimony is evidence that can be properly considered to support his claim, and that the Board's rejection of this evidence was patently unreasonable. The applicant also submits that the Board erred in relying on s. 7 of the Refugee Protection Division Rules, SOR/2002-228 ("Rules") to reject his credibility.

[7] The respondent submits that the Board is entitled to reject an applicant's claim on the basis of credibility alone, and that inconsistencies and contradictions do not form the only basis for making negative credibility findings in a refugee case. The respondent also submits that the Board has the discretion to assess credibility on the basis of explanations provided by the applicant.

[8] I will deal first with the applicant's submission with respect to section 7 of the Rules. That submission is without merit since the Board is entitled to take section 7 into account. Section 7 states:
Documents establishing identity and other elements of the claim
7. The claimant must provide acceptable documents establishing identity and other elements of the claim. A claimant who does not provide acceptable documents must explain why they were not provided and what steps were taken to obtain them.
Documents d'identité et autres éléments de la demande
7. Le demandeur d'asile transmet à la Section des documents acceptables pour établir son identité et les autres éléments de sa demande. S'il ne peut le faire, il en donne la raison et indique quelles mesures il a prises pour s'en procurer.

[9] Section 7 makes documentation a requirement not only for establishing identity, but also for other elements of the claim. However, a reasonable explanation for the failure to provide documents under section 7 means that corroboration documents are not always necessary.

[10] It is well established that a panel cannot make negative inferences solely from the fact that a refugee claimant failed to produce any extrinsic documents to corroborate a claim. But where there are valid reasons to doubt a claimant's credibility, a failure to provide corroborating documentation is a proper consideration for a panel if the Board does not accept the applicant's explanation for failing to produce that evidence. See Singh v. Canada (Minister of Citizenship and Immigration), [2003] F.C.J. 755 per O'Reilly J. at paragraph 9.

[11] In this case, the applicant provided documents about his father's and brother's involvement in the UNP, and the Board reasonably expected documents would be produced about the applicant's involvement with the UNP. The failure to produce documents one would normally expect is a relevant consideration in assessing and rejecting the credibility of the applicant.

[12] The onus is on the applicant to establish a credible claim. The applicant failed to do so, and the Board provided clear reasons for its credibility finding. This finding is not patently unreasonable, and does not err with respect to the absence of corroborative documents which the Board reasonably expected.

[13] The questions for certification proposed by the applicant regarding Rule 7 and the absence of corroborative evidence would not be dispositive of this case because corroborative evidence is not necessary in every case, but was necessary in this case for the reasons stated herein. Accordingly, the Court will not certify any question.
ORDER
THIS COURT ORDERS that this application is dismissed.
"Michael A. Kelen"
J.F.C.
FEDERAL COURT
NAMES OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-5034-03

STYLE OF CAUSE: PRIYANGA UDAYANTHA AMARAPALA
Applicant
and
MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: JANUARY 6, 2004
REASONS FOR 

## 15260:2 · paragraphs 15-15

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `da3bd937c7fe46664a2f4fb40982f926b2bbe60f26c676ff06e641c7128352de`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 15260:2:subtheme:1 · paragraphs 15-15

- Raw key terms: `amarapala, appearances, applicant, attorney, canada, citizenship, court, crane`
- Display key terms: `amarapala, crane`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: amarapala, crane No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 15-15. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER: KELEN J.
DATED: JANUARY 7, 2004
APPEARANCES:
Micheal Crane For the Applicant
Neeta Logsetty For the Respondent
SOLICITORS OF RECORD:
Micheal Crane
Toronto, Ontario For the Applicant
Morris Rosenberg
Deputy Attorney General of Canada
Toronto, Ontario For the Respondent
FEDERAL COURT
TRIAL DIVISION
Date: 20040107
Docket: IMM-5034-03
BETWEEN:
PRIYANGA UDAYANTHA AMARAPALA
Applicant
and
THE MINISTER OF
CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER
AND ORDER
