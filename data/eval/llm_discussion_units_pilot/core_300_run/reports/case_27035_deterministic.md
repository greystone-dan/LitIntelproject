# Discussion Units: case 27035

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **31**
- Continuity pairs: **30**
- Discussion Units: **4**
- Paragraph source hashes: **31**
- Sub-themes: **7**

## 27035:1 · paragraphs 0-2

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fc17bd8932987e100004d04fc6a4712477a1aee9e4f83ea2254625282f78d4bb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 27035:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicants, decision, applicant, basis, canada, immigration, june, based`
- Display key terms: `basis, june, based`
- Argument roles: `party_position`
- Explanation: Observed roles: party_position Display terms: basis, june, based Position/evidence statements: Sai Su (the Principal Applicant) and her two children (the Minor Applicants) claim to be citizens of the People’s Republic of China (China) resident in Guangdong province. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claim` at chunk `5270877` offsets `85-90`; context: Sai Su (the Principal Applicant) and her two children (the Minor Applicants) claim to be citizens of the People’s Republic of China (China) resident in Guangdong province.

#### Section text

Su v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-06-14
Neutral citation
2012 FC 743
File numbers
IMM-4632-11
Decision Content
Date: 20120614
Docket: IMM-4632-11
Citation: 2012 FC 743
Ottawa, Ontario, June 14, 2012
PRESENT: The Honourable Madam Justice Snider
BETWEEN:
SAI SU, XI TANG ZHUANG, AND
XI HUA ZHUANG
Applicants
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT
I. Introduction

[1] Ms. Sai Su (the Principal Applicant) and her two children (the Minor Applicants) claim to be citizens of the People’s Republic of China (China) resident in Guangdong province. They came to Canada in 2006 and claimed refugee protection based on the Principal Applicant’s fear of forced sterilization. In a decision dated June 28, 2011, a panel of the Immigration and Refugee Board, Refugee Protection Division (Board) rejected their claim on the basis that the Applicants had failed to establish their identities.

[2] The Applicants seek to overturn the decision on the basis that it is unreasonable. In spite of the most capable submissions of counsel for the Applicant, I have concluded that the decision should stand.


## 27035:2 · paragraphs 3-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7f34daebc2b4a7cfe64b5249792b81255fee7d615a3003a9c6ab19730394d4d6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 27035:2:subtheme:1 · paragraphs 3-5

- Raw key terms: `acceptable, claimant, documentation, establishing, identity, acceptables, account, agissant`
- Display key terms: `acceptable, documentation, establishing, identity, acceptables, account, agissant`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: acceptable, documentation, establishing, identity, acceptables, account, agissant Evidence spans paragraphs 3-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5270879` offsets `784-791`; context: The Refugee Protection Division must take into account, with respect to the credibility of a claimant, whether the claimant possesses acceptable documentation establishing identity, and if not, whether they have provided a reasonable explanation for the lack of documentation or have
taken reasonable steps to obtain the documentation.

#### 27035:2:subtheme:2 · paragraphs 6-22

- Raw key terms: `board, identity, applicant, applicants, documents, establish, principal, document`
- Display key terms: `identity, documents, establish, principal, document`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: identity, documents, establish, principal, document Position/evidence statements: [12] The Applicants argue that the forensic result of “inconclusive” does not mean that the documents are fraudulent. Rule/authority context: The Board was under no obligation to conduct forensic testing of each and every document. Application context: Therefore, the panel gives this witness’ testimony little weight. Evidence spans paragraphs 6-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5270881` offsets `603-610`; context: The Court elaborated that “reasonableness is concerned mostly with the existence of justification, transparency and intelligibility within the decision-making process”, as well as with “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”.
- Evidence: `evidence_fact` cue `record` at chunk `5270882` offsets `196-202`; context: In oral submissions to this Court, counsel for the Applicants described the record as containing an “avalanche” of evidence establishing their identities.
- Evidence: `evidence_fact` cue `evidence` at chunk `5270883` offsets `60-68`; context: [7] The Board considered and dealt with three categories of evidence (or lack thereof): (1) primary documents, such as passports, resident identity cards (RICs), birth certificates and a household register (hukou); (2) secondary documents, such as drivers’ licences and photographs; and (3) viva voce evidence from two witnesses called by the Applicants.
- Evidence: `party_position` cue `argue` at chunk `5270888` offsets `20-25`; context: [12] The Applicants argue that the forensic result of “inconclusive” does not mean that the documents are fraudulent.
- Evidence: `counterargument_limitation` cue `However` at chunk `5270888` offsets `127-134`; context: However, this argument fails to recognize that the burden was on the Applicants to establish their identities.
- Evidence: `governing_rule` cue `under` at chunk `5270891` offsets `248-253`; context: The Board was under no obligation to conduct forensic testing of each and every document.
- Evidence: `evidence_fact` cue `Evidence` at chunk `5270894` offsets `106-114`; context: Viva Voce Evidence
- Evidence: `evidence_fact` cue `testimony` at chunk `5270895` offsets `212-221`; context: The Board was skeptical of this witness’s testimony on the following basis:
The panel finds it is not plausible for the claimant to “bump” into a witness who she had not seen in more than 16 years and did so a month or so before her November 2009 hearing.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5270895` offsets `426-435`; context: Therefore, the panel gives this witness’ testimony little weight.
- Evidence: `evidence_fact` cue `evidence` at chunk `5270896` offsets `271-279`; context: [20] With respect to the second witness, who claimed to be a cousin of the Principal Applicant, the Board observed that:
[T]he witness cannot establish or corroborate the children’s birthplace and citizenship with any first-hand knowledge and she provided no documentary evidence of her relationship to the claimant.
- Evidence: `evidence_fact` cue `testimony` at chunk `5270897` offsets `73-82`; context: [21] The Board’s conclusion that little weight should be accorded to the testimony of these witnesses is not unreasonable.

#### Section text

II. Analysis

[3] Proof of identity is a pre-requisite for a person claiming refugee protection as without it there can “be no sound basis for testing or verifying the claims of persecution or, indeed for determining the Applicant’s true nationality” (Jin v Canada (Minister of Citizenship and Immigration), 2006 FC 126 at para 26, [2006] FCJ No 181 (QL); see also Liu v Canada (Minister of Citizenship and Immigration), 2007 FC 831 at para 18, [2007] FCJ No 1101 (QL)). Section 106 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] and s. 7 of the Refugee Protection Division Rules, SOR/2002-228 [Rules] set out the importance of establishing a claimant’s identity:
IRPA
106. The Refugee Protection Division must take into account, with respect to the credibility of a claimant, whether the claimant possesses acceptable documentation establishing identity, and if not, whether they have provided a reasonable explanation for the lack of documentation or have
taken reasonable steps to obtain the documentation.
Rules
7. The claimant must provide acceptable documents establishing identity and other elements of the claim. A claimant who does not provide acceptable documents must explain why they were not provided and what steps were taken to obtain them.
106. La Section de la protection des réfugiés prend en compte, s’agissant de crédibilité, le fait que, n’étant pas muni de papiers d’identité acceptables, le demandeur ne peut raisonnablement en justifier la raison et n’a pas pris les mesures voulues pour s’en procurer.
7. Le demandeur d’asile transmet à la Section des documents acceptables pour établir son identité et les autres éléments de sa demande. S’il ne peut le faire, il en donne la raison et indique quelles mesures il a prises pour s’en procurer.

[4] The onus is on the claimant to produce acceptable documentation establishing his or her identity. This is a high burden, as it should be.

[5] A decision of the Board with respect to identity is exclusively fact driven. As such, the Board’s decision is reviewable on a standard of reasonableness. In Dunsmuir v New Brunswick, 2008 SCC 9 at para 47, [2008] 1 SCR 190, the Supreme Court of Canada explained that reasonableness is a deferential standard which recognizes that certain questions “may give rise to a number of possible, reasonable conclusions”. The Court elaborated that “reasonableness is concerned mostly with the existence of justification, transparency and intelligibility within the decision-making process”, as well as with “whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law”.

[6] During the course of the hearing, the Applicants produced much information allegedly establishing their identities. In oral submissions to this Court, counsel for the Applicants described the record as containing an “avalanche” of evidence establishing their identities. I will consider this “avalanche” and the Board’s findings with respect to the evidence.

[7] The Board considered and dealt with three categories of evidence (or lack thereof): (1) primary documents, such as passports, resident identity cards (RICs), birth certificates and a household register (hukou); (2) secondary documents, such as drivers’ licences and photographs; and (3) viva voce evidence from two witnesses called by the Applicants. I will consider each of these categories.
A. Primary Documents

[8] The Applicants arrived in Canada on the basis of a false passport. Obviously, a false passport cannot establish identity.

[9] A second problem for the Principal Applicant was that she was unable to provide either the original or a copy of her RIC. As noted by the Board, the RIC is “the most important document to establish a claimant’s identity”. While the Principal Applicant attempted to explain why she did not have her RIC, the point remains that she did not have this important document that could have established her identity.

[10] The Principal Applicant did provide another very important document – a hukou. When that document was submitted for forensic testing, the result was “Inconclusive”. Given that the burden was on the Applicants to provide proof of their identities, an “inconclusive” conclusion from forensic testing arguably did not meet that onus. Moreover, the officer conducting the forensic analysis noted that the document was altered by the addition of middle pages to refer to the older Minor Applicant. The Board – reasonably, in my view – concluded “on a balance of probabilities, that the household register is not an authentic identity document”.

[11] The final primary document was the alleged birth certificate of the older Minor Applicant. This document was also sent for forensic testing, with a result of “Inconclusive”. The analyst noted that “There are a number of significant differences between Birth Certificates believed to be genuine and [the birth certificate submitted]”. As observed by the Board, this document was “questionable”. Once again, this document failed to establish the Minor Applicant’s identity.

[12] The Applicants argue that the forensic result of “inconclusive” does not mean that the documents are fraudulent. I agree. However, this argument fails to recognize that the burden was on the Applicants to establish their identities. Forensic examination of a document that results in an “inconclusive” finding (particularly when specific problems with the document are identified) does not establish the authenticity of the document.

[13] In sum, there was not a single reliable or genuine primary document that conclusively or persuasively established the identity of the Applicants.
B. Secondary Documents

[14] During the course of the hearing, the Applicants put forward a number of other documents purporting to establish the Principal Applicant’s identity; specifically, a driver’s licence, marriage certificate, IUD booklet and a Notice of Assessment. None of these documents contained the type of security features that would permit a meaningful forensic analysis.

[15] The Board examined all of these documents, although none were sent for forensic testing. However, the Board referred to country documentation that confirmed that fraudulent documents were readily available in Guangdong province. The Board was under no obligation to conduct forensic testing of each and every document. As stated by Justice Harrington in Farooqi v Canada (Minister of Citizenship and Immigration), 2004 FC 1396 at para 10, [2004] FCJ No 1696 (QL):
As far as I am concerned, once the identity documents which were offered as being real were found to be fake, the matter came to an end. There was no duty on the part of the Board to submit other documents for analysis. A legitimate claimant might well have reason to carry fake identification, but no reason to proffer that fake identification as real. Was the next set of documents better fakes? The Board should not be treated as a training school in which counterfeiters can practice their craft.

[16] In this case, having concluded that the primary documents were either missing or not genuine and that fake identity documents were easily obtained in Guangdong province, it was not unreasonable for the Board to give the secondary documents “little weight”.

[17] The Board also considered the photograph of the Principal Applicant in a class photograph. The Board concluded that, even if the unclear photograph included the Principal Applicant, a class photograph did not establish citizenship.

[18] These secondary documents did not substantiate the identity of the Principal Applicant.
C. Viva Voce Evidence

[19] Two persons testified in support of the Principal Applicant’s identity. The first witness claimed to be a friend of the Principal Applicant during secondary school. The Board was skeptical of this witness’s testimony on the following basis:
The panel finds it is not plausible for the claimant to “bump” into a witness who she had not seen in more than 16 years and did so a month or so before her November 2009 hearing. Therefore, the panel gives this witness’ testimony little weight.

[20] With respect to the second witness, who claimed to be a cousin of the Principal Applicant, the Board observed that:
[T]he witness cannot establish or corroborate the children’s birthplace and citizenship with any first-hand knowledge and she provided no documentary evidence of her relationship to the claimant.

[21] The Board’s conclusion that little weight should be accorded to the testimony of these witnesses is not unreasonable.


## 27035:3 · paragraphs 23-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0bc0d6c55e13e948016d228e5c1d7c7e80810d4342de79d12b251b9238b380c0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 27035:3:subtheme:1 · paragraphs 23-25

- Raw key terms: `applicants, board, decision, acceptable, argue, avalanche, canada, cannot`
- Display key terms: `acceptable, argue, avalanche, cannot`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, party_position Display terms: acceptable, argue, avalanche, cannot Position/evidence statements: [23] Finally the Applicants argue that, if the Board’s decision is upheld, they are entitled to a declaration that they cannot be removed to China and an order prohibiting the Government of Canada from removing the Appli Operative outcome context: [23] Finally the Applicants argue that, if the Board’s decision is upheld, they are entitled to a declaration that they cannot be removed to China and an order prohibiting the Government of Canada from removing the Appli Evidence spans paragraphs 23-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `5270898` offsets `103-111`; context: [22] Quite simply, the Applicants failed to establish their identities, in spite of the “avalanche” of evidence.
- Evidence: `party_position` cue `argue` at chunk `5270899` offsets `28-33`; context: [23] Finally the Applicants argue that, if the Board’s decision is upheld, they are entitled to a declaration that they cannot be removed to China and an order prohibiting the Government of Canada from removing the Applicants to China.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5270899` offsets `120-126`; context: [23] Finally the Applicants argue that, if the Board’s decision is upheld, they are entitled to a declaration that they cannot be removed to China and an order prohibiting the Government of Canada from removing the Applicants to China.
- Evidence: `disposition` cue `upheld` at chunk `5270899` offsets `67-73`; context: [23] Finally the Applicants argue that, if the Board’s decision is upheld, they are entitled to a declaration that they cannot be removed to China and an order prohibiting the Government of Canada from removing the Applicants to China.

#### 27035:3:subtheme:2 · paragraphs 26-27

- Raw key terms: `applicants, cbsa, accordingly, actions, addition, agency, agree, although`
- Display key terms: `cbsa, accordingly, actions, addition, agency, agree, although`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: cbsa, accordingly, actions, addition, agency, agree, although Rule/authority context: Although I agree that the Federal Court has the jurisdiction to issue the remedies of a declaration or a writ of prohibition under s. Application context: A declaration or prohibition order based on the current judicial review application would bind a separate series of decision makers and is, accordingly, inappropriate. Operative outcome context: 1(3) of the Federal Courts Act, RSC 1985, c F-7, this is not a case where such a declaration can be granted. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5270900` offsets `161-166`; context: Although I agree that the Federal Court has the jurisdiction to issue the remedies of a declaration or a writ of prohibition under s.
- Evidence: `governing_rule` cue `under` at chunk `5270900` offsets `222-227`; context: Although I agree that the Federal Court has the jurisdiction to issue the remedies of a declaration or a writ of prohibition under s.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5270900` offsets `823-834`; context: A declaration or prohibition order based on the current judicial review application would bind a separate series of decision makers and is, accordingly, inappropriate.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5270900` offsets `97-105`; context: Although I agree that the Federal Court has the jurisdiction to issue the remedies of a declaration or a writ of prohibition under s.
- Evidence: `disposition` cue `granted` at chunk `5270900` offsets `334-341`; context: 1(3) of the Federal Courts Act, RSC 1985, c F-7, this is not a case where such a declaration can be granted.

#### 27035:3:subtheme:3 · paragraphs 28-29

- Raw key terms: `ability, adjudges, answer, applicants, application, based, cause, certified`
- Display key terms: `ability, adjudges, answer, based, certified`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: ability, adjudges, answer, based, certified Operative outcome context: the application for judicial review is dismissed; and 2. Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5270902` offsets `30-38`; context: [26] The Applicants propose a question related to the ability of this Court to grant a declaration in these circumstances.
- Evidence: `disposition` cue `dismissed` at chunk `5270902` offsets `423-432`; context: the application for judicial review is dismissed; and
2.

#### Section text

III. Conclusion

[22] Quite simply, the Applicants failed to establish their identities, in spite of the “avalanche” of evidence. There were significant problems with each and every document and witness proffered. The Board’s decision, when read as a whole, falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law.

[23] Finally the Applicants argue that, if the Board’s decision is upheld, they are entitled to a declaration that they cannot be removed to China and an order prohibiting the Government of Canada from removing the Applicants to China.

[24] The Applicants’ request for declaratory relief is beyond the scope of this judicial review. Although I agree that the Federal Court has the jurisdiction to issue the remedies of a declaration or a writ of prohibition under s. 18.1(3) of the Federal Courts Act, RSC 1985, c F-7, this is not a case where such a declaration can be granted. This judicial review is of a decision by the Board which is within the purview of the Minister of Citizenship and Immigration. Removal orders (made under s. 48(1) of IRPA) are put in place by the Canada Border Services Agency (CBSA), and thus within the statutory responsibility of the Minister of Public Safety and Emergency Preparedness. A declaration or prohibition order based on the current judicial review application would bind a separate series of decision makers and is, accordingly, inappropriate.

[25] In addition, at this point in time, the actions that may be taken by CBSA in removing the Applicants are not known. We can only speculate that the CBSA may ultimately attempt to send the Applicants to China.

[26] The Applicants propose a question related to the ability of this Court to grant a declaration in these circumstances. Given that the answer to any such question is not determinative of this application and would be, in any event, based on speculation as to where the Applicants will be removed, I decline to certify any question.
JUDGMENT
THIS COURT ORDERS AND ADJUDGES that:
1. the application for judicial review is dismissed; and
2. no question of general importance is certified.
“Judith A. Snider”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-4632-11
STYLE OF CAUSE: SAI SU et al v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: JUNE 6, 2012
REASONS FOR 

## 27035:4 · paragraphs 30-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9c728a7ac84b57e2f839623fa09a2a89dffd12098d0cf82f3fcf11f4f32d4420`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 27035:4:subtheme:1 · paragraphs 30-30

- Raw key terms: `appearances, applicant, attorney, canada, corporation, dated, deputy, firm`
- Display key terms: `corporation, dated, deputy, firm`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: corporation, dated, deputy, firm No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 30-30. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: SNIDER J.
DATED: JUNE 14, 2012
APPEARANCES:
Mr. Rocco Galati
FOR THE APPLICANT
Ms. A. Leena Jaakkimainen
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Rocco Galati Law Firm
Professional Corporation
Toronto, Ontario
FOR THE APPLICANT
Myles J. Kirvan
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
