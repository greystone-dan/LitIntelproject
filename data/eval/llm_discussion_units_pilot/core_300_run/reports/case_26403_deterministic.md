# Discussion Units: case 26403

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **26**
- Continuity pairs: **25**
- Discussion Units: **2**
- Paragraph source hashes: **26**
- Sub-themes: **5**

## 26403:1 · paragraphs 0-24

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `5867bc54740685e03c83337b46c27cf2c66b087d0430722376ebdd587391bb28`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26403:1:subtheme:1 · paragraphs 0-11

- Raw key terms: `applicant, principal, applicants, alleges, canada, congolese, decision, forces`
- Display key terms: `principal, alleges, congolese, forces`
- Argument roles: `counterargument_limitation, governing_rule, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, governing_rule, reasoning_application Display terms: principal, alleges, congolese, forces Rule/authority context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] for judicial review of the decision rendered by the Refugee Protection Division of the Immigratio | Decision under Review Application context: [9] Fearing for his life, the principal applicant maintains that he requested a one-year leave from his place of work and applied for Canadian visitors visas. Evidence spans paragraphs 0-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `governing_rule` cue `pursuant to` at chunk `5241605` offsets `27-38`; context: [1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] for judicial review of the decision rendered by the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated December 12, 2011, which refused the applicants’ claim to be deemed Convention refugees or persons in need of protection under sections 96 and 97 of the Act.
- Evidence: `counterargument_limitation` cue `However` at chunk `5241609` offsets `230-237`; context: However, the applicant maintains that he learned from the Receiver that the funds had been transferred to an account managed by the President of the DRC.
- Evidence: `reasoning_application` cue `applied` at chunk `5241613` offsets `122-129`; context: [9] Fearing for his life, the principal applicant maintains that he requested a one-year leave from his place of work and applied for Canadian visitors visas.
- Evidence: `governing_rule` cue `under` at chunk `5241615` offsets `93-98`; context: Decision under Review

#### 26403:1:subtheme:2 · paragraphs 12-14

- Raw key terms: `applicants, board, account, applicant, found, merely, because, canada`
- Display key terms: `account, merely, because`
- Argument roles: `evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: evidence_fact, issue, reasoning_application Display terms: account, merely, because Application context: [13] The Board found it to be implausible that the applicants would be persecuted by the presidential security forces merely because the principal applicant had reported the irregularity while carrying out his duties as  Evidence spans paragraphs 12-14. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5241616` offsets `89-94`; context: [12] The Board rejected the applicants’ refugee claim as it found that the determinative issue was the lack of credibility of their account.
- Evidence: `evidence_fact` cue `found that` at chunk `5241616` offsets `60-70`; context: [12] The Board rejected the applicants’ refugee claim as it found that the determinative issue was the lack of credibility of their account.
- Evidence: `reasoning_application` cue `because` at chunk `5241617` offsets `125-132`; context: [13] The Board found it to be implausible that the applicants would be persecuted by the presidential security forces merely because the principal applicant had reported the irregularity while carrying out his duties as a civil servant.

#### 26403:1:subtheme:3 · paragraphs 15-22

- Raw key terms: `board, applicant, canada, court, immigration, citizenship, employment, evidence`
- Display key terms: `employment`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: employment Position/evidence statements: [15] The Board also acknowledged that the applicants had submitted substantial documentation indicating the human rights abuses in the DRC. Application context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subj | [18] It is trite law that the Board’s findings on credibility and implausibility are questions of fact and are therefore reviewable according to the standard of reasonableness (Aguebor v Canada (Minister of Employment an Evidence spans paragraphs 15-22. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `5241619` offsets `468-473`; context: Issue
- Evidence: `party_position` cue `submitted` at chunk `5241619` offsets `57-66`; context: [15] The Board also acknowledged that the applicants had submitted substantial documentation indicating the human rights abuses in the DRC.
- Evidence: `evidence_fact` cue `evidence` at chunk `5241619` offsets `303-311`; context: However, the Board concluded that, as a government employee, the applicant had not presented any evidence which demonstrated that he had been persecuted during his long career and found it unlikely that he would be persecuted now, at the end of his career.
- Evidence: `counterargument_limitation` cue `However` at chunk `5241619` offsets `206-213`; context: However, the Board concluded that, as a government employee, the applicant had not presented any evidence which demonstrated that he had been persecuted during his long career and found it unlikely that he would be persecuted now, at the end of his career.
- Evidence: `issue` cue `issue` at chunk `5241620` offsets `14-19`; context: [16] The sole issue in this case is the following: were the Board’s findings reasonable?
- Evidence: `reasoning_application` cue `because` at chunk `5241621` offsets `1949-1956`; context: (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
- Evidence: `reasoning_application` cue `therefore` at chunk `5241622` offsets `111-120`; context: [18] It is trite law that the Board’s findings on credibility and implausibility are questions of fact and are therefore reviewable according to the standard of reasonableness (Aguebor v Canada (Minister of Employment and Immigration) (F.
- Evidence: `reasoning_application` cue `because` at chunk `5241623` offsets `198-205`; context: [19] Essentially, the Court notes that the Board found it to be implausible that the principal applicant would be persecuted by the presidential security forces at the end of his long career merely because he had reported a financial irregularity in the amount of $23 million while carrying out his duties as an auditor for the Ministry of Finance.
- Evidence: `evidence_fact` cue `evidence` at chunk `5241624` offsets `102-110`; context: [20] However, the Court is of the view that, in the case at bar, this finding is not supported by any evidence and as such, the Board could not reasonably make the implausibility finding that it did as it is not based on the documentation on record.
- Evidence: `evidence_fact` cue `Record` at chunk `5241625` offsets `253-259`; context: [21] For instance, the Court makes reference to civil servant Steve Nyembo, a senior official at the Tax Department who was murdered and had his genitals cut off for denouncing tax funds being misappropriated by the office of the President (Applicant’s Record, pp 102 and 103):
- Evidence: `evidence_fact` cue `evidence` at chunk `5241626` offsets `71-79`; context: [22] The Court is of the opinion that the Board could not dismiss this evidence out of hand.

#### 26403:1:subtheme:4 · paragraphs 23-24

- Raw key terms: `hearing, record, accepts, addressed, allowed, although, applicant, application`
- Display key terms: `hearing, accepts, addressed, allowed, although`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, issue`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, issue Display terms: hearing, accepts, addressed, allowed, although Operative outcome context: The application is allowed. Evidence spans paragraphs 23-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5241627` offsets `262-267`; context: Although the Court accepts the respondent’s argument that this issue was addressed and discussed during the hearing (Tribunal’s Record, pp 317-320 and 826-833), it was completely ignored by the Board in its decision.
- Evidence: `evidence_fact` cue `evidence` at chunk `5241627` offsets `189-197`; context: This statement was unfounded and unsupported by the evidence.
- Evidence: `counterargument_limitation` cue `Although` at chunk `5241627` offsets `199-207`; context: Although the Court accepts the respondent’s argument that this issue was addressed and discussed during the hearing (Tribunal’s Record, pp 317-320 and 826-833), it was completely ignored by the Board in its decision.
- Evidence: `disposition` cue `allowed` at chunk `5241627` offsets `477-484`; context: The application is allowed.

#### Section text

Kipa Numbi v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2012-08-30
Neutral citation
2012 FC 1037
File numbers
IMM-92-12
Decision Content
Date: 20120830
Docket: IMM-92-12
Citation: 2012 FC 1037
Ottawa, Ontario, August 30, 2012
PRESENT: The Honourable Mr. Justice Boivin
BETWEEN:
GASTON KIPA NUMBI
FRANÇOISE TSHIKUDI NDJIBU
Applicants
and
LE MINISTER DE LA CITOYENNETÉ
ET DE L’IMMIGRATION
Respondent
REASONS FOR JUDGMENT AND JUDGMENT

[1] This is an application pursuant to subsection 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [Act] for judicial review of the decision rendered by the Refugee Protection Division of the Immigration and Refugee Board (the Board) dated December 12, 2011, which refused the applicants’ claim to be deemed Convention refugees or persons in need of protection under sections 96 and 97 of the Act.
I. Factual Background

[2] The applicants, Mr. Gaston Kipa Numbi (the principal applicant) and his wife, Ms. Françoise Tshikudi Ndjibu, are both citizens of the Democratic Republic of the Congo (the DRC). They seek protection in Canada as they fear persecution by the DRC government in light of the fact that the principal applicant denounced the corruption and the embezzlement of funds carried out by the Congolese president.

[3] The principal applicant has worked as a civil servant in the Congolese Ministry of Finance for approximately thirty (30) years.

[4] In July 2006, the principal applicant alleges that he was appointed to the head of a government body that was mandated to investigate financial impropriety, contentious fiscal cases and recover tax or custom payments that had not been properly paid to the government.

[5] On March 30, 2010, in the course of his duties, the principal applicant presented himself at the customs and excise office in order to collect funds that were supposed to have been paid by a company to the customs department. However, the applicant maintains that he learned from the Receiver that the funds had been transferred to an account managed by the President of the DRC. These funds totalled approximately $23 million USD.

[6] The principal applicant alleges that he reported this irregularity and, as a result, he affirms that he subsequently became the target of the security forces of the Congolese president.

[7] On April 15, 2010, the principal applicant affirms that he received a telephone call from one of his colleagues who warned him not to return to his office as the presidential security forces were there to arrest him. Consequently, he maintains that he never returned to his office.

[8] The principal applicant also alleges that he began to receive anonymous and threatening telephone calls and unexpected visits from the presidential security forces at his home. As a result, he explains that he decided to leave and hide at a family member’s house.

[9] Fearing for his life, the principal applicant maintains that he requested a one-year leave from his place of work and applied for Canadian visitors visas.

[10] The applicants arrived in Canada on July 5, 2010 and filed for refugee protection on August 11, 2010.

[11] The applicants’ refugee claim was heard by the Board on November 14, 2011.
II. Decision under Review

[12] The Board rejected the applicants’ refugee claim as it found that the determinative issue was the lack of credibility of their account.

[13] The Board found it to be implausible that the applicants would be persecuted by the presidential security forces merely because the principal applicant had reported the irregularity while carrying out his duties as a civil servant. The Board concluded that the principal applicant had no other choice but to inform his supervisor that the funds had been transferred to an account managed by the Congolese president and that he was not in possession of these funds.

[14] Rather, the Board noted that it was likely that after a long career in the public service, that the applicant merely wanted to retire in Canada. The Board observed that the applicants had not left the DRC in a hurry but had taken their time to plan their trip and to obtain Canadian visas.

[15] The Board also acknowledged that the applicants had submitted substantial documentation indicating the human rights abuses in the DRC. The Board affirmed that it was aware of the country’s violations. However, the Board concluded that, as a government employee, the applicant had not presented any evidence which demonstrated that he had been persecuted during his long career and found it unlikely that he would be persecuted now, at the end of his career.
III. Issue

[16] The sole issue in this case is the following: were the Board’s findings reasonable?
IV. Statutory Provisions

[17] The following provisions of the Immigration and Refugee Protection Act are applicable in these proceedings:
Refugee Protection, Convention Refugees and Persons in Need of Protection
Convention refugee
96. A Convention refugee is a person who, by reason of a well-founded fear of persecution for reasons of race, religion, nationality, membership in a particular social group or political opinion,
(a) is outside each of their countries of nationality and is unable or, by reason of that fear, unwilling to avail themself of the protection of each of those countries; or
(b) not having a country of nationality, is outside the country of their former habitual residence and is unable or, by reason of that fear, unwilling to return to that country.
Notions d’asile, de rÉfugiÉ et de personne à protÉger
Définition de « réfugié »
96. A qualité de réfugié au sens de la Convention – le réfugié – la personne qui, craignant avec raison d’être persécutée du fait de sa race, de sa religion, de sa nationalité, de son appartenance à un groupe social ou de ses opinions politiques :
a) soit se trouve hors de tout pays dont elle a la nationalité et ne peut ou, du fait de cette crainte, ne veut se réclamer de la protection de chacun de ces pays;
b) soit, si elle n’a pas de nationalité et se trouve hors du pays dans lequel elle avait sa résidence habituelle, ne peut ni, du fait de cette crainte, ne veut y retourner.
Person in need of protection
97. (1) A person in need of protection is a person in Canada whose removal to their country or countries of nationality or, if they do not have a country of nationality, their country of former habitual residence, would subject them personally
(a) to a danger, believed on substantial grounds to exist, of torture within the meaning of Article 1 of the Convention Against Torture; or
(b) to a risk to their life or to a risk of cruel and unusual treatment or punishment if
(i) the person is unable or, because of that risk, unwilling to avail themself of the protection of that country,
(ii) the risk would be faced by the person in every part of that country and is not faced generally by other individuals in or from that country,
(iii) the risk is not inherent or incidental to lawful sanctions, unless imposed in disregard of accepted international standards, and
(iv) the risk is not caused by the inability of that country to provide adequate health or medical care.
Person in need of protection
(2) A person in Canada who is a member of a class of persons prescribed by the regulations as being in need of protection is also a person in need of protection.
Personne à protéger
97. (1) A qualité de personne à protéger la personne qui se trouve au Canada et serait personnellement, par son renvoi vers tout pays dont elle a la nationalité ou, si elle n’a pas de nationalité, dans lequel elle avait sa résidence habituelle, exposée :
a) soit au risque, s’il y a des motifs sérieux de le croire, d’être soumise à la torture au sens de l’article premier de la Convention contre la torture;
b) soit à une menace à sa vie ou au risque de traitements ou peines cruels et inusités dans le cas suivant :
(i) elle ne peut ou, de ce fait, ne veut se réclamer de la protection de ce pays,
(ii) elle y est exposée en tout lieu de ce pays alors que d’autres personnes originaires de ce pays ou qui s’y trouvent ne le sont généralement pas,
(iii) la menace ou le risque ne résulte pas de sanctions légitimes — sauf celles infligées au mépris des normes internationales — et inhérents à celles-ci ou occasionnés par elles,
(iv) la menace ou le risque ne résulte pas de l’incapacité du pays de fournir des soins médicaux ou de santé adéquats.
Personne à protéger
(2) A également qualité de personne à protéger la personne qui se trouve au Canada et fait partie d’une catégorie de personnes auxquelles est reconnu par règlement le besoin de protection.

[18] It is trite law that the Board’s findings on credibility and implausibility are questions of fact and are therefore reviewable according to the standard of reasonableness (Aguebor v Canada (Minister of Employment and Immigration) (F.C.A.), [1993] FCJ No 732, 160 NR 315; Hafeez v Canada (Minister of Citizenship and Immigration), 2012 FC 747 at para 13, [2012] FCJ No 798; Cekim v Canada (Minister of Citizenship and Immigration), 2011 FC 177 at para 6, [2011] FCJ No 221; Dunsmuir v New Brunswick, 2008 SCC 9, [2008] 1 SCR 190).

[19] Essentially, the Court notes that the Board found it to be implausible that the principal applicant would be persecuted by the presidential security forces at the end of his long career merely because he had reported a financial irregularity in the amount of $23 million while carrying out his duties as an auditor for the Ministry of Finance. The Court recalls that the Board is entitled to make credibility findings based on implausibility, common sense and rationality (Cooper v Canada (Minister of Citizenship and Immigration), 2012 FC 118, [2012] FCJ No 135; Hilo v Canada (Minister of Employment and Immigration) (F.C.A.), [1991] FCJ No 228, 130 NR 236; RKL v Canada (Minister of Citizenship and Immigration), 2003 FCT 116, 228 FTR 43).

[20] However, the Court is of the view that, in the case at bar, this finding is not supported by any evidence and as such, the Board could not reasonably make the implausibility finding that it did as it is not based on the documentation on record. More particularly, the Court finds that the Board’s implausibility finding was not adequately supported by the evidence and was not nourished by content. Indeed, the applicants had drawn the Board’s attention to various documents relating to the murders of certain individuals (civil servants, politicians, journalists and activists with non-governmental organizations) who had denounced the misappropriation of funds by the Congolese state (Tribunal’s Record, pp 833 and 838). Though this evidence was provided to the Board, it was not treated and/or analysed in its decision (Fok v Canada (Minister of Employment and Immigration) (F.C.A.), [1993] FCJ No. 800 (available on QL); Zakhour v Canada (Minister of Citizenship and Immigration), 2011 FC 1178, [2011] FCJ No 1449).

[21] For instance, the Court makes reference to civil servant Steve Nyembo, a senior official at the Tax Department who was murdered and had his genitals cut off for denouncing tax funds being misappropriated by the office of the President (Applicant’s Record, pp 102 and 103):

[22] The Court is of the opinion that the Board could not dismiss this evidence out of hand. It had the obligation to treat this information, as well as the principal applicant’s testimony, in its decision. In this regard, the Board’s decision was unreasonable.

[23] Also, the Board erred in speculating that the principal applicant merely wished to stay in Canada in order to enjoy his retirement. This statement was unfounded and unsupported by the evidence. Although the Court accepts the respondent’s argument that this issue was addressed and discussed during the hearing (Tribunal’s Record, pp 317-320 and 826-833), it was completely ignored by the Board in its decision.
JUDGMENT
THIS COURT’S JUDGMENT is that
1. The application is allowed.
2. The decision is quashed and the matter is returned for reconsideration by a differently constituted panel of the Board.
3. There is no question for certification.
“Richard Boivin”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET: IMM-92-12
STYLE OF CAUSE: Gaston Kipa Numbi et al v MCI
PLACE OF HEARING: Toronto, Ontario
DATE OF HEARING: July 26, 2012
REASONS FOR 

## 26403:2 · paragraphs 25-25

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `c798c6306d6ccd8e53aaefcd7d8b2c900ad1d805c30cf4ca9c8973e29de125fa`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 26403:2:subtheme:1 · paragraphs 25-25

- Raw key terms: `appearances, applicants, attorney, august, boivin, boulakia, canada, dated`
- Display key terms: `august, boivin, boulakia, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, boivin, boulakia, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 25-25. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT: BOIVIN J.
DATED: August 30, 2012
APPEARANCES:
Raoul Boulakia
FOR THE APPLICANTS
Sybil Thompson
FOR THE RESPONDENT
SOLICITORS OF RECORD:
Law firm of Raoul Boulakia
Toronto, Ontario
FOR THE APPLICANTS
Myles J. Kirvan
Deputy Attorney General of Canada
FOR THE RESPONDENT
