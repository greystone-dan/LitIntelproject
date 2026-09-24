# Discussion Units: case 33288

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **22**
- Continuity pairs: **21**
- Discussion Units: **2**
- Paragraph source hashes: **22**
- Sub-themes: **8**

## 33288:1 · paragraphs 0-19

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `52a794bc94822430e3718d710f855b87f4f96f6568e27566ffe02d833ee0231b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 33288:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `august, canada, decision, family, immigration, yanfen, accompanying, allegedly`
- Display key terms: `august, family, yanfen, accompanying, allegedly`
- Argument roles: `counterargument_limitation, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, party_position, reasoning_application Display terms: august, family, yanfen, accompanying, allegedly Position/evidence statements: [2] The Applicants claimed to be citizens of the People’s Republica of China who were fleeing from persecution related to that country’s family planning policies and Ms. Application context: Liu claimed, however, that their remaining identity documents including their Household Register (hukou), their resident identity cards (RIC’s), and their birth and marriage certificates were all genuine and, therefore,  Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claimed` at chunk `5543515` offsets `19-26`; context: [2] The Applicants claimed to be citizens of the People’s Republica of China who were fleeing from persecution related to that country’s family planning policies and Ms.
- Evidence: `reasoning_application` cue `therefore` at chunk `5543515` offsets `821-830`; context: Liu claimed, however, that their remaining identity documents including their Household Register (hukou), their resident identity cards (RIC’s), and their birth and marriage certificates were all genuine and, therefore, sufficient to establish identity.
- Evidence: `counterargument_limitation` cue `however` at chunk `5543515` offsets `625-632`; context: Liu claimed, however, that their remaining identity documents including their Household Register (hukou), their resident identity cards (RIC’s), and their birth and marriage certificates were all genuine and, therefore, sufficient to establish identity.

#### 33288:1:subtheme:2 · paragraphs 3-5

- Raw key terms: `board, documents, addressed, applicants, birth, certificates, claimant, claimed`
- Display key terms: `documents, addressed, birth, certificates, claimed`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: documents, addressed, birth, certificates, claimed Position/evidence statements: It is apparent from the transcript that counsel for the Applicants had some reservations about the Board’s claimed expertise as is reflected in the following exchange: PRESIDING MEMBER: Now, there’s one thing about each  Application context: PRESIDING MEMBER: Well, my question is that because this hukou and the other - - sorry, this birth certificate and the other two birth certificates all have very straight edges, it’s apparent to me that nothing has been  Evidence spans paragraphs 3-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5543516` offsets `282-287`; context: Liu was later questioned on this issue, she claimed that they had given their original RIC’s to the two snakeheads and had unknowingly received, in return, the forged copies upon arrival in Canada.
- Evidence: `evidence_fact` cue `evidence` at chunk `5543516` offsets `654-662`; context: She testified that the documents before the Board were valid originals but she was unable to offer much evidence that directly addressed the Board’s authenticity concerns.
- Evidence: `issue` cue `question` at chunk `5543517` offsets `932-940`; context: PRESIDING MEMBER: Well, my question is that because this hukou and the other - - sorry, this birth certificate and the other two birth certificates all have very straight edges, it’s apparent to me that nothing has been torn off, because usually that edge is perforated.
- Evidence: `party_position` cue `claimed` at chunk `5543517` offsets `296-303`; context: It is apparent from the transcript that counsel for the Applicants had some reservations about the Board’s claimed expertise as is reflected in the following exchange:
PRESIDING MEMBER: Now, there’s one thing about each of the birth certificates that I want to ask you about.
- Evidence: `reasoning_application` cue `because` at chunk `5543517` offsets `949-956`; context: PRESIDING MEMBER: Well, my question is that because this hukou and the other - - sorry, this birth certificate and the other two birth certificates all have very straight edges, it’s apparent to me that nothing has been torn off, because usually that edge is perforated.
- Evidence: `evidence_fact` cue `evidence` at chunk `5543518` offsets `135-143`; context: [5] The Board rejected the Applicants’ claims on the basis that the Applicants had failed to produce sufficient credible documents and evidence to establish their identities as required by section 106 of the Immigration Refugee and Protection Act, S.

#### 33288:1:subtheme:3 · paragraphs 6-8

- Raw key terms: `board, documents, identity, applicants, assessment, issues, review, standard`
- Display key terms: `documents, identity, assessment, issues, review, standard`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: documents, identity, assessment, issues, review, standard Position/evidence statements: The Board also found that the Applicants had knowingly submitted false documents as proof of their identities. Rule/authority context: [7] (a) What is the appropriate standard of review for the issues raised on this application? | [8] It is well established that the standard of review for the Board’s assessment of identity documents is patent unreasonableness. Application context: Liu’s explanation for how that may have happened was improbable; (b) that the authenticity of the hukou was “questionable” on its face because the document appeared to have been disassembled; (c) that Ms. Evidence spans paragraphs 6-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5543519` offsets `873-879`; context: Issues
- Evidence: `party_position` cue `submitted` at chunk `5543519` offsets `160-169`; context: The Board also found that the Applicants had knowingly submitted false documents as proof of their identities.
- Evidence: `evidence_fact` cue `testimony` at chunk `5543519` offsets `69-78`; context: Liu’s testimony with respect to identity.
- Evidence: `reasoning_application` cue `because` at chunk `5543519` offsets `473-480`; context: Liu’s explanation for how that may have happened was improbable;
(b) that the authenticity of the hukou was “questionable” on its face because the document appeared to have been disassembled;
(c) that Ms.
- Evidence: `issue` cue `issues` at chunk `5543520` offsets `59-65`; context: [7] (a) What is the appropriate standard of review for the issues raised on this application?
- Evidence: `governing_rule` cue `standard of review` at chunk `5543520` offsets `32-50`; context: [7] (a) What is the appropriate standard of review for the issues raised on this application?
- Evidence: `governing_rule` cue `standard of review` at chunk `5543521` offsets `36-54`; context: [8] It is well established that the standard of review for the Board’s assessment of identity documents is patent unreasonableness.

#### 33288:1:subtheme:4 · paragraphs 9-11

- Raw key terms: `applicants, board, finding, application, balance, cards, claimants, counsel`
- Display key terms: `finding, balance, cards`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: finding, balance, cards Position/evidence statements: Its finding on this issue was expressed as follows: I therefore reject the claimants’ attempts to avoid responsibility for the cards, which they themselves submitted, and find on a balance of probabilities that the claim | [11] The Applicants contend that the Board erred in the application of its claimed specialized knowledge in the authentication of some of their identity documents. Application context: Its finding on this issue was expressed as follows: I therefore reject the claimants’ attempts to avoid responsibility for the cards, which they themselves submitted, and find on a balance of probabilities that the claim | Accordingly, there is nothing about the Board’s approach to this issue which constitutes an analytical error. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5543522` offsets `459-464`; context: Its finding on this issue was expressed as follows:
I therefore reject the claimants’ attempts to avoid responsibility for the cards, which they themselves submitted, and find on a balance of probabilities that the claimants knowingly submitted false cards.
- Evidence: `party_position` cue `submitted` at chunk `5543522` offsets `595-604`; context: Its finding on this issue was expressed as follows:
I therefore reject the claimants’ attempts to avoid responsibility for the cards, which they themselves submitted, and find on a balance of probabilities that the claimants knowingly submitted false cards.
- Evidence: `reasoning_application` cue `therefore` at chunk `5543522` offsets `493-502`; context: Its finding on this issue was expressed as follows:
I therefore reject the claimants’ attempts to avoid responsibility for the cards, which they themselves submitted, and find on a balance of probabilities that the claimants knowingly submitted false cards.
- Evidence: `issue` cue `issue` at chunk `5543523` offsets `680-685`; context: Accordingly, there is nothing about the Board’s approach to this issue which constitutes an analytical error.
- Evidence: `evidence_fact` cue `evidence` at chunk `5543523` offsets `190-198`; context: It requires only that the Board weigh the conflicting pieces of evidence to determine which is the more likely event or explanation.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5543523` offsets `615-626`; context: Accordingly, there is nothing about the Board’s approach to this issue which constitutes an analytical error.
- Evidence: `party_position` cue `contend` at chunk `5543524` offsets `20-27`; context: [11] The Applicants contend that the Board erred in the application of its claimed specialized knowledge in the authentication of some of their identity documents.
- Evidence: `reasoning_application` cue `because` at chunk `5543524` offsets `1478-1485`; context: This is also because fraudulent documents are so readily available in China.
- Evidence: `counterargument_limitation` cue `However` at chunk `5543524` offsets `1169-1176`; context: However, when I assess these documents in light of the fact that the claimants presented both a fraudulent Household Register and fraudulent Resident Identity Cards, and that these are the two most reliable documents from China, I give both the marriage and the birth certificates little weight.

#### 33288:1:subtheme:5 · paragraphs 12-14

- Raw key terms: `applicants, board, argument, challenge, claim, issue, knowledge, problem`
- Display key terms: `argument, challenge, knowledge, problem`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: argument, challenge, knowledge, problem Position/evidence statements: [1] The problem with this argument is that the Applicants neither put evidence before the Board to challenge its claim to specialized knowledge nor requested an adjournment to seek out such evidence. | [13] By failing to take this issue further, the Applicants clearly waived the opportunity to challenge the basis of the Board’s claim to specialized knowledge and therefore there is no evidentiary foundation to support t Application context: In the absence of such evidence to support the objection, I am left with a finding that, on its face, is sound and well within the Board’s authority to apply its specialized knowledge. | [13] By failing to take this issue further, the Applicants clearly waived the opportunity to challenge the basis of the Board’s claim to specialized knowledge and therefore there is no evidentiary foundation to support t Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5543525` offsets `132-137`; context: [12] Counsel for the Applicants challenged the Board’s reliance on specialized knowledge and pointed to counsel’s objection on this issue made during the hearing.
- Evidence: `party_position` cue `claim` at chunk `5543525` offsets `275-280`; context: [1] The problem with this argument is that the Applicants neither put evidence before the Board to challenge its claim to specialized knowledge nor requested an adjournment to seek out such evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5543525` offsets `232-240`; context: [1] The problem with this argument is that the Applicants neither put evidence before the Board to challenge its claim to specialized knowledge nor requested an adjournment to seek out such evidence.
- Evidence: `reasoning_application` cue `apply` at chunk `5543525` offsets `514-519`; context: In the absence of such evidence to support the objection, I am left with a finding that, on its face, is sound and well within the Board’s authority to apply its specialized knowledge.
- Evidence: `issue` cue `issue` at chunk `5543526` offsets `29-34`; context: [13] By failing to take this issue further, the Applicants clearly waived the opportunity to challenge the basis of the Board’s claim to specialized knowledge and therefore there is no evidentiary foundation to support the argument on judicial review.
- Evidence: `party_position` cue `claim` at chunk `5543526` offsets `128-133`; context: [13] By failing to take this issue further, the Applicants clearly waived the opportunity to challenge the basis of the Board’s claim to specialized knowledge and therefore there is no evidentiary foundation to support the argument on judicial review.
- Evidence: `reasoning_application` cue `therefore` at chunk `5543526` offsets `163-172`; context: [13] By failing to take this issue further, the Applicants clearly waived the opportunity to challenge the basis of the Board’s claim to specialized knowledge and therefore there is no evidentiary foundation to support the argument on judicial review.

#### 33288:1:subtheme:6 · paragraphs 15-18

- Raw key terms: `applicants, board, canada, citizenship, documents, establish, identity, minister`
- Display key terms: `documents, establish, identity`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: documents, establish, identity Application context: The burden was on the respondent to establish that living in Colombo was not an internal flight alternative because of the alleged three-day policy. Operative outcome context: 2118 where the Court reflected on this problem in the following passage: I am of the view that the Board cannot be faulted for not having addressed in its reasons the fact that Tamils are not allowed to reside in Colombo Evidence spans paragraphs 15-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5543528` offsets `978-983`; context: It appears from a version of the transcript of the hearing before the Board that the respondent was represented by counsel at the hearing and never raised that issue with the Board.
- Evidence: `reasoning_application` cue `because` at chunk `5543528` offsets `1108-1115`; context: The burden was on the respondent to establish that living in Colombo was not an internal flight alternative because of the alleged three-day policy.
- Evidence: `disposition` cue `allowed` at chunk `5543528` offsets `763-770`; context: 2118 where the Court reflected on this problem in the following passage:
I am of the view that the Board cannot be faulted for not having addressed in its reasons the fact that Tamils are not allowed to reside in Colombo for more than three days.
- Evidence: `evidence_fact` cue `determined that` at chunk `5543531` offsets `92-107`; context: [18] Having concluded that the Applicants had failed to establish their identity, the Board determined that it need not go further to consider their evidence of persecution.

#### 33288:1:subtheme:7 · paragraphs 19-19

- Raw key terms: `application, arises, certified, dismissed, general, importance, issue, neither`
- Display key terms: `arises, certified, dismissed, importance, neither`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: arises, certified, dismissed, importance, neither Operative outcome context: [19] In the result, this application is dismissed. Evidence spans paragraphs 19-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5543532` offsets `86-94`; context: Neither party proposed a certified question and no issue of general importance arises on this record.
- Evidence: `evidence_fact` cue `record` at chunk `5543532` offsets `145-151`; context: Neither party proposed a certified question and no issue of general importance arises on this record.
- Evidence: `disposition` cue `dismissed` at chunk `5543532` offsets `40-49`; context: [19] In the result, this application is dismissed.

#### Section text

Liu v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2007-08-10
Neutral citation
2007 FC 831
File numbers
IMM-4384-06
Decision Content
.
Date: 20070810
Docket: IMM-4384-06
Citation: 2007 FC 831
Ottawa, Ontario, August 10, 2007
PRESENT: The Honourable Mr. Justice Barnes
BETWEEN:
YANFEN LIU (a.k.a. Yan Fen Liu)
ZHI XIN CHEN (a minor)
ZHEN YI CHEN (a minor)
MEI YU CHEN (a minor)
YUN CHEN
Applicant(s)
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent(s)
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review brought by Yanfen Liu and her family from a negative decision of the Refugee Protection Division of the Immigration and Refugee Board (Board) rendered on July 12, 2006.
Background

[2] The Applicants claimed to be citizens of the People’s Republica of China who were fleeing from persecution related to that country’s family planning policies and Ms. Liu’s involvement with the Falun Gong movement. Ms. Liu left China with her three children in March 2003 with the assistance of a smuggler or “snakehead.” Her husband followed and arrived in Canada in August 2003. He, too, travelled here with the assistance of a snakehead. It was undisputed that the Applicants came to Canada from Hong Kong with false passports which were allegedly returned to the accompanying snakeheads upon arrival. Ms. Liu claimed, however, that their remaining identity documents including their Household Register (hukou), their resident identity cards (RIC’s), and their birth and marriage certificates were all genuine and, therefore, sufficient to establish identity.

[3] The Board apparently had reservations about the authenticity of the tendered identity documents and submitted the RIC’s to the Royal Canadian Mounted Police (RCMP) for forensic analysis. The RCMP reported that the RIC’s were forgeries. When Ms. Liu was later questioned on this issue, she claimed that they had given their original RIC’s to the two snakeheads and had unknowingly received, in return, the forged copies upon arrival in Canada. Ms. Liu was also questioned about other perceived discrepancies with the hukou and birth certificates. She testified that the documents before the Board were valid originals but she was unable to offer much evidence that directly addressed the Board’s authenticity concerns. With respect to one dating anomaly, she offered the following testimony:
CLAIMANT #1: Well, it’s after I got married and then I received the hukou. When I got married I received the hukou, I received this hukou.
PRESIDING MEMBER: What year was that?
CLAIMANT #1: I was married in 1989.
PRESIDING MEMBER: So, did you receive this hukou in 1989?
CLAIMANT #1: Yes.
PRESIDING MEMBER: Well, the translation says it was registered on November 18th, 1999.
CLAIMANT #1: If that is so, then I don’t really quite remember. It was after I married with my husband that I got this hukou, but if it’s written like that, I really am not sure what it is, and it’s after we got married that I received this hukou.

[4] During the hearing, the Board gave notice to the Applicants that it intended to rely upon specialized knowledge with respect to the expected presentation of Chinese birth certificates. It is apparent from the transcript that counsel for the Applicants had some reservations about the Board’s claimed expertise as is reflected in the following exchange:
PRESIDING MEMBER: Now, there’s one thing about each of the birth certificates that I want to ask you about. I have what I would describe as specialized knowledge and that is that when a birth certificate is issued there’s a small attachment on the right-hand side, and that attachment is used in order to have the name added to the hukou. In fact, it says right on the form that that part is to be given to the person who changes the hukou.
CLAIMANT #1: Well, that part I don’t really know. So, it’s the person who helped me deliver gave it to me.
PRESIDING MEMBER: Well, my question is that because this hukou and the other - - sorry, this birth certificate and the other two birth certificates all have very straight edges, it’s apparent to me that nothing has been torn off, because usually that edge is perforated. Counsel, do you want to see?
COUNSEL: My problem is your knowledge, is it based back decades, your specialized knowledge?
PRESIDING MEMBER: We’ll come back to that.
COUNSEL: I mean, I trust if you say there’s no perforation there’s no perforation, but I don’t know what that means 10, 15 years ago.
PRESIDING MEMBER: Do you have any comment, Ma’am, on what I’m saying?
CLAIMANT #1: I don’t have anything to say. You asked me a question and I will answer you.
PRESIDING MEMBER: My question is: Do you know why the birth certificate doesn’t have a perforated edge?
CLAIMANT #1: That part I don’t know. All I know is when I gave birth, the person who help me deliver gave me the certificate. I check out if the name is correct, and then we just put it away.
Notwithstanding the above statement that the Board intended to come back to counsel’s concern, the issue was not addressed again until final submissions when counsel challenged the Board’s claim to specialized knowledge with the following statement:
There was some discussion about the documents, themselves, and while we do have some information, and the Board may have some specialized knowledge regarding birth certificates, surely they have taken many forms over the years and there was no consistency throughout the country, and accordingly I would submit that it would be impossible to say with any certainty whether documents from that particular time period must have had - - must have a perforated edge.
The Board Decision

[5] The Board rejected the Applicants’ claims on the basis that the Applicants had failed to produce sufficient credible documents and evidence to establish their identities as required by section 106 of the Immigration Refugee and Protection Act, S.C. 2001, c.27, (IRPA). Having made that finding, it declined to assess their allegations of persecution.

[6] The Board’s decision indicates that it did not believe Ms. Liu’s testimony with respect to identity. The Board also found that the Applicants had knowingly submitted false documents as proof of their identities. Those conclusions were based on several specific findings including the following:
(a) that the RIC’s were forged and Ms. Liu’s explanation for how that may have happened was improbable;
(b) that the authenticity of the hukou was “questionable” on its face because the document appeared to have been disassembled;
(c) that Ms. Liu’s explanations for the dating inconsistencies on the hukou were “unsatisfactory” and the cumulative problems with the documents led the Board to conclude that it was fraudulent; and
(d) that the birth certificates were not in the expected form based on the Board’s specialized knowledge and, therefore, carried little weight.
Issues

[7] (a) What is the appropriate standard of review for the issues raised on this application?
(b) Did the Board commit a reviewable error in its assessment of the Applicants’ identity documents?
Analysis

[8] It is well established that the standard of review for the Board’s assessment of identity documents is patent unreasonableness. In Ipala v. Canada (Minister of Citizenship), 2005 FC 472, [2005] F.C.J. No. 583, Justice Edmond Blanchard noted that this heightened level of deference to the Board’s assessment of identity documents is justified by its first-hand access to those documents and by its high level of expertise in this area (see para. 18).

[9] Counsel for the Applicants characterized the Board’s rejection of Ms. Liu’s explanation for tendering the forged RIC’s as a plausibility finding. He contended that, since her explanation was not outside of the realm of reasonable possibilities, it should not have been characterized as implausible. The problem with this argument is that the Board did not find Ms. Liu’s explanation implausible but, rather, found it to be improbable. Its finding on this issue was expressed as follows:
I therefore reject the claimants’ attempts to avoid responsibility for the cards, which they themselves submitted, and find on a balance of probabilities that the claimants knowingly submitted false cards.

[10] A factual finding reached on a balance of probabilities need not exclude all other rational or reasonable possibilities. It requires only that the Board weigh the conflicting pieces of evidence to determine which is the more likely event or explanation. That is precisely what the Board did in concluding that it was unlikely that two different snakeheads would substitute forgeries which were exact duplications of the Applicants’ authentic RIC’s. The simple application of common sense to factual findings of this sort does not transform a finding of fact based on probabilities into a plausibility finding. Accordingly, there is nothing about the Board’s approach to this issue which constitutes an analytical error.

[11] The Applicants contend that the Board erred in the application of its claimed specialized knowledge in the authentication of some of their identity documents. In particular, the Board found discrepancies between the presentation of the birth certificates and the hukou and its knowledge of what those documents should look like. With respect to the birth certificates, the Board’s finding was as follows:
In the hearing I declared specialized knowledge with respect to birth certificates in that genuine birth certificates normally have a perforated right edge where the tear-off portion has been removed. The three certificates before me in this hearing had a straight, cleanly cut right edge. Both the claimants and counsel were given an opportunity to comment. Counsel stated that she was not sure what my specialized knowledge would mean with respect to a birth certificate issued 10 to 15 years ago. The principal claimant said that she did not know why the birth certificates had no perforated edge, only that the person who helped her deliver her children had given her those certificates, that she had checked the names and then put the certificates away. However, when I assess these documents in light of the fact that the claimants presented both a fraudulent Household Register and fraudulent Resident Identity Cards, and that these are the two most reliable documents from China, I give both the marriage and the birth certificates little weight. This is also because fraudulent documents are so readily available in China.

[12] Counsel for the Applicants challenged the Board’s reliance on specialized knowledge and pointed to counsel’s objection on this issue made during the hearing.[1] The problem with this argument is that the Applicants neither put evidence before the Board to challenge its claim to specialized knowledge nor requested an adjournment to seek out such evidence. In the absence of such evidence to support the objection, I am left with a finding that, on its face, is sound and well within the Board’s authority to apply its specialized knowledge.

[13] By failing to take this issue further, the Applicants clearly waived the opportunity to challenge the basis of the Board’s claim to specialized knowledge and therefore there is no evidentiary foundation to support the argument on judicial review.

[14] Essentially the same problem arises with respect to the Applicants’ contention that the Board should have addressed other documents which were tendered to establish their claims to persecution. Some of those documents contained identification information which arguably could corroborate the primary identification documents which they were relying upon.

[15] While it is correct that the Board made no mention of the potential significance of those collateral documents, it is also the case that the attention of the Board was not drawn to this point. If the documents had insufficient evidentiary value to warrant any specific comment from the Applicants’ counsel, it is not surprising that the Board apparently did not factor them into its authenticity assessment. On this point I adopt the view of the Federal Court of Appeal in Canada (Minister of Citizenship) v. Ranganathan, [2001] 2 F.C. 164 (C.A.), [2000] F.C.J. No. 2118 where the Court reflected on this problem in the following passage:
I am of the view that the Board cannot be faulted for not having addressed in its reasons the fact that Tamils are not allowed to reside in Colombo for more than three days. It appears from a version of the transcript of the hearing before the Board that the respondent was represented by counsel at the hearing and never raised that issue with the Board. The burden was on the respondent to establish that living in Colombo was not an internal flight alternative because of the alleged three-day policy. One would have expected her to raise that issue if it was really a serious concern to her. But she did not and the Board was entitled to assume that this was a non-issue especially as she had lived there for four years before departing for Canada in 1997.

[16] The argument that the Applicants should have been warned about the Board’s doubts about Ms. Liu’s explanation for tendering the forged RIC’s has no merit. Ms. Liu was given the opportunity to explain how they came to possess these documents. Anything beyond the explanation that she gave would presumably have called for speculation. She was also well aware of the Board’s concern that the family had relied upon forged documents to establish their identity. Given, as well, that the Applicants were represented at the hearing, nothing prevented them from offering additional details to advance any helpful point the Board may have overlooked in its questioning. The points which the Board later expressed scepticism about were obvious and did not require any forewarning beyond what was given.

[17] The Applicants’ arguments about the hukou are similarly unmeritorious. The Board was entitled to be concerned about the appearance of the hukou and Ms. Liu was questioned about its condition. The findings that it appeared to have been taken apart and reassembled and that it also contained dating anomalies were obvious and did not require forensic analysis. These are the types of common-sense observations that the Board may rely upon to draw conclusions about the authenticity of identity documents: see Hossain v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 160 at para. 4, Wang v. Canada (Minister of Citizenship and Immigration), 2001 FCT 590, [2001] F.C.J. No. 911 at paras. 18 and 19, Akindele v. Canada (Minister of Citizenship and Immigration), 2002 FCT 37, [2002] F.C.J. No. 68 at para. 5 and Adar v. Canada (Minister of Citizenship and Immigration), [1997] F.C.J. No. 695 at para. 16.

[18] Having concluded that the Applicants had failed to establish their identity, the Board determined that it need not go further to consider their evidence of persecution. It is well established that proof of identity is a pre-requisite for a person claiming refugee protection. As was stated in Jin v. Canada (Minister of Citizenship and Immigration), 2006 FC 126, [2006] F.C.J. No. 181, without the foundation of identity there can “be no sound basis for testing or verifying the claims of persecution or, indeed, for determining the Applicant’s true nationality” (para. 26); see also Husein v. Canada (Minister of Citizenship and Immigration), [1998] F.C.J. 726.

[19] In the result, this application is dismissed. Neither party proposed a certified question and no issue of general importance arises on this record.


## 33288:2 · paragraphs 20-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1369875cf3a34e22d5f72a4b2c995da0d4818e9f83ff6937abb835a431c00422`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 33288:2:subtheme:1 · paragraphs 20-21

- Raw key terms: `application, counsel, adjudges, anderson, appearances, appeared, applicant, associates`
- Display key terms: `adjudges, anderson, appeared, associates`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: adjudges, anderson, appeared, associates No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT ADJUDGES that this application is dismissed.
“ R. L. Barnes ”
Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-4384-06
STYLE OF CAUSE: YANFEN LIU ET AL v. MCI
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: JULY 26, 2007
REASONS FOR ORDER: BARNES, J.
DATED: August 10, 2007
APPEARANCES:
LEONARD H. BORENSTEIN FOR THE APPLICANT
MARTIN ANDERSON FOR THE RESPONDENT
SOLICITORS OF RECORD:
LEWIS & ASSOCIATES
BARRISTERS & SOLICITORS
41 MADISON AVENUE FOR THE APPLICANT
TORONTO, ON, M5R 2S2
P: 416-924-2227
F: 416-924-9993
JOHN H. SIMS, QC FOR THE RESPONDENT
TORONTO, ON
P: 416-952-2856
F: 416-954-8982

[1] Counsel attending on this application for judicial review was not the same counsel who appeared before the Board.
