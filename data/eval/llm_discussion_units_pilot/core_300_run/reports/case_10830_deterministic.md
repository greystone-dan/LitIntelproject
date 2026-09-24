# Discussion Units: case 10830

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **67**
- Continuity pairs: **66**
- Discussion Units: **6**
- Paragraph source hashes: **67**
- Sub-themes: **23**

## 10830:1 · paragraphs 0-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c8707804e26036d9ebdc1653f2f573cb4d2c060fb615cc499053b218832ca482`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10830:1:subtheme:1 · paragraphs 0-2

- Raw key terms: `decision, huang, immigration, applicant, canada, china, court, minxiang`
- Display key terms: `huang, china, minxiang`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position Display terms: huang, china, minxiang Position/evidence statements: When she arrived in Canada, she claimed refugee protection. | She argues that the PRRA Officer erred in rejecting her new evidence of risk and breached the principles of procedural fairness in failing to convoke an oral hearing. Rule/authority context: She argues that the PRRA Officer erred in rejecting her new evidence of risk and breached the principles of procedural fairness in failing to convoke an oral hearing. Operative outcome context: In December 2015, a panel of the Refugee Protection Division [RPD] of the Immigration and Refugee Board of Canada dismissed her claim on the ground that it lacked credibility. Evidence spans paragraphs 0-2. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4546365` offsets `564-570`; context: The Refugee Appeal Division [RAD] upheld the RPD’s decision on two key credibility issues: (i) Ms.
- Evidence: `party_position` cue `claimed` at chunk `4546365` offsets `94-101`; context: When she arrived in Canada, she claimed refugee protection.
- Evidence: `disposition` cue `dismissed` at chunk `4546365` offsets `419-428`; context: In December 2015, a panel of the Refugee Protection Division [RPD] of the Immigration and Refugee Board of Canada dismissed her claim on the ground that it lacked credibility.
- Evidence: `party_position` cue `argues` at chunk `4546366` offsets `404-410`; context: She argues that the PRRA Officer erred in rejecting her new evidence of risk and breached the principles of procedural fairness in failing to convoke an oral hearing.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546366` offsets `460-468`; context: She argues that the PRRA Officer erred in rejecting her new evidence of risk and breached the principles of procedural fairness in failing to convoke an oral hearing.
- Evidence: `governing_rule` cue `principles` at chunk `4546366` offsets `494-504`; context: She argues that the PRRA Officer erred in rejecting her new evidence of risk and breached the principles of procedural fairness in failing to convoke an oral hearing.

#### 10830:1:subtheme:2 · paragraphs 3-9

- Raw key terms: `evidence, huang, officer, prra, considered, decision, found, application`
- Display key terms: `huang, officer, prra, considered`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: huang, officer, prra, considered Position/evidence statements: The Officer observed that it was not sufficient for the alleged new statements to have been made after the RPD’s decision; the information contained in them also had to be significantly different from what had already be Rule/authority context: The standard of review Application context: There are no grounds to justify this Court’s intervention, and I must therefore dismiss the application for judicial review. | Huang’s statements about the risks she faces in China as a Shouter and her fear that the Chinese authorities kept looking for her, the PRRA Officer noted that the same allegations had been unsuccessfully made to the RPD, Evidence spans paragraphs 3-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4546367` offsets `39-45`; context: Huang’s application raises two issues: (i) did the PRRA Officer err in the assessment of the new evidence submitted by Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546367` offsets `105-113`; context: Huang’s application raises two issues: (i) did the PRRA Officer err in the assessment of the new evidence submitted by Ms.
- Evidence: `issue` cue `question` at chunk `4546368` offsets `498-506`; context: Huang’s evidence insufficient to support her claim and did not question her credibility.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546368` offsets `26-34`; context: [4] Having considered the evidence before the PRRA Officer and the applicable law, I can find no basis for overturning the Decision.
- Evidence: `reasoning_application` cue `therefore` at chunk `4546368` offsets `594-603`; context: There are no grounds to justify this Court’s intervention, and I must therefore dismiss the application for judicial review.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546369` offsets `63-71`; context: [5] In the Decision, the PRRA Officer considered the following evidence presented by Ms.
- Evidence: `evidence_fact` cue `found that` at chunk `4546370` offsets `27-37`; context: [6] The PRRA Officer first found that the undated photographs of Ms.
- Evidence: `party_position` cue `submitted` at chunk `4546371` offsets `546-555`; context: The Officer observed that it was not sufficient for the alleged new statements to have been made after the RPD’s decision; the information contained in them also had to be significantly different from what had already been previously submitted by Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546371` offsets `302-310`; context: Huang’s statements about the risks she faces in China as a Shouter and her fear that the Chinese authorities kept looking for her, the PRRA Officer noted that the same allegations had been unsuccessfully made to the RPD, and concluded that this therefore did not qualify as new evidence.
- Evidence: `reasoning_application` cue `therefore` at chunk `4546371` offsets `269-278`; context: Huang’s statements about the risks she faces in China as a Shouter and her fear that the Chinese authorities kept looking for her, the PRRA Officer noted that the same allegations had been unsuccessfully made to the RPD, and concluded that this therefore did not qualify as new evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546372` offsets `110-118`; context: Huang did not qualify as new evidence, even though they postdated the RPD’s decision.
- Evidence: `counterargument_limitation` cue `but` at chunk `4546372` offsets `207-210`; context: The PRRA Officer analyzed the articles, but concluded that they did not demonstrate how Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546373` offsets `30-38`; context: [9] Having considered all the evidence, the PRRA Officer found that Ms.
- Evidence: `governing_rule` cue `standard of review` at chunk `4546373` offsets `250-268`; context: The standard of review

#### 10830:1:subtheme:3 · paragraphs 10-11

- Raw key terms: `assessment, canada, dunsmuir, evidence, immigration, mixed, officers, para`
- Display key terms: `assessment, dunsmuir, mixed, officers, para`
- Argument roles: `evidence_fact, governing_rule, issue`
- Explanation: Observed roles: evidence_fact, governing_rule, issue Display terms: assessment, dunsmuir, mixed, officers, para Rule/authority context: [10] It is well-recognized by the case law that PRRA applications involve questions of mixed facts and law, and that the standard of review applicable to the assessment of the evidence by PRRA officers is reasonableness  | Under a reasonableness review, when a question of mixed fact and law falls squarely within the expertise of a decision-maker, “the reviewing court’s task is to supervise the tribunal’s approach in the context of the deci Evidence spans paragraphs 10-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4546374` offsets `567-572`; context: As a result, there is no need to proceed to a further analysis of the standard of review applicable to the first issue raised by Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546374` offsets `176-184`; context: [10] It is well-recognized by the case law that PRRA applications involve questions of mixed facts and law, and that the standard of review applicable to the assessment of the evidence by PRRA officers is reasonableness (Flores Carrillo v Canada (Minister of Citizenship and Immigration, 2008 FCA 94 at para 36; Benko v Canada (Citizenship and Immigration), 2017 FC 1032 at para 15; Fares v Canada (Citizenship and Immigration), 2017 FC 797 at para 19).
- Evidence: `governing_rule` cue `standard of review` at chunk `4546374` offsets `121-139`; context: [10] It is well-recognized by the case law that PRRA applications involve questions of mixed facts and law, and that the standard of review applicable to the assessment of the evidence by PRRA officers is reasonableness (Flores Carrillo v Canada (Minister of Citizenship and Immigration, 2008 FCA 94 at para 36; Benko v Canada (Citizenship and Immigration), 2017 FC 1032 at para 15; Fares v Canada (Citizenship and Immigration), 2017 FC 797 at para 19).
- Evidence: `issue` cue `question` at chunk `4546375` offsets `658-666`; context: Under a reasonableness review, when a question of mixed fact and law falls squarely within the expertise of a decision-maker, “the reviewing court’s task is to supervise the tribunal’s approach in the context of the decision as a whole.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546375` offsets `1139-1147`; context: In such circumstances, a high degree of deference is owed to the PRRA officers’ factual findings and assessment of the evidence.
- Evidence: `governing_rule` cue `Under` at chunk `4546375` offsets `620-625`; context: Under a reasonableness review, when a question of mixed fact and law falls squarely within the expertise of a decision-maker, “the reviewing court’s task is to supervise the tribunal’s approach in the context of the decision as a whole.

#### 10830:1:subtheme:4 · paragraphs 12-14

- Raw key terms: `application, decision, hearing, prra, allowing, applicant, central, context`
- Display key terms: `hearing, prra, allowing, central, context`
- Argument roles: `evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, reasoning_application Display terms: hearing, prra, allowing, central, context Rule/authority context: [12] Turning to the decision to hold an oral hearing in the context of a PRRA application, the jurisprudence of this Court regarding the applicable standard of review has been mixed. | They read as follows: 113 Consideration of an application for protection shall be as follows: 113 Il est disposé de la demande comme il suit : (…) (…) (b) a hearing may be held if the Minister, on the basis of prescribed Application context: As summarized by Justice Boswell in Zmari v Canada (Citizenship and Immigration), 2016 FC 132 [Zmari], some decisions apply the standard of correctness because the issue is characterized as a matter of procedural fairnes Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4546376` offsets `359-364`; context: The turbulence in the case law, and the diverging views on the selection of the applicable standard of review, result from the different approaches taken in characterizing the issue at stake.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4546376` offsets `95-108`; context: [12] Turning to the decision to hold an oral hearing in the context of a PRRA application, the jurisprudence of this Court regarding the applicable standard of review has been mixed.
- Evidence: `reasoning_application` cue `apply` at chunk `4546376` offsets `493-498`; context: As summarized by Justice Boswell in Zmari v Canada (Citizenship and Immigration), 2016 FC 132 [Zmari], some decisions apply the standard of correctness because the issue is characterized as a matter of procedural fairness, whereas others apply the standard of reasonableness because the issue is viewed as a question of mixed law and facts involving the interpretation of the IRPA (Zmari at paras 10-13).
- Evidence: `issue` cue `whether` at chunk `4546377` offsets `647-654`; context: They read as follows:
113 Consideration of an application for protection shall be as follows:
113 Il est disposé de la demande comme il suit :
(…)
(…)
(b) a hearing may be held if the Minister, on the basis of prescribed factors, is of the opinion that a hearing is required;
b) une audience peut être tenue si le ministre l’estime requis compte tenu des facteurs réglementaires;
(…)
(…)
167 For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
167 Pour l’application de l’alinéa 113b) de la Loi, les facteurs ci-après servent à décider si la tenue d’une audience est requise :
(a) whether there is evidence that raises a serious issue of the applicant’s credibility and is related to the factors set out in sections 96 and 97 of the Act;
a) l’existence d’éléments de preuve relatifs aux éléments mentionnés aux articles 96 et 97 de la Loi qui soulèvent une question importante en ce qui concerne la crédibilité du demandeur;
(b) whether the evidence is central to the decision with respect to the application for protection; and
b) l’importance de ces éléments de preuve pour la prise de la décision relative à la demande de protection;
(c) whether the evidence, if accepted, would justify allowing the application for protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546377` offsets `897-905`; context: They read as follows:
113 Consideration of an application for protection shall be as follows:
113 Il est disposé de la demande comme il suit :
(…)
(…)
(b) a hearing may be held if the Minister, on the basis of prescribed factors, is of the opinion that a hearing is required;
b) une audience peut être tenue si le ministre l’estime requis compte tenu des facteurs réglementaires;
(…)
(…)
167 For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
167 Pour l’application de l’alinéa 113b) de la Loi, les facteurs ci-après servent à décider si la tenue d’une audience est requise :
(a) whether there is evidence that raises a serious issue of the applicant’s credibility and is related to the factors set out in sections 96 and 97 of the Act;
a) l’existence d’éléments de preuve relatifs aux éléments mentionnés aux articles 96 et 97 de la Loi qui soulèvent une question importante en ce qui concerne la crédibilité du demandeur;
(b) whether the evidence is central to the decision with respect to the application for protection; and
b) l’importance de ces éléments de preuve pour la prise de la décision relative à la demande de protection;
(c) whether the evidence, if accepted, would justify allowing the application for protection.
- Evidence: `governing_rule` cue `under` at chunk `4546377` offsets `677-682`; context: They read as follows:
113 Consideration of an application for protection shall be as follows:
113 Il est disposé de la demande comme il suit :
(…)
(…)
(b) a hearing may be held if the Minister, on the basis of prescribed factors, is of the opinion that a hearing is required;
b) une audience peut être tenue si le ministre l’estime requis compte tenu des facteurs réglementaires;
(…)
(…)
167 For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
167 Pour l’application de l’alinéa 113b) de la Loi, les facteurs ci-après servent à décider si la tenue d’une audience est requise :
(a) whether there is evidence that raises a serious issue of the applicant’s credibility and is related to the factors set out in sections 96 and 97 of the Act;
a) l’existence d’éléments de preuve relatifs aux éléments mentionnés aux articles 96 et 97 de la Loi qui soulèvent une question importante en ce qui concerne la crédibilité du demandeur;
(b) whether the evidence is central to the decision with respect to the application for protection; and
b) l’importance de ces éléments de preuve pour la prise de la décision relative à la demande de protection;
(c) whether the evidence, if accepted, would justify allowing the application for protection.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546378` offsets `134-142`; context: [14] Section 167 of the IRP Regulations thus expressly provides that a hearing is required when three enumerated factors are present: evidence going to the credibility of the applicant, central to the decision, and able to justify allowing the PRRA application.

#### Section text

Huang v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2018-09-20
Neutral citation
2018 FC 940
File numbers
IMM-325-18
Decision Content
Date: 20180920
Docket: IMM-325-18
Citation: 2018 FC 940
Montréal, Quebec, September 20, 2018
PRESENT: The Honourable Mr. Justice Gascon
BETWEEN:
MINXIANG HUANG
Applicant
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Overview

[1] The applicant, Ms. Minxiang Huang, is a citizen of China. When she arrived in Canada, she claimed refugee protection. She said that she feared persecution by the Chinese authorities based on her participation, when she lived in China, in a banned Christian underground church known as the “Shouters”. In December 2015, a panel of the Refugee Protection Division [RPD] of the Immigration and Refugee Board of Canada dismissed her claim on the ground that it lacked credibility. The Refugee Appeal Division [RAD] upheld the RPD’s decision on two key credibility issues: (i) Ms. Huang was not likely wanted by the Public Security Bureau [PSB] in China since she fled the country using her own passport, and (ii) her religious beliefs would not require her to join and attend a Shouters church upon return to China since she had attended a non-Shouters church while in Canada.

[2] Ms. Huang then made a Pre-Removal Risk Assessment [PRRA] application. In September 2017, a senior immigration officer [Officer] rejected her PRRA application on the basis that she would not be subject to risk of persecution, danger of torture, risk to life or of cruel and unusual treatment or punishment if returned to China [Decision]. Ms. Huang now seeks judicial review of the PRRA Decision. She argues that the PRRA Officer erred in rejecting her new evidence of risk and breached the principles of procedural fairness in failing to convoke an oral hearing. She asks this Court to quash the Decision and to send it back for redetermination by a different PRRA officer.

[3] Ms. Huang’s application raises two issues: (i) did the PRRA Officer err in the assessment of the new evidence submitted by Ms. Huang?; (ii) did the PRRA Officer err and deny procedural fairness by failing to hold an oral hearing?

[4] Having considered the evidence before the PRRA Officer and the applicable law, I can find no basis for overturning the Decision. The Officer’s findings with respect to Ms. Huang’s new evidence are reasonable in the circumstances and fall within the range of possible, acceptable outcomes defensible based on the facts and the law. In addition, I am satisfied that no oral hearing was required in this case as the Officer found Ms. Huang’s evidence insufficient to support her claim and did not question her credibility. There are no grounds to justify this Court’s intervention, and I must therefore dismiss the application for judicial review.
II. Background
A. The PRRA Decision

[5] In the Decision, the PRRA Officer considered the following evidence presented by Ms. Huang: (i) various photographs of her baptism at a Toronto church, (ii) additional statements of Ms. Huang about the risks she faces in China, including information allegedly reported by her mother, and (iii) news articles about the Chinese authorities launching a large scale suppression of underground churches in 2016.

[6] The PRRA Officer first found that the undated photographs of Ms. Huang’s baptism did not constitute new evidence, since a letter from the church confirmed that the baptism occurred in October 2015. This event thus happened before Ms. Huang amended her refugee application and had her hearing at the RPD.

[7] With respect to Ms. Huang’s statements about the risks she faces in China as a Shouter and her fear that the Chinese authorities kept looking for her, the PRRA Officer noted that the same allegations had been unsuccessfully made to the RPD, and concluded that this therefore did not qualify as new evidence. The Officer observed that it was not sufficient for the alleged new statements to have been made after the RPD’s decision; the information contained in them also had to be significantly different from what had already been previously submitted by Ms. Huang (Raza v Canada (Citizenship and Immigration), 2006 FC 1385 [Raza FC] at para 22). The PRRA Officer looked more specifically at Ms. Huang’s statement reporting that her mother had informed her that the PSB was still looking for her in China. Again, the Officer found that this did not amount to new evidence, as Ms. Huang simply repeated what had been already considered (and rejected) by the RPD and the RAD. The Officer further concluded that Ms. Huang had not provided “sufficient objective evidence to support her statements” in that regard, such as an affidavit sworn by her mother. Therefore, there was “insufficient evidence” to establish that the Chinese authorities were looking for Ms. Huang.

[8] Finally, the PRRA Officer considered that the news articles submitted by Ms. Huang did not qualify as new evidence, even though they postdated the RPD’s decision. The PRRA Officer analyzed the articles, but concluded that they did not demonstrate how Ms. Huang fitted with the profile of the persecuted Christians described in the materials.

[9] Having considered all the evidence, the PRRA Officer found that Ms. Huang provided insufficient new materials to demonstrate that she would face risks and be persecuted, due to her purported religious identity, should she return to China.
B. The standard of review

[10] It is well-recognized by the case law that PRRA applications involve questions of mixed facts and law, and that the standard of review applicable to the assessment of the evidence by PRRA officers is reasonableness (Flores Carrillo v Canada (Minister of Citizenship and Immigration, 2008 FCA 94 at para 36; Benko v Canada (Citizenship and Immigration), 2017 FC 1032 at para 15; Fares v Canada (Citizenship and Immigration), 2017 FC 797 at para 19). As a result, there is no need to proceed to a further analysis of the standard of review applicable to the first issue raised by Ms. Huang (Dunsmuir v New Brunswick, 2008 SCC 9 [Dunsmuir] at para 62).

[11] The standard of reasonableness requires to show deference to the decision-maker as it is “grounded in the legislature’s choice to give a specialized tribunal responsibility for administering the statutory provisions, and the expertise of the tribunal in so doing” (Edmonton (City) v Edmonton East (Capilano) Shopping Centres Ltd, 2016 SCC 47 [City of Edmonton] at para 33; Dunsmuir at paras 48-49). Since the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA] is the enabling statute that PRRA officers are mandated to enforce, its interpretation and application fall within their core area of expertise. Under a reasonableness review, when a question of mixed fact and law falls squarely within the expertise of a decision-maker, “the reviewing court’s task is to supervise the tribunal’s approach in the context of the decision as a whole. Its role is not to impose an approach of its own choosing” (Canada (Canadian Human Rights Commission) v Canada (Attorney General), 2018 SCC 31 [CHRC] at para 57). In such circumstances, a high degree of deference is owed to the PRRA officers’ factual findings and assessment of the evidence.

[12] Turning to the decision to hold an oral hearing in the context of a PRRA application, the jurisprudence of this Court regarding the applicable standard of review has been mixed. The turbulence in the case law, and the diverging views on the selection of the applicable standard of review, result from the different approaches taken in characterizing the issue at stake. As summarized by Justice Boswell in Zmari v Canada (Citizenship and Immigration), 2016 FC 132 [Zmari], some decisions apply the standard of correctness because the issue is characterized as a matter of procedural fairness, whereas others apply the standard of reasonableness because the issue is viewed as a question of mixed law and facts involving the interpretation of the IRPA (Zmari at paras 10-13). The Court continues to be divided since Zmari, with some decisions applying correctness (for example, Mudiyanselage v Canada (Citizenship and Immigration), 2018 FC 749 at para 11; Nadarajan v Canada (Public Safety and Emergency Preparedness), 2017 FC 403 [Nadarajan] at paras 12-17), and others applying reasonableness (for example, Haji v Canada (Citizenship and Immigration), 2018 FC 474 at para 9; Gjoka v Canada (Citizenship and Immigration), 2018 FC 292 at para 12; Lionel v Canada (Public Safety and Emergency Preparedness), 2017 FC 1180 at para 11; AB v Canada (Citizenship and Immigration), 2017 FC 629 at paras 13-17).

[13] In the context of a PRRA application, the right to an oral hearing finds its source in paragraph 113(b) of the IRPA and section 167 of the Immigration and Refugee Protection Regulations, SOR/2002-227 [IRP Regulations]. They read as follows:
113 Consideration of an application for protection shall be as follows:
113 Il est disposé de la demande comme il suit :
(…)
(…)
(b) a hearing may be held if the Minister, on the basis of prescribed factors, is of the opinion that a hearing is required;
b) une audience peut être tenue si le ministre l’estime requis compte tenu des facteurs réglementaires;
(…)
(…)
167 For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
167 Pour l’application de l’alinéa 113b) de la Loi, les facteurs ci-après servent à décider si la tenue d’une audience est requise :
(a) whether there is evidence that raises a serious issue of the applicant’s credibility and is related to the factors set out in sections 96 and 97 of the Act;
a) l’existence d’éléments de preuve relatifs aux éléments mentionnés aux articles 96 et 97 de la Loi qui soulèvent une question importante en ce qui concerne la crédibilité du demandeur;
(b) whether the evidence is central to the decision with respect to the application for protection; and
b) l’importance de ces éléments de preuve pour la prise de la décision relative à la demande de protection;
(c) whether the evidence, if accepted, would justify allowing the application for protection.
c) la question de savoir si ces éléments de preuve, à supposer qu’ils soient admis, justifieraient que soit accordée la protection.

[14] Section 167 of the IRP Regulations thus expressly provides that a hearing is required when three enumerated factors are present: evidence going to the credibility of the applicant, central to the decision, and able to justify allowing the PRRA application.

## 10830:2 · paragraphs 15-17

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `28361fb7e62eaba38baa630a8cce38f7fed9b0c03344782b5007a409165f188d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10830:2:subtheme:1 · paragraphs 15-16

- Raw key terms: `applies, case, factors, first, interpretation, issue, raised, reasonableness`
- Display key terms: `applies, case, factors, first, interpretation, raised, reasonableness`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: applies, case, factors, first, interpretation, raised, reasonableness Rule/authority context: Since Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61, the Supreme Court has stated many times that, when an administrative tribunal interprets or applies its home statute, the Application context: [15] It is no longer disputed that, whenever a matter is considered as one of statutory interpretation, the reasonableness standard presumably applies. | [16] In my view, when the issue raised on judicial review is whether a PRRA officer should have granted an oral hearing, the standard of reasonableness applies: the decision on that issue turns on the interpretation and  Operative outcome context: [16] In my view, when the issue raised on judicial review is whether a PRRA officer should have granted an oral hearing, the standard of reasonableness applies: the decision on that issue turns on the interpretation and  Evidence spans paragraphs 15-16. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4546379` offsets `1103-1109`; context: Such is the case when a contextual analysis reveals a clear intent of Parliament not to protect the administrative tribunal’s authority with respect to certain issues; when several courts have competing and non-exclusive jurisdiction on a point of law; when an issue raised is a general question of law that is of central importance to the legal system as a whole and outside the area of expertise of the specialized administrative tribunal; or when a constitutional question relating to the division of powers is at play (CHRC at para 28; City of Edmonton at para 24; in Dunsmuir at paras 58-61).
- Evidence: `governing_rule` cue `standard of review` at chunk `4546379` offsets `412-430`; context: Since Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61, the Supreme Court has stated many times that, when an administrative tribunal interprets or applies its home statute, there is a presumption that the applicable standard of review is reasonableness (CHRC at para 27; City of Edmonton at paras 22-23; Commission scolaire de Laval v Syndicat de l’enseignement de la région de Laval, 2016 SCC 8 at para 32; Wilson v British Columbia (Superintendent of Motor Vehicles), 2015 SCC 47 at para 17).
- Evidence: `reasoning_application` cue `applies` at chunk `4546379` offsets `143-150`; context: [15] It is no longer disputed that, whenever a matter is considered as one of statutory interpretation, the reasonableness standard presumably applies.
- Evidence: `issue` cue `issue` at chunk `4546380` offsets `26-31`; context: [16] In my view, when the issue raised on judicial review is whether a PRRA officer should have granted an oral hearing, the standard of reasonableness applies: the decision on that issue turns on the interpretation and application of the officer’s governing legislation, namely paragraph 113(b) of the IRPA providing that a hearing may be held if the minister, on the basis of the specific factors prescribed in section 167 of the IRP Regulations, is of the opinion that a hearing is required.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546380` offsets `621-629`; context: Huang focused on the first of these factors, namely whether there was evidence that raised a serious issue of her credibility, and in particular whether the PRRA Officer’s reasoning, which is expressed in terms of sufficiency of evidence, should be more properly characterized as a veiled credibility finding.
- Evidence: `reasoning_application` cue `applies` at chunk `4546380` offsets `152-159`; context: [16] In my view, when the issue raised on judicial review is whether a PRRA officer should have granted an oral hearing, the standard of reasonableness applies: the decision on that issue turns on the interpretation and application of the officer’s governing legislation, namely paragraph 113(b) of the IRPA providing that a hearing may be held if the minister, on the basis of the specific factors prescribed in section 167 of the IRP Regulations, is of the opinion that a hearing is required.
- Evidence: `disposition` cue `granted` at chunk `4546380` offsets `96-103`; context: [16] In my view, when the issue raised on judicial review is whether a PRRA officer should have granted an oral hearing, the standard of reasonableness applies: the decision on that issue turns on the interpretation and application of the officer’s governing legislation, namely paragraph 113(b) of the IRPA providing that a hearing may be held if the minister, on the basis of the specific factors prescribed in section 167 of the IRP Regulations, is of the opinion that a hearing is required.

#### 10830:2:subtheme:2 · paragraphs 17-17

- Raw key terms: `below, conclusions, considered, detail, duty, even, explained, fairness`
- Display key terms: `below, conclusions, considered, detail, duty, even, explained, fairness`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: below, conclusions, considered, detail, duty, even, explained, fairness Rule/authority context: [17] However, I pause to note that, as explained in more detail below, my conclusions would remain the same even if I had considered the oral hearing issue under the lens of the duty of procedural fairness. Evidence spans paragraphs 17-17. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4546381` offsets `150-155`; context: [17] However, I pause to note that, as explained in more detail below, my conclusions would remain the same even if I had considered the oral hearing issue under the lens of the duty of procedural fairness.
- Evidence: `governing_rule` cue `under` at chunk `4546381` offsets `156-161`; context: [17] However, I pause to note that, as explained in more detail below, my conclusions would remain the same even if I had considered the oral hearing issue under the lens of the duty of procedural fairness.

#### Section text

[15] It is no longer disputed that, whenever a matter is considered as one of statutory interpretation, the reasonableness standard presumably applies. Since Alberta (Information and Privacy Commissioner) v Alberta Teachers’ Association, 2011 SCC 61, the Supreme Court has stated many times that, when an administrative tribunal interprets or applies its home statute, there is a presumption that the applicable standard of review is reasonableness (CHRC at para 27; City of Edmonton at paras 22-23; Commission scolaire de Laval v Syndicat de l’enseignement de la région de Laval, 2016 SCC 8 at para 32; Wilson v British Columbia (Superintendent of Motor Vehicles), 2015 SCC 47 at para 17). This presumption can only be overruled – and the standard of correctness applied – when the reviewing court is confronted with one of the four factors first set out by the Supreme Court in Dunsmuir and recently reiterated in CHRC and City of Edmonton. Such is the case when a contextual analysis reveals a clear intent of Parliament not to protect the administrative tribunal’s authority with respect to certain issues; when several courts have competing and non-exclusive jurisdiction on a point of law; when an issue raised is a general question of law that is of central importance to the legal system as a whole and outside the area of expertise of the specialized administrative tribunal; or when a constitutional question relating to the division of powers is at play (CHRC at para 28; City of Edmonton at para 24; in Dunsmuir at paras 58-61). The issue before this Court does not fall in any of these four categories.

[16] In my view, when the issue raised on judicial review is whether a PRRA officer should have granted an oral hearing, the standard of reasonableness applies: the decision on that issue turns on the interpretation and application of the officer’s governing legislation, namely paragraph 113(b) of the IRPA providing that a hearing may be held if the minister, on the basis of the specific factors prescribed in section 167 of the IRP Regulations, is of the opinion that a hearing is required. In this case, it is even more so as the argument of Ms. Huang focused on the first of these factors, namely whether there was evidence that raised a serious issue of her credibility, and in particular whether the PRRA Officer’s reasoning, which is expressed in terms of sufficiency of evidence, should be more properly characterized as a veiled credibility finding.

[17] However, I pause to note that, as explained in more detail below, my conclusions would remain the same even if I had considered the oral hearing issue under the lens of the duty of procedural fairness.


## 10830:3 · paragraphs 18-23

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `fb41455d872360d76476a9afdcb9b2cf79524efc62a5bbd3a196afea5400f168`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10830:3:subtheme:1 · paragraphs 18-23

- Raw key terms: `evidence, paragraph, prra, irpa, officer, appeal, applicant, application`
- Display key terms: `paragraph, prra, irpa, officer`
- Argument roles: `evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, reasoning_application Display terms: paragraph, prra, irpa, officer Rule/authority context: Huang claims that the Officer erred in concluding that her evidence and allegations were not “new” pursuant to paragraph 113(a) of the IRPA because they spoke to the same risks already considered by the RPD. | [21] In Raza v Canada (Citizenship and Immigration), 2007 FCA 385 [Raza], the Federal Court of Appeal established five criteria to be met for evidence to qualify as “new evidence” admissible under paragraph 113(a) of the Application context: Huang claims that the Officer erred in concluding that her evidence and allegations were not “new” pursuant to paragraph 113(a) of the IRPA because they spoke to the same risks already considered by the RPD. | (b) If the evidence is capable of proving an event that occurred or circumstances that arose after the RPD hearing, then the evidence must be considered (unless it is rejected because it is not credible, not relevant, no Evidence spans paragraphs 18-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546381` offsets `265-273`; context: The PRRA Officer’s assessment of the new evidence was reasonable
- Evidence: `evidence_fact` cue `evidence` at chunk `4546382` offsets `45-53`; context: [18] On the PRRA Officer’s assessment of the evidence, Ms.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4546382` offsets `158-169`; context: Huang claims that the Officer erred in concluding that her evidence and allegations were not “new” pursuant to paragraph 113(a) of the IRPA because they spoke to the same risks already considered by the RPD.
- Evidence: `reasoning_application` cue `because` at chunk `4546382` offsets `199-206`; context: Huang claims that the Officer erred in concluding that her evidence and allegations were not “new” pursuant to paragraph 113(a) of the IRPA because they spoke to the same risks already considered by the RPD.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546384` offsets `184-192`; context: [20] As a PRRA application is not an appeal or reconsideration of the RPD decision rejecting a claim for refugee protection, paragraph 113(a) of the IRPA prescribes some limits to the evidence that may be presented to PRRA officers.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546385` offsets `142-150`; context: [21] In Raza v Canada (Citizenship and Immigration), 2007 FCA 385 [Raza], the Federal Court of Appeal established five criteria to be met for evidence to qualify as “new evidence” admissible under paragraph 113(a) of the IRPA.
- Evidence: `governing_rule` cue `under` at chunk `4546385` offsets `191-196`; context: [21] In Raza v Canada (Citizenship and Immigration), 2007 FCA 385 [Raza], the Federal Court of Appeal established five criteria to be met for evidence to qualify as “new evidence” admissible under paragraph 113(a) of the IRPA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546386` offsets `168-176`; context: [13] As I read paragraph 113(a), it is based on the premise that a negative refugee determination by the RPD must be respected by the PRRA officer, unless there is new evidence of facts that might have affected the outcome of the RPD hearing if the evidence had been presented to the RPD.
- Evidence: `reasoning_application` cue `because` at chunk `4546386` offsets `2139-2146`; context: (b) If the evidence is capable of proving an event that occurred or circumstances that arose after the RPD hearing, then the evidence must be considered (unless it is rejected because it is not credible, not relevant, not new or not material).

#### Section text

III. Analysis
A. The PRRA Officer’s assessment of the new evidence was reasonable

[18] On the PRRA Officer’s assessment of the evidence, Ms. Huang claims that the Officer erred in concluding that her evidence and allegations were not “new” pursuant to paragraph 113(a) of the IRPA because they spoke to the same risks already considered by the RPD. According to her, the fact that the RPD found insufficient credible evidence that she is at risk in China was not a sufficient basis for rejecting evidence of events that happened after the RPD’s decision, namely the crackdown on underground churches in China and the Chinese officials continuing to look for her. Relying notably on this Court’s decision in Cho v Canada (Immigration, Refugees and Citizenship), 2017 FC 1051 [Cho], Ms. Huang pleads that it was unreasonable for the PRRA Officer not to consider evidence of new facts because they related to facts already found not to be credible by the RPD.

[19] I do not agree with Ms. Huang.

[20] As a PRRA application is not an appeal or reconsideration of the RPD decision rejecting a claim for refugee protection, paragraph 113(a) of the IRPA prescribes some limits to the evidence that may be presented to PRRA officers. The provision expressly states that “an applicant whose claim to refugee protection has been rejected may present only new evidence that arose after the rejection or was not reasonably available, or that the applicant could not reasonably have been expected in the circumstances to have presented, at the time of the rejection” [my emphasis].

[21] In Raza v Canada (Citizenship and Immigration), 2007 FCA 385 [Raza], the Federal Court of Appeal established five criteria to be met for evidence to qualify as “new evidence” admissible under paragraph 113(a) of the IRPA. These cumulative criteria are: credibility, relevance, newness, materiality and express statutory conditions (Raza at para 13):

[13] As I read paragraph 113(a), it is based on the premise that a negative refugee determination by the RPD must be respected by the PRRA officer, unless there is new evidence of facts that might have affected the outcome of the RPD hearing if the evidence had been presented to the RPD. Paragraph 113(a) asks a number of questions, some expressly and some by necessary implication, about the proposed new evidence. I summarize those questions as follows:
1. Credibility: Is the evidence credible, considering its source and the circumstances in which it came into existence? If not, the evidence need not be considered.
2. Relevance: Is the evidence relevant to the PRRA application, in the sense that it is capable of proving or disproving a fact that is relevant to the claim for protection? If not, the evidence need not be considered.
3. Newness: Is the evidence new in the sense that it is capable of:
(a) proving the current state of affairs in the country of removal or an event that occurred or a circumstance that arose after the hearing in the RPD, or
(b) proving a fact that was unknown to the refugee claimant at the time of the RPD hearing, or
(c) contradicting a finding of fact by the RPD (including a credibility finding)?
If not, the evidence need not be considered.
4. Materiality: Is the evidence material, in the sense that the refugee claim probably would have succeeded if the evidence had been made available to the RPD? If not, the evidence need not be considered.
5. Express statutory conditions:
(a) If the evidence is capable of proving only an event that occurred or circumstances that arose prior to the RPD hearing, then has the applicant established either that the evidence was not reasonably available to him or her for presentation at the RPD hearing, or that he or she could not reasonably have been expected in the circumstances to have presented the evidence at the RPD hearing? If not, the evidence need not be considered.
(b) If the evidence is capable of proving an event that occurred or circumstances that arose after the RPD hearing, then the evidence must be considered (unless it is rejected because it is not credible, not relevant, not new or not material).

## 10830:4 · paragraphs 24-63

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `691479f37989cf1816b0a808dcd6fa30aa1192ca2ec3b65a6a768fdfb8c5ab66`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10830:4:subtheme:1 · paragraphs 24-26

- Raw key terms: `admissible, evidence, found, claim, criteria, huang, meet, officer`
- Display key terms: `admissible, criteria, huang, meet, officer`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, reasoning_application Display terms: admissible, criteria, huang, meet, officer Rule/authority context: Once evidence is found to be admissible under the Raza criteria, the PRRA officers must then decide if the evidence is sufficient to meet the burden of proof (i. | This evidence was therefore not admissible under paragraph 113(a) of the IRPA as it did not arise after the rejection of Ms. Application context: Huang because it did not meet the “newness” or “materiality” criteria identified in Raza. | This evidence was therefore not admissible under paragraph 113(a) of the IRPA as it did not arise after the rejection of Ms. Evidence spans paragraphs 24-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546387` offsets `78-86`; context: [22] The five criteria established in Raza are conditions of admissibility of evidence when a PRRA application follows a rejected refugee claim (Canada (Citizenship and Immigration) v Singh, 2016 FCA 96 [Singh] at para 38).
- Evidence: `governing_rule` cue `under` at chunk `4546387` offsets `264-269`; context: Once evidence is found to be admissible under the Raza criteria, the PRRA officers must then decide if the evidence is sufficient to meet the burden of proof (i.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546388` offsets `41-49`; context: [23] Here, the PRRA Officer rejected the evidence presented by Ms.
- Evidence: `reasoning_application` cue `because` at chunk `4546388` offsets `73-80`; context: Huang because it did not meet the “newness” or “materiality” criteria identified in Raza.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546389` offsets `79-87`; context: Huang as “new evidence”, but found that these photographs were undated and unlabelled.
- Evidence: `governing_rule` cue `under` at chunk `4546389` offsets `332-337`; context: This evidence was therefore not admissible under paragraph 113(a) of the IRPA as it did not arise after the rejection of Ms.
- Evidence: `reasoning_application` cue `therefore` at chunk `4546389` offsets `307-316`; context: This evidence was therefore not admissible under paragraph 113(a) of the IRPA as it did not arise after the rejection of Ms.
- Evidence: `counterargument_limitation` cue `but` at chunk `4546389` offsets `90-93`; context: Huang as “new evidence”, but found that these photographs were undated and unlabelled.

#### 10830:4:subtheme:2 · paragraphs 27-33

- Raw key terms: `officer, prra, decision, evidence, huang, find, found, china`
- Display key terms: `officer, prra, huang, find, china`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: officer, prra, huang, find, china Rule/authority context: Huang failed to meet her burden of proving these allegations on a balance of probabilities and that the evidence she presented could not be considered “new” pursuant to paragraph 113(a) of the IRPA and capable of proving | Under a reasonableness standard, as long as the process and outcome fit comfortably with the principles of justification, transparency and intelligibility, a reviewing court should not substitute its own view of a prefer Application context: Huang argues, the evidence was not rejected because the RPD had already found not credible that she was at risk in China. | Huang was relying on a declaration made by her mother, I find nothing unreasonable in the PRRA Officer’s finding that that Ms. Evidence spans paragraphs 27-33. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4546390` offsets `229-234`; context: I acknowledge that the statements at issue postdate the RPD decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546390` offsets `98-106`; context: Huang, the PRRA Officer concluded that this evidence could not qualify as “new” it did not amount to significantly different information.
- Evidence: `reasoning_application` cue `because` at chunk `4546390` offsets `541-548`; context: Huang argues, the evidence was not rejected because the RPD had already found not credible that she was at risk in China.
- Evidence: `counterargument_limitation` cue `However` at chunk `4546390` offsets `262-269`; context: However, they contain a general summary of articles and general statements which simply echoed the evidence already presented by Ms.
- Evidence: `evidence_fact` cue `found that` at chunk `4546392` offsets `285-295`; context: The Officer found that Ms.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4546392` offsets `984-995`; context: Huang failed to meet her burden of proving these allegations on a balance of probabilities and that the evidence she presented could not be considered “new” pursuant to paragraph 113(a) of the IRPA and capable of proving an event that occurred after the hearing before the RPD.
- Evidence: `reasoning_application` cue `I find` at chunk `4546392` offsets `755-761`; context: Huang was relying on a declaration made by her mother, I find nothing unreasonable in the PRRA Officer’s finding that that Ms.
- Evidence: `evidence_fact` cue `found that` at chunk `4546393` offsets `110-120`; context: [28] With respect to the news articles, the PRRA Officer assessed them as they postdated the RPD decision but found that they were not material to Ms.
- Evidence: `reasoning_application` cue `because` at chunk `4546393` offsets `192-199`; context: The articles were rejected because, even if they referred to Christians being prosecuted in China, they did not show how Ms.
- Evidence: `counterargument_limitation` cue `but` at chunk `4546393` offsets `106-109`; context: [28] With respect to the news articles, the PRRA Officer assessed them as they postdated the RPD decision but found that they were not material to Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546394` offsets `22-30`; context: [29] On each piece of evidence submitted by Ms.
- Evidence: `reasoning_application` cue `I find` at chunk `4546394` offsets `55-61`; context: Huang, I find the PRRA Officer’s reasoning to be transparent and intelligible.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546395` offsets `518-526`; context: In conducting a reasonableness review of factual findings, it is not the role of the Court to reweigh the evidence or the relative importance given by the decision-maker to any relevant factor.
- Evidence: `governing_rule` cue `Under` at chunk `4546395` offsets `606-611`; context: Under a reasonableness standard, as long as the process and outcome fit comfortably with the principles of justification, transparency and intelligibility, a reviewing court should not substitute its own view of a preferable outcome (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 16).
- Evidence: `evidence_fact` cue `record` at chunk `4546396` offsets `616-622`; context: The reviewing court shall look at the reasons, the record and the outcome and, if there is a justifiable explanation for the outcome reached, it shall refrain from intervening.
- Evidence: `governing_rule` cue `standard of review` at chunk `4546396` offsets `167-185`; context: An imperfect decision may still be immune from judicial review, as the standard of review is not concerned with the decision’s degree of perfection but rather its reasonableness (Bhatia v Canada (Citizenship and Immigration), 2017 FC 1000 at para 29).
- Evidence: `counterargument_limitation` cue `but` at chunk `4546396` offsets `244-247`; context: An imperfect decision may still be immune from judicial review, as the standard of review is not concerned with the decision’s degree of perfection but rather its reasonableness (Bhatia v Canada (Citizenship and Immigration), 2017 FC 1000 at para 29).

#### 10830:4:subtheme:3 · paragraphs 34-35

- Raw key terms: `acknowledges, application, argues, because, believe, bozik, canada, case`
- Display key terms: `acknowledges, argues, because, believe, bozik, case`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: acknowledges, argues, because, believe, bozik, case Rule/authority context: Huang submits that a hearing was required under paragraph 113(b) of the IRPA and section 167 of the IRP Regulations because serious issues of credibility were central to her PRRA application. Application context: Huang submits that a hearing was required under paragraph 113(b) of the IRPA and section 167 of the IRP Regulations because serious issues of credibility were central to her PRRA application. Evidence spans paragraphs 34-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4546397` offsets `191-197`; context: Huang submits that a hearing was required under paragraph 113(b) of the IRPA and section 167 of the IRP Regulations because serious issues of credibility were central to her PRRA application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546397` offsets `337-345`; context: Huang acknowledges the inherent difficulty to distinguish between an insufficient evidence finding and a negative credibility finding made by the PRRA officers, but argues that her case truly turned on credibility, as was the situation in Bozik v Canada (Citizenship and Immigration), 2017 FC 961[Bozik] at paragraphs 17-20.
- Evidence: `governing_rule` cue `under` at chunk `4546397` offsets `101-106`; context: Huang submits that a hearing was required under paragraph 113(b) of the IRPA and section 167 of the IRP Regulations because serious issues of credibility were central to her PRRA application.
- Evidence: `reasoning_application` cue `because` at chunk `4546397` offsets `175-182`; context: Huang submits that a hearing was required under paragraph 113(b) of the IRPA and section 167 of the IRP Regulations because serious issues of credibility were central to her PRRA application.
- Evidence: `counterargument_limitation` cue `but` at chunk `4546397` offsets `416-419`; context: Huang acknowledges the inherent difficulty to distinguish between an insufficient evidence finding and a negative credibility finding made by the PRRA officers, but argues that her case truly turned on credibility, as was the situation in Bozik v Canada (Citizenship and Immigration), 2017 FC 961[Bozik] at paragraphs 17-20.

#### 10830:4:subtheme:4 · paragraphs 36-37

- Raw key terms: `application, credibility, decision, evidence, generally, hearing, minister, oral`
- Display key terms: `credibility, generally, hearing, oral`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: credibility, generally, hearing, oral Rule/authority context: However, pursuant to subsection 113(b) of the IRPA, an oral hearing may be held if the minister is of the opinion, on the basis of prescribed factors, that such a hearing is required. Evidence spans paragraphs 36-37. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4546399` offsets `457-462`; context: The prescribed factors are set out in section 167 of the IRP Regulations, and they are cumulative: an oral hearing will generally be required if there is a serious credibility issue regarding evidence that is central to the decision and which, if accepted, would justify allowing the application.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546399` offsets `473-481`; context: The prescribed factors are set out in section 167 of the IRP Regulations, and they are cumulative: an oral hearing will generally be required if there is a serious credibility issue regarding evidence that is central to the decision and which, if accepted, would justify allowing the application.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4546399` offsets `106-117`; context: However, pursuant to subsection 113(b) of the IRPA, an oral hearing may be held if the minister is of the opinion, on the basis of prescribed factors, that such a hearing is required.
- Evidence: `counterargument_limitation` cue `However` at chunk `4546399` offsets `97-104`; context: However, pursuant to subsection 113(b) of the IRPA, an oral hearing may be held if the minister is of the opinion, on the basis of prescribed factors, that such a hearing is required.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546400` offsets `315-323`; context: Huang asserts that, despite the language used by the PRRA Officer, the Decision to reject her PRRA application was based on veiled credibility findings, not on the insufficiency of the evidence or its lack of corroboration, as the minister contends.

#### 10830:4:subtheme:5 · paragraphs 38-40

- Raw key terms: `huang, actually, case, conclusion, court, credibility, decision, disguised`
- Display key terms: `huang, actually, case, conclusion, credibility, disguised`
- Argument roles: `counterargument_limitation, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue Display terms: huang, actually, case, conclusion, credibility, disguised Evidence spans paragraphs 38-40. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4546401` offsets `534-541`; context: However, determining whether an insufficiency finding is actually a veiled credibility finding is very fact-specific.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546401` offsets `76-84`; context: [36] I accept that a decision-maker’s conclusion that there is insufficient evidence to support an assertion can sometimes hide what is actually a veiled or implicit adverse credibility finding.
- Evidence: `counterargument_limitation` cue `However` at chunk `4546401` offsets `513-520`; context: However, determining whether an insufficiency finding is actually a veiled credibility finding is very fact-specific.
- Evidence: `issue` cue `issues` at chunk `4546402` offsets `907-913`; context: Huang’s new evidence expressly and repeatedly couched in “sufficiency of evidence” language, but I can find no expressions or statement leaving open the interpretation that the Officer had credibility issues with Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546402` offsets `31-39`; context: [37] A finding of insufficient evidence can sometimes be difficult to distinguish from a finding of credibility.
- Evidence: `counterargument_limitation` cue `but` at chunk `4546402` offsets `799-802`; context: Huang’s new evidence expressly and repeatedly couched in “sufficiency of evidence” language, but I can find no expressions or statement leaving open the interpretation that the Officer had credibility issues with Ms.

#### 10830:4:subtheme:6 · paragraphs 41-44

- Raw key terms: `credibility, evidence, canada, officer, probative, adduced, applicant, burden`
- Display key terms: `credibility, officer, probative, adduced, burden`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: credibility, officer, probative, adduced, burden Rule/authority context: Where a PRRA officer assesses the weight or probative value of the evidence, it is well established that no oral hearing is warranted under section 167 of the IRP Regulations. Evidence spans paragraphs 41-44. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4546404` offsets `111-116`; context: Huang’s credibility in issue.
- Evidence: `evidence_fact` cue `record` at chunk `4546404` offsets `174-180`; context: I can find no basis in the Officer’s Decision or in the record from the PRRA application to support a conclusion that there was evidence presented by Ms.
- Evidence: `issue` cue `issue` at chunk `4546405` offsets `23-28`; context: [40] Since no “serious issue” concerning Ms.
- Evidence: `evidence_fact` cue `testimony` at chunk `4546405` offsets `255-264`; context: The PRRA Officer had concerns with the testimony attributed to her mother, and relayed in Ms.
- Evidence: `governing_rule` cue `under` at chunk `4546405` offsets `603-608`; context: Where a PRRA officer assesses the weight or probative value of the evidence, it is well established that no oral hearing is warranted under section 167 of the IRP Regulations.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546406` offsets `102-110`; context: [41] An adverse finding of credibility is not to be confused with a finding of insufficient probative evidence.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4546406` offsets `359-365`; context: It cannot be assumed that, in cases where an immigration officer finds that the evidence does not establish the applicant’s claim, the officer has not believed the applicant (Gao v Canada (Citizenship and Immigration), 2014 FC 59 at para 32).
- Evidence: `evidence_fact` cue `evidence` at chunk `4546407` offsets `218-226`; context: A credibility assessment goes to the reliability of the evidence.
- Evidence: `counterargument_limitation` cue `However` at chunk `4546407` offsets `119-126`; context: However, these are two different concepts.

#### 10830:4:subtheme:7 · paragraphs 45-47

- Raw key terms: `balance, establish, evidence, fact, provided, sufficient, canada, citizenship`
- Display key terms: `balance, establish, fact, provided, sufficient`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: balance, establish, fact, provided, sufficient Application context: Therefore, there was “insufficient evidence” to establish that the Chinese authorities were looking for Ms. Evidence spans paragraphs 45-47. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4546408` offsets `718-725`; context: When frailties have been highlighted in the evidence, it is appropriate for the trier of fact to consider whether the evidentiary threshold has been satisfied by an applicant.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546408` offsets `71-79`; context: [43] The trier of fact may decide to assign little or no weight to the evidence, and hold that the legal standard has not been met.
- Evidence: `issue` cue `whether` at chunk `4546409` offsets `818-825`; context: It is perfectly open to a trier of fact to assess the weight and probative value of evidence without considering first whether it is credible or not (Ferguson at para 26).
- Evidence: `evidence_fact` cue `evidence` at chunk `4546409` offsets `191-199`; context: [44] In Ferguson v Canada (Citizenship and Immigration), 2008 FC 1067 [Ferguson], Justice Zinn provided a useful synopsis of the interplay between weight, sufficiency, and credibility of the evidence.
- Evidence: `evidence_fact` cue `found that` at chunk `4546410` offsets `48-58`; context: Huang, the PRRA Officer found that there was insufficient objective evidence to prove, on a balance of probabilities, that the PSB had a continuing interest in her in China.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4546410` offsets `522-531`; context: Therefore, there was “insufficient evidence” to establish that the Chinese authorities were looking for Ms.

#### 10830:4:subtheme:8 · paragraphs 48-52

- Raw key terms: `credibility, evidence, fairness, huang, procedural, prra, review, standard`
- Display key terms: `credibility, fairness, huang, procedural, prra, review, standard`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue Display terms: credibility, fairness, huang, procedural, prra, review, standard Rule/authority context: Only evidence raising issues with respect to the applicant’s credibility may call for an oral hearing under section 167 of the IRP Regulations. | Under a standard of reasonableness, Ms. Evidence spans paragraphs 48-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4546411` offsets `46-54`; context: [46] Such a determination does not bring into question Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546411` offsets `115-123`; context: Such an assessment and weighing of evidence does not need to be put to an applicant and does not raise any issues of procedural fairness.
- Evidence: `issue` cue `issues` at chunk `4546412` offsets `291-297`; context: Only evidence raising issues with respect to the applicant’s credibility may call for an oral hearing under section 167 of the IRP Regulations.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546412` offsets `38-46`; context: [47] Moreover, the credibility of the evidence must not be confused with the credibility of the applicant (Singh at para 44).
- Evidence: `governing_rule` cue `under` at chunk `4546412` offsets `371-376`; context: Only evidence raising issues with respect to the applicant’s credibility may call for an oral hearing under section 167 of the IRP Regulations.
- Evidence: `counterargument_limitation` cue `but` at chunk `4546412` offsets `209-212`; context: True, the credibility of the evidence can turn on the credibility of an applicant, but it can also depend on the credibility of third parties.
- Evidence: `evidence_fact` cue `record` at chunk `4546413` offsets `66-72`; context: [48] I can find no basis in the PRRA Officer’s Decision or in the record from the PRRA application to support a conclusion that there was evidence presented by Ms.
- Evidence: `governing_rule` cue `Under` at chunk `4546413` offsets `608-613`; context: Under a standard of reasonableness, Ms.
- Evidence: `governing_rule` cue `standard of review` at chunk `4546414` offsets `51-69`; context: [49] In light of the diverging views regarding the standard of review applicable to decisions to hold an oral hearing in the context of a PRRA application, I make the following additional remarks.
- Evidence: `governing_rule` cue `standard of review` at chunk `4546415` offsets `73-91`; context: [50] In the circumstances of this case, the selection of the appropriate standard of review or analytical approach is of no consequence since, under either the lens of the reasonableness standard or the lens of procedural fairness, I am satisfied that the decision of the PRRA Officer must not be set aside.

#### 10830:4:subtheme:9 · paragraphs 53-54

- Raw key terms: `administrative, appeal, canada, citizenship, correctness, court, decision-maker, duty`
- Display key terms: `administrative, correctness, decision-maker, duty`
- Argument roles: `counterargument_limitation, governing_rule, issue`
- Explanation: Observed roles: counterargument_limitation, governing_rule, issue Display terms: administrative, correctness, decision-maker, duty Rule/authority context: [51] It is generally accepted that “correctness” is the standard of review for determining whether a decision-maker complies with the duty of procedural fairness and the principles of fundamental justice (Mission Institu | [52] In CPR, the Federal Court of Appeal instead emphasized that “correctness” in the context of procedural fairness should be approached from a different angle, an angle somewhat detached from the usual standard of revi Evidence spans paragraphs 53-54. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4546416` offsets `91-98`; context: [51] It is generally accepted that “correctness” is the standard of review for determining whether a decision-maker complies with the duty of procedural fairness and the principles of fundamental justice (Mission Institution v Khela, 2014 SCC 24 at para 79; Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 43; Canadian Pacific Railway Company v Canada (Attorney General), 2018 FCA 69 [CPR] at paras 34-36; Sketchley v Canada (Attorney General), 2005 FCA 404 at para 53).
- Evidence: `governing_rule` cue `standard of review` at chunk `4546416` offsets `56-74`; context: [51] It is generally accepted that “correctness” is the standard of review for determining whether a decision-maker complies with the duty of procedural fairness and the principles of fundamental justice (Mission Institution v Khela, 2014 SCC 24 at para 79; Canada (Citizenship and Immigration) v Khosa, 2009 SCC 12 at para 43; Canadian Pacific Railway Company v Canada (Attorney General), 2018 FCA 69 [CPR] at paras 34-36; Sketchley v Canada (Attorney General), 2005 FCA 404 at para 53).
- Evidence: `counterargument_limitation` cue `however` at chunk `4546416` offsets `1171-1178`; context: In the more recent CPR case, the Federal Court of Appeal has however sought to put an end to this debate, affirming that the “suggestion that procedural fairness is reviewed on a correctness standard with some deference is both confusing and unhelpful” (CPR at para 44).
- Evidence: `issue` cue `whether` at chunk `4546417` offsets `551-558`; context: The Court stated that, where the duty of an administrative decision-maker to act fairly is questioned, assessing a procedural fairness argument requires to verify whether the procedure was fair having regard to all of the circumstances (CPR at para 54), including the five, non-exhaustive contextual factors set out in Baker v Canada (Minister of Citizenship and Immigration), [1999] 2 SCR 817 [Baker] at paras 23-27).
- Evidence: `governing_rule` cue `standard of review` at chunk `4546417` offsets `204-222`; context: [52] In CPR, the Federal Court of Appeal instead emphasized that “correctness” in the context of procedural fairness should be approached from a different angle, an angle somewhat detached from the usual standard of review analysis.

#### 10830:4:subtheme:10 · paragraphs 55-56

- Raw key terms: `canada, case, context, decision, decision-maker, duty, fair, fairness`
- Display key terms: `case, context, decision-maker, duty, fair, fairness`
- Argument roles: `counterargument_limitation, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, issue, reasoning_application Display terms: case, context, decision-maker, duty, fair, fairness Application context: [54] Therefore, the true question raised when procedural fairness and the duty to act fairly are the object of an application for judicial review is not so much whether the decision was “correct”, but rather whether, tak Evidence spans paragraphs 55-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Whether` at chunk `4546418` offsets `5-12`; context: [53] Whether a decision is procedurally fair must be determined on a case-by-case basis.
- Evidence: `counterargument_limitation` cue `however` at chunk `4546418` offsets `660-667`; context: In any situation, however, procedural fairness issues do not create substantive rights but instead relate to the process followed by the decision-maker (Baker at para 26).
- Evidence: `issue` cue `question` at chunk `4546419` offsets `25-33`; context: [54] Therefore, the true question raised when procedural fairness and the duty to act fairly are the object of an application for judicial review is not so much whether the decision was “correct”, but rather whether, taking into account the particular context and circumstances at issue, the process followed by the decision-maker was fair and offered the parties a right to be heard and the opportunity to know and respond to the case against them (Makoundi v Canada (Attorney General), 2014 FC 1177 at para 35).
- Evidence: `reasoning_application` cue `Therefore` at chunk `4546419` offsets `5-14`; context: [54] Therefore, the true question raised when procedural fairness and the duty to act fairly are the object of an application for judicial review is not so much whether the decision was “correct”, but rather whether, taking into account the particular context and circumstances at issue, the process followed by the decision-maker was fair and offered the parties a right to be heard and the opportunity to know and respond to the case against them (Makoundi v Canada (Attorney General), 2014 FC 1177 at para 35).
- Evidence: `counterargument_limitation` cue `but` at chunk `4546419` offsets `197-200`; context: [54] Therefore, the true question raised when procedural fairness and the duty to act fairly are the object of an application for judicial review is not so much whether the decision was “correct”, but rather whether, taking into account the particular context and circumstances at issue, the process followed by the decision-maker was fair and offered the parties a right to be heard and the opportunity to know and respond to the case against them (Makoundi v Canada (Attorney General), 2014 FC 1177 at para 35).

#### 10830:4:subtheme:11 · paragraphs 57-58

- Raw key terms: `fair, huang, officer, process, prra, achieved, address, affected`
- Display key terms: `fair, huang, officer, process, prra, achieved, address, affected`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: fair, huang, officer, process, prra, achieved, address, affected Rule/authority context: In the circumstances of this case, I am satisfied that, even if the matter is considered under the lens of procedural fairness, the PRRA Officer was not required to hold an oral hearing as no credibility issues were at s Evidence spans paragraphs 57-58. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4546420` offsets `679-685`; context: In the circumstances of this case, I am satisfied that, even if the matter is considered under the lens of procedural fairness, the PRRA Officer was not required to hold an oral hearing as no credibility issues were at stake.
- Evidence: `governing_rule` cue `under` at chunk `4546420` offsets `564-569`; context: In the circumstances of this case, I am satisfied that, even if the matter is considered under the lens of procedural fairness, the PRRA Officer was not required to hold an oral hearing as no credibility issues were at stake.
- Evidence: `issue` cue `question` at chunk `4546421` offsets `174-182`; context: Certified question

#### 10830:4:subtheme:12 · paragraphs 59-60

- Raw key terms: `court, question, according, appeal, applicable, arise, asks, broad`
- Display key terms: `question, according, applicable, arise, asks, broad`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: question, according, applicable, arise, asks, broad Rule/authority context: [57] The minister asks the Court to certify the following question: “What standard of review is applicable to the judicial review of an officer’s determination of whether a hearing is required, under section 167 of the I Evidence spans paragraphs 59-60. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4546422` offsets `58-66`; context: [57] The minister asks the Court to certify the following question: “What standard of review is applicable to the judicial review of an officer’s determination of whether a hearing is required, under section 167 of the IRP Regulations?
- Evidence: `governing_rule` cue `standard of review` at chunk `4546422` offsets `74-92`; context: [57] The minister asks the Court to certify the following question: “What standard of review is applicable to the judicial review of an officer’s determination of whether a hearing is required, under section 167 of the IRP Regulations?
- Evidence: `issue` cue `question` at chunk `4546423` offsets `66-74`; context: [58] For the reasons that follow, I do not find that the proposed question meets the strict requirements for certification developed by the Federal Court of Appeal.

#### 10830:4:subtheme:13 · paragraphs 61-62

- Raw key terms: `above, case, decision, determination, fairness, findings, hearing, huang`
- Display key terms: `above, case, determination, fairness, findings, hearing, huang`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, reasoning_application Display terms: above, case, determination, fairness, findings, hearing, huang Rule/authority context: As explained above, no matter whether the PRRA Officer’s Decision is looked at under the standard of reasonableness or under the lens of the rules of procedural fairness, there are no reasons for the Court to intervene a Application context: Therefore, I cannot overturn the PRRA Officer’s Decision and must dismiss this application for judicial review. Evidence spans paragraphs 61-62. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4546424` offsets `30-38`; context: [59] I decline to certify the question proposed by the minister as it is not dispositive of the appeal.
- Evidence: `governing_rule` cue `under` at chunk `4546424` offsets `183-188`; context: As explained above, no matter whether the PRRA Officer’s Decision is looked at under the standard of reasonableness or under the lens of the rules of procedural fairness, there are no reasons for the Court to intervene and to quash the Officer’s determination that, in the case of Ms.
- Evidence: `evidence_fact` cue `evidence` at chunk `4546425` offsets `118-126`; context: [60] For the above reasons, the Decision of the PRRA Officer represents a reasonable outcome based on the law and the evidence before the decision-maker.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4546425` offsets `823-832`; context: Therefore, I cannot overturn the PRRA Officer’s Decision and must dismiss this application for judicial review.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4546425` offsets `836-842`; context: Therefore, I cannot overturn the PRRA Officer’s Decision and must dismiss this application for judicial review.

#### 10830:4:subtheme:14 · paragraphs 63-63

- Raw key terms: `certified, general, importance, question`
- Display key terms: `certified, importance, question`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: certified, importance, question Evidence spans paragraphs 63-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4546426` offsets `8-16`; context: [61] No question of general importance is certified.

#### Section text

[22] The five criteria established in Raza are conditions of admissibility of evidence when a PRRA application follows a rejected refugee claim (Canada (Citizenship and Immigration) v Singh, 2016 FCA 96 [Singh] at para 38). Once evidence is found to be admissible under the Raza criteria, the PRRA officers must then decide if the evidence is sufficient to meet the burden of proof (i.e., each essential fact is proven) and the standard of proof (i.e., balance of probabilities) for getting refugee protection.

[23] Here, the PRRA Officer rejected the evidence presented by Ms. Huang because it did not meet the “newness” or “materiality” criteria identified in Raza. In addition, even if some evidence would have been admissible, the Officer found it insufficient to meet the standard of proof.

[24] The Officer first assessed the photographs submitted by Ms. Huang as “new evidence”, but found that these photographs were undated and unlabelled. Moreover, the events allegedly depicted on the picture occurred in October 2015, thus predating both the RPD and the RAD determinations. This evidence was therefore not admissible under paragraph 113(a) of the IRPA as it did not arise after the rejection of Ms. Huang’s refugee claim. Ms. Huang did not directly challenge this finding in her submissions before this Court.

[25] Turning to the additional statements made by Ms. Huang, the PRRA Officer concluded that this evidence could not qualify as “new” it did not amount to significantly different information. I acknowledge that the statements at issue postdate the RPD decision. However, they contain a general summary of articles and general statements which simply echoed the evidence already presented by Ms. Huang before the RPD regarding the PSB allegedly still looking for her in China. Contrary to what Ms. Huang argues, the evidence was not rejected because the RPD had already found not credible that she was at risk in China. It was rejected because it was not significantly different from the information presented to the RPD, in accordance with the teachings of Raza FC. I find nothing irrational or arbitrary in such finding, as it is well accepted that it is open to the PRRA officers, and reasonable, to reject information which is essentially a repetition of information that was before the RPD (Raza at para 18).

[26] Citing Cho is of little assistance to Ms. Huang. In that decision, the very fact that the mother had been sex trafficked was itself new and had not been before the RPD or the RAD. Here, the PRRA Officer found no such new fact. A plain reading of the Decision reveals that Ms. Huang’s additional statements were essentially restating risks already examined by the RPD and the RAD.

[27] Furthermore, the PRRA Officer more specifically referred to the statement made by Ms. Huang indicating that she was informed by her mother that the PSB continued to look for her. This was the crux underlying Ms. Huang’s allegation that she was still at risk in China. The Officer found that Ms. Huang had “not provided sufficient objective evidence to support her statements” in that respect, and notably that she had failed to present an affidavit from her mother attesting to the PSB’s continued interest. In the Decision, the PRRA Officer repeated on three occasions that there was “insufficient evidence” to support the allegations that the PSB were continuing to look for Ms. Huang. As Ms. Huang was relying on a declaration made by her mother, I find nothing unreasonable in the PRRA Officer’s finding that that Ms. Huang failed to meet her burden of proving these allegations on a balance of probabilities and that the evidence she presented could not be considered “new” pursuant to paragraph 113(a) of the IRPA and capable of proving an event that occurred after the hearing before the RPD.

[28] With respect to the news articles, the PRRA Officer assessed them as they postdated the RPD decision but found that they were not material to Ms. Huang’s case. The articles were rejected because, even if they referred to Christians being prosecuted in China, they did not show how Ms. Huang was part of the groups and churches being targeted. I add that the articles did not relate to the Shouters church to which Ms. Huang belonged when in China. I find nothing unreasonable in the Officer’s decision to exclude such evidence as it provided information on crackdowns in Chinese provinces other than the province where Ms. Huang is from and did not establish that Ms. Huang fitted the profile of those who face difficulties with the Chinese authorities. The news articles were not material and not required for the PRRA assessment, and it was therefore open to the PRRA Officer to conclude that they “provided insufficient new evidence that Ms. Huang will be at risk in China”.

[29] On each piece of evidence submitted by Ms. Huang, I find the PRRA Officer’s reasoning to be transparent and intelligible. This is not a case where the PRRA Officer failed to consider the evidence provided or ignored some contrary country conditions evidence. Looking at the reasons as a whole and having reviewed the record, I find that the Officer conducted a reasonably thorough and balanced assessment of the evidence offered by Ms. Huang.

[30] When reviewing a decision on the standard of reasonableness, the analysis is concerned “with the existence of justification, transparency and intelligibility within the decision-making process”, and the PRRA Officer’s findings should not be disturbed as long as the decision “falls within a range of possible, acceptable outcomes which are defensible in respect of the facts and law” (Dunsmuir at para 47). In conducting a reasonableness review of factual findings, it is not the role of the Court to reweigh the evidence or the relative importance given by the decision-maker to any relevant factor. Under a reasonableness standard, as long as the process and outcome fit comfortably with the principles of justification, transparency and intelligibility, a reviewing court should not substitute its own view of a preferable outcome (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62 at para 16).

[31] Reasons need not to be perfect or even comprehensive. They only need to be comprehensible. An imperfect decision may still be immune from judicial review, as the standard of review is not concerned with the decision’s degree of perfection but rather its reasonableness (Bhatia v Canada (Citizenship and Immigration), 2017 FC 1000 at para 29). The test for reasonableness dictates that the reviewing court must start from the decision and the recognition that the administrative decision-maker has the primary responsibility to make the factual determinations. The reviewing court shall look at the reasons, the record and the outcome and, if there is a justifiable explanation for the outcome reached, it shall refrain from intervening. I am satisfied that this is the situation here. The Decision allows a reader to know exactly why the PRRA Officer did not consider the new evidence submitted by Ms. Huang. This does not call for the Court’s intervention.
B. No oral hearing needed to be convened

[32] Regarding the failure to conduct an oral hearing, Ms. Huang submits that a hearing was required under paragraph 113(b) of the IRPA and section 167 of the IRP Regulations because serious issues of credibility were central to her PRRA application. Ms. Huang acknowledges the inherent difficulty to distinguish between an insufficient evidence finding and a negative credibility finding made by the PRRA officers, but argues that her case truly turned on credibility, as was the situation in Bozik v Canada (Citizenship and Immigration), 2017 FC 961[Bozik] at paragraphs 17-20. More specifically, Ms. Huang claims that the PRRA Officer did not believe that Chinese officials were still looking for her because (i) her statement about the information provided by her mother was not corroborated and (ii) the RPD had found not credible the Chinese officials’ interest in her. As such, she pleads that the rules of procedural fairness and section 167 of the IRP Regulations mandated an oral hearing.

[33] I disagree.

[34] In the normal course of determining PRRA applications, oral hearings are not commonly held. However, pursuant to subsection 113(b) of the IRPA, an oral hearing may be held if the minister is of the opinion, on the basis of prescribed factors, that such a hearing is required. The prescribed factors are set out in section 167 of the IRP Regulations, and they are cumulative: an oral hearing will generally be required if there is a serious credibility issue regarding evidence that is central to the decision and which, if accepted, would justify allowing the application.

[35] It is not disputed that, when the credibility of an applicant is at stake, an oral hearing is indeed generally required. Ms. Huang asserts that, despite the language used by the PRRA Officer, the Decision to reject her PRRA application was based on veiled credibility findings, not on the insufficiency of the evidence or its lack of corroboration, as the minister contends.

[36] I accept that a decision-maker’s conclusion that there is insufficient evidence to support an assertion can sometimes hide what is actually a veiled or implicit adverse credibility finding. This was indeed the situation in the Bozik decision relied on by Ms. Huang. I further concede that there is a bubbling cauldron of decisions of this Court having similarly concluded that PRRA officers’ conclusions on insufficient evidence effectively boiled down to implicit, disguised or veiled credibility findings. However, determining whether an insufficiency finding is actually a veiled credibility finding is very fact-specific. Sometimes it is; sometimes it is not. It depends on the language used in the reasons, the particular facts on the record as well as the context of the decision. As is the case on any aspect of a judicial review, the starting point is the decision itself and what it actually says. The Court must also look beyond the express wording of the decision to determine whether, in fact, the applicant’s credibility was indeed in issue.

[37] A finding of insufficient evidence can sometimes be difficult to distinguish from a finding of credibility. In this case, it is not. The PRRA Officer’s findings are framed and expressly written in terms of insufficiency of evidence, and a review of the Officer’s analysis and the record does not support a conclusion that the finding was actually one of credibility. This is not a situation where the language used by the Officer is obscure and or where the analysis conducted can lead to variable interpretations. Nor is it a situation where, on its face, the PRRA Decision appears to be based on a disguised or veiled credibility finding. Not only are the findings of the PRRA Officer regarding Ms. Huang’s new evidence expressly and repeatedly couched in “sufficiency of evidence” language, but I can find no expressions or statement leaving open the interpretation that the Officer had credibility issues with Ms. Huang and her new evidence of risk. Nowhere did the Officer refer to inconsistencies in Ms. Huang’s statements, nor was there any suggestion that she has not been truthful. No passage raises any ambiguity or creates any uncertainty. No expressions or comments refer to changes in Ms. Huang’s story or to conflicting affirmations or questioning the truthfulness of Ms. Huang. Nowhere in the PRRA Decision is there any reference to her credibility, expressed or implied.

[38] And, indeed, counsel for Ms. Huang could not refer to the Court to any.

[39] In my view, there is simply no merit to the argument that the PRRA Officer put Ms. Huang’s credibility in issue. I can find no basis in the Officer’s Decision or in the record from the PRRA application to support a conclusion that there was evidence presented by Ms. Huang which the Officer did not believe. The Officer was simply not convinced by the evidence adduced by Ms. Huang. I pause to observe that the PRRA Officer was entitled to refer to the basis of the RPD’s decision (i.e., credibility) without the PRRA Decision itself assessing credibility (Titkova v Canada (Immigration, Refugees and Citizenship), 2017 FC 691 at paras 15-16).

[40] Since no “serious issue” concerning Ms. Huang’s credibility was in issue at the PRRA, there is no merit to her contention that the Officer acted unreasonably or contrary to law in not convoking an oral hearing. The PRRA Officer had concerns with the testimony attributed to her mother, and relayed in Ms. Huang’s new statements. The concerns were not with Ms. Huang’s credibility. Only the quality of the evidence adduced, and the weight to give it, was assessed. Where a PRRA officer assesses the weight or probative value of the evidence, it is well established that no oral hearing is warranted under section 167 of the IRP Regulations.

[41] An adverse finding of credibility is not to be confused with a finding of insufficient probative evidence. As I stated in Ibabu v Canada (Citizenship and Immigration), 2015 FC 1068 at paragraph 35, “[a]n adverse finding of credibility is different from a finding of insufficient evidence or an applicant’s failure to meet his or her burden of proof”. It cannot be assumed that, in cases where an immigration officer finds that the evidence does not establish the applicant’s claim, the officer has not believed the applicant (Gao v Canada (Citizenship and Immigration), 2014 FC 59 at para 32).

[42] The term “credibility” is often erroneously used in a broader sense of insufficiency or lack of persuasive value. However, these are two different concepts. A credibility assessment goes to the reliability of the evidence. When there is a finding that the evidence is not credible, it is a determination that the source of the evidence (for example, an applicant’s testimony) is not reliable. Reliability of the evidence is one thing, but the evidence must also have sufficient probative value to meet the applicable standard of proof. A sufficiency assessment goes to the nature and quality of the evidence needed to be brought forward by an applicant in order to obtain relief, to its probative value, and to the weight to be given to the evidence by the trier of fact, be it a court or an administrative decision-makerThe law of evidence operates a binary system in which only two possibilities exist: a fact either happened or it did not. If the trier of fact is left in doubt, the doubt is resolved by the rule that one party carries the burden of proof and must ensure that there is sufficient evidence of the existence or non-existence of the fact to satisfy the applicable standard of proof. In FH v McDougall, 2008 SCC 53 [McDougall], the Supreme Court established that there is only one civil standard of proof in Canada, the balance of probabilities: evidence “must be scrutinized with care by the trial judge” and “must always be sufficiently clear, convincing and cogent to satisfy the balance of probabilities test” (McDougall at paras 45-46).

[43] The trier of fact may decide to assign little or no weight to the evidence, and hold that the legal standard has not been met. In the same vein, the presumption of truth or reliability of statements made by refugee applicants, as expressed in Maldonado v Canada (Minister of Employment and Immigration), [1980] 2 FC 302 (FCA), cannot be equated with a presumption of sufficiency. Even if presumed credible and reliable, evidence from a refugee applicant cannot be presumed to be sufficient, in and of itself, to establish the facts on a balance of probabilities. This is for the trier of fact to determine. When frailties have been highlighted in the evidence, it is appropriate for the trier of fact to consider whether the evidentiary threshold has been satisfied by an applicant. By doing so, the trier of fact does not question the applicant’s credibility. Rather, the trier of fact determines whether the evidence provided, assuming it is credible, is sufficient to establish, on a balance of probabilities, the facts alleged (Zdraviak v Canada (Citizenship and Immigration), 2017 FC 305 at paras 17-18). In other words, not being convinced by the evidence does not necessarily mean that the trier of fact disbelieves the applicant.

[44] In Ferguson v Canada (Citizenship and Immigration), 2008 FC 1067 [Ferguson], Justice Zinn provided a useful synopsis of the interplay between weight, sufficiency, and credibility of the evidence. As he stated at paragraph 27, when a trier of fact assesses the weight and sufficiency of the evidence, he or she “is simply saying the evidence that has been tendered does not have sufficient probative value, either on its own or coupled with the other tendered evidence, to establish on the balance of probability, the fact for which it has been tendered”. It is not only evidence that has passed the test of reliability (i.e., credible evidence) that may be assessed for weight and sufficiency. It is perfectly open to a trier of fact to assess the weight and probative value of evidence without considering first whether it is credible or not (Ferguson at para 26). This will occur when the trier of fact is of the view that the evidence is to be given little or no weight, even if it is found to be reliable.

[45] In the case of Ms. Huang, the PRRA Officer found that there was insufficient objective evidence to prove, on a balance of probabilities, that the PSB had a continuing interest in her in China. The Officer neither believed nor disbelieved Ms. Huang’s statement in that regard. As the statements essentially relied on an affirmation made by her mother, the Officer found that Ms. Huang had not provided “sufficient objective evidence to support her statements” in that regard, such as an affidavit sworn by her mother. Therefore, there was “insufficient evidence” to establish that the Chinese authorities were looking for Ms. Huang. Stated otherwise, the PRRA Officer found that the evidence was insufficient to prove, on the balance of probabilities, the fact that Ms. Huang was still at risk in China based on the PSB’s continued interest.

[46] Such a determination does not bring into question Ms. Huang’s credibility. Such an assessment and weighing of evidence does not need to be put to an applicant and does not raise any issues of procedural fairness.

[47] Moreover, the credibility of the evidence must not be confused with the credibility of the applicant (Singh at para 44). True, the credibility of the evidence can turn on the credibility of an applicant, but it can also depend on the credibility of third parties. Only evidence raising issues with respect to the applicant’s credibility may call for an oral hearing under section 167 of the IRP Regulations. In this case, the absence of reasonably expected evidence, such as an affidavit from Ms. Huang’s mother, is not an assessment of Ms. Huang’s credibility.

[48] I can find no basis in the PRRA Officer’s Decision or in the record from the PRRA application to support a conclusion that there was evidence presented by Ms. Huang which the Officer did not believe. Rather, as expressly reflected in the PRRA Officer’s reasons, the Decision was based on the Officer finding that there was a lack of persuasive evidence to support a finding of forward-looking risk. Having concluded that the PRRA Officer did not base the Decision on veiled credibility findings, the procedural fairness arguments advanced by Ms. Huang in this application for judicial review must fail. Under a standard of reasonableness, Ms. Huang had to demonstrate the absence of justification, transparency and intelligibility within the decision-making process and to demonstrate that the decision does not fall within a range of possible, acceptable outcomes which are defensible in respect of the facts a

[Section text truncated at 20000 characters; full text and hashes remain in JSON.]


## 10830:5 · paragraphs 64-65

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `a09ad4de9b65da21ccbc8998a2808c8307c84f49f08d5c265201b3c7190d9c56`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10830:5:subtheme:1 · paragraphs 64-65

- Raw key terms: `imm-325-18, application, cause, certified, citizenship, costs, court, date`
- Display key terms: `imm-325-18, certified, costs, date`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-325-18, certified, costs, date Operative outcome context: JUDGMENT in IMM-325-18 THIS COURT’S JUDGMENT is that: The application for judicial review is dismissed, without costs. Evidence spans paragraphs 64-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4546426` offsets `183-191`; context: No serious question of general importance is certified.
- Evidence: `disposition` cue `dismissed` at chunk `4546426` offsets `146-155`; context: JUDGMENT in IMM-325-18
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed, without costs.

#### Section text

JUDGMENT in IMM-325-18
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed, without costs.
No serious question of general importance is certified.
"Denis Gascon"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-325-18
STYLE OF CAUSE:
MINXIANG HUANG v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
TORONTO, ONTARIO
DATE OF HEARING:
September 5, 2018


## 10830:6 · paragraphs 66-66

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `bebdf995729ff29290826c9ab82e10e8cf3ddf34e5726af6a57d603eca782c21`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 10830:6:subtheme:1 · paragraphs 66-66

- Raw key terms: `appearances, applicant, attorney, bruce, canada, dated, gascon, general`
- Display key terms: `bruce, dated, gascon`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: bruce, dated, gascon No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 66-66. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
GASCON J.
DATED:
September 20, 2018
APPEARANCES :
Michael Korman
For The Applicant
Suzanne M. Bruce
For The Respondent
SOLICITORS OF RECORD :
Korman & Korman LLP
Toronto, Ontario
For The Applicant
Attorney General of Canada
Toronto, Ontario
For The Respondent
