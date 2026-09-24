# Discussion Units: case 12321

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **25**
- Continuity pairs: **24**
- Discussion Units: **2**
- Paragraph source hashes: **25**
- Sub-themes: **7**

## 12321:1 · paragraphs 0-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `93895ef2ea0b0a0a478a771c3b1cc773b4b16631e0548973509cb1e5144c72cd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12321:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, algerian, central, decision, division, form, refugee, businessman`
- Display key terms: `algerian, central, division, form, refugee, businessman`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: algerian, central, division, form, refugee, businessman Rule/authority context: Introduction [3] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], of a decision by the RAD confirming the RPD’s determination that the | Decision of the Refugee Protection Division [6] In a decision dated January 21, 2014, the RPD determined that the applicant is not a Convention refugee or a person in need of protection under sections 96 and 97 of the IR Application context: [2] It was reasonable for the RAD to confirm the adverse credibility findings made by the Refugee Protection Division [RPD] against the applicant because of the lateness and central nature of the changes made to his stor Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4615575` offsets `506-511`; context: Preliminary remarks [1] The important issue for the Court is whether the Refugee Appeal Division [RAD] undertook an independent examination of the record on appeal as a whole (G.
- Evidence: `evidence_fact` cue `record` at chunk `4615575` offsets `615-621`; context: Preliminary remarks [1] The important issue for the Court is whether the Refugee Appeal Division [RAD] undertook an independent examination of the record on appeal as a whole (G.
- Evidence: `governing_rule` cue `under` at chunk `4615576` offsets `512-517`; context: Introduction [3] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], of a decision by the RAD confirming the RPD’s determination that the applicant is neither a refugee nor a person in need of protection.
- Evidence: `reasoning_application` cue `because` at chunk `4615576` offsets `146-153`; context: [2] It was reasonable for the RAD to confirm the adverse credibility findings made by the Refugee Protection Division [RPD] against the applicant because of the lateness and central nature of the changes made to his story and the absence of any explanation that was considered satisfactory, plausible or credible in the circumstances (Zeferino v Canada (Minister of Citizenship and Immigration), 2011 FC 456, above, at paras 31 and 32 [Zeferino]).
- Evidence: `evidence_fact` cue `determined that` at chunk `4615577` offsets `330-345`; context: Decision of the Refugee Protection Division [6] In a decision dated January 21, 2014, the RPD determined that the applicant is not a Convention refugee or a person in need of protection under sections 96 and 97 of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `4615577` offsets `422-427`; context: Decision of the Refugee Protection Division [6] In a decision dated January 21, 2014, the RPD determined that the applicant is not a Convention refugee or a person in need of protection under sections 96 and 97 of the IRPA.
- Evidence: `evidence_fact` cue `found that` at chunk `4615578` offsets `194-204`; context: The RPD found that the explanations provided by the applicant concerning those omissions were not credible in light of the evidence as a whole.
- Evidence: `evidence_fact` cue `found that` at chunk `4615579` offsets `27-37`; context: [8] In particular, the RPD found that the initial BOC Form did not state that the applicant was an MAK sympathizer and that he had personally been stopped and threatened by Algerian police officers in 2010, 2011 and 2012, even though these were elements central to his alleged fear.

#### 12321:1:subtheme:2 · paragraphs 5-7

- Raw key terms: `applicant, explanation, form, because, noted, omission, question, rejected`
- Display key terms: `explanation, form, because, noted, omission, question, rejected`
- Argument roles: `disposition, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, party_position, reasoning_application Display terms: explanation, form, because, noted, omission, question, rejected Position/evidence statements: It rejected the applicant’s explanation that he had left out that information because he planned to supplement his story at the hearing, in part because of the fact that the applicant was represented by counsel at the ti Rule/authority context: [9] The RPD also took note of the applicant’s failure to include his longstanding association with the MAK under question 9 of his IMM 5669 immigration form, especially since that association was the basis for the allege Application context: The RPD rejected the applicant’s explanation of that omission (the applicant testified that he had not written anything under that question because he did not have an MAK membership card), since the question required him | It rejected the applicant’s explanation that he had left out that information because he planned to supplement his story at the hearing, in part because of the fact that the applicant was represented by counsel at the ti Operative outcome context: Impugned decision by the Refugee Appeal Division [12] On June 2, 2014, the RAD dismissed the appeal and confirmed the RPD’s determination. Evidence spans paragraphs 5-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4615580` offsets `113-121`; context: [9] The RPD also took note of the applicant’s failure to include his longstanding association with the MAK under question 9 of his IMM 5669 immigration form, especially since that association was the basis for the alleged persecution.
- Evidence: `governing_rule` cue `under` at chunk `4615580` offsets `107-112`; context: [9] The RPD also took note of the applicant’s failure to include his longstanding association with the MAK under question 9 of his IMM 5669 immigration form, especially since that association was the basis for the alleged persecution.
- Evidence: `reasoning_application` cue `because` at chunk `4615580` offsets `375-382`; context: The RPD rejected the applicant’s explanation of that omission (the applicant testified that he had not written anything under that question because he did not have an MAK membership card), since the question required him to include any organization he had “supported, been a member of or been associated with”.
- Evidence: `issue` cue `question` at chunk `4615581` offsets `64-72`; context: [10] The RPD also noted that the applicant had answered “no” to question 2(a) of his BOC Form, “Have you or your family ever been harmed, mistreated or threatened by any person or group?
- Evidence: `party_position` cue `submitted` at chunk `4615582` offsets `540-549`; context: It rejected the applicant’s explanation that he had left out that information because he planned to supplement his story at the hearing, in part because of the fact that the applicant was represented by counsel at the time he submitted amendments to his BOC Form on November 18, 2013.
- Evidence: `reasoning_application` cue `because` at chunk `4615582` offsets `392-399`; context: It rejected the applicant’s explanation that he had left out that information because he planned to supplement his story at the hearing, in part because of the fact that the applicant was represented by counsel at the time he submitted amendments to his BOC Form on November 18, 2013.
- Evidence: `disposition` cue `dismissed` at chunk `4615582` offsets `681-690`; context: Impugned decision by the Refugee Appeal Division [12] On June 2, 2014, the RAD dismissed the appeal and confirmed the RPD’s determination.

#### 12321:1:subtheme:3 · paragraphs 8-10

- Raw key terms: `evidence, appeal, applicable, canada, findings, found, irpa, jurisdiction`
- Display key terms: `applicable, findings, irpa, jurisdiction`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: applicable, findings, irpa, jurisdiction Application context: (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa r Evidence spans paragraphs 8-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4615583` offsets `49-55`; context: [13] The RAD began by addressing the preliminary issues concerning its jurisdiction and the scope of the appeal before it.
- Evidence: `evidence_fact` cue `determined that` at chunk `4615583` offsets `133-148`; context: First, it determined that no new evidence was being presented on appeal and that there was no cause to hold a hearing, in accordance with subsections 110(3), 110(4) and 110(6) of the IRPA.
- Evidence: `evidence_fact` cue `found that` at chunk `4615584` offsets `66-76`; context: [14] Next, by analogy with the regime of judicial review, the RAD found that the applicable standard for reviewing the RPD’s decision was reasonableness (Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir]; Ndam v Canada (Minister of Citizenship and Immigration), 2010 FC 513; Ferencova v Canada (Minister of Citizenship and Immigration), 2011 FC 443).
- Evidence: `counterargument_limitation` cue `but` at chunk `4615584` offsets `484-487`; context: With regard to its jurisdiction as an appellate administrative tribunal, the RAD stated that its role was not to reassess the evidence but rather to show deference to the RPD’s credibility findings.
- Evidence: `evidence_fact` cue `record` at chunk `4615585` offsets `74-80`; context: [15] On the merits of the appeal, following a thorough examination of the record and the RPD’s findings, the RAD found that the RPD had not erred in assessing the evidence and the applicant’s explanations.
- Evidence: `reasoning_application` cue `because` at chunk `4615585` offsets `2583-2590`; context: (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée:
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant:
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.

#### 12321:1:subtheme:4 · paragraphs 11-13

- Raw key terms: `applicable, minister, ministre, above, canada, citizenship, citoyennet, concerning`
- Display key terms: `applicable, ministre, above, citoyennet, concerning`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: applicable, ministre, above, citoyennet, concerning Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4615586` offsets `322-330`; context: 1) and (2), a person or the Minister may appeal, in accordance with the rules of the Board, on a question of law, of fact or of mixed law and fact, to the Refugee Appeal Division against a decision of the Refugee Protection Division to allow or reject the person’s claim for refugee protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4615586` offsets `107-115`; context: [17] The following sections of the IRPA set out the applicable requirements concerning the RAD’s role, the evidence that may be presented on appeal and the holding of hearings:
Appeal
Appel
110.

#### 12321:1:subtheme:5 · paragraphs 14-21

- Raw key terms: `above, canada, citizenship, credibility, immigration, minister, para, applicant`
- Display key terms: `above, credibility, para`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: above, credibility, para Application context: [29] From this perspective, it was therefore reasonable for the RAD to confirm the adverse credibility findings made by the RPD against the applicant because of the lateness and central nature of the changes made to his  Evidence spans paragraphs 14-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4615589` offsets `81-86`; context: The important issue for the Court is whether the RAD undertook an independent examination of the record on appeal as a whole (G.
- Evidence: `evidence_fact` cue `record` at chunk `4615589` offsets `164-170`; context: The important issue for the Court is whether the RAD undertook an independent examination of the record on appeal as a whole (G.
- Evidence: `evidence_fact` cue `record` at chunk `4615590` offsets `164-170`; context: Rather, it relied on a thorough examination of the record and on the parties’ submissions to confirm the RPD’s credibility findings, resulting in the dismissal of the appeal.
- Evidence: `evidence_fact` cue `testimony` at chunk `4615591` offsets `168-177`; context: [24] The Court finds that it was reasonable for the RAD to show some deference to the RPD’s credibility findings; the RPD has the considerable advantage of hearing the testimony in person and weighing the credibility and probative value of the evidence presented by the parties (Alyafi v Canada (Minister of Citizenship and Immigration), 2014 FC 952 at para 12; Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 at paras 34 and 50; G.
- Evidence: `evidence_fact` cue `testimony` at chunk `4615592` offsets `148-157`; context: [25] As noted by the RAD and the RPD, the applicant added many central elements in support of his alleged fear in his amended BOC Form and his oral testimony, including his involvement with the MAK and the threats made against him by Algerian police officers.
- Evidence: `evidence_fact` cue `evidence` at chunk `4615594` offsets `158-166`; context: [27] The case law has established that any omission in a previous version of the facts must be examined in its context and be assessed in light of all of the evidence; a claimant’s credibility cannot be impugned when the changes made to the BOC Form are minimal and the claimant has provided a plausible explanation of the corrections made (V.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4615594` offsets `193-199`; context: [27] The case law has established that any omission in a previous version of the facts must be examined in its context and be assessed in light of all of the evidence; a claimant’s credibility cannot be impugned when the changes made to the BOC Form are minimal and the claimant has provided a plausible explanation of the corrections made (V.
- Evidence: `reasoning_application` cue `therefore` at chunk `4615596` offsets `35-44`; context: [29] From this perspective, it was therefore reasonable for the RAD to confirm the adverse credibility findings made by the RPD against the applicant because of the lateness and central nature of the changes made to his story and the absence of any explanation that was considered satisfactory, plausible or credible in the circumstances (Zeferino, above, at paras 31 and 32).

#### 12321:1:subtheme:6 · paragraphs 22-23

- Raw key terms: `record, above, accordance, adjudges, appellate, application, cause, certified`
- Display key terms: `above, accordance, adjudges, appellate, certified`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: above, accordance, adjudges, appellate, certified Operative outcome context: Conclusion [31] The application for judicial review is dismissed. Evidence spans paragraphs 22-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4615597` offsets `413-421`; context: There is no question of importance to be certified.
- Evidence: `evidence_fact` cue `record` at chunk `4615597` offsets `141-147`; context: [30] In light of the foregoing, the Court is of the opinion that the RAD’s findings are reasonable and reflect a thorough examination of the record in accordance with its role as an appellate tribunal (Yin, above, at paras 37 and 40).
- Evidence: `disposition` cue `dismissed` at chunk `4615597` offsets `294-303`; context: Conclusion [31] The application for judicial review is dismissed.

#### Section text

Hamidi v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-02-26
Neutral citation
2015 FC 243
File numbers
IMM-5049-14
Decision Content
Date: 20150226
Docket: IMM-5049-14
Citation: 2015 FC 243
[UNREVISED ENGLISH CERTIFIED TRANSLATION]
Ottawa, Ontario, February 26, 2015
PRESENT: The Honourable Mr. Justice Shore
BETWEEN:
SAMIR HAMIDI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Preliminary remarks [1] The important issue for the Court is whether the Refugee Appeal Division [RAD] undertook an independent examination of the record on appeal as a whole (G.L.N.N. v Canada (Minister of Citizenship and Immigration), 2014 FC 859 at para 18 [G.L.N.N.]; Sajad v Canada (Minister of Citizenship and Immigration), 2014 FC 1107 at para 23).

[2] It was reasonable for the RAD to confirm the adverse credibility findings made by the Refugee Protection Division [RPD] against the applicant because of the lateness and central nature of the changes made to his story and the absence of any explanation that was considered satisfactory, plausible or credible in the circumstances (Zeferino v Canada (Minister of Citizenship and Immigration), 2011 FC 456, above, at paras 31 and 32 [Zeferino]).
II. Introduction [3] This is an application for judicial review under subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], of a decision by the RAD confirming the RPD’s determination that the applicant is neither a refugee nor a person in need of protection.
III. Facts [4] The applicant is a 38‑year‑old Algerian businessman from the Kabylie region in northern Algeria.

[5] In his Basis of Claim [BOC] Form and an amendment to his BOC Form, the applicant claims to fear persecution by the Algerian police in Kabylie as a businessman and a sympathizer of the Movement for the Autonomy of Kabylie [MAK].
IV. Decision of the Refugee Protection Division [6] In a decision dated January 21, 2014, the RPD determined that the applicant is not a Convention refugee or a person in need of protection under sections 96 and 97 of the IRPA.

[7] The RPD identified the applicant’s credibility as being central to the rejection of his claim, including in relation to the major omissions in his BOC Form and his amended BOC Form. The RPD found that the explanations provided by the applicant concerning those omissions were not credible in light of the evidence as a whole.

[8] In particular, the RPD found that the initial BOC Form did not state that the applicant was an MAK sympathizer and that he had personally been stopped and threatened by Algerian police officers in 2010, 2011 and 2012, even though these were elements central to his alleged fear. When asked to explain the omissions at the hearing, the applicant testified that he had thought he would supplement his story at the hearing and that he had not been represented by counsel when he completed his BOC Form.

[9] The RPD also took note of the applicant’s failure to include his longstanding association with the MAK under question 9 of his IMM 5669 immigration form, especially since that association was the basis for the alleged persecution. The RPD rejected the applicant’s explanation of that omission (the applicant testified that he had not written anything under that question because he did not have an MAK membership card), since the question required him to include any organization he had “supported, been a member of or been associated with”.

[10] The RPD also noted that the applicant had answered “no” to question 2(a) of his BOC Form, “Have you or your family ever been harmed, mistreated or threatened by any person or group?”. When confronted with that omission, the applicant did not provide an explanation that was considered credible and sufficient by the RPD.

[11] As well, the applicant testified at the hearing that police officers had threatened to kill him during a roadblock on May 15, 2012, which had convinced him to stop his work transporting sand by land. The RPD noted that that incident was not in either the applicant’s initial BOC Form or his amended BOC Form. It rejected the applicant’s explanation that he had left out that information because he planned to supplement his story at the hearing, in part because of the fact that the applicant was represented by counsel at the time he submitted amendments to his BOC Form on November 18, 2013.
V. Impugned decision by the Refugee Appeal Division [12] On June 2, 2014, the RAD dismissed the appeal and confirmed the RPD’s determination.

[13] The RAD began by addressing the preliminary issues concerning its jurisdiction and the scope of the appeal before it. First, it determined that no new evidence was being presented on appeal and that there was no cause to hold a hearing, in accordance with subsections 110(3), 110(4) and 110(6) of the IRPA.

[14] Next, by analogy with the regime of judicial review, the RAD found that the applicable standard for reviewing the RPD’s decision was reasonableness (Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir]; Ndam v Canada (Minister of Citizenship and Immigration), 2010 FC 513; Ferencova v Canada (Minister of Citizenship and Immigration), 2011 FC 443). With regard to its jurisdiction as an appellate administrative tribunal, the RAD stated that its role was not to reassess the evidence but rather to show deference to the RPD’s credibility findings.

[15] On the merits of the appeal, following a thorough examination of the record and the RPD’s findings, the RAD found that the RPD had not erred in assessing the evidence and the applicant’s explanations.
VI. Statutory provisions [16] Sections 96 and 97 of the IRPA set out the law applicable to the determination of refugee status in Canada:
Convention refugee
Définition de réfugié
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
96. A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques:
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Person in need of protection
Personne à protéger
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée:
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant:
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

[17] The following sections of the IRPA set out the applicable requirements concerning the RAD’s role, the evidence that may be presented on appeal and the holding of hearings:
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
(6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés, au paragraphe (3) qui, à la fois:
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
VII. Issue [18] The issue raised by the application is whether the RAD’s decision is reasonable.
VIII. Analysis [19] On appeal, the central question before the RAD was the applicant’s credibility.

[20] The Court’s recent decisions concerning the scope of judicial review of RAD decisions indicate that, when reviewing questions of credibility, which are determinations of fact and of mixed law and fact, the applicable standard is reasonableness (Yin v Canada (Minister of Citizenship and Immigration), 2014 FC 1209 at para 34 [Yin]; Nahal c Canada (Ministre de la Citoyenneté et de l'Immigration), 2014 CF 1208 at para 25 [Nahal]; Siliya v Canada (Minister of Citizenship and Immigration), 2015 FC 120 at para 20; Dunsmuir, above, at para 53).

[21] The RAD erred from the outset by stating that the applicable standard was reasonableness (Djossou v Canada (Minister of Citizenship and Immigration), 2014 FC 1080 at para 39; Nahal, above, at para 26; Genu c Canada (Ministre de la Citoyenneté et de l'Immigration), 2015 CF 129 at para 31).

[22] That error is not in itself determinative of the application. The important issue for the Court is whether the RAD undertook an independent examination of the record on appeal as a whole (G.L.N.N., above, at para 18; Sajad v Canada (Minister of Citizenship and Immigration), 2014 FC 1107 at para 23).

[23] It is clear from the RAD’s reasons that it did not simply confirm the RPD’s findings without qualification. Rather, it relied on a thorough examination of the record and on the parties’ submissions to confirm the RPD’s credibility findings, resulting in the dismissal of the appeal.

[24] The Court finds that it was reasonable for the RAD to show some deference to the RPD’s credibility findings; the RPD has the considerable advantage of hearing the testimony in person and weighing the credibility and probative value of the evidence presented by the parties (Alyafi v Canada (Minister of Citizenship and Immigration), 2014 FC 952 at para 12; Akuffo v Canada (Minister of Citizenship and Immigration), 2014 FC 1063 at paras 34 and 50; G.L.N.N., above, at para 14; Cienfuegos v Canada (Minister of Citizenship and Immigration), 2009 FC 1262 at para 2).

[25] As noted by the RAD and the RPD, the applicant added many central elements in support of his alleged fear in his amended BOC Form and his oral testimony, including his involvement with the MAK and the threats made against him by Algerian police officers. He thus presented a version of the facts that was very different from the one in his initial BOC Form.

[26] Moreover, when confronted with the many discrepancies and omissions in his initial story, the applicant was unable to provide explanations that were considered reasonable or sufficient by the RAD and the RPD.

[27] The case law has established that any omission in a previous version of the facts must be examined in its context and be assessed in light of all of the evidence; a claimant’s credibility cannot be impugned when the changes made to the BOC Form are minimal and the claimant has provided a plausible explanation of the corrections made (V.V. v Canada (Minister of Citizenship and Immigration), 2012 FC 1097 at para 34 [V.V.]).

[28] However, “the impact is different when omissions have to do with the facts that directly concern the very basis of a claim for refugee protection” (V.V., above, at para 35; see Zeferino, above, at paras 31‑32; Aragon v Canada (Minister of Citizenship and Immigration), 2008 FC 144 at para 21).

[29] From this perspective, it was therefore reasonable for the RAD to confirm the adverse credibility findings made by the RPD against the applicant because of the lateness and central nature of the changes made to his story and the absence of any explanation that was considered satisfactory, plausible or credible in the circumstances (Zeferino, above, at paras 31 and 32).

[30] In light of the foregoing, the Court is of the opinion that the RAD’s findings are reasonable and reflect a thorough examination of the record in accordance with its role as an appellate tribunal (Yin, above, at paras 37 and 40).
IX. Conclusion [31] The application for judicial review is dismissed.
JUDGMENT
THE COURT’S ORDERS AND ADJUDGES that the application for judicial review is dismissed. There is no question of importance to be certified.
“Michel M.J. Shore”
Judge
Certified true translation
Johanna Kratz, Translator
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-5049-14
STYLE OF CAUSE:
SAMIR HAMIDI v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Montréal, QuEbec
DATE OF HEARING:
FEBRUARY 25, 2015


## 12321:2 · paragraphs 24-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fe6c7ec46bf9c0e3a02bcd6ff25efe04f47d62fcb61217aae2c5cd355a47b5e7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12321:2:subtheme:1 · paragraphs 24-24

- Raw key terms: `alain, appearances, applicant, attorney, canada, dated, deputy, february`
- Display key terms: `alain, dated, deputy, february`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alain, dated, deputy, february No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 24-24. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS BY:
SHORE J.
DATED:
FEBRUARY 26, 2015
APPEARANCES:
Moriba Alain Koné
FOR THE APPLICANT
Suzon Létourneau
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Moriba Alain Koné
Montréal, Quebec
FOR THE APPLICANT
William F. Pentney
Deputy Attorney General of Canada
Montréal, Quebec
FOR THE RESPONDENT
