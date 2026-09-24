# Discussion Units: case 26315

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **38**
- Continuity pairs: **37**
- Discussion Units: **3**
- Paragraph source hashes: **38**
- Sub-themes: **13**

## 26315:1 · paragraphs 0-34

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d826812688d249823c9ed90aa37f4e5522b4c405a6068aad4b6ca3de4e01c9a4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26315:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `applicant, canada, claims, decision, china, christian, church, filed`
- Display key terms: `claims, china, christian, church, filed`
- Argument roles: `disposition, governing_rule, party_position`
- Explanation: Observed roles: disposition, governing_rule, party_position Display terms: claims, china, christian, church, filed Position/evidence statements: [2] The applicant is a citizen of the People’s Republic of China from Shijiazhuang, Hebei province and claims that he was a member of an underground Christian house church that was raided by the Public Security Bureau [P | [3] Once in Canada, the applicant joined a Pentecostal church (the Living Stone Assembly in Scarborough, Ontario) and claims to be a practicing Christian. Rule/authority context: [1] This is an application for judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board [RPD or the Board], dated October 27, 2011, in which the Board dismissed the applican Operative outcome context: [1] This is an application for judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board [RPD or the Board], dated October 27, 2011, in which the Board dismissed the applican Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `5237191` offsets `231-236`; context: [1] This is an application for judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board [RPD or the Board], dated October 27, 2011, in which the Board dismissed the applicant’s claims under section 96 and subsection 97(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act].
- Evidence: `disposition` cue `dismissed` at chunk `5237191` offsets `198-207`; context: [1] This is an application for judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board [RPD or the Board], dated October 27, 2011, in which the Board dismissed the applicant’s claims under section 96 and subsection 97(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act].
- Evidence: `party_position` cue `claims` at chunk `5237192` offsets `103-109`; context: [2] The applicant is a citizen of the People’s Republic of China from Shijiazhuang, Hebei province and claims that he was a member of an underground Christian house church that was raided by the Public Security Bureau [PSB] in 2010.
- Evidence: `party_position` cue `claims` at chunk `5237193` offsets `118-124`; context: [3] Once in Canada, the applicant joined a Pentecostal church (the Living Stone Assembly in Scarborough, Ontario) and claims to be a practicing Christian.

#### 26315:1:subtheme:2 · paragraphs 4-9

- Raw key terms: `applicant, board, china, christian, church, fraudulent, alleged, application`
- Display key terms: `china, christian, church, fraudulent, alleged`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, party_position, reasoning_application Display terms: china, christian, church, fraudulent, alleged Position/evidence statements: The applicant claimed to have no knowledge of any such application. | The Board reasoned in this regard that if the applicant had really been a consistent church-goer in China, as he claimed, he ought to have been able to recall that Easter Sunday was just a week before his church had been Application context: The Board determined that the first document was not genuine and gave little weight to the letter from the applicant’s mother because his parents had been complicit in his earlier fraudulent student visa application. Operative outcome context: In his testimony before the Board, the applicant denied any knowledge of the student visa application, despite the fact that the visa file contained a picture of him, his passport number and date of birth. Evidence spans paragraphs 4-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `5237194` offsets `14-29`; context: [4] The Board determined that there was no credible basis for the applicant’s claim and, as a result, that he was neither a Convention refugee nor a person in need of protection.
- Evidence: `disposition` cue `denied` at chunk `5237194` offsets `456-462`; context: In his testimony before the Board, the applicant denied any knowledge of the student visa application, despite the fact that the visa file contained a picture of him, his passport number and date of birth.
- Evidence: `party_position` cue `claimed` at chunk `5237195` offsets `244-251`; context: The applicant claimed to have no knowledge of any such application.
- Evidence: `counterargument_limitation` cue `However` at chunk `5237195` offsets `1100-1107`; context: However, he continued to deny that he had any knowledge of the application.
- Evidence: `party_position` cue `claimed` at chunk `5237196` offsets `522-529`; context: The Board reasoned in this regard that if the applicant had really been a consistent church-goer in China, as he claimed, he ought to have been able to recall that Easter Sunday was just a week before his church had been raided.
- Evidence: `counterargument_limitation` cue `However` at chunk `5237196` offsets `221-228`; context: However, he could not remember the date of Easter in 2010.
- Evidence: `evidence_fact` cue `determined that` at chunk `5237197` offsets `39-54`; context: [7] In light of these facts, the Board determined that the applicant was not a practicing Christian in China, that the alleged raid on his house church did not occur and that none of his fellow alleged church members had been arrested or incarcerated.
- Evidence: `reasoning_application` cue `because` at chunk `5237197` offsets `573-580`; context: The Board determined that the first document was not genuine and gave little weight to the letter from the applicant’s mother because his parents had been complicit in his earlier fraudulent student visa application.
- Evidence: `party_position` cue `claim` at chunk `5237198` offsets `141-146`; context: [8] After determining that the applicant had not been a practicing Christian in China, the Board went on to assess the applicant’s sur place claim, or his claim to have acquired refugee status through his adherence to Christianity in Canada.
- Evidence: `evidence_fact` cue `determined that` at chunk `5237199` offsets `14-29`; context: [9] The Board determined that, in light of its credibility findings, the claimant had joined a Christian church in Canada only for the purpose of supporting a fraudulent refugee claim.

#### 26315:1:subtheme:3 · paragraphs 10-12

- Raw key terms: `applicant, finding, application, argues, beliefs, board, canada, china`
- Display key terms: `finding, argues, beliefs, china`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: finding, argues, beliefs, china Position/evidence statements: [11] The applicant argues that the RPD’s decision should be set aside because its credibility findings were unreasonable. | [12] The respondent, on the other hand, submits that it was reasonable for the Board to draw a negative inference from the applicant’s student visa application and from the applicant’s inability to remember the date of E Rule/authority context: The applicant also argues that the Board failed to properly consider evidence of the genuineness of his religious beliefs and practices and that it was improper for the Board to have considered his motive in joining and  Application context: [10] The RPD therefore dismissed the applicant’s claim, finding the applicant had not satisfied the burden of establishing a serious possibility that he would be persecuted or subjected to risk to his life, risk of cruel | [11] The applicant argues that the RPD’s decision should be set aside because its credibility findings were unreasonable. Operative outcome context: [10] The RPD therefore dismissed the applicant’s claim, finding the applicant had not satisfied the burden of establishing a serious possibility that he would be persecuted or subjected to risk to his life, risk of cruel Evidence spans paragraphs 10-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `5237200` offsets `300-306`; context: Issues
- Evidence: `reasoning_application` cue `therefore` at chunk `5237200` offsets `13-22`; context: [10] The RPD therefore dismissed the applicant’s claim, finding the applicant had not satisfied the burden of establishing a serious possibility that he would be persecuted or subjected to risk to his life, risk of cruel and unusual treatment or punishment or danger of torture if returned to China.
- Evidence: `disposition` cue `dismissed` at chunk `5237200` offsets `23-32`; context: [10] The RPD therefore dismissed the applicant’s claim, finding the applicant had not satisfied the burden of establishing a serious possibility that he would be persecuted or subjected to risk to his life, risk of cruel and unusual treatment or punishment or danger of torture if returned to China.
- Evidence: `party_position` cue `argues` at chunk `5237201` offsets `19-25`; context: [11] The applicant argues that the RPD’s decision should be set aside because its credibility findings were unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `5237201` offsets `909-917`; context: The applicant also argues that the Board failed to properly consider evidence of the genuineness of his religious beliefs and practices and that it was improper for the Board to have considered his motive in joining and participating in the activities of the Living Stone Assembly because the presence or absence of a good faith motive for engaging in activities that may give rise to a sur place claim is irrelevant to the assessment of the validity of such a claim under Canadian law.
- Evidence: `governing_rule` cue `under` at chunk `5237201` offsets `1307-1312`; context: The applicant also argues that the Board failed to properly consider evidence of the genuineness of his religious beliefs and practices and that it was improper for the Board to have considered his motive in joining and participating in the activities of the Living Stone Assembly because the presence or absence of a good faith motive for engaging in activities that may give rise to a sur place claim is irrelevant to the assessment of the validity of such a claim under Canadian law.
- Evidence: `reasoning_application` cue `because` at chunk `5237201` offsets `70-77`; context: [11] The applicant argues that the RPD’s decision should be set aside because its credibility findings were unreasonable.
- Evidence: `party_position` cue `submits` at chunk `5237202` offsets `40-47`; context: [12] The respondent, on the other hand, submits that it was reasonable for the Board to draw a negative inference from the applicant’s student visa application and from the applicant’s inability to remember the date of Easter.
- Evidence: `evidence_fact` cue `evidence` at chunk `5237202` offsets `1063-1071`; context: The respondent also argues that the Board did not place an improper reliance on the applicant’s motives and that the Board’s finding that the applicant had not demonstrated that he was a genuine Christian in Canada is reasonable in light of the applicant’s lack of credibility and the lack of other evidence about sincerity of his beliefs.

#### 26315:1:subtheme:4 · paragraphs 13-14

- Raw key terms: `applicable, applicant, board, christianity, credibility, errors, findings, issues`
- Display key terms: `applicable, christianity, credibility, errors, findings, issues`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: applicable, christianity, credibility, errors, findings, issues Rule/authority context: What standard of review is applicable to the errors the applicant alleges were made by the RPD; 2. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5237203` offsets `37-43`; context: [13] In light of the foregoing, four issues arise in this matter:
1.
- Evidence: `governing_rule` cue `standard of review` at chunk `5237203` offsets `74-92`; context: What standard of review is applicable to the errors the applicant alleges were made by the RPD;
2.
- Evidence: `issue` cue `question` at chunk `5237204` offsets `528-536`; context: The question concerning the consideration of the applicant’s motives for practicing Christianity in Canada and concerning the reasonableness of the RPD’s decision are intertwined: the lack of good faith motive was an important consideration of the RPD in determining that the applicant’s beliefs were not sincere.

#### 26315:1:subtheme:5 · paragraphs 15-15

- Raw key terms: `acceptable, afford, agrees, applicable, applying, board, cannot, conclusion`
- Display key terms: `acceptable, afford, agrees, applicable, applying, cannot, conclusion`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: acceptable, afford, agrees, applicable, applying, cannot, conclusion Rule/authority context: So long as the reasons are understandable and the result is one that is rational and supportable in light of the facts and the applicable law, a court should not overturn an inferior tribunal’s decision under the reasona Evidence spans paragraphs 15-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5237205` offsets `468-475`; context: In applying this deferential standard, it matters not whether the reviewing court agrees with a tribunal’s conclusion, would have reached a different result or might have reasoned differently.
- Evidence: `governing_rule` cue `under` at chunk `5237205` offsets `810-815`; context: So long as the reasons are understandable and the result is one that is rational and supportable in light of the facts and the applicable law, a court should not overturn an inferior tribunal’s decision under the reasonableness standard of review.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5237205` offsets `136-142`; context: [15] The reasonableness standard is an exacting one and requires the reviewing court afford deference to a tribunal’s decision; a court cannot intervene unless it is satisfied that the reasons of a tribunal are not justified, transparent or intelligible and that the result does not fall “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at para 47).

#### 26315:1:subtheme:6 · paragraphs 16-17

- Raw key terms: `applicant, application, board, date, fraudulent, made, student, visa`
- Display key terms: `date, fraudulent, made, student, visa`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: date, fraudulent, made, student, visa Application context: In the absence of any such explanation, the Board drew the obvious conclusion, namely, that the applicant was complicit in making the application, which is accordingly a reasonable finding. Evidence spans paragraphs 16-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `determined that` at chunk `5237206` offsets `84-99`; context: [16] As noted, the applicant alleges that it was unreasonable for the Board to have determined that the applicant made a fraudulent student visa application in 2009 and that the Board’s reliance on the applicant’s inability to remember the date of Easter in 2010 was unreasonable.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5237207` offsets `448-459`; context: In the absence of any such explanation, the Board drew the obvious conclusion, namely, that the applicant was complicit in making the application, which is accordingly a reasonable finding.

#### 26315:1:subtheme:7 · paragraphs 18-20

- Raw key terms: `applicant, basis, board, church, claim, credibility, factor, motive`
- Display key terms: `basis, church, credibility, factor, motive`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: basis, church, credibility, factor, motive Position/evidence statements: [20] Contrary to what the applicant asserts, the case law recognises that motive for engaging in a religious practice in Canada may be considered by the RPD in an appropriate case. Application context: It was accordingly reasonable for the RPD to determine the applicant’s inability to remember Easter to be a factor in support of a negative inference regarding his credibility. Evidence spans paragraphs 18-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5237208` offsets `727-733`; context: Moreover, when questioned about these issues, the applicant obfuscated and backtracked regarding how frequently his pastor attended church.
- Evidence: `evidence_fact` cue `found that` at chunk `5237208` offsets `287-297`; context: The Board did not find the inability to remember to be indicative of a lack of knowledge of the tenets of Christianity but, rather, found that it undercut the applicant’s claim that his church was raided.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5237208` offsets `836-847`; context: It was accordingly reasonable for the RPD to determine the applicant’s inability to remember Easter to be a factor in support of a negative inference regarding his credibility.
- Evidence: `party_position` cue `asserts` at chunk `5237210` offsets `36-43`; context: [20] Contrary to what the applicant asserts, the case law recognises that motive for engaging in a religious practice in Canada may be considered by the RPD in an appropriate case.
- Evidence: `counterargument_limitation` cue `However` at chunk `5237210` offsets `181-188`; context: However, a finding that a claimant was motivated to practice a religion in Canada to buttress a fraudulent refugee claim cannot be used, in and of itself, as a basis to reject the claim.

#### 26315:1:subtheme:8 · paragraphs 21-24

- Raw key terms: `canada, claim, place, applicant, board, cases, country, court`
- Display key terms: `place, cases, country`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: place, cases, country Position/evidence statements: [23] This Court has assessed the requirements of religion-based sur place claims in a series of recent cases. | [24] In a series of recent cases involving claimants from China, this Court has applied the holding in Ejtehadian and held that the Board cannot reject a sur place claim due to lack of credibility or improper motive but, Application context: The Court accordingly set aside the decision of the Board, which had focused on the fact that the applicant had obtained an exit visa from Iran, as opposed to the risk that subsequent events in the country had created fo | The Board dismissed his claim because it determined that his conversion was not genuine, finding that he had become a Christian in order to obtain a means of remaining in Canada and claiming refugee status. Operative outcome context: The Board dismissed his claim because it determined that his conversion was not genuine, finding that he had become a Christian in order to obtain a means of remaining in Canada and claiming refugee status. Evidence spans paragraphs 21-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5237211` offsets `47-52`; context: [21] The sincerity of those beliefs will be an issue in cases, like the present, where continuing the religious practice in the country of origin might place the claimant at risk.
- Evidence: `counterargument_limitation` cue `but` at chunk `5237211` offsets `579-582`; context: On the other hand, there may well be situations where a claimant might initially have been motivated to join a religion due to these types of motivations, but along the route, may have developed faith and become a true adherent of the religion.
- Evidence: `reasoning_application` cue `accordingly` at chunk `5237212` offsets `420-431`; context: The Court accordingly set aside the decision of the Board, which had focused on the fact that the applicant had obtained an exit visa from Iran, as opposed to the risk that subsequent events in the country had created for him if he returned.
- Evidence: `party_position` cue `claims` at chunk `5237213` offsets `74-80`; context: [23] This Court has assessed the requirements of religion-based sur place claims in a series of recent cases.
- Evidence: `evidence_fact` cue `determined that` at chunk `5237213` offsets `261-276`; context: The Board dismissed his claim because it determined that his conversion was not genuine, finding that he had become a Christian in order to obtain a means of remaining in Canada and claiming refugee status.
- Evidence: `reasoning_application` cue `because` at chunk `5237213` offsets `250-257`; context: The Board dismissed his claim because it determined that his conversion was not genuine, finding that he had become a Christian in order to obtain a means of remaining in Canada and claiming refugee status.
- Evidence: `disposition` cue `dismissed` at chunk `5237213` offsets `230-239`; context: The Board dismissed his claim because it determined that his conversion was not genuine, finding that he had become a Christian in order to obtain a means of remaining in Canada and claiming refugee status.
- Evidence: `party_position` cue `claim` at chunk `5237214` offsets `164-169`; context: [24] In a series of recent cases involving claimants from China, this Court has applied the holding in Ejtehadian and held that the Board cannot reject a sur place claim due to lack of credibility or improper motive but, rather, must assess the genuineness of the applicant’s religious practice to determine if he or she will be at risk if returned to the country of origin (see Jin v Canada (Minister of Citizenship and Immigration), 2012 FC 595, [2012] FCJ No 677 [Jin]; El Aoudie v Canada (Minister of Citizenship and Immigration), 2012 FC 450, [2012] FCJ No 487 [El Aoudie]; Hannoon v Canada (Minister of Citizenship and Immigration), 2012 FC 448, [2012] FCJ No 480 [Hannoon]; Jia v Canada (Minister of Citizenship and Immigration), 2012 FC 444, [2012] FCJ No 463; Huang v Canada (Minister of Citizenship and Immigration), 2012 FC 205 [Huang]; Wang v Canada (Minister of Citizenship and Immigration), 2011 FC 614 [Wang]; Yin v Canada (Minister of Citizenship and Immigration), 2010 FC 544 [Yin]; Chen v Canada (Minister of Citizenship and Immigration), 2009 FC 677, [2009] FCJ No 1391 [Chen]).
- Evidence: `reasoning_application` cue `applied` at chunk `5237214` offsets `80-87`; context: [24] In a series of recent cases involving claimants from China, this Court has applied the holding in Ejtehadian and held that the Board cannot reject a sur place claim due to lack of credibility or improper motive but, rather, must assess the genuineness of the applicant’s religious practice to determine if he or she will be at risk if returned to the country of origin (see Jin v Canada (Minister of Citizenship and Immigration), 2012 FC 595, [2012] FCJ No 677 [Jin]; El Aoudie v Canada (Minister of Citizenship and Immigration), 2012 FC 450, [2012] FCJ No 487 [El Aoudie]; Hannoon v Canada (Minister of Citizenship and Immigration), 2012 FC 448, [2012] FCJ No 480 [Hannoon]; Jia v Canada (Minister of Citizenship and Immigration), 2012 FC 444, [2012] FCJ No 463; Huang v Canada (Minister of Citizenship and Immigration), 2012 FC 205 [Huang]; Wang v Canada (Minister of Citizenship and Immigration), 2011 FC 614 [Wang]; Yin v Canada (Minister of Citizenship and Immigration), 2010 FC 544 [Yin]; Chen v Canada (Minister of Citizenship and Immigration), 2009 FC 677, [2009] FCJ No 1391 [Chen]).

#### 26315:1:subtheme:9 · paragraphs 25-26

- Raw key terms: `above, assertion, canada, issue, noted, para, persecution, refugee`
- Display key terms: `above, assertion, noted, para, persecution, refugee`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, assertion, noted, para, persecution, refugee Rule/authority context: For example, in Slawomir Krzystof Hubicki evidence was adduced that under then-prevailing Polish criminal law, the claimant would face imprisonment of up to eight years because he had made a refugee claim in Canada. Application context: Since refugee law is fundamentally concerned with the provision of protection against unconscionable state action, an assessment should be made of any potential harm to be faced upon return because of the fact of the non Evidence spans paragraphs 25-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5237215` offsets `399-404`; context: Nor does it reflect Professor Hathaway’s views on the issue.
- Evidence: `issue` cue `issue` at chunk `5237216` offsets `1003-1008`; context: This issue is most poignantly raised when it is alleged that the fact of having made an unfounded asylum claim may per se give rise to a serious risk of persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `5237216` offsets `1751-1759`; context: For example, in Slawomir Krzystof Hubicki evidence was adduced that under then-prevailing Polish criminal law, the claimant would face imprisonment of up to eight years because he had made a refugee claim in Canada.
- Evidence: `governing_rule` cue `under` at chunk `5237216` offsets `1777-1782`; context: For example, in Slawomir Krzystof Hubicki evidence was adduced that under then-prevailing Polish criminal law, the claimant would face imprisonment of up to eight years because he had made a refugee claim in Canada.
- Evidence: `reasoning_application` cue `because` at chunk `5237216` offsets `915-922`; context: Since refugee law is fundamentally concerned with the provision of protection against unconscionable state action, an assessment should be made of any potential harm to be faced upon return because of the fact of the non-genuine political activity engaged in while abroad.
- Evidence: `counterargument_limitation` cue `however` at chunk `5237216` offsets `244-251`; context: He writes in this regard:
It does not follow, however, that all persons whose activities abroad are not genuinely demonstrative of oppositional political opinion are outside the refugee definition.

#### 26315:1:subtheme:10 · paragraphs 27-33

- Raw key terms: `applicant, board, determination, fact, light, offered, sincerity, above`
- Display key terms: `determination, fact, light, offered, sincerity, above`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: determination, fact, light, offered, sincerity, above Position/evidence statements: [30] The applicant argues that his case is distinguishable from Jin and Wang (cited above at para 24) because there, unlike here, the claimants’ knowledge of the religion they claimed to adhere to was found to be lacking | While, as noted above, the motive and sincerity findings made by the Board in this case are intertwined, the Board’s determination that the applicant lacked sincerity was additionally premised on the Board’s assessment o Rule/authority context: [28] As noted, the reasonableness standard of review is an exacting one and prevents a court from substituting its opinion for that of the RPD. | While, as noted above, the motive and sincerity findings made by the Board in this case are intertwined, the Board’s determination that the applicant lacked sincerity was additionally premised on the Board’s assessment o Application context: Application of this test to the RPD’s determination that the applicant’s beliefs were insincere leads to the conclusion that the decision must be maintained because the reasons the RPD offered were understandable and the | [30] The applicant argues that his case is distinguishable from Jin and Wang (cited above at para 24) because there, unlike here, the claimants’ knowledge of the religion they claimed to adhere to was found to be lacking Operative outcome context: Accordingly, this application for judicial review will be dismissed. Evidence spans paragraphs 27-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5237217` offsets `226-234`; context: Rather, the question which must be answered by me in this application is whether the RPD reached a reasonable conclusion in determining that the applicant is not a genuine Christian.
- Evidence: `governing_rule` cue `standard of review` at chunk `5237218` offsets `34-52`; context: [28] As noted, the reasonableness standard of review is an exacting one and prevents a court from substituting its opinion for that of the RPD.
- Evidence: `reasoning_application` cue `because` at chunk `5237218` offsets `586-593`; context: Application of this test to the RPD’s determination that the applicant’s beliefs were insincere leads to the conclusion that the decision must be maintained because the reasons the RPD offered were understandable and the result it reached is supportable in light of the facts and applicable law.
- Evidence: `evidence_fact` cue `testimony` at chunk `5237219` offsets `332-341`; context: The Board’s determination that he had not discharged this burden was based on its assessment of the applicant’s credibility: the fact that he had obviously fabricated a story about what occurred in China, had lied during his testimony before the Board and had offered no convincing proof of a conversion experience in Canada.
- Evidence: `party_position` cue `argues` at chunk `5237220` offsets `19-25`; context: [30] The applicant argues that his case is distinguishable from Jin and Wang (cited above at para 24) because there, unlike here, the claimants’ knowledge of the religion they claimed to adhere to was found to be lacking.
- Evidence: `reasoning_application` cue `because` at chunk `5237220` offsets `102-109`; context: [30] The applicant argues that his case is distinguishable from Jin and Wang (cited above at para 24) because there, unlike here, the claimants’ knowledge of the religion they claimed to adhere to was found to be lacking.
- Evidence: `party_position` cue `claim` at chunk `5237221` offsets `528-533`; context: While, as noted above, the motive and sincerity findings made by the Board in this case are intertwined, the Board’s determination that the applicant lacked sincerity was additionally premised on the Board’s assessment of the applicant’s credibility, the fact that he lied under oath and offered no convincing evidence to explain why his practice of Christianity in Canada should be viewed any differently from his fraudulent claim to have practiced Christianity in China.
- Evidence: `evidence_fact` cue `evidence` at chunk `5237221` offsets `412-420`; context: While, as noted above, the motive and sincerity findings made by the Board in this case are intertwined, the Board’s determination that the applicant lacked sincerity was additionally premised on the Board’s assessment of the applicant’s credibility, the fact that he lied under oath and offered no convincing evidence to explain why his practice of Christianity in Canada should be viewed any differently from his fraudulent claim to have practiced Christianity in China.
- Evidence: `governing_rule` cue `under` at chunk `5237221` offsets `375-380`; context: While, as noted above, the motive and sincerity findings made by the Board in this case are intertwined, the Board’s determination that the applicant lacked sincerity was additionally premised on the Board’s assessment of the applicant’s credibility, the fact that he lied under oath and offered no convincing evidence to explain why his practice of Christianity in Canada should be viewed any differently from his fraudulent claim to have practiced Christianity in China.
- Evidence: `party_position` cue `claim` at chunk `5237222` offsets `294-299`; context: [32] Where, as here, a claimant’s assertion to have been the victim of religious persecution abroad is found to be a fabrication, it is completely reasonable for the RPD to require a much higher degree of proof of the sincerity of the applicant’s beliefs and practice in support of a sur place claim than might be required where the mere fact of apostasy might lead to persecution or where the Board believes the claimant to have been the victim of religious persecution abroad.
- Evidence: `counterargument_limitation` cue `however` at chunk `5237222` offsets `714-721`; context: Proof of joining a church and knowledge of its precepts, however, does not equate to proof that the individual would be at risk if returned to his or her country of origin.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `5237223` offsets `103-114`; context: Accordingly, this application for judicial review will be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `5237223` offsets `161-170`; context: Accordingly, this application for judicial review will be dismissed.

#### 26315:1:subtheme:11 · paragraphs 34-34

- Raw key terms: `arises, case, certification, irpa, none, presented, question, section`
- Display key terms: `arises, case, certification, irpa, none, presented, question, section`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: arises, case, certification, irpa, none, presented, question, section Rule/authority context: [34] No question for certification under section 74 of IRPA was presented and none arises in this case. Evidence spans paragraphs 34-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5237224` offsets `8-16`; context: [34] No question for certification under section 74 of IRPA was presented and none arises in this case.
- Evidence: `governing_rule` cue `under` at chunk `5237224` offsets `35-40`; context: [34] No question for certification under section 74 of IRPA was presented and none arises in this case.

#### Section text

Li v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-08-15
Neutral citation
2012 FC 998
File numbers
IMM-8521-11
Decision Content
Federal Court
Cour fédérale
Date: 20120815
Docket: IMM-8521-11
Citation: 2012 FC 998
Ottawa, Ontario, August 15, 2012
PRESENT: The Honourable Madam Justice Gleason
BETWEEN:
SHI JIE LI
(aka SHIJIE LI)
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application for judicial review of the decision of the Refugee Protection Division of the Immigration and Refugee Board [RPD or the Board], dated October 27, 2011, in which the Board dismissed the applicant’s claims under section 96 and subsection 97(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA or the Act].

[2] The applicant is a citizen of the People’s Republic of China from Shijiazhuang, Hebei province and claims that he was a member of an underground Christian house church that was raided by the Public Security Bureau [PSB] in 2010. He alleges that he went into hiding following the raid and that while in hiding learned both that members of the PSB had gone to his home looking for him and that other members of his congregation had been arrested. The applicant fled China on July 18, 2010, with the help of a smuggler, and sought protection in Canada. He asserts that he has since learned that the PSB has returned to his home multiple times and filed a letter with the RPD from his mother that purports to confirm these visits.

[3] Once in Canada, the applicant joined a Pentecostal church (the Living Stone Assembly in Scarborough, Ontario) and claims to be a practicing Christian. The applicant filed with the RPD a copy of a letter from the pastor of his church, attesting to the applicant’s regular church attendance, a baptismal certificate and several photographs of the applicant participating in church-related activities. He claims that by virtue of his beliefs, he would be subject to risk if returned to China.
The RPD’s Decision

[4] The Board determined that there was no credible basis for the applicant’s claim and, as a result, that he was neither a Convention refugee nor a person in need of protection. The credibility finding centred on the fact that the applicant had made a failed attempt to obtain a student visa in 2009, well before the applicant’s alleged conversion to Christianity and the alleged raid on his house church. In his testimony before the Board, the applicant denied any knowledge of the student visa application, despite the fact that the visa file contained a picture of him, his passport number and date of birth. The student visa file also contained fraudulent documentation regarding the applicant’s parents’ occupations and assets as well as details regarding the applicant’s background that were completely at odds with those he provided in connection with his refugee claim.

[5] The Board discovered the fraudulent student visa application somewhat fortuitously: during the hearing, the member noted a cryptic reference in the file to a previous denial of a student visa and asked the applicant about it. The applicant claimed to have no knowledge of any such application. During an adjournment of the hearing, the Board member called the Canada Border Services Agency. The Agency provided copies of the Field Operations Support System, commonly referred to as “FOSS”, notes to the member that confirmed the existence of the applicant’s earlier student visa application. When the hearing resumed, the applicant continued to deny any knowledge of the application. The RPD then adjourned the hearing for several weeks to obtain copies of all the documents associated with the 2009 application and to allow the applicant time to review them. Upon resumption of the hearing, the applicant confirmed that the 2009 fraudulent student visa application contained his photograph, the same passport number and expiry date as on his passport and also set out his correct date of birth. However, he continued to deny that he had any knowledge of the application. The Board did not believe him.

[6] During the hearing, the Board member questioned the applicant about his knowledge of Christianity, and the applicant was able to provide answers to many of the questions about the basic tenets of the Christian faith. However, he could not remember the date of Easter in 2010. In the decision, the RPD found this omission to be significant, as Easter that year had fallen the week before the alleged raid. The Board reasoned in this regard that if the applicant had really been a consistent church-goer in China, as he claimed, he ought to have been able to recall that Easter Sunday was just a week before his church had been raided.

[7] In light of these facts, the Board determined that the applicant was not a practicing Christian in China, that the alleged raid on his house church did not occur and that none of his fellow alleged church members had been arrested or incarcerated. In so finding, the Board accorded little weight to a “Jail Visiting Card” or letter from the claimant’s mother, purporting to confirm that the PSB had been at her home looking for the applicant. The Board determined that the first document was not genuine and gave little weight to the letter from the applicant’s mother because his parents had been complicit in his earlier fraudulent student visa application.

[8] After determining that the applicant had not been a practicing Christian in China, the Board went on to assess the applicant’s sur place claim, or his claim to have acquired refugee status through his adherence to Christianity in Canada. In assessing this claim, the Board first purported to cite from James Hathaway’s The Law of Refugee Status (Toronto: Butterworths, 1991), claiming that Hathaway wrote that “an individual who as a stratagem deliberately manipulates circumstances to create a real chance persecution, which did not exist, cannot be said to belong to this category [i.e. of those who can legitimately advance a sur place refugee claim]” (decision at para 40. As is discussed below, however, this citation is not from The Law of Refugee Status. However, as is also discussed below, this does not impact the reasonableness of the Board’s decision.

[9] The Board determined that, in light of its credibility findings, the claimant had joined a Christian church in Canada only for the purpose of supporting a fraudulent refugee claim. It afforded little or no weight to the pastor’s letter, certificate of baptism and church photos filed by the applicant. The Board then determined that the applicant was not a genuine Christian, stating as follows at paragraph 41 of the decision:
The panel finds, on a balance of probabilities, and in the context of findings noted above, that the claimant joined a Christian church in Canada only for the purpose of supporting a fraudulent refugee claim. In the context as noted above, and on the basis of the totality of the evidence disclosed the panel finds that the claimant is not a genuine practicing Christian and never was, nor would he be perceived to be in China. I do not believe that, if he returned to China, he would engage in any Christian practice.

[10] The RPD therefore dismissed the applicant’s claim, finding the applicant had not satisfied the burden of establishing a serious possibility that he would be persecuted or subjected to risk to his life, risk of cruel and unusual treatment or punishment or danger of torture if returned to China.
Issues

[11] The applicant argues that the RPD’s decision should be set aside because its credibility findings were unreasonable. He contends in this regard that the application for a study permit outside of Canada is insufficient to impugn his credibility and that the Board’s reliance on his inability to remember the date of Easter is unreasonable. In support of the latter point, the applicant claims that this finding constitutes an improper reliance on “religious trivia”, which should result in the decision’s being set aside as was done in Wang v Canada (Minister of Citizenship and Immigration),2011 FC 1030 at para 13, 206 ACWS (3d) 800; Dong v Canada (Minister of Citizenship and Immigration), 2010 FC 55 at para 20, [2010] FCJ No 54 and Wu v Canada (Minister of Citizenship and Immigration), 2009 FC 929 at para 22, [2009] FCJ No 1143. The applicant also argues that the Board failed to properly consider evidence of the genuineness of his religious beliefs and practices and that it was improper for the Board to have considered his motive in joining and participating in the activities of the Living Stone Assembly because the presence or absence of a good faith motive for engaging in activities that may give rise to a sur place claim is irrelevant to the assessment of the validity of such a claim under Canadian law.

[12] The respondent, on the other hand, submits that it was reasonable for the Board to draw a negative inference from the applicant’s student visa application and from the applicant’s inability to remember the date of Easter. On this point, counsel asserts that the RPD’s determination turns not on the inability of the applicant to remember the date of Easter as being indicative of his lack of knowledge of Christianity, but rather on his inability to situate the alleged raid with reference to Easter Sunday, which he ought to have been able to remember if he were a regular church-goer, as he claimed. Based on these facts, the respondent asserts that is was reasonable for the Board to find that the applicant had not been attending a house church in China. The respondent also argues that the Board did not place an improper reliance on the applicant’s motives and that the Board’s finding that the applicant had not demonstrated that he was a genuine Christian in Canada is reasonable in light of the applicant’s lack of credibility and the lack of other evidence about sincerity of his beliefs. The respondent notes in this regard that it was not unreasonable for the Board to accord little weight to the pastor’s letter, photographs and baptismal certificate filed by the applicant.

[13] In light of the foregoing, four issues arise in this matter:
1. What standard of review is applicable to the errors the applicant alleges were made by the RPD;
2. Were the Board’s credibility findings reasonable;
3. Did the Board err in considering the applicant’s motive for joining the Living Stone Assembly church; and
4. Was the Board’s assessment of the lack of sincerity of the applicant’s adherence to Christianity reasonable?
What standard of review is applicable to the errors the applicant alleges the RPD made?

[14] The reasonableness standard is applicable to each of the alleged errors. It is well-established that credibility findings, as matters of fact, are reviewable on the reasonableness standard (Aguebor v Canada (Minister of Employment and Immigration) (1993), 160 NR 315, [1993] FCJ No 732 (CA) at para 4; Singh v Canada (Minister of Employment and Immigration) (1994), 169 NR 107, [1994] FCJ No 486 (CA) at para 3; and Cetinkaya v Canada (Minister of Citizenship and Immigration), 2012 FC 8 at para 17, [2012] FCJ No 13). The question concerning the consideration of the applicant’s motives for practicing Christianity in Canada and concerning the reasonableness of the RPD’s decision are intertwined: the lack of good faith motive was an important consideration of the RPD in determining that the applicant’s beliefs were not sincere. The Board’s determinations on these issues involve matters of mixed fact and law and are reviewable on the reasonableness standard (Dunsmuir v New Brunswick, 2008 SCC 9 at para 51, [2008] 1 SCR 190 [Dunsmuir], see also Xin Cai Hou (a.k.a. Xincai Hou) v. The Minister of Citizenship and Immigration), 2012 FC 933).

[15] The reasonableness standard is an exacting one and requires the reviewing court afford deference to a tribunal’s decision; a court cannot intervene unless it is satisfied that the reasons of a tribunal are not justified, transparent or intelligible and that the result does not fall “within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at para 47). In applying this deferential standard, it matters not whether the reviewing court agrees with a tribunal’s conclusion, would have reached a different result or might have reasoned differently. So long as the reasons are understandable and the result is one that is rational and supportable in light of the facts and the applicable law, a court should not overturn an inferior tribunal’s decision under the reasonableness standard of review.
Were the Board’s credibility findings reasonable?

[16] As noted, the applicant alleges that it was unreasonable for the Board to have determined that the applicant made a fraudulent student visa application in 2009 and that the Board’s reliance on the applicant’s inability to remember the date of Easter in 2010 was unreasonable. In my view, neither of these submissions has merit.

[17] Insofar as concerns the fraudulent student visa application, the visa file contained the applicant’s picture, passport number and date the passport was issued. The applicant was unable to offer any explanation as to how these details and his picture came to be in the student visa file. In the absence of any such explanation, the Board drew the obvious conclusion, namely, that the applicant was complicit in making the application, which is accordingly a reasonable finding. Moreover, the fact that the applicant had made an earlier fraudulent attempt to enter Canada taints his refugee claim as it shows that he was willing to employ dishonesty in an effort to gain admittance to the country. Once again, the obvious inference to be drawn from this fact is that a similar motive is behind his refugee claim. It was accordingly reasonable for the Board to rely on this factor as a significant reason for disbelieving the applicant’s claims regarding what occurred in China and for finding the applicant to not be a sincere Christian.

[18] Insofar as concerns the reliance on the applicant’s inability to remember the date of Easter in 2010, the submission of the respondent is convincing. The Board did not find the inability to remember to be indicative of a lack of knowledge of the tenets of Christianity but, rather, found that it undercut the applicant’s claim that his church was raided. As the RPD noted in its decision, Easter is one of the key celebrations of the Christian religion, and it is not believable that a new adherent to the religion would not remember the proximity of Easter to an event as significant as the raid of his church, if he had in fact attended that church on a weekly basis as he claimed. Moreover, when questioned about these issues, the applicant obfuscated and backtracked regarding how frequently his pastor attended church. It was accordingly reasonable for the RPD to determine the applicant’s inability to remember Easter to be a factor in support of a negative inference regarding his credibility.

[19] Thus, neither of the reasons asserted by the applicant for setting aside the RPD’s credibility determinations bears weight.
Did the Board err in considering the applicant’s motive for joining the Living Stone Assembly
church?

[20] Contrary to what the applicant asserts, the case law recognises that motive for engaging in a religious practice in Canada may be considered by the RPD in an appropriate case. However, a finding that a claimant was motivated to practice a religion in Canada to buttress a fraudulent refugee claim cannot be used, in and of itself, as a basis to reject the claim. Rather, the finding that the claimant has been motivated by a desire to buttress his or her refugee claim is one factor that may be considered by the RPD in assessing the sincerity of a claimant’s religious beliefs.

[21] The sincerity of those beliefs will be an issue in cases, like the present, where continuing the religious practice in the country of origin might place the claimant at risk. If the beliefs are not genuine, then there is no risk, as a claimant would not likely practice his or her newly-acquired religion in the country of origin if adherence to the religion is motivated solely by a desire to support a refugee claim. On the other hand, there may well be situations where a claimant might initially have been motivated to join a religion due to these types of motivations, but along the route, may have developed faith and become a true adherent of the religion. This appears to be what occurred in Ejtehadian v Canada (Minister of Citizenship and Immigration), 2007 FC 158 [Ejtehadian], where the claimant was found to have originally began practicing Christianity to fuel his refugee claim, but later went on to become a priest in the Mormon church.

[22] The starting point for the discussion of the notion of a sur place claim in Canadian law is the decision of the Federal Court of Appeal in Ghazizadeh v Canada (Minister of Employment and Immigration), [1993] FCJ No 465, 154 NR 236, where the Court held that the “… concept of a refugee ‘sur place’ requires an assessment of the situation in the applicant’s country of origin after he or she has left it”. The Court accordingly set aside the decision of the Board, which had focused on the fact that the applicant had obtained an exit visa from Iran, as opposed to the risk that subsequent events in the country had created for him if he returned.

[23] This Court has assessed the requirements of religion-based sur place claims in a series of recent cases. The first of these, Ejtehadian, arose in the context of a claimant who became a Christian after he left Iran. The Board dismissed his claim because it determined that his conversion was not genuine, finding that he had become a Christian in order to obtain a means of remaining in Canada and claiming refugee status. Importantly, in that case, unlike the present, there was evidence before the Board that apostates were persecuted and executed in Iran and thus that the mere fact of apostasy (as opposed to ongoing practice of religion) might have founded the basis for persecution. In addition, it appears that the claimant underwent a conversion experience and became a sincere practitioner because, as noted, he went on to join the priesthood in the Mormon faith. Justice Blanchard overturned the RPD’s decision, noting that the Board had misarticulated the test in a sur place claim and held that on the facts of that case “[i]n assessing the Applicant’s risks of return, in the context of a sur-place claim, it is necessary to consider the credible evidence of [the applicant’s] activities while in Canada, independently from his motives for conversion”.

[24] In a series of recent cases involving claimants from China, this Court has applied the holding in Ejtehadian and held that the Board cannot reject a sur place claim due to lack of credibility or improper motive but, rather, must assess the genuineness of the applicant’s religious practice to determine if he or she will be at risk if returned to the country of origin (see Jin v Canada (Minister of Citizenship and Immigration), 2012 FC 595, [2012] FCJ No 677 [Jin]; El Aoudie v Canada (Minister of Citizenship and Immigration), 2012 FC 450, [2012] FCJ No 487 [El Aoudie]; Hannoon v Canada (Minister of Citizenship and Immigration), 2012 FC 448, [2012] FCJ No 480 [Hannoon]; Jia v Canada (Minister of Citizenship and Immigration), 2012 FC 444, [2012] FCJ No 463; Huang v Canada (Minister of Citizenship and Immigration), 2012 FC 205 [Huang]; Wang v Canada (Minister of Citizenship and Immigration), 2011 FC 614 [Wang]; Yin v Canada (Minister of Citizenship and Immigration), 2010 FC 544 [Yin]; Chen v Canada (Minister of Citizenship and Immigration), 2009 FC 677, [2009] FCJ No 1391 [Chen]). In many of those

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 26315:2 · paragraphs 35-36

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6c80cd09262f50b5d018745ab96fe7745da201cacb39ef38b963d5087532c5c5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26315:2:subtheme:1 · paragraphs 35-36

- Raw key terms: `application, cause, certified, citizenship, costs, court, date, dismissed`
- Display key terms: `certified, costs, date, dismissed`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: certified, costs, date, dismissed Operative outcome context: This application for judicial review is dismissed; 2. Evidence spans paragraphs 35-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5237224` offsets `204-212`; context: No question of general importance is certified; and
3.
- Evidence: `disposition` cue `dismissed` at chunk `5237224` offsets `187-196`; context: This application for judicial review is dismissed;
2.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that:
1. This application for judicial review is dismissed;
2. No question of general importance is certified; and
3. There is no order as to costs.
"Mary J.L. Gleason"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-8521-11
STYLE OF CAUSE: Shi Jie Li (aka Shijie Li) v The Minister of Citizenship and Immigration
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: June 12, 2012
REASONS FOR 

## 26315:3 · paragraphs 37-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c7ffecebd0233c0e9557c3b418326d664f66d8902bcbd1e7b1d437d35a350665`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26315:3:subtheme:1 · paragraphs 37-37

- Raw key terms: `appearances, applicant, attorney, august, barrister, canada, dated, deputy`
- Display key terms: `august, barrister, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, barrister, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 37-37. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT
AND JUDGMENT: GLEASON J.
DATED: August 15, 2012
APPEARANCES:
Marvin Moses
FOR THE APPLICANT
Nadine Silverman
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Marvin Moses Law Office,
Barrister & Solicitor
Toronto, Ontario
FOR THE APPLICANT
Myles J. Kirvan,
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
