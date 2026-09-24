# Discussion Units: case 13554

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **50**
- Continuity pairs: **49**
- Discussion Units: **2**
- Paragraph source hashes: **50**
- Sub-themes: **13**

## 13554:1 · paragraphs 0-48

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `45215c5a646762d289ab023fa39a89e4a4149b3c12f5a7e96cfc7ec56b51a1bb`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13554:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `applicant, canada, court, decision, general, justice, tribunal, allowed`
- Display key terms: `justice, allowed`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: justice, allowed Operative outcome context: [2] This application for judicial review should be allowed. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `allowed` at chunk `4667475` offsets `51-58`; context: [2] This application for judicial review should be allowed.

#### 13554:1:subtheme:2 · paragraphs 3-7

- Raw key terms: `appeal, division, employment, general, insurance, decision, subsection, tribunal`
- Display key terms: `division, employment, insurance, subsection`
- Argument roles: `disposition, governing_rule, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, reasoning_application Display terms: division, employment, insurance, subsection Rule/authority context: [4] Established under subsection 44(1) of the Department of Employment and Social Development Act, SC 2005, c 34 [Act], the Tribunal is an independent administrative tribunal that provides a fair and impartial appeal pro | Under subsection 54(1), the General Division may dismiss the appeal or confirm, rescind or vary a decision of the Minister or the Commission in whole or in part or give the decision that the Minister or the Commission sh Application context: [3] On May 29, 2013, the Canada Employment Insurance Commission [Commission] informed the applicant that he could no longer receive regular Employment Insurance benefits as of October 3, 2010, because he had voluntarily  | This is therefore an appeal as of right. Operative outcome context: On April 15, 2014, in a 16-page decision with reasons, the General Division dismissed the applicant’s appeal on the merits, on the grounds that, on October 5, 2010, the applicant had voluntarily left his employment at Ca Evidence spans paragraphs 3-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4667476` offsets `193-200`; context: [3] On May 29, 2013, the Canada Employment Insurance Commission [Commission] informed the applicant that he could no longer receive regular Employment Insurance benefits as of October 3, 2010, because he had voluntarily left his employment without just cause, resulting in an overpayment of $16,864 being made to him.
- Evidence: `governing_rule` cue `under` at chunk `4667477` offsets `16-21`; context: [4] Established under subsection 44(1) of the Department of Employment and Social Development Act, SC 2005, c 34 [Act], the Tribunal is an independent administrative tribunal that provides a fair and impartial appeal process for appeals under the Employment Insurance Act, SC 1996, c 23, the Canada Pension Plan, and the Old Age Security Act, RSC 1985, c O-9.
- Evidence: `governing_rule` cue `Under` at chunk `4667478` offsets `136-141`; context: Under subsection 54(1), the General Division may dismiss the appeal or confirm, rescind or vary a decision of the Minister or the Commission in whole or in part or give the decision that the Minister or the Commission should have given.
- Evidence: `reasoning_application` cue `therefore` at chunk `4667478` offsets `381-390`; context: This is therefore an appeal as of right.
- Evidence: `disposition` cue `dismissed` at chunk `4667479` offsets `213-222`; context: On April 15, 2014, in a 16-page decision with reasons, the General Division dismissed the applicant’s appeal on the merits, on the grounds that, on October 5, 2010, the applicant had voluntarily left his employment at Canpar Transport without just cause within the meaning of sections 29 and 30 of the Employment Insurance Act.

#### 13554:1:subtheme:3 · paragraphs 8-11

- Raw key terms: `appeal, decision, division, general, leave, made, appellant, application`
- Display key terms: `division, leave, made, appellant`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: division, leave, made, appellant Operative outcome context: Nevertheless, for an application for leave to appeal to be granted, there must be an “arguable case” (DB v Minister of Employment and Social Development, 2015 SSTAD 806 at para 53; CM v Canada Employment Insurance Commis | If leave to appeal is granted, the application for leave to appeal becomes the notice of appeal and is deemed to have been filed on the day on which the application for leave to appeal was filed (subsection 58(5)). Evidence spans paragraphs 8-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4667481` offsets `660-667`; context: (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `4667481` offsets `712-718`; context: (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4667483` offsets `210-222`; context: Nevertheless, for an application for leave to appeal to be granted, there must be an “arguable case” (DB v Minister of Employment and Social Development, 2015 SSTAD 806 at para 53; CM v Canada Employment Insurance Commission, 2015 SSTAD 574; Bellefeuille v Canada (Attorney General), 2014 FC 963 at para 29 CanLII [Bellefeuille]; Canada (Attorney General) v Zakaria, [2011] FCJ No 189 at para 37; Fancy v Canada (Attorney General), 2010 FCA 63 at paras 2 and 3; Canada (Minister of Human Resources Development) v Hogervorst, 2007 FCA 41 at para 37 [Hogervorst]; Kerth v Canada (Minister of Human Resources Development), [1999] FCJ No 1252 at para 24).
- Evidence: `disposition` cue `granted` at chunk `4667483` offsets `269-276`; context: Nevertheless, for an application for leave to appeal to be granted, there must be an “arguable case” (DB v Minister of Employment and Social Development, 2015 SSTAD 806 at para 53; CM v Canada Employment Insurance Commission, 2015 SSTAD 574; Bellefeuille v Canada (Attorney General), 2014 FC 963 at para 29 CanLII [Bellefeuille]; Canada (Attorney General) v Zakaria, [2011] FCJ No 189 at para 37; Fancy v Canada (Attorney General), 2010 FCA 63 at paras 2 and 3; Canada (Minister of Human Resources Development) v Hogervorst, 2007 FCA 41 at para 37 [Hogervorst]; Kerth v Canada (Minister of Human Resources Development), [1999] FCJ No 1252 at para 24).
- Evidence: `disposition` cue `granted` at chunk `4667484` offsets `481-488`; context: If leave to appeal is granted, the application for leave to appeal becomes the notice of appeal and is deemed to have been filed on the day on which the application for leave to appeal was filed (subsection 58(5)).

#### 13554:1:subtheme:4 · paragraphs 12-18

- Raw key terms: `appeal, case, application, division, form, leave, appellant, following`
- Display key terms: `case, division, form, leave, appellant, following`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: case, division, form, leave, appellant, following Rule/authority context: [14] It should be noted that under paragraphs 40(1)(c) and (d) of the Regulations, the application for leave to appeal must include the “grounds for the application” and “any statements of fact that were presented to the | In particular, for the Request for Leave to Appeal field, the appellant must complete the following introductory paragraph: “Pursuant to s. Application context: [16] Therefore, in accordance with the Instructions given by the Tribunal for completing the Application Requesting Leave to Appeal to the Appeal Division form (form SST-ARLTATTAD), available on the website, the appellan | The same requirement applies in the case of a notice of appeal against a summary dismissal by the General Division (form SST-ATATTAD). Operative outcome context: According to the case law of the Federal Court and the Federal Court of Appeal upon which the Tribunal relied, when the issue to be decided is whether it is appropriate to grant an extension of time to file a notice of a Evidence spans paragraphs 12-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4667485` offsets `381-386`; context: According to the case law of the Federal Court and the Federal Court of Appeal upon which the Tribunal relied, when the issue to be decided is whether it is appropriate to grant an extension of time to file a notice of appeal, the most important factor is whether it is in the interests of justice that the extension be granted (AW at para 8; Grewal v Canada (Minister of Employment and Immigration), [1985] 2 FC 263 at pages 278-279).
- Evidence: `disposition` cue `granted` at chunk `4667485` offsets `581-588`; context: According to the case law of the Federal Court and the Federal Court of Appeal upon which the Tribunal relied, when the issue to be decided is whether it is appropriate to grant an extension of time to file a notice of appeal, the most important factor is whether it is in the interests of justice that the extension be granted (AW at para 8; Grewal v Canada (Minister of Employment and Immigration), [1985] 2 FC 263 at pages 278-279).
- Evidence: `governing_rule` cue `under` at chunk `4667487` offsets `29-34`; context: [14] It should be noted that under paragraphs 40(1)(c) and (d) of the Regulations, the application for leave to appeal must include the “grounds for the application” and “any statements of fact that were presented to the General Division” and that the applicant relies on in the application.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `4667489` offsets `496-507`; context: In particular, for the Request for Leave to Appeal field, the appellant must complete the following introductory paragraph: “Pursuant to s.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4667489` offsets `5-14`; context: [16] Therefore, in accordance with the Instructions given by the Tribunal for completing the Application Requesting Leave to Appeal to the Appeal Division form (form SST-ARLTATTAD), available on the website, the appellant must complete fields 3(C) REQUEST FOR LEAVE TO APPEAL - (see instructions on page 1) and 3(D) REASONS FOR THE APPEAL - (see instructions on page 1).
- Evidence: `reasoning_application` cue `applies` at chunk `4667490` offsets `312-319`; context: The same requirement applies in the case of a notice of appeal against a summary dismissal by the General Division (form SST-ATATTAD).
- Evidence: `evidence_fact` cue `evidence` at chunk `4667491` offsets `829-837`; context: On August 13, 2014, the applicant filed a third notice of appeal with the Appeal Division, in which he stated this time in field 3(B) REASON(S) FOR LATE APPEAL: [translation] “I am sending you the evidence that I duly sent my papers on 05-02 at 3:34 AM”.
- Evidence: `counterargument_limitation` cue `but` at chunk `4667491` offsets `145-148`; context: [18] In this case, a first notice of appeal from the April 15, 2014, decision was filed by the applicant within the prescribed time in May 2014, but for a reason that was not explained to this Court, the notice was lost or not received by the Tribunal.

#### 13554:1:subtheme:5 · paragraphs 19-20

- Raw key terms: `application, extension, question, regulations, request, tribunal, accept, analogie`
- Display key terms: `extension, question, regulations, request, accept, analogie`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: extension, question, regulations, request, accept, analogie Operative outcome context: [19] The applicant clearly used the wrong appeal form – his appeal required leave first, since the General Division had not dismissed his appeal summarily. Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4667492` offsets `198-206`; context: Instead of refusing to accept the form in question (SST-ATATTAD) and returning the appropriate application requesting leave to appeal form to the applicant (SST-ARLTATTAD), the Tribunal, for a reason that was not explained to this Court, chose to process the applicant’s notice of appeal as an application requesting leave to appeal, with a request for extension.
- Evidence: `disposition` cue `dismissed` at chunk `4667492` offsets `124-133`; context: [19] The applicant clearly used the wrong appeal form – his appeal required leave first, since the General Division had not dismissed his appeal summarily.
- Evidence: `issue` cue `question` at chunk `4667493` offsets `691-699`; context: (2) If a question of procedure that is not dealt with by these Regulations arises in a proceeding, the Tribunal must proceed by way of analogy to these Regulations.

#### 13554:1:subtheme:6 · paragraphs 21-23

- Raw key terms: `appeal, division, leave, member, applicant, application, decision, extension`
- Display key terms: `division, leave, extension`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, reasoning_application Display terms: division, leave, extension Rule/authority context: [21] The decision whose legality is now under review by this Court was rendered by the Tribunal on February 3, 2015. Application context: He therefore sent the documents a second time in July 2014. | The member therefore refused the applicant leave to appeal, hence this application for judicial review. Operative outcome context: The member of the Appeal Division began by considering whether an extension of time to file the request for leave to appeal should be granted. Evidence spans paragraphs 21-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4667494` offsets `172-179`; context: The member of the Appeal Division began by considering whether an extension of time to file the request for leave to appeal should be granted.
- Evidence: `governing_rule` cue `under` at chunk `4667494` offsets `40-45`; context: [21] The decision whose legality is now under review by this Court was rendered by the Tribunal on February 3, 2015.
- Evidence: `disposition` cue `granted` at chunk `4667494` offsets `251-258`; context: The member of the Appeal Division began by considering whether an extension of time to file the request for leave to appeal should be granted.
- Evidence: `reasoning_application` cue `therefore` at chunk `4667495` offsets `235-244`; context: He therefore sent the documents a second time in July 2014.
- Evidence: `reasoning_application` cue `therefore` at chunk `4667496` offsets `255-264`; context: The member therefore refused the applicant leave to appeal, hence this application for judicial review.
- Evidence: `counterargument_limitation` cue `However` at chunk `4667496` offsets `89-96`; context: However, the member of the Appeal Division went on to determine that, without further details, the applicant’s appeal had no reasonable chance of success.

#### 13554:1:subtheme:7 · paragraphs 24-26

- Raw key terms: `application, tribunal, appeal, applicant, case, development, employment, general`
- Display key terms: `case, development, employment`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position Display terms: case, development, employment Position/evidence statements: It is not up to the Member who has to determine whether to grant leave to appeal to clarify the grounds of appeal or to reweigh and reassess the evidence submitted before the General Division. | [25] The applicant argues that the Tribunal failed to observe a principle of natural justice or that the refusal to grant leave to appeal was otherwise unreasonable. Rule/authority context: Nonetheless, according to Rule 303(3), the Court may, on a motion by the Attorney General of Canada, where it is satisfied that the Attorney General is unable or unwilling to act as a respondent after having been named u Operative outcome context: This is challenged by the respondent, who submits that the application for judicial review should be dismissed. Evidence spans paragraphs 24-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4667497` offsets `780-788`; context: To do so, the Tribunal must, in accordance with subsection 58(1) of the Department of Employment and Social Development Act, be able to see a question of law, fact or jurisdiction the answer to which may lead to the setting aside of the decision attacked.
- Evidence: `party_position` cue `submitted` at chunk `4667497` offsets `1575-1584`; context: It is not up to the Member who has to determine whether to grant leave to appeal to clarify the grounds of appeal or to reweigh and reassess the evidence submitted before the General Division.
- Evidence: `evidence_fact` cue `evidence` at chunk `4667497` offsets `1566-1574`; context: It is not up to the Member who has to determine whether to grant leave to appeal to clarify the grounds of appeal or to reweigh and reassess the evidence submitted before the General Division.
- Evidence: `counterargument_limitation` cue `However` at chunk `4667497` offsets `1227-1234`; context: However, he provides no details concerning his ground of appeal.
- Evidence: `party_position` cue `argues` at chunk `4667498` offsets `19-25`; context: [25] The applicant argues that the Tribunal failed to observe a principle of natural justice or that the refusal to grant leave to appeal was otherwise unreasonable.
- Evidence: `disposition` cue `dismissed` at chunk `4667498` offsets `267-276`; context: This is challenged by the respondent, who submits that the application for judicial review should be dismissed.
- Evidence: `governing_rule` cue `under` at chunk `4667499` offsets `496-501`; context: Nonetheless, according to Rule 303(3), the Court may, on a motion by the Attorney General of Canada, where it is satisfied that the Attorney General is unable or unwilling to act as a respondent after having been named under subsection (2), substitute another person or body, including the tribunal in respect of which the application is made, as a respondent in the place of the Attorney General of Canada.

#### 13554:1:subtheme:8 · paragraphs 27-28

- Raw key terms: `administrative, appeal, aptly, attorney, canada, court, general, girouard`
- Display key terms: `administrative, aptly, girouard`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: administrative, aptly, girouard Rule/authority context: However, there is generally no dispute that it is not up to a tribunal whose decision is under review, whether it is an appeal or a judicial review, to vindicate itself, as well as the merit of its decision. Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4667500` offsets `675-682`; context: However, there is generally no dispute that it is not up to a tribunal whose decision is under review, whether it is an appeal or a judicial review, to vindicate itself, as well as the merit of its decision.
- Evidence: `governing_rule` cue `under` at chunk `4667500` offsets `661-666`; context: However, there is generally no dispute that it is not up to a tribunal whose decision is under review, whether it is an appeal or a judicial review, to vindicate itself, as well as the merit of its decision.
- Evidence: `counterargument_limitation` cue `However` at chunk `4667500` offsets `572-579`; context: However, there is generally no dispute that it is not up to a tribunal whose decision is under review, whether it is an appeal or a judicial review, to vindicate itself, as well as the merit of its decision.

#### 13554:1:subtheme:9 · paragraphs 29-39

- Raw key terms: `appeal, decision, division, tribunal, applicant, general, leave, made`
- Display key terms: `division, leave, made`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: division, leave, made Position/evidence statements: However, the respondent argues that there was no breach of natural justice and, in the alternative, raises a number of reasons for which the applicant’s appeal had no reasonable chance of success on its merits. | By refusing leave to appeal from the General Division’s decision on the application of sections 29 and 30 of the Employment Insurance Act, the Tribunal ended the matter in dispute with the Commission, which concerned the Rule/authority context: The standard of review of correctness applies to the issue of whether there was a breach of procedural fairness (Canada (Attorney General) v. | The Supreme Court set out a non-exhaustive list of factors that must be considered in determining the content of the duty of procedural fairness: (1) the nature of the decision being made and the process followed in maki Application context: The standard of review of correctness applies to the issue of whether there was a breach of procedural fairness (Canada (Attorney General) v. | It should also be noted that in Employment Insurance matters, one of the Tribunal’s missions is to interpret and apply the Employment Insurance Act. Operative outcome context: That being said, the respondent’s counsel confirmed that there was no instruction to agree to the application for judicial review being allowed if the Court were to take the view that the procedure followed was unjust an | By adapting the new appeal system established in sections 55 to 59 of the Act, Parliament wanted to give the Tribunal similar or even identical powers to those previously granted to the Umpire by subsection 115(2) and se Evidence spans paragraphs 29-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4667502` offsets `105-110`; context: [29] At the start of the hearing, the Court informed the applicant and the respondent’s counsel that the issue of natural justice seemed determinative in this case.
- Evidence: `party_position` cue `argues` at chunk `4667502` offsets `542-548`; context: However, the respondent argues that there was no breach of natural justice and, in the alternative, raises a number of reasons for which the applicant’s appeal had no reasonable chance of success on its merits.
- Evidence: `governing_rule` cue `standard of review` at chunk `4667502` offsets `169-187`; context: The standard of review of correctness applies to the issue of whether there was a breach of procedural fairness (Canada (Attorney General) v.
- Evidence: `reasoning_application` cue `applies` at chunk `4667502` offsets `203-210`; context: The standard of review of correctness applies to the issue of whether there was a breach of procedural fairness (Canada (Attorney General) v.
- Evidence: `disposition` cue `allowed` at chunk `4667502` offsets `922-929`; context: That being said, the respondent’s counsel confirmed that there was no instruction to agree to the application for judicial review being allowed if the Court were to take the view that the procedure followed was unjust and unfair.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4667503` offsets `446-457`; context: The Supreme Court set out a non-exhaustive list of factors that must be considered in determining the content of the duty of procedural fairness: (1) the nature of the decision being made and the process followed in making it; (2) the nature of the statutory scheme and the terms of the statute pursuant to which the body operates; (3) the importance of the decision to the individual or individuals affected; (4) the legitimate expectations of the person challenging the decision; and (5) the choices of procedure made by the agency itself (Baker v Canada (Minister of Citizenship and Immigration), [1999] 2 SCR 817).
- Evidence: `reasoning_application` cue `apply` at chunk `4667504` offsets `273-278`; context: It should also be noted that in Employment Insurance matters, one of the Tribunal’s missions is to interpret and apply the Employment Insurance Act.
- Evidence: `disposition` cue `granted` at chunk `4667504` offsets `480-487`; context: By adapting the new appeal system established in sections 55 to 59 of the Act, Parliament wanted to give the Tribunal similar or even identical powers to those previously granted to the Umpire by subsection 115(2) and section 117 of the Employment Insurance Act, which were repealed on April 1, 2013.
- Evidence: `disposition` cue `allowed` at chunk `4667506` offsets `340-347`; context: Given the high volume of cases heard by the Tribunal, the Tribunal must be allowed a certain amount of administrative flexibility, without compromising the objective of excellence that it has established along with other equally laudable objectives (accessibility, efficiency and speed) (Peak Energy Services Ltd.
- Evidence: `reasoning_application` cue `therefore` at chunk `4667507` offsets `474-483`; context: It is therefore necessary to wait for the leave file prepared by the clerk of the Tribunal to be complete and to allow the member of the Appeal Division to exercise his or her discretion to grant or refuse leave to appeal from a decision of the General Division.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4667508` offsets `375-381`; context: The same assumption cannot be made of employees and other workers who are representing themselves and who are not familiar with the Act and the case law.
- Evidence: `party_position` cue `claim` at chunk `4667509` offsets `335-340`; context: By refusing leave to appeal from the General Division’s decision on the application of sections 29 and 30 of the Employment Insurance Act, the Tribunal ended the matter in dispute with the Commission, which concerned the merits of the monetary claim against the applicant, who is alleged to have voluntarily left his employment after two days of work.
- Evidence: `governing_rule` cue `under` at chunk `4667509` offsets `32-37`; context: [36] In this case, the decision under judicial review was rendered by the Appeal Division.
- Evidence: `party_position` cue `argue` at chunk `4667510` offsets `534-539`; context: After filing his notice of appeal, he was convinced that he would be called upon later to argue the grounds of appeal set out in the form.
- Evidence: `counterargument_limitation` cue `but` at chunk `4667510` offsets `347-350`; context: The applicant, who was not represented by counsel, completed his notice of appeal on the basis of errors of fact and law but did not know he had to give more details about his reasons at this stage of the proceedings.
- Evidence: `disposition` cue `granted` at chunk `4667510` offsets `175-182`; context: [37] The applicant is claiming today that he did not have the opportunity to explain to the Tribunal why leave to appeal the decision of the General Division should have been granted to him by a member of the Appeal Division.
- Evidence: `evidence_fact` cue `evidence` at chunk `4667511` offsets `262-270`; context: It allegedly ignored relevant evidence and accepted a completely erroneous factual interpretation that contradicted what the applicant had reported in his statements to the Commission, particularly with respect to the employment conditions discussed with the employer at the hiring interview.
- Evidence: `governing_rule` cue `under` at chunk `4667511` offsets `690-695`; context: The employer allegedly made false representations, and the applicant had just cause for leaving his employment after two days because it was not suitable employment under the Employment Insurance Act.
- Evidence: `reasoning_application` cue `because` at chunk `4667511` offsets `651-658`; context: The employer allegedly made false representations, and the applicant had just cause for leaving his employment after two days because it was not suitable employment under the Employment Insurance Act.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4667512` offsets `459-468`; context: Without ruling on the merits of the arguments that the applicant wanted to make with respect to his appeal to the Tribunal, I am satisfied that the applicant is genuine, and I have no reason to doubt his statements in his affidavit with respect to his legitimate expectations.
- Evidence: `reasoning_application` cue `because` at chunk `4667512` offsets `58-65`; context: [39] This application for judicial review will be allowed because a serious injustice was done by the Tribunal in this case when it failed to return to the applicant the appeal form that he had completed and that was clearly incomplete.
- Evidence: `disposition` cue `allowed` at chunk `4667512` offsets `50-57`; context: [39] This application for judicial review will be allowed because a serious injustice was done by the Tribunal in this case when it failed to return to the applicant the appeal form that he had completed and that was clearly incomplete.

#### 13554:1:subtheme:10 · paragraphs 40-44

- Raw key terms: `appeal, application, division, leave, additional, applicant, case, chance`
- Display key terms: `division, leave, additional, case, chance`
- Argument roles: `counterargument_limitation, disposition, governing_rule, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, party_position Display terms: division, leave, additional, case, chance Position/evidence statements: [40] Among the things to keep in mind when filing a request to appeal to the Tribunal, the Tribunal’s website states that “if the form is incomplete, the SST will return it to you with a request to complete and return it | [44] From the start, the Tribunal registry should have returned the incorrect form to the applicant and asked him to submit a new form stating not only the grounds of appeal, but also the reasons why leave to appeal shou Rule/authority context: [41] By analogy, before summarily dismissing an appeal under subsection 53(1) of the Act, the General Division must give notice in writing to the appellant and allow reasonable time for submissions. | That being said, form SST-ARLTATTAD contains the following additional comment in section 3 – DECISION UNDER APPEAL (page 4) of the instructions, a comment that is not present in form SST-ATATTAD: Note: Leave to appeal is Operative outcome context: [44] From the start, the Tribunal registry should have returned the incorrect form to the applicant and asked him to submit a new form stating not only the grounds of appeal, but also the reasons why leave to appeal shou Evidence spans paragraphs 40-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submit` at chunk `4667513` offsets `371-377`; context: [40] Among the things to keep in mind when filing a request to appeal to the Tribunal, the Tribunal’s website states that “if the form is incomplete, the SST will return it to you with a request to complete and return it by a certain date,” and that “it is not necessary to have all the information (other than the required information) to support your appeal before you submit your Application Requesting Leave to Appeal to the Appeal Division form.
- Evidence: `governing_rule` cue `under` at chunk `4667514` offsets `55-60`; context: [41] By analogy, before summarily dismissing an appeal under subsection 53(1) of the Act, the General Division must give notice in writing to the appellant and allow reasonable time for submissions.
- Evidence: `governing_rule` cue `UNDER` at chunk `4667515` offsets `508-513`; context: That being said, form SST-ARLTATTAD contains the following additional comment in section 3 – DECISION UNDER APPEAL (page 4) of the instructions, a comment that is not present in form SST-ATATTAD:
Note: Leave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success
- Evidence: `party_position` cue `submit` at chunk `4667517` offsets `117-123`; context: [44] From the start, the Tribunal registry should have returned the incorrect form to the applicant and asked him to submit a new form stating not only the grounds of appeal, but also the reasons why leave to appeal should be granted.
- Evidence: `counterargument_limitation` cue `but` at chunk `4667517` offsets `175-178`; context: [44] From the start, the Tribunal registry should have returned the incorrect form to the applicant and asked him to submit a new form stating not only the grounds of appeal, but also the reasons why leave to appeal should be granted.
- Evidence: `disposition` cue `granted` at chunk `4667517` offsets `226-233`; context: [44] From the start, the Tribunal registry should have returned the incorrect form to the applicant and asked him to submit a new form stating not only the grounds of appeal, but also the reasons why leave to appeal should be granted.

#### 13554:1:subtheme:11 · paragraphs 45-46

- Raw key terms: `appeal, division, fact, form, general, grounds, instructions, made`
- Display key terms: `division, fact, form, grounds, instructions, made`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: division, fact, form, grounds, instructions, made Position/evidence statements: In this case, the applicant submitted only the third ground of appeal indicated in paragraph 58(1)(c) of the Act, which he copied word-for-word in section 3 of form SST-ARLTATTAD. Rule/authority context: In section 3 – DECISION UNDER APPEAL (page 4) of the instructions, the Tribunal states as follows: Section 3 is to be completed using reasons based on the grounds in s. Evidence spans paragraphs 45-46. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4667518` offsets `767-774`; context: (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `evidence_fact` cue `record` at chunk `4667518` offsets `819-825`; context: (1) The only grounds of appeal are that
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
- Evidence: `governing_rule` cue `UNDER` at chunk `4667518` offsets `307-312`; context: In section 3 – DECISION UNDER APPEAL (page 4) of the instructions, the Tribunal states as follows:
Section 3 is to be completed using reasons based on the grounds in s.
- Evidence: `party_position` cue `submitted` at chunk `4667519` offsets `598-607`; context: In this case, the applicant submitted only the third ground of appeal indicated in paragraph 58(1)(c) of the Act, which he copied word-for-word in section 3 of form SST-ARLTATTAD.

#### 13554:1:subtheme:12 · paragraphs 47-48

- Raw key terms: `canada, date, general, allow, allows, another, appeal, applicant`
- Display key terms: `date, allow, allows, another`
- Argument roles: `disposition, issue, party_position`
- Explanation: Observed roles: disposition, issue, party_position Display terms: date, allow, allows, another Position/evidence statements: Within 30 days of the date of this judgment, the applicant will have to duly complete and submit to the Tribunal a new application requesting leave to appeal (form SST-ARLTATTAD) setting out the grounds of appeal, as wel Operative outcome context: Within 30 days of the date of this judgment, the applicant will have to duly complete and submit to the Tribunal a new application requesting leave to appeal (form SST-ARLTATTAD) setting out the grounds of appeal, as wel Evidence spans paragraphs 47-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4667520` offsets `193-200`; context: [47] For all these reasons, I have no hesitation in concluding that the applicant was misled and that there was a breach of procedural fairness such that it is not necessary today to determine whether the impugned decision is reasonable.
- Evidence: `party_position` cue `submit` at chunk `4667520` offsets `771-777`; context: Within 30 days of the date of this judgment, the applicant will have to duly complete and submit to the Tribunal a new application requesting leave to appeal (form SST-ARLTATTAD) setting out the grounds of appeal, as well as the errors of fact and/or law made by the Appeal Division and the specific reasons for which the applicant believes his appeal has a reasonable chance of success and the application for leave to appeal should be granted by the Tribunal.
- Evidence: `disposition` cue `granted` at chunk `4667520` offsets `1118-1125`; context: Within 30 days of the date of this judgment, the applicant will have to duly complete and submit to the Tribunal a new application requesting leave to appeal (form SST-ARLTATTAD) setting out the grounds of appeal, as well as the errors of fact and/or law made by the Appeal Division and the specific reasons for which the applicant believes his appeal has a reasonable chance of success and the application for leave to appeal should be granted by the Tribunal.

#### Section text

Bossé v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2015-10-07
Neutral citation
2015 FC 1142
File numbers
T-339-15
Decision Content
Date: 20151007
Docket: T-339-15
Citation: 2015 FC 1142
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, October 7, 2015
PRESENT: The Honourable Mr. Justice Martineau
BETWEEN:
MARTIN BOSSÉ
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS:

[1] The applicant is seeking to have set aside a decision rendered on February 3, 2015, by a member of the Appeal Division of the Social Security Tribunal of Canada [Tribunal] refusing leave to appeal from a decision of the General Division of the Tribunal, dated April 15, 2014, concerning his Employment Insurance benefits.

[2] This application for judicial review should be allowed. The Court is satisfied in this case that the Tribunal failed to observe a principle of natural justice, procedural fairness or other procedure that it was required by law to observe in the circumstances.

[3] On May 29, 2013, the Canada Employment Insurance Commission [Commission] informed the applicant that he could no longer receive regular Employment Insurance benefits as of October 3, 2010, because he had voluntarily left his employment without just cause, resulting in an overpayment of $16,864 being made to him. The applicant appealed to the Tribunal.

[4] Established under subsection 44(1) of the Department of Employment and Social Development Act, SC 2005, c 34 [Act], the Tribunal is an independent administrative tribunal that provides a fair and impartial appeal process for appeals under the Employment Insurance Act, SC 1996, c 23, the Canada Pension Plan, and the Old Age Security Act, RSC 1985, c O-9. The Tribunal is independent from Employment and Social Development Canada. The Tribunal consists of a General Division and an Appeal Division. Every application to the Tribunal is to be heard before a single member (section 61 of the Act).

[5] The General Division is the first level of appeal. It consists of the Income Security Section and the Employment Insurance Section. Under subsection 54(1), the General Division may dismiss the appeal or confirm, rescind or vary a decision of the Minister or the Commission in whole or in part or give the decision that the Minister or the Commission should have given. This is therefore an appeal as of right. It does not require leave of any sort. The appellant must simply bring the appeal within the prescribed time or must have obtained an extension of time (section 52 of the Act). That being said, under subsection 53(1) of the Act, the General Division can summarily dismiss an appeal if it is satisfied that the appeal has no reasonable chance of success.

[6] In this case, on March 5, 2014, a hearing was held by teleconference before a member of the General Division (Employment Insurance). On April 15, 2014, in a 16-page decision with reasons, the General Division dismissed the applicant’s appeal on the merits, on the grounds that, on October 5, 2010, the applicant had voluntarily left his employment at Canpar Transport without just cause within the meaning of sections 29 and 30 of the Employment Insurance Act. The applicant appealed.

[7] The Appeal Division is the second level of appeal before the Tribunal. The right to appeal a decision of the General Division before the Appeal Division is governed by sections 52 to 59 of the Act. The Appeal Division may dismiss the appeal, give the decision that the General Division should have given, refer the matter back to the General Division for reconsideration in accordance with any directions that the Appeal Division considers appropriate or confirm, rescind or vary the decision of the General Division in whole or in part (subsection 59(1) of the Act).

[8] The appeal before the Appeal Division is a combination of a traditional appeal (error of law) and judicial review (jurisdiction, natural justice, patently unreasonable finding of fact). Section 58 of the Act reads as follows:
58. (1) The only grounds of appeal are that
58. (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.

[9] However, an important legal distinction must be made: although an appellant may appeal as of right to the Appeal Division concerning a decision of the General Division to summarily dismiss an appeal, it is necessary to obtain leave to appeal a decision of the General Division dismissing an appeal on the merits (sections 52 and 56). The test for obtaining leave to appeal is written in negative terms in subsection 58(2) of the Act, which provides that “[l]eave to appeal is refused if the Appeal Division is satisfied that the appeal has no reasonable chance of success”.

[10] According to the case law of the Federal Court and the Federal Court of Appeal upon which the Tribunal relied, at the application for leave stage, the applicant does not have to prove his or her argument. Nevertheless, for an application for leave to appeal to be granted, there must be an “arguable case” (DB v Minister of Employment and Social Development, 2015 SSTAD 806 at para 53; CM v Canada Employment Insurance Commission, 2015 SSTAD 574; Bellefeuille v Canada (Attorney General), 2014 FC 963 at para 29 CanLII [Bellefeuille]; Canada (Attorney General) v Zakaria, [2011] FCJ No 189 at para 37; Fancy v Canada (Attorney General), 2010 FCA 63 at paras 2 and 3; Canada (Minister of Human Resources Development) v Hogervorst, 2007 FCA 41 at para 37 [Hogervorst]; Kerth v Canada (Minister of Human Resources Development), [1999] FCJ No 1252 at para 24).

[11] Regarding the appeal periods, in the case of a decision by the Employment Insurance Section, the notice of appeal (summary dismissal) or the application for leave to appeal (dismissal on the merits) must be made within 30 days after the day on which the decision is communicated to the appellant (paragraph 57(1)(a) of the Act). The Appeal Division may allow further time within which an application for leave to appeal is to be made (subsection 57(2)). If leave to appeal is granted, the application for leave to appeal becomes the notice of appeal and is deemed to have been filed on the day on which the application for leave to appeal was filed (subsection 58(5)).

[12] In practice, the request for an extension of time and the application for leave to appeal will be decided at the same time (MP v Canada Employment Insurance Commission, 2015 SSTAD 626 [MP]; AW v Canada Employment Insurance Commission, 2015 SSTAD 380 [AW]. According to the case law of the Federal Court and the Federal Court of Appeal upon which the Tribunal relied, when the issue to be decided is whether it is appropriate to grant an extension of time to file a notice of appeal, the most important factor is whether it is in the interests of justice that the extension be granted (AW at para 8; Grewal v Canada (Minister of Employment and Immigration), [1985] 2 FC 263 at pages 278-279). The factors that must be considered are the following: (a) there was and is a continuing intention on the part of the party presenting the motion to pursue the appeal; (b) the subject matter of the appeal discloses an arguable case; (c) there is a reasonable explanation for the defaulting party’s delay; and (d) there is no prejudice to the other party in allowing the extension (MP at paras 13 to 16; AW at paras 7 to 9; Hogervorst at paras 32, 37 and 38; X (Re), 2014 FCA 249 at para 26).

[13] From a procedural standpoint, section 58 of the Act does not stipulate the manner in which the appellant must proceed. We must instead look to section 39 and subsection 40(1) of the Social Security Tribunal Regulations, SOR/2013-60 [Regulations], which state as follows:
39. An application for leave to appeal a decision of the General Division is brought by filing the application with the Appeal Division at the address, facsimile number or email address — or in accordance with the electronic filing procedure — provided by the Tribunal on its website.
39. La demande de permission d’appeler d’une décision de la division générale est présentée en déposant la demande d’en appeler à l’adresse, au numéro de télécopieur ou à l’adresse électronique — ou selon les modalités de dépôt électronique — fournis par le Tribunal sur son site Web.
40. (1) An application for leave to appeal must be in the form set out by the Tribunal on its website and contain
40. (1) La demande de permission d’en appeler est présentée selon la forme prévue par le Tribunal sur son site Web et contient :
(a) a copy of the decision in respect of which leave to appeal is being sought;
a) une copie de la décision qui fait l’objet de la demande;
(b) if a person is authorized to represent the applicant, the person’s name, address, telephone number and, if any, facsimile number and email address;
b) si une personne est autorisée à représenter le demandeur, le nom, l’adresse et le numéro de téléphone de cette personne et tout numéro de télécopieur et adresse électronique qu’elle possède;
(c) the grounds for the application;
c) les moyens invoqués à l’appui de la demande;
(d) any statements of fact that were presented to the General Division and that the application relies on in the application;
{d) l’exposé des faits présentés à la division générale que le demandeur entend invoquer à l’appui de la demande;
(e) if the application is brought by a person other than the Minister or the Commission, the applicant’s full name, address, telephone number and, if any, facsimile number and email address;
e) si la demande émane d’une personne autre que le ministre ou la Commission, le nom complet, l’adresse et le numéro de téléphone du demandeur et tout numéro de télécopieur et adresse électronique qu’il possède;
(f) if the application is brought by the Minister or the Commission, the address, telephone number, facsimile number and email address of the Minister or the Commission, as the case may be;
f) si la demande émane du ministre ou de la Commission, les adresse, numéro de téléphone, numéro de télécopieur et adresse électronique du ministre ou de la Commission, selon le cas;
(g) an identifying number of the type specified by the Tribunal on its website for the purpose of the application; and
g) le numéro identificateur du type précisé par le Tribunal sur son site Web aux fins de la demande ;
(h) a declaration that the information provided is true to the best of the applicant’s knowledge.
h) une déclaration selon laquelle les renseignements fournis dans la demande sont, à la connaissance du demandeur, véridiques.

[14] It should be noted that under paragraphs 40(1)(c) and (d) of the Regulations, the application for leave to appeal must include the “grounds for the application” and “any statements of fact that were presented to the General Division” and that the applicant relies on in the application. These are two mandatory fields. On the other hand, in the case of an appeal from a decision of the General Division to summarily dismiss an appeal, the notice of appeal must simply include the “grounds for the appeal,” as well as “any statements of fact that were presented to the General Division” and that the appellant relies on in the appeal (paragraphs 35(1)(c) and (d) of the Regulations).

[15] Moreover, the appeal forms differ in one significant area in the case of an appeal from a summary dismissal (form SST-ATATTAD) and an appeal in other cases that are subject to an application for leave to appeal (form SST-ARLTATTAD).

[16] Therefore, in accordance with the Instructions given by the Tribunal for completing the Application Requesting Leave to Appeal to the Appeal Division form (form SST-ARLTATTAD), available on the website, the appellant must complete fields 3(C) REQUEST FOR LEAVE TO APPEAL - (see instructions on page 1) and 3(D) REASONS FOR THE APPEAL - (see instructions on page 1). In particular, for the Request for Leave to Appeal field, the appellant must complete the following introductory paragraph: “Pursuant to s. 58(2) of the Department of Human Resources and Skills Development Act, I believe my Application Requesting Leave to Appeal to the Appeal Division has a reasonable chance for success because: . . .”.

[17] In addition, for the Reasons for the Appeal field, the appellant must complete the following introductory paragraph: “Based on the grounds in s. 58(1) of the Department of Human Resources and Skills Development Act I am appealing for the following reasons: . . .” (form SST-ARLTATTAD). The same requirement applies in the case of a notice of appeal against a summary dismissal by the General Division (form SST-ATATTAD).

[18] In this case, a first notice of appeal from the April 15, 2014, decision was filed by the applicant within the prescribed time in May 2014, but for a reason that was not explained to this Court, the notice was lost or not received by the Tribunal. Nevertheless, on July 7, 2014, the applicant filed a second notice of appeal. On the form he used to appeal (SST-ATATTAD), the applicant wrote the following in field 3(C) REASONS FOR THE APPEAL: [translation] “[The General Division] based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it”. On August 13, 2014, the applicant filed a third notice of appeal with the Appeal Division, in which he stated this time in field 3(B) REASON(S) FOR LATE APPEAL: [translation] “I am sending you the evidence that I duly sent my papers on 05-02 at 3:34 AM”.

[19] The applicant clearly used the wrong appeal form – his appeal required leave first, since the General Division had not dismissed his appeal summarily. Instead of refusing to accept the form in question (SST-ATATTAD) and returning the appropriate application requesting leave to appeal form to the applicant (SST-ARLTATTAD), the Tribunal, for a reason that was not explained to this Court, chose to process the applicant’s notice of appeal as an application requesting leave to appeal, with a request for extension.‑ This method seems to be permitted by the provisions of the Regulations, as long as it does not cause any prejudice to the applicant and does not prevent the applicant from explaining to the Tribunal why the appeal has a reasonable chance of success.

[20] Sections 3 and 4 of the Regulations stipulate the following:
3. (1) The Tribunal
3. (1) Le Tribunal :
(a) must conduct proceedings as informally and quickly as the circumstances and the considerations of fairness and natural justice permit; and
a) veille à ce que l’instance se déroule de la manière la plus informelle et expéditive que les circonstances, l’équité et la justice naturelle permettent;
(b) may, if there are special circumstances, vary a provision of these Regulations or dispense a party from compliance with a provision.
b) peut, s’il existe des circonstances spéciales, modifier une disposition du présent règlement ou exempter une partie de son application.
(2) If a question of procedure that is not dealt with by these Regulations arises in a proceeding, the Tribunal must proceed by way of analogy to these Regulations.
(2) Il résout par analogie avec le présent règlement toute question de nature procédurale qui, n’y étant pas réglée, est soulevée dans le cadre de l’instance.
4. A party may request the Tribunal to provide for any matter concerning a proceeding, including the extension of a time limit imposed by these Regulations, by filing the request with the Tribunal.
4. À la demande déposée par une partie auprès du Tribunal, celui-ci peut déterminer la règle applicable à toute question relative à l’instance, notamment la prorogation des délais impartis par le présent règlement.

[21] The decision whose legality is now under review by this Court was rendered by the Tribunal on February 3, 2015. The member of the Appeal Division began by considering whether an extension of time to file the request for leave to appeal should be granted.

[22] In that regard, the member of the Appeal Division noted the following:
It appears from the file that the Applicant sent his application for leave to appeal in May 2014 but that the application was not received by the Tribunal. He therefore sent the documents a second time in July 2014. In the circumstances, the Tribunal is of the opinion that the interests of justice favour granting an extension of time to file the Applicant’s application for leave to appeal: X (Re), 2014 FCA 249 (CanLII); Grewal v. Minister of Employment and Immigration, [1985] 2 F.C. 263 (F.C.A.).

[23] The applicant is not challenging this part of the Appeal Division’s decision today. However, the member of the Appeal Division went on to determine that, without further details, the applicant’s appeal had no reasonable chance of success. The member therefore refused the applicant leave to appeal, hence this application for judicial review.

[24] On this point, the member noted the following in his decision:
An application for leave to appeal is a preliminary step to a hearing on the merits. It is a first, and lower, hurdle for the Applicant to meet than the one that must be met on the hearing of the appeal on the merits. At the application for leave to appeal stage, the Applicant does not have to prove his case.
The Tribunal will grant leave to appeal if the Applicant shows that any of the above grounds of appeal [set out in paragraphs (a), (b) and (c) of subsection 58(a) of the Department of Employment and Social Development Act] has a reasonable chance of success.
To do so, the Tribunal must, in accordance with subsection 58(1) of the Department of Employment and Social Development Act, be able to see a question of law, fact or jurisdiction the answer to which may lead to the setting aside of the decision attacked.
In light of the foregoing, does the Applicant’s appeal have a reasonable chance of success?
In his application for leave to appeal, the Applicant states that the General Division based its decision or order on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it. However, he provides no details concerning his ground of appeal. He alleges only that the decision contains errors of fact, without saying what errors of fact were made by the General Division.
It is not up to the Member who has to determine whether to grant leave to appeal to clarify the grounds of appeal or to reweigh and reassess the evidence submitted before the General Division.
The Tribunal has no choice but to find that the appeal has no reasonable chance of success.

[25] The applicant argues that the Tribunal failed to observe a principle of natural justice or that the refusal to grant leave to appeal was otherwise unreasonable. This is challenged by the respondent, who submits that the application for judicial review should be dismissed.

[26] The Court notes that the Minister of Employment and Social Development is not party to the case, and that according to Rule 303(2) of the Federal Courts Rules, SOR/98-106 [Rules], the Attorney General of Canada is the proper respondent in this case: Bell

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 13554:2 · paragraphs 49-49

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `da7eb7d76b7f91c39d7442c7aed3d64a83a1c128836bac5e5a38123a4cf44b9d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 13554:2:subtheme:1 · paragraphs 49-49

- Raw key terms: `appearances, applicant, attorney, behalf, boss, canada, carole, dated`
- Display key terms: `behalf, boss, carole, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: behalf, boss, carole, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 49-49. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
MARTINEAU J.
DATED:
October 7, 2015
APPEARANCES:
Martin Bossé
FOR THE APPLICANT
(ON HIS OWN BEHALF)
Carole Vary
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Martin Bossé
FOR THE APPLICANT
(ON HIS OWN BEHALF)
William F. Pentney
Deputy Attorney General of Canada
Québec, Quebec
FOR THE RESPONDENT
