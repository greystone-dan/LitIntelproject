# Discussion Units: case 10710

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **26**
- Continuity pairs: **25**
- Discussion Units: **3**
- Paragraph source hashes: **26**
- Sub-themes: **7**

## 10710:1 · paragraphs 0-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `de07088717f9fa4b2fca666c7d09e660d57c2eb079da51e0dc43f424c67f1e2d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10710:1:subtheme:1 · paragraphs 0-1

- Raw key terms: `applicant, canada, date, allowed, application, attorney, benefits, citation`
- Display key terms: `date, allowed, benefits, citation`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: date, allowed, benefits, citation Rule/authority context: [1] The applicant has been granted disability benefits under the Canada Pension Plan, RSC 1985, c C-8 [CPP] retroactive to December 2013 [date of onset]. Operative outcome context: [1] The applicant has been granted disability benefits under the Canada Pension Plan, RSC 1985, c C-8 [CPP] retroactive to December 2013 [date of onset]. Evidence spans paragraphs 0-1. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4539347` offsets `55-60`; context: [1] The applicant has been granted disability benefits under the Canada Pension Plan, RSC 1985, c C-8 [CPP] retroactive to December 2013 [date of onset].
- Evidence: `disposition` cue `granted` at chunk `4539347` offsets `27-34`; context: [1] The applicant has been granted disability benefits under the Canada Pension Plan, RSC 1985, c C-8 [CPP] retroactive to December 2013 [date of onset].

#### 10710:1:subtheme:2 · paragraphs 2-4

- Raw key terms: `appeal, application, canada, decision, division, general, judicial, leave`
- Display key terms: `division, judicial, leave`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: division, judicial, leave Rule/authority context: [3] The impugned decision was made pursuant to subsection 58(2) of the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA], which allows the Appeal Division to refuse leave if the appeal has “no re Operative outcome context: [4] The present judicial review application is dismissed. Evidence spans paragraphs 2-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4539348` offsets `109-114`; context: The sole issue to be determined in this judicial review application is whether the Appeal Division of the Social Security Tribunal of Canada made a reviewable error by dismissing her leave application against the negative decision rendered in this matter by the General Division – Income Security Section who concluded that the applicant was not incapacitated despite her psychiatric condition.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4539349` offsets `35-46`; context: [3] The impugned decision was made pursuant to subsection 58(2) of the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA], which allows the Appeal Division to refuse leave if the appeal has “no reasonable chance of success”.
- Evidence: `disposition` cue `dismissed` at chunk `4539350` offsets `47-56`; context: [4] The present judicial review application is dismissed.

#### 10710:1:subtheme:3 · paragraphs 5-13

- Raw key terms: `applicant, medical, benefits, july, make, application, disability, able`
- Display key terms: `medical, benefits, july, make, disability, able`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: medical, benefits, july, make, disability, able Position/evidence statements: At the time, she did not know that she could receive disability benefits under the CPP until someone suggested that she could submit a late application. | [7] On August 20, 2015, the applicant submitted a declaration of incapacity stating being incapacitated since the July 2008 incident, and therefore unable to apply for benefits sooner. Rule/authority context: She counted on her union to make sure that she would receive disability benefits under the Manitoba Teachers’ Society Disability Benefits Plan – benefits which she effectively received until September 2011. | While recognizing that her health issues and limitations went back to July 2008, December 2013 was nevertheless established as the date of onset, that is the maximum retroactivity allowed under the legislation (see parag Application context: [7] On August 20, 2015, the applicant submitted a declaration of incapacity stating being incapacitated since the July 2008 incident, and therefore unable to apply for benefits sooner. Operative outcome context: While recognizing that her health issues and limitations went back to July 2008, December 2013 was nevertheless established as the date of onset, that is the maximum retroactivity allowed under the legislation (see parag | [12] After having first laid out the applicable legal provisions from the CPP covering eligibility requirements for disability benefits (paragraph 44(1)(b)), the definition of disability (paragraph 42(2)(a)), maximum ret Evidence spans paragraphs 5-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4539351` offsets `1198-1204`; context: In March 2015, she claimed permanent disability based on her diagnosis of PTSD, as well as other medical issues which do not need to be mentioned here.
- Evidence: `party_position` cue `submit` at chunk `4539351` offsets `1066-1072`; context: At the time, she did not know that she could receive disability benefits under the CPP until someone suggested that she could submit a late application.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4539351` offsets `641-650`; context: Unfortunately, as the applicant explains in her affidavit, over the next few years, she was left without medical care, was evicted, and fell into homelessness, all of which exacerbated her trauma.
- Evidence: `governing_rule` cue `under` at chunk `4539351` offsets `467-472`; context: She counted on her union to make sure that she would receive disability benefits under the Manitoba Teachers’ Society Disability Benefits Plan – benefits which she effectively received until September 2011.
- Evidence: `issue` cue `issues` at chunk `4539352` offsets `121-127`; context: While recognizing that her health issues and limitations went back to July 2008, December 2013 was nevertheless established as the date of onset, that is the maximum retroactivity allowed under the legislation (see paragraph 42(2)(b) of the CPP).
- Evidence: `governing_rule` cue `under` at chunk `4539352` offsets `275-280`; context: While recognizing that her health issues and limitations went back to July 2008, December 2013 was nevertheless established as the date of onset, that is the maximum retroactivity allowed under the legislation (see paragraph 42(2)(b) of the CPP).
- Evidence: `counterargument_limitation` cue `nevertheless` at chunk `4539352` offsets `186-198`; context: While recognizing that her health issues and limitations went back to July 2008, December 2013 was nevertheless established as the date of onset, that is the maximum retroactivity allowed under the legislation (see paragraph 42(2)(b) of the CPP).
- Evidence: `disposition` cue `allowed` at chunk `4539352` offsets `267-274`; context: While recognizing that her health issues and limitations went back to July 2008, December 2013 was nevertheless established as the date of onset, that is the maximum retroactivity allowed under the legislation (see paragraph 42(2)(b) of the CPP).
- Evidence: `party_position` cue `submitted` at chunk `4539353` offsets `38-47`; context: [7] On August 20, 2015, the applicant submitted a declaration of incapacity stating being incapacitated since the July 2008 incident, and therefore unable to apply for benefits sooner.
- Evidence: `evidence_fact` cue `evidence` at chunk `4539353` offsets `359-367`; context: She invoked subsection 60(8) of the CPP which provides:
60(8) Where an application for a benefit is made on behalf of a person and the Minister is satisfied, on the basis of evidence provided by or on behalf of that person, that the person had been incapable of forming or expressing an intention to make an application on the person’s own behalf on the day on which the application was actually made, the Minister may deem the application to have been made in the month preceding the first month in which the relevant benefit could have commenced to be paid or in the month that the Minister considers the person’s last relevant period of incapacity to have commenced, whichever is the later.
- Evidence: `reasoning_application` cue `therefore` at chunk `4539353` offsets `138-147`; context: [7] On August 20, 2015, the applicant submitted a declaration of incapacity stating being incapacitated since the July 2008 incident, and therefore unable to apply for benefits sooner.
- Evidence: `evidence_fact` cue `determined that` at chunk `4539354` offsets `49-64`; context: [8] On September 10, 2015, a medical adjudicator determined that the applicant’s medical condition did not stop her from applying earlier, and declined her request for retroactive benefits, relying on the declaration of incapacity form where the applicant’s family physician states that the applicant’s condition does not make her incapable of forming or expressing the intention to make an application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4539355` offsets `892-900`; context: However, in October 2010, he documented that the applicant was able to find solutions to daily practical problems; she was able to make appropriate judgments most of the time; and to plan independently her daily activities;
In November 2011, the same doctor documented that the applicant could perform basic skills of daily living; remember instructions and be self-directed in planning activities;
The Incapacity Form from August 2015 further documented that there is not enough evidence to support incapacity;
No one assisted the applicant with her various medical requests since 2008, and she was able to attend medical appointments and consent to treatments;
She was able to appeal the Manitoba Teachers’ Society disability benefits decision in 2014, as documented in the July 10, 2014 report by a psychiatrist; and
The applicant was able to drive herself around and to use her bank card.
- Evidence: `counterargument_limitation` cue `However` at chunk `4539355` offsets `412-419`; context: However, in October 2010, he documented that the applicant was able to find solutions to daily practical problems; she was able to make appropriate judgments most of the time; and to plan independently her daily activities;
In November 2011, the same doctor documented that the applicant could perform basic skills of daily living; remember instructions and be self-directed in planning activities;
The Incapacity Form from August 2015 further documented that there is not enough evidence to support incapacity;
No one assisted the applicant with her various medical requests since 2008, and she was able to attend medical appointments and consent to treatments;
She was able to appeal the Manitoba Teachers’ Society disability benefits decision in 2014, as documented in the July 10, 2014 report by a psychiatrist; and
The applicant was able to drive herself around and to use her bank card.
- Evidence: `evidence_fact` cue `found that` at chunk `4539357` offsets `26-36`; context: [11] The General Division found that the documentary and testimonial evidence did not support a finding that the applicant was unable of forming or expressing the intention to make an application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4539358` offsets `457-465`; context: 1)) and the incapacity exception to the maximum retroactivity (subsection 60(8)), the General Division based its finding of capacity on the following key pieces of documentary evidence:
The Declaration of Incapacity: the applicant’s family physician states that her incapacity began on November 2, 2008, but that it did not make her incapable of forming or expressing the intention to make an application, and that the evidence was insufficient to support a finding of incapacity;
A medical report from another doctor dated February 3, 2009: it shows a diagnosis of anxiety disorder.
- Evidence: `counterargument_limitation` cue `but` at chunk `4539358` offsets `585-588`; context: 1)) and the incapacity exception to the maximum retroactivity (subsection 60(8)), the General Division based its finding of capacity on the following key pieces of documentary evidence:
The Declaration of Incapacity: the applicant’s family physician states that her incapacity began on November 2, 2008, but that it did not make her incapable of forming or expressing the intention to make an application, and that the evidence was insufficient to support a finding of incapacity;
A medical report from another doctor dated February 3, 2009: it shows a diagnosis of anxiety disorder.
- Evidence: `disposition` cue `allowed` at chunk `4539358` offsets `231-238`; context: [12] After having first laid out the applicable legal provisions from the CPP covering eligibility requirements for disability benefits (paragraph 44(1)(b)), the definition of disability (paragraph 42(2)(a)), maximum retroactivity allowed (paragraph 42(2)(b) and subsection 66.
- Evidence: `evidence_fact` cue `testimony` at chunk `4539359` offsets `58-67`; context: [13] The General Division also considered the applicant’s testimony.

#### 10710:1:subtheme:4 · paragraphs 14-21

- Raw key terms: `appeal, applicant, division, general, application, attorney, chance, disability`
- Display key terms: `division, chance, disability`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: division, chance, disability Position/evidence statements: While the applicant claims she did not know she could apply for CPP disability benefits, she essentially disagrees with the General Division’s findings of fact. | [18] The respondent submits the Appeal Division’s decision refusing leave was reasonable. Rule/authority context: [16] The Appeal Division refused the applicant’s request for leave to appeal on the ground that, pursuant to subsection 58(2) of the DESDA it was “satisfied that the appeal has no reasonable chance of success” [emphasis  | I am also satisfied that the Appeal Division applied the appropriate legal test, as laid out in section 58 of the DESDA and relevant case law. Application context: The General Division therefore dismissed the appeal. | While the applicant claims she did not know she could apply for CPP disability benefits, she essentially disagrees with the General Division’s findings of fact. Operative outcome context: The General Division therefore dismissed the appeal. | Leave to appeal should therefore have been granted by the Appeal Division. Evidence spans paragraphs 14-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4539360` offsets `80-88`; context: [14] Be that as it may, the General Division found that the evidence calls into question a finding of incapacity.
- Evidence: `evidence_fact` cue `found that` at chunk `4539360` offsets `45-55`; context: [14] Be that as it may, the General Division found that the evidence calls into question a finding of incapacity.
- Evidence: `reasoning_application` cue `therefore` at chunk `4539360` offsets `1290-1299`; context: The General Division therefore dismissed the appeal.
- Evidence: `disposition` cue `dismissed` at chunk `4539360` offsets `1300-1309`; context: The General Division therefore dismissed the appeal.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4539362` offsets `97-108`; context: [16] The Appeal Division refused the applicant’s request for leave to appeal on the ground that, pursuant to subsection 58(2) of the DESDA it was “satisfied that the appeal has no reasonable chance of success” [emphasis added].
- Evidence: `party_position` cue `claims` at chunk `4539363` offsets `282-288`; context: While the applicant claims she did not know she could apply for CPP disability benefits, she essentially disagrees with the General Division’s findings of fact.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4539363` offsets `148-157`; context: Both her affidavit and her oral submissions reasserted facts already brought to the attention of previous decision-makers.
- Evidence: `reasoning_application` cue `apply` at chunk `4539363` offsets `316-321`; context: While the applicant claims she did not know she could apply for CPP disability benefits, she essentially disagrees with the General Division’s findings of fact.
- Evidence: `disposition` cue `granted` at chunk `4539363` offsets `701-708`; context: Leave to appeal should therefore have been granted by the Appeal Division.
- Evidence: `party_position` cue `submits` at chunk `4539364` offsets `20-27`; context: [18] The respondent submits the Appeal Division’s decision refusing leave was reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4539364` offsets `363-371`; context: Be that as it may, the dismissal of the leave application is based on the applicable law and shows a reasonable conclusion in light of the evidence on record; it also provides adequate reasons.
- Evidence: `evidence_fact` cue `evidence` at chunk `4539365` offsets `1401-1409`; context: When making such a finding, the General Division needs to consider both the medical evidence and “the relevant activities of the individual concerned between the claimed date of commencement of disability and the date of application” (Morrison at para 5 cited in Danielson at para 6).
- Evidence: `reasoning_application` cue `apply` at chunk `4539365` offsets `1142-1147`; context: Capacity needs to be understood in its ordinary meaning: “the capacity to form the intention to apply for benefits is not different in kind from the capacity to form an intention with respect to other choices which present themselves to an applicant” (Sedrak at para 3).
- Evidence: `party_position` cue `argued` at chunk `4539366` offsets `450-456`; context: The Appeal Division made no reviewable error in refusing to grant leave to appeal and its reasoning is clear and articulated:
(a) The applicant argued that the General Division should not have relied on her family physician’s Declaration of Incapacity, since he was a general practitioner and not a psychiatrist, and therefore less credible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4539366` offsets `1589-1597`; context: The Appeal Division found this was an attempt at reweighing the evidence, which these elements were not determinative.
- Evidence: `governing_rule` cue `legal test` at chunk `4539366` offsets `232-242`; context: I am also satisfied that the Appeal Division applied the appropriate legal test, as laid out in section 58 of the DESDA and relevant case law.
- Evidence: `reasoning_application` cue `applied` at chunk `4539366` offsets `208-215`; context: I am also satisfied that the Appeal Division applied the appropriate legal test, as laid out in section 58 of the DESDA and relevant case law.
- Evidence: `disposition` cue `granted` at chunk `4539366` offsets `3454-3461`; context: As an administrative tribunal, it is only vested with powers granted by statute.

#### 10710:1:subtheme:5 · paragraphs 22-22

- Raw key terms: `applicant, application, costs, court, disability, dismissed, empathizes, hardship`
- Display key terms: `costs, disability, dismissed, empathizes, hardship`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: costs, disability, dismissed, empathizes, hardship Operative outcome context: [22] While the Court empathizes with the hardship suffered and does not question the applicant’s disability, the present application must be dismissed. Evidence spans paragraphs 22-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4539368` offsets `72-80`; context: [22] While the Court empathizes with the hardship suffered and does not question the applicant’s disability, the present application must be dismissed.
- Evidence: `disposition` cue `dismissed` at chunk `4539368` offsets `141-150`; context: [22] While the Court empathizes with the hardship suffered and does not question the applicant’s disability, the present application must be dismissed.

#### Section text

O'Rourke v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2018-05-09
Neutral citation
2018 FC 498
File numbers
T-965-17
Decision Content
Date: 20180509
Docket: T-965-17
Citation: 2018 FC 498
Ottawa, Ontario, May 9, 2018
PRESENT: The Honourable Mr. Justice Martineau
BETWEEN:
DARLA-JEAN O'ROURKE
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS

[1] The applicant has been granted disability benefits under the Canada Pension Plan, RSC 1985, c C-8 [CPP] retroactive to December 2013 [date of onset]. She is not allowed further retroactive benefits unless she can prove her incapacity of forming or expressing an intention to make an application prior to the date of her application, that is, March 18, 2015.

[2] The applicant sought additional benefits, retroactive to July 2008, on the basis of incapacity. The sole issue to be determined in this judicial review application is whether the Appeal Division of the Social Security Tribunal of Canada made a reviewable error by dismissing her leave application against the negative decision rendered in this matter by the General Division – Income Security Section who concluded that the applicant was not incapacitated despite her psychiatric condition.

[3] The impugned decision was made pursuant to subsection 58(2) of the Department of Employment and Social Development Act, SC 2005, c 34 [DESDA], which allows the Appeal Division to refuse leave if the appeal has “no reasonable chance of success”. Such decision is reviewable under the reasonableness standard (see Tracey v Canada (Attorney General), 2015 FC 1300 at para 22).

[4] The present judicial review application is dismissed.
I Background

[5] It is not contested that the applicant has experienced a series of events that rendered her disabled. In July 2008, she was victim of an armed assault at a hotel in Minnesota, United States, where she was to undergo a surgical intervention. She was later diagnosed with Post-Traumatic Stress Disorder [PTSD]. Upon returning to Canada, she tried going back to work, but had to stop. She counted on her union to make sure that she would receive disability benefits under the Manitoba Teachers’ Society Disability Benefits Plan – benefits which she effectively received until September 2011. Unfortunately, as the applicant explains in her affidavit, over the next few years, she was left without medical care, was evicted, and fell into homelessness, all of which exacerbated her trauma. She stopped many of her prior daily activities, including skating, and also abandoned the Masters of Education she had started prior to the incident. At the time, she did not know that she could receive disability benefits under the CPP until someone suggested that she could submit a late application. In March 2015, she claimed permanent disability based on her diagnosis of PTSD, as well as other medical issues which do not need to be mentioned here.

[6] On June 16, 2015, a medical adjudicator concluded that the applicant was disabled. While recognizing that her health issues and limitations went back to July 2008, December 2013 was nevertheless established as the date of onset, that is the maximum retroactivity allowed under the legislation (see paragraph 42(2)(b) of the CPP). Retroactive payments started as of March 2014, that is, four months after the established date of onset (see section 69 of the CPP).

[7] On August 20, 2015, the applicant submitted a declaration of incapacity stating being incapacitated since the July 2008 incident, and therefore unable to apply for benefits sooner. She invoked subsection 60(8) of the CPP which provides:
60(8) Where an application for a benefit is made on behalf of a person and the Minister is satisfied, on the basis of evidence provided by or on behalf of that person, that the person had been incapable of forming or expressing an intention to make an application on the person’s own behalf on the day on which the application was actually made, the Minister may deem the application to have been made in the month preceding the first month in which the relevant benefit could have commenced to be paid or in the month that the Minister considers the person’s last relevant period of incapacity to have commenced, whichever is the later.
60(8) Dans le cas où il est convaincu, sur preuve présentée par le demandeur ou en son nom, que celui-ci n’avait pas la capacité de former ou d’exprimer l’intention de faire une demande le jour où celle-ci a été faite, le ministre peut réputer cette demande de prestation avoir été faite le mois qui précède celui au cours duquel la prestation aurait pu commencer à être payable ou, s’il est postérieur, le mois au cours duquel, selon le ministre, la dernière période pertinente d’incapacité du demandeur a commencé.
[Je souligne]
[Emphasis added.]
[Je souligne.]

[8] On September 10, 2015, a medical adjudicator determined that the applicant’s medical condition did not stop her from applying earlier, and declined her request for retroactive benefits, relying on the declaration of incapacity form where the applicant’s family physician states that the applicant’s condition does not make her incapable of forming or expressing the intention to make an application. The adjudicator also noted several “indicia” of capacity: the applicant could complete and sign her application herself; she did not have a power of attorney; she can manage driving her vehicle and attend appointments and treatment. Finally, the report of her psychiatrist dated July 10, 2014 indicated that she had been appealing a Manitoba Teacher Society disability benefits decision to cut her off from other benefits. As such, the adjudicator concluded that she did not meet the CPP definition of incapacity. The applicant sought reconsideration of this decision.

[9] On October 28, 2015, upon reconsideration, another medical adjudicator concluded that her medical condition did not stop her from applying for disability benefits earlier. The letter lists the following determinative elements, which could not support a finding of incapacity:
In July 2010, the applicant’s family physician stated on her Disability Tax Credit form that the applicant was markedly restricted. However, in October 2010, he documented that the applicant was able to find solutions to daily practical problems; she was able to make appropriate judgments most of the time; and to plan independently her daily activities;
In November 2011, the same doctor documented that the applicant could perform basic skills of daily living; remember instructions and be self-directed in planning activities;
The Incapacity Form from August 2015 further documented that there is not enough evidence to support incapacity;
No one assisted the applicant with her various medical requests since 2008, and she was able to attend medical appointments and consent to treatments;
She was able to appeal the Manitoba Teachers’ Society disability benefits decision in 2014, as documented in the July 10, 2014 report by a psychiatrist; and
The applicant was able to drive herself around and to use her bank card.

[10] The applicant appealed the date of onset to the General Division – Income Security Section.
General Division Decision

[11] The General Division found that the documentary and testimonial evidence did not support a finding that the applicant was unable of forming or expressing the intention to make an application. It was necessary to look at both the medical evidence and the individual’s relevant activities (Morrison v Canada (Minister of Human Resources Development), 1997 CEB & PGR 8679, 1997 CarswellNat 3378 (Canada Pension Appeals Board) [Morrison cited to CarswellNat] cited in Canada (Attorney General) v Danielson, 2008 FCA 78 at para 5 [Danielson]; see also Canada (Attorney General) v Kirkland, 2008 FCA 144 at para 7). The intention required in the sense of the CPP was the same as the capacity to form an intention with respect to any other choices that present themselves to the applicant (Sedrak v Canada (Social Development), 2008 FCA 86 at para 3 [Sedrak]). In this respect, the evidence showed that the applicant was indeed able of forming or expressing the intention to make an application prior to March 2015.

[12] After having first laid out the applicable legal provisions from the CPP covering eligibility requirements for disability benefits (paragraph 44(1)(b)), the definition of disability (paragraph 42(2)(a)), maximum retroactivity allowed (paragraph 42(2)(b) and subsection 66.1(1.1)) and the incapacity exception to the maximum retroactivity (subsection 60(8)), the General Division based its finding of capacity on the following key pieces of documentary evidence:
The Declaration of Incapacity: the applicant’s family physician states that her incapacity began on November 2, 2008, but that it did not make her incapable of forming or expressing the intention to make an application, and that the evidence was insufficient to support a finding of incapacity;
A medical report from another doctor dated February 3, 2009: it shows a diagnosis of anxiety disorder. The other doctor notes an improvement in the applicant’s state after she stopped working. At the time of the report, she was not yet ready to return to work;
A questionnaire supporting the Disability Tax Credit with Canada Revenue dated October 26, 2010: The applicant’s family physician there states that the applicant was able to find solutions, make appropriate judgments, and plan her daily activities independently most of the time;
A letter from the applicant’s family physician dated May 10, 2011: it refers to treatment for a PTSD diagnosis. The doctor states that the applicant had asked him to write a letter supporting the continuance of her long term disability benefits; and
A letter from the applicant’s family physician dated June 25, 2013: it states that the applicant has been repetitively asking for his support in getting long term disability benefits reinstated since she was not ready to go back to work due to PTSD.

[13] The General Division also considered the applicant’s testimony. At the hearing, she recounted the July 2008 assault incident in Minnesota, her return to Manitoba, how she was bullied by her employer, went on medical leave and then got evicted from her home. She initially received long term disability benefits from the Manitoba Teachers’ Society after leaving her job in December 2008. She lived with a friend briefly and then found another apartment, from which she was evicted again, as she was unable to pay rent since her disability payments had temporarily stopped in the summer of 2009. The payments resumed around December 2009, allowing her to live on her own again. They last stopped around February 2012. She became homeless. She has been living with her father since 2013. She explained suffering from PTSD: she tried living the same way she did before in order to heal. She saw her family physician on her own, using public transit. But when she had a medical appointment, it was the only thing she could accomplish during that day. She testified that her body still reacts from her mental trauma. Before the accident she was able to care for her close ones and pursue higher education. She has no Power of Attorney and is responsible for her own decisions.

[14] Be that as it may, the General Division found that the evidence calls into question a finding of incapacity. According to the family physician’s letter from 2010, the applicant was able to find solutions and make appropriate judgments most of the time. According to the other doctor, in February 2009, she had a level of function not congruent with incapacity. In addition, she asked her family physician for letters in support of her other disability payments. This shows that she was able to express herself and participate in treatment. She was capable of forming and expressing an intention to dispute the termination of her long term disability benefits and take actions to attempt to have them reinstated. Moreover, she was able to drive herself to doctors’ appointments or use public transit to do so: driving is an activity that demands constant attention and decision-making. Finally, she had signed no Power of Attorney; she was responsible for her own decisions; she was able to live on her own; find new accommodation when needed; and manage her daily affairs. Her evictions were due to lack of funds, not incapacity. While she still suffers from PTSD, this in itself is not sufficient to prove that she was incapable of filing an application earlier. The General Division therefore dismissed the appeal.

[15] The applicant requested leave to the Appeal Division of the Tribunal, leading to the present judicial review application, following the Appeal Division’s refusal to grant leave.
II Analysis

[16] The Appeal Division refused the applicant’s request for leave to appeal on the ground that, pursuant to subsection 58(2) of the DESDA it was “satisfied that the appeal has no reasonable chance of success” [emphasis added]. In other words, there must be an arguable case (see Kerth v Canada (Minister of Human Resources Development), 173 FTR 102, [1999] FCJ No 1252 (QL) (FCTD); Fancy v Canada (Attorney General), 2010 FCA 63; Bossé v Canada (Attorney General), 2015 FC 1142 at para 10). Substantial deference is owed to the Appeal Division (see Canada (Attorney General) v O'keefe, 2016 FC 503 at para 17).

[17] The applicant is a self-represented litigant. Her legal submissions in this judicial review application are brief, if not inexistent. Both her affidavit and her oral submissions reasserted facts already brought to the attention of previous decision-makers. While the applicant claims she did not know she could apply for CPP disability benefits, she essentially disagrees with the General Division’s findings of fact. She reiterates how she was traumatized, demoralized, dehumanized and hospitalized. She is seeking review on compassionate grounds: she wants to move forward after the injustices she suffered, and needs CPP disability benefits to live. Leave to appeal should therefore have been granted by the Appeal Division.

[18] The respondent submits the Appeal Division’s decision refusing leave was reasonable. The simple fact the applicant does not raise any specific errors or grounds for review is sufficient to uphold the impugned decision. Be that as it may, the dismissal of the leave application is based on the applicable law and shows a reasonable conclusion in light of the evidence on record; it also provides adequate reasons. The applicant essentially disagrees with the General Division decision. It is not the role of the Appeal Division or this Court to substitute itself to the decision-maker. The Appeal Division did not act unreasonably in finding that the appeal had no reasonable chance of success since the applicant’s arguments all amounted to reweighing the evidence.

[19] In the case at bar, the onus was on the applicant to prove that her appeal had a reasonable chance of success on either of the three grounds of appeal listed in subsection 58(1) of the DESDA, that is: (a) a breach of natural justice; (b) an error of law; or (c) an erroneous finding of fact made in a perverse and capricious manner or without regard for the material before it. More particularly, the applicant needed to satisfy the Appeal Division that the General Division erred in fact or law when deciding that she was not “incapable of forming or expressing an intention to make an application on the person’s own behalf on the day on which the application was actually made” (subsection 60(8) of the CPP). The threshold to prove such incapacity is high: “it does not require consideration of the capacity to make, prepare, process or complete an application for disability benefits, but only the capacity, quite simply, of ‘forming or expressing an intention to make an application’” (Morrison at para 5 cited in Danielson at para 5). Capacity needs to be understood in its ordinary meaning: “the capacity to form the intention to apply for benefits is not different in kind from the capacity to form an intention with respect to other choices which present themselves to an applicant” (Sedrak at para 3). When making such a finding, the General Division needs to consider both the medical evidence and “the relevant activities of the individual concerned between the claimed date of commencement of disability and the date of application” (Morrison at para 5 cited in Danielson at para 6). The General Division was entitled to consider the applicant’s daily activities to assess her capacity. The General Division had the opportunity to hear the applicant first hand and to examine all the relevant evidence. Its decision is entitled to significant deference (see Hussein v Canada (Attorney General), 2016 FC 1417 at para 44).

[20] The impugned decision undeniably meets the requirements of justification, transparency and intelligibility (Dunsmuir v New Brunswick, 2008 SCC 9 at para 47). I am also satisfied that the Appeal Division applied the appropriate legal test, as laid out in section 58 of the DESDA and relevant case law. The Appeal Division made no reviewable error in refusing to grant leave to appeal and its reasoning is clear and articulated:
(a) The applicant argued that the General Division should not have relied on her family physician’s Declaration of Incapacity, since he was a general practitioner and not a psychiatrist, and therefore less credible. The Appeal Division found no reasonable chance of success on this ground of appeal since it amounts to disagreement, while not showing why the opinion was not valuable. The General Division is the trier of fact: it was entitled to give weight to a Declaration of Incapacity filed by a general practitioner, especially given the fact it is the applicant herself who asked her family physician to fill this form (see Simpson v Canada (Attorney General), 2012 FCA 82 at para 10; Griffin v Canada (Attorney General), 2016 FC 874 at para 23 [Griffin]). This conclusion of the Appeal Division is reasonable;
(b) The applicant argued that the Disability Tax Credit form indicated that she was not “fit to work”, but stressed that her family physician also wrote that she was “markedly restricted”. He also made a mistake by writing “2006” as the year during which restrictions began. The Appeal Division found this was an attempt at reweighing the evidence, which these elements were not determinative. The General Division could very well conclude that being markedly restricted or no fit to work were insufficient to ground a finding of incapacity in the sense of subsection 60(8) of the CPP. This conclusion of the Appeal Division is reasonable;
(c) The applicant also alleged that her family physician saw her five times, rather than the eleven times stated in the June 25, 2013 letter. The Appeal Division found that this did not amount to a sufficient ground of appeal. The applicant had ample opportunity before the General Division to correct this error and failed to do so, while new evidence cannot be introduced on appeal. This conclusion of the Appeal Division is reasonable, as the appeal should be based on the underlying record before the General Division, rather than on new evidence (see Hideq v Canada (Attorney General), 2017 FC 439 at para 14; Griffin at para 20);
(d) The applicant further argued that the General Division failed to consider the cognitive dissolution triggered by her return to work plan, thereby failing to apply a principle of natural justice. The Appeal Division reiterated that the General Division is presumed to have considered all the evidence. Regardless, these facts alone would not bind the General Division to find that the applicant lacked the capacity to form or express an intention to apply for benefits. This conclusion of the Appeal Division is also reasonable;

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 10710:2 · paragraphs 23-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `85e54dba2fe322bdb6e2dc9eca4ec7948816eb47a9e27205db67750620ce4095`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10710:2:subtheme:1 · paragraphs 23-24

- Raw key terms: `t-965-17, application, attorney, canada, cause, costs, court, darla-jean`
- Display key terms: `t-965-17, costs, darla-jean`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: t-965-17, costs, darla-jean Operative outcome context: JUDGMENT in T-965-17 THIS COURT’S JUDGMENT is that the application for judicial review be dismissed without costs. Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4539368` offsets `279-288`; context: JUDGMENT in T-965-17
THIS COURT’S JUDGMENT is that the application for judicial review be dismissed without costs.

#### Section text

JUDGMENT in T-965-17
THIS COURT’S JUDGMENT is that the application for judicial review be dismissed without costs.
"Luc Martineau"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-965-17
STYLE OF CAUSE:
DARLA-JEAN O'ROURKE v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Winnipeg, Manitoba
DATE OF HEARING:
May 2, 2018


## 10710:3 · paragraphs 25-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `20874c31e5221509d717ed43c54bed9697854dba8b26943fd244460380affebd`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10710:3:subtheme:1 · paragraphs 25-25

- Raw key terms: `appearances, applicant, attorney, behalf, canada, darla-jean, dated, general`
- Display key terms: `behalf, darla-jean, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: behalf, darla-jean, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 25-25. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
MARTINEAU J.
DATED:
maY 9, 2018
APPEARANCES:
Darla-Jean O'Rourke
For The Applicant
(ON HER OWN BEHALF)
Michael Stevenson
For The Respondent
SOLICITORS OF RECORD:
Attorney General of Canada
For The Respondent
