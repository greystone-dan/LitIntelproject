# Discussion Units: case 12178

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **95**
- Continuity pairs: **94**
- Discussion Units: **6**
- Paragraph source hashes: **95**
- Sub-themes: **34**

## 12178:1 · paragraphs 0-36

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7882fbd78542638a2d76f613e666fb3adfb6b74bdc41c675a1fee1736762fe6b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12178:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, decision, canada, claim, convention, explained, finding, hearing`
- Display key terms: `convention, explained, finding, hearing`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: convention, explained, finding, hearing Rule/authority context: [1] This is an application for judicial review of a decision of the Refugee Appeal Division of the Immigration and Refugee Board of Canada (RAD), dated September 17, 2014, in which the RAD confirmed the finding of the Re Application context: Prior to the second sitting of his hearing on January 16, 2014, the Applicant submitted a second addendum to his BOC narrative in which he explained that he feared persecution upon return to Ghana as a result of his HIV  Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4609679` offsets `338-349`; context: [1] This is an application for judicial review of a decision of the Refugee Appeal Division of the Immigration and Refugee Board of Canada (RAD), dated September 17, 2014, in which the RAD confirmed the finding of the Refugee Protection Division (RPD) that the Applicant is neither a Convention Refugee nor a person in need of protection pursuant to s 96 or s 97, respectively, of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].
- Evidence: `reasoning_application` cue `because` at chunk `4609679` offsets `1388-1395`; context: Prior to the second sitting of his hearing on January 16, 2014, the Applicant submitted a second addendum to his BOC narrative in which he explained that he feared persecution upon return to Ghana as a result of his HIV positive status because, after disclosing his status to his wife who is in Ghana, he had received death threats from her family.

#### 12178:1:subtheme:2 · paragraphs 3-4

- Raw key terms: `accept, applicant, evidence, issue, persecution, appeal, articles, based`
- Display key terms: `accept, persecution, articles, based`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: accept, persecution, articles, based Position/evidence statements: His new counsel submitted a request to the RAD to consider four articles about stigma and HIV status in Ghana based on the Applicant’s view that there had been a lack of evidence before the RPD on this issue. Rule/authority context: His new counsel also made detailed submissions about why the RAD should accept the new evidence, pursuant to s 110(4) of the IRPA. Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609681` offsets `356-361`; context: His new counsel submitted a request to the RAD to consider four articles about stigma and HIV status in Ghana based on the Applicant’s view that there had been a lack of evidence before the RPD on this issue.
- Evidence: `party_position` cue `submitted` at chunk `4609681` offsets `170-179`; context: His new counsel submitted a request to the RAD to consider four articles about stigma and HIV status in Ghana based on the Applicant’s view that there had been a lack of evidence before the RPD on this issue.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609681` offsets `324-332`; context: His new counsel submitted a request to the RAD to consider four articles about stigma and HIV status in Ghana based on the Applicant’s view that there had been a lack of evidence before the RPD on this issue.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4609681` offsets `460-471`; context: His new counsel also made detailed submissions about why the RAD should accept the new evidence, pursuant to s 110(4) of the IRPA.
- Evidence: `issue` cue `issues` at chunk `4609682` offsets `234-240`; context: The RPD’s Decision [6] The determinative issues before the RPD were the Applicant’s credibility, the well-foundedness of his fear of persecution, and the issue of discrimination versus persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609682` offsets `38-46`; context: [5] The RAD refused to accept the new evidence finding that it did not meet the requirements of s 110(4).

#### 12178:1:subtheme:3 · paragraphs 5-6

- Raw key terms: `applicant, concluded, documentary, evidence, persecution, accept, accepted, amount`
- Display key terms: `concluded, documentary, persecution, accept, accepted, amount`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: concluded, documentary, persecution, accept, accepted, amount Rule/authority context: However, based on the documentary evidence, the RPD concluded that while the Applicant may be subject to discrimination upon return to Ghana, that discrimination was not sufficiently persistent and punitive so as to amou Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609683` offsets `11-16`; context: [7] On the issue of credibility, the RPD concluded that the Applicant did not provide credible evidence regarding his fear of persecution as a result of his refusal to accept the Chieftaincy.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609683` offsets `95-103`; context: [7] On the issue of credibility, the RPD concluded that the Applicant did not provide credible evidence regarding his fear of persecution as a result of his refusal to accept the Chieftaincy.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609684` offsets `253-261`; context: However, based on the documentary evidence, the RPD concluded that while the Applicant may be subject to discrimination upon return to Ghana, that discrimination was not sufficiently persistent and punitive so as to amount to persecution under the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `4609684` offsets `457-462`; context: However, based on the documentary evidence, the RPD concluded that while the Applicant may be subject to discrimination upon return to Ghana, that discrimination was not sufficiently persistent and punitive so as to amount to persecution under the IRPA.
- Evidence: `counterargument_limitation` cue `However` at chunk `4609684` offsets `219-226`; context: However, based on the documentary evidence, the RPD concluded that while the Applicant may be subject to discrimination upon return to Ghana, that discrimination was not sufficiently persistent and punitive so as to amount to persecution under the IRPA.

#### 12178:1:subtheme:4 · paragraphs 7-13

- Raw key terms: `evidence, applicant, claim, assessment, credible, decision, found, ghana`
- Display key terms: `assessment, credible, ghana`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: assessment, credible, ghana Rule/authority context: Decision Under Review – RAD Decision [11] On appeal, the RAD first considered the admissibility of the new evidence pursuant to s 110(4) of the IRPA, which evidence was comprised of four articles concerning HIV related s | [18] The RAD finds that it is bound by s 110(4) of the IRPA, and is not bound by jurisprudence which related to the admissibility of new evidence in Pre-Removal Risk Assessment (PRRA) applications, and therefore the RAD  Application context: [13] Therefore, the RAD concluded that: | [18] The RAD finds that it is bound by s 110(4) of the IRPA, and is not bound by jurisprudence which related to the admissibility of new evidence in Pre-Removal Risk Assessment (PRRA) applications, and therefore the RAD  Evidence spans paragraphs 7-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609685` offsets `175-180`; context: [9] Finally, the RPD considered the Applicant’s claim that he also fears persecution as a result of his status as a homosexual man, and found the Applicant’s evidence on this issue not to be credible for a number of reasons, including the fact that he omitted this information from his initial BOC narrative.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609685` offsets `158-166`; context: [9] Finally, the RPD considered the Applicant’s claim that he also fears persecution as a result of his status as a homosexual man, and found the Applicant’s evidence on this issue not to be credible for a number of reasons, including the fact that he omitted this information from his initial BOC narrative.
- Evidence: `evidence_fact` cue `found that` at chunk `4609686` offsets `18-28`; context: [10] The RPD also found that the Applicant was not credible overall and, for all these reasons, the Applicant’s claim was rejected.
- Evidence: `governing_rule` cue `Under` at chunk `4609686` offsets `141-146`; context: Decision Under Review – RAD Decision [11] On appeal, the RAD first considered the admissibility of the new evidence pursuant to s 110(4) of the IRPA, which evidence was comprised of four articles concerning HIV related stigma and discrimination.
- Evidence: `counterargument_limitation` cue `However` at chunk `4609686` offsets `850-857`; context: However, the RAD rejected this explanation, noting that the Applicant was represented by experienced counsel who submitted some evidence regarding the treatment of HIV positive individuals in Ghana and made extensive submissions on the risks that the Applicant would face as an HIV positive person should he return to Ghana.
- Evidence: `evidence_fact` cue `found that` at chunk `4609687` offsets `26-36`; context: [12] In addition, the RAD found that the Applicant did not provide sufficient evidence to prove that the new evidence was not reasonably available, or that he could not reasonably have been expected in the circumstances to have presented the new evidence at the time of the rejection of his claim by the RPD.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4609688` offsets `5-14`; context: [13] Therefore, the RAD concluded that:
- Evidence: `evidence_fact` cue `evidence` at chunk `4609689` offsets `137-145`; context: [18] The RAD finds that it is bound by s 110(4) of the IRPA, and is not bound by jurisprudence which related to the admissibility of new evidence in Pre-Removal Risk Assessment (PRRA) applications, and therefore the RAD does not have discretion to accept evidence that is not covered by s 110(4).
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4609689` offsets `81-94`; context: [18] The RAD finds that it is bound by s 110(4) of the IRPA, and is not bound by jurisprudence which related to the admissibility of new evidence in Pre-Removal Risk Assessment (PRRA) applications, and therefore the RAD does not have discretion to accept evidence that is not covered by s 110(4).
- Evidence: `reasoning_application` cue `therefore` at chunk `4609689` offsets `202-211`; context: [18] The RAD finds that it is bound by s 110(4) of the IRPA, and is not bound by jurisprudence which related to the admissibility of new evidence in Pre-Removal Risk Assessment (PRRA) applications, and therefore the RAD does not have discretion to accept evidence that is not covered by s 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4609690` offsets `243-251`; context: [14] Relying on this Court’s decision in Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 [Huruglica], the RAD noted that its task was to conduct an independent assessment of the Applicant’s claim by reviewing the totality of the evidence which was presented at the time of the rejection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609691` offsets `228-236`; context: After reviewing the evidence on the record, the RAD concurred with the RPD’s finding that the Applicant’s allegations were not credible and that he was not a credible witness.

#### 12178:1:subtheme:5 · paragraphs 14-16

- Raw key terms: `applicant, evidence, appeal, apply, canada, correctness, even, irpa`
- Display key terms: `apply, correctness, even, irpa`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: apply, correctness, even, irpa Position/evidence statements: [16] The RAD then considered the evidence relating to the Applicant’s sur place claim, based on his status as a person who is HIV positive, and considered whether he would face a serious possibility of persecution as a r | Standard of Review [19] As to the first issue, the Applicant submits that the RAD’s interpretation of s 110(4) is a pure question of law that gives rise to issues under the Canadian Charter of Rights and Freedoms, Part I Rule/authority context: [17] As a result, the RAD confirmed the RPD’s determination that the Applicant is neither a Convention refugee nor a person in need of protection, pursuant to s 111(1)(a) of the IRPA. | This point was recognized by the Federal Court of Appeal in Raza v Canada (Citizenship and Immigration), 2007 FCA 385 [Raza], where it developed a legal test for assessing the admissibility of new evidence on a Pre-Remov Application context: Moreover, the RAD concluded that the Applicant had not provided sufficient credible or trustworthy evidence that he would be perceived as sexually immoral or to be a homosexual because of his HIV positive status. | Therefore, the appeal was dismissed. Operative outcome context: Therefore, the appeal was dismissed. Evidence spans paragraphs 14-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609692` offsets `155-162`; context: [16] The RAD then considered the evidence relating to the Applicant’s sur place claim, based on his status as a person who is HIV positive, and considered whether he would face a serious possibility of persecution as a result of that status.
- Evidence: `party_position` cue `claim` at chunk `4609692` offsets `80-85`; context: [16] The RAD then considered the evidence relating to the Applicant’s sur place claim, based on his status as a person who is HIV positive, and considered whether he would face a serious possibility of persecution as a result of that status.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609692` offsets `33-41`; context: [16] The RAD then considered the evidence relating to the Applicant’s sur place claim, based on his status as a person who is HIV positive, and considered whether he would face a serious possibility of persecution as a result of that status.
- Evidence: `reasoning_application` cue `because` at chunk `4609692` offsets `683-690`; context: Moreover, the RAD concluded that the Applicant had not provided sufficient credible or trustworthy evidence that he would be perceived as sexually immoral or to be a homosexual because of his HIV positive status.
- Evidence: `issue` cue `Issues` at chunk `4609693` offsets `221-227`; context: Issues [18] In my view, the issues can be framed as follows:
Did the RAD err in interpreting s 110(4) by finding that it did not have the discretion to admit new evidence that was otherwise technically inadmissible and, therefore, fail to consider Charter values in refusing to admit the new evidence?
- Evidence: `party_position` cue `submits` at chunk `4609693` offsets `835-842`; context: Standard of Review [19] As to the first issue, the Applicant submits that the RAD’s interpretation of s 110(4) is a pure question of law that gives rise to issues under the Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), 1982, c 11 [Charter] and, as such, should be reviewed on the correctness standard (Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir]).
- Evidence: `evidence_fact` cue `evidence` at chunk `4609693` offsets `383-391`; context: Issues [18] In my view, the issues can be framed as follows:
Did the RAD err in interpreting s 110(4) by finding that it did not have the discretion to admit new evidence that was otherwise technically inadmissible and, therefore, fail to consider Charter values in refusing to admit the new evidence?
- Evidence: `governing_rule` cue `pursuant to` at chunk `4609693` offsets `147-158`; context: [17] As a result, the RAD confirmed the RPD’s determination that the Applicant is neither a Convention refugee nor a person in need of protection, pursuant to s 111(1)(a) of the IRPA.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4609693` offsets `184-193`; context: Therefore, the appeal was dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4609693` offsets `210-219`; context: Therefore, the appeal was dismissed.
- Evidence: `party_position` cue `submits` at chunk `4609694` offsets `24-31`; context: [20] The Applicant also submits that review on a correctness standard is important to ensure judicial consistency.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609694` offsets `184-192`; context: Allowing every RAD member to apply their own test when assessing new evidence creates the absurd situation in which the application of the law changes in accordance with each member, rather than the evidence provided.
- Evidence: `governing_rule` cue `legal test` at chunk `4609694` offsets `480-490`; context: This point was recognized by the Federal Court of Appeal in Raza v Canada (Citizenship and Immigration), 2007 FCA 385 [Raza], where it developed a legal test for assessing the admissibility of new evidence on a Pre-Removal Risk Assessment [PRRA] application, pursuant to s 113(a) of the IRPA, that would apply to all PRRA applications.
- Evidence: `reasoning_application` cue `apply` at chunk `4609694` offsets `144-149`; context: Allowing every RAD member to apply their own test when assessing new evidence creates the absurd situation in which the application of the law changes in accordance with each member, rather than the evidence provided.

#### 12178:1:subtheme:6 · paragraphs 17-19

- Raw key terms: `decision, paras, respondent, review, singh, standard, a-512-14, above`
- Display key terms: `paras, review, singh, standard, a-512-14, above`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: paras, review, singh, standard, a-512-14, above Position/evidence statements: [21] The Respondent, on the other hand, submits that the RAD’s interpretation of s 110(4) is squarely within its own expertise and does not involve a question of central importance to the legal system as a whole or any o Rule/authority context: [22] Further, when Charter values are applied to an individual administrative decision, they are applied in relation to a particular set of facts and, therefore, a deferential standard of review is to be applied (Doré v  | In the recent decision of Singh (currently under appeal, see: A-512-14), Madam Justice Gagné reviewed the same cases cited by the Respondent above and, based on those cases, she concluded: Application context: Thus, the reasonableness standard should apply to this issue (Saskatchewan Human Rights Commission v Whatcott, 2013 SCC 11 at para 167; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Assn, 2011 SCC 61 | [22] Further, when Charter values are applied to an individual administrative decision, they are applied in relation to a particular set of facts and, therefore, a deferential standard of review is to be applied (Doré v  Evidence spans paragraphs 17-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4609695` offsets `150-158`; context: [21] The Respondent, on the other hand, submits that the RAD’s interpretation of s 110(4) is squarely within its own expertise and does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard.
- Evidence: `party_position` cue `submits` at chunk `4609695` offsets `40-47`; context: [21] The Respondent, on the other hand, submits that the RAD’s interpretation of s 110(4) is squarely within its own expertise and does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard.
- Evidence: `reasoning_application` cue `apply` at chunk `4609695` offsets `341-346`; context: Thus, the reasonableness standard should apply to this issue (Saskatchewan Human Rights Commission v Whatcott, 2013 SCC 11 at para 167; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Assn, 2011 SCC 61 at paras 45-46; McLean v British Columbia, 2013 SCC 67 at paras 26, 30; Singh v Canada (Citizenship and Immigration), 2014 FC 1022 at para 42 [Singh]).
- Evidence: `governing_rule` cue `standard of review` at chunk `4609696` offsets `176-194`; context: [22] Further, when Charter values are applied to an individual administrative decision, they are applied in relation to a particular set of facts and, therefore, a deferential standard of review is to be applied (Doré v Barreau du Quebec, 2012 SCC 12 at paras 35-36, 52-58 [Doré]).
- Evidence: `reasoning_application` cue `applied` at chunk `4609696` offsets `38-45`; context: [22] Further, when Charter values are applied to an individual administrative decision, they are applied in relation to a particular set of facts and, therefore, a deferential standard of review is to be applied (Doré v Barreau du Quebec, 2012 SCC 12 at paras 35-36, 52-58 [Doré]).
- Evidence: `governing_rule` cue `under` at chunk `4609697` offsets `91-96`; context: In the recent decision of Singh (currently under appeal, see: A-512-14), Madam Justice Gagné reviewed the same cases cited by the Respondent above and, based on those cases, she concluded:

#### 12178:1:subtheme:7 · paragraphs 20-21

- Raw key terms: `reasonableness, standard, therefore, admit, application, case, comity, determination`
- Display key terms: `reasonableness, standard, therefore, admit, case, comity, determination`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: reasonableness, standard, therefore, admit, case, comity, determination Application context: [42] Therefore, I am of the view that both the RAD's interpretation of subsection 110(4) of the Act (as a question of law that is not of general importance to the legal system as a whole and outside the expertise of the  | [24] In the interests of judicial comity, I will therefore review the RAD’s determination that s 110(4) did not provide it with discretion to admit the new evidence on the reasonableness standard. Evidence spans paragraphs 20-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4609698` offsets `106-114`; context: [42] Therefore, I am of the view that both the RAD's interpretation of subsection 110(4) of the Act (as a question of law that is not of general importance to the legal system as a whole and outside the expertise of the RAD) and its application to the facts of this case (as a question of mixed fact and law) are to be reviewed on the reasonableness standard.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4609698` offsets `5-14`; context: [42] Therefore, I am of the view that both the RAD's interpretation of subsection 110(4) of the Act (as a question of law that is not of general importance to the legal system as a whole and outside the expertise of the RAD) and its application to the facts of this case (as a question of mixed fact and law) are to be reviewed on the reasonableness standard.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609699` offsets `156-164`; context: [24] In the interests of judicial comity, I will therefore review the RAD’s determination that
s 110(4) did not provide it with discretion to admit the new evidence on the reasonableness standard.
- Evidence: `reasoning_application` cue `therefore` at chunk `4609699` offsets `49-58`; context: [24] In the interests of judicial comity, I will therefore review the RAD’s determination that
s 110(4) did not provide it with discretion to admit the new evidence on the reasonableness standard.

#### 12178:1:subtheme:8 · paragraphs 22-23

- Raw key terms: `fact, issue, para, reasonableness, reviewable, standard, acceptable, admissible`
- Display key terms: `fact, para, reasonableness, reviewable, standard, acceptable, admissible`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: fact, para, reasonableness, reviewable, standard, acceptable, admissible Position/evidence statements: Applicant’s Position [27] The Applicant submits that this matter concerns the factors the RAD must consider when applying the new evidence rule set out in s 110(4) of the IRPA. Application context: Issue 1: Did the RAD err in interpreting s 110(4) by finding that it did not have the discretion to admit new evidence that was otherwise technically inadmissible and, therefore, fail to consider Charter values in refusi Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609700` offsets `22-27`; context: [25] As to the second issue, the RAD’s application of s 110(4) is a question of mixed fact and law that is reviewable on the reasonableness standard (Singh at para 42; Iyamuremye v Canada (Citizenship and Immigration), 2014 FC 494 at para 43).
- Evidence: `issue` cue `issue` at chunk `4609701` offsets `21-26`; context: [26] As to the third issue, the RAD’s assessment of the documentary evidence that was before the RPD involves findings of fact that are subject to deference and thus reviewable on the reasonableness standard (Dunsmuir at para 51).
- Evidence: `party_position` cue `submits` at chunk `4609701` offsets `779-786`; context: Applicant’s Position [27] The Applicant submits that this matter concerns the factors the RAD must consider when applying the new evidence rule set out in s 110(4) of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609701` offsets `68-76`; context: [26] As to the third issue, the RAD’s assessment of the documentary evidence that was before the RPD involves findings of fact that are subject to deference and thus reviewable on the reasonableness standard (Dunsmuir at para 51).
- Evidence: `reasoning_application` cue `therefore` at chunk `4609701` offsets `654-663`; context: Issue 1: Did the RAD err in interpreting s 110(4) by finding that it did not have the discretion to admit new evidence that was otherwise technically inadmissible and, therefore, fail to consider Charter values in refusing to admit the new evidence?
- Evidence: `counterargument_limitation` cue `but` at chunk `4609701` offsets `1055-1058`; context: More specifically, how the RAD should consider its Charter jurisdiction when new evidence is raised that may not be technically admissible but does raise serious evidence of risk that challenges the core findings of the RPD’s decision.

#### 12178:1:subtheme:9 · paragraphs 24-28

- Raw key terms: `charter, applicant, approach, consider, court, discretion, evidence, exercise`
- Display key terms: `charter, approach, consider, discretion, exercise`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: charter, approach, consider, discretion, exercise Position/evidence statements: [28] The Applicant submits that the Raza test is not appropriate in the RAD context and, instead, proposes a new test derived from the Supreme Court of Canada’s decision in Doré in which the RAD’s Charter considerations  | a) Inconsistent Application at the RAD - The Applicant submits that there are currently three different interpretations by the RAD of its jurisdiction under s 110(4). Rule/authority context: [29] In support of this position, which broadens the RAD’s jurisdiction under s 110(4) to include the discretion to admit new evidence that is technically inadmissible, the Applicant relies on the following arguments. | [49] […] even if the Officer may exclude a report under paragraph 113(a), the PRRA Officer had discretion to consider the report. Application context: The first is a strict statutory interpretation, as was applied by the RAD in this case. | The PRRA Officer therefore erred in that he failed to properly exercise his discretion to consider credible, material evidence that supports Mr. Operative outcome context: In this proposed new test, where fresh evidence is submitted that is not technically admissible, the RAD should consider whether that evidence contradicts a specific finding of the RPD and, if allowed, could lead the RAD | Relying on these findings in Singh, the Applicant submits that the fact that the RAD is a de novo hearing, with broad remedial powers, and is often the last assessment of risk prior to removal, are all important indicato Evidence spans paragraphs 24-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609702` offsets `382-389`; context: In this proposed new test, where fresh evidence is submitted that is not technically admissible, the RAD should consider whether that evidence contradicts a specific finding of the RPD and, if allowed, could lead the RAD to a different conclusion on a central aspect of the claim.
- Evidence: `party_position` cue `submits` at chunk `4609702` offsets `19-26`; context: [28] The Applicant submits that the Raza test is not appropriate in the RAD context and, instead, proposes a new test derived from the Supreme Court of Canada’s decision in Doré in which the RAD’s Charter considerations are implicit in its s 110(4) assessment.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609702` offsets `300-308`; context: In this proposed new test, where fresh evidence is submitted that is not technically admissible, the RAD should consider whether that evidence contradicts a specific finding of the RPD and, if allowed, could lead the RAD to a different conclusion on a central aspect of the claim.
- Evidence: `disposition` cue `allowed` at chunk `4609702` offsets `454-461`; context: In this proposed new test, where fresh evidence is submitted that is not technically admissible, the RAD should consider whether that evidence contradicts a specific finding of the RPD and, if allowed, could lead the RAD to a different conclusion on a central aspect of the claim.
- Evidence: `issue` cue `whether` at chunk `4609703` offsets `707-714`; context: The second approach involves the application of the Raza test, which was developed for determining whether evidence is admissible under s 113(a) of the IRPA, a nearly identical provision that applies in the context of a PRRA (for example: X (RE), 2014 CanLII 55520 (CA IRB); X(RE), 2014 CanLII 60409 (CA IRB)).
- Evidence: `party_position` cue `submits` at chunk `4609703` offsets `273-280`; context: a) Inconsistent Application at the RAD - The Applicant submits that there are currently three different interpretations by the RAD of its jurisdiction under s 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4609703` offsets `126-134`; context: [29] In support of this position, which broadens the RAD’s jurisdiction under s 110(4) to include the discretion to admit new evidence that is technically inadmissible, the Applicant relies on the following arguments.
- Evidence: `governing_rule` cue `under` at chunk `4609703` offsets `72-77`; context: [29] In support of this position, which broadens the RAD’s jurisdiction under s 110(4) to include the discretion to admit new evidence that is technically inadmissible, the Applicant relies on the following arguments.
- Evidence: `reasoning_application` cue `applied` at chunk `4609703` offsets `440-447`; context: The first is a strict statutory interpretation, as was applied by the RAD in this case.
- Evidence: `counterargument_limitation` cue `fails` at chunk `4609703` offsets `1142-1147`; context: For example, the test fails to account for situations, like the present case, where the evidence may have been available at the time of the RPD hearing, but nevertheless raises a serious issue of risk.
- Evidence: `disposition` cue `upheld` at chunk `4609703` offsets `3961-3967`; context: Relying on these findings in Singh, the Applicant submits that the fact that the RAD is a de novo hearing, with broad remedial powers, and is often the last assessment of risk prior to removal, are all important indicators that the RAD must also ensure that the Applicant’s s 7 Charter rights, which are an inherent part of the refugee process, are upheld in the exercise of its discretion to admit new evidence under s 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4609704` offsets `175-183`; context: A PRRA Officer is not limited to considering evidence submitted by the applicant, but rather has an obligation to conduct sufficient independent research in order to come to a proper determination.
- Evidence: `governing_rule` cue `under` at chunk `4609704` offsets `50-55`; context: [49] […] even if the Officer may exclude a report under paragraph 113(a), the PRRA Officer had discretion to consider the report.
- Evidence: `reasoning_application` cue `therefore` at chunk `4609704` offsets `528-537`; context: The PRRA Officer therefore erred in that he failed to properly exercise his discretion to consider credible, material evidence that supports Mr.
- Evidence: `counterargument_limitation` cue `but` at chunk `4609704` offsets `212-215`; context: A PRRA Officer is not limited to considering evidence submitted by the applicant, but rather has an obligation to conduct sufficient independent research in order to come to a proper determination.
- Evidence: `party_position` cue `submits` at chunk `4609705` offsets `19-26`; context: [30] The Applicant submits that interpreting s 110(4) in a rigid manner, with no element of Charter discretion, would lead to a rigid regime in which new evidence would be rejected under a technical reading of the statute and applicants would be routinely forced to seek a remedy pursuant to s 24 of the Charter.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609705` offsets `154-162`; context: [30] The Applicant submits that interpreting s 110(4) in a rigid manner, with no element of Charter discretion, would lead to a rigid regime in which new evidence would be rejected under a technical reading of the statute and applicants would be routinely forced to seek a remedy pursuant to s 24 of the Charter.
- Evidence: `governing_rule` cue `under` at chunk `4609705` offsets `181-186`; context: [30] The Applicant submits that interpreting s 110(4) in a rigid manner, with no element of Charter discretion, would lead to a rigid regime in which new evidence would be rejected under a technical reading of the statute and applicants would be routinely forced to seek a remedy pursuant to s 24 of the Charter.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4609706` offsets `36-49`; context: [31] Recent Supreme Court of Canada jurisprudence has favoured a more nuanced approach in which Charter values are folded into all reasonable decisions and are “fully addressed within the framework of the Board’s statutory mandate and the exercise of its discretion in accordance with Charter values” (Conway at para 103).

#### 12178:1:subtheme:10 · paragraphs 29-30

- Raw key terms: `analysis, applicant, evidence, upon, whether, accepted, amounts, assess`
- Display key terms: `analysis, upon, whether, accepted, amounts, assess`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: analysis, upon, whether, accepted, amounts, assess Position/evidence statements: [32] Following Doré, the Applicant submits that the RAD’s parallel Charter jurisdiction should be implicitly folded into the s 110(4) analysis. Evidence spans paragraphs 29-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609707` offsets `243-250`; context: Thus, even if the RAD finds that new evidence is technically inadmissible, it must go on to assess whether that evidence, if included, would raise a serious possibility of risk.
- Evidence: `party_position` cue `submits` at chunk `4609707` offsets `35-42`; context: [32] Following Doré, the Applicant submits that the RAD’s parallel Charter jurisdiction should be implicitly folded into the s 110(4) analysis.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609707` offsets `181-189`; context: Thus, even if the RAD finds that new evidence is technically inadmissible, it must go on to assess whether that evidence, if included, would raise a serious possibility of risk.
- Evidence: `issue` cue `whether` at chunk `4609708` offsets `90-97`; context: [33] In the present case, the RAD found that there was insufficient evidence to determine whether the discrimination the Applicant would face as a result of his HIV positive status amounts to persecution.
- Evidence: `evidence_fact` cue `found that` at chunk `4609708` offsets `34-44`; context: [33] In the present case, the RAD found that there was insufficient evidence to determine whether the discrimination the Applicant would face as a result of his HIV positive status amounts to persecution.
- Evidence: `counterargument_limitation` cue `However` at chunk `4609708` offsets `205-212`; context: However, that analysis was based only on the documents that were before the RPD, and had the RAD simply “turned the page”, i.

#### 12178:1:subtheme:11 · paragraphs 31-36

- Raw key terms: `applicant, evidence, considered, canada, condition, country, establish, explanation`
- Display key terms: `considered, condition, country, establish, explanation`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: considered, condition, country, establish, explanation Position/evidence statements: Respondent’s Position [35] The Respondent submits that there was no error in the application of the test for admitting new evidence; the Applicant has failed to show that the RAD erred in refusing to admit the new eviden | [36] The Respondent submits that the RAD’s interpretation of s 110(4) is consistent with the Charter and that Charter values do not provide extra-legislative discretion to admit evidence that is clearly inadmissible unde Rule/authority context: [36] The Respondent submits that the RAD’s interpretation of s 110(4) is consistent with the Charter and that Charter values do not provide extra-legislative discretion to admit evidence that is clearly inadmissible unde Application context: It properly applied s 110(4) and reasonably concluded that the evidence did not meet the statutory requirements, which is admitted by the Applicant. | While the Applicant relies on Elezi, that case is of little assistance because in addition to the evidence being of a different nature, the Court also found that the applicant could not reasonably have been expected in t Operative outcome context: Moreover, the fact that the Federal Court can review the RAD’s decision provides a further indication that the Applicant is afforded fundamental justice, and that the RAD is not required to conduct an appeal de novo of t Evidence spans paragraphs 31-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609709` offsets `20-27`; context: [34] In considering whether to admit the new evidence, the RAD had an obligation to consider whether rejecting that evidence would have an impact on the Applicant’s s 7 Charter rights, and if so, the RAD was required to balance any infringement against Parliament’s intent to make the RAD a fast and expedient process.
- Evidence: `party_position` cue `submits` at chunk `4609709` offsets `426-433`; context: Respondent’s Position [35] The Respondent submits that there was no error in the application of the test for admitting new evidence; the Applicant has failed to show that the RAD erred in refusing to admit the new evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609709` offsets `45-53`; context: [34] In considering whether to admit the new evidence, the RAD had an obligation to consider whether rejecting that evidence would have an impact on the Applicant’s s 7 Charter rights, and if so, the RAD was required to balance any infringement against Parliament’s intent to make the RAD a fast and expedient process.
- Evidence: `reasoning_application` cue `applied` at chunk `4609709` offsets `620-627`; context: It properly applied s 110(4) and reasonably concluded that the evidence did not meet the statutory requirements, which is admitted by the Applicant.
- Evidence: `issue` cue `issue` at chunk `4609710` offsets `1266-1271`; context: b) Application of s 110(4) by the RAD is not fundamentally inconsistent - The Respondent takes issue with the Applicant’s assertion that there are significant differences in the application of the Raza analysis by different RAD members.
- Evidence: `party_position` cue `submits` at chunk `4609710` offsets `20-27`; context: [36] The Respondent submits that the RAD’s interpretation of s 110(4) is consistent with the Charter and that Charter values do not provide extra-legislative discretion to admit evidence that is clearly inadmissible under that provision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609710` offsets `178-186`; context: [36] The Respondent submits that the RAD’s interpretation of s 110(4) is consistent with the Charter and that Charter values do not provide extra-legislative discretion to admit evidence that is clearly inadmissible under that provision.
- Evidence: `governing_rule` cue `under` at chunk `4609710` offsets `216-221`; context: [36] The Respondent submits that the RAD’s interpretation of s 110(4) is consistent with the Charter and that Charter values do not provide extra-legislative discretion to admit evidence that is clearly inadmissible under that provision.
- Evidence: `reasoning_application` cue `because` at chunk `4609710` offsets `7845-7852`; context: While the Applicant relies on Elezi, that case is of little assistance because in addition to the evidence being of a different nature, the Court also found that the applicant could not reasonably have been expected in the circumstances to have presented that new evidence to the RPD (at paragraph 43).
- Evidence: `counterargument_limitation` cue `but` at chunk `4609710` offsets `510-513`; context: It is not an appeal de novo, but rather it conducts a mostly, or entirely, paper-based appeal of the RPD decision where it considers potential errors in the decision of the RPD that are raised by the appellant (Eng v Canada (Citizenship and Immigration), 2014 FC 711 at para 26; Spasoja v Canada (Citizenship and Immigration), 2014 FC 913 at paras 42-44; Dhillon v Canada (Citizenship and Immigration), 2015 FC 321 at para 18).
- Evidence: `disposition` cue `dismissed` at chunk `4609710` offsets `4077-4086`; context: Moreover, the fact that the Federal Court can review the RAD’s decision provides a further indication that the Applicant is afforded fundamental justice, and that the RAD is not required to conduct an appeal de novo of the RPD hearing (Chiarelli at para 41; Kourtessis v Minister of National Revenue, [1993] 2 SCR 53 at pp 69-70; Williams v Canada (Minister of Citizenship and Immigration), [1997] 2 FC 646 (CA) at pp 664-667; leave to appeal dismissed [1997] SCCA No 332 ; Luitjens v Canada (Secretary of State), [1992] FCJ No 319).
- Evidence: `evidence_fact` cue `evidence` at chunk `4609711` offsets `28-36`; context: [37] The restriction on new evidence is also consistent with the overall goal of the IRPA to establish fair and efficient procedures that maintain the integrity of the Canadian refugee protection system (IRPA, s 3(2)(e)) while upholding Canada’s respect for human rights and fundamental freedoms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609712` offsets `105-113`; context: [38] The RAD’s decision was also reasonable because the Applicant had the opportunity to present the new evidence for consideration in his refugee claim, as the documents were available at the time of his hearing.
- Evidence: `reasoning_application` cue `because` at chunk `4609712` offsets `44-51`; context: [38] The RAD’s decision was also reasonable because the Applicant had the opportunity to present the new evidence for consideration in his refugee claim, as the documents were available at the time of his hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609714` offsets `22-30`; context: [40] Finally, the new evidence is not evidence of a new risk allegation that was not considered by the RPD or evidence that is personal to the Applicant.
- Evidence: `reasoning_application` cue `conclude` at chunk `4609714` offsets `428-436`; context: It was not unreasonable for the RAD to conclude that the nature of this evidence did not warrant admitting it when considering the reasonableness of the Applicant’s explanation for not providing it earlier.

#### Section text

Deri v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-09-02
Neutral citation
2015 FC 1042
File numbers
IMM-7050-14
Notes
A correction was made on Febuary 1, 2016
Reported Decision
Decision Content
Date: 20150902
Docket: IMM-7050-14
Citation: 2015 FC 1042
Ottawa, Ontario, September 2, 2015
PRESENT: The Honourable Madam Justice Strickland
BETWEEN:
SAMUEL DERI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] This is an application for judicial review of a decision of the Refugee Appeal Division of the Immigration and Refugee Board of Canada (RAD), dated September 17, 2014, in which the RAD confirmed the finding of the Refugee Protection Division (RPD) that the Applicant is neither a Convention Refugee nor a person in need of protection pursuant to s 96 or s 97, respectively, of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].
Background [2] The Applicant is a citizen of Ghana. In September 2013, he fled to Canada and made a claim for refugee status. In his initial Basis of Claim (BOC) narrative he claimed that his father’s relatives threatened him with death after he declared that he would not accept the Chieftaincy of the Dagari tribe. On October 18, 2013, he submitted an addendum to his BOC narrative in which he explained that he is bisexual and that he worried that his sexual orientation would be discovered by his community in Ghana. In November 2013, the Applicant learned he was HIV positive and, at his first sitting of his hearing before the RPD on December 6, 2013, provided a physician’s letter confirming this. Prior to the second sitting of his hearing on January 16, 2014, the Applicant submitted a second addendum to his BOC narrative in which he explained that he feared persecution upon return to Ghana as a result of his HIV positive status because, after disclosing his status to his wife who is in Ghana, he had received death threats from her family.

[3] At the second sitting of his hearing, the Applicant explained to the RPD that he is actually a homosexual, and that he learned he had contracted HIV from his male partner, with whom he had been in a relationship for several years. In support of the Applicant’s claim of persecution based on his HIV status, his counsel submitted three articles about the stigma faced by Ghanaians who are HIV positive. On May 9, 2014, the RPD rendered its negative decision finding the Applicant to be neither a Convention refugee nor a person in need of protection.

[4] On appeal to the RAD, the Applicant focused his submissions on the risk of persecution he would face in Ghana as a result of his HIV positive status. His new counsel submitted a request to the RAD to consider four articles about stigma and HIV status in Ghana based on the Applicant’s view that there had been a lack of evidence before the RPD on this issue. His new counsel also made detailed submissions about why the RAD should accept the new evidence, pursuant to s 110(4) of the IRPA.

[5] The RAD refused to accept the new evidence finding that it did not meet the requirements of s 110(4). It rendered its negative decision on September 17, 2014 confirming the RPD’s decision.
The RPD’s Decision [6] The determinative issues before the RPD were the Applicant’s credibility, the well-foundedness of his fear of persecution, and the issue of discrimination versus persecution.

[7] On the issue of credibility, the RPD concluded that the Applicant did not provide credible evidence regarding his fear of persecution as a result of his refusal to accept the Chieftaincy. The RPD further found that the Applicant’s evidence was contrary to the objective documentary evidence which stated that a Chieftancy is not forced on anyone who does not aspire to take the position.

[8] With regard to the Applicant’s HIV positive status, the RPD accepted that the Applicant is a member of a particular social group, and that people with his status in Ghana “suffer a certain degree of social stigma”. However, based on the documentary evidence, the RPD concluded that while the Applicant may be subject to discrimination upon return to Ghana, that discrimination was not sufficiently persistent and punitive so as to amount to persecution under the IRPA.

[9] Finally, the RPD considered the Applicant’s claim that he also fears persecution as a result of his status as a homosexual man, and found the Applicant’s evidence on this issue not to be credible for a number of reasons, including the fact that he omitted this information from his initial BOC narrative. While the Applicant provided evidence of his email communications with his male partner in Ghana, the RPD found it implausible that this evidence did not include communications about the Applicant’s HIV positive status, especially since the Applicant testified that he had disclosed his status to his partner.

[10] The RPD also found that the Applicant was not credible overall and, for all these reasons, the Applicant’s claim was rejected.
Decision Under Review – RAD Decision [11] On appeal, the RAD first considered the admissibility of the new evidence pursuant to s 110(4) of the IRPA, which evidence was comprised of four articles concerning HIV related stigma and discrimination. The RAD found that the new evidence did not arise after the rejection of the Applicant’s claim, as each article was produced before the Applicant’s final sitting before the RPD on January 16, 2014, and after he discovered that he is HIV positive. In his affidavit before the RAD, the Applicant stated that he did not “know that [he] was supposed to gather this evidence as part of [his] RPD hearing” and that he “did not know why [his] counsel did not gather more of it”. However, the RAD rejected this explanation, noting that the Applicant was represented by experienced counsel who submitted some evidence regarding the treatment of HIV positive individuals in Ghana and made extensive submissions on the risks that the Applicant would face as an HIV positive person should he return to Ghana. Furthermore, the Applicant did not provide any evidence to suggest that his former counsel was incompetent in not disclosing further documentary evidence.

[12] In addition, the RAD found that the Applicant did not provide sufficient evidence to prove that the new evidence was not reasonably available, or that he could not reasonably have been expected in the circumstances to have presented the new evidence at the time of the rejection of his claim by the RPD.

[13] Therefore, the RAD concluded that:

[18] The RAD finds that it is bound by s 110(4) of the IRPA, and is not bound by jurisprudence which related to the admissibility of new evidence in Pre-Removal Risk Assessment (PRRA) applications, and therefore the RAD does not have discretion to accept evidence that is not covered by s 110(4).

[14] Relying on this Court’s decision in Huruglica v Canada (Citizenship and Immigration), 2014 FC 799 [Huruglica], the RAD noted that its task was to conduct an independent assessment of the Applicant’s claim by reviewing the totality of the evidence which was presented at the time of the rejection. As such, the RAD refused to engage in its own independent research, which was suggested by the Applicant’s new counsel in his submissions, and instead limited its analysis to the evidence that was before the RPD at the time of the rejection. Finally, the RAD noted that it would not consider any of counsel’s submissions that related to the new evidence, or any evidence that was not before the RPD, such as the most recent versions of the Immigration and Refugee Board of Canada’s National Documentation Package (NDP), including the most recent United States Department of State report (US DOS Report).

[15] Turning to the RPD’s decision, the RAD first conducted an independent assessment of the RPD’s credibility findings, despite the fact that the Applicant did not challenge any of these findings on appeal. After reviewing the evidence on the record, the RAD concurred with the RPD’s finding that the Applicant’s allegations were not credible and that he was not a credible witness. The RAD concluded, after a consideration of the totality of the evidence, that it was left with the fact that the Applicant is a heterosexual man from Ghana who was diagnosed with HIV after his arrival in Canada.

[16] The RAD then considered the evidence relating to the Applicant’s sur place claim, based on his status as a person who is HIV positive, and considered whether he would face a serious possibility of persecution as a result of that status. In doing so, the RAD reviewed the evidence that was before the RPD. Having done so, it concluded that the Applicant did not provide sufficient credible or trustworthy evidence to persuade it that the treatment he would face would rise to the level of persecution. Moreover, the RAD concluded that the Applicant had not provided sufficient credible or trustworthy evidence that he would be perceived as sexually immoral or to be a homosexual because of his HIV positive status. Even if that was the case, the Applicant had also failed to provide sufficient credible or trustworthy evidence that the stigma he might face would rise to the level of persecution and would result in a denial of a core human right.

[17] As a result, the RAD confirmed the RPD’s determination that the Applicant is neither a Convention refugee nor a person in need of protection, pursuant to s 111(1)(a) of the IRPA. Therefore, the appeal was dismissed.
Issues [18] In my view, the issues can be framed as follows:
Did the RAD err in interpreting s 110(4) by finding that it did not have the discretion to admit new evidence that was otherwise technically inadmissible and, therefore, fail to consider Charter values in refusing to admit the new evidence?
2. Did the RAD err in applying s 110(4) when it refused to consider updated documents in the NDP?
3. Did the RAD unreasonably conclude that the evidence regarding discrimination against HIV positive individuals in Ghana did not amount to persecution?
Standard of Review [19] As to the first issue, the Applicant submits that the RAD’s interpretation of s 110(4) is a pure question of law that gives rise to issues under the Canadian Charter of Rights and Freedoms, Part I of the Constitution Act, 1982, being Schedule B to the Canada Act 1982 (UK), 1982, c 11 [Charter] and, as such, should be reviewed on the correctness standard (Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir]). Like the standard of review issues raised in Huruglica, the test to apply under this provision is also a “legal question well beyond the scope of the RAD’s expertise, even though it depends on the interpretation of the IRPA, the RAD’s home statute” (Huruglica at para 30).

[20] The Applicant also submits that review on a correctness standard is important to ensure judicial consistency. Allowing every RAD member to apply their own test when assessing new evidence creates the absurd situation in which the application of the law changes in accordance with each member, rather than the evidence provided. This point was recognized by the Federal Court of Appeal in Raza v Canada (Citizenship and Immigration), 2007 FCA 385 [Raza], where it developed a legal test for assessing the admissibility of new evidence on a Pre-Removal Risk Assessment [PRRA] application, pursuant to s 113(a) of the IRPA, that would apply to all PRRA applications.

[21] The Respondent, on the other hand, submits that the RAD’s interpretation of s 110(4) is squarely within its own expertise and does not involve a question of central importance to the legal system as a whole or any other special circumstances that would require review on a correctness standard. Thus, the reasonableness standard should apply to this issue (Saskatchewan Human Rights Commission v Whatcott, 2013 SCC 11 at para 167; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Assn, 2011 SCC 61 at paras 45-46; McLean v British Columbia, 2013 SCC 67 at paras 26, 30; Singh v Canada (Citizenship and Immigration), 2014 FC 1022 at para 42 [Singh]).

[22] Further, when Charter values are applied to an individual administrative decision, they are applied in relation to a particular set of facts and, therefore, a deferential standard of review is to be applied (Doré v Barreau du Quebec, 2012 SCC 12 at paras 35-36, 52-58 [Doré]).

[23] I agree with the Respondent’s submissions. In the recent decision of Singh (currently under appeal, see: A-512-14), Madam Justice Gagné reviewed the same cases cited by the Respondent above and, based on those cases, she concluded:

[42] Therefore, I am of the view that both the RAD's interpretation of subsection 110(4) of the Act (as a question of law that is not of general importance to the legal system as a whole and outside the expertise of the RAD) and its application to the facts of this case (as a question of mixed fact and law) are to be reviewed on the reasonableness standard.

[24] In the interests of judicial comity, I will therefore review the RAD’s determination that
s 110(4) did not provide it with discretion to admit the new evidence on the reasonableness standard.

[25] As to the second issue, the RAD’s application of s 110(4) is a question of mixed fact and law that is reviewable on the reasonableness standard (Singh at para 42; Iyamuremye v Canada (Citizenship and Immigration), 2014 FC 494 at para 43).

[26] As to the third issue, the RAD’s assessment of the documentary evidence that was before the RPD involves findings of fact that are subject to deference and thus reviewable on the reasonableness standard (Dunsmuir at para 51). As a result, this Court will not intervene as long as the RAD’s assessment is justified, transparent and intelligible, and “falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at para 47).
Issue 1: Did the RAD err in interpreting s 110(4) by finding that it did not have the discretion to admit new evidence that was otherwise technically inadmissible and, therefore, fail to consider Charter values in refusing to admit the new evidence? A. Applicant’s Position [27] The Applicant submits that this matter concerns the factors the RAD must consider when applying the new evidence rule set out in s 110(4) of the IRPA. More specifically, how the RAD should consider its Charter jurisdiction when new evidence is raised that may not be technically admissible but does raise serious evidence of risk that challenges the core findings of the RPD’s decision.

[28] The Applicant submits that the Raza test is not appropriate in the RAD context and, instead, proposes a new test derived from the Supreme Court of Canada’s decision in Doré in which the RAD’s Charter considerations are implicit in its s 110(4) assessment. In this proposed new test, where fresh evidence is submitted that is not technically admissible, the RAD should consider whether that evidence contradicts a specific finding of the RPD and, if allowed, could lead the RAD to a different conclusion on a central aspect of the claim. If it could, then the RAD has an obligation to conduct a proportionality exercise in which it balances the severity of the interference of the Charter protection with the statutory objective. Failure to conduct this assessment, or consider the Charter values in applying s 110(4), is an error of law.

[29] In support of this position, which broadens the RAD’s jurisdiction under s 110(4) to include the discretion to admit new evidence that is technically inadmissible, the Applicant relies on the following arguments.
a) Inconsistent Application at the RAD - The Applicant submits that there are currently three different interpretations by the RAD of its jurisdiction under s 110(4). The first is a strict statutory interpretation, as was applied by the RAD in this case. Under this approach, the factors discussed in Raza and the related jurisprudence regarding PRRA applications do not apply to s 110(4).
The second approach involves the application of the Raza test, which was developed for determining whether evidence is admissible under s 113(a) of the IRPA, a nearly identical provision that applies in the context of a PRRA (for example: X (RE), 2014 CanLII 55520 (CA IRB); X(RE), 2014 CanLII 60409 (CA IRB)). The Applicant submits that a strict application of the Raza test does not fully contemplate the distinct differences between the purposes of a PRRA as opposed to the de novo appeal set out in the RAD. For example, the test fails to account for situations, like the present case, where the evidence may have been available at the time of the RPD hearing, but nevertheless raises a serious issue of risk. However, Raza is useful for establishing that along with express statutory restrictions, there are a number of additional considerations that arise from “necessary implication”, and thus must be considered (Raza at para 14). In the context of the RAD, a factor that arises by “necessary implication” is whether s 110(4) is being read in a manner that is consistent with the RAD’s Charter obligations.
Finally, the Applicant notes that other members of the RAD have adopted a broader interpretation of s 110(4) that acknowledges the fact that the purposes underlying the RAD differ from those that inform the decision of a PRRA officer (for example, in X (Re), 2014 CanLII 33085 (CA IRB) at paras 17-21).
The Applicant submits that these variances in the interpretation of s 110(4) are troubling because they create serious inconsistencies amongst RAD members’ decisions. As such, this case raises an opportunity to clarify the test for the admissibility of new evidence that should be applied by the RAD.
b) Purpose of the RAD - The Applicant also submits that in Singh, the RAD applied the criteria in Raza in determining that the new evidence submitted by the Applicant was not admissible. However, Justice Gagné held that it was unreasonable for the RAD to strictly apply the Raza factors in interpreting s 110(4) without appreciating that its role is quite different from that of a PRRA officer. She also emphasized that the RAD, unlike a PRRA officer, is a quasi-judicial administrative tribunal that has the power, pursuant to s 111(1)(b) of the IRPA, to set aside the RPD’s decision and substitute a determination that it, in its opinion, should have been made. Further, she noted that the underlying rationale for s 113(a) of the IRPA is not appellate in nature, but rather to assure the claimant has a last chance to have any new risks of refoulement, not previously assessed by the RPD, assessed before removal can take place (para 50). By contrast, the RAD considers this evidence in an appellate review of the correctness of the RPD’s determination. A restrictive interpretation of s 110(4) would limit the ability of a claimant to get a ‘full fact-based appeal’. Accordingly, the criteria for the admissibility of evidence must be sufficiently flexible to ensure it can occur.
Relying on these findings in Singh, the Applicant submits that the fact that the RAD is a de novo hearing, with broad remedial powers, and is often the last assessment of risk prior to removal, are all important indicators that the RAD must also ensure that the Applicant’s s 7 Charter rights, which are an inherent part of the refugee process, are upheld in the exercise of its discretion to admit new evidence under s 110(4).
c) Implicit considerations: Parallel Charter and Legislative Jurisdictions - The Applicant submits that in addition to the discretion granted by statute, the RAD also carries inherent Charter jurisdiction because it is a critical part of the entire refugee process, which was specifically implemented to protect s 7 Charter interests. Moreover, ss 3(3)(d) and (f) of the IRPA require that all clauses in the IRPA must be construed and applied in a man

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 12178:2 · paragraphs 37-37

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9dabb19852762c6071f717a8fcd70b200af7676887e4f206a323434d14949c6d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12178:2:subtheme:1 · paragraphs 37-37

- Raw key terms: `abella, adjudicated, adjudicator, administrative, analysis, applicant, asserted, balancing`
- Display key terms: `abella, adjudicated, adjudicator, administrative, analysis, asserted, balancing`
- Argument roles: `governing_rule, issue, party_position`
- Explanation: Observed roles: governing_rule, issue, party_position Display terms: abella, adjudicated, adjudicator, administrative, analysis, asserted, balancing Position/evidence statements: [41] For all these reasons, the Respondent submits that the RAD’s decision represents a reasonable and proportionate balancing of the Charter values and statutory objectives at issue. Rule/authority context: There, the Supreme Court faced a challenge to the constitutionality of a decision of a disciplinary body, which asserted that the decision violated the applicant’s freedom of expression under the Charter. Evidence spans paragraphs 37-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609715` offsets `177-182`; context: [41] For all these reasons, the Respondent submits that the RAD’s decision represents a reasonable and proportionate balancing of the Charter values and statutory objectives at issue.
- Evidence: `party_position` cue `submits` at chunk `4609715` offsets `43-50`; context: [41] For all these reasons, the Respondent submits that the RAD’s decision represents a reasonable and proportionate balancing of the Charter values and statutory objectives at issue.
- Evidence: `governing_rule` cue `under` at chunk `4609715` offsets `485-490`; context: There, the Supreme Court faced a challenge to the constitutionality of a decision of a disciplinary body, which asserted that the decision violated the applicant’s freedom of expression under the Charter.

#### Section text

[41] For all these reasons, the Respondent submits that the RAD’s decision represents a reasonable and proportionate balancing of the Charter values and statutory objectives at issue.
Analysis [42] The Applicant’s position is, in essence, centered on the Supreme Court of Canada’s decision in Doré. There, the Supreme Court faced a challenge to the constitutionality of a decision of a disciplinary body, which asserted that the decision violated the applicant’s freedom of expression under the Charter. This raised the question of how to protect Charter guarantees and the values they reflect in the context of adjudicated administrative decisions. The Court stated that normally, if a discretionary administrative decision is made by an adjudicator within his or her mandate, the decision is judicially reviewed for its reasonableness. The question was whether the presence of a Charter issue called for the replacement of that administrative framework with the test described in R v Oakes, [1986] 1 SCR 103 [Oakes] that is traditionally used to determine whether the state has justified a law’s violation of the Charter as a “reasonable limit” under s 1 (Doré at paras 2-3). Justice Abella stated that it was clear that in exercising their discretion, administrative decision-makers must act consistently with the values underlying the grant of discretion, including Charter values (at para 24).

## 12178:3 · paragraphs 38-44

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `291f2283e21a4ec0b087b6c2ef828af805215ccef164a5b62fdbc6f4cc974205`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12178:3:subtheme:1 · paragraphs 38-43

- Raw key terms: `administrative, charter, court, values, approach, decisions, compliance, conception`
- Display key terms: `administrative, charter, values, approach, decisions, compliance, conception`
- Argument roles: `governing_rule, reasoning_application`
- Explanation: Observed roles: governing_rule, reasoning_application Display terms: administrative, charter, values, approach, decisions, compliance, conception Rule/authority context: [35] The alternative is for the Court to embrace a richer conception of administrative law, under which discretion is exercised “in light of constitutional guarantees and the values they reflect” (Multani, at para. | When a particular “law” is being assessed for Charter compliance, on the other hand, we are dealing with principles of general application. Application context: When Charter values are applied to an individual administrative decision, they are being applied in relation to a particular set of facts. | [45] In order to consider Charter values, the Supreme Court set out the following framework for decision-makers to apply in exercising their statutory discretion: Evidence spans paragraphs 38-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4609718` offsets `92-97`; context: [35] The alternative is for the Court to embrace a richer conception of administrative law, under which discretion is exercised “in light of constitutional guarantees and the values they reflect” (Multani, at para.
- Evidence: `governing_rule` cue `principles` at chunk `4609719` offsets `784-794`; context: When a particular “law” is being assessed for Charter compliance, on the other hand, we are dealing with principles of general application.
- Evidence: `reasoning_application` cue `applied` at chunk `4609719` offsets `391-398`; context: When Charter values are applied to an individual administrative decision, they are being applied in relation to a particular set of facts.
- Evidence: `governing_rule` cue `under` at chunk `4609720` offsets `268-273`; context: [44] By adopting the second approach and concluding that such decisions should be reviewed on the reasonableness standard, the Supreme Court acknowledged the importance of an administrative decision-maker’s expertise when it comes to exercising “a discretionary power under his or her home statute” (at paras 45 and 47).
- Evidence: `reasoning_application` cue `apply` at chunk `4609721` offsets `115-120`; context: [45] In order to consider Charter values, the Supreme Court set out the following framework for decision-makers to apply in exercising their statutory discretion:

#### 12178:3:subtheme:2 · paragraphs 44-44

- Raw key terms: `administrative, apply, assessment, balances, balancing, canada, charter, consider`
- Display key terms: `administrative, apply, assessment, balances, balancing, charter, consider`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: administrative, apply, assessment, balances, balancing, charter, consider Rule/authority context: In Lake, for instance, the importance of Canada’s international obligations, its relationships with foreign governments, and the investigation, prosecution and suppression of international crime justified the prima facie Application context: [55] How then does an administrative decision-maker apply Charter values in the exercise of statutory discretion? Evidence spans paragraphs 44-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609722` offsets `646-653`; context: In Pinet, the twin goals of public safety and fair treatment grounded the assessment of whether an infringement of an individual’s liberty interest was justified (para.
- Evidence: `governing_rule` cue `under` at chunk `4609722` offsets `532-537`; context: In Lake, for instance, the importance of Canada’s international obligations, its relationships with foreign governments, and the investigation, prosecution and suppression of international crime justified the prima facie infringement of mobility rights under s.
- Evidence: `reasoning_application` cue `apply` at chunk `4609722` offsets `52-57`; context: [55] How then does an administrative decision-maker apply Charter values in the exercise of statutory discretion?

#### Section text

[43] In considering these two approaches Justice Abella stated that:

[34] …Today, the Court has two options for reviewing discretionary administrative decisions that implicate Charter values. The first is to adopt the Oakes framework, developed for reviewing laws for compliance with the Constitution. This undoubtedly protects Charter rights, but it does so at the risk of undermining a more robust conception of administrative law. In the words of Prof. Evans, if administrative law is bypassed for the Charter, “a rich source of thought and experience about law and government will be overlooked”.

[35] The alternative is for the Court to embrace a richer conception of administrative law, under which discretion is exercised “in light of constitutional guarantees and the values they reflect” (Multani, at para. 152, per LeBel J.). Under this approach, it is unnecessary to retreat to a s. 1 Oakes analysis in order to protect Charter values. Rather, administrative decisions are always required to consider fundamental values. The Charter simply acts as “a reminder that some values are clearly fundamental and . . . cannot be violated lightly” (Cartier, at p. 86). The administrative law approach also recognizes the legitimacy that this Court has given to administrative decision-making in cases such as Dunsmuir and Conway. These cases emphasize that administrative bodies are empowered, and indeed required, to consider Charter values within their scope of expertise. Integrating Charter values into the administrative approach, and recognizing the expertise of these decision-makers, opens “an institutional dialogue about the appropriate use and control of discretion, rather than the older command-and-control relationship” (Liston, at p. 100).

[36] As explained by Chief Justice McLachlin in Alberta v. Hutterian Brethren of Wilson Colony, 2009 SCC 37, [2009] 2 S.C.R. 567, the approach used when reviewing the constitutionality of a law should be distinguished from the approach used for reviewing an administrative decision that is said to violate the rights of a particular individual (see also Bernatchez). When Charter values are applied to an individual administrative decision, they are being applied in relation to a particular set of facts. Dunsmuir tells us this should attract deference (para. 53; see also Suresh v. Canada (Minister of Citizenship and Immigration), 2002 SCC 1, [2002] 1 S.C.R. 3, at para. 39). When a particular “law” is being assessed for Charter compliance, on the other hand, we are dealing with principles of general application.

[44] By adopting the second approach and concluding that such decisions should be reviewed on the reasonableness standard, the Supreme Court acknowledged the importance of an administrative decision-maker’s expertise when it comes to exercising “a discretionary power under his or her home statute” (at paras 45 and 47).

[45] In order to consider Charter values, the Supreme Court set out the following framework for decision-makers to apply in exercising their statutory discretion:

[55] How then does an administrative decision-maker apply Charter values in the exercise of statutory discretion? He or she balances the Charter values with the statutory objectives. In effecting this balancing, the decision-maker should first consider the statutory objectives. In Lake, for instance, the importance of Canada’s international obligations, its relationships with foreign governments, and the investigation, prosecution and suppression of international crime justified the prima facie infringement of mobility rights under s. 6(1) (para. 27). In Pinet, the twin goals of public safety and fair treatment grounded the assessment of whether an infringement of an individual’s liberty interest was justified (para. 19).

## 12178:4 · paragraphs 45-89

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `898daab2af5849a342ae0b9d06afd39ee18c286eb19788fa0bffb8d5959a4bdc`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12178:4:subtheme:1 · paragraphs 45-47

- Raw key terms: `charter, decision, decision-maker, discretion, acceptable, accord, accordance, administrative`
- Display key terms: `charter, decision-maker, discretion, acceptable, accord, accordance, administrative`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: charter, decision-maker, discretion, acceptable, accord, accordance, administrative Position/evidence statements: [47] In the present case, the Applicant submits that the RAD has the discretion to admit evidence that is otherwise “technically inadmissible” as a result of its obligation to interpret the law in accordance with the Cha Rule/authority context: [47] In the present case, the Applicant submits that the RAD has the discretion to admit evidence that is otherwise “technically inadmissible” as a result of its obligation to interpret the law in accordance with the Cha Application context: This is where the role of judicial review for reasonableness aligns with the one applied in the Oakes context. Evidence spans paragraphs 45-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609723` offsets `65-70`; context: [56] Then the decision-maker should ask how the Charter value at issue will best be protected in view of the statutory objectives.
- Evidence: `reasoning_application` cue `applied` at chunk `4609723` offsets `398-405`; context: This is where the role of judicial review for reasonableness aligns with the one applied in the Oakes context.
- Evidence: `issue` cue `whether` at chunk `4609724` offsets `141-148`; context: [46] Significantly, for the purposes of this matter, Doré makes it clear that the trigger for the consideration of Charter values depends on whether the decision-maker is exercising discretion in reaching his or her decision.
- Evidence: `party_position` cue `submits` at chunk `4609725` offsets `40-47`; context: [47] In the present case, the Applicant submits that the RAD has the discretion to admit evidence that is otherwise “technically inadmissible” as a result of its obligation to interpret the law in accordance with the Charter, pursuant to s 3(3)(d) of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609725` offsets `89-97`; context: [47] In the present case, the Applicant submits that the RAD has the discretion to admit evidence that is otherwise “technically inadmissible” as a result of its obligation to interpret the law in accordance with the Charter, pursuant to s 3(3)(d) of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4609725` offsets `226-237`; context: [47] In the present case, the Applicant submits that the RAD has the discretion to admit evidence that is otherwise “technically inadmissible” as a result of its obligation to interpret the law in accordance with the Charter, pursuant to s 3(3)(d) of the IRPA.

#### 12178:4:subtheme:2 · paragraphs 48-51

- Raw key terms: `statutory, canada, construction, evidence, irpa, matter, principle, question`
- Display key terms: `statutory, construction, irpa, matter, principle, question`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: statutory, construction, irpa, matter, principle, question Rule/authority context: 1) Unless a hearing is held under subsection (6), the Refugee Appeal Division must make a decision within the time limits set out in the regulations. Application context: [48] Therefore, in my view, this matter appears to turn on the question of whether the RAD has discretion to admit new evidence that does not meet the statutory conditions in s 110(4). Evidence spans paragraphs 48-51. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4609726` offsets `63-71`; context: [48] Therefore, in my view, this matter appears to turn on the question of whether the RAD has discretion to admit new evidence that does not meet the statutory conditions in s 110(4).
- Evidence: `evidence_fact` cue `evidence` at chunk `4609726` offsets `119-127`; context: [48] Therefore, in my view, this matter appears to turn on the question of whether the RAD has discretion to admit new evidence that does not meet the statutory conditions in s 110(4).
- Evidence: `reasoning_application` cue `Therefore` at chunk `4609726` offsets `5-14`; context: [48] Therefore, in my view, this matter appears to turn on the question of whether the RAD has discretion to admit new evidence that does not meet the statutory conditions in s 110(4).
- Evidence: `counterargument_limitation` cue `However` at chunk `4609726` offsets `356-363`; context: However, if it does not have discretion to admit new evidence that does not meet the requirements of s 110(4), then the analysis ends there.
- Evidence: `issue` cue `issue` at chunk `4609727` offsets `2386-2391`; context: […]
[…]
(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
- Evidence: `evidence_fact` cue `record` at chunk `4609727` offsets `203-209`; context: 1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
- Evidence: `governing_rule` cue `under` at chunk `4609727` offsets `1225-1230`; context: 1) Unless a hearing is held under subsection (6), the Refugee Appeal Division must make a decision within the time limits set out in the regulations.

#### 12178:4:subtheme:3 · paragraphs 52-55

- Raw key terms: `admit, conditions, context, evidence, factors, consideration, discretion, explicit`
- Display key terms: `admit, conditions, context, factors, consideration, discretion, explicit`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: admit, conditions, context, factors, consideration, discretion, explicit Position/evidence statements: The Respondent argues that the same reasoning should apply to the interpretation of s 110(4); thus, if the statutory conditions have not been met, the RAD does not have discretion to admit the evidence. Rule/authority context: [52] The Respondent suggests that the jurisprudence in the PRRA context is applicable when interpreting s 110(4). Application context: The Respondent argues that the same reasoning should apply to the interpretation of s 110(4); thus, if the statutory conditions have not been met, the RAD does not have discretion to admit the evidence. Evidence spans paragraphs 52-55. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609730` offsets `1004-1011`; context: Section 110(6) permits the RAD to hold a hearing if it is of the opinion that there is new documentary evidence, as referenced in s 110(3), that meets the requirements of s 110(4), in which case the RAD will then consider whether that evidence raises serious credibility issues, is central to the claim and, if accepted, it would justify allowing or rejecting the claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609730` offsets `168-176`; context: [51] Based on the grammatical and ordinary sense of the language in s 110(4), in my view, the RAD reasonably concluded that it did not have the discretion to admit new evidence that it found did not meet one of the explicit conditions set out in that provision.
- Evidence: `party_position` cue `argues` at chunk `4609731` offsets `318-324`; context: The Respondent argues that the same reasoning should apply to the interpretation of s 110(4); thus, if the statutory conditions have not been met, the RAD does not have discretion to admit the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609731` offsets `198-206`; context: In that regard, the Raza test does not expand a PRRA officer’s ability to admit new evidence, as its factors only come into play if the officer finds that the statutory conditions are met.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4609731` offsets `38-51`; context: [52] The Respondent suggests that the jurisprudence in the PRRA context is applicable when interpreting s 110(4).
- Evidence: `reasoning_application` cue `apply` at chunk `4609731` offsets `356-361`; context: The Respondent argues that the same reasoning should apply to the interpretation of s 110(4); thus, if the statutory conditions have not been met, the RAD does not have discretion to admit the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609732` offsets `110-118`; context: [53] I am inclined to agree with the Respondent that the test in Raza does not permit a PRRA officer to admit evidence that does not meet the explicit statutory conditions for new evidence found in s 113(a) of the IRPA.

#### 12178:4:subtheme:4 · paragraphs 56-57

- Raw key terms: `evidence, first, three, added, admit, although, applicant, approach`
- Display key terms: `first, three, added, admit, although, approach`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: first, three, added, admit, although, approach Rule/authority context: Moreover, one must be careful not to mix up the issue of whether evidence is new evidence under subsection 133(a) with the issue of whether the evidence establishes risk. Evidence spans paragraphs 56-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609734` offsets `209-214`; context: Moreover, one must be careful not to mix up the issue of whether evidence is new evidence under subsection 133(a) with the issue of whether the evidence establishes risk.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609734` offsets `55-63`; context: [17] Although the PRRA process is meant to assess only evidence of new risks, this does not mean that new evidence relating to old risks need not be considered.
- Evidence: `governing_rule` cue `under` at chunk `4609734` offsets `251-256`; context: Moreover, one must be careful not to mix up the issue of whether evidence is new evidence under subsection 133(a) with the issue of whether the evidence establishes risk.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609735` offsets `197-205`; context: The RAD must first determine if the three explicit conditions set out in s 110(4) have been met: 1) did the evidence arise after the rejection of their claim?

#### 12178:4:subtheme:5 · paragraphs 58-61

- Raw key terms: `statutory, applicable, court, decision, discretionary, case, charter, discretion`
- Display key terms: `statutory, applicable, discretionary, case, charter, discretion`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: statutory, applicable, discretionary, case, charter, discretion Rule/authority context: [4] Under Doré, where a discretionary administrative decision engages the protections enumerated in the Charter — both the Charter’s guarantees and the foundational values they reflect — the discretionary decision-maker  Application context: However, in this case the RAD did not apply the implicit Raza factors. Evidence spans paragraphs 58-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4609736` offsets `9-17`; context: [56] The question of whether the Raza criteria are applicable to s 110(4) is currently unsettled (see, for example, Singh and Denbel v Canada (Citizenship and Immigration), 2015 FC 629 at paras 40-44).
- Evidence: `evidence_fact` cue `found that` at chunk `4609736` offsets `284-294`; context: Rather, it found that it did not have discretion to accept evidence that did not fall within s 110(4).
- Evidence: `reasoning_application` cue `apply` at chunk `4609736` offsets `240-245`; context: However, in this case the RAD did not apply the implicit Raza factors.
- Evidence: `counterargument_limitation` cue `However` at chunk `4609736` offsets `202-209`; context: However, in this case the RAD did not apply the implicit Raza factors.
- Evidence: `issue` cue `question` at chunk `4609737` offsets `22-30`; context: [57] Returning to the question of the discretionary nature of the RAD’s decision, I would also note that this is not a situation such as Loyola High School where the source of the discretion at issue was clear as it arose from the Minister’s refusal to grant an exemption to a regulatory requirement.
- Evidence: `governing_rule` cue `Under` at chunk `4609738` offsets `4-9`; context: [4] Under Doré, where a discretionary administrative decision engages the protections enumerated in the Charter — both the Charter’s guarantees and the foundational values they reflect — the discretionary decision-maker is required to proportionately balance the Charter protections to ensure that they are limited no more than is necessary given the applicable statutory objectives that she or he is obliged to pursue.

#### 12178:4:subtheme:6 · paragraphs 62-63

- Raw key terms: `alternative, baker, balance, based, boundaries, canada, catholic, choice`
- Display key terms: `alternative, baker, balance, based, boundaries, catholic, choice`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: alternative, baker, balance, based, boundaries, catholic, choice Evidence spans paragraphs 62-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609740` offsets `12-19`; context: [32] […] on whether it reflected a proportionate balance between the statutory mandate to grant exemptions only when a proposed alternative program is “equivalent” to the prescribed curriculum, based on the ERC Program’s goals of promoting tolerance and respect for difference, and the religious freedom of the members of the Loyola community who seek to offer and wish to receive a Catholic education.

#### 12178:4:subtheme:7 · paragraphs 64-65

- Raw key terms: `admissibility, applicant, decision, evidence, expected, presented, reasonably, abide`
- Display key terms: `admissibility, expected, presented, reasonably, abide`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: admissibility, expected, presented, reasonably, abide Rule/authority context: However, as noted by the Respondent, in Elezi, Justice de Montigny actually found that the officer’s decision not to admit the applicant’s new evidence under s 113(a) was unreasonable because it was either created after  Application context: [60] By contrast, s 110(4) offers the RAD no discretion to refuse to apply its explicit admissibility requirements for new evidence. | However, as noted by the Respondent, in Elezi, Justice de Montigny actually found that the officer’s decision not to admit the applicant’s new evidence under s 113(a) was unreasonable because it was either created after  Evidence spans paragraphs 64-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609742` offsets `455-462`; context: While there is an element of subjectivity in assessing whether the evidence was reasonably available or if an applicant could not reasonably have been expected to have previously presented it, this is a factual assessment, it does not alter the character of the ultimate decision as to admissibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609742` offsets `123-131`; context: [60] By contrast, s 110(4) offers the RAD no discretion to refuse to apply its explicit admissibility requirements for new evidence.
- Evidence: `reasoning_application` cue `apply` at chunk `4609742` offsets `69-74`; context: [60] By contrast, s 110(4) offers the RAD no discretion to refuse to apply its explicit admissibility requirements for new evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609743` offsets `427-435`; context: There, Justice de Montigny (then of this Court) commented that if Canada is to respect its international obligations and abide by the Charter, “it cannot disregard credible evidence that a person would be at risk if sent back to his or her country of origin on the sole basis that this evidence is technically inadmissible” (at para 45).
- Evidence: `governing_rule` cue `under` at chunk `4609743` offsets `744-749`; context: However, as noted by the Respondent, in Elezi, Justice de Montigny actually found that the officer’s decision not to admit the applicant’s new evidence under s 113(a) was unreasonable because it was either created after the RPD’s decision, or the applicant could not reasonably have been expected in the circumstances to have presented the evidence to the RPD (at paras 39 and 43).
- Evidence: `reasoning_application` cue `because` at chunk `4609743` offsets `776-783`; context: However, as noted by the Respondent, in Elezi, Justice de Montigny actually found that the officer’s decision not to admit the applicant’s new evidence under s 113(a) was unreasonable because it was either created after the RPD’s decision, or the applicant could not reasonably have been expected in the circumstances to have presented the evidence to the RPD (at paras 39 and 43).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4609743` offsets `401-407`; context: There, Justice de Montigny (then of this Court) commented that if Canada is to respect its international obligations and abide by the Charter, “it cannot disregard credible evidence that a person would be at risk if sent back to his or her country of origin on the sole basis that this evidence is technically inadmissible” (at para 45).

#### 12178:4:subtheme:8 · paragraphs 66-68

- Raw key terms: `consider, evidence, sanchez, appears, applicant, basis, condition, country`
- Display key terms: `consider, sanchez, appears, basis, condition, country`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: consider, sanchez, appears, basis, condition, country Rule/authority context: There the PRRA officer excluded a country condition document pursuant to s 113(a) of the IRPA on the basis that it was published prior to the date of his hearing and the applicant or his counsel could have located and pr Application context: As a result, I am not convinced that this case is of assistance to the Applicant because his explanation for not providing the country condition documents was not accepted by the RAD, and he has not challenged the reason Evidence spans paragraphs 66-68. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609744` offsets `1439-1444`; context: For this and other reasons, the applicant had demonstrated that there was a serious issue to be tried and a stay was warranted.
- Evidence: `evidence_fact` cue `found that` at chunk `4609744` offsets `334-344`; context: Justice Shore found that the mere fact that the report was published prior to the hearing did not mean that it was obvious or easily accessible to the applicant.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4609744` offsets `130-141`; context: There the PRRA officer excluded a country condition document pursuant to s 113(a) of the IRPA on the basis that it was published prior to the date of his hearing and the applicant or his counsel could have located and presented it at the RPD hearing.
- Evidence: `counterargument_limitation` cue `but` at chunk `4609744` offsets `1004-1007`; context: On my reading of the decision, this conclusion appears to be based on Justice Shore’s comment that a PRRA officer is not limited to considering evidence submitted by the applicant, but has an obligation to conduct sufficient independent research in order to come to a proper determination.
- Evidence: `issue` cue `issue` at chunk `4609745` offsets `697-702`; context: Further, the reports which he sought to submit as new evidence addressed an issue upon which evidence had been tendered and considered by the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609745` offsets `675-683`; context: Further, the reports which he sought to submit as new evidence addressed an issue upon which evidence had been tendered and considered by the RPD.
- Evidence: `reasoning_application` cue `because` at chunk `4609745` offsets `456-463`; context: As a result, I am not convinced that this case is of assistance to the Applicant because his explanation for not providing the country condition documents was not accepted by the RAD, and he has not challenged the reasonableness of that finding.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609746` offsets `95-103`; context: [64] Thus, Elezi and Sanchez do not support a view that the RAD has discretion to consider new evidence that did not meet any of the three explicit criteria set out in s 110(4) nor that that legislative provision is, in these circumstances, overridden by Charter interests.

#### 12178:4:subtheme:9 · paragraphs 69-70

- Raw key terms: `applicant, evidence, found, reasonably, above, absence, accept, added`
- Display key terms: `reasonably, above, absence, accept, added`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: reasonably, above, absence, accept, added Application context: And, even if applied, those factors would only serve to narrow the admissibility of new evidence that meets the explicit conditions. Evidence spans paragraphs 69-70. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609747` offsets `892-897`; context: Further, the RAD did not accept the Applicant’s explanation that he was unaware that he needed to gather information related to this issue given that both he and his counsel had provided evidence on that very issue.
- Evidence: `evidence_fact` cue `found that` at chunk `4609747` offsets `27-37`; context: [65] In this case, the RAD found that the four new documents were all produced before the Applicant’s second sitting before the RPD, after he learned that he was HIV positive and after he added that ground to his refugee claim.
- Evidence: `evidence_fact` cue `found that` at chunk `4609748` offsets `23-33`; context: [66] In short, the RAD found that the Applicant failed to meet the explicit statutory requirements of s 110(4).
- Evidence: `reasoning_application` cue `applied` at chunk `4609748` offsets `404-411`; context: And, even if applied, those factors would only serve to narrow the admissibility of new evidence that meets the explicit conditions.

#### 12178:4:subtheme:10 · paragraphs 71-72

- Raw key terms: `applicant, circumstances, counsel, evidence, expected, former, found, presented`
- Display key terms: `circumstances, expected, former, presented`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: circumstances, expected, former, presented Rule/authority context: [68] And while I acknowledge that in Singh, Justice Gagné found that it was unreasonable to require the applicant to file a complaint of incompetency against his counsel, by way of comparison I would note that this Court Evidence spans paragraphs 71-72. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609749` offsets `764-769`; context: The Applicant and his former counsel were aware of the issue and did submit documentary evidence addressing the manner in which HIV positive people are treated in Ghana.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609749` offsets `88-96`; context: [67] In that regard, I am also of the view that the RAD’s decision not to admit the new evidence was reasonable.
- Evidence: `counterargument_limitation` cue `but` at chunk `4609749` offsets `935-938`; context: The new evidence is also not personal to the Applicant, but is comprised of further country documentation evidence which the RAD found the Applicant could reasonably have been expected in the circumstances to have presented prior to the rejection of his claim.
- Evidence: `issue` cue `whether` at chunk `4609750` offsets `912-919`; context: Thus, in the context of an appeal before the RAD where incompetence of former counsel is alleged by current counsel or an applicant, I am not convinced that it would be unreasonable for the RAD to find the fact that an appellant had not brought a formal complaint against his former counsel weighed negatively in its assessment of whether the appellant could not reasonably have been expected to have presented the evidence in the circumstances.
- Evidence: `evidence_fact` cue `found that` at chunk `4609750` offsets `58-68`; context: [68] And while I acknowledge that in Singh, Justice Gagné found that it was unreasonable to require the applicant to file a complaint of incompetency against his counsel, by way of comparison I would note that this Court implemented a procedural protocol on March 7, 2014 for applicants to follow before pleading incompetence or negligence by former counsel as a ground for relief within the context of applications for leave and for judicial review made under the Federal Courts Immigration and Refugee Protection Rules or applications filed as appeals under the Citizenship Act.
- Evidence: `governing_rule` cue `under` at chunk `4609750` offsets `455-460`; context: [68] And while I acknowledge that in Singh, Justice Gagné found that it was unreasonable to require the applicant to file a complaint of incompetency against his counsel, by way of comparison I would note that this Court implemented a procedural protocol on March 7, 2014 for applicants to follow before pleading incompetence or negligence by former counsel as a ground for relief within the context of applications for leave and for judicial review made under the Federal Courts Immigration and Refugee Protection Rules or applications filed as appeals under the Citizenship Act.

#### 12178:4:subtheme:11 · paragraphs 73-74

- Raw key terms: `applicant, consider, considered, decision, documents, even, evidence, fact`
- Display key terms: `consider, considered, documents, even, fact`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: consider, considered, documents, even, fact Position/evidence statements: [70] The Applicant also submits that the RAD erred by refusing to consider updated documents in the NDP. | [71] The Respondent submits that if there was new evidence in the NDP that post-dated the RPD’s decision, the Applicant was required to request that the RAD consider that evidence and to submit it with the appellant’s re Evidence spans paragraphs 73-74. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609751` offsets `789-796`; context: Further, without clear evidence of risk, the Applicant’s s 7 Charter rights are not engaged, and thus, there is no need to consider whether “the decision engages the Charter by limiting its protections” (Loyola High School at para 39).
- Evidence: `party_position` cue `submits` at chunk `4609751` offsets `1021-1028`; context: [70] The Applicant also submits that the RAD erred by refusing to consider updated documents in the NDP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609751` offsets `62-70`; context: [69] Finally, I would note that in this case the proposed new evidence is quite similar to the evidence that was before the RPD, which was considered by the RAD, in that it largely consists of general statements about stigma, which individually and collectively, are not highly supportive of persecution as the result of cumulative discrimination.
- Evidence: `counterargument_limitation` cue `However` at chunk `4609751` offsets `1238-1245`; context: However, he submits that the latter document could still be relevant as it demonstrates the continuity of the stigma issue.
- Evidence: `party_position` cue `submits` at chunk `4609752` offsets `20-27`; context: [71] The Respondent submits that if there was new evidence in the NDP that post-dated the RPD’s decision, the Applicant was required to request that the RAD consider that evidence and to submit it with the appellant’s record (RAD Rules, Rules 3 and 29).
- Evidence: `evidence_fact` cue `evidence` at chunk `4609752` offsets `50-58`; context: [71] The Respondent submits that if there was new evidence in the NDP that post-dated the RPD’s decision, the Applicant was required to request that the RAD consider that evidence and to submit it with the appellant’s record (RAD Rules, Rules 3 and 29).

#### 12178:4:subtheme:12 · paragraphs 75-77

- Raw key terms: `persons, against, article, concerning, content, discrimination, evidence, found`
- Display key terms: `persons, against, article, concerning, content, discrimination`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: persons, against, article, concerning, content, discrimination Position/evidence statements: [73] The Applicant submits that the RAD’s assessment of the documents that were before the RPD was unreasonable. | [74] The Respondent submits that the RAD conducted a thorough review of the documentary evidence that was before the RPD and reasonably concluded that it did not show HIV positive persons are subject to persecution. Application context: Issue 3: Did the RAD unreasonably conclude that the evidence regarding discrimination against HIV positive individuals in Ghana did not amount to persecution? | Upon review of the document, I find the RAD’s description of the content of this article to be accurate, the article speaks to stigmatization from a global overview. Evidence spans paragraphs 75-77. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609753` offsets `67-72`; context: [72] In my view, it is not necessary for the Court to address this issue given that the updated NDP did not include any new information concerning the treatment of HIV positive persons in Ghana.
- Evidence: `party_position` cue `submits` at chunk `4609753` offsets `373-380`; context: [73] The Applicant submits that the RAD’s assessment of the documents that were before the RPD was unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609753` offsets `247-255`; context: Issue 3: Did the RAD unreasonably conclude that the evidence regarding discrimination against HIV positive individuals in Ghana did not amount to persecution?
- Evidence: `reasoning_application` cue `conclude` at chunk `4609753` offsets `229-237`; context: Issue 3: Did the RAD unreasonably conclude that the evidence regarding discrimination against HIV positive individuals in Ghana did not amount to persecution?
- Evidence: `party_position` cue `submits` at chunk `4609754` offsets `20-27`; context: [74] The Respondent submits that the RAD conducted a thorough review of the documentary evidence that was before the RPD and reasonably concluded that it did not show HIV positive persons are subject to persecution.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609754` offsets `88-96`; context: [74] The Respondent submits that the RAD conducted a thorough review of the documentary evidence that was before the RPD and reasonably concluded that it did not show HIV positive persons are subject to persecution.
- Evidence: `counterargument_limitation` cue `however` at chunk `4609754` offsets `316-323`; context: The RAD noted the evidence that HIV positive persons face stigma and that some had lost their jobs, however, it also noted evidence indicating that some individuals with HIV continue to work and that their condition had not weighed them down.
- Evidence: `evidence_fact` cue `found that` at chunk `4609755` offsets `30-40`; context: [75] In its decision, the RAD found that the document entitled “FightAIDS Ghana – Stop Stigmatization” to be of little probative value as it speaks to the impact of stigma in a general sense and its impact on seeking testing and treatment of HIV.
- Evidence: `reasoning_application` cue `I find` at chunk `4609755` offsets `496-502`; context: Upon review of the document, I find the RAD’s description of the content of this article to be accurate, the article speaks to stigmatization from a global overview.

#### 12178:4:subtheme:13 · paragraphs 78-80

- Raw key terms: `aids, discrimination, ghana, people, stigma, against, article, considered`
- Display key terms: `aids, discrimination, ghana, people, stigma, against, article, considered`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: aids, discrimination, ghana, people, stigma, against, article, considered Application context: This indicated that because of national laws against homosexuality, the only form of sexual transmission of HIV considered in Ghana is by heterosexual intercourse. Evidence spans paragraphs 78-80. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609756` offsets `739-746`; context: While the article spoke generally about stigma, and quoted one woman who indicated that she was discriminated against when people came to know her status, the RAD found that it did not provide detailed examples from individuals which would have assisted it to determine whether stigma experienced by similarly-situated persons could rise to the level of persecution.
- Evidence: `evidence_fact` cue `found that` at chunk `4609756` offsets `113-123`; context: [76] With respect to the article entitled “Stigma Against People Living with HIV/Aids – Ghana Situation” the RAD found that this indicated that stigma and discrimination remain major impediments to the prevention of HIV transmission and providing treatment, care and support.
- Evidence: `reasoning_application` cue `because` at chunk `4609757` offsets `125-132`; context: This indicated that because of national laws against homosexuality, the only form of sexual transmission of HIV considered in Ghana is by heterosexual intercourse.
- Evidence: `counterargument_limitation` cue `However` at chunk `4609758` offsets `784-791`; context: However, there are some who have HIV are still healthy and working and their conditions have never weighed them down i.

#### 12178:4:subtheme:14 · paragraphs 81-82

- Raw key terms: `applicant, article, found, ghana, little, probative, value, analyzing`
- Display key terms: `article, ghana, little, probative, value, analyzing`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: article, ghana, little, probative, value, analyzing Evidence spans paragraphs 81-82. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609759` offsets `224-231`; context: For that reason, it was of little probative value in analyzing whether the discrimination that the Applicant may face in Ghana would rise to the level of persecution.
- Evidence: `evidence_fact` cue `found that` at chunk `4609759` offsets `13-23`; context: [79] The RAD found that this article, like the others, did not provide any specific examples and only spoke of stigmatization and its impact in a general sense.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609760` offsets `338-346`; context: [80] The RAD next referenced a document entitled “Ghana: Treatment and sexual minorities and government authorities, including legislation, state protection and support services”, but found it to have little probative value as the Applicant had not challenged the RPD’s finding that he had not provided sufficient credible or trustworthy evidence to support his claim that he was a homosexual or bisexual and, before the RAD, had focused on his sur place claim, being his HIV positive status.

#### 12178:4:subtheme:15 · paragraphs 83-84

- Raw key terms: `aids, country, crossroads, ghana, human, people, persons, quoted`
- Display key terms: `aids, country, crossroads, ghana, human, people, persons, quoted`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: aids, country, crossroads, ghana, human, people, persons, quoted Operative outcome context: This was in the form of a recommendation and noted that: Although Ghana has progressed in the enforcement of human rights over the last few decades, certain social minorities – especially the disabled, homosexuals, and p Evidence spans paragraphs 83-84. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4609761` offsets `801-808`; context: The RAD found that the statement did not provide any further detail and did not indicate whether the situation was the same for heterosexual persons, such as the Applicant, or if it differed between rural and urban centers.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609761` offsets `62-70`; context: [81] The RAD then stated that it had considered the remaining evidence in the NDP and consulted its core human rights documents including the US DOS Report, the UK Country of Origin Report, the Amnesty International Report 2013, Ghana: Country at the Crossroads, and Freedom of the World Report and found that in the documents there were only two mentions of persecution of individuals with HIV/AIDS in Ghana who are not affiliated with the Lesbian Gay Bisexual and Transgender community.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4609762` offsets `152-160`; context: This was in the form of a recommendation and noted that:
Although Ghana has progressed in the enforcement of human rights over the last few decades, certain social minorities – especially the disabled, homosexuals, and people living with HIV/AIDS – continue to disproportionately face human rights abuses, or have their rights completely denied.
- Evidence: `disposition` cue `denied` at chunk `4609762` offsets `433-439`; context: This was in the form of a recommendation and noted that:
Although Ghana has progressed in the enforcement of human rights over the last few decades, certain social minorities – especially the disabled, homosexuals, and people living with HIV/AIDS – continue to disproportionately face human rights abuses, or have their rights completely denied.

#### 12178:4:subtheme:16 · paragraphs 85-88

- Raw key terms: `evidence, found, because, considered, level, noted, persecution, positive`
- Display key terms: `because, considered, level, noted, persecution, positive`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: because, considered, level, noted, persecution, positive Position/evidence statements: [85] The RAD noted that counsel had linked some of his arguments to the Applicant’s perceived sexual orientation and also submitted that social stigma related to sexual immorality must be assessed, taking into considerat Rule/authority context: The RAD considered Canada (Attorney General) v Ward, [1993] 2 SCR 689 and concluded, based on the evidence and the jurisprudence regarding discrimination versus persecution, that it was not provided with sufficient credi Application context: [83] The RAD noted that this report did not provide details of the nature and extent of human rights abuses and does not differentiate between abuses experienced because of issues related to sexual orientation or solely  | [84] The RAD also declined to put significant weight on the Applicant’s testimony before the RPD that he was aware of a person who committed suicide because of his HIV status as the Applicant could provide no details abo Operative outcome context: It also noted that no evidence was presented to establish that state authorities are involved in the persecution of HIV positive individuals or that such individuals whose rights have been denied have also been denied st Evidence spans paragraphs 85-88. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4609763` offsets `173-179`; context: [83] The RAD noted that this report did not provide details of the nature and extent of human rights abuses and does not differentiate between abuses experienced because of issues related to sexual orientation or solely on the basis of HIV status.
- Evidence: `evidence_fact` cue `found that` at chunk `4609763` offsets `251-261`; context: It found that while the NDP contained ample evidence regarding the human rights abuses experienced by homosexuals, it could not place significant weight on a broad all-encompassing statement regarding human rights abuses in Ghana as found in the above extract.
- Evidence: `reasoning_application` cue `because` at chunk `4609763` offsets `162-169`; context: [83] The RAD noted that this report did not provide details of the nature and extent of human rights abuses and does not differentiate between abuses experienced because of issues related to sexual orientation or solely on the basis of HIV status.
- Evidence: `evidence_fact` cue `testimony` at chunk `4609764` offsets `72-81`; context: [84] The RAD also declined to put significant weight on the Applicant’s testimony before the RPD that he was aware of a person who committed suicide because of his HIV status as the Applicant could provide no details about this and because of the Applicant’s history of embellishment.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4609764` offsets `771-784`; context: The RAD considered Canada (Attorney General) v Ward, [1993] 2 SCR 689 and concluded, based on the evidence and the jurisprudence regarding discrimination versus persecution, that it was not provided with sufficient credible or trustworthy evidence to persuade it that the treatment that the Applicant would face if he returned to Ghana would rise to the level of persecution.
- Evidence: `reasoning_application` cue `because` at chunk `4609764` offsets `149-156`; context: [84] The RAD also declined to put significant weight on the Applicant’s testimony before the RPD that he was aware of a person who committed suicide because of his HIV status as the Applicant could provide no details about this and because of the Applicant’s history of embellishment.
- Evidence: `disposition` cue `denied` at chunk `4609764` offsets `474-480`; context: It also noted that no evidence was presented to establish that state authorities are involved in the persecution of HIV positive individuals or that such individuals whose rights have been denied have also been denied state protection.
- Evidence: `party_position` cue `submitted` at chunk `4609765` offsets `122-131`; context: [85] The RAD noted that counsel had linked some of his arguments to the Applicant’s perceived sexual orientation and also submitted that social stigma related to sexual immorality must be assessed, taking into consideration the particular situation of each claimant.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609765` offsets `397-405`; context: Further, the documentary evidence indicated that because of national laws against homosexuality, the only recognized manner of sexual transmission of HIV is considered to be by heterosexual intercourse.
- Evidence: `reasoning_application` cue `because` at chunk `4609765` offsets `421-428`; context: Further, the documentary evidence indicated that because of national laws against homosexuality, the only recognized manner of sexual transmission of HIV is considered to be by heterosexual intercourse.
- Evidence: `evidence_fact` cue `evidence` at chunk `4609766` offsets `60-68`; context: [86] In my view, the RAD accurately set out the documentary evidence, weighed it and reasonably concluded that it did not rise to the level of persecution.

#### 12178:4:subtheme:17 · paragraphs 89-89

- Raw key terms: `absence, admission, admit, applicant, certification, certified, challenge, charter`
- Display key terms: `absence, admission, admit, certification, certified, challenge, charter`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: absence, admission, admit, certification, certified, challenge, charter Position/evidence statements: Certified Question [88] The Applicant submitted the following question for certification: Does the Charter provide the RAD with jurisdiction to admit evidence that does not meet the test for admission of new evidence set Operative outcome context: [87] For all of these reasons, the judicial review is dismissed. Evidence spans paragraphs 89-89. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Question` at chunk `4609767` offsets `75-83`; context: Certified Question [88] The Applicant submitted the following question for certification:
Does the Charter provide the RAD with jurisdiction to admit evidence that does not meet the test for admission of new evidence set out in s 110(4) in the absence of a direct constitutional challenge to that provision?
- Evidence: `party_position` cue `submitted` at chunk `4609767` offsets `103-112`; context: Certified Question [88] The Applicant submitted the following question for certification:
Does the Charter provide the RAD with jurisdiction to admit evidence that does not meet the test for admission of new evidence set out in s 110(4) in the absence of a direct constitutional challenge to that provision?
- Evidence: `evidence_fact` cue `evidence` at chunk `4609767` offsets `215-223`; context: Certified Question [88] The Applicant submitted the following question for certification:
Does the Charter provide the RAD with jurisdiction to admit evidence that does not meet the test for admission of new evidence set out in s 110(4) in the absence of a direct constitutional challenge to that provision?
- Evidence: `disposition` cue `dismissed` at chunk `4609767` offsets `54-63`; context: [87] For all of these reasons, the judicial review is dismissed.

#### Section text

[56] Then the decision-maker should ask how the Charter value at issue will best be protected in view of the statutory objectives. This is at the core of the proportionality exercise, and requires the decision-maker to balance the severity of the interference of the Charter protection with the statutory objectives. This is where the role of judicial review for reasonableness aligns with the one applied in the Oakes context. As this Court recognized in RJR-MacDonald Inc. v. Canada (Attorney General), 1995 CanLII 64 (SCC), [1995] 3 S.C.R. 199, at para. 160, “courts must accord some leeway to the legislator” in the Charter balancing exercise, and the proportionality test will be satisfied if the measure “falls within a range of reasonable alternatives”. The same is true in the context of a review of an administrative decision for reasonableness, where decision-makers are entitled to a measure of deference so long as the decision, in the words of Dunsmuir, “falls within a range of possible, acceptable outcomes” (para. 47).

[46] Significantly, for the purposes of this matter, Doré makes it clear that the trigger for the consideration of Charter values depends on whether the decision-maker is exercising discretion in reaching his or her decision.

[47] In the present case, the Applicant submits that the RAD has the discretion to admit evidence that is otherwise “technically inadmissible” as a result of its obligation to interpret the law in accordance with the Charter, pursuant to s 3(3)(d) of the IRPA. On the other hand, the Respondent submits the RAD has no such discretion, and as a result, its jurisdiction to admit new evidence is limited by a strict interpretation of s 110(4).

[48] Therefore, in my view, this matter appears to turn on the question of whether the RAD has discretion to admit new evidence that does not meet the statutory conditions in s 110(4). If it does have discretion, then per Doré, it is required to balance the values that underpin an appellant’s s 7 Charter rights with the statutory objectives of the IRPA. However, if it does not have discretion to admit new evidence that does not meet the requirements of s 110(4), then the analysis ends there.

[49] Section 110 of the IRPA states, in part, as follows:
110. […]
110. […]
(3) Subject to subsections (3.1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
(3) Sous réserve des paragraphes (3.1), (4) et (6), la section procède sans tenir d’audience en se fondant sur le dossier de la Section de la protection des réfugiés, mais peut recevoir des éléments de preuve documentaire et des observations écrites du ministre et de la personne en cause ainsi que, s’agissant d’une affaire tenue devant un tribunal constitué de trois commissaires, des observations écrites du représentant ou mandataire du Haut-Commissariat des Nations Unies pour les réfugiés et de toute autre personne visée par les règles de la Commission.
(3.1) Unless a hearing is held under subsection (6), the Refugee Appeal Division must make a decision within the time limits set out in the regulations.
(3.1) Sauf si elle tient une audience au titre du paragraphe (6), la section rend sa décision dans les délais prévus par les règlements.
(4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
(4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
[…]
[…]
(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
c) à supposer qu’ils soient admis, justifieraient que la demande d’asile soit accordée ou refusée, selon le cas.

[50] In Rizzo & Rizzo Shoes Ltd (Re), [1998] 1 SCR 27, and in subsequent decisions, the Supreme Court of Canada endorsed the “modern principle” of statutory construction:

[21] Although much has been written about the interpretation of legislation (see, e.g., Ruth Sullivan, Statutory Interpretation (1997); Ruth Sullivan, Driedger on the Construction of Statutes (3rd ed. 1994) (hereinafter “Construction of Statutes”); Pierre-André Côté, The Interpretation of Legislation in Canada (2nd ed. 1991)), Elmer Driedger in Construction of Statutes (2nd ed. 1983) best encapsulates the approach upon which I prefer to rely. He recognizes that statutory interpretation cannot be founded on the wording of the legislation alone. At p. 87 he states:
Today there is only one principle or approach, namely, the words of an Act are to be read in their entire context and in their grammatical and ordinary sense harmoniously with the scheme of the Act, the object of the Act, and the intention of Parliament.
(also see R v Middleton, 2009 SCC 21 at para 78; Canada Trustco Mortgage Co v Canada, 2005 SCC 54 at para 10; Bell ExpressVu Ltd Partnership v Rex, 2002 SCC 42 at para 26).

[51] Based on the grammatical and ordinary sense of the language in s 110(4), in my view, the RAD reasonably concluded that it did not have the discretion to admit new evidence that it found did not meet one of the explicit conditions set out in that provision. The operative words of s 110(4) are that an appellant “may present only evidence” (emphasis added) that meets the subsequent conditions. The use of the word “only” imports exclusivity, limiting the RAD’s consideration exclusively to that evidence that satisfies the factors in s 110(4). This is further supported by the context in which s 110(4) is found. Section 110(3) stipulates that, subject to ss 110(3.1), (4) and (6), the RAD must proceed without a hearing and on the basis of the record that was before the RPD. Section 110(6) permits the RAD to hold a hearing if it is of the opinion that there is new documentary evidence, as referenced in s 110(3), that meets the requirements of s 110(4), in which case the RAD will then consider whether that evidence raises serious credibility issues, is central to the claim and, if accepted, it would justify allowing or rejecting the claim. This suggests that the new evidence must first be found to be admissible. If it is and if a hearing is sought, then the new evidence is to be further assessed to determine if a hearing is warranted.

[52] The Respondent suggests that the jurisprudence in the PRRA context is applicable when interpreting s 110(4). In that regard, the Raza test does not expand a PRRA officer’s ability to admit new evidence, as its factors only come into play if the officer finds that the statutory conditions are met. The Respondent argues that the same reasoning should apply to the interpretation of s 110(4); thus, if the statutory conditions have not been met, the RAD does not have discretion to admit the evidence.

[53] I am inclined to agree with the Respondent that the test in Raza does not permit a PRRA officer to admit evidence that does not meet the explicit statutory conditions for new evidence found in s 113(a) of the IRPA. Rather, that the implicit factors articulated by the Federal Court of Appeal are to be taken into consideration once an officer has determined that the evidence first meets one of the explicit statutory conditions.

[54] As stated in De Silva v Canada (Citizenship and Immigration), 2007 FC 841 in the context of s 113(a):

[17] Although the PRRA process is meant to assess only evidence of new risks, this does not mean that new evidence relating to old risks need not be considered. Moreover, one must be careful not to mix up the issue of whether evidence is new evidence under subsection 133(a) with the issue of whether the evidence establishes risk. The PRRA officer should first consider whether a document falls within one of the three prongs of subsection 113(a). If it does, then the Officer should go on to consider whether the document evidences a new risk.
(Emphasis in bold is added; emphasis in underline is original)

[55] I see no reason why that same approach would not be followed in regard to s 110(4). The RAD must first determine if the three explicit conditions set out in s 110(4) have been met: 1) did the evidence arise after the rejection of their claim? If not, 2) was it reasonably available, or 3) could the applicant reasonably have been expected, in the circumstances to provide the evidence? If none of these conditions are met, then, on a plain reading of s 110(4), the RAD has no discretion to admit the new evidence.

[56] The question of whether the Raza criteria are applicable to s 110(4) is currently unsettled (see, for example, Singh and Denbel v Canada (Citizenship and Immigration), 2015 FC 629 at paras 40-44). However, in this case the RAD did not apply the implicit Raza factors. Rather, it found that it did not have discretion to accept evidence that did not fall within s 110(4). Accordingly, it is not necessary here to enter this debate which, by way of certified question in Singh, will be resolved by the Federal Court of Appeal. In any event, I do not understand Singh to suggest that the explicit statutory requirements of s 110(4) need not be met.

[57] Returning to the question of the discretionary nature of the RAD’s decision, I would also note that this is not a situation such as Loyola High School where the source of the discretion at issue was clear as it arose from the Minister’s refusal to grant an exemption to a regulatory requirement. Indeed, in that case the Supreme Court referred to its prior decision in Doré, which it described as setting out the applicable framework for assessing whether the Minister had exercised her statutory discretion in accordance with the relevant Charter protections (at para 3), and then stated that:

[4] Under Doré, where a discretionary administrative decision engages the protections enumerated in the Charter — both the Charter’s guarantees and the foundational values they reflect — the discretionary decision-maker is required to proportionately balance the Charter protections to ensure that they are limited no more than is necessary given the applicable statutory objectives that she or he is obliged to pursue.

[58] In Loyola High School, the challenge was not to the Minister’s statutory authority to impose curricular requirements, but rather to her discretionary decision to deny the appellant an exemption. In that situation, the Supreme Court held that the reasonableness of the Minister’s decision depended

[32] […] on whether it reflected a proportionate balance between the statutory mandate to grant exemptions only when a proposed alternative program is “equivalent” to the prescribed curriculum, based on the ERC Program’s goals of promoting tolerance and respect for difference, and the religious freedom of the members of the Loyola community who seek to offer and wish to receive a Catholic education.

[59] The Supreme Court of Canada has also stated that “The concept of discretion refers to decisions where the law does not dictate a specific outcome, or where the decision-maker is given a choice of options within a statutorily imposed set of boundaries” (Baker at para 52).

[60] By contrast, s 110(4) offers the RAD no discretion to refuse to apply its explicit admissibility requirements for new evidence. That provision enumerates the factors that the RAD must apply, thereby determining the result based on the facts of the case. If the new evidence meets the requirements of s 110(4) then the RAD must accept it. Conversely, if it does not, then the RAD must reject it. While there is an element of subjectivity in assessing whether the evidence was reasonably available or if an applicant could not reasonably have been expected to have previously presented it, this is a factual assessment, it does not alter the character of the ultimate decision as to admissibility. Accordingly, in my view, the RAD’s interpretation of s 110(4) was reasonable.

[61] The Applicant also relies on two decisions of this Court made in the PRRA context to support his argument that Charter interests can override legislative interests. The first is Elezi, which pre-dates the Federal Court of Appeal’s decision in Raza. There, Justice de Montigny (then of this Court) commented that if Canada is to respect its international obligations and abide by the Charter, “it cannot disregard credible evidence that a person would be at risk if sent back to his or her country of origin on the sole basis that this evidence is technically inadmissible” (at para 45). However, as noted by the Respondent, in Elezi, Justice de Montigny actually found that the officer’s decision not to admit the applicant’s new evidence under s 113(a) was unreasonable because it was either created after the RPD’s decision, or the applicant could not reasonably have been expected in the circumstances to have presented the evidence to the RPD (at paras 39 and 43). In this regard, his comments on the admissibility of evidence that is “technically inadmissible” may properly be regarded as obiter. Further, this proposed broadening of the test under s 113(a) of the IRPA does not subsequently appear to have been followed.

[62] The Applicant also relies on Sanchez, which is a stay decision. There the PRRA officer excluded a country condition document pursuant to s 113(a) of the IRPA on the basis that it was published prior to the date of his hearing and the applicant or his counsel could have located and presented it at the RPD hearing. Justice Shore found that the mere fact that the report was published prior to the hearing did not mean that it was obvious or easily accessible to the applicant. As it was not located and included in the NDP, he queried how the applicant and his counsel could reasonably have been expected to have located it. He also found that it was an extremely relevant report from a credible source. He stated that even if the officer may exclude a report under s 113(a), he had discretion to consider the report. On my reading of the decision, this conclusion appears to be based on Justice Shore’s comment that a PRRA officer is not limited to considering evidence submitted by the applicant, but has an obligation to conduct sufficient independent research in order to come to a proper determination. The officer had, in fact, consulted and relied on other sources. Justice Shore found that the PRRA officer failed to properly exercise his discretion to consider credible, material evidence that supported the applicant’s allegations of risk. For this and other reasons, the applicant had demonstrated that there was a serious issue to be tried and a stay was warranted.

[63] In my view, in Sanchez Justice Shore appears to find that there was a reasonable explanation as to why the report had not been submitted previously by the applicant. On that basis, even though it pre-dated the RPD hearing, the PRRA officer could consider it as it was relevant and credible. The officer could also have considered it as part of his independent research. As a result, I am not convinced that this case is of assistance to the Applicant because his explanation for not providing the country condition documents was not accepted by the RAD, and he has not challenged the reasonableness of that finding. Further, the reports which he sought to submit as new evidence addressed an issue upon which evidence had been tendered and considered by the RPD.

[64] Thus, Elezi and Sanchez do not support a view that the RAD has discretion to consider new evidence that did not meet any of the three explicit criteria set out in s 110(4) nor that that legislative provision is, in these circumstances, overridden by Charter interests.

[65] In this case, the RAD found that the four new documents were all produced before the Applicant’s second sitting before the RPD, after he learned that he was HIV positive and after he added that ground to his refugee claim. He was represented by experienced counsel who, in fact, did disclose some documents related to the treatment of persons with HIV in Ghana, which were considered by the RPD, his counsel also made “extensive submissions on the risks that the Appellant would face as a HIV+ person, should he return to Ghana” (para 15). The Applicant did not provide any evidence in support of his explanation for not tendering the new evidence previously, being that his former counsel was incompetent in not disclosing further documentary evidence. Further, the RAD did not accept the Applicant’s explanation that he was unaware that he needed to gather information related to this issue given that both he and his counsel had provided evidence on that very issue. The RAD also found that the Applicant had not provided sufficient evidence to persuade it that the new evidence was not reasonably available or that he could not reasonably have been expected in the circumstances to have presented it prior to the RPD’s rejection of his claim.

[66] In short, the RAD found that the Applicant failed to meet the explicit statutory requirements of s 110(4). In my view and as noted above, in the absence of discretion to admit new evidence that did not meet these requirements, if the RAD reasonably reached that conclusion, then the applicability or consideration of the implicit Raza factors or other criteria, was no longer relevant. And, even if applied, those factors would only serve to narrow the admissibility of new evidence that meets the explicit conditions.

[67] In that regard, I am also of the view that the RAD’s decision not to admit the new evidence was reasonable. The evidence arose after the rejection of the claim. There was no evidence that it was not reasonably available. The Applicant in his affidavit stated that he was attaching further documentary evidence detailing the persecution HIV positive people face in Ghana and, by way of explanation for not having previously provided it stated that he “did not know that [he] was supposed to gather this evidence as part of [his] RPD hearing” and that he did “not know why [his] counsel did not gather more of it”. It was not unreasonable for the RAD not to accept that explanation in these circumstances. The Applicant and his former counsel were aware of the issue and did submit documentary evidence addressing the manner in which HIV positive people are treated in Ghana. The new evidence is also not personal to the Applicant, but is comprised of further country documentation evidence which the RAD found the Applicant could reasonably have been expected in the circumstances to have presented prior to the rejection of his claim.

[68] And while I acknowledge that in

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 12178:5 · paragraphs 90-93

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `18a9bc682c012f8310512d1fb098e749d5fe30c6a9953464d6e702b74d0edc1e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12178:5:subtheme:1 · paragraphs 90-91

- Raw key terms: `account, appeal, apply, applying, appropriate, balancing, broad, canada`
- Display key terms: `account, apply, applying, appropriate, balancing, broad`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: account, apply, applying, appropriate, balancing, broad Position/evidence statements: [89] The Respondent submitted the following two questions for consideration: 1. Rule/authority context: Does the RAD have an obligation to apply Charter values in the exercise of statutory discretion under s 110(4)? Application context: Does the RAD have an obligation to apply Charter values in the exercise of statutory discretion under s 110(4)? Evidence spans paragraphs 90-91. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submitted` at chunk `4609768` offsets `20-29`; context: [89] The Respondent submitted the following two questions for consideration:
1.
- Evidence: `governing_rule` cue `under` at chunk `4609768` offsets `302-307`; context: Does the RAD have an obligation to apply Charter values in the exercise of statutory discretion under s 110(4)?
- Evidence: `reasoning_application` cue `apply` at chunk `4609768` offsets `241-246`; context: Does the RAD have an obligation to apply Charter values in the exercise of statutory discretion under s 110(4)?
- Evidence: `issue` cue `whether` at chunk `4609769` offsets `35-42`; context: [90] The test for certification is whether there is a serious question of general importance and of broad significance which would be dispositive of the appeal and which transcends the interests of the parties to the litigation (Zhang v Canada (Minister of Citizenship and Immigration), 2013 FCA 168 at para 9; Varela v Canada (Minister of Citizenship and Immigration), 2009 FCA 145 at paras 28-30; Zazai v Canada (Minister of Citizenship and Immigration), 2004 FCA 89 at para 11).

#### 12178:5:subtheme:2 · paragraphs 92-93

- Raw key terms: `absence, admission, admit, application, case, cause, cecily, certified`
- Display key terms: `absence, admission, admit, case, cecily, certified`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: absence, admission, admit, case, cecily, certified Rule/authority context: Therefore, I will certify the following question: Does the admission of new evidence under s 110(4) involve the exercise of discretion by the RAD? Application context: Therefore, I will certify the following question: Does the admission of new evidence under s 110(4) involve the exercise of discretion by the RAD? Operative outcome context: The application for judicial review is dismissed. Evidence spans paragraphs 92-93. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4609770` offsets `175-180`; context: However, the issue of whether there is discretion to admit new evidence in that circumstance could be dispositive in the absence of a consideration by the RAD of Charter values.
- Evidence: `evidence_fact` cue `found that` at chunk `4609770` offsets `26-36`; context: [91] In this case, I have found that the RAD did not have the discretion to admit new evidence when the explicit statutory requirements of s 110(4) were not met.
- Evidence: `governing_rule` cue `under` at chunk `4609770` offsets `425-430`; context: Therefore, I will certify the following question:
Does the admission of new evidence under s 110(4) involve the exercise of discretion by the RAD?
- Evidence: `reasoning_application` cue `Therefore` at chunk `4609770` offsets `340-349`; context: Therefore, I will certify the following question:
Does the admission of new evidence under s 110(4) involve the exercise of discretion by the RAD?
- Evidence: `counterargument_limitation` cue `However` at chunk `4609770` offsets `162-169`; context: However, the issue of whether there is discretion to admit new evidence in that circumstance could be dispositive in the absence of a consideration by the RAD of Charter values.
- Evidence: `disposition` cue `dismissed` at chunk `4609770` offsets `738-747`; context: The application for judicial review is dismissed.

#### Section text

[89] The Respondent submitted the following two questions for consideration:
1. What are the appropriate implicit and explicit considerations that the RAD should consider when applying s 110(4) of IRPA?
2. Does the RAD have an obligation to apply Charter values in the exercise of statutory discretion under s 110(4)? If so, what considerations should it take into account when balancing Charter values with statutory objectives?

[90] The test for certification is whether there is a serious question of general importance and of broad significance which would be dispositive of the appeal and which transcends the interests of the parties to the litigation (Zhang v Canada (Minister of Citizenship and Immigration), 2013 FCA 168 at para 9; Varela v Canada (Minister of Citizenship and Immigration), 2009 FCA 145 at paras 28-30; Zazai v Canada (Minister of Citizenship and Immigration), 2004 FCA 89 at para 11).

[91] In this case, I have found that the RAD did not have the discretion to admit new evidence when the explicit statutory requirements of s 110(4) were not met. However, the issue of whether there is discretion to admit new evidence in that circumstance could be dispositive in the absence of a consideration by the RAD of Charter values. Therefore, I will certify the following question:
Does the admission of new evidence under s 110(4) involve the exercise of discretion by the RAD? If so, does this discretion permit the RAD to admit evidence which does not meet the test under s 110(4) and does its admission engage a consideration of Charter values?
JUDGMENT
THIS COURT’S JUDGMENT is that
1. The application for judicial review is dismissed.
2. There is no order as to costs.
3. The following question is certified:
Does the admission of new evidence under s 110(4) involve the exercise of discretion by the RAD? If so, does this discretion permit the RAD to admit evidence which does not meet the test under s 110(4) and does its admission engage a consideration of Charter values?
"Cecily Y. Strickland"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-7050-14
STYLE OF CAUSE:
SAMUEL DERI v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
June 17, 2015


## 12178:6 · paragraphs 94-94

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a5c4f2abcdaac60b6a19c318b115ece82281b8681f72d8731359897752df27e3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12178:6:subtheme:1 · paragraphs 94-94

- Raw key terms: `aadil, appearances, applicant, attorney, barristers, canada, dated, deputy`
- Display key terms: `aadil, barristers, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: aadil, barristers, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 94-94. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
STRICKLAND J.
DATED:
September 2, 2015
APPEARANCES:
Aadil Mangalji
For The Applicant
Amy King
For The Respondent
SOLICITORS OF RECORD:
LM Law Group
Barristers and Solicitors
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
