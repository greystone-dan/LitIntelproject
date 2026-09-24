# Discussion Units: case 3761

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **26**
- Continuity pairs: **25**
- Discussion Units: **4**
- Paragraph source hashes: **26**
- Sub-themes: **13**

## 3761:1 · paragraphs 0-3

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b56af9d5c576f30b229d45ad8437efbdd2a23b75fd63902793ac5d23d6fc1da0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3761:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `immigration, nemeth, adjournment, applicants, application, asked, assist, attend`
- Display key terms: `nemeth, adjournment, asked, assist, attend`
- Argument roles: `counterargument_limitation`
- Explanation: Observed roles: counterargument_limitation Display terms: nemeth, adjournment, asked, assist, attend Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `4226234` offsets `265-272`; context: However, on such short notice, the lawyer was unable to attend the hearing.

#### 3761:1:subtheme:2 · paragraphs 2-3

- Raw key terms: `board, claim, agnes, appeared, because, circumstances, claimant, counsel`
- Display key terms: `agnes, appeared, because, circumstances`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: agnes, appeared, because, circumstances Rule/authority context: Claimant #1: Yes, I think so, because I think in our situation or under our circumstances, we have no need of a counsel. Application context: Claimant #1: Yes, I think so, because I think in our situation or under our circumstances, we have no need of a counsel. Operative outcome context: It dismissed the Nemeths' claim orally and issued written reasons several weeks later. Evidence spans paragraphs 2-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4226235` offsets `479-484`; context: Claimant #1: Yes, I think so, because I think in our situation or under our circumstances, we have no need of a counsel.
- Evidence: `reasoning_application` cue `because` at chunk `4226235` offsets `443-450`; context: Claimant #1: Yes, I think so, because I think in our situation or under our circumstances, we have no need of a counsel.
- Evidence: `evidence_fact` cue `evidence` at chunk `4226236` offsets `36-44`; context: [3] The Board proceeded to hear the evidence.
- Evidence: `disposition` cue `dismissed` at chunk `4226236` offsets `49-58`; context: It dismissed the Nemeths' claim orally and issued written reasons several weeks later.

#### Section text

Nemeth v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2003-05-14
Neutral citation
2003 FCT 590
File numbers
IMM-2522-02
Decision Content
Date: 20030514
Docket: IMM-2522-02
Citation: 2003 FCT 590
Ottawa, Ontario, this 14th day of May, 2003
Present: THE HONOURABLE MR. JUSTICE O'REILLY
BETWEEN:
IMRE JANOS NEMETH, IMRENE NEMETH
AND NIKOLETT MARIA NEMETH
Applicants
- and -
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] The Nemeth family engaged an immigration consultant to assist them with their application for refugee status. Six days prior to their hearing before the Immigration and Refugee Board in March of 2002, they decided to dismiss the consultant and engage a lawyer. However, on such short notice, the lawyer was unable to attend the hearing. He sent a letter to the Board explaining the situation and asked for an adjournment. The Board did not respond.

[2] The Nemeths appeared before the Board on the date of the hearing. The following exchange between the Presiding Board member and Mr. Nemeth took place:
Presiding member: We were expecting you to be represented by Ms. Agnes Schiffer Varnai. Does she remain your counsel, sir, or have you dispensed with her?
Claimant #1: No.
Presiding member: And you are going to proceed in this claim today without a counsel?
Claimant #1: Yes, I think so, because I think in our situation or under our circumstances, we have no need of a counsel.
Presiding member: All right. Thank you.

[3] The Board proceeded to hear the evidence. It dismissed the Nemeths' claim orally and issued written reasons several weeks later.


## 3761:2 · paragraphs 4-11

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ffec8a26dbe1e2f18446230c9e11d254eda09e238577d56b8c436898df287de2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3761:2:subtheme:1 · paragraphs 4-5

- Raw key terms: `issues, alleged, board, case, claim, concluding, convention, counsel`
- Display key terms: `issues, alleged, case, concluding, convention`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: issues, alleged, case, concluding, convention Rule/authority context: Did the Board make an error in concluding that the Nemeths had failed to show a nexus between the mistreatment they alleged and the recognized grounds for a refugee claim under the Refugee Convention? Operative outcome context: Were the Nemeths denied their right to be represented by counsel? Evidence spans paragraphs 4-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4226237` offsets `20-26`; context: [4] There are three issues in this case.
- Evidence: `governing_rule` cue `under` at chunk `4226237` offsets `327-332`; context: Did the Board make an error in concluding that the Nemeths had failed to show a nexus between the mistreatment they alleged and the recognized grounds for a refugee claim under the Refugee Convention?
- Evidence: `disposition` cue `denied` at chunk `4226237` offsets `61-67`; context: Were the Nemeths denied their right to be represented by counsel?

#### 3761:2:subtheme:2 · paragraphs 6-9

- Raw key terms: `right, board, counsel, denied, hearing, nemeths, represented, adjournment`
- Display key terms: `right, denied, hearing, nemeths, represented, adjournment`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: right, denied, hearing, nemeths, represented, adjournment Rule/authority context: [6] The Board is under no obligation to function in accordance with the schedule of counsel. Application context: ), a claimant has the right to choose counsel, but "if the counsel he chooses is not able to appear because he is too busy or for any other reason, he cannot expect the tribunal to adjust to the requirements of that coun | [8] Therefore, I can see no basis for the claim that the Board denied the Nemeths their right to be represented at the hearing. Operative outcome context: If the Board fails to grant an adjournment in that situation, the right to counsel has effectively been denied. | Nemeth stated in his affidavit that he had explained the situation to the Board and expressly requested an adjournment, which the Board denied. Evidence spans paragraphs 6-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4226238` offsets `284-292`; context: The question is whether the Board's failure to adjourn the hearing in order to accommodate the lawyer amounted, in effect, to a violation of the Nemeths' right to be represented at the hearing.
- Evidence: `governing_rule` cue `under` at chunk `4226239` offsets `17-22`; context: [6] The Board is under no obligation to function in accordance with the schedule of counsel.
- Evidence: `reasoning_application` cue `because` at chunk `4226239` offsets `311-318`; context: ), a claimant has the right to choose counsel, but "if the counsel he chooses is not able to appear because he is too busy or for any other reason, he cannot expect the tribunal to adjust to the requirements of that counsel" (at para.
- Evidence: `disposition` cue `denied` at chunk `4226239` offsets `845-851`; context: If the Board fails to grant an adjournment in that situation, the right to counsel has effectively been denied.
- Evidence: `evidence_fact` cue `evidence` at chunk `4226240` offsets `438-446`; context: I see no evidence of that.
- Evidence: `disposition` cue `denied` at chunk `4226240` offsets `596-602`; context: Nemeth stated in his affidavit that he had explained the situation to the Board and expressly requested an adjournment, which the Board denied.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4226241` offsets `4-13`; context: [8] Therefore, I can see no basis for the claim that the Board denied the Nemeths their right to be represented at the hearing.
- Evidence: `disposition` cue `denied` at chunk `4226241` offsets `63-69`; context: [8] Therefore, I can see no basis for the claim that the Board denied the Nemeths their right to be represented at the hearing.

#### 3761:2:subtheme:3 · paragraphs 10-11

- Raw key terms: `board, ensure, hearing, nemeths, obligation, represented, alive, answer`
- Display key terms: `ensure, hearing, nemeths, obligation, represented, alive, answer`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: ensure, hearing, nemeths, obligation, represented, alive, answer Rule/authority context: Under the circumstances, it had an obligation to ensure that the Nemeths understood the proceedings, had a reasonable opportunity to tender any evidence that supported their claim and were given a chance to persuade the  Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4226242` offsets `29-37`; context: [9] This is a more difficult question to answer.
- Evidence: `evidence_fact` cue `evidence` at chunk `4226243` offsets `352-360`; context: Under the circumstances, it had an obligation to ensure that the Nemeths understood the proceedings, had a reasonable opportunity to tender any evidence that supported their claim and were given a chance to persuade the Board that their claims were well-founded.
- Evidence: `governing_rule` cue `Under` at chunk `4226243` offsets `208-213`; context: Under the circumstances, it had an obligation to ensure that the Nemeths understood the proceedings, had a reasonable opportunity to tender any evidence that supported their claim and were given a chance to persuade the Board that their claims were well-founded.

#### Section text

I. Issues

[4] There are three issues in this case.
1. Were the Nemeths denied their right to be represented by counsel?
2. Did the Nemeths receive a fair hearing?
3. Did the Board make an error in concluding that the Nemeths had failed to show a nexus between the mistreatment they alleged and the recognized grounds for a refugee claim under the Refugee Convention?
A. Were the Nemeths denied their right to be represented by counsel?

[5] Refugee claimants are entitled to be represented by "a barrister, solicitor or other counsel" (s. 69(1), Immigration Act). Until just prior to their hearing, the Nemeths had been represented by an immigration consultant. They then decided to hire a lawyer at the last minute. The question is whether the Board's failure to adjourn the hearing in order to accommodate the lawyer amounted, in effect, to a violation of the Nemeths' right to be represented at the hearing.

[6] The Board is under no obligation to function in accordance with the schedule of counsel. As Dubé J. stated in Aseervatham v. Canada (Minister of Citizenship and Immigration), [2000] F.C.J. No. 804 (QL) (T.D.), a claimant has the right to choose counsel, but "if the counsel he chooses is not able to appear because he is too busy or for any other reason, he cannot expect the tribunal to adjust to the requirements of that counsel" (at para. 25). See also Afrane v. Canada (Minister of Employment and Immigration), [1993] F.C.J. No. 609 (QL) (T.D.). The situation is different if an applicant is abandoned by counsel at the last minute: see De Sousa v. Canada (Minister of Employment and Immigration), [1988] F.C.J. No. 569 (QL) (C.A.). If the Board fails to grant an adjournment in that situation, the right to counsel has effectively been denied. See also Siloch v. Canada (Minister of Employment and Immigration), [1993] F.C.J. No. 10 (QL) (C.A.); Castroman v. Canada (Secretary of State), [1994] F.C.J. No. 962 (QL) (T.D.); Dadi v. Canada (Minister of Citizenship and Immigration), [1999] F.C.J. No. 1243 (QL) (T.D.). In this case, the Nemeths were not abandoned by counsel. They dismissed her.

[7] Further, it is clear to me from the exchange between the Presiding Board member and Mr. Nemeth that there was a waiver of the right to be represented at the hearing. Mr. Nemeth stated that the family had no need of counsel. He did not ask for an adjournment. It was suggested during argument before me that the transcript of the hearing may be incomplete and that Mr. Nemeth may have asked for an adjournment during a break. I see no evidence of that. Mr. Nemeth stated in his affidavit that he had explained the situation to the Board and expressly requested an adjournment, which the Board denied. To my mind, the transcript is clear. Mr. Nemeth is either mistaken or he misunderstood what the Board had said.

[8] Therefore, I can see no basis for the claim that the Board denied the Nemeths their right to be represented at the hearing.
B. Did the Nemeths receive a fair hearing?

[9] This is a more difficult question to answer. While the Board did not deny the Nemeths the right to be represented, it still had an obligation to ensure a fair hearing.

[10] The Board was aware that the Nemeths had been represented up until just prior to the hearing. It was, or should have been, alive to the risk that the claimants were ill-prepared to represent themselves. Under the circumstances, it had an obligation to ensure that the Nemeths understood the proceedings, had a reasonable opportunity to tender any evidence that supported their claim and were given a chance to persuade the Board that their claims were well-founded.

## 3761:3 · paragraphs 12-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3df945cb4ae997ec247e536b833d33f38fd284c26503da17c770f7c5db5c4822`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3761:3:subtheme:1 · paragraphs 12-12

- Raw key terms: `accordingly, accuracy, acknowledged, activities, added, additional, anyone, applicant's`
- Display key terms: `accordingly, accuracy, acknowledged, activities, added, additional, anyone, applicant's`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: accordingly, accuracy, acknowledged, activities, added, additional, anyone, applicant's Application context: He said that he believed he had because a package of documents was sent to him. Operative outcome context: - The Board dismissed the family's claims orally and immediately. Evidence spans paragraphs 12-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4226244` offsets `1566-1572`; context: - The Board stated that it would limit the issues in the hearing to credibility and nexus.
- Evidence: `evidence_fact` cue `record` at chunk `4226244` offsets `25-31`; context: [11] I have reviewed the record of the proceedings and note the following events:
- At the beginning of the hearing, Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4226244` offsets `925-932`; context: He said that he believed he had because a package of documents was sent to him.
- Evidence: `disposition` cue `dismissed` at chunk `4226244` offsets `2844-2853`; context: - The Board dismissed the family's claims orally and immediately.

#### 3761:3:subtheme:2 · paragraphs 13-14

- Raw key terms: `counsel, fair, hearing, above, absence, absolve, actually, already`
- Display key terms: `fair, hearing, above, absence, absolve, actually, already`
- Argument roles: `counterargument_limitation, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, reasoning_application Display terms: fair, hearing, above, absence, absolve, actually, already Application context: Indeed, the Board's obligations in situations where claimants are without legal representation may actually be more onerous because it cannot rely on counsel to protect their interests. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `However` at chunk `4226245` offsets `70-77`; context: However, that does not mean, in itself, that the Nemeths did not receive a fair hearing.
- Evidence: `reasoning_application` cue `because` at chunk `4226246` offsets `366-373`; context: Indeed, the Board's obligations in situations where claimants are without legal representation may actually be more onerous because it cannot rely on counsel to protect their interests.

#### 3761:3:subtheme:3 · paragraphs 15-16

- Raw key terms: `adjournment, board, case, claim, counsel, explain, fair, further`
- Display key terms: `adjournment, case, explain, fair, further`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: adjournment, case, explain, fair, further Application context: [15] For similar reasons, I find that the Nemeths did not receive a fair hearing. Operative outcome context: ), that the claimant had been denied a fair hearing. Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4226247` offsets `92-99`; context: [14] In Castroman, above, after counsel had withdrawn, the Board failed to ask the claimant whether he wanted an adjournment.
- Evidence: `disposition` cue `denied` at chunk `4226247` offsets `446-452`; context: ), that the claimant had been denied a fair hearing.
- Evidence: `issue` cue `issue` at chunk `4226248` offsets `681-686`; context: (c) The case involved an issue of legal interpretation - whether the targeting of persons involved in business activities amounted to persecution because of "membership in a particular social group.
- Evidence: `evidence_fact` cue `record` at chunk `4226248` offsets `369-375`; context: While an adjournment should have also been requested by the Nemeths at the hearing, the Board should have at least inquired further into the matter of representation given that it was clearly aware that counsel of record had recently left the case.
- Evidence: `reasoning_application` cue `I find` at chunk `4226248` offsets `26-32`; context: [15] For similar reasons, I find that the Nemeths did not receive a fair hearing.

#### 3761:3:subtheme:4 · paragraphs 17-18

- Raw key terms: `board, claim, hearing, nemeths, refugee, ability, absence, accordingly`
- Display key terms: `hearing, nemeths, refugee, ability, absence, accordingly`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: hearing, nemeths, refugee, ability, absence, accordingly Position/evidence statements: Did the Board make an error in concluding that the Nemeths had failed to show a nexus between the mistreatment they alleged and the recognized grounds for a claim under the Refugee Convention? Rule/authority context: Did the Board make an error in concluding that the Nemeths had failed to show a nexus between the mistreatment they alleged and the recognized grounds for a claim under the Refugee Convention? Application context: [17] Accordingly, the Nemeths are entitled to a new hearing before a different panel of the Board. Operative outcome context: It could easily have permitted the Nemeths an opportunity to gather the documents on which their claim depended, allowed them sufficient time to respond to the other evidence before the Board, as well as the submissions  Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4226249` offsets `651-656`; context: It could easily have permitted the Nemeths an opportunity to gather the documents on which their claim depended, allowed them sufficient time to respond to the other evidence before the Board, as well as the submissions of the Refugee Claim Officer, and ensured that they understood the legal issue in their case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4226249` offsets `524-532`; context: It could easily have permitted the Nemeths an opportunity to gather the documents on which their claim depended, allowed them sufficient time to respond to the other evidence before the Board, as well as the submissions of the Refugee Claim Officer, and ensured that they understood the legal issue in their case.
- Evidence: `disposition` cue `allowed` at chunk `4226249` offsets `471-478`; context: It could easily have permitted the Nemeths an opportunity to gather the documents on which their claim depended, allowed them sufficient time to respond to the other evidence before the Board, as well as the submissions of the Refugee Claim Officer, and ensured that they understood the legal issue in their case.
- Evidence: `party_position` cue `claim` at chunk `4226250` offsets `259-264`; context: Did the Board make an error in concluding that the Nemeths had failed to show a nexus between the mistreatment they alleged and the recognized grounds for a claim under the Refugee Convention?
- Evidence: `governing_rule` cue `under` at chunk `4226250` offsets `265-270`; context: Did the Board make an error in concluding that the Nemeths had failed to show a nexus between the mistreatment they alleged and the recognized grounds for a claim under the Refugee Convention?
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4226250` offsets `5-16`; context: [17] Accordingly, the Nemeths are entitled to a new hearing before a different panel of the Board.

#### 3761:3:subtheme:5 · paragraphs 19-20

- Raw key terms: `conclusion, counsel, hearing, matter, representations, above, absence, activities`
- Display key terms: `conclusion, hearing, matter, representations, above, absence, activities`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: conclusion, hearing, matter, representations, above, absence, activities Position/evidence statements: [19] At the conclusion of the hearing in this matter, I asked counsel to submit in writing any representations they might have with respect to certification of a question of general importance and costs. Application context: While there is case law that casts doubt on whether mistreatment because of business activities can amount to persecution on grounds of "membership in a particular social group", this is another issue on which representa Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4226251` offsets `36-41`; context: [18] As mentioned above, this legal issue came up before the Board and figured largely in its reasons.
- Evidence: `evidence_fact` cue `record` at chunk `4226251` offsets `738-744`; context: Further, by definition, the absence of a fair hearing means there is no proper factual record before me on which to decide the legal issue.
- Evidence: `reasoning_application` cue `because` at chunk `4226251` offsets `297-304`; context: While there is case law that casts doubt on whether mistreatment because of business activities can amount to persecution on grounds of "membership in a particular social group", this is another issue on which representations from counsel would have been helpful.
- Evidence: `issue` cue `question` at chunk `4226252` offsets `162-170`; context: [19] At the conclusion of the hearing in this matter, I asked counsel to submit in writing any representations they might have with respect to certification of a question of general importance and costs.
- Evidence: `party_position` cue `submit` at chunk `4226252` offsets `73-79`; context: [19] At the conclusion of the hearing in this matter, I asked counsel to submit in writing any representations they might have with respect to certification of a question of general importance and costs.

#### 3761:3:subtheme:6 · paragraphs 21-22

- Raw key terms: `above, because, board, galati, order, record, adjourn, adjournment`
- Display key terms: `above, because, galati, order, adjourn, adjournment`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: above, because, galati, order, adjourn, adjournment Application context: With respect to the first issue, it is inappropriate to certify a question because the case law is well settled and, in any case, I have decided the issue primarily on the basis of waiver. | For its part, the respondent had originally sought costs because of the alleged misrepresentation. Operative outcome context: Nemeth said that the Board specifically denied an adjournment, yet no such denial appears on the record. Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4226253` offsets `53-61`; context: Galati, counsel for the Nemeths, proposed a question regarding the duty of the Board to adjourn in order to protect the right to counsel, and another with respect to the issue of nexus, discussed briefly above.
- Evidence: `evidence_fact` cue `record` at chunk `4226253` offsets `564-570`; context: As mentioned, given that there has not been a fair hearing, the factual record is unreliable.
- Evidence: `reasoning_application` cue `because` at chunk `4226253` offsets `295-302`; context: With respect to the first issue, it is inappropriate to certify a question because the case law is well settled and, in any case, I have decided the issue primarily on the basis of waiver.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4226254` offsets `127-136`; context: Galati is seeking costs on the grounds that the respondent inappropriately characterized the affidavit of Mr.
- Evidence: `reasoning_application` cue `because` at chunk `4226254` offsets `420-427`; context: For its part, the respondent had originally sought costs because of the alleged misrepresentation.
- Evidence: `disposition` cue `denied` at chunk `4226254` offsets `217-223`; context: Nemeth said that the Board specifically denied an adjournment, yet no such denial appears on the record.

#### 3761:3:subtheme:7 · paragraphs 23-23

- Raw key terms: `allowed, application, board, different, entitled, general, hearing, importance`
- Display key terms: `allowed, different, entitled, hearing, importance`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: allowed, different, entitled, hearing, importance Operative outcome context: [22] This application for judicial review is allowed. Evidence spans paragraphs 23-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4226255` offsets `138-146`; context: No question of general importance is stated.
- Evidence: `disposition` cue `allowed` at chunk `4226255` offsets `45-52`; context: [22] This application for judicial review is allowed.

#### Section text

[11] I have reviewed the record of the proceedings and note the following events:
- At the beginning of the hearing, Mr. Nemeth was asked if he wanted to make any changes to his Personal Information Form (PIF). He said there were many things that could be added to it but he thought, based on the instructions his former representative had given him, that his narrative should be limited to a page. The Board pointed out to him that the instructions on the form indicate otherwise. It asked him if he had signed the form, indicating that he read and understood English. He acknowledged his signature, but said that he did not know what the signature was meant to signify. The Board then permitted Mr. Nemeth to change his PIF to indicate that he does not read or understand English.
- The Board asked Mr. Nemeth if he had received all of the required documents from his former representative. He said that he believed he had because a package of documents was sent to him. He left them at home because he did not know they would be required. In fact, their representative had told them it was not necessary to bring the documents to the hearing. He was asked if he was familiar with the contents of the package and he said "not entirely".
- The Board presented the Nemeths with certain documents from the Minister's office that pointed out discrepancies between their PIFs and their landed immigrant applications. It asked Nikolett Nemeth, the principal applicant's daughter, to translate them for her parents on the spot.
- The Board stated that it would limit the issues in the hearing to credibility and nexus. Accordingly, it said that it would not need to rely on documentary evidence or evidence on conditions in Hungary. Therefore, there was no need to have that evidence translated.
- Mr. Nemeth was asked why he did not have documentary evidence of his business activities in Hungary. He said that he provided all the documents his previous representative had requested and could provide additional documents if they were important. The Board noted that a screening form sent a month before the hearing specifically requested this documentary evidence. Mr. Nemeth said that he had not received that form. He said he had some documents at home and could provide them within a few days. The Board said "Fine."
- The Refugee Claim Officer made submissions to the effect that there were discrepancies in the evidence and no nexus to a recognized ground for a claim of refugee status. He stated that the applicants were responsible for the accuracy and completeness of their claims, not their former representative. In his final submissions, Mr. Nemeth simply said that he did not want to blame anyone else for the shortcomings of the family's claims and lamented the fact that it seemed to be too late for him to correct them.
- The Board dismissed the family's claims orally and immediately. It issued written reasons a few weeks later. In those reasons, the Board relied in part on the documentary evidence it had told the Nemeths it did not need to consider or translate for them.

[12] In each of these areas, counsel could have played a useful role. However, that does not mean, in itself, that the Nemeths did not receive a fair hearing.

[13] I have already stated above that the Board did not violate the Nemeths' right to counsel. But the Board's freedom to proceed in the absence of counsel obviously does not absolve it of the overarching obligation to ensure a fair hearing. Indeed, the Board's obligations in situations where claimants are without legal representation may actually be more onerous because it cannot rely on counsel to protect their interests.

[14] In Castroman, above, after counsel had withdrawn, the Board failed to ask the claimant whether he wanted an adjournment. Further, it did not allow the claimant to explain himself on re-examination and misled the claimant as to the next step in the hearing. The Court held, relying on Re Howard and Presiding Officer of Inmate Disciplinary Court of Stoney Mountain Institution (1985), 19 D.L.R. (4th) 502 (F.C.A.), that the claimant had been denied a fair hearing. The Court took account of the fact that the matter - a refugee claim - was serious, a difficult point of law was in issue, and the applicant did not have the capacity to present his own case.

[15] For similar reasons, I find that the Nemeths did not receive a fair hearing.
(a) The Board did not respond to the written request for an adjournment. While an adjournment should have also been requested by the Nemeths at the hearing, the Board should have at least inquired further into the matter of representation given that it was clearly aware that counsel of record had recently left the case. In addition, when the Board asked Mr. Nemeth if counsel of record still represented the family or if she had been discharged, it received an ambiguous answer: "No".
(b) The matter before the Board - determination of a refugee claim - was very serious.
(c) The case involved an issue of legal interpretation - whether the targeting of persons involved in business activities amounted to persecution because of "membership in a particular social group." While the Board made some effort to explain this issue to the Nemeths, I have no doubt that they were completely bewildered by that brief explanation and were in no position to make submissions in relation to it.
(d) It was clear that the Nemeths were ill-prepared for the hearing. They did not bring relevant documents with them. They did not appreciate the importance of corroborative evidence. They had not reviewed the documentation on which the Board was relying. Some of those documents were presented to them at the hearing and translated for them by their daughter, with little opportunity for them to respond. Others found their way into the Board's written reasons, even though the Board said they were not relevant.

[16] These problems were cumulative and arose against the backdrop of the circumstances in which the Nemeths found themselves at the commencement of the hearing. In that context, the Board should have realized that the Nemeths were prejudiced in their ability to present their claims by the absence of a representative, particularly as the hearing unfolded. It could easily have permitted the Nemeths an opportunity to gather the documents on which their claim depended, allowed them sufficient time to respond to the other evidence before the Board, as well as the submissions of the Refugee Claim Officer, and ensured that they understood the legal issue in their case. This was not a situation in which the applicants had made the decision to prosecute their claims without assistance and did so carelessly. There were numerous points where it was clear that they had placed reliance on the advice and assistance of their former representative and that they were in no position to proceed on their own, at least not on that day.

[17] Accordingly, the Nemeths are entitled to a new hearing before a different panel of the Board.
C. Did the Board make an error in concluding that the Nemeths had failed to show a nexus between the mistreatment they alleged and the recognized grounds for a claim under the Refugee Convention?

[18] As mentioned above, this legal issue came up before the Board and figured largely in its reasons. It is unnecessary, in light of my conclusion that a new hearing is required on other grounds, to say very much about this issue. While there is case law that casts doubt on whether mistreatment because of business activities can amount to persecution on grounds of "membership in a particular social group", this is another issue on which representations from counsel would have been helpful. The denial of a fair hearing justifies sending this matter back for redetermination, even though the legal foundation for the Nemeths' claim is not clear. Further, by definition, the absence of a fair hearing means there is no proper factual record before me on which to decide the legal issue.
II. Disposition

[19] At the conclusion of the hearing in this matter, I asked counsel to submit in writing any representations they might have with respect to certification of a question of general importance and costs.

[20] Mr. Galati, counsel for the Nemeths, proposed a question regarding the duty of the Board to adjourn in order to protect the right to counsel, and another with respect to the issue of nexus, discussed briefly above. With respect to the first issue, it is inappropriate to certify a question because the case law is well settled and, in any case, I have decided the issue primarily on the basis of waiver. With respect to the second issue, this is a not a proper case to state a question. As mentioned, given that there has not been a fair hearing, the factual record is unreliable.

[21] On the subject of costs, Mr. Galati is seeking costs on the grounds that the respondent inappropriately characterized the affidavit of Mr. Nemeth as misrepresentative. Mr. Nemeth said that the Board specifically denied an adjournment, yet no such denial appears on the record. As I said above, Mr. Nemeth must have made a mistake or misunderstood something. For its part, the respondent had originally sought costs because of the alleged misrepresentation. Quite properly, that request has now been withdrawn. In the circumstances, I make no order as to costs.

[22] This application for judicial review is allowed. The Nemeths are entitled to a new hearing before a different panel of the Board. No question of general importance is stated.


## 3761:4 · paragraphs 24-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `20762c81bc876bac00a421c2ace9f529fb2e015432977442d037a1b0dc4002b4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 3761:4:subtheme:1 · paragraphs 24-25

- Raw key terms: `applicants, canada, general, hearing, judgment, o'reilly, record, solicitors`
- Display key terms: `hearing, o'reilly, solicitors`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: hearing, o'reilly, solicitors No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
THIS COURT HEREBY ADJUDGED that:
1. The application for judicial review is allowed;
2. The applicants are entitled to a new hearing before a different panel of the Board; and
3. No question of general importance is stated.
"James W. O'Reilly"
J.F.C.C.
FEDERAL COURT OF CANADA
NAMES OF SOLICITORS AND SOLICITORS OF RECORD
DOCKET: IMM-2522-02

STYLE OF CAUSE: IMRE JANOS NEMETH, IMRENE NEMETH, NIKOLETT NEMETH
Applicants
- and -
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: THURSDAY, MARCH 20, 2003
REASONS FOR JDUGMENT
AND JUDGMENT BY: THE HONOURABLE MR. JUSTICE O'REILLY
DATED: WEDNESDAY, MAY 14, 2003
APPEARANCES BY:
Mr. Rocco Galati FOR THE APPLICANTS
Mr. Brad Gotkin FOR THE RESPONDENT
SOLICITORS OF RECORD:
Mr. Rocco Galati
GALATI, RODRIGUES & ASSOCIATES
637 College Street, Suite 203
Toronto, Ontario M6G 1B5 FOR THE APPLICANTS
Mr. Morris Rosenberg, Q.C.
Deputy Attorney General of Canada
FOR THE RESPONDENT
