# Discussion Units: case 25606

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **18**
- Continuity pairs: **17**
- Discussion Units: **3**
- Paragraph source hashes: **18**
- Sub-themes: **5**

## 25606:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3ab7d0880b5e213991a8ecd480a768c6a7f09b8a3f10f277ea7c5198b9a68375`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25606:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, board, canada, decision, found, immigration, neither, reasons`
- Display key terms: `neither`
- Argument roles: `disposition, evidence_fact, governing_rule`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule Display terms: neither Rule/authority context: [1] The applicant seeks an order setting aside the May 24, 2011 decision of the Refugee Protection Division of the Immigration Refugee Board of Canada (the Board), which found her to be neither a Convention (United Natio Operative outcome context: For the reasons that follow, the application for judicial review is granted. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5205356` offsets `334-339`; context: [1] The applicant seeks an order setting aside the May 24, 2011 decision of the Refugee Protection Division of the Immigration Refugee Board of Canada (the Board), which found her to be neither a Convention (United Nations’ Convention Relating to the Status of Refugees, [1969] Can TS No 6) refugee nor a person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA).
- Evidence: `disposition` cue `granted` at chunk `5205356` offsets `496-503`; context: For the reasons that follow, the application for judicial review is granted.
- Evidence: `evidence_fact` cue `testimony` at chunk `5205357` offsets `178-187`; context: The Board found:
The claimant’s testimony was marked with inconsistencies, contradictions and implausibilities.

#### 25606:1:subtheme:2 · paragraphs 3-6

- Raw key terms: `applicant, board, credibility, case, claim, clear, decision, documents`
- Display key terms: `credibility, case, clear, documents`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: credibility, case, clear, documents Rule/authority context: Prior to examining the decision in question, it is helpful to revisit some of the principles which govern the assessment of credibility: a. | In Hilo, the Federal Court of Appeal held at paragraph 6 that: …the board was under a duty to give its reasons for casting doubt upon the appellant’s credibility in clear and unmistakable terms. Application context: [3] I find that the Board’s decision falls outside the scope or range of legally permissible outcomes given the facts and law and is unreasonable. | is defective because it is couched in vague and general terms. Evidence spans paragraphs 3-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5205358` offsets `301-307`; context: Instead of focusing on the factual issues that are material to a claim for protection, the Board focused its attention on matters that were immaterial and irrelevant to the claim for protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `5205358` offsets `817-825`; context: the Board is entitled to make reasonable findings based on implausibilities, common sense and rationality…The Board may reject uncontradicted evidence if it is not consistent with the probabilities affecting the case as a whole, or where inconsistencies are found in the evidence….
- Evidence: `reasoning_application` cue `I find` at chunk `5205358` offsets `4-10`; context: [3] I find that the Board’s decision falls outside the scope or range of legally permissible outcomes given the facts and law and is unreasonable.
- Evidence: `counterargument_limitation` cue `Notwithstanding` at chunk `5205358` offsets `147-162`; context: Notwithstanding the concerns about the applicant’s credibility, the decision fails to substantively analyze the claim.
- Evidence: `issue` cue `question` at chunk `5205359` offsets `138-146`; context: Prior to examining the decision in question, it is helpful to revisit some of the principles which govern the assessment of credibility:
a.
- Evidence: `evidence_fact` cue `evidence` at chunk `5205359` offsets `458-466`; context: Uncontradicted evidence may be rejected if it is not consistent with the probabilities of the case as a whole, or where inconsistencies are found in the evidence: Akinlolu v Canada (Minister of Citizenship and Immigration), [1997] FCJ No 296;
c.
- Evidence: `governing_rule` cue `principles` at chunk `5205359` offsets `185-195`; context: Prior to examining the decision in question, it is helpful to revisit some of the principles which govern the assessment of credibility:
a.
- Evidence: `evidence_fact` cue `testimony` at chunk `5205360` offsets `291-300`; context: As for the inconsistencies, contradictions and implausibilities which the Board claimed marked the entirety of the applicant’s testimony, the Board failed to provide specific examples or to demonstrate new the applicant’s testimony was inconsistent, contradictory or implausible.
- Evidence: `governing_rule` cue `under` at chunk `5205360` offsets `522-527`; context: In Hilo, the Federal Court of Appeal held at paragraph 6 that:
…the board was under a duty to give its reasons for casting doubt upon the appellant’s credibility in clear and unmistakable terms.
- Evidence: `reasoning_application` cue `because` at chunk `5205360` offsets `688-695`; context: is defective because it is couched in vague and general terms.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5205361` offsets `39-45`; context: [6] Reading the decision as a whole it cannot be said that the Board has provided, in clear and unmistakeable terms, reasons for casting doubt on the applicant’s credibility.

#### 25606:1:subtheme:3 · paragraphs 7-14

- Raw key terms: `board, member, applicant, claim, status, claimant, credibility, find`
- Display key terms: `status, credibility, find`
- Argument roles: `disposition, issue, reasoning_application`
- Explanation: Observed roles: disposition, issue, reasoning_application Display terms: status, credibility, find Application context: … I find it more likely than not that the claimant travelled to the United Kingdom and possibly back to Saint Lucia on a passport that she has not disclosed that contains information that she does not want me to know. Operative outcome context: [14] The application for judicial review is granted. Evidence spans paragraphs 7-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5205362` offsets `326-334`; context: First, the Board was focussed on its analysis on events prior to those giving rise to the claim, such that it never asked the question; secondly, the name of the persecutor was included in the applicant’s PIF.
- Evidence: `reasoning_application` cue `I find` at chunk `5205365` offsets `311-317`; context: … I find it more likely than not that the claimant travelled to the United Kingdom and possibly back to Saint Lucia on a passport that she has not disclosed that contains information that she does not want me to know.
- Evidence: `disposition` cue `granted` at chunk `5205369` offsets `44-51`; context: [14] The application for judicial review is granted.

#### Section text

Cooper v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-01-31
Neutral citation
2012 FC 118
File numbers
IMM-3840-11
Decision Content
Date: 20120131
Docket: IMM-3840-11
Citation: 2012 FC 118
Ottawa, Ontario, January 31, 2012
PRESENT: The Honourable Mr. Justice Rennie
BETWEEN:
LIZ COOPER
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] The applicant seeks an order setting aside the May 24, 2011 decision of the Refugee Protection Division of the Immigration Refugee Board of Canada (the Board), which found her to be neither a Convention (United Nations’ Convention Relating to the Status of Refugees, [1969] Can TS No 6) refugee nor a person in need of protection under sections 96 and 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA). For the reasons that follow, the application for judicial review is granted.

[2] The applicant is from St. Lucia and fears her ex-boyfriend. The Board refused the applicant’s claim on the basis that she lacked credibility. The Board found:
The claimant’s testimony was marked with inconsistencies, contradictions and implausibilities. The claimant’s evidence concerning the more material aspects of her claim was neither consistent nor cogent. Given the importance of the search for her parents to her story, it is reasonable to expect the claimant to give clear and consistent evidence in this regard. She did not.

[3] I find that the Board’s decision falls outside the scope or range of legally permissible outcomes given the facts and law and is unreasonable. Notwithstanding the concerns about the applicant’s credibility, the decision fails to substantively analyze the claim. Instead of focusing on the factual issues that are material to a claim for protection, the Board focused its attention on matters that were immaterial and irrelevant to the claim for protection. In consequence, the Board undertook no analysis of the principle basis of the claim of risk. As Justice Luc Martineau held in Lubana v Canada (Minister of Citizenship and Immigration), 2003 FCT 116, paras 10-12:
….the Board is entitled to make reasonable findings based on implausibilities, common sense and rationality…The Board may reject uncontradicted evidence if it is not consistent with the probabilities affecting the case as a whole, or where inconsistencies are found in the evidence….
However, not every kind of inconsistency or implausibility in the applicant's evidence will reasonably support the Board's negative findings on overall credibility. It would not be proper for the Board to base its findings on extensive “microscopic” examination of issues irrelevant or peripheral to the applicant’s claim: …. In particular, where a claimant travels on false documents, destroys travel documents or lies about them upon arrival following an agent's instructions, it has been held to be peripheral and of very limited value to a determination of general credibility.
[Citations omitted]

[4] Secondly, the Board’s determination that the applicant lacked credibility was vague and imprecise. Prior to examining the decision in question, it is helpful to revisit some of the principles which govern the assessment of credibility:
a. A board is entitled to make findings of credibility based on implausibility, common sense and rationality: Hilo v Canada (Minister of Employment and Immigration), [1991] FCJ No 228; Lubana, above;
b. Uncontradicted evidence may be rejected if it is not consistent with the probabilities of the case as a whole, or where inconsistencies are found in the evidence: Akinlolu v Canada (Minister of Citizenship and Immigration), [1997] FCJ No 296;
c. Inferences must be reasonable and must be set out in clear and unmistakable terms: Hilo;
d. Not all inconsistencies and implausibilities will support a negative finding of credibility. Adverse credibility findings should not be based on microscopic examination of issues irrelevant or peripheral to the claim: Attakora v Canada (Minister of Employment and Immigration), [1989] FCJ No 444;
e. Evidence or testimony with respect to whether a claimant travels on false travel documents, destroys travel documents or lies about them upon arrival is peripheral and of very limited value to a determination of credibility: Lubana;
f. Assessment of testimony should take into account the age, culture, background and prior social experience of the witness, as should a lack of coherence in testimony where the psychological condition of the witness has been medically established;
g. Similarly, in assessing statements made by refugees to immigration officials on first arrival to Canada, the trier of fact must consider that “most refugees have lived experiences in their country of origin which gives them good reason to distrust persons in authority”: Professor J.C. Hathaway, The Law of Refugee Status (Toronto, Butterworths) (1991), pp 84-85, as cited by Justice Martineau in Lubana;
h. Where a credibility finding is based on inconsistencies of the applicant, specific examples of inconsistency must be set out. The inconsistency must arise in respect of other evidence which was accepted as trustworthy. Put otherwise, an inconsistency can arise in one of two ways: evidence is internally inconsistent in the testimony of the witness, or; evidence that is inconsistent with respect to the testimony of other witnesses or documents. If, in the later situation, that of external inconsistency, the evidence on which the inconsistency is predicated must be accepted as trustworthy;
i. The cumulative effect of minor inconsistencies and contradictions can support an overall finding that an applicant is not credible: Feng v Canada (Citizenship and Immigration), 2010 FC 476; and
j. A general finding of a lack of credibility may conceivably extend to all relevant evidence emanating from the testimony of a witness: Sheikh v Canada (Minister of Employment and Immigration), [1990] 3 FC 238.

[5] In the present case, the Board placed an unreasonable emphasis on the applicant’s travel documents which, in turn, served as the basis for rejecting the claim. As for the inconsistencies, contradictions and implausibilities which the Board claimed marked the entirety of the applicant’s testimony, the Board failed to provide specific examples or to demonstrate new the applicant’s testimony was inconsistent, contradictory or implausible. In Hilo, the Federal Court of Appeal held at paragraph 6 that:
…the board was under a duty to give its reasons for casting doubt upon the appellant’s credibility in clear and unmistakable terms. The board’s credibility assessment….is defective because it is couched in vague and general terms. The board concluded that the appellant’s evidence lacked detail and was sometimes inconsistent. Surely particulars of the lack of detail and of the inconsistencies should have been provided. Likewise particulars of his inability to answer questions should have been made available.
[Citations omitted]

[6] Reading the decision as a whole it cannot be said that the Board has provided, in clear and unmistakeable terms, reasons for casting doubt on the applicant’s credibility. To the extent reasons were given, they were vague and speculative. In consequence, the Board failed to substantively and materially evaluate the nexus to the Convention ground the applicant asserted came into being after she had returned from the United Kingdom (UK); namely, the threat of physical abuse from her male partner after she had returned from the UK to St. Lucia.

[7] I note as well that the Board supports its conclusion on credibility in its observation that the applicant did not state the name of her persecutor. In this regard, two observations are in order. First, the Board was focussed on its analysis on events prior to those giving rise to the claim, such that it never asked the question; secondly, the name of the persecutor was included in the applicant’s PIF.

[8] In my view, while it is appropriate to test and probe events ancillary to the substance of the claim, in this case the credibility findings were based on an entirely peripheral matter. The Board member was clearly of the view that the applicant held status in another country and theorized as to how the applicant’s life unfolded:
… I believe it more plausible that Liz left Saint Lucia with her parents and the middle child Lena, leaving the eldest child alone in Saint Lucia, rather than the story Liz wants the Division to accept,…

[9] The proof of the alternate theory advanced by the Board member would lie of course in proof of UK status, which the Board member sought to establish. Even the Board member noted the correlation between the two:
This suggests to this panel (and I so find) that the claimant likely has or had status in the United Kingdom. I note that the claimant failed to provide her British immigration file, which would have cleared up this mystery.

[10] The Board member set-up, through this analysis, a false paradigm. If it could be established that the applicant lied about her UK status, the claim failed:
From my experience both as a member of this Division and in my professional life before becoming a member, I gained some experience with passports. … I find it more likely than not that the claimant travelled to the United Kingdom and possibly back to Saint Lucia on a passport that she has not disclosed that contains information that she does not want me to know.

[11] The reasons for decision, and the questioning of the Board member, reflect a singular pursuit of a theory of a case that the applicant was a resident of the UK:
MEMBER: If I were to ask you for your permission, and I need your permission, you do not have to say yes, but if I were to ask your consent to contact the English authorities to find out what your status was in the UK, would you agree?
CLAIMANT: My status?
MEMBER: Yes.
CLAIMANT: I did not have any status in the UK.
MEMBER: Well, you had a status of visitor, according to you.
CLAIMANT: Well, I thought you were talking about (inaudible).
MEMBER: You… according to your own personal information form, you had the status of visitor, alright, so that is a status. It is a temporary resident visitor. So, if I were to ask you for your permission to give me your consent…
CLAIMANT: Yeah you can (inaudible).
MEMBER: And I can check with the UK authorities to see if you were a citizen of the UK or a permanent resident of the UK. Would you give me your permission?
CLAIMANT: Yes, you can go ahead.
MEMBER: Are you a citizen of the UK?
CLAIMANT: I am not.
MEMBER: Are you a permanent resident of the UK?
CLAIMANT: No I am not.

[12] In a subsequent correspondence to the applicant the Board member indicated that he would not be contacting the UK authorities.

[13] The Board member then speculated as to what that passport might have disclosed. While interesting, and relevant to an exploration of the overall credibility of the claim, it is not determinative of the claim for protection, which was, in main, unexplored.

[14] The application for judicial review is granted.


## 25606:2 · paragraphs 15-16

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a459b819d5e86c346e44d95e504f96e0f0d006cb2d06da81252bc83ba8525232`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25606:2:subtheme:1 · paragraphs 15-16

- Raw key terms: `immigration, application, arises, back, board, cause, certification, citizenship`
- Display key terms: `arises, back, certification`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: arises, back, certification Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that the application for judicial review is granted. Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5205369` offsets `294-302`; context: No question for certification has been proposed and the Court finds that none arises.
- Evidence: `disposition` cue `granted` at chunk `5205369` offsets `131-138`; context: JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is granted.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is granted. The matter is referred back to the Immigration Refugee Board for reconsideration before a different member of the Board’s Refugee Protection Division. No question for certification has been proposed and the Court finds that none arises.
"Donald J. Rennie"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-3840-11
STYLE OF CAUSE: LIZ COOPER v. THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING: Toronto
DATE OF HEARING: December 13, 2011
REASONS FOR 

## 25606:3 · paragraphs 17-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `efda16ddd403abf9919132da4e267def9771f280745e96e9c9ed8ba5402a31a4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 25606:3:subtheme:1 · paragraphs 17-17

- Raw key terms: `appearances, applicant, attorney, babalola, barristers, canada, dated, deputy`
- Display key terms: `babalola, barristers, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: babalola, barristers, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 17-17. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: RENNIE J.
DATED: January 31, 2012
APPEARANCES:
Mr. Richard Odeleye
FOR THE APPLICANT
Ms. Jane Stewart
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Babalola, Odeleye
Barristers & Solicitors
North York, Ontario
FOR THE APPLICANT
Myles J. Kirvan,
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
