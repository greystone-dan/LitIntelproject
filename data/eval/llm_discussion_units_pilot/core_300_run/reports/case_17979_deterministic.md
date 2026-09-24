# Discussion Units: case 17979

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **22**
- Continuity pairs: **21**
- Discussion Units: **2**
- Paragraph source hashes: **22**
- Sub-themes: **7**

## 17979:1 · paragraphs 0-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e0718cd781eae55028c307eec00ba832764dc32487603f7cc2e2b8240c387ae6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 17979:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `brovina, canada, albania, albanian, applicant, april, based, belief`
- Display key terms: `brovina, albania, albanian, april, based, belief`
- Argument roles: `party_position`
- Explanation: Observed roles: party_position Display terms: brovina, albania, albanian, april, based, belief Position/evidence statements: She claims a well-founded fear of persecution based on her membership in a social group - a family member of her son, Fisnik Brovina, who based his claim on political belief. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4851988` offsets `123-129`; context: She claims a well-founded fear of persecution based on her membership in a social group - a family member of her son, Fisnik Brovina, who based his claim on political belief.

#### 17979:1:subtheme:2 · paragraphs 2-3

- Raw key terms: `board, brovina, academic, accepted, active, albania, although, apartment`
- Display key terms: `brovina, academic, accepted, active, albania, although, apartment`
- Argument roles: `counterargument_limitation, evidence_fact, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, reasoning_application Display terms: brovina, academic, accepted, active, albania, although, apartment Application context: [2] The couple were accepted as refugees based on persecution because of their political opinion. Evidence spans paragraphs 2-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `4851989` offsets `173-183`; context: The Refugee Protection Division of the Immigration and Refugee Board (RPD) found that Mrs.
- Evidence: `reasoning_application` cue `because` at chunk `4851989` offsets `62-69`; context: [2] The couple were accepted as refugees based on persecution because of their political opinion.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4851990` offsets `125-133`; context: Although the arguments are interesting from an academic perspective, the facts of this particular matter do not support them.

#### 17979:1:subtheme:3 · paragraphs 4-12

- Raw key terms: `brovina, persecution, because, board, argument, past, finding, found`
- Display key terms: `brovina, persecution, because, argument, past, finding`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: brovina, persecution, because, argument, past, finding Rule/authority context: [4] The first alleged error is that the RPD erred by failing to consider the "compelling reasons" exception under section 108 of the Immigration and Refugee Protection Act, S. | It is only then that the Board should consider whether the nature of the claimant's experiences in the former country were so appalling that he or she should not be expected to return and put himself or herself under the Application context: The gist of this argument is that the RPD found, in the same decision, that because Mrs. | On the contrary, it noted that very few Albanians qualify as refugees because of political involvement. Evidence spans paragraphs 4-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4851991` offsets `625-632`; context: Brovina left Albania had ceased to exist - because of the board's own decision - it should have determined whether there are compelling reasons that she should not be returned to Albania.
- Evidence: `governing_rule` cue `under` at chunk `4851991` offsets `108-113`; context: [4] The first alleged error is that the RPD erred by failing to consider the "compelling reasons" exception under section 108 of the Immigration and Refugee Protection Act, S.
- Evidence: `reasoning_application` cue `because` at chunk `4851991` offsets `274-281`; context: The gist of this argument is that the RPD found, in the same decision, that because Mrs.
- Evidence: `issue` cue `whether` at chunk `4851992` offsets `392-399`; context: It is only then that the Board should consider whether the nature of the claimant's experiences in the former country were so appalling that he or she should not be expected to return and put himself or herself under the protection of that state.
- Evidence: `governing_rule` cue `under` at chunk `4851992` offsets `556-561`; context: It is only then that the Board should consider whether the nature of the claimant's experiences in the former country were so appalling that he or she should not be expected to return and put himself or herself under the protection of that state.
- Evidence: `evidence_fact` cue `evidence` at chunk `4851993` offsets `702-710`; context: However, there was no evidence to suggest that the perpetrators were interested in her.
- Evidence: `reasoning_application` cue `because` at chunk `4851993` offsets `279-286`; context: On the contrary, it noted that very few Albanians qualify as refugees because of political involvement.
- Evidence: `evidence_fact` cue `evidence` at chunk `4851994` offsets `135-143`; context: Brovina submits that the credibility of her evidence and her subjective fear were accepted by the board.
- Evidence: `reasoning_application` cue `because` at chunk `4851994` offsets `325-332`; context: Although the board did not explicitly state that she was subject to past persecution, she contends that it is clear that she was because of the phone calls and the home invasion in which she was involved.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4851994` offsets `196-204`; context: Although the board did not explicitly state that she was subject to past persecution, she contends that it is clear that she was because of the phone calls and the home invasion in which she was involved.
- Evidence: `reasoning_application` cue `because` at chunk `4851996` offsets `60-67`; context: [9] There was no need to make a finding of past persecution because the RPD made (properly) a forward-looking analysis and concluded that Mrs.
- Evidence: `evidence_fact` cue `found that` at chunk `4851997` offsets `96-106`; context: Brovina argues that the RPD erred in relation to the burden of proof because it found that, on a balance of probabilities, there was not a serious possibility that Mrs.
- Evidence: `reasoning_application` cue `because` at chunk `4851997` offsets `85-92`; context: Brovina argues that the RPD erred in relation to the burden of proof because it found that, on a balance of probabilities, there was not a serious possibility that Mrs.
- Evidence: `counterargument_limitation` cue `but` at chunk `4851997` offsets `308-311`; context: She submits that the burden to establish facts is the balance of probabilities, but the burden in terms of well-foundedness is serious grounds to consider (more than a mere possibility).
- Evidence: `evidence_fact` cue `evidence` at chunk `4851998` offsets `264-272`; context: The RPD based its findings on the balance of probabilities that there was not a serious possibility of persecution: "Nothing in the evidence before me indicates that should the principal claimant's mother return to Albania, on balance of probabilities, there is a serious possibility that she would be targeted for persecution".
- Evidence: `reasoning_application` cue `because` at chunk `4851998` offsets `916-923`; context: Thus, the threshold for the disputed burden of proof was not engaged because the board found there was no evidence to find any kind of risk.
- Evidence: `counterargument_limitation` cue `although` at chunk `4851998` offsets `520-528`; context: This is not an incorrect formulation of the relevant test, although the sentence may be somewhat awkwardly worded.
- Evidence: `governing_rule` cue `under` at chunk `4851999` offsets `96-101`; context: Brovina submits that it was incumbent on the RPD to conduct a separate analysis under section 97.

#### 17979:1:subtheme:4 · paragraphs 13-16

- Raw key terms: `canada, citizenship, immigration, justice, minister, section, board, board's`
- Display key terms: `justice, section, board's`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: justice, section, board's Rule/authority context: It is evident that in Kilic, supra, there was evidence that was not addressed under the section 96 analysis that should have received section 97 consideration. Application context: Therefore, the result of the Board's error is unknown, and accordingly, this application should be sent back for redetermination on this ground. | Justice von Finckenstein found that the board's negative credibility finding was substantiated by the facts and that the failure to perform a section 97 analysis was not relevant to the result because of a lack of eviden Evidence spans paragraphs 13-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4852000` offsets `119-124`; context: Justice Blanchard discussed this issue in the context of a situation where identity was not disputed, but the country conditions might lead to an objective fear (though still based on personal circumstances) of section 97 risk, even if the subjective fear was found to be not credible.
- Evidence: `issue` cue `whether` at chunk `4852001` offsets `282-289`; context: Justice Mosley, at paragraph 27 stated:
In my opinion, the Board in this case did not address the country documentation and other evidence related to prison conditions in Turkey and failed to consider whether the applicant could be a "person in need of protection" if returned to that country, in light of the possibility that he may face a "serious prison sentence" for evading Turkish military service.
- Evidence: `evidence_fact` cue `evidence` at chunk `4852001` offsets `211-219`; context: Justice Mosley, at paragraph 27 stated:
In my opinion, the Board in this case did not address the country documentation and other evidence related to prison conditions in Turkey and failed to consider whether the applicant could be a "person in need of protection" if returned to that country, in light of the possibility that he may face a "serious prison sentence" for evading Turkish military service.
- Evidence: `governing_rule` cue `under` at chunk `4852001` offsets `966-971`; context: It is evident that in Kilic, supra, there was evidence that was not addressed under the section 96 analysis that should have received section 97 consideration.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4852001` offsets `743-752`; context: Therefore, the result of the Board's error is unknown, and accordingly, this application should be sent back for redetermination on this ground.
- Evidence: `evidence_fact` cue `found that` at chunk `4852002` offsets `110-120`; context: Justice von Finckenstein found that the board's negative credibility finding was substantiated by the facts and that the failure to perform a section 97 analysis was not relevant to the result because of a lack of evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4852002` offsets `278-285`; context: Justice von Finckenstein found that the board's negative credibility finding was substantiated by the facts and that the failure to perform a section 97 analysis was not relevant to the result because of a lack of evidence.
- Evidence: `evidence_fact` cue `determined that` at chunk `4852003` offsets `105-120`; context: Canada (Minister of Citizenship and Immigration) 2004 FC 79 determined that the board did not err in arriving at its negative credibility finding.
- Evidence: `reasoning_application` cue `because` at chunk `4852003` offsets `496-503`; context: Justice Gibson further determined that the claimant was not a person in need of protection because no ground to support a need of protection other than a Convention ground had been advanced.

#### 17979:1:subtheme:5 · paragraphs 17-18

- Raw key terms: `analysis, board, evidence, performed, section, support, albania, authorities`
- Display key terms: `analysis, performed, section, support, albania, authorities`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: analysis, performed, section, support, albania, authorities Evidence spans paragraphs 17-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4852004` offsets `156-164`; context: It is a question that must be reviewed on a case by case basis.
- Evidence: `evidence_fact` cue `evidence` at chunk `4852004` offsets `224-232`; context: If there is evidence before the board to support a section 97 analysis, the analysis must be conducted.
- Evidence: `evidence_fact` cue `evidence` at chunk `4852005` offsets `155-163`; context: [18] Thus, while a separate section 97 analysis is desirable, the failure to conduct such an analysis will not be fatal in circumstances where there is no evidence that would require it.

#### 17979:1:subtheme:6 · paragraphs 19-20

- Raw key terms: `brovina, respondent, agree, applicable, applicant, application, appropriate, april`
- Display key terms: `brovina, agree, applicable, appropriate, april`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: brovina, agree, applicable, appropriate, april Operative outcome context: ORDER IT IS HEREBY ORDERED THAT the application for judicial review is dismissed. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4852006` offsets `159-164`; context: Brovina suggested that if my decision in this matter turned on the standard of proof tests in paragraphs 97(1)(a) and 97(1)(b), that the issue of the applicable standard would be one that is appropriate for certification.
- Evidence: `evidence_fact` cue `Record` at chunk `4852006` offsets `553-559`; context: FEDERAL COURT
Names of Counsel and Solicitors of Record
DOCKET: IMM-2427-03
- Evidence: `disposition` cue `dismissed` at chunk `4852006` offsets `433-442`; context: ORDER
IT IS HEREBY ORDERED THAT the application for judicial review is dismissed.

#### Section text

Brovina v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2004-04-29
Neutral citation
2004 FC 635
File numbers
IMM-2427-03
Notes
Digest
Decision Content
Date: 20040429
Docket: IMM-2427-03
Citation: 2004 FC 635
Toronto, Ontario, April 29th, 2004
Present: The Honourable Madam Justice Layden-Stevenson
BETWEEN:
QEFSERE BROVINA
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER AND ORDER

[1] Before coming to Canada, Mrs. Brovina, a 71-year-old Albanian citizen, lived with her son and his wife in Albania. She claims a well-founded fear of persecution based on her membership in a social group - a family member of her son, Fisnik Brovina, who based his claim on political belief. Mrs. Brovina's personal information form (PIF) narrative stated that she relied upon her son's narrative. Her son's narrative in turn incorporated the incidents recounted in his wife's narrative. The claims of Mrs. Brovina's son and daughter-in-law were joined with her claim.

[2] The couple were accepted as refugees based on persecution because of their political opinion. The Refugee Protection Division of the Immigration and Refugee Board (RPD) found that Mrs. Brovina was not personally in any danger in Albania and, since her son and his wife were staying in Canada, she should have no difficulty upon her return. The board found that Mrs. Brovina was not politically active and, while she had received harassing calls for her son and had been present when her son's apartment was ransacked, she had not been personally targeted. With the successful claimants in Canada, Mrs. Brovina could safely return to Albania without fear of retaliation.

[3] Mrs. Brovina says that the board made some errors and that the matter should be returned to the RPD for redetermination. Although the arguments are interesting from an academic perspective, the facts of this particular matter do not support them.

[4] The first alleged error is that the RPD erred by failing to consider the "compelling reasons" exception under section 108 of the Immigration and Refugee Protection Act, S.C. 2001, c. 27 (IRPA). The gist of this argument is that the RPD found, in the same decision, that because Mrs. Brovina's son and daughter-in-law were accepted as refugees, they would not be going back to Albania and the reason for which Mrs. Brovina was persecuted in Albania would therefore no longer exist. Since the reasons for which Mrs. Brovina left Albania had ceased to exist - because of the board's own decision - it should have determined whether there are compelling reasons that she should not be returned to Albania.

[5] The difficulty with this argument is that the RPD did not find that Mrs. Brovina had suffered past persecution. For the board to embark on a compelling reasons analysis, it must first find that there was a valid refugee (or protected person) claim and that the reasons for the claim have ceased to exist (due to changed country conditions). It is only then that the Board should consider whether the nature of the claimant's experiences in the former country were so appalling that he or she should not be expected to return and put himself or herself under the protection of that state.

[6] Here, there was no finding of past persecution and it is implicit in the decision that, notwithstanding that the RPD believed Mrs. Brovina, it did not accept that she had been subject to past persecution. On the contrary, it noted that very few Albanians qualify as refugees because of political involvement. The leadership roles and the high level positions held by Mrs. Brovina's son and daughter-in-law in the Democratic Party constituted the reason for allowing their claims. Mrs. Brovina, on the other hand, was never politically active. She was, unfortunately, in her son's apartment when it was ransacked and she, again unfortunately, happened to answer the telephone. However, there was no evidence to suggest that the perpetrators were interested in her. In the absence of a finding of past persecution, subsection 108(4) has no application.

[7] The second argument is that the RPD failed to make a finding on past persecution. Mrs. Brovina submits that the credibility of her evidence and her subjective fear were accepted by the board. Although the board did not explicitly state that she was subject to past persecution, she contends that it is clear that she was because of the phone calls and the home invasion in which she was involved. Based on the same events, the board found that the younger claimants were refugees.

[8] This argument relates back to the first. While the RPD did not expressly state that she did not experience past persecution, as noted earlier, the finding is implicit in the reasons. Moreover, the board did not, as alleged, find that Mrs. Brovina's son and daughter-in-law were Convention refugees based on the same events as those that Mrs. Brovina experienced. Both were subject to considerable threats and violent events - in the case of the daughter-in-law, sexual assault and in the case of the son, beatings and threats to his life. That was not so with respect to Mrs. Brovina.

[9] There was no need to make a finding of past persecution because the RPD made (properly) a forward-looking analysis and concluded that Mrs. Brovina would not suffer future persecution. It was reasonably open to the board to make the finding it made - that if Mrs. Brovina was not living with her son, she would be in no more danger than was her second son, who remained safely in Albania.

[10] Next, Mrs. Brovina argues that the RPD erred in relation to the burden of proof because it found that, on a balance of probabilities, there was not a serious possibility that Mrs. Brovina would be targeted for persecution. She submits that the burden to establish facts is the balance of probabilities, but the burden in terms of well-foundedness is serious grounds to consider (more than a mere possibility). It is alleged that the board also erred in relation to section 97 in referring to a likelihood of risk. Section 97, it is said, arguably has a higher burden of proof than section 96. The test for section 96 is reasonable chance, but a mere risk is a lower threshold still. Furthermore, paragraphs 97(1)(a) and 97(1)(b) arguably do not have the same test since 97(1)(a) refers to risk of torture on substantial grounds, while 97(1)(b) refers only to risk.

[11] This argument is academic. Regardless of the standard of proof, it could have made no difference to the findings in this case. The RPD based its findings on the balance of probabilities that there was not a serious possibility of persecution: "Nothing in the evidence before me indicates that should the principal claimant's mother return to Albania, on balance of probabilities, there is a serious possibility that she would be targeted for persecution". This is not an incorrect formulation of the relevant test, although the sentence may be somewhat awkwardly worded. The board also found that there was "no reason to believe that she should be in any way targeted" and "no reason to believe that ... she should face any more likelihood than her son in Albania of persecution or of risk to life or a risk of cruel and unusual punishment". Thus, the threshold for the disputed burden of proof was not engaged because the board found there was no evidence to find any kind of risk.

[12] Last, Mrs. Brovina submits that it was incumbent on the RPD to conduct a separate analysis under section 97. Referring to recent authority from this court, she argues that unless the RPD decision turns on credibility - which is not the case - it must conduct a separate section 97 analysis. The exception regarding credibility, it is said, can be gleaned from the cases.

[13] In Bouaouni v. Canada (Minister of Citizenship and Immigration)2003 FC 1211, Mr. Justice Blanchard discussed this issue in the context of a situation where identity was not disputed, but the country conditions might lead to an objective fear (though still based on personal circumstances) of section 97 risk, even if the subjective fear was found to be not credible. Justice Blanchard noted the distinction between section 96 and section 97 claims and stated that although the evidentiary basis may be the same, the claims should be considered as separate. Most importantly, for present purposes, he stated, "Whether a Board properly considered both claims is a matter to be determined in the circumstances of each individual case bearing in mind the different elements required to establish each claim". Although the board had erred in failing to specifically analyze the section 97 claim, its error was not material to the result in that case.

[14] In Kilic v. Canada (Minister of Citizenship and Immigration)2004 FC 84, Mr. Justice Mosley, at paragraph 27 stated:
In my opinion, the Board in this case did not address the country documentation and other evidence related to prison conditions in Turkey and failed to consider whether the applicant could be a "person in need of protection" if returned to that country, in light of the possibility that he may face a "serious prison sentence" for evading Turkish military service. Despite the Board's negative credibility findings, a separate analysis, along the lines described in Bouaouni, supra, and having regard to the legislative wording of section 97, may have produced a finding that Mr. Kilic was a person in need of protection. Therefore, the result of the Board's error is unknown, and accordingly, this application should be sent back for redetermination on this ground.
It is evident that in Kilic, supra, there was evidence that was not addressed under the section 96 analysis that should have received section 97 consideration.

[15] In Yorulmaz v. Canada (Minister of Citizenship and Immigration)2004 FC 128, Mr. Justice von Finckenstein found that the board's negative credibility finding was substantiated by the facts and that the failure to perform a section 97 analysis was not relevant to the result because of a lack of evidence.

[16] Mr. Justice Gibson, in Kulendrarajah v. Canada (Minister of Citizenship and Immigration) 2004 FC 79 determined that the board did not err in arriving at its negative credibility finding. Since the sole bases for the claim were Convention grounds (ethnicity and membership in a particular social group), the board's credibility and risk analyses were sufficient to support a denial of refugee status. Justice Gibson further determined that the claimant was not a person in need of protection because no ground to support a need of protection other than a Convention ground had been advanced. While a more extensive explanation for the board's determination regarding section 97 might have been desirable, its absence did not constitute reviewable error.

[17] These authorities, in my view, do not demand that a section 97 analysis be performed in every case. Rather, it will be required in some cases. It is a question that must be reviewed on a case by case basis. If there is evidence before the board to support a section 97 analysis, the analysis must be conducted.

[18] Thus, while a separate section 97 analysis is desirable, the failure to conduct such an analysis will not be fatal in circumstances where there is no evidence that would require it. Here, there were no other grounds to support a finding of person in need of protection and the risk analysis was performed for Mrs. Brovina in the context of refugee protection. Moreover, the board did conduct a brief analysis related to a section 97 risk when it found that there was "no reason to believe" that Mrs. Brovina would face any risk in returning to Albania. There was no objective evidence before the board that might have led to any other conclusion.

[19] Counsel for Mrs. Brovina suggested that if my decision in this matter turned on the standard of proof tests in paragraphs 97(1)(a) and 97(1)(b), that the issue of the applicable standard would be one that is appropriate for certification. That is not the case. The respondent opposed certification on the basis that there is no factual foundation. I agree.
ORDER
IT IS HEREBY ORDERED THAT the application for judicial review is dismissed. No question is certified.
"Carolyn Layden-Stevenson"
J.F.C.
FEDERAL COURT
Names of Counsel and Solicitors of Record
DOCKET: IMM-2427-03

STYLE OF CAUSE: QEFSERE BROVINA
Applicant
and
THE MINISTER OF CITIZENSHIP AND
IMMIGRATION
Respondent
PLACE OF HEARING: TORONTO, ONTARIO
DATE OF HEARING: APRIL 22, 2004
REASONS FOR 

## 17979:2 · paragraphs 21-21

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `857d68eec76b6e628412df0b56b81c728e219caae2a3857188e93aafab737f8e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 17979:2:subtheme:1 · paragraphs 21-21

- Raw key terms: `appearances, applicant, april, attorney, barrister, brovina, canada, citizenship`
- Display key terms: `april, barrister, brovina`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, barrister, brovina No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 21-21. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER
AND ORDER BY: LAYDEN-STEVENSON J.
DATED: APRIL 29, 2004
APPEARANCES BY: Mr. Micheal Crane
For the Applicant
Ms. Ann Margaret Oberst
For the Respondent
SOLICITORS OF RECORD: Micheal Crane
Barrister & Solicitor
Toronto, Ontario
For the Applicant
Morris Rosenberg
Deputy Attorney General of Canada
For the Respondent
FEDERAL COURT
TRIAL DIVISION
Date: 20040429
Docket: IMM-2427-03
BETWEEN:
QEFSERE BROVINA
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR ORDER
AND ORDER
