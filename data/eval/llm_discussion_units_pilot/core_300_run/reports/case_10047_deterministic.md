# Discussion Units: case 10047

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **31**
- Continuity pairs: **30**
- Discussion Units: **3**
- Paragraph source hashes: **31**
- Sub-themes: **9**

## 10047:1 · paragraphs 0-8

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6eb70e2cd773a23854f537d2e71569b97d9fc1434dfc895dcb73bb32c9dc8d8b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10047:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicant, decision, paradis, sst-gd, appeal, application, april, employment`
- Display key terms: `paradis, sst-gd, april, employment`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application Display terms: paradis, sst-gd, april, employment Rule/authority context: He is pursuing remedies for his termination under Alberta labour relations legislation. | On April 15, 2016, the SST-AD refused the applicant’s leave to appeal under subsection 58(1) of the Department of Employment and Social Development Act, SC 2005, c 34 (DESDA). Application context: The Commission concluded that the applicant’s employment was terminated because of his own misconduct. Operative outcome context: Paradis claimed employment insurance benefits but they were denied. | On May 18, 2015, the claim was denied by the Employment Insurance Commission (the Commission). Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `record` at chunk `4507039` offsets `1282-1288`; context: There is no indication in the record that he was operating equipment while he was impaired.
- Evidence: `governing_rule` cue `under` at chunk `4507039` offsets `1388-1393`; context: He is pursuing remedies for his termination under Alberta labour relations legislation.
- Evidence: `counterargument_limitation` cue `However` at chunk `4507039` offsets `225-232`; context: However, he was fired when a urine test detected THC in his system.
- Evidence: `disposition` cue `denied` at chunk `4507039` offsets `357-363`; context: Paradis claimed employment insurance benefits but they were denied.
- Evidence: `reasoning_application` cue `because` at chunk `4507040` offsets `241-248`; context: The Commission concluded that the applicant’s employment was terminated because of his own misconduct.
- Evidence: `disposition` cue `denied` at chunk `4507040` offsets `105-111`; context: On May 18, 2015, the claim was denied by the Employment Insurance Commission (the Commission).
- Evidence: `disposition` cue `upheld` at chunk `4507041` offsets `153-159`; context: In its decision, communicated to the applicant on December 1, 2015, the SST-GD upheld the Commission’s finding that the applicant’s actions amounted to misconduct and dismissed the appeal.
- Evidence: `governing_rule` cue `under` at chunk `4507042` offsets `185-190`; context: On April 15, 2016, the SST-AD refused the applicant’s leave to appeal under subsection 58(1) of the Department of Employment and Social Development Act, SC 2005, c 34 (DESDA).
- Evidence: `evidence_fact` cue `record` at chunk `4507043` offsets `99-105`; context: Paradis asked that a medical record from his childhood be entered into evidence.

#### 10047:1:subtheme:2 · paragraphs 6-7

- Raw key terms: `evidence, paradis, adhd, admissible, appeal, applicable, application, assessed`
- Display key terms: `paradis, adhd, admissible, applicable, assessed`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: paradis, adhd, admissible, applicable, assessed Rule/authority context: ISSUES [8] There is no dispute between the parties that the standard of review applicable when reviewing a decision of the SST-AD to grant or deny leave to appeal is reasonableness: Canada (AG) v Hines, 2016 FC 112, [201 Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4507044` offsets `407-413`; context: ISSUES [8] There is no dispute between the parties that the standard of review applicable when reviewing a decision of the SST-AD to grant or deny leave to appeal is reasonableness: Canada (AG) v Hines, 2016 FC 112, [2016] FCJ No 84 at para 28; see also Canada (AG) v Hoffman, 2015 FC 1348, [2015] FCJ No 1511 at paras 26-27; Bergerson v Canada, 2016 FC 220 at para 6.
- Evidence: `evidence_fact` cue `evidence` at chunk `4507044` offsets `16-24`; context: [7] The medical evidence consisted of a report from a pediatrician who had assessed Mr.
- Evidence: `governing_rule` cue `standard of review` at chunk `4507044` offsets `467-485`; context: ISSUES [8] There is no dispute between the parties that the standard of review applicable when reviewing a decision of the SST-AD to grant or deny leave to appeal is reasonableness: Canada (AG) v Hines, 2016 FC 112, [2016] FCJ No 84 at para 28; see also Canada (AG) v Hoffman, 2015 FC 1348, [2015] FCJ No 1511 at paras 26-27; Bergerson v Canada, 2016 FC 220 at para 6.
- Evidence: `issue` cue `whether` at chunk `4507045` offsets `54-61`; context: [9] As a preliminary matter, the Court must determine whether the new evidence which Mr.
- Evidence: `evidence_fact` cue `evidence` at chunk `4507045` offsets `70-78`; context: [9] As a preliminary matter, the Court must determine whether the new evidence which Mr.

#### 10047:1:subtheme:3 · paragraphs 8-8

- Raw key terms: `abusive, acceptable, acted, admissibility, apart, appeal, appears, appel`
- Display key terms: `abusive, acceptable, acted, admissibility, apart, appears, appel`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: abusive, acceptable, acted, admissibility, apart, appears, appel Evidence spans paragraphs 8-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4507046` offsets `20-28`; context: [10] Apart from the question of admissibility of the new evidence, the sole issue in this judicial review is whether the SST-AD’s decision refusing leave to appeal was reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4507046` offsets `57-65`; context: [10] Apart from the question of admissibility of the new evidence, the sole issue in this judicial review is whether the SST-AD’s decision refusing leave to appeal was reasonable.

#### Section text

Paradis v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2016-11-17
Neutral citation
2016 FC 1282
File numbers
T-649-16
Decision Content
Date: 20161117
Docket: T-649-16
Citation: 2016 FC 1282
Ottawa, Ontario, November 17, 2016
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
DANNY PARADIS
Applicant
and
THE ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS

[1] Danny Paradis was employed as a crane operator building powerlines in Alberta. He used cannabis at night to help him sleep due to insomnia. There is no suggestion that he used it at work or was impaired while on the job. However, he was fired when a urine test detected THC in his system. Mr. Paradis claimed employment insurance benefits but they were denied. The Social Security Tribunal upheld his disqualification. He tried to appeal but was refused leave. Representing himself, he brought this application for judicial review of that decision.
I. BACKGROUND [2] Mr. Paradis is 27 years old. From May 26, 2014 until April 4, 2015, he worked as a crane operator for Forbes Bros. Ltd. On April 4, 2015, he fainted on the job due, he says, to dehydration and inhaling exhaust fumes. Mr. Paradis was sent to the hospital as a precaution. Since he had been operating heavy equipment, as per company policy, a post incident drug test was administered. The test was positive for THC, an active ingredient in marijuana. The employer’s policy states that all employees must remain free from the effects of and dependency on illegal drugs and/or alcohol while on the worksite. Mr. Paradis’ employment was immediately terminated for breaching the policy. There is no indication in the record that he was operating equipment while he was impaired. He is pursuing remedies for his termination under Alberta labour relations legislation.

[3] On April 19, 2015, Mr. Paradis claimed employment insurance benefits. On May 18, 2015, the claim was denied by the Employment Insurance Commission (the Commission). The Commission concluded that the applicant’s employment was terminated because of his own misconduct. As a result, it imposed an indefinite disqualification effective April 5, 2015. An application for reconsideration was denied. Mr. Paradis then appealed to the Social Security Tribunal – General Division (SST-GD).

[4] The SST-GD conducted a hearing by teleconference on October 15, 2015. In its decision, communicated to the applicant on December 1, 2015, the SST-GD upheld the Commission’s finding that the applicant’s actions amounted to misconduct and dismissed the appeal.

[5] Mr. Paradis filed an application requesting leave to appeal the decision of the SST-GD to the Appeal Division. On April 15, 2016, the SST-AD refused the applicant’s leave to appeal under subsection 58(1) of the Department of Employment and Social Development Act, SC 2005, c 34 (DESDA). He seeks judicial review of that decision under section 18.1 of the Federal Courts Act, RSC, 1985, c F-7.

[6] In a communication to the Court just days before the hearing, Mr. Paradis asked that a medical record from his childhood be entered into evidence. He produced that record at the hearing. The respondent objected to its introduction and to the inclusion in the applicant’s record of several documents that were not before the SST-GD when it rendered its decision. These included a copy of the employer’s termination letter dated June 1, 2015 and a copy of the Alberta Human Rights Act policy on drug and alcohol dependencies in Alberta workplaces.

[7] The medical evidence consisted of a report from a pediatrician who had assessed Mr. Paradis when he was 12 and 15 years old and a recent prescription for cannabis. The report indicates that Mr. Paradis suffered from Attention Deficit and Hyper-activity Disorder (ADHD) as a child. Mr. Paradis says he continues to experience ADHD and for that reason is prescribed marijuana to control the symptoms.
II. ISSUES [8] There is no dispute between the parties that the standard of review applicable when reviewing a decision of the SST-AD to grant or deny leave to appeal is reasonableness: Canada (AG) v Hines, 2016 FC 112, [2016] FCJ No 84 at para 28; see also Canada (AG) v Hoffman, 2015 FC 1348, [2015] FCJ No 1511 at paras 26-27; Bergerson v Canada, 2016 FC 220 at para 6.

[9] As a preliminary matter, the Court must determine whether the new evidence which Mr. Paradis included in his Application Record and produced at the hearing is admissible.

[10] Apart from the question of admissibility of the new evidence, the sole issue in this judicial review is whether the SST-AD’s decision refusing leave to appeal was reasonable. The Court must decide whether the decision falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law: Dunsmuir v New Brunswick, 2008 SCC 9, [2008] SCJ No 9 at para 57.
III. RELEVANT LEGISLATION [11] The relevant provisions of the DESDA read as follows:
Grounds of appeal
Moyens d’appel
58 (1) The only grounds of appeal are that
58 (1) Les seuls moyens d’appel sont les suivants :
(a) the General Division failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise its jurisdiction;
a) la division générale n’a pas observé un principe de justice naturelle ou a autrement excédé ou refusé d’exercer sa compétence;
(b) the General Division erred in law in making its decision, whether or not the error appears on the face of the record; or
b) elle a rendu une décision entachée d’une erreur de droit, que l’erreur ressorte ou non à la lecture du dossier;
(c) the General Division based its decision on an erroneous finding of fact that it made in a perverse or capricious manner or without regard for the material before it.
c) elle a fondé sa décision sur une conclusion de fait erronée, tirée de façon abusive ou arbitraire ou sans tenir compte des éléments portés à sa connaissance.

## 10047:2 · paragraphs 9-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f0b9e88318811d4f4ef6ba753be20719850a521ac72d12b8ce66fb582e4a560f`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10047:2:subtheme:1 · paragraphs 9-11

- Raw key terms: `applicant, employment, misconduct, canada, cause, dismissal, employed, issue`
- Display key terms: `employment, misconduct, dismissal, employed`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: employment, misconduct, dismissal, employed Rule/authority context: 1, pour recevoir des prestations de chômage; (b) the claimant is disentitled under sections 31 to 33 in relation to the employment. Application context: [12] The relevant provisions of the EIA read as follows: Interpretation Interprétation 29 For the purposes of sections 30 to 33, 29 Pour l’application des articles 30 à 33 : (a) employment refers to any employment of the | [14] The EIA does not define “misconduct”; the Member therefore relied on several cases that discuss how the term should apply. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4507047` offsets `2064-2069`; context: SST-GD’s Decision [13] The sole issue before the SST-GD was whether a disqualification from receiving benefits should be imposed under sections 29 and 30 of the EIA because the applicant lost his employment by reason of his own “misconduct”.
- Evidence: `governing_rule` cue `under` at chunk `4507047` offsets `1839-1844`; context: 1, pour recevoir des prestations de chômage;
(b) the claimant is disentitled under sections 31 to 33 in relation to the employment.
- Evidence: `reasoning_application` cue `because` at chunk `4507047` offsets `1143-1150`; context: [12] The relevant provisions of the EIA read as follows:
Interpretation
Interprétation
29 For the purposes of sections 30 to 33,
29 Pour l’application des articles 30 à 33 :
(a) employment refers to any employment of the claimant within their qualifying period or their benefit period;
a) emploi s’entend de tout emploi exercé par le prestataire au cours de sa période de référence ou de sa période de prestations;
(b) loss of employment includes a suspension from employment, but does not include loss of, or suspension from, employment on account of membership in, or lawful activity connected with, an association, organization or union of workers;
b) la suspension est assimilée à la perte d’emploi, mais n’est pas assimilée à la perte d’emploi la suspension ou la perte d’emploi résultant de l’affiliation à une association, une organisation ou un syndicat de travailleurs ou de l’exercice d’une activité licite s’y rattachant;
Disqualification — misconduct or leaving without just Cause
Exclusion : inconduite ou départ sans justification
30 (1) A claimant is disqualified from receiving any benefits if the claimant lost any employment because of their misconduct or voluntarily left any employment without just cause, unless
30 (1) Le prestataire est exclu du bénéfice des prestations s’il perd un emploi en raison de son inconduite ou s’il quitte volontairement un emploi sans justification, à moins, selon le cas :
(a) the claimant has, since losing or leaving the employment, been employed in insurable employment for the number of hours required by section 7 or 7.
- Evidence: `issue` cue `issue` at chunk `4507048` offsets `132-137`; context: The issue is not whether the employer was guilty of misconduct by engaging in unjust dismissal; rather, the question is whether the applicant was guilty of misconduct, and whether this misconduct resulted in the applicant’s dismissal from employment: Canada (AG) v McNamara, 2007 FCA 107, [2007] FCJ No 364 [McNamara]; Fleming v Canada (Attorney General), 2006 FCA 16, [2006] FCJ No 31.
- Evidence: `reasoning_application` cue `therefore` at chunk `4507048` offsets `54-63`; context: [14] The EIA does not define “misconduct”; the Member therefore relied on several cases that discuss how the term should apply.
- Evidence: `evidence_fact` cue `found that` at chunk `4507049` offsets `376-386`; context: The Member found that in acting as he did the applicant ought to have known that his conduct was such that it might lead to his dismissal: Canada (AG) v Kaba, 2013 FCA 208; Canada (AG) v Hastings, 2007 FCA 372.

#### 10047:2:subtheme:2 · paragraphs 12-18

- Raw key terms: `applicant, evidence, sst-ad, admitted, appeal, canada, dependency, drug`
- Display key terms: `sst-ad, admitted, dependency, drug`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: sst-ad, admitted, dependency, drug Position/evidence statements: [18] The applicant responded to the SST-AD’s request and submitted that he could not be fired for misconduct for using drugs because he had a drug dependency. Rule/authority context: ” This, the SST-AD considered, failed to provide sufficient details of the grounds of appeal under subsection 58(1) of the DESDA. Application context: The applicant’s assertion that he was wrongfully dismissed was not accepted as a relevant consideration because it is not the employer’s conduct that is in question. | [18] The applicant responded to the SST-AD’s request and submitted that he could not be fired for misconduct for using drugs because he had a drug dependency. Operative outcome context: The applicant’s assertion that he was wrongfully dismissed was not accepted as a relevant consideration because it is not the employer’s conduct that is in question. | The applicant admitted to smoking marijuana on a regular basis to help him sleep but he denied that he smokes before or at work. Evidence spans paragraphs 12-18. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4507050` offsets `255-263`; context: The applicant’s assertion that he was wrongfully dismissed was not accepted as a relevant consideration because it is not the employer’s conduct that is in question.
- Evidence: `evidence_fact` cue `found that` at chunk `4507050` offsets `16-26`; context: [16] The Member found that the applicant’s positive drug test result is what led to his dismissal.
- Evidence: `governing_rule` cue `under` at chunk `4507050` offsets `827-832`; context: ” This, the SST-AD considered, failed to provide sufficient details of the grounds of appeal under subsection 58(1) of the DESDA.
- Evidence: `reasoning_application` cue `because` at chunk `4507050` offsets `203-210`; context: The applicant’s assertion that he was wrongfully dismissed was not accepted as a relevant consideration because it is not the employer’s conduct that is in question.
- Evidence: `disposition` cue `dismissed` at chunk `4507050` offsets `148-157`; context: The applicant’s assertion that he was wrongfully dismissed was not accepted as a relevant consideration because it is not the employer’s conduct that is in question.
- Evidence: `party_position` cue `submitted` at chunk `4507051` offsets `57-66`; context: [18] The applicant responded to the SST-AD’s request and submitted that he could not be fired for misconduct for using drugs because he had a drug dependency.
- Evidence: `reasoning_application` cue `because` at chunk `4507051` offsets `125-132`; context: [18] The applicant responded to the SST-AD’s request and submitted that he could not be fired for misconduct for using drugs because he had a drug dependency.
- Evidence: `disposition` cue `denied` at chunk `4507051` offsets `247-253`; context: The applicant admitted to smoking marijuana on a regular basis to help him sleep but he denied that he smokes before or at work.
- Evidence: `evidence_fact` cue `found that` at chunk `4507052` offsets `126-136`; context: The SST-AD found that the applicant’s submissions on his drug dependency and his reliance on the Alberta Human Rights Act did not disclose an appeal with a reasonable chance of success.
- Evidence: `evidence_fact` cue `record` at chunk `4507053` offsets `43-49`; context: [21] In a judicial review application, the record is usually confined to that which was before the Tribunal decision-maker: Lemiecha (Litigation guardian of) v Canada (Minister of Employment and Immigration), [1993] FCJ No 1333 (FCTD) at para 4.
- Evidence: `evidence_fact` cue `evidence` at chunk `4507055` offsets `17-25`; context: [23] There is no evidence of a breach of procedural fairness or of bias on the part of the Tribunal in these proceedings.
- Evidence: `evidence_fact` cue `evidence` at chunk `4507056` offsets `11-19`; context: [24] Fresh evidence may also be admitted where the material is considered general background information that would assist the Court.

#### 10047:2:subtheme:3 · paragraphs 19-22

- Raw key terms: `applicant, alcohol, drug, employer, failed, record, refusing, test`
- Display key terms: `alcohol, drug, employer, failed, refusing`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: alcohol, drug, employer, failed, refusing Position/evidence statements: [27] The applicant argues that he has a substance abuse problem related to his ADHD and that he should have been given the opportunity to access a treatment program rather than have his employment terminated. Rule/authority context: The results of the drug test show that he was not under the influence of marijuana at work as they were below the level that would indicate impairment. Application context: Accordingly, they are inadmissible in this judicial review. | He contends that he was entitled to receive unemployment benefits because of his employer’s misconduct in wrongfully dismissing him. Operative outcome context: Paradis contends that he was wrongfully dismissed by his employer. | Wagner stated that the applicant was dismissed by the employer for drinking alcohol on the work site. Evidence spans paragraphs 19-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4507057` offsets `283-291`; context: Moreover, they are not, in the Court’s view, relevant to the question that was before the tribunal for reasons that I will discuss below.
- Evidence: `evidence_fact` cue `record` at chunk `4507057` offsets `119-125`; context: [25] The Alberta Human Rights Act policy on drug and alcohol dependencies in Alberta workplaces, the childhood medical record and the cannabis prescription fall within no exception to the principle against fresh evidence.
- Evidence: `governing_rule` cue `under` at chunk `4507057` offsets `624-629`; context: The results of the drug test show that he was not under the influence of marijuana at work as they were below the level that would indicate impairment.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4507057` offsets `360-371`; context: Accordingly, they are inadmissible in this judicial review.
- Evidence: `disposition` cue `dismissed` at chunk `4507057` offsets `547-556`; context: Paradis contends that he was wrongfully dismissed by his employer.
- Evidence: `party_position` cue `argues` at chunk `4507058` offsets `19-25`; context: [27] The applicant argues that he has a substance abuse problem related to his ADHD and that he should have been given the opportunity to access a treatment program rather than have his employment terminated.
- Evidence: `reasoning_application` cue `because` at chunk `4507058` offsets `275-282`; context: He contends that he was entitled to receive unemployment benefits because of his employer’s misconduct in wrongfully dismissing him.
- Evidence: `evidence_fact` cue `record` at chunk `4507059` offsets `339-345`; context: There is nothing in the record to support that allegation.
- Evidence: `disposition` cue `dismissed` at chunk `4507059` offsets `250-259`; context: Wagner stated that the applicant was dismissed by the employer for drinking alcohol on the work site.
- Evidence: `evidence_fact` cue `record` at chunk `4507060` offsets `30-36`; context: Wagner corrected the record with a phone call to the Commission on May 22, 2015.

#### 10047:2:subtheme:4 · paragraphs 23-26

- Raw key terms: `applicant, sst-ad, sst-gd, decision, employer, appeal, chance, context`
- Display key terms: `sst-ad, sst-gd, employer, chance, context`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: sst-ad, sst-gd, employer, chance, context Position/evidence statements: The applicant’s reliance on the Alberta Human Rights Act policy on drug and alcohol dependencies in Alberta workplaces to argue that he was wrongfully dismissed is irrelevant. Rule/authority context: [31] Both the SST-AD and the SST-GD were correct in finding that the conduct of the employer is not a relevant consideration under section 30 of the EIA. Application context: At the heart of the matter is whether the SST-GD erred in disqualifying the applicant from receiving benefits because of his own misconduct, not that of the employer. Operative outcome context: The applicant’s reliance on the Alberta Human Rights Act policy on drug and alcohol dependencies in Alberta workplaces to argue that he was wrongfully dismissed is irrelevant. | Leave may only be granted where the applicant satisfies that their appeal has a reasonable chance of success on one or more of the grounds identified in subsection 58(1) of the DESDA: Alves v Canada (AG), 2014 FC 1100, [ Evidence spans paragraphs 23-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4507061` offsets `20-25`; context: [30] That said, the issue of whether the applicant’s dismissal was wrongful is not before this Court.
- Evidence: `party_position` cue `argue` at chunk `4507061` offsets `391-396`; context: The applicant’s reliance on the Alberta Human Rights Act policy on drug and alcohol dependencies in Alberta workplaces to argue that he was wrongfully dismissed is irrelevant.
- Evidence: `reasoning_application` cue `because` at chunk `4507061` offsets `212-219`; context: At the heart of the matter is whether the SST-GD erred in disqualifying the applicant from receiving benefits because of his own misconduct, not that of the employer.
- Evidence: `disposition` cue `dismissed` at chunk `4507061` offsets `420-429`; context: The applicant’s reliance on the Alberta Human Rights Act policy on drug and alcohol dependencies in Alberta workplaces to argue that he was wrongfully dismissed is irrelevant.
- Evidence: `issue` cue `whether` at chunk `4507062` offsets `225-232`; context: Rather, the analysis is focused on the applicant’s act or omission and whether that amounted to misconduct within the meaning of section 30 of the EIA: McNamara, above, at para 22.
- Evidence: `evidence_fact` cue `record` at chunk `4507062` offsets `562-568`; context: Based on the record before it, the SST-GD reasonably found that it was the applicant failing a drug test that led to his dismissal.
- Evidence: `governing_rule` cue `under` at chunk `4507062` offsets `125-130`; context: [31] Both the SST-AD and the SST-GD were correct in finding that the conduct of the employer is not a relevant consideration under section 30 of the EIA.
- Evidence: `disposition` cue `granted` at chunk `4507063` offsets `260-267`; context: Leave may only be granted where the applicant satisfies that their appeal has a reasonable chance of success on one or more of the grounds identified in subsection 58(1) of the DESDA: Alves v Canada (AG), 2014 FC 1100, [2014] FCJ No 1187 at paras 70-73.

#### 10047:2:subtheme:5 · paragraphs 27-29

- Raw key terms: `costs, court, dismissed, federal, judicial, paradis, remedy, review`
- Display key terms: `costs, dismissed, federal, judicial, paradis, remedy, review`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue Display terms: costs, dismissed, federal, judicial, paradis, remedy, review Rule/authority context: Paradis impressed as intelligent, articulate and resourceful in preparing and submitting his application to contest the decision of the SST-AD but the Court is unable under the law and the jurisprudence to provide him wi Operative outcome context: [34] In McNamara, above, at paragraph 23, the Federal Court of Appeal noted that “[t]here are, available to an employee wrongfully dismissed, remedies to sanction the behaviour of an employer other than transferring the  | In the result, the application for judicial review is dismissed. Evidence spans paragraphs 27-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4507065` offsets `437-445`; context: The question of whether the employer should have provided reasonable accommodation to assist the applicant to deal with his drug dependency is a matter for another forum.
- Evidence: `disposition` cue `dismissed` at chunk `4507065` offsets `131-140`; context: [34] In McNamara, above, at paragraph 23, the Federal Court of Appeal noted that “[t]here are, available to an employee wrongfully dismissed, remedies to sanction the behaviour of an employer other than transferring the costs of that behaviour to the Canadian taxpayers by way of unemployment benefits”.
- Evidence: `governing_rule` cue `under` at chunk `4507066` offsets `176-181`; context: Paradis impressed as intelligent, articulate and resourceful in preparing and submitting his application to contest the decision of the SST-AD but the Court is unable under the law and the jurisprudence to provide him with a remedy.
- Evidence: `counterargument_limitation` cue `but` at chunk `4507066` offsets `152-155`; context: Paradis impressed as intelligent, articulate and resourceful in preparing and submitting his application to contest the decision of the SST-AD but the Court is unable under the law and the jurisprudence to provide him with a remedy.
- Evidence: `disposition` cue `dismissed` at chunk `4507066` offsets `296-305`; context: In the result, the application for judicial review is dismissed.

#### Section text

[12] The relevant provisions of the EIA read as follows:
Interpretation
Interprétation
29 For the purposes of sections 30 to 33,
29 Pour l’application des articles 30 à 33 :
(a) employment refers to any employment of the claimant within their qualifying period or their benefit period;
a) emploi s’entend de tout emploi exercé par le prestataire au cours de sa période de référence ou de sa période de prestations;
(b) loss of employment includes a suspension from employment, but does not include loss of, or suspension from, employment on account of membership in, or lawful activity connected with, an association, organization or union of workers;
b) la suspension est assimilée à la perte d’emploi, mais n’est pas assimilée à la perte d’emploi la suspension ou la perte d’emploi résultant de l’affiliation à une association, une organisation ou un syndicat de travailleurs ou de l’exercice d’une activité licite s’y rattachant;
Disqualification — misconduct or leaving without just Cause
Exclusion : inconduite ou départ sans justification
30 (1) A claimant is disqualified from receiving any benefits if the claimant lost any employment because of their misconduct or voluntarily left any employment without just cause, unless
30 (1) Le prestataire est exclu du bénéfice des prestations s’il perd un emploi en raison de son inconduite ou s’il quitte volontairement un emploi sans justification, à moins, selon le cas :
(a) the claimant has, since losing or leaving the employment, been employed in insurable employment for the number of hours required by section 7 or 7.1 to qualify to receive benefits; or
a) que, depuis qu’il a perdu ou quitté cet emploi, il ait exercé un emploi assurable pendant le nombre d’heures requis, au titre de l’article 7 ou 7.1, pour recevoir des prestations de chômage;
(b) the claimant is disentitled under sections 31 to 33 in relation to the employment.
b) qu’il ne soit inadmissible, à l’égard de cet emploi, pour l’une des raisons prévues aux articles 31 à 33.
IV. DECISION UNDER REVIEW A. SST-GD’s Decision [13] The sole issue before the SST-GD was whether a disqualification from receiving benefits should be imposed under sections 29 and 30 of the EIA because the applicant lost his employment by reason of his own “misconduct”.

[14] The EIA does not define “misconduct”; the Member therefore relied on several cases that discuss how the term should apply. The issue is not whether the employer was guilty of misconduct by engaging in unjust dismissal; rather, the question is whether the applicant was guilty of misconduct, and whether this misconduct resulted in the applicant’s dismissal from employment: Canada (AG) v McNamara, 2007 FCA 107, [2007] FCJ No 364 [McNamara]; Fleming v Canada (Attorney General), 2006 FCA 16, [2006] FCJ No 31.

[15] The SST-GD Member stated that the misconduct must cause the loss of employment and that it must be an operative cause. Moreover, the misconduct must be committed by the applicant while employed, and it must constitute a breach of a duty that is expressly noted or implied in the contract of employment: Canada (AG) v Cartier, 2001 FCA 274, [2001] FCJ No 1422. The Member found that in acting as he did the applicant ought to have known that his conduct was such that it might lead to his dismissal: Canada (AG) v Kaba, 2013 FCA 208; Canada (AG) v Hastings, 2007 FCA 372. In this instance, the Member found, the applicant’s actions were wilful to the point that he would or could assume that those actions would result in his dismissal.

[16] The Member found that the applicant’s positive drug test result is what led to his dismissal. The applicant’s assertion that he was wrongfully dismissed was not accepted as a relevant consideration because it is not the employer’s conduct that is in question. At the hearing, the applicant admitted to smoking marijuana every evening to help him sleep. Based on this evidence, the Member noted that the applicant should or could have expected that residual amounts of marijuana would be retained in his system contrary to his employer’s drug and alcohol policy.
B. SST-AD’s Decision [17] The basis for the applicant’s appeal was that his employer did not accept that drug dependency “is protected by the Alberta Human Rights Act.” This, the SST-AD considered, failed to provide sufficient details of the grounds of appeal under subsection 58(1) of the DESDA. The SST-AD contacted the applicant on two occasions requesting him to provide detailed grounds of appeal and provided examples of what constitutes grounds of appeal.

[18] The applicant responded to the SST-AD’s request and submitted that he could not be fired for misconduct for using drugs because he had a drug dependency. The applicant admitted to smoking marijuana on a regular basis to help him sleep but he denied that he smokes before or at work. The applicant also denied that his frequent drug use impacted his skills as “an amazing crane operator”.

[19] The DESDA provides that leave to appeal is to be refused if the appeal has “no reasonable chance of success”. The SST-AD found that the applicant’s submissions on his drug dependency and his reliance on the Alberta Human Rights Act did not disclose an appeal with a reasonable chance of success. In the absence of a reviewable error, the SST-AD found that it could not intervene as it is not its role to re-hear the case de novo. As a result, the applicant’s application for leave to appeal was refused.
V. ANALYSIS Is the new evidence admissible? [20] As noted above, in both his Application Record and at the hearing of this application Mr. Paradis sought to introduce new evidence that was not before the SST-GD when it rendered its decisions.

[21] In a judicial review application, the record is usually confined to that which was before the Tribunal decision-maker: Lemiecha (Litigation guardian of) v Canada (Minister of Employment and Immigration), [1993] FCJ No 1333 (FCTD) at para 4. See also Bernard v Professional Institute of the Public Service of Canada, 2015 FCA 263 [Bernard].

[22] As stated by Justice Stratas in Bernard, above, the reason for this is well known. To allow additional material to be introduced at a judicial review that was not before the decision maker would transform the judicial review hearing into a trial de novo. That is not its purpose. There are exceptions to this principle such as when there are allegations of a breach of procedural fairness or of a reasonable apprehension of bias: Ontario Assn. of Architects v Assn. of Architectural Technologists of Ontario, 2002 FCA 218, [2002] FCJ No 813 at para 30; McFadyen v. Canada (Attorney General) 2005 FCA 360, [2005] FCJ No 1817; Nametco Holdings Ltd v MNR, 2002 FCA 149, [2002] FCJ No 592.

[23] There is no evidence of a breach of procedural fairness or of bias on the part of the Tribunal in these proceedings. The applicant seeks to introduce the fresh evidence to bolster his argument that the SST-GD erred in finding that he was disqualified and the SST-AD erred in refusing to grant him leave to appeal.

[24] Fresh evidence may also be admitted where the material is considered general background information that would assist the Court. See, for example, Chopra v Canada (Treasury Board) [1999] FCJ No 835, 168 FTR 273 at para 9. In that regard, I would consider the employer’s termination letter to be general background information, relevant and admissible.

[25] The Alberta Human Rights Act policy on drug and alcohol dependencies in Alberta workplaces, the childhood medical record and the cannabis prescription fall within no exception to the principle against fresh evidence. Moreover, they are not, in the Court’s view, relevant to the question that was before the tribunal for reasons that I will discuss below. Accordingly, they are inadmissible in this judicial review.
Is the SST-AD’s decision refusing the applicant’s leave to appeal reasonable? [26] Mr. Paradis contends that he was wrongfully dismissed by his employer. The results of the drug test show that he was not under the influence of marijuana at work as they were below the level that would indicate impairment. He argues that his employer fabricated statements to the effect that he refused to comply with a drug test and that he was drinking on the job. His employer failed to provide him with reasonable accommodation in accordance with the Alberta Human Rights Act and its own company policy.

[27] The applicant argues that he has a substance abuse problem related to his ADHD and that he should have been given the opportunity to access a treatment program rather than have his employment terminated. He contends that he was entitled to receive unemployment benefits because of his employer’s misconduct in wrongfully dismissing him. On this basis, the applicant argues that the SST-GD failed to observe a principle of natural justice or otherwise acted beyond or refused to exercise it jurisdiction and the SST-AD erred in refusing to grant him leave to appeal on those grounds.

[28] The employer’s human resources manager, David Wagner, twice misstated the grounds for Mr. Paradis’s termination when contacted by the Commission for information. On the first occasion, on April 21, 2015, Mr. Wagner stated that the applicant was dismissed by the employer for drinking alcohol on the work site. There is nothing in the record to support that allegation. On the second date, May 18, 2015, Mr. Wagner said that the applicant had been dismissed for refusing to carry out a drug test. That statement was patently false as the record of the drug test demonstrates.

[29] Mr. Wagner corrected the record with a phone call to the Commission on May 22, 2015. At that time he stated that the reason for the applicant’s dismissal was that he failed the drug and alcohol test, which violated their company policy. There is nothing in the record to explain why he had previously given the Commission incorrect information.

[30] That said, the issue of whether the applicant’s dismissal was wrongful is not before this Court. At the heart of the matter is whether the SST-GD erred in disqualifying the applicant from receiving benefits because of his own misconduct, not that of the employer. The applicant’s reliance on the Alberta Human Rights Act policy on drug and alcohol dependencies in Alberta workplaces to argue that he was wrongfully dismissed is irrelevant. The issue the Court must ultimately determine is whether the SST-AD erred in refusing to grant the applicant leave to challenge the SST-GD’s decision.

[31] Both the SST-AD and the SST-GD were correct in finding that the conduct of the employer is not a relevant consideration under section 30 of the EIA. Rather, the analysis is focused on the applicant’s act or omission and whether that amounted to misconduct within the meaning of section 30 of the EIA: McNamara, above, at para 22. “Misconduct” in this context means “deliberate” or “wilful”. The SST-GD set out the correct test for determining a claimant’s loss of employment by reason of his own misconduct under sections 29 and 30 of the EIA. Based on the record before it, the SST-GD reasonably found that it was the applicant failing a drug test that led to his dismissal.

[32] The requirement to obtain leave to appeal to the SST-AD from a decision of the SST-GD serves the objective to eliminate appeals that have no reasonable chance of success: Bossé v Canada (AG), 2015 FC 1142, [2015] FCJ No 1342 at para 34. Leave may only be granted where the applicant satisfies that their appeal has a reasonable chance of success on one or more of the grounds identified in subsection 58(1) of the DESDA: Alves v Canada (AG), 2014 FC 1100, [2014] FCJ No 1187 at paras 70-73. In this context, having a reasonable chance of success means “having some arguable ground upon which the proposed appeal might succeed”: Osaj v Canada (AG), 2016 FC 115, [2016] FCJ No 131 at para 12.

[33] While the applicant feels very strongly that he was unfairly treated by his employer, he could not point to a reviewable error in the SST-GD decision or in that of the SST-AD upon which his appeal could succeed. He was unable to identify a failure to observe a principal of natural justice, error in law or erroneous finding of fact. The applicant was given two opportunities to clarify the grounds for appeal and failed to do so. The SST-AD’s decision that the appeal had no reasonable chance of success falls within a range of possible acceptable outcomes which are defensible in respect of the facts and law.

[34] In McNamara, above, at paragraph 23, the Federal Court of Appeal noted that “[t]here are, available to an employee wrongfully dismissed, remedies to sanction the behaviour of an employer other than transferring the costs of that behaviour to the Canadian taxpayers by way of unemployment benefits”. As such, this judicial review is not the appropriate forum through which the applicant can obtain the remedy that he is seeking. The question of whether the employer should have provided reasonable accommodation to assist the applicant to deal with his drug dependency is a matter for another forum.

[35] Mr. Paradis impressed as intelligent, articulate and resourceful in preparing and submitting his application to contest the decision of the SST-AD but the Court is unable under the law and the jurisprudence to provide him with a remedy. In the result, the application for judicial review is dismissed. The respondent has not requested costs and none will be awarded.
JUDGMENT
THIS COURT’S JUDGMENT is that the application for judicial review is dismissed without costs.
“Richard G. Mosley”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
t-649-16
STYLE OF CAUSE:
DANNY PARADIS V THE ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
nOVEMBER 7, 2016


## 10047:3 · paragraphs 30-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `0c6b74eb30be7c2f90f18487d3b70f7d92f2058e2731488c7c28bca06ebea74b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10047:3:subtheme:1 · paragraphs 30-30

- Raw key terms: `appearances, applicant, attorney, canada, danny, dated, deputy, general`
- Display key terms: `danny, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: danny, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 30-30. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND Reasons:
MOSLEY, J.
DATED:
NOVEMBER 17, 2016
APPEARANCES:
Danny Paradis
For The Applicant
(Self-represented)
Hasan Junaid
For The Respondent
SOLICITORS OF RECORD:
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
