# Discussion Units: case 4325

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **76**
- Continuity pairs: **75**
- Discussion Units: **5**
- Paragraph source hashes: **76**
- Sub-themes: **20**

## 4325:1 · paragraphs 0-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4335e441c26ee5213c09c3ced838355e08b82c298aaad51bc24b535a8bcca085`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4325:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicants, canada, pakistan, khan, decision, father, february, immigration`
- Display key terms: `pakistan, khan, father, february`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: pakistan, khan, father, february Rule/authority context: [1] This is an application under s 72 (1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of the decision of the Refugee Appeal Division of the Immigration and Refugee Board of Ca Operative outcome context: [1] This is an application under s 72 (1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of the decision of the Refugee Appeal Division of the Immigration and Refugee Board of Ca Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4246080` offsets `27-32`; context: [1] This is an application under s 72 (1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of the decision of the Refugee Appeal Division of the Immigration and Refugee Board of Canada [RAD], dated December 3, 2018 [Decision], which dismissed the Applicants’ appeal of the Refugee Protection Division of the Immigration and Refugee Board of Canada’s [RPD] decision denying the Applicants’ refugee and person in need of protection claims under ss 96 and 97 of the IRPA.
- Evidence: `disposition` cue `dismissed` at chunk `4246080` offsets `273-282`; context: [1] This is an application under s 72 (1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of the decision of the Refugee Appeal Division of the Immigration and Refugee Board of Canada [RAD], dated December 3, 2018 [Decision], which dismissed the Applicants’ appeal of the Refugee Protection Division of the Immigration and Refugee Board of Canada’s [RPD] decision denying the Applicants’ refugee and person in need of protection claims under ss 96 and 97 of the IRPA.

#### 4325:1:subtheme:2 · paragraphs 6-9

- Raw key terms: `applicants, claims, country, decision, found, hyderabad, irpa, need`
- Display key terms: `claims, country, hyderabad, irpa, need`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: claims, country, hyderabad, irpa, need Rule/authority context: [8] Following a hearing on September 7, 2017, the RPD denied the Applicants’ claims under ss 96 and 97 of the IRPA. | [9] On December 3, 2018, the RAD dismissed the Applicants’ appeal of the RPD’s decision and found that the Applicants had a reasonable IFA in Hyderabad and therefore did not qualify as refugees or persons in need of prot Application context: The TTP considers the Applicants as enemies because their children were born in Canada and they have paid taxes in Canada, which the TTP sees as directly contributing to the war against Islam. | [9] On December 3, 2018, the RAD dismissed the Applicants’ appeal of the RPD’s decision and found that the Applicants had a reasonable IFA in Hyderabad and therefore did not qualify as refugees or persons in need of prot Operative outcome context: [8] Following a hearing on September 7, 2017, the RPD denied the Applicants’ claims under ss 96 and 97 of the IRPA. | [9] On December 3, 2018, the RAD dismissed the Applicants’ appeal of the RPD’s decision and found that the Applicants had a reasonable IFA in Hyderabad and therefore did not qualify as refugees or persons in need of prot Evidence spans paragraphs 6-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4246085` offsets `52-57`; context: Ali’s testimony suggests that the TTP takes issue with the Applicants’ ties to Canada, a country which the TTP believe has waged a war against Islam.
- Evidence: `evidence_fact` cue `testimony` at chunk `4246085` offsets `14-23`; context: Ali’s testimony suggests that the TTP takes issue with the Applicants’ ties to Canada, a country which the TTP believe has waged a war against Islam.
- Evidence: `reasoning_application` cue `because` at chunk `4246085` offsets `202-209`; context: The TTP considers the Applicants as enemies because their children were born in Canada and they have paid taxes in Canada, which the TTP sees as directly contributing to the war against Islam.
- Evidence: `evidence_fact` cue `determined that` at chunk `4246087` offsets `133-148`; context: Although the RPD determined that the Applicants were credible and accepted their allegations, it found that a viable internal flight alternative [IFA] existed within Pakistan in Hyderabad, Sindh.
- Evidence: `governing_rule` cue `under` at chunk `4246087` offsets `84-89`; context: [8] Following a hearing on September 7, 2017, the RPD denied the Applicants’ claims under ss 96 and 97 of the IRPA.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4246087` offsets `116-124`; context: Although the RPD determined that the Applicants were credible and accepted their allegations, it found that a viable internal flight alternative [IFA] existed within Pakistan in Hyderabad, Sindh.
- Evidence: `disposition` cue `denied` at chunk `4246087` offsets `54-60`; context: [8] Following a hearing on September 7, 2017, the RPD denied the Applicants’ claims under ss 96 and 97 of the IRPA.
- Evidence: `evidence_fact` cue `found that` at chunk `4246088` offsets `92-102`; context: [9] On December 3, 2018, the RAD dismissed the Applicants’ appeal of the RPD’s decision and found that the Applicants had a reasonable IFA in Hyderabad and therefore did not qualify as refugees or persons in need of protection under ss 96 and 97 of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `4246088` offsets `227-232`; context: [9] On December 3, 2018, the RAD dismissed the Applicants’ appeal of the RPD’s decision and found that the Applicants had a reasonable IFA in Hyderabad and therefore did not qualify as refugees or persons in need of protection under ss 96 and 97 of the IRPA.
- Evidence: `reasoning_application` cue `therefore` at chunk `4246088` offsets `156-165`; context: [9] On December 3, 2018, the RAD dismissed the Applicants’ appeal of the RPD’s decision and found that the Applicants had a reasonable IFA in Hyderabad and therefore did not qualify as refugees or persons in need of protection under ss 96 and 97 of the IRPA.
- Evidence: `disposition` cue `dismissed` at chunk `4246088` offsets `33-42`; context: [9] On December 3, 2018, the RAD dismissed the Applicants’ appeal of the RPD’s decision and found that the Applicants had a reasonable IFA in Hyderabad and therefore did not qualify as refugees or persons in need of protection under ss 96 and 97 of the IRPA.

#### 4325:1:subtheme:3 · paragraphs 10-11

- Raw key terms: `applicants, evidence, items, prior, pursuant, sixteen, admissible, admit`
- Display key terms: `items, prior, pursuant, sixteen, admissible, admit`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: items, prior, pursuant, sixteen, admissible, admit Position/evidence statements: [10] Prior to analyzing whether a viable IFA existed, the RAD first considered whether the sixteen new items of evidence submitted by the Applicants were admissible pursuant to s 110(4) of the IRPA. Rule/authority context: [10] Prior to analyzing whether a viable IFA existed, the RAD first considered whether the sixteen new items of evidence submitted by the Applicants were admissible pursuant to s 110(4) of the IRPA. | Nevertheless, the RAD decided to admit the new evidence pursuant to s 110(4) because the Applicants could not have anticipated the specific IFA location in advance of the RPD hearing, and this issue was clearly a central Application context: Nevertheless, the RAD decided to admit the new evidence pursuant to s 110(4) because the Applicants could not have anticipated the specific IFA location in advance of the RPD hearing, and this issue was clearly a central Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4246089` offsets `24-31`; context: [10] Prior to analyzing whether a viable IFA existed, the RAD first considered whether the sixteen new items of evidence submitted by the Applicants were admissible pursuant to s 110(4) of the IRPA.
- Evidence: `party_position` cue `submitted` at chunk `4246089` offsets `121-130`; context: [10] Prior to analyzing whether a viable IFA existed, the RAD first considered whether the sixteen new items of evidence submitted by the Applicants were admissible pursuant to s 110(4) of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246089` offsets `112-120`; context: [10] Prior to analyzing whether a viable IFA existed, the RAD first considered whether the sixteen new items of evidence submitted by the Applicants were admissible pursuant to s 110(4) of the IRPA.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4246089` offsets `165-176`; context: [10] Prior to analyzing whether a viable IFA existed, the RAD first considered whether the sixteen new items of evidence submitted by the Applicants were admissible pursuant to s 110(4) of the IRPA.
- Evidence: `issue` cue `issue` at chunk `4246090` offsets `352-357`; context: Nevertheless, the RAD decided to admit the new evidence pursuant to s 110(4) because the Applicants could not have anticipated the specific IFA location in advance of the RPD hearing, and this issue was clearly a central component of the appeal.
- Evidence: `evidence_fact` cue `found that` at chunk `4246090` offsets `13-23`; context: [11] The RAD found that the sixteen new items of evidence, mostly news articles relating to Hyderabad and the TTP, were available prior to the RPD’s decision.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4246090` offsets `215-226`; context: Nevertheless, the RAD decided to admit the new evidence pursuant to s 110(4) because the Applicants could not have anticipated the specific IFA location in advance of the RPD hearing, and this issue was clearly a central component of the appeal.
- Evidence: `reasoning_application` cue `because` at chunk `4246090` offsets `236-243`; context: Nevertheless, the RAD decided to admit the new evidence pursuant to s 110(4) because the Applicants could not have anticipated the specific IFA location in advance of the RPD hearing, and this issue was clearly a central component of the appeal.
- Evidence: `counterargument_limitation` cue `Nevertheless` at chunk `4246090` offsets `159-171`; context: Nevertheless, the RAD decided to admit the new evidence pursuant to s 110(4) because the Applicants could not have anticipated the specific IFA location in advance of the RPD hearing, and this issue was clearly a central component of the appeal.

#### 4325:1:subtheme:4 · paragraphs 12-17

- Raw key terms: `applicants, hyderabad, found, finding, profile, risk, attacks, capacity`
- Display key terms: `hyderabad, finding, profile, risk, attacks, capacity`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: hyderabad, finding, profile, risk, attacks, capacity Rule/authority context: [12] The RAD, however, refused to hold a new hearing based on this new evidence pursuant to s 110(6) of the IRPA as it believed the evidence did not raise a serious issue with respect to the credibility of the Applicants Application context: [13] Moving on to the merits of the appeal, the RAD applied the two-prong test set out in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706, 140 NR 138 (FCA) [Rasaratnam] to assess the IFA pro Evidence spans paragraphs 12-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4246091` offsets `165-170`; context: [12] The RAD, however, refused to hold a new hearing based on this new evidence pursuant to s 110(6) of the IRPA as it believed the evidence did not raise a serious issue with respect to the credibility of the Applicants, nor was it determinative of the refugee protection claim.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246091` offsets `71-79`; context: [12] The RAD, however, refused to hold a new hearing based on this new evidence pursuant to s 110(6) of the IRPA as it believed the evidence did not raise a serious issue with respect to the credibility of the Applicants, nor was it determinative of the refugee protection claim.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4246091` offsets `80-91`; context: [12] The RAD, however, refused to hold a new hearing based on this new evidence pursuant to s 110(6) of the IRPA as it believed the evidence did not raise a serious issue with respect to the credibility of the Applicants, nor was it determinative of the refugee protection claim.
- Evidence: `evidence_fact` cue `found that` at chunk `4246092` offsets `245-255`; context: Having found that it is unlikely that the Applicants would be persecuted or personally subjected to a substantial risk of death or cruel and unusual punishment in Hyderabad, and it is reasonable, in all circumstances, for the Applicants to seek refuge in Hyderabad, the RAD rejected the Applicants’ appeal finding that a reasonable IFA existed in Hyderabad.
- Evidence: `reasoning_application` cue `applied` at chunk `4246092` offsets `52-59`; context: [13] Moving on to the merits of the appeal, the RAD applied the two-prong test set out in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706, 140 NR 138 (FCA) [Rasaratnam] to assess the IFA proposed by the RPD.
- Evidence: `evidence_fact` cue `found that` at chunk `4246094` offsets `22-32`; context: [15] In fact, the RAD found that the evidence does not show that the TTP has the capacity to learn of the Applicants’ return to Pakistan, their relocation to Hyderabad, or their whereabouts in Hyderabad.
- Evidence: `evidence_fact` cue `found that` at chunk `4246095` offsets `23-33`; context: [16] Moreover, the RAD found that the TTP does not often undertake personal targeted attacks in Hyderabad and, when it does, these attacks primarily target high-profile persons and not persons with a profile similar to that of the Applicants.

#### 4325:1:subtheme:5 · paragraphs 18-19

- Raw key terms: `applicants, hyderabad, noted, relocation, applying, balance, barriers, came`
- Display key terms: `hyderabad, noted, relocation, applying, balance, barriers, came`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: hyderabad, noted, relocation, applying, balance, barriers, came Evidence spans paragraphs 18-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4246097` offsets `58-65`; context: [18] The RAD also explicitly noted that it had considered whether the relocation of the Applicants to Hyderabad would leave them unable to contact their family members in Pakistan for fear that the TTP would learn of their whereabouts.
- Evidence: `evidence_fact` cue `found that` at chunk `4246097` offsets `253-263`; context: However, the RAD found that it would be “reasonable to expect that his family members would use a degree of discretion in any discussion about the claimants’ location,” and that Mr.
- Evidence: `counterargument_limitation` cue `However` at chunk `4246097` offsets `236-243`; context: However, the RAD found that it would be “reasonable to expect that his family members would use a degree of discretion in any discussion about the claimants’ location,” and that Mr.

#### 4325:1:subtheme:6 · paragraphs 20-22

- Raw key terms: `applicants, hyderabad, issues, make, matter, review, standard, abroad`
- Display key terms: `hyderabad, issues, make, matter, review, standard, abroad`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: hyderabad, issues, make, matter, review, standard, abroad Rule/authority context: STANDARD OF REVIEW | This Court’s judgment was taken under reserve. Application context: More specifically: Was it unreasonable for the RAD to conclude that the Applicants are unlikely to be personally targeted by the TTP in Hyderabad due to their profile? | The parties’ submissions on the standard of review were therefore made under the Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] framework. Evidence spans paragraphs 20-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `ISSUES` at chunk `4246099` offsets `302-308`; context: ISSUES
- Evidence: `issue` cue `issues` at chunk `4246100` offsets `9-15`; context: [21] The issues to be determined in the present matter solely relate to whether the RAD’s Decision concerning the existence of a viable IFA in Hyderabad was unreasonable.
- Evidence: `governing_rule` cue `STANDARD OF REVIEW` at chunk `4246100` offsets `652-670`; context: STANDARD OF REVIEW
- Evidence: `reasoning_application` cue `conclude` at chunk `4246100` offsets `225-233`; context: More specifically:
Was it unreasonable for the RAD to conclude that the Applicants are unlikely to be personally targeted by the TTP in Hyderabad due to their profile?
- Evidence: `evidence_fact` cue `found that` at chunk `4246101` offsets `550-560`; context: However, given the circumstances in this matter, and the Supreme Court of Canada’s instructions in Vavilov at para 144, this Court found that it was not necessary to ask the parties to make additional submissions on the standard of review.
- Evidence: `governing_rule` cue `under` at chunk `4246101` offsets `264-269`; context: This Court’s judgment was taken under reserve.
- Evidence: `reasoning_application` cue `therefore` at chunk `4246101` offsets `335-344`; context: The parties’ submissions on the standard of review were therefore made under the Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] framework.
- Evidence: `counterargument_limitation` cue `However` at chunk `4246101` offsets `419-426`; context: However, given the circumstances in this matter, and the Supreme Court of Canada’s instructions in Vavilov at para 144, this Court found that it was not necessary to ask the parties to make additional submissions on the standard of review.

#### 4325:1:subtheme:7 · paragraphs 23-24

- Raw key terms: `applicable, reasonableness, review, standard, administrative, application, applies, approach`
- Display key terms: `applicable, reasonableness, review, standard, administrative, applies, approach`
- Argument roles: `counterargument_limitation, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, reasoning_application Display terms: applicable, reasonableness, review, standard, administrative, applies, approach Rule/authority context: [23] In Vavilov, at paras 23-32, the majority sought to simplify how a court selects the standard of review applicable to the issues before it. | [24] There was no disagreement between the parties that the applicable standard of review in this matter was the standard of reasonableness. Application context: The majority did away with the contextual and categorical approach taken in Dunsmuir in favour of instating a presumption that the reasonableness standard applies. Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4246102` offsets `126-132`; context: [23] In Vavilov, at paras 23-32, the majority sought to simplify how a court selects the standard of review applicable to the issues before it.
- Evidence: `governing_rule` cue `standard of review` at chunk `4246102` offsets `89-107`; context: [23] In Vavilov, at paras 23-32, the majority sought to simplify how a court selects the standard of review applicable to the issues before it.
- Evidence: `reasoning_application` cue `applies` at chunk `4246102` offsets `299-306`; context: The majority did away with the contextual and categorical approach taken in Dunsmuir in favour of instating a presumption that the reasonableness standard applies.
- Evidence: `counterargument_limitation` cue `However` at chunk `4246102` offsets `308-315`; context: However, the majority noted that this presumption can be set aside on the basis of (1) clear legislative intent to prescribe a different standard of review (Vavilov, at paras 33-52), and (2) certain scenarios where the rule of law requires the application of the standard of correctness, such as constitutional questions, general questions of law of central importance to the legal system as a whole and questions regarding the jurisdictional boundaries between two or more administrative bodies (Vavilov, at paras 53-64).
- Evidence: `governing_rule` cue `standard of review` at chunk `4246103` offsets `71-89`; context: [24] There was no disagreement between the parties that the applicable standard of review in this matter was the standard of reasonableness.

#### 4325:1:subtheme:8 · paragraphs 25-27

- Raw key terms: `canada, citizenship, court, immigration, para, applicant, deference, reasonableness`
- Display key terms: `para, deference, reasonableness`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: para, deference, reasonableness Rule/authority context: The application of the standard of reasonableness to these issues is also consistent with the existing jurisprudence prior to the Supreme Court of Canada’s decision in Vavilov. Application context: [25] There is nothing to rebut the presumption that the standard of reasonableness applies in this case. | [14] […] Moreover, as the Court noted in Lebedeva v Canada (Minister of Citizenship and Immigration), 2011 FC 1165 at para 32, [2011] FCJ No 1439, determinations concerning an IFA “warrant deference because they involve  Evidence spans paragraphs 25-27. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4246104` offsets `164-170`; context: The application of the standard of reasonableness to these issues is also consistent with the existing jurisprudence prior to the Supreme Court of Canada’s decision in Vavilov.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4246104` offsets `208-221`; context: The application of the standard of reasonableness to these issues is also consistent with the existing jurisprudence prior to the Supreme Court of Canada’s decision in Vavilov.
- Evidence: `reasoning_application` cue `applies` at chunk `4246104` offsets `83-90`; context: [25] There is nothing to rebut the presumption that the standard of reasonableness applies in this case.
- Evidence: `evidence_fact` cue `testimony` at chunk `4246106` offsets `298-307`; context: [14] […] Moreover, as the Court noted in Lebedeva v Canada (Minister of Citizenship and Immigration), 2011 FC 1165 at para 32, [2011] FCJ No 1439, determinations concerning an IFA “warrant deference because they involve not only the evaluation of the applicant’s circumstances, as related by their testimony, but also an expert understanding of the country conditions involved.
- Evidence: `reasoning_application` cue `because` at chunk `4246106` offsets `199-206`; context: [14] […] Moreover, as the Court noted in Lebedeva v Canada (Minister of Citizenship and Immigration), 2011 FC 1165 at para 32, [2011] FCJ No 1439, determinations concerning an IFA “warrant deference because they involve not only the evaluation of the applicant’s circumstances, as related by their testimony, but also an expert understanding of the country conditions involved.

#### 4325:1:subtheme:9 · paragraphs 28-29

- Raw key terms: `canada, decision, minister, provisions, relevant, review, serious, accept`
- Display key terms: `provisions, relevant, review, serious, accept`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: provisions, relevant, review, serious, accept Rule/authority context: Reasonableness is a single standard of review that varies and “takes its colour from the context” (Vavilov, at para 89 citing Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59). Application context: Person in need of protection Personne à protéger 97 (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, th Evidence spans paragraphs 28-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4246107` offsets `102-109`; context: [26] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with whether it “bears the hallmarks of reasonableness — justification, transparency and intelligibility — and whether it is justified in relation to the relevant factual and legal constraints that bear on the decision” (Vavilov, at para 99).
- Evidence: `governing_rule` cue `standard of review` at chunk `4246107` offsets `367-385`; context: Reasonableness is a single standard of review that varies and “takes its colour from the context” (Vavilov, at para 89 citing Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59).
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4246107` offsets `855-861`; context: Put in another way, the Court should intervene only when “there are sufficiently serious shortcomings in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency” (Vavilov, at para 100).
- Evidence: `issue` cue `issue` at chunk `4246108` offsets `5564-5569`; context: …
…
Hearing
Audience
110 (6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
110 (6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause ;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile ;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
- Evidence: `evidence_fact` cue `record` at chunk `4246108` offsets `3576-3582`; context: 1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
- Evidence: `reasoning_application` cue `because` at chunk `4246108` offsets `2336-2343`; context: Person in need of protection
Personne à protéger
97 (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
97 (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture ;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.

#### Section text

Ali v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2020-01-22
Neutral citation
2020 FC 93
File numbers
IMM-6570-18
Decision Content
Date: 20200122
Docket: IMM-6570-18
Citation: 2020 FC 93
Ottawa, Ontario, January 22, 2020
PRESENT: The Honourable Mr. Justice Russell
BETWEEN:
IRFAN ALI
SANA KHAN
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. INTRODUCTION

[1] This is an application under s 72 (1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], for judicial review of the decision of the Refugee Appeal Division of the Immigration and Refugee Board of Canada [RAD], dated December 3, 2018 [Decision], which dismissed the Applicants’ appeal of the Refugee Protection Division of the Immigration and Refugee Board of Canada’s [RPD] decision denying the Applicants’ refugee and person in need of protection claims under ss 96 and 97 of the IRPA.
II. BACKGROUND

[2] The Applicants, Irfan Ali and Sana Khan, are citizens of Pakistan. The couple married in 2013 and have three children together, all of whom were born in Canada.

[3] Mr. Ali arrived in Canada in February 2009 as a Temporary Foreign Worker. He returned to Pakistan for six months in 2013 where he married Ms. Khan. The Applicants returned to Canada in 2014.

[4] In October 2016, while planning to visit family in Pakistan, the Applicants learned of threats made against them by the Tehrik-i-Taliban Pakistan [TTP]. In fact, Mr. Ali’s father received two threatening calls from unknown persons warning that, unless money was paid, they would harm the father and the Applicants if the latter came to Pakistan.

[5] A week later, at least a dozen armed men claiming to be members of the TTP showed up at the father’s home near Mardan in the night and threatened to kill him and the Applicants if the latter were to return to Pakistan unless they paid $500,000. The TTP returned a few months later in February 2017 to deliver the same threats to Mr. Ali’s father, prompting him to seek assistance from the jirga (council of elders) to mediate the conflict. The jirga was unsuccessful in convincing the TTP to pursue a mediated solution to the dispute.

[6] Mr. Ali’s testimony suggests that the TTP takes issue with the Applicants’ ties to Canada, a country which the TTP believe has waged a war against Islam. The TTP considers the Applicants as enemies because their children were born in Canada and they have paid taxes in Canada, which the TTP sees as directly contributing to the war against Islam.

[7] The Applicants subsequently cancelled their plans to visit Pakistan and filed refugee and person in need of protection claims on January 9, 2017.

[8] Following a hearing on September 7, 2017, the RPD denied the Applicants’ claims under ss 96 and 97 of the IRPA. Although the RPD determined that the Applicants were credible and accepted their allegations, it found that a viable internal flight alternative [IFA] existed within Pakistan in Hyderabad, Sindh. The RPD concluded there was “insufficient evidence […] that the TTP would be likely to know of the claimants’ return to the country, would seek out the claimants in other cities or that the claimants have the profile of people likely to be tracked throughout the country.”
III. DECISION UNDER REVIEW

[9] On December 3, 2018, the RAD dismissed the Applicants’ appeal of the RPD’s decision and found that the Applicants had a reasonable IFA in Hyderabad and therefore did not qualify as refugees or persons in need of protection under ss 96 and 97 of the IRPA.

[10] Prior to analyzing whether a viable IFA existed, the RAD first considered whether the sixteen new items of evidence submitted by the Applicants were admissible pursuant to s 110(4) of the IRPA. This was determined using the first three factors set out in Raza v Canada (Citizenship and Immigration), 2007 FCA 385, namely, credibility, relevance, and newness, which were later endorsed in Canada (Citizenship and Immigration) v Singh, 2016 FCA 96 at para 64.

[11] The RAD found that the sixteen new items of evidence, mostly news articles relating to Hyderabad and the TTP, were available prior to the RPD’s decision. Nevertheless, the RAD decided to admit the new evidence pursuant to s 110(4) because the Applicants could not have anticipated the specific IFA location in advance of the RPD hearing, and this issue was clearly a central component of the appeal.

[12] The RAD, however, refused to hold a new hearing based on this new evidence pursuant to s 110(6) of the IRPA as it believed the evidence did not raise a serious issue with respect to the credibility of the Applicants, nor was it determinative of the refugee protection claim. The RAD concluded that after reviewing the new articles, very few were relevant to the ability of the TTP to locate and target the Applicants in Hyderabad, as they largely referenced non-targeted attacks and events that took place in 2013–2014. The RAD found that the two articles directly related to targeted threats/attacks by the TTP in Hyderabad were not sufficiently persuasive to support the Applicants’ position, since the TTP’s actions in these instances targeted higher profile individuals such as a political candidate and a jail chief holding Taliban prisoners.

[13] Moving on to the merits of the appeal, the RAD applied the two-prong test set out in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706, 140 NR 138 (FCA) [Rasaratnam] to assess the IFA proposed by the RPD. Having found that it is unlikely that the Applicants would be persecuted or personally subjected to a substantial risk of death or cruel and unusual punishment in Hyderabad, and it is reasonable, in all circumstances, for the Applicants to seek refuge in Hyderabad, the RAD rejected the Applicants’ appeal finding that a reasonable IFA existed in Hyderabad.

[14] Concerning the first prong of the Rasaratnam test, the RAD justified its finding that the Applicants did not face a risk of persecution or a personal risk in Hyderabad by citing: (1) the capacity and geographic reach of the TTP; (2) the Applicants’ profile; and (3) the size of Hyderabad.

[15] In fact, the RAD found that the evidence does not show that the TTP has the capacity to learn of the Applicants’ return to Pakistan, their relocation to Hyderabad, or their whereabouts in Hyderabad. The RAD notes that the TTP does not operate as a unified and integral organization and has a limited history of activity in Hyderabad as compared to the region formally known as the Federally Administered Tribal Areas [FATA] near the Applicants’ hometown, which is some 1200 km away from Hyderabad.

[16] Moreover, the RAD found that the TTP does not often undertake personal targeted attacks in Hyderabad and, when it does, these attacks primarily target high-profile persons and not persons with a profile similar to that of the Applicants. Given the fact that the Applicants are not politically active and the limited number of incidents in Hyderabad, the RAD found that the Applicants do not meet the profile of individuals historically targeted by the TTP, making it unlikely that the Applicants would be at personal risk from the TTP in Hyderabad.

[17] The RAD also cited numerous reports from the Canadian, UK and Australian governments as well as the United Nations High Commissioner for Refugees to support the finding that Hyderabad is a reasonable IFA for the Applicants. It noted that, along with the reasons stated above, Hyderabad is a “large urban centre” that will provide the Applicants with a “degree of anonymity.”

[18] The RAD also explicitly noted that it had considered whether the relocation of the Applicants to Hyderabad would leave them unable to contact their family members in Pakistan for fear that the TTP would learn of their whereabouts. However, the RAD found that it would be “reasonable to expect that his family members would use a degree of discretion in any discussion about the claimants’ location,” and that Mr. Ali’s father has not had contact with the TTP since February 2017.

[19] As for the second prong of the Rasaratnam test, the RAD noted that, on a balance of probabilities, there are no serious social, economic, or other barriers to make the Applicants’ relocation to Hyderabad unreasonable. The RAD came to this conclusion by applying the test to determine the reasonability of an IFA set out in Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589, 163 NR 232 which, as the RAD notes, sets a very high threshold for what makes an IFA unreasonable.

[20] In particular, the RAD concluded that the multiple languages spoken by the Applicants, their years of education, their work experience abroad, along with Mr. Ali’s international travel experience and Ms. Khan’s familiarity with the Sindh region, make their relocation to Hyderabad reasonable.
IV. ISSUES

[21] The issues to be determined in the present matter solely relate to whether the RAD’s Decision concerning the existence of a viable IFA in Hyderabad was unreasonable. More specifically:
Was it unreasonable for the RAD to conclude that the Applicants are unlikely to be personally targeted by the TTP in Hyderabad due to their profile?
Was it unreasonable for the RAD to conclude that the TTP does not have the capacity and geographic reach to locate the Applicants in Hyderabad?
Does the Decision unreasonably require the Applicants to go into hiding?
Was it unreasonable for the RAD to conclude that the Applicants could relocate to Hyderabad?
V. STANDARD OF REVIEW

[22] This application was argued prior to the Supreme Court of Canada’s recent decisions in Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov] and Bell Canada v Canada (Attorney General), 2019 SCC 66. This Court’s judgment was taken under reserve. The parties’ submissions on the standard of review were therefore made under the Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] framework. However, given the circumstances in this matter, and the Supreme Court of Canada’s instructions in Vavilov at para 144, this Court found that it was not necessary to ask the parties to make additional submissions on the standard of review. I have applied the Vavilov framework in my consideration of the application and it does not change the applicable standards of review in this case nor my conclusions.

[23] In Vavilov, at paras 23-32, the majority sought to simplify how a court selects the standard of review applicable to the issues before it. The majority did away with the contextual and categorical approach taken in Dunsmuir in favour of instating a presumption that the reasonableness standard applies. However, the majority noted that this presumption can be set aside on the basis of (1) clear legislative intent to prescribe a different standard of review (Vavilov, at paras 33-52), and (2) certain scenarios where the rule of law requires the application of the standard of correctness, such as constitutional questions, general questions of law of central importance to the legal system as a whole and questions regarding the jurisdictional boundaries between two or more administrative bodies (Vavilov, at paras 53-64).

[24] There was no disagreement between the parties that the applicable standard of review in this matter was the standard of reasonableness.

[25] There is nothing to rebut the presumption that the standard of reasonableness applies in this case. The application of the standard of reasonableness to these issues is also consistent with the existing jurisprudence prior to the Supreme Court of Canada’s decision in Vavilov. See, for example, Tagne v Canada (Citizenship and Immigration), 2019 FC 273 which summarized the state of the law prior to Vavilov on this matter noting at para 19 that:

[19] It is well-established that a decision-maker’s assessment of an IFA involves questions of mixed fact and law and is subject to review by this Court for reasonableness (Singh v Canada (Citizenship and Immigration), 2017 FC 719 at paras 8-10; Figueroa v Canada (Citizenship and Immigration), 2016 FC 521 at para 13; Kamburona v Canada (Citizenship and Immigration), 2013 FC 1052 at para 18). As a result, the RAD’s assessment of the availability of an IFA to the Applicant in Yaoundé attracts deference (Figueroa at para 13). In Tariq v Canada (Citizenship and Immigration), 2017 FC 1017 at paragraph 14, Justice Boswell explained the reason for the Court’s deference:

[14] […] Moreover, as the Court noted in Lebedeva v Canada (Minister of Citizenship and Immigration), 2011 FC 1165 at para 32, [2011] FCJ No 1439, determinations concerning an IFA “warrant deference because they involve not only the evaluation of the applicant’s circumstances, as related by their testimony, but also an expert understanding of the country conditions involved.”

[26] When reviewing a decision on the standard of reasonableness, the analysis will be concerned with whether it “bears the hallmarks of reasonableness — justification, transparency and intelligibility — and whether it is justified in relation to the relevant factual and legal constraints that bear on the decision” (Vavilov, at para 99). Reasonableness is a single standard of review that varies and “takes its colour from the context” (Vavilov, at para 89 citing Canada (Minister of Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 59). These contextual constraints “dictate the limits and contours of the space in which the decision maker may act and the types of solutions it may adopt” (Vavilov, at para 90). Put in another way, the Court should intervene only when “there are sufficiently serious shortcomings in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency” (Vavilov, at para 100). The Supreme Court of Canada lists two types of fundamental flaws that make a decision unreasonable: (1) a failure of rationality internal to the decision-maker’s reasoning process; and (2) untenability “in light of the relevant factual and legal constraints that bear on it” (Vavilov, at para 101).
VI. STATUTORY PROVISIONS

[27] The following provisions of the IRPA are relevant to this application for judicial review:
Convention refugee
Définition de réfugié
96 A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
96 A qualité de réfugié au sens de la Convention — le réfugié — la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays ;
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Person in need of protection
Personne à protéger
97 (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
97 (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture ;
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
…
…
Appeal to Refugee Appeal Division
Appel devant la Section d’appel des réfugiés
Procedure
Fonctionnement
110 (3) Subject to subsections (3.1), (4) and (6), the Refugee Appeal Division must proceed without a hearing, on the basis of the record of the proceedings of the Refugee Protection Division, and may accept documentary evidence and written submissions from the Minister and the person who is the subject of the appeal and, in the case of a matter that is conducted before a panel of three members, written submissions from a representative or agent of the United Nations High Commissioner for Refugees and any other person described in the rules of the Board.
110 (3) Sous réserve des paragraphes (3,1), (4) et (6), la section procède sans tenir d’audience en se fondant sur le dossier de la Section de la protection des réfugiés, mais peut recevoir des éléments de preuve documentaire et des observations écrites du ministre et de la personne en cause ainsi que, s’agissant d’une affaire tenue devant un tribunal constitué de trois commissaires, des observations écrites du représentant ou mandataire du Haut-Commissariat des Nations Unies pour les réfugiés et de toute autre personne visée par les règles de la Commission.
Evidence that may be presented
Éléments de preuve admissibles
110 (4) On appeal, the person who is the subject of the appeal may present only evidence that arose after the rejection of their claim or that was not reasonably available, or that the person could not reasonably have been expected in the circumstances to have presented, at the time of the rejection.
110 (4) Dans le cadre de l’appel, la personne en cause ne peut présenter que des éléments de preuve survenus depuis le rejet de sa demande ou qui n’étaient alors pas normalement accessibles ou, s’ils l’étaient, qu’elle n’aurait pas normalement présentés, dans les circonstances, au moment du rejet.
…
…
Hearing
Audience
110 (6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
110 (6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause ;
(b) that

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 4325:2 · paragraphs 30-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `822697887d06c59cc575e8948eb7bdb2c4512baf148face0e876fb39fd29caf9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4325:2:subtheme:1 · paragraphs 30-41

- Raw key terms: `applicants, unreasonable, canada, immigration, citizenship, court, analysis, because`
- Display key terms: `unreasonable, analysis, because`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: unreasonable, analysis, because Position/evidence statements: [28] The Applicants submit that the Decision is unreasonable because of: the RAD’s speculative analysis of the Applicants’ profile; the RAD’s failure to consider critical information regarding the TTP’s capacity and its  | [29] Concerning the RAD’s analysis of the Applicants’ profile, the Applicants submit that the RAD failed to consider the fact that they have already attracted the attention of the TTP. Application context: [28] The Applicants submit that the Decision is unreasonable because of: the RAD’s speculative analysis of the Applicants’ profile; the RAD’s failure to consider critical information regarding the TTP’s capacity and its  | ” As such, it is unreasonable in these circumstances to conclude that the Applicants’ profile is not one that would likely be targeted by the TTP if the Applicants return to Pakistan simply because the Applicants do not  Evidence spans paragraphs 30-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submit` at chunk `4246109` offsets `20-26`; context: [28] The Applicants submit that the Decision is unreasonable because of:
the RAD’s speculative analysis of the Applicants’ profile;
the RAD’s failure to consider critical information regarding the TTP’s capacity and its presence in Hyderabad;
the effect of the Decision which, for all intents and purposes, requires the Applicants to go into hiding; and
the RAD’s failure to consider the integration barriers and security risks the Applicants will face in Hyderabad.
- Evidence: `reasoning_application` cue `because` at chunk `4246109` offsets `61-68`; context: [28] The Applicants submit that the Decision is unreasonable because of:
the RAD’s speculative analysis of the Applicants’ profile;
the RAD’s failure to consider critical information regarding the TTP’s capacity and its presence in Hyderabad;
the effect of the Decision which, for all intents and purposes, requires the Applicants to go into hiding; and
the RAD’s failure to consider the integration barriers and security risks the Applicants will face in Hyderabad.
- Evidence: `party_position` cue `submit` at chunk `4246110` offsets `78-84`; context: [29] Concerning the RAD’s analysis of the Applicants’ profile, the Applicants submit that the RAD failed to consider the fact that they have already attracted the attention of the TTP.
- Evidence: `reasoning_application` cue `conclude` at chunk `4246111` offsets `338-346`; context: ” As such, it is unreasonable in these circumstances to conclude that the Applicants’ profile is not one that would likely be targeted by the TTP if the Applicants return to Pakistan simply because the Applicants do not neatly fit into one of the profiles outlined in the national documentation package.
- Evidence: `evidence_fact` cue `found that` at chunk `4246112` offsets `222-232`; context: In Qaddafi, the Court found that it was unreasonable for the RAD to speculate that the applicant would no longer be targeted because he had ceased working for the UN.
- Evidence: `reasoning_application` cue `because` at chunk `4246112` offsets `325-332`; context: In Qaddafi, the Court found that it was unreasonable for the RAD to speculate that the applicant would no longer be targeted because he had ceased working for the UN.
- Evidence: `evidence_fact` cue `found that` at chunk `4246113` offsets `165-175`; context: [32] The Applicants also cite Mendoza v Canada (Citizenship and Immigration), 2014 FC 715 where the Court summarizes a previous order rendered by Justice Kane which found that the assessment of the risk faced by the applicants in the proposed IFA was speculative.
- Evidence: `party_position` cue `argue` at chunk `4246114` offsets `25-30`; context: [33] The Applicants also argue that the RAD did not rely on the most recent evidence at hand when determining that the TTP does not have the “operational capacity or geographic reach” to locate and target the Applicants in Hyderabad.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246114` offsets `76-84`; context: [33] The Applicants also argue that the RAD did not rely on the most recent evidence at hand when determining that the TTP does not have the “operational capacity or geographic reach” to locate and target the Applicants in Hyderabad.
- Evidence: `party_position` cue `argue` at chunk `4246115` offsets `30-35`; context: [34] Moreover, the Applicants argue that the Decision is unreasonable as it effectively forces the Applicants to hide their whereabouts from their own family to avoid alerting the TTP to their presence in Pakistan.
- Evidence: `evidence_fact` cue `found that` at chunk `4246115` offsets `567-577`; context: ” The Applicants cite Zamora Huerta v Canada (Citizenship and Immigration), 2008 FC 586 [Zamora Huerta] in support of their position, a decision where this Court found that not being able to share one’s whereabouts with family or friends is tantamount to requiring applicants to go into hiding and is therefore unreasonable.
- Evidence: `reasoning_application` cue `because` at chunk `4246115` offsets `249-256`; context: The Applicants argue that this is because their family lives near the TTP and “a reasonable inference can be made that the TTP could threaten the Applicants’ family to reveal their location.
- Evidence: `party_position` cue `argue` at chunk `4246116` offsets `29-34`; context: [35] Finally, the Applicants argue that their Pashto accents and their Canadian children, who speak English and have a Western accent, would prevent them from “blending in” while in Hyderabad, and would render them visible to the TTP.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246116` offsets `260-268`; context: They also argue that the evidence in this case clearly establishes that the security situation in Hyderabad is unstable as there have been several suicide bombings and terrorist attacks.
- Evidence: `party_position` cue `argues` at chunk `4246117` offsets `20-26`; context: [36] The Respondent argues that the RAD’s conclusions that there is an IFA in Hyderabad falls within the range of acceptable outcomes that were available following a thorough and proper analysis of the law and facts in this case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246117` offsets `454-462`; context: More specifically, the Respondent points to the “high onus” on the Applicants to establish that the proposed IFA is unreasonable and argues that the Applicants’ argument “is merely an invitation to this Court to reweigh the evidence.

#### Section text

[28] The Applicants submit that the Decision is unreasonable because of:
the RAD’s speculative analysis of the Applicants’ profile;
the RAD’s failure to consider critical information regarding the TTP’s capacity and its presence in Hyderabad;
the effect of the Decision which, for all intents and purposes, requires the Applicants to go into hiding; and
the RAD’s failure to consider the integration barriers and security risks the Applicants will face in Hyderabad.

[29] Concerning the RAD’s analysis of the Applicants’ profile, the Applicants submit that the RAD failed to consider the fact that they have already attracted the attention of the TTP. The Applicants have been explicitly warned by the TTP, on numerous occasions, that they and their family will be harmed if they return to Pakistan. The RAD unreasonably chose to ignore this fact and conducted its own speculative analysis regarding the intent of the TTP.

[30] The Applicants point out that there was no indication that the TTP had lost interest in targeting them, no indication that they did not intend to follow through with their threats, and no indication that they no longer believed that the Applicants support a “war against Islam.” As such, it is unreasonable in these circumstances to conclude that the Applicants’ profile is not one that would likely be targeted by the TTP if the Applicants return to Pakistan simply because the Applicants do not neatly fit into one of the profiles outlined in the national documentation package.

[31] The Applicants rely on Qaddafi v Canada (Citizenship and Immigration), 2016 FC 629 [Qaddafi] to support their argument that the RAD’s analysis regarding the Applicants’ profile was unreasonable. In Qaddafi, the Court found that it was unreasonable for the RAD to speculate that the applicant would no longer be targeted because he had ceased working for the UN. The threats received by the applicant in Qaddafi were clear, and there was no evidence to suggest that the agent of persecution did not intend to follow through on its threats because the applicant did not have a sufficient profile. In fact, the Court noted that the applicant “obviously had a sufficient profile to provoke the threat” (Qaddafi at para 76).

[32] The Applicants also cite Mendoza v Canada (Citizenship and Immigration), 2014 FC 715 where the Court summarizes a previous order rendered by Justice Kane which found that the assessment of the risk faced by the applicants in the proposed IFA was speculative. The Court found that it was unreasonable for the RPD to decide that the applicants were no longer active targets while at the same time accepting that they had been specifically targeted by the agent of persecution. In fact, the Court cites Justice Kane’s finding at para 7 noting that: “speculation about how the Zetas [(the agent of persecution in that case)] would operate vis à vis the applicants is illogical and unreasonable” given the explicit threats made against them.

[33] The Applicants also argue that the RAD did not rely on the most recent evidence at hand when determining that the TTP does not have the “operational capacity or geographic reach” to locate and target the Applicants in Hyderabad. In fact, the Applicants argue that the RAD ignored a critical article published by The Daily Beast, three years after the report relied upon, which documents the intent of the Taliban to unify in Pakistan and in Afghanistan. The Applicants argue that the RAD also erred in its consideration of an article regarding the killing of a political candidate in Hyderabad by the TTP, as well as another article detailing threats made by the TTP to a Hyderabad jail superintendent. The Applicants are not asking this Court to re-weigh the evidence; it is trite law that a decision-maker’s failure to analyze critical evidence that contradicts its finding is unreasonable (Cepeda-Gutierrez v Canada (Minister of Citizenship and Immigration), 157 FTR 35 at para 17, FCJ No 1425 [Cepeda-Gutierrez]).

[34] Moreover, the Applicants argue that the Decision is unreasonable as it effectively forces the Applicants to hide their whereabouts from their own family to avoid alerting the TTP to their presence in Pakistan. The Applicants argue that this is because their family lives near the TTP and “a reasonable inference can be made that the TTP could threaten the Applicants’ family to reveal their location.” The Applicants cite Zamora Huerta v Canada (Citizenship and Immigration), 2008 FC 586 [Zamora Huerta] in support of their position, a decision where this Court found that not being able to share one’s whereabouts with family or friends is tantamount to requiring applicants to go into hiding and is therefore unreasonable.

[35] Finally, the Applicants argue that their Pashto accents and their Canadian children, who speak English and have a Western accent, would prevent them from “blending in” while in Hyderabad, and would render them visible to the TTP. They also argue that the evidence in this case clearly establishes that the security situation in Hyderabad is unstable as there have been several suicide bombings and terrorist attacks. As such, they state that Hyderabad is not a reasonable IFA in this case.
B. Respondent

[36] The Respondent argues that the RAD’s conclusions that there is an IFA in Hyderabad falls within the range of acceptable outcomes that were available following a thorough and proper analysis of the law and facts in this case. More specifically, the Respondent points to the “high onus” on the Applicants to establish that the proposed IFA is unreasonable and argues that the Applicants’ argument “is merely an invitation to this Court to reweigh the evidence.”

[37] The Respondent cites this Court’s decisions in Enhodor v Canada (Citizenship and Immigration), 2017 FC 1143 at para 10 and in Pidhorna v Canada (Citizenship and Immigration), 2016 FC 1 at paras 39-42, and suggests that the latter provides an excellent overview of the state of the law on this point:

[39] The test for an IFA is well established. There is a high onus on the applicant to demonstrate that a proposed IFA is unreasonable (Ranganathan v Canada (Minister of Citizenship and Immigration), [2001] 2 FC 164, [2000] FCJ No 2118 (FCA)).

[40] The two part test for an IFA was established in Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589, [1993] FCJ No 1172 (QL) (FCA) [Thirunavukkarasu]. The test is: (1) the Board must be satisfied, on a balance of probabilities, that there is no serious possibility of the claimant being persecuted in the proposed IFA; and, (2) conditions in the proposed IFA must be such that it would not be unreasonable, upon consideration of all the circumstances, including consideration of a claimant’s personal circumstances, for the claimant to seek refuge there.

## 4325:3 · paragraphs 42-72

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6a22c19dc5fb6cbfd77cd0ef0e4388112cb9a5fd46812da460dfb3a6baf967b4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4325:3:subtheme:1 · paragraphs 42-43

- Raw key terms: `able, accessible, alternative, area, areas, attainable, available, barriers`
- Display key terms: `able, accessible, alternative, area, areas, attainable, available, barriers`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: able, accessible, alternative, area, areas, attainable, available, barriers No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.

#### 4325:3:subtheme:2 · paragraphs 44-55

- Raw key terms: `evidence, appellants, applicants, pakistan, decision, finds, learn, taliban`
- Display key terms: `appellants, pakistan, finds, learn, taliban`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: appellants, pakistan, finds, learn, taliban Position/evidence statements: [38] In this case, the Respondent argues that the RAD, after considering all submissions and evidence, came to a reasonable conclusion that the Applicants had not established that the TTP in Mardan had the organizational | [40] Finally, the Respondent argues that the Applicants are simply seeking a re-weighing of the evidence by this Court. Application context: The evidence is therefore clear that those in need of protection do not have to belong to a “primary target” group. Evidence spans paragraphs 44-55. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `4246123` offsets `257-264`; context: [42] In Argote et al v Canada (Minister of Citizenship and Immigration), 2009 FC 128 at para 12, [2009] FCJ No 153 (QL), the Court noted that the onus is on an applicant to establish on objective evidence that the relocation to the IFA is unreasonable:
[…] Whether the relocation to the IFA is unreasonable is an objective test and the onus is on the applicants to establish on objective evidence that the relocation to the IFA is unreasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246123` offsets `196-204`; context: [42] In Argote et al v Canada (Minister of Citizenship and Immigration), 2009 FC 128 at para 12, [2009] FCJ No 153 (QL), the Court noted that the onus is on an applicant to establish on objective evidence that the relocation to the IFA is unreasonable:
[…] Whether the relocation to the IFA is unreasonable is an objective test and the onus is on the applicants to establish on objective evidence that the relocation to the IFA is unreasonable.
- Evidence: `party_position` cue `argues` at chunk `4246124` offsets `34-40`; context: [38] In this case, the Respondent argues that the RAD, after considering all submissions and evidence, came to a reasonable conclusion that the Applicants had not established that the TTP in Mardan had the organizational capacity and geographic reach to learn of their relocation to Hyderabad and to target them there.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246124` offsets `93-101`; context: [38] In this case, the Respondent argues that the RAD, after considering all submissions and evidence, came to a reasonable conclusion that the Applicants had not established that the TTP in Mardan had the organizational capacity and geographic reach to learn of their relocation to Hyderabad and to target them there.
- Evidence: `party_position` cue `argues` at chunk `4246126` offsets `29-35`; context: [40] Finally, the Respondent argues that the Applicants are simply seeking a re-weighing of the evidence by this Court.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246126` offsets `96-104`; context: [40] Finally, the Respondent argues that the Applicants are simply seeking a re-weighing of the evidence by this Court.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246128` offsets `22-30`; context: [35] The RAD ﬁnds the evidence does conﬁrm the risk to individuals, especially those of a high proﬁle, during the time period of the articles.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246129` offsets `36-44`; context: [36] The RAD further ﬁnds that this evidence does not indicate that the Taliban has targeted speciﬁc individuals with a proﬁle such as the Appellants, nor does it conﬁrm that the Taliban has the willingness or ability to search for the Appellants outside of their village in the Mardan region of KPK province.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246130` offsets `87-95`; context: [37] The RAD has reviewed the submissions of the Appellants, the available documentary evidence, and ﬁnds that as much as the principal Appellant’s father may have been targeted by individuals in his home village who are members of the TTP, there is not sufﬁcient credible evidence to establish that they have the operational capacity or geographic reach to learn of the Appellants’ return to Pakistan upon arrival at a regular port of entry to the country, or trace the Appellants’ movements within Pakistan.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246131` offsets `59-67`; context: [38] The RAD has previously discussed that the documentary evidence does not support that the TTP has that ability in Pakistan.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246132` offsets `310-318`; context: The evidence is therefore clear that those in need of protection do not have to belong to a “primary target” group.
- Evidence: `reasoning_application` cue `therefore` at chunk `4246132` offsets `322-331`; context: The evidence is therefore clear that those in need of protection do not have to belong to a “primary target” group.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246133` offsets `372-380`; context: The evidence is clear that the Applicants have already been targeted and threatened with death if they return to Pakistan.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246134` offsets `84-92`; context: [44] Consequently, the Decision must stand or fall on the RAD’s conclusion that the evidence does not confirm that “the Taliban has the willingness or ability to search for the Appellants outside of their village in the Mardan region of KPK province” and its finding that:
there is not sufficient credible evidence to establish that [the Taliban] have the operational capacity or geographic reach to learn of the Appellants’ return to Pakistan upon arrival at a regular port of entry to the country, or trace the Appellants’ movements within Pakistan.

#### 4325:3:subtheme:3 · paragraphs 56-57

- Raw key terms: `applicants, issue, pakistan, return, whether, willingness, against, arrival`
- Display key terms: `pakistan, return, whether, willingness, against, arrival`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: pakistan, return, whether, willingness, against, arrival Evidence spans paragraphs 56-57. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4246135` offsets `9-14`; context: [45] The issue of whether the TTP has the “willingness” to search for the Applicants beyond the Mardan region is somewhat tied to the RAD’s mishandling of the Applicants’ profile.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246135` offsets `376-384`; context: The RAD does not question the evidence that the Applicants now have a political/religious aspect to their profile and that the TTP are of the view that they are supporting a western power in a war against Islam.
- Evidence: `issue` cue `issue` at chunk `4246136` offsets `9-14`; context: [46] The issue is not whether the TTP will learn of the Applicants’ return to Pakistan “upon arrival at a regular port of entry […].

#### 4325:3:subtheme:4 · paragraphs 58-59

- Raw key terms: `appellants, degree, evidence, finds, follows, hyderabad, members, pakistan`
- Display key terms: `appellants, degree, finds, follows, hyderabad, members, pakistan`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: appellants, degree, finds, follows, hyderabad, members, pakistan Application context: He further stated, “They have arranged for the celebration that there would be songs and celebrations because is the ﬁrst time my grandchildren are coming and there will be celebrations, he told everyone”. Evidence spans paragraphs 58-59. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4246137` offsets `21-26`; context: [47] On this crucial issue, the RAD summarizes its view of the evidence and finds as follows at para 25:
● The evidence before the RPD and the RAD establishes the TTP in Pakistan does not operate as a uniﬁed, integrated organization that operates within a solitary hierarchical structure;
● The limited documentary evidence that indicates the TTP have been active in Hyderabad;
● The evidence that the Taliban has carried out attacks against state actors and members of religious minorities or others it perceives to be in opposition to its goals, which have taken place mainly in the region previously known as the FATA, close to the Appellants’ home in Peshawar region, and in other regions distant from the proposed IFA locations;
● The proposed IFA in Hyderabad (a city of over 3 million people), qualiﬁes as a “large urban center” that would provide a “degree of anonymity” as stated in the U.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246137` offsets `63-71`; context: [47] On this crucial issue, the RAD summarizes its view of the evidence and finds as follows at para 25:
● The evidence before the RPD and the RAD establishes the TTP in Pakistan does not operate as a uniﬁed, integrated organization that operates within a solitary hierarchical structure;
● The limited documentary evidence that indicates the TTP have been active in Hyderabad;
● The evidence that the Taliban has carried out attacks against state actors and members of religious minorities or others it perceives to be in opposition to its goals, which have taken place mainly in the region previously known as the FATA, close to the Appellants’ home in Peshawar region, and in other regions distant from the proposed IFA locations;
● The proposed IFA in Hyderabad (a city of over 3 million people), qualiﬁes as a “large urban center” that would provide a “degree of anonymity” as stated in the U.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246138` offsets `1086-1094`; context: No additional evidence has been adduced to indicate that the local TTP have an ongoing interest in the Appellants.
- Evidence: `reasoning_application` cue `because` at chunk `4246138` offsets `646-653`; context: He further stated, “They have arranged for the celebration that there would be songs and celebrations because is the ﬁrst time my grandchildren are coming and there will be celebrations, he told everyone”.

#### 4325:3:subtheme:5 · paragraphs 60-64

- Raw key terms: `applicants, members, pakistan, return, whereabouts, appellants, evidence, family`
- Display key terms: `members, pakistan, return, whereabouts, appellants, family`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: members, pakistan, return, whereabouts, appellants, family Rule/authority context: This is not a reasonable requirement and so cannot be used to obviate risk under the first prong. Application context: The Applicants therefore cannot be characterized as ordinary Pakistanis. | There is no basis to conclude that the TTP has lost interest in the Applicants or that they are not likely to approach the family again for further information on their whereabouts. Evidence spans paragraphs 60-64. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4246139` offsets `174-179`; context: This raises the issue of how family members will deal with a direct inquiry from the TTP as to the Applicants’ whereabouts.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246139` offsets `530-538`; context: The RAD’s principal point on this issue is that “[n]o evidence has been adduced to indicate that the local TTP have an ongoing interest in the Appellants.
- Evidence: `counterargument_limitation` cue `However` at chunk `4246139` offsets `861-868`; context: However, there is no evidence at all that the TTP has lost interest in the Applicants and no longer intends to harm them should the opportunity arise.
- Evidence: `governing_rule` cue `under` at chunk `4246140` offsets `272-277`; context: This is not a reasonable requirement and so cannot be used to obviate risk under the first prong.
- Evidence: `reasoning_application` cue `therefore` at chunk `4246141` offsets `189-198`; context: The Applicants therefore cannot be characterized as ordinary Pakistanis.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246142` offsets `396-404`; context: To require new evidence on this point that post-dates the 2017 visit is to lose sight of the grounds for the TTP’s threats against the Applicants and what the TTP now knows about their whereabouts.
- Evidence: `reasoning_application` cue `conclude` at chunk `4246142` offsets `220-228`; context: There is no basis to conclude that the TTP has lost interest in the Applicants or that they are not likely to approach the family again for further information on their whereabouts.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246143` offsets `127-135`; context: [53] When these factors are taken into account, the remaining basis for the Decision is that “there is not sufficient credible evidence that [the TTP] ha[s] the operational capacity or geographical reach to learn of the Appellants’ return to Pakistan upon arrival at a regular port of entry to the country, or trace the Appellants’ movements within Pakistan,” and that “there is little persuasive evidence to support […] that the TTP (the agent of persecution) ha[s] an active presence in Hyderabad or that they have interest or the ability to find the Appellants in the IFA location.

#### 4325:3:subtheme:6 · paragraphs 65-68

- Raw key terms: `applicants, evidence, return, article, beast, conclusion, daily, dispersed`
- Display key terms: `return, article, beast, conclusion, daily, dispersed`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: return, article, beast, conclusion, daily, dispersed Rule/authority context: Meanwhile, The Daily Beast article also describes a dispersed TTP in 2014 (consistent with the report relied on by the RAD) but goes on to detail the TTP’s efforts to rebuild in the following years, their increasing acti Application context: [56] The RAD’s conclusions that the TTP would not have the operational capacity or geographic reach to find or pursue the Applicants in Hyderabad because it does not operate as a unified, integrated organization with a s Evidence spans paragraphs 65-68. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4246144` offsets `40-45`; context: [54] As I have already pointed out, the issue is whether the TTP has the wherewithal to discover that the Applicants are living in Hyderabad.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246145` offsets `252-260`; context: Given the specificity of this threat, there is no evidence to support a conclusion that the TTP is unlikely to target the Applicants if they return to Pakistan.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246146` offsets `279-287`; context: [56] The RAD’s conclusions that the TTP would not have the operational capacity or geographic reach to find or pursue the Applicants in Hyderabad because it does not operate as a unified, integrated organization with a solitary hierarchical structure, fails to take into account evidence that conflicts with such a conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4246146` offsets `146-153`; context: [56] The RAD’s conclusions that the TTP would not have the operational capacity or geographic reach to find or pursue the Applicants in Hyderabad because it does not operate as a unified, integrated organization with a solitary hierarchical structure, fails to take into account evidence that conflicts with such a conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246147` offsets `24-32`; context: [57] Read together, the evidence shows the evolution of the TTP from 2014 to 2017.
- Evidence: `governing_rule` cue `under` at chunk `4246147` offsets `603-608`; context: Meanwhile, The Daily Beast article also describes a dispersed TTP in 2014 (consistent with the report relied on by the RAD) but goes on to detail the TTP’s efforts to rebuild in the following years, their increasing activity outside their traditional region, and the unification of TTP factions under common leadership.

#### 4325:3:subtheme:7 · paragraphs 69-71

- Raw key terms: `applicants, conclusions, consider, evidence, issue, matter, mention, pakistan`
- Display key terms: `conclusions, consider, matter, mention, pakistan`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: conclusions, consider, matter, mention, pakistan Rule/authority context: In accordance with the principles set out in Cepeda-Gutierrez, at paras 14-17, this was a reviewable error that requires this matter to be returned for reconsideration. Application context: The RAD does not address this factor in its Decision because it concludes, mistakenly, that the Applicants are in the same position as ordinary Pakistanis who have no profile with the TTP. | Accordingly, there is no point in addressing the second prong of that test. Evidence spans paragraphs 69-71. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4246148` offsets `285-290`; context: In addition, the RAD’s mistakes about the Applicants’ profile cannot be separated from the issue of the TTP’s motivation to pursue the Applicants.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246148` offsets `65-73`; context: [58] The RAD was, at least, obliged to consider and mention this evidence and provide reasons for discounting it in its conclusions on the operational reach and capacity of the TTP in Pakistan.
- Evidence: `reasoning_application` cue `because` at chunk `4246148` offsets `704-711`; context: The RAD does not address this factor in its Decision because it concludes, mistakenly, that the Applicants are in the same position as ordinary Pakistanis who have no profile with the TTP.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4246148` offsets `256-262`; context: In addition, the RAD’s mistakes about the Applicants’ profile cannot be separated from the issue of the TTP’s motivation to pursue the Applicants.
- Evidence: `issue` cue `issue` at chunk `4246149` offsets `395-400`; context: The Daily Beast article should have alerted the RAD to the issue of whether the information on lack of unification and integration relied upon was still valid.
- Evidence: `evidence_fact` cue `evidence` at chunk `4246149` offsets `578-586`; context: There was clear evidence before the RAD to suggest that conditions had changed and that its conclusions about the TTP’s reach were dated and inaccurate.
- Evidence: `governing_rule` cue `principles` at chunk `4246149` offsets `1039-1049`; context: In accordance with the principles set out in Cepeda-Gutierrez, at paras 14-17, this was a reviewable error that requires this matter to be returned for reconsideration.
- Evidence: `counterargument_limitation` cue `However` at chunk `4246149` offsets `102-109`; context: However, the specific Response to Information Request contained in the national document package which the RAD relied upon for the finding that the TTP does not operate as a unified, integrated organization was prepared in July 2014.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4246150` offsets `117-128`; context: Accordingly, there is no point in addressing the second prong of that test.

#### 4325:3:subtheme:8 · paragraphs 72-72

- Raw key terms: `agree, certification, concurs, counsel, court, question`
- Display key terms: `agree, certification, concurs, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: agree, certification, concurs, question Evidence spans paragraphs 72-72. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4246151` offsets `31-39`; context: [61] Counsel agree there is no question for certification and the Court concurs.

#### Section text

[41] As noted in Thirunavukkarasu:

[14] An IFA cannot be speculative or theoretical only; it must be a realistic, attainable option. Essentially, this means that the alternative place of safety must be realistically accessible to the claimant. Any barriers to getting there should be reasonably surmountable. The claimant cannot be required to encounter great physical danger or to undergo undue hardship in travelling there or in staying there. For example, claimants should not be required to cross battle lines where fighting is going on at great risk to their lives in order to reach a place of safety. Similarly, claimants should not be compelled to hide out in an isolated region of their country, like a cave in the mountains, or in a desert or a jungle, if those are the only areas of internal safety available. But neither is it enough for refugee claimants to say that they do not like the weather in a safe area, or that they have no friends or relatives there, or that they may not be able to find suitable work there. If it is objectively reasonable in these latter cases to live in these places, without fear of persecution, then IFA exists and the claimant is not a refugee.

[42] In Argote et al v Canada (Minister of Citizenship and Immigration), 2009 FC 128 at para 12, [2009] FCJ No 153 (QL), the Court noted that the onus is on an applicant to establish on objective evidence that the relocation to the IFA is unreasonable:
[…] Whether the relocation to the IFA is unreasonable is an objective test and the onus is on the applicants to establish on objective evidence that the relocation to the IFA is unreasonable. It is not for the Board to prove that it is reasonable, as the applicants suggest. [...]

[38] In this case, the Respondent argues that the RAD, after considering all submissions and evidence, came to a reasonable conclusion that the Applicants had not established that the TTP in Mardan had the organizational capacity and geographic reach to learn of their relocation to Hyderabad and to target them there.

[39] Moreover, the Respondent denies that the Decision requires the Applicants to hide their location from their family. The Respondent distinguishes this case from Zamora Huerta as Ms. Zamora had been targeted and located by an agent of the State rather than non-state actors, as is the case of the Applicants.

[40] Finally, the Respondent argues that the Applicants are simply seeking a re-weighing of the evidence by this Court. The Respondent highlights that the Applicants’ arguments primarily rely on the allocation of greater weight to certain newspaper articles as opposed to the contents of the national documentation package for Pakistan. The Respondent submits that the RAD has the discretion to assess and weigh the evidence on the record before coming to a decision, and that such a decision should not be disturbed if it is within the range of acceptable outcomes. The Respondent cites Petrova v Canada (Minister of Citizenship and Immigration), 2004 FC 506 at paras 55-56 in support of this principle.
VIII. ANALYSIS

[41] As regards the first prong of the IFA test set out by the Federal Court of Appeal in Rasaratnam, the heart of the RAD’s Decision is as follows:

[35] The RAD ﬁnds the evidence does conﬁrm the risk to individuals, especially those of a high proﬁle, during the time period of the articles. The RAD having reviewed all of the documentary evidence available ﬁnds there is no persuasive evidence that the Taliban have conducted any operations associated with the targeting of individuals with a proﬁle similar to the Appellants.

[36] The RAD further ﬁnds that this evidence does not indicate that the Taliban has targeted speciﬁc individuals with a proﬁle such as the Appellants, nor does it conﬁrm that the Taliban has the willingness or ability to search for the Appellants outside of their village in the Mardan region of KPK province.

[37] The RAD has reviewed the submissions of the Appellants, the available documentary evidence, and ﬁnds that as much as the principal Appellant’s father may have been targeted by individuals in his home village who are members of the TTP, there is not sufﬁcient credible evidence to establish that they have the operational capacity or geographic reach to learn of the Appellants’ return to Pakistan upon arrival at a regular port of entry to the country, or trace the Appellants’ movements within Pakistan.

[38] The RAD has previously discussed that the documentary evidence does not support that the TTP has that ability in Pakistan. The RAD agrees with the ﬁndings of the RPD in this instance. As such, the RAD ﬁnds the problem faced by the Appellants is limited and local in nature. The RAD ﬁnds the Appellants’ argument must fail.

[42] The RAD relies, inter alia, upon the UK Home Office report which specifically says that “ordinary Pakistanis, including students and those perceived to be opposing the Taliban and other militant groups or not following Sharia law, have also been subject to violence by these groups” (emphasis added). The evidence is therefore clear that those in need of protection do not have to belong to a “primary target” group.

[43] The Applicants have clearly established that they have been targeted and threatened by the TTP. The RAD says that Mr. Ali’s father has been targeted in his home village but, in fact, it is the Applicants who are the primary target and the father is little more than a conduit at the moment, although he would be harmed if the TTP learn of the Applicants’ return. The evidence is clear that the Applicants have already been targeted and threatened with death if they return to Pakistan. The fact that they do not fit some primary target profile is irrelevant.

[44] Consequently, the Decision must stand or fall on the RAD’s conclusion that the evidence does not confirm that “the Taliban has the willingness or ability to search for the Appellants outside of their village in the Mardan region of KPK province” and its finding that:
there is not sufficient credible evidence to establish that [the Taliban] have the operational capacity or geographic reach to learn of the Appellants’ return to Pakistan upon arrival at a regular port of entry to the country, or trace the Appellants’ movements within Pakistan.

[45] The issue of whether the TTP has the “willingness” to search for the Applicants beyond the Mardan region is somewhat tied to the RAD’s mishandling of the Applicants’ profile. The TTP has shown that they are more than willing to threaten the Applicants in Canada and warn them that they face death if they return to any location in Pakistan. The RAD does not question the evidence that the Applicants now have a political/religious aspect to their profile and that the TTP are of the view that they are supporting a western power in a war against Islam.

[46] The issue is not whether the TTP will learn of the Applicants’ return to Pakistan “upon arrival at a regular port of entry […].” Rather, the issue is whether the TTP is likely to learn of the Applicants’ return to Pakistan and their presence in Hyderabad and whether the TTP has either the willingness or the wherewithal to seek them out in that large city to cause them harm.

[47] On this crucial issue, the RAD summarizes its view of the evidence and finds as follows at para 25:
● The evidence before the RPD and the RAD establishes the TTP in Pakistan does not operate as a uniﬁed, integrated organization that operates within a solitary hierarchical structure;
● The limited documentary evidence that indicates the TTP have been active in Hyderabad;
● The evidence that the Taliban has carried out attacks against state actors and members of religious minorities or others it perceives to be in opposition to its goals, which have taken place mainly in the region previously known as the FATA, close to the Appellants’ home in Peshawar region, and in other regions distant from the proposed IFA locations;
● The proposed IFA in Hyderabad (a city of over 3 million people), qualiﬁes as a “large urban center” that would provide a “degree of anonymity” as stated in the U.K. Home Office document; and
● That considering the geographic size of Pakistan, the large number of ports of entry to the country, and the vast population of Hyderabad, it would take a signiﬁcantly coordinated, networked and organized entity to target the Appellants in Hyderabad. The documentary evidence does not support the notion that the TTP has that organizational ability.
[footnotes omitted.]

[48] An obvious concern for the Applicants is that the TTP will learn that they are in Hyderabad through their family members. The RAD deals with this concern as follows at para 26:
The RAD has considered the Appellants’ argument that the Appellants would be unable to contact their family members should they return to Pakistan. The RAD notes that the Appellants clearly testiﬁed that when the Appellants initially planned to return to their village in Pakistan, that the principal Appellant’s father told everyone in town about their return. He further stated, “They have arranged for the celebration that there would be songs and celebrations because is the ﬁrst time my grandchildren are coming and there will be celebrations, he told everyone”. The RAD ﬁnds that it would be reasonable to expect that his family members would use a degree of discretion in any discussion about the Appellants’ location. The RAD further notes that the principal Appellant testiﬁed that the last contact his father had with individuals from the TTP in his village was in February 2017. No additional evidence has been adduced to indicate that the local TTP have an ongoing interest in the Appellants.

[49] The finding here is that Mr. Ali’s father and other family members are unlikely to tell anyone that the Applicants have taken up residence in Hyderabad. This raises the issue of how family members will deal with a direct inquiry from the TTP as to the Applicants’ whereabouts. In my view, it would not be reasonable to expect family members to place their own lives in danger by either denying knowledge of the Applicants’ whereabouts or deliberately misleading the TTP. The RAD’s principal point on this issue is that “[n]o evidence has been adduced to indicate that the local TTP have an ongoing interest in the Appellants.” Indeed, the burden of proof is upon the Applicants to demonstrate on a balance of probabilities that, in accordance with Rasaratnam, there is a serious possibility that the Applicants would be persecuted by the TTP in Hyderabad. However, there is no evidence at all that the TTP has lost interest in the Applicants and no longer intends to harm them should the opportunity arise. The TTP has made it clear that the Applicants will be killed if they return to Pakistan.

[50] Given the dangers posed by knowledge of their whereabouts, or even their return to Pakistan, the Applicants would be forced to hide from family members and friends and cut off communications. This is not a reasonable requirement and so cannot be used to obviate risk under the first prong. This Court noted in Zamora Huerta at para 29 that:
Not to be able to share your whereabouts with family or friends is tantamount to requiring the Applicant to go into hiding. It is also an implicit recognition that even in these large cities, the Applicant is not beyond her common-law spouse’s reach. In these particular circumstances, this cannot constitute an IFA for the Applicant. The Board’s finding of an IFA does not fall within a range of possible, acceptable outcomes which are defensible in respect of the facts and law in the circumstances. As a result, the decision with respect to an IFA is unreasonable and must be set aside.

[51] It also has to be born in mind that the Applicants have lived and worked in Canada since 2009 and they have Canadian children who cannot be kept in hiding in Hyderabad. The Applicants therefore cannot be characterized as ordinary Pakistanis. Their links with Canada are bound to become known, at least locally.

[52] Given that the TTP is fully aware that the Applicants are in Canada, it is no surprise that the TTP has not again approached family members in Pakistan to discover their whereabouts since 2017. There is no basis to conclude that the TTP has lost interest in the Applicants or that they are not likely to approach the family again for further information on their whereabouts. To require new evidence on this point that post-dates the 2017 visit is to lose sight of the grounds for the TTP’s threats against the Applicants and what the TTP now knows about their whereabouts. The Applicants have been warned by the TTP not to return to Pakistan – not just their home district. The evidence is clear that the TTP view the Applicants as enemies because they reside in Canada, have Canadian-born children, and have been paying taxes in Canada. Mr. Ali’s testimony that the TTP regards them as Canadians who have supported a war against Islam was accepted. It is unreasonable for the RAD to suggest that there is no evidence to support that “the local TTP have an ongoing interest in the Appellants.”

[53] When these factors are taken into account, the remaining basis for the Decision is that “there is not sufficient credible evidence that [the TTP] ha[s] the operational capacity or geographical reach to learn of the Appellants’ return to Pakistan upon arrival at a regular port of entry to the country, or trace the Appellants’ movements within Pakistan,” and that “there is little persuasive evidence to support […] that the TTP (the agent of persecution) ha[s] an active presence in Hyderabad or that they have interest or the ability to find the Appellants in the IFA location.” The RPD concluded as follows and this appears to have been endorsed by the RAD:
Overall, the claimants’ proﬁle is not among the groups likely to be targeted throughout the country. The Taliban is splintered and different groups control different areas. It is unlikely that the group that controls Mardan would be aware of the claimant’s [sic] return to Pakistan, would track his whereabouts throughout the country, would coordinate with other Taliban related groups, or with members in Hyderabad, or follow through on an attack in an area such as Hyderabad where they do not exert control and where there is insufﬁcient evidence of likely terrorist attacks and violence. Based on all of this, there is no serious possibility of persecution or a likely risk of harm to the claimants in Hyderabad.

[54] As I have already pointed out, the issue is whether the TTP has the wherewithal to discover that the Applicants are living in Hyderabad. If the Applicants return to Hyderabad, the TTP could discover their whereabouts in the same way they discovered the Applicants were living in Canada.

[55] The Applicants have now been identified by the TTP as enemies of Islam who have assisted a foreign power. They have also been specifically told that if they return to Pakistan they will be killed. Given the specificity of this threat, there is no evidence to support a conclusion that the TTP is unlikely to target the Applicants if they return to Pakistan. The RAD is speculating. There is no evidence before the RAD that the TTP has lost interest in the Applicants or that they have no intention of following through on their threats if the Applicants return to Pakistan. Instead, the Applicants’ profile as described, e.g. supporters of the war against Islam, was sufficient for the TTP to target them in the first place, and it has not changed.

[56] The RAD’s conclusions that the TTP would not have the operational capacity or geographic reach to find or pursue the Applicants in Hyderabad because it does not operate as a unified, integrated organization with a solitary hierarchical structure, fails to take into account evidence that conflicts with such a conclusion. See Cepeda-Gutierrez at paras 14-17. An article in The Daily Beast titled “The Blood-Drenched Return of Pakistan’s Taliban,” published three years after the 2014 Response to Information Request relied upon by the RAD, reports as follows:
Muhammad Khorasni, a spokesman for the TTP militants, sent an email last week announcing that all the fractured Taliban groups are coming together and have appointed a new deputy head of the organization, uniting what had been separate factions.
Another TTP source told The Daily Beast that the organization was dispersed after government offensives that began in 2014, but their ideology and commitment remained and they were able to rebuild. “Your Western media forecasted that the Taliban regime in Afghanistan collapse, but the Taliban regrouped and reorganized. That is exactly what the TTP has been doing since the Pakistan army operations. It bounced back, reorganized, and will take revenge.”
“TTP leaders had a meeting on Jan. 20 near the Af/Pak border,” this source claimed. “All the groups agreed in principle to combine attacks in Afghanistan and Pakistan.”

[57] Read together, the evidence shows the evolution of the TTP from 2014 to 2017. There is a clear difference between the state of the TTP in 2014 and in 2017. The report relied on by the RAD explicitly mentions that the TTP is fractious, is facing its biggest schism yet, and not a unified fighting force. Meanwhile, The Daily Beast article also describes a dispersed TTP in 2014 (consistent with the report relied on by the RAD) but goes on to detail the TTP’s efforts to rebuild in the following years, their increasing activity outside their traditional region, and the unification of TTP factions under common leadership. This evidence was ignored by the RAD.

[58] The RAD was, at least, obliged to consider and mention this evidence and provide reasons for discounting it in its conclusions on the operational reach and capacity of the TTP in Pakistan. In addition, the RAD’s mistakes about the Applicants’ profile cannot be separated from the issue of the TTP’s motivation to pursue the Applicants. They are not ordinary people who have not been targeted and who are unlikely to be targeted. They have already been targeted in a specific way and have been identified as enemies of Islam who should be killed. This necessarily results in an increase in the TTP’s motivation to pursue them and cause them harm. The RAD does not address this factor in its Decision because it concludes, mistakenly, that the Applicants are in the same position as ordinary Pakistanis who have no profile with the TTP.

[59] The Respondent says that the RAD did not consider reports that predated The Daily Beast article. However, the specific Response to Information Request contained in the national document package which the RAD relied upon for the finding that the TTP does not operate as a unified, integrated organization was prepared in July 2014. The Daily Beast article should have alerted the RAD to the issue of whether the information on lack of unification and integration relied upon was still valid. After all, the safety of the Applicants depends upon it being so. There was clear evidence before the RAD to suggest that conditions had changed and that its conclusions about the TTP’s reach were dated and inaccurate. No mention is made of The Daily Beast article. It did not have to be accepted, but it had to be dealt with and weighed against the other information about the TTP’s reach in Pakistan. This is not a weighing issue. Rather, the RAD appears to have ignored evidence that contradicts its own conclusions. In accordance with the principles set out in Cepeda-Gutierrez, at paras 14-17, this was a reviewable error that requires this matter to be returned for reconsideration.

[60] My conclusion is that the RAD has not reasonably addressed the first prong of the Rasaratnam test in this case. Accordingly, there is no point in addressing the second prong of that test. This matter needs to be reconsidered by a differently c

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 4325:4 · paragraphs 73-74

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `f52b363d4bce57ef115c080a348c60b5d33ae55e467a23b9a59ffd2e40f896e3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4325:4:subtheme:1 · paragraphs 73-74

- Raw key terms: `imm-6570-18, alberta, application, calgary, cause, certification, citizenship, constituted`
- Display key terms: `imm-6570-18, alberta, calgary, certification, constituted`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-6570-18, alberta, calgary, certification, constituted Operative outcome context: JUDGMENT IN IMM-6570-18 THIS COURT’S JUDGMENT is that The application is granted and the Decision is quashed. Evidence spans paragraphs 73-74. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4246151` offsets `286-294`; context: There is no question for certification.
- Evidence: `disposition` cue `granted` at chunk `4246151` offsets `154-161`; context: JUDGMENT IN IMM-6570-18
THIS COURT’S JUDGMENT is that
The application is granted and the Decision is quashed.

#### Section text

JUDGMENT IN IMM-6570-18
THIS COURT’S JUDGMENT is that
The application is granted and the Decision is quashed. The matter shall be returned for reconsideration by a differently constituted RAD.
There is no question for certification.
“James Russell”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-6570-18
STYLE OF CAUSE:
IRFAN ALI ET AL v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Calgary, Alberta
DATE OF HEARING:
October 7, 2019


## 4325:5 · paragraphs 75-75

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1736031bb55d4018c12f9f938088ed857038d72eb9f5cdee34bd194fba359146`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4325:5:subtheme:1 · paragraphs 75-75

- Raw key terms: `alberta, appearances, applicants, attorney, audain, bjorn, calgary, camille`
- Display key terms: `alberta, audain, bjorn, calgary, camille`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: alberta, audain, bjorn, calgary, camille No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 75-75. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
RUSSELL J.
DATED:
January 22, 2020
APPEARANCES:
Bjorn Harsanyi
For The Applicants
Camille N. Audain
For The Respondent
SOLICITORS OF RECORD:
Stewart Sharma Harsanyi
Calgary, Alberta
For The Applicants
Attorney General of Canada
Calgary, Alberta
For The Respondent
