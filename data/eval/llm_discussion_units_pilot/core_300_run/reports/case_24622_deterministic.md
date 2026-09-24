# Discussion Units: case 24622

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **46**
- Continuity pairs: **45**
- Discussion Units: **2**
- Paragraph source hashes: **46**
- Sub-themes: **12**

## 24622:1 · paragraphs 0-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7be4405ec97a6defe0e4db2f53fbe53eb642789c663d6133e1dafec85b415295`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24622:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `appellate, body, canada, case, court, division, fact, findings`
- Display key terms: `appellate, body, case, division, fact, findings`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: appellate, body, case, division, fact, findings Rule/authority context: [2] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the Refugee Protection Division (RPD) is reasonableness. Application context: [2] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the Refugee Protection Division (RPD) is reasonableness. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5157632` offsets `845-852`; context: Preliminary remarks [1] The Court recognizes that it would be absurd, and contrary to subsection 110(3) of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA), to task the Refugee Appeal Division (RAD) of the Immigration and Refugee Board with re-examining, for every instance, whether the claimants are in fact refugees or persons in need of protection within the meaning of sections 96 and 97 of the IRPA.
- Evidence: `evidence_fact` cue `testimony` at chunk `5157632` offsets `1187-1196`; context: It is clear from the case law that an appellate body cannot substitute its own reasoning for that of a specialized tribunal of first instance, the tribunal of fact, having the advantage of having heard viva voce testimony and with its authority conferred by the Inquiries Act, RS (1985), c I-11, unless the trial judge made a “palpable and overriding error” that led to an erroneous result (Housen v Nikolaisen, 2002 SCC 33, [2002] 2 SCR 235 at para 10).
- Evidence: `governing_rule` cue `standard of review` at chunk `5157633` offsets `75-93`; context: [2] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the Refugee Protection Division (RPD) is reasonableness.
- Evidence: `reasoning_application` cue `applied` at chunk `5157633` offsets `100-107`; context: [2] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the Refugee Protection Division (RPD) is reasonableness.

#### 24622:1:subtheme:2 · paragraphs 2-12

- Raw key terms: `applicant, applicants, brother, principal, accused, appeal, assessment, canada`
- Display key terms: `brother, principal, accused, assessment`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: brother, principal, accused, assessment Position/evidence statements: He was charged, then acquitted, but claims that he continued to be persecuted afterwards. | [10] In September 2012, he claims he was summoned to an interrogation by the Rwandan military police during which he was accused of supporting the Rwandan National Congress (RNC) and of promoting a genocidal ideology. Rule/authority context: Introduction [4] This is an application for judicial review filed pursuant to subsection 72(1) of the IRPA, of a decision dated July 25, 2013, by the RAD dismissing the applicants’ appeal from a decision of the RPD refus | Decision under review [15] In its decision, the RAD began by addressing the admissibility of two pieces of evidence submitted in their appeal – a refugee card belonging to the principal applicant’s brother, Richard Bweng Application context: Relying on the criteria for admissibility applicable in the context of a Pre-Removal Risk Assessment (PRRA) (Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385), the RAD determined that the documents c Operative outcome context: That claim was dismissed by the RPD on April 11, 2013. | The appeal was dismissed on July 25, 2013. Evidence spans paragraphs 2-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5157634` offsets `266-273`; context: [3] That said, the Court finds that in assessing the reasonableness of the decision, the RAD should, at the very least, have reviewed the evidence that was presented before the RPD and conducted an independent assessment of all of the evidence in order to determine whether the RPD, on the basis of the facts and the conditions of the country in question, had properly considered the evidence and reasonably justified its conclusion (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at para 47; Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708 ; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61, [2011] 3 SCR 654).
- Evidence: `evidence_fact` cue `evidence` at chunk `5157634` offsets `138-146`; context: [3] That said, the Court finds that in assessing the reasonableness of the decision, the RAD should, at the very least, have reviewed the evidence that was presented before the RPD and conducted an independent assessment of all of the evidence in order to determine whether the RPD, on the basis of the facts and the conditions of the country in question, had properly considered the evidence and reasonably justified its conclusion (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at para 47; Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708 ; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61, [2011] 3 SCR 654).
- Evidence: `governing_rule` cue `pursuant to` at chunk `5157634` offsets `940-951`; context: Introduction [4] This is an application for judicial review filed pursuant to subsection 72(1) of the IRPA, of a decision dated July 25, 2013, by the RAD dismissing the applicants’ appeal from a decision of the RPD refusing to recognize their claim that they are refugees or persons in need of protection within the meaning of sections 96 and 97 of the IRPA.
- Evidence: `party_position` cue `claims` at chunk `5157636` offsets `177-183`; context: He was charged, then acquitted, but claims that he continued to be persecuted afterwards.
- Evidence: `party_position` cue `claims` at chunk `5157639` offsets `27-33`; context: [10] In September 2012, he claims he was summoned to an interrogation by the Rwandan military police during which he was accused of supporting the Rwandan National Congress (RNC) and of promoting a genocidal ideology.
- Evidence: `party_position` cue `claimed` at chunk `5157641` offsets `114-121`; context: They arrived in Canada on December 21, 2012, and claimed refugee protection.
- Evidence: `disposition` cue `dismissed` at chunk `5157641` offsets `157-166`; context: That claim was dismissed by the RPD on April 11, 2013.
- Evidence: `disposition` cue `dismissed` at chunk `5157642` offsets `72-81`; context: The appeal was dismissed on July 25, 2013.
- Evidence: `party_position` cue `submitted` at chunk `5157643` offsets `227-236`; context: Decision under review [15] In its decision, the RAD began by addressing the admissibility of two pieces of evidence submitted in their appeal – a refugee card belonging to the principal applicant’s brother, Richard Bwenge, and a document relating to a refugee claim by his parents in Uganda.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157643` offsets `218-226`; context: Decision under review [15] In its decision, the RAD began by addressing the admissibility of two pieces of evidence submitted in their appeal – a refugee card belonging to the principal applicant’s brother, Richard Bwenge, and a document relating to a refugee claim by his parents in Uganda.
- Evidence: `governing_rule` cue `under` at chunk `5157643` offsets `120-125`; context: Decision under review [15] In its decision, the RAD began by addressing the admissibility of two pieces of evidence submitted in their appeal – a refugee card belonging to the principal applicant’s brother, Richard Bwenge, and a document relating to a refugee claim by his parents in Uganda.
- Evidence: `reasoning_application` cue `because` at chunk `5157643` offsets `722-729`; context: Relying on the criteria for admissibility applicable in the context of a Pre-Removal Risk Assessment (PRRA) (Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385), the RAD determined that the documents constituted, at first blush, credible, relevant and new evidence, but that they were not admissible because the applicants had not presented complete and detailed observations on the essential nature of the documents.
- Evidence: `counterargument_limitation` cue `but` at chunk `5157643` offsets `688-691`; context: Relying on the criteria for admissibility applicable in the context of a Pre-Removal Risk Assessment (PRRA) (Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385), the RAD determined that the documents constituted, at first blush, credible, relevant and new evidence, but that they were not admissible because the applicants had not presented complete and detailed observations on the essential nature of the documents.
- Evidence: `evidence_fact` cue `determined that` at chunk `5157644` offsets `18-33`; context: [16] The RAD then determined that the RPD had made no error in its assessment of the applicants’ credibility.

#### 24622:1:subtheme:3 · paragraphs 13-15

- Raw key terms: `analysis, decision, appeal, applicants, central, credibility, detailed, erred`
- Display key terms: `analysis, central, credibility, detailed, erred`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: analysis, central, credibility, detailed, erred Position/evidence statements: The applicants contend that the RAD had an obligation to review the new evidence they had submitted as part of their appeal, as the file met these criteria; in particular, it raised a serious issue with respect to the ap | [23] The respondent asserts that the RAD’s analysis was detailed and clear, and that the elements the RAD covered in its reasons were sufficient to demonstrate that its decision is reasonable. Rule/authority context: Referrals Renvoi (2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that (2) Elle ne peut procéder au renvoi que si elle estime, à la fois : (a) the decision  | [22] The applicants further allege that the RAD erred in its analysis of the criteria regarding the admissibility of new evidence under subsection 110(4) of the IRPA. Application context: Relevant statutory provisions [19] The following sections of the IRPA apply to this case: 96. Evidence spans paragraphs 13-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `5157645` offsets `344-349`; context: Issue [18] Is the decision of the RAD reasonable?
- Evidence: `evidence_fact` cue `determined that` at chunk `5157645` offsets `21-36`; context: [17] Lastly, the RAD determined that the RPD had not shown apparent bias, as the applicants alleged.
- Evidence: `governing_rule` cue `under` at chunk `5157645` offsets `6674-6679`; context: Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `reasoning_application` cue `apply` at chunk `5157645` offsets `468-473`; context: Relevant statutory provisions [19] The following sections of the IRPA apply to this case:
96.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5157645` offsets `6651-6657`; context: Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
- Evidence: `issue` cue `issue` at chunk `5157646` offsets `359-364`; context: The applicants contend that the RAD had an obligation to review the new evidence they had submitted as part of their appeal, as the file met these criteria; in particular, it raised a serious issue with respect to the applicants’ credibility that was central to the decision.
- Evidence: `party_position` cue `contend` at chunk `5157646` offsets `182-189`; context: The applicants contend that the RAD had an obligation to review the new evidence they had submitted as part of their appeal, as the file met these criteria; in particular, it raised a serious issue with respect to the applicants’ credibility that was central to the decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157646` offsets `121-129`; context: [22] The applicants further allege that the RAD erred in its analysis of the criteria regarding the admissibility of new evidence under subsection 110(4) of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `5157646` offsets `130-135`; context: [22] The applicants further allege that the RAD erred in its analysis of the criteria regarding the admissibility of new evidence under subsection 110(4) of the IRPA.
- Evidence: `party_position` cue `asserts` at chunk `5157647` offsets `20-27`; context: [23] The respondent asserts that the RAD’s analysis was detailed and clear, and that the elements the RAD covered in its reasons were sufficient to demonstrate that its decision is reasonable.

#### 24622:1:subtheme:4 · paragraphs 16-18

- Raw key terms: `agree, case, court, irpa, jurisdiction, subsection, although, analyse`
- Display key terms: `agree, case, irpa, jurisdiction, subsection, although, analyse`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: agree, case, irpa, jurisdiction, subsection, although, analyse Position/evidence statements: [24] The respondent submits that the RAD did not fail to exercise its jurisdiction when it limited its analysis to the reasons of the RPD. Rule/authority context: [27] In this case, it is a matter of interpreting the IRPA and, in particular, of determining the role of the RAD under subsection 111(1) of the IRPA. Application context: This case therefore identifies a need to reflect on this issue. Evidence spans paragraphs 16-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5157648` offsets `418-424`; context: Analysis [25] The applicants raised a number of issues, and although the Court does not agree with their position on every one of these issues, it does agree with the applicants that the RAD erred when it asserted that reassessing the evidence was not within its jurisdiction (Reasons and decision at para 71).
- Evidence: `party_position` cue `submits` at chunk `5157648` offsets `20-27`; context: [24] The respondent submits that the RAD did not fail to exercise its jurisdiction when it limited its analysis to the reasons of the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157648` offsets `262-270`; context: The respondent posits that neither subsection 110(3) nor section 111 of the IRPA require the RAD to analyse every piece of evidence that was before the RPD.
- Evidence: `counterargument_limitation` cue `although` at chunk `5157648` offsets `430-438`; context: Analysis [25] The applicants raised a number of issues, and although the Court does not agree with their position on every one of these issues, it does agree with the applicants that the RAD erred when it asserted that reassessing the evidence was not within its jurisdiction (Reasons and decision at para 71).
- Evidence: `issue` cue `issue` at chunk `5157649` offsets `162-167`; context: This case therefore identifies a need to reflect on this issue.
- Evidence: `reasoning_application` cue `therefore` at chunk `5157649` offsets `115-124`; context: This case therefore identifies a need to reflect on this issue.
- Evidence: `governing_rule` cue `under` at chunk `5157650` offsets `114-119`; context: [27] In this case, it is a matter of interpreting the IRPA and, in particular, of determining the role of the RAD under subsection 111(1) of the IRPA.

#### 24622:1:subtheme:5 · paragraphs 19-20

- Raw key terms: `articulated, construction, context, court, driedger, entire, follow, formulation`
- Display key terms: `articulated, construction, context, driedger, entire, follow, formulation`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: articulated, construction, context, driedger, entire, follow, formulation Evidence spans paragraphs 19-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5157651` offsets `124-132`; context: [28] For the reasons that follow, the Court is of the view that a plain reading of the IRPA with regard to the provision in question does not permit the formulation articulated by the RAD.

#### 24622:1:subtheme:6 · paragraphs 21-31

- Raw key terms: `subsection, jurisdiction, appeal, decision, made, substitute, canada, irpa`
- Display key terms: `subsection, jurisdiction, made, substitute, irpa`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: subsection, jurisdiction, made, substitute, irpa Position/evidence statements: [28] The applicant submits that the only role of the IAD in a challenge of the legal validity of the visa officer’s decision is to determine the reasonableness of the officer’s decision on excessive demand at the time th Rule/authority context: [29] In my view the applicant has mischaracterized the role of the IAD in an appeal under subsection 67(2) of IRPA. Application context: [31] The RAD therefore has the authority to undertake its own analysis of the evidence and, indeed, to substitute the impugned decision with a determination that should have been made. | The IAD therefore exceeded its jurisdiction by not limiting itself to assessing the reasonableness of the officer’s decision at the time it was made. Evidence spans paragraphs 21-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5157653` offsets `222-229`; context: [30] Applying these rules regarding the interpretation of statutes to subsection 111(1), it is clear that Parliament’s intention was to allow the RAD to render decisions on the merits of an appeal and not merely to decide whether the RPD reached its conclusion in a “reasonable” manner as the member stated in this matter.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157654` offsets `78-86`; context: [31] The RAD therefore has the authority to undertake its own analysis of the evidence and, indeed, to substitute the impugned decision with a determination that should have been made.
- Evidence: `reasoning_application` cue `therefore` at chunk `5157654` offsets `13-22`; context: [31] The RAD therefore has the authority to undertake its own analysis of the evidence and, indeed, to substitute the impugned decision with a determination that should have been made.
- Evidence: `party_position` cue `submits` at chunk `5157657` offsets `19-26`; context: [28] The applicant submits that the only role of the IAD in a challenge of the legal validity of the visa officer’s decision is to determine the reasonableness of the officer’s decision on excessive demand at the time that the decision is made.
- Evidence: `reasoning_application` cue `therefore` at chunk `5157657` offsets `253-262`; context: The IAD therefore exceeded its jurisdiction by not limiting itself to assessing the reasonableness of the officer’s decision at the time it was made.
- Evidence: `governing_rule` cue `under` at chunk `5157658` offsets `84-89`; context: [29] In my view the applicant has mischaracterized the role of the IAD in an appeal under subsection 67(2) of IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157661` offsets `200-208`; context: The Court is mindful of the fact that the IRPA limits the power of the RAD, contrary to that of the IAD, to consider new evidence and to hold a hearing only in exceptional cases (see subsections 110(4) and 110(6)).
- Evidence: `reasoning_application` cue `therefore` at chunk `5157661` offsets `358-367`; context: The nature of the proceeding set out at subsection 67(2) cannot therefore be considered as being perfectly analogous to that in subsection 111(1) in all cases.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5157661` offsets `351-357`; context: The nature of the proceeding set out at subsection 67(2) cannot therefore be considered as being perfectly analogous to that in subsection 111(1) in all cases.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157663` offsets `102-110`; context: [37] In this case, the articulation of the RAD’s decision does not show that it considered all of the evidence presented to the RPD or that it conducted its own analysis of it.

#### 24622:1:subtheme:7 · paragraphs 32-34

- Raw key terms: `body, court, made, above, appellate, canada, case, fact`
- Display key terms: `body, made, above, appellate, case, fact`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: body, made, above, appellate, case, fact Rule/authority context: [38] In the words of Justice Karen Sharlow, in Kumar v Canada, 2004 FCA 399, 135 ACWS (3d) 554 at paragraph 17, the role of an appeal body “is to determine whether the Judge who made the order under appeal complied with  | [40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness. Application context: ” The Court fails to see how the RAD, having itself not considered the evidence, was able to conclude that the RPD had properly considered it. | [40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness. Evidence spans paragraphs 32-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5157664` offsets `156-163`; context: [38] In the words of Justice Karen Sharlow, in Kumar v Canada, 2004 FCA 399, 135 ACWS (3d) 554 at paragraph 17, the role of an appeal body “is to determine whether the Judge who made the order under appeal complied with the law and properly considered the evidence submitted.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157664` offsets `256-264`; context: [38] In the words of Justice Karen Sharlow, in Kumar v Canada, 2004 FCA 399, 135 ACWS (3d) 554 at paragraph 17, the role of an appeal body “is to determine whether the Judge who made the order under appeal complied with the law and properly considered the evidence submitted.
- Evidence: `governing_rule` cue `under` at chunk `5157664` offsets `193-198`; context: [38] In the words of Justice Karen Sharlow, in Kumar v Canada, 2004 FCA 399, 135 ACWS (3d) 554 at paragraph 17, the role of an appeal body “is to determine whether the Judge who made the order under appeal complied with the law and properly considered the evidence submitted.
- Evidence: `reasoning_application` cue `conclude` at chunk `5157664` offsets `368-376`; context: ” The Court fails to see how the RAD, having itself not considered the evidence, was able to conclude that the RPD had properly considered it.
- Evidence: `counterargument_limitation` cue `fails` at chunk `5157664` offsets `287-292`; context: ” The Court fails to see how the RAD, having itself not considered the evidence, was able to conclude that the RPD had properly considered it.
- Evidence: `issue` cue `whether` at chunk `5157665` offsets `141-148`; context: [39] The Court recognizes that it would be absurd, and contrary to subsection 110(3), to task the RAD with re-examining, for every instance, whether the claimants are in fact refugees or persons in need of protection within the meaning of sections 96 and 97 of the IRPA.
- Evidence: `evidence_fact` cue `testimony` at chunk `5157665` offsets `483-492`; context: It is clear from the case law that an appellate body cannot substitute its own reasoning for that of a specialized tribunal of first instance, the tribunal of fact, having the advantage of having heard viva voce testimony and with its authority conferred by the Inquiries Act, unless the trial judge made a “palpable and overriding error” that led to an erroneous result (Housen, above at para 10).
- Evidence: `governing_rule` cue `standard of review` at chunk `5157666` offsets `76-94`; context: [40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness.
- Evidence: `reasoning_application` cue `applied` at chunk `5157666` offsets `101-108`; context: [40] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the RPD is reasonableness.

#### 24622:1:subtheme:8 · paragraphs 35-36

- Raw key terms: `court, decision, evidence, above, according, address, alberta, applicants`
- Display key terms: `above, according, address, alberta`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: above, according, address, alberta Position/evidence statements: However, the Court will briefly address the RAD’s decision to refuse fresh evidence submitted by the applicants, given that there is no case law on this point. Evidence spans paragraphs 35-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5157667` offsets `267-274`; context: [41] That said, the Court finds that in assessing the reasonableness of the decision, the RAD should, at the very least, have reviewed the evidence that was presented before the RPD and conducted an independent assessment of all of the evidence in order to determine whether the RPD, on the basis of the facts and the conditions of the country in question, had properly considered the evidence and reasonably justified its conclusion (Dunsmuir, above; Newfoundland and Labrador Nurses’ Union, above; Alberta Teachers’ Association, above).
- Evidence: `evidence_fact` cue `evidence` at chunk `5157667` offsets `139-147`; context: [41] That said, the Court finds that in assessing the reasonableness of the decision, the RAD should, at the very least, have reviewed the evidence that was presented before the RPD and conducted an independent assessment of all of the evidence in order to determine whether the RPD, on the basis of the facts and the conditions of the country in question, had properly considered the evidence and reasonably justified its conclusion (Dunsmuir, above; Newfoundland and Labrador Nurses’ Union, above; Alberta Teachers’ Association, above).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `5157667` offsets `615-621`; context: According to this trio of judgments by the Supreme Court of Canada, the RAD cannot exempt itself from considering the evidence as a whole.
- Evidence: `party_position` cue `submitted` at chunk `5157668` offsets `209-218`; context: However, the Court will briefly address the RAD’s decision to refuse fresh evidence submitted by the applicants, given that there is no case law on this point.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157668` offsets `200-208`; context: However, the Court will briefly address the RAD’s decision to refuse fresh evidence submitted by the applicants, given that there is no case law on this point.
- Evidence: `counterargument_limitation` cue `However` at chunk `5157668` offsets `125-132`; context: However, the Court will briefly address the RAD’s decision to refuse fresh evidence submitted by the applicants, given that there is no case law on this point.

#### 24622:1:subtheme:9 · paragraphs 37-38

- Raw key terms: `admissibility, case, court, evidence, fresh, prra, accessibles, acws`
- Display key terms: `admissibility, case, fresh, prra, accessibles, acws`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: admissibility, case, fresh, prra, accessibles, acws Rule/authority context: [43] First, as in the case of a PRRA, the Court finds that the standard of review to be applied to the RAD’s decision with respect to the admissibility of fresh evidence is that of reasonableness. Application context: [43] First, as in the case of a PRRA, the Court finds that the standard of review to be applied to the RAD’s decision with respect to the admissibility of fresh evidence is that of reasonableness. Evidence spans paragraphs 37-38. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5157669` offsets `379-387`; context: As Justice de Montigny noted in Elezi v Canada (Minister of Citizenship and Immigration), 2007 FC 240, 156 ACWS (3d) 426, applying a provision to the particular facts of a case is a question of mixed fact and law, to be reviewed on a standard of reasonableness (at para 20).
- Evidence: `evidence_fact` cue `evidence` at chunk `5157669` offsets `161-169`; context: [43] First, as in the case of a PRRA, the Court finds that the standard of review to be applied to the RAD’s decision with respect to the admissibility of fresh evidence is that of reasonableness.
- Evidence: `governing_rule` cue `standard of review` at chunk `5157669` offsets `63-81`; context: [43] First, as in the case of a PRRA, the Court finds that the standard of review to be applied to the RAD’s decision with respect to the admissibility of fresh evidence is that of reasonableness.
- Evidence: `reasoning_application` cue `applied` at chunk `5157669` offsets `88-95`; context: [43] First, as in the case of a PRRA, the Court finds that the standard of review to be applied to the RAD’s decision with respect to the admissibility of fresh evidence is that of reasonableness.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157670` offsets `148-156`; context: [44] In this case, the Court agrees with the RAD that the wording of subsection 110(4) is very similar to that governing the admissibility of fresh evidence in the context of a PRRA at paragraph 113(a):
110 (4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection
110.

#### 24622:1:subtheme:10 · paragraphs 39-41

- Raw key terms: `evidence, affected, application, arose, considering, credible, established, hearing`
- Display key terms: `affected, arose, considering, credible, established, hearing`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: affected, arose, considering, credible, established, hearing Rule/authority context: [46] The legal test for new evidence under paragraph 113(a) is set forth in Raza, below: Application context: (b) If the evidence is capable of proving an event that occurred or circumstances that arose after the RPD hearing, then the evidence must be considered (unless it is rejected because it is not credible, not relevant, no Evidence spans paragraphs 39-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5157671` offsets `132-140`; context: [45] Considering the dearth of case law interpreting subsection 110(4) and given the essential similarity between the provisions in question, the Court does not find it unreasonable for the RAD to have referred to the factors set out in Raza, above, to analyse the admissibility of fresh evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157671` offsets `288-296`; context: [45] Considering the dearth of case law interpreting subsection 110(4) and given the essential similarity between the provisions in question, the Court does not find it unreasonable for the RAD to have referred to the factors set out in Raza, above, to analyse the admissibility of fresh evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157672` offsets `28-36`; context: [46] The legal test for new evidence under paragraph 113(a) is set forth in Raza, below:
- Evidence: `governing_rule` cue `legal test` at chunk `5157672` offsets `9-19`; context: [46] The legal test for new evidence under paragraph 113(a) is set forth in Raza, below:
- Evidence: `evidence_fact` cue `evidence` at chunk `5157673` offsets `168-176`; context: [13] As I read paragraph 113(a), it is based on the premise that a negative refugee determination by the RPD must be respected by the PRRA officer, unless there is new evidence of facts that might have affected the outcome of the RPD hearing if the evidence had been presented to the RPD.
- Evidence: `reasoning_application` cue `because` at chunk `5157673` offsets `2139-2146`; context: (b) If the evidence is capable of proving an event that occurred or circumstances that arose after the RPD hearing, then the evidence must be considered (unless it is rejected because it is not credible, not relevant, not new or not material).

#### 24622:1:subtheme:11 · paragraphs 42-43

- Raw key terms: `conclusion, matter, probably, according, although, applicants, arrived, articulation`
- Display key terms: `conclusion, matter, probably, according, although, arrived, articulation`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: conclusion, matter, probably, according, although, arrived, articulation Application context: [48] Although the RAD probably fulfilled its substantive duty according to the conclusion at which it arrived, the matter is referred back to the RAD solely because of the articulation of the reasons for its decision. Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5157674` offsets `121-129`; context: [47] In the present matter, the Court considers that even if the RPD had been aware of the two new pieces of evidence in question, it is highly doubtful that these two elements, in and of themselves, would have been determinative of this case.
- Evidence: `evidence_fact` cue `evidence` at chunk `5157674` offsets `109-117`; context: [47] In the present matter, the Court considers that even if the RPD had been aware of the two new pieces of evidence in question, it is highly doubtful that these two elements, in and of themselves, would have been determinative of this case.
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `5157674` offsets `256-268`; context: There were, nevertheless, a number of flaws with regard to the applicants’ credibility which remain unresolved to this day.
- Evidence: `reasoning_application` cue `because` at chunk `5157675` offsets `157-164`; context: [48] Although the RAD probably fulfilled its substantive duty according to the conclusion at which it arrived, the matter is referred back to the RAD solely because of the articulation of the reasons for its decision.

#### Section text

Iyamuremye v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-05-26
Neutral citation
2014 FC 494
File numbers
IMM-5282-13
Notes
Reported Decision
Decision Content
Date: 20140526
Docket: IMM-5282-13
Citation: 2014 FC 494
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, May 26, 2014
PRESENT: The Honourable Mr. Justice Shore
BETWEEN:
OSCAR IYAMUREMYE
JEAN DE DIEU NTIBESHYA
JEANINE UMUHIRE
KARABO GRETA INEZA
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Preliminary remarks [1] The Court recognizes that it would be absurd, and contrary to subsection 110(3) of the Immigration and Refugee Protection Act, SC 2001, c 27 (IRPA), to task the Refugee Appeal Division (RAD) of the Immigration and Refugee Board with re-examining, for every instance, whether the claimants are in fact refugees or persons in need of protection within the meaning of sections 96 and 97 of the IRPA. It is clear from the case law that an appellate body cannot substitute its own reasoning for that of a specialized tribunal of first instance, the tribunal of fact, having the advantage of having heard viva voce testimony and with its authority conferred by the Inquiries Act, RS (1985), c I-11, unless the trial judge made a “palpable and overriding error” that led to an erroneous result (Housen v Nikolaisen, 2002 SCC 33, [2002] 2 SCR 235 at para 10). As Justice Gérard Vincent La Forest of the Supreme Court of Canada reminds us in Schwartz v Canada, [1996] 1 SCR 254, citing Beaudoin-Daigneault v Richard, [1984] 1 RCS 2, at paragraph 33, an appellate court:
… will be justified in disturbing the trial judge's findings of fact only if a specific and identifiable error made by the trial judge convinces it that the conclusion of fact reached is unreasonable, and not one that constitutes a mere divergence of opinion as to the assessment of the balance of probabilities. [Emphasis added.]

[2] In this case, the Court is entirely in agreement with the RAD that the standard of review to be applied to findings of fact made by the Refugee Protection Division (RPD) is reasonableness. It is well established that an appellate body must review the findings of a trial court by applying a correctness standard to findings that involve questions of law, and by applying a reasonableness standard to those involving questions of mixed fact and law (Canada (Attorney General) v White, 2011 FCA 190, 423 NR 251 at para 2; see also, Budhai v Canada (Attorney General), 2002 FCA 298, [2003] 2 FC 57 and Edmonton (Police Service) v Furlong, 2013 ABCA 121).

[3] That said, the Court finds that in assessing the reasonableness of the decision, the RAD should, at the very least, have reviewed the evidence that was presented before the RPD and conducted an independent assessment of all of the evidence in order to determine whether the RPD, on the basis of the facts and the conditions of the country in question, had properly considered the evidence and reasonably justified its conclusion (Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190 at para 47; Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708 ; Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61, [2011] 3 SCR 654). According to this trio of judgments by the Supreme Court of Canada, the RAD cannot exempt itself from considering the evidence as a whole.
II. Introduction [4] This is an application for judicial review filed pursuant to subsection 72(1) of the IRPA, of a decision dated July 25, 2013, by the RAD dismissing the applicants’ appeal from a decision of the RPD refusing to recognize their claim that they are refugees or persons in need of protection within the meaning of sections 96 and 97 of the IRPA.
III. Facts [5] The principal applicant, Oscar Iyamuremye, his spouse, Jeannine Umuhire, her minor daughter, Karabo Greta Ineza, and her brother, Jean de Dieu Ntibeshya, are all Rwandan citizens. The principal applicant and his brother are reportedly of mixed Hutu and Tutsi origin.

[6] The applicants were allegedly persecuted during the Rwandan genocide in 1994, and several members of their family were killed.

[7] The principal applicant states that his father, a Hutu, and other members of his family, testified before the Gacaca after the genocide. He was charged, then acquitted, but claims that he continued to be persecuted afterwards.

[8] The principal applicant further states that his brother, Jean, suffered ill-treatment and was threatened, having been accused of being an opponent of the government. His brother left Rwanda for the United States in September 2010, and remained there for two years. Shortly after his brother’s departure, the applicant was purportedly approached by his employer, the Ministry of the Public Service, with regard to his political allegiance.

[9] In July 2012, his employer allegedly accused him of failing to deliver a project on time and of awarding a supply procurement contract to an opponent of the government.

[10] In September 2012, he claims he was summoned to an interrogation by the Rwandan military police during which he was accused of supporting the Rwandan National Congress (RNC) and of promoting a genocidal ideology. He further states that he was questioned about his brother, Jean, and about his political allegiance. Later, the military police reportedly conducted an illegal search of the applicant’s home.

[11] In November 2012, the applicant alleges that he was the victim of an attempted kidnapping by the military police.

[12] The applicants left Rwanda for Canada on December 15, 2012. They arrived in Canada on December 21, 2012, and claimed refugee protection. That claim was dismissed by the RPD on April 11, 2013.

[13] On May 8, 2013, the applicants appealed to the RAD. The appeal was dismissed on July 25, 2013.

[14] On August 9, 2013, the applicants filed the present application for judicial review of that decision.
IV. Decision under review [15] In its decision, the RAD began by addressing the admissibility of two pieces of evidence submitted in their appeal – a refugee card belonging to the principal applicant’s brother, Richard Bwenge, and a document relating to a refugee claim by his parents in Uganda. Relying on the criteria for admissibility applicable in the context of a Pre-Removal Risk Assessment (PRRA) (Raza v Canada (Minister of Citizenship and Immigration), 2007 FCA 385), the RAD determined that the documents constituted, at first blush, credible, relevant and new evidence, but that they were not admissible because the applicants had not presented complete and detailed observations on the essential nature of the documents. It further noted that these documents did not include evidence that, in and of itself, would be determinative of the applicants’ refugee protection claim.

[16] The RAD then determined that the RPD had made no error in its assessment of the applicants’ credibility. The RAD found that the RPD had justified its reasons for having arrived at the conclusion that the applicants were not credible, having regard for the evidence as a whole, including the explanations offered by the applicants.

[17] Lastly, the RAD determined that the RPD had not shown apparent bias, as the applicants alleged. The RAD noted that after carefully reviewing the transcript of excerpts from the hearing, there was no conduct that derogated from the standard that an informed and reasonable observer could interpret as constituting an appearance of bias.
V. Issue [18] Is the decision of the RAD reasonable?
VI. Relevant statutory provisions [19] The following sections of the IRPA apply to this case:
96. A Convention refugee is a person who, by reason of a well‑founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles‑ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
Person in need of protection
Personne à protéger
(2) A person in Canada who is a member of a class of persons prescribed by the regulations as being in need of protection is also a person in need of protection.
(2) A également qualité de personne à protéger la personne qui se trouve au Canada et fait partie d’une catégorie de personnes auxquelles est reconnu par règlement le besoin de protection.
…
[…]
110. (4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
110. (4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
…
[…]
(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
c) à supposer qu’ils soient admis, justifieraient que la demande d’asile soit accordée ou refusée, selon le cas.
…
[…]
111. (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
111. (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate.
Referrals
Renvoi
(2) The Refugee Appeal Division may make the referral described in paragraph (1)(c) only if it is of the opinion that
(2) Elle ne peut procéder au renvoi que si elle estime, à la fois :
(a) the decision of the Refugee Protection Division is wrong in law, in fact or in mixed law and fact; and
a) que la décision attaquée de la Section de la protection des réfugiés est erronée en droit, en fait ou en droit et en fait;
(b) it cannot make a decision under paragraph 111(1)(a) or (b) without hearing evidence that was presented to the Refugee Protection Division.
b) qu’elle ne peut confirmer la décision attaquée ou casser la décision et y substituer la décision qui aurait dû être rendue sans tenir une nouvelle audience en vue du réexamen des éléments de preuve qui ont été présentés à la Section de la protection des réfugiés.
VII. Standard of review [20] The main issue before the Court, as submitted by the applicants, is whether the RAD erred in its interpretation of its jurisdiction. As the question that arises is a question of law, the decision of the RAD is reviewable on a standard of correctness (Housen, above; Canada v Toney, 2013 FCA 217, 448 NR 175 at para 5).
VIII. The parties’ positions [21] The applicants submit that the RAD erred by determining that it did not have jurisdiction to reassess the evidence that was before the RPD, thus failing to exercise its jurisdiction. They assert that the RAD’s role as an appellate body differs from that of the Federal Court with respect to judicial review. The RAD could not restrict itself to assessing the “reasonableness” of the RPD’s decision—it ought to have proceeded with a thorough and detailed review of each piece of evidence and every argument that was before the RPD (pursuant to subsection 110(3) and section 111 of the IRPA). The applicants argue that the RAD in this case essentially limited itself to repeating the RPD’s findings, without conducting a proper analysis of the arguments or the evidence in the record.

[22] The applicants further allege that the RAD erred in its analysis of the criteria regarding the admissibility of new evidence under subsection 110(4) of the IRPA. The applicants contend that the RAD had an obligation to review the new evidence they had submitted as part of their appeal, as the file met these criteria; in particular, it raised a serious issue with respect to the applicants’ credibility that was central to the decision.

[23] The respondent asserts that the RAD’s analysis was detailed and clear, and that the elements the RAD covered in its reasons were sufficient to demonstrate that its decision is reasonable.

[24] The respondent submits that the RAD did not fail to exercise its jurisdiction when it limited its analysis to the reasons of the RPD. The respondent posits that neither subsection 110(3) nor section 111 of the IRPA require the RAD to analyse every piece of evidence that was before the RPD. These provisions simply set out the framework of the RAD’s authority.
IX. Analysis [25] The applicants raised a number of issues, and although the Court does not agree with their position on every one of these issues, it does agree with the applicants that the RAD erred when it asserted that reassessing the evidence was not within its jurisdiction (Reasons and decision at para 71).

[26] The Court notes that, to this day there is no case law with respect to the jurisdiction of the RAD. This case therefore identifies a need to reflect on this issue.

[27] In this case, it is a matter of interpreting the IRPA and, in particular, of determining the role of the RAD under subsection 111(1) of the IRPA. The parties agree that the key provision here is subsection 111(1).

[28] For the reasons that follow, the Court is of the view that a plain reading of the IRPA with regard to the provision in question does not permit the formulation articulated by the RAD.

[29] It is settled law that the words of a statute are to be read in their entire context and in their grammatical and ordinary sense harmoniously with the scheme of the statute, the object of the statute and the intention of Parliament (Rizzo & Rizzo Shoes Ltd, [1998] 1 SCR 27; see also, E.A. Driedger, Construction of Statutes (2nd Ed 1983) at p. 87).

[30] Applying these rules regarding the interpretation of statutes to subsection 111(1), it is clear that Parliament’s intention was to allow the RAD to render decisions on the merits of an appeal and not merely to decide whether the RPD reached its conclusion in a “reasonable” manner as the member stated in this matter. Subsection 111(1) defines the jurisdiction of the RAD in precise and unequivocal terms:
After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate. [Emphasis added.]

[31] The RAD therefore has the authority to undertake its own analysis of the evidence and, indeed, to substitute the impugned decision with a determination that should have been made.

[32] This interpretation of subsection 111(1) is supported by the near-identical wording of subsection 67(2). Subsection 67(2) reads as follows:
67. (2) If the Immigration Appeal Division allows the appeal, it shall set aside the original decision and substitute a determination that, in its opinion, should have been made, including the making of a removal order, or refer the matter to the appropriate decision-maker for reconsideration.
67. (2) La décision attaquée est cassée; y est substituée celle, accompagnée, le cas échéant, d’une mesure de renvoi, qui aurait dû être rendue, ou l’affaire est renvoyée devant l’instance compétente.

[33] The case law regarding this provision is particularly important here, as it refuses to read subsection 67(2) as conferring upon the Immigration Appeal Division (IAD) a jurisdiction similar to that of a judicial review body (see Canada (Minister of Citizenship and Immigration) v Abdul, 2009 FC 967 at paras 28-31). In Abdul, Justice Michael Kelen writes:

[28] The applicant submits that the only role of the IAD in a challenge of the legal validity of the visa officer’s decision is to determine the reasonableness of the offi

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 24622:2 · paragraphs 44-45

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e391f455a95adb3265116ed6d4fd197600382241dcdae5ad455d6dc13ec322c4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 24622:2:subtheme:1 · paragraphs 44-45

- Raw key terms: `applicants, general, judgment, reasons, shore, allowed, appearances, applicant`
- Display key terms: `shore, allowed`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: shore, allowed Operative outcome context: Conclusion [49] For all of the foregoing reasons, the applicants’ application for judicial review is allowed and the matter is referred back for redetermination before a differently constituted panel. Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5157675` offsets `616-624`; context: There is no question of general importance to be certified.
- Evidence: `disposition` cue `allowed` at chunk `5157675` offsets `322-329`; context: Conclusion [49] For all of the foregoing reasons, the applicants’ application for judicial review is allowed and the matter is referred back for redetermination before a differently constituted panel.

#### Section text

X. Conclusion [49] For all of the foregoing reasons, the applicants’ application for judicial review is allowed and the matter is referred back for redetermination before a differently constituted panel.
JUDGMENT
THE COURT RULES that the applicants’ application for judicial review be allowed and that the matter be referred back for redetermination by a differently constituted panel. There is no question of general importance to be certified.
“Michel M.J. Shore”
Judge
Certified true translation
Sebastian Desbarats, Translator
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-5282-13
STYLE OF CAUSE:
OSCAR IYAMUREMYE, JEAN DE DIEU NTIBESHYA, JEANINE UMUHIRE, KARABO GRETA INEZA v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, QuEbec
DATE OF HEARING:
MAY 13, 2014
JUDGMENT AND REASONS:
SHORE J.
DATED:
MAY 26, 2014
APPEARANCES:
Zofia Przybytkowski
FOR THE APPLICANT
Gretchen Timmins
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Zofia Przybytkowski
Attorney
Montréal, Quebec
FOR THE APPLICANTS
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
