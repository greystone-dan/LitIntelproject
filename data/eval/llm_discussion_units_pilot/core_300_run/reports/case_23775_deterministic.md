# Discussion Units: case 23775

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **63**
- Continuity pairs: **62**
- Discussion Units: **4**
- Paragraph source hashes: **63**
- Sub-themes: **13**

## 23775:1 · paragraphs 0-18

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `45aa3d375c7cd8b16d4684d14bbf27cde26639a7a002f4d97d5e4b1cbfd7931a`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23775:1:subtheme:1 · paragraphs 0-8

- Raw key terms: `applicant, living, villeneuve, death, decision, july, morris, pension`
- Display key terms: `living, villeneuve, death, july, morris, pension`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: living, villeneuve, death, july, morris, pension Rule/authority context: [1] This is an application for judicial review of a decision of the Pension Appeals Board (Board) which was made pursuant to subsection 83(1) of the Canada Pension Plan, RSC 1985, c C-8, (CPP). | [6] On October 2, 2008, Human Resources Development Canada (HRDC) informed the Applicant that her application for a survivor’s pension could not be approved as she did not meet the eligibility requirements under the CPP. Application context: [4] On July 22, 2008, the Applicant applied for a CPP survivor’s pension indicating in her application that she and Mr. | Morris also applied for the same survivor’s pension. Evidence spans paragraphs 0-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5116846` offsets `113-124`; context: [1] This is an application for judicial review of a decision of the Pension Appeals Board (Board) which was made pursuant to subsection 83(1) of the Canada Pension Plan, RSC 1985, c C-8, (CPP).
- Evidence: `reasoning_application` cue `applied` at chunk `5116849` offsets `36-43`; context: [4] On July 22, 2008, the Applicant applied for a CPP survivor’s pension indicating in her application that she and Mr.
- Evidence: `reasoning_application` cue `applied` at chunk `5116850` offsets `38-45`; context: Morris also applied for the same survivor’s pension.
- Evidence: `governing_rule` cue `under` at chunk `5116851` offsets `206-211`; context: [6] On October 2, 2008, Human Resources Development Canada (HRDC) informed the Applicant that her application for a survivor’s pension could not be approved as she did not meet the eligibility requirements under the CPP.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5116853` offsets `87-98`; context: [8] On December 17, 2009, the Applicant filed a Notice of Appeal of the HRDC decision, pursuant to section 82 of the CPP which was acknowledged by the Office of the Commissioner of the RT on January 18, 2010.

#### 23775:1:subtheme:2 · paragraphs 9-17

- Raw key terms: `applicant, appeal, board, arguable, case, decision, time, criteria`
- Display key terms: `arguable, case, time, criteria`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: arguable, case, time, criteria Position/evidence statements: She acknowledged that her application was submitted beyond the 90 day appeal period. | [12] In response, the Applicant’s new counsel submitted a letter dated January 25, 2012, stating that the Applicant had a continuing intention to pursue the appeal, there was an arguable case, a reasonable explanation fo Rule/authority context: [11] By Notice of Appeal dated December 8, 2011, the Applicant sought leave to appeal the RT Decision pursuant to subsection 83(1) of the CPP. | Decision Under Review Application context: Villeneuve was a surviving spouse as defined by subsection 42(1)(a) of the CPP and was, therefore, entitled to a survivor’s pension in accordance with subsection 44(1)(d) of the CPP. | Therefore, Ms. Operative outcome context: [10] In its decision dated August 17, 2011 the RT (RT Decision) upheld the decision of the HRDC and dismissed the Applicant’s appeal. | By letter dated December 19, 2011, the Board advised the Applicant that she would have to comply with Rule 5 of the Pension Appeals Board Rules of Procedure (Benefits), CRC 1978, c 390 (Board Rules) and the four criteria Evidence spans paragraphs 9-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5116854` offsets `8-13`; context: [9] The issue before the RT was whether Mrs.
- Evidence: `reasoning_application` cue `therefore` at chunk `5116854` offsets `133-142`; context: Villeneuve was a surviving spouse as defined by subsection 42(1)(a) of the CPP and was, therefore, entitled to a survivor’s pension in accordance with subsection 44(1)(d) of the CPP.
- Evidence: `evidence_fact` cue `found that` at chunk `5116855` offsets `137-147`; context: It found that Ms.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5116855` offsets `293-302`; context: Therefore, Ms.
- Evidence: `disposition` cue `upheld` at chunk `5116855` offsets `64-70`; context: [10] In its decision dated August 17, 2011 the RT (RT Decision) upheld the decision of the HRDC and dismissed the Applicant’s appeal.
- Evidence: `evidence_fact` cue `testimony` at chunk `5116856` offsets `100-109`; context: [34] Reviewing all the documents filed by both the Appellant and the Added Parties, and hearing the testimony and the submissions of the Parties, this Review Tribunal finds that the deceased contributor Stephane Villeneuve and Leigh-Ann Morris were cohabiting at the time of Mr.
- Evidence: `party_position` cue `submitted` at chunk `5116857` offsets `185-194`; context: She acknowledged that her application was submitted beyond the 90 day appeal period.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5116857` offsets `102-113`; context: [11] By Notice of Appeal dated December 8, 2011, the Applicant sought leave to appeal the RT Decision pursuant to subsection 83(1) of the CPP.
- Evidence: `disposition` cue `granted` at chunk `5116857` offsets `567-574`; context: By letter dated December 19, 2011, the Board advised the Applicant that she would have to comply with Rule 5 of the Pension Appeals Board Rules of Procedure (Benefits), CRC 1978, c 390 (Board Rules) and the four criteria set out in Canada (Minister of Human Resources and Development) v Gattellaro, 2005 FC 883 [Gattellaro] in order to be granted an extension of time within which to appeal.
- Evidence: `party_position` cue `submitted` at chunk `5116858` offsets `46-55`; context: [12] In response, the Applicant’s new counsel submitted a letter dated January 25, 2012, stating that the Applicant had a continuing intention to pursue the appeal, there was an arguable case, a reasonable explanation for the 18 day late filing of the Notice of Appeal and that the delay did not cause any prejudice.
- Evidence: `governing_rule` cue `Under` at chunk `5116859` offsets `205-210`; context: Decision Under Review
- Evidence: `counterargument_limitation` cue `However` at chunk `5116861` offsets `81-88`; context: However, the Board’s main concern was that the Applicant did not meet the second criterion of the test, an arguable case.

#### 23775:1:subtheme:3 · paragraphs 18-18

- Raw key terms: `absence, additional, application, arguable, case, considered, correctness, decision`
- Display key terms: `absence, additional, arguable, case, considered, correctness`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: absence, additional, arguable, case, considered, correctness Evidence spans paragraphs 18-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5116863` offsets `215-223`; context: [22] In the absence of significant new or additional evidence not considered by the Review Tribunal, an application for leave may raise an arguable case where the leave decision maker finds the application raises a question of an error of law, measured by a standard of correctness, or an error of significant fact that is unreasonable or perverse in light of the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116863` offsets `53-61`; context: [22] In the absence of significant new or additional evidence not considered by the Review Tribunal, an application for leave may raise an arguable case where the leave decision maker finds the application raises a question of an error of law, measured by a standard of correctness, or an error of significant fact that is unreasonable or perverse in light of the evidence.

#### Section text

Lee Villeneuve v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2013-05-14
Neutral citation
2013 FC 498
File numbers
T-1561-12
Decision Content
Federal Court
Cour fédérale
Date: 20130514
Docket: T-1561-12
Citation: 2013 FC 498
Ottawa, Ontario, May 14, 2013
PRESENT: The Honourable Madam Justice Strickland
BETWEEN:
JODY LEE VILLENEUVE
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of a decision of the Pension Appeals Board (Board) which was made pursuant to subsection 83(1) of the Canada Pension Plan, RSC 1985, c C-8, (CPP). The Board refused to grant the Applicant an extension of time to appeal a decision of a Review Tribunal (RT) dated August 17, 2011.
Background

[2] On July 7, 2001, the Applicant, Jody Lee Villeneuve, and Stephane Villeneuve were married. On or about February 25, 2007, they ceased living together.

[3] Mr. Villeneuve moved to the residence of Leigh-Anne Morris and began living as a tenant in the basement of her home. By May of 2007, a personal relationship developed between Mr. Villeneuve and Ms. Morris. On July 12, 2008, Mr. Villeneuve died. Prior to his death he had been a contributor to CPP.

[4] On July 22, 2008, the Applicant applied for a CPP survivor’s pension indicating in her application that she and Mr. Villeneuve were legally married but that they were no longer living together at the time of his death.

[5] On July 25, 2008, Ms. Morris also applied for the same survivor’s pension. Ms. Morris indicated in a Statutory Declaration of Common-Law Union that she and Mr. Villeneuve had commenced living together on February 28, 2007, and lived together continuously in a common-law relationship until Mr. Villeneuve’s death.

[6] On October 2, 2008, Human Resources Development Canada (HRDC) informed the Applicant that her application for a survivor’s pension could not be approved as she did not meet the eligibility requirements under the CPP. Specifically, she did not meet the definition of a surviving spouse as another person was living in a common-law relationship with the deceased contributor at the time of his death. That other person is Ms. Morris.

[7] On December 18, 2008, the Applicant requested a reconsideration of that decision and on March 30, 2009, she forwarded additional information to substantiate her claim. On December 11, 2009, the Applicant was informed by HRDC that its decision had been reconsidered and confirmed.

[8] On December 17, 2009, the Applicant filed a Notice of Appeal of the HRDC decision, pursuant to section 82 of the CPP which was acknowledged by the Office of the Commissioner of the RT on January 18, 2010. By letter dated May 31, 2010, the RT informed Ms. Morris that a Notice of Appeal had been received and that she was being included in the proceedings as an “Added Party.”

[9] The issue before the RT was whether Mrs. Villeneuve was a surviving spouse as defined by subsection 42(1)(a) of the CPP and was, therefore, entitled to a survivor’s pension in accordance with subsection 44(1)(d) of the CPP.

[10] In its decision dated August 17, 2011 the RT (RT Decision) upheld the decision of the HRDC and dismissed the Applicant’s appeal. It found that Ms. Morris and Mr. Villeneuve had cohabited in a conjugal relationship for a continuous period of at least one year up to the time of his death. Therefore, Ms. Morris was the common law spouse of Mr. Villeneuve and was the surviving spouse eligible to receive the CPP survivor benefit. The RT stated the following:

[34] Reviewing all the documents filed by both the Appellant and the Added Parties, and hearing the testimony and the submissions of the Parties, this Review Tribunal finds that the deceased contributor Stephane Villeneuve and Leigh-Ann Morris were cohabiting at the time of Mr. Villeneuve’s death, and that such cohabitation was well in excess of one year.

[11] By Notice of Appeal dated December 8, 2011, the Applicant sought leave to appeal the RT Decision pursuant to subsection 83(1) of the CPP. She acknowledged that her application was submitted beyond the 90 day appeal period. By letter dated December 19, 2011, the Board advised the Applicant that she would have to comply with Rule 5 of the Pension Appeals Board Rules of Procedure (Benefits), CRC 1978, c 390 (Board Rules) and the four criteria set out in Canada (Minister of Human Resources and Development) v Gattellaro, 2005 FC 883 [Gattellaro] in order to be granted an extension of time within which to appeal.

[12] In response, the Applicant’s new counsel submitted a letter dated January 25, 2012, stating that the Applicant had a continuing intention to pursue the appeal, there was an arguable case, a reasonable explanation for the 18 day late filing of the Notice of Appeal and that the delay did not cause any prejudice.

[13] On April 2, 2012 the Board issued its decision denying the Applicant’s request to extend the time for filing of her Notice of Appeal (Decision). This is the judicial review of that Decision.
Decision Under Review

[14] The Decision referenced subsection 83(1) of the CPP, the Board’s letter of December 19, 2011 to the Applicant, and, her counsel’s response on January 25, 2012, addressing the Gattellaro criteria. The Board stated that the Gattellaro test is conjunctive and that the four criteria to be considered are:
1. A continuing intention to pursue the application or appeal;
2. The matter discloses an arguable case;
3. There is a reasonable explanation for the delay; and
4. There is no prejudice to the other party in allowing the extension.

[15] It was satisfied that the Applicant satisfied criteria one, three and four. However, the Board’s main concern was that the Applicant did not meet the second criterion of the test, an arguable case.

[16] The Board cited Callihoo v Canada (Attorney General), [2000] FCJ No 612 [Callihoo] as authority for the test to be met to raise an arguable case:

[22] In the absence of significant new or additional evidence not considered by the Review Tribunal, an application for leave may raise an arguable case where the leave decision maker finds the application raises a question of an error of law, measured by a standard of correctness, or an error of significant fact that is unreasonable or perverse in light of the evidence. […]

## 23775:2 · paragraphs 19-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `105599df7ccff6d594f4b99442149f17c9c059edac29214b4986da9f280c1ed3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23775:2:subtheme:1 · paragraphs 19-20

- Raw key terms: `applicant, arguable, case, accord, allow, board, callihoo, complete`
- Display key terms: `arguable, case, accord, allow, callihoo, complete`
- Argument roles: `governing_rule`
- Explanation: Observed roles: governing_rule Display terms: arguable, case, accord, allow, callihoo, complete Rule/authority context: [15] I can find nothing in the complete file before me that would allow me to determine that the applicant has an arguable case in accord with the principles of law set out in Callihoo. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `principles` at chunk `5116865` offsets `147-157`; context: [15] I can find nothing in the complete file before me that would allow me to determine that the applicant has an arguable case in accord with the principles of law set out in Callihoo.

#### 23775:2:subtheme:2 · paragraphs 21-22

- Raw key terms: `application, reasons, above, appeal, arrived, assessment, clearly, conclusions`
- Display key terms: `above, arrived, assessment, clearly, conclusions`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: above, arrived, assessment, clearly, conclusions Application context: I do not find that the application raises a question of an error of law, measured by a standard of correctness, that was not dealt with by the Tribunal, nor do I find any error of significant fact that is unreasonable or Evidence spans paragraphs 21-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5116866` offsets `200-208`; context: I do not find that the application raises a question of an error of law, measured by a standard of correctness, that was not dealt with by the Tribunal, nor do I find any error of significant fact that is unreasonable or perverse in light of the findings of evidence set out in the decision of the Review Tribunal.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116866` offsets `414-422`; context: I do not find that the application raises a question of an error of law, measured by a standard of correctness, that was not dealt with by the Tribunal, nor do I find any error of significant fact that is unreasonable or perverse in light of the findings of evidence set out in the decision of the Review Tribunal.
- Evidence: `reasoning_application` cue `I find` at chunk `5116866` offsets `316-322`; context: I do not find that the application raises a question of an error of law, measured by a standard of correctness, that was not dealt with by the Tribunal, nor do I find any error of significant fact that is unreasonable or perverse in light of the findings of evidence set out in the decision of the Review Tribunal.
- Evidence: `issue` cue `Issues` at chunk `5116867` offsets `117-123`; context: Issues

#### Section text

[17] The Board concluded that the Applicant had not established an arguable case:

[15] I can find nothing in the complete file before me that would allow me to determine that the applicant has an arguable case in accord with the principles of law set out in Callihoo.

[16] The Review Tribunal clearly gave their findings and assessment of credibility, and conclusions, and the reasons why they arrived at those conclusions. I do not find that the application raises a question of an error of law, measured by a standard of correctness, that was not dealt with by the Tribunal, nor do I find any error of significant fact that is unreasonable or perverse in light of the findings of evidence set out in the decision of the Review Tribunal. (The only error is a typing error in paragraph 21 of the decision where it states July 2 rather than July 12).
[…]

[20] For the above reasons, the application for an Order for an extension of time within which to appeal is refused.
Issues

## 23775:3 · paragraphs 23-61

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e2f4ebb7e1ec499978a744a15f6a2ff3d622047951c0a153363474bffd6fb3a2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23775:3:subtheme:1 · paragraphs 23-25

- Raw key terms: `review, standard, appropriate, board, decision, extension, jurisprudence, para`
- Display key terms: `review, standard, appropriate, extension, jurisprudence, para`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: review, standard, appropriate, extension, jurisprudence, para Rule/authority context: What is the appropriate standard of review? | [19] A standard of review analysis need not be conducted in every instance if the jurisprudence satisfactorily establishes which standard is to apply (Dunsmuir v New Brunswick, 2008 SCC 9 at para 57 [Dunsmuir]). Application context: [19] A standard of review analysis need not be conducted in every instance if the jurisprudence satisfactorily establishes which standard is to apply (Dunsmuir v New Brunswick, 2008 SCC 9 at para 57 [Dunsmuir]). Evidence spans paragraphs 23-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5116868` offsets `24-30`; context: [18] I have phrased the issues as follows:
1.
- Evidence: `governing_rule` cue `standard of review` at chunk `5116868` offsets `70-88`; context: What is the appropriate standard of review?
- Evidence: `governing_rule` cue `standard of review` at chunk `5116869` offsets `7-25`; context: [19] A standard of review analysis need not be conducted in every instance if the jurisprudence satisfactorily establishes which standard is to apply (Dunsmuir v New Brunswick, 2008 SCC 9 at para 57 [Dunsmuir]).
- Evidence: `reasoning_application` cue `apply` at chunk `5116869` offsets `144-149`; context: [19] A standard of review analysis need not be conducted in every instance if the jurisprudence satisfactorily establishes which standard is to apply (Dunsmuir v New Brunswick, 2008 SCC 9 at para 57 [Dunsmuir]).
- Evidence: `governing_rule` cue `Jurisprudence` at chunk `5116870` offsets `5-18`; context: [20] Jurisprudence has established that the appropriate standard of review for a decision of the Board regarding a request for an extension of time is reasonableness (Leblanc v Canada (Minister of Human Resources and Skills Development), 2010 FC 641, at para 15 [Leblanc]; Canada (Attorney General) v Graca, 2011 FC 615 at para 10 [Graca]; Handa v Canada (Attorney General) 2008 FCA 223, at paras 10-12 [Handa]).

#### 23775:3:subtheme:2 · paragraphs 26-27

- Raw key terms: `applicant, board, time, above, acceptable, another, appeal, arguable`
- Display key terms: `time, above, acceptable, another, arguable`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: time, above, acceptable, another, arguable Position/evidence statements: [22] The Applicant submits that the Board unreasonably found that she did not establish an arguable case. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5116871` offsets `200-207`; context: [21] A Court reviewing a decision on the reasonableness standard is concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above, at para 47; Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59 [Khosa]).
- Evidence: `party_position` cue `submits` at chunk `5116872` offsets `19-26`; context: [22] The Applicant submits that the Board unreasonably found that she did not establish an arguable case.
- Evidence: `evidence_fact` cue `found that` at chunk `5116872` offsets `55-65`; context: [22] The Applicant submits that the Board unreasonably found that she did not establish an arguable case.

#### 23775:3:subtheme:3 · paragraphs 28-42

- Raw key terms: `board, time, case, applicant, arguable, extension, submits, appeal`
- Display key terms: `time, case, arguable, extension, submits`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: time, case, arguable, extension, submits Position/evidence statements: [23] The Applicant submits that while the Board referred to her January 25, 2012 letter, it did not address the Applicant’s specific submissions indicating that there was an arguable case. | [24] The Applicant submits that the Board’s finding that there was nothing in the complete file to demonstrate an arguable case indicates that the Board failed to consider whether the Applicant had a reasonable chance of Rule/authority context: [32] A survivor’s pension shall be paid to a survivor of a deceased contributor pursuant to subsection 44(1)(d). | [34] Pursuant to subsection 82(1), a person who is dissatisfied with a Minister’s decision can appeal the decision to the RT. Application context: Having reviewed the evidence, it was open to the RT to decide on its reliability and to weigh the evidence accordingly. | [35] An applicant who does not apply for leave to appeal the RT’s decision within 90 days must first be granted a discretionary extension of the time to seek leave. Operative outcome context: [35] An applicant who does not apply for leave to appeal the RT’s decision within 90 days must first be granted a discretionary extension of the time to seek leave. Evidence spans paragraphs 28-42. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5116873` offsets `1322-1328`; context: Sager’s evidence based on credibility issues when the Review Tribunal never met or heard testimony from Mr.
- Evidence: `party_position` cue `submits` at chunk `5116873` offsets `19-26`; context: [23] The Applicant submits that while the Board referred to her January 25, 2012 letter, it did not address the Applicant’s specific submissions indicating that there was an arguable case.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116873` offsets `236-244`; context: The Board erred in failing to consider the new evidence that was not before the RT but which the Applicant intended to present if the Board permitted her appeal.
- Evidence: `counterargument_limitation` cue `but` at chunk `5116873` offsets `272-275`; context: The Board erred in failing to consider the new evidence that was not before the RT but which the Applicant intended to present if the Board permitted her appeal.
- Evidence: `issue` cue `whether` at chunk `5116874` offsets `172-179`; context: [24] The Applicant submits that the Board’s finding that there was nothing in the complete file to demonstrate an arguable case indicates that the Board failed to consider whether the Applicant had a reasonable chance of success.
- Evidence: `party_position` cue `submits` at chunk `5116874` offsets `19-26`; context: [24] The Applicant submits that the Board’s finding that there was nothing in the complete file to demonstrate an arguable case indicates that the Board failed to consider whether the Applicant had a reasonable chance of success.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116874` offsets `276-284`; context: Sager’s evidence on the basis of an inference that he was attempting to use innuendo for some unknown purpose.
- Evidence: `evidence_fact` cue `found that` at chunk `5116875` offsets `173-183`; context: [25] The Applicant states that the present facts are similar to Leblanc v Canada (Minister of Human Resources and Skills Development), 2010 FC 641 [Leblanc] where the Court found that the new medical evidence of the applicant therein was clearly sufficient to ground an argument that an arguable case was disclosed.
- Evidence: `party_position` cue `submits` at chunk `5116876` offsets `20-27`; context: [26] The Respondent submits that the Board reasonably held that there was nothing in the complete file that would allow it to find that the Applicant had an arguable case.
- Evidence: `party_position` cue `submits` at chunk `5116877` offsets `20-27`; context: [27] The Respondent submits that, although the Board mistakenly stated that the test for an extension of time is conjunctive, this is not fatal to the final outcome as it reasonably found that the application for an extension of time did not disclose an arguable case (Canada (Attorney General) v Blondahl, 2009 FC 118, at para 16 [Blondahl]).
- Evidence: `evidence_fact` cue `found that` at chunk `5116877` offsets `182-192`; context: [27] The Respondent submits that, although the Board mistakenly stated that the test for an extension of time is conjunctive, this is not fatal to the final outcome as it reasonably found that the application for an extension of time did not disclose an arguable case (Canada (Attorney General) v Blondahl, 2009 FC 118, at para 16 [Blondahl]).
- Evidence: `party_position` cue `submits` at chunk `5116878` offsets `20-27`; context: [28] The Respondent submits that the Applicant did not raise an arguable case in her application for an extension of time.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116878` offsets `176-184`; context: She did not submit any significant new or additional evidence with her application that was not already considered by the RT.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5116878` offsets `259-265`; context: The Board cannot determine the existence of an arguable case on the basis of promised evidence to be submitted at a later stage.
- Evidence: `party_position` cue `submits` at chunk `5116879` offsets `20-27`; context: [29] The Respondent submits that the RT reviewed and considered the evidence of Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116879` offsets `68-76`; context: [29] The Respondent submits that the RT reviewed and considered the evidence of Mr.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5116879` offsets `382-393`; context: Having reviewed the evidence, it was open to the RT to decide on its reliability and to weigh the evidence accordingly.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5116879` offsets `406-412`; context: This Court cannot re-weigh the evidence and retry the case that was before the Board.
- Evidence: `party_position` cue `submits` at chunk `5116880` offsets `20-27`; context: [30] The Respondent submits that there was no error in the RT’s Decision that would raise an arguable case.
- Evidence: `evidence_fact` cue `testimony` at chunk `5116880` offsets `143-152`; context: The RT had the benefit of the oral testimony and written submissions of each party.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5116882` offsets `80-91`; context: [32] A survivor’s pension shall be paid to a survivor of a deceased contributor pursuant to subsection 44(1)(d).
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5116884` offsets `5-16`; context: [34] Pursuant to subsection 82(1), a person who is dissatisfied with a Minister’s decision can appeal the decision to the RT.
- Evidence: `reasoning_application` cue `apply` at chunk `5116885` offsets `31-36`; context: [35] An applicant who does not apply for leave to appeal the RT’s decision within 90 days must first be granted a discretionary extension of the time to seek leave.
- Evidence: `disposition` cue `granted` at chunk `5116885` offsets `104-111`; context: [35] An applicant who does not apply for leave to appeal the RT’s decision within 90 days must first be granted a discretionary extension of the time to seek leave.

#### 23775:3:subtheme:4 · paragraphs 43-48

- Raw key terms: `applicant, evidence, time, above, appeal, arguable, case, decision`
- Display key terms: `time, above, arguable, case`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: time, above, arguable, case Position/evidence statements: [41] The Applicant submits that the above evidence confirmed that she was the lawful survivor entitled to the CPP survivor’s pension as Ms. | She submitted no other evidence to support her application. Application context: Villeneuve until the time of his death and, therefore, was not his common law spouse. | [43] I find that the RT had before it, reviewed and considered the Sagar Declaration, the Hawkins and Zinck letters. Evidence spans paragraphs 43-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5116888` offsets `200-208`; context: Another way to raise an arguable case is through a question of an error of law or an error of fact (Callihoo, above, at para 22).
- Evidence: `evidence_fact` cue `evidence` at chunk `5116888` offsets `83-91`; context: [38] One of the ways to establish an arguable case is to present new or additional evidence that was not before the RT (Leblanc, above, at para 25).
- Evidence: `issue` cue `whether` at chunk `5116889` offsets `18-25`; context: [39] In assessing whether a decision is reasonable, courts should not substitute their own reasons but may, if they find it necessary, look to the record for the purpose of assessing the reasonableness of the outcome (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 15 [Newfoundland Nurses]).
- Evidence: `evidence_fact` cue `record` at chunk `5116889` offsets `147-153`; context: [39] In assessing whether a decision is reasonable, courts should not substitute their own reasons but may, if they find it necessary, look to the record for the purpose of assessing the reasonableness of the outcome (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 15 [Newfoundland Nurses]).
- Evidence: `counterargument_limitation` cue `but` at chunk `5116889` offsets `99-102`; context: [39] In assessing whether a decision is reasonable, courts should not substitute their own reasons but may, if they find it necessary, look to the record for the purpose of assessing the reasonableness of the outcome (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 15 [Newfoundland Nurses]).
- Evidence: `evidence_fact` cue `evidence` at chunk `5116890` offsets `36-44`; context: [40] Before the RT, the Applicant’s evidence included a statutory declaration by Shane Sager dated February 25, 2009 (Sagar Declaration), in which Mr.
- Evidence: `party_position` cue `submits` at chunk `5116891` offsets `19-26`; context: [41] The Applicant submits that the above evidence confirmed that she was the lawful survivor entitled to the CPP survivor’s pension as Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116891` offsets `42-50`; context: [41] The Applicant submits that the above evidence confirmed that she was the lawful survivor entitled to the CPP survivor’s pension as Ms.
- Evidence: `reasoning_application` cue `therefore` at chunk `5116891` offsets `219-228`; context: Villeneuve until the time of his death and, therefore, was not his common law spouse.
- Evidence: `party_position` cue `submitted` at chunk `5116892` offsets `175-184`; context: She submitted no other evidence to support her application.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116892` offsets `194-202`; context: She submitted no other evidence to support her application.
- Evidence: `party_position` cue `submit` at chunk `5116893` offsets `308-314`; context: Accordingly, in my view, the Applicant did not submit any significant new or additional evidence that could have given rise to an arguable case in support of her application to extend the time to file her appeal of the RT Decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116893` offsets `349-357`; context: Accordingly, in my view, the Applicant did not submit any significant new or additional evidence that could have given rise to an arguable case in support of her application to extend the time to file her appeal of the RT Decision.
- Evidence: `reasoning_application` cue `I find` at chunk `5116893` offsets `5-11`; context: [43] I find that the RT had before it, reviewed and considered the Sagar Declaration, the Hawkins and Zinck letters.

#### 23775:3:subtheme:5 · paragraphs 49-52

- Raw key terms: `evidence, applicant, arguable, belo-alves, board, case, extension, above`
- Display key terms: `arguable, belo-alves, case, extension, above`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: arguable, belo-alves, case, extension, above Position/evidence statements: In Belo-Alves, the applicant actually submitted new evidence with its application seeking an extension of time. Application context: Belo-Alves […] and a legal argument that an improper test for new facts was applied […]. | Therefore, the Board made no reviewable error in failing to do so. Evidence spans paragraphs 49-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5116894` offsets `220-227`; context: In the context of whether to grant an extension to appeal, Justice Campbell held that the Board should not consider whether it would allow the appeal, only whether the evidence and legal arguments gives the appeal a “reasonable chance of success.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116894` offsets `124-132`; context: [44] The Applicant relies on Belo-Alves, above, to support her argument that the Board erred by failing to consider the new evidence that would be available to the Board and that was not before the RT.
- Evidence: `issue` cue `issue` at chunk `5116895` offsets `25-30`; context: [11] With respect to the issue of arguable case, the argument placed before the Board by Counsel for Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116895` offsets `169-177`; context: Belo-Alves has two components: an evidentiary argument that new evidence exists within the medical evidence produced by Ms.
- Evidence: `reasoning_application` cue `applied` at chunk `5116895` offsets `305-312`; context: Belo-Alves […] and a legal argument that an improper test for new facts was applied […].
- Evidence: `party_position` cue `submitted` at chunk `5116896` offsets `100-109`; context: In Belo-Alves, the applicant actually submitted new evidence with its application seeking an extension of time.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116896` offsets `114-122`; context: In Belo-Alves, the applicant actually submitted new evidence with its application seeking an extension of time.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116897` offsets `57-65`; context: [46] Here, however, the Applicant relies on anticipatory evidence and speculates as to what that evidence will be and what it will establish.
- Evidence: `reasoning_application` cue `Therefore` at chunk `5116897` offsets `301-310`; context: Therefore, the Board made no reviewable error in failing to do so.

#### 23775:3:subtheme:6 · paragraphs 53-54

- Raw key terms: `above, case, evidence, fact, weight, amount, analysis, apartment`
- Display key terms: `above, case, fact, weight, amount, analysis, apartment`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: above, case, fact, weight, amount, analysis, apartment Evidence spans paragraphs 53-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5116898` offsets `307-315`; context: The RT also specifically considered the weight that should be given to that evidence and found that “The attempts in both the declaration and the investigator’s report to use innuendo put into question the veracity of all associated remarks in the declaration and the Investigator’s Report.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116898` offsets `190-198`; context: The RT also specifically considered the weight that should be given to that evidence and found that “The attempts in both the declaration and the investigator’s report to use innuendo put into question the veracity of all associated remarks in the declaration and the Investigator’s Report.
- Evidence: `evidence_fact` cue `testimony` at chunk `5116899` offsets `195-204`; context: The RT had the benefit of hearing the parties oral testimony as well as reviewing the documentary evidence.

#### 23775:3:subtheme:7 · paragraphs 55-61

- Raw key terms: `arguable, board, case, above, decision, applicant, para, reasons`
- Display key terms: `arguable, case, above, para`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: arguable, case, above, para Position/evidence statements: [50] The Applicant also submits that the Board failed to explain why the Applicant’s submissions did not raise an arguable case. Rule/authority context: [51] Here the Board stated that it found nothing in the complete file before it that would allow it to determine that the Applicant had an arguable case in accordance with the principles of law set out in Callihoo, above Application context: [54] In my view, the Board did not make a reviewable error in finding that the Applicant had failed to make an arguable case and therefore dismissing her application for an extension of time to appeal the RT’s Decision. Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that this application for judicial review is dismissed. Evidence spans paragraphs 55-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5116900` offsets `35-42`; context: [49] The Board properly considered whether the application for an extension of time to appeal the RT decision raised an arguable case.
- Evidence: `evidence_fact` cue `found that` at chunk `5116900` offsets `149-159`; context: It reasonably found that the RT had clearly set out its findings, assessments of credibility and its reasons for its conclusions and that the RT Decision did not raise a question of law or error of significant fact.
- Evidence: `issue` cue `whether` at chunk `5116901` offsets `245-252`; context: However, the reasons offered for a decision are to be assessed along with the outcome of that decision to determine whether the decision as a whole is reasonable, “adequacy of reasons” is no longer a stand-alone ground for challenging a decision (Newfoundland Nurses, above, at para 14).
- Evidence: `party_position` cue `submits` at chunk `5116901` offsets `24-31`; context: [50] The Applicant also submits that the Board failed to explain why the Applicant’s submissions did not raise an arguable case.
- Evidence: `counterargument_limitation` cue `However` at chunk `5116901` offsets `129-136`; context: However, the reasons offered for a decision are to be assessed along with the outcome of that decision to determine whether the decision as a whole is reasonable, “adequacy of reasons” is no longer a stand-alone ground for challenging a decision (Newfoundland Nurses, above, at para 14).
- Evidence: `evidence_fact` cue `evidence` at chunk `5116902` offsets `278-286`; context: A decision-maker is presumed to have considered all the evidence before it (Florea v Canada (Minister of Employment and Immigration), [1993] FCJ No 598 [Florea]) and the Court will consider putting aside this presumption only when the probative value of the evidence that is not expressly discussed is such that it should have been addressed (Cepeda-Gutierrez v Canada (Minister of Citizenship and Immigration), (1998) 157 FTR 35 at paras 14-17 [Cepeda]).
- Evidence: `governing_rule` cue `principles` at chunk `5116902` offsets `176-186`; context: [51] Here the Board stated that it found nothing in the complete file before it that would allow it to determine that the Applicant had an arguable case in accordance with the principles of law set out in Callihoo, above.
- Evidence: `evidence_fact` cue `evidence` at chunk `5116903` offsets `96-104`; context: [52] The submissions contained in the July 25, 2012 letter from the Applicant’s counsel rely on evidence that was before the RT and on anticipatory evidence, addressed above.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5116903` offsets `259-267`; context: Although the Board did not address the specifics of the submissions, they were referred to in its Decision and it did state that there was nothing in the record before it that would allow it to determine that the Applicant raised an arguable case.
- Evidence: `counterargument_limitation` cue `However` at chunk `5116904` offsets `313-320`; context: However, in my view, the Board’s mistake in describing the test as conjunctive is not fatal to its final decision as the Board clearly stated that it was concerned with the second criterion, that of an “arguable case.
- Evidence: `reasoning_application` cue `therefore` at chunk `5116905` offsets `129-138`; context: [54] In my view, the Board did not make a reviewable error in finding that the Applicant had failed to make an arguable case and therefore dismissing her application for an extension of time to appeal the RT’s Decision.
- Evidence: `disposition` cue `dismissed` at chunk `5116905` offsets `366-375`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application for judicial review is dismissed.

#### Section text

[18] I have phrased the issues as follows:
1. What is the appropriate standard of review?
2. Did the Board err in denying the Applicant’s request for an extension of time to seek leave to appeal the RT Decision?
Standard of Review

[19] A standard of review analysis need not be conducted in every instance if the jurisprudence satisfactorily establishes which standard is to apply (Dunsmuir v New Brunswick, 2008 SCC 9 at para 57 [Dunsmuir]).

[20] Jurisprudence has established that the appropriate standard of review for a decision of the Board regarding a request for an extension of time is reasonableness (Leblanc v Canada (Minister of Human Resources and Skills Development), 2010 FC 641, at para 15 [Leblanc]; Canada (Attorney General) v Graca, 2011 FC 615 at para 10 [Graca]; Handa v Canada (Attorney General) 2008 FCA 223, at paras 10-12 [Handa]).

[21] A Court reviewing a decision on the reasonableness standard is concerned with “the existence of justification, transparency and intelligibility within the decision-making process [and also with] whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir, above, at para 47; Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59 [Khosa]).
Did the Board err in denying the Applicant’s request for an extension of time to seek leave to appeal the RT Decision?
Applicant’s Submissions

[22] The Applicant submits that the Board unreasonably found that she did not establish an arguable case. The Applicant submits that her arguable case is that she is the surviving spouse entitled to the survivor’s pension as Ms. Morris was not Mr. Villeneuve’s common law spouse as defined by the CPP. There is compelling, dispositive evidence that at the time of Mr. Villeneuve’s death, Ms. Morris and Mr. Villeneuve were living separately and Ms. Morris was living with and was in a common law relationship with another man, Mr. Sager.

[23] The Applicant submits that while the Board referred to her January 25, 2012 letter, it did not address the Applicant’s specific submissions indicating that there was an arguable case. The Board erred in failing to consider the new evidence that was not before the RT but which the Applicant intended to present if the Board permitted her appeal. The Applicant alleges that the Board did not refer to the following submissions:
a. Mr. Sager’s evidence is that he was living in a conjugal relationship with Ms. Morris at her house at the time of death;
b. That the applicant intends to marshal new evidence by compelling Mr. Sager to testify in person by way of subpoena in order to permit the trier of fact to assess Mr. Sager’s credibility;
c. That the deceased had entered a lease for a separate apartment and was living alone in his apartment at the time of his death;
d. That the applicant intends to marshal new evidence by compelling the deceased’s former landlords, Allan and Wendy Zinck, to testify in person at the appeal hearing by way of subpoena in order to permit the trier of fact to better assess credibility;
e. It would be Allan and Wendy Zinck’s evidence that Ms. Morris was not living with the deceased at the time of death;
f. The Review Tribunal rejected Mr. Sager’s evidence based on credibility issues when the Review Tribunal never met or heard testimony from Mr. Sager;
g. The Review Tribunal makes its findings based on hearsay documentary evidence and did not have an opportunity to hear from Mr. Sager in person;
h. The applicant intends to obtain medical records indicating that the deceased was living alone when he died. This new evidence was not available to the Review Tribunal for consideration.

[24] The Applicant submits that the Board’s finding that there was nothing in the complete file to demonstrate an arguable case indicates that the Board failed to consider whether the Applicant had a reasonable chance of success. The Board also erred in rejecting Mr. Sager’s evidence on the basis of an inference that he was attempting to use innuendo for some unknown purpose. And, in assessing whether to grant an extension of the time to appeal, the Board should not consider whether it would allow the appeal, only whether the evidence and legal arguments give the appeal a “reasonable chance of success” (Belo-Alves v Canada (Minister of Social Development), 2009 FC 413 at para 11 [Belo-Alves]).

[25] The Applicant states that the present facts are similar to Leblanc v Canada (Minister of Human Resources and Skills Development), 2010 FC 641 [Leblanc] where the Court found that the new medical evidence of the applicant therein was clearly sufficient to ground an argument that an arguable case was disclosed.
Respondent’s Submissions

[26] The Respondent submits that the Board reasonably held that there was nothing in the complete file that would allow it to find that the Applicant had an arguable case. The Board also reasonably held that there was no indication that the application for an extension of time raises an error of law or an error of significant fact committed by the RT.

[27] The Respondent submits that, although the Board mistakenly stated that the test for an extension of time is conjunctive, this is not fatal to the final outcome as it reasonably found that the application for an extension of time did not disclose an arguable case (Canada (Attorney General) v Blondahl, 2009 FC 118, at para 16 [Blondahl]).

[28] The Respondent submits that the Applicant did not raise an arguable case in her application for an extension of time. She did not submit any significant new or additional evidence with her application that was not already considered by the RT. The Board cannot determine the existence of an arguable case on the basis of promised evidence to be submitted at a later stage.

[29] The Respondent submits that the RT reviewed and considered the evidence of Mr. Sager, Mr. Hawkins, a private investigator retained by the Applicant, as well as the fact that at the time of his death Mr. Villeneuve was living in an apartment and not in Ms. Morris’ home. Having reviewed the evidence, it was open to the RT to decide on its reliability and to weigh the evidence accordingly. This Court cannot re-weigh the evidence and retry the case that was before the Board.

[30] The Respondent submits that there was no error in the RT’s Decision that would raise an arguable case. The RT had the benefit of the oral testimony and written submissions of each party. It conducted a thorough analysis of the evidence before it, addressed the Applicant’s main arguments based on the evidence and was entitled to prefer some evidence over other evidence (Dossa v Canada (Pension Appeal Board), 2005 FCA 387 at para 4 [Dossa]). In addition, the Board was not entitled to assess the merits of the case when it determined that there was no arguable case (Callihoo, above, at para 21).
Analysis

[31] Subsections 2(1), 42(1), 44(1), 44(1)(1.1), 82(1) and 83(1) of the CPP and Rules 4 and 5 of the Board Rules are relevant to this proceeding.

[32] A survivor’s pension shall be paid to a survivor of a deceased contributor pursuant to subsection 44(1)(d). Section 42(1) defines a “survivor”:
42. (1) In this Part,
[…]
“survivor”, in relation to a deceased contributor, means
(a) if there is no person described in paragraph (b), a person who was married to the contributor at the time of the contributor’s death, or
(b) a person who was the common-law partner of the contributor at the time of the contributor’s death;
42. (1) Les définitions qui suivent s’appliquent à la présente partie.
[…]
« survivant » S’entend :
a) à défaut de la personne visée à l’alinéa b), de l’époux du cotisant au décès de celui-ci;
b) du conjoint de fait du cotisant au décès de celui-ci.

[33] Subsection 2(1) defines a common law partner as follows:
2. (1) In this Act,
“common-law partner”, in relation to a contributor, means a person who is cohabiting with the contributor in a conjugal relationship at the relevant time, having so cohabited with the contributor for a continuous period of at least one year. For greater certainty, in the case of a contributor’s death, the “relevant time” means the time of the contributor’s death.
2. (1) Les définitions qui suivent s’appliquent à la présente loi.
« conjoint de fait » La personne qui, au moment considéré, vit avec un cotisant dans une relation conjugale depuis au moins un an. Il est entendu que, dans le cas du décès du cotisant, « moment considéré » s’entend du moment du décès.

[34] Pursuant to subsection 82(1), a person who is dissatisfied with a Minister’s decision can appeal the decision to the RT. Subsection 83(1) provides that a party may seek leave to appeal an RT decision to the Board within 90 days after receiving the decision or within such longer period as the Chairman or Vice-Chairman of the Board may permit.

[35] An applicant who does not apply for leave to appeal the RT’s decision within 90 days must first be granted a discretionary extension of the time to seek leave. Rules 4 and 5 of the Board Rules outline the information that is required in an application for leave and specify that the applicant must state the grounds on which an extension is sought (Canada (Minister of Human Resources and Development) v Dawdy, 2006 FC 429 at paras 23 -24 [Dawdy]).

[36] The Board’s decision to extend time and grant leave to file an appeal is highly discretionary (Gattellaro, above, at para 4). In the absence of any express statutory limitations on the scope of the discretion delegated to the Board to grant an extension of time, it has broad decision making latitude (Handa, above, at para 11).

[37] The Board must assess the four criteria as set out in Gattellaro, above. With respect to the third criteria, an arguable case in the context of a request for an extension of time requires that some reasonable chance of success at law be established (Canada (Minister of Human Resources Development) v Hogervorst, 2007 FCA 41 at para 37 [Hogervorst]; LeBlanc, above, para 24).

[38] One of the ways to establish an arguable case is to present new or additional evidence that was not before the RT (Leblanc, above, at para 25). Another way to raise an arguable case is through a question of an error of law or an error of fact (Callihoo, above, at para 22).
New Evidence

[39] In assessing whether a decision is reasonable, courts should not substitute their own reasons but may, if they find it necessary, look to the record for the purpose of assessing the reasonableness of the outcome (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 15 [Newfoundland Nurses]). In this case, although the Applicant seeks judicial review of the Board’s Decision, the Court must also look at RT Decision to assess whether the Board reasonably found that the request for an extension of time to seek leave to appeal did not disclose an arguable case based on the record before it (Callihoo, above, at paras 15-16).

[40] Before the RT, the Applicant’s evidence included a statutory declaration by Shane Sager dated February 25, 2009 (Sagar Declaration), in which Mr. Sagar claimed that he lived in a common law relationship with Ms. Morris in her home, from approximately May 8, 2008, until the end of September 2008. The Applicant also submitted a letter dated February 7, 2009 from William Hawkins which stated that, based on an interview with Mr. Sagar, his investigation found that Mr. Sager and Ms. Morris started a common law relationship on approximately May 13, 2008, the same date that Mr. Villeneuve moved into an apartment. And, a letter dated March 26, 2009, from Mr. Villeneuve’s landlords, Wendy and Al Zinc, which described their understanding of why Mr. Villeneuve had taken the apartment.

[41] The Applicant submits that the above evidence confirmed that she was the lawful survivor entitled to the CPP survivor’s pension as Ms. Morris was not cohabiting with Mr. Villeneuve until the time of his death and, therefore, was not his common law spouse.

[42] In her application seeking an extension of time to file an appeal of the RT Decision, the Applicant attached the Sagar Declaration and the Hawkins and Zinck letters. She submitted no other evidence to support her application.

[43] I find that the RT had before it, reviewed and considered the Sagar Declaration, the Hawkins and Zinck letters. It was aware of, and acknowledged the fact that Mr. Villeneuve was living in an apartment and not in Ms. Morris’ home at the time of his death. Accordingly, in my view, the Applicant did not submit any significant new or additional evidence that could have given rise to an arguable case in support of her application to extend the time to file her appeal of the RT Decision.

[44] The Applicant relies on Belo-Alves, above, to support her argument that the Board erred by failing to consider the new evidence that would be available to the Board and that was not before the RT. In the context of whether to grant an extension to appeal, Justice Campbell held that the Board should not consider whether it would allow the appeal, only whether the evidence and legal arguments gives the appeal a “reasonable chance of success.”:

[11] With respect to the issue of arguable case, the argument placed before the Board by Counsel for Ms. Belo-Alves has two components: an evidentiary argument that new evidence exists within the medical evidence produced by Ms. Belo-Alves […] and a legal argument that an improper test for new facts was applied […]. On the evidentiary point, what more can she say, and what more is necessary to say to meet this criterion? In my opinion, it is not possible to evaluate the quality of such evidence on an extension application; I find it is enough to show that there is an argument with evidence to substantiate it to meet this particular factor. This Ms. Belo-Alves did do. With respect to the legal argument, in my opinion it has a reasonable chance of success. As a result, I find that the Board’s “nothing” evidentiary finding on this factor is unsupportable.

[45] I do not think that this decision assists the Applicant. In Belo-Alves, the applicant actually submitted new evidence with its application seeking an extension of time. Without assessing the merits of the application, that new evidence was enough to show that the applicant therein had an arguable case. This was also the situation in LeBlanc, above, and Lavin v Canada (Attorney General), 2011 FC 1387 [Lavin].

[46] Here, however, the Applicant relies on anticipatory evidence and speculates as to what that evidence will be and what it will establish. In my view, it was not possible for the Board to determine the existence of an arguable case on the basis of anticipatory new evidence that was not before it. Therefore, the Board made no reviewable error in failing to do so.
Error of Fact or Law

[47] As noted above, the RT considered and specifically referred to the Sagar Declaration and the Hawkins letter. The RT also specifically considered the weight that should be given to that evidence and found that “The attempts in both the declaration and the investigator’s report to use innuendo put into question the veracity of all associated remarks in the declaration and the Investigator’s Report.” The RT found the suggested date of the termination of any cohabitation by Ms. Morris and Mr. Villeneuve and the suggested date of the commencement of the relationship between Ms. Morris and Mr. Sagar to be “too close to be plausible” and most convenient to Mrs. Villeneuve’s case. The RT also referred to the undisputed fact that Mr. Villeneuve had entered into a lease of the Zinck’s apartment and was living there at the time of his death and the explanation for this offered by Ms. Morris. It also specifically references other evidence that it considered in reaching its conclusions.

[48] I see no reason to disturb the Board’s finding, which was highly discretionary, that there was no error of fact or law in the RT Decision. The RT had the benefit of hearing the parties oral testimony as well as reviewing the documentary evidence. It was entitled to decide on the reliability and weight of the evidence before it. The RT was also entitled to prefer some evidence over other evidence, as long as the evidence was not of such probative value that doing so would amount to a failure to discharge its elementary duty to engage in a meaningful analysis of the evidence (Dossa, above, at para 4). That was not the situation in this case.

[49] The Board properly considered whether the application for an extension of time to appeal the RT decision raised an arguable case. It reasonably found that the RT had clearly set out its findings, assessments of credibility and its reasons for its conclusions and that the RT Decision did not raise a question of law or error of significant fact. Provided that the record demonstrates that there was a reasonable evidentiary basis upon which the Board could assess the existence of an arguable case, as it does here, then it is not the role of this court to re-weigh the evidence on judicial review (Gattellaro, above, at para 10; Janzen v Canada (Attorney General), 2008 FCA 150; Dossa, above, at para 4).

[50] The Applicant also submits that the Board failed to explain why the Applicant’s submissions did not raise an arguable case. However, the reasons offered for a decision are to be assessed along with the outcome of that decision to determine whether the decision as a whole is reasonable, “adequacy of reasons” is no longer a stand-alone ground for challenging a decision (Newfoundland Nurses, above, at para 14).

[51] Here the Board stated that it found nothing in the complete file before it that would allow it to determine that the Applicant had an arguable case in accordance with the principles of law set out in Callihoo, above. A decision-maker is presumed to have considered all the evidence before it (Florea v Canada (Minister of Employment and Immigration), [1993] FCJ No 598 [Florea]) and the Court will consider putting aside this presumption only when the probative value of the evidence that is not expressly discussed is such that it should have been addressed (Cepeda-Gutierrez v Canada (Minister of Citizenship and Immigration), (1998) 157 FTR 35 at paras 14-17 [Cepeda]).

[52] The submissions contained in the July 25, 2012 letter from the Applicant’s counsel rely on evidence that was before the RT and on anticipatory evidence, addressed above. Those submissions essentially restate the Applicant’s arguments made before the RT. Although the Board did not address the specifics of the submissions, they were referred to in its Decision and it did state that there was nothing in the record before it that would allow it to determine that the Applicant raised an arguable case. The Board is not required or expected to refer to every document (Dossa, above, para 4). The Board’s reasons were adequate and its Decision was reasonable being transparent, justifiable, intelligible and within the range of acceptable outcomes.

[53] As to the Board’s statement that the test for an extension of time is conjunctive in reliance on Clayton, above, recent case law states that the test can still be met even if one of the criterion is not met (Blondahl, above, at para 18; Canada (Attorney General) v Pentney, 2008 FC 96 at para 40 [Pentney]). However, in my view, the Board’s mistake in describing the test as conjunctive is not fatal to its final decision as the Board clearly stated that it was concerned with the second criterion, that of an “arguable case.”

[54] In my view, the Board did not make a reviewable error in finding that the Applicant had failed to make an arguable case and therefore dismissing her application for an extension of time to appeal the RT’s Decision. Accordingly, I would dismiss this application for judicia

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 23775:4 · paragraphs 62-62

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9edb7ec6670c5eb4d80cbc1ca942dbba7f913f49b8d063219d05f2616c8cf555`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 23775:4:subtheme:1 · paragraphs 62-62

- Raw key terms: `appearances, applicant, attorney, bahaa, baldwin, belleville, canada, corporation`
- Display key terms: `bahaa, baldwin, belleville, corporation`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: bahaa, baldwin, belleville, corporation No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 62-62. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT BY: STRICKLAND J.
DATED: May 14, 2013
APPEARANCES:
J. Keenan Sprague
FOR THE APPLICANT
Bahaa I. Sunallah
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Baldwin Law Professional Corporation
Belleville, Ontario
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Ottawa, Ontario
FOR THE RESPONDENT
