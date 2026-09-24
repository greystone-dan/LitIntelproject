# Discussion Units: case 2044

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **246**
- Continuity pairs: **245**
- Discussion Units: **12**
- Paragraph source hashes: **246**
- Sub-themes: **84**

## 2044:1 · paragraphs 0-6

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `dc94b809883bdb827be7c74fcb1f58628ca8917cacd27e5c3f9aa4c4ab4bc5e5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `guideline, immigration, justice, order, paragraph, reasons, applicant, application`
- Display key terms: `guideline, justice, order, paragraph`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: guideline, justice, order, paragraph Rule/authority context: Each of the 19 applications raises issues regarding a guideline made by the Chairperson of the Immigration and Refugee Board (“IRB”) under the authority of paragraph 159(1)(h) of the Immigration and Refugee Protection Ac Operative outcome context: In reasons dated January 6, 2006, Justice Blanchard found that Guideline 7 unlawfully fettered the discretion of members of the Refugee Protection Division (“RPD”) and held that the decision that was before him would be  Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168129` offsets `213-219`; context: Each of the 19 applications raises issues regarding a guideline made by the Chairperson of the Immigration and Refugee Board (“IRB”) under the authority of paragraph 159(1)(h) of the Immigration and Refugee Protection Act S.
- Evidence: `governing_rule` cue `under` at chunk `4168129` offsets `311-316`; context: Each of the 19 applications raises issues regarding a guideline made by the Chairperson of the Immigration and Refugee Board (“IRB”) under the authority of paragraph 159(1)(h) of the Immigration and Refugee Protection Act S.
- Evidence: `evidence_fact` cue `found that` at chunk `4168130` offsets `350-360`; context: In reasons dated January 6, 2006, Justice Blanchard found that Guideline 7 unlawfully fettered the discretion of members of the Refugee Protection Division (“RPD”) and held that the decision that was before him would be quashed and the applicant’s claim remitted for redetermination by a differently constituted panel.
- Evidence: `disposition` cue `quashed` at chunk `4168130` offsets `518-525`; context: In reasons dated January 6, 2006, Justice Blanchard found that Guideline 7 unlawfully fettered the discretion of members of the Refugee Protection Division (“RPD”) and held that the decision that was before him would be quashed and the applicant’s claim remitted for redetermination by a differently constituted panel.

#### 2044:1:subtheme:2 · paragraphs 3-4

- Raw key terms: `applications, counsel, gibson, issues, justice, ordered, parties, snider`
- Display key terms: `applications, gibson, issues, justice, ordered, snider`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: applications, gibson, issues, justice, ordered, snider Rule/authority context: Following consultations with counsel for the parties, Chief Justice Allan Lutfy ordered that 20 applications be continued as specially managed proceedings and, pursuant to Rule 383, appointed Mr. Evidence spans paragraphs 3-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168131` offsets `170-176`; context: [3] Following the release of Justice Blanchard’s decision in Thamotharem, it became apparent that there were a number of applications for judicial review raising similar issues scheduled to be heard by different judges at various sittings of this Court.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4168131` offsets `414-425`; context: Following consultations with counsel for the parties, Chief Justice Allan Lutfy ordered that 20 applications be continued as specially managed proceedings and, pursuant to Rule 383, appointed Mr.
- Evidence: `issue` cue `issues` at chunk `4168132` offsets `235-241`; context: Upon being satisfied that it was in the interest of justice that the identified Guideline 7 issues be dealt with as expeditiously as is consistent with fairness and justice, Justice Snider ordered the consolidation of the twenty applications.

#### 2044:1:subtheme:3 · paragraphs 5-6

- Raw key terms: `conference, consolidated, counsel, each, following, further, guideline, hearing`
- Display key terms: `conference, consolidated, each, following, further, guideline, hearing`
- Argument roles: `disposition, governing_rule, issue, party_position`
- Explanation: Observed roles: disposition, governing_rule, issue, party_position Display terms: conference, consolidated, each, following, further, guideline, hearing Position/evidence statements: As one of the applicants sought and was granted leave, on consent, to file an IRB document during reply submissions, Counsel were invited to submit further written representations on the content of that document followin Rule/authority context: [5] Pursuant to Rule 105 (a) of the Federal Court Rules, Justice Snider’s Order provided that the consolidated judicial reviews were, in part, to be heard together, or one immediately after the other, at the discretion o Operative outcome context: As one of the applicants sought and was granted leave, on consent, to file an IRB document during reply submissions, Counsel were invited to submit further written representations on the content of that document followin Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168133` offsets `269-275`; context: Further to Rule 107(1), the issues in the consolidated judicial reviews that relate in whole or in part to Guideline 7 were to be determined separately following a single hearing with counsel located in centres outside the Greater Toronto Area participating by video conference if it were impractical to attend in person.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `4168133` offsets `4-15`; context: [5] Pursuant to Rule 105 (a) of the Federal Court Rules, Justice Snider’s Order provided that the consolidated judicial reviews were, in part, to be heard together, or one immediately after the other, at the discretion of the hearing judge.
- Evidence: `issue` cue `issues` at chunk `4168134` offsets `44-50`; context: [6] Prior to the hearing on the Guideline 7 issues, one application was resolved on consent leaving 19 which were the subject of these proceedings.
- Evidence: `party_position` cue `submit` at chunk `4168134` offsets `605-611`; context: As one of the applicants sought and was granted leave, on consent, to file an IRB document during reply submissions, Counsel were invited to submit further written representations on the content of that document following the hearing as well as to propose serious questions of general importance for certification in accord with IRPA s.
- Evidence: `disposition` cue `granted` at chunk `4168134` offsets `504-511`; context: As one of the applicants sought and was granted leave, on consent, to file an IRB document during reply submissions, Counsel were invited to submit further written representations on the content of that document following the hearing as well as to propose serious questions of general importance for certification in accord with IRPA s.

#### Section text

Restrepo Benitez v. Canada (Minister of Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2006-04-10
Neutral citation
2006 FC 461
File numbers
IMM-1144-05, IMM-1419-05, IMM-1877-05, IMM-2034-05, IMM-2150-05, IMM-2709-05, IMM-3313-05, IMM-353-05, IMM-4044-05, IMM-4064-05, IMM-407-05, IMM-470-05, IMM-712-05, IMM-9220-04, IMM-934-05, IMM-9452-04, IMM-9766-04, IMM-9797-04
Notes
Reported Decision
Decision Content
Date: 20060410
Docket: IMM-9766-04
Citation: 2006 FC 461
Ottawa, Ontario, April 10th, 2006
PRESENT: The Honourable Mr. Justice Mosley
BETWEEN:
JORGE LUIS RESTREPO BENITEZ
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-9220-04
SIRISENA KURUVITA ARACHCHIGE
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-9452-04
AFUA GYANKOMA
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-9797-04
MIKE BILOMBA
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-353-05
GERARDO MARTIN ROSALES RINCON
CATALINA RODRIGUEZ PATINO
ERLIS BEATRIZ DELGADO OCANDO
GERLY JOANNY ROSALES DELGADO
WANDA SOFIA ROSALES DELGADO
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-407-05
EDWIN ERNESTO CARRILLO MEJIA
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-934-05
MAJID REZA YONGE SAVAGOLI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-1144-05
MUHAMMAD SADIK QADRI
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-1419-05
JUVINNY BALMORE FLORES GOMEZ
YANETH BEATRIZ CASTILLO CAMPOS
KONNY BEATRIZ FLORES CASTILLO
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-1877-05
SHURLYN CATHY ANN JONES
SHURNIKYA JONES
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-2034-05
LUIS ALEJANDRO LEMUS ORTIZ
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-2150-05
INTHIKHAB HUSSAIN MATHEEN
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-2709-05
GUILLERMO GUTIERREZ TRUJILLO
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-3313-05
JACQUELINE ROBINSON
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-3994-05
SIRISENA KURUVITA ARACHCHIGE
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-4044-05
RANJIT DEY ROY
RATNA RANI DEY ROY
SWAKSHAR DEY ROY
SWAIKOT DEY ROY
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-712-05
MENA GUIRGUIS
MARIE GOORGY
MONICA GUIRGUIS
MALAK GUIRGUIS
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-470-05
JORGE ISAAC MARTINEZ MARTINEZ
EVA LIBERTAD MORALES (a.k.a. EVA LIBERTAD MORALES DE MARTINEZ)
JORGE ARMANDO MARTINEZ MORALES
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
and
Docket: IMM-4064-05
SUTHARMINI KAMALENDRAN
SINOJAN KAMALENDRAN
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
REASONS FOR ORDER
TABLE OF CONTENTS
Paragraph
1. Procedural History 1
2. Legislative Framework 12
3. Background to the Guideline 7 Controversy 18
4. Issues 33
5. Analysis 43
Standard of Review 43
Application of the Charter of Rights and Freedoms 46
Application of Section 7 47
Application of Section 15 68
Is the procedure mandated by Guideline 7 and adopted by the tribunal 72
contrary to natural justice?
Baker Analysis 85
Nature of the decision being made 93
Legitimate expectation 100
Choice of procedure by the agency itself 108
“Other” factors 113
Conclusion on Baker Analysis 127
Was the discretion of Board Members fettered by the imposition and 129
implementation of Guideline 7 ?
Is Guideline 7 beyond the scope of the Chairperson’s authority? 173
Does questioning by the Board Member result in a reasonable 189
apprehension of bias?
When must an objection to the use of Guideline 7 be raised? 204
6. Conclusions 237
7. Certified questions 238
Procedural History

[1] These reasons concern nineteen applications for judicial review which were consolidated in part for hearing by the Order of Justice Judith A. Snider dated February 20, 2006. Each of the 19 applications raises issues regarding a guideline made by the Chairperson of the Immigration and Refugee Board (“IRB”) under the authority of paragraph 159(1)(h) of the Immigration and Refugee Protection Act S.C. 2001, c. 27 (“IRPA”).

[2] This guideline, entitled “Guideline 7 – Concerning Preparation and Conduct of a Hearing in the Refugee Protection Division”, was the subject of a recent decision of Justice Edmond P. Blanchard in Thamotharem v. The Minister of Citizenship and Immigration, 2006 FC 16, [2006] F.C.J. No. 8 (QL). In reasons dated January 6, 2006, Justice Blanchard found that Guideline 7 unlawfully fettered the discretion of members of the Refugee Protection Division (“RPD”) and held that the decision that was before him would be quashed and the applicant’s claim remitted for redetermination by a differently constituted panel. In an Order dated January 19, 2006, Justice Blanchard allowed the application and certified three questions as being of general importance in accordance paragraph 74(d) of IRPA. An appeal and cross-appeal have been filed from this decision.

[3] Following the release of Justice Blanchard’s decision in Thamotharem, it became apparent that there were a number of applications for judicial review raising similar issues scheduled to be heard by different judges at various sittings of this Court. Following consultations with counsel for the parties, Chief Justice Allan Lutfy ordered that 20 applications be continued as specially managed proceedings and, pursuant to Rule 383, appointed Mr. Justice Gibson and Madam Justice Snider as Case Management Judges for those applications.

[4] Justice Frederick E. Gibson and Justice Snider participated in conference calls with counsel for the parties on several dates in February. Upon being satisfied that it was in the interest of justice that the identified Guideline 7 issues be dealt with as expeditiously as is consistent with fairness and justice, Justice Snider ordered the consolidation of the twenty applications.

[5] Pursuant to Rule 105 (a) of the Federal Court Rules, Justice Snider’s Order provided that the consolidated judicial reviews were, in part, to be heard together, or one immediately after the other, at the discretion of the hearing judge. Further to Rule 107(1), the issues in the consolidated judicial reviews that relate in whole or in part to Guideline 7 were to be determined separately following a single hearing with counsel located in centres outside the Greater Toronto Area participating by video conference if it were impractical to attend in person. The Order also instructed that any remaining issues on each of the consolidated cases were to be determined in separate hearings presided over by one or more different judges, on dates that are as early as practicable following the expedited hearing of the Guideline 7 issues. It also set out deadlines for the filing of further written submissions and affidavits and completion of cross-examinations on the affidavits.

[6] Prior to the hearing on the Guideline 7 issues, one application was resolved on consent leaving 19 which were the subject of these proceedings. The hearing took place at Toronto on March 7 and 8, 2006 with counsel participating by video conference from Montreal and Halifax. Submissions were received from counsel for each of the applicants in sequence, followed by the respondent’s consolidated submissions. Reply submissions were received in the same order. As one of the applicants sought and was granted leave, on consent, to file an IRB document during reply submissions, Counsel were invited to submit further written representations on the content of that document following the hearing as well as to propose serious questions of general importance for certification in accord with IRPA s.74.

## 2044:2 · paragraphs 7-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `96d94176bdf52f0a4fe34153cb0190957656c4558dc6529afe42b8321c36641c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:2:subtheme:1 · paragraphs 7-9

- Raw key terms: `aterman, filed, respondent, addition, affidavit, affidavits, applicant, asad`
- Display key terms: `aterman, filed, addition, affidavit, affidavits, asad`
- Argument roles: `evidence_fact, party_position`
- Explanation: Observed roles: evidence_fact, party_position Display terms: aterman, filed, addition, affidavit, affidavits, asad Position/evidence statements: In addition, the respondent submitted the affidavit of Asad Kiyani sworn February 20, 2006 to which was attached two volumes of RPD decisions and excerpts of transcripts from RPD hearings relating to the implementation o Evidence spans paragraphs 7-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168135` offsets `8-16`; context: [7] The evidence that was before Justice Blanchard in Thamotharem was also filed in these proceedings.
- Evidence: `party_position` cue `submitted` at chunk `4168136` offsets `156-165`; context: In addition, the respondent submitted the affidavit of Asad Kiyani sworn February 20, 2006 to which was attached two volumes of RPD decisions and excerpts of transcripts from RPD hearings relating to the implementation of Guideline 7.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4168136` offsets `13-22`; context: [8] A second affidavit from Mr.

#### 2044:2:subtheme:2 · paragraphs 10-12

- Raw key terms: `applicants, application, counsel, guideline, hearing, order, particular, refugee`
- Display key terms: `guideline, hearing, order, particular, refugee`
- Argument roles: `disposition, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue Display terms: guideline, hearing, order, particular, refugee Rule/authority context: [11] After the hearing, on March 13, 2006, counsel for one of the applicants brought a motion in writing pursuant to Rule 369 for an Order to permit the applicant to amend his application record to include a second affid Operative outcome context: By Order dated April 1, 2006, I dismissed the motion to amend the application record. Evidence spans paragraphs 10-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168138` offsets `306-312`; context: [10] In keeping with the consolidation order, submissions from counsel respecting the facts in relation to each application for judicial review were not received in this hearing except to the extent that counsel deemed it necessary to refer to them in support of their arguments respecting the Guideline 7 issues.
- Evidence: `evidence_fact` cue `record` at chunk `4168139` offsets `188-194`; context: [11] After the hearing, on March 13, 2006, counsel for one of the applicants brought a motion in writing pursuant to Rule 369 for an Order to permit the applicant to amend his application record to include a second affidavit from Mr.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4168139` offsets `105-116`; context: [11] After the hearing, on March 13, 2006, counsel for one of the applicants brought a motion in writing pursuant to Rule 369 for an Order to permit the applicant to amend his application record to include a second affidavit from Mr.
- Evidence: `disposition` cue `dismissed` at chunk `4168139` offsets `476-485`; context: By Order dated April 1, 2006, I dismissed the motion to amend the application record.

#### 2044:2:subtheme:3 · paragraphs 13-14

- Raw key terms: `authority, board, chairperson, division, each, guidelines, guides, irpa`
- Display key terms: `authority, chairperson, division, each, guidelines, guides, irpa`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: authority, chairperson, division, each, guidelines, guides, irpa Rule/authority context: [14] Under IRPA s. Evidence spans paragraphs 13-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168141` offsets `50-55`; context: [13] The Chairperson’s discretionary authority to issue guidelines to Board members is set out in IRPA paragraph 159(1)(h).
- Evidence: `governing_rule` cue `Under` at chunk `4168142` offsets `5-10`; context: [14] Under IRPA s.

#### Section text

[7] The evidence that was before Justice Blanchard in Thamotharem was also filed in these proceedings. That included the affidavits and cross-examinations, of Mr. Raoul Boulakia, President of the Refugee Lawyers Association, Professor James Galloway of the University of Victoria and former IRB Member, Dr. Donald Payne, a psychiatrist, and Mr. Paul Aterman, lawyer and Director General, Operations for the IRB. This evidence is described in detail in Justice Blanchard’s reasons at paragraphs 26 and 27.

[8] A second affidavit from Mr. Aterman, sworn January 6, 2006, and cross-examination dated February 23, 2006, were also filed. In addition, the respondent submitted the affidavit of Asad Kiyani sworn February 20, 2006 to which was attached two volumes of RPD decisions and excerpts of transcripts from RPD hearings relating to the implementation of Guideline 7.

[9] Simultaneous interpretation in English and French was provided on Tuesday, March 7, 2006 at the request of counsel for the respondent. Counsel for one applicant presented her submissions in French. The submissions in both languages were heard and understood by the Court without the assistance of the interpretation, as required by s.16 of the Official Languages Act R.S., 1985, c. 31 (4th Supp.).

[10] In keeping with the consolidation order, submissions from counsel respecting the facts in relation to each application for judicial review were not received in this hearing except to the extent that counsel deemed it necessary to refer to them in support of their arguments respecting the Guideline 7 issues. Counsel did draw the Court’s attention to the particular circumstances of certain applicants for whom an increased susceptibility to stress in a hearing room and to questioning by strangers could be inferred. Counsel also referred to portions of the transcripts of the refugee determination hearings to illustrate certain points in issue.

[11] After the hearing, on March 13, 2006, counsel for one of the applicants brought a motion in writing pursuant to Rule 369 for an Order to permit the applicant to amend his application record to include a second affidavit from Mr. Boulakia, attaching a recent decision by a RPD member opposed to Guideline 7. The respondent opposed that motion on the ground that it was incompatible with the Order of Justice Snider dated February 20, 2006. By Order dated April 1, 2006, I dismissed the motion to amend the application record.
LEGISLATIVE FRAMEWORK

[12] The provisions of the Immigration and Refugee Protection Act that are of particular significance in these proceedings, in my view, are paragraph 159 (1)(h), section 161, subsection 162(2) and section 170.

[13] The Chairperson’s discretionary authority to issue guidelines to Board members is set out in IRPA paragraph 159(1)(h). The enactment states that the purpose of this authority is to assist the members with carrying out their duties:
159. (1) The Chairperson is, by virtue of holding that office, a member of each Division of the Board and is the chief executive officer of the Board. In that capacity, the Chairperson
…
159. (1) Le président est le premier dirigeant de la Commission ainsi que membre d’office des quatre sections; à ce titre :
…
(h) may issue guidelines in writing to members of the Board and identify decisions of the Board as jurisprudential guides, after consulting with the Deputy Chairpersons and the Director General of the Immigration Division, to assist members in carrying out their duties;
h) après consultation des vice-présidents et du directeur général de la Section de l’immigration et en vue d’aider les commissaires dans l’exécution de leurs fonctions, il donne des directives écrites aux commissaires et précise les décisions de la Commission qui serviront de guide jurisprudentiel ;

[14] Under IRPA s. 161, the IRB Chairperson may also make rules respecting, among other things, the “activities, practice and procedure” of each division of the Board. Rules made under this authority require the approval of the Governor-in-Council and must be laid before each House of Parliament within 15 sitting days of such approval. I note that there are no similar requirements for guidelines or jurisprudential guides under paragraph 159 (1) (h). See Refugee Protection Division Rules, SOR/2002-228.

## 2044:3 · paragraphs 15-22

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5a7412267b50420519c4354fda07d1f15cbf10eec330e2d251c12b6e5ae929f2`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:3:subtheme:1 · paragraphs 15-16

- Raw key terms: `avec, dans, division, each, mesure, proceedings, sections, subsection`
- Display key terms: `avec, dans, division, each, mesure, proceedings, sections, subsection`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: avec, dans, division, each, mesure, proceedings, sections, subsection No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.

#### 2044:3:subtheme:2 · paragraphs 17-19

- Raw key terms: `refugee, board, chairperson, decision, guideline, guidelines, information, issued`
- Display key terms: `refugee, chairperson, guideline, guidelines, information, issued`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: refugee, chairperson, guideline, guidelines, information, issued Rule/authority context: [18] Under the authority of a provision in the precedessor statute, subsection 65(3) of the Immigration Act R. Evidence spans paragraphs 17-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168145` offsets `305-312`; context: The Refugee Protection Division, in any proceeding before it,
(a) may inquire into any matter that it considers relevant to establishing whether a claim is well-founded;
(b) must hold a hearing;
(c ) must notify the person who is the subject of the proceeding and the Minister of the hearing;
(d) must provide the Minister, on request, with the documents and information referred to in subsection 100(4);
(e) must give the person and the Minister a reasonable opportunity to present evidence, question witnesses and make representations;
(f) may, despite paragraph (b), allow a claim for refugee protection without a hearing, if the Minister has not notified the Division, within the period set out in the rules of the Board, of the Minister's intention to intervene;
(g) is not bound by any legal or technical rules of evidence;
(h) may receive and base a decision on evidence that is adduced in the proceedings and considered credible or trustworthy in the circumstances; and
(i) may take notice of any facts that may be judicially noticed, any other generally recognized facts and any information or opinion that is within its specialized knowledge
170.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168145` offsets `651-659`; context: The Refugee Protection Division, in any proceeding before it,
(a) may inquire into any matter that it considers relevant to establishing whether a claim is well-founded;
(b) must hold a hearing;
(c ) must notify the person who is the subject of the proceeding and the Minister of the hearing;
(d) must provide the Minister, on request, with the documents and information referred to in subsection 100(4);
(e) must give the person and the Minister a reasonable opportunity to present evidence, question witnesses and make representations;
(f) may, despite paragraph (b), allow a claim for refugee protection without a hearing, if the Minister has not notified the Division, within the period set out in the rules of the Board, of the Minister's intention to intervene;
(g) is not bound by any legal or technical rules of evidence;
(h) may receive and base a decision on evidence that is adduced in the proceedings and considered credible or trustworthy in the circumstances; and
(i) may take notice of any facts that may be judicially noticed, any other generally recognized facts and any information or opinion that is within its specialized knowledge
170.
- Evidence: `governing_rule` cue `Under` at chunk `4168146` offsets `5-10`; context: [18] Under the authority of a provision in the precedessor statute, subsection 65(3) of the Immigration Act R.

#### 2044:3:subtheme:3 · paragraphs 20-22

- Raw key terms: `affidavit, aterman, second, advised, board, claimant, exhibit, guideline`
- Display key terms: `affidavit, aterman, second, advised, exhibit, guideline`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: affidavit, aterman, second, advised, exhibit, guideline Operative outcome context: Aterman states that prior to the issuance of Guideline 7, the order of questioning at RPD hearings varied regionally within the IRB. Evidence spans paragraphs 20-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168148` offsets `157-163`; context: He says that they are issued to address specific legal issues, to provide guidance on questions of mixed law and fact, to codify the exercise of discretion, and to provide guidance on procedural issues.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4168148` offsets `701-710`; context: These views are also set out in a statement entitled “Policy on the use of the Chairperson’s Guidelines” attached as Exhibit “J” to the second Aterman affidavit.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4168149` offsets `35-44`; context: [21] At paragraph 30 of the second affidavit, Mr.
- Evidence: `disposition` cue `varied` at chunk `4168149` offsets `149-155`; context: Aterman states that prior to the issuance of Guideline 7, the order of questioning at RPD hearings varied regionally within the IRB.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4168150` offsets `80-89`; context: [22] In paragraph 19 of Guideline 7, found at Exhibit “I” to the second Aterman affidavit, RPD members and others are advised:
In a claim for refugee protection, the standard practice will be for the [Refugee Protection Officer] RPO to start questioning the claimant.

#### Section text

[15] The text of subsection 161 (1) is reproduced here:
161. (1) Subject to the approval of the Governor in Council, and in consultation with the Deputy Chairpersons and the Director General of the Immigration Division, the Chairperson may make rules respecting
(a) the activities, practice and procedure of each of the Divisions of the Board, including the periods for appeal, the priority to be given to proceedings, the notice that is required and the period in which notice must be given;
(b) the conduct of persons in proceedings before the Board, as well as the consequences of, and sanctions for, the breach of those rules;
(c) the information that may be required and the manner in which, and the time within which, it must be provided with respect to a proceeding before the Board; and
(d) any other matter considered by the Chairperson to require rules.
161. (1) Sous réserve de l’agrément du gouverneur en conseil et en consultation avec les vice-présidents et le directeur général de la Section de l’immigration, le président peut prendre des règles visant :
a) les travaux, la procédure et la pratique des sections, et notamment les délais pour interjeter appel de leurs décisions, l’ordre de priorité pour l’étude des affaires et les préavis à donner, ainsi que les délais afférents;
b) la conduite des personnes dans les affaires devant la Commission, ainsi que les conséquences et sanctions applicables aux manquements aux règles de conduite;
c) la teneur, la forme, le délai de présentation et les modalités d’examen des renseignements à fournir dans le cadre d’une affaire dont la Commission est saisie;
d) toute autre mesure nécessitant, selon lui, la prise de règles.

[16] Subsection 162 (2) indicates Parliament’s intent that proceedings before the IRB are to be conducted with as little formality, and as quickly, as is consistent with natural justice:
(2) Each Division shall deal with all proceedings before it as informally and quickly as the circumstances and the considerations of fairness and natural justice permit.
(2) Chacune des sections fonctionne, dans la mesure où les circonstances et les considérations d’équité et de justice naturelle le permettent, sans formalisme et avec célérité.

[17] Section 170 describes the mandate of the Refugee Protection Division and sets out certain mandatory and permissive considerations respecting its proceedings:
170. The Refugee Protection Division, in any proceeding before it,
(a) may inquire into any matter that it considers relevant to establishing whether a claim is well-founded;
(b) must hold a hearing;
(c ) must notify the person who is the subject of the proceeding and the Minister of the hearing;
(d) must provide the Minister, on request, with the documents and information referred to in subsection 100(4);
(e) must give the person and the Minister a reasonable opportunity to present evidence, question witnesses and make representations;
(f) may, despite paragraph (b), allow a claim for refugee protection without a hearing, if the Minister has not notified the Division, within the period set out in the rules of the Board, of the Minister's intention to intervene;
(g) is not bound by any legal or technical rules of evidence;
(h) may receive and base a decision on evidence that is adduced in the proceedings and considered credible or trustworthy in the circumstances; and
(i) may take notice of any facts that may be judicially noticed, any other generally recognized facts and any information or opinion that is within its specialized knowledge
170. Dans toute affaire dont elle est saisie, la Section de la protection des réfugiés :
a) procède à tous les actes qu'elle juge utiles à la manifestation du bien-fondé de la demande;
b) dispose de celle-ci par la tenue d'une audience;
c) convoque la personne en cause et le ministre;
d) transmet au ministre, sur demande, les renseignements et documents fournis au titre du paragraphe 100(4);
e) donne à la personne en cause et au ministre la possibilité de produire des éléments de preuve, d'interroger des témoins et de présenter des observations;
f) peut accueillir la demande d'asile sans qu'une audience soit tenue si le ministre ne lui a pas, dans le délai prévu par les règles, donné avis de son intention d'intervenir;
g) n'est pas liée par les règles légales ou techniques de présentation de la preuve;
h) peut recevoir les éléments qu'elle juge crédibles ou dignes de foi en l'occurrence et fonder sur eux sa décision;
i) peut admettre d'office les faits admissibles en justice et les faits généralement reconnus et les renseignements ou opinions qui sont du ressort de sa spécialisation.
BACKGROUND TO THE GUIDELINE 7 CONTROVERSY

[18] Under the authority of a provision in the precedessor statute, subsection 65(3) of the Immigration Act R.S.C. 1985, c.I-2, guidelines were issued by the Chairperson of the Immigration and Refugee Board to encourage consistent and transparent decision making with respect to a number of subject areas. The Guidelines on Women Refugee Claimants Fearing Gender-Related Persecution were issued in 1993 and updated in November 1996. The Guidelines on Civilian Non-Combatants Fearing Persecution in Civil War Situations were issued in March 1996, Guidelines on Child Refugee Claimants in August 1996, Guidelines on Detention on March 12, 1998. Upon the coming into force of IRPA on June 28, 2002, the gender, civilian non-combatants and child refugee claimant guidelines were reissued by the Chairperson under paragraph 159 (1) (h).

[19] In October, 2003 the Chairperson issued three further guidelines as part of an action plan to address the backlog of refugee claims which had accumulated by that time. Guideline 5 dealing with the submission of personal information forms and abandonment proceedings came into effect on October 30, 2003 and Guideline 6, relating to scheduling and date changes, became effective on December 1, 2003. Guideline 7 was also made effective December 1, 2003 but was not brought fully into effect until June 2004.

[20] Paul Aterman’s affidavits describe the purpose of these guidelines from the Board’s perspective. He says that they are issued to address specific legal issues, to provide guidance on questions of mixed law and fact, to codify the exercise of discretion, and to provide guidance on procedural issues. The intent is to promote consistency, coherence and fairness in the treatment of cases at the Board. They are not viewed as binding. Members are advised to use their discretion to follow a different approach where warranted in individual cases. These views are also set out in a statement entitled “Policy on the use of the Chairperson’s Guidelines” attached as Exhibit “J” to the second Aterman affidavit.

[21] At paragraph 30 of the second affidavit, Mr. Aterman states that prior to the issuance of Guideline 7, the order of questioning at RPD hearings varied regionally within the IRB. Guideline 7 introduced a national standard order of questioning. His affidavit further describes the consultations that were undertaken with interested non-governmental organizations prior to the implementation of the guideline which resulted in steps being taken by the Board to respond to concerns raised. These included internal training sessions on questioning and a six month phase-in period from December 1, 2003 to May 31, 2004 during which the standard order was implemented only with the claimant’s consent.

[22] In paragraph 19 of Guideline 7, found at Exhibit “I” to the second Aterman affidavit, RPD members and others are advised:
In a claim for refugee protection, the standard practice will be for the [Refugee Protection Officer] RPO to start questioning the claimant. If there is no RPO participating in the hearing, the member will begin, followed by counsel for the claimant [emphasis added].

## 2044:4 · paragraphs 23-30

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `825827120f2a1d087138ec03d021e1e8873a9a84d2edbe78483e25dcce061cb5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:4:subtheme:1 · paragraphs 23-26

- Raw key terms: `hearing, claimant, guideline, order, application, case, circumstances, evidence`
- Display key terms: `hearing, guideline, order, case, circumstances`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: hearing, guideline, order, case, circumstances Position/evidence statements: [24] The Guideline contemplates that the RPD will define the issues which are to be addressed at the hearing through disclosure of the RPD File Screening Form with the Notice to Appear for the hearing and that questionin Application context: [23] The paragraph concludes with the statement: Beginning the hearing in this way allows the claimant to quickly understand what evidence the member needs from the claimant in order for the claimant to prove his or her  | Accordingly, the Immigration and Refugee Protection Act (IRPA) requires the IRB to deal with proceedings before it informally, quickly and fairly. Evidence spans paragraphs 23-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168151` offsets `130-138`; context: [23] The paragraph concludes with the statement:
Beginning the hearing in this way allows the claimant to quickly understand what evidence the member needs from the claimant in order for the claimant to prove his or her case.
- Evidence: `reasoning_application` cue `concludes` at chunk `4168151` offsets `19-28`; context: [23] The paragraph concludes with the statement:
Beginning the hearing in this way allows the claimant to quickly understand what evidence the member needs from the claimant in order for the claimant to prove his or her case.
- Evidence: `issue` cue `issues` at chunk `4168152` offsets `61-67`; context: [24] The Guideline contemplates that the RPD will define the issues which are to be addressed at the hearing through disclosure of the RPD File Screening Form with the Notice to Appear for the hearing and that questioning would be limited to those issues and any others that the claimant may wish to submit.
- Evidence: `party_position` cue `submit` at chunk `4168152` offsets `300-306`; context: [24] The Guideline contemplates that the RPD will define the issues which are to be addressed at the hearing through disclosure of the RPD File Screening Form with the Notice to Appear for the hearing and that questioning would be limited to those issues and any others that the claimant may wish to submit.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168153` offsets `778-786`; context: 44, that is, in writing before the hearing supported by evidence in affidavit or statutory declaration form.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168153` offsets `501-508`; context: However, the party who believes that exceptional circumstances exist is expected to make an application to change the order of questioning before the hearing and the application is to be made according to the RPD Rules s.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4168154` offsets `146-157`; context: Accordingly, the Immigration and Refugee Protection Act (IRPA) requires the IRB to deal with proceedings before it informally, quickly and fairly.

#### 2044:4:subtheme:2 · paragraphs 27-29

- Raw key terms: `evidence, members, questioning, described, guideline, rpos, training, actively`
- Display key terms: `members, questioning, described, guideline, rpos, training, actively`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: members, questioning, described, guideline, rpos, training, actively Rule/authority context: [27] The role of RPD members under IRPA is described in the Guideline as comparable to that of Commissioners under the Inquiries Act R. Evidence spans paragraphs 27-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168155` offsets `245-252`; context: The text states that members may inquire into anything they consider relevant to establishing whether a claim is well-founded and define the issues that must be resolved in order to render a decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168155` offsets `475-483`; context: A judge’s role, the Guideline states, is to consider the evidence and argument which the parties chose to present.
- Evidence: `governing_rule` cue `under` at chunk `4168155` offsets `29-34`; context: [27] The role of RPD members under IRPA is described in the Guideline as comparable to that of Commissioners under the Inquiries Act R.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168156` offsets `19-27`; context: Aterman’s evidence is that in drafting the guideline, a deliberate choice was made to avoid the use of terminology such as “examination-in-chief” and “cross-examination” as inappropriate concepts better suited to an adversarial model requiring judicial formality.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168157` offsets `230-238`; context: [29] Notwithstanding these instructions, the Court is familiar with instances in which RPD members have failed to live up to these expectations, some of which are described in the cases discussed below in these reasons and in the evidence of Mr.

#### 2044:4:subtheme:3 · paragraphs 30-30

- Raw key terms: `allowed, although, appears, applicants, assistance, begin, board, calgary`
- Display key terms: `allowed, although, appears, assistance, begin, calgary`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: allowed, although, appears, assistance, begin, calgary Position/evidence statements: This practice, the applicants submit, was more in keeping with the nature of a quasi-judicial hearing and allowed for an “examination-in-chief” in which claimants were encouraged to fully recount their histories with the Operative outcome context: This practice, the applicants submit, was more in keeping with the nature of a quasi-judicial hearing and allowed for an “examination-in-chief” in which claimants were encouraged to fully recount their histories with the Evidence spans paragraphs 30-30. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168158` offsets `342-350`; context: The RPO (if present) would then question the claimant, followed by the Board member if he or she had any remaining matters to raise.
- Evidence: `party_position` cue `submit` at chunk `4168158` offsets `473-479`; context: This practice, the applicants submit, was more in keeping with the nature of a quasi-judicial hearing and allowed for an “examination-in-chief” in which claimants were encouraged to fully recount their histories with the assistance of counsel whom they had come to know and trust.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168158` offsets `25-33`; context: [30] It appears from the evidence, and submissions of counsel, that prior to the implementation of Guideline 7, it was common in Toronto, and possibly Calgary and Vancouver, although the evidence with respect to those cities is not clear, for counsel for the claimant to begin the questioning at the hearings.
- Evidence: `disposition` cue `allowed` at chunk `4168158` offsets `549-556`; context: This practice, the applicants submit, was more in keeping with the nature of a quasi-judicial hearing and allowed for an “examination-in-chief” in which claimants were encouraged to fully recount their histories with the assistance of counsel whom they had come to know and trust.

#### Section text

[23] The paragraph concludes with the statement:
Beginning the hearing in this way allows the claimant to quickly understand what evidence the member needs from the claimant in order for the claimant to prove his or her case.

[24] The Guideline contemplates that the RPD will define the issues which are to be addressed at the hearing through disclosure of the RPD File Screening Form with the Notice to Appear for the hearing and that questioning would be limited to those issues and any others that the claimant may wish to submit. Guideline 7 covers matters such as case preparation, disclosure of documents, research requests, pre-hearing conferences, interpretation and the making of representations. The Guideline also stipulates the order of questioning where the Minister intervenes on the issue of exclusion, on other issues, or in an application to vacate or cease refugee protection.

[25] Paragraph 23 of the Guideline provides that the RPD member may change the order of questioning in exceptional circumstances. The examples provided of exceptional circumstances are a severely disturbed claimant or a very young child who might feel intimidated by an unfamiliar examiner and thereby finds it difficult to understand and answer questions. In such circumstances, the paragraph says, the member could decide that it would be better for the claimant’s counsel to begin the questioning. However, the party who believes that exceptional circumstances exist is expected to make an application to change the order of questioning before the hearing and the application is to be made according to the RPD Rules s.44, that is, in writing before the hearing supported by evidence in affidavit or statutory declaration form.

[26] The introduction to the Guideline states, in part:
Administrative tribunals operate less formally and more expeditiously than courts of law. Accordingly, the Immigration and Refugee Protection Act (IRPA) requires the IRB to deal with proceedings before it informally, quickly and fairly. The Chairperson has issued these guidelines to explain what the RPD does before and during the hearing to make its proceedings more efficient but still fair. The guidelines also set out what the RPD expects participants to do.
The guidelines apply to most cases heard by the RPD. However, in compelling or exceptional circumstances, the members will use their discretion not to apply some guidelines or to apply them less strictly.
Generally speaking, the RPD will make allowances for unrepresented claimants who are unfamiliar with the Division's processes and rules. Claimants identified as particularly vulnerable will be treated with special sensitivity.

[27] The role of RPD members under IRPA is described in the Guideline as comparable to that of Commissioners under the Inquiries Act R.S.1985, c.I-11. The text states that members may inquire into anything they consider relevant to establishing whether a claim is well-founded and define the issues that must be resolved in order to render a decision. This role is distinguished in the Guideline from that of a judge. A judge’s role, the Guideline states, is to consider the evidence and argument which the parties chose to present. Moreover, it provides, the RPD has control of its own procedure, including who is to start the questioning. RPD members, the text states, have to be actively involved to make the RPD’s inquiry process work properly.

[28] Mr. Aterman’s evidence is that in drafting the guideline, a deliberate choice was made to avoid the use of terminology such as “examination-in-chief” and “cross-examination” as inappropriate concepts better suited to an adversarial model requiring judicial formality. Attached to his affidavit as Exhibit “N” is a copy of the Board’s training handout entitled “Questioning 101” which instructs new members and RPOs that they are not to “cross-examine” claimants, or employ aggressive techniques such as attempting to trap the claimant, to badger or harass by repetitious or misleading questions or to adopt a hostile or sarcastic tone. The object is not to try to “win” a case.

[29] Notwithstanding these instructions, the Court is familiar with instances in which RPD members have failed to live up to these expectations, some of which are described in the cases discussed below in these reasons and in the evidence of Mr. Boulakia and Professor Galloway. It is clear from that evidence that RPOs and members do not always maintain neutrality and a non-adversarial stance in their questioning as they are instructed to do in their training.

[30] It appears from the evidence, and submissions of counsel, that prior to the implementation of Guideline 7, it was common in Toronto, and possibly Calgary and Vancouver, although the evidence with respect to those cities is not clear, for counsel for the claimant to begin the questioning at the hearings. The RPO (if present) would then question the claimant, followed by the Board member if he or she had any remaining matters to raise. This practice, the applicants submit, was more in keeping with the nature of a quasi-judicial hearing and allowed for an “examination-in-chief” in which claimants were encouraged to fully recount their histories with the assistance of counsel whom they had come to know and trust.

## 2044:5 · paragraphs 31-35

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e9b39931f8042c91d32304c14ae243424685854915eeaaf0ed745c8f75ebf48c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:5:subtheme:1 · paragraphs 31-32

- Raw key terms: `board, counsel, accommodated, according, action, affidavit, appears, applicants`
- Display key terms: `accommodated, according, action, affidavit, appears`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: accommodated, according, action, affidavit, appears Operative outcome context: The change, they say, has had little effect on hearing times or the overall disposition rate for refugee determinations but has denied claimants their rights to the effective assistance of counsel and to be heard, both o Evidence spans paragraphs 31-32. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168159` offsets `173-181`; context: In those cities, counsel could ask to question their clients first and were frequently accommodated by the Board members.
- Evidence: `issue` cue `ISSUES` at chunk `4168160` offsets `634-640`; context: ISSUES
- Evidence: `evidence_fact` cue `affidavit` at chunk `4168160` offsets `32-41`; context: Aterman’s affidavit evidence, the standard order of questioning was introduced as part of an Action Plan to increase the Board’s efficiency, decrease the average time of a hearing and reduce burdens on the Board’s resources while maintaining fairness.
- Evidence: `disposition` cue `denied` at chunk `4168160` offsets `474-480`; context: The change, they say, has had little effect on hearing times or the overall disposition rate for refugee determinations but has denied claimants their rights to the effective assistance of counsel and to be heard, both of which are aspects of fundamental justice and procedural fairness.

#### 2044:5:subtheme:2 · paragraphs 33-35

- Raw key terms: `comity, court, decisions, judicial, colleagues, decided, differ, legal`
- Display key terms: `comity, decisions, judicial, colleagues, decided, differ, legal`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: comity, decisions, judicial, colleagues, decided, differ, legal Application context: I have no power to overrule a brother Judge, I can only differ from him, and the effect of my doing so is not to settle but rather to unsettle the law, because, following such a difference of opinion, the unhappy litigan Evidence spans paragraphs 33-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168161` offsets `24-30`; context: [33] In considering the issues raised by the parties in these proceedings I have been conscious of the fact that much of the ground that I am covering has been travelled previously by other judges of this Court, notably Justice Blanchard in Thamotharem.
- Evidence: `reasoning_application` cue `because` at chunk `4168162` offsets `461-468`; context: I have no power to overrule a brother Judge, I can only differ from him, and the effect of my doing so is not to settle but rather to unsettle the law, because, following such a difference of opinion, the unhappy litigant is confronted with conflicting opinions emanating from the same Court and therefore of the same legal weight.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168163` offsets `147-155`; context: [35] With judicial comity in mind, I have concluded that I should differ from the prior decisions of my colleagues only if I am satisfied that the evidence before me requires it or that I am convinced that the decisions were wrongly decided in that they did not consider some binding authority or relevant statute.

#### Section text

[31] In Montreal and Ottawa, it appears the practice described in Guideline 7 was more common but was not mandatory before June, 2004. In those cities, counsel could ask to question their clients first and were frequently accommodated by the Board members.

[32] According to Mr. Aterman’s affidavit evidence, the standard order of questioning was introduced as part of an Action Plan to increase the Board’s efficiency, decrease the average time of a hearing and reduce burdens on the Board’s resources while maintaining fairness. The applicants challenge these assertions as unfounded and unwarranted. The change, they say, has had little effect on hearing times or the overall disposition rate for refugee determinations but has denied claimants their rights to the effective assistance of counsel and to be heard, both of which are aspects of fundamental justice and procedural fairness.
ISSUES

[33] In considering the issues raised by the parties in these proceedings I have been conscious of the fact that much of the ground that I am covering has been travelled previously by other judges of this Court, notably Justice Blanchard in Thamotharem. I am not bound by those decisions but the notion of judicial comity suggests that I should exercise restraint when dealing with legal issues which my colleagues have previously decided.

[34] Judicial comity is not the application of the rule of stare decisis, but recognition that decisions of the Court should be consistent to the extent possible so as to provide litigants with some predictability. I am aware, as was stated in Re Hansard Spruce Mills Ltd., [1954] 4 D.L.R. 590 (B.C.S.C.):
...I have no power to overrule a brother Judge, I can only differ from him, and the effect of my doing so is not to settle but rather to unsettle the law, because, following such a difference of opinion, the unhappy litigant is confronted with conflicting opinions emanating from the same Court and therefore of the same legal weight.

[35] With judicial comity in mind, I have concluded that I should differ from the prior decisions of my colleagues only if I am satisfied that the evidence before me requires it or that I am convinced that the decisions were wrongly decided in that they did not consider some binding authority or relevant statute. In that regard, I would note that while the record before me includes the evidence that was before the Court in Thamotharem, it also includes new evidence that was not part of the record in that case.

## 2044:6 · paragraphs 36-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d44789079b17ad308c06e7a82c0623839d9b2f0d85d1336b29b074a723373ec9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:6:subtheme:1 · paragraphs 36-41

- Raw key terms: `court, procedural, applicants, charter, denied, fairness, guideline, refugee`
- Display key terms: `procedural, charter, denied, fairness, guideline, refugee`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: procedural, charter, denied, fairness, guideline, refugee Position/evidence statements: However, as he did not hold that the Guideline order of questioning, in itself, denied procedural fairness, the applicants collectively submit that the Court should recognize that a higher standard of procedural fairness | [37] One applicant, Shurlyn Jones (IMM-1877-05), submits that it is never permissible for a RPD member, in the absence of an RPO, to engage in questioning the claimant prior to claimant’s counsel and that this practice r Rule/authority context: [40] The respondent urges the Court to resolve the controversy between the parties on administrative law principles rather than upon a Charter analysis. Application context: ” The respondent asks the Court to conclude, on the basis of the fresh evidence before me, that the discretion of RPD members has not in fact been fettered by implementation of the Guideline. Operative outcome context: However, as he did not hold that the Guideline order of questioning, in itself, denied procedural fairness, the applicants collectively submit that the Court should recognize that a higher standard of procedural fairness | [38] Another applicant, Mike Balomba (IMM-9797-04), contends that the equality rights guaranteed by section 15 of the Charter have been infringed in that refugee claimants are discriminated against by being denied the sa Evidence spans paragraphs 36-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submit` at chunk `4168164` offsets `352-358`; context: However, as he did not hold that the Guideline order of questioning, in itself, denied procedural fairness, the applicants collectively submit that the Court should recognize that a higher standard of procedural fairness is called for in refugee determination hearings.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168164` offsets `216-223`; context: However, as he did not hold that the Guideline order of questioning, in itself, denied procedural fairness, the applicants collectively submit that the Court should recognize that a higher standard of procedural fairness is called for in refugee determination hearings.
- Evidence: `disposition` cue `denied` at chunk `4168164` offsets `296-302`; context: However, as he did not hold that the Guideline order of questioning, in itself, denied procedural fairness, the applicants collectively submit that the Court should recognize that a higher standard of procedural fairness is called for in refugee determination hearings.
- Evidence: `party_position` cue `submits` at chunk `4168165` offsets `49-56`; context: [37] One applicant, Shurlyn Jones (IMM-1877-05), submits that it is never permissible for a RPD member, in the absence of an RPO, to engage in questioning the claimant prior to claimant’s counsel and that this practice results in an apprehension of institutional bias and undermines claimants’ right to an impartial and independent tribunal.
- Evidence: `party_position` cue `contends` at chunk `4168166` offsets `52-60`; context: [38] Another applicant, Mike Balomba (IMM-9797-04), contends that the equality rights guaranteed by section 15 of the Charter have been infringed in that refugee claimants are discriminated against by being denied the same procedural protections as other litigants before judicial and quasi-judicial bodies, notably those who appear before the other Divisions of the IRB.
- Evidence: `disposition` cue `denied` at chunk `4168166` offsets `207-213`; context: [38] Another applicant, Mike Balomba (IMM-9797-04), contends that the equality rights guaranteed by section 15 of the Charter have been infringed in that refugee claimants are discriminated against by being denied the same procedural protections as other litigants before judicial and quasi-judicial bodies, notably those who appear before the other Divisions of the IRB.
- Evidence: `party_position` cue `submits` at chunk `4168167` offsets `496-503`; context: To the extent that any of the applicants perceive that the application of the Guideline has denied them a fair hearing, the respondent submits that they may seek a remedy in this Court, as they have, and that each case of alleged procedural unfairness should be reviewed on an individual basis.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168167` offsets `240-248`; context: ” The respondent asks the Court to conclude, on the basis of the fresh evidence before me, that the discretion of RPD members has not in fact been fettered by implementation of the Guideline.
- Evidence: `reasoning_application` cue `conclude` at chunk `4168167` offsets `204-212`; context: ” The respondent asks the Court to conclude, on the basis of the fresh evidence before me, that the discretion of RPD members has not in fact been fettered by implementation of the Guideline.
- Evidence: `disposition` cue `denied` at chunk `4168167` offsets `453-459`; context: To the extent that any of the applicants perceive that the application of the Guideline has denied them a fair hearing, the respondent submits that they may seek a remedy in this Court, as they have, and that each case of alleged procedural unfairness should be reviewed on an individual basis.
- Evidence: `governing_rule` cue `principles` at chunk `4168168` offsets `105-115`; context: [40] The respondent urges the Court to resolve the controversy between the parties on administrative law principles rather than upon a Charter analysis.
- Evidence: `party_position` cue `submits` at chunk `4168169` offsets `29-36`; context: [41] Further, the respondent submits that any applicants who did not object to the Guideline 7 procedure in a timely manner before the refugee hearing or in their applications for leave to this Court, should not now be permitted to claim a denial of procedural fairness.

#### 2044:6:subtheme:2 · paragraphs 42-43

- Raw key terms: `analysis, applications, review, standard, actions, address, administrative, agreement`
- Display key terms: `analysis, applications, review, standard, actions, address, administrative, agreement`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: analysis, applications, review, standard, actions, address, administrative, agreement Rule/authority context: What is the standard of review to be applied to the applications under review? | [43] In applications for judicial review of the actions of administrative tribunals, the starting point is usually to determine the standard of review on a pragmatic and functional analysis. Application context: What is the standard of review to be applied to the applications under review? Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168170` offsets `31-37`; context: [42] I have concluded that the issues related to Guideline 7 in the 19 applications before me that I must address in these reasons are as follows:
1.
- Evidence: `governing_rule` cue `standard of review` at chunk `4168170` offsets `162-180`; context: What is the standard of review to be applied to the applications under review?
- Evidence: `reasoning_application` cue `applied` at chunk `4168170` offsets `187-194`; context: What is the standard of review to be applied to the applications under review?
- Evidence: `issue` cue `question` at chunk `4168171` offsets `201-209`; context: This is a question of law which must be decided by the Court even in cases where the parties are in agreement as to what that standard should be: Monsanto Canada Inc.
- Evidence: `governing_rule` cue `standard of review` at chunk `4168171` offsets `132-150`; context: [43] In applications for judicial review of the actions of administrative tribunals, the starting point is usually to determine the standard of review on a pragmatic and functional analysis.

#### Section text

[36] In these proceedings, the applicants’ submissions start from Justice Blanchard’s finding in Thamotharem that RPD members’ discretion has been fettered by the manner in which Guideline 7 was defined and imposed. However, as he did not hold that the Guideline order of questioning, in itself, denied procedural fairness, the applicants collectively submit that the Court should recognize that a higher standard of procedural fairness is called for in refugee determination hearings. This, they contend, would include a right to an “examination-in-chief” by their counsel in advance of any questioning by the RPO or Board member. The applicants submit that this should be acknowledged by the Court to be an aspect of fundamental justice in the context of refugee hearings, as contemplated by section 7 of the Charter, or, at the very least, as a principle of natural justice in the common law sense.

[37] One applicant, Shurlyn Jones (IMM-1877-05), submits that it is never permissible for a RPD member, in the absence of an RPO, to engage in questioning the claimant prior to claimant’s counsel and that this practice results in an apprehension of institutional bias and undermines claimants’ right to an impartial and independent tribunal.

[38] Another applicant, Mike Balomba (IMM-9797-04), contends that the equality rights guaranteed by section 15 of the Charter have been infringed in that refugee claimants are discriminated against by being denied the same procedural protections as other litigants before judicial and quasi-judicial bodies, notably those who appear before the other Divisions of the IRB.

[39] The respondent also starts from Justice Blanchard’s decision and urges that I follow his finding that fairness does not dictate a right to an “examination-in-chief.” The respondent asks the Court to conclude, on the basis of the fresh evidence before me, that the discretion of RPD members has not in fact been fettered by implementation of the Guideline. To the extent that any of the applicants perceive that the application of the Guideline has denied them a fair hearing, the respondent submits that they may seek a remedy in this Court, as they have, and that each case of alleged procedural unfairness should be reviewed on an individual basis.

[40] The respondent urges the Court to resolve the controversy between the parties on administrative law principles rather than upon a Charter analysis.

[41] Further, the respondent submits that any applicants who did not object to the Guideline 7 procedure in a timely manner before the refugee hearing or in their applications for leave to this Court, should not now be permitted to claim a denial of procedural fairness.

[42] I have concluded that the issues related to Guideline 7 in the 19 applications before me that I must address in these reasons are as follows:
1. What is the standard of review to be applied to the applications under review?
2. Whether an analysis of the Guideline 7 procedure pursuant to the Canadian Charter of Rights and Freedoms analysis is required and, if so, does it infringe fundamental justice under s.7 or violate s.15?
3. Was the procedure mandated by Guideline 7, in itself, contrary to common law principles of natural justice?
4. Did the implementation of Guideline 7 fetter the discretion of Board members?
5. Is Guideline 7 beyond the scope of the Chairperson’s authority to issue guidelines?
6. Does questioning by the Board member demonstrate a reasonable apprehension of institutional bias?
7. If natural justice is implicated, when must the applicant raise an objection to the use of Guideline 7?
ANALYSIS
Standard of Review

[43] In applications for judicial review of the actions of administrative tribunals, the starting point is usually to determine the standard of review on a pragmatic and functional analysis. This is a question of law which must be decided by the Court even in cases where the parties are in agreement as to what that standard should be: Monsanto Canada Inc. v. Ontario (Superintendent of Financial Services), [2004] 3 S.C.R. 152, 2004 SCC 54 at para. 6.

## 2044:7 · paragraphs 44-50

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a2cb7f5f50dc01890966054dc7a84656edc24189fdeb6df699ce19d3e764b49e`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:7:subtheme:1 · paragraphs 44-45

- Raw key terms: `board, breach, canadian, fairness, minister, allegations, analysis, application`
- Display key terms: `breach, canadian, fairness, allegations, analysis`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: breach, canadian, fairness, allegations, analysis Application context: If the Court concludes that there has been a breach of natural justice or procedural fairness, no deference is due and the Court will set aside the decision of the Board. Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168172` offsets `423-430`; context: Instead, the Court must examine the specific circumstances of the case and determine whether the tribunal in question observed the duty of fairness.
- Evidence: `reasoning_application` cue `concludes` at chunk `4168172` offsets `500-509`; context: If the Court concludes that there has been a breach of natural justice or procedural fairness, no deference is due and the Court will set aside the decision of the Board.

#### 2044:7:subtheme:2 · paragraphs 46-48

- Raw key terms: `charter, section, argued, canada, case, determined, fundamental, immigration`
- Display key terms: `charter, section, case, determined, fundamental`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: charter, section, case, determined, fundamental Position/evidence statements: [48] I note that in Thamotharem, neither the applicant nor the intervener argued that the Chairperson’s standard order of questioning procedure violates the principles of fundamental justice guaranteed under section 7 of Rule/authority context: The respondent takes the position, however, that there is no need for the Court to determine this matter on fundamental justice considerations as this case may be resolved through the application of administrative law pr | [48] I note that in Thamotharem, neither the applicant nor the intervener argued that the Chairperson’s standard order of questioning procedure violates the principles of fundamental justice guaranteed under section 7 of Application context: They are: (1) that the order of questioning mandated by paragraph 19 of Guideline 7 is contrary to section 7 of the Charter; (2) that Guideline 7 is also contrary to section 15 of the Charter because persons appearing be | Accordingly, Justice Blanchard determined the content of the procedural protections to be afforded the applicant in that case by an analysis of the factors described by Justice L’Heureux-Dubé in Baker v. Evidence spans paragraphs 46-48. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168174` offsets `35-43`; context: [46] Two notices of constitutional question were served on the federal and provincial Attorneys General in these proceedings as required by section 57 of the Federal Courts Act R.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168174` offsets `551-559`; context: They are: (1) that the order of questioning mandated by paragraph 19 of Guideline 7 is contrary to section 7 of the Charter; (2) that Guideline 7 is also contrary to section 15 of the Charter because persons appearing before other tribunals have a right to present their evidence first, have their counsel present their evidence first, and have their counsel question first; and (3) that the failure to implement the Refugee Appeal Division is contrary to section 7.
- Evidence: `reasoning_application` cue `because` at chunk `4168174` offsets `472-479`; context: They are: (1) that the order of questioning mandated by paragraph 19 of Guideline 7 is contrary to section 7 of the Charter; (2) that Guideline 7 is also contrary to section 15 of the Charter because persons appearing before other tribunals have a right to present their evidence first, have their counsel present their evidence first, and have their counsel question first; and (3) that the failure to implement the Refugee Appeal Division is contrary to section 7.
- Evidence: `issue` cue `question` at chunk `4168175` offsets `131-139`; context: [47] There is no dispute between the parties that section 7 of the Charter is engaged in the refugee determination process as that question was determined by the Supreme Court in Singh v.
- Evidence: `governing_rule` cue `principles` at chunk `4168175` offsets `505-515`; context: The respondent takes the position, however, that there is no need for the Court to determine this matter on fundamental justice considerations as this case may be resolved through the application of administrative law principles respecting natural justice.
- Evidence: `counterargument_limitation` cue `however` at chunk `4168175` offsets `322-329`; context: The respondent takes the position, however, that there is no need for the Court to determine this matter on fundamental justice considerations as this case may be resolved through the application of administrative law principles respecting natural justice.
- Evidence: `party_position` cue `argued` at chunk `4168176` offsets `74-80`; context: [48] I note that in Thamotharem, neither the applicant nor the intervener argued that the Chairperson’s standard order of questioning procedure violates the principles of fundamental justice guaranteed under section 7 of the Charter.
- Evidence: `governing_rule` cue `principles` at chunk `4168176` offsets `157-167`; context: [48] I note that in Thamotharem, neither the applicant nor the intervener argued that the Chairperson’s standard order of questioning procedure violates the principles of fundamental justice guaranteed under section 7 of the Charter.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4168176` offsets `344-355`; context: Accordingly, Justice Blanchard determined the content of the procedural protections to be afforded the applicant in that case by an analysis of the factors described by Justice L’Heureux-Dubé in Baker v.

#### 2044:7:subtheme:3 · paragraphs 49-50

- Raw key terms: `administrative, charter, determination, found, fundamental, held, justice, meet`
- Display key terms: `administrative, charter, determination, fundamental, justice, meet`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, party_position, reasoning_application Display terms: administrative, charter, determination, fundamental, justice, meet Position/evidence statements: [50] The applicants submit that refugee determination proceedings are quasi-judicial in nature because the Board has some of the trappings of a judicial body, adjudicates on individual rights, is statutorily mandated to  Rule/authority context: Moreover, as held in Singh, administrative convenience and considerations such as the interest of the tribunal in quicker resolution of cases cannot be determinative of fundamental justice principles. Application context: [50] The applicants submit that refugee determination proceedings are quasi-judicial in nature because the Board has some of the trappings of a judicial body, adjudicates on individual rights, is statutorily mandated to  Evidence spans paragraphs 49-50. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `4168177` offsets `681-691`; context: In Singh, the Supreme Court found that this requires notice and an oral hearing, although how that hearing was to be conducted was not specified.
- Evidence: `counterargument_limitation` cue `although` at chunk `4168177` offsets `734-742`; context: In Singh, the Supreme Court found that this requires notice and an oral hearing, although how that hearing was to be conducted was not specified.
- Evidence: `party_position` cue `submit` at chunk `4168178` offsets `20-26`; context: [50] The applicants submit that refugee determination proceedings are quasi-judicial in nature because the Board has some of the trappings of a judicial body, adjudicates on individual rights, is statutorily mandated to hold hearings to make findings of fact, and must identify the relevant laws and apply them to the facts as found.
- Evidence: `governing_rule` cue `principles` at chunk `4168178` offsets `692-702`; context: Moreover, as held in Singh, administrative convenience and considerations such as the interest of the tribunal in quicker resolution of cases cannot be determinative of fundamental justice principles.
- Evidence: `reasoning_application` cue `because` at chunk `4168178` offsets `95-102`; context: [50] The applicants submit that refugee determination proceedings are quasi-judicial in nature because the Board has some of the trappings of a judicial body, adjudicates on individual rights, is statutorily mandated to hold hearings to make findings of fact, and must identify the relevant laws and apply them to the facts as found.

#### Section text

[44] However, as noted by Justice Blanchard in Thamotharem at paragraph 15, a pragmatic and functional analysis is not required when the Court is assessing allegations of the denial of natural justice or procedural fairness: Canadian Union of Public Employees (C.U.P.E.) v. Ontario (Minister of Labour), [2003] 1 S.C.R. 539, 2003 SCC 29. Instead, the Court must examine the specific circumstances of the case and determine whether the tribunal in question observed the duty of fairness. If the Court concludes that there has been a breach of natural justice or procedural fairness, no deference is due and the Court will set aside the decision of the Board.

[45] Where a breach of fairness is found to result from a reasonable apprehension of bias, the standard is particularly demanding, particularly where, as here, the rights of claimants in proceedings before the Board are at stake: Kozak v. Canada (Minister of Citizenship and Immigration; Smajda v. Canada (Minister of Citizenship and Immigration), 2006 FCA 124 [Kozak].
Application of the Canadian Charter of Rights and Freedoms

[46] Two notices of constitutional question were served on the federal and provincial Attorneys General in these proceedings as required by section 57 of the Federal Courts Act R.S.C. 1985, c. F-7. The Notice filed in Benitez (IMM-9766-04) identifies three constitutional issues. They are: (1) that the order of questioning mandated by paragraph 19 of Guideline 7 is contrary to section 7 of the Charter; (2) that Guideline 7 is also contrary to section 15 of the Charter because persons appearing before other tribunals have a right to present their evidence first, have their counsel present their evidence first, and have their counsel question first; and (3) that the failure to implement the Refugee Appeal Division is contrary to section 7. This third issue was not argued at the hearing. The Notice filed in Jones (IMM-1877-05) states that by permitting the Board member to conduct an examination-in-chief of the claimant, paragraph 19 breaches the right to a fair and independent judiciary resulting in a reasonable apprehension of bias which is contrary to section 7 of the Charter.
Section 7

[47] There is no dispute between the parties that section 7 of the Charter is engaged in the refugee determination process as that question was determined by the Supreme Court in Singh v. Canada (Minister of Employment and Immigration), [1985] 1 S.C.R. 177, 17 D.L.R. (4th) 422 [Singh]. The respondent takes the position, however, that there is no need for the Court to determine this matter on fundamental justice considerations as this case may be resolved through the application of administrative law principles respecting natural justice.

[48] I note that in Thamotharem, neither the applicant nor the intervener argued that the Chairperson’s standard order of questioning procedure violates the principles of fundamental justice guaranteed under section 7 of the Charter. Rather, they based their submissions on the common law principles of natural justice and procedural fairness. Accordingly, Justice Blanchard determined the content of the procedural protections to be afforded the applicant in that case by an analysis of the factors described by Justice L’Heureux-Dubé in Baker v. Canada (Minister of Citizenship and Immigration), [1999] 2 S.C.R. 817, 174 D.L.R. (4th) 193 [Baker]. The applicants submit that should be the starting point in considering fundamental justice.

[49] As held in Singh, the Charter protects the personal security interests of Convention refugee status claimants. Those interests are engaged by the risk of being returned to persecution and claimants are thus entitled to fundamental justice in the determination of their status. “Fundamental justice”, as used in Charter s. 7, is broader than the administrative law concept of natural justice. It encompasses substantive as well as procedural elements. At a minimum, fundamental justice in the refugee determination context requires that claimants are provided with an adequate opportunity to state their case and to know the case they have to meet. In Singh, the Supreme Court found that this requires notice and an oral hearing, although how that hearing was to be conducted was not specified.

[50] The applicants submit that refugee determination proceedings are quasi-judicial in nature because the Board has some of the trappings of a judicial body, adjudicates on individual rights, is statutorily mandated to hold hearings to make findings of fact, and must identify the relevant laws and apply them to the facts as found. Accordingly, the applicants submit, the procedures employed by the Board will not meet minimum standards of fairness if they deviate significantly from the curial mode. Moreover, as held in Singh, administrative convenience and considerations such as the interest of the tribunal in quicker resolution of cases cannot be determinative of fundamental justice principles. That is the important difference, they submit, between a natural justice argument and a fundamental justice argument – the needs of the tribunal, relevant to a natural justice analysis, cannot trump the Charter rights of the individual.

## 2044:8 · paragraphs 51-58

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `91b0e530f4b121e34c7b06164c2f91eb9a3b71ef985ad2ddeaeac3393d3ab2e7`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:8:subtheme:1 · paragraphs 51-52

- Raw key terms: `counsel, fundamental, heard, principles, right, adequately, adopted, applicants`
- Display key terms: `fundamental, heard, principles, right, adequately, adopted`
- Argument roles: `counterargument_limitation, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, party_position, reasoning_application Display terms: fundamental, heard, principles, right, adequately, adopted Position/evidence statements: [51] The fundamental principles at stake here, the applicants submit, are the right to counsel and the right to be heard. | Counsel submitted that the two principles at play, the right to counsel and to be heard meet the test of fundamental justice principles defined by the Supreme Court in Canadian Foundation for Children, Youth and the Law  Rule/authority context: [51] The fundamental principles at stake here, the applicants submit, are the right to counsel and the right to be heard. | Counsel submitted that the two principles at play, the right to counsel and to be heard meet the test of fundamental justice principles defined by the Supreme Court in Canadian Foundation for Children, Youth and the Law  Application context: , they are legal principles, vital to our societal notion of justice and can be applied with precision and applied predictably. Evidence spans paragraphs 51-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submit` at chunk `4168179` offsets `62-68`; context: [51] The fundamental principles at stake here, the applicants submit, are the right to counsel and the right to be heard.
- Evidence: `governing_rule` cue `principles` at chunk `4168179` offsets `21-31`; context: [51] The fundamental principles at stake here, the applicants submit, are the right to counsel and the right to be heard.
- Evidence: `issue` cue `issue` at chunk `4168180` offsets `9-14`; context: [52] The issue was framed in somewhat different terms during oral argument.
- Evidence: `party_position` cue `submitted` at chunk `4168180` offsets `84-93`; context: Counsel submitted that the two principles at play, the right to counsel and to be heard meet the test of fundamental justice principles defined by the Supreme Court in Canadian Foundation for Children, Youth and the Law v.
- Evidence: `governing_rule` cue `principles` at chunk `4168180` offsets `107-117`; context: Counsel submitted that the two principles at play, the right to counsel and to be heard meet the test of fundamental justice principles defined by the Supreme Court in Canadian Foundation for Children, Youth and the Law v.
- Evidence: `reasoning_application` cue `applied` at chunk `4168180` offsets `442-449`; context: , they are legal principles, vital to our societal notion of justice and can be applied with precision and applied predictably.
- Evidence: `counterargument_limitation` cue `however` at chunk `4168180` offsets `509-516`; context: Counsel suggested, however, that the issue before the Court was slightly more subtle:
It is whether or not within the context of a refugee hearing the right to be heard…encompasses the right of counsel to determine whether or not he will examine in chief.

#### 2044:8:subtheme:2 · paragraphs 53-54

- Raw key terms: `counsel, accept, adduced, argument, board, case, claimant, claimants`
- Display key terms: `accept, adduced, argument, case`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: accept, adduced, argument, case Evidence spans paragraphs 53-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168181` offsets `63-68`; context: [53] I have some difficulty with the notion that the rights at issue in these proceedings are those of counsel.
- Evidence: `issue` cue `question` at chunk `4168182` offsets `382-390`; context: Should the RPO or the Board member, strangers to the claimants, question first, the claimants may be exposed to unnecessary stress that may make it difficult for them to be properly heard.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168182` offsets `147-155`; context: [54] I accept that counsel, generally, have spent considerable time with the claimants prior to the hearings, have gained their trust and know the evidence to be adduced and the claimants’ frailties.

#### 2044:8:subtheme:3 · paragraphs 55-56

- Raw key terms: `claimant, fundamental, justice, refugee, adept, administrative, adverse, applicants`
- Display key terms: `fundamental, justice, refugee, adept, administrative, adverse`
- Argument roles: `party_position, reasoning_application`
- Explanation: Observed roles: party_position, reasoning_application Display terms: fundamental, justice, refugee, adept, administrative, adverse Position/evidence statements: [56] The respondent submits that fundamental justice does not require that a claimant for refugee status have a right to an “examination-in-chief”. Application context: [55] In the applicants’ submissions, this vulnerability requires that the highest order of procedural protection be applied in refugee determinations and that the application of Guideline 7 be reviewed on fundamental jus Evidence spans paragraphs 55-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `applied` at chunk `4168183` offsets `116-123`; context: [55] In the applicants’ submissions, this vulnerability requires that the highest order of procedural protection be applied in refugee determinations and that the application of Guideline 7 be reviewed on fundamental justice standards.
- Evidence: `party_position` cue `submits` at chunk `4168184` offsets `20-27`; context: [56] The respondent submits that fundamental justice does not require that a claimant for refugee status have a right to an “examination-in-chief”.

#### 2044:8:subtheme:4 · paragraphs 57-58

- Raw key terms: `case, decided, necessary, para, above, absolutely, administrative, ambiguity`
- Display key terms: `case, decided, necessary, para, above, absolutely, administrative, ambiguity`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: case, decided, necessary, para, above, absolutely, administrative, ambiguity Rule/authority context: 84, 2002 SCC 3 at para 19, Justice Iacobucci stated that it was not necessary to consider the scope of section 7 in a case arising in the immigration context as it could be decided on administrative law principles and st Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168185` offsets `88-96`; context: [57] As a general rule, the courts should endeavour to avoid expressing an opinion on a question of law where it is not necessary to do so in order to dispose of a case, especially when the question of law that need not be decided is a constitutional question: A.
- Evidence: `governing_rule` cue `principles` at chunk `4168186` offsets `298-308`; context: 84, 2002 SCC 3 at para 19, Justice Iacobucci stated that it was not necessary to consider the scope of section 7 in a case arising in the immigration context as it could be decided on administrative law principles and statutory interpretation.

#### Section text

[51] The fundamental principles at stake here, the applicants submit, are the right to counsel and the right to be heard. Both principles, they argue, are undermined by the standard order of questioning procedure adopted by the Board, as the practice diminishes the role of counsel in assisting the client and prevents the claimant from adequately presenting his or her case.

[52] The issue was framed in somewhat different terms during oral argument. Counsel submitted that the two principles at play, the right to counsel and to be heard meet the test of fundamental justice principles defined by the Supreme Court in Canadian Foundation for Children, Youth and the Law v. Canada (Attorney General), [2004] 1 S.C.R. 76, 2004 SCC 4, i.e., they are legal principles, vital to our societal notion of justice and can be applied with precision and applied predictably. Counsel suggested, however, that the issue before the Court was slightly more subtle:
It is whether or not within the context of a refugee hearing the right to be heard…encompasses the right of counsel to determine whether or not he will examine in chief. (Transcript at 76)

[53] I have some difficulty with the notion that the rights at issue in these proceedings are those of counsel. This may have been just a matter of unfortunate phrasing but a recurring theme throughout the oral argument was that what upset counsel most was the loss of control over the presentation of the claimant’s case in the hearing setting.

[54] I accept that counsel, generally, have spent considerable time with the claimants prior to the hearings, have gained their trust and know the evidence to be adduced and the claimants’ frailties. Many claimants will have been traumatized from their past experiences, as was indicated by Dr. Payne in his evidence. Should the RPO or the Board member, strangers to the claimants, question first, the claimants may be exposed to unnecessary stress that may make it difficult for them to be properly heard.

[55] In the applicants’ submissions, this vulnerability requires that the highest order of procedural protection be applied in refugee determinations and that the application of Guideline 7 be reviewed on fundamental justice standards. In my view, that vulnerability calls for sensitivity and discretion to be exercised by whomever is examining the claimant. Experienced RPOs and Board members may be more adept at it than inexperienced or poorly trained counsel.

[56] The respondent submits that fundamental justice does not require that a claimant for refugee status have a right to an “examination-in-chief”. The proceedings are administrative in nature and the role of the hearings has to be considered in the context of the entire inquiry into the validity of the claim. There is no party adverse in interest to the claimant, unless the Minister intervenes on exclusion grounds, which happens in a small percentage of cases.

[57] As a general rule, the courts should endeavour to avoid expressing an opinion on a question of law where it is not necessary to do so in order to dispose of a case, especially when the question of law that need not be decided is a constitutional question: A.G. Quebec v. Cumming, [1978] 2 S.C.R. 605 at 611, 22 N.R. 271; Philips v. Nova Scotia (Commission of Inquiry in the Westray Mine Tragedy), [1995] 2 S.C.R. 97, 124 D.L.R. (4th) 129 at para 9; Tremblay v. Daigle, [1989] 2 S.C.R. 530, 62 D.L.R. (4th) 634.

[58] I note that in Chieu v. Canada (Minister of Citizenship and Immigration), [2002] 1 S.C.R. 84, 2002 SCC 3 at para 19, Justice Iacobucci stated that it was not necessary to consider the scope of section 7 in a case arising in the immigration context as it could be decided on administrative law principles and statutory interpretation. The same conclusion was reached by the Supreme Court in Baker, above, at para. 11. In Bell ExpressVu Limited Partnership v. Rex, [2002] 2 S.C.R. 559, 2002 SCC 42, the Court discouraged litigants from seeking the use of “Charter values” to interpret legislation when it was not absolutely necessary to resolve ambiguity.

## 2044:9 · paragraphs 59-190

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `53279aa4738c01af4302fa75423a32298ebfd5564de0d73f205cec8c550570e3`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:9:subtheme:1 · paragraphs 59-60

- Raw key terms: `common, constitutional, doctrine, duty, fairness, justice, principles, procedural`
- Display key terms: `common, constitutional, doctrine, duty, fairness, justice, principles, procedural`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: common, constitutional, doctrine, duty, fairness, justice, principles, procedural Rule/authority context: 3, 2002 SCC 1 [Suresh], the Supreme Court made the following comment in relation to the scope of fundamental justice at paragraph 113: The principles of fundamental justice of which s. | While it is an important issue in light of the security of the person interests that are affected by the fairness of the refugee determination process, I am satisfied that this case concerns classic administrative law is Evidence spans paragraphs 59-60. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `principles` at chunk `4168187` offsets `220-230`; context: 3, 2002 SCC 1 [Suresh], the Supreme Court made the following comment in relation to the scope of fundamental justice at paragraph 113:
The principles of fundamental justice of which s.
- Evidence: `issue` cue `issue` at chunk `4168188` offsets `40-45`; context: [60] The applicants seek to elevate the issue of the order of questioning in refugee determination proceedings to a level where constitutional protection would be required and appropriate.
- Evidence: `governing_rule` cue `under` at chunk `4168188` offsets `437-442`; context: While it is an important issue in light of the security of the person interests that are affected by the fairness of the refugee determination process, I am satisfied that this case concerns classic administrative law issues that may be determined under the principles of natural justice and fairness without invoking the Charter.

#### 2044:9:subtheme:2 · paragraphs 61-62

- Raw key terms: `court, guideline, hearings, order, questioning, section, administrative, adversarial`
- Display key terms: `guideline, hearings, order, questioning, section, administrative, adversarial`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: guideline, hearings, order, questioning, section, administrative, adversarial Rule/authority context: [61] I find, therefore, that it is not necessary for the Court to determine the scope and effect of fundamental justice under section 7 with regard to the application of the Guideline. Application context: [61] I find, therefore, that it is not necessary for the Court to determine the scope and effect of fundamental justice under section 7 with regard to the application of the Guideline. Evidence spans paragraphs 61-62. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168189` offsets `583-589`; context: That procedural order was developed in the context of adversarial proceedings and strict rules of evidence in which the role of the Court was to oversee the contest between the parties, decide issues of law and instruct a jury, if sitting with one, or itself, if sitting alone, to find the facts and apply the law within the narrow confines of the pleadings or indictment.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168189` offsets `488-496`; context: That procedural order was developed in the context of adversarial proceedings and strict rules of evidence in which the role of the Court was to oversee the contest between the parties, decide issues of law and instruct a jury, if sitting with one, or itself, if sitting alone, to find the facts and apply the law within the narrow confines of the pleadings or indictment.
- Evidence: `governing_rule` cue `under` at chunk `4168189` offsets `120-125`; context: [61] I find, therefore, that it is not necessary for the Court to determine the scope and effect of fundamental justice under section 7 with regard to the application of the Guideline.
- Evidence: `reasoning_application` cue `I find` at chunk `4168189` offsets `5-11`; context: [61] I find, therefore, that it is not necessary for the Court to determine the scope and effect of fundamental justice under section 7 with regard to the application of the Guideline.

#### 2044:9:subtheme:3 · paragraphs 63-65

- Raw key terms: `administrative, claimant, court, justice, procedural, procedure, proceedings, ability`
- Display key terms: `administrative, justice, procedural, procedure, proceedings, ability`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: administrative, justice, procedural, procedure, proceedings, ability Evidence spans paragraphs 63-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168191` offsets `325-333`; context: 170 states that the RPD must give the claimant and the Minister a reasonable opportunity to present evidence, question witnesses and make representations, the procedure is not bound by “legal or technical rules of evidence”.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168191` offsets `315-323`; context: 170 states that the RPD must give the claimant and the Minister a reasonable opportunity to present evidence, question witnesses and make representations, the procedure is not bound by “legal or technical rules of evidence”.

#### 2044:9:subtheme:4 · paragraphs 66-67

- Raw key terms: `case, claimant, counsel, determination, each, fundamental, hearing, justice`
- Display key terms: `case, determination, each, fundamental, hearing, justice`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position Display terms: case, determination, each, fundamental, hearing, justice Position/evidence statements: But I have difficulty understanding why that would be necessary in every case or why it is essential in fundamental justice terms that the claimant have the option at his or her discretion to determine the order of quest Rule/authority context: [67] Under Guideline 7, it remains open to each claimant in a refugee determination hearing to fully present any element of his or her case that the RPO or Board member does not explore in their initial questioning and t Operative outcome context: Were it to foreclose such an opportunity, I would have no hesitation in finding that the right to a hearing was being denied. Evidence spans paragraphs 66-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168194` offsets `231-239`; context: It may be that in a particular refugee determination hearing it would be necessary for the claimant’s counsel to question first in order to ensure that his or her evidence is properly presented.
- Evidence: `party_position` cue `argued` at chunk `4168194` offsets `564-570`; context: But I have difficulty understanding why that would be necessary in every case or why it is essential in fundamental justice terms that the claimant have the option at his or her discretion to determine the order of questioning, as the applicants have argued.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168194` offsets `59-67`; context: [66] What constitutes a “reasonable opportunity to present evidence” must depend upon the circumstances of each case.
- Evidence: `counterargument_limitation` cue `But` at chunk `4168194` offsets `313-316`; context: But I have difficulty understanding why that would be necessary in every case or why it is essential in fundamental justice terms that the claimant have the option at his or her discretion to determine the order of questioning, as the applicants have argued.
- Evidence: `governing_rule` cue `Under` at chunk `4168195` offsets `5-10`; context: [67] Under Guideline 7, it remains open to each claimant in a refugee determination hearing to fully present any element of his or her case that the RPO or Board member does not explore in their initial questioning and to have the effective assistance of counsel in so doing.
- Evidence: `disposition` cue `denied` at chunk `4168195` offsets `394-400`; context: Were it to foreclose such an opportunity, I would have no hesitation in finding that the right to a hearing was being denied.

#### 2044:9:subtheme:5 · paragraphs 68-70

- Raw key terms: `charter, counsel, divisions, evidence, factual, proceedings, section, tribunals`
- Display key terms: `charter, divisions, factual, proceedings, section, tribunals`
- Argument roles: `evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, party_position, reasoning_application Display terms: charter, divisions, factual, proceedings, section, tribunals Position/evidence statements: [68] With regard to section 15 of the Charter, counsel for one of the applicants has argued that refugee claimants are discriminated against because they do not have the right to present their evidence first and to have  Application context: [68] With regard to section 15 of the Charter, counsel for one of the applicants has argued that refugee claimants are discriminated against because they do not have the right to present their evidence first and to have  Evidence spans paragraphs 68-70. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168196` offsets `234-242`; context: [68] With regard to section 15 of the Charter, counsel for one of the applicants has argued that refugee claimants are discriminated against because they do not have the right to present their evidence first and to have their counsel question them first, in contrast to the procedure before other tribunals, including the other IRB Divisions.
- Evidence: `party_position` cue `argued` at chunk `4168196` offsets `85-91`; context: [68] With regard to section 15 of the Charter, counsel for one of the applicants has argued that refugee claimants are discriminated against because they do not have the right to present their evidence first and to have their counsel question them first, in contrast to the procedure before other tribunals, including the other IRB Divisions.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168196` offsets `193-201`; context: [68] With regard to section 15 of the Charter, counsel for one of the applicants has argued that refugee claimants are discriminated against because they do not have the right to present their evidence first and to have their counsel question them first, in contrast to the procedure before other tribunals, including the other IRB Divisions.
- Evidence: `reasoning_application` cue `because` at chunk `4168196` offsets `141-148`; context: [68] With regard to section 15 of the Charter, counsel for one of the applicants has argued that refugee claimants are discriminated against because they do not have the right to present their evidence first and to have their counsel question them first, in contrast to the procedure before other tribunals, including the other IRB Divisions.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168197` offsets `17-25`; context: [69] There is no evidence before me as to the practice of other administrative tribunals and I am not prepared to speculate as to what their practices might be based on my own knowledge or counsel’s submissions.

#### 2044:9:subtheme:6 · paragraphs 71-72

- Raw key terms: `court, guideline, justice, natural, question, whether, above, accordingly`
- Display key terms: `guideline, justice, natural, question, whether, above, accordingly`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: guideline, justice, natural, question, whether, above, accordingly Rule/authority context: [72] The question of whether the order of questioning implemented by the Board under Guideline 7 is, in itself, inconsistent with natural justice was addressed in a number of decisions of this Court prior to Thamotharem. Application context: Accordingly, I decline to address that question. Evidence spans paragraphs 71-72. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168199` offsets `111-118`; context: [71] I am satisfied that there is an insufficient factual basis in this case upon which the Court could decide whether claimants in refugee determination proceedings were discriminated against through the implementation of Guideline 7 as contemplated by s.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4168199` offsets `434-445`; context: Accordingly, I decline to address that question.
- Evidence: `issue` cue `question` at chunk `4168200` offsets `9-17`; context: [72] The question of whether the order of questioning implemented by the Board under Guideline 7 is, in itself, inconsistent with natural justice was addressed in a number of decisions of this Court prior to Thamotharem.
- Evidence: `governing_rule` cue `under` at chunk `4168200` offsets `79-84`; context: [72] The question of whether the order of questioning implemented by the Board under Guideline 7 is, in itself, inconsistent with natural justice was addressed in a number of decisions of this Court prior to Thamotharem.

#### 2044:9:subtheme:7 · paragraphs 73-74

- Raw key terms: `case, court, decisions, fairness, guideline, question, whether, above`
- Display key terms: `case, decisions, fairness, guideline, question, whether, above`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: case, decisions, fairness, guideline, question, whether, above Application context: Accordingly, Justice Blanchard revisited the question of whether the application of Guideline 7, was, in itself, inconsistent with procedural fairness. Evidence spans paragraphs 73-74. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168201` offsets `155-162`; context: [73] In general, the common view expressed by my colleagues in these decisions is that the procedure followed in each case had to be examined to determine whether there had been a breach of fairness.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4168201` offsets `256-264`; context: As stated by the Court in Zaki, above, at paragraph 14:
Although the Guideline per se is not, in my view, procedurally unfair, it may well be that its implementation in any given case is done in such a way as to lead to a conclusion that a claimant was not afforded an opportunity to make his case.
- Evidence: `issue` cue `issues` at chunk `4168202` offsets `133-139`; context: [74] Justice Blanchard reviewed these decisions in Thamotharem and found that, while instructive, they were not determinative of the issues before him.
- Evidence: `evidence_fact` cue `found that` at chunk `4168202` offsets `67-77`; context: [74] Justice Blanchard reviewed these decisions in Thamotharem and found that, while instructive, they were not determinative of the issues before him.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4168202` offsets `375-386`; context: Accordingly, Justice Blanchard revisited the question of whether the application of Guideline 7, was, in itself, inconsistent with procedural fairness.

#### 2044:9:subtheme:8 · paragraphs 75-76

- Raw key terms: `counsel, question, analysis, applicants, atwal, benefit, blanchard, canada`
- Display key terms: `question, analysis, atwal, benefit, blanchard`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: question, analysis, atwal, benefit, blanchard Evidence spans paragraphs 75-76. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168203` offsets `59-67`; context: [75] I have had the benefit of the thorough review of that question which Justice Blanchard conducted together with the submissions of counsel in these proceedings which have largely focused on his analysis.
- Evidence: `issue` cue `question` at chunk `4168204` offsets `246-254`; context: [76] In an effort to establish that the Court has previously recognized that fairness dictates that refugee claimants must be examined first by their counsel, the applicants have cited several decisions in which the conduct of the hearing was in question.

#### 2044:9:subtheme:9 · paragraphs 77-79

- Raw key terms: `court, decisions, blanchard, case, cases, cited, claimant, considered`
- Display key terms: `decisions, blanchard, case, cases, cited, considered`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: decisions, blanchard, case, cases, cited, considered Rule/authority context: Following a review of each case, Justice Blanchard expressed the following conclusion at paragraph 46 of his reasons: In my opinion, in none of these cases did the Court establish that the principles of natural justice a Evidence spans paragraphs 77-79. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168205` offsets `408-415`; context: In fact, whether the Board’s choice of the order of questioning accorded with natural justice or procedural fairness was not before the Court in any of the cases.
- Evidence: `governing_rule` cue `principles` at chunk `4168205` offsets `276-286`; context: Following a review of each case, Justice Blanchard expressed the following conclusion at paragraph 46 of his reasons:
In my opinion, in none of these cases did the Court establish that the principles of natural justice and procedural fairness require that refugee claimants be questioned by their counsel first.
- Evidence: `issue` cue `question` at chunk `4168206` offsets `421-429`; context: While the reasons for decision contain statements which may be construed as lending support for the notion that a fair hearing requires that the claimant’s counsel question first, a close examination discloses that the Court in each case was more concerned with whether the hearing, as a whole, was fair than with the order of questioning.

#### 2044:9:subtheme:10 · paragraphs 80-81

- Raw key terms: `applicant, badgering, conducted, court, cross-examination, described, hearing, lead`
- Display key terms: `badgering, conducted, cross-examination, described, hearing, lead`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, party_position, reasoning_application Display terms: badgering, conducted, cross-examination, described, hearing, lead Position/evidence statements: The applicants rely on paragraph 4 of the reasons which reads as follows: As argued by Counsel for the Applicant in the present application, a serious due process issue exists as to whether there was a fair hearing befor | Immediately prior to asking for the Applicant's lawyer to consent to the procedure whereby the RPO would lead the claimant's case, the case was simply called "a simple outlined claim". Application context: At the hearing, the Applicant was not allowed to lead his evidence, but instead, the Refugee Protection Officer was instructed to question first, and then, the RPD followed with what I find is accurately described by Cou Operative outcome context: At the hearing, the Applicant was not allowed to lead his evidence, but instead, the Refugee Protection Officer was instructed to question first, and then, the RPD followed with what I find is accurately described by Cou Evidence spans paragraphs 80-81. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168208` offsets `346-351`; context: The applicants rely on paragraph 4 of the reasons which reads as follows:
As argued by Counsel for the Applicant in the present application, a serious due process issue exists as to whether there was a fair hearing before the RPD.
- Evidence: `party_position` cue `argued` at chunk `4168208` offsets `260-266`; context: The applicants rely on paragraph 4 of the reasons which reads as follows:
As argued by Counsel for the Applicant in the present application, a serious due process issue exists as to whether there was a fair hearing before the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168208` offsets `472-480`; context: At the hearing, the Applicant was not allowed to lead his evidence, but instead, the Refugee Protection Officer was instructed to question first, and then, the RPD followed with what I find is accurately described by Counsel for the Applicant as "badgering" cross-examination
- Evidence: `reasoning_application` cue `I find` at chunk `4168208` offsets `597-603`; context: At the hearing, the Applicant was not allowed to lead his evidence, but instead, the Refugee Protection Officer was instructed to question first, and then, the RPD followed with what I find is accurately described by Counsel for the Applicant as "badgering" cross-examination
- Evidence: `counterargument_limitation` cue `but` at chunk `4168208` offsets `482-485`; context: At the hearing, the Applicant was not allowed to lead his evidence, but instead, the Refugee Protection Officer was instructed to question first, and then, the RPD followed with what I find is accurately described by Counsel for the Applicant as "badgering" cross-examination
- Evidence: `disposition` cue `allowed` at chunk `4168208` offsets `452-459`; context: At the hearing, the Applicant was not allowed to lead his evidence, but instead, the Refugee Protection Officer was instructed to question first, and then, the RPD followed with what I find is accurately described by Counsel for the Applicant as "badgering" cross-examination
- Evidence: `issue` cue `issues` at chunk `4168209` offsets `364-370`; context: However, it is also clear from the decision that the Court was concerned that the RPD had effectively set a trap for the applicant at the outset of the hearing by misdescribing the issues to be addressed.
- Evidence: `party_position` cue `claim` at chunk `4168209` offsets `808-813`; context: Immediately prior to asking for the Applicant's lawyer to consent to the procedure whereby the RPO would lead the claimant's case, the case was simply called "a simple outlined claim".
- Evidence: `evidence_fact` cue `record` at chunk `4168209` offsets `623-629`; context: At paragraph 5 he states:
It is quite clear that at the opening of the hearing the RPD had a suspicion that the Applicant's credibility was seriously in question, given the variance between the two statements which were in the written record.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168209` offsets `183-190`; context: However, it is also clear from the decision that the Court was concerned that the RPD had effectively set a trap for the applicant at the outset of the hearing by misdescribing the issues to be addressed.

#### 2044:9:subtheme:11 · paragraphs 82-83

- Raw key terms: `counsel, court, fair, first, reached, above, accepted, added`
- Display key terms: `fair, first, reached, above, accepted, added`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: fair, first, reached, above, accepted, added Application context: [83] In Sandor, above, at paragraph 36, the Court found that the applicant was denied a fair hearing largely because of the Board Member’s extensive questioning. Operative outcome context: [83] In Sandor, above, at paragraph 36, the Court found that the applicant was denied a fair hearing largely because of the Board Member’s extensive questioning. Evidence spans paragraphs 82-83. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168210` offsets `125-133`; context: [82] As I read the Court’s reasons, this decision does not stand for the proposition that the claimant’s counsel must always question first but rather, whichever procedure is followed, that the claimant must be given fair notice of the issues and a fair opportunity to be heard.
- Evidence: `counterargument_limitation` cue `but` at chunk `4168210` offsets `140-143`; context: [82] As I read the Court’s reasons, this decision does not stand for the proposition that the claimant’s counsel must always question first but rather, whichever procedure is followed, that the claimant must be given fair notice of the issues and a fair opportunity to be heard.
- Evidence: `evidence_fact` cue `found that` at chunk `4168211` offsets `50-60`; context: [83] In Sandor, above, at paragraph 36, the Court found that the applicant was denied a fair hearing largely because of the Board Member’s extensive questioning.
- Evidence: `reasoning_application` cue `because` at chunk `4168211` offsets `109-116`; context: [83] In Sandor, above, at paragraph 36, the Court found that the applicant was denied a fair hearing largely because of the Board Member’s extensive questioning.
- Evidence: `disposition` cue `denied` at chunk `4168211` offsets `79-85`; context: [83] In Sandor, above, at paragraph 36, the Court found that the applicant was denied a fair hearing largely because of the Board Member’s extensive questioning.

#### 2044:9:subtheme:12 · paragraphs 84-86

- Raw key terms: `fairness, affected, analysis, baker, board, claimants, decision, factors`
- Display key terms: `fairness, affected, analysis, baker, factors`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: fairness, affected, analysis, baker, factors Evidence spans paragraphs 84-86. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168212` offsets `148-153`; context: The issue of whether procedural fairness required that the claimant’s counsel go first does not appear to have been squarely addressed in the proceedings as it had not been raised prior to the judicial review hearing.
- Evidence: `issue` cue `whether` at chunk `4168213` offsets `65-72`; context: [85] As noted above, the factors to be considered in determining whether the common law duty of fairness has been met by the procedures in question were discussed by Justice L’Heureux-Dubé in Baker, above, at paragraphs 22-28.

#### 2044:9:subtheme:13 · paragraphs 87-90

- Raw key terms: `decision, higher, protection, second, appeal, applicants, baker, blanchard`
- Display key terms: `higher, protection, second, baker, blanchard`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: higher, protection, second, baker, blanchard Position/evidence statements: They submit that there are additional factors that militate in favour of a higher standard of procedural fairness that were not considered in Thamotharem. | The first, the respondent submits, should indicate a lower standard and the second is, at best, neutral. Evidence spans paragraphs 87-90. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168215` offsets `32-37`; context: [87] The applicants do not take issue with Justice Blanchard’s analysis of the second and third Baker factors but question his analysis of the first factor and invite me to reach different conclusions regarding the remaining two.
- Evidence: `party_position` cue `submit` at chunk `4168215` offsets `235-241`; context: They submit that there are additional factors that militate in favour of a higher standard of procedural fairness that were not considered in Thamotharem.
- Evidence: `party_position` cue `submits` at chunk `4168216` offsets `140-147`; context: The first, the respondent submits, should indicate a lower standard and the second is, at best, neutral.
- Evidence: `party_position` cue `submit` at chunk `4168218` offsets `20-26`; context: [90] The applicants submit that the enactment by Parliament in IRPA of provisions for a Refugee Appeal Division (RAD), combined with the failure of the Governor-in-Council to bring the RAD into effect enhances the duty of fairness owed to the applicant and decreases the deference owed by the Court to a decision of the Board on refugee protection.

#### 2044:9:subtheme:14 · paragraphs 91-92

- Raw key terms: `appeal, baker, court, decision, factor, procedural, refugee, second`
- Display key terms: `baker, factor, procedural, refugee, second`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: baker, factor, procedural, refugee, second Position/evidence statements: The respondent submits, however, that issues concerning the RAD are separate and distinct from the Guideline 7 issues that are properly before this Court. Evidence spans paragraphs 91-92. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168219` offsets `278-284`; context: The respondent submits, however, that issues concerning the RAD are separate and distinct from the Guideline 7 issues that are properly before this Court.
- Evidence: `party_position` cue `submits` at chunk `4168219` offsets `255-262`; context: The respondent submits, however, that issues concerning the RAD are separate and distinct from the Guideline 7 issues that are properly before this Court.
- Evidence: `counterargument_limitation` cue `however` at chunk `4168219` offsets `264-271`; context: The respondent submits, however, that issues concerning the RAD are separate and distinct from the Guideline 7 issues that are properly before this Court.
- Evidence: `evidence_fact` cue `record` at chunk `4168220` offsets `379-385`; context: I have nothing to add to his conclusion in that regard other than to note that the appeal provided for in the unproclaimed sections was to be conducted on the basis of the record of the refugee determination proceedings below rather than through an oral hearing.

#### 2044:9:subtheme:15 · paragraphs 93-96

- Raw key terms: `refugee, adversarial, non-adversarial, proceedings, protection, applicants, blanchard, claimant`
- Display key terms: `refugee, adversarial, non-adversarial, proceedings, protection, blanchard`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: refugee, adversarial, non-adversarial, proceedings, protection, blanchard Position/evidence statements: [94] The applicants submit that the characterization of the refugee determination process as non-adversarial is suspect when the role of counsel for the claimant is compared to that of the RPO. | [95] Further, the applicants submit that Justice Blanchard reached the conclusion that the refugee proceedings are non-adversarial without reference to a suitable factual foundation. Rule/authority context: In particular, the respondent contrasts the rules applicable to the Immigration Appeal Division, constituted as a court of record under IRPA s. Application context: However, because the nature of the decision calls for the Board to adjudicate issues that have an impact on the rights of refugee claimants he concluded that a higher level of procedural protection is warranted. Evidence spans paragraphs 93-96. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168221` offsets `455-461`; context: However, because the nature of the decision calls for the Board to adjudicate issues that have an impact on the rights of refugee claimants he concluded that a higher level of procedural protection is warranted.
- Evidence: `evidence_fact` cue `found that` at chunk `4168221` offsets `57-67`; context: [93] With respect to the first factor, Justice Blanchard found that Parliament intended the RPD procedure to be less judicial and more inquisitorial.
- Evidence: `reasoning_application` cue `because` at chunk `4168221` offsets `386-393`; context: However, because the nature of the decision calls for the Board to adjudicate issues that have an impact on the rights of refugee claimants he concluded that a higher level of procedural protection is warranted.
- Evidence: `counterargument_limitation` cue `notwithstanding` at chunk `4168221` offsets `285-300`; context: He concluded at paragraph 75, after comparing RPD hearings with court proceedings, that the RPD hearing was not an adversarial process notwithstanding the often aggressive and probing nature of questioning by RPOs and members.
- Evidence: `party_position` cue `submit` at chunk `4168222` offsets `20-26`; context: [94] The applicants submit that the characterization of the refugee determination process as non-adversarial is suspect when the role of counsel for the claimant is compared to that of the RPO.
- Evidence: `party_position` cue `submit` at chunk `4168223` offsets `29-35`; context: [95] Further, the applicants submit that Justice Blanchard reached the conclusion that the refugee proceedings are non-adversarial without reference to a suitable factual foundation.
- Evidence: `evidence_fact` cue `record` at chunk `4168223` offsets `360-366`; context: In Benitez, it is submitted, the record discloses that the Member and RPO in turn, took turns over almost the entire day of the hearing to aggressively examine the claimant on perceived inconsistencies in his account.
- Evidence: `evidence_fact` cue `record` at chunk `4168224` offsets `305-311`; context: In particular, the respondent contrasts the rules applicable to the Immigration Appeal Division, constituted as a court of record under IRPA s.
- Evidence: `governing_rule` cue `under` at chunk `4168224` offsets `312-317`; context: In particular, the respondent contrasts the rules applicable to the Immigration Appeal Division, constituted as a court of record under IRPA s.

#### 2044:9:subtheme:16 · paragraphs 97-98

- Raw key terms: `adversarial, board, canada, consistent, court, member, members, process`
- Display key terms: `adversarial, consistent, members, process`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: adversarial, consistent, members, process Position/evidence statements: [97] The respondent further submits that the fact that RPOs and Board members may question claimants does not make the process adversarial. | The process was not designed to be a contest between parties adverse in interest but rather an inquiry into whether a claim to Canada’s protection is being legitimately made. Evidence spans paragraphs 97-98. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168225` offsets `82-90`; context: [97] The respondent further submits that the fact that RPOs and Board members may question claimants does not make the process adversarial.
- Evidence: `party_position` cue `submits` at chunk `4168225` offsets `28-35`; context: [97] The respondent further submits that the fact that RPOs and Board members may question claimants does not make the process adversarial.
- Evidence: `issue` cue `whether` at chunk `4168226` offsets `565-572`; context: The process was not designed to be a contest between parties adverse in interest but rather an inquiry into whether a claim to Canada’s protection is being legitimately made.
- Evidence: `party_position` cue `claim` at chunk `4168226` offsets `575-580`; context: The process was not designed to be a contest between parties adverse in interest but rather an inquiry into whether a claim to Canada’s protection is being legitimately made.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168226` offsets `212-220`; context: Notwithstanding Professor Galloway’s evidence and the Court’s awareness of egregious examples of hostile and aggressive questioning, I am not persuaded that a failure to respect that intent by RPOs or Board members in individual cases establishes that the hearings are adversarial.
- Evidence: `counterargument_limitation` cue `Notwithstanding` at chunk `4168226` offsets `175-190`; context: Notwithstanding Professor Galloway’s evidence and the Court’s awareness of egregious examples of hostile and aggressive questioning, I am not persuaded that a failure to respect that intent by RPOs or Board members in individual cases establishes that the hearings are adversarial.

#### 2044:9:subtheme:17 · paragraphs 99-100

- Raw key terms: `board, expectation, legitimate, question, refugee, able, acceptable, adopted`
- Display key terms: `expectation, legitimate, question, refugee, able, acceptable, adopted`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: expectation, legitimate, question, refugee, able, acceptable, adopted Evidence spans paragraphs 99-100. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168227` offsets `97-105`; context: [99] While Refugee Protection Officers and Board members receive training and guidance on how to question effectively and how to deal with vulnerable claimants, it is not surprising that there will be cases in which the questioning crosses a line as to what is acceptable in terms of fairness.
- Evidence: `issue` cue `question` at chunk `4168228` offsets `253-261`; context: [100] With regard to the fourth Baker factor, Justice Blanchard found that the Board’s advance notice that it was implementing the procedure set out in Guideline 7 indicated that there was no legitimate expectation that refugee counsel would be able to question first.
- Evidence: `evidence_fact` cue `found that` at chunk `4168228` offsets `64-74`; context: [100] With regard to the fourth Baker factor, Justice Blanchard found that the Board’s advance notice that it was implementing the procedure set out in Guideline 7 indicated that there was no legitimate expectation that refugee counsel would be able to question first.

#### 2044:9:subtheme:18 · paragraphs 101-105

- Raw key terms: `expectation, legitimate, applicants, adoption, certain, counsel, done, first`
- Display key terms: `expectation, legitimate, adoption, certain, done, first`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue, party_position, reasoning_application Display terms: expectation, legitimate, adoption, certain, done, first Position/evidence statements: [101] In these proceedings, the Toronto-based applicants submit that they had a legitimate expectation that they would be allowed to question first because that was the general practice prior to the adoption of the Guide | [102] Further the applicants submit, the elimination of certain of the procedural safeguards that were present under the former Immigration Act, such as two-member panels and the reduction of time within which to submit  Rule/authority context: [102] Further the applicants submit, the elimination of certain of the procedural safeguards that were present under the former Immigration Act, such as two-member panels and the reduction of time within which to submit  Application context: [101] In these proceedings, the Toronto-based applicants submit that they had a legitimate expectation that they would be allowed to question first because that was the general practice prior to the adoption of the Guide Operative outcome context: [101] In these proceedings, the Toronto-based applicants submit that they had a legitimate expectation that they would be allowed to question first because that was the general practice prior to the adoption of the Guide | They cannot rely on their counsel’s experience that this is the way it was done in Toronto and assert that it should remain the same as the practice varied across the country. Evidence spans paragraphs 101-105. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168229` offsets `133-141`; context: [101] In these proceedings, the Toronto-based applicants submit that they had a legitimate expectation that they would be allowed to question first because that was the general practice prior to the adoption of the Guideline, outside of hearings conducted in Montreal and Ottawa.
- Evidence: `party_position` cue `submit` at chunk `4168229` offsets `57-63`; context: [101] In these proceedings, the Toronto-based applicants submit that they had a legitimate expectation that they would be allowed to question first because that was the general practice prior to the adoption of the Guideline, outside of hearings conducted in Montreal and Ottawa.
- Evidence: `reasoning_application` cue `because` at chunk `4168229` offsets `148-155`; context: [101] In these proceedings, the Toronto-based applicants submit that they had a legitimate expectation that they would be allowed to question first because that was the general practice prior to the adoption of the Guideline, outside of hearings conducted in Montreal and Ottawa.
- Evidence: `disposition` cue `allowed` at chunk `4168229` offsets `122-129`; context: [101] In these proceedings, the Toronto-based applicants submit that they had a legitimate expectation that they would be allowed to question first because that was the general practice prior to the adoption of the Guideline, outside of hearings conducted in Montreal and Ottawa.
- Evidence: `party_position` cue `submit` at chunk `4168230` offsets `29-35`; context: [102] Further the applicants submit, the elimination of certain of the procedural safeguards that were present under the former Immigration Act, such as two-member panels and the reduction of time within which to submit a personal information form (“PIF”) has led to a legitimate expectation on the part of refugees that such protections as they have left will be respected, particularly in the absence of a statutory right to an appeal.
- Evidence: `governing_rule` cue `under` at chunk `4168230` offsets `111-116`; context: [102] Further the applicants submit, the elimination of certain of the procedural safeguards that were present under the former Immigration Act, such as two-member panels and the reduction of time within which to submit a personal information form (“PIF”) has led to a legitimate expectation on the part of refugees that such protections as they have left will be respected, particularly in the absence of a statutory right to an appeal.
- Evidence: `party_position` cue `contends` at chunk `4168231` offsets `21-29`; context: [103] The respondent contends that the applicants could not have a legitimate expectation concerning the order of questioning as refugee claimants were never given any indication that they would be questioned first by their counsel when they made their claims.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4168231` offsets `266-272`; context: They cannot rely on their counsel’s experience that this is the way it was done in Toronto and assert that it should remain the same as the practice varied across the country.
- Evidence: `disposition` cue `varied` at chunk `4168231` offsets `410-416`; context: They cannot rely on their counsel’s experience that this is the way it was done in Toronto and assert that it should remain the same as the practice varied across the country.

#### 2044:9:subtheme:19 · paragraphs 106-109

- Raw key terms: `procedures, applicants, arose, board, cases, counsel, determine, directly`
- Display key terms: `procedures, arose, cases, determine, directly`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: procedures, arose, cases, determine, directly Rule/authority context: [108] At paragraphs 81-83 of his reasons, Justice Blanchard concluded that Parliament accorded the Board the authority to determine its own procedures provided they were not contrary to the principles of natural justice. Application context: I am asked to find that a legitimate expectation arose from the regular practice of some Board members, at least in Toronto, to allow or invite counsel to question their clients first because that is what, in essence, co Operative outcome context: For example in Qi, the applicant had been invited to have counsel present at her interview but counsel was then denied an opportunity to take part in the process. Evidence spans paragraphs 106-109. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168234` offsets `34-42`; context: [106] In each of these cases, the question of legitimate expectation arose in the context of representations made or alleged to have been made directly to the party seeking to rely on the doctrine.
- Evidence: `disposition` cue `denied` at chunk `4168234` offsets `310-316`; context: For example in Qi, the applicant had been invited to have counsel present at her interview but counsel was then denied an opportunity to take part in the process.
- Evidence: `issue` cue `question` at chunk `4168235` offsets `351-359`; context: I am asked to find that a legitimate expectation arose from the regular practice of some Board members, at least in Toronto, to allow or invite counsel to question their clients first because that is what, in essence, counsel there have come to expect.
- Evidence: `reasoning_application` cue `because` at chunk `4168235` offsets `380-387`; context: I am asked to find that a legitimate expectation arose from the regular practice of some Board members, at least in Toronto, to allow or invite counsel to question their clients first because that is what, in essence, counsel there have come to expect.
- Evidence: `governing_rule` cue `principles` at chunk `4168236` offsets `190-200`; context: [108] At paragraphs 81-83 of his reasons, Justice Blanchard concluded that Parliament accorded the Board the authority to determine its own procedures provided they were not contrary to the principles of natural justice.

#### 2044:9:subtheme:20 · paragraphs 110-114

- Raw key terms: `baker, case, justice, questioning, refugee, result, weight, always`
- Display key terms: `baker, case, justice, questioning, refugee, result, weight, always`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: baker, case, justice, questioning, refugee, result, weight, always Position/evidence statements: [110] The applicants submit, nonetheless, that for the purpose of the Baker analysis in this case, it is necessary to consider whether the evidence supports the conclusion that the order of questioning adopted by the Boa | [114] The applicants submit that a number of considerations common to refugee claimants underscore the need to allow claimants’ counsel to conduct an examination-in-chief in refugee proceedings. Application context: In giving weight to the choices made by the Board respecting its procedures, it is not necessary for the Court to conclude that these procedures have been effective or the best choice. | The applicants submit that because of these considerations, it is unfair to the applicants to have questioning begin by someone other than their own counsel. Evidence spans paragraphs 110-114. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168238` offsets `127-134`; context: [110] The applicants submit, nonetheless, that for the purpose of the Baker analysis in this case, it is necessary to consider whether the evidence supports the conclusion that the order of questioning adopted by the Board does in fact improve its efficiency or, put another way, whether counsel-first questioning would be an impediment to hearing efficiency.
- Evidence: `party_position` cue `submit` at chunk `4168238` offsets `21-27`; context: [110] The applicants submit, nonetheless, that for the purpose of the Baker analysis in this case, it is necessary to consider whether the evidence supports the conclusion that the order of questioning adopted by the Board does in fact improve its efficiency or, put another way, whether counsel-first questioning would be an impediment to hearing efficiency.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168238` offsets `139-147`; context: [110] The applicants submit, nonetheless, that for the purpose of the Baker analysis in this case, it is necessary to consider whether the evidence supports the conclusion that the order of questioning adopted by the Board does in fact improve its efficiency or, put another way, whether counsel-first questioning would be an impediment to hearing efficiency.
- Evidence: `reasoning_application` cue `conclude` at chunk `4168240` offsets `283-291`; context: In giving weight to the choices made by the Board respecting its procedures, it is not necessary for the Court to conclude that these procedures have been effective or the best choice.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168241` offsets `400-407`; context: However, he concluded, at paragraph 90, that the fact that many refugee claimants are vulnerable and as a result have difficulty testifying effectively does not necessarily make Guideline 7 unfair.
- Evidence: `party_position` cue `submit` at chunk `4168242` offsets `21-27`; context: [114] The applicants submit that a number of considerations common to refugee claimants underscore the need to allow claimants’ counsel to conduct an examination-in-chief in refugee proceedings.
- Evidence: `reasoning_application` cue `because` at chunk `4168242` offsets `622-629`; context: The applicants submit that because of these considerations, it is unfair to the applicants to have questioning begin by someone other than their own counsel.

#### 2044:9:subtheme:21 · paragraphs 115-117

- Raw key terms: `applicants, board, case, claimant, evidence, guideline, hearing, particular`
- Display key terms: `case, guideline, hearing, particular`
- Argument roles: `evidence_fact, issue, party_position`
- Explanation: Observed roles: evidence_fact, issue, party_position Display terms: case, guideline, hearing, particular Position/evidence statements: [116] Contrary to the applicants’ assertions that Guideline 7 is intended to be a mandatory provision, the respondent submits that paragraph 23 anticipates that it may not be appropriate in every hearing. | The applicants submit that Justice Blanchard may have reached a different conclusion on the weight to be given this factor if he had evidence before him of actual, rather than hypothetical vulnerability. Evidence spans paragraphs 115-117. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168243` offsets `526-533`; context: The Board would then be in a position to make a determination as to whether the application of Guideline 7 to the particular case is the best course of action.
- Evidence: `party_position` cue `submits` at chunk `4168244` offsets `118-125`; context: [116] Contrary to the applicants’ assertions that Guideline 7 is intended to be a mandatory provision, the respondent submits that paragraph 23 anticipates that it may not be appropriate in every hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168244` offsets `362-370`; context: The claimant is free in any particular case to bring to the attention of the Board any relevant evidence which would establish why proceeding with an examination by the RPO or Board member would prejudice their case.
- Evidence: `party_position` cue `submit` at chunk `4168245` offsets `140-146`; context: The applicants submit that Justice Blanchard may have reached a different conclusion on the weight to be given this factor if he had evidence before him of actual, rather than hypothetical vulnerability.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168245` offsets `59-67`; context: [117] The applicant in Thamotharem had not put forward any evidence that he had any of these characteristic vulnerabilities.

#### 2044:9:subtheme:22 · paragraphs 118-119

- Raw key terms: `ability, claimants, counsel, evidence, questioning, acknowledged, affect, afforded`
- Display key terms: `ability, questioning, acknowledged, affect, afforded`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: ability, questioning, acknowledged, affect, afforded Position/evidence statements: [118] To illustrate, the applicants point to the case of applicant Gutierrez Trujillo (IMM-2709-05) in which a psychological report had been submitted to the Board indicating that he was suffering from post-traumatic str | [119] The respondent submits that the evidence indicates that the manner in which vulnerable claimants are questioned matters much more than who questions them. Evidence spans paragraphs 118-119. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168246` offsets `801-809`; context: The only practical approach to the reality that many claimants have vulnerabilities which would make it fairer for their counsel to question them first, is to require this as the normal procedure.
- Evidence: `party_position` cue `submitted` at chunk `4168246` offsets `141-150`; context: [118] To illustrate, the applicants point to the case of applicant Gutierrez Trujillo (IMM-2709-05) in which a psychological report had been submitted to the Board indicating that he was suffering from post-traumatic stress that could affect his ability to testify.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168246` offsets `305-313`; context: The Board Member did not refer to this evidence in making his determination that the Guideline 7 order should be maintained.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4168246` offsets `427-433`; context: The applicants submit that fairness cannot be ensured by a case-by-case determination of the order of questioning if such evidence can be readily discounted or overlooked.
- Evidence: `party_position` cue `submits` at chunk `4168247` offsets `21-28`; context: [119] The respondent submits that the evidence indicates that the manner in which vulnerable claimants are questioned matters much more than who questions them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168247` offsets `38-46`; context: [119] The respondent submits that the evidence indicates that the manner in which vulnerable claimants are questioned matters much more than who questions them.

#### 2044:9:subtheme:23 · paragraphs 120-123

- Raw key terms: `board, applicants, counsel, evidence, member, questioning, additional, appropriate`
- Display key terms: `questioning, additional, appropriate`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: questioning, additional, appropriate Position/evidence statements: [122] The applicants submit that while a Board member can and should ask questions to clarify matters that arise in the course of a hearing, it is not appropriate for the member to take on the role of counsel or the RPO  Rule/authority context: Justice Stone referred to the principles respecting judicial intervention in hearings and concluded that the questioning had remained within the bounds of propriety. Evidence spans paragraphs 120-123. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168248` offsets `454-462`; context: It is not every case that would require counsel to question first and I am satisfied from the additional evidence filed in these proceedings that members can and do make appropriate decisions to change the order of questioning when presented with a request and supporting information.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168248` offsets `132-140`; context: [120] There is considerable strength to the applicants’ argument that vulnerable claimants require greater care in presenting their evidence and that may well mean that counsel should be permitted to assist their clients by questioning them first, but I am not persuaded that this cannot be accommodated on a case-by-case basis with prior notice to the Board that a change in the order may be required.
- Evidence: `counterargument_limitation` cue `but` at chunk `4168248` offsets `248-251`; context: [120] There is considerable strength to the applicants’ argument that vulnerable claimants require greater care in presenting their evidence and that may well mean that counsel should be permitted to assist their clients by questioning them first, but I am not persuaded that this cannot be accommodated on a case-by-case basis with prior notice to the Board that a change in the order may be required.
- Evidence: `party_position` cue `submit` at chunk `4168250` offsets `21-27`; context: [122] The applicants submit that while a Board member can and should ask questions to clarify matters that arise in the course of a hearing, it is not appropriate for the member to take on the role of counsel or the RPO and conduct an examination and/or cross-examination of a refugee claimant.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168250` offsets `372-380`; context: The member should remain out of the arena in order to impartially assess the evidence presented in the course of the hearing and intervene only when necessary to clarify or gather evidence necessary to the determination if that evidence has not been elicited by counsel or the RPO.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168251` offsets `486-494`; context: ” This arose in the context of extensive questioning by the Member after the evidence of the claimant had already been elicited by counsel and the refugee hearing officer.
- Evidence: `governing_rule` cue `principles` at chunk `4168251` offsets `611-621`; context: Justice Stone referred to the principles respecting judicial intervention in hearings and concluded that the questioning had remained within the bounds of propriety.

#### 2044:9:subtheme:24 · paragraphs 124-126

- Raw key terms: `justice, claimant, claimants, counsel, evidence, examination-in-chief, fairness, form`
- Display key terms: `justice, examination-in-chief, fairness, form`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: justice, examination-in-chief, fairness, form Position/evidence statements: [124] The question was raised in Rajaratnam by the Court on its own motion and does not appear to have been fully argued by the parties. | [125] Some of the applicants have submitted that an additional factor in determining the content of the duty of fairness in refugee hearings should be the short time allowed for the preparation of the claimants Personal  Rule/authority context: Moreover it occurred in the context of proceedings under the former legislation and the order of questioning was not in issue. Application context: This is particularly so because of the central role that credibility determinations play in refugee proceedings. Operative outcome context: [125] Some of the applicants have submitted that an additional factor in determining the content of the duty of fairness in refugee hearings should be the short time allowed for the preparation of the claimants Personal  Evidence spans paragraphs 124-126. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168252` offsets `10-18`; context: [124] The question was raised in Rajaratnam by the Court on its own motion and does not appear to have been fully argued by the parties.
- Evidence: `party_position` cue `argued` at chunk `4168252` offsets `114-120`; context: [124] The question was raised in Rajaratnam by the Court on its own motion and does not appear to have been fully argued by the parties.
- Evidence: `governing_rule` cue `under` at chunk `4168252` offsets `188-193`; context: Moreover it occurred in the context of proceedings under the former legislation and the order of questioning was not in issue.
- Evidence: `party_position` cue `submitted` at chunk `4168253` offsets `34-43`; context: [125] Some of the applicants have submitted that an additional factor in determining the content of the duty of fairness in refugee hearings should be the short time allowed for the preparation of the claimants Personal Information Form (PIF).
- Evidence: `evidence_fact` cue `evidence` at chunk `4168253` offsets `836-844`; context: Since natural justice requires that credibility be assessed primarily on the basis of viva voce evidence, it follows that presentation of the PIF is not an adequate substitution for an examination-in-chief, the applicants submit.
- Evidence: `reasoning_application` cue `because` at chunk `4168253` offsets `651-658`; context: This is particularly so because of the central role that credibility determinations play in refugee proceedings.
- Evidence: `disposition` cue `allowed` at chunk `4168253` offsets `166-173`; context: [125] Some of the applicants have submitted that an additional factor in determining the content of the duty of fairness in refugee hearings should be the short time allowed for the preparation of the claimants Personal Information Form (PIF).
- Evidence: `party_position` cue `submit` at chunk `4168254` offsets `138-144`; context: They may also submit documentary evidence, make further written submissions before the hearing, make oral representations at the hearing and may have the opportunity to subsequently file further submissions.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168254` offsets `157-165`; context: They may also submit documentary evidence, make further written submissions before the hearing, make oral representations at the hearing and may have the opportunity to subsequently file further submissions.

#### 2044:9:subtheme:25 · paragraphs 127-128

- Raw key terms: `counsel, guideline, justice, opportunity, agree, applicant, applicants, assistance`
- Display key terms: `guideline, justice, opportunity, agree, assistance`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: guideline, justice, opportunity, agree, assistance Evidence spans paragraphs 127-128. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168255` offsets `264-272`; context: [127] I have no difficulty, after considering the Baker factors and the further factors submitted by the applicants, in deciding that it has not been established that natural justice requires that counsel for a refugee claimant be provided with the opportunity to question the claimant first in order for the claimant to have a meaningful opportunity to present his or her case fully and fairly, or that the Guideline results in denial of the effective assistance of counsel.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168256` offsets `142-150`; context: [128] I agree with the conclusion reached by Justice Blanchard that the opportunity for the applicant to make written submissions and provide evidence to the Board, to have an oral hearing with the participation of counsel, and to make oral submissions, satisfies the requirements of the participatory rights required by the duty of fairness and that Guideline 7 does not, in itself, breach that duty.

#### 2044:9:subtheme:26 · paragraphs 129-130

- Raw key terms: `ainsley, commission, corporation, court, financial, ontario, policy, regulatory`
- Display key terms: `ainsley, commission, corporation, financial, ontario, policy, regulatory`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: ainsley, commission, corporation, financial, ontario, policy, regulatory Evidence spans paragraphs 129-130. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168257` offsets `58-63`; context: [129] A convenient starting point for an analysis of this issue is the decision of the Ontario Court of Appeal in Ainsley Financial Corporation et al.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168258` offsets `239-247`; context: [130] At the trial level, the Court in Ainsley found the statement to be mandatory and regulatory in nature based on three factors: (1) the language of the policy; (2) the practical effect of failing to comply with the policy; and (3) the evidence with respect to the expectations of the Commission and staff regarding the implementation of the policy: see Ainsley Financial Corporation et al.

#### 2044:9:subtheme:27 · paragraphs 131-135

- Raw key terms: `case, circumstances, discretion, guideline, justice, language, mandatory, appeal`
- Display key terms: `case, circumstances, discretion, guideline, justice, language, mandatory`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: case, circumstances, discretion, guideline, justice, language, mandatory Rule/authority context: Such fettering, in Justice Blanchard’s view, constitutes undue influence upon the member and violates the principles of procedural fairness. Application context: The Court of Appeal concluded, at paragraphs 74-77, that the policy fettered the discretion of visa officers because of the mandatory nature of the language used, there was no indication that the officers had a duty to c | In the circumstances of this case, the balancing of these interests, essentially because of the mandatory language used in Guideline 7, results in the interests of consistency outweighing the adjudicative independence of Operative outcome context: The Court of Appeal concluded, at paragraphs 74-77, that the policy fettered the discretion of visa officers because of the mandatory nature of the language used, there was no indication that the officers had a duty to c Evidence spans paragraphs 131-135. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168259` offsets `120-127`; context: [131] In upholding that decision, the Court of Appeal held that the two factors of particular importance in determining whether a guideline has “crossed the Rubicon” dividing the not always clear line between guideline and regulation are the language of the statement and the threat of coercive action.
- Evidence: `issue` cue `question` at chunk `4168260` offsets `732-740`; context: The Court of Appeal concluded, at paragraphs 74-77, that the policy fettered the discretion of visa officers because of the mandatory nature of the language used, there was no indication that the officers had a duty to consider the particular circumstances of each case, the policy gave no guidance to the officers as to how to exercise that discretion other than to deny the attendance of counsel in each case, the objective evidence indicated that the officer in question treated the policy as fettering his discretion and the respondent had offered no evidence to indicate that counsel had ever been allowed to attend.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168260` offsets `693-701`; context: The Court of Appeal concluded, at paragraphs 74-77, that the policy fettered the discretion of visa officers because of the mandatory nature of the language used, there was no indication that the officers had a duty to consider the particular circumstances of each case, the policy gave no guidance to the officers as to how to exercise that discretion other than to deny the attendance of counsel in each case, the objective evidence indicated that the officer in question treated the policy as fettering his discretion and the respondent had offered no evidence to indicate that counsel had ever been allowed to attend.
- Evidence: `reasoning_application` cue `because` at chunk `4168260` offsets `376-383`; context: The Court of Appeal concluded, at paragraphs 74-77, that the policy fettered the discretion of visa officers because of the mandatory nature of the language used, there was no indication that the officers had a duty to consider the particular circumstances of each case, the policy gave no guidance to the officers as to how to exercise that discretion other than to deny the attendance of counsel in each case, the objective evidence indicated that the officer in question treated the policy as fettering his discretion and the respondent had offered no evidence to indicate that counsel had ever been allowed to attend.
- Evidence: `disposition` cue `allowed` at chunk `4168260` offsets `870-877`; context: The Court of Appeal concluded, at paragraphs 74-77, that the policy fettered the discretion of visa officers because of the mandatory nature of the language used, there was no indication that the officers had a duty to consider the particular circumstances of each case, the policy gave no guidance to the officers as to how to exercise that discretion other than to deny the attendance of counsel in each case, the objective evidence indicated that the officer in question treated the policy as fettering his discretion and the respondent had offered no evidence to indicate that counsel had ever been allowed to attend.
- Evidence: `evidence_fact` cue `determined that` at chunk `4168261` offsets `40-55`; context: [133] In Thamotharem, Justice Blanchard determined that the implementation of Guideline 7 had the effect of fettering a Board member’s discretion to decide the most appropriate process to follow in the circumstances of each case.
- Evidence: `governing_rule` cue `principles` at chunk `4168261` offsets `492-502`; context: Such fettering, in Justice Blanchard’s view, constitutes undue influence upon the member and violates the principles of procedural fairness.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168262` offsets `221-229`; context: [134] The factors relied upon by Justice Blanchard in arriving at this conclusion are set out in paragraph 135 of his reasons which I reproduce below in part:
In the instant case, I am satisfied that there is significant evidence that the IRB made known to its members that they are expected to comply with the guideline save in exceptional cases.
- Evidence: `reasoning_application` cue `because` at chunk `4168262` offsets `985-992`; context: In the circumstances of this case, the balancing of these interests, essentially because of the mandatory language used in Guideline 7, results in the interests of consistency outweighing the adjudicative independence of the Board Member.
- Evidence: `counterargument_limitation` cue `but` at chunk `4168262` offsets `427-430`; context: The problem is not so much with the expression of this expectation by the IRB, but rather its combination with a number of factors: the monitoring and expectation of compliance, the evidence of compliance, and especially the mandatory language of Guideline 7.

#### 2044:9:subtheme:28 · paragraphs 136-138

- Raw key terms: `court, thamotharem, concluded, decisions, fettering, guideline, order, reasons`
- Display key terms: `thamotharem, concluded, decisions, fettering, guideline, order`
- Argument roles: `disposition, evidence_fact, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position Display terms: thamotharem, concluded, decisions, fettering, guideline, order Position/evidence statements: The Court gave counsel the opportunity to submit written submissions once the Thamotharem reasons were available. Operative outcome context: Whether a claimant will be granted the right to proceed first will depend on the facts of each case. Evidence spans paragraphs 136-138. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168264` offsets `183-191`; context: The Court declined to do so, noting that the two decisions were not in conflict on the central question of whether Guideline 7, in itself, breaches procedural fairness.
- Evidence: `issue` cue `Whether` at chunk `4168265` offsets `641-648`; context: Whether a claimant will be granted the right to proceed first will depend on the facts of each case.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168265` offsets `129-137`; context: [137] Contrary to what may have been suggested in Jin, fettering was argued and considered in Zaki, albeit without the extensive evidence and submissions that were before the Court in Thamotharem.
- Evidence: `disposition` cue `granted` at chunk `4168265` offsets `668-675`; context: Whether a claimant will be granted the right to proceed first will depend on the facts of each case.
- Evidence: `party_position` cue `submit` at chunk `4168266` offsets `144-150`; context: The Court gave counsel the opportunity to submit written submissions once the Thamotharem reasons were available.

#### 2044:9:subtheme:29 · paragraphs 139-146

- Raw key terms: `discretion, guideline, board, members, evidence, order, questioning, respondent`
- Display key terms: `discretion, guideline, members, order, questioning`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: discretion, guideline, members, order, questioning Position/evidence statements: The issue, the respondent submits, is whether the working and implementation of Guideline 7 has crossed the line between a non-mandatory guideline and a mandatory pronouncement having the same effect as a statutory instr | Indeed the applicants have submitted, as discussed above, that had he had a record before him similar to certain of those in these proceedings, he may have found that a higher degree of procedural protection was called f Rule/authority context: The issue, the respondent submits, is whether the working and implementation of Guideline 7 has crossed the line between a non-mandatory guideline and a mandatory pronouncement having the same effect as a statutory instr | [144] In urging me to depart from these conclusions, the respondent submits that the language of the Guideline has to be read as permissive rather than mandatory in keeping with the principles established in Maple Lodge  Application context: [142] The finding in Thamotharem that members’ discretion is fettered turns on the language of the Guideline itself and the extrinsic evidence about how it could be interpreted and applied by RPD members and not on the f | Further, while paragraph 23 allowed for the Board member to vary the order of questioning, the basis for the finding by the Court in Zaki that it was sufficiently flexible, Justice Blanchard found that it set a high thre Operative outcome context: Further, while paragraph 23 allowed for the Board member to vary the order of questioning, the basis for the finding by the Court in Zaki that it was sufficiently flexible, Justice Blanchard found that it set a high thre | [146] While the attachments to the Kiyani affidavit provide only a selective picture of the response of Board members to Guideline 7, they support the respondent’s contention that the discretion of Board members is not f Evidence spans paragraphs 139-146. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168267` offsets `160-165`; context: The issue, the respondent submits, is whether the working and implementation of Guideline 7 has crossed the line between a non-mandatory guideline and a mandatory pronouncement having the same effect as a statutory instrument, such as a rule made by the Chairperson under the authority of IRPA s.
- Evidence: `party_position` cue `submits` at chunk `4168267` offsets `182-189`; context: The issue, the respondent submits, is whether the working and implementation of Guideline 7 has crossed the line between a non-mandatory guideline and a mandatory pronouncement having the same effect as a statutory instrument, such as a rule made by the Chairperson under the authority of IRPA s.
- Evidence: `governing_rule` cue `under` at chunk `4168267` offsets `422-427`; context: The issue, the respondent submits, is whether the working and implementation of Guideline 7 has crossed the line between a non-mandatory guideline and a mandatory pronouncement having the same effect as a statutory instrument, such as a rule made by the Chairperson under the authority of IRPA s.
- Evidence: `party_position` cue `submitted` at chunk `4168268` offsets `396-405`; context: Indeed the applicants have submitted, as discussed above, that had he had a record before him similar to certain of those in these proceedings, he may have found that a higher degree of procedural protection was called for.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168268` offsets `160-168`; context: [140] I think it fair to say that my colleague Justice Blanchard relied less upon the factual history of the matter before him in Thamotharem and more upon the evidence relating to the form and content of the Guideline and the manner in which it was implemented in reaching his conclusion that Board Members’ discretion was fettered by the imposition of the Guideline.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168269` offsets `50-58`; context: [141] The respondent points out that there was no evidence on the record in Thamotharem of a refusal by the Board Member to exercise his discretion to vary the order of questioning due to the claimant’s particular circumstances, no evidence of any particular vulnerability that would make testimony difficult, no argument of improper questioning and no request to vary the order outside the assertion of an absolute right to an examination-in-chief.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168270` offsets `134-142`; context: [142] The finding in Thamotharem that members’ discretion is fettered turns on the language of the Guideline itself and the extrinsic evidence about how it could be interpreted and applied by RPD members and not on the facts of the particular case.
- Evidence: `reasoning_application` cue `applied` at chunk `4168270` offsets `181-188`; context: [142] The finding in Thamotharem that members’ discretion is fettered turns on the language of the Guideline itself and the extrinsic evidence about how it could be interpreted and applied by RPD members and not on the facts of the particular case.
- Evidence: `evidence_fact` cue `found that` at chunk `4168271` offsets `57-67`; context: [143] At paragraph 119 of his reasons, Justice Blanchard found that the language of Guideline 7 left little doubt that the thrust of the Guideline indicates to Board members a mandatory process rather than a recommended but optional process: paragraph 19 provides that the standard practice will be for the RPO to begin, and if no RPO is participating at the hearing, the Board member will begin.
- Evidence: `reasoning_application` cue `apply` at chunk `4168271` offsets `770-775`; context: Further, while paragraph 23 allowed for the Board member to vary the order of questioning, the basis for the finding by the Court in Zaki that it was sufficiently flexible, Justice Blanchard found that it set a high threshold for what constitutes “exceptional circumstances”: the claimant must be “severely” disturbed and the child must be “very” young for an exception to apply.
- Evidence: `counterargument_limitation` cue `but` at chunk `4168271` offsets `220-223`; context: [143] At paragraph 119 of his reasons, Justice Blanchard found that the language of Guideline 7 left little doubt that the thrust of the Guideline indicates to Board members a mandatory process rather than a recommended but optional process: paragraph 19 provides that the standard practice will be for the RPO to begin, and if no RPO is participating at the hearing, the Board member will begin.
- Evidence: `disposition` cue `allowed` at chunk `4168271` offsets `425-432`; context: Further, while paragraph 23 allowed for the Board member to vary the order of questioning, the basis for the finding by the Court in Zaki that it was sufficiently flexible, Justice Blanchard found that it set a high threshold for what constitutes “exceptional circumstances”: the claimant must be “severely” disturbed and the child must be “very” young for an exception to apply.
- Evidence: `party_position` cue `submits` at chunk `4168272` offsets `68-75`; context: [144] In urging me to depart from these conclusions, the respondent submits that the language of the Guideline has to be read as permissive rather than mandatory in keeping with the principles established in Maple Lodge Farms Ltd.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168272` offsets `479-487`; context: Here, the respondent submits, the contextual evidence including the Board’s policy on the use of guidelines, indicate that members retain discretion to vary the order of questioning where they deem it appropriate.
- Evidence: `governing_rule` cue `principles` at chunk `4168272` offsets `182-192`; context: [144] In urging me to depart from these conclusions, the respondent submits that the language of the Guideline has to be read as permissive rather than mandatory in keeping with the principles established in Maple Lodge Farms Ltd.
- Evidence: `party_position` cue `submits` at chunk `4168273` offsets `203-210`; context: [145] The respondent relies on the new evidence attached to the affidavit of Asad Kiyani, some forty decisions and excerpts of transcripts from hearings before various RPD members, which, the respondent submits, demonstrate that the conclusion that members’ discretion has been fettered is not shared by the members themselves.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168273` offsets `39-47`; context: [145] The respondent relies on the new evidence attached to the affidavit of Asad Kiyani, some forty decisions and excerpts of transcripts from hearings before various RPD members, which, the respondent submits, demonstrate that the conclusion that members’ discretion has been fettered is not shared by the members themselves.
- Evidence: `counterargument_limitation` cue `although` at chunk `4168273` offsets `449-457`; context: I note that Justice Blanchard had evidence before him of Board members deviating from the Guideline order of questioning although the evidence was not as extensive as that filed by the respondent in these proceedings.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4168274` offsets `42-51`; context: [146] While the attachments to the Kiyani affidavit provide only a selective picture of the response of Board members to Guideline 7, they support the respondent’s contention that the discretion of Board members is not fettered by Guideline 7 and that members are not restricting themselves to the exceptional examples set out in paragraph 23 of Guideline 7 as an exhaustive list of instances in which the order of questioning should be varied as Justice Blanchard feared.
- Evidence: `disposition` cue `varied` at chunk `4168274` offsets `437-443`; context: [146] While the attachments to the Kiyani affidavit provide only a selective picture of the response of Board members to Guideline 7, they support the respondent’s contention that the discretion of Board members is not fettered by Guideline 7 and that members are not restricting themselves to the exceptional examples set out in paragraph 23 of Guideline 7 as an exhaustive list of instances in which the order of questioning should be varied as Justice Blanchard feared.

#### 2044:9:subtheme:30 · paragraphs 147-150

- Raw key terms: `member, exhibit, guideline, hearing, indications, order, procedure, questioning`
- Display key terms: `exhibit, guideline, hearing, indications, order, procedure, questioning`
- Argument roles: `counterargument_limitation, disposition, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, issue, reasoning_application Display terms: exhibit, guideline, hearing, indications, order, procedure, questioning Application context: [150] In exhibit A-6, the Member said she was not fully persuaded that changing the order of questioning was necessary because she was “very experienced in dealing with claims of gender and gender violence” but proceeded Operative outcome context: [147] In each of the cases, the Member considers the applicability of the Guideline in the circumstances and then decides whether the order of questioning should be varied. Evidence spans paragraphs 147-150. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168275` offsets `122-129`; context: [147] In each of the cases, the Member considers the applicability of the Guideline in the circumstances and then decides whether the order of questioning should be varied.
- Evidence: `disposition` cue `varied` at chunk `4168275` offsets `165-171`; context: [147] In each of the cases, the Member considers the applicability of the Guideline in the circumstances and then decides whether the order of questioning should be varied.
- Evidence: `reasoning_application` cue `because` at chunk `4168278` offsets `119-126`; context: [150] In exhibit A-6, the Member said she was not fully persuaded that changing the order of questioning was necessary because she was “very experienced in dealing with claims of gender and gender violence” but proceeded to grant the exception.
- Evidence: `counterargument_limitation` cue `but` at chunk `4168278` offsets `207-210`; context: [150] In exhibit A-6, the Member said she was not fully persuaded that changing the order of questioning was necessary because she was “very experienced in dealing with claims of gender and gender violence” but proceeded to grant the exception.

#### 2044:9:subtheme:31 · paragraphs 151-152

- Raw key terms: `cases, clear, each, exhibits, guideline, implementation, member, reasons`
- Display key terms: `cases, clear, each, exhibits, guideline, implementation`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: cases, clear, each, exhibits, guideline, implementation Application context: Steve Ellis, each set of reasons includes an “Appendix A” that is a 38 page analysis of why the Guideline in his view violates natural justice and why he therefore refuses to apply it. Evidence spans paragraphs 151-152. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168279` offsets `214-221`; context: Although it is not clear from his reasons whether the Member considered whether the applicant before him fell within the paragraph 23 examples, a review of the Tribunal Record for each of these cases (which are part of the consolidated action) shows that the applicant’s counsel in each case did not raise a specific objection to the implementation of Guideline 7 based on the circumstances of the particular claimant.
- Evidence: `evidence_fact` cue `Record` at chunk `4168279` offsets `341-347`; context: Although it is not clear from his reasons whether the Member considered whether the applicant before him fell within the paragraph 23 examples, a review of the Tribunal Record for each of these cases (which are part of the consolidated action) shows that the applicant’s counsel in each case did not raise a specific objection to the implementation of Guideline 7 based on the circumstances of the particular claimant.
- Evidence: `reasoning_application` cue `therefore` at chunk `4168280` offsets `289-298`; context: Steve Ellis, each set of reasons includes an “Appendix A” that is a 38 page analysis of why the Guideline in his view violates natural justice and why he therefore refuses to apply it.

#### 2044:9:subtheme:32 · paragraphs 153-157

- Raw key terms: `member, questioning, board, circumstances, counsel, order, affidavit, attached`
- Display key terms: `questioning, circumstances, order, affidavit, attached`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: questioning, circumstances, order, affidavit, attached Position/evidence statements: [153] There are several decisions in which counsel submitted evidence of pyschological or emotional fraility, or the Board was otherwise aware of the condition, and the Member allowed the order of questioning to be rever Application context: [155] In Exhibit B-7, while the Member refers to “exceptional circumstances” she accedes to a request to change the order of questioning because counsel indicated that the claimant, an 18 year old Iranian national, was a | [156] These examples indicate to me that members understand that the illustrations of exceptional circumstances provided by the Guideline are simply that and that members feel free to apply them broadly. Operative outcome context: [153] There are several decisions in which counsel submitted evidence of pyschological or emotional fraility, or the Board was otherwise aware of the condition, and the Member allowed the order of questioning to be rever | [154] In the cases attached as Exhibits C-7 and C-8 to the Kiyani affidavit, the Board Member states that the order of questioning is being varied on the Member’s own motion, rather than upon application by the claimant, Evidence spans paragraphs 153-157. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168281` offsets `362-370`; context: In others, a RPO was not present at the hearing and the Member opted to have counsel question first: B-9, C-9, C-15.
- Evidence: `party_position` cue `submitted` at chunk `4168281` offsets `51-60`; context: [153] There are several decisions in which counsel submitted evidence of pyschological or emotional fraility, or the Board was otherwise aware of the condition, and the Member allowed the order of questioning to be reversed: B-2, B-3, B-5, B-8, B-11, B-12, C-2, C-3, C-4, C-6.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168281` offsets `61-69`; context: [153] There are several decisions in which counsel submitted evidence of pyschological or emotional fraility, or the Board was otherwise aware of the condition, and the Member allowed the order of questioning to be reversed: B-2, B-3, B-5, B-8, B-11, B-12, C-2, C-3, C-4, C-6.
- Evidence: `disposition` cue `allowed` at chunk `4168281` offsets `176-183`; context: [153] There are several decisions in which counsel submitted evidence of pyschological or emotional fraility, or the Board was otherwise aware of the condition, and the Member allowed the order of questioning to be reversed: B-2, B-3, B-5, B-8, B-11, B-12, C-2, C-3, C-4, C-6.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4168282` offsets `66-75`; context: [154] In the cases attached as Exhibits C-7 and C-8 to the Kiyani affidavit, the Board Member states that the order of questioning is being varied on the Member’s own motion, rather than upon application by the claimant, after having taken into account the particular circumstances of the claimant.
- Evidence: `disposition` cue `varied` at chunk `4168282` offsets `140-146`; context: [154] In the cases attached as Exhibits C-7 and C-8 to the Kiyani affidavit, the Board Member states that the order of questioning is being varied on the Member’s own motion, rather than upon application by the claimant, after having taken into account the particular circumstances of the claimant.
- Evidence: `reasoning_application` cue `because` at chunk `4168283` offsets `137-144`; context: [155] In Exhibit B-7, while the Member refers to “exceptional circumstances” she accedes to a request to change the order of questioning because counsel indicated that the claimant, an 18 year old Iranian national, was accustomed to different institutions “…and because counsel was Iranian and knowledgeable of Iranian culture…”.
- Evidence: `reasoning_application` cue `apply` at chunk `4168284` offsets `184-189`; context: [156] These examples indicate to me that members understand that the illustrations of exceptional circumstances provided by the Guideline are simply that and that members feel free to apply them broadly.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168285` offsets `33-41`; context: [157] In contrast, the strongest evidence put forward by the applicants is an excerpt from the Board’s decision in Baskaran (Board File: TA1-07530), attached to Mr.

#### 2044:9:subtheme:33 · paragraphs 158-168

- Raw key terms: `guideline, members, board, evidence, chairperson, member, case, discretion`
- Display key terms: `guideline, members, chairperson, case, discretion`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: guideline, members, chairperson, case, discretion Rule/authority context: [158] The applicants point to this excerpt as indicating that members would feel under pressure to conform to the practice outlined in the Guideline, out of loyalty to the institution and, in some cases, from a lack of c | decision has not been identified by the Chairperson as a jurisprudential guide nor does it fall within the category of “persuasive decision”, which the Deputy Chair, Refugee Protection Division may designate under a poli Application context: [159] Professor Galloway’s evidence as a former Board Member also lends support to the applicants’ contentions as to how the Guideline would be interpreted and applied by RPD members. | Aterman also expressed the view on cross-examination that members exercise their judgment with respect to how and when to apply the Guideline bearing in mind the particular circumstances of any given case (September 15,  Evidence spans paragraphs 158-168. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `under` at chunk `4168286` offsets `81-86`; context: [158] The applicants point to this excerpt as indicating that members would feel under pressure to conform to the practice outlined in the Guideline, out of loyalty to the institution and, in some cases, from a lack of confidence in their own discretion and ability to make independent decisions as to the correct procedure to follow.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168287` offsets `27-35`; context: [159] Professor Galloway’s evidence as a former Board Member also lends support to the applicants’ contentions as to how the Guideline would be interpreted and applied by RPD members.
- Evidence: `reasoning_application` cue `applied` at chunk `4168287` offsets `160-167`; context: [159] Professor Galloway’s evidence as a former Board Member also lends support to the applicants’ contentions as to how the Guideline would be interpreted and applied by RPD members.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168287` offsets `184-191`; context: However, he had no direct experience with the implementation of the Guideline and his evidence as to how the Guideline would be interpreted and applied by members was, while helpful, largely speculative.
- Evidence: `evidence_fact` cue `testimony` at chunk `4168288` offsets `66-75`; context: [160] The respondent asks the Court to give greater weight to the testimony of Mr.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4168289` offsets `376-385`; context: Those comments are supported by the examples of decisions deviating from the Guideline that are attached to the Kiyani affidavit.
- Evidence: `reasoning_application` cue `apply` at chunk `4168289` offsets `132-137`; context: Aterman also expressed the view on cross-examination that members exercise their judgment with respect to how and when to apply the Guideline bearing in mind the particular circumstances of any given case (September 15, 2006 transcript at 79-80).
- Evidence: `evidence_fact` cue `evidence` at chunk `4168290` offsets `466-474`; context: However, the distribution of the decision is not in my view evidence of fettering so long as members did not consider themselves bound to follow Member Brennenstuhl’s conclusions.
- Evidence: `governing_rule` cue `under` at chunk `4168290` offsets `860-865`; context: decision has not been identified by the Chairperson as a jurisprudential guide nor does it fall within the category of “persuasive decision”, which the Deputy Chair, Refugee Protection Division may designate under a policy adopted by the Board as “models of sound reasoning” which members are encouraged to adopt.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168290` offsets `406-413`; context: However, the distribution of the decision is not in my view evidence of fettering so long as members did not consider themselves bound to follow Member Brennenstuhl’s conclusions.
- Evidence: `governing_rule` cue `under` at chunk `4168291` offsets `420-425`; context: But that does not necessarily lead to the conclusion that members consider themselves bound to apply it as if it were legislation, a regulation or a formal rule made under the Chairperson’s authority.
- Evidence: `reasoning_application` cue `apply` at chunk `4168291` offsets `349-354`; context: But that does not necessarily lead to the conclusion that members consider themselves bound to apply it as if it were legislation, a regulation or a formal rule made under the Chairperson’s authority.
- Evidence: `counterargument_limitation` cue `But` at chunk `4168291` offsets `254-257`; context: But that does not necessarily lead to the conclusion that members consider themselves bound to apply it as if it were legislation, a regulation or a formal rule made under the Chairperson’s authority.
- Evidence: `reasoning_application` cue `because` at chunk `4168292` offsets `86-93`; context: observed in Ainsley, guidelines are not rendered invalid merely because they regulate the conduct of those to whom they are directed.
- Evidence: `evidence_fact` cue `record` at chunk `4168293` offsets `25-31`; context: [165] On the face of the record in this case, the evidence does not in my view support a finding of fettering similar to that considered by the courts in Ainsley and Ha.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168294` offsets `187-195`; context: And further, unlike Ha, the evidence before me indicates that members have chosen to disregard the “standard practice” when they deemed it necessary and for reasons that go beyond the type of exceptional circumstance described in paragraph 23.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168295` offsets `179-187`; context: There is no evidence on the record to suggest that the Chairperson has threatened to, or has in fact, sanctioned any Board member for non-compliance with Guideline 7.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168296` offsets `10-18`; context: [168] The evidence indicates that the Board was monitoring compliance with the implementation of the Chairperson’s guidelines through a voluntary reporting system employing “Hearing Information Sheets”.

#### 2044:9:subtheme:34 · paragraphs 169-172

- Raw key terms: `evidence, applied, apply, guideline, members, application, board, circumstances`
- Display key terms: `applied, apply, guideline, members, circumstances`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: applied, apply, guideline, members, circumstances Application context: Aterman conceded that managers were required to monitor individual members’ compliance with the guidelines but, again, there is no evidence of any consequences flowing to those who chose to ignore or to not strictly appl | As I read the evidence, this provision applied to all of the guidelines and there is no evidence of any member ever receiving a poor performance appraisal for failing to apply Guideline 7. Evidence spans paragraphs 169-172. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168297` offsets `70-77`; context: [169] There is also evidence of e-mails from the Vice-Chair inquiring whether members were applying the guidelines and that members were asked to explain whether there were exceptional circumstances or other reasons for not following them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168297` offsets `20-28`; context: [169] There is also evidence of e-mails from the Vice-Chair inquiring whether members were applying the guidelines and that members were asked to explain whether there were exceptional circumstances or other reasons for not following them.
- Evidence: `reasoning_application` cue `apply` at chunk `4168297` offsets `460-465`; context: Aterman conceded that managers were required to monitor individual members’ compliance with the guidelines but, again, there is no evidence of any consequences flowing to those who chose to ignore or to not strictly apply them.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168298` offsets `201-209`; context: As I read the evidence, this provision applied to all of the guidelines and there is no evidence of any member ever receiving a poor performance appraisal for failing to apply Guideline 7.
- Evidence: `reasoning_application` cue `applied` at chunk `4168298` offsets `226-233`; context: As I read the evidence, this provision applied to all of the guidelines and there is no evidence of any member ever receiving a poor performance appraisal for failing to apply Guideline 7.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168299` offsets `33-41`; context: [171] There is considerably more evidence before me as to the manner in which Guideline 7 is actually being applied by RPD members than there was before my colleague in Thamotharem.
- Evidence: `reasoning_application` cue `applied` at chunk `4168299` offsets `108-115`; context: [171] There is considerably more evidence before me as to the manner in which Guideline 7 is actually being applied by RPD members than there was before my colleague in Thamotharem.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168300` offsets `350-358`; context: ), the application of a policy guideline may amount to an unlawful fettering of a Board's discretion, if applied without due consideration to the evidence and submissions in a particular case.
- Evidence: `reasoning_application` cue `applied` at chunk `4168300` offsets `309-316`; context: ), the application of a policy guideline may amount to an unlawful fettering of a Board's discretion, if applied without due consideration to the evidence and submissions in a particular case.

#### 2044:9:subtheme:35 · paragraphs 173-174

- Raw key terms: `applicants, argument, board, decisions, guides, identify, jurisprudential, paragraph`
- Display key terms: `argument, decisions, guides, identify, jurisprudential, paragraph`
- Argument roles: `governing_rule, issue, party_position`
- Explanation: Observed roles: governing_rule, issue, party_position Display terms: argument, decisions, guides, identify, jurisprudential, paragraph Position/evidence statements: [173] The applicants submit that Guideline 7 is ultra vires or beyond the scope of the Chairperson’s statutory authority to issue guidelines. | [174] The applicants submit that the guideline-making power under paragraph 159 (1) (h) is only to be used to identify decisions of the Board which may be used as jurisprudential guides. Rule/authority context: [174] The applicants submit that the guideline-making power under paragraph 159 (1) (h) is only to be used to identify decisions of the Board which may be used as jurisprudential guides. Evidence spans paragraphs 173-174. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168301` offsets `124-129`; context: [173] The applicants submit that Guideline 7 is ultra vires or beyond the scope of the Chairperson’s statutory authority to issue guidelines.
- Evidence: `party_position` cue `submit` at chunk `4168301` offsets `21-27`; context: [173] The applicants submit that Guideline 7 is ultra vires or beyond the scope of the Chairperson’s statutory authority to issue guidelines.
- Evidence: `party_position` cue `submit` at chunk `4168302` offsets `21-27`; context: [174] The applicants submit that the guideline-making power under paragraph 159 (1) (h) is only to be used to identify decisions of the Board which may be used as jurisprudential guides.
- Evidence: `governing_rule` cue `under` at chunk `4168302` offsets `60-65`; context: [174] The applicants submit that the guideline-making power under paragraph 159 (1) (h) is only to be used to identify decisions of the Board which may be used as jurisprudential guides.

#### 2044:9:subtheme:36 · paragraphs 175-179

- Raw key terms: `guidelines, policy, action, authority, board, canada, chairperson, defined`
- Display key terms: `guidelines, policy, action, authority, chairperson, defined`
- Argument roles: `counterargument_limitation, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue, party_position Display terms: guidelines, policy, action, authority, chairperson, defined Position/evidence statements: [179] The applicants submit that a plain reading of paragraph 159 (1) (h) indicates that the kind of guidelines envisioned are those which facilitate a consistent, economical and sound decision making process. Rule/authority context: [176] The issue before me is whether the Chairperson overstepped the bounds of the authority provided by the statute to issue guidelines and imposed a mandatory rule which required legislative action, or the approval of  | I-23, as they are “made or established…in the execution of a power conferred by or under the authority of an Act”. Evidence spans paragraphs 175-179. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168303` offsets `265-270`; context: The legislative intent from the plain language employed is that the Chairperson is authorized to both issue guidelines and to identify certain decisions of the Board as models for the members to emulate.
- Evidence: `issue` cue `issue` at chunk `4168304` offsets `10-15`; context: [176] The issue before me is whether the Chairperson overstepped the bounds of the authority provided by the statute to issue guidelines and imposed a mandatory rule which required legislative action, or the approval of the Governor-in-Council and at least passive acquiescence of both Houses of Parliament under the terms of section 161 of IRPA.
- Evidence: `governing_rule` cue `under` at chunk `4168304` offsets `307-312`; context: [176] The issue before me is whether the Chairperson overstepped the bounds of the authority provided by the statute to issue guidelines and imposed a mandatory rule which required legislative action, or the approval of the Governor-in-Council and at least passive acquiescence of both Houses of Parliament under the terms of section 161 of IRPA.
- Evidence: `governing_rule` cue `under` at chunk `4168305` offsets `179-184`; context: I-23, as they are “made or established…in the execution of a power conferred by or under the authority of an Act”.
- Evidence: `party_position` cue `submit` at chunk `4168307` offsets `21-27`; context: [179] The applicants submit that a plain reading of paragraph 159 (1) (h) indicates that the kind of guidelines envisioned are those which facilitate a consistent, economical and sound decision making process.
- Evidence: `counterargument_limitation` cue `but` at chunk `4168307` offsets `277-280`; context: Guideline 7, they submit, is not about the decision-making process but is concerned with the setting of fundamental procedural norms, and with an attempt to transform the Board from its established role as a quasi-judicial body, as recognized in Singh, to a “Board of Inquiry.

#### 2044:9:subtheme:37 · paragraphs 180-181

- Raw key terms: `applicants, fundamental, order, procedural, proper, questioning, administration, allowed`
- Display key terms: `fundamental, order, procedural, proper, questioning, administration, allowed`
- Argument roles: `disposition, issue, party_position`
- Explanation: Observed roles: disposition, issue, party_position Display terms: fundamental, order, procedural, proper, questioning, administration, allowed Position/evidence statements: [181] Moreover, the applicants submit, changes to procedural norms which seek to alter the very nature of the Board are the proper purview of the legislature and legislation and not of the Board’s administration. Operative outcome context: While the Rules covered complicated procedural issues such as how claims may be allowed without a hearing (Rule 19), and how to proceed with claims involving issues of inadmissibility and exclusion (Rules 23-25), the Rul Evidence spans paragraphs 180-181. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168308` offsets `271-277`; context: While the Rules covered complicated procedural issues such as how claims may be allowed without a hearing (Rule 19), and how to proceed with claims involving issues of inadmissibility and exclusion (Rules 23-25), the Rules also spell out lesser aspects such as the procedure for scheduling hearings (Rule 21) and the appropriate size of paper to be used (Rule 27).
- Evidence: `disposition` cue `allowed` at chunk `4168308` offsets `304-311`; context: While the Rules covered complicated procedural issues such as how claims may be allowed without a hearing (Rule 19), and how to proceed with claims involving issues of inadmissibility and exclusion (Rules 23-25), the Rules also spell out lesser aspects such as the procedure for scheduling hearings (Rule 21) and the appropriate size of paper to be used (Rule 27).
- Evidence: `party_position` cue `submit` at chunk `4168309` offsets `31-37`; context: [181] Moreover, the applicants submit, changes to procedural norms which seek to alter the very nature of the Board are the proper purview of the legislature and legislation and not of the Board’s administration.

#### 2044:9:subtheme:38 · paragraphs 182-183

- Raw key terms: `canada, determine, free, immigration, minister, para, procedures, reason`
- Display key terms: `determine, free, para, procedures, reason`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: determine, free, para, procedures, reason Position/evidence statements: The respondent further argues that the role of the panel is properly characterized as inquisitorial in nature, not adversarial, and therefore a member can lead the inquiry into the claim: Sivasamboo v. Application context: The respondent further argues that the role of the panel is properly characterized as inquisitorial in nature, not adversarial, and therefore a member can lead the inquiry into the claim: Sivasamboo v. Evidence spans paragraphs 182-183. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168310` offsets `93-98`; context: [182] The respondent’s answer is that the Chairperson clearly has the statutory authority to issue guidelines to Board members.
- Evidence: `party_position` cue `argues` at chunk `4168310` offsets `396-402`; context: The respondent further argues that the role of the panel is properly characterized as inquisitorial in nature, not adversarial, and therefore a member can lead the inquiry into the claim: Sivasamboo v.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168310` offsets `242-250`; context: Parliament has legislated that the RPD must hold a hearing and give claimants a reasonable opportunity to present evidence, question witnesses and make representations; however a tribunal is free, within reason, to determine its own procedures.
- Evidence: `reasoning_application` cue `therefore` at chunk `4168310` offsets `505-514`; context: The respondent further argues that the role of the panel is properly characterized as inquisitorial in nature, not adversarial, and therefore a member can lead the inquiry into the claim: Sivasamboo v.
- Evidence: `counterargument_limitation` cue `however` at chunk `4168310` offsets `297-304`; context: Parliament has legislated that the RPD must hold a hearing and give claimants a reasonable opportunity to present evidence, question witnesses and make representations; however a tribunal is free, within reason, to determine its own procedures.

#### 2044:9:subtheme:39 · paragraphs 184-185

- Raw key terms: `approval, authority, board, chairperson, changes, guideline, guidelines, making`
- Display key terms: `approval, authority, chairperson, changes, guideline, guidelines, making`
- Argument roles: `counterargument_limitation, disposition, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, governing_rule, issue Display terms: approval, authority, chairperson, changes, guideline, guidelines, making Rule/authority context: [184] In this instance, Parliament has seen fit to equip the Board with two mechanisms by which to determine its process; the rule making authority under s. Operative outcome context: That process also exposes proposals to greater scrutiny and may well result in revisions or changes before formal approval is granted. Evidence spans paragraphs 184-185. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168312` offsets `181-186`; context: 161 and the authority to issue guidelines and to identify Board decisions as jurisprudential guides under paragraph 159 (1) (h).
- Evidence: `governing_rule` cue `under` at chunk `4168312` offsets `148-153`; context: [184] In this instance, Parliament has seen fit to equip the Board with two mechanisms by which to determine its process; the rule making authority under s.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168313` offsets `469-476`; context: However, I am not persuaded that the Chairperson’s authority to make guidelines is not broad enough to encompass the adoption of a procedure such as the standard order of questioning contemplated by Guideline 7.
- Evidence: `disposition` cue `granted` at chunk `4168313` offsets `299-306`; context: That process also exposes proposals to greater scrutiny and may well result in revisions or changes before formal approval is granted.

#### 2044:9:subtheme:40 · paragraphs 186-189

- Raw key terms: `board, discretion, guideline, mandatory, member, members, rule, apprehension`
- Display key terms: `discretion, guideline, mandatory, members, rule, apprehension`
- Argument roles: `counterargument_limitation, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, party_position, reasoning_application Display terms: discretion, guideline, mandatory, members, rule, apprehension Position/evidence statements: [189] Counsel for the applicant Shurlyn Jones (IMM-1877-05) argued that as a result of the diminishing presence of RPOs in refugee hearings, the role of the Board member is being distorted giving rise to a reasonable app Application context: Accordingly, I do not find that the Guideline operated as a mandatory rule and as such was outside the Chairperson’s authority. Evidence spans paragraphs 186-189. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168314` offsets `78-85`; context: [186] In Thamotharem, Justice Blanchard did not make a specific finding as to whether the Chairperson’s authority was exceeded by Guideline 7.
- Evidence: `counterargument_limitation` cue `however` at chunk `4168314` offsets `153-160`; context: He noted, however, at paragraph 103 of his reasons that while the enactment explicitly authorized the Chairperson to make and issue guidelines to assist members in carrying out their duties, the guidelines cannot be mandatory in the sense that they leave little room for the exercise of discretion by each Board member to conduct a full and proper hearing.
- Evidence: `issue` cue `question` at chunk `4168315` offsets `47-55`; context: [187] Justice Blanchard went on to address the question of whether Guideline 7 presented a recommended non-binding approach to Board members or served as a mandatory pronouncement which fetters the members’ discretion.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4168316` offsets `164-175`; context: Accordingly, I do not find that the Guideline operated as a mandatory rule and as such was outside the Chairperson’s authority.
- Evidence: `party_position` cue `argued` at chunk `4168317` offsets `60-66`; context: [189] Counsel for the applicant Shurlyn Jones (IMM-1877-05) argued that as a result of the diminishing presence of RPOs in refugee hearings, the role of the Board member is being distorted giving rise to a reasonable apprehension of institutional bias.

#### 2044:9:subtheme:41 · paragraphs 190-190

- Raw key terms: `appear, applicant, argues, because, becomes, board, claim, claimant`
- Display key terms: `appear, argues, because, becomes`
- Argument roles: `issue, party_position, reasoning_application`
- Explanation: Observed roles: issue, party_position, reasoning_application Display terms: appear, argues, because, becomes Position/evidence statements: [190] This applicant argues that this is a constitutional issue going directly to the independence of the tribunal. Application context: It matters not whether Guideline 7 was implemented as a guideline or a rule, because the result remains the same. Evidence spans paragraphs 190-190. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168318` offsets `58-63`; context: [190] This applicant argues that this is a constitutional issue going directly to the independence of the tribunal.
- Evidence: `party_position` cue `argues` at chunk `4168318` offsets `21-27`; context: [190] This applicant argues that this is a constitutional issue going directly to the independence of the tribunal.
- Evidence: `reasoning_application` cue `because` at chunk `4168318` offsets `193-200`; context: It matters not whether Guideline 7 was implemented as a guideline or a rule, because the result remains the same.

#### Section text

[59] In Suresh v. Canada (Minister of Citizenship & Immigration) [2002] 1 S.C.R. 3, 2002 SCC 1 [Suresh], the Supreme Court made the following comment in relation to the scope of fundamental justice at paragraph 113:
The principles of fundamental justice of which s. 7 speaks, though not identical to the duty of fairness elucidated in Baker, are the same principles underlying that duty. As Professor Hogg has said, "The common law rules [of procedural fairness] are in fact basic tenets of the legal system, and they have evolved in response to the same values and objectives as s. 7": see P. W. Hogg, Constitutional Law of Canada (loose-leaf ed.) vol. 2, at para. 44.20. In Singh v. Minister of Employment and Immigration, [1985] 1 S.C.R. 177, at pp. 212-13, Wilson J. recognized that the principles of fundamental justice demand, at a minimum, compliance with the common law requirements of procedural fairness. Section 7 protects substantive as well as procedural rights: Re B.C. Motor Vehicle Act, supra. Insofar as procedural rights are concerned, the common law doctrine summarized in Baker, supra, properly recognizes the ingredients of fundamental justice [emphasis added].

[60] The applicants seek to elevate the issue of the order of questioning in refugee determination proceedings to a level where constitutional protection would be required and appropriate. While it is an important issue in light of the security of the person interests that are affected by the fairness of the refugee determination process, I am satisfied that this case concerns classic administrative law issues that may be determined under the principles of natural justice and fairness without invoking the Charter. As noted in Suresh, the principles underlying the duty of fairness are the same as those of which section 7 speaks in the procedural context. This controversy can be properly dealt with on the basis of the procedural protections reflected in the common law doctrine of fairness.

[61] I find, therefore, that it is not necessary for the Court to determine the scope and effect of fundamental justice under section 7 with regard to the application of the Guideline. If I am wrong in that regard, I would conclude that fundamental justice does not require that the questioning order employed in the civil and criminal courts be extended to refugee determination hearings. That procedural order was developed in the context of adversarial proceedings and strict rules of evidence in which the role of the Court was to oversee the contest between the parties, decide issues of law and instruct a jury, if sitting with one, or itself, if sitting alone, to find the facts and apply the law within the narrow confines of the pleadings or indictment.

[62] I recognize that the language of court procedures has crept into the practice of the IRB. Counsel and, indeed, Board members in their decisions speak of “examination-in-chief” and “cross-examination” and describe the procedure mandated by Guideline 7 as a “reverse order” of questioning. But the nature of the hearings before the RPD is meant to be administrative and non-adversarial, as is reflected in the language of subsection 162(2) and section 170 of the statute. If Parliament had intended that these hearings employ court procedures it could easily have said so. The legislative intent is to the contrary.

[63] Subsection 162(2) provides that “[e]ach Division shall deal with all proceedings before it as informally and quickly as the circumstances and the considerations of fairness and natural justice permit”. While s.170 states that the RPD must give the claimant and the Minister a reasonable opportunity to present evidence, question witnesses and make representations, the procedure is not bound by “legal or technical rules of evidence”.

[64] These provisions indicate to me, a legislative intention to avoid the formalities which are attendant upon court hearings in civil or criminal proceedings. This legislative intention is not inconsistent with the requirements of fundamental justice. I note that the Supreme Court has cautioned against extending the procedural rights provided by the Charter for criminal cases to administrative law cases: Blencoe v. British Columbia (Human Rights Commission), [2000] 2 S.C.R. 307, 2000 SCC 44 at para. 88.

[65] The Board should not be held to the same procedural standards as a judicial body. In Kozak, above, the Court of Appeal in commenting on the Board’s “uniquely difficult mandate of administrative adjudication” had this to say at paragraph 56:
In view of these challenges, the Board has had to devise means of maintaining and enhancing the consistency and quality of its decisions, which is of critical importance to its ability to perform its statutory functions and to retain its legitimacy. To this end, the Board's procedure should not be confined in a model of due process that draws exclusively on the judicial paradigm and discourages innovation. Nonetheless, procedures designed to increase quality and consistency cannot be adopted at the expense of the duty of each panel to afford to the claimant before it a high degree of impartiality and independence [emphasis added].

[66] What constitutes a “reasonable opportunity to present evidence” must depend upon the circumstances of each case. It may be that in a particular refugee determination hearing it would be necessary for the claimant’s counsel to question first in order to ensure that his or her evidence is properly presented. But I have difficulty understanding why that would be necessary in every case or why it is essential in fundamental justice terms that the claimant have the option at his or her discretion to determine the order of questioning, as the applicants have argued.

[67] Under Guideline 7, it remains open to each claimant in a refugee determination hearing to fully present any element of his or her case that the RPO or Board member does not explore in their initial questioning and to have the effective assistance of counsel in so doing. Were it to foreclose such an opportunity, I would have no hesitation in finding that the right to a hearing was being denied. But that is not the result of the implementation of Guideline 7. While fundamental justice entitles a refugee claimant to a fair hearing, it does not entitle him or her to “the most favourable procedures that could possibly be imagined”: R v. Lyons, [1987] 2 S.C.R. 309 at 362, 44 D.L.R. (4th) 193; Ruby v. Canada (Solicitor General), [2002] 4 S.C.R. 3 at para. 46, 2002 SCC 75.
Section 15

[68] With regard to section 15 of the Charter, counsel for one of the applicants has argued that refugee claimants are discriminated against because they do not have the right to present their evidence first and to have their counsel question them first, in contrast to the procedure before other tribunals, including the other IRB Divisions. This argument is advanced on a hypothetical and theoretical basis without reference to a factual foundation other than that revealed by the Guideline 7 documentation filed in these proceedings.

[69] There is no evidence before me as to the practice of other administrative tribunals and I am not prepared to speculate as to what their practices might be based on my own knowledge or counsel’s submissions. In so far as the proceedings before the other IRB Divisions are concerned, the only material that I have indicates that they are in fact adversarial and involve parties with opposing interests. Thus, I would have difficulty finding that they are suitable comparators for the purpose of a section 15 analysis.

[70] In MacKay v. Manitoba, [1989] 2 S.C.R. 357, 61 D.L.R. (4th) 385, the Supreme Court of Canada cautioned that Charter decisions should not be made in a factual vacuum as doing so would both trivialize the Charter and result in ill-considered opinions.

[71] I am satisfied that there is an insufficient factual basis in this case upon which the Court could decide whether claimants in refugee determination proceedings were discriminated against through the implementation of Guideline 7 as contemplated by s.15 of the Charter. And, as discussed above, it is not necessary to determine the question when there is an adequate alternative remedy available to the applicants at common law. Accordingly, I decline to address that question.
Is the procedure mandated by Guideline 7 and adopted by the tribunal contrary to natural justice?

[72] The question of whether the order of questioning implemented by the Board under Guideline 7 is, in itself, inconsistent with natural justice was addressed in a number of decisions of this Court prior to Thamotharem. In none of these decisions was “reverse order questioning” alone found to deny procedural fairness: B.D.L. v. Canada (Minister of Citizenship and Immigration), 2005 FC 866, [2005] F.C.J. No. 1080 (QL) [B.D.L.]; Cortes Silva v. Canada (Minister of Citizenship and Immigration), 2005 FC 738 , [2005] F.C.J. No. 920 (QL) [Cortes Silva]; Martinez v. Canada (Minister of Citizenship and Immigration), 2005 FC 1121, [2005] F.C.J. No. 1377 (QL) [Martinez]; Fabiano v. Canada (Minister of Citizenship and Immigration), 2005 FC 1260, [2005] F.C.J. No. 1510 (QL) [Fabiano]; Liang v. Canada (Minister of Citizenship and Immigration), 2005 FC 622, [2005] F.C.J. No. 750 (QL) [Liang]; and Zaki v. Canada (Minister of Citizenship and Immigration), 2005 FC 1066, 48 Imm. L.R. (3d) 149 [Zaki].

[73] In general, the common view expressed by my colleagues in these decisions is that the procedure followed in each case had to be examined to determine whether there had been a breach of fairness. As stated by the Court in Zaki, above, at paragraph 14:
Although the Guideline per se is not, in my view, procedurally unfair, it may well be that its implementation in any given case is done in such a way as to lead to a conclusion that a claimant was not afforded an opportunity to make his case. The relevant question is whether the procedure, on the facts of this case, resulted in unfairness to the Applicant…

[74] Justice Blanchard reviewed these decisions in Thamotharem and found that, while instructive, they were not determinative of the issues before him. The Court had not previously had the benefit of the extensive evidence and submissions that were presented by the parties and by the intervenor in that case. The issues had not been as comprehensively canvassed and argued. Accordingly, Justice Blanchard revisited the question of whether the application of Guideline 7, was, in itself, inconsistent with procedural fairness.

[75] I have had the benefit of the thorough review of that question which Justice Blanchard conducted together with the submissions of counsel in these proceedings which have largely focused on his analysis.

[76] In an effort to establish that the Court has previously recognized that fairness dictates that refugee claimants must be examined first by their counsel, the applicants have cited several decisions in which the conduct of the hearing was in question. These include Kante v. Canada (Minister of Employment and Immigration), [1994] F.CJ. No. 525 (F.C.T.D.) (QL); Ganji v. Canada (Minister of Citizenship and Immigration) (1997), 135 F.T.R. 283, 40 Imm. L.R. (2d) 95 (F.C.T.D.) [Ganji]; Atwal v. Canada (Minister of Citizenship and Immigration) (1998), 157 F.T.R. 258, [1998] F.C.J. No. 1693 (F.C.T.D.) (QL); and Veres v. Canada (Minister of Citizenship and Immigration), [2001] 2 F.C. 124, [2000] F.C.J. No. 1913 (F.C.T.D.) (QL).

[77] These decisions were also the subject of submissions to the Court in Thamotharem. Following a review of each case, Justice Blanchard expressed the following conclusion at paragraph 46 of his reasons:
In my opinion, in none of these cases did the Court establish that the principles of natural justice and procedural fairness require that refugee claimants be questioned by their counsel first. In fact, whether the Board’s choice of the order of questioning accorded with natural justice or procedural fairness was not before the Court in any of the cases. The cases all dealt with specific circumstances in which the Court held that the Refugee Board’s conduct of the hearing was improper or led to an error in the Board’s findings of fact.
And further at paragraph 53:
In my opinion, the cases cited by the Applicant and the Intervener do not lead to the conclusion that a meaningful opportunity to present one’s case includes a right to question first. Rather, they reaffirm that the Board is entitled to control the procedures of a hearing but that the Board must conduct the hearing in a way that does not unfairly restrict the claimant’s right to present her or his case.

[78] Having closely reviewed the reasons in each of the cases cited above and considered the arguments of counsel, I see no reason to depart from the conclusions reached by my colleague in Thamotharem on the correct interpretation of these prior decisions. While the reasons for decision contain statements which may be construed as lending support for the notion that a fair hearing requires that the claimant’s counsel question first, a close examination discloses that the Court in each case was more concerned with whether the hearing, as a whole, was fair than with the order of questioning. The order of questioning may have contributed to unfairness in a particular case but was not determinative of that finding.

[79] The applicants rely in particular upon two decisions of this Court: Herrera v. Canada (Minister of Citizenship and Immigration), 2004 FC 1724, [2005] F.C.J. No. 118 (QL) [Herrera] and Sandor v. Canada (Minister of Citizenship and Immigration) (2004), 266 F.T.R. 311, 2004 FC 1782 [Sandor]. Herrera was considered by Justice Blanchard and distinguished. Sandor was, I believe, not addressed before Justice Blanchard.

[80] In Herrera, the Court held that a hearing had been unfairly conducted where the applicant’s counsel had consented to the RPO questioning first, to be followed by the RPD member. The applicants rely on paragraph 4 of the reasons which reads as follows:
As argued by Counsel for the Applicant in the present application, a serious due process issue exists as to whether there was a fair hearing before the RPD. At the hearing, the Applicant was not allowed to lead his evidence, but instead, the Refugee Protection Officer was instructed to question first, and then, the RPD followed with what I find is accurately described by Counsel for the Applicant as "badgering" cross-examination

[81] The fact that the Member conducted what the Court described as a “badgering cross-examination” alone would have been enough, in my view, to send the matter back for a rehearing. However, it is also clear from the decision that the Court was concerned that the RPD had effectively set a trap for the applicant at the outset of the hearing by misdescribing the issues to be addressed. At paragraph 5 he states:
It is quite clear that at the opening of the hearing the RPD had a suspicion that the Applicant's credibility was seriously in question, given the variance between the two statements which were in the written record. Immediately prior to asking for the Applicant's lawyer to consent to the procedure whereby the RPO would lead the claimant's case, the case was simply called "a simple outlined claim". As it turns out, it was anything but.

[82] As I read the Court’s reasons, this decision does not stand for the proposition that the claimant’s counsel must always question first but rather, whichever procedure is followed, that the claimant must be given fair notice of the issues and a fair opportunity to be heard. A similar reading of this decision was reached by Justice Blanchard in Thamotharem and by Justice Snider in Zaki.

[83] In Sandor, above, at paragraph 36, the Court found that the applicant was denied a fair hearing largely because of the Board Member’s extensive questioning. He stated that he reached that conclusion because of this questioning and because of “the fact that the RPO was allowed to cross-examine the applicant before his examination in chief was completed” [emphasis added]. This is the phrase that the applicants rely upon but, in my view, it is an exceedingly thin basis upon which to make the case that the Court has accepted that procedural fairness requires that counsel examine first.

[84] It appears that the hearing had commenced with the claimants counsel questioning first when the interruptions from the Board Member began. The issue of whether procedural fairness required that the claimant’s counsel go first does not appear to have been squarely addressed in the proceedings as it had not been raised prior to the judicial review hearing. One may infer from the Court’s reasons that it was the interruptions by the Board Member that offended my colleague’s sense of fairness together with the RPO’s extensive questioning.
Baker Analysis

[85] As noted above, the factors to be considered in determining whether the common law duty of fairness has been met by the procedures in question were discussed by Justice L’Heureux-Dubé in Baker, above, at paragraphs 22-28. The factors identified by Justice L’Heureux-Dubé, while not exhaustive, are as follows:
1. The nature of the decision being made and the process followed in making it.
The role of the particular decision within the statutory scheme. The importance of the decision to the individual affected.
4. The legitimate expectations of the person challenging the decision where undertakings were made as to the procedure to be followed.
5. Whether the decision-maker is empowered by statute to set its own procedures.

[86] The application of these factors to the Guideline 7 order of questioning procedure was analysed in depth by Justice Blanchard in Thamotharem at paragraphs 68-83 of his reasons. He concluded that an application of the first, second and third factors indicated that a higher level of procedural fairness was called for. His analysis of the fourth factor dealing with legitimate expectation and the fifth concerning the ability of the tribunal to control its own process pointed to a lesser standard. With regard to the importance of the decision to the individual affected, the third factor, I agree with Justice Blanchard that as the security interests of the claimants are engaged and will be determined by the Board’s decision, this indicates that a higher degree of procedural fairness is required.

[87] The applicants do not take issue with Justice Blanchard’s analysis of the second and third Baker factors but question his analysis of the first factor and invite me to reach different conclusions regarding the remaining two. They submit that there are additional factors that militate in favour of a higher standard of procedural fairness that were not considered in Thamotharem.

[88] The respondent questions Justice Blanchard’s findings that the first two factors indicate a higher standard. The first, the respondent submits, should indicate a lower standard and the second is, at best, neutral. The third, the importance of the decision to the individual, the respondent agrees points to greater protection. In these reasons, I will deal only with those factors where there is a substantial disagreement between the parties.

[89] With respect to the second factor, the nature of the decision making process in the legislative scheme, Baker, above, at paragraph 24, indicates that the lack of a right of appeal suggests a higher degree of procedural protection will be required.

[90] The applicants submit that the enactment by Parliament in IRPA of provisions for a Refugee Appeal Division (RAD), combined with the failure of the Governor-in-Council to bring the RAD into effect enhances the duty of fairness owed to the applicant and decreases the deference owed by the Court to a decision of the Board on refugee protection. The applicants submit that the duty 

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 2044:10 · paragraphs 191-201

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b7f634117ecf13e05b259fb8fca69329cb488ca079632f6cafb24c13e52a046b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:10:subtheme:1 · paragraphs 191-192

- Raw key terms: `independence, justice, question, accept, apply, articulated, aspect, attempt`
- Display key terms: `independence, justice, question, accept, apply, articulated, aspect, attempt`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: independence, justice, question, accept, apply, articulated, aspect, attempt Rule/authority context: If the legislation is silent or insufficiently precise, the courts will generally infer that Parliament or the legislature intended that the tribunal’s process will comport with the principles of natural justice. Application context: 781, 2001 SCC 52, the standard of independence articulated in Régie stemmed from the Quebec Charter, a quasi-constitutional statute, and does not apply to tribunals created by other jurisdictions. Evidence spans paragraphs 191-192. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168319` offsets `49-57`; context: [191] In Régie, the Supreme Court dealt with the question of the independence of quasi-judicial tribunals in the context of s.
- Evidence: `governing_rule` cue `principles` at chunk `4168319` offsets `913-923`; context: If the legislation is silent or insufficiently precise, the courts will generally infer that Parliament or the legislature intended that the tribunal’s process will comport with the principles of natural justice.
- Evidence: `reasoning_application` cue `apply` at chunk `4168319` offsets `588-593`; context: 781, 2001 SCC 52, the standard of independence articulated in Régie stemmed from the Quebec Charter, a quasi-constitutional statute, and does not apply to tribunals created by other jurisdictions.
- Evidence: `issue` cue `question` at chunk `4168320` offsets `22-30`; context: [192] In my view, the question of the independence of the IRB is not squarely raised in these proceedings on the records before me and I do not intend to attempt to decide that question.

#### 2044:10:subtheme:2 · paragraphs 193-195

- Raw key terms: `institutional, bias, gonthier, justice, legislation, test, account, adjudication`
- Display key terms: `institutional, bias, gonthier, justice, legislation, account, adjudication`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: institutional, bias, gonthier, justice, legislation, account, adjudication Rule/authority context: [195] Justice Gonthier noted that in applying this test, greater flexibility must be shown to administrative tribunals than would be required of the courts and the institutional constraints under which the tribunals oper Evidence spans paragraphs 193-195. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168321` offsets `127-135`; context: [193] Institutional bias was made out in Régie on a detailed review of the legislation and the structure of the institution in question.
- Evidence: `governing_rule` cue `under` at chunk `4168323` offsets `190-195`; context: [195] Justice Gonthier noted that in applying this test, greater flexibility must be shown to administrative tribunals than would be required of the courts and the institutional constraints under which the tribunals operate must be taken into account.

#### 2044:10:subtheme:3 · paragraphs 196-197

- Raw key terms: `absence, allegations, appeal, apprehension, band, basis, bias, brought`
- Display key terms: `absence, allegations, apprehension, band, basis, bias, brought`
- Argument roles: `counterargument_limitation, evidence_fact`
- Explanation: Observed roles: counterargument_limitation, evidence_fact Display terms: absence, allegations, apprehension, band, basis, bias, brought Evidence spans paragraphs 196-197. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4168324` offsets `197-203`; context: Failing that, allegations of an apprehension of bias cannot be brought on an institutional level but must be dealt with on a case-by-case basis: Canadian Pacific Ltd.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168325` offsets `24-32`; context: [197] In the absence of evidence to the contrary, there is a strong presumption that a decision maker will act impartially: Zundel v.

#### 2044:10:subtheme:4 · paragraphs 198-201

- Raw key terms: `circumstances, bias, decisions, particular, reasonable, above, apprehension, board`
- Display key terms: `circumstances, bias, decisions, particular, reasonable, above, apprehension`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue, reasoning_application Display terms: circumstances, bias, decisions, particular, reasonable, above, apprehension Application context: There is no suggestion that any improper influence was brought to bear on the outcome of the decisions rendered by the RPD members who applied the Guideline or that the application of the Guideline was intended to have a | [201] I am not persuaded that a reasonable apprehension of bias arises merely because the member conducts the questioning. Operative outcome context: Indeed, the uncontradicted evidence is that the claim acceptance rate has not varied for the periods before and after the adoption of the Guideline. Evidence spans paragraphs 198-201. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168326` offsets `130-138`; context: [198] In Kozak, above, at paragraphs 51-57, the Federal Court of Appeal noted three considerations of particular relevance to the question of bias in the context of RPD decision making.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168327` offsets `89-97`; context: [199] In the particular circumstances of that case, the Court found there was sufficient evidence of external pressures and influences bearing on the decision makers that a reasonable apprehension of bias was established.
- Evidence: `counterargument_limitation` cue `but` at chunk `4168327` offsets `380-383`; context: Specifically, that the lead case strategy employed in that case was designed not only to bring consistency to future decisions and to improve their accuracy, but to reduce the number of positive decisions that might otherwise be rendered and to reduce the number of potential claimants.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168328` offsets `430-438`; context: Indeed, the uncontradicted evidence is that the claim acceptance rate has not varied for the periods before and after the adoption of the Guideline.
- Evidence: `reasoning_application` cue `applied` at chunk `4168328` offsets `278-285`; context: There is no suggestion that any improper influence was brought to bear on the outcome of the decisions rendered by the RPD members who applied the Guideline or that the application of the Guideline was intended to have any effect on the results of the claims.
- Evidence: `disposition` cue `varied` at chunk `4168328` offsets `481-487`; context: Indeed, the uncontradicted evidence is that the claim acceptance rate has not varied for the periods before and after the adoption of the Guideline.
- Evidence: `reasoning_application` cue `because` at chunk `4168329` offsets `78-85`; context: [201] I am not persuaded that a reasonable apprehension of bias arises merely because the member conducts the questioning.

#### Section text

[191] In Régie, the Supreme Court dealt with the question of the independence of quasi-judicial tribunals in the context of s. 23 of the Quebec Charter of Human Rights and Freedoms, R.S.Q., c. C-12 which guarantees the right to a full and equal, public and fair hearing by an independent and impartial tribunal. As explained in Ocean Port Hotel Ltd. v. British Columbia (General Manager, Liquor Control and Licensing Branch), [2001] 2 S.C.R. 781, 2001 SCC 52, the standard of independence articulated in Régie stemmed from the Quebec Charter, a quasi-constitutional statute, and does not apply to tribunals created by other jurisdictions. In other contexts, the standard is to be determined by the express will of the legislature. If the legislation is silent or insufficiently precise, the courts will generally infer that Parliament or the legislature intended that the tribunal’s process will comport with the principles of natural justice. In some instances, but generally not, the tribunal may attract Charter requirements of independence.

[192] In my view, the question of the independence of the IRB is not squarely raised in these proceedings on the records before me and I do not intend to attempt to decide that question. I accept, of course, as stated at paragraph 42 of Justice Gonthier’s reasons for the majority in Régie citing R. v. Lippé, [1991] 2 S.C.R. 114 , [1990] S.C.J. No. 128 (QL) that impartiality can have an institutional or structural aspect.

[193] Institutional bias was made out in Régie on a detailed review of the legislation and the structure of the institution in question. Crucial to the outcome was the Court’s view of the role of staff counsel who were involved in every stage of the proceedings, including the investigation, prosecution and adjudication of complaints.

[194] At paragraph 44 of his reasons, Justice Gonthier referred to the well-established test for institutional impartiality put forward by Justice de Grandpré in Committee for Justice and Liberty v. National Energy Board, [1978] 1 S.C.R. 369 at 394. Justice Gonthier summarized the test in these words:
…The determination of institutional bias presupposes that a well-informed person, viewing the matter realistically and practically -- and having thought the matter through -- would have a reasonable apprehension of bias in a substantial number of cases. In this regard, all factors must be considered, but the guarantees provided for in the legislation to counter the prejudicial effects of certain institutional characteristics must be given special attention.

[195] Justice Gonthier noted that in applying this test, greater flexibility must be shown to administrative tribunals than would be required of the courts and the institutional constraints under which the tribunals operate must be taken into account. Moreover, a plurality of functions in a single administrative agency is not necessarily problematic.

[196] Institutional bias will not be found unless a well-informed person would have a reasonable apprehension in a substantial number of cases. Failing that, allegations of an apprehension of bias cannot be brought on an institutional level but must be dealt with on a case-by-case basis: Canadian Pacific Ltd. v. Matsqui Indian Band, [1995] 1 S.C.R. 3, 122 D.L.R. (4th) 129.

[197] In the absence of evidence to the contrary, there is a strong presumption that a decision maker will act impartially: Zundel v. Citron, [2000] 4 F.C. 225, 189 D.L.R. (4th) 131 (F.C.A.) leave to appeal refused, [2000] S.C.C.A. No. 322.

[198] In Kozak, above, at paragraphs 51-57, the Federal Court of Appeal noted three considerations of particular relevance to the question of bias in the context of RPD decision making. First, that the content of the duty of fairness owed by the Board falls at the high end of the continuum of procedural fairness. Secondly, that the Board has a particularly difficult mandate of administrative adjudication. And third, that the notion of bias connotes circumstances giving rise to a reasonable and informed belief that the decision maker has been influenced by some extraneous or improper considerations.

[199] In the particular circumstances of that case, the Court found there was sufficient evidence of external pressures and influences bearing on the decision makers that a reasonable apprehension of bias was established. Specifically, that the lead case strategy employed in that case was designed not only to bring consistency to future decisions and to improve their accuracy, but to reduce the number of positive decisions that might otherwise be rendered and to reduce the number of potential claimants.

[200] The circumstances surrounding the Board’s adoption of the standard order of questioning do not, in my view, compare with those in Kozak. There is no suggestion that any improper influence was brought to bear on the outcome of the decisions rendered by the RPD members who applied the Guideline or that the application of the Guideline was intended to have any effect on the results of the claims. Indeed, the uncontradicted evidence is that the claim acceptance rate has not varied for the periods before and after the adoption of the Guideline.

[201] I am not persuaded that a reasonable apprehension of bias arises merely because the member conducts the questioning. As stated by Dr. Payne on cross-examination, it matters less who does the questioning than how it is carried out. In the particular circumstances of an individual case, aggressive questioning may amount to a breach of fairness, as is illustrated by two decisions cited by the applicant: Farkas v. Canada (Minister of Citizenship and Immigration), 2001 FCT 190, [2001] F.C.J. No. 356 (F.C.T.D.) (QL) and Sandor, discussed above.

## 2044:11 · paragraphs 202-244

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `81e27f926fa9905dee78c77515001fcff50df7f3a187194ec6486d41d61384c5`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:11:subtheme:1 · paragraphs 202-203

- Raw key terms: `apprehension, bias, hearing, member, order, questioning, reasonable, support`
- Display key terms: `apprehension, bias, hearing, order, questioning, reasonable, support`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: apprehension, bias, hearing, order, questioning, reasonable, support Application context: [202] In Farkas, a Board ruling was set aside because of persistent and aggressive questioning by one of the Board members. Evidence spans paragraphs 202-203. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `4168330` offsets `155-165`; context: Similarly in Sandor, the Court found that extensive questioning by a Board member constituted a breach of natural justice and the denial of the right to a fair hearing.
- Evidence: `reasoning_application` cue `because` at chunk `4168330` offsets `46-53`; context: [202] In Farkas, a Board ruling was set aside because of persistent and aggressive questioning by one of the Board members.
- Evidence: `counterargument_limitation` cue `But` at chunk `4168330` offsets `293-296`; context: But these decisions do not support the proposition that a change in the order of questioning in itself gives rise to a reasonable apprehension of bias.
- Evidence: `issue` cue `question` at chunk `4168331` offsets `22-30`; context: [203] In my view, the question of bias in this context has to be raised on a case-by-case basis.
- Evidence: `evidence_fact` cue `record` at chunk `4168331` offsets `164-170`; context: I note, without deciding the matter, that in the Jones application record there is evidence of what counsel described as “long, nasty, brutish and hostile” examination of the claimant by the Member.

#### 2044:11:subtheme:2 · paragraphs 204-205

- Raw key terms: `applicants, cases, guideline, able, application, arises, because, board`
- Display key terms: `cases, guideline, able, arises, because`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: cases, guideline, able, arises, because Application context: [204] The question of waiver arises in these proceedings because a number of the applicants neither raised an objection to the Guideline 7 procedure at the Board hearing, nor sought a decision to vary the order of questi Operative outcome context: In some cases, it was not raised as a ground for judicial review prior to leave being granted and was raised then only after the reasons for decision in Thamotharem were released. | [205] While I have found that the applicants were not denied procedural fairness by the imposition of Guideline 7 in itself, certain of the applicants may be able to establish a denial of procedural fairness by its appli Evidence spans paragraphs 204-205. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168332` offsets `10-18`; context: [204] The question of waiver arises in these proceedings because a number of the applicants neither raised an objection to the Guideline 7 procedure at the Board hearing, nor sought a decision to vary the order of questioning from the member.
- Evidence: `reasoning_application` cue `because` at chunk `4168332` offsets `57-64`; context: [204] The question of waiver arises in these proceedings because a number of the applicants neither raised an objection to the Guideline 7 procedure at the Board hearing, nor sought a decision to vary the order of questioning from the member.
- Evidence: `disposition` cue `granted` at chunk `4168332` offsets `329-336`; context: In some cases, it was not raised as a ground for judicial review prior to leave being granted and was raised then only after the reasons for decision in Thamotharem were released.
- Evidence: `evidence_fact` cue `found that` at chunk `4168333` offsets `19-29`; context: [205] While I have found that the applicants were not denied procedural fairness by the imposition of Guideline 7 in itself, certain of the applicants may be able to establish a denial of procedural fairness by its application in their particular cases.
- Evidence: `disposition` cue `denied` at chunk `4168333` offsets `54-60`; context: [205] While I have found that the applicants were not denied procedural fairness by the imposition of Guideline 7 in itself, certain of the applicants may be able to establish a denial of procedural fairness by its application in their particular cases.

#### 2044:11:subtheme:3 · paragraphs 206-209

- Raw key terms: `applicant, above, hearing, waiver, addressed, board, cases, common`
- Display key terms: `above, hearing, waiver, addressed, cases, common`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: above, hearing, waiver, addressed, cases, common Position/evidence statements: The jurisprudence to date has not dealt specifically with the issue of waiver as it relates to an applicant’s ability to argue Guideline 7 upon judicial review. Rule/authority context: The jurisprudence to date has not dealt specifically with the issue of waiver as it relates to an applicant’s ability to argue Guideline 7 upon judicial review. Application context: 5 -6 that because …the applicant did not think it necessary to object and did not establish the existence of any harm… In view of the particular facts of the case at bar, the argument now relied on by the applicant as to Evidence spans paragraphs 206-209. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168334` offsets `169-174`; context: The jurisprudence to date has not dealt specifically with the issue of waiver as it relates to an applicant’s ability to argue Guideline 7 upon judicial review.
- Evidence: `party_position` cue `argue` at chunk `4168334` offsets `228-233`; context: The jurisprudence to date has not dealt specifically with the issue of waiver as it relates to an applicant’s ability to argue Guideline 7 upon judicial review.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4168334` offsets `111-124`; context: The jurisprudence to date has not dealt specifically with the issue of waiver as it relates to an applicant’s ability to argue Guideline 7 upon judicial review.
- Evidence: `issue` cue `whether` at chunk `4168335` offsets `65-72`; context: [207] The second common scenario is cases in which it is unclear whether the applicant objected to Guideline 7 at the hearing, but the issue was raised in the judicial review of the Board’s decision and the Court dealt with the question of procedural fairness without reference to waiver.
- Evidence: `reasoning_application` cue `because` at chunk `4168336` offsets `107-114`; context: 5 -6 that because
…the applicant did not think it necessary to object and did not establish the existence of any harm… In view of the particular facts of the case at bar, the argument now relied on by the applicant as to unfairness of the procedure is entirely without basis.

#### 2044:11:subtheme:4 · paragraphs 210-215

- Raw key terms: `court, appeal, applicant, breach, canada, earliest, object, objection`
- Display key terms: `breach, earliest, object, objection`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: breach, earliest, object, objection Rule/authority context: [211] It appears, therefore, that the jurisprudence of this Court regarding when an applicant must raise an objection to the order of questioning in order to have it dealt with upon judicial review is unsettled. Application context: [211] It appears, therefore, that the jurisprudence of this Court regarding when an applicant must raise an objection to the order of questioning in order to have it dealt with upon judicial review is unsettled. | [214] The reasoning of Justice MacGuigan was applied by the Court of Appeal in Yassine v. Operative outcome context: In Ganji, the Court quashed a decision of the Board in which the Board had seized control of the applicant’s case and conducted the examination. Evidence spans paragraphs 210-215. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168338` offsets `486-492`; context: In Herrera, as discussed above, counsel had consented to the procedure without full disclosure of the issues to be raised.
- Evidence: `disposition` cue `quashed` at chunk `4168338` offsets `259-266`; context: In Ganji, the Court quashed a decision of the Board in which the Board had seized control of the applicant’s case and conducted the examination.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4168339` offsets `38-51`; context: [211] It appears, therefore, that the jurisprudence of this Court regarding when an applicant must raise an objection to the order of questioning in order to have it dealt with upon judicial review is unsettled.
- Evidence: `reasoning_application` cue `therefore` at chunk `4168339` offsets `18-27`; context: [211] It appears, therefore, that the jurisprudence of this Court regarding when an applicant must raise an objection to the order of questioning in order to have it dealt with upon judicial review is unsettled.
- Evidence: `reasoning_application` cue `applied` at chunk `4168342` offsets `45-52`; context: [214] The reasoning of Justice MacGuigan was applied by the Court of Appeal in Yassine v.

#### 2044:11:subtheme:5 · paragraphs 216-217

- Raw key terms: `appeal, appellant, court, objection, proceedings, waiver, zundel, address`
- Display key terms: `appellant, objection, proceedings, waiver, zundel, address`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: appellant, objection, proceedings, waiver, zundel, address Evidence spans paragraphs 216-217. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4168344` offsets `178-186`; context: 174 [Zundel] the Court of Appeal considered the question of whether the doctrine of waiver may be relied upon in the face of a finding of reasonable apprehension of bias.
- Evidence: `counterargument_limitation` cue `however` at chunk `4168344` offsets `613-620`; context: Newfoundland Telephone, however, did not address the question of waiver and the objection to the proceedings was raised at the very outset.

#### 2044:11:subtheme:6 · paragraphs 218-222

- Raw key terms: `applicant, bias, earliest, hearing, justice, opportunity, practical, raise`
- Display key terms: `bias, earliest, hearing, justice, opportunity, practical, raise`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: bias, earliest, hearing, justice, opportunity, practical, raise Evidence spans paragraphs 218-222. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168346` offsets `199-206`; context: [218] In concluding his analysis for the Court in Zundel, Justice Stone accepted that any waiver to be effective must be made freely and with full knowledge of all the facts relevant to the decision whether to waive or not.

#### 2044:11:subtheme:7 · paragraphs 223-227

- Raw key terms: `court, grounds, review, applicants, decision, federal, judicial, pleaded`
- Display key terms: `grounds, review, federal, judicial, pleaded`
- Argument roles: `counterargument_limitation, disposition, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, issue, party_position Display terms: grounds, review, federal, judicial, pleaded Position/evidence statements: [223] The respondent submits that the Court should not consider grounds for judicial review that were not expressly pleaded in the applications for leave. Operative outcome context: 1 of the Federal Courts Act, which among other things, sets out the various forms of relief which may be granted an applicant. Evidence spans paragraphs 223-227. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168351` offsets `219-224`; context: In these proceedings, several applicants raised the Guideline 7 issue in their memoranda of fact and law or supplementary memoranda for the first time after the release of the decision in Thamotharem.
- Evidence: `party_position` cue `submits` at chunk `4168351` offsets `21-28`; context: [223] The respondent submits that the Court should not consider grounds for judicial review that were not expressly pleaded in the applications for leave.
- Evidence: `disposition` cue `granted` at chunk `4168352` offsets `483-490`; context: 1 of the Federal Courts Act, which among other things, sets out the various forms of relief which may be granted an applicant.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4168353` offsets `46-52`; context: [225] The Native Women’s Association decision cannot be extended, in my view, to support the proposition that applicants may raise new grounds that were not specifically pleaded in their applications for judicial review.

#### 2044:11:subtheme:8 · paragraphs 228-229

- Raw key terms: `applicants, board, case, facts, failure, issue, prejudiced, proceedings`
- Display key terms: `case, facts, failure, prejudiced, proceedings`
- Argument roles: `disposition, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, reasoning_application Display terms: case, facts, failure, prejudiced, proceedings Application context: The Court determined that it was appropriate to consider it at that time because the record disclosed all of the relevant facts, and there was no suggestion that the Minister would be prejudiced if the issue was consider | Thus I would conclude that, unlike in Stumpf, the respondent may be prejudiced by the failure of the applicants to raise the issue at an earlier stage of the proceedings. Operative outcome context: 165, the Court of Appeal allowed the applicants to raise an issue in oral arguments which had not been raised in the judicial review or in any of the proceedings before the Board. Evidence spans paragraphs 228-229. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168356` offsets `164-169`; context: 165, the Court of Appeal allowed the applicants to raise an issue in oral arguments which had not been raised in the judicial review or in any of the proceedings before the Board.
- Evidence: `evidence_fact` cue `determined that` at chunk `4168356` offsets `501-516`; context: The Court determined that it was appropriate to consider it at that time because the record disclosed all of the relevant facts, and there was no suggestion that the Minister would be prejudiced if the issue was considered.
- Evidence: `reasoning_application` cue `because` at chunk `4168356` offsets `564-571`; context: The Court determined that it was appropriate to consider it at that time because the record disclosed all of the relevant facts, and there was no suggestion that the Minister would be prejudiced if the issue was considered.
- Evidence: `disposition` cue `allowed` at chunk `4168356` offsets `129-136`; context: 165, the Court of Appeal allowed the applicants to raise an issue in oral arguments which had not been raised in the judicial review or in any of the proceedings before the Board.
- Evidence: `issue` cue `whether` at chunk `4168357` offsets `197-204`; context: For instance, it is not clear through reading the applicable Tribunal Records whether there was evidence before the Board Member of why the order of questioning outlined in Guideline 7 should not be followed in a given case, particularly if it was raised before the hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168357` offsets `215-223`; context: For instance, it is not clear through reading the applicable Tribunal Records whether there was evidence before the Board Member of why the order of questioning outlined in Guideline 7 should not be followed in a given case, particularly if it was raised before the hearing.
- Evidence: `reasoning_application` cue `conclude` at chunk `4168357` offsets `407-415`; context: Thus I would conclude that, unlike in Stumpf, the respondent may be prejudiced by the failure of the applicants to raise the issue at an earlier stage of the proceedings.

#### 2044:11:subtheme:9 · paragraphs 230-231

- Raw key terms: `canada, court, judicial, raised, review, added, appeal, applicant`
- Display key terms: `judicial, raised, review, added`
- Argument roles: `counterargument_limitation, issue`
- Explanation: Observed roles: counterargument_limitation, issue Display terms: judicial, raised, review, added Evidence spans paragraphs 230-231. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168358` offsets `181-186`; context: 73 (QL) the Court stated at paragraph 2:
The applicant at the hearing raised the issue of reasonable apprehension of bias by the presiding member.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168358` offsets `247-254`; context: However this issue was not raised in the applicant's original pleadings, but only in a further Memorandum of Argument on behalf of the Applicant filed subsequently to receiving the Minister's Memorandum of Argument.

#### 2044:11:subtheme:10 · paragraphs 232-233

- Raw key terms: `board, hearing, made, objection, respecting, respondent, written, accept`
- Display key terms: `hearing, made, objection, respecting, written, accept`
- Argument roles: `evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position Display terms: hearing, made, objection, respecting, written, accept Position/evidence statements: As I read the jurisprudence, waiver will not be implied where the party against whom it is claimed has made an objection to the procedure before or during the hearing itself. Rule/authority context: As I read the jurisprudence, waiver will not be implied where the party against whom it is claimed has made an objection to the procedure before or during the hearing itself. Evidence spans paragraphs 232-233. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168360` offsets `100-106`; context: [232] In conclusion, I agree with the respondent that the applicants in this case who did not raise issues of procedural fairness respecting Guideline 7 before the Board and in their Applications for Leave and for Judicial Review should be precluded from doing so by way of written and oral argument at this time.
- Evidence: `issue` cue `issue` at chunk `4168361` offsets `682-687`; context: What the doctrine seeks to prevent is the litigant who sits mute through the procedure and tries to take advantage of the issue before a higher forum.
- Evidence: `party_position` cue `claimed` at chunk `4168361` offsets `476-483`; context: As I read the jurisprudence, waiver will not be implied where the party against whom it is claimed has made an objection to the procedure before or during the hearing itself.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168361` offsets `235-243`; context: [233] While claimants seeking decisions from the Board respecting the procedure to be followed at its hearings should normally follow the requirements set out in RPD Rules 43 and 44, that is by filing a written submission supported by evidence without delay before the hearing, I do not accept the respondent’s submission that failure to do so necessarily invokes the waiver doctrine.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4168361` offsets `399-412`; context: As I read the jurisprudence, waiver will not be implied where the party against whom it is claimed has made an objection to the procedure before or during the hearing itself.

#### 2044:11:subtheme:11 · paragraphs 234-235

- Raw key terms: `applicants, application, applications, court, fact, fairness, filed, further`
- Display key terms: `applications, fact, fairness, filed, further`
- Argument roles: `counterargument_limitation, disposition, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, disposition, issue, party_position Display terms: applications, fact, fairness, filed, further Position/evidence statements: The common “basket clause” formula “such further and other grounds as the applicants may advise and this Honourable Court permit” is not a complete and concise statement of the grounds intended to be argued within the me Operative outcome context: [235] In view of the unsettled state of the law on these issues and that prior to Thamotharem this Court had consistently denied applications based solely on Guideline 7, applicants should not be penalized for the failur Evidence spans paragraphs 234-235. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168362` offsets `470-475`; context: However, in some cases, the issue was identified in the memorandum of fact and law filed with the application.
- Evidence: `party_position` cue `argued` at chunk `4168362` offsets `403-409`; context: The common “basket clause” formula “such further and other grounds as the applicants may advise and this Honourable Court permit” is not a complete and concise statement of the grounds intended to be argued within the meaning of Rule 301.
- Evidence: `counterargument_limitation` cue `However` at chunk `4168362` offsets `442-449`; context: However, in some cases, the issue was identified in the memorandum of fact and law filed with the application.
- Evidence: `issue` cue `issues` at chunk `4168363` offsets `57-63`; context: [235] In view of the unsettled state of the law on these issues and that prior to Thamotharem this Court had consistently denied applications based solely on Guideline 7, applicants should not be penalized for the failure of counsel to specify the ground in the Notice of Application if it is clear from the materials filed with the application that procedural fairness was in issue.
- Evidence: `disposition` cue `denied` at chunk `4168363` offsets `122-128`; context: [235] In view of the unsettled state of the law on these issues and that prior to Thamotharem this Court had consistently denied applications based solely on Guideline 7, applicants should not be penalized for the failure of counsel to specify the ground in the Notice of Application if it is clear from the materials filed with the application that procedural fairness was in issue.

#### 2044:11:subtheme:12 · paragraphs 236-237

- Raw key terms: `application, applications, because, board, case, denial, fairness, findings`
- Display key terms: `applications, because, case, denial, fairness, findings`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: applications, because, case, denial, fairness, findings Position/evidence statements: The legislative intention to avoid the formalities attendant upon court proceedings is not inconsistent with the requirements of fundamental justice § After considering the factors laid out by the Supreme Court in Baker  Rule/authority context: [236] Turning to the application of these principles to the cases before me, I make the following findings: Cases in which there was no waiver because of a timely objection at or before the Board hearing and the denial o | § Although the order of questioning in refugee determination proceedings engages the security of the person interests of claimants, this case concerns classic administrative law issues that may be determined under the pr Application context: [236] Turning to the application of these principles to the cases before me, I make the following findings: Cases in which there was no waiver because of a timely objection at or before the Board hearing and the denial o | It is therefore not necessary for the Court to determine the scope and effect of fundamental justice under section 7 with regard to the application of the Guideline. Evidence spans paragraphs 236-237. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168364` offsets `765-770`; context: These applications are not barred from proceeding on the procedural fairness issue in relation to the application of Guideline 7 in that case.
- Evidence: `governing_rule` cue `principles` at chunk `4168364` offsets `42-52`; context: [236] Turning to the application of these principles to the cases before me, I make the following findings:
Cases in which there was no waiver because of a timely objection at or before the Board hearing and the denial of procedural fairness was identified as a ground for judicial review in the leave application either expressly or through a basket clause: IMM-9766-04 (Restrepo Benitez); IMM-1144-05 (Quadri); IMM-4044-05 (Roy); IMM-470-05 (Martinez & others); IMM-2150-05 (Matheen); IMM-353-05 (Rincon & others); IMM-1419-05 (Gomez & others); IMM-1877-05 (Jones); IMM-712-05 (Guirguis & others); IMM-407-05 (Mejia); IMM-9797-04 (Bilomba); IMM-2709-05 (Trujillo); IMM-2034-05 (Ortiz).
- Evidence: `reasoning_application` cue `because` at chunk `4168364` offsets `143-150`; context: [236] Turning to the application of these principles to the cases before me, I make the following findings:
Cases in which there was no waiver because of a timely objection at or before the Board hearing and the denial of procedural fairness was identified as a ground for judicial review in the leave application either expressly or through a basket clause: IMM-9766-04 (Restrepo Benitez); IMM-1144-05 (Quadri); IMM-4044-05 (Roy); IMM-470-05 (Martinez & others); IMM-2150-05 (Matheen); IMM-353-05 (Rincon & others); IMM-1419-05 (Gomez & others); IMM-1877-05 (Jones); IMM-712-05 (Guirguis & others); IMM-407-05 (Mejia); IMM-9797-04 (Bilomba); IMM-2709-05 (Trujillo); IMM-2034-05 (Ortiz).
- Evidence: `issue` cue `issues` at chunk `4168365` offsets `79-85`; context: [237] Based on the analysis above I make the following findings on each of the issues.
- Evidence: `party_position` cue `submitted` at chunk `4168365` offsets `996-1005`; context: The legislative intention to avoid the formalities attendant upon court proceedings is not inconsistent with the requirements of fundamental justice
§ After considering the factors laid out by the Supreme Court in Baker and the further factors submitted by the applicants, it has not been established that natural justice requires that counsel for a refugee claimant be provided with the opportunity to question the claimant first.
- Evidence: `evidence_fact` cue `evidence` at chunk `4168365` offsets `1258-1266`; context: The opportunity for the applicant to make written submissions and provide evidence to the Board, to have an oral hearing with the participation of counsel, and to make oral submissions, satisfies the participatory rights required by the duty of fairness and Guideline 7 does not, in itself, breach that duty.
- Evidence: `governing_rule` cue `under` at chunk `4168365` offsets `295-300`; context: § Although the order of questioning in refugee determination proceedings engages the security of the person interests of claimants, this case concerns classic administrative law issues that may be determined under the principles of natural justice and fairness without invoking the Charter.
- Evidence: `reasoning_application` cue `therefore` at chunk `4168365` offsets `384-393`; context: It is therefore not necessary for the Court to determine the scope and effect of fundamental justice under section 7 with regard to the application of the Guideline.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4168365` offsets `89-97`; context: § Although the order of questioning in refugee determination proceedings engages the security of the person interests of claimants, this case concerns classic administrative law issues that may be determined under the principles of natural justice and fairness without invoking the Charter.

#### 2044:11:subtheme:13 · paragraphs 238-240

- Raw key terms: `questions, respondent, agree, applicants, apprehension, bias, board, case`
- Display key terms: `questions, agree, apprehension, bias, case`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: questions, agree, apprehension, bias, case Position/evidence statements: [238] The applicants in this case have submitted a number of questions for certification: The proposed questions are as follows: 1. | [240] The respondent submits and I agree, that the questions regarding independence of Board members be re-written as follows: Does the role of Refugee Protection Division members in questioning refugee claimants, as con Rule/authority context: Does the implementation of paragraphs 19 and 23 of the Chairperson’s Guideline 7 violate principles of natural justice by unduly interfering with the claimant’s right to be heard? Application context: Is Guideline 7 unlawful because it is ultra vires the guideline making authority of the Chairperson under the IRPA? Evidence spans paragraphs 238-240. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4168366` offsets `1888-1893`; context: With respect to Guideline 7 and the objection/non-objection of the claimant’s counsel at the refugee hearing:
a) Does the respondent confuse the doctrine of waiver with that of the failure to object before the trier of fact as constituting an issue estoppel on judicial review?
- Evidence: `party_position` cue `submitted` at chunk `4168366` offsets `39-48`; context: [238] The applicants in this case have submitted a number of questions for certification:
The proposed questions are as follows:
1.
- Evidence: `governing_rule` cue `principles` at chunk `4168366` offsets `221-231`; context: Does the implementation of paragraphs 19 and 23 of the Chairperson’s Guideline 7 violate principles of natural justice by unduly interfering with the claimant’s right to be heard?
- Evidence: `reasoning_application` cue `because` at chunk `4168366` offsets `644-651`; context: Is Guideline 7 unlawful because it is ultra vires the guideline making authority of the Chairperson under the IRPA?
- Evidence: `issue` cue `question` at chunk `4168367` offsets `202-210`; context: The respondent agrees that these be certified in this case and also requests that the third question certified by Justice Blanchard in Thamotharem be again certified, which I agree should be done.
- Evidence: `party_position` cue `submits` at chunk `4168368` offsets `21-28`; context: [240] The respondent submits and I agree, that the questions regarding independence of Board members be re-written as follows: Does the role of Refugee Protection Division members in questioning refugee claimants, as contemplated by Guideline 7, give rise to a reasonable apprehension of bias?

#### 2044:11:subtheme:14 · paragraphs 241-242

- Raw key terms: `question, respondent, adequately, administrative, agree, applicants, board, charter`
- Display key terms: `question, adequately, administrative, agree, charter`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: question, adequately, administrative, agree, charter Position/evidence statements: [241] The respondent submits that the procedural fairness issues raised by the applicants can be dealt with through administrative law principles and therefore resort to the Charter is unnecessary. | [242] The respondent also contends that the vires of Guideline 7 is adequately subsumed under the question dealing with fettering of Board member’s discretion. Rule/authority context: [241] The respondent submits that the procedural fairness issues raised by the applicants can be dealt with through administrative law principles and therefore resort to the Charter is unnecessary. | [242] The respondent also contends that the vires of Guideline 7 is adequately subsumed under the question dealing with fettering of Board member’s discretion. Application context: [241] The respondent submits that the procedural fairness issues raised by the applicants can be dealt with through administrative law principles and therefore resort to the Charter is unnecessary. Evidence spans paragraphs 241-242. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4168369` offsets `58-64`; context: [241] The respondent submits that the procedural fairness issues raised by the applicants can be dealt with through administrative law principles and therefore resort to the Charter is unnecessary.
- Evidence: `party_position` cue `submits` at chunk `4168369` offsets `21-28`; context: [241] The respondent submits that the procedural fairness issues raised by the applicants can be dealt with through administrative law principles and therefore resort to the Charter is unnecessary.
- Evidence: `governing_rule` cue `principles` at chunk `4168369` offsets `135-145`; context: [241] The respondent submits that the procedural fairness issues raised by the applicants can be dealt with through administrative law principles and therefore resort to the Charter is unnecessary.
- Evidence: `reasoning_application` cue `therefore` at chunk `4168369` offsets `150-159`; context: [241] The respondent submits that the procedural fairness issues raised by the applicants can be dealt with through administrative law principles and therefore resort to the Charter is unnecessary.
- Evidence: `issue` cue `question` at chunk `4168370` offsets `98-106`; context: [242] The respondent also contends that the vires of Guideline 7 is adequately subsumed under the question dealing with fettering of Board member’s discretion.
- Evidence: `party_position` cue `contends` at chunk `4168370` offsets `26-34`; context: [242] The respondent also contends that the vires of Guideline 7 is adequately subsumed under the question dealing with fettering of Board member’s discretion.
- Evidence: `governing_rule` cue `under` at chunk `4168370` offsets `88-93`; context: [242] The respondent also contends that the vires of Guideline 7 is adequately subsumed under the question dealing with fettering of Board member’s discretion.

#### 2044:11:subtheme:15 · paragraphs 243-244

- Raw key terms: `citizenship, immigration, minister, able, afforded, alternate, appeal, applicant`
- Display key terms: `able, afforded, alternate`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: able, afforded, alternate Rule/authority context: Does Guideline 7, issued under the authority of the Chairperson of the Immigration and Refugee Board, violate the principles of fundamental justice under s. Application context: Is Guideline 7 unlawful because it is ultra vires the guideline-making authority of the Chairperson under paragraph 159 (1) (h) of the Immigration and Refugee Protection Act? Operative outcome context: Does a finding that Guideline 7 fetters a Refugee Protection Division Member’s discretion necessarily mean that the application for judicial review must be granted, without regard to whether or not the applicant was othe Evidence spans paragraphs 243-244. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4168371` offsets `1021-1028`; context: Does a finding that Guideline 7 fetters a Refugee Protection Division Member’s discretion necessarily mean that the application for judicial review must be granted, without regard to whether or not the applicant was otherwise afforded procedural fairness in the particular case or whether there was an alternate basis for rejecting the claim?
- Evidence: `evidence_fact` cue `RECORD` at chunk `4168371` offsets `1897-1903`; context: Mosley”
Judge
FEDERAL COURT
NAME OF COUNSEL AND SOLICITORS OF RECORD
DOCKET: IMM-9766-04
- Evidence: `governing_rule` cue `under` at chunk `4168371` offsets `352-357`; context: Does Guideline 7, issued under the authority of the Chairperson of the Immigration and Refugee Board, violate the principles of fundamental justice under s.
- Evidence: `reasoning_application` cue `because` at chunk `4168371` offsets `1378-1385`; context: Is Guideline 7 unlawful because it is ultra vires the guideline-making authority of the Chairperson under paragraph 159 (1) (h) of the Immigration and Refugee Protection Act?
- Evidence: `disposition` cue `granted` at chunk `4168371` offsets `994-1001`; context: Does a finding that Guideline 7 fetters a Refugee Protection Division Member’s discretion necessarily mean that the application for judicial review must be granted, without regard to whether or not the applicant was otherwise afforded procedural fairness in the particular case or whether there was an alternate basis for rejecting the claim?

#### Section text

[202] In Farkas, a Board ruling was set aside because of persistent and aggressive questioning by one of the Board members. Similarly in Sandor, the Court found that extensive questioning by a Board member constituted a breach of natural justice and the denial of the right to a fair hearing. But these decisions do not support the proposition that a change in the order of questioning in itself gives rise to a reasonable apprehension of bias.

[203] In my view, the question of bias in this context has to be raised on a case-by-case basis. I note, without deciding the matter, that in the Jones application record there is evidence of what counsel described as “long, nasty, brutish and hostile” examination of the claimant by the Member. That evidence may support a finding that in the particular circumstances of that case, a reasonable apprehension of bias is made out. That is to be decided by the judge hearing the merits of the case. It does not, in my view, support a finding that institutional bias results from the questioning order called for by Guideline 7.
When must an objection to the use of Guideline 7 be raised?

[204] The question of waiver arises in these proceedings because a number of the applicants neither raised an objection to the Guideline 7 procedure at the Board hearing, nor sought a decision to vary the order of questioning from the member. In some cases, it was not raised as a ground for judicial review prior to leave being granted and was raised then only after the reasons for decision in Thamotharem were released.

[205] While I have found that the applicants were not denied procedural fairness by the imposition of Guideline 7 in itself, certain of the applicants may be able to establish a denial of procedural fairness by its application in their particular cases.

[206] Since its implementation in June 2004, this Court has examined Guideline 7 in a number of decisions. The jurisprudence to date has not dealt specifically with the issue of waiver as it relates to an applicant’s ability to argue Guideline 7 upon judicial review. Among the cases, there are two common scenarios in which the Court has addressed Guideline 7. The first scenario is one in which the applicant raised an objection to the implementation of Guideline 7 at the hearing before the Board and the issue of waiver was not dealt with on judicial review. These cases include Thamotharem, Jin, Vazquez, Fabiano and Martinez, all cited above.

[207] The second common scenario is cases in which it is unclear whether the applicant objected to Guideline 7 at the hearing, but the issue was raised in the judicial review of the Board’s decision and the Court dealt with the question of procedural fairness without reference to waiver. These cases include Sy v. Canada (Minister of Citizenship and Immigration), 2005 FC 379, [2005] F.C.J. No. 462 (QL), Liang, and Cortes Silva above.

[208] An implied waiver was addressed in B.D.L, above, where Justice Yvon Pinard stated at para. 5 -6 that because
…the applicant did not think it necessary to object and did not establish the existence of any harm… In view of the particular facts of the case at bar, the argument now relied on by the applicant as to unfairness of the procedure is entirely without basis.

[209] The particular facts in B.D.L were that the applicant not only did not object but in response to questions from the member at the close of the hearing, expressly confirmed that he had said everything he had wanted to.

[210] In two cases which were decided before the implementation of Guideline 7 but which relate to the order of questioning at a refugee hearing, the Court found a breach of the duty of fairness despite a failure to object at the hearing. In Ganji, the Court quashed a decision of the Board in which the Board had seized control of the applicant’s case and conducted the examination. In Herrera, as discussed above, counsel had consented to the procedure without full disclosure of the issues to be raised. The Court refused to give any weight to the consent.

[211] It appears, therefore, that the jurisprudence of this Court regarding when an applicant must raise an objection to the order of questioning in order to have it dealt with upon judicial review is unsettled. In order to arrive at the correct approach to be applied in these consolidated cases I will rely upon the general principles of waiver developed in the jurisprudence.

[212] As observed by the Federal Court of Appeal in Kozak, above at paragraph 66, parties are not normally able to complain of a breach of a duty of procedural fairness by an administrative tribunal if they did not raise it at the earliest reasonable moment.

[213] The principle of common law waiver is described by Justice MacGuigan in In re Human Rights Tribunal and Atomic Energy of Canada Limited, [1986] 1 F.C. 103, (1985) 24 D.L.R. (4th) 675 (F.C.A.), leave to appeal to S.C.C. refused, [1986] 2 S.C.R. v. Justice MacGuigan stated that at common law, even an implied waiver of objection to an adjudicator at the initial stages is sufficient to invalidate a later objection. Justice MacGuigan noted:
The only reasonable course of conduct for a party reasonably apprehensive of bias would be to allege a violation of natural justice at the earliest practicable opportunity. Here, AECL called witnesses, cross-examined the witnesses called by the Commission, made many submissions to the Tribunal, and took proceedings before both the Trial Division and this Court, all without challenge to the independence of the Commission. In short, it ... impliedly ... waived its right to object [emphasis added].

[214] The reasoning of Justice MacGuigan was applied by the Court of Appeal in Yassine v. Canada (Minister of Employment and Immigration) (1994), 172 N.R. 308, 27 Imm. L.R. (2d) 135 where an applicant did not object until after the Refugee Division’s decision was released. Justice Stone for the Court stated at paragraph 7:
It must also be noted that no objection was taken to the procedure that the Presiding Member adopted for receiving the additional information…That surely was the time to raise an objection and to ask the panel to reconvene the hearing, assuming that the information could not otherwise be received. The appellant was then in possession of all of the new information and was aware that the panel intended to take notice of it. Not only was no objection made at that time, which I would regard as the "earliest practicable opportunity" to do so ... the appellant remained silent until after the Refugee Division's decision was released on April 18, 1991. Thus, even if a breach of natural justice did occur, I view the appellant's conduct as an implied waiver of that breach [emphasis added and citation omitted].

[215] The reasoning of the Court of Appeal in Atomic Energy was accepted by the Supreme Court, in Canada (Human Rights Commission) v. Taylor, [1990] 3 S.C.R. 892, 75 D.L.R. (4th) 577.

[216] In Zundel v. Canada (Canadian Human Rights Commission) (re Canadian Jewish Congress) (2000), 195 D.L.R. (4th) 399, 264 N.R. 174 [Zundel] the Court of Appeal considered the question of whether the doctrine of waiver may be relied upon in the face of a finding of reasonable apprehension of bias. The appellant had cited Newfoundland Telephone Co. v. Newfoundland (Board of Commissioners of Public Utilities), [1992] 1 S.C.R. 623, 89 D.L.R. (4th) 289 [Newfoundland Telephone] for the proposition that a finding of bias rendered the hearing void, leaving no room for waiver to operate. Newfoundland Telephone, however, did not address the question of waiver and the objection to the proceedings was raised at the very outset.

[217] In Zundel, the appellant argued that he had not waived his objection and did so promptly once a court ruling favouring his position was handed down in another case. The Court of Appeal noted that it was the framework of the legislation that gave rise to the complaint of unfairness and nothing had prevented the appellant from objecting at the beginning of the proceedings. In those circumstances, waiver was implied.

[218] In concluding his analysis for the Court in Zundel, Justice Stone accepted that any waiver to be effective must be made freely and with full knowledge of all the facts relevant to the decision whether to waive or not. In Kozak, while counsel for the appellants had consented to the procedure, he could not have known of the background facts suggesting bias.

[219] The rationale for why an applicant must raise a violation of natural justice or apprehension of bias at the earliest practical opportunity was articulated by Justice Pelletier (as he was then) in Mohammadian v. Canada (Minister of Citizenship and Immigration), [2000] 3 F.C. 371, 4 Imm. L.R. (3d) 131(F.C.T.D) aff’d [2001] 4 F.C. 85 (F.C.A.), where he stated at paragraph 25:
There is a powerful argument in favour of such a requirement arising from judicial economy. If applicants are permitted to obtain judicial review of adverse decisions by remaining silent in the face of known problems of interpretation, they will remain silent. This will result in a duplication of hearings. It seems a better policy to provide an incentive to make the original hearing as fair as possible and to avoid repetitious proceedings. Applicants should be required to complain at the first opportunity when it is reasonable to expect them to do so.
Justice Pelletier went on to say at para. 26 “[t]he crucial element is the reasonableness of the expectation that the claimant complain at the first opportunity.”

[220] From the above discussion, I would take the principle that an applicant must raise an allegation of bias or other violation of natural justice before the tribunal at the earliest practical opportunity. The earliest practical opportunity arises when the applicant is aware of the relevant information and it is reasonable to expect him or her to raise an objection.

[221] In the present cases, counsel for the applicants would have been aware of the implementation of Guideline 7 from December 7, 2003. If they were of the view that its application in a particular case would result in a denial of their client’s right to a fair hearing, the earliest practical opportunity to raise an objection and to seek an exception from the standard order of questioning would have been in advance of each scheduled hearing, in accordance with Rules 43 and 44, or orally, at the hearing itself. A failure to object at the hearing must be taken as an implied waiver of any perceived unfairness resulting from the application of the Guideline itself.

[222] I wish to stress, however, that the operation of the doctrine of waiver does not preclude an applicant from arguing that the manner in which the hearing was conducted breached the duty of fairness by reason of, for example, badgering cross-examination as was found in Herrera, if that ground is otherwise properly before the Court.

[223] The respondent submits that the Court should not consider grounds for judicial review that were not expressly pleaded in the applications for leave. In these proceedings, several applicants raised the Guideline 7 issue in their memoranda of fact and law or supplementary memoranda for the first time after the release of the decision in Thamotharem.

[224] The applicants rely upon the decision of the Supreme Court in Native Women’s Association of Canada v. Canada [1994] 3 S.C.R. 627, 119 D.L.R. (4th) 224 in which the Court observed that a "basket clause" in the prayer for relief permitted a court to exercise its discretion to grant a declaration even though it was not specifically pleaded. The Court also referred to s.18.1 of the Federal Courts Act, which among other things, sets out the various forms of relief which may be granted an applicant.

[225] The Native Women’s Association decision cannot be extended, in my view, to support the proposition that applicants may raise new grounds that were not specifically pleaded in their applications for judicial review.

[226] Rule 301 of the Federal Court Rules, sets out the requirements for an application for judicial review. It states:
An application shall be commenced by a notice of application in Form 301 setting out
...
(e) a complete and concise statement of the grounds intended to be argued, including reference to any statutory provision or rule to be relied on.

[227] This Court has held that it will only deal with grounds of review raised by the applicant in the notice of application and supporting affidavits: Métis National Council of Women v. Canada (Attorney General), [2005] 4 F.C.R. 272, 2005 FC 230. (See also Schut v. Canada (Attorney General) (2000), 186 F.T.R. 212, [2000] F.C.J. No. 424 (F.C.T.D.) (QL)). The same position has been taken by the Federal Court of Appeal: Canada (Human Rights Commission) v. Pathak, [1995] 2 F.C. 455, 180 N.R. 152, leave to appeal refused [1995] S.C.C.A. No. 306.

[228] I note that in Stumpf v. Canada (Minister of Citizenship and Immigration), 2002 FCA 148, 289 N.R. 165, the Court of Appeal allowed the applicants to raise an issue in oral arguments which had not been raised in the judicial review or in any of the proceedings before the Board. The issue in this case was the failure of the Board to consider the designation of a representative for a minor refugee applicant as required by subsection 69(4) of the Immigration Act, R.S.C. 1985, c. I-2. The Court determined that it was appropriate to consider it at that time because the record disclosed all of the relevant facts, and there was no suggestion that the Minister would be prejudiced if the issue was considered.

[229] It is not clear that the records in each of the 19 applications consolidated disclose all of the relevant facts. For instance, it is not clear through reading the applicable Tribunal Records whether there was evidence before the Board Member of why the order of questioning outlined in Guideline 7 should not be followed in a given case, particularly if it was raised before the hearing. Thus I would conclude that, unlike in Stumpf, the respondent may be prejudiced by the failure of the applicants to raise the issue at an earlier stage of the proceedings.

[230] In Marshall v. Canada (Minister of Citizenship and Immigration) 2004 FC 34, [2004] F.C.J. No. 73 (QL) the Court stated at paragraph 2:
The applicant at the hearing raised the issue of reasonable apprehension of bias by the presiding member. However this issue was not raised in the applicant's original pleadings, but only in a further Memorandum of Argument on behalf of the Applicant filed subsequently to receiving the Minister's Memorandum of Argument. Given that Rule 301(e) requires a complete and concise statement of the grounds intended to be argued, I believe it is too late at this stage as it was not part of the original application. In any event if there was such an issue, it should have been raised by motion before the presiding member and not now on judicial review [emphasis added].

[231] The Court of Appeal has also held that arguments not made before the tribunal cannot be raised on judicial review: Toussaint v. Canada (Labour Relations Board) (1993), 160 N.R. 396 , [1993] F.C.J. No. 616 (QL); Society of Composers, Authors & Music Publishers of Canada v. Canadian Association of Internet Providers (2001), 267 N.R. 82, 2001 FCA 4.

[232] In conclusion, I agree with the respondent that the applicants in this case who did not raise issues of procedural fairness respecting Guideline 7 before the Board and in their Applications for Leave and for Judicial Review should be precluded from doing so by way of written and oral argument at this time. If the objection was made in a timely manner at or before the hearing, the applicants are entitled to raise it as a ground for judicial review in their applications for leave.

[233] While claimants seeking decisions from the Board respecting the procedure to be followed at its hearings should normally follow the requirements set out in RPD Rules 43 and 44, that is by filing a written submission supported by evidence without delay before the hearing, I do not accept the respondent’s submission that failure to do so necessarily invokes the waiver doctrine. As I read the jurisprudence, waiver will not be implied where the party against whom it is claimed has made an objection to the procedure before or during the hearing itself. What the doctrine seeks to prevent is the litigant who sits mute through the procedure and tries to take advantage of the issue before a higher forum.

[234] If the applicants failed to cite a denial of procedural fairness in their applications for leave, judicial review of the applications should be confined to the grounds for which they sought leave. The common “basket clause” formula “such further and other grounds as the applicants may advise and this Honourable Court permit” is not a complete and concise statement of the grounds intended to be argued within the meaning of Rule 301. However, in some cases, the issue was identified in the memorandum of fact and law filed with the application.

[235] In view of the unsettled state of the law on these issues and that prior to Thamotharem this Court had consistently denied applications based solely on Guideline 7, applicants should not be penalized for the failure of counsel to specify the ground in the Notice of Application if it is clear from the materials filed with the application that procedural fairness was in issue. That is not to be taken as an invitation to expand the grounds for which leave has been granted. If the issue of Guideline 7 is only raised in a further memorandum of fact and law filed subsequent to the granting of leave, there has been an implied waiver and the applicants are restricted to the issues identified in the initial application and memorandum.

[236] Turning to the application of these principles to the cases before me, I make the following findings:
Cases in which there was no waiver because of a timely objection at or before the Board hearing and the denial of procedural fairness was identified as a ground for judicial review in the leave application either expressly or through a basket clause: IMM-9766-04 (Restrepo Benitez); IMM-1144-05 (Quadri); IMM-4044-05 (Roy); IMM-470-05 (Martinez & others); IMM-2150-05 (Matheen); IMM-353-05 (Rincon & others); IMM-1419-05 (Gomez & others); IMM-1877-05 (Jones); IMM-712-05 (Guirguis & others); IMM-407-05 (Mejia); IMM-9797-04 (Bilomba); IMM-2709-05 (Trujillo); IMM-2034-05 (Ortiz). These applications are not barred from proceeding on the procedural fairness issue in relation to the application of Guideline 7 in that case.
Cases in which no objection was raised before or during the hearing and for which waiver will be implied: IMM-4064-05 (Kamalendran); IMM-9220-04 & IMM-3994-05 (Arachchige); IMM-3313-05 (Robinson); IMM-9452-04 (Gyankoma); IMM-934-05 (Savagoli). These applications are barred from proceeding on the ground of procedural unfairness in relation to Guideline 7.
Conclusions

[237] Based on the analysis above I make the following findings on each of the issues.
§ Although the order of questioning in refugee determination proceedings engages the security of the person interests of claimants, this case concerns classic administrative law issues that may be determined under the principles of natural justice and fairness without invoking the Charter. It is therefore not necessary for the Court to determine the scope and effect of fundamental justice under section 7 with regard to the application of the Guideline. In the alternative, if a Charter analysis is required, fundamental justice does not require that the questioning order employed in the civil and criminal courts be extended to refugee determination hearings. The legislative intention to avoid the formalities attendant upon court proceedings is not inconsistent with the requirements of fu

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 2044:12 · paragraphs 245-245

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fa9243cb11edafa0856a0d67ebf09c79f7fdfd01aa4c1a5fb131a272f4ab138c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 2044:12:subtheme:1 · paragraphs 245-245

- Raw key terms: `appearances, applicant, april, attorney, barrister, butterfield, canada, catherine`
- Display key terms: `april, barrister, butterfield, catherine`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: april, barrister, butterfield, catherine No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 245-245. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

ORDER: MOSLEY J.
DATED: April 10, 2006
APPEARANCES:
Matthew J. Jeffery
FOR THE APPLICANT
Jamie Todd
Catherine Vasilaros
John Provart
Michael Butterfield
FOR THE RESPONDENT
SOLICITORS OF RECORD:
MATTHEW J. JEFFERY
Barrister & Solicitor
Toronto, Ontario
FOR THE APPLICANT
JOHN H. SIMS, Q.C.
Deputy Attorney General of Canada
Toronto, Ontario
FOR THE RESPONDENT
