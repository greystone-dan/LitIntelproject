# Discussion Units: case 12438

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **26**
- Continuity pairs: **25**
- Discussion Units: **2**
- Paragraph source hashes: **26**
- Sub-themes: **5**

## 12438:1 · paragraphs 0-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0067e43357bbdd7d2d8df9e76f1b448fc785e84b9a6def887e3512ad7b145dff`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12438:1:subtheme:1 · paragraphs 0-7

- Raw key terms: `applicant, decision, appeal, canada, evidence, irpa, protection, refugee`
- Display key terms: `irpa, protection, refugee`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: irpa, protection, refugee Position/evidence statements: [3] The applicant claims to be persecuted by a Colonel in the Vietnamese Army [the Colonel]. | [4] Fearing for his life, the applicant claimed refugee protection in Canada on April 2, 2013, and a hearing before the Refugee Protection Division [RPD] was held on October 29, 2013. Rule/authority context: Introduction [1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], of a decision of the Refugee Appeal Division [RAD] of the Immi | Impugned decision [8] First, in its reasons, the RAD concluded that the applicant failed to meet his burden of demonstrating the admissibility of the new evidence, pursuant to subsection 110(4) of the IRPA. Application context: [9] In addition, the RAD determined that there were no grounds to hold a hearing because the criteria set out in subsection 110(6) of the IRPA had not been met. Operative outcome context: [7] The RAD dismissed the applicant’s appeal on February 24, 2014. Evidence spans paragraphs 0-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4620921` offsets `526-537`; context: Introduction [1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], of a decision of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board determining that the applicant is neither a “Convention refugee” nor a “person in need of protection” within the meaning of sections 96 and 97 of the IRPA.
- Evidence: `party_position` cue `claims` at chunk `4620922` offsets `18-24`; context: [3] The applicant claims to be persecuted by a Colonel in the Vietnamese Army [the Colonel].
- Evidence: `party_position` cue `claimed` at chunk `4620923` offsets `40-47`; context: [4] Fearing for his life, the applicant claimed refugee protection in Canada on April 2, 2013, and a hearing before the Refugee Protection Division [RPD] was held on October 29, 2013.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620924` offsets `199-207`; context: In particular, the RPD noted “the complete lack of corroborative evidence in support of this refugee protection claim”.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620925` offsets `136-144`; context: In that appeal, the applicant filed two new pieces of evidence, namely, two articles on the current political situation in Vietnam.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620926` offsets `226-234`; context: Impugned decision [8] First, in its reasons, the RAD concluded that the applicant failed to meet his burden of demonstrating the admissibility of the new evidence, pursuant to subsection 110(4) of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4620926` offsets `236-247`; context: Impugned decision [8] First, in its reasons, the RAD concluded that the applicant failed to meet his burden of demonstrating the admissibility of the new evidence, pursuant to subsection 110(4) of the IRPA.
- Evidence: `disposition` cue `dismissed` at chunk `4620926` offsets `12-21`; context: [7] The RAD dismissed the applicant’s appeal on February 24, 2014.
- Evidence: `evidence_fact` cue `determined that` at chunk `4620927` offsets `25-40`; context: [9] In addition, the RAD determined that there were no grounds to hold a hearing because the criteria set out in subsection 110(6) of the IRPA had not been met.
- Evidence: `reasoning_application` cue `because` at chunk `4620927` offsets `81-88`; context: [9] In addition, the RAD determined that there were no grounds to hold a hearing because the criteria set out in subsection 110(6) of the IRPA had not been met.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620928` offsets `276-294`; context: The RAD indicated that although it is not a judicial review court, it must show deference to findings of fact and of mixed fact and law made by the RPD by applying a reasonableness standard of review.
- Evidence: `counterargument_limitation` cue `although` at chunk `4620928` offsets `118-126`; context: The RAD indicated that although it is not a judicial review court, it must show deference to findings of fact and of mixed fact and law made by the RPD by applying a reasonableness standard of review.

#### 12438:1:subtheme:2 · paragraphs 8-10

- Raw key terms: `applicant, application, credibility, evidence, accepted, according, against, alors`
- Display key terms: `credibility, accepted, according, against, alors`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: credibility, accepted, according, against, alors Position/evidence statements: Furthermore, the applicant contends that the RPD and the RAD erred in their assessment of the evidence and from this made unreasonable findings as to the applicant’s credibility. Rule/authority context: [16] According to the applicant, the RAD should have applied a correctness standard of review and should not have shown deference to the RPD’s credibility findings (Canada (Minister of Citizenship and Immigration) v B472 Application context: (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa r | [16] According to the applicant, the RAD should have applied a correctness standard of review and should not have shown deference to the RPD’s credibility findings (Canada (Minister of Citizenship and Immigration) v B472 Evidence spans paragraphs 8-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issues` at chunk `4620929` offsets `255-261`; context: Issues [12] The Court is of the view that the application raises the following issues:
a) Did the RAD err in its assessment of new evidence filed on appeal and with respect to holding a hearing?
- Evidence: `evidence_fact` cue `evidence` at chunk `4620929` offsets `31-39`; context: [11] Lastly, given the lack of evidence corroborating the applicant’s narrative, and the inconsistencies and contradictions found in the record, the RAD was of the view that the RPD committed no error in its assessment of the applicant’s credibility.
- Evidence: `reasoning_application` cue `because` at chunk `4620929` offsets `2914-2921`; context: (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
- Evidence: `issue` cue `question` at chunk `4620930` offsets `323-331`; context: 1) and (2), a person or the Minister may appeal, in accordance with the rules of the Board, on a question of law, of fact or of mixed law and fact, to the Refugee Appeal Division against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620930` offsets `125-133`; context: [14] The following sections of the IRPA set out the applicable criteria with respect to the RAD’s role, the admissibility of evidence on appeal, and on the holding of a hearing:
Appeal
Appel
110.
- Evidence: `party_position` cue `contends` at chunk `4620931` offsets `263-271`; context: Furthermore, the applicant contends that the RPD and the RAD erred in their assessment of the evidence and from this made unreasonable findings as to the applicant’s credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620931` offsets `330-338`; context: Furthermore, the applicant contends that the RPD and the RAD erred in their assessment of the evidence and from this made unreasonable findings as to the applicant’s credibility.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620931` offsets `75-93`; context: [16] According to the applicant, the RAD should have applied a correctness standard of review and should not have shown deference to the RPD’s credibility findings (Canada (Minister of Citizenship and Immigration) v B472, 2013 FC 151).
- Evidence: `reasoning_application` cue `applied` at chunk `4620931` offsets `53-60`; context: [16] According to the applicant, the RAD should have applied a correctness standard of review and should not have shown deference to the RPD’s credibility findings (Canada (Minister of Citizenship and Immigration) v B472, 2013 FC 151).

#### 12438:1:subtheme:3 · paragraphs 11-20

- Raw key terms: `appeal, evidence, above, applicant, canada, citizenship, credibility, hearing`
- Display key terms: `above, credibility, hearing`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, credibility, hearing Rule/authority context: [33] It is therefore apparent that RAD has jurisdiction over any question of law that is presented to it, including the standard of review it should apply. | Furthermore, the onus is on the applicant to justify the holding of a heating and to provide full and detailed submissions to the RAD, as required under paragraph 3(3)(g) of the Rules. Application context: [33] It is therefore apparent that RAD has jurisdiction over any question of law that is presented to it, including the standard of review it should apply. | In addition, the RAD indicated that the evidence filed on appeal was dated November 7 and 25, 2013, and was therefore available before the RPD issued its decision on December 4, 2013. Evidence spans paragraphs 11-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4620932` offsets `65-73`; context: [33] It is therefore apparent that RAD has jurisdiction over any question of law that is presented to it, including the standard of review it should apply.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620932` offsets `555-563`; context: Analysis a) Admissibility of new evidence and the holding of a hearing [18] First, paragraph 3(3))(g) of the Refugee Appeal Division Rules, SOR/2012-257 [Rules], below, states that the appeal record before the RAD must include full and detailed submissions regarding the relevance of the new evidence relied upon in the appeal and whether it meets the requirements of subsection 110(4) of the IRPA.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620932` offsets `120-138`; context: [33] It is therefore apparent that RAD has jurisdiction over any question of law that is presented to it, including the standard of review it should apply.
- Evidence: `reasoning_application` cue `therefore` at chunk `4620932` offsets `11-20`; context: [33] It is therefore apparent that RAD has jurisdiction over any question of law that is presented to it, including the standard of review it should apply.
- Evidence: `evidence_fact` cue `record` at chunk `4620933` offsets `406-412`; context: Content of appellant’s record
Contenu du dossier de l’appelant
(3) The appellant’s record must contain the following documents, on consecutively numbered pages, in the following order:
(3) Le dossier de l’appelant comporte les documents ci-après, sur des pages numérotées consécutivement, dans l’ordre qui suit :
[…]
[…]
(g) a memorandum that includes full and detailed submissions regarding
g) un mémoire qui inclut des observations complètes et détaillées concernant :
(i) the errors that are the grounds of the appeal,
(i) les erreurs commises qui constituent les motifs d’appel,
[…]
[…]
(iii) how any documentary evidence referred to in paragraph (e) meets the requirements of subsection 110(4) of the Act and how that evidence relates to the appellant,
(iii) la façon dont les éléments de preuve documentaire visés à l’alinéa e) sont conformes aux exigences du paragraphe 110(4) de la Loi et la façon dont ils sont liés à l’appelant,
[…]
[…]
(v) why the Division should hold a hearing under subsection 110(6) of the Act if the appellant is requesting that a hearing be held.
- Evidence: `governing_rule` cue `under` at chunk `4620933` offsets `345-350`; context: Furthermore, the onus is on the applicant to justify the holding of a heating and to provide full and detailed submissions to the RAD, as required under paragraph 3(3)(g) of the Rules.
- Evidence: `counterargument_limitation` cue `However` at chunk `4620933` offsets `74-81`; context: However, the RAD may hold a hearing in limited circumstances, in accordance with subsections 110(3) and 110(6) of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620934` offsets `55-63`; context: [20] However, in its reasons, the RAD rejected the new evidence filed by the applicant on the basis that the applicant failed to meet the criteria required under the IRPA and Rules.
- Evidence: `governing_rule` cue `under` at chunk `4620934` offsets `156-161`; context: [20] However, in its reasons, the RAD rejected the new evidence filed by the applicant on the basis that the applicant failed to meet the criteria required under the IRPA and Rules.
- Evidence: `reasoning_application` cue `therefore` at chunk `4620934` offsets `290-299`; context: In addition, the RAD indicated that the evidence filed on appeal was dated November 7 and 25, 2013, and was therefore available before the RPD issued its decision on December 4, 2013.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620935` offsets `37-45`; context: [21] In light of its analysis of the evidence and statutory framework, it was reasonable for the RAD to find the evidence filed by the applicant on appeal inadmissible, on the basis that this evidence failed to meet the requirements set out in the IRPA and Rules.
- Evidence: `reasoning_application` cue `conclude` at chunk `4620935` offsets `316-324`; context: It was also open to, and reasonable for, the RAD to conclude that the circumstances did not warrant the holding of a hearing.
- Evidence: `evidence_fact` cue `testimony` at chunk `4620936` offsets `366-375`; context: It should be noted that the RPD has the considerable advantage of hearing testimony viva voce and weighing the probative value of that testimony and the evidence in the record (Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 at para 33; Spasoja v Canada (Minister of Citizenship and Immigration), 2014 FC 913 at para 40; Alyafi, above, at para 12).
- Evidence: `governing_rule` cue `pursuant to` at chunk `4620936` offsets `249-260`; context: [23] The onus however, is on the appellant to show that the RPD made an error in order for the RAD to substitute a determination that, in its opinion, the RPD should have made or refer the matter back to the RPD for redetermination with directions, pursuant to subsection 111(1) of the IRPA.
- Evidence: `governing_rule` cue `standard of review` at chunk `4620937` offsets `109-127`; context: [24] Contrary to the applicant’s arguments, the Court is of the view that the RAD’s interpretation as to the standard of review applicable to the RPD’s decision is not, in and of itself, determinative.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4620938` offsets `36-49`; context: [25] It has emerged from the recent jurisprudence of this Court that the centrality of the credibility of an applicant in an appeal filed before the RAD may engage a certain level of deference on the part of the RAD with respect to the RPD’s findings.
- Evidence: `evidence_fact` cue `evidence` at chunk `4620940` offsets `240-248`; context: [17] Save for cases in which the credibility of a witness is critical or determinative, or where the RPD enjoys a particular advantage over the RAD in reaching a specific conclusion, the RAD owes no deference to the RPD’s assessment of the evidence: see Huruglica, at paras 37 and 55.

#### 12438:1:subtheme:4 · paragraphs 21-24

- Raw key terms: `assessment, conclusion, conduct, court, credibility, decision, facts, having`
- Display key terms: `assessment, conclusion, conduct, credibility, facts, having`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: assessment, conclusion, conduct, credibility, facts, having Application context: [27] The Court notes that although the RAD indicated that it had applied a standard of reasonableness in reviewing the RPD’s decision, in practice, it engaged in an analysis of the contradictions and inconsistencies rais Operative outcome context: For the foregoing reasons, this application for judicial review should be dismissed. Evidence spans paragraphs 21-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4620942` offsets `299-306`; context: It must review all aspects of the RPD’s decision and come to an independent assessment of whether the claimant is a Convention refugee or a person in need of protection.
- Evidence: `issue` cue `issues` at chunk `4620943` offsets `98-104`; context: [55] In conducting its assessment, it can recognize and respect the conclusion of the RPD on such issues as credibility and/or where the RPD enjoys a particular advantage in reaching such a conclusion but it is not restricted, as an appellate court is, to intervening on facts only where there is a “palpable and overriding error".
- Evidence: `evidence_fact` cue `evidence` at chunk `4620944` offsets `265-273`; context: [27] The Court notes that although the RAD indicated that it had applied a standard of reasonableness in reviewing the RPD’s decision, in practice, it engaged in an analysis of the contradictions and inconsistencies raised by the RPD, in light of the facts and the evidence in the record.
- Evidence: `reasoning_application` cue `applied` at chunk `4620944` offsets `65-72`; context: [27] The Court notes that although the RAD indicated that it had applied a standard of reasonableness in reviewing the RPD’s decision, in practice, it engaged in an analysis of the contradictions and inconsistencies raised by the RPD, in light of the facts and the evidence in the record.
- Evidence: `disposition` cue `dismissed` at chunk `4620944` offsets `2215-2224`; context: For the foregoing reasons, this application for judicial review should be dismissed.

#### Section text

Bui v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2014-11-28
Neutral citation
2014 FC 1145
File numbers
IMM-1654-14
Decision Content
Date: 20141128
Docket: IMM-1654-14
Citation: 2014 FC 1145
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, November 28, 2014
PRESENT: The Honourable Mr. Justice Shore
BETWEEN:
VAN SON BUI
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Introduction [1] This is an application for judicial review pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], of a decision of the Refugee Appeal Division [RAD] of the Immigration and Refugee Board determining that the applicant is neither a “Convention refugee” nor a “person in need of protection” within the meaning of sections 96 and 97 of the IRPA.
II. Facts [2] The applicant is a Vietnamese citizen who arrived in Canada on April 28, 2010, as a student.

[3] The applicant claims to be persecuted by a Colonel in the Vietnamese Army [the Colonel]. The applicant contends that in February 2013, his father was accused of acts of espionage on behalf of China by Vietnamese authorities, acts in which the Colonel was allegedly complicit. Following the arrest of the applicant’s father, the Colonel purportedly made death threats against the applicant and his mother out of fear of being reported to the Vietnamese authorities.

[4] Fearing for his life, the applicant claimed refugee protection in Canada on April 2, 2013, and a hearing before the Refugee Protection Division [RPD] was held on October 29, 2013.

[5] In a decision dated December 4, 2013, the RPD rejected the applicant’s refugee protection claim based on his lack of credibility. In particular, the RPD noted “the complete lack of corroborative evidence in support of this refugee protection claim”. In particular, the RPD was of the view that the applicant’s refugee protection claim was a tactic to remain in Canada (Tribunal Record, at pp 35 and 39; RPD Decision, at paras 9, 10 and 23).

[6] On December 17, 2013, the applicant appealed the RPD decision before the RAD. In that appeal, the applicant filed two new pieces of evidence, namely, two articles on the current political situation in Vietnam.

[7] The RAD dismissed the applicant’s appeal on February 24, 2014.
III. Impugned decision [8] First, in its reasons, the RAD concluded that the applicant failed to meet his burden of demonstrating the admissibility of the new evidence, pursuant to subsection 110(4) of the IRPA. The RAD found that the evidence had no direct or specific reference to the applicant.

[9] In addition, the RAD determined that there were no grounds to hold a hearing because the criteria set out in subsection 110(6) of the IRPA had not been met.

[10] Moreover, the RAD set out its role as an appellate tribunal in an administrative context. The RAD indicated that although it is not a judicial review court, it must show deference to findings of fact and of mixed fact and law made by the RPD by applying a reasonableness standard of review.

[11] Lastly, given the lack of evidence corroborating the applicant’s narrative, and the inconsistencies and contradictions found in the record, the RAD was of the view that the RPD committed no error in its assessment of the applicant’s credibility.
IV. Issues [12] The Court is of the view that the application raises the following issues:
a) Did the RAD err in its assessment of new evidence filed on appeal and with respect to holding a hearing?
b) Did the RAD err in upholding the RPD’s findings as to the applicant’s lack of credibility?
V. Statutory provisions [13] The following sections of the IRPA are relevant to determining the applicant’s refugee status:
Convention refugee
Définition de « réfugié »
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Person in need of protection
Personne à protéger
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
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
(2) A person in Canada who is a member of a class of persons prescribed by the regulations as being in need of protection is also a person in need of protection.
(2) A également qualité de personne à protéger la personne qui se trouve au Canada et fait partie d’une catégorie de personnes auxquelles est reconnu par règlement le besoin de protection.

[14] The following sections of the IRPA set out the applicable criteria with respect to the RAD’s role, the admissibility of evidence on appeal, and on the holding of a hearing:
Appeal
Appel
110. (1) Subject to subsections (1.1) and (2), a person or the Minister may appeal, in accordance with the rules of the Board, on a question of law, of fact or of mixed law and fact, to the Refugee Appeal Division against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.
110. (1) Sous réserve des paragraphes (1.1) et (2), la personne en cause et le ministre peuvent, conformément aux règles de la Commission, porter en appel — relativement à une question de droit, de fait ou mixte — auprès de la Section d’appel des réfugiés la décision de la Section de la protection des réfugiés accordant ou rejetant la demande d’asile.
Procedure
Fonctionnement
(3) Subject to subsections (3.1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
(3) Sous réserve des paragraphes (3.1), (4) et (6), la section procède sans tenir d’audience en se fondant sur le dossier de la Section de la protection des réfugiés, mais peut recevoir des éléments de preuve documentaire et des observations écrites du ministre et de la personne en cause ainsi que, s’agissant d’une affaire tenue devant un tribunal constitué de trois commissaires, des observations écrites du représentant ou mandataire du Haut-Commissariat des Nations Unies pour les réfugiés et de toute autre personne visée par les règles de la Commission.
Evidence that may be presented
Éléments de preuve admissibles
(4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
(4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
Hearing
Audience
(6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
c) à supposer qu’ils soient admis, justifieraient que la demande d’asile soit accordée ou refusée, selon le cas.
Decision
Décision
111. (1) After considering the appeal, the Refugee Appeal Division shall make one of the following decisions:
(a) confirm the determination of the Refugee Protection Division;
(b) set aside the determination and substitute a determination that, in its opinion, should have been made; or
(c) refer the matter to the Refugee Protection Division for re-determination, giving the directions to the Refugee Protection Division that it considers appropriate.
111. (1) La Section d’appel des réfugiés confirme la décision attaquée, casse la décision et y substitue la décision qui aurait dû être rendue ou renvoie, conformément à ses instructions, l’affaire à la Section de la protection des réfugiés.
VI. Applicant’s position [15] In support of his application, the applicant argues that the RAD erred in determining that the evidence filed on appeal was inadmissible. According to the applicant, this evidence could not reasonably have been expected to be presented in a timely manner and its content shows that the applicant’s situation had changed since the hearing before the RPD, particularly with regard to arbitrary detention in Vietnam.

[16] According to the applicant, the RAD should have applied a correctness standard of review and should not have shown deference to the RPD’s credibility findings (Canada (Minister of Citizenship and Immigration) v B472, 2013 FC 151). Furthermore, the applicant contends that the RPD and the RAD erred in their assessment of the evidence and from this made unreasonable findings as to the applicant’s credibility.
VII. Standard of review [17] The judicial review of the RAD’s interpretation of its home statute and of questions of mixed fact and attracts a reasonableness standard of review (Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 at paras 26 and 27 [Akuffo]). In adopting a pragmatic approach to an application for judicial review of an RAD decision, Justice Luc Martineau indicated that, depending on the circumstances, the Court must show some deference to the RAD:

[33] It is therefore apparent that RAD has jurisdiction over any question of law that is presented to it, including the standard of review it should apply. The RAD’s specialization, and the expertise of its members, as demonstrated by its function of standardization of law and the precedential value of decisions of three members pursuant to paragraph 171(c) of the IRPA, indicates that the Federal Court must defer to the RAD.
(Djossou v Canada (Minister of Citizenship and Immigration), 2014 FC 1080 at para 33).
VIII. Analysis a) Admissibility of new evidence and the holding of a hearing [18] First, paragraph 3(3))(g) of the Refugee Appeal Division Rules, SOR/2012-257 [Rules], below, states that the appeal record before the RAD must include full and detailed submissions regarding the relevance of the new evidence relied upon in the appeal and whether it meets the requirements of subsection 110(4) of the IRPA.

[19] Second, the RAD generally reviews appeals without holding a hearing. However, the RAD may hold a hearing in limited circumstances, in accordance with subsections 110(3) and 110(6) of the IRPA. Furthermore, the onus is on the applicant to justify the holding of a heating and to provide full and detailed submissions to the RAD, as required under paragraph 3(3)(g) of the Rules.
Content of appellant’s record
Contenu du dossier de l’appelant
(3) The appellant’s record must contain the following documents, on consecutively numbered pages, in the following order:
(3) Le dossier de l’appelant comporte les documents ci-après, sur des pages numérotées consécutivement, dans l’ordre qui suit :
[…]
[…]
(g) a memorandum that includes full and detailed submissions regarding
g) un mémoire qui inclut des observations complètes et détaillées concernant :
(i) the errors that are the grounds of the appeal,
(i) les erreurs commises qui constituent les motifs d’appel,
[…]
[…]
(iii) how any documentary evidence referred to in paragraph (e) meets the requirements of subsection 110(4) of the Act and how that evidence relates to the appellant,
(iii) la façon dont les éléments de preuve documentaire visés à l’alinéa e) sont conformes aux exigences du paragraphe 110(4) de la Loi et la façon dont ils sont liés à l’appelant,
[…]
[…]
(v) why the Division should hold a hearing under subsection 110(6) of the Act if the appellant is requesting that a hearing be held.
(v) les motifs pour lesquels la Section devrait tenir l’audience visée au paragraphe 110(6) de la Loi, si l’appelant en fait la demande.

[20] However, in its reasons, the RAD rejected the new evidence filed by the applicant on the basis that the applicant failed to meet the criteria required under the IRPA and Rules. In addition, the RAD indicated that the evidence filed on appeal was dated November 7 and 25, 2013, and was therefore available before the RPD issued its decision on December 4, 2013. Furthermore, the RAD noted that the lack of relevance of this new evidence added to its inadmissibility. Moreover, the RAD stated that the applicant had failed to show how the holding of a hearing would be justified under subsections 110(3) and 110(6) of the IRPA.

[21] In light of its analysis of the evidence and statutory framework, it was reasonable for the RAD to find the evidence filed by the applicant on appeal inadmissible, on the basis that this evidence failed to meet the requirements set out in the IRPA and Rules. It was also open to, and reasonable for, the RAD to conclude that the circumstances did not warrant the holding of a hearing.
b) Reasonableness of RAD’s analysis of RPD’s credibility findings [22] It is settled law that the judicial review regime does not apply to appeals before the RAD (Akuffo, above at para 33; Huruglica v Canada (Minister of Citizenship and Immigration), 2014 FC 799 at para 34 [Huruglica]; Alyafi v Canada (Minister of Citizenship and Immigration), 2014 FC 952 at para 10 [Alyafi]).

[23] The onus however, is on the appellant to show that the RPD made an error in order for the RAD to substitute a determination that, in its opinion, the RPD should have made or refer the matter back to the RPD for redetermination with directions, pursuant to subsection 111(1) of the IRPA. It should be noted that the RPD has the considerable advantage of hearing testimony viva voce and weighing the probative value of that testimony and the evidence in the record (Alvarez v Canada (Minister of Citizenship and Immigration), 2014 FC 702 at para 33; Spasoja v Canada (Minister of Citizenship and Immigration), 2014 FC 913 at para 40; Alyafi, above, at para 12). This does not detract from the fact that the RAD, as an appellate body, exercises a specialized jurisdiction on appeal at least equal to, and perhaps greater than, that of the RPD at trial (Alyafi, above, at para 12; Yetna v Canada (Minister of Citizenship and Immigration), 2014 FC 858 at para 17).

[24] Contrary to the applicant’s arguments, the Court is of the view that the RAD’s interpretation as to the standard of review applicable to the RPD’s decision is not, in and of itself, determinative. Rather, the credibility of the applicant is central to his claim for refugee protection (G.L.N.N. v Canada (Minister of Citizenship and Immigration), 2014 FC 859 at para 18; Huruglica, above, at para 37; Sajad v Canada (Minister of Citizenship and Immigration), 2014 FC 1107 at para 23).

[25] It has emerged from the recent jurisprudence of this Court that the centrality of the credibility of an applicant in an appeal filed before the RAD may engage a certain level of deference on the part of the RAD with respect to the RPD’s findings. In that regard, Justice George R. Locke writes:

[16] Taking into consideration once more Justice Phelan’s decision in Huruglica, above, I am of the view that the RAD erred in concluding that the RPD decision was reviewable on a reasonableness standard.

[17] Save for cases in which the credibility of a witness is critical or determinative, or where the RPD enjoys a particular advantage over the RAD in reaching a specific conclusion, the RAD owes no deference to the RPD’s assessment of the evidence: see Huruglica, at paras 37 and 55. The RAD has as much expertise as the RPD, and perhaps more in terms of analyzing relevant documents and parties’ submissions.
[Emphasis added.]
(Yetna v Canada (Minister of Citizenship and Immigration), 2014 FC 858).

[26] In the recent Akuffo decision, above, at para 39, Justice Jocelyne Gagné states that a certain level of deference is owed by the RAD to the RPD’s credibility findings and where the RPD enjoys a particular advantage in reaching its conclusion. This approach is supported in Huruglica, above, wherein Justice Michael L. Phelan writes:

[54] Having concluded that the RAD erred in reviewing the RPD’s decision on the standard of reasonableness, I have further concluded that for the reasons above, the RAD is required to conduct a hybrid appeal. It must review all aspects of the RPD’s decision and come to an independ

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 12438:2 · paragraphs 25-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `7b08b96b09a936b7f1f4ca276b6e79147224e747141b3a3552de05d8f2b3d1f0`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12438:2:subtheme:1 · paragraphs 25-25

- Raw key terms: `ageorges, anne-ren, appearances, applicant, attorney, canada, cecilia, dated`
- Display key terms: `ageorges, anne-ren, cecilia, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: ageorges, anne-ren, cecilia, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 25-25. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
SHORE J.
DATED:
NOVEMBER 28, 2014
APPEARANCES:
Cecilia Ageorges
FOR THE APPLICANT
Anne-Renée Touchette
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Cecilia Ageorges
Montréal, Quebec
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
