# Discussion Units: case 4090

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **30**
- Continuity pairs: **29**
- Discussion Units: **3**
- Paragraph source hashes: **30**
- Sub-themes: **7**

## 4090:1 · paragraphs 0-26

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `6680a4552e45777dc36944d108ffb72820aac8e786536ad25fa26e36dfc4e36d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4090:1:subtheme:1 · paragraphs 0-5

- Raw key terms: `applicants, canada, kanawati, protection, refugee, basis, bilal, claim`
- Display key terms: `kanawati, protection, refugee, basis, bilal`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: kanawati, protection, refugee, basis, bilal Position/evidence statements: [2] The principal applicant, Youssef Soultani Kanawati, claims that in April 2016 he was approached by Bilal Akar, a well-known member of the group, who encouraged him to join the group. | [3] The applicants submitted an inland claim for refugee protection on October 21, 2016. Application context: Kanawati, the member gave it no weight because Mr. Evidence spans paragraphs 0-5. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `claims` at chunk `4238636` offsets `56-62`; context: [2] The principal applicant, Youssef Soultani Kanawati, claims that in April 2016 he was approached by Bilal Akar, a well-known member of the group, who encouraged him to join the group.
- Evidence: `party_position` cue `submitted` at chunk `4238637` offsets `19-28`; context: [3] The applicants submitted an inland claim for refugee protection on October 21, 2016.
- Evidence: `evidence_fact` cue `testimony` at chunk `4238639` offsets `264-273`; context: Kanawati in support of the claim and his testimony at the hearing.
- Evidence: `reasoning_application` cue `because` at chunk `4238639` offsets `620-627`; context: Kanawati, the member gave it no weight because Mr.
- Evidence: `counterargument_limitation` cue `However` at chunk `4238639` offsets `508-515`; context: However, since the report relied entirely on information provided by Mr.

#### 4090:1:subtheme:2 · paragraphs 6-7

- Raw key terms: `applicants, decision, protection, refugee, appeal, appealed, application, brought`
- Display key terms: `protection, refugee, appealed, brought`
- Argument roles: `disposition, governing_rule`
- Explanation: Observed roles: disposition, governing_rule Display terms: protection, refugee, appealed, brought Rule/authority context: Kaminker again and brought this application for judicial review of the RAD’s decision under section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA]. Operative outcome context: In a decision dated November 28, 2018, the RAD dismissed the appeal and confirmed the RPD’s determination that the applicants are neither Convention refugees nor persons in need of protection. Evidence spans paragraphs 6-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4238640` offsets `163-172`; context: In a decision dated November 28, 2018, the RAD dismissed the appeal and confirmed the RPD’s determination that the applicants are neither Convention refugees nor persons in need of protection.
- Evidence: `governing_rule` cue `under` at chunk `4238641` offsets `123-128`; context: Kaminker again and brought this application for judicial review of the RAD’s decision under section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].

#### 4090:1:subtheme:3 · paragraphs 8-15

- Raw key terms: `applicants, decision, para, vavilov, appeal, application, court, majority`
- Display key terms: `para, vavilov, majority`
- Argument roles: `disposition, evidence_fact, governing_rule, party_position`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, party_position Display terms: para, vavilov, majority Position/evidence statements: [12] The applicants contend that it was unreasonable for the RAD to uphold the RPD’s negative credibility findings and to fail to consider the potentially corroborative documents (i. Rule/authority context: That this is the appropriate standard is reinforced by Canada (Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov], where the majority of the Court set out a revised framework for determining the standard of re | The principles the majority emphasizes were drawn in large measure from prior jurisprudence, including Dunsmuir v New Brunswick, [2008] 1 S. Operative outcome context: [8] For the reasons that follow, the application will be dismissed. Evidence spans paragraphs 8-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `4238642` offsets `57-66`; context: [8] For the reasons that follow, the application will be dismissed.
- Evidence: `governing_rule` cue `standard of review` at chunk `4238643` offsets `391-409`; context: That this is the appropriate standard is reinforced by Canada (Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov], where the majority of the Court set out a revised framework for determining the standard of review with respect to the merits of an administrative decision (at para 10).
- Evidence: `governing_rule` cue `principles` at chunk `4238644` offsets `125-135`; context: The principles the majority emphasizes were drawn in large measure from prior jurisprudence, including Dunsmuir v New Brunswick, [2008] 1 S.
- Evidence: `party_position` cue `contend` at chunk `4238646` offsets `20-27`; context: [12] The applicants contend that it was unreasonable for the RAD to uphold the RPD’s negative credibility findings and to fail to consider the potentially corroborative documents (i.
- Evidence: `evidence_fact` cue `testimony` at chunk `4238648` offsets `198-207`; context: Kanawati to the RAD dated February 22, 2018, in effect the applicants raised three related errors by the RPD: first, the differences between the original narrative and the testimony before the RPD were not material; second, Mr.
- Evidence: `governing_rule` cue `under` at chunk `4238648` offsets `282-287`; context: Kanawati stated that he was under a lot of stress and very nervous when he provided the information for the original narrative; and third, he was “perhaps, wrongly advised, to be as brief & to the point in my application as possible.
- Evidence: `governing_rule` cue `pursuant to` at chunk `4238649` offsets `153-164`; context: [15] The errors alleged by the applicants were reiterated in substance and without further elaboration in the Applicants’ Memorandum to the RAD prepared pursuant to the requirements of Rule 3(3)(g) of the Refugee Appeal Division Rules, SOR/2012-257.

#### 4090:1:subtheme:4 · paragraphs 16-21

- Raw key terms: `applicants, member, basis, credibility, failed, omissions, allegations, appellants`
- Display key terms: `basis, credibility, failed, omissions, allegations, appellants`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: basis, credibility, failed, omissions, allegations, appellants Position/evidence statements: As Justice McDonald stated recently in Ogaulu v Canada (Citizenship and Immigration), 2019 FC 547 [Ogaulu], this Court “has confirmed on numerous occasions that all the important facts and details of a claim must be incl | Kanawati stated in his BOC that he worked as a plumber and that his job “exposes him to many people,” he failed to mention that he often worked for high placed civilian and military officials in Lebanon and that this was Application context: ” The member therefore concluded that “there is insufficient evidence to support the Appellants’ speculation that ‘perhaps’ they were given wrong advice. | [20] It was not unreasonable for the RAD member to conclude that the RPD’s findings regarding the omissions from the BOC “were well-founded and central to the key allegations of the Appellants’ risk of persecution. Operative outcome context: [19] In the present case, the RAD upheld the RPD’s determination that Mr. Evidence spans paragraphs 16-21. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4238650` offsets `449-454`; context: Kanawati did not raise the issue of stress or anxiety at the RPD hearing and provided no medical evidence of an impairment that would have prevented him from completing his BOC properly.
- Evidence: `evidence_fact` cue `record` at chunk `4238650` offsets `101-107`; context: The member confirmed that she had reviewed the record in its entirety.
- Evidence: `evidence_fact` cue `evidence` at chunk `4238651` offsets `388-396`; context: ” The member therefore concluded that “there is insufficient evidence to support the Appellants’ speculation that ‘perhaps’ they were given wrong advice.
- Evidence: `reasoning_application` cue `therefore` at chunk `4238651` offsets `340-349`; context: ” The member therefore concluded that “there is insufficient evidence to support the Appellants’ speculation that ‘perhaps’ they were given wrong advice.
- Evidence: `party_position` cue `claim` at chunk `4238652` offsets `381-386`; context: As Justice McDonald stated recently in Ogaulu v Canada (Citizenship and Immigration), 2019 FC 547 [Ogaulu], this Court “has confirmed on numerous occasions that all the important facts and details of a claim must be included, and failing to do so can affect the credibility of all or part of a claimant’s testimony” (at para 18).
- Evidence: `evidence_fact` cue `testimony` at chunk `4238652` offsets `484-493`; context: As Justice McDonald stated recently in Ogaulu v Canada (Citizenship and Immigration), 2019 FC 547 [Ogaulu], this Court “has confirmed on numerous occasions that all the important facts and details of a claim must be included, and failing to do so can affect the credibility of all or part of a claimant’s testimony” (at para 18).
- Evidence: `party_position` cue `claimed` at chunk `4238653` offsets `536-543`; context: Kanawati stated in his BOC that he worked as a plumber and that his job “exposes him to many people,” he failed to mention that he often worked for high placed civilian and military officials in Lebanon and that this was why Bilal was specifically trying to recruit him as a spy (as he claimed at the hearing).
- Evidence: `evidence_fact` cue `testimony` at chunk `4238653` offsets `822-831`; context: Kanawati had “added this detail at his hearing to bolster his testimony.
- Evidence: `disposition` cue `upheld` at chunk `4238653` offsets `34-40`; context: [19] In the present case, the RAD upheld the RPD’s determination that Mr.
- Evidence: `reasoning_application` cue `conclude` at chunk `4238654` offsets `51-59`; context: [20] It was not unreasonable for the RAD member to conclude that the RPD’s findings regarding the omissions from the BOC “were well-founded and central to the key allegations of the Appellants’ risk of persecution.

#### 4090:1:subtheme:5 · paragraphs 22-26

- Raw key terms: `applicants, consider, agree, alleged, appeal, canada, citizenship, errors`
- Display key terms: `consider, agree, alleged, errors`
- Argument roles: `disposition, governing_rule, issue, party_position`
- Explanation: Observed roles: disposition, governing_rule, issue, party_position Display terms: consider, agree, alleged, errors Position/evidence statements: [22] The applicants do, however, contend that it was unreasonable for the RAD not to consider the potentially corroborative documents and whether the RPD had erred in that respect. Rule/authority context: [26] The parties did not suggest any serious questions of general importance for certification under section 74(d) of the IRPA. Operative outcome context: [25] For these reasons, the application for judicial review will be dismissed. Evidence spans paragraphs 22-26. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4238656` offsets `138-145`; context: [22] The applicants do, however, contend that it was unreasonable for the RAD not to consider the potentially corroborative documents and whether the RPD had erred in that respect.
- Evidence: `party_position` cue `contend` at chunk `4238656` offsets `33-40`; context: [22] The applicants do, however, contend that it was unreasonable for the RAD not to consider the potentially corroborative documents and whether the RPD had erred in that respect.
- Evidence: `disposition` cue `dismissed` at chunk `4238659` offsets `68-77`; context: [25] For these reasons, the application for judicial review will be dismissed.
- Evidence: `governing_rule` cue `under` at chunk `4238660` offsets `95-100`; context: [26] The parties did not suggest any serious questions of general importance for certification under section 74(d) of the IRPA.

#### Section text

Kanawati v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2020-01-03
Neutral citation
2020 FC 12
File numbers
IMM-6486-18
Notes
A correction was made on January 21, 2020.
Decision Content
Date: 20200103
Docket: IMM-6486-18
Citation: 2020 FC 12
Ottawa, Ontario, January 3, 2020
PRESENT: Mr. Justice Norris
BETWEEN:
YOUSSEF SOULTANI KANAWATI
MAYSAA SAAD
MALAKE SULTANI KANAWATI
YAACOUB SOULTANI KANAWATI
ROLA SULTANI KANAWATI
Applicants
and
THE MINISTER OF CITIZENSHIP AND IMMIGRATION
Respondent
JUDGMENT AND REASONS

[1] The applicants are citizens of Lebanon. They sought refugee protection in Canada on the basis of their fear of persecution by members the Saraya Resistance, a faction of Hezbollah that is active in Lebanon.

[2] The principal applicant, Youssef Soultani Kanawati, claims that in April 2016 he was approached by Bilal Akar, a well-known member of the group, who encouraged him to join the group. Mr. Kanawati declined. Bilal said he would give him some time to reconsider. A few weeks later, Bilal and his friends approached Mr. Kanawati’s wife on the street and harassed her. When Mr. Kanawati confronted them, Bilal and his friends assaulted him and his wife. Bilal took out a pocket knife and threatened to break Mr. Kanawati’s legs if he reported him to the police. Mr. Kanawati filed a complaint with the police despite the threat. Bilal and his friends approached Mr. Kanawati yet again a few weeks later and, once again, threatened him and his family if he did not join the Saraya Resistance. They also assaulted him again. Mr. Kanawati was taken to the hospital and he reported the incident to the police. He claims that the police also fear the Saraya Resistance and, as a result, they refused to prosecute his assailants. Fearing continued persecution by this group, Mr. Kanawati, his wife and their minor children left Lebanon for Canada. They entered Canada at Pearson International Airport on August 17, 2016, on visitor visas.

[3] The applicants submitted an inland claim for refugee protection on October 21, 2016. Their claim was prepared with the assistance of a lawyer (Mr. Kaminker) and an Arabic interpreter.

[4] The applicants’ hearing before the Refugee Protection Division [RPD] of the Immigration and Refugee Board of Canada [IRB] took place on December 6, 2017. The applicants were represented by Mr. Kaminker at that hearing.

[5] For reasons dated December 19, 2017, the RPD rejected the claims. The member made negative credibility findings against the applicants on the basis of material differences between the original narrative provided by Mr. Kanawati in support of the claim and his testimony at the hearing. In short: “The testimony regarding Bilal and his actions against the claimants is not credible.” The RPD member acknowledged that the applicants had provided a copy of a police report to corroborate their allegations. However, since the report relied entirely on information provided by Mr. Kanawati, the member gave it no weight because Mr. Kanawati had been found not to be credible with respect to key aspects of his allegations.

[6] Representing themselves, the applicants appealed this decision to the Refugee Appeal Division [RAD] of the IRB. In a decision dated November 28, 2018, the RAD dismissed the appeal and confirmed the RPD’s determination that the applicants are neither Convention refugees nor persons in need of protection.

[7] The applicants then retained Mr. Kaminker again and brought this application for judicial review of the RAD’s decision under section 72(1) of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA].

[8] For the reasons that follow, the application will be dismissed.

[9] It is well-established that the substance of the RAD’s decision is reviewed on a reasonableness standard (Canada (Citizenship and Immigration) v Huruglica, 2016 FCA 93 at para 35). That this is the appropriate standard is reinforced by Canada (Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov], where the majority of the Court set out a revised framework for determining the standard of review with respect to the merits of an administrative decision (at para 10). Applying Vavilov, there is no basis for derogating from the presumption that reasonableness is the applicable standard of review of the RAD’s decision.

[10] The majority in Vavilov also sought to clarify the proper application of the reasonableness standard (at para 143). The principles the majority emphasizes were drawn in large measure from prior jurisprudence, including Dunsmuir v New Brunswick, [2008] 1 S.C.R. 190, 2008 SCC 9. Even though the present application was argued prior to the release of Vavilov, the footing upon which the parties advanced their respective positions concerning the reasonableness of the RAD’s decision is consistent with these principles.

[11] As discussed in Vavilov, the exercise of public power “must be justified, intelligible and transparent, not in the abstract but to the individuals subject to it” (Vavilov at para 95). For this reason, an administrative decision maker has a responsibility “to justify to the affected party, in a manner that is transparent and intelligible, the basis on which it arrived at a particular conclusion” (Vavilov at para 96). A reasonable decision “is one that is based on an internally coherent and rational chain of analysis and that is justified in relation to the facts and law that constrain the decision maker” (Vavilov at para 85). The onus is on the applicants to demonstrate that the RAD’s decision is unreasonable. Before a decision can be set aside on this basis, the reviewing court must be satisfied that “there are sufficiently serious shortcomings in the decision such that it cannot be said to exhibit the requisite degree of justification, intelligibility and transparency” (Vavilov at para 100).

[12] The applicants contend that it was unreasonable for the RAD to uphold the RPD’s negative credibility findings and to fail to consider the potentially corroborative documents (i.e. police and medical reports). I do not agree in either respect.

[13] As the majority emphasized in Vavilov, a reviewing court must “read the decision maker’s reasons in light of the history and context of the proceedings in which they were rendered” (at para 94). In the present case, a crucial part of the context of the RAD’s decision is how the applicants framed their appeal.

[14] In a letter from Mr. Kanawati to the RAD dated February 22, 2018, in effect the applicants raised three related errors by the RPD: first, the differences between the original narrative and the testimony before the RPD were not material; second, Mr. Kanawati stated that he was under a lot of stress and very nervous when he provided the information for the original narrative; and third, he was “perhaps, wrongly advised, to be as brief & to the point in my application as possible.” While not exactly a ground of appeal, Mr. Kanawati also claimed in his letter that the tactics of the Saraya Resistance, including the use of spies, are well known.

[15] The errors alleged by the applicants were reiterated in substance and without further elaboration in the Applicants’ Memorandum to the RAD prepared pursuant to the requirements of Rule 3(3)(g) of the Refugee Appeal Division Rules, SOR/2012-257.

[16] The RAD member rejected these grounds of appeal. The member confirmed that she had reviewed the record in its entirety. She found the omissions in Mr. Kanawati’s narrative were central to the claim and warranted the negative credibility findings, especially considering that the applicants had had the assistance of able and experienced counsel when preparing the Basis of Claim [BOC]. The member also noted that Mr. Kanawati did not raise the issue of stress or anxiety at the RPD hearing and provided no medical evidence of an impairment that would have prevented him from completing his BOC properly. She noted that it was insufficient simply to claim that “everyone knows” that the Saraya Resistance relies on a network of spies.

[17] Further, the member noted that the applicants had failed to identify clearly who allegedly gave them incorrect advice in the preparation of their BOC. As well, “[w]hether it was the translator or legal counsel, no notice was provided in either case to allow them to respond to the allegations of professional incompetence.” The member therefore concluded that “there is insufficient evidence to support the Appellants’ speculation that ‘perhaps’ they were given wrong advice.”

[18] The applicants have failed to demonstrate that these determinations are unreasonable. The importance of providing a complete account in a BOC has been emphasized many times. As Justice McDonald stated recently in Ogaulu v Canada (Citizenship and Immigration), 2019 FC 547 [Ogaulu], this Court “has confirmed on numerous occasions that all the important facts and details of a claim must be included, and failing to do so can affect the credibility of all or part of a claimant’s testimony” (at para 18). When a BOC omits significant or material details, such omissions can form a reasonable basis for doubting a claimant’s credibility (Ogaulu at para 20; Jele v Canada (Immigration, Refugees and Citizenship), 2017 FC 24 at para 50).

[19] In the present case, the RAD upheld the RPD’s determination that Mr. Kanawati had omitted material information from his BOC and that this had an adverse impact on his credibility. This conclusion is altogether reasonable. For example, while Mr. Kanawati stated in his BOC that he worked as a plumber and that his job “exposes him to many people,” he failed to mention that he often worked for high placed civilian and military officials in Lebanon and that this was why Bilal was specifically trying to recruit him as a spy (as he claimed at the hearing). The RPD member stated: “[i]f it were true that it [being a plumber] exposed him to government officials, it is reasonable to expect this would have been mentioned.” The RPD member concluded that Mr. Kanawati had “added this detail at his hearing to bolster his testimony.”

[20] It was not unreasonable for the RAD member to conclude that the RPD’s findings regarding the omissions from the BOC “were well-founded and central to the key allegations of the Appellants’ risk of persecution.” There is no basis for me to interfere.

[21] Understandably, the applicants do not challenge the RAD’s determination with respect to their allegation that they were ill-advised in the preparation of their BOC.

[22] The applicants do, however, contend that it was unreasonable for the RAD not to consider the potentially corroborative documents and whether the RPD had erred in that respect. I do not agree.

[23] Once again, the RAD’s decision must be assessed in the context of how the applicants framed their appeal. The applicants did not raise any alleged error in relation to the RPD’s assessment of the police or medical reports. It is well-established that the RAD is not required to consider potential errors that an appellant did not raise: see Dhillon v Canada (Citizenship and Immigration), 2015 FC 321 at paras 18-20; Ilias v Canada (Citizenship and Immigration), 2018 FC 661 at para 39; Broni v Canada (Citizenship and Immigration), 2019 FC 365 at para 15; and Canada (Citizenship and Immigration) v Chamanpreet Kaur Kaler, 2019 FC 883 at paras 11-13 (IMM-57-19).

[24] The RAD member was required to address the specific errors alleged by the applicants (Dahal v Canada (Citizenship and Immigration), 2017 FC 1102 at para 30). This is exactly what she did. She was not required to go beyond the applicants’ grounds of appeal and consider other potential errors. As a result, it was not unreasonable for her to dispose of the appeal as she did.

[25] For these reasons, the application for judicial review will be dismissed.

[26] The parties did not suggest any serious questions of general importance for certification under section 74(d) of the IRPA. I agree that none arise.


## 4090:2 · paragraphs 27-28

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `45038bfa19cea22b6234f7e2a43269fc44021bd42e003a1e37c139339916351b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4090:2:subtheme:1 · paragraphs 27-28

- Raw key terms: `imm-6486-18, application, cause, citizenship, court, date, dismissed, docket`
- Display key terms: `imm-6486-18, date, dismissed`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-6486-18, date, dismissed Operative outcome context: JUDGMENT IN IMM-6486-18 THIS COURT’S JUDGMENT is that The application for judicial review is dismissed. Evidence spans paragraphs 27-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4238660` offsets `260-268`; context: No question of general importance is stated.
- Evidence: `disposition` cue `dismissed` at chunk `4238660` offsets `246-255`; context: JUDGMENT IN IMM-6486-18
THIS COURT’S JUDGMENT is that
The application for judicial review is dismissed.

#### Section text

JUDGMENT IN IMM-6486-18
THIS COURT’S JUDGMENT is that
The application for judicial review is dismissed.
No question of general importance is stated.
“John Norris”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-6486-18
STYLE OF CAUSE:
YOUSSEF SOULTANI KANAWATI ET AL v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
JULY 18, 2019


## 4090:3 · paragraphs 29-29

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `191ad0eb4077970a6ed2264680a3f4d6a83e894b4d7329deffa48bfc48cc5147`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4090:3:subtheme:1 · paragraphs 29-29

- Raw key terms: `appearances, applicants, associates, attorney, barristers, canada, christodoulides, dated`
- Display key terms: `associates, barristers, christodoulides, dated`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: associates, barristers, christodoulides, dated No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 29-29. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
NORRIS J.
DATED:
January 3, 2020
APPEARANCES:
Hart A. Kaminker
For The Applicants
Laoura Christodoulides
For The Respondent
SOLICITORS OF RECORD:
Kaminker and Associates
Barristers and Solicitors
Toronto, Ontario
For The Applicants
Attorney General of Canada
Toronto, Ontario
For The Respondent
