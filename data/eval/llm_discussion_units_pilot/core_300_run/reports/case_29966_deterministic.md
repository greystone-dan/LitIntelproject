# Discussion Units: case 29966

> Read-only inspection. Units are derived from existing `CaseChunk rows (chunk_set=paragraph)`; no canonical rows were written.

## Deterministic reading

This is a rule-based reading, not an LLM summary. Paragraphs are grouped using continuity signals such as text overlap, shared authority, changes in signal density, heading boundaries, citation/statute/tag overlap, and detected argument-role cues.
The deterministic layer identifies evidence-bearing spans and roles; it does not generate the fluent explanations or semantic labels produced by the hybrid LLM review.

- Paragraph-like inputs: **45**
- Continuity pairs: **44**
- Discussion Units: **5**
- Paragraph source hashes: **45**
- Sub-themes: **15**

## 29966:1 · paragraphs 0-9

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `e81b525302eebb69c5e2a9986400675787d5067754d238beb4e43d6e8d9a3390`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 29966:1:subtheme:1 · paragraphs 0-7

- Raw key terms: `applicant, employment, policy, vaccination, august, misconduct, terminated, benefits`
- Display key terms: `employment, policy, vaccination, august, misconduct, terminated, benefits`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: employment, policy, vaccination, august, misconduct, terminated, benefits Rule/authority context: That directive was implemented under section 77. | [5] Specially, on September 21, 2021, the Applicant requested an exemption under the Human Rights Code. Application context: [7] On December 18, 2021, the Applicant applied for regular EI benefits. | [8] On May 5, 2022, the Commission denied the Applicant’s EI benefits because it found that the Applicant lost his employment due to his own misconduct. Operative outcome context: For this reason, the SST-GD upheld the Canada Employment Insurance Commission’s (the “Commission”) decision to deny employment insurance (EI) benefits to the Applicant. | Since his exemption request was denied, the UHN reminded the Applicant that he would be terminated on October 22, 2021, if he did not provide proof of his COVID vaccination. Evidence spans paragraphs 0-7. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5395414` offsets `614-622`; context: The SST-GD decision in question found that the Applicant was terminated for misconduct from his job at the Toronto General Hospital’s Universal Health Network (the “UHN”).
- Evidence: `evidence_fact` cue `found that` at chunk `5395414` offsets `623-633`; context: The SST-GD decision in question found that the Applicant was terminated for misconduct from his job at the Toronto General Hospital’s Universal Health Network (the “UHN”).
- Evidence: `disposition` cue `upheld` at chunk `5395414` offsets `791-797`; context: For this reason, the SST-GD upheld the Canada Employment Insurance Commission’s (the “Commission”) decision to deny employment insurance (EI) benefits to the Applicant.
- Evidence: `evidence_fact` cue `record` at chunk `5395415` offsets `183-189`; context: [3] In August 2021, the UHN implemented a COVID-19 vaccine policy in accordance with Directive 6, which required all public health employees to prove their full COVID- 19 vaccination record or receive an exemption on medical or Ontario’s Human Rights Code grounds (the “Policy”).
- Evidence: `governing_rule` cue `under` at chunk `5395415` offsets `311-316`; context: That directive was implemented under section 77.
- Evidence: `governing_rule` cue `under` at chunk `5395417` offsets `75-80`; context: [5] Specially, on September 21, 2021, the Applicant requested an exemption under the Human Rights Code.
- Evidence: `disposition` cue `denied` at chunk `5395417` offsets `334-340`; context: Since his exemption request was denied, the UHN reminded the Applicant that he would be terminated on October 22, 2021, if he did not provide proof of his COVID vaccination.
- Evidence: `reasoning_application` cue `applied` at chunk `5395419` offsets `40-47`; context: [7] On December 18, 2021, the Applicant applied for regular EI benefits.
- Evidence: `evidence_fact` cue `found that` at chunk `5395420` offsets `81-91`; context: [8] On May 5, 2022, the Commission denied the Applicant’s EI benefits because it found that the Applicant lost his employment due to his own misconduct.
- Evidence: `reasoning_application` cue `because` at chunk `5395420` offsets `70-77`; context: [8] On May 5, 2022, the Commission denied the Applicant’s EI benefits because it found that the Applicant lost his employment due to his own misconduct.
- Evidence: `disposition` cue `denied` at chunk `5395420` offsets `35-41`; context: [8] On May 5, 2022, the Commission denied the Applicant’s EI benefits because it found that the Applicant lost his employment due to his own misconduct.
- Evidence: `evidence_fact` cue `found that` at chunk `5395421` offsets `52-62`; context: [9] The SST-GD upheld the Commission’s decision and found that the Applicant was terminated because he refused to follow the UHN’s vaccination policy that had been implemented to protect staff and clients during the pandemic.
- Evidence: `governing_rule` cue `under` at chunk `5395421` offsets `262-267`; context: This refusal constituted misconduct under the Act because it was an intentional breach of his employment obligations – a breach that he knew (or ought to have known) would likely result in his termination.
- Evidence: `reasoning_application` cue `because` at chunk `5395421` offsets `92-99`; context: [9] The SST-GD upheld the Commission’s decision and found that the Applicant was terminated because he refused to follow the UHN’s vaccination policy that had been implemented to protect staff and clients during the pandemic.
- Evidence: `disposition` cue `upheld` at chunk `5395421` offsets `15-21`; context: [9] The SST-GD upheld the Commission’s decision and found that the Applicant was terminated because he refused to follow the UHN’s vaccination policy that had been implemented to protect staff and clients during the pandemic.

#### 29966:1:subtheme:2 · paragraphs 8-9

- Raw key terms: `deliberate, employer, made, misconduct, policy, sst-ad, sst-gd, according`
- Display key terms: `deliberate, employer, made, misconduct, policy, sst-ad, sst-gd, according`
- Argument roles: `disposition, evidence_fact, issue`
- Explanation: Observed roles: disposition, evidence_fact, issue Display terms: deliberate, employer, made, misconduct, policy, sst-ad, sst-gd, according Operative outcome context: [11] The SST-AD upheld the SST-GD’s finding that the Applicant made a personal and deliberate choice not to follow the employer’s Policy, which resulted in him being terminated from his employment for misconduct. Evidence spans paragraphs 8-9. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issue` at chunk `5395422` offsets `81-86`; context: [10] The SST-AD found no reviewable error made by the SST-GD when it decided the issue of misconduct.
- Evidence: `evidence_fact` cue `found that` at chunk `5395422` offsets `105-115`; context: It found that the SST-GD evaluated this issue by reviewing the parameters set out in the case law: AD Decision, at para 34, citing Paradis v Canada (Attorney General), 2016 FC 1282; see also Canada (Attorney General) v McNamara, 2007 FCA 107.
- Evidence: `disposition` cue `upheld` at chunk `5395423` offsets `16-22`; context: [11] The SST-AD upheld the SST-GD’s finding that the Applicant made a personal and deliberate choice not to follow the employer’s Policy, which resulted in him being terminated from his employment for misconduct.

#### Section text

Kuk v. Canada (Attorney General)
Court (s) Database
Federal Court Decisions
Date
2023-08-23
Neutral citation
2023 FC 1134
File numbers
T-186-23
Decision Content
Date: 20230823
Docket: T-186-23
Citation: 2023 FC 1134
Ottawa, Ontario, August 23, 2023
PRESENT: The Honourable Madam Justice McVeigh
BETWEEN:
WIESLAW KUK
Applicant
and
ATTORNEY GENERAL OF CANADA
Respondent
JUDGMENT AND REASONS
I. Introduction [1] This is an application for judicial review of a Social Security Tribunal (SST) Appeal Division (SST-AD) decision not to grant leave to appeal a General Division’s (SST-GD) decision. The SST-GD decision in question found that the Applicant was terminated for misconduct from his job at the Toronto General Hospital’s Universal Health Network (the “UHN”). For this reason, the SST-GD upheld the Canada Employment Insurance Commission’s (the “Commission”) decision to deny employment insurance (EI) benefits to the Applicant. The misconduct at issue involved the Applicant’s intentional voluntary choice not to comply with the UHN’s COVID-19 vaccination policy.
II. Background [2] The Applicant represented himself at the hearing. He was employed at the UHN as an information technology analyst from 2006 until November 2021. The Applicant indicated that the 16 years before the pandemic he worked half time at home and half time at the office. He said he rarely had interaction with staff or patients. Once the COVID-19 pandemic began he worked full time at home.

[3] In August 2021, the UHN implemented a COVID-19 vaccine policy in accordance with Directive 6, which required all public health employees to prove their full COVID- 19 vaccination record or receive an exemption on medical or Ontario’s Human Rights Code grounds (the “Policy”). That directive was implemented under section 77.7 of the Health Protection and Promotion Act, RSO 1990, c H7 which mandated Ontario public health organizations to establish, implement, and ensure compliance with a COVID-19 vaccination policy.

[4] Throughout August and September 2021, the UHN sent multiple email communications to its employees reminding them of the requirement to get vaccinated for COVID-19. While one of these communications gave the impression that remote employees did not need to get vaccinated, later communications specified that all employees needed to get vaccinated unless they received an exemption. These communications included:
On August 19, 2021, the UHN told its employees by email that it was updating its existing COVID-19 vaccine policy to comply with Directive 6. All staff had to prove their vaccination status, “with the exception of those who have a medical exception.”
On August 25, 2021, the UHN emailed a follow-up message to address concerns and frequently asked questions (FAQ). The FAQ section stated that, for the few employees who are never required to work on site, the vaccination requirement is not mandatory. It added this: “[h]owever, if your situation changes and you are in a role where you have to come on site, even if very infrequently, you must be vaccinated.”
On August 31, 2021, the UHN told staff that “all employees” had to prove their vaccination status. This email did not reference any exception for remote workers.
On September 13, 2021, the UHN again reminded staff by email that “everyone must upload their vaccination receipts”. The only exceptions listed were medical and Human Rights Code grounds. This message clarified the previous FAQ section’s commentary about remote work, as follows:
A: The intent of the Remote Work Policy is to allow our employees flexibility in how the work is performed. The vast majority of UHN’s employees are considered essential and as such might be recalled back to the worksite at any given time. In accordance with the Business Continuity Policy, those recalled back to work will be expected to be compliant with the COVID-19 Vaccine Policy. There are very few UHN employees who work remotely 100% of their time and as a result, can be exempted. Each case will be reviewed on its own merits.

[5] Specially, on September 21, 2021, the Applicant requested an exemption under the Human Rights Code. This request was rejected by the UHN on October 4, 2021. The Applicant’s request was rooted in the fact that he disagreed with the policy and it did not specify any protected ground under the Code. Since his exemption request was denied, the UHN reminded the Applicant that he would be terminated on October 22, 2021, if he did not provide proof of his COVID vaccination. The UHN also told him that he could avoid termination by booking a first COVID vaccination dose.

[6] The Applicant did not take steps to get a COVID vaccine and as such, the UHN terminated his employment on November 2, 2021.

[7] On December 18, 2021, the Applicant applied for regular EI benefits. Such benefits are governed by the Employment Insurance Act, SC 1996, c 23 (the “EIA”), which establishes a public insurance program to preserve economic security and ensure Canadian workers’ re-entry into the labour market. It accomplishes this goal by paying EI benefits to claimants when their earnings are interrupted. Sections 29 to 33 of the EIA stipulate that a claimant’s lost employment is only insurable if it is involuntary. Accordingly, claimants are disqualified from receiving EI benefits if they voluntarily leave their job without “just cause” or due to their own misconduct. See relevant provisions of the EIA reproduced in Appendix A.

[8] On May 5, 2022, the Commission denied the Applicant’s EI benefits because it found that the Applicant lost his employment due to his own misconduct. On July 22, 2022, the Commission upheld its decision on reconsideration. The Applicant appealed this decision to the SST-GD on August 14, 2022.

[9] The SST-GD upheld the Commission’s decision and found that the Applicant was terminated because he refused to follow the UHN’s vaccination policy that had been implemented to protect staff and clients during the pandemic. This refusal constituted misconduct under the Act because it was an intentional breach of his employment obligations – a breach that he knew (or ought to have known) would likely result in his termination.

[10] The SST-AD found no reviewable error made by the SST-GD when it decided the issue of misconduct. It found that the SST-GD evaluated this issue by reviewing the parameters set out in the case law: AD Decision, at para 34, citing Paradis v Canada (Attorney General), 2016 FC 1282; see also Canada (Attorney General) v McNamara, 2007 FCA 107. According to the SST-GD decision, “it is well established that a deliberate violation of the employer’s policy is considered misconduct within the meaning of the EIA”: AD Decision, at para 25, citing Canada (Attorney General) v Bellavance, 2005 FCA 87 [Bellavance]; Canada (Attorney General) v Gagnon, 2002 FCA 460.

[11] The SST-AD upheld the SST-GD’s finding that the Applicant made a personal and deliberate choice not to follow the employer’s Policy, which resulted in him being terminated from his employment for misconduct.


## 29966:2 · paragraphs 10-39

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `08781d8d1b917f7e9f490a4fb7faf84baa33b4263877e670f792b870ff79706d`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 29966:2:subtheme:1 · paragraphs 10-12

- Raw key terms: `canada, appeal, applicant, bhamra, citing, decision, general, issue`
- Display key terms: `bhamra, citing`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: bhamra, citing Position/evidence statements: The Applicant argued that it was background information and should be allowed. Rule/authority context: Standard of Review [13] The standard of review to be applied to an SST-AD decision denying leave to appeal is reasonableness: Bhamra v Canada (Attorney General), 2023 FCA 121 [Bhamra] at para 3, citing Cameron v Canada ( Application context: Standard of Review [13] The standard of review to be applied to an SST-AD decision denying leave to appeal is reasonableness: Bhamra v Canada (Attorney General), 2023 FCA 121 [Bhamra] at para 3, citing Cameron v Canada ( Operative outcome context: Issue [12] The sole issue in this application is whether the SST-AD reasonably denied the Applicant leave to appeal the SST-GD’s Decision. | The Applicant argued that it was background information and should be allowed. Evidence spans paragraphs 10-12. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `Issue` at chunk `5395423` offsets `218-223`; context: Issue [12] The sole issue in this application is whether the SST-AD reasonably denied the Applicant leave to appeal the SST-GD’s Decision.
- Evidence: `governing_rule` cue `Standard of Review` at chunk `5395423` offsets `361-379`; context: Standard of Review [13] The standard of review to be applied to an SST-AD decision denying leave to appeal is reasonableness: Bhamra v Canada (Attorney General), 2023 FCA 121 [Bhamra] at para 3, citing Cameron v Canada (Attorney General), 2018 FCA 100.
- Evidence: `reasoning_application` cue `applied` at chunk `5395423` offsets `414-421`; context: Standard of Review [13] The standard of review to be applied to an SST-AD decision denying leave to appeal is reasonableness: Bhamra v Canada (Attorney General), 2023 FCA 121 [Bhamra] at para 3, citing Cameron v Canada (Attorney General), 2018 FCA 100.
- Evidence: `disposition` cue `denied` at chunk `5395423` offsets `297-303`; context: Issue [12] The sole issue in this application is whether the SST-AD reasonably denied the Applicant leave to appeal the SST-GD’s Decision.
- Evidence: `issue` cue `whether` at chunk `5395424` offsets `308-315`; context: To determine whether the SST-AD’s decision is reasonable, the reviewing court must ask “whether the decision bears the hallmarks of reasonableness – justification, transparency and intelligibility – and whether it is justified in relation to the relevant factual and legal constraints that bear on the decision”: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 86 and 99.
- Evidence: `party_position` cue `argued` at chunk `5395424` offsets `923-929`; context: The Applicant argued that it was background information and should be allowed.
- Evidence: `evidence_fact` cue `affidavit` at chunk `5395424` offsets `781-790`; context: Preliminary Issue [15] Several of the exhibits in the Applicant’s affidavit are inadmissible.
- Evidence: `disposition` cue `allowed` at chunk `5395424` offsets `979-986`; context: The Applicant argued that it was background information and should be allowed.
- Evidence: `evidence_fact` cue `record` at chunk `5395425` offsets `51-57`; context: [16] The general rule is that only the evidentiary record before the administrative decision-maker is admissible on judicial review: see Bernard v Canada (Revenue Agency), 2015 FCA 263 [Bernard] at paras 13-18.

#### 29966:2:subtheme:2 · paragraphs 13-15

- Raw key terms: `attorney, canada, desda, evidence, exceptions, found, general, pursuant`
- Display key terms: `desda, exceptions, pursuant`
- Argument roles: `disposition, evidence_fact, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, governing_rule, issue, reasoning_application Display terms: desda, exceptions, pursuant Rule/authority context: The Law [19] Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed in  | [20] Pursuant to, section 58 of the DESDA, the SST-AD was empowered to set the SST-GD’s decision aside only if it found the latter to have failed to observe a principle of natural justice, erred in law, or based its deci Application context: This evidence is also irrelevant and immaterial because it is focussed on the effectiveness of the UHN’s policy and behaviour (rather than the EI misconduct test). Operative outcome context: The Law [19] Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed in  Evidence spans paragraphs 13-15. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5395426` offsets `227-233`; context: [17] There are three exceptions to the general rule that new evidence is not admissible on judicial review:
(1)evidence that provides general background in circumstances where that information might assist in understanding the issues relevant to the judicial review;
(2)evidence necessary to bring to the attention of the court procedural defects not found in the evidentiary record of the administrative decision-maker; and
(3)evidence to highlight the complete absence of evidence before the administrative decision-maker.
- Evidence: `evidence_fact` cue `evidence` at chunk `5395426` offsets `61-69`; context: [17] There are three exceptions to the general rule that new evidence is not admissible on judicial review:
(1)evidence that provides general background in circumstances where that information might assist in understanding the issues relevant to the judicial review;
(2)evidence necessary to bring to the attention of the court procedural defects not found in the evidentiary record of the administrative decision-maker; and
(3)evidence to highlight the complete absence of evidence before the administrative decision-maker.
- Evidence: `evidence_fact` cue `evidence` at chunk `5395427` offsets `82-90`; context: [18] These exhibits do not fit into any of the exceptions to the rule against new evidence, outlined below.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5395427` offsets `363-374`; context: The Law [19] Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed in the subsection.
- Evidence: `reasoning_application` cue `because` at chunk `5395427` offsets `156-163`; context: This evidence is also irrelevant and immaterial because it is focussed on the effectiveness of the UHN’s policy and behaviour (rather than the EI misconduct test).
- Evidence: `disposition` cue `granted` at chunk `5395427` offsets `424-431`; context: The Law [19] Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed in the subsection.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5395428` offsets `5-16`; context: [20] Pursuant to, section 58 of the DESDA, the SST-AD was empowered to set the SST-GD’s decision aside only if it found the latter to have failed to observe a principle of natural justice, erred in law, or based its decision on an erroneous finding of fact made in a perverse or capricious manner without regard to the material before it: see Cecchetto v.

#### 29966:2:subtheme:3 · paragraphs 16-20

- Raw key terms: `applicant, employment, misconduct, appeal, attorney, canada, claimant, court`
- Display key terms: `employment, misconduct`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, issue, party_position, reasoning_application Display terms: employment, misconduct Position/evidence statements: [24] The Applicant submits that it is his belief that the SST-AD misinterpreted the term “misconduct” and consequently, erred in concluding that his refusal to be vaccinated amounted to misconduct under the EIA. Rule/authority context: Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed above: see O’Rou | Further, as the Federal Court of Appeal found in Lemire at para 15 “[misconduct] is not a question of deciding whether or not the dismissal is justified under the meaning of labour law but, rather, of determining, accord Application context: The SST’s findings of misconduct [22] This case focuses on the concept of misconduct under the EIA framework, which stipulates that a claimant is disqualified from receiving any benefits if the claimant lost any employme | The Applicant applied for an exemption; it was not granted to him. Operative outcome context: Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed above: see O’Rou | Here, as in Nelson, the Applicant was aware of the policy and made a deliberate voluntary choice not to follow the policy, even after being notified that his exemption was denied and without the COVID vaccine his employm Evidence spans paragraphs 16-20. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5395429` offsets `54-61`; context: [21] To do so, the SST-AD is first required to decide whether to grant the Applicant leave to appeal.
- Evidence: `governing_rule` cue `Pursuant to` at chunk `5395429` offsets `102-113`; context: Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed above: see O’Rourke v Canada (Attorney General), 2019 FCA 60 at para 9; Mishibinijima v Canada (Attorney General), 2007 FCA 36 at para 14.
- Evidence: `reasoning_application` cue `because` at chunk `5395429` offsets `894-901`; context: The SST’s findings of misconduct [22] This case focuses on the concept of misconduct under the EIA framework, which stipulates that a claimant is disqualified from receiving any benefits if the claimant lost any employment because of their misconduct: see section 30.
- Evidence: `disposition` cue `granted` at chunk `5395429` offsets `163-170`; context: Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed above: see O’Rourke v Canada (Attorney General), 2019 FCA 60 at para 9; Mishibinijima v Canada (Attorney General), 2007 FCA 36 at para 14.
- Evidence: `issue` cue `whether` at chunk `5395430` offsets `18-25`; context: [23] To determine whether the misconduct could result in dismissal, there must be a causal link between the claimant’s misconduct and the claimant’s employment.
- Evidence: `evidence_fact` cue `evidence` at chunk `5395430` offsets `618-626`; context: Further, as the Federal Court of Appeal found in Lemire at para 15 “[misconduct] is not a question of deciding whether or not the dismissal is justified under the meaning of labour law but, rather, of determining, according to an objective assessment of the evidence, whether the misconduct was such that its author could normally foresee that it would be likely to result in his or her dismissal”.
- Evidence: `governing_rule` cue `under` at chunk `5395430` offsets `513-518`; context: Further, as the Federal Court of Appeal found in Lemire at para 15 “[misconduct] is not a question of deciding whether or not the dismissal is justified under the meaning of labour law but, rather, of determining, according to an objective assessment of the evidence, whether the misconduct was such that its author could normally foresee that it would be likely to result in his or her dismissal”.
- Evidence: `counterargument_limitation` cue `but` at chunk `5395430` offsets `545-548`; context: Further, as the Federal Court of Appeal found in Lemire at para 15 “[misconduct] is not a question of deciding whether or not the dismissal is justified under the meaning of labour law but, rather, of determining, according to an objective assessment of the evidence, whether the misconduct was such that its author could normally foresee that it would be likely to result in his or her dismissal”.
- Evidence: `party_position` cue `submits` at chunk `5395431` offsets `19-26`; context: [24] The Applicant submits that it is his belief that the SST-AD misinterpreted the term “misconduct” and consequently, erred in concluding that his refusal to be vaccinated amounted to misconduct under the EIA.
- Evidence: `governing_rule` cue `under` at chunk `5395431` offsets `197-202`; context: [24] The Applicant submits that it is his belief that the SST-AD misinterpreted the term “misconduct” and consequently, erred in concluding that his refusal to be vaccinated amounted to misconduct under the EIA.
- Evidence: `counterargument_limitation` cue `but` at chunk `5395431` offsets `312-315`; context: The Applicant argues that his decision not to get vaccinated for COVID is not voluntary misconduct, but rather, an “unavoidable consequence of employer’s intimidating tactics”.
- Evidence: `disposition` cue `denied` at chunk `5395432` offsets `543-549`; context: Here, as in Nelson, the Applicant was aware of the policy and made a deliberate voluntary choice not to follow the policy, even after being notified that his exemption was denied and without the COVID vaccine his employment would be terminated.
- Evidence: `evidence_fact` cue `found that` at chunk `5395433` offsets `479-489`; context: The SST-GD also found that the Applicant had been informed of the employer’s Policy and was given time to comply.
- Evidence: `reasoning_application` cue `applied` at chunk `5395433` offsets `660-667`; context: The Applicant applied for an exemption; it was not granted to him.
- Evidence: `disposition` cue `granted` at chunk `5395433` offsets `697-704`; context: The Applicant applied for an exemption; it was not granted to him.

#### 29966:2:subtheme:4 · paragraphs 21-23

- Raw key terms: `applicant, reasonable, sst-ad, sst-gd, decision, findings, found, given`
- Display key terms: `reasonable, sst-ad, sst-gd, findings, given`
- Argument roles: `disposition, evidence_fact, issue, party_position, reasoning_application`
- Explanation: Observed roles: disposition, evidence_fact, issue, party_position, reasoning_application Display terms: reasonable, sst-ad, sst-gd, findings, given Position/evidence statements: [29] Although the Applicant submitted that the SST-GD erred in determining that the Policy was part of his contract of employment and that he breached his contract by not getting vaccinated, the SST-AD found that i) an e Application context: Given the Applicant’s failure to find a reviewable error, the SST-AD denied leave to appeal because the appeal had no reasonable chance of success. Operative outcome context: Given the Applicant’s failure to find a reviewable error, the SST-AD denied leave to appeal because the appeal had no reasonable chance of success. Evidence spans paragraphs 21-23. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5395434` offsets `139-147`; context: [27] Even though it is clear that the Applicant disagrees with the UHN that this policy protected his health and safety, the only relevant question before the SST-GD was whether the Applicant knew that his voluntary decision not to get vaccinated might result in his termination.
- Evidence: `issue` cue `issue` at chunk `5395435` offsets `87-92`; context: [28] The SST-AD found the SST-GD did not commit a reviewable error when it decided the issue of misconduct.
- Evidence: `reasoning_application` cue `because` at chunk `5395435` offsets `390-397`; context: Given the Applicant’s failure to find a reviewable error, the SST-AD denied leave to appeal because the appeal had no reasonable chance of success.
- Evidence: `disposition` cue `denied` at chunk `5395435` offsets `367-373`; context: Given the Applicant’s failure to find a reviewable error, the SST-AD denied leave to appeal because the appeal had no reasonable chance of success.
- Evidence: `party_position` cue `submitted` at chunk `5395436` offsets `28-37`; context: [29] Although the Applicant submitted that the SST-GD erred in determining that the Policy was part of his contract of employment and that he breached his contract by not getting vaccinated, the SST-AD found that i) an employer has an obligation to take all reasonable precautions to protect the health and safety of its employees in their workplace, and ii) such precautions include mandatory vaccination policies, imposed by the province.
- Evidence: `evidence_fact` cue `found that` at chunk `5395436` offsets `202-212`; context: [29] Although the Applicant submitted that the SST-GD erred in determining that the Policy was part of his contract of employment and that he breached his contract by not getting vaccinated, the SST-AD found that i) an employer has an obligation to take all reasonable precautions to protect the health and safety of its employees in their workplace, and ii) such precautions include mandatory vaccination policies, imposed by the province.

#### 29966:2:subtheme:5 · paragraphs 24-24

- Raw key terms: `applicant, argued, care, changes, contract, covid, doing, employed`
- Display key terms: `care, changes, contract, covid, doing, employed`
- Argument roles: `issue, party_position`
- Explanation: Observed roles: issue, party_position Display terms: care, changes, contract, covid, doing, employed Position/evidence statements: [30] The Applicant argued that his letter of employment was not an employment contract and it did not have within it that he must receive a COVID vaccine so how could he be fired for not doing it. Evidence spans paragraphs 24-24. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `question` at chunk `5395437` offsets `503-511`; context: COVID was unknown at the time of his letter and is now included as one of many immunizations that must be proven to be employed by the health care institute in question.
- Evidence: `party_position` cue `argued` at chunk `5395437` offsets `19-25`; context: [30] The Applicant argued that his letter of employment was not an employment contract and it did not have within it that he must receive a COVID vaccine so how could he be fired for not doing it.

#### 29966:2:subtheme:6 · paragraphs 25-29

- Raw key terms: `found, misconduct, applicant, dismissal, employer, policy, appeal, arguments`
- Display key terms: `misconduct, dismissal, employer, policy, arguments`
- Argument roles: `counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application`
- Explanation: Observed roles: counterargument_limitation, disposition, evidence_fact, governing_rule, party_position, reasoning_application Display terms: misconduct, dismissal, employer, policy, arguments Position/evidence statements: Other Arguments [34] The Applicant argued that the SST-AD made an error of law by finding that he breached his contractual obligations by not getting vaccinated. | The Applicant submits that if he had known he was not being paid for those three days he would have been able to claim constructive dismissal on his EI claim. Rule/authority context: [33] I find that it was reasonable for the SST-AD to conclude that the Applicant had no reasonable chance of success in arguing that his actions did not constitute misconduct under the EIA framework. Application context: [31] Justice Pentney recently released a highly analogous decision, where he found that an employee who is terminated for misconduct because they refused to get a COVID vaccine, contrary to an employer’s vaccination poli | [33] I find that it was reasonable for the SST-AD to conclude that the Applicant had no reasonable chance of success in arguing that his actions did not constitute misconduct under the EIA framework. Operative outcome context: The Applicant was aware that his request for an exemption was denied. Evidence spans paragraphs 25-29. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `evidence_fact` cue `found that` at chunk `5395438` offsets `77-87`; context: [31] Justice Pentney recently released a highly analogous decision, where he found that an employee who is terminated for misconduct because they refused to get a COVID vaccine, contrary to an employer’s vaccination policy, is not entitled to receive EI benefits: see Cecchetto.
- Evidence: `reasoning_application` cue `because` at chunk `5395438` offsets `133-140`; context: [31] Justice Pentney recently released a highly analogous decision, where he found that an employee who is terminated for misconduct because they refused to get a COVID vaccine, contrary to an employer’s vaccination policy, is not entitled to receive EI benefits: see Cecchetto.
- Evidence: `disposition` cue `denied` at chunk `5395439` offsets `324-330`; context: The Applicant was aware that his request for an exemption was denied.
- Evidence: `party_position` cue `argued` at chunk `5395440` offsets `238-244`; context: Other Arguments [34] The Applicant argued that the SST-AD made an error of law by finding that he breached his contractual obligations by not getting vaccinated.
- Evidence: `evidence_fact` cue `evidence` at chunk `5395440` offsets `742-750`; context: A written policy communicated to an employee can be in itself sufficient evidence of an employee’s objective knowledge “that dismissal was a real possibility” of failing to abide by that policy.
- Evidence: `governing_rule` cue `under` at chunk `5395440` offsets `175-180`; context: [33] I find that it was reasonable for the SST-AD to conclude that the Applicant had no reasonable chance of success in arguing that his actions did not constitute misconduct under the EIA framework.
- Evidence: `reasoning_application` cue `I find` at chunk `5395440` offsets `5-11`; context: [33] I find that it was reasonable for the SST-AD to conclude that the Applicant had no reasonable chance of success in arguing that his actions did not constitute misconduct under the EIA framework.
- Evidence: `party_position` cue `submits` at chunk `5395441` offsets `125-132`; context: The Applicant submits that if he had known he was not being paid for those three days he would have been able to claim constructive dismissal on his EI claim.
- Evidence: `counterargument_limitation` cue `but` at chunk `5395441` offsets `356-359`; context: If he wished to pursue constructive dismissal this would be done in a different forum but is not applicable to this EI refusal.
- Evidence: `evidence_fact` cue `found that` at chunk `5395442` offsets `270-280`; context: First, it highlighted Paradis at paras 30-34, where the Federal Court found that wrongful dismissal and other arguments directed at sanctioning employer conduct are “a matter for another forum.
- Evidence: `reasoning_application` cue `conclude` at chunk `5395442` offsets `53-61`; context: [36] Given this, it was reasonable for the SST-AD to conclude that these arguments had no reasonable chance of success on appeal.

#### 29966:2:subtheme:7 · paragraphs 30-31

- Raw key terms: `above, applicant, employment, arguments, chance, claimant, commit, committed`
- Display key terms: `above, employment, arguments, chance, commit, committed`
- Argument roles: `disposition, governing_rule, issue, reasoning_application`
- Explanation: Observed roles: disposition, governing_rule, issue, reasoning_application Display terms: above, employment, arguments, chance, commit, committed Rule/authority context: [37] Further, unlike what the Applicant suggests, the Tribunal is not obligated to focus on contractual language or determine if a claimant was dismissed justifiably under labour law principles when it is considering mis Application context: [38] For all of the above reasons, it was reasonable for the SST-AD to conclude that the Applicant’s arguments relating to his employment contract and constructive dismissal had no reasonable chance of success. Operative outcome context: [37] Further, unlike what the Applicant suggests, the Tribunal is not obligated to focus on contractual language or determine if a claimant was dismissed justifiably under labour law principles when it is considering mis Evidence spans paragraphs 30-31. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5395443` offsets `302-309`; context: Instead, as outlined above, the misconduct test focuses on whether a claimant intentionally committed an act (or failed to commit an act) contrary to their employment obligations.
- Evidence: `governing_rule` cue `under` at chunk `5395443` offsets `166-171`; context: [37] Further, unlike what the Applicant suggests, the Tribunal is not obligated to focus on contractual language or determine if a claimant was dismissed justifiably under labour law principles when it is considering misconduct under the EIA.
- Evidence: `disposition` cue `dismissed` at chunk `5395443` offsets `144-153`; context: [37] Further, unlike what the Applicant suggests, the Tribunal is not obligated to focus on contractual language or determine if a claimant was dismissed justifiably under labour law principles when it is considering misconduct under the EIA.
- Evidence: `reasoning_application` cue `conclude` at chunk `5395444` offsets `71-79`; context: [38] For all of the above reasons, it was reasonable for the SST-AD to conclude that the Applicant’s arguments relating to his employment contract and constructive dismissal had no reasonable chance of success.

#### 29966:2:subtheme:8 · paragraphs 32-34

- Raw key terms: `applicant, arguments, error, legal, without, against, agreed, alarming`
- Display key terms: `arguments, error, legal, without, against, agreed, alarming`
- Argument roles: `governing_rule, issue, party_position, reasoning_application`
- Explanation: Observed roles: governing_rule, issue, party_position, reasoning_application Display terms: arguments, error, legal, without, against, agreed, alarming Position/evidence statements: He argued that all of this make his denial of EI benefits an error. | Procedural Fairness [42] The Applicant submitted that the SST-AD breached his procedural fairness through “short cycling analysis without applying essential legal test principles established in case law to fully satisfy  Rule/authority context: Procedural Fairness [42] The Applicant submitted that the SST-AD breached his procedural fairness through “short cycling analysis without applying essential legal test principles established in case law to fully satisfy  Application context: [40] Further, he had issues with his exemption application because it was vague and a blanket response without saying why he did qualify. Evidence spans paragraphs 32-34. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5395445` offsets `277-284`; context: He stated he did not consent and he has a legal right to exercise whether he is treated medically.
- Evidence: `issue` cue `issues` at chunk `5395446` offsets `21-27`; context: [40] Further, he had issues with his exemption application because it was vague and a blanket response without saying why he did qualify.
- Evidence: `party_position` cue `argued` at chunk `5395446` offsets `416-422`; context: He argued that all of this make his denial of EI benefits an error.
- Evidence: `reasoning_application` cue `because` at chunk `5395446` offsets `59-66`; context: [40] Further, he had issues with his exemption application because it was vague and a blanket response without saying why he did qualify.
- Evidence: `party_position` cue `submitted` at chunk `5395447` offsets `187-196`; context: Procedural Fairness [42] The Applicant submitted that the SST-AD breached his procedural fairness through “short cycling analysis without applying essential legal test principles established in case law to fully satisfy the finding of misconduct”.
- Evidence: `governing_rule` cue `legal test` at chunk `5395447` offsets `305-315`; context: Procedural Fairness [42] The Applicant submitted that the SST-AD breached his procedural fairness through “short cycling analysis without applying essential legal test principles established in case law to fully satisfy the finding of misconduct”.

#### 29966:2:subtheme:9 · paragraphs 35-36

- Raw key terms: `address, applicant, arguments, case, decision-maker, fall, legal, mandate`
- Display key terms: `address, arguments, case, decision-maker, fall, legal, mandate`
- Argument roles: `issue, reasoning_application`
- Explanation: Observed roles: issue, reasoning_application Display terms: address, arguments, case, decision-maker, fall, legal, mandate Application context: [46] [I]t is likely that the Applicant will find this result frustrating, because my reasons do not deal with the fundamental legal, ethical, and factual questions he is raising. Evidence spans paragraphs 35-36. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `issues` at chunk `5395448` offsets `51-57`; context: [43] After reviewing the SST-AD decision, I see no issues of procedural fairness.
- Evidence: `reasoning_application` cue `because` at chunk `5395449` offsets `74-81`; context: [46] [I]t is likely that the Applicant will find this result frustrating, because my reasons do not deal with the fundamental legal, ethical, and factual questions he is raising.

#### 29966:2:subtheme:10 · paragraphs 37-39

- Raw key terms: `applicant, decision, dismissed, employment, neither, sst-gd, acquired, action`
- Display key terms: `dismissed, employment, neither, sst-gd, acquired, action`
- Argument roles: `disposition, issue`
- Explanation: Observed roles: disposition, issue Display terms: dismissed, employment, neither, sst-gd, acquired, action Operative outcome context: In this case, that role involved determining why the Applicant was dismissed from his employment, and whether that reason constituted “misconduct. | Those arguments are not relevant to this determination nor were they arguments that the SST-GD or SST-AD had to consider when deciding why he was dismissed from his employment. Evidence spans paragraphs 37-39. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5395450` offsets `221-228`; context: In this case, that role involved determining why the Applicant was dismissed from his employment, and whether that reason constituted “misconduct.
- Evidence: `disposition` cue `dismissed` at chunk `5395450` offsets `186-195`; context: In this case, that role involved determining why the Applicant was dismissed from his employment, and whether that reason constituted “misconduct.
- Evidence: `disposition` cue `dismissed` at chunk `5395451` offsets `571-580`; context: Those arguments are not relevant to this determination nor were they arguments that the SST-GD or SST-AD had to consider when deciding why he was dismissed from his employment.

#### Section text

III. Issue [12] The sole issue in this application is whether the SST-AD reasonably denied the Applicant leave to appeal the SST-GD’s Decision.
IV. Standard of Review [13] The standard of review to be applied to an SST-AD decision denying leave to appeal is reasonableness: Bhamra v Canada (Attorney General), 2023 FCA 121 [Bhamra] at para 3, citing Cameron v Canada (Attorney General), 2018 FCA 100.

[14] SST-AD will only grant leave in limited situations, and it will not grant leave unless the appellant can demonstrate that the appeal has a reasonable chance of success: Bhamra at para 15, citing 58(2) of the Department of Employment and Social Development Act, SC 2005, c 34 (the “DESDA”). To determine whether the SST-AD’s decision is reasonable, the reviewing court must ask “whether the decision bears the hallmarks of reasonableness – justification, transparency and intelligibility – and whether it is justified in relation to the relevant factual and legal constraints that bear on the decision”: Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 at paras 86 and 99.
V. Analysis A. Preliminary Issue [15] Several of the exhibits in the Applicant’s affidavit are inadmissible. Exhibits 15 to 18 and 22 concern the Applicant’s employer and its policies—some past, some present. The Applicant argued that it was background information and should be allowed. I do not agree.

[16] The general rule is that only the evidentiary record before the administrative decision-maker is admissible on judicial review: see Bernard v Canada (Revenue Agency), 2015 FCA 263 [Bernard] at paras 13-18.

[17] There are three exceptions to the general rule that new evidence is not admissible on judicial review:
(1)evidence that provides general background in circumstances where that information might assist in understanding the issues relevant to the judicial review;
(2)evidence necessary to bring to the attention of the court procedural defects not found in the evidentiary record of the administrative decision-maker; and
(3)evidence to highlight the complete absence of evidence before the administrative decision-maker.
Tsleil-Waututh Nation v Canada (Attorney General), 2018 FCA 153 at paras 97-98

[18] These exhibits do not fit into any of the exceptions to the rule against new evidence, outlined below. This evidence is also irrelevant and immaterial because it is focussed on the effectiveness of the UHN’s policy and behaviour (rather than the EI misconduct test). Exhibits 15-18 and 22 of the Applicant’s affidavit will not be considered.
B. The Law [19] Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed in the subsection.

[20] Pursuant to, section 58 of the DESDA, the SST-AD was empowered to set the SST-GD’s decision aside only if it found the latter to have failed to observe a principle of natural justice, erred in law, or based its decision on an erroneous finding of fact made in a perverse or capricious manner without regard to the material before it: see Cecchetto v. Canada (Attorney General), 2023 FC 102 [Cecchetto] at para 22, citing Cameron v Canada (Attorney General), 2018 FCA 100 [Cameron] at para 2).

[21] To do so, the SST-AD is first required to decide whether to grant the Applicant leave to appeal. Pursuant to subsection 58(2) of the DESDA, leave can only be granted where the claimant satisfies the SST-AD that the proposed appeal has a reasonable chance of success on one of the three grounds listed above: see O’Rourke v Canada (Attorney General), 2019 FCA 60 at para 9; Mishibinijima v Canada (Attorney General), 2007 FCA 36 at para 14. As this Court stated in Osaj v Canada (Attorney General), 2016 FC 115: “having a ‘reasonable chance of success’ in this context means having some arguable ground upon which the proposed appeal might succeed” (see para 12).
C. The SST’s findings of misconduct [22] This case focuses on the concept of misconduct under the EIA framework, which stipulates that a claimant is disqualified from receiving any benefits if the claimant lost any employment because of their misconduct: see section 30. While the term “misconduct” is not defined in the legislation, its definition has been clearly set out in the jurisprudence.

[23] To determine whether the misconduct could result in dismissal, there must be a causal link between the claimant’s misconduct and the claimant’s employment. In other words, the misconduct must constitute a breach of an express or implied duty resulting from the contract of employment: Canada (Attorney General) v Lemire, 2010 FCA 314 [Lemire] at para 14. Further, as the Federal Court of Appeal found in Lemire at para 15 “[misconduct] is not a question of deciding whether or not the dismissal is justified under the meaning of labour law but, rather, of determining, according to an objective assessment of the evidence, whether the misconduct was such that its author could normally foresee that it would be likely to result in his or her dismissal”.

[24] The Applicant submits that it is his belief that the SST-AD misinterpreted the term “misconduct” and consequently, erred in concluding that his refusal to be vaccinated amounted to misconduct under the EIA. The Applicant argues that his decision not to get vaccinated for COVID is not voluntary misconduct, but rather, an “unavoidable consequence of employer’s intimidating tactics”. I disagree.

[25] The Federal Court of Appeal, in Nelson v Canada (Attorney General), 2019 FCA 222 [Nelson], is clear that “there will be misconduct where the claimant knew or ought to have known that his conduct was such as to impair the performance of the duties owed to his employer and that, as a result, dismissal was a real possibility”: see para 21; see Bellavance at para 9). Here, as in Nelson, the Applicant was aware of the policy and made a deliberate voluntary choice not to follow the policy, even after being notified that his exemption was denied and without the COVID vaccine his employment would be terminated.

[26] Given this, it was reasonable for the SST-AD to uphold the SST-GD’s findings that the Applicant’s deliberate voluntary decision not to get vaccinated constituted a breach of express duty set out in the Policy. While this Policy is not explicitly in his employment contract, it is a workplace safety policy that the employer imposed to protect the health and safety of all of its employees. Given this, the Policy imposes obligations on all of its employees. The SST-GD also found that the Applicant had been informed of the employer’s Policy and was given time to comply. The policy provided for exemptions for religious or medical reasons. The Applicant applied for an exemption; it was not granted to him.

[27] Even though it is clear that the Applicant disagrees with the UHN that this policy protected his health and safety, the only relevant question before the SST-GD was whether the Applicant knew that his voluntary decision not to get vaccinated might result in his termination. Given this, it was reasonable for the SST-AD to uphold the SST-GD’s findings that the Applicant knew about the Policy, as well as the consequences for not following it.

[28] The SST-AD found the SST-GD did not commit a reviewable error when it decided the issue of misconduct. At paragraph 36 of the SST-AD Decision it held that the Applicant failed to identify any errors of law or any erroneous findings of fact and did not identify any procedural fairness issues. Given the Applicant’s failure to find a reviewable error, the SST-AD denied leave to appeal because the appeal had no reasonable chance of success.

[29] Although the Applicant submitted that the SST-GD erred in determining that the Policy was part of his contract of employment and that he breached his contract by not getting vaccinated, the SST-AD found that i) an employer has an obligation to take all reasonable precautions to protect the health and safety of its employees in their workplace, and ii) such precautions include mandatory vaccination policies, imposed by the province.

[30] The Applicant argued that his letter of employment was not an employment contract and it did not have within it that he must receive a COVID vaccine so how could he be fired for not doing it. When this is unpacked, his employment letter did in fact list a number of immunization records that he must prove he has in order to be employed. COVID was unknown at the time of his letter and is now included as one of many immunizations that must be proven to be employed by the health care institute in question. The letter of employment would be subject to policies implemented over time and the Applicant was informed of those policy changes which would add to his terms of employment.

[31] Justice Pentney recently released a highly analogous decision, where he found that an employee who is terminated for misconduct because they refused to get a COVID vaccine, contrary to an employer’s vaccination policy, is not entitled to receive EI benefits: see Cecchetto.

[32] Like in Cecchetto, this Applicant was aware of the consequences of non-compliance with the Policy in light of the multiple communications from the UHN explaining as such. The Applicant also had the opportunity to remedy his situation on multiple occasions. The Applicant was aware that his request for an exemption was denied. His voluntary decision not to comply with the Policy constituted voluntary misconduct in this context.

[33] I find that it was reasonable for the SST-AD to conclude that the Applicant had no reasonable chance of success in arguing that his actions did not constitute misconduct under the EIA framework.
D. Other Arguments [34] The Applicant argued that the SST-AD made an error of law by finding that he breached his contractual obligations by not getting vaccinated. As I noted above, the SST-AD reasonably found no basis to intervene from the Applicant’s arguments about his employment contract. As the Federal Court of Appeal held in Nelson, an employer’s written policy does not need to exist in the original employment contract to ground misconduct: see paras 22-26. A written policy communicated to an employee can be in itself sufficient evidence of an employee’s objective knowledge “that dismissal was a real possibility” of failing to abide by that policy. The Applicant’s contract and offer letter do not comprise the complete terms, express or implied, of his employment at UHN. It is well accepted in labour law that employees have obligations to abide by the health and safety policies that are implemented by their employers over time.

[35] The Applicant indicated that after his termination he found out he was not paid for three days he worked. The Applicant submits that if he had known he was not being paid for those three days he would have been able to claim constructive dismissal on his EI claim. If he wished to pursue constructive dismissal this would be done in a different forum but is not applicable to this EI refusal.

[36] Given this, it was reasonable for the SST-AD to conclude that these arguments had no reasonable chance of success on appeal. The SST-AD cited two cases to support its conclusions in this regard. First, it highlighted Paradis at paras 30-34, where the Federal Court found that wrongful dismissal and other arguments directed at sanctioning employer conduct are “a matter for another forum.” The Tribunal also highlighted the Mishibinijima case in which the Federal Court of Appeal found that an employer’s duty to accommodate is irrelevant to deciding EI misconduct.

[37] Further, unlike what the Applicant suggests, the Tribunal is not obligated to focus on contractual language or determine if a claimant was dismissed justifiably under labour law principles when it is considering misconduct under the EIA. Instead, as outlined above, the misconduct test focuses on whether a claimant intentionally committed an act (or failed to commit an act) contrary to their employment obligations.

[38] For all of the above reasons, it was reasonable for the SST-AD to conclude that the Applicant’s arguments relating to his employment contract and constructive dismissal had no reasonable chance of success.

[39] Another of the Applicant’s arguments was that the policy’s objective was to force him to take medical treatment against his will. He said this was unilateral and “my way or the highway” which was an error. He stated he did not consent and he has a legal right to exercise whether he is treated medically. The Applicant said it was alarming that the policy went from voluntary to mandatory with no alternative and the objective of the policy forced him to take medical treatment. This argument is again related to whether he agreed or not with the policy and not whether he was entitled to EI.

[40] Further, he had issues with his exemption application because it was vague and a blanket response without saying why he did qualify. At his exit interview, when he wanted to know why he was not exempt, the only answer was of the hypothetical that it was possible he would be called in to the hospital so he needed the vaccine. He said no one really explored why he could not use testing if he was called in. He argued that all of this make his denial of EI benefits an error.

[41] Again, while these last two arguments may be labour law arguments for a different forum this does not impact the finding of his misconduct.
E. Procedural Fairness [42] The Applicant submitted that the SST-AD breached his procedural fairness through “short cycling analysis without applying essential legal test principles established in case law to fully satisfy the finding of misconduct”.

[43] After reviewing the SST-AD decision, I see no issues of procedural fairness. I agree with the SST-AD that the Applicant has not identified any reviewable errors such as jurisdiction or any failure by the General Division to observe a principle of natural justice: see AD Decision, at para 36.
F. Relevance [44] The SST-AD and SST-GD, in this case, have taken the time to respond to many of the Applicant’s arguments – many of which that were not relevant to the application before them. It is not unreasonable for a decision-maker not to address legal arguments when they fall outside the scope of its legal mandate. As Justice Pentney concluded in Cecchetto:

[46] [I]t is likely that the Applicant will find this result frustrating, because my reasons do not deal with the fundamental legal, ethical, and factual questions he is raising. That is because many of these questions are simply beyond the scope of this case. It is not unreasonable for a decision-maker to fail to address legal arguments that fall outside the scope of its legal mandate. [emphasis added]

[47] The SST-GD, and the Appeal Division, have an important, but narrow and specific role to play in the legal system. In this case, that role involved determining why the Applicant was dismissed from his employment, and whether that reason constituted “misconduct.” That is exactly what they did, and the Applicant has not put forward any legal or factual argument that persuades me that the Appeal Division’s decision is unreasonable.

[45] Neither will I address some of the Applicant’s submissions which as Justice Pentney concluded may be frustrating for the Applicant. I will not address the Applicant’s arguments regarding a number of both Federal and Provincial health and hospital acts which relate to his arguments against the mandatory vaccine policy. Neither will I address his arguments that acquired natural immunity had not been considered either. Those arguments are not relevant to this determination nor were they arguments that the SST-GD or SST-AD had to consider when deciding why he was dismissed from his employment. Nor will I make any determinations regarding his alleged participation in a Class Action as those arguments are also beyond the scope of the decision being judicially reviewed.

[46] Neither party sought costs and none are awarded.


## 29966:3 · paragraphs 40-41

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `9bb185bd4d0b0d598057577c4c5e48914ae665c1e48c0c3766e3536d0ca50588`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 29966:3:subtheme:1 · paragraphs 40-41

- Raw key terms: `application, appeal, applicant, chance, conclusion, considered, costs, denying`
- Display key terms: `chance, conclusion, considered, costs, denying`
- Argument roles: `disposition, governing_rule, issue`
- Explanation: Observed roles: disposition, governing_rule, issue Display terms: chance, conclusion, considered, costs, denying Rule/authority context: In denying leave to appeal, the SST-AD reasonably considered whether the Applicant raised any of the reviewable errors listed in subsection 58(1) of the DESDA and whether the appeal ultimately had a reasonable chance of  Operative outcome context: [48] For these reasons, this application should be dismissed without costs. Evidence spans paragraphs 40-41. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `issue` cue `whether` at chunk `5395452` offsets `252-259`; context: In denying leave to appeal, the SST-AD reasonably considered whether the Applicant raised any of the reviewable errors listed in subsection 58(1) of the DESDA and whether the appeal ultimately had a reasonable chance of success, as it was required to do under subsection 58(2) of the DESDA.
- Evidence: `governing_rule` cue `under` at chunk `5395452` offsets `445-450`; context: In denying leave to appeal, the SST-AD reasonably considered whether the Applicant raised any of the reviewable errors listed in subsection 58(1) of the DESDA and whether the appeal ultimately had a reasonable chance of success, as it was required to do under subsection 58(2) of the DESDA.
- Evidence: `disposition` cue `dismissed` at chunk `5395453` offsets `51-60`; context: [48] For these reasons, this application should be dismissed without costs.

#### Section text

VI. Conclusion [47] I am not persuaded that the SST-AD made any errors that would justify granting this application for judicial review. In denying leave to appeal, the SST-AD reasonably considered whether the Applicant raised any of the reviewable errors listed in subsection 58(1) of the DESDA and whether the appeal ultimately had a reasonable chance of success, as it was required to do under subsection 58(2) of the DESDA.

[48] For these reasons, this application should be dismissed without costs.


## 29966:4 · paragraphs 42-43

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `115499f42996fbd291518894c31ff80def7a825bf234ad35d6c8a8c86eb3fcf4`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 29966:4:subtheme:1 · paragraphs 42-43

- Raw key terms: `t-186-23, application, attorney, awarded, canada, cause, costs, court`
- Display key terms: `t-186-23, awarded, costs`
- Argument roles: `disposition`
- Explanation: Observed roles: disposition Display terms: t-186-23, awarded, costs Operative outcome context: JUDGMENT in T-186-23 THIS COURT’S JUDGMENT is that: The application is dismissed. Evidence spans paragraphs 42-43. This is a deterministic evidence summary, not a legal conclusion.
- Evidence: `disposition` cue `dismissed` at chunk `5395453` offsets `147-156`; context: JUDGMENT in T-186-23
THIS COURT’S JUDGMENT is that:
The application is dismissed.

#### Section text

JUDGMENT in T-186-23
THIS COURT’S JUDGMENT is that:
The application is dismissed.
No costs are awarded.
"Glennys L. McVeigh"
Judge
FEDERAL COURT

SOLICITORS OF RECORD
DOCKET:
T-186-23
STYLE OF CAUSE:
WIESLAW KUK v ATTORNEY GENERAL OF CANADA
PLACE OF HEARING:
Toronto, Ontario
DATE OF HEARING:
July 4, 2023


## 29966:5 · paragraphs 44-44

- Citations: `{}`
- Statutes: `{}`
- Tags: `{}`
- Source hash: `63cff0a3ecc21040a31e068e43eac1c415cceb54fe9f1d729a4e18ae29c85540`

### Deterministic evidence spans

These are finer rule-based clusters inside the broader deterministic unit. Their explanations describe detected cues and roles; they are not model-generated conclusions.

#### 29966:5:subtheme:1 · paragraphs 44-44

- Raw key terms: `appearances, applicant, attorney, august, behalf, canada, dated, fine`
- Display key terms: `august, behalf, dated, fine`
- Argument roles: `none`
- Explanation: Observed roles: no explicit argument role cue Display terms: august, behalf, dated, fine No explicit argument evidence was detected in this span; review it as metadata or cue-free text Evidence spans paragraphs 44-44. This is a deterministic evidence summary, not a legal conclusion.

#### Section text

JUDGMENT AND REASONS:
MCVEIGH J.
DATED:
August 23, 2023
APPEARANCES:
Weislaw Kuk
For The Applicant (ON HIS OWN BEHALF)
Jordan Fine
For The Respondent
SOLICITORS OF RECORD:
Attorney General of Canada Gatineau, Quebec
For The Respondent
