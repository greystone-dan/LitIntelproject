# Discussion Units: case 11809

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **49**
- Continuity pairs: **48**
- Discussion Units: **2**
- Paragraph source hashes: **49**
- Sub-themes: **10**

## 11809:1 · paragraphs 0-46

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c5784575f7e1c6db80b35528a59a0e68b34cf610d651b92a4bb92f2f166b4151`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11809:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicant, alleges, decision, husband, january, refugee, appeal, arrested`
- Display key terms: `alleges, husband, january, refugee, arrested`
- Argument roles: `disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, reasoning_application Display terms: alleges, husband, january, refugee, arrested Rule/authority context: [1] In this application for judicial review brought under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], Denbel Bekelech challenges a decision rendered by the Refugee Appeal Divisio Application context: [3] The applicant alleges that she was arrested on July 11, 2012 and held for one month because the authorities wanted to draw her husband out of hiding. | Thereafter, she applied for refugee protection due to her political opinion. Operative outcome context: [1] In this application for judicial review brought under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], Denbel Bekelech challenges a decision rendered by the Refugee Appeal Divisio | The RAD dismissed the applicant’s appeal by decision dated April 10, 2014. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4593495` offsets `52-57`; context: [1] In this application for judicial review brought under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], Denbel Bekelech challenges a decision rendered by the Refugee Appeal Division [RAD], which dismissed her appeal from a decision of the Refugee Protection Division [RPD] rejecting her claim for refugee protection.
- Evidence: `disposition` cue `dismissed` at chunk `4593495` offsets `235-244`; context: [1] In this application for judicial review brought under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], Denbel Bekelech challenges a decision rendered by the Refugee Appeal Division [RAD], which dismissed her appeal from a decision of the Refugee Protection Division [RPD] rejecting her claim for refugee protection.
- Evidence: `reasoning_application` cue `because` at chunk `4593496` offsets `88-95`; context: [3] The applicant alleges that she was arrested on July 11, 2012 and held for one month because the authorities wanted to draw her husband out of hiding.
- Evidence: `reasoning_application` cue `applied` at chunk `4593498` offsets `100-107`; context: Thereafter, she applied for refugee protection due to her political opinion.
- Evidence: `evidence_fact` cue `record` at chunk `4593499` offsets `186-192`; context: She submitted an appeal record on January 6, 2014.
- Evidence: `disposition` cue `dismissed` at chunk `4593499` offsets `304-313`; context: The RAD dismissed the applicant’s appeal by decision dated April 10, 2014.

#### 11809:1:subtheme:2 · paragraphs 6-13

- Raw key terms: `applicant, hearing, credibility, panel, arrested, because, evidence, explain`
- Display key terms: `hearing, credibility, arrested, because, explain`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: hearing, credibility, arrested, because, explain Rule/authority context: [7] While the decision under review, properly speaking, is the RAD decision, it makes sense to begin with an overview of the RPD decision. Application context: The panel considered this contradiction highly material because her second arrest was the event which allegedly motivated her to seek refuge in another country. | In her BOC, she stated that the police arrested her in January 2013 because they believed that she had been distributing political flyers for the UDJ party. Evidence spans paragraphs 6-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4593500` offsets `185-190`; context: The RPD panel declared that the determinative issue was credibility.
- Evidence: `governing_rule` cue `under` at chunk `4593500` offsets `23-28`; context: [7] While the decision under review, properly speaking, is the RAD decision, it makes sense to begin with an overview of the RPD decision.
- Evidence: `reasoning_application` cue `because` at chunk `4593501` offsets `565-572`; context: The panel considered this contradiction highly material because her second arrest was the event which allegedly motivated her to seek refuge in another country.
- Evidence: `reasoning_application` cue `because` at chunk `4593502` offsets `154-161`; context: In her BOC, she stated that the police arrested her in January 2013 because they believed that she had been distributing political flyers for the UDJ party.
- Evidence: `evidence_fact` cue `testimony` at chunk `4593503` offsets `49-58`; context: [10] Third, the applicant did not offer credible testimony on being followed by government officials.
- Evidence: `evidence_fact` cue `testimony` at chunk `4593504` offsets `161-170`; context: [11] Finally, the panel noted that there were inconsistencies between the applicant’s knowledge of her husband’s activities as expressed in her BOC and her oral testimony.
- Evidence: `counterargument_limitation` cue `However` at chunk `4593504` offsets `303-310`; context: However, her oral testimony was vague and ambiguous.
- Evidence: `evidence_fact` cue `determined that` at chunk `4593505` offsets `79-94`; context: It determined that there was no serious possibility that the applicant would be persecuted.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593506` offsets `82-90`; context: [13] In her appeal to the RAD, the applicant provided the following pieces of new evidence:
1.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593507` offsets `60-68`; context: [14] The RAD member considers the admissibility of this new evidence.

#### 11809:1:subtheme:3 · paragraphs 14-19

- Raw key terms: `evidence, applicant, letter, raza, affidavit, analysis, appeal, claim`
- Display key terms: `letter, raza, affidavit, analysis`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: letter, raza, affidavit, analysis Position/evidence statements: The author inquires into the applicant’s health; states that her husband is alive and probably joined the OLF; and affirms that he plans to travel to South Africa himself to claim refugee protection. Rule/authority context: [17] The RAD then turns to the evidence which the applicant tendered by way of motion brought under Rule 29 of the Refugee Appeal Division Rules, SOR/2012-257 [the Rules]: a letter from her son, Wondemu Yohannes, and Can | The letter is inadmissible under Rule 29 and so a full Raza analysis is not necessary. Application context: The second piece of information fails the Raza test because it lacks probative value. | He concludes that the standard of reasonableness governs the appeal. Evidence spans paragraphs 14-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4593508` offsets `591-596`; context: There was no indication in the RPD record that the applicant raised the issue or required accommodation for her hearing loss.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4593508` offsets `21-30`; context: [15] The applicant’s affidavit proffers evidence that was not before the RPD.
- Evidence: `reasoning_application` cue `because` at chunk `4593508` offsets `697-704`; context: The second piece of information fails the Raza test because it lacks probative value.
- Evidence: `counterargument_limitation` cue `fails` at chunk `4593508` offsets `677-682`; context: The second piece of information fails the Raza test because it lacks probative value.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593509` offsets `72-80`; context: [16] The RAD employs the Raza test to exclude the three other pieces of evidence as well.
- Evidence: `counterargument_limitation` cue `but` at chunk `4593509` offsets `152-155`; context: The letter from the friend was written after the RPD decision but it did not meet the relevance test as it was vague and lacked probative value.
- Evidence: `party_position` cue `claim` at chunk `4593510` offsets `515-520`; context: The author inquires into the applicant’s health; states that her husband is alive and probably joined the OLF; and affirms that he plans to travel to South Africa himself to claim refugee protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593510` offsets `31-39`; context: [17] The RAD then turns to the evidence which the applicant tendered by way of motion brought under Rule 29 of the Refugee Appeal Division Rules, SOR/2012-257 [the Rules]: a letter from her son, Wondemu Yohannes, and Canada Post tracking results for that letter.
- Evidence: `governing_rule` cue `under` at chunk `4593510` offsets `94-99`; context: [17] The RAD then turns to the evidence which the applicant tendered by way of motion brought under Rule 29 of the Refugee Appeal Division Rules, SOR/2012-257 [the Rules]: a letter from her son, Wondemu Yohannes, and Canada Post tracking results for that letter.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593511` offsets `63-71`; context: [18] According to the RAD, the letter does not provide any new evidence which would justify altering the RPD decision.
- Evidence: `governing_rule` cue `under` at chunk `4593511` offsets `280-285`; context: The letter is inadmissible under Rule 29 and so a full Raza analysis is not necessary.
- Evidence: `governing_rule` cue `standard of review` at chunk `4593512` offsets `44-62`; context: [19] The RAD member then conducts a lengthy standard of review analysis.
- Evidence: `reasoning_application` cue `concludes` at chunk `4593512` offsets `76-85`; context: He concludes that the standard of reasonableness governs the appeal.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593513` offsets `81-89`; context: [20] The applicant alleged that the RPD erred in failing to consider documentary evidence in support of her claim, including a letter from Ali Keder, an affidavit from Konjit Mitiku and objective country conditions evidence.

#### 11809:1:subtheme:4 · paragraphs 20-23

- Raw key terms: `applicant, evidence, analysis, central, conduct, credibility, decision, error`
- Display key terms: `analysis, central, conduct, credibility, error`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: analysis, central, conduct, credibility, error Rule/authority context: [24] The RAD disagrees with the applicant that the RPD erred by failing to conduct an objective risk assessment under section 97. Evidence spans paragraphs 20-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4593514` offsets `226-231`; context: A reviewable error occurs only where the RPD omits to mention important evidence that is directly relevant to a central issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593514` offsets `86-94`; context: [21] The RAD recalls that the RPD is not required to refer to each and every piece of evidence before it.
- Evidence: `issue` cue `issue` at chunk `4593515` offsets `296-301`; context: The letter did not speak to an issue central to the decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593515` offsets `25-33`; context: [22] The RAD reviews the evidence mentioned by the applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593516` offsets `51-59`; context: [23] The RAD accepts that some important pieces of evidence were not mentioned in the RPD decision, specifically the affidavit where Konjit Mitiku swears to have visited the applicant while she was in prison, the receipt of the donation to the UDJ and the country conditions evidence.
- Evidence: `governing_rule` cue `under` at chunk `4593517` offsets `112-117`; context: [24] The RAD disagrees with the applicant that the RPD erred by failing to conduct an objective risk assessment under section 97.

#### 11809:1:subtheme:5 · paragraphs 24-25

- Raw key terms: `court, huruglica, question, review, selection, standard, turns, against`
- Display key terms: `huruglica, question, review, selection, standard, turns, against`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: huruglica, question, review, selection, standard, turns, against Rule/authority context: Did the RAD err in its standard of review analysis? | In any event, nothing turns on the Court-to-RAD standard of review here, since the RAD’s selection of a deferential standard of review was both correct and reasonable, as I explain below. Application context: In light of the numerous concerns identified by the RPD and the deference which credibility findings deserve, the RAD concludes that these findings pass muster on the standard of reasonableness. Evidence spans paragraphs 24-25. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4593518` offsets `26-31`; context: [25] The RAD turns to the issue of credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593518` offsets `449-457`; context: Did the RAD err in its analysis of the new evidence?
- Evidence: `governing_rule` cue `standard of review` at chunk `4593518` offsets `374-392`; context: Did the RAD err in its standard of review analysis?
- Evidence: `reasoning_application` cue `concludes` at chunk `4593518` offsets `166-175`; context: In light of the numerous concerns identified by the RPD and the deference which credibility findings deserve, the RAD concludes that these findings pass muster on the standard of reasonableness.
- Evidence: `issue` cue `question` at chunk `4593519` offsets `197-205`; context: As an appeal has been brought against Huruglica, the Court of Appeal will soon have an opportunity to answer this question.
- Evidence: `governing_rule` cue `standard of review` at chunk `4593519` offsets `255-273`; context: In any event, nothing turns on the Court-to-RAD standard of review here, since the RAD’s selection of a deferential standard of review was both correct and reasonable, as I explain below.

#### 11809:1:subtheme:6 · paragraphs 26-27

- Raw key terms: `facts, reasonableness, review, standard, statute, analysis, application, appropriate`
- Display key terms: `facts, reasonableness, review, standard, statute, analysis, appropriate`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: facts, reasonableness, review, standard, statute, analysis, appropriate Rule/authority context: [29] The standard of review for the second issue is reasonableness, as it involves the RAD’s application of its home statute and regulations to the facts before it: Dunsmuir v New Brunswick, 2008 SCC 9 at paras 53-54. | Since this required the RAD to evaluate the facts before it in light of its enabling statute, the Court-to-RAD standard of review is reasonableness again. Evidence spans paragraphs 26-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4593520` offsets `43-48`; context: [29] The standard of review for the second issue is reasonableness, as it involves the RAD’s application of its home statute and regulations to the facts before it: Dunsmuir v New Brunswick, 2008 SCC 9 at paras 53-54.
- Evidence: `governing_rule` cue `standard of review` at chunk `4593520` offsets `9-27`; context: [29] The standard of review for the second issue is reasonableness, as it involves the RAD’s application of its home statute and regulations to the facts before it: Dunsmuir v New Brunswick, 2008 SCC 9 at paras 53-54.
- Evidence: `governing_rule` cue `standard of review` at chunk `4593521` offsets `234-252`; context: Since this required the RAD to evaluate the facts before it in light of its enabling statute, the Court-to-RAD standard of review is reasonableness again.

#### 11809:1:subtheme:7 · paragraphs 28-29

- Raw key terms: `court, deference, findings, accept, alyafi, analogous, analysis, appeal`
- Display key terms: `deference, findings, accept, alyafi, analogous, analysis`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: deference, findings, accept, alyafi, analogous, analysis Rule/authority context: Yet both strands in the jurisprudence accept the principle that findings of credibility must be shown deference, since the RAD does not typically hold oral hearings and is therefore at a disadvantage in comparison to the Application context: Yet both strands in the jurisprudence accept the principle that findings of credibility must be shown deference, since the RAD does not typically hold oral hearings and is therefore at a disadvantage in comparison to the Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4593522` offsets `83-89`; context: [32] The Court has sent back decisions where the RAD showed deference on different issues.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4593523` offsets `230-243`; context: Yet both strands in the jurisprudence accept the principle that findings of credibility must be shown deference, since the RAD does not typically hold oral hearings and is therefore at a disadvantage in comparison to the RPD.
- Evidence: `reasoning_application` cue `therefore` at chunk `4593523` offsets `378-387`; context: Yet both strands in the jurisprudence accept the principle that findings of credibility must be shown deference, since the RAD does not typically hold oral hearings and is therefore at a disadvantage in comparison to the RPD.

#### 11809:1:subtheme:8 · paragraphs 30-33

- Raw key terms: `credibility, error, justice, overriding, palpable, review, standard, agree`
- Display key terms: `credibility, error, justice, overriding, palpable, review, standard, agree`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: credibility, error, justice, overriding, palpable, review, standard, agree Rule/authority context: Furthermore, he stated that the standard of review for credibility is not “palpable and overriding error” (paras 54-55). | When credibility findings are at issue, he asserted that the RAD ought to apply the standard of review of “palpable and overriding error”. Application context: When credibility findings are at issue, he asserted that the RAD ought to apply the standard of review of “palpable and overriding error”. | [36] This debate is largely academic because neither side would agree with the applicant that the standard of correctness applies. Evidence spans paragraphs 30-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4593524` offsets `169-174`; context: Yet he recognized the need for deference when credibility is at issue (para 37).
- Evidence: `governing_rule` cue `standard of review` at chunk `4593524` offsets `218-236`; context: Furthermore, he stated that the standard of review for credibility is not “palpable and overriding error” (paras 54-55).
- Evidence: `issue` cue `issue` at chunk `4593525` offsets `296-301`; context: When credibility findings are at issue, he asserted that the RAD ought to apply the standard of review of “palpable and overriding error”.
- Evidence: `governing_rule` cue `standard of review` at chunk `4593525` offsets `347-365`; context: When credibility findings are at issue, he asserted that the RAD ought to apply the standard of review of “palpable and overriding error”.
- Evidence: `reasoning_application` cue `apply` at chunk `4593525` offsets `337-342`; context: When credibility findings are at issue, he asserted that the RAD ought to apply the standard of review of “palpable and overriding error”.
- Evidence: `reasoning_application` cue `because` at chunk `4593526` offsets `37-44`; context: [36] This debate is largely academic because neither side would agree with the applicant that the standard of correctness applies.
- Evidence: `counterargument_limitation` cue `However` at chunk `4593527` offsets `525-532`; context: However, and with the greatest respect, I do not agree that the RAD should routinely conduct a fresh assessment of credibility on appeals brought before it.

#### 11809:1:subtheme:9 · paragraphs 34-46

- Raw key terms: `credibility, evidence, analysis, applicant, canada, para, reasonable, view`
- Display key terms: `credibility, analysis, para, reasonable, view`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: credibility, analysis, para, reasonable, view Position/evidence statements: Although counsel for the applicant forcefully argued at the hearing that the RAD should have given some weight to the affidavit of Konjit Mikitu, who allegedly visited the applicant while she was in prison, the failure d Rule/authority context: In my view, Parliament intended these two provisions to enshrine the same legal test. | The applicant focused on the RAD’s exclusion of her son’s letter under Rule 29(4). Application context: [38] It is difficult to understand how an administrative tribunal could apply the standard of correctness to findings of credibility on a paper-based appeal. | Yet the RAD ultimately upheld the RPD’s conclusions because its credibility findings were reasonable in light of the record. Operative outcome context: Yet the RAD ultimately upheld the RPD’s conclusions because its credibility findings were reasonable in light of the record. | He dismissed the judicial review application for the following reasons, expressed at para 45: Although the Applicants have demonstrated an error in the assessment of state protection, it is of no consequence because they Evidence spans paragraphs 34-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4593528` offsets `381-386`; context: If the RAD owed no deference to the RPD’s findings on the issue which the RPD is best placed to decide, the statutory scheme would involve unnecessary duplication.
- Evidence: `reasoning_application` cue `apply` at chunk `4593528` offsets `72-77`; context: [38] It is difficult to understand how an administrative tribunal could apply the standard of correctness to findings of credibility on a paper-based appeal.
- Evidence: `issue` cue `question` at chunk `4593529` offsets `646-654`; context: In Iyamuremye v Canada (Citizenship and Immigration), 2014 FC 494 at para 45, Justice Shore held that:
Considering the dearth of case law interpreting subsection 110(4) and given the essential similarity between the provisions in question, the Court does not find it unreasonable for the RAD to have referred to the factors set out in Raza, above, to analyse the admissibility of fresh evidence.
- Evidence: `evidence_fact` cue `testimony` at chunk `4593529` offsets `216-225`; context: [39] I am satisfied, in any event, that the RAD made its own assessment of the applicant’s credibility relying on the very thorough discussion by the RPD of the inconsistencies which it had found between her BOC and testimony.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593530` offsets `83-91`; context: [41] Moreover, the RAD relied on the express language of Rule 29(4) to exclude new evidence tendered after the appeal record was filed.
- Evidence: `governing_rule` cue `legal test` at chunk `4593532` offsets `322-332`; context: In my view, Parliament intended these two provisions to enshrine the same legal test.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593533` offsets `67-75`; context: [44] I am satisfied that the RAD reasonably excluded the contested evidence for the reasons it provided.
- Evidence: `governing_rule` cue `under` at chunk `4593533` offsets `170-175`; context: The applicant focused on the RAD’s exclusion of her son’s letter under Rule 29(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4593534` offsets `131-139`; context: [46] The RAD lent some support to the applicant’s argument, declaring that the RPD behaved unreasonably by failing to mention that evidence.
- Evidence: `reasoning_application` cue `because` at chunk `4593534` offsets `193-200`; context: Yet the RAD ultimately upheld the RPD’s conclusions because its credibility findings were reasonable in light of the record.
- Evidence: `disposition` cue `upheld` at chunk `4593534` offsets `164-170`; context: Yet the RAD ultimately upheld the RPD’s conclusions because its credibility findings were reasonable in light of the record.
- Evidence: `evidence_fact` cue `found that` at chunk `4593535` offsets `88-98`; context: [47] In Kanto v Canada (Citizenship and Immigration), 2012 FC 1049, Justice de Montigny found that the RPD had erred in its state protection analysis but had still reasonably concluded that the applicants lacked credibility.
- Evidence: `reasoning_application` cue `because` at chunk `4593535` offsets `433-440`; context: He dismissed the judicial review application for the following reasons, expressed at para 45:
Although the Applicants have demonstrated an error in the assessment of state protection, it is of no consequence because they have failed to establish that they are in need of that protection.
- Evidence: `counterargument_limitation` cue `but` at chunk `4593535` offsets `150-153`; context: [47] In Kanto v Canada (Citizenship and Immigration), 2012 FC 1049, Justice de Montigny found that the RPD had erred in its state protection analysis but had still reasonably concluded that the applicants lacked credibility.
- Evidence: `disposition` cue `dismissed` at chunk `4593535` offsets `228-237`; context: He dismissed the judicial review application for the following reasons, expressed at para 45:
Although the Applicants have demonstrated an error in the assessment of state protection, it is of no consequence because they have failed to establish that they are in need of that protection.
- Evidence: `party_position` cue `argued` at chunk `4593536` offsets `381-387`; context: Although counsel for the applicant forcefully argued at the hearing that the RAD should have given some weight to the affidavit of Konjit Mikitu, who allegedly visited the applicant while she was in prison, the failure do so does not establish a reviewable error in my view.
- Evidence: `evidence_fact` cue `determined that` at chunk `4593536` offsets `74-89`; context: The RAD implicitly and reasonably determined that the RPD’s error was immaterial due to the applicant’s lack of credibility.
- Evidence: `reasoning_application` cue `conclude` at chunk `4593536` offsets `198-206`; context: It was reasonable for the RAD to conclude that the unmentioned evidence could not remedy the significant contradictions and inconsistencies in the applicant’s testimony.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4593536` offsets `335-343`; context: Although counsel for the applicant forcefully argued at the hearing that the RAD should have given some weight to the affidavit of Konjit Mikitu, who allegedly visited the applicant while she was in prison, the failure do so does not establish a reviewable error in my view.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593538` offsets `619-627`; context: I also draw attention to the Court of Appeal’s instructions in Canada (Citizenship and Immigration) v Sellan, 2008 FCA 381 at para 3:
…where the Board makes a general finding that the claimant lacks credibility, that determination is sufficient to dispose of the claim unless there is independent and credible documentary evidence in the record capable of supporting a positive disposition of the claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4593539` offsets `76-84`; context: [51] In the case at bar, the applicant provided no independent and credible evidence to show that she faces risk in Ethiopia.
- Evidence: `disposition` cue `dismissed` at chunk `4593540` offsets `25-34`; context: [52] This application is dismissed.

#### Section text

Denbel v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-05-13
Neutral citation
2015 FC 629
File numbers
IMM-3827-14
Decision Content
Date: 20150513
Docket: IMM-3827-14
Citation: 2015 FC 629
Toronto, Ontario, May 13, 2015
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
BEKELECH DENBEL
(A.K.A. BEKELECH SHIFER DENBEL,
BEKELECH SHIFERAW DENBEL)
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] In this application for judicial review brought under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], Denbel Bekelech challenges a decision rendered by the Refugee Appeal Division [RAD], which dismissed her appeal from a decision of the Refugee Protection Division [RPD] rejecting her claim for refugee protection. For the reasons that follow, this application is dismissed.
I. Background [2] The applicant is a citizen of Ethiopia. Her ethnicity is part Oromo and part Gurage. The ethnicity of her husband is Oromo. According to the applicant, the Ethiopian authorities perceive her husband as a member of the Oromo Liberation Front [OLF], a group that is currently engaged in armed struggle against the government. She alleges that the authorities arrested, imprisoned and tortured her husband in January 2012. After she posted bail and secured his release in June 2012, he disappeared to hide from the authorities.

[3] The applicant alleges that she was arrested on July 11, 2012 and held for one month because the authorities wanted to draw her husband out of hiding. She alleges that she was arrested a second time on January 3, 2013 and detained until January 5, 2013.

[4] The applicant also alleges that she supports an opposition party named Unity for Democracy and Justice [UDJ], having voted for it and distributed pamphlets on its behalf. She attributes her persecution to her support for this party and her husband’s affiliation with the OLF.

[5] On May 28, 2013, the applicant entered Canada, where she has family, on a visa. Thereafter, she applied for refugee protection due to her political opinion.

[6] The RPD rejected the applicant’s refugee claim in a decision dated September 6, 2013. The applicant filed a notice of appeal at the RAD on December 20, 2013. She submitted an appeal record on January 6, 2014. On January 31, 2014, she brought a motion to admit new evidence to the RAD record. The RAD dismissed the applicant’s appeal by decision dated April 10, 2014.

[7] While the decision under review, properly speaking, is the RAD decision, it makes sense to begin with an overview of the RPD decision. The RPD panel declared that the determinative issue was credibility. It drew several negative inferences against Mrs Bekelech’s credibility.

[8] First, the applicant was inconsistent about the circumstances surrounding her arrest. In her basis of claim form [BOC], she stated that she had been arrested twice. After her first arrest, she had been told to report to the police station regularly, and she was arrested a second time in January 2013 while reporting. At the hearing, the applicant testified that the police had come to her home at night to arrest her the second time. She could not explain this contradiction to the panel’s satisfaction. The panel considered this contradiction highly material because her second arrest was the event which allegedly motivated her to seek refuge in another country.

[9] Second, the applicant was inconsistent about the reasons the police arrested her. In her BOC, she stated that the police arrested her in January 2013 because they believed that she had been distributing political flyers for the UDJ party. At the hearing, the applicant said that she had not distributed flyers and she did not know why the police suspected her. She could not explain why she had written that she had been arrested for distributing flyers in her BOC.

[10] Third, the applicant did not offer credible testimony on being followed by government officials. In her BOC, she alleged that she had been followed for about two months. When asked to provide examples at the hearing, she offered very general and vague testimony. She could not describe a single specific example or incident.

[11] Finally, the panel noted that there were inconsistencies between the applicant’s knowledge of her husband’s activities as expressed in her BOC and her oral testimony. In the BOC, she provided a detailed account of her husband’s activities, replete with dates and background information on the OLF. However, her oral testimony was vague and ambiguous.

[12] The RPD concluded that the applicant’s allegations lacked credibility. It determined that there was no serious possibility that the applicant would be persecuted. It further determined, on the balance of probabilities, that she would not face torture or a risk to life or a risk of cruel and unusual punishment in Ethiopia.

[13] In her appeal to the RAD, the applicant provided the following pieces of new evidence:
1. An affidavit she swore;
2. An audiologist’s report;
3. A letter from a friend dated August 1, 2013; and
4. An article printed from the Internet about hearing loss.

[14] The RAD member considers the admissibility of this new evidence. He explains that he will use the test developed in the context of Pre-Removal Risk Assessment applications [PRRAs] in Raza v Canada (Citizenship and Immigration), 2007 FCA 385 [Raza]. Evidence is admissible if it meets four criteria: credibility, newness, relevance and materiality.

[15] The applicant’s affidavit proffers evidence that was not before the RPD. In particular, it states (1) that her hearing became impaired when she was struck on her left ear during her second term of imprisonment and (2) that her son called her a few weeks after the RPD hearing to tell her that the authorities were searching for him. The RAD does not accept the affidavit, since the applicant would have been aware of any hearing impairment at the time of the hearing and could have given that evidence to the RPD. There was no indication in the RPD record that the applicant raised the issue or required accommodation for her hearing loss. The second piece of information fails the Raza test because it lacks probative value. It indicates that the authorities are looking for the applicant’s son, not the applicant.

[16] The RAD employs the Raza test to exclude the three other pieces of evidence as well. The letter from the friend was written after the RPD decision but it did not meet the relevance test as it was vague and lacked probative value. The Internet article contained no date and was of a general nature about improving communication when there was hearing loss.

[17] The RAD then turns to the evidence which the applicant tendered by way of motion brought under Rule 29 of the Refugee Appeal Division Rules, SOR/2012-257 [the Rules]: a letter from her son, Wondemu Yohannes, and Canada Post tracking results for that letter. It is dated December 15, 2013. The applicant received it on January 14, 2014. The author inquires into the applicant’s health; states that her husband is alive and probably joined the OLF; and affirms that he plans to travel to South Africa himself to claim refugee protection. The writer does not allege that anyone is looking for the applicant.

[18] According to the RAD, the letter does not provide any new evidence which would justify altering the RPD decision. Nor has the applicant provided an explanation as to why she was unable to obtain or tender this document at an earlier point in time. The letter is inadmissible under Rule 29 and so a full Raza analysis is not necessary.

[19] The RAD member then conducts a lengthy standard of review analysis. He concludes that the standard of reasonableness governs the appeal.

[20] The applicant alleged that the RPD erred in failing to consider documentary evidence in support of her claim, including a letter from Ali Keder, an affidavit from Konjit Mitiku and objective country conditions evidence. The RPD also took no consideration of a receipt from the UJD party corroborating a donation she had made to it.

[21] The RAD recalls that the RPD is not required to refer to each and every piece of evidence before it. A reviewable error occurs only where the RPD omits to mention important evidence that is directly relevant to a central issue.

[22] The RAD reviews the evidence mentioned by the applicant. The RAD is satisfied that no error occurred with respect to the letter from Ali Keder, as it refers to the arrest in 2012. By contrast, the RPD’s credibility findings related only to the arrest in 2013. The letter did not speak to an issue central to the decision.

[23] The RAD accepts that some important pieces of evidence were not mentioned in the RPD decision, specifically the affidavit where Konjit Mitiku swears to have visited the applicant while she was in prison, the receipt of the donation to the UDJ and the country conditions evidence. The RAD determines that it was unreasonable for the RPD to conduct its analysis without mentioning this evidence in its reasons.

[24] The RAD disagrees with the applicant that the RPD erred by failing to conduct an objective risk assessment under section 97. The language used by the RPD shows that it did conduct a section 97 assessment in the RAD’s view. The applicant’s lack of credibility was equally fatal to her claim under section 96 and section 97. It is trite law that a negative credibility finding in relation to section 96 may obviate the need to consider section 97. Given the RPD’s concerns with the applicant’s credibility, the cursory nature of its section 97 analysis was reasonable.

[25] The RAD turns to the issue of credibility. In light of the numerous concerns identified by the RPD and the deference which credibility findings deserve, the RAD concludes that these findings pass muster on the standard of reasonableness. Consequently, the RAD confirms the RPD’s decision.
II. Issues [26] This application raises three issues:
1. Did the RAD err in its standard of review analysis?
2. Did the RAD err in its analysis of the new evidence?
3. Did the RAD err in its analysis of credibility?
III. Standard of Review [27] The standard of review which the Court ought to apply to the RAD’s selection of a standard of review is the subject of differing jurisprudence in this Court. In Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 at paras 25-34, Justice Phelan selected the standard of correctness, characterizing the RAD’s choice of a standard of review as a question of law of general interest to the legal system. Other members of the Court have taken a different view and preferred the standard of reasonableness, characterizing the issue as a legal question within the expertise of the decision-maker: see e.g. Akuffo v Canada (Citizenship and Immigration), 2014 FC 1063 and Djossou v Canada (Citizenship and Immigration), 2014 FC 1080.

[28] I do not deem it necessary to express an opinion on this matter in this case. As an appeal has been brought against Huruglica, the Court of Appeal will soon have an opportunity to answer this question. In any event, nothing turns on the Court-to-RAD standard of review here, since the RAD’s selection of a deferential standard of review was both correct and reasonable, as I explain below.

[29] The standard of review for the second issue is reasonableness, as it involves the RAD’s application of its home statute and regulations to the facts before it: Dunsmuir v New Brunswick, 2008 SCC 9 at paras 53-54.

[30] The RAD did not make independent credibility findings. Rather, it confirmed the credibility findings made by the RPD. Since this required the RAD to evaluate the facts before it in light of its enabling statute, the Court-to-RAD standard of review is reasonableness again.
IV. Analysis A. Did the RAD err in its standard of review analysis? [31] The RAD committed no error in deferring to the RPD’s findings on questions of fact and credibility despite the live debate in this Court on the appropriate standard of review,

[32] The Court has sent back decisions where the RAD showed deference on different issues. For instance, in Huruglica, the RAD deferred to the RPD’s state protection analysis. In Alyafi v Canada (Citizenship and Immigration), 2014 FC 952, the RAD deferred to the RPD’s findings on plausibility but also generalized risk – the latter was a question of mixed fact and law.

[33] In these cases, the Court has either interpreted the RAD scheme as a hybrid procedure that is somewhat similar to a de novo appeal or as a true appeal analogous to those performed by appellate courts. Yet both strands in the jurisprudence accept the principle that findings of credibility must be shown deference, since the RAD does not typically hold oral hearings and is therefore at a disadvantage in comparison to the RPD.

[34] In Huruglica, Justice Phelan expressed the view that the RAD scheme functions as an appeal de novo. Yet he recognized the need for deference when credibility is at issue (para 37). Furthermore, he stated that the standard of review for credibility is not “palpable and overriding error” (paras 54-55). On my interpretation, he implicitly endorsed the standard of reasonableness, as that is the most common deferential standard in our law.

[35] In Spasoja v Canada (Citizenship and Immigration), 2014 FC 913 at para 39, Justice Roy took the view that the RAD functions like an appellate court, relying on the analytical framework in Barreau (Québec) c Québec (Tribunal des professions), 2011 QCCA 1498. When credibility findings are at issue, he asserted that the RAD ought to apply the standard of review of “palpable and overriding error”.

[36] This debate is largely academic because neither side would agree with the applicant that the standard of correctness applies. If the RAD erred by naming the deferential standard it chose “reasonableness” instead of “palpable and overriding error”, nothing turns on it.

[37] Shortly before the hearing, the applicant brought to my attention a recent case decided by my brother Justice Simon Noël: Khachatourian v Canada (Citizenship and Immigration), 2015 FC 182. In comments made in obiter at paras 30-34, Justice Noël questioned the wisdom of allowing the RAD to defer to the RPD’s findings, even on questions of credibility. I agree with Justice Noël that an appellate tribunal does not play a judicial review function and deplore any language used by the RAD which points in that direction. However, and with the greatest respect, I do not agree that the RAD should routinely conduct a fresh assessment of credibility on appeals brought before it.

[38] It is difficult to understand how an administrative tribunal could apply the standard of correctness to findings of credibility on a paper-based appeal. The RPD has a situational advantage when compared to the RAD, as it can observe the claimant in person while the RAD does not do so except in unusual circumstances. If the RAD owed no deference to the RPD’s findings on the issue which the RPD is best placed to decide, the statutory scheme would involve unnecessary duplication. The RPD would have no raison d’être. This recommends RAD-to-RPD deference on issues of credibility.

[39] I am satisfied, in any event, that the RAD made its own assessment of the applicant’s credibility relying on the very thorough discussion by the RPD of the inconsistencies which it had found between her BOC and testimony.
B. Did the RAD err in its analysis of the new evidence? [40] The RAD was entitled to import the Raza factors established for PRRAs when applying the new evidence rule in subsection 110(4). In Iyamuremye v Canada (Citizenship and Immigration), 2014 FC 494 at para 45, Justice Shore held that:
Considering the dearth of case law interpreting subsection 110(4) and given the essential similarity between the provisions in question, the Court does not find it unreasonable for the RAD to have referred to the factors set out in Raza, above, to analyse the admissibility of fresh evidence. This case law established a legal meaning to the general application of the words “new evidence,” which, in the Court’s view, is consistent with Parliament’s clear intention with regard to subsection 110(4) to require that the RAD review the RPD’s decision as is, unless new, credible and relevant evidence arose after the rejection, that might have affected the outcome of the RPD hearing if that evidence had been presented to it.
[Emphasis in original]

[41] Moreover, the RAD relied on the express language of Rule 29(4) to exclude new evidence tendered after the appeal record was filed. That Rule explicitly lists some of the Raza factors.

[42] In Khachatourian, above, at para 37, Justice Simon Noël expressed reservations about the propriety of transposing Raza to the RAD context, referring to the analysis of Justice Gagné in Singh v Canada (Citizenship and Immigration), 2014 FC 1022 at paras 44-58. Once again, I respectfully disagree. As Justice Shore observed in Iyamuremye, subsections 110(4) and 113(a) contain virtually identical language. In light of the overall structure of these provisions, I accord no significance to the slight discrepancy in the French text (“qu’elle n’aurait pas normalement présentés” versus “qu’il n’était pas raisonnable, dans les circonstances, de s’attendre à ce qu’il les ait présentés”).

[43] When interpreting legislative intent, the Court must give priority to the written text in the absence of any lexical ambiguity. The Court’s opinions on best policy cannot supplant the text of the law; nor can select passages from the Hansard. In my view, Parliament intended these two provisions to enshrine the same legal test. If Parliament had intended to establish more flexible admissibility rules in RAD appeals, it would not have replicated the restrictive language which governs PRRAs.

[44] I am satisfied that the RAD reasonably excluded the contested evidence for the reasons it provided. The applicant focused on the RAD’s exclusion of her son’s letter under Rule 29(4). In my view, the RAD reasonably excluded the letter due to its low relevance and probative value. It also expressed reasonable concerns that the letter could have been available earlier.
C. Did the RAD err in its analysis of credibility? [45] The RPD based its numerous negative credibility findings on significant inconsistencies and contradictions between the applicant’s BOC narrative and her oral testimony. The applicant did not dispute these findings during her appeal at the RAD, nor has she done so on this judicial review application. Rather, she insists that the RPD erred by failing to consider documentary evidence which corroborates her allegations and establishes the risk she faces in Ethiopia.

[46] The RAD lent some support to the applicant’s argument, declaring that the RPD behaved unreasonably by failing to mention that evidence. Yet the RAD ultimately upheld the RPD’s conclusions because its credibility findings were reasonable in light of the record. The RAD committed no reviewable error in this regard.

[47] In Kanto v Canada (Citizenship and Immigration), 2012 FC 1049, Justice de Montigny found that the RPD had erred in its state protection analysis but had still reasonably concluded that the applicants lacked credibility. He dismissed the judicial review application for the following reasons, expressed at para 45:
Although the Applicants have demonstrated an error in the assessment of state protection, it is of no consequence because they have failed to establish that they are in need of that protection. The Board member has not found their story credible and, as a result, their fear of persecution is not subjectively grounded. As a result, this application for judicial review ought to be dismissed.

[48] The same can be said in this case. The RAD implicitly and

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 11809:2 · paragraphs 47-48

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3085e18812d793ece9f9d382dff10831b61e52ac6b69a9203ad716279e7db7e5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 11809:2:subtheme:1 · paragraphs 47-48

- Raw key terms: `judgment, mosley, appearances, applicant, application, attorney, barrister, bekelech`
- Display key terms: `mosley, barrister, bekelech`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: mosley, barrister, bekelech Operative outcome context: JUDGMENT THIS COURT’S JUDGMENT is that this application is dismissed. Evidence spans paragraphs 47-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4593540` offsets `179-188`; context: JUDGMENT
THIS COURT’S JUDGMENT is that this application is dismissed.

#### Section text

JUDGMENT
THIS COURT’S JUDGMENT is that this application is dismissed. No questions are certified.
“Richard G. Mosley”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-3827-14
STYLE OF CAUSE:
BEKELECH DENBEL (A.K.A. BEKELECH SHIFER DENBEL, BEKELECH SHIFERAW DENBEL) v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
MAY 12, 2015
JUDGMENT AND REASONS:
MOSLEY J.
DATED:
MAY 13, 2015
APPEARANCES:
D. Clifford Luyt
For The Applicant
Negar Hashemi
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Barrister and Solicitor
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
FOR THE RESPONDENT
