# Treatment Distillation Review: mason-single-review-20260923

> Status: **human review required**. This packet is provisional and cannot publish runtime behavior.

## How To Review

For each item, answer one question: **Does the evidence phrase correctly describe how the judge treats the cited authority?**

- `supportive`: the judge relies on, agrees with, or applies the authority.
- `distinguishing`: the judge says the authority is different, limited, or does not control.
- `negative`: the judge rejects or criticizes the authority.
- `neutral`: the authority is discussed without a clear positive or negative treatment.
- `absent`: the citation appears, but there is no treatment of it in the evidence.
- `ambiguous`: the wording is too unclear to decide.

Reply with item IDs using `approve`, `reject`, or `unclear`, plus a short reason. Example: `citation-context-1018: reject - this is the court's merits reasoning, not treatment of the cited case.`

- Review the treatment against the full evidence text, not the citation alone.
- Use the decision context to check what the judge says before and after the citation.
- Confirm the phrase expresses treatment or judicial reasoning about the cited authority.
- Reject generic nouns, citation text, party-only assertions, or unsupported conclusions.
- Record approve, reject, or needs_context in review_decision and explain uncertainty in review_notes.

## Summary

- Rules: **24** pending review
- Treatment distribution: `{"neutral": 9, "supportive": 15}`
- Rules with repaired spans: **24**
- Rules with one evidence item: **21**
- Priority labels requiring direct review: **31**
- Priority treatment distribution: `{"absent": 4, "neutral": 10, "supportive": 17}`
- Full source artifact: `data\eval\llm_discussion_units_pilot\mason_argument_citation_single_distillation.json`

## Review Queue

## Priority Labels: Start Here

Review these first 10 items. The JSON packet contains all 31 priority labels.

- `mason-argument-citation-001`; proposed **supportive**; confidence **0.99**; citation: `Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653`
  - Proposed evidence: `apply the framework for judicial review developed in Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653`
  - Decision context: `[1] These appeals require the Court to apply the framework for judicial review developed in Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653, to two administrative decisions involving a question of statutory interpretation in the immigration context.
[2] The statutory provision at issue, s. 34(1) (e) of the Immigration and Refugee Protection Act , S.C. 2001, c. 27 (“IRPA ”), provides that permanent residents and foreign nationals are inadmissible to Canada on “security grounds” for “engaging in acts of violence that would or might endanger the lives or safety of persons in Canada”. The key point of disagreement among the administrative decision makers and courts below is whether the “acts of violence” listed as “security grounds” in s. 34(1)(e) require a link to national security or the security of Canada, or whether s. 34(1)(e) applies to acts of violence more broadly even without such a link.
[3] Both administrative decisions under review interpreted s. 34(1)(e) as not requiring the acts of violence to have a link to national security or the security of Canada. In the first administrative decision, the Immigration Appeal Division (“IAD”) of the Immigration and Refugee Board of Canada (“IRB”) ruled that Mr. Earl Mason, a foreign national, could be found inadmissible under s. 34(1)(e) if his alleged violent conduct wer`
  - Offsets repaired: `True`; source hash: `cd68903baf5313e2e9db03e1c709cdd1ec6a7cf79073d281de91fab59ae2c9ee`

- `mason-argument-citation-009`; proposed **neutral**; confidence **0.95**; citation: `2018 CanLII 57522`
  - Proposed evidence: `A. Immigration Division Decision (Mr. Mason), 2018 CanLII 57522`
  - Decision context: `g in Canada, Mr. Dleiow had engaged in acts of violence against intimate partners and other persons. Criminal charges flowing from these incidents were stayed, except for 3 charges: being unlawfully in a dwelling house with intent to commit an indictable offence, mischief under $5,000, and uttering threats to cause death or bodily harm. Mr. Dleiow pleaded guilty to these charges and received a conditional discharge. A delegate of the Minister of Public Safety and Emergency Preparedness then referred the CBSA’s inadmissibility report to the ID for an admissibility hearing.
III. Decisions Below
A. Immigration Division Decision (Mr. Mason), 2018 CanLII 57522
[19] The ID addressed a preliminary question of law as to whether Mr. Mason’s alleged conduct, if proven, could be a ground of inadmissibility under s. 34(1)(e). The ID ruled that a “security groun[d]” under s. 34(1) means a threat to the security of Canada or another country, and that the act of violence in question must have some connection to a threat to the security of Canada. In the ID’s view, Mr. Mason’s alleged conduct involved “mere criminal offences”, which “although very serious”, lacked “any element that would elevate them to security grounds”, and thus s. 34(1)(e) could not apply (para. 24).
B. Immigration Appeal Division Decision (Mr. Mason), 2019 CanLII 55171
[20] The Minister of Public Safety and Emergency Preparedness appealed the ID’s decision in Mr. Mason’s case to the IAD, which allowed the Minister’s appeal, set aside the ID’s decision, and referred the matter back for a full hearing on the merits. The IAD concluded that inadmissibility under s. 34(1)(e) does not require a link to national security or the security of Canada. In the IAD’s view, “security” under s. 34(1)(e) relates to “security in a broader sense”, namely, to ensure “that individual Canadians are`
  - Offsets repaired: `True`; source hash: `5a56af3efd045986ecf0d358a8cebdd49f1636e4b1b2fd7724b57365d5fd6286`

- `mason-argument-citation-010`; proposed **neutral**; confidence **0.95**; citation: `2019 CanLII 55171`
  - Proposed evidence: `The IAD concluded that inadmissibility under s. 34(1)(e) does not require a link to national security or the security of Canada.`
  - Decision context: `r Mr. Mason’s alleged conduct, if proven, could be a ground of inadmissibility under s. 34(1)(e). The ID ruled that a “security groun[d]” under s. 34(1) means a threat to the security of Canada or another country, and that the act of violence in question must have some connection to a threat to the security of Canada. In the ID’s view, Mr. Mason’s alleged conduct involved “mere criminal offences”, which “although very serious”, lacked “any element that would elevate them to security grounds”, and thus s. 34(1)(e) could not apply (para. 24).
B. Immigration Appeal Division Decision (Mr. Mason), 2019 CanLII 55171
[20] The Minister of Public Safety and Emergency Preparedness appealed the ID’s decision in Mr. Mason’s case to the IAD, which allowed the Minister’s appeal, set aside the ID’s decision, and referred the matter back for a full hearing on the merits. The IAD concluded that inadmissibility under s. 34(1)(e) does not require a link to national security or the security of Canada. In the IAD’s view, “security” under s. 34(1)(e) relates to “security in a broader sense”, namely, to ensure “that individual Canadians are secure from acts of violence that would or might endanger their lives or safety” (para. 37).
C. Immigration Division Decision (Mr. Dleiow), 2019 CanLII 129531
[21] In Mr. Dleiow’s case, the ID saw no basis to depart from the IAD’s interpretation of s. 34(1)(e) in Mr. Mason’s case, and therefore affirmed that s. 34(1)(e) does not require a link to national security or the security of Canada. The ID also heard evidence and concluded that Mr. Dleiow was inadmissible because he had engaged in violent acts against two intimate partners, which there were reasonable grounds to believe had endangered their safety. The ID based this conclusion on a guilty plea for acts relating to one intimate partner, and on testimony and police occurrence reports relating to the other intimate partner. As a result, the ID ruled that Mr. Dleiow was inadmissible and issued a deportation order.
D. Federal Court Decision (Mr. Mason), 2019 FC 1251, [2020] 2 F.C.R. 3 (Grammond J.)`
  - Offsets repaired: `True`; source hash: `504fb7c73df4cc70c6a14846e4c94ece608d29d3e373edd13ed62b078879cb50`

- `mason-argument-citation-013`; proposed **neutral**; confidence **0.95**; citation: `Vavilov`
  - Proposed evidence: `outlined how a reviewing court should evaluate the reasonableness of an administrative decision maker’s interpretation of a statute`
  - Decision context: `and issued a deportation order.
D. Federal Court Decision (Mr. Mason), 2019 FC 1251, [2020] 2 F.C.R. 3 (Grammond J.)
[22] The Federal Court granted Mr. Mason’s application for judicial review of the IAD’s decision. The court held that the IAD’s interpretation of s. 34(1) (e) of the IRPA was unreasonable because it disregarded the structure of the Act and rendered meaningless statutory provisions for inadmissibility based on criminality. In the Federal Court’s view, s. 34(1)(e) requires a link to national security.
[23] The Federal Court — whose reasons were released before this Court released Vavilov — outlined how a reviewing court should evaluate the reasonableness of an administrative decision maker’s interpretation of a statute. In the Federal Court’s view, a reviewing court must ensure that an administrative decision maker did not overlook a very strong argument — a “knock-out punch”, that is, an interpretation that is internally consistent, withstands scrutiny, and is not met by a countervailing interpretation of similar force — or choose an interpretation when the interpretive “clues” point overwhelmingly in the other direction.
[24] The Federal Court ruled that the IAD’s interpretation of s. 34(1)(e) was unreasonable because it conflicted with the broader structure of the IRPA , thus undermining Parliament’s intent. In the court’s view, this structural argument was a “knock-out punch”. The IAD’s decision upset the carefully crafted structure of the IRPA by including under s. 34(1)(e) a vast range of conduct that “would or might endanger the lives or safety of persons in Canada”. This would thwart Parliament’s intent by bringing under the most serious category of inadmissibility conduct falling below the thresholds for less serious categories of inadmissibility, and it would discard Parliament’s choice under s. 36 of the IRPA to require a conviction when criminal conduct was committed in Canada. Secti`
  - Offsets repaired: `True`; source hash: `d1575850909b309588a707c64d4925531ab92990ce6a04d0e30a328ab4a11fac`

- `mason-argument-citation-016`; proposed **neutral**; confidence **0.95**; citation: `Vavilov`
  - Proposed evidence: `Vavilov tells us much but it leaves some things unclear`
  - Decision context: `lication for judicial review of the ID’s decision. The court applied the Federal Court’s reasoning in Mr. Mason’s case for reasons of comity, set aside the ID’s decision and ordered the matter be reconsidered on the merits by a different decision maker. The court also certified the same serious question of general importance.
F. Federal Court of Appeal (Mr. Mason and Mr. Dleiow), 2021 FCA 156, [2022] 1 F.C.R. 3 (Stratas J.A., Rennie and Mactavish JJ.A. concurring)
[28] The Federal Court of Appeal decided the appeals in Mr. Mason’s and Mr. Dleiow’s cases together, after this Court had released Vavilov. The court held that the administrative decisions reasonably interpreted s. 34(1)(e) as not requiring a nexus with national security or the security of Canada.
[29] The Court of Appeal began by discussing how a court should conduct reasonableness review. The court said that “Vavilov tells us much but it leaves some things unclear” (para. 9). The court cautioned that a reviewing court should not fashion its own yardstick and use it to measure what the administrator did, but should instead conduct “a preliminary analysis of the text, context and purpose of the legislation just to understand the lay of the land before they examine the administrators’ reasons” (para. 17). The Court of Appeal also criticized the Federal Court’s “knock-out punch” approach in Mr. Mason’s case as involving disguised correctness review.
[30] The Court of Appeal concluded that the IAD was alive to the essential elements of s. 34(1)(e)’s text, context, and purpose, and saw no omitted aspects that would cause a loss of confidence in the outcome. It rejected Mr. Mason’s argument that reading s. 34(1)(e) without a nexus to national security is inconsistent with the broader statutory context. The court ruled that the IAD reasonably concluded that the conduct captured by s. 34(1)(e), which speaks of the danger posed to the “lives or safety” of persons in Canada, is only a small subset of what would be considered serious criminality under s. 36 of the IRPA . Sections 34 and 36 address two different matters — conduct and convictions, respec`
  - Offsets repaired: `True`; source hash: `e2d854ae68cb221e855db59ef17795f5a3abef57b2622e9d897a15ea7317a818`

- `mason-argument-citation-017`; proposed **neutral**; confidence **0.95**; citation: `Vavilov`
  - Proposed evidence: `Vavilov tells us much but it leaves some things unclear`
  - Decision context: `ame serious question of general importance.
F. Federal Court of Appeal (Mr. Mason and Mr. Dleiow), 2021 FCA 156, [2022] 1 F.C.R. 3 (Stratas J.A., Rennie and Mactavish JJ.A. concurring)
[28] The Federal Court of Appeal decided the appeals in Mr. Mason’s and Mr. Dleiow’s cases together, after this Court had released Vavilov. The court held that the administrative decisions reasonably interpreted s. 34(1)(e) as not requiring a nexus with national security or the security of Canada.
[29] The Court of Appeal began by discussing how a court should conduct reasonableness review. The court said that “Vavilov tells us much but it leaves some things unclear” (para. 9). The court cautioned that a reviewing court should not fashion its own yardstick and use it to measure what the administrator did, but should instead conduct “a preliminary analysis of the text, context and purpose of the legislation just to understand the lay of the land before they examine the administrators’ reasons” (para. 17). The Court of Appeal also criticized the Federal Court’s “knock-out punch” approach in Mr. Mason’s case as involving disguised correctness review.
[30] The Court of Appeal concluded that the IAD was alive to the essential elements of s. 34(1)(e)’s text, context, and purpose, and saw no omitted aspects that would cause a loss of confidence in the outcome. It rejected Mr. Mason’s argument that reading s. 34(1)(e) without a nexus to national security is inconsistent with the broader statutory context. The court ruled that the IAD reasonably concluded that the conduct captured by s. 34(1)(e), which speaks of the danger posed to the “lives or safety” of persons in Canada, is only a small subset of what would be considered serious criminality under s. 36 of the IRPA . Sections 34 and 36 address two different matters — conduct and convictions, respec`
  - Offsets repaired: `True`; source hash: `6bd97b7867d0da49dca1d4ac000f263c0946e3b88833ad93423a6598e9412f30`

- `mason-argument-citation-037`; proposed **supportive**; confidence **0.95**; citation: `Vavilov`
  - Proposed evidence: `By being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer`
  - Decision context: `ion maker may draw on its institutional expertise and experience and rely on considerations that a court would not have thought to employ, but which “enrich and elevate the interpretive exercise” (paras. 93 and 119; Canada Post, at para. 43). As Professor Audrey Macklin explains, courts should be “genuinely receptive to input beyond the usual techniques that courts use to discern text, context and purpose. These may include operational implications, alignment with broader statutory mandate, and so on” (“Seven Out of Nine Legal Experts Agree: Expertise No Longer Matters (in the Same Way) After Vavilov!” (2021), 100 S.C.L.R. (2d) 249, at p. 261). By being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer (Vavilov, at para. 108). Reasonableness review demands both that administrative decision makers demonstrate their expertise through their reasons and that judges pay “[r]espectful attention” to the ways in which their reasons reflect that expertise (para. 93; P. Daly, “Vavilov and the Culture of Justification in Contemporary Administrative Law” (2021), 100 S.C.L.R. (2d) 279, at pp. 285‑86).
[71] Finally, a court may conclude during a reasonableness review that “the interplay of text, context and purpose leaves room for a single reasonable interpretation of the statutory provision, or aspect of the statutory provision” (Vavilov, at para. 124, citing Dunsmuir, at paras. 72‑76, and Nova Tube Inc./Nova Steel Inc. v. Conares Metal Supply Ltd., 2019 FCA 52). In such a case, although a court should “generally pause before definitively pronouncing upon the interpretation” of a statutory provision, the court may conclude that remitting the question to the administrative decision maker may serve no useful purpose (Vavilov, at para. 124). It must be stressed that the possibility of a single reasonable interpretation is not a starting point of reasonableness review, as this would be contrary `
  - Offsets repaired: `True`; source hash: `539897eed2517b049231165f054bd3b5616fea6327b2117811f12211b52029a3`

- `mason-argument-citation-038`; proposed **supportive**; confidence **0.95**; citation: `(Vavilov, at para. 108)`
  - Proposed evidence: `By being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer`
  - Decision context: ` experience and rely on considerations that a court would not have thought to employ, but which “enrich and elevate the interpretive exercise” (paras. 93 and 119; Canada Post, at para. 43). As Professor Audrey Macklin explains, courts should be “genuinely receptive to input beyond the usual techniques that courts use to discern text, context and purpose. These may include operational implications, alignment with broader statutory mandate, and so on” (“Seven Out of Nine Legal Experts Agree: Expertise No Longer Matters (in the Same Way) After Vavilov!” (2021), 100 S.C.L.R. (2d) 249, at p. 261). By being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer (Vavilov, at para. 108). Reasonableness review demands both that administrative decision makers demonstrate their expertise through their reasons and that judges pay “[r]espectful attention” to the ways in which their reasons reflect that expertise (para. 93; P. Daly, “Vavilov and the Culture of Justification in Contemporary Administrative Law” (2021), 100 S.C.L.R. (2d) 279, at pp. 285‑86).
[71] Finally, a court may conclude during a reasonableness review that “the interplay of text, context and purpose leaves room for a single reasonable interpretation of the statutory provision, or aspect of the statutory provision” (Vavilov, at para. 124, citing Dunsmuir, at paras. 72‑76, and Nova Tube Inc./Nova Steel Inc. v. Conares Metal Supply Ltd., 2019 FCA 52). In such a case, although a court should “generally pause before definitively pronouncing upon the interpretation” of a statutory provision, the court may conclude that remitting the question to the administrative decision maker may serve no useful purpose (Vavilov, at para. 124). It must be stressed that the possibility of a single reasonable interpretation is not a starting point of reasonableness review, as this would be contrary to a “reasons first” app`
  - Offsets repaired: `True`; source hash: `539897eed2517b049231165f054bd3b5616fea6327b2117811f12211b52029a3`

- `mason-argument-citation-045`; proposed **neutral**; confidence **0.90**; citation: `authority`
  - Proposed evidence: `may operate as legal constraints on an administrative decision maker`
  - Decision context: `y conclude that remitting the question to the administrative decision maker may serve no useful purpose (Vavilov, at para. 124). It must be stressed that the possibility of a single reasonable interpretation is not a starting point of reasonableness review, as this would be contrary to a “reasons first” approach. Rather, it is a conclusion that a reviewing court may draw as a result of a proper reasonableness review, as part of the court’s consideration of the appropriate remedy.
3. Relevant Statutory Law, Common Law, and International Law
[72] Statutory law, common law, and international law may operate as legal constraints on an administrative decision maker (paras. 111 and 114). An administrative decision will be unreasonable if it fails to justify a departure from binding precedents (para. 112). International law can also operate as an important constraint, arising from the presumption that legislation is presumed to operate in conformity with Canada’s international obligations and the values and principles of customary and conventional international law, or by informing whether a decision was a reasonable exercise of administrative authority (para. 114).
4. The Evidence and Facts Before the Decision Maker
[73] Absent exceptional circumstances, a reviewing court will defer to an administrative decision maker’s factual findings (para. 125). A reviewing court may intervene, however, if the decision is unreasonable: if it is not “justified in light of the facts” or when “the decision maker has fundamentally misapprehended or failed to account for the evidence before it” (para. 126).
5. The Submissions of the Parties
[74] An administrative decision maker’s reasons must “meaningfully account for the central issues and concerns raised by the parties” (para. 127). Reasons must be “responsive” to the parties’ submissions, because reasons are the “primary mechanism by which decision makers demonstrate that they have actually listened to the parties” (para. 127 (emphasis in original)). Although an administrative decision does not have to “respond to every argument or line of possible analysis” raised by the parties, “a decision maker’s failure to meaningfully grapple with key issues or central arguments raised by the parties may call into question whether the decision maker was actually alert and sensitive to the matter before i`
  - Offsets repaired: `True`; source hash: `04c5bd74789a21a9c8885d492a330bacc791b6fbe843b33bd5f00865b1ccf188`

- `mason-argument-citation-046`; proposed **absent**; confidence **1.00**; citation: `authority`
  - Proposed evidence: ``
  - Decision context: `[73] Absent exceptional circumstances, a reviewing court will defer to an administrative decision maker’s factual findings (para. 125). A reviewing court may intervene, however, if the decision is unreasonable: if it is not “justified in light of the facts” or when “the decision maker has fundamentally misapprehended or failed to account for the evidence before it” (para. 126).
5. The Submissions of the Parties
[74] An administrative decision maker’s reasons must “meaningfully account for the central issues and concerns raised by the parties” (para. 127). Reasons must be “responsive” to the parties’ submissions, because reasons are the “primary mechanism by which decision makers demonstrate that they have actually listened to the parties” (para. 127 (emphasis in original)). Although an administrative decision does not have to “respond to every argument or line of possible analysis” raised by the parties, “a decision maker’s failure to meaningfully grapple with key issues or central arguments raised by the parties may call into question whether the decision maker was actually alert and sensitive to the matter before it” (para. 128).
6. The Past Practices and Decisions of the Administrative Body
[75] Administrative decision makers should be concerned with the general consistency of their decisions, even if they are not bound by their prior decisions in the same way that courts are bound by stare decisis (para. 129). A decision will be unreasonable if the reasons fail to meet the “justificatory burden” for departing from “longstanding practices or established internal authority” (para. 131).
7. The Potential Impact of the Decision on the Affected Individual
[76] Vavilov also explained that “[w]here the impact of a decision on an individual’s rights and interests is severe, the reasons provided to that individual must reflect the stakes” (para. 133). The principle of “responsive justification” means that if a decision has “particularly harsh consequences for the affected individual”, then “the decision maker must explain why its decision best reflects the legislature’s intention” (para. 133). An administrative decision may be unreasonable if it fails to grapple with particularly severe or harsh consequences for the affected individual (para. 134). An administrative decision maker’s reasons must “demonstrate that they have considered the consequences of a decision and that those consequences are justified in light of the facts and law” (para. 135).
[77] Having set out Vavilov’s guidance on conducting reasonableness review, I now comment briefly on the approach to reasonableness review of the courts below.
(2) Methodology of Reasonableness Review in the Courts Below`
  - Offsets repaired: `False`; source hash: `bbe54eff1c90460e6911c92df413724d660859d37e30b22e21fef28c83a83093`

## Remaining Review Material

After the starting batch, continue with the remaining priority labels and then the repeated-rule queue below.

## Repeated-Rule Queue

### 1. `teacher-phrase-neutral-0001`

- Proposed treatment: **neutral**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `a. immigration division decision (mr. mason), 2018 canlii 57522`

Evidence:
- `mason-argument-citation-009`; citation: `2018 CanLII 57522`; hash: `5a56af3efd045986ecf0d358a8cebdd49f1636e4b1b2fd7724b57365d5fd6286`
  - Proposed evidence: `A. Immigration Division Decision (Mr. Mason), 2018 CanLII 57522`
  - Decision context: `g in Canada, Mr. Dleiow had engaged in acts of violence against intimate partners and other persons. Criminal charges flowing from these incidents were stayed, except for 3 charges: being unlawfully in a dwelling house with intent to commit an indictable offence, mischief under $5,000, and uttering threats to cause death or bodily harm. Mr. Dleiow pleaded guilty to these charges and received a conditional discharge. A delegate of the Minister of Public Safety and Emergency Preparedness then referred the CBSA’s inadmissibility report to the ID for an admissibility hearing.
III. Decisions Below
A. Immigration Division Decision (Mr. Mason), 2018 CanLII 57522
[19] The ID addressed a preliminary question of law as to whether Mr. Mason’s alleged conduct, if proven, could be a ground of inadmissibility under s. 34(1)(e). The ID ruled that a “security groun[d]” under s. 34(1) means a threat to the security of Canada or another country, and that the act of violence in question must have some connection to a threat to the security of Canada. In the ID’s view, Mr. Mason’s alleged conduct involved “mere criminal offences”, which “although very serious”, lacked “any element that would elevate them to security grounds”, and thus s. 34(1)(e) could not apply (para. 24).
B. Immigration Appeal Division Decision (Mr. Mason), 2019 CanLII 55171
[20] The Minister of Public Safety and Emergency Preparedness appealed the ID’s decision in Mr. Mason’s case to the IAD, which allowed the Minister’s appeal, set aside the ID’s decision, and referred the matter back for a full hearing on the merits. The IAD concluded that inadmissibility under s. 34(1)(e) does not require a link to national security or the security of Canada. In the IAD’s view, “security” under s. 34(1)(e) relates to “security in a broader sense”, namely, to ensure “that individual Canadians are`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 2. `teacher-phrase-neutral-0002`

- Proposed treatment: **neutral**
- Support: **1** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `in kanthasamy, the majority of this court arguably did the same.`

Evidence:
- `mason-argument-citation-080`; citation: `Kanthasamy v. Canada (Citizenship and Immigration), 2014 FCA 113, [2015] 1 F.C.R. 335, at para. 33`; hash: `34ef2710502ba1bbd00d386a7b9fe2fb746a747f75a0deadbbb4dcab76a49717`
  - Proposed evidence: `In Kanthasamy, the majority of this Court arguably did the same.`
  - Decision context: `t, this Court did not endorse or even cite Kanthasamy in Vavilov. It relied on Baker in Vavilov, but for reasons unrelated to the determination of the standard of review.
[134] Second, prior to Vavilov, this Court consistently provided definitive answers to certified questions of statutory interpretation (see, e.g., Pushpanathan, at paras. 75‑76; Baker, at para. 75; Chieu, at para. 90; Ezokola, at paras. 6‑9; Febles, at para. 60; Hilewitz, at para. 71; B010, at para. 76; Tran, at para. 56; see also Vavilov v. Canada (Citizenship and Immigration), 2017 FCA 132, [2018] 3 F.C.R. 75, at para. 37; Kanthasamy v. Canada (Citizenship and Immigration), 2014 FCA 113, [2015] 1 F.C.R. 335, at para. 33). In Kanthasamy, the majority of this Court arguably did the same. Indeed, prior to considering the standard of review, Abella J., who wrote the majority reasons, engaged in a lengthy interpretive exercise with respect to s. 25(1) of the IRPA (see paras. 10‑41). In dissent, Moldaver J. (Wagner J. (as he then was) concurring) lamented that the majority had adopted a “do as we say, not what we do” approach to reasonableness review:
In particular, I am concerned that my colleague has not given the Officer’s reasons the deference which, time and again, this Court has said they deserve. In her reasons, she parses the Officer’s decision for legal errors, resolves ambiguities against the Officer, and reweighs the evidence. Lest we be accused of adopting a “do as we say, not what we do” approach to reasonableness review, this approach fails to heed the admonition in Newfoundland and Labrador Nurses — that reviewing courts must be cautious about substituting their own view of the proper outcome by designating certain omissions in the reasons to be fatal (para. 17). As is the case with every other court, this Court has no licence to find an officer’s decision unreasonable simply because it considers the result unpalatable and would itself have come to a di`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 3. `teacher-phrase-neutral-0003`

- Proposed treatment: **neutral**
- Support: **1** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `may operate as legal constraints on an administrative decision maker`

Evidence:
- `mason-argument-citation-045`; citation: `authority`; hash: `04c5bd74789a21a9c8885d492a330bacc791b6fbe843b33bd5f00865b1ccf188`
  - Proposed evidence: `may operate as legal constraints on an administrative decision maker`
  - Decision context: `y conclude that remitting the question to the administrative decision maker may serve no useful purpose (Vavilov, at para. 124). It must be stressed that the possibility of a single reasonable interpretation is not a starting point of reasonableness review, as this would be contrary to a “reasons first” approach. Rather, it is a conclusion that a reviewing court may draw as a result of a proper reasonableness review, as part of the court’s consideration of the appropriate remedy.
3. Relevant Statutory Law, Common Law, and International Law
[72] Statutory law, common law, and international law may operate as legal constraints on an administrative decision maker (paras. 111 and 114). An administrative decision will be unreasonable if it fails to justify a departure from binding precedents (para. 112). International law can also operate as an important constraint, arising from the presumption that legislation is presumed to operate in conformity with Canada’s international obligations and the values and principles of customary and conventional international law, or by informing whether a decision was a reasonable exercise of administrative authority (para. 114).
4. The Evidence and Facts Before the Decision Maker
[73] Absent exceptional circumstances, a reviewing court will defer to an administrative decision maker’s factual findings (para. 125). A reviewing court may intervene, however, if the decision is unreasonable: if it is not “justified in light of the facts” or when “the decision maker has fundamentally misapprehended or failed to account for the evidence before it” (para. 126).
5. The Submissions of the Parties
[74] An administrative decision maker’s reasons must “meaningfully account for the central issues and concerns raised by the parties” (para. 127). Reasons must be “responsive” to the parties’ submissions, because reasons are the “primary mechanism by which decision makers demonstrate that they have actually listened to the parties” (para. 127 (emphasis in original)). Although an administrative decision does not have to “respond to every argument or line of possible analysis” raised by the parties, “a decision maker’s failure to meaningfully grapple with key issues or central arguments raised by the parties may call into question whether the decision maker was actually alert and sensitive to the matter before i`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 4. `teacher-phrase-neutral-0004`

- Proposed treatment: **neutral**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `outlined how a reviewing court should evaluate the reasonableness of an administrative decision maker’s interpretation of a statute`

Evidence:
- `mason-argument-citation-013`; citation: `Vavilov`; hash: `d1575850909b309588a707c64d4925531ab92990ce6a04d0e30a328ab4a11fac`
  - Proposed evidence: `outlined how a reviewing court should evaluate the reasonableness of an administrative decision maker’s interpretation of a statute`
  - Decision context: `and issued a deportation order.
D. Federal Court Decision (Mr. Mason), 2019 FC 1251, [2020] 2 F.C.R. 3 (Grammond J.)
[22] The Federal Court granted Mr. Mason’s application for judicial review of the IAD’s decision. The court held that the IAD’s interpretation of s. 34(1) (e) of the IRPA was unreasonable because it disregarded the structure of the Act and rendered meaningless statutory provisions for inadmissibility based on criminality. In the Federal Court’s view, s. 34(1)(e) requires a link to national security.
[23] The Federal Court — whose reasons were released before this Court released Vavilov — outlined how a reviewing court should evaluate the reasonableness of an administrative decision maker’s interpretation of a statute. In the Federal Court’s view, a reviewing court must ensure that an administrative decision maker did not overlook a very strong argument — a “knock-out punch”, that is, an interpretation that is internally consistent, withstands scrutiny, and is not met by a countervailing interpretation of similar force — or choose an interpretation when the interpretive “clues” point overwhelmingly in the other direction.
[24] The Federal Court ruled that the IAD’s interpretation of s. 34(1)(e) was unreasonable because it conflicted with the broader structure of the IRPA , thus undermining Parliament’s intent. In the court’s view, this structural argument was a “knock-out punch”. The IAD’s decision upset the carefully crafted structure of the IRPA by including under s. 34(1)(e) a vast range of conduct that “would or might endanger the lives or safety of persons in Canada”. This would thwart Parliament’s intent by bringing under the most serious category of inadmissibility conduct falling below the thresholds for less serious categories of inadmissibility, and it would discard Parliament’s choice under s. 36 of the IRPA to require a conviction when criminal conduct was committed in Canada. Secti`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 5. `teacher-phrase-neutral-0005`

- Proposed treatment: **neutral**
- Support: **1** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `see also al yamani v. canada (solicitor general), [1996] 1 f.c. 174 (t.d.)`

Evidence:
- `mason-argument-citation-097`; citation: `Al Yamani v. Canada (Solicitor General), [1996] 1 F.C. 174`; hash: `5a8d1e2a41cdf55774cce77077725ae09a538ce98e11a7b5c160941880bec3bf`
  - Proposed evidence: `see also Al Yamani v. Canada (Solicitor General), [1996] 1 F.C. 174 (T.D.)`
  - Decision context: `olent acts that exist in this case. While assaults against individuals are undesirable, they cannot be considered to be a threat to the safety of persons in Canada and the security of Canadian society, as contemplated by this section of the IRPA . [para. 42]
[185] Member King also distinguished the circumstances in X (Re) from those before the Federal Court in Moumdjian v. Canada (Security Intelligence Review Committee), [1999] 4 F.C. 624 (C.A.), which were “more obviously related to the security of Canada” and dealt with a conspiracy to assassinate a Turkish diplomat in Canada (paras. 77‑78; see also Al Yamani v. Canada (Solicitor General), [1996] 1 F.C. 174 (T.D.)).
[186] For these reasons, in addition to those identified by my colleague and by Grammond J. in the Federal Court, I would conclude that inadmissibility under s. 34(1)(e) requires a nexus between the relevant act of violence and with national security or the security of Canada. However, it remains the task of administrative decision makers under the IRPA to apply this interpretation going forward, including determining which acts of violence may indeed qualify as a threat to national security or the security of Canada.`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 6. `teacher-phrase-neutral-0006`

- Proposed treatment: **neutral**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `the court also applied a standard of review of reasonableness in agraira v. canada (public safety and emergency preparedness), 2013 scc 36, [2013] 2 s.c.r. 559, on the basis that the minister’s decision under the former s. 34(2) of the irpa was discretionary (para. 50)`

Evidence:
- `mason-argument-citation-071`; citation: `Agraira v. Canada (Public Safety and Emergency Preparedness), 2013 SCC 36, [2013] 2 S.C.R. 559`; hash: `e461e3ff604328770db929db5c7a109f8361b794d10873d8efa0504e7d375458`
  - Proposed evidence: `The Court also applied a standard of review of reasonableness in Agraira v. Canada (Public Safety and Emergency Preparedness), 2013 SCC 36, [2013] 2 S.C.R. 559, on the basis that the Minister’s decision under the former s. 34(2) of the IRPA was discretionary (para. 50)`
  - Decision context: `ation in assessing an applicant under s. 114(2) of the Immigration Act?”
. . .
The certified question asks whether the best interests of children must be a primary consideration when assessing an applicant under s. 114(2) and the Regulations. The principles discussed above indicate that, for the exercise of the discretion to fall within the standard of reasonableness, the decision‑maker should consider children’s best interests as an important factor, give them substantial weight, and be alert, alive and sensitive to them. [Emphasis added; emphasis in original deleted; paras. 9 and 75.]
[130] The Court also applied a standard of review of reasonableness in Agraira v. Canada (Public Safety and Emergency Preparedness), 2013 SCC 36, [2013] 2 S.C.R. 559, on the basis that the Minister’s decision under the former s. 34(2) of the IRPA was discretionary (para. 50). In Kanthasamy v. Canada (Citizenship and Immigration), 2015 SCC 61, [2015] 3 S.C.R. 909, the majority of this Court held that the fact that the reviewing judge “considered the question to be of general importance” was “relevant, but not determinative” of the standard of review (para. 44). “Despite the presence of a certified question, the appropriate standard of review” in that case was reasonableness (ibid., citing Baker, at para. 62).
[131] However, as the Canadian Association of Refugee Lawyers notes in its factum, Agraira and Kanthasamy are outliers. The Court applied a standard of correctness in Chieu v. Canada (Minister of Citizenship and Immigration), 2002 SCC 3, [2002] 1 S.C.R. 84, at para. 26, and Hilewitz v. Canada (Minister of Citizenship and Immigration), 2005 SCC 57, [2005] 2 S.C.R. 706, at para. 71. In other cases, the Court gave definitive answers to certified questions of interpretation either without addressing the standard of review (see Ezokola v. Canada (Citizenship and Immigration), 2013 SCC 40, [2013] 2 S.C.R. 678, at paras. 6‑9; Febles v. Canada (Citizenship and Immigration), 2014 SCC 68, [2014] 3 S.C.R. 431, at paras. 6 and 60) or after finding that it was`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 7. `teacher-phrase-neutral-0007`

- Proposed treatment: **neutral**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `the court gave definitive answers to certified questions of interpretation either without addressing the standard of review`

Evidence:
- `mason-argument-citation-075`; citation: `Ezokola v. Canada (Citizenship and Immigration), 2013 SCC 40, [2013] 2 S.C.R. 678, at paras. 6`; hash: `7dd83e29fe4fb470b5f105897d85e6a53ec8dace61b715321f30d1ba4bfad63f`
  - Proposed evidence: `the Court gave definitive answers to certified questions of interpretation either without addressing the standard of review`
  - Decision context: `rminative” of the standard of review (para. 44). “Despite the presence of a certified question, the appropriate standard of review” in that case was reasonableness (ibid., citing Baker, at para. 62).
[131] However, as the Canadian Association of Refugee Lawyers notes in its factum, Agraira and Kanthasamy are outliers. The Court applied a standard of correctness in Chieu v. Canada (Minister of Citizenship and Immigration), 2002 SCC 3, [2002] 1 S.C.R. 84, at para. 26, and Hilewitz v. Canada (Minister of Citizenship and Immigration), 2005 SCC 57, [2005] 2 S.C.R. 706, at para. 71. In other cases, the Court gave definitive answers to certified questions of interpretation either without addressing the standard of review (see Ezokola v. Canada (Citizenship and Immigration), 2013 SCC 40, [2013] 2 S.C.R. 678, at paras. 6‑9; Febles v. Canada (Citizenship and Immigration), 2014 SCC 68, [2014] 3 S.C.R. 431, at paras. 6 and 60) or after finding that it was unnecessary to resolve the issue (B010 v. Canada (Citizenship and Immigration), 2015 SCC 58, [2015] 3 S.C.R. 704, at paras. 26 and 76; Tran v. Canada (Public Safety and Emergency Preparedness), 2017 SCC 50, [2017] 2 S.C.R. 289, at paras. 23, 53 and 56).
[132] Relying on pre‑Vavilov authorities, my colleague says that this Court has “concluded in the immigration context” that the standard of review for certified questions is reasonableness (para. 51, citing Kanthasamy and Baker). With respect, I disagree.
[133] First, this Court did not endorse or even cite Kanthasamy in Vavilov. It relied on Baker in Vavilov, but for reasons unrelated to the determination of the standard of review.`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 8. `teacher-phrase-neutral-0008`

- Proposed treatment: **neutral**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `the iad concluded that inadmissibility under s. 34(1)(e) does not require a link to national security or the security of canada.`

Evidence:
- `mason-argument-citation-010`; citation: `2019 CanLII 55171`; hash: `504fb7c73df4cc70c6a14846e4c94ece608d29d3e373edd13ed62b078879cb50`
  - Proposed evidence: `The IAD concluded that inadmissibility under s. 34(1)(e) does not require a link to national security or the security of Canada.`
  - Decision context: `r Mr. Mason’s alleged conduct, if proven, could be a ground of inadmissibility under s. 34(1)(e). The ID ruled that a “security groun[d]” under s. 34(1) means a threat to the security of Canada or another country, and that the act of violence in question must have some connection to a threat to the security of Canada. In the ID’s view, Mr. Mason’s alleged conduct involved “mere criminal offences”, which “although very serious”, lacked “any element that would elevate them to security grounds”, and thus s. 34(1)(e) could not apply (para. 24).
B. Immigration Appeal Division Decision (Mr. Mason), 2019 CanLII 55171
[20] The Minister of Public Safety and Emergency Preparedness appealed the ID’s decision in Mr. Mason’s case to the IAD, which allowed the Minister’s appeal, set aside the ID’s decision, and referred the matter back for a full hearing on the merits. The IAD concluded that inadmissibility under s. 34(1)(e) does not require a link to national security or the security of Canada. In the IAD’s view, “security” under s. 34(1)(e) relates to “security in a broader sense”, namely, to ensure “that individual Canadians are secure from acts of violence that would or might endanger their lives or safety” (para. 37).
C. Immigration Division Decision (Mr. Dleiow), 2019 CanLII 129531
[21] In Mr. Dleiow’s case, the ID saw no basis to depart from the IAD’s interpretation of s. 34(1)(e) in Mr. Mason’s case, and therefore affirmed that s. 34(1)(e) does not require a link to national security or the security of Canada. The ID also heard evidence and concluded that Mr. Dleiow was inadmissible because he had engaged in violent acts against two intimate partners, which there were reasonable grounds to believe had endangered their safety. The ID based this conclusion on a guilty plea for acts relating to one intimate partner, and on testimony and police occurrence reports relating to the other intimate partner. As a result, the ID ruled that Mr. Dleiow was inadmissible and issued a deportation order.
D. Federal Court Decision (Mr. Mason), 2019 FC 1251, [2020] 2 F.C.R. 3 (Grammond J.)`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 9. `teacher-phrase-neutral-0009`

- Proposed treatment: **neutral**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `vavilov tells us much but it leaves some things unclear`

Evidence:
- `mason-argument-citation-016`; citation: `Vavilov`; hash: `e2d854ae68cb221e855db59ef17795f5a3abef57b2622e9d897a15ea7317a818`
  - Proposed evidence: `Vavilov tells us much but it leaves some things unclear`
  - Decision context: `lication for judicial review of the ID’s decision. The court applied the Federal Court’s reasoning in Mr. Mason’s case for reasons of comity, set aside the ID’s decision and ordered the matter be reconsidered on the merits by a different decision maker. The court also certified the same serious question of general importance.
F. Federal Court of Appeal (Mr. Mason and Mr. Dleiow), 2021 FCA 156, [2022] 1 F.C.R. 3 (Stratas J.A., Rennie and Mactavish JJ.A. concurring)
[28] The Federal Court of Appeal decided the appeals in Mr. Mason’s and Mr. Dleiow’s cases together, after this Court had released Vavilov. The court held that the administrative decisions reasonably interpreted s. 34(1)(e) as not requiring a nexus with national security or the security of Canada.
[29] The Court of Appeal began by discussing how a court should conduct reasonableness review. The court said that “Vavilov tells us much but it leaves some things unclear” (para. 9). The court cautioned that a reviewing court should not fashion its own yardstick and use it to measure what the administrator did, but should instead conduct “a preliminary analysis of the text, context and purpose of the legislation just to understand the lay of the land before they examine the administrators’ reasons” (para. 17). The Court of Appeal also criticized the Federal Court’s “knock-out punch” approach in Mr. Mason’s case as involving disguised correctness review.
[30] The Court of Appeal concluded that the IAD was alive to the essential elements of s. 34(1)(e)’s text, context, and purpose, and saw no omitted aspects that would cause a loss of confidence in the outcome. It rejected Mr. Mason’s argument that reading s. 34(1)(e) without a nexus to national security is inconsistent with the broader statutory context. The court ruled that the IAD reasonably concluded that the conduct captured by s. 34(1)(e), which speaks of the danger posed to the “lives or safety” of persons in Canada, is only a small subset of what would be considered serious criminality under s. 36 of the IRPA . Sections 34 and 36 address two different matters — conduct and convictions, respec`
  - Offsets repaired: `True`; confidence: `0.95`
- `mason-argument-citation-017`; citation: `Vavilov`; hash: `6bd97b7867d0da49dca1d4ac000f263c0946e3b88833ad93423a6598e9412f30`
  - Proposed evidence: `Vavilov tells us much but it leaves some things unclear`
  - Decision context: `ame serious question of general importance.
F. Federal Court of Appeal (Mr. Mason and Mr. Dleiow), 2021 FCA 156, [2022] 1 F.C.R. 3 (Stratas J.A., Rennie and Mactavish JJ.A. concurring)
[28] The Federal Court of Appeal decided the appeals in Mr. Mason’s and Mr. Dleiow’s cases together, after this Court had released Vavilov. The court held that the administrative decisions reasonably interpreted s. 34(1)(e) as not requiring a nexus with national security or the security of Canada.
[29] The Court of Appeal began by discussing how a court should conduct reasonableness review. The court said that “Vavilov tells us much but it leaves some things unclear” (para. 9). The court cautioned that a reviewing court should not fashion its own yardstick and use it to measure what the administrator did, but should instead conduct “a preliminary analysis of the text, context and purpose of the legislation just to understand the lay of the land before they examine the administrators’ reasons” (para. 17). The Court of Appeal also criticized the Federal Court’s “knock-out punch” approach in Mr. Mason’s case as involving disguised correctness review.
[30] The Court of Appeal concluded that the IAD was alive to the essential elements of s. 34(1)(e)’s text, context, and purpose, and saw no omitted aspects that would cause a loss of confidence in the outcome. It rejected Mr. Mason’s argument that reading s. 34(1)(e) without a nexus to national security is inconsistent with the broader statutory context. The court ruled that the IAD reasonably concluded that the conduct captured by s. 34(1)(e), which speaks of the danger posed to the “lives or safety” of persons in Canada, is only a small subset of what would be considered serious criminality under s. 36 of the IRPA . Sections 34 and 36 address two different matters — conduct and convictions, respec`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 10. `teacher-phrase-supportive-0010`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `(see also canada (immigration and citizenship) v. laing, 2021 fca 194, at para. 11 (canlii); canada (public safety and emergency preparedness) v. xy, 2022 fca 113, 89 imm. l.r. (4th) 173, at para. 7)`

Evidence:
- `mason-argument-citation-087`; citation: `Canada (Public Safety and Emergency Preparedness) v. XY, 2022 FCA 113`; hash: `7a93668bdfec93ad8e5c03e9e2079541ade99ccbf616c38248feaa5aa0214885`
  - Proposed evidence: `(See also Canada (Immigration and Citizenship) v. Laing, 2021 FCA 194, at para. 11 (CanLII); Canada (Public Safety and Emergency Preparedness) v. XY, 2022 FCA 113, 89 Imm. L.R. (4th) 173, at para. 7)`
  - Decision context: `at para. 53). I say this for two reasons.
(a) The Risk of Arbitrariness Is Unacceptable in This Context
[159] First, the rule of law demands a “singular, determinate and final answer” (Vavilov, at para. 32) to a question certified as a serious question of general importance under the IRPA . In Lunyamila, the Federal Court of Appeal reiterated the criteria for certification under s. 74(d):
The question must be a serious question that is dispositive of the appeal, transcends the interests of the parties and raises an issue of broad significance or general importance. [Emphasis added; para. 46.]
(See also Canada (Immigration and Citizenship) v. Laing, 2021 FCA 194, at para. 11 (CanLII); Canada (Public Safety and Emergency Preparedness) v. XY, 2022 FCA 113, 89 Imm. L.R. (4th) 173, at para. 7).
[160] A question whose answer turns on the unique facts of the case will not be certified (Lunyamila, at para. 46, citing Mudrak v. Canada (Minister of Citizenship and Immigration), 2016 FCA 178, 43 Imm. L.R. (4th) 199). By definition, then, certified questions concern issues of broad significance or general importance within Canada’s immigration and refugee protection regime. In my view, these are exactly the types of questions for which the rule of law demands consistent and definitive answers — and for which the risk of arbitrariness is unacceptable.
[161] In Vavilov, our Court accepted that legal incoherence is antithetical to the rule of law (para. 72). While the Court rejected “persistent discord within an administrative body” as a standalone category of correctness review, this was based on the ability of a “more robust” form of reasonableness to guard against the risk of arbitrariness:
We are not persuaded that the Court should recognize a distinct correctness category for legal questions on which there is persistent discord within an administrative body. In Domtar Inc. v. Quebec (Commission d’appel en matière de lésions professionnelles), [1993] 2 S.C.R. 756, this Court `
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 11. `teacher-phrase-supportive-0011`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `a question whose answer turns on the unique facts of the case will not be certified (lunyamila, at para. 46, citing mudrak v. canada (minister of citizenship and immigration), 2016 fca 178, 43 imm. l.r. (4th) 199).`

Evidence:
- `mason-argument-citation-088`; citation: `Mudrak v. Canada (Minister of Citizenship and Immigration), 2016 FCA 178`; hash: `7b25e76a0bb231abb4012b419956e31b0f008f30965907d78a549e74f6149a66`
  - Proposed evidence: `A question whose answer turns on the unique facts of the case will not be certified (Lunyamila, at para. 46, citing Mudrak v. Canada (Minister of Citizenship and Immigration), 2016 FCA 178, 43 Imm. L.R. (4th) 199).`
  - Decision context: `to a question certified as a serious question of general importance under the IRPA . In Lunyamila, the Federal Court of Appeal reiterated the criteria for certification under s. 74(d):
The question must be a serious question that is dispositive of the appeal, transcends the interests of the parties and raises an issue of broad significance or general importance. [Emphasis added; para. 46.]
(See also Canada (Immigration and Citizenship) v. Laing, 2021 FCA 194, at para. 11 (CanLII); Canada (Public Safety and Emergency Preparedness) v. XY, 2022 FCA 113, 89 Imm. L.R. (4th) 173, at para. 7).
[160] A question whose answer turns on the unique facts of the case will not be certified (Lunyamila, at para. 46, citing Mudrak v. Canada (Minister of Citizenship and Immigration), 2016 FCA 178, 43 Imm. L.R. (4th) 199). By definition, then, certified questions concern issues of broad significance or general importance within Canada’s immigration and refugee protection regime. In my view, these are exactly the types of questions for which the rule of law demands consistent and definitive answers — and for which the risk of arbitrariness is unacceptable.
[161] In Vavilov, our Court accepted that legal incoherence is antithetical to the rule of law (para. 72). While the Court rejected “persistent discord within an administrative body” as a standalone category of correctness review, this was based on the ability of a “more robust” form of reasonableness to guard against the risk of arbitrariness:
We are not persuaded that the Court should recognize a distinct correctness category for legal questions on which there is persistent discord within an administrative body. In Domtar Inc. v. Quebec (Commission d’appel en matière de lésions professionnelles), [1993] 2 S.C.R. 756, this Court held that “a lack of unanimity [within a tribunal] is the price to pay for the decision-making freedom and independence given to the members of these tribunals”: p. 800; see also Ellis‑Don Ltd. v. Ontario (Labour Relations`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 12. `teacher-phrase-supportive-0012`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.99**
- Span quality: **repaired**
- Phrase: `apply the framework for judicial review developed in canada (minister of citizenship and immigration) v. vavilov, 2019 scc 65, [2019] 4 s.c.r. 653`

Evidence:
- `mason-argument-citation-001`; citation: `Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653`; hash: `cd68903baf5313e2e9db03e1c709cdd1ec6a7cf79073d281de91fab59ae2c9ee`
  - Proposed evidence: `apply the framework for judicial review developed in Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653`
  - Decision context: `[1] These appeals require the Court to apply the framework for judicial review developed in Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653, to two administrative decisions involving a question of statutory interpretation in the immigration context.
[2] The statutory provision at issue, s. 34(1) (e) of the Immigration and Refugee Protection Act , S.C. 2001, c. 27 (“IRPA ”), provides that permanent residents and foreign nationals are inadmissible to Canada on “security grounds” for “engaging in acts of violence that would or might endanger the lives or safety of persons in Canada”. The key point of disagreement among the administrative decision makers and courts below is whether the “acts of violence” listed as “security grounds” in s. 34(1)(e) require a link to national security or the security of Canada, or whether s. 34(1)(e) applies to acts of violence more broadly even without such a link.
[3] Both administrative decisions under review interpreted s. 34(1)(e) as not requiring the acts of violence to have a link to national security or the security of Canada. In the first administrative decision, the Immigration Appeal Division (“IAD”) of the Immigration and Refugee Board of Canada (“IRB”) ruled that Mr. Earl Mason, a foreign national, could be found inadmissible under s. 34(1)(e) if his alleged violent conduct wer`
  - Offsets repaired: `True`; confidence: `0.99`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 13. `teacher-phrase-supportive-0013`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `by being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer`

Evidence:
- `mason-argument-citation-037`; citation: `Vavilov`; hash: `539897eed2517b049231165f054bd3b5616fea6327b2117811f12211b52029a3`
  - Proposed evidence: `By being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer`
  - Decision context: `ion maker may draw on its institutional expertise and experience and rely on considerations that a court would not have thought to employ, but which “enrich and elevate the interpretive exercise” (paras. 93 and 119; Canada Post, at para. 43). As Professor Audrey Macklin explains, courts should be “genuinely receptive to input beyond the usual techniques that courts use to discern text, context and purpose. These may include operational implications, alignment with broader statutory mandate, and so on” (“Seven Out of Nine Legal Experts Agree: Expertise No Longer Matters (in the Same Way) After Vavilov!” (2021), 100 S.C.L.R. (2d) 249, at p. 261). By being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer (Vavilov, at para. 108). Reasonableness review demands both that administrative decision makers demonstrate their expertise through their reasons and that judges pay “[r]espectful attention” to the ways in which their reasons reflect that expertise (para. 93; P. Daly, “Vavilov and the Culture of Justification in Contemporary Administrative Law” (2021), 100 S.C.L.R. (2d) 279, at pp. 285‑86).
[71] Finally, a court may conclude during a reasonableness review that “the interplay of text, context and purpose leaves room for a single reasonable interpretation of the statutory provision, or aspect of the statutory provision” (Vavilov, at para. 124, citing Dunsmuir, at paras. 72‑76, and Nova Tube Inc./Nova Steel Inc. v. Conares Metal Supply Ltd., 2019 FCA 52). In such a case, although a court should “generally pause before definitively pronouncing upon the interpretation” of a statutory provision, the court may conclude that remitting the question to the administrative decision maker may serve no useful purpose (Vavilov, at para. 124). It must be stressed that the possibility of a single reasonable interpretation is not a starting point of reasonableness review, as this would be contrary `
  - Offsets repaired: `True`; confidence: `0.95`
- `mason-argument-citation-038`; citation: `(Vavilov, at para. 108)`; hash: `539897eed2517b049231165f054bd3b5616fea6327b2117811f12211b52029a3`
  - Proposed evidence: `By being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer`
  - Decision context: ` experience and rely on considerations that a court would not have thought to employ, but which “enrich and elevate the interpretive exercise” (paras. 93 and 119; Canada Post, at para. 43). As Professor Audrey Macklin explains, courts should be “genuinely receptive to input beyond the usual techniques that courts use to discern text, context and purpose. These may include operational implications, alignment with broader statutory mandate, and so on” (“Seven Out of Nine Legal Experts Agree: Expertise No Longer Matters (in the Same Way) After Vavilov!” (2021), 100 S.C.L.R. (2d) 249, at p. 261). By being receptive to such factors, courts acknowledge that administrative decision makers have a role to play in elaborating the content of the schemes that they administer (Vavilov, at para. 108). Reasonableness review demands both that administrative decision makers demonstrate their expertise through their reasons and that judges pay “[r]espectful attention” to the ways in which their reasons reflect that expertise (para. 93; P. Daly, “Vavilov and the Culture of Justification in Contemporary Administrative Law” (2021), 100 S.C.L.R. (2d) 279, at pp. 285‑86).
[71] Finally, a court may conclude during a reasonableness review that “the interplay of text, context and purpose leaves room for a single reasonable interpretation of the statutory provision, or aspect of the statutory provision” (Vavilov, at para. 124, citing Dunsmuir, at paras. 72‑76, and Nova Tube Inc./Nova Steel Inc. v. Conares Metal Supply Ltd., 2019 FCA 52). In such a case, although a court should “generally pause before definitively pronouncing upon the interpretation” of a statutory provision, the court may conclude that remitting the question to the administrative decision maker may serve no useful purpose (Vavilov, at para. 124). It must be stressed that the possibility of a single reasonable interpretation is not a starting point of reasonableness review, as this would be contrary to a “reasons first” app`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 14. `teacher-phrase-supportive-0014`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `by definition, these are questions that transcend the interests of the parties and raise issues of broad significance within canada’s immigration and refugee protection scheme`

Evidence:
- `mason-argument-citation-068`; citation: `Lunyamila v. Canada (Public Safety and Emergency Preparedness), 2018 FCA 22, [2018] 3 F.C.R. 674, at para. 46`; hash: `73165598fefe84909d903292aa6623307fceb120a9392df67e850d6f3b1db272`
  - Proposed evidence: `By definition, these are questions that transcend the interests of the parties and raise issues of broad significance within Canada’s immigration and refugee protection scheme`
  - Decision context: `Earl Mason and the interveners the Canadian Association of Refugee Lawyers and the Canadian Council for Refugees.
[125] In Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653, this Court held that reviewing courts should derogate from the presumption of reasonableness review where required by (1) a clear indication of legislative intent or (2) the rule of law (para. 10). In my view, the rule of law requires — and Parliament intended for appellate courts to provide — definitive, correct answers to legal questions certified under s. 74 (d) of the IRPA . By definition, these are questions that transcend the interests of the parties and raise issues of broad significance within Canada’s immigration and refugee protection scheme (see Lunyamila v. Canada (Public Safety and Emergency Preparedness), 2018 FCA 22, [2018] 3 F.C.R. 674, at para. 46).
[126] In Pushpanathan v. Canada (Minister of Citizenship and Immigration), [1998] 1 S.C.R. 982, this Court noted that the certified question regime would be “incoherent” if the standard of review were anything other than correctness (para. 43). This is exemplified by the companion appeals before us. The IAD’s interpretation of s. 34(1)(e) in Mr. Mason’s case, subsequently applied to Mr. Dleiow, would significantly expand the grounds on which foreign nationals or permanent residents may be deported from Canada. It would allow foreign nationals to be returned to countries where they may face persecution, in a manner contrary to Canada’s obligations under the Convention Relating to the Status of Refugees, Can. T.S. 1969 No. 6 (see Jamal J.’s reasons, at paras. 104‑17). Parliament did not intend for appellate courts, as the Federal Court of Appeal did in this case, to defer to such interpretations where they may be “reasonable”, but are nonetheless wrong in law (see Pushpanathan, at para. 43).
[127] To be consistent with the principles and framework set out in Vavilov, I would recognize a new category of correctness review: when appellate courts decide a “serious question of general`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 15. `teacher-phrase-supportive-0015`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `canada has ratified both the 1951 refugee convention and the 1967 refugee protocol (németh v. canada (justice), 2010 scc 56, [2010] 3 s.c.r. 281, at para. 17).`

Evidence:
- `mason-argument-citation-058`; citation: `Németh v. Canada (Justice), 2010 SCC 56, [2010] 3 S.C.R. 281, at para. 17`; hash: `003a2f2d54de269268a301549eb5b80d72e71bd7a8b2decb8a706c39a12127f3`
  - Proposed evidence: `Canada has ratified both the 1951 Refugee Convention and the 1967 Refugee Protocol (Németh v. Canada (Justice), 2010 SCC 56, [2010] 3 S.C.R. 281, at para. 17).`
  - Decision context: `h Article 33. Although this argument was not presented to the IAD, the IAD was required by its home statute to interpret and apply the IRPA in a manner that complies with Canada’s international human rights obligations, including Canada’s non-refoulement obligation under Article 33 of the Refugee Convention.
[105] Vavilov highlighted that international law may be an “important constraint on an administrative decision maker”, including through the presumption of statutory interpretation that “legislation is presumed to operate in conformity with Canada’s international obligations” (para. 114). Canada has ratified both the 1951 Refugee Convention and the 1967 Refugee Protocol (Németh v. Canada (Justice), 2010 SCC 56, [2010] 3 S.C.R. 281, at para. 17). These international human rights instruments to which Canada is a party trigger the interpretive presumption of conformity with international law.
[106] The presumption of conformity with international law assumes added force when interpreting the IRPA , because Parliament has made its “presumed intent to conform to Canada’s international obligations explicit” through two provisions of the IRPA (B010 v. Canada (Citizenship and Immigration), 2015 SCC 58, [2015] 3 S.C.R. 704, at para. 49). First, s. 3(2)(b) of the IRPA expressly identifies one of the IRPA ’s objectives as being “to fulfil Canada’s international legal obligations with respect to refugees and affirm Canada’s commitment to international efforts to provide assistance to those in need of resettlement”. Indeed, this Court has described the IRPA as the “main legislative vehicle for implementing Canada’s international refugee obligations” (Németh, at para. 21). Second, s. 3(3) (f) of the IRPA instructs courts and administrative decision makers to construe and apply the IRPA in a manner that “complies with international human rights instruments to which Canada is signatory” (B010, at para. 49). This Court has stated that “[t`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 16. `teacher-phrase-supportive-0016`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `reiterated the criteria for certification under s. 74(d): the question must be a serious question that is dispositive of the appeal, transcends the interests of the parties and raises an issue of broad significance or general importance`

Evidence:
- `mason-argument-citation-086`; citation: `Canada (Immigration and Citizenship) v. Laing, 2021 FCA 194, at para. 11`; hash: `7a93668bdfec93ad8e5c03e9e2079541ade99ccbf616c38248feaa5aa0214885`
  - Proposed evidence: `reiterated the criteria for certification under s. 74(d):
The question must be a serious question that is dispositive of the appeal, transcends the interests of the parties and raises an issue of broad significance or general importance`
  - Decision context: `2) The Rule of Law
[158] The presumption of reasonableness review must also give way to the importance of maintaining the rule of law, which requires that certified questions be answered consistently and definitively (see Society of Composers, at para. 33; Vavilov, at para. 53). I say this for two reasons.
(a) The Risk of Arbitrariness Is Unacceptable in This Context
[159] First, the rule of law demands a “singular, determinate and final answer” (Vavilov, at para. 32) to a question certified as a serious question of general importance under the IRPA . In Lunyamila, the Federal Court of Appeal reiterated the criteria for certification under s. 74(d):
The question must be a serious question that is dispositive of the appeal, transcends the interests of the parties and raises an issue of broad significance or general importance. [Emphasis added; para. 46.]
(See also Canada (Immigration and Citizenship) v. Laing, 2021 FCA 194, at para. 11 (CanLII); Canada (Public Safety and Emergency Preparedness) v. XY, 2022 FCA 113, 89 Imm. L.R. (4th) 173, at para. 7).
[160] A question whose answer turns on the unique facts of the case will not be certified (Lunyamila, at para. 46, citing Mudrak v. Canada (Minister of Citizenship and Immigration), 2016 FCA 178, 43 Imm. L.R. (4th) 199). By definition, then, certified questions concern issues of broad significance or general importance within Canada’s immigration and refugee protection regime. In my view, these are exactly the types of questions for which the rule of law demands consistent and definitive answers — and for which the risk of arbitrariness is unacceptable.
[161] In Vavilov, our Court accepted that legal incoherence is antithetical to the rule of law (para. 72). While the Court rejected “persistent discord within an administrative body” as a standalone category of correctness review, this was based on the ability of a “more robust” form of reasonableness to guard against the risk of arbitrariness:
We are not persuaded that the Court should recognize a distinct correctness category for legal questions on which there is persistent discord within an administrative body. I`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 17. `teacher-phrase-supportive-0017`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **1.00**
- Span quality: **repaired**
- Phrase: `the principle of non-refoulement is generally recognized as a norm of customary international law`

Evidence:
- `mason-argument-citation-064`; citation: `in E. Feller, V. Türk`; hash: `58ef2abc2379e7d495cd4317ac56fbc14fce4460c7c72ebf8ab9341d5a7594c9`
  - Proposed evidence: `The principle of non-refoulement is generally recognized as a norm of customary international law`
  - Decision context: `iple of non-refoulement in Article 33(1), allows a person to be removed in exceptional circumstances: when there are reasonable grounds for regarding the person as a danger to the security of the country in which they are, or when the person is convicted of a serious crime and is a danger to the community of that country (see Febles v. Canada (Citizenship and Immigration), 2014 SCC 68, [2014] 3 S.C.R. 431, at para. 25). Article 42 of the Refugee Convention further stipulates that ratifying states may not make reservations to the non-refoulement protections of Article 33 (Németh, at para. 18). The principle of non-refoulement is generally recognized as a norm of customary international law (see Prosecutor v. Germain Katanga, ICC-01/04-01/07, Decision on the application for the interim release of detained Witnesses, 1 October 2013 (Trial Chamber II), at para. 30; Zaoui v. Attorney-General (No. 2), [2005] 1 N.Z.L.R. 690 (C.A.), at paras. 34-35; S. E. Lauterpacht and D. Bethlehem, “The scope and content of the principle of non-refoulement: Opinion”, in E. Feller, V. Türk and F. Nicholson, eds., Refugee Protection in International Law: UNHCR’s Global Consultations on International Protection (2003), 87, at paras. 193-253; H. Lambert, “Customary Refugee Law”, in C. Costello, M. Foster and J. McAdam, eds., The Oxford Handbook of International Refugee Law (2021), 240, at pp. 242-49; and United Nations High Commissioner for Refugees, Advisory Opinion on the Extraterritorial Application of Non-Refoulement Obligations under the 1951 Convention relating to the Status of Refugees and its 1967 Protocol (2007), at paras. 14-16).
[109] The IAD’s interpretation allows a foreign national found inadmissible under s. 34(1)(e) to be subject to refoulement contrary to Article 33(1) of the Refugee Convention. On the IAD’s interpretation, a foreign national can be deported to persecution once they are found inadmissible under s. 34(1)(e), without a finding that the person poses a danger to the security of Canada or even if they have not been convicted of a serious offence. Such a person would be entitled to the benefit of Article 33(1) of the Refugee Convention, as the exceptions under Article 33(2) would not apply: on the IAD’s approach to inadmissibility under s. 3`
  - Offsets repaired: `True`; confidence: `1.00`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 18. `teacher-phrase-supportive-0018`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `the principle of non-refoulement is generally recognized as a norm of customary international law (see prosecutor v. germain katanga, icc-01/04-01/07, decision on the application for the interim release of detained witnesses, 1 october 2013 (trial chamber ii), at para. 30`

Evidence:
- `mason-argument-citation-062`; citation: `Prosecutor v. Germain`; hash: `58ef2abc2379e7d495cd4317ac56fbc14fce4460c7c72ebf8ab9341d5a7594c9`
  - Proposed evidence: `The principle of non-refoulement is generally recognized as a norm of customary international law (see Prosecutor v. Germain Katanga, ICC-01/04-01/07, Decision on the application for the interim release of detained Witnesses, 1 October 2013 (Trial Chamber II), at para. 30`
  - Decision context: `iple of non-refoulement in Article 33(1), allows a person to be removed in exceptional circumstances: when there are reasonable grounds for regarding the person as a danger to the security of the country in which they are, or when the person is convicted of a serious crime and is a danger to the community of that country (see Febles v. Canada (Citizenship and Immigration), 2014 SCC 68, [2014] 3 S.C.R. 431, at para. 25). Article 42 of the Refugee Convention further stipulates that ratifying states may not make reservations to the non-refoulement protections of Article 33 (Németh, at para. 18). The principle of non-refoulement is generally recognized as a norm of customary international law (see Prosecutor v. Germain Katanga, ICC-01/04-01/07, Decision on the application for the interim release of detained Witnesses, 1 October 2013 (Trial Chamber II), at para. 30; Zaoui v. Attorney-General (No. 2), [2005] 1 N.Z.L.R. 690 (C.A.), at paras. 34-35; S. E. Lauterpacht and D. Bethlehem, “The scope and content of the principle of non-refoulement: Opinion”, in E. Feller, V. Türk and F. Nicholson, eds., Refugee Protection in International Law: UNHCR’s Global Consultations on International Protection (2003), 87, at paras. 193-253; H. Lambert, “Customary Refugee Law”, in C. Costello, M. Foster and J. McAdam, eds., The Oxford Handbook of International Refugee Law (2021), 240, at pp. 242-49; and United Nations High Commissioner for Refugees, Advisory Opinion on the Extraterritorial Application of Non-Refoulement Obligations under the 1951 Convention relating to the Status of Refugees and its 1967 Protocol (2007), at paras. 14-16).
[109] The IAD’s interpretation allows a foreign national found inadmissible under s. 34(1)(e) to be subject to refoulement contrary to Article 33(1) of the Refugee Convention. On the IAD’s interpretation, a foreign national can be deported to persecution once they are found inadmissible under s. 34(1)(e), without a finding that the person poses a danger to the security of Canada or even if they have not been convicted of a ser`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 19. `teacher-phrase-supportive-0019`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **1.00**
- Span quality: **repaired**
- Phrase: `the principle of non-refoulement is generally recognized as a norm of customary international law (see prosecutor v. germain katanga, icc-01/04-01/07, decision on the application for the interim release of detained witnesses, 1 october 2013 (trial chamber ii), at para. 30; zaoui v. attorney-general (no. 2), [2005] 1 n.z.l.r. 690 (c.a.), at paras. 34-35;`

Evidence:
- `mason-argument-citation-063`; citation: `Zaoui v. Attorney-General (No. 2), [2005] 1 N.Z.L.R. 690`; hash: `58ef2abc2379e7d495cd4317ac56fbc14fce4460c7c72ebf8ab9341d5a7594c9`
  - Proposed evidence: `The principle of non-refoulement is generally recognized as a norm of customary international law (see Prosecutor v. Germain Katanga, ICC-01/04-01/07, Decision on the application for the interim release of detained Witnesses, 1 October 2013 (Trial Chamber II), at para. 30; Zaoui v. Attorney-General (No. 2), [2005] 1 N.Z.L.R. 690 (C.A.), at paras. 34-35;`
  - Decision context: `iple of non-refoulement in Article 33(1), allows a person to be removed in exceptional circumstances: when there are reasonable grounds for regarding the person as a danger to the security of the country in which they are, or when the person is convicted of a serious crime and is a danger to the community of that country (see Febles v. Canada (Citizenship and Immigration), 2014 SCC 68, [2014] 3 S.C.R. 431, at para. 25). Article 42 of the Refugee Convention further stipulates that ratifying states may not make reservations to the non-refoulement protections of Article 33 (Németh, at para. 18). The principle of non-refoulement is generally recognized as a norm of customary international law (see Prosecutor v. Germain Katanga, ICC-01/04-01/07, Decision on the application for the interim release of detained Witnesses, 1 October 2013 (Trial Chamber II), at para. 30; Zaoui v. Attorney-General (No. 2), [2005] 1 N.Z.L.R. 690 (C.A.), at paras. 34-35; S. E. Lauterpacht and D. Bethlehem, “The scope and content of the principle of non-refoulement: Opinion”, in E. Feller, V. Türk and F. Nicholson, eds., Refugee Protection in International Law: UNHCR’s Global Consultations on International Protection (2003), 87, at paras. 193-253; H. Lambert, “Customary Refugee Law”, in C. Costello, M. Foster and J. McAdam, eds., The Oxford Handbook of International Refugee Law (2021), 240, at pp. 242-49; and United Nations High Commissioner for Refugees, Advisory Opinion on the Extraterritorial Application of Non-Refoulement Obligations under the 1951 Convention relating to the Status of Refugees and its 1967 Protocol (2007), at paras. 14-16).
[109] The IAD’s interpretation allows a foreign national found inadmissible under s. 34(1)(e) to be subject to refoulement contrary to Article 33(1) of the Refugee Convention. On the IAD’s interpretation, a foreign national can be deported to persecution once they are found inadmissible under s. 34(1)(e), without a finding that the person poses a danger to the security of Canada or even if they have not been convicted of a serious offence. Such a person would be entitled to the benefit of Article 33(1) of th`
  - Offsets repaired: `True`; confidence: `1.00`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 20. `teacher-phrase-supportive-0020`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `the risk of arbitrariness may be acceptable in the context of decisions regarding the extent of an income replacement indemnity during a temporary plant closure (as in domtar inc. v. quebec`

Evidence:
- `mason-argument-citation-092`; citation: `Domtar Inc. v. Quebec`; hash: `df195e32720e519271a63e39333dac0935c68a3d1103dbfe7b5beac8aa60a399`
  - Proposed evidence: `the risk of arbitrariness may be acceptable in the context of decisions regarding the extent of an income replacement indemnity during a temporary plant closure (as in Domtar Inc. v. Quebec`
  - Decision context: ` category of questions may be defined with precision (see Society of Composers, at para. 39). As Paul Daly notes, “the unique features of [Canada’s] immigration regime could allow for correctness review where questions have been certified without having unfortunate consequences in other areas of law” (Certified Questions, References and Reasonableness: Canada (Citizenship and Immigration) v. Galindo Camayo, 2022 FCA 50, April 8, 2022 (online)). In the immigration context, the certified question procedure is “tailor‑made to achieve correctness review on questions of law” (ibid.).
[164] Second, the risk of arbitrariness may be acceptable in the context of decisions regarding the extent of an income replacement indemnity during a temporary plant closure (as in Domtar Inc. v. Quebec (Commission d’appel en matière de lésions professionnelles), [1993] 2 S.C.R. 756) or alleged violations of a provincial collective agreement (as in Ellis‑Don Ltd. v. Ontario (Labour Relations Board), 2001 SCC 4, [2001] 1 S.C.R. 221) to use the two examples referred to in Vavilov (para. 72). It is not acceptable when the identity of the individual decision maker is what determines who is permitted to remain in Canada, as in these companion appeals, or in the context of other serious questions of general importance under the IRPA .
[165] A number of scholars and several interveners in these appeals emphasize the fundamental importance of certified questions, the potential consequences for affected individuals, and the corresponding need for courts to provide correct and definitive answers in this context (see, e.g., J. C. Y. Liew, “The Good, the Bad, and the Ugly: A Preliminary Assessment of Whether the Vavilov Framework Adequately Addresses Concerns of Marginalized Communities in the Immigration Law Context” (2020), 98 Can. Bar Rev. 398, at p. 425; G. Heckman and A. Khoday, “Once More unto the Breach: Confronting the Standard of Review (Again) and the Imperative of Correctness Revi`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 21. `teacher-phrase-supportive-0021`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **1.00**
- Span quality: **repaired**
- Phrase: `the statutory certification process has been widely used under the irpa to settle divergent interpretations or disagreements on legal issues of general importance`

Evidence:
- `mason-argument-citation-083`; citation: `Huruglica v. Canada (Citizenship and Immigration), 2016 FCA 93, [2016] 4 F.C.R. 157, at para. 28`; hash: `64ca9d11053a8db6b17960941d30753b6369ef2cb6bfa718ff0946890ce02272`
  - Proposed evidence: `the statutory certification process has been widely used under the IRPA to settle divergent interpretations or disagreements on legal issues of general importance`
  - Decision context: `ee para. 42).
[144] Second, the certified question in Vavilov arose under different legislation, the Citizenship Act . In the separate and unique context of the IRPA , multiple different ministers, government departments, and agencies, as well as Canada’s largest administrative tribunal (the Immigration and Refugee Board) are charged with independently administering the statutory scheme. In many cases, these separate decision makers are required to interpret the same statutory provisions. While it is beyond the scope of these appeals to exhaustively canvass the scheme of the Citizenship Act , the statutory certification process has been widely used under the IRPA to settle divergent interpretations or disagreements on legal issues of general importance (see Huruglica v. Canada (Citizenship and Immigration), 2016 FCA 93, [2016] 4 F.C.R. 157, at para. 28).
[145] Finally, to say that Vavilov is determinative and that the standard of review for certified questions is reasonableness would contradict the Vavilov framework itself. As I explain below, reasonableness review of certified questions under the IRPA is inconsistent with both Parliament’s intent and the rule of law.
B. Certified Questions Under the IRPA Should Be Recognized as a New Category of Correctness Review
(1) Legislative Intent
[146] In s. 74(d) of the IRPA , Parliament has provided for an “exceptional” appeal (see Pushpanathan, at para. 43) to the Federal Court of Appeal for legal questions certified as “serious question[s] of general importance”. This indicates legislative intent for judicial involvement and a desire to subject these particular questions, as distinct from all others arising under the IRPA more broadly, to appellate standards of review (see Society of Composers, at para. 30; Vavilov, at para. 36). Parliament’s institutional design choice should be respected by the courts.`
  - Offsets repaired: `True`; confidence: `1.00`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 22. `teacher-phrase-supportive-0022`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `this conclusion is consistent with the only prior interpretations of s. 34(1)(e) and its predecessor, s. 19(1)(g) of the immigration act. in x (re), 2017 canlii 146735 (i.r.b. (imm. div.)), member king held that a series of common assaults could not ground inadmissibility under s. 34(1)(e):`

Evidence:
- `mason-argument-citation-095`; citation: `2017 CanLII 146735`; hash: `93279cd64a91dd6bf579d96832613d8e997c9339f592441e149ce353d80287b2`
  - Proposed evidence: `This conclusion is consistent with the only prior interpretations of s. 34(1)(e) and its predecessor, s. 19(1)(g) of the Immigration Act. In X (Re), 2017 CanLII 146735 (I.R.B. (Imm. Div.)), Member King held that a series of common assaults could not ground inadmissibility under s. 34(1)(e):`
  - Decision context: `ludes acts that are below the thresholds set by section 36” (F.C. reasons, Mason, at para. 50). Given the careful wording of s. 36, this cannot have been Parliament’s intention.
[183] Third, I would return to s. 10.5(1) of the Citizenship Act , which also distinguishes between facts described in ss. 34, 35, and 37 of the IRPA and those described in s. 36. This, too, reinforces the fact that inadmissibility under s. 34 is considered among the gravest forms of inadmissibility and that the section should be interpreted as applying only to acts of violence with a nexus to national security.
[184] This conclusion is consistent with the only prior interpretations of s. 34(1)(e) and its predecessor, s. 19(1)(g) of the Immigration Act. In X (Re), 2017 CanLII 146735 (I.R.B. (Imm. Div.)), Member King held that a series of common assaults could not ground inadmissibility under s. 34(1)(e):
I conclude that paragraph 34(1)(e) cannot be interpreted to include the type of one‑on‑one violent acts that exist in this case. While assaults against individuals are undesirable, they cannot be considered to be a threat to the safety of persons in Canada and the security of Canadian society, as contemplated by this section of the IRPA . [para. 42]
[185] Member King also distinguished the circumstances in X (Re) from those before the Federal Court in Moumdjian v. Canada (Security Intelligence Review Committee), [1999] 4 F.C. 624 (C.A.), which were “more obviously related to the security of Canada” and dealt with a conspiracy to assassinate a Turkish diplomat in Canada (paras. 77‑78; see also Al Yamani v. Canada (Solicitor General), [1996] 1 F.C. 174 (T.D.)).
[186] For these reasons, in addition to those identified by my colleague and by Grammond J. in the Federal Court, I would conclude that inadmissibility under s. 34(1)(e) requires a nexus between the relevant act of violence and with national security or the security of Canada. However, it remains the task of administrative decision makers under the IRPA to apply this interpretation going forward, including determining which a`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 23. `teacher-phrase-supportive-0023`

- Proposed treatment: **supportive**
- Support: **1** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `this court held that reviewing courts should derogate from the presumption of reasonableness review where required by (1) a clear indication of legislative intent or (2) the rule of law (para. 10)`

Evidence:
- `mason-argument-citation-067`; citation: `Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653`; hash: `73165598fefe84909d903292aa6623307fceb120a9392df67e850d6f3b1db272`
  - Proposed evidence: `this Court held that reviewing courts should derogate from the presumption of reasonableness review where required by (1) a clear indication of legislative intent or (2) the rule of law (para. 10)`
  - Decision context: `[124] I agree with my colleague’s disposition of these appeals. Inadmissibility under s. 34(1) (e) of the Immigration and Refugee Protection Act , S.C. 2001, c. 27 (“IRPA ”), requires a nexus between the relevant act of violence and with national security or the security of Canada (see paras. 11 and 121). However, I would review the Immigration Appeal Division’s (“IAD”) interpretation of s. 34(1)(e) on a standard of correctness, as submitted by the appellant Mr. Earl Mason and the interveners the Canadian Association of Refugee Lawyers and the Canadian Council for Refugees.
[125] In Canada (Minister of Citizenship and Immigration) v. Vavilov, 2019 SCC 65, [2019] 4 S.C.R. 653, this Court held that reviewing courts should derogate from the presumption of reasonableness review where required by (1) a clear indication of legislative intent or (2) the rule of law (para. 10). In my view, the rule of law requires — and Parliament intended for appellate courts to provide — definitive, correct answers to legal questions certified under s. 74 (d) of the IRPA . By definition, these are questions that transcend the interests of the parties and raise issues of broad significance within Canada’s immigration and refugee protection scheme (see Lunyamila v. Canada (Public Safety and Emergency Preparedness), 2018 FCA 22, [2018] 3 F.C.R. 674, at para. 46).
[126] In Pushpanathan v. Canada (Minister of Citizenship and Immigration), [1998] 1 S.C.R. 982, this Court noted that the certified question regime would be “incoherent” if the standard of review were anything other than correctness (para. 43). This is exemplified by the companion appeals before us. The IAD’s interpretation of s. 34(1)(e) in Mr. Mason’s case, subsequently applied to Mr. Dleiow, would significantly expand the grounds on which foreign nationals or permanent residents may be deported from Canada. It would allow foreign nationals to be returned to countries where they may face persecution, in a manner contrary to Canada’s obligations under the Convention Relating to the Status of Refugees, Can. T.S.`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 24. `teacher-phrase-supportive-0024`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `vavilov is clear that a reviewing court must start its analysis with the reasons of the administrative decision maker; starting with its own perception of the merits may lead a court to slip into correctness review`

Evidence:
- `mason-argument-citation-051`; citation: `Vavilov`; hash: `d562cde8ec947f0a7053212cb238ae88dc8a3745f8021125f41887f22768b8c8`
  - Proposed evidence: `Vavilov is clear that a reviewing court must start its analysis with the reasons of the administrative decision maker; starting with its own perception of the merits may lead a court to slip into correctness review`
  - Decision context: ` the administrator’s interpretation and interfering if the difference is too much” (para. 24). This approach was eschewed in this Court’s decision in Vavilov.
[79] But the Federal Court of Appeal also strayed from Vavilov’s methodology of reasonableness review. The Court of Appeal grafted onto Vavilov an extra step of “conducting a preliminary analysis of the text, context and purpose of the legislation just to understand the lay of the land before . . . examin[ing] the administrators’ reasons” (para. 17). The parties before this Court contended that this preliminary step is inconsistent with Vavilov. The respondent Minister of Citizenship and Immigration — who otherwise agreed with the Court of Appeal’s conclusion — submitted that the Court of Appeal’s approach “should not be adopted”, and urged that “[t]he focus in the reasonableness analysis needs to remain, as this Court has instructed, on the reasons of the decision-maker, and not on a range of potential conclusions to be determined by a reviewing court in the abstract” (R.F., at para. 54). I agree. Vavilov is clear that a reviewing court must start its analysis with the reasons of the administrative decision maker; starting with its own perception of the merits may lead a court to slip into correctness review.
C. Were the Administrative Decisions Reasonable?
[80] I now turn to consider whether the administrative decisions under review reasonably interpreted s. 34(1) (e) of the IRPA as not requiring a nexus with national security or the security of Canada.
[81] In reviewing the IAD’s reasons, I recall this Court’s instruction in Vavilov that a reviewing court should conduct reasonableness review mindful of the impact of the decision on the affected individual. The principle of “responsive justification” means that “[w]here the impact of a decision on an individual’s rights and interests is severe, the reasons provided to that individual must reflect the stakes” (para. 133). Here, the interpretation of s. 34(1)(e) will affect whether two individuals — one of whom has not been convicted of a criminal offence — could be deported from Canada. As this Court has noted, individuals facing deportation may experience “any number of serious life-changing consequences”, including dislocation or permanent separation from their family (R. v. Wong, 2018 SCC 25, [2018] 1 S.C.R. 696, at para. 72, per Wagner J. (as he then was), dissenting). The IAD’s reasons must reflect these stakes.`
  - Offsets repaired: `True`; confidence: `0.95`
- `mason-argument-citation-052`; citation: `Vavilov`; hash: `d562cde8ec947f0a7053212cb238ae88dc8a3745f8021125f41887f22768b8c8`
  - Proposed evidence: `Vavilov is clear that a reviewing court must start its analysis with the reasons of the administrative decision maker; starting with its own perception of the merits may lead a court to slip into correctness review`
  - Decision context: `the administrators’ reasons” (para. 17). The parties before this Court contended that this preliminary step is inconsistent with Vavilov. The respondent Minister of Citizenship and Immigration — who otherwise agreed with the Court of Appeal’s conclusion — submitted that the Court of Appeal’s approach “should not be adopted”, and urged that “[t]he focus in the reasonableness analysis needs to remain, as this Court has instructed, on the reasons of the decision-maker, and not on a range of potential conclusions to be determined by a reviewing court in the abstract” (R.F., at para. 54). I agree. Vavilov is clear that a reviewing court must start its analysis with the reasons of the administrative decision maker; starting with its own perception of the merits may lead a court to slip into correctness review.
C. Were the Administrative Decisions Reasonable?
[80] I now turn to consider whether the administrative decisions under review reasonably interpreted s. 34(1) (e) of the IRPA as not requiring a nexus with national security or the security of Canada.
[81] In reviewing the IAD’s reasons, I recall this Court’s instruction in Vavilov that a reviewing court should conduct reasonableness review mindful of the impact of the decision on the affected individual. The principle of “responsive justification” means that “[w]here the impact of a decision on an individual’s rights and interests is severe, the reasons provided to that individual must reflect the stakes” (para. 133). Here, the interpretation of s. 34(1)(e) will affect whether two individuals — one of whom has not been convicted of a criminal offence — could be deported from Canada. As this Court has noted, individuals facing deportation may experience “any number of serious life-changing consequences”, including dislocation or permanent separation from their family (R. v. Wong, 2018 SCC 25, [2018] 1 S.C.R. 696, at para. 72, per Wagner J. (as he then was), dissenting). The IAD’s reasons must reflect these stakes.`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.
