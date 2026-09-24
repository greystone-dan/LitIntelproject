# Discussion Units: case 4458

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **68**
- Continuity pairs: **67**
- Discussion Units: **6**
- Paragraph source hashes: **68**
- Sub-themes: **19**

## 4458:1 · paragraphs 0-11

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `d112e6f42213d1e61ea3ee52720fb5fb415f229743e5508c5ca7fc1163f1ecf9`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4458:1:subtheme:1 · paragraphs 0-4

- Raw key terms: `applicant, applicants, principal, blessing, feboke, decision, nigeria, present`
- Display key terms: `principal, blessing, feboke, nigeria, present`
- Argument roles: `evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, party_position, reasoning_application Display terms: principal, blessing, feboke, nigeria, present Position/evidence statements: The Applicants claim they started to receive threatening phone calls following the arrests. Application context: The RAD found that Ibadan is a suitable IFA because a relocation to Ibadan would not expose the Applicants to a serious risk of persecution or provoke serious psychological harm to the Principal Applicant, Blessing Febok Evidence spans paragraphs 0-4. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `4252262` offsets `433-443`; context: The RAD found that Ibadan is a suitable IFA because a relocation to Ibadan would not expose the Applicants to a serious risk of persecution or provoke serious psychological harm to the Principal Applicant, Blessing Feboke.
- Evidence: `reasoning_application` cue `because` at chunk `4252262` offsets `469-476`; context: The RAD found that Ibadan is a suitable IFA because a relocation to Ibadan would not expose the Applicants to a serious risk of persecution or provoke serious psychological harm to the Principal Applicant, Blessing Feboke.
- Evidence: `party_position` cue `claim` at chunk `4252265` offsets `97-102`; context: The Applicants claim they started to receive threatening phone calls following the arrests.

#### 4458:1:subtheme:2 · paragraphs 5-6

- Raw key terms: `applicants, lagos, affidavit, applicant, arrived, based, because, came`
- Display key terms: `lagos, affidavit, arrived, based, because, came`
- Argument roles: `evidence_fact, reasoning_application`
- Explanation: Observed roles: evidence_fact, reasoning_application Display terms: lagos, affidavit, arrived, based, because, came Application context: In her narrative, the Principal Applicant indicated that her family is not safe in Nigeria because of the threat posed by the NDA. Evidence spans paragraphs 5-6. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `because` at chunk `4252266` offsets `375-382`; context: In her narrative, the Principal Applicant indicated that her family is not safe in Nigeria because of the threat posed by the NDA.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4252267` offsets `65-74`; context: [6] In December 2016, one of the Applicants’ friends provided an affidavit indicating that certain members of the NDA came to his home in Lagos searching for the Applicants.

#### 4458:1:subtheme:3 · paragraphs 7-8

- Raw key terms: `abuja, applicants, because, credibility, decision, findings, ibadan, issue`
- Display key terms: `abuja, because, credibility, findings, ibadan`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: abuja, because, credibility, findings, ibadan Position/evidence statements: In the submissions, the Applicants argued that the NDA have the capacity to track them to the proposed IFAs, and that the Principal Applicant does not have a reasonable IFA in the proposed locations because of a lack of  Rule/authority context: Decision under Review Application context: ” In Feboke v Canada (Immigration, Refugees and Citizenship), 2017 FC 855, this Court held that the RPD’s decision was unreasonable because it was “devoted to reaching strongly contested findings of general negative cred | In the submissions, the Applicants argued that the NDA have the capacity to track them to the proposed IFAs, and that the Principal Applicant does not have a reasonable IFA in the proposed locations because of a lack of  Evidence spans paragraphs 7-8. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4252268` offsets `685-690`; context: While the issue of an IFA in Lagos, Ibadan, and Abuja was raised by the RPD, the claim was ultimately refused for credibility reasons.
- Evidence: `reasoning_application` cue `because` at chunk `4252268` offsets `358-365`; context: ” In Feboke v Canada (Immigration, Refugees and Citizenship), 2017 FC 855, this Court held that the RPD’s decision was unreasonable because it was “devoted to reaching strongly contested findings of general negative credibility on evidentiary features ancillary to the substance of the claim” (at para 3).
- Evidence: `issue` cue `issue` at chunk `4252269` offsets `332-337`; context: In a letter dated February 1, 2019, the RAD directed the Applicants to make submissions regarding the IFA locations of Lagos, Ibadan, and Abuja, as the RPD did not make a determination on this issue.
- Evidence: `party_position` cue `argued` at chunk `4252269` offsets `437-443`; context: In the submissions, the Applicants argued that the NDA have the capacity to track them to the proposed IFAs, and that the Principal Applicant does not have a reasonable IFA in the proposed locations because of a lack of adequate mental health services in the proposed locations.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252269` offsets `360-368`; context: The Applicants filed evidence and submissions two weeks later.
- Evidence: `governing_rule` cue `under` at chunk `4252269` offsets `872-877`; context: Decision under Review
- Evidence: `reasoning_application` cue `because` at chunk `4252269` offsets `601-608`; context: In the submissions, the Applicants argued that the NDA have the capacity to track them to the proposed IFAs, and that the Principal Applicant does not have a reasonable IFA in the proposed locations because of a lack of adequate mental health services in the proposed locations.

#### 4458:1:subtheme:4 · paragraphs 9-11

- Raw key terms: `applicants, evidence, ibadan, part, risk, accept, acknowledged, activities`
- Display key terms: `ibadan, part, risk, accept, acknowledged, activities`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: ibadan, part, risk, accept, acknowledged, activities Rule/authority context: The RAD acknowledged that the RPD’s credibility analysis was “microscopic and misstated some of the evidence”, but made no credibility finding of its own; the RAD also did not address the Applicants’ exposure to risk und Application context: [10] On the first prong of the IFA test, the RAD found that the NDA would not present a risk in Ibadan because their activities “do not extend to Oyo state, where Ibadan is” and because there was little evidence the NDA  Operative outcome context: The request was granted by Madam Justice Kane. Evidence spans paragraphs 9-11. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4252270` offsets `684-689`; context: Consequently, the only determinative issue dealt with by the RAD was whether Ibadan constituted a viable IFA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252270` offsets `170-178`; context: The RAD acknowledged that the RPD’s credibility analysis was “microscopic and misstated some of the evidence”, but made no credibility finding of its own; the RAD also did not address the Applicants’ exposure to risk under sections 96 or 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], independently of its finding of a viable IFA.
- Evidence: `governing_rule` cue `under` at chunk `4252270` offsets `287-292`; context: The RAD acknowledged that the RPD’s credibility analysis was “microscopic and misstated some of the evidence”, but made no credibility finding of its own; the RAD also did not address the Applicants’ exposure to risk under sections 96 or 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], independently of its finding of a viable IFA.
- Evidence: `counterargument_limitation` cue `but` at chunk `4252270` offsets `181-184`; context: The RAD acknowledged that the RPD’s credibility analysis was “microscopic and misstated some of the evidence”, but made no credibility finding of its own; the RAD also did not address the Applicants’ exposure to risk under sections 96 or 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], independently of its finding of a viable IFA.
- Evidence: `evidence_fact` cue `found that` at chunk `4252271` offsets `49-59`; context: [10] On the first prong of the IFA test, the RAD found that the NDA would not present a risk in Ibadan because their activities “do not extend to Oyo state, where Ibadan is” and because there was little evidence the NDA was motivated to search for the Applicants outside of the Delta region.
- Evidence: `reasoning_application` cue `because` at chunk `4252271` offsets `103-110`; context: [10] On the first prong of the IFA test, the RAD found that the NDA would not present a risk in Ibadan because their activities “do not extend to Oyo state, where Ibadan is” and because there was little evidence the NDA was motivated to search for the Applicants outside of the Delta region.
- Evidence: `disposition` cue `granted` at chunk `4252272` offsets `180-187`; context: The request was granted by Madam Justice Kane.

#### Section text

Feboke v. Canada (Citizenship and Immigration)
Court (s) Database
Federal Court Decisions
Date
2020-01-28
Neutral citation
2020 FC 155
File numbers
IMM-2401-19
Decision Content
Date: 20200128
Docket: IMM-2401-19
Citation: 2020 FC 155
Ottawa, Ontario, January 28, 2020
PRESENT: The Honourable Mr. Justice Pamel
BETWEEN:
BLESSING FEBOKE
PREYE FEBOKE
DAVID DOUBRA FEBOKE
PEREZIDE FEBOKE
CHRISTABEL EDIERE FEBOKE
FAITH TAMARAKHURO FEBOKE
Applicants
and
THE MINISTER OF IMMIGRATION, REFUGEES AND CITIZENSHIP
Respondent
JUDGMENT AND REASONS
I. Nature of the Matter

[1] This case concerns a decision by the Refugee Appeal Division [RAD] finding that the Applicants have an Internal Flight Alternative [IFA] in Nigeria. The Applicants are Nigerian refugee claimants who fear persecution from the Niger Delta Avengers [NDA]. The NDA is a participant in the ongoing conflict in the Niger Delta resulting from tensions between oil corporations and a number of the area’s minority ethnic groups. The RAD found that Ibadan is a suitable IFA because a relocation to Ibadan would not expose the Applicants to a serious risk of persecution or provoke serious psychological harm to the Principal Applicant, Blessing Feboke. The Applicants challenge both of these determinations. For the reasons that follow, I would dismiss the present application.
II. Facts

[2] The Applicants are a family of six from Nigeria: Blessing Feboke [Principal Applicant], her husband Preye Feboke, and their four children. The Principal Applicant owns and operates a catering company. Her husband was previously employed by the Shell Petroleum Development Company of Nigeria.

[3] On July 13, 2016, the Principal Applicant catered an event where she overheard three men discussing blowing up an oil pipeline in the Akwa Ibom State and carrying out another planned attack in early August 2016. The Principal Applicant approached the men and attempted to dissuade them from carrying out the plan. The men rebuked and threatened her to keep her quiet. The men paid her for her silence.

[4] Later, certain members of the NDA were arrested for attacks on oil pipelines. The Applicants claim they started to receive threatening phone calls following the arrests. It would seem as though the NDA blamed the Principal Applicant for having exposed them to the police.

[5] Based on these threats, the Applicants fled to a cousin’s house in the Delta state, and then to a friend’s house in Lagos (in the Lagos state). The Applicants eventually left Nigeria on September 11, 2016. The Applicants arrived in Canada and filed claims for refugee protection. In her narrative, the Principal Applicant indicated that her family is not safe in Nigeria because of the threat posed by the NDA.

[6] In December 2016, one of the Applicants’ friends provided an affidavit indicating that certain members of the NDA came to his home in Lagos searching for the Applicants.

[7] The Refugee Protection Division [RPD] has twice refused the Applicants’ refugee claim. The first time, the RPD rejected their claim in its decision of January 23, 2017 on a finding that the claim was “manifestly unfounded.” In Feboke v Canada (Immigration, Refugees and Citizenship), 2017 FC 855, this Court held that the RPD’s decision was unreasonable because it was “devoted to reaching strongly contested findings of general negative credibility on evidentiary features ancillary to the substance of the claim” (at para 3). The refugee claim was returned to the RPD for redetermination. The refugee claim was refused a second time by the RPD for credibility reasons. While the issue of an IFA in Lagos, Ibadan, and Abuja was raised by the RPD, the claim was ultimately refused for credibility reasons.

[8] On July 6, 2018, the Applicants appealed the decision to the RAD. On appeal, the Applicants challenged the RPD’s credibility findings. In a letter dated February 1, 2019, the RAD directed the Applicants to make submissions regarding the IFA locations of Lagos, Ibadan, and Abuja, as the RPD did not make a determination on this issue. The Applicants filed evidence and submissions two weeks later. In the submissions, the Applicants argued that the NDA have the capacity to track them to the proposed IFAs, and that the Principal Applicant does not have a reasonable IFA in the proposed locations because of a lack of adequate mental health services in the proposed locations. On account of her subjective fear of returning to any area in Nigeria where she may be exposed to the risk of harm, there is no available IFA in Nigeria for her to relocate to.
III. Decision under Review

[9] The RAD refused the Applicants’ refugee claims on March 18, 2019. The RAD acknowledged that the RPD’s credibility analysis was “microscopic and misstated some of the evidence”, but made no credibility finding of its own; the RAD also did not address the Applicants’ exposure to risk under sections 96 or 97 of the Immigration and Refugee Protection Act, SC 2001, c 27 [IRPA], independently of its finding of a viable IFA. In any event, I accept that the determination of an IFA is part and parcel of the process of consideration under sections 96 and 97 of the IRPA (Amadi v Canada (Citizenship and Immigration), 2019 FC 1166 at paras 41-42). Consequently, the only determinative issue dealt with by the RAD was whether Ibadan constituted a viable IFA.

[10] On the first prong of the IFA test, the RAD found that the NDA would not present a risk in Ibadan because their activities “do not extend to Oyo state, where Ibadan is” and because there was little evidence the NDA was motivated to search for the Applicants outside of the Delta region. On the second prong of the IFA test, the RAD found that it was not unreasonable to expect the Applicants to relocate to Ibadan, in part because the Principal Applicant’s mental health concerns could be addressed in Ibadan.
IV. Procedural History

[11] The Applicants requested an extension of time for the filing of the application for leave and for judicial review. The Respondent did not oppose this request. The request was granted by Madam Justice Kane.


## 4458:2 · paragraphs 12-13

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e56364652d3ce6566bad1710b59317dd188ff85e17fc713bc04a9f1bb4024a1c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4458:2:subtheme:1 · paragraphs 12-13

- Raw key terms: `case, decision, issue, issues, reasonable, sole, whether`
- Display key terms: `case, issues, reasonable, sole, whether`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: case, issues, reasonable, sole, whether Evidence spans paragraphs 12-13. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4252273` offsets `14-19`; context: [12] The sole issue in the case at bar is whether the RAD decision was reasonable.

#### Section text

V. Issues

[12] The sole issue in the case at bar is whether the RAD decision was reasonable.


## 4458:3 · paragraphs 14-20

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `ab5b84982f20b38c6c481d79c7310c3fd06d128bf3f5f6a910934a8a8696e5f6`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4458:3:subtheme:1 · paragraphs 14-15

- Raw key terms: `review, standard, administrative, agree, analysis, canada, citizenship, consider`
- Display key terms: `review, standard, administrative, agree, analysis, consider`
- Argument roles: `governing_rule, issue`
- Explanation: Observed roles: governing_rule, issue Display terms: review, standard, administrative, agree, analysis, consider Rule/authority context: [13] The parties agree that the standard of review is reasonableness. Evidence spans paragraphs 14-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4252274` offsets `259-266`; context: Under the reasonableness standard of review, “the reviewing court must consider only whether the decision made by the administrative decision maker — including both the rationale for the decision and the outcome to which it led — was unreasonable” (Vavilov at para 83).
- Evidence: `governing_rule` cue `standard of review` at chunk `4252274` offsets `32-50`; context: [13] The parties agree that the standard of review is reasonableness.

#### 4458:3:subtheme:2 · paragraphs 16-19

- Raw key terms: `analysis, applicants, canada, citizenship, committed, errors, finding, first`
- Display key terms: `analysis, committed, errors, finding, first`
- Argument roles: `evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: analysis, committed, errors, finding, first Position/evidence statements: Concerning the first prong, the Applicants submit that the RAD committed two reviewable errors in finding that the NDA lacked the ability or motivation to locate the Principal Applicant in Ibadan. | [17] The Applicants submit that the RAD committed two reviewable errors in its analysis of the risk posed by the NDA, in particular, in its assessment of the evidence. Rule/authority context: [16] The Applicants challenge the RAD’s analysis under both prongs of the IFA test. Application context: [15] The decisions in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706, and Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589, have established a two-prong t Evidence spans paragraphs 16-19. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4252275` offsets `9-17`; context: [14] The question of whether an IFA exists is an essential component of the refugee system.
- Evidence: `issue` cue `whether` at chunk `4252276` offsets `253-260`; context: [15] The decisions in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706, and Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589, have established a two-prong test to be applied in determining whether there is an IFA: (i) there must be no serious possibility of the individual being persecuted in the IFA area (on the balance of probabilities); and (ii) conditions in the proposed IFA must be such that it would not be unreasonable in all the circumstances for an individual to seek refuge there (Reci v Canada (Citizenship and Immigration), 2016 FC 833 at para 19; Titcombe v Canada (Citizenship and Immigration), 2019 FC 1346 at para 15).
- Evidence: `reasoning_application` cue `applied` at chunk `4252276` offsets `230-237`; context: [15] The decisions in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706, and Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589, have established a two-prong test to be applied in determining whether there is an IFA: (i) there must be no serious possibility of the individual being persecuted in the IFA area (on the balance of probabilities); and (ii) conditions in the proposed IFA must be such that it would not be unreasonable in all the circumstances for an individual to seek refuge there (Reci v Canada (Citizenship and Immigration), 2016 FC 833 at para 19; Titcombe v Canada (Citizenship and Immigration), 2019 FC 1346 at para 15).
- Evidence: `party_position` cue `submit` at chunk `4252277` offsets `127-133`; context: Concerning the first prong, the Applicants submit that the RAD committed two reviewable errors in finding that the NDA lacked the ability or motivation to locate the Principal Applicant in Ibadan.
- Evidence: `governing_rule` cue `under` at chunk `4252277` offsets `49-54`; context: [16] The Applicants challenge the RAD’s analysis under both prongs of the IFA test.
- Evidence: `party_position` cue `submit` at chunk `4252278` offsets `20-26`; context: [17] The Applicants submit that the RAD committed two reviewable errors in its analysis of the risk posed by the NDA, in particular, in its assessment of the evidence.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252278` offsets `158-166`; context: [17] The Applicants submit that the RAD committed two reviewable errors in its analysis of the risk posed by the NDA, in particular, in its assessment of the evidence.

#### 4458:3:subtheme:3 · paragraphs 20-20

- Raw key terms: `accepted, alleged, applicants, balance, capacity, delta, error, finding`
- Display key terms: `accepted, alleged, balance, capacity, delta, error, finding`
- Argument roles: `issue`
- Explanation: Observed roles: issue Display terms: accepted, alleged, balance, capacity, delta, error, finding Evidence spans paragraphs 20-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4252279` offsets `180-185`; context: The Applicants take issue with the finding of the RAD that on the balance of probabilities, the NDA does not operate outside the Niger Delta region, when at the same time, the RAD accepted that the NDA went searching for the Applicants in Lagos.

#### Section text

VI. Standard of Review

[13] The parties agree that the standard of review is reasonableness. I agree (Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at para 23 [Vavilov]). Under the reasonableness standard of review, “the reviewing court must consider only whether the decision made by the administrative decision maker — including both the rationale for the decision and the outcome to which it led — was unreasonable” (Vavilov at para 83).
VII. Analysis

[14] The question of whether an IFA exists is an essential component of the refugee system. The IFA concept flows from the definition of convention refugee and helps ensure that international refugee law serves as a back-up to national protection when such protection is inadequate (Dejo Dillon v Canada (Minister of Citizenship and Immigration), 2005 FC 381 at para 8; James C. Hathaway and Michelle Foster, The Law of Refugee Status, 2nd ed (Cambridge: Cambridge University Press, 2014) at 332–333; the UNHCR Guidelines on International Protection: “Internal Flight or Relocation Alternative” within the Context of Article 1A (2) of the 1951 Convention and/or 1967 Protocol relating to the Status of Refugees, HCR/GIP/03/04, 23 July 2003 at para 6 [UNHCR Guidelines]; Jamie Chai Yun Liew and Donald Galloway, Immigration Law, 2nd ed (Toronto: Irwin Law, 2015) at 341–342). In essence, the IFA concept helps ensure that persecuted individuals first approach their own country before seeking protection through the international refugee system (Canada (Attorney General) v Ward, [1993] 2 SCR 689, 1993 CanLII 105 (SCC)).

[15] The decisions in Rasaratnam v Canada (Minister of Employment and Immigration), [1992] 1 FC 706, and Thirunavukkarasu v Canada (Minister of Employment and Immigration), [1994] 1 FC 589, have established a two-prong test to be applied in determining whether there is an IFA: (i) there must be no serious possibility of the individual being persecuted in the IFA area (on the balance of probabilities); and (ii) conditions in the proposed IFA must be such that it would not be unreasonable in all the circumstances for an individual to seek refuge there (Reci v Canada (Citizenship and Immigration), 2016 FC 833 at para 19; Titcombe v Canada (Citizenship and Immigration), 2019 FC 1346 at para 15). Both prongs must be satisfied in order to make a finding that the claimant has an IFA. This two-prong test ensures that Canada complies with international norms regarding IFAs (UNHCR Guidelines at paras 7, 24–30).

[16] The Applicants challenge the RAD’s analysis under both prongs of the IFA test. Concerning the first prong, the Applicants submit that the RAD committed two reviewable errors in finding that the NDA lacked the ability or motivation to locate the Principal Applicant in Ibadan. Regarding the second prong, the Applicants submit that the RAD committed a reviewable error in assessing how the Principal Applicant’s mental health concerns affect the reasonableness of the IFA.
A. First prong of the IFA test: Fear relating to the Niger Delta Avengers

[17] The Applicants submit that the RAD committed two reviewable errors in its analysis of the risk posed by the NDA, in particular, in its assessment of the evidence.

[18] The first alleged error relates to the capacity of the NDA, and the RAD’s finding that the NDA do not generally operate outside of the Niger Delta region. The Applicants take issue with the finding of the RAD that on the balance of probabilities, the NDA does not operate outside the Niger Delta region, when at the same time, the RAD accepted that the NDA went searching for the Applicants in Lagos.

## 4458:4 · paragraphs 21-63

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `4f7c3e5e750016e65f91622e2cdac240ac04a21504cd2750f2572eedb1a6527b`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4458:4:subtheme:1 · paragraphs 21-28

- Raw key terms: `ibadan, region, states, applicants, known, outside, active, argue`
- Display key terms: `ibadan, region, states, known, outside, active, argue`
- Argument roles: `counterargument_limitation, evidence_fact, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, party_position, reasoning_application Display terms: ibadan, region, states, known, outside, active, argue Position/evidence statements: [21] The Applicants contest the finding of the RAD that Ibadan is outside the reach of the NDA and in particular argue that this determination is erroneous because it fails to consider the fact that the Applicants were p | [22] In particular, the Applicants underscore that the RAD accepted that the NDA were searching for the Applicants in Lagos, and argue that the Lagos incident (being outside the enumerated states where the NDA are known  Application context: Accordingly, I do not find, on a balance of probabilities, that the reach and sophistication of the NDA extends to Ibadan, Oyo state. | [21] The Applicants contest the finding of the RAD that Ibadan is outside the reach of the NDA and in particular argue that this determination is erroneous because it fails to consider the fact that the Applicants were p Evidence spans paragraphs 21-28. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252280` offsets `599-607`; context: First, as outlined above, I do not accept the Appellants’ news articles on NDA attacks which pre-dated their refugee hearing as new evidence, and, as such, I am not considering them here.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4252280` offsets `995-1006`; context: Accordingly, I do not find, on a balance of probabilities, that the reach and sophistication of the NDA extends to Ibadan, Oyo state.
- Evidence: `counterargument_limitation` cue `but` at chunk `4252280` offsets `261-264`; context: [19] The RAD stated the following in its decision:
Regarding the reach and sophistication of the NDA, I accept that the NDA is relatively sophisticated in its actions, as the Board’s Response to Information Request […] states that the group is relatively small but that their activities show a high degree of sophistication.
- Evidence: `party_position` cue `argue` at chunk `4252282` offsets `113-118`; context: [21] The Applicants contest the finding of the RAD that Ibadan is outside the reach of the NDA and in particular argue that this determination is erroneous because it fails to consider the fact that the Applicants were pursued by the NDA in an area lying outside of the enumerated states (citing Ikechi v Canada (Citizenship and Immigration), 2013 FC 361 [Ikechi] and Zablon v Canada (Citizenship and Immigration), 2013 FC 58 [Zablon]).
- Evidence: `reasoning_application` cue `because` at chunk `4252282` offsets `156-163`; context: [21] The Applicants contest the finding of the RAD that Ibadan is outside the reach of the NDA and in particular argue that this determination is erroneous because it fails to consider the fact that the Applicants were pursued by the NDA in an area lying outside of the enumerated states (citing Ikechi v Canada (Citizenship and Immigration), 2013 FC 361 [Ikechi] and Zablon v Canada (Citizenship and Immigration), 2013 FC 58 [Zablon]).
- Evidence: `counterargument_limitation` cue `fails` at chunk `4252282` offsets `167-172`; context: [21] The Applicants contest the finding of the RAD that Ibadan is outside the reach of the NDA and in particular argue that this determination is erroneous because it fails to consider the fact that the Applicants were pursued by the NDA in an area lying outside of the enumerated states (citing Ikechi v Canada (Citizenship and Immigration), 2013 FC 361 [Ikechi] and Zablon v Canada (Citizenship and Immigration), 2013 FC 58 [Zablon]).
- Evidence: `party_position` cue `argue` at chunk `4252283` offsets `129-134`; context: [22] In particular, the Applicants underscore that the RAD accepted that the NDA were searching for the Applicants in Lagos, and argue that the Lagos incident (being outside the enumerated states where the NDA are known to operate) demonstrates that the NDA have the capacity to operate outside those regions, including in Ibadan—a possibility that was not contemplated sufficiently by the RAD.
- Evidence: `party_position` cue `submits` at chunk `4252284` offsets `20-27`; context: [23] The Respondent submits that the RAD’s analysis on the first prong of the IFA test was reasonable.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252284` offsets `179-187`; context: The Respondent argues that the Applicants have failed to provide sufficient evidence of the willingness or capacity of the NDA to look for the Applicants outside the Niger Delta region since December 2016.
- Evidence: `party_position` cue `argue` at chunk `4252285` offsets `67-72`; context: [24] The Applicants also provided me with a map of the region, and argue that Ibadan is closer in distance (as the crow flies) than Lagos to the outer perimeter of the area where the NDA operates in the east.
- Evidence: `evidence_fact` cue `record` at chunk `4252285` offsets `279-285`; context: The Applicants argued that although they were not suggesting that the record compelled the RAD to find that the Applicants could be found by the NDA in Ibadan, the RAD could not rely simply upon the distance between Ibadan and the known operating territory of the NDA to find no risk in Ibadan when the RAD also accepted that the Applicants had been sought by the NDA further afield than Ibadan, i.
- Evidence: `counterargument_limitation` cue `although` at chunk `4252285` offsets `236-244`; context: The Applicants argued that although they were not suggesting that the record compelled the RAD to find that the Applicants could be found by the NDA in Ibadan, the RAD could not rely simply upon the distance between Ibadan and the known operating territory of the NDA to find no risk in Ibadan when the RAD also accepted that the Applicants had been sought by the NDA further afield than Ibadan, i.
- Evidence: `counterargument_limitation` cue `cannot` at chunk `4252286` offsets `277-283`; context: In any event, I cannot see how a straight‑line distance comparison alone can play a significant role in the determination of the level of risk posed by an assailant group.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252287` offsets `17-25`; context: [26] There is no evidence to allow one to conclude that the NDA have the motivation, willingness, capacity and resolve, on the balance of probabilities, to be active in Ibadan solely because the straight-line distance between Ibadan and the outer perimeter of the known NDA territory is similar to that of Lagos.
- Evidence: `reasoning_application` cue `conclude` at chunk `4252287` offsets `42-50`; context: [26] There is no evidence to allow one to conclude that the NDA have the motivation, willingness, capacity and resolve, on the balance of probabilities, to be active in Ibadan solely because the straight-line distance between Ibadan and the outer perimeter of the known NDA territory is similar to that of Lagos.

#### 4458:4:subtheme:2 · paragraphs 29-35

- Raw key terms: `applicants, evidence, ibadan, ikechi, risk, applicant, case, determination`
- Display key terms: `ibadan, ikechi, risk, case, determination`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: ibadan, ikechi, risk, case, determination Position/evidence statements: Here, the RAD considered the Applicants’ submitted evidence (i. Application context: [27] In Ikechi, the Pre-Removal Risk Assessment [PRRA] officer dismissed new evidence that the applicant’s sister had been kidnapped because the kidnapping did not occur in the specified IFA location. | , the friend’s affidavits from December 2016, and older news articles) and concluded that it was insufficient because it failed to establish a continued risk of persecution in Ibadan. Operative outcome context: [27] In Ikechi, the Pre-Removal Risk Assessment [PRRA] officer dismissed new evidence that the applicant’s sister had been kidnapped because the kidnapping did not occur in the specified IFA location. Evidence spans paragraphs 29-35. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4252288` offsets `524-531`; context: In the same case, Justice Shore specifically noted that further analysis was required to determine whether the IFA remains viable:
- Evidence: `evidence_fact` cue `evidence` at chunk `4252288` offsets `77-85`; context: [27] In Ikechi, the Pre-Removal Risk Assessment [PRRA] officer dismissed new evidence that the applicant’s sister had been kidnapped because the kidnapping did not occur in the specified IFA location.
- Evidence: `reasoning_application` cue `because` at chunk `4252288` offsets `133-140`; context: [27] In Ikechi, the Pre-Removal Risk Assessment [PRRA] officer dismissed new evidence that the applicant’s sister had been kidnapped because the kidnapping did not occur in the specified IFA location.
- Evidence: `disposition` cue `dismissed` at chunk `4252288` offsets `63-72`; context: [27] In Ikechi, the Pre-Removal Risk Assessment [PRRA] officer dismissed new evidence that the applicant’s sister had been kidnapped because the kidnapping did not occur in the specified IFA location.
- Evidence: `evidence_fact` cue `record` at chunk `4252289` offsets `477-483`; context: The record does not contain information that would allow the Court to look to the record to support the PRRA Officer’s finding in this regard (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708 at para 15).
- Evidence: `party_position` cue `submitted` at chunk `4252290` offsets `172-181`; context: Here, the RAD considered the Applicants’ submitted evidence (i.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252290` offsets `74-82`; context: [28] However, in contrast to Ikechi, in this case, the RAD did assess the evidence in respect of the risk associated with the IFA.
- Evidence: `reasoning_application` cue `because` at chunk `4252290` offsets `306-313`; context: , the friend’s affidavits from December 2016, and older news articles) and concluded that it was insufficient because it failed to establish a continued risk of persecution in Ibadan.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252291` offsets `499-507`; context: In fact, there is no evidence to suggest that Ibadan would pose the same risk of association with the Applicants.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252292` offsets `412-420`; context: Here, the RAD engaged with the evidence and simply found that Ibadan was a viable IFA.
- Evidence: `evidence_fact` cue `determined that` at chunk `4252293` offsets `219-234`; context: [31] The Applicants also cite Zablon in support of the proposition that where the extent of an assailant group’s reach beyond its otherwise known territory is not well documented, it is unreasonable for the RAD to have determined that the first prong of the test for an IFA has been met.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252294` offsets `237-245`; context: Although there was some discrepancy in the documentation in this case as to the reach of the NDA throughout the southern part of Nigeria, even on the most favourable reading of the evidence, there was nothing to suggest that the activities of the NDA extended into Ibadan.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4252294` offsets `469-480`; context: Accordingly, this is not a case of the RAD ignoring the evidence on record and making a determination that cannot be justified on the facts of the case (Zablon at para 22).

#### 4458:4:subtheme:3 · paragraphs 36-39

- Raw key terms: `applicants, evidence, lagos, look, search, suggest, active, although`
- Display key terms: `lagos, look, search, suggest, active, although`
- Argument roles: `counterargument_limitation, evidence_fact, issue, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, reasoning_application Display terms: lagos, look, search, suggest, active, although Application context: [33] The NDA proceeded to Lagos not because they normally operate there, but because they knew that a person with whom the Applicants stayed after fleeing their village and before travelling to the U. | Accordingly, the RAD did not consider there to be any reasonable evidence to suggest the NDA would look for the Applicants in Ibadan today, hence the finding that there is no risk to them there. Evidence spans paragraphs 36-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4252295` offsets `414-421`; context: Although this may suggest that the NDA may have some capacity to search for individuals in areas where they are not normally active, the NDA would have to know where to look, regardless of whether they were still motivated to do so.
- Evidence: `reasoning_application` cue `because` at chunk `4252295` offsets `36-43`; context: [33] The NDA proceeded to Lagos not because they normally operate there, but because they knew that a person with whom the Applicants stayed after fleeing their village and before travelling to the U.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252296` offsets `259-267`; context: Although the RAD accepted that the NDA may have had the capacity to search for the Applicants in Lagos (even though they may not have been operationally active in that area), there was no evidence that such concerns continued to exist even in Lagos.
- Evidence: `counterargument_limitation` cue `Although` at chunk `4252296` offsets `71-79`; context: Although the RAD accepted that the NDA may have had the capacity to search for the Applicants in Lagos (even though they may not have been operationally active in that area), there was no evidence that such concerns continued to exist even in Lagos.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252297` offsets `68-76`; context: [35] From what I can tell in reading the RAD decision, there was no evidence to suggest that the NDA would know to look for the Applicants in Ibadan, or that they would do so today.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252298` offsets `260-268`; context: Other than an expressed concern that if the NDA can reach Lagos to search for the Applicants, they may be able to reach Ibadan, there was no evidence presented by the Applicants to establish that Ibadan posed a risk to them.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4252298` offsets `344-355`; context: Accordingly, the RAD did not consider there to be any reasonable evidence to suggest the NDA would look for the Applicants in Ibadan today, hence the finding that there is no risk to them there.

#### 4458:4:subtheme:4 · paragraphs 40-43

- Raw key terms: `evidence, affidavit, applicants, december, delta, finding, ibadan, outside`
- Display key terms: `affidavit, december, delta, finding, ibadan, outside`
- Argument roles: `counterargument_limitation, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, issue, party_position, reasoning_application Display terms: affidavit, december, delta, finding, ibadan, outside Position/evidence statements: [40] The Applicants argue that the RAD’s finding of no ongoing risk in Ibadan is based upon the lack of affidavit evidence of NDA searches outside the Niger Delta region beyond December 2016. Application context: Based upon this, I find that, while the NDA may have some interest in continuing to search for the Appellants in the Delta region, they have not expressed any willingness or capacity to look for the Appellants outside th Evidence spans paragraphs 40-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4252299` offsets `162-169`; context: [37] This is not a situation, as was the case in Ikechi, where an analysis of evidence was not undertaken, but should have been undertaken, in order to determine whether an alternative IFA existed.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252299` offsets `78-86`; context: [37] This is not a situation, as was the case in Ikechi, where an analysis of evidence was not undertaken, but should have been undertaken, in order to determine whether an alternative IFA existed.
- Evidence: `counterargument_limitation` cue `but` at chunk `4252299` offsets `107-110`; context: [37] This is not a situation, as was the case in Ikechi, where an analysis of evidence was not undertaken, but should have been undertaken, in order to determine whether an alternative IFA existed.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4252300` offsets `114-123`; context: [38] The second alleged error relates to the motivation of the NDA, and the RAD’s finding that although there was affidavit evidence of the NDA searching for the Applicants five times and as late as March 2017 within the Niger Delta region, there is no evidence that the NDA have looked for the Applicants outside of the Niger Delta region (in particular in Lagos) since December 2016.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4252301` offsets `28-37`; context: [39] After finding that the affidavit evidence submitted by the Applicants did not establish a section 96 or 97 risk for the Applicants in Ibadan, the RAD noted the following:
[…] this evidence does not speak to the current situation for the Appellants even in Lagos.
- Evidence: `reasoning_application` cue `I find` at chunk `4252301` offsets `717-723`; context: Based upon this, I find that, while the NDA may have some interest in continuing to search for the Appellants in the Delta region, they have not expressed any willingness or capacity to look for the Appellants outside this region since December 2016.
- Evidence: `party_position` cue `argue` at chunk `4252302` offsets `20-25`; context: [40] The Applicants argue that the RAD’s finding of no ongoing risk in Ibadan is based upon the lack of affidavit evidence of NDA searches outside the Niger Delta region beyond December 2016.
- Evidence: `evidence_fact` cue `affidavit` at chunk `4252302` offsets `104-113`; context: [40] The Applicants argue that the RAD’s finding of no ongoing risk in Ibadan is based upon the lack of affidavit evidence of NDA searches outside the Niger Delta region beyond December 2016.

#### 4458:4:subtheme:5 · paragraphs 44-45

- Raw key terms: `applicants, proposed, according, actual, argue, attempts, burden, continued`
- Display key terms: `proposed, according, actual, argue, attempts, burden, continued`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: proposed, according, actual, argue, attempts, burden, continued Position/evidence statements: [42] The Applicants further argue that the RAD is effectively imposing a high burden of proof on them to demonstrate the persecutors’ continued interest in them, while they have not lived in the proposed IFA. Evidence spans paragraphs 44-45. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `4252303` offsets `210-217`; context: According to the Applicants, the timing of the actual attempts made by the NDA to search for the Applicants is irrelevant; what is relevant is whether the NDA have the proper means and motivation to locate the Applicants in the proposed IFA.
- Evidence: `party_position` cue `argue` at chunk `4252304` offsets `28-33`; context: [42] The Applicants further argue that the RAD is effectively imposing a high burden of proof on them to demonstrate the persecutors’ continued interest in them, while they have not lived in the proposed IFA.

#### 4458:4:subtheme:6 · paragraphs 46-52

- Raw key terms: `applicant, health, mental, applicants, principal, risk, canada, evidence`
- Display key terms: `health, mental, principal, risk`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: health, mental, principal, risk Position/evidence statements: [46] The Applicants submit that the RAD committed a reviewable error in assessing how the Principal Applicant’s mental health concerns affect the reasonableness of the IFA. Rule/authority context: The RAD’s failure to realize that the Principal Applicant will be exposed to this risk is inconsistent with this Court’s jurisprudence (Cartagena v Canada (Citizenship and Immigration), 2008 FC 289 [Cartagena]; Okafor v  Application context: This Court determined that the RPD’s reasoning was unreasonable because it did not address the key issue of the applicant’s claim, namely, the issue of “whether [the agent of persecution] has the probable means and motiv | However, as I have found that the Appellants do not face a risk in Ibadan, I find that the principal Appellant is not being returned to a place where she would be exposed to further threats of harm. Evidence spans paragraphs 46-52. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4252305` offsets `462-467`; context: This Court determined that the RPD’s reasoning was unreasonable because it did not address the key issue of the applicant’s claim, namely, the issue of “whether [the agent of persecution] has the probable means and motivation to [search for the applicant]” (Nimako at para 7).
- Evidence: `evidence_fact` cue `found that` at chunk `4252305` offsets `205-215`; context: In that case, the RPD found that there was no persuasive evidence that the agent of persecution had made any efforts to search for the claimant beyond going to the family’s house.
- Evidence: `reasoning_application` cue `because` at chunk `4252305` offsets `427-434`; context: This Court determined that the RPD’s reasoning was unreasonable because it did not address the key issue of the applicant’s claim, namely, the issue of “whether [the agent of persecution] has the probable means and motivation to [search for the applicant]” (Nimako at para 7).
- Evidence: `counterargument_limitation` cue `However` at chunk `4252305` offsets `129-136`; context: However, Nimako offers little help to the Applicants.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252306` offsets `88-96`; context: First, in Nimako, there was clear evidence of an ongoing desire on the part of the assailant to search for the applicant.
- Evidence: `party_position` cue `submit` at chunk `4252308` offsets `20-26`; context: [46] The Applicants submit that the RAD committed a reviewable error in assessing how the Principal Applicant’s mental health concerns affect the reasonableness of the IFA.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252309` offsets `297-305`; context: I acknowledge that there is evidence on the record which indicates that she suffers from major depressive disorder and PTSD and that her condition could deteriorate if exposed to further threats of harm.
- Evidence: `reasoning_application` cue `I find` at chunk `4252309` offsets `641-647`; context: However, as I have found that the Appellants do not face a risk in Ibadan, I find that the principal Appellant is not being returned to a place where she would be exposed to further threats of harm.
- Evidence: `counterargument_limitation` cue `However` at chunk `4252309` offsets `566-573`; context: However, as I have found that the Appellants do not face a risk in Ibadan, I find that the principal Appellant is not being returned to a place where she would be exposed to further threats of harm.
- Evidence: `governing_rule` cue `jurisprudence` at chunk `4252311` offsets `256-269`; context: The RAD’s failure to realize that the Principal Applicant will be exposed to this risk is inconsistent with this Court’s jurisprudence (Cartagena v Canada (Citizenship and Immigration), 2008 FC 289 [Cartagena]; Okafor v Canada (Citizenship and Immigration), 2011 FC 1002 [Okafor]; Haastrup v Canada (Citizenship and Immigration), 2018 FC 711 [Haastrup]; Konaté v Canada (Public Safety and Emergency Preparedness), 2018 FC 703 [Konaté]; Nagarasa v Canada (Citizenship and Immigration), 2018 FC 313 [Nagarasa]).

#### 4458:4:subtheme:7 · paragraphs 53-56

- Raw key terms: `applicant, harm, principal, psychological, concluded, conditions, exposed, further`
- Display key terms: `harm, principal, psychological, concluded, conditions, exposed, further`
- Argument roles: `evidence_fact, party_position`
- Explanation: Observed roles: evidence_fact, party_position Display terms: harm, principal, psychological, concluded, conditions, exposed, further Position/evidence statements: [50] The Respondent submits that the RAD had regard to the psychological report and addressed the Principal Applicant’s particular circumstances. Evidence spans paragraphs 53-56. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `party_position` cue `submits` at chunk `4252312` offsets `20-27`; context: [50] The Respondent submits that the RAD had regard to the psychological report and addressed the Principal Applicant’s particular circumstances.
- Evidence: `evidence_fact` cue `evidence` at chunk `4252313` offsets `99-107`; context: [51] Contrary to the Applicants’ submissions, the RAD did not disregard the relevant psychological evidence (a contrario, Cartagena at para 11; Okafor at para 13; Haastrup at para 26; Konaté at para 23).

#### 4458:4:subtheme:8 · paragraphs 57-61

- Raw key terms: `applicant, applicants, canada, place, principal, psychological, state, assessment`
- Display key terms: `place, principal, psychological, state, assessment`
- Argument roles: `counterargument_limitation, evidence_fact, governing_rule, issue, party_position`
- Explanation: Observed roles: counterargument_limitation, evidence_fact, governing_rule, issue, party_position Display terms: place, principal, psychological, state, assessment Position/evidence statements: [54] The Applicants argue that it is not the objective fear of the Principal Applicant that was the issue, but rather her subjective fear of returning to Nigeria. Rule/authority context: [58] Under these circumstances, it seems to me that it would then be reasonable for the RAD to consider the psychological assessment and determine the extent to which it is relevant to the reasonableness of the proposed  Evidence spans paragraphs 57-61. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `4252316` offsets `100-105`; context: [54] The Applicants argue that it is not the objective fear of the Principal Applicant that was the issue, but rather her subjective fear of returning to Nigeria.
- Evidence: `party_position` cue `argue` at chunk `4252316` offsets `20-25`; context: [54] The Applicants argue that it is not the objective fear of the Principal Applicant that was the issue, but rather her subjective fear of returning to Nigeria.
- Evidence: `counterargument_limitation` cue `but` at chunk `4252316` offsets `107-110`; context: [54] The Applicants argue that it is not the objective fear of the Principal Applicant that was the issue, but rather her subjective fear of returning to Nigeria.
- Evidence: `evidence_fact` cue `found that` at chunk `4252318` offsets `92-102`; context: Justice Grammond found that the removal of the applicant from Canada, in and of itself, would cause the applicant irreparable harm given his mental state.
- Evidence: `governing_rule` cue `Under` at chunk `4252320` offsets `5-10`; context: [58] Under these circumstances, it seems to me that it would then be reasonable for the RAD to consider the psychological assessment and determine the extent to which it is relevant to the reasonableness of the proposed IFA (Iyere v Canada (Citizenship and Immigration), 2018 FC 67).

#### 4458:4:subtheme:9 · paragraphs 62-63

- Raw key terms: `analysis, unreasonable, applicant, assessment, bring, canada, citizenship, clear`
- Display key terms: `analysis, unreasonable, assessment, bring, clear`
- Argument roles: `evidence_fact, issue`
- Explanation: Observed roles: evidence_fact, issue Display terms: analysis, unreasonable, assessment, bring, clear Evidence spans paragraphs 62-63. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `4252321` offsets `559-565`; context: The RAD’s analysis did not display an “utter unfamiliarity or insensitivity” toward mental health issues (Nagarasa at para 28).
- Evidence: `evidence_fact` cue `evidence` at chunk `4252321` offsets `232-240`; context: [59] While it is clear that removal from Canada may bring about negative psychological effects (Kanthasamy v Canada (Citizenship and Immigration), 2015 SCC 61, [2015] 3 SCR 909 at para 23), the RAD’s assessment of the psychological evidence was not unreasonable.

#### Section text

[19] The RAD stated the following in its decision:
Regarding the reach and sophistication of the NDA, I accept that the NDA is relatively sophisticated in its actions, as the Board’s Response to Information Request […] states that the group is relatively small but that their activities show a high degree of sophistication. However, I do not accept that the NDA operates outside of the Niger Delta Region and, specifically, in Ibadan, on a balance of probabilities. First, as outlined above, I do not accept the Appellants’ news articles on NDA attacks which pre-dated their refugee hearing as new evidence, and, as such, I am not considering them here. Second, the other evidence pointed to by the Appellants indicates that the NDA is active in the following states: Rivers, Ondo, Delta, Bayelsa, Cross River, Akwa Ibom, and is most active in Delta State. These regions are generally contained to the Delta region or South of Nigeria and certainty do not extend to Oyo state, where Ibadan is. Accordingly, I do not find, on a balance of probabilities, that the reach and sophistication of the NDA extends to Ibadan, Oyo state.
[Footnotes omitted; emphasis added.]

[20] The six states referred to as being active areas for the NDA are all located in the southern Niger Delta region of the country, along the coast of Nigeria where many oil refineries are located.

[21] The Applicants contest the finding of the RAD that Ibadan is outside the reach of the NDA and in particular argue that this determination is erroneous because it fails to consider the fact that the Applicants were pursued by the NDA in an area lying outside of the enumerated states (citing Ikechi v Canada (Citizenship and Immigration), 2013 FC 361 [Ikechi] and Zablon v Canada (Citizenship and Immigration), 2013 FC 58 [Zablon]).

[22] In particular, the Applicants underscore that the RAD accepted that the NDA were searching for the Applicants in Lagos, and argue that the Lagos incident (being outside the enumerated states where the NDA are known to operate) demonstrates that the NDA have the capacity to operate outside those regions, including in Ibadan—a possibility that was not contemplated sufficiently by the RAD.

[23] The Respondent submits that the RAD’s analysis on the first prong of the IFA test was reasonable. The Respondent argues that the Applicants have failed to provide sufficient evidence of the willingness or capacity of the NDA to look for the Applicants outside the Niger Delta region since December 2016. The Respondent also argues that the authorities cited in support of the Applicants’ argument are distinguishable from the case at bar (i.e., Ikechi and Zablon).

[24] The Applicants also provided me with a map of the region, and argue that Ibadan is closer in distance (as the crow flies) than Lagos to the outer perimeter of the area where the NDA operates in the east. The Applicants argued that although they were not suggesting that the record compelled the RAD to find that the Applicants could be found by the NDA in Ibadan, the RAD could not rely simply upon the distance between Ibadan and the known operating territory of the NDA to find no risk in Ibadan when the RAD also accepted that the Applicants had been sought by the NDA further afield than Ibadan, i.e., in Lagos.

[25] In reading the RAD decision, I do not see that the RAD relied upon distance as a determinative factor in its decision, other than the fact that it simply mentioned that Ibadan is in the Oyo state (not one of the states where the NDA are known to operate). In any event, I cannot see how a straight‑line distance comparison alone can play a significant role in the determination of the level of risk posed by an assailant group. The documentation does not elaborate on why the NDA operate in one region versus another, other than to say that they focus on regions where there is oil production.

[26] There is no evidence to allow one to conclude that the NDA have the motivation, willingness, capacity and resolve, on the balance of probabilities, to be active in Ibadan solely because the straight-line distance between Ibadan and the outer perimeter of the known NDA territory is similar to that of Lagos. A straight-line comparison is simply too simplistic and does not reflect other conditions, such as driving distance, road network infrastructure, forest density, the agent of persecution’s sphere of influence, etc.

[27] In Ikechi, the Pre-Removal Risk Assessment [PRRA] officer dismissed new evidence that the applicant’s sister had been kidnapped because the kidnapping did not occur in the specified IFA location. Mr. Justice Shore found that this determination was unreasonable because it suggests that the agents of persecution have “the ability and inclination to locate [the applicant] in other parts of Nigeria” (Ikechi at para 34). In the same case, Justice Shore specifically noted that further analysis was required to determine whether the IFA remains viable:

[35] Further analysis of the kidnapping was required in order to justify a finding that it did not rebut the IFA finding. It might, for example, be reasonable to infer from the location of the kidnapping (on a road between Umuahia and Orie Akpu) that Abuja and Benin remain viable IFAs. If it occurred somewhere far from those cities or in a place her in-laws associate with her, it may be reasonable to find that there is no serious possibility of risk in Benin or Abuja. The record does not contain information that would allow the Court to look to the record to support the PRRA Officer’s finding in this regard (Newfoundland and Labrador Nurses’ Union v Newfoundland and Labrador (Treasury Board), 2011 SCC 62, [2011] 3 SCR 708 at para 15).

[28] However, in contrast to Ikechi, in this case, the RAD did assess the evidence in respect of the risk associated with the IFA. Here, the RAD considered the Applicants’ submitted evidence (i.e., the friend’s affidavits from December 2016, and older news articles) and concluded that it was insufficient because it failed to establish a continued risk of persecution in Ibadan. In other words, the RAD considered the relevant evidence and made a determination about its persuasiveness.

[29] In addition, in Ikechi, the Court considered that if the applicant was in a place where her assailants would not think to find her, such a place could be a reasonable IFA. This goes back to why the NDA searched for the Applicants in Lagos. It was reasonable to search for them there on account of the fact that they fled to Lagos after the threats began; also, the friend with whom they stayed continued to live in Lagos, hence the reasonable connection to the Applicants. In fact, there is no evidence to suggest that Ibadan would pose the same risk of association with the Applicants.

[30] Finally, the Applicants read Ikechi as somehow putting the burden on the RAD to set out the reasons why Ibadan was a viable IFA. I do not agree. Once a viable IFA is identified by the decision-maker, the burden shifts to the applicant to show why it is not a viable option, on the balance of probabilities. It is this that the Applicants failed to do, in the eyes of the RAD. Here, the RAD engaged with the evidence and simply found that Ibadan was a viable IFA.

[31] The Applicants also cite Zablon in support of the proposition that where the extent of an assailant group’s reach beyond its otherwise known territory is not well documented, it is unreasonable for the RAD to have determined that the first prong of the test for an IFA has been met.

[32] I cannot agree that Zablon assists the Applicants. Although there was some discrepancy in the documentation in this case as to the reach of the NDA throughout the southern part of Nigeria, even on the most favourable reading of the evidence, there was nothing to suggest that the activities of the NDA extended into Ibadan. In addition, unlike the situation in Zablon, considerable documentary information was reviewed as regards the areas of activity of the NDA. Accordingly, this is not a case of the RAD ignoring the evidence on record and making a determination that cannot be justified on the facts of the case (Zablon at para 22).

[33] The NDA proceeded to Lagos not because they normally operate there, but because they knew that a person with whom the Applicants stayed after fleeing their village and before travelling to the U.S. and Canada was there. Although this may suggest that the NDA may have some capacity to search for individuals in areas where they are not normally active, the NDA would have to know where to look, regardless of whether they were still motivated to do so.

[34] Also, a distinction should be made between capacity and activity. Although the RAD accepted that the NDA may have had the capacity to search for the Applicants in Lagos (even though they may not have been operationally active in that area), there was no evidence that such concerns continued to exist even in Lagos. From a temporal perspective, although there may have been some capacity for the NDA to search outside their traditional area to find the Applicants, there is no evidence of them doing so past 2016.

[35] From what I can tell in reading the RAD decision, there was no evidence to suggest that the NDA would know to look for the Applicants in Ibadan, or that they would do so today. I see nothing unreasonable in that finding.

[36] The burden was on the Applicants to show that Ibadan was not a safe alternative, on the balance of probabilities. Other than an expressed concern that if the NDA can reach Lagos to search for the Applicants, they may be able to reach Ibadan, there was no evidence presented by the Applicants to establish that Ibadan posed a risk to them. Accordingly, the RAD did not consider there to be any reasonable evidence to suggest the NDA would look for the Applicants in Ibadan today, hence the finding that there is no risk to them there. There is nothing unreasonable in this finding.

[37] This is not a situation, as was the case in Ikechi, where an analysis of evidence was not undertaken, but should have been undertaken, in order to determine whether an alternative IFA existed. Here the analysis was undertaken, but there was simply insufficient evidence to displace the reasonableness of Ibadan being a viable IFA.

[38] The second alleged error relates to the motivation of the NDA, and the RAD’s finding that although there was affidavit evidence of the NDA searching for the Applicants five times and as late as March 2017 within the Niger Delta region, there is no evidence that the NDA have looked for the Applicants outside of the Niger Delta region (in particular in Lagos) since December 2016.

[39] After finding that the affidavit evidence submitted by the Applicants did not establish a section 96 or 97 risk for the Applicants in Ibadan, the RAD noted the following:
[…] this evidence does not speak to the current situation for the Appellants even in Lagos. I note that this affidavit was obtained in advance of the Appellants’ first RPD hearing, as it is dated December 28, 2016. In advance of their second hearing, the Appellants obtained updated affidavits indicating that the NDA continued to look for them with family in the Delta region, but no updated affidavit was obtained from [their friend] nor was any updated information obtained from [their friend] in advance of this appeal. Based upon this, I find that, while the NDA may have some interest in continuing to search for the Appellants in the Delta region, they have not expressed any willingness or capacity to look for the Appellants outside this region since December 2016. Accordingly, I find the fact that the NDA looked for the Appellants, once, in Lagos, in 2016, does not establish a section 96 or 97 risk for them in Ibadan on a forward-facing basis.
[Footnotes omitted; emphasis added.]

[40] The Applicants argue that the RAD’s finding of no ongoing risk in Ibadan is based upon the lack of affidavit evidence of NDA searches outside the Niger Delta region beyond December 2016.

[41] In the Applicants’ opinion, the RAD focused on a red herring. According to the Applicants, the timing of the actual attempts made by the NDA to search for the Applicants is irrelevant; what is relevant is whether the NDA have the proper means and motivation to locate the Applicants in the proposed IFA.

[42] The Applicants further argue that the RAD is effectively imposing a high burden of proof on them to demonstrate the persecutors’ continued interest in them, while they have not lived in the proposed IFA.

[43] In their argumentation, the Applicants rely heavily on Nimako v Canada (Citizenship and Immigration), 2013 FC 540 [Nimako]. However, Nimako offers little help to the Applicants. In that case, the RPD found that there was no persuasive evidence that the agent of persecution had made any efforts to search for the claimant beyond going to the family’s house. This Court determined that the RPD’s reasoning was unreasonable because it did not address the key issue of the applicant’s claim, namely, the issue of “whether [the agent of persecution] has the probable means and motivation to [search for the applicant]” (Nimako at para 7).

[44] That finding is inapplicable to the case at bar. First, in Nimako, there was clear evidence of an ongoing desire on the part of the assailant to search for the applicant. There is no such evidence here. Also, and contrary to Nimako, the tribunal in this case evaluated the search efforts by the NDA in Lagos as well as other evidence related to their ability and motivation to find the Applicants, and found that they were insufficient to support the Applicants’ claim of a continued risk of persecution.

[45] As a result, I see no reason to intervene here.
B. Second prong of the IFA test: Mental health concerns

[46] The Applicants submit that the RAD committed a reviewable error in assessing how the Principal Applicant’s mental health concerns affect the reasonableness of the IFA.

[47] At paragraph 40 of its decision, the RAD assessed the viability of the proposed IFA in the context of the Principal Applicant’s situation and mental health:
[…] I accept that the principal Appellant’s mental health may make relocation more difficult than average. I acknowledge that there is evidence on the record which indicates that she suffers from major depressive disorder and PTSD and that her condition could deteriorate if exposed to further threats of harm. I also accept that mental health care is not as comprehensive in Nigeria as it is in Canada. However, as I have found that the Appellants do not face a risk in Ibadan, I find that the principal Appellant is not being returned to a place where she would be exposed to further threats of harm. Moreover, even by the Appellants’ own submissions, there is some available mental health care in Nigeria. Accordingly, I do not find that the principal Appellant’s mental health renders relocation unreasonable, although it may make it more difficult than average.
[Footnotes omitted; emphasis added.]

[48] In particular, the Principal Applicant was diagnosed with major depressive disorder and post-traumatic stress disorder. The diagnosis report indicates that the Principal Applicant requires mental health treatment, and that the Principal Applicant’s “condition will deteriorate with exposure to further threats of harm; suicide risk will increase.”

[49] According to the Applicants, returning the Principal Applicant to Nigeria would have damaging mental health consequences for her. The RAD’s failure to realize that the Principal Applicant will be exposed to this risk is inconsistent with this Court’s jurisprudence (Cartagena v Canada (Citizenship and Immigration), 2008 FC 289 [Cartagena]; Okafor v Canada (Citizenship and Immigration), 2011 FC 1002 [Okafor]; Haastrup v Canada (Citizenship and Immigration), 2018 FC 711 [Haastrup]; Konaté v Canada (Public Safety and Emergency Preparedness), 2018 FC 703 [Konaté]; Nagarasa v Canada (Citizenship and Immigration), 2018 FC 313 [Nagarasa]).

[50] The Respondent submits that the RAD had regard to the psychological report and addressed the Principal Applicant’s particular circumstances. According to the Respondent, the RAD noted that it considered the report that indicated that the Principal Applicant suffered from mental health conditions and reasonably concluded that the Principal Applicant would not be exposed to a risk of harm.

[51] Contrary to the Applicants’ submissions, the RAD did not disregard the relevant psychological evidence (a contrario, Cartagena at para 11; Okafor at para 13; Haastrup at para 26; Konaté at para 23).

[52] The psychological assessment report filed by the Principal Applicant confirmed that the Principal Applicant is suffering from major depressive disorder and post-traumatic stress disorder. The psychologist stated that the Principal Applicant felt that she would be in grave danger if she returned to Nigeria. The report concluded with the finding that the Principal Applicant’s mental health conditions would deteriorate if she were to be exposed to “further threats of harm,” and her suicide risk would increase.

[53] However, the point made by the RAD is that Ibadan was not a place that would expose the Principal Applicant to “further threats of harm.”

[54] The Applicants argue that it is not the objective fear of the Principal Applicant that was the issue, but rather her subjective fear of returning to Nigeria. In fact, the Applicants’ counsel conceded that there is no place in Nigeria where the Principal Applicant, in her present state, would feel safe.

[55] I do not read the cases cited by the Applicants’ counsel as supportive of his position. First, in Cartagena, Mr. Justice Mosley concluded that the finding of a viable IFA for the applicant was unreasonable for a variety of reasons, only one of which was the applicant’s mental state. That is not the case here.

[56] As for Konaté, that was a motion to stay the applicant’s removal. Mr. Justice Grammond found that the removal of the applicant from Canada, in and of itself, would cause the applicant irreparable harm given his mental state. That is not the case here. According to the psychological assessment, concerns over the possible deterioration of the Principal Applicant’s mental condition are tied to her finding herself in a place where she is exposed to risk and “further threats of harm.”

[57] Although the Applicants’ psychological report does raise concerns regarding the Principal Applicant returning to Nigeria, it does not assess the impact of her returning to specific cities far from the place where their lives were initially threatened (Verma v Canada (Citizenship and Immigration), 2016 FC 404) other than to say that the concerns in respect of the Principal Applicant’s psychological well-being related only to her returning to an area where there was a continued risk of harm.

[58] Under these circumstances, it seems to me that it would then be reasonable for the RAD to consider the psychological assessment and determine the extent to which it is relevant to the reasonableness of the proposed IFA (Iyere v Canada (Citizenship and Immigration), 2018 FC 67).

[59] While it is clear that removal from Canada may bring about negative psychological effects (Kanthasamy v Canada (Citizenship and Immigration), 2015 SCC 61, [2015] 3 SCR 909 at para 23), the RAD’s assessment of the psychological evidence was not unreasonable. The RAD evaluated the Principal Applicant’s mental health, considered the impact of relocation to Ibadan on her mental health, and evaluated the sufficiency of the mental health services in Ibadan. The RAD’s analysis did not display an “utter unfamiliarity or insensitivity” toward mental health issues (Nagarasa at para 28).

[60] As a result, I see nothing unreasonable in this analysis or in the conclusion of the RAD.


## 4458:5 · paragraphs 64-65

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `1044a4e7b27c5f7efc3cefac1e14f124816a778e3293e863866c07fda1d38e29`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4458:5:subtheme:1 · paragraphs 64-65

- Raw key terms: `accordingly, application, conclusion, dismiss, judicial, review, viii`
- Display key terms: `accordingly, conclusion, dismiss, judicial, review, viii`
- Argument roles: `reasoning_application`
- Explanation: Observed roles: reasoning_application Display terms: accordingly, conclusion, dismiss, judicial, review, viii Application context: [61] Accordingly, I would dismiss the application for judicial review. Evidence spans paragraphs 64-65. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `reasoning_application` cue `Accordingly` at chunk `4252323` offsets `5-16`; context: [61] Accordingly, I would dismiss the application for judicial review.

#### Section text

VIII. Conclusion

[61] Accordingly, I would dismiss the application for judicial review.


## 4458:6 · paragraphs 66-67

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `3ababe0c1368dfc7dce0962b153432fdabf76531d805d53ff40d214852b1f87c`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 4458:6:subtheme:1 · paragraphs 66-67

- Raw key terms: `imm-2401-19, judgment, pamel, appearances, applicants, application, attorney, blessing`
- Display key terms: `imm-2401-19, pamel, blessing`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: imm-2401-19, pamel, blessing Operative outcome context: JUDGMENT for IMM-2401-19 THIS COURT’S JUDGMENT is that: The application for judicial review is dismissed. Evidence spans paragraphs 66-67. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `4252323` offsets `189-197`; context: There is no question for certification.
- Evidence: `disposition` cue `dismissed` at chunk `4252323` offsets `166-175`; context: JUDGMENT for IMM-2401-19
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed.

#### Section text

JUDGMENT for IMM-2401-19
THIS COURT’S JUDGMENT is that:
The application for judicial review is dismissed.
There is no question for certification.
“Peter G. Pamel”
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
IMM-2401-19
STYLE OF CAUSE:
BLESSING FEBOKE, PREYE FEBOKE, DAVID DOUBRA FEBOKE, PEREZIDE FEBOKE, CHRISTABEL EDIERE FEBOKE, FAITH TAMARAKHURO FEBOKE v THE MINISTER OF CITIZENSHIP AND IMMIGRATION
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
December 12, 2019
JUDGMENT AND REASONS:
PAMEL J.
DATED:
january 28, 2020
APPEARANCES:
Luke Mc Rae
For The Applicants
Nicole Paduraru
For The Respondent
SOLICITORS OF RECORD:
Bondy Immigration Law
Toronto, Ontario
For The Applicants
Attorney General of Canada
Toronto, Ontario
For The Respondent
