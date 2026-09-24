# Discussion Units: case 12123

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **15**
- Continuity pairs: **14**
- Discussion Units: **4**
- Paragraph source hashes: **15**
- Sub-themes: **6**

## 12123:1 · paragraphs 0-9

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3e0a94e1fe015f20ddd1b9b7b9ab8c1819c91229fff2404814b8ecbec3bc26ba`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12123:1:subtheme:1 · paragraphs 0-3

- Raw key terms: `zhou, hearing, oral, appeal, china, credibility, decision, file`
- Display key terms: `zhou, hearing, oral, china, credibility, file`
- Argument roles: `disposition, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, party_position, reasoning_application Display terms: zhou, hearing, oral, china, credibility, file Position/evidence statements: [2] Before the RAD, the Minister intervened to file new evidence in the form of US visa applications that had previously been submitted by Mr Zhou and his father. Application context: Therefore, I will allow this application for judicial review Operative outcome context: A panel of the Immigration and Refugee Board denied his claim and, on appeal, the Refugee Appeal Division (RAD) upheld the Board’s decision. Evidence spans paragraphs 0-3. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `denied` at chunk `4607027` offsets `595-601`; context: A panel of the Immigration and Refugee Board denied his claim and, on appeal, the Refugee Appeal Division (RAD) upheld the Board’s decision.
- Evidence: `party_position` cue `submitted` at chunk `4607028` offsets `126-135`; context: [2] Before the RAD, the Minister intervened to file new evidence in the form of US visa applications that had previously been submitted by Mr Zhou and his father.
- Evidence: `evidence_fact` cue `evidence` at chunk `4607028` offsets `56-64`; context: [2] Before the RAD, the Minister intervened to file new evidence in the form of US visa applications that had previously been submitted by Mr Zhou and his father.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4607030` offsets `127-136`; context: Therefore, I will allow this application for judicial review

#### 12123:1:subtheme:2 · paragraphs 4-6

- Raw key terms: `evidence, hearing, hold, however, oral, claim, concluded, criteria`
- Display key terms: `hearing, hold, however, oral, concluded, criteria`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position Display terms: hearing, hold, however, oral, concluded, criteria Position/evidence statements: The RAD’s Decision [6] Mr Zhou claimed that he was being sought by authorities in China after he and his family protested against the proposed expropriation of their farm. Evidence spans paragraphs 4-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4607031` offsets `13-18`; context: [5] The sole issue is whether the RAD was obliged to hold an oral hearing.
- Evidence: `party_position` cue `claimed` at chunk `4607031` offsets `110-117`; context: The RAD’s Decision [6] Mr Zhou claimed that he was being sought by authorities in China after he and his family protested against the proposed expropriation of their farm.
- Evidence: `evidence_fact` cue `evidence` at chunk `4607031` offsets `341-349`; context: However, the new evidence tendered by the Minister showed that the family did not own a farm, they lived in an urban apartment building, and that Mr Zhou did not attend college.
- Evidence: `counterargument_limitation` cue `However` at chunk `4607031` offsets `324-331`; context: However, the new evidence tendered by the Minister showed that the family did not own a farm, they lived in an urban apartment building, and that Mr Zhou did not attend college.
- Evidence: `issue` cue `issue` at chunk `4607032` offsets `226-231`; context: Subsection 110(6) of IRPA provides that the RAD may hold a hearing if there is documentary evidence before it raising a serious issue of credibility that is central to the claim and would justify allowing or rejecting it.
- Evidence: `evidence_fact` cue `evidence` at chunk `4607032` offsets `189-197`; context: Subsection 110(6) of IRPA provides that the RAD may hold a hearing if there is documentary evidence before it raising a serious issue of credibility that is central to the claim and would justify allowing or rejecting it.
- Evidence: `counterargument_limitation` cue `However` at chunk `4607032` offsets `320-327`; context: However, the RAD concluded that it had a discretion whether to hold a hearing and decided not to do so in the absence of a specific request.
- Evidence: `evidence_fact` cue `evidence` at chunk `4607033` offsets `21-29`; context: [8] Based on the new evidence, the RAD concluded that Mr Zhou’s claim of persecution arising from expropriation of the family farm was not credible.
- Evidence: `counterargument_limitation` cue `however` at chunk `4607033` offsets `318-325`; context: In my view, however, an oral hearing will generally be required when the statutory criteria have been satisfied.

#### 12123:1:subtheme:3 · paragraphs 7-9

- Raw key terms: `hearing, oral, appeal, circumstances, credibility, generally, irpa, refugee`
- Display key terms: `hearing, oral, circumstances, credibility, generally, irpa, refugee`
- Argument roles: `governing_rule, issue, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, reasoning_application Display terms: hearing, oral, circumstances, credibility, generally, irpa, refugee Rule/authority context: [10] In an analogous context, officers conducting a pre-removal risk assessment must generally hold an oral hearing in similar circumstances (under s 113(b) of IRPA, and s 167 of the Immigration and Refugee Protection Re Application context: [11] I believe the same should apply here. | [12] Therefore, in this case, I find that the RAD should have convened an oral hearing before dismissing Mr Zhou’s appeal on credibility grounds. Evidence spans paragraphs 7-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4607034` offsets `422-428`; context: Even though the language is equally permissive (“a hearing may be held”), this Court has held that an oral hearing will usually be required where there are serious credibility issues before the officer that are central to the decision (Strachn v Canada (Minister of Citizenship and Immigration), 2012 FC 984, at para 34).
- Evidence: `governing_rule` cue `under` at chunk `4607034` offsets `142-147`; context: [10] In an analogous context, officers conducting a pre-removal risk assessment must generally hold an oral hearing in similar circumstances (under s 113(b) of IRPA, and s 167 of the Immigration and Refugee Protection Regulations, SOR/2002-227).
- Evidence: `issue` cue `question` at chunk `4607035` offsets `206-214`; context: Obviously, the RAD retains a discretion on this question but that discretion must be exercised reasonably in the circumstances.
- Evidence: `reasoning_application` cue `apply` at chunk `4607035` offsets `31-36`; context: [11] I believe the same should apply here.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4607036` offsets `5-14`; context: [12] Therefore, in this case, I find that the RAD should have convened an oral hearing before dismissing Mr Zhou’s appeal on credibility grounds.

#### Section text

Zhuo v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2015-07-27
Neutral citation
2015 FC 911
File numbers
IMM-2693-14
Decision Content
Date: 20150727
Docket: IMM-2693-14
Citation: 2015 FC 911
Ottawa, Ontario, July 27, 2015
PRESENT: The Honourable Mr. Justice O'Reilly
BETWEEN:
JIN HAN ZHUO
Applicant
and
THE MINISTER OF CITIZENSHIP
AND IMMIGRATION
Respondent
JUDGMENT AND REASONS
I. Overview [1] In 2013, Mr Jin Han Zhou sought refugee protection in Canada based on his fear of political persecution in China. A panel of the Immigration and Refugee Board denied his claim and, on appeal, the Refugee Appeal Division (RAD) upheld the Board’s decision.

[2] Before the RAD, the Minister intervened to file new evidence in the form of US visa applications that had previously been submitted by Mr Zhou and his father. The RAD admitted the new evidence and found that it substantially contradicted Mr Zhou’s evidence about his experiences in China, and negatively affected his credibility. While the RAD found that the circumstances likely justified holding an oral hearing, it chose not to convene one since neither Mr Zhou nor the Minister had requested it.

[3] Mr Zhou now argues that the RAD was obliged to hold an oral hearing, even if one was not requested, when the applicable statutory criteria were met (Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], s 110(6)) (see Annex for provisions cited). He asks me to quash the RAD’s decision and order another panel member to reconsider his appeal.

[4] I agree with Mr Zhou that the RAD should have held an oral hearing before making adverse credibility findings against him. Therefore, I will allow this application for judicial review

[5] The sole issue is whether the RAD was obliged to hold an oral hearing.
II. The RAD’s Decision [6] Mr Zhou claimed that he was being sought by authorities in China after he and his family protested against the proposed expropriation of their farm. He also said that he had been suspended from college for his activities. However, the new evidence tendered by the Minister showed that the family did not own a farm, they lived in an urban apartment building, and that Mr Zhou did not attend college.

[7] The RAD acknowledged that the criteria for holding an oral hearing appeared to have been met. Subsection 110(6) of IRPA provides that the RAD may hold a hearing if there is documentary evidence before it raising a serious issue of credibility that is central to the claim and would justify allowing or rejecting it. However, the RAD concluded that it had a discretion whether to hold a hearing and decided not to do so in the absence of a specific request.

[8] Based on the new evidence, the RAD concluded that Mr Zhou’s claim of persecution arising from expropriation of the family farm was not credible.
III. Was the RAD obliged to hold an oral hearing? [9] The legislation clearly states that the RAD “may” hold a hearing where the statutory criteria are met. In my view, however, an oral hearing will generally be required when the statutory criteria have been satisfied.

[10] In an analogous context, officers conducting a pre-removal risk assessment must generally hold an oral hearing in similar circumstances (under s 113(b) of IRPA, and s 167 of the Immigration and Refugee Protection Regulations, SOR/2002-227). Even though the language is equally permissive (“a hearing may be held”), this Court has held that an oral hearing will usually be required where there are serious credibility issues before the officer that are central to the decision (Strachn v Canada (Minister of Citizenship and Immigration), 2012 FC 984, at para 34).

[11] I believe the same should apply here. Where the conditions for holding an oral hearing are present, the RAD should generally be required to convene one. Obviously, the RAD retains a discretion on this question but that discretion must be exercised reasonably in the circumstances. In particular, the mere fact that a party has not requested a hearing will generally not be sufficient reason to justify a refusal to convene one when the circumstances appear to require it. While the RAD rules allow an appellant to request a hearing, IRPA does not actually impose a burden either to request, or to satisfy the RAD that the circumstances merit, an oral hearing (see Refugee Appeal Division Rules, SOR/2012-257, Rule 5(2)(d)(iii)). The onus rests with the RAD to consider and apply the statutory criteria reasonably.

[12] Therefore, in this case, I find that the RAD should have convened an oral hearing before dismissing Mr Zhou’s appeal on credibility grounds.


## 12123:2 · paragraphs 10-10

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `12607782fca33e50523711b7bbb85bd3b6b028bc8246a09f45f2c1cbea72049d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12123:2:subtheme:1 · paragraphs 10-10

- Raw key terms: `another, appeal, circumstances, conclusion, convened, dismissal, disposition, hearing`
- Display key terms: `another, circumstances, conclusion, convened, dismissal, disposition, hearing`
- Argument roles: `reasoning_application`
- Explanation: Observed roles: reasoning_application Display terms: another, circumstances, conclusion, convened, dismissal, disposition, hearing Application context: I must, therefore, overturn its dismissal of Mr Zhou’s appeal and order another panel of the RAD to reconsider it. Evidence spans paragraphs 10-10. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `therefore` at chunk `4607036` offsets `258-267`; context: I must, therefore, overturn its dismissal of Mr Zhou’s appeal and order another panel of the RAD to reconsider it.

#### Section text

IV. Conclusion and Disposition [13] In the circumstances, the RAD should have convened an oral hearing. I must, therefore, overturn its dismissal of Mr Zhou’s appeal and order another panel of the RAD to reconsider it.

## 12123:3 · paragraphs 11-13

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `b37f2b3d216711ce59ebc915188b54f61cbc8edb42f06624fff0dab234620b20`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12123:3:subtheme:1 · paragraphs 11-13

- Raw key terms: `hearing, cause, counsel, following, hold, immigration, minister, proposed`
- Display key terms: `hearing, following, hold, proposed`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: hearing, following, hold, proposed Rule/authority context: For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following: 167. Application context: Therefore, he says, the proposed question should not be stated. Operative outcome context: The application for judicial review is allowed. Evidence spans paragraphs 11-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4607037` offsets `48-56`; context: [14] Counsel for Mr Zhou proposed the following question for certification:
Is the RAD required to hold an oral hearing when the criteria set out in s 110(6) of IRPA are met?
- Evidence: `issue` cue `whether` at chunk `4607038` offsets `59-66`; context: [15] Counsel for the Minister points out that the decision whether to convene a hearing is clearly discretionary and each case should be reviewed on its own facts.
- Evidence: `evidence_fact` cue `evidence` at chunk `4607038` offsets `888-896`; context: (6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
110.
- Evidence: `governing_rule` cue `under` at chunk `4607038` offsets `2192-2197`; context: For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
167.
- Evidence: `reasoning_application` cue `Therefore` at chunk `4607038` offsets `164-173`; context: Therefore, he says, the proposed question should not be stated.
- Evidence: `disposition` cue `allowed` at chunk `4607038` offsets `505-512`; context: The application for judicial review is allowed.

#### Section text

[14] Counsel for Mr Zhou proposed the following question for certification:
Is the RAD required to hold an oral hearing when the criteria set out in s 110(6) of IRPA are met?

[15] Counsel for the Minister points out that the decision whether to convene a hearing is clearly discretionary and each case should be reviewed on its own facts. Therefore, he says, the proposed question should not be stated. I agree. As discussed above, the RAD retains a discretion that must be exercised reasonably. Therefore, I would not certify a question based on a proposition that the RAD has no such discretion.
JUDGMENT
THIS COURT’S JUDGMENT is that:
1. The application for judicial review is allowed.
2. The matter is returned to the RAD for redetermination.
3. No question of general importance is stated.
“James W. O’Reilly”
Judge
ANNEX
Immigration and Refugee Protection Act, SC 2001, c 27
Loi sur l’immigration et la protection des réfugiés, LC 2001, ch 27
Hearing
Audience
110. (6) The Refugee Appeal Division may hold a hearing if, in its opinion, there is documentary evidence referred to in subsection (3)
110. (6) La section peut tenir une audience si elle estime qu’il existe des éléments de preuve documentaire visés au paragraphe (3) qui, à la fois :
(a) that raises a serious issue with respect to the credibility of the person who is the subject of the appeal;
a) soulèvent une question importante en ce qui concerne la crédibilité de la personne en cause;
(b) that is central to the decision with respect to the refugee protection claim; and
b) sont essentiels pour la prise de la décision relative à la demande d’asile;
(c) that, if accepted, would justify allowing or rejecting the refugee protection claim.
c) à supposer qu’ils soient admis, justifieraient que la demande d’asile soit accordée ou refusée, selon le cas.
Consideration of application
Examen de la demande
113. Consideration of an application for protection shall be as follows:
113. Il est disposé de la demande comme il suit :
…
[…]
(b) a hearing may be held if the Minister, on the basis of prescribed factors, is of the opinion that a hearing is required;
b) une audience peut être tenue si le ministre l’estime requis compte tenu des facteurs réglementaires;
Hearing — prescribed factors
Facteurs pour la tenue d’une audience
167. For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
167. Pour l’application de l’alinéa 113b) de la Loi, les facteurs ci-après servent à décider si la tenue d’une audience est requise :
(a) whether there is evidence that raises a serious issue of the applicant's credibility and is related to the factors set out in sections 96 and 97 of the Act;
a) l’existence d’éléments de preuve relatifs aux éléments mentionnés aux articles 96 et 97 de la Loi qui soulèvent une question importante en ce qui concerne la crédibilité du demandeur;
(b) whether the evidence is central to the decision with respect to the application for protection; and
b) l’importance de ces éléments de preuve pour la prise de la décision relative à la demande de protection;
(c) whether the evidence, if accepted, would justify allowing the application for protection.
c) la question de savoir si ces éléments de preuve, à supposer qu’ils soient admis, justifieraient que soit accordée la protection.
Refugee Appeal Division Rules, SOR/2012-257
Règles de la Section d’appel des réfugiés, DORS/2012-257
Hearing — prescribed factors
Facteurs pour la tenue d’une audience
167. For the purpose of determining whether a hearing is required under paragraph 113(b) of the Act, the factors are the following:
167. Pour l’application de l’alinéa 113b) de la Loi, les facteurs ci-après servent à décider si la tenue d’une audience est requise :
(a) whether there is evidence that raises a serious issue of the applicant's credibility and is related to the factors set out in sections 96 and 97 of the Act;
a) l’existence d’éléments de preuve relatifs aux éléments mentionnés aux articles 96 et 97 de la Loi qui soulèvent une question importante en ce qui concerne la crédibilité du demandeur;
(b) whether the evidence is central to the decision with respect to the application for protection; and
b) l’importance de ces éléments de preuve pour la prise de la décision relative à la demande de protection;
(c) whether the evidence, if accepted, would justify allowing the application for protection.
c) la question de savoir si ces éléments de preuve, à supposer qu’ils soient admis, justifieraient que soit accordée la protection.
Refugee Appeal Division Rules, SOR/2012-257
Règles de la Section d’appel des réfugiés, DORS/2012-257
Content of reply record
Contenu du dossier de réplique
5. (2) The reply record must contain the following documents, on consecutively numbered pages, in the following order:
5. (2) Le dossier de réplique comporte les documents ci-après, sur des pages numérotées consécutivement, dans l’ordre qui suit :
…
[…]
(d) a memorandum that includes full and detailed submissions regarding:
d) un mémoire qui inclut des observations complètes et détaillées concernant :
…
[…]
(iii) why the Division should hold a hearing under subsection 110(6) of the Act if the appellant is requesting that a hearing be held and they did not include such a request in the appellant’s record, and if the appellant is requesting a hearing, whether they are making an application under rule 66 to change the location of the hearing.
(iii) les motifs pour lesquels la Section devrait tenir l’audience visée au paragraphe 110(6) de la Loi, si l’appelant en fait la demande et qu’il n’a pas inclus cette demande dans le dossier de l’appelant, et le cas échéant, s’il fait une demande de changement de lieu de l’audience en vertu de la règle 66.
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-2693-14
STYLE OF CAUSE:
JIN HAN ZHUO v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
April 28, 2015


## 12123:4 · paragraphs 14-14

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1c4f7318dd23aad6cb6d77adb812e619ec2c1c1c4e2502c4a3d6b6052688df71`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 12123:4:subtheme:1 · paragraphs 14-14

- Raw key terms: `appearances, applicant, attorney, barristers, canada, chris, dated, deputy`
- Display key terms: `barristers, chris, dated, deputy`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: barristers, chris, dated, deputy No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 14-14. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
O'REILLY J.
DATED:
July 27, 2015
APPEARANCES:
Michael Korman
For The Applicant
Chris Ezrin
For The Respondent
SOLICITORS OF RECORD:
Otis & Korman
Barristers and Solicitors
Toronto, Ontario
For The Applicant
William F. Pentney
Deputy Attorney General of Canada
Toronto, Ontario
For The Respondent
