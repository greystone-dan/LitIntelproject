# Treatment Distillation Review: treatment-distillation-review-20260918

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

- Rules: **19** pending review
- Treatment distribution: `{"supportive": 19}`
- Rules with repaired spans: **19**
- Rules with one evidence item: **0**
- Priority labels requiring direct review: **90**
- Priority treatment distribution: `{"absent": 7, "distinguishing": 1, "supportive": 82}`
- Full source artifact: `data\eval\treatment_distillation_candidate.json`

## Review Queue

## Priority Labels: Start Here

Review these first 10 items. The JSON packet contains all 90 priority labels.

- `citation-context-0001`; proposed **supportive**; confidence **0.95**; citation: `Piekut v. Canada (National Revenue), 2025 SCC 13, at para. 45`
  - Proposed evidence: `see Piekut v. Canada (National Revenue), 2025 SCC 13, at para. 45`
  - Decision context: `[80] First, while the text is an important indicator of legislative intent, it is not in itself determinative of the meaning of a statutory provision (see Piekut v. Canada (National Revenue), 2025 SCC 13, at para. 45, citing R. v. Alex, 2017 SCC 37, [2017] 1 S.C.R. 967, at para. 31; R. v. Wilson, 2025 SCC 32, at para. 34). Even words that appear clear on their face may reveal a different meaning when viewed in their full context and in light of their purpose (see La Presse, at para. 23, citing Montréal (City) v. 2952-1366 Québec Inc., 2005 SCC 62, [2005] 3 S.C.R. 141, at para. 10). This is a necessary and well-accepted feature of the modern approach (2952-1366 Québec, at para. 10), which represented a departure from an analysis centred on whether text is plain or ambiguous towards a broader search for legislative meaning (see R. Sullivan, The Construction of Statutes (7th ed. 2022), at § 2.04; Côté and Devinat, at paras. 155‑60). It is a methodological mistake — a mistake that can lead the reader to fall into a reviewable error of law — to end the interpretative exercise by concluding the perceived meaning of the text to be plain. It is the meaning of the provision of the statute and its clarity that is at issue, informed by its text, context and purpose. The meaning assigned to plain text may coincide with the true statutory meaning, but it is perilous to assume that it does without undertaki`
  - Offsets repaired: `True`; source hash: `3a911f73335cac39edd17ee63109fa648d8219696b07c55e139b3464b56a045f`

- `citation-context-0008`; proposed **supportive**; confidence **0.95**; citation: `R. v. Khill, 2021 SCC 37, [2021] 2 S.C.R. 948, at para. 111`
  - Proposed evidence: `see R. v. Khill, 2021 SCC 37, [2021] 2 S.C.R. 948, at para. 111`
  - Decision context: `[82] Third, extrinsic aids like Hansard are relevant to the exercise of discerning legislative intent, but should be treated with caution and not be given undue weight in the interpretative exercise (see R. v. Khill, 2021 SCC 37, [2021] 2 S.C.R. 948, at para. 111; see also Wilson, at para. 44; R. v. Safarzadeh-Markhali, 2016 SCC 14, [2016] 1 S.C.R. 180, at para. 36). Statements of individual members can be imperfect indicators of what the legislature as a whole intended (see Sullivan, at §§ 23.03[2][c] and 23.03[4][d]).`
  - Offsets repaired: `True`; source hash: `60d02d584b3eb8f78e17776d81f86b505b4c15360f0c39202bf61b1ce930d988`

- `citation-context-0014`; proposed **supportive**; confidence **0.95**; citation: `tribunal`
  - Proposed evidence: `le tribunal peut rendre une ordonnance de confiscation`
  - Decision context: `u moment du procès, des biens obtenus par la commission de l’infraction :
(a) is before the court or has been detained so that it can be immediately dealt with, and
a) d’une part, sont devant le tribunal ou sont détenus de façon à être disponibles immédiatement;
(b) will not be required as evidence in any other proceedings,
b) d’autre part, ne seront pas nécessaires à titre de preuve dans d’autres procédures,
section 490 does not apply in respect of the property and the court shall make an order under subsection (2) in respect of the property.
l’article 490 ne s’applique pas à ces biens et le tribunal rend une ordonnance en vertu du paragraphe (2) à l’égard de ceux-ci.
Section 16(2) CDSA reads as follows:
(2) Subject to sections 18 to 19.1, if the evidence does not establish to the satisfaction of the court that property in respect of which an order of forfeiture would otherwise be made under subsection (1) is related to the commission of the designated substance offence of which a person is convicted or discharged, but the court is satisfied, beyond a reasonable doubt, that the property is non-chemical offence-related property, the court may make an order of forfeiture under subsection (1) in relation to that property.
(2) Sous réserve des articles 18 à 19.1, le tribunal peut rendre une ordonnance de confiscation aux termes du paragraphe (1) à l’égard de biens dont il n’est pas convaincu qu’ils sont liés à la perpétration de l’infraction désignée pour laquelle la personne a été condamnée — ou à l’égard de laquelle elle a été absoute — s’il est convaincu, hors de tout doute raisonnable, qu’il s’agit de biens infractionnels non-chimiques.`
  - Offsets repaired: `True`; source hash: `7c76c67974d293e5d04e04cc59aba2f86222e56a5818bfaddc60941aa9122100`

- `citation-context-0015`; proposed **supportive**; confidence **0.95**; citation: `tribunal`
  - Proposed evidence: `le tribunal rend une ordonnance en vertu du paragraphe (2)`
  - Decision context: `red as evidence in any other proceedings,
b) d’autre part, ne seront pas nécessaires à titre de preuve dans d’autres procédures,
section 490 does not apply in respect of the property and the court shall make an order under subsection (2) in respect of the property.
l’article 490 ne s’applique pas à ces biens et le tribunal rend une ordonnance en vertu du paragraphe (2) à l’égard de ceux-ci.
Section 16(2) CDSA reads as follows:
(2) Subject to sections 18 to 19.1, if the evidence does not establish to the satisfaction of the court that property in respect of which an order of forfeiture would otherwise be made under subsection (1) is related to the commission of the designated substance offence of which a person is convicted or discharged, but the court is satisfied, beyond a reasonable doubt, that the property is non-chemical offence-related property, the court may make an order of forfeiture under subsection (1) in relation to that property.
(2) Sous réserve des articles 18 à 19.1, le tribunal peut rendre une ordonnance de confiscation aux termes du paragraphe (1) à l’égard de biens dont il n’est pas convaincu qu’ils sont liés à la perpétration de l’infraction désignée pour laquelle la personne a été condamnée — ou à l’égard de laquelle elle a été absoute — s’il est convaincu, hors de tout doute raisonnable, qu’il s’agit de biens infractionnels non-chimiques.`
  - Offsets repaired: `True`; source hash: `713e709438ef9b42d12ecef738c6f987f6978c4ca0219239b2697a0cbe07a0b3`

- `citation-context-0021`; proposed **supportive**; confidence **0.95**; citation: `R. v. Witvoet, 2015 ABCA 152`
  - Proposed evidence: `Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA).`
  - Decision context: `[87] Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA). Forfeiture is still available if the Crown can satisfy the court beyond a reasonable doubt that the property is otherwise proceeds of crime or offence-related property (see generally Craig, at para. 42; Lavigne, at para. 17; R. v. Lanteigne (1994), 156 N.B.R. (2d) 17 (Q.B.), at para. 29; R. v. Shearer, 2015 ONCA 355, 336 O.A.C. 30, at paras. 12-13; Croussette v. R., 2017 QCCA 1040, at para. 10 (Lexis); see also Procureur général du Québec v. Hydrobec (9031-7579 Québec inc.), 2022 QCCA 534, at para. 7; R. v. Witvoet, 2015 ABCA 152, 600 A.R. 200, at para. 27; Trecartin, at para. 31; Bergevin and Darbouze, at p. 65). In contrast to subsection (1) of each provision, which specifies that the court “shall” order forfeiture, subsection (2) says that the court “may” order forfeiture, indicating greater discretion for the sentencing court.`
  - Offsets repaired: `True`; source hash: `61b4d43b9f1b6005450e4b350e9a7951cfd461104fcc8988b3efb90ceb20e58c`

- `citation-context-0022`; proposed **supportive**; confidence **0.95**; citation: `Trecartin, at para. 31`
  - Proposed evidence: `Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA).`
  - Decision context: `[87] Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA). Forfeiture is still available if the Crown can satisfy the court beyond a reasonable doubt that the property is otherwise proceeds of crime or offence-related property (see generally Craig, at para. 42; Lavigne, at para. 17; R. v. Lanteigne (1994), 156 N.B.R. (2d) 17 (Q.B.), at para. 29; R. v. Shearer, 2015 ONCA 355, 336 O.A.C. 30, at paras. 12-13; Croussette v. R., 2017 QCCA 1040, at para. 10 (Lexis); see also Procureur général du Québec v. Hydrobec (9031-7579 Québec inc.), 2022 QCCA 534, at para. 7; R. v. Witvoet, 2015 ABCA 152, 600 A.R. 200, at para. 27; Trecartin, at para. 31; Bergevin and Darbouze, at p. 65). In contrast to subsection (1) of each provision, which specifies that the court “shall” order forfeiture, subsection (2) says that the court “may” order forfeiture, indicating greater discretion for the sentencing court.`
  - Offsets repaired: `True`; source hash: `61b4d43b9f1b6005450e4b350e9a7951cfd461104fcc8988b3efb90ceb20e58c`

- `citation-context-0023`; proposed **supportive**; confidence **0.90**; citation: `Craig`
  - Proposed evidence: `In Craig, this Court recognized that forfeiture pursuant to s. 16 CDSA “may apply to property owned by a complicit individual who is neither sentenced nor even charged with an offence” (para. 41).`
  - Decision context: `[90] Second, I also agree with the Crown that the property need not be the offender’s property or that of the person who was tried (A.F., at paras. 62-63; see also German, at § 15:14). The language of the provisions does not expressly limit their scope in this way. In Craig, this Court recognized that forfeiture pursuant to s. 16 CDSA “may apply to property owned by a complicit individual who is neither sentenced nor even charged with an offence” (para. 41). Significantly, the 2018 change of “biens d’un contrevenant” to “biens” in the French text of s. 462.37(2) supports the view that Parliament’s intention is that forfeiture orders may target property that does not belong to the offender whose conviction or discharge triggered the application of the provision (see An Act to amend the Controlled Drugs and Substances Act and to make related amendments to other Acts, S.C. 2017, c. 7, s. 59).`
  - Offsets repaired: `True`; source hash: `9fd5ca83040c80d053b26160310552605e89f16a8014dd9a49ec28e8c0282bb8`

- `citation-context-0025`; proposed **supportive**; confidence **0.90**; citation: `Hape, at para. 41`
  - Proposed evidence: `It is important not to lose sight of the fact that, while the scope of the property subject to forfeiture is broader than an accused’s finding of guilt, an accused’s finding of guilt (s. 462.37 Cr. C.; s. 16 CDSA) or trial for an offence (s. 491.1 Cr. C.) is still required to engage the forfeiture power in the first place.`
  - Decision context: `[94] It is important not to lose sight of the fact that, while the scope of the property subject to forfeiture is broader than an accused’s finding of guilt, an accused’s finding of guilt (s. 462.37 Cr. C.; s. 16 CDSA) or trial for an offence (s. 491.1 Cr. C.) is still required to engage the forfeiture power in the first place. Denying the existence of some requisite connection between the proceedings that engage forfeiture and the subject property would create an expansive forfeiture power that Parliament could not have intended. It would mean that the Crown could ground the forfeiture of virtually any proceeds of crime or offence-related property on any unrelated trial or finding of guilt, and could undesirably burden an accused’s criminal proceedings with wholly unrelated matters. As Doherty, Feldman and LaForme JJ.A. put it in Hape, at para. 41, this kind of broad unstructured forfeiture power and loose connection to criminal proceedings would raise serious concerns for our system of justice:
The Crown’s submission that it can introduce entirely new allegations, unrelated to those advanced at trial, as part of a forfeiture hearing during the sentencing proceedings raises serious constitutional problems. The forfeiture provisions cannot be read so as to allow the Crown to circumvent the comprehensive process complete with constitutional protections, associated with the charging and prosecuting of criminal allegations. The section does not contemplate the forfeiture of property that was not the subject matter of the criminal allegation made at trial.`
  - Offsets repaired: `True`; source hash: `2bd05230e5855d87d5b846cccfa7af253192e54f5b39f46b0bdb2abfaec9763f`

- `citation-context-0027`; proposed **supportive**; confidence **0.90**; citation: `R. v. Dolbec, 2011 QCCA 1610, at para. 27`
  - Proposed evidence: `This does not mean that all the evidence justifying forfeiture need be adduced at trial, but merely that there is some connection between the property and the criminal allegations underlying the information or indictment that circumscribes the criminal liability proceedings.`
  - Decision context: `[95] I therefore agree with the Court of Appeal for Ontario in Hape that some nexus to criminal liability proceedings is required (para. 40; see also R. v. Dolbec, 2011 QCCA 1610, at para. 27). Specifically, while no direct link between the property and the finding of guilt or the accused is necessary, there must be a sufficient nexus between the property and the criminal allegations underlying the proceedings in which the forfeiture power is triggered. This does not mean that all the evidence justifying forfeiture need be adduced at trial, but merely that there is some connection between the property and the criminal allegations underlying the information or indictment that circumscribes the criminal liability proceedings. The property must reasonably form part of the broader context surrounding the allegations. For example, in this case, the court that heard Manh Hung Nguyen’s guilty plea could have considered forfeiture of property if there was a reasonable basis to believe it was connected to the broader alleged cannabis production enterprise in respect of which he was charged. Forfeiture of the property could have been considered even if that property was not directly tied to Manh Hung Nguyen himself or to the offence of which he was found guilty.`
  - Offsets repaired: `True`; source hash: `d7f66cc646b410c36d2330ddfaea229cefe7900f1296351fb9aada36381bd3c7`

- `citation-context-0030`; proposed **supportive**; confidence **0.95**; citation: `Laroche, at paras. 59-62`
  - Proposed evidence: `As discussed above, subsection (2) broadens the basis on which these orders under s. 462.37(1) may be made, by clarifying that forfeiture is available even if the property was not obtained through the commission of the offence on which there is a finding of guilt.`
  - Decision context: `[99] As discussed above, subsection (2) broadens the basis on which these orders under s. 462.37(1) may be made, by clarifying that forfeiture is available even if the property was not obtained through the commission of the offence on which there is a finding of guilt. But the provision specifies that this remains an “order of forfeiture under subsection (1)” (“ordonnance de confiscation aux termes du paragraphe (1)”), in other words one that must be made by the sentencing court (see Laroche, at paras. 59-62, citing Lanteigne, at paras. 29-30 and 32; see also Arif v. R., 2020 QCCA 848, at para. 126). I recall that s. 462.37(2) provides:
(2) If the evidence does not establish to the satisfaction of the court that property in respect of which an order of forfeiture would otherwise be made under subsection (1) was obtained through the commission of the designated offence of which the offender is convicted or discharged, but the court is satisfied, beyond a reasonable doubt, that the property is proceeds of crime, the court may make an order of forfeiture under subsection (1) in relation to that property.
(2) Le tribunal peut rendre une ordonnance de confiscation aux termes du paragraphe (1) à l’égard de biens dont il n’est pas convaincu qu’ils ont été obtenus par la perpétration de l’infraction désignée pour laquelle le contrevenant a été condamné — ou à l’égard de laquelle il a été absous — s’il est convaincu, hors de tout doute raisonnable, qu’il s’agit de produits de la criminalité.`
  - Offsets repaired: `True`; source hash: `b5a018dedbe189e429b327f5be97e785ca8d359acdbcaade1fdcd83dba6ddc66`

## Remaining Review Material

After the starting batch, continue with the remaining priority labels and then the repeated-rule queue below.

## Repeated-Rule Queue

### 1. `teacher-phrase-supportive-0001`

- Proposed treatment: **supportive**
- Support: **3** examples; mean confidence **0.92**
- Span quality: **repaired**
- Phrase: `because the designation of the united states of america is not and/or was not at the time of the decision under review in conformity with ss. 102(1)(a), 102(2) and 102(3) of the immigration and refugee protection act;`

Evidence:
- `citation-context-1018`; citation: `Canadian Council for Refugees`; hash: `75176d851ef78ec6b21a76fd1774997dd1ebb5454ff11fb4d493a47a78d282f1`
  - Proposed evidence: `because the designation of the United States of America is not and/or was not at the time of the decision under review in conformity with ss. 102(1)(a), 102(2) and 102(3) of the Immigration and Refugee Protection Act;`
  - Decision context: `rd-de-Lacolle, Quebec, POE.
[25] On February 3, 2017, Ms. Al Nahass was told she and her children were ineligible because they were attempting to enter Canada from the US. While Ms. Al Nahass was at Saint-Bernard-de-Lacolle, she managed to contact a lawyer who filed an emergency stay of removal application on behalf of the family. The stay was granted, following which the family was granted TRPs allowing them to remain in Canada. The family has since been granted permanent resident status.
Public Interest Parties
[26] On December 11, 2017, Justice Diner granted public interest standing to the Canadian Council for Refugees, Amnesty International, and the Canadian Council of Churches on the grounds that the application for judicial review “raises a serious justiciable issue in which the Organizations have a genuine interest” (Canadian Council for Refugees et al. v Canada (Immigration, Refugees and Citizenship) 2017 FC 1131 at para 74).
III. CONSOLIDATION ORDER
[27] On April 12, 2018, Justice Diner ordered these three applications be consolidated and heard together (Canadian Council for Refugees et al. v Canada (Immigration, Refugees and Citizenship), 2018 FC 396 at para 39).
IV. RELIEF SOUGHT
[28] In their Applications for Judicial Review, the Applicants each phrase the requested relief slightly differently, however, they all seek the following common relief:
An order that the decisions of the Officers be set aside and the individual Applicants’ claims for refugee protection be found eligible and referred to the Refugee Protection Division for determination;
A declaration that s. 159.3 of the Immigration and Refugee Protection Regulations is ultra vires or otherwise unlawful because the designation of the United States of America is not and/or was not at the time of the decision under review in conformity with ss. 102(1)(a), 102(2) and 102(3) of the Immigration and Refugee Protection Act;
A declaration that s. 159.3 of the Regulations is inconsistent with Canada’s international obligations under the Refugee Convention and the Convention Against Torture;
A declaration that s. 159.3 of the Regulations is of no force or effect pursuant to section 52 of the Constitution Act, 1982, because it violates section 7 and/or section 15(1) of the Charter of Rights and Freedoms;
A declaration that s. 101(1)(e) of the IRPA is of no force or effect pursuant to section 52 of the Constitution Act, 1982, because it violates section 7 and/or section 15(1) of the Charter of Rights and Freedoms.
V. NOTICE OF CONSTITUTIONAL QUESTION
[29] The Applicants served a Notice of Constitutional question pursuant to `
  - Offsets repaired: `True`; confidence: `0.92`
- `citation-context-1019`; citation: `Canadian Council for Refugees et al. v Canada (Immigration, Refugees and Citizenship) 2017 FC 1131 at para 74`; hash: `81c1cb6fceea5f60a77fe3a00e10a63b7777e227e2c930e3c66cf96b3a047824`
  - Proposed evidence: `because the designation of the United States of America is not and/or was not at the time of the decision under review in conformity with ss. 102(1)(a), 102(2) and 102(3) of the Immigration and Refugee Protection Act;`
  - Decision context: ` to contact a lawyer who filed an emergency stay of removal application on behalf of the family. The stay was granted, following which the family was granted TRPs allowing them to remain in Canada. The family has since been granted permanent resident status.
Public Interest Parties
[26] On December 11, 2017, Justice Diner granted public interest standing to the Canadian Council for Refugees, Amnesty International, and the Canadian Council of Churches on the grounds that the application for judicial review “raises a serious justiciable issue in which the Organizations have a genuine interest” (Canadian Council for Refugees et al. v Canada (Immigration, Refugees and Citizenship) 2017 FC 1131 at para 74).
III. CONSOLIDATION ORDER
[27] On April 12, 2018, Justice Diner ordered these three applications be consolidated and heard together (Canadian Council for Refugees et al. v Canada (Immigration, Refugees and Citizenship), 2018 FC 396 at para 39).
IV. RELIEF SOUGHT
[28] In their Applications for Judicial Review, the Applicants each phrase the requested relief slightly differently, however, they all seek the following common relief:
An order that the decisions of the Officers be set aside and the individual Applicants’ claims for refugee protection be found eligible and referred to the Refugee Protection Division for determination;
A declaration that s. 159.3 of the Immigration and Refugee Protection Regulations is ultra vires or otherwise unlawful because the designation of the United States of America is not and/or was not at the time of the decision under review in conformity with ss. 102(1)(a), 102(2) and 102(3) of the Immigration and Refugee Protection Act;
A declaration that s. 159.3 of the Regulations is inconsistent with Canada’s international obligations under the Refugee Convention and the Convention Against Torture;
A declaration that s. 159.3 of the Regulations is of no force or effect pursuant to section 52 of the Constitution Act, 1982, because it violates section 7 and/or section 15(1) of the Charter of Rights and Freedoms;
A declaration that s. 101(1)(e) of the IRPA is of no force or effect pursuant to section 52 of the Constitution Act, 1982, because it violates section 7 and/or section 15(1) of the Charter of Rights and Freedoms.
V. NOTICE OF CONSTITUTIONAL QUESTION
[29] The Applicants served a Notice of Constitutional question pursuant to section 57 of the Federal Courts Act, RSC 1985 c F-7, on the Attorney General of Canada and each of the Attorneys General for the Provinces and Territories. Apart from the Attorney General of Canada, none of the Attorneys General responded. The Notice of Constitutional question stated:
The Applicants intend to ques`
  - Offsets repaired: `True`; confidence: `0.92`
- `citation-context-1020`; citation: `Canadian Council for Refugees et al. v Canada (Immigration, Refugees and Citizenship), 2018 FC 396 at para 39`; hash: `35d9b4c6174f885d55cfa378d85433b80a67b31627215f23e13c681f94d56318`
  - Proposed evidence: `because the designation of the United States of America is not and/or was not at the time of the decision under review in conformity with ss. 102(1)(a), 102(2) and 102(3) of the Immigration and Refugee Protection Act;`
  - Decision context: `sident status.
Public Interest Parties
[26] On December 11, 2017, Justice Diner granted public interest standing to the Canadian Council for Refugees, Amnesty International, and the Canadian Council of Churches on the grounds that the application for judicial review “raises a serious justiciable issue in which the Organizations have a genuine interest” (Canadian Council for Refugees et al. v Canada (Immigration, Refugees and Citizenship) 2017 FC 1131 at para 74).
III. CONSOLIDATION ORDER
[27] On April 12, 2018, Justice Diner ordered these three applications be consolidated and heard together (Canadian Council for Refugees et al. v Canada (Immigration, Refugees and Citizenship), 2018 FC 396 at para 39).
IV. RELIEF SOUGHT
[28] In their Applications for Judicial Review, the Applicants each phrase the requested relief slightly differently, however, they all seek the following common relief:
An order that the decisions of the Officers be set aside and the individual Applicants’ claims for refugee protection be found eligible and referred to the Refugee Protection Division for determination;
A declaration that s. 159.3 of the Immigration and Refugee Protection Regulations is ultra vires or otherwise unlawful because the designation of the United States of America is not and/or was not at the time of the decision under review in conformity with ss. 102(1)(a), 102(2) and 102(3) of the Immigration and Refugee Protection Act;
A declaration that s. 159.3 of the Regulations is inconsistent with Canada’s international obligations under the Refugee Convention and the Convention Against Torture;
A declaration that s. 159.3 of the Regulations is of no force or effect pursuant to section 52 of the Constitution Act, 1982, because it violates section 7 and/or section 15(1) of the Charter of Rights and Freedoms;
A declaration that s. 101(1)(e) of the IRPA is of no force or effect pursuant to section 52 of the Constitution Act, 1982, because it violates section 7 and/or section 15(1) of the Charter of Rights and Freedoms.
V. NOTICE OF CONSTITUTIONAL QUESTION
[29] The Applicants served a Notice of Constitutional question pursuant to section 57 of the Federal Courts Act, RSC 1985 c F-7, on the Attorney General of Canada and each of the Attorneys General for the Provinces and Territories. Apart from the Attorney General of Canada, none of the Attorneys General responded. The Notice of Constitutional question stated:
The Applicants intend to question the constitutional validity of the combined effect of s. 101(1)(e) of the Immigration and Refugee Protection Act (“the IRPA”) and s. 159.3 of the Immigration and Refugee`
  - Offsets repaired: `True`; confidence: `0.92`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 2. `teacher-phrase-supportive-0002`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `citing sun indalex finance, llc v. united steelworkers, 2013 scc 6, [2013] 1 s.c.r. 271, at para. 174`

Evidence:
- `citation-context-0531`; citation: `Sun Indalex Finance, LLC v. United Steelworkers, 2013 SCC 6, [2013] 1 S.C.R. 271, at para. 174`; hash: `fab90a9891806c73d176abc2bd7c1137b52fed4bac717673f8463d241f8ca923`
  - Proposed evidence: `citing Sun Indalex Finance, LLC v. United Steelworkers, 2013 SCC 6, [2013] 1 S.C.R. 271, at para. 174`
  - Decision context: `[81] Second, the overall purpose or goal of a legislative scheme informs the analysis, although one must be mindful that the legislature’s intent is rarely that one purpose be pursued at all costs. Other interests and subsidiary purposes, revealed through a careful analysis of the legislative scheme and the means the legislature has chosen to achieve its goal, are also important in ascertaining the intended meaning (R. v. Rafilovich, 2019 SCC 51, [2019] 3 S.C.R. 838, at para. 30, citing Sun Indalex Finance, LLC v. United Steelworkers, 2013 SCC 6, [2013] 1 S.C.R. 271, at para. 174). The aim is to achieve a fitting harmony between these various purposes in a manner that best accords with the legislature’s intent (see Sullivan, at § 9.02[5]; A. Barak, Purposive Interpretation in Law (2005), at p. 116; Telus, at para. 32).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0532`; citation: `Telus, at para. 32`; hash: `fab90a9891806c73d176abc2bd7c1137b52fed4bac717673f8463d241f8ca923`
  - Proposed evidence: `citing Sun Indalex Finance, LLC v. United Steelworkers, 2013 SCC 6, [2013] 1 S.C.R. 271, at para. 174`
  - Decision context: `[81] Second, the overall purpose or goal of a legislative scheme informs the analysis, although one must be mindful that the legislature’s intent is rarely that one purpose be pursued at all costs. Other interests and subsidiary purposes, revealed through a careful analysis of the legislative scheme and the means the legislature has chosen to achieve its goal, are also important in ascertaining the intended meaning (R. v. Rafilovich, 2019 SCC 51, [2019] 3 S.C.R. 838, at para. 30, citing Sun Indalex Finance, LLC v. United Steelworkers, 2013 SCC 6, [2013] 1 S.C.R. 271, at para. 174). The aim is to achieve a fitting harmony between these various purposes in a manner that best accords with the legislature’s intent (see Sullivan, at § 9.02[5]; A. Barak, Purposive Interpretation in Law (2005), at p. 116; Telus, at para. 32).`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 3. `teacher-phrase-supportive-0003`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `contrary to the 1951 convention relating to the status of refugees, 28 july 1951, 189 unts at 137 (refugee convention or rt) and contrary to the united nations convention against torture and other cruel, inhumane or degrading treatment or punishment (cat, collectively referred to as the conventions).`

Evidence:
- `citation-context-1013`; citation: `United States`; hash: `ba15e0b256b6ff47a18dbe4c91c4aded247f31831c31b3f6e4534ae40b17b867`
  - Proposed evidence: `contrary to the 1951 Convention Relating to the Status of Refugees, 28 July 1951, 189 UNTS at 137 (Refugee Convention or RT) and contrary to the United Nations Convention Against Torture and Other Cruel, Inhumane or Degrading Treatment or Punishment (CAT, collectively referred to as the Conventions).`
  - Decision context: `I. INTRODUCTION
[1] The Applicants challenge the validity and the constitutionality of the legislation implementing the Agreement between the Government of Canada and the Government of the United States of America For Cooperation in the Examination of Refugee Status Claims from Nationals of Third Countries (referred to as the “Safe Third Country Agreement” or “STCA”). The Applicants allege that by returning ineligible refugee claimants to the United States (US), Canada exposes them to risks in the form of detention, refoulement, and other violations of their rights contrary to the 1951 Convention Relating to the Status of Refugees, 28 July 1951, 189 UNTS at 137 (Refugee Convention or RT) and contrary to the United Nations Convention Against Torture and Other Cruel, Inhumane or Degrading Treatment or Punishment (CAT, collectively referred to as the Conventions).
[2] The Safe Third Country Agreement is given effect by s. 101(1)(e) of the Immigration and Refugee Protection Act, SC 2001 c 27 (IRPA), and by s. 159.3 of the Immigration and Refugee Protection Regulations SOR/2002-227 (IRPR or the Regulations) which in 2004 designated the US a “safe third country”.
[3] The Safe Third Country Agreement operates by deeming those who arrive at a Canada land Port of Entry (POE) from the US ineligible to make a refugee claim in Canada. These ineligibility provisions apply to a narrow category of refugee claimants – only those arriving from the US at a Canada land POE. Claimants arriving from the US by air, by sea or between land POEs, are eligible to have their refugee claims referred to the Refugee Protection Division (RPD) for assessment.
[4] Each of the individual Applicants, who are citizens of El Salvador, Ethiopia, and Syria, arrived at a Canada land POE from the US and sought refugee protection. The Applicants, ABC and her children, are from El Salvador. Their refugee claim relates to gang violence and gender-based persecution. The Applicant, Ms. Mustefa is a Muslim woman from Ethiopia who was detained after her attempt to enter Canada from th`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1014`; citation: `United States`; hash: `7e322c31f8b417b9697c5a2bc1651ceaf15d1f8a660d8b0b98eca2100d250906`
  - Proposed evidence: `contrary to the 1951 Convention Relating to the Status of Refugees, 28 July 1951, 189 UNTS at 137 (Refugee Convention or RT) and contrary to the United Nations Convention Against Torture and Other Cruel, Inhumane or Degrading Treatment or Punishment (CAT, collectively referred to as the Conventions).`
  - Decision context: `I. INTRODUCTION
[1] The Applicants challenge the validity and the constitutionality of the legislation implementing the Agreement between the Government of Canada and the Government of the United States of America For Cooperation in the Examination of Refugee Status Claims from Nationals of Third Countries (referred to as the “Safe Third Country Agreement” or “STCA”). The Applicants allege that by returning ineligible refugee claimants to the United States (US), Canada exposes them to risks in the form of detention, refoulement, and other violations of their rights contrary to the 1951 Convention Relating to the Status of Refugees, 28 July 1951, 189 UNTS at 137 (Refugee Convention or RT) and contrary to the United Nations Convention Against Torture and Other Cruel, Inhumane or Degrading Treatment or Punishment (CAT, collectively referred to as the Conventions).
[2] The Safe Third Country Agreement is given effect by s. 101(1)(e) of the Immigration and Refugee Protection Act, SC 2001 c 27 (IRPA), and by s. 159.3 of the Immigration and Refugee Protection Regulations SOR/2002-227 (IRPR or the Regulations) which in 2004 designated the US a “safe third country”.
[3] The Safe Third Country Agreement operates by deeming those who arrive at a Canada land Port of Entry (POE) from the US ineligible to make a refugee claim in Canada. These ineligibility provisions apply to a narrow category of refugee claimants – only those arriving from the US at a Canada land POE. Claimants arriving from the US by air, by sea or between land POEs, are eligible to have their refugee claims referred to the Refugee Protection Division (RPD) for assessment.
[4] Each of the individual Applicants, who are citizens of El Salvador, Ethiopia, and Syria, arrived at a Canada land POE from the US and sought refugee protection. The Applicants, ABC and her children, are from El Salvador. Their refugee claim relates to gang violence and gender-based persecution. The Applicant, Ms. Mustefa is a Muslim woman from Ethiopia who was detained after her attempt to enter Canada from th`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 4. `teacher-phrase-supportive-0004`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `it purports to provide a “complete scheme” for this purpose`

Evidence:
- `citation-context-0573`; citation: `Raponi, at para. 28`; hash: `0c2261de4da9de1c8cefde6e5a37f94e1c24fce772ca9e153e53f8a831797b41`
  - Proposed evidence: `It purports to provide a “complete scheme” for this purpose`
  - Decision context: `t that property to judicial supervision under s. 490 (ss. 489.1(1)(b) and 490(1) Cr. C.; see N. Hasan et al., Search and Seizure (2021), at pp. 538-39). The purpose of s. 490 is to ensure that courts supervising seized property can carefully balance the private interests in that property against the public need for that property to be detained in pursuit of investigating and prosecuting crime (see Hollaman, at paras. 97-98; Breton, at para. 62; see also Uniform Law Conference of Canada, at paras. 12-13; Further Detention of Things Seized (Re), 2024 BCSC 354, at para. 15; Ayotte, at para. 51). It purports to provide a “complete scheme” for this purpose (Raponi, at para. 28; see also paras. 8‑15 and 30; R. v. Backhouse (2005), 195 O.A.C. 80, at para. 111). Section 490 also applies with necessary modifications to property that has not actually been seized but is nonetheless subject to judicial supervision, such as property subject to a restraint order, where this is contemplated by statute (see, e.g., s. 490.9(1) Cr. C.; s. 15(1) CDSA).`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-0574`; citation: `R. v. Backhouse (2005), 195 O.A.C. 80, at para. 111`; hash: `c1e65ffa1d33d13309c535903f284871d6d83322be3c4490bee00313757e80a8`
  - Proposed evidence: `It purports to provide a “complete scheme” for this purpose`
  - Decision context: `t that property to judicial supervision under s. 490 (ss. 489.1(1)(b) and 490(1) Cr. C.; see N. Hasan et al., Search and Seizure (2021), at pp. 538-39). The purpose of s. 490 is to ensure that courts supervising seized property can carefully balance the private interests in that property against the public need for that property to be detained in pursuit of investigating and prosecuting crime (see Hollaman, at paras. 97-98; Breton, at para. 62; see also Uniform Law Conference of Canada, at paras. 12-13; Further Detention of Things Seized (Re), 2024 BCSC 354, at para. 15; Ayotte, at para. 51). It purports to provide a “complete scheme” for this purpose (Raponi, at para. 28; see also paras. 8‑15 and 30; R. v. Backhouse (2005), 195 O.A.C. 80, at para. 111). Section 490 also applies with necessary modifications to property that has not actually been seized but is nonetheless subject to judicial supervision, such as property subject to a restraint order, where this is contemplated by statute (see, e.g., s. 490.9(1) Cr. C.; s. 15(1) CDSA).`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 5. `teacher-phrase-supportive-0005`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `may make an order of forfeiture`

Evidence:
- `citation-context-0032`; citation: `Arif v. R., 2020 QCCA 848, at para. 126`; hash: `b5a018dedbe189e429b327f5be97e785ca8d359acdbcaade1fdcd83dba6ddc66`
  - Proposed evidence: `may make an order of forfeiture`
  - Decision context: `[99] As discussed above, subsection (2) broadens the basis on which these orders under s. 462.37(1) may be made, by clarifying that forfeiture is available even if the property was not obtained through the commission of the offence on which there is a finding of guilt. But the provision specifies that this remains an “order of forfeiture under subsection (1)” (“ordonnance de confiscation aux termes du paragraphe (1)”), in other words one that must be made by the sentencing court (see Laroche, at paras. 59-62, citing Lanteigne, at paras. 29-30 and 32; see also Arif v. R., 2020 QCCA 848, at para. 126). I recall that s. 462.37(2) provides:
(2) If the evidence does not establish to the satisfaction of the court that property in respect of which an order of forfeiture would otherwise be made under subsection (1) was obtained through the commission of the designated offence of which the offender is convicted or discharged, but the court is satisfied, beyond a reasonable doubt, that the property is proceeds of crime, the court may make an order of forfeiture under subsection (1) in relation to that property.
(2) Le tribunal peut rendre une ordonnance de confiscation aux termes du paragraphe (1) à l’égard de biens dont il n’est pas convaincu qu’ils ont été obtenus par la perpétration de l’infraction désignée pour laquelle le contrevenant a été condamné — ou à l’égard de laquelle il a été absous — s’il est convaincu, hors de tout doute raisonnable, qu’il s’agit de produits de la criminalité.`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-0033`; citation: `tribunal`; hash: `2b359ea05dc9451ea8a5d2e99833ada347565db42bf59f5af3becf66cf67b588`
  - Proposed evidence: `may make an order of forfeiture`
  - Decision context: `s one that must be made by the sentencing court (see Laroche, at paras. 59-62, citing Lanteigne, at paras. 29-30 and 32; see also Arif v. R., 2020 QCCA 848, at para. 126). I recall that s. 462.37(2) provides:
(2) If the evidence does not establish to the satisfaction of the court that property in respect of which an order of forfeiture would otherwise be made under subsection (1) was obtained through the commission of the designated offence of which the offender is convicted or discharged, but the court is satisfied, beyond a reasonable doubt, that the property is proceeds of crime, the court may make an order of forfeiture under subsection (1) in relation to that property.
(2) Le tribunal peut rendre une ordonnance de confiscation aux termes du paragraphe (1) à l’égard de biens dont il n’est pas convaincu qu’ils ont été obtenus par la perpétration de l’infraction désignée pour laquelle le contrevenant a été condamné — ou à l’égard de laquelle il a été absous — s’il est convaincu, hors de tout doute raisonnable, qu’il s’agit de produits de la criminalité.`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 6. `teacher-phrase-supportive-0006`

- Proposed treatment: **supportive**
- Support: **3** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `must order forfeiture`

Evidence:
- `citation-context-0038`; citation: `2022 SCC 48`; hash: `ea00e4c54a368e00a868bbfa0d9acf895a2566a72dc4f599590250c2a800e829`
  - Proposed evidence: `must order forfeiture`
  - Decision context: `[107] Read in context, this suggests that it is the court convicting or discharging that must order forfeiture. If there were any ambiguity on this point, it is cleared away by the French version, which is narrower and more specific and thereby indicative of shared meaning (see Canada (Transportation Safety Board) v. Carroll‑Byrne, 2022 SCC 48, [2022] 3 S.C.R. 515, at para. 72). It says it is specifically “le tribunal qui condamne une personne pour une infraction désignée ou l’en absout” (the court that convicts a person of a designated offence or discharges them of it) that is so empowered:
16 (1) Sous réserve des articles 18 à 19.1 et sur demande du procureur général, le tribunal qui condamne une personne pour une infraction désignée ou l’en absout en vertu de l’article 730 du Code criminel et qui est convaincu, selon la prépondérance des probabilités, que des biens infractionnels non-chimiques sont liés à la perpétration de cette infraction ordonne qu’ils soient confisqués au profit :
a) soit de Sa Majesté du chef de la province où les procédures relatives à l’infraction ont été engagées, si elles l’ont été à la demande du gouvernement de cette province et menées par ce dernier ou en son nom, pour que le procureur général ou le solliciteur général de la province en dispose conformément au droit applicable;
b) soit de Sa Majesté du chef du Canada pour que le membre du Conseil privé de la Reine pour le Canada chargé par le gouverneur en conseil de l’application du présent alinéa en dispose conformément au droit applica`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-0039`; citation: `tribunal`; hash: `ea00e4c54a368e00a868bbfa0d9acf895a2566a72dc4f599590250c2a800e829`
  - Proposed evidence: `must order forfeiture`
  - Decision context: `[107] Read in context, this suggests that it is the court convicting or discharging that must order forfeiture. If there were any ambiguity on this point, it is cleared away by the French version, which is narrower and more specific and thereby indicative of shared meaning (see Canada (Transportation Safety Board) v. Carroll‑Byrne, 2022 SCC 48, [2022] 3 S.C.R. 515, at para. 72). It says it is specifically “le tribunal qui condamne une personne pour une infraction désignée ou l’en absout” (the court that convicts a person of a designated offence or discharges them of it) that is so empowered:
16 (1) Sous réserve des articles 18 à 19.1 et sur demande du procureur général, le tribunal qui condamne une personne pour une infraction désignée ou l’en absout en vertu de l’article 730 du Code criminel et qui est convaincu, selon la prépondérance des probabilités, que des biens infractionnels non-chimiques sont liés à la perpétration de cette infraction ordonne qu’ils soient confisqués au profit :
a) soit de Sa Majesté du chef de la province où les procédures relatives à l’infraction ont été engagées, si elles l’ont été à la demande du gouvernement de cette province et menées par ce dernier ou en son nom, pour que le procureur général ou le solliciteur général de la province en dispose conformément au droit applicable;
b) soit de Sa Majesté du chef du Canada pour que le membre du Conseil privé de la Reine pour le Canada chargé par le gouverneur en conseil de l’application du présent alinéa en dispose conformément au droit applicable, dans tout autre cas.`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-0040`; citation: `tribunal`; hash: `ea00e4c54a368e00a868bbfa0d9acf895a2566a72dc4f599590250c2a800e829`
  - Proposed evidence: `must order forfeiture`
  - Decision context: `[107] Read in context, this suggests that it is the court convicting or discharging that must order forfeiture. If there were any ambiguity on this point, it is cleared away by the French version, which is narrower and more specific and thereby indicative of shared meaning (see Canada (Transportation Safety Board) v. Carroll‑Byrne, 2022 SCC 48, [2022] 3 S.C.R. 515, at para. 72). It says it is specifically “le tribunal qui condamne une personne pour une infraction désignée ou l’en absout” (the court that convicts a person of a designated offence or discharges them of it) that is so empowered:
16 (1) Sous réserve des articles 18 à 19.1 et sur demande du procureur général, le tribunal qui condamne une personne pour une infraction désignée ou l’en absout en vertu de l’article 730 du Code criminel et qui est convaincu, selon la prépondérance des probabilités, que des biens infractionnels non-chimiques sont liés à la perpétration de cette infraction ordonne qu’ils soient confisqués au profit :
a) soit de Sa Majesté du chef de la province où les procédures relatives à l’infraction ont été engagées, si elles l’ont été à la demande du gouvernement de cette province et menées par ce dernier ou en son nom, pour que le procureur général ou le solliciteur général de la province en dispose conformément au droit applicable;
b) soit de Sa Majesté du chef du Canada pour que le membre du Conseil privé de la Reine pour le Canada chargé par le gouverneur en conseil de l’application du présent alinéa en dispose conformément au droit applicable, dans tout autre cas.`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 7. `teacher-phrase-supportive-0007`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `see generally craig, at para. 42`

Evidence:
- `citation-context-0541`; citation: `Craig, at para. 42`; hash: `61b4d43b9f1b6005450e4b350e9a7951cfd461104fcc8988b3efb90ceb20e58c`
  - Proposed evidence: `see generally Craig, at para. 42`
  - Decision context: `[87] Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA). Forfeiture is still available if the Crown can satisfy the court beyond a reasonable doubt that the property is otherwise proceeds of crime or offence-related property (see generally Craig, at para. 42; Lavigne, at para. 17; R. v. Lanteigne (1994), 156 N.B.R. (2d) 17 (Q.B.), at para. 29; R. v. Shearer, 2015 ONCA 355, 336 O.A.C. 30, at paras. 12-13; Croussette v. R., 2017 QCCA 1040, at para. 10 (Lexis); see also Procureur général du Québec v. Hydrobec (9031-7579 Québec inc.), 2022 QCCA 534, at para. 7; R. v. Witvoet, 2015 ABCA 152, 600 A.R. 200, at para. 27; Trecartin, at para. 31; Bergevin and Darbouze, at p. 65). In contrast to subsection (1) of each provision, which specifies that the court “shall” order forfeiture, subsection (2) says that the court “may” order forfeiture, indicating greater discretion for the sentencing court.`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0542`; citation: `Lavigne, at para. 17`; hash: `61b4d43b9f1b6005450e4b350e9a7951cfd461104fcc8988b3efb90ceb20e58c`
  - Proposed evidence: `see generally Craig, at para. 42`
  - Decision context: `[87] Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA). Forfeiture is still available if the Crown can satisfy the court beyond a reasonable doubt that the property is otherwise proceeds of crime or offence-related property (see generally Craig, at para. 42; Lavigne, at para. 17; R. v. Lanteigne (1994), 156 N.B.R. (2d) 17 (Q.B.), at para. 29; R. v. Shearer, 2015 ONCA 355, 336 O.A.C. 30, at paras. 12-13; Croussette v. R., 2017 QCCA 1040, at para. 10 (Lexis); see also Procureur général du Québec v. Hydrobec (9031-7579 Québec inc.), 2022 QCCA 534, at para. 7; R. v. Witvoet, 2015 ABCA 152, 600 A.R. 200, at para. 27; Trecartin, at para. 31; Bergevin and Darbouze, at p. 65). In contrast to subsection (1) of each provision, which specifies that the court “shall” order forfeiture, subsection (2) says that the court “may” order forfeiture, indicating greater discretion for the sentencing court.`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 8. `teacher-phrase-supportive-0008`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `see r. v. west (2005), 199 c.c.c. (3d) 449 (ont. c.a.), at paras. 27-28`

Evidence:
- `citation-context-0514`; citation: `R. v. West`; hash: `79a6b8c5e68f4b5aceb3b7e3eab960c322aa54cf87982f967c02d78519942288`
  - Proposed evidence: `see R. v. West (2005), 199 C.C.C. (3d) 449 (Ont. C.A.), at paras. 27-28`
  - Decision context: `[155] To meet this burden, the Crown may have to call evidence of the person’s unlawful acts in the context of the forfeiture hearing (see British Columbia (Attorney General) v. Forseth (1995), 99 C.C.C. (3d) 296 (B.C.C.A.), at paras. 27 and 30). The Crown can rely on a previous conviction or adduce evidence to prove unlawful possession in accordance with the applicable rules of criminal procedure. If the Crown adduces evidence, normal rules of criminal evidence will apply (see R. v. West (2005), 199 C.C.C. (3d) 449 (Ont. C.A.), at paras. 27-28; see also Fleming, at pp. 445‑46). While evidence may be adduced through affidavit, it must comply with the relevant rules of evidence in the context of criminal applications (see West, at paras. 27-31 and 35; Canada (Attorney General) v. Acero, 2006 BCSC 1015, 210 C.C.C. (3d) 549, at paras. 53 and 56-58; see also Uniform Law Conference of Canada, at para. 218).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0516`; citation: `West, at paras. 27-31 and 35`; hash: `79a6b8c5e68f4b5aceb3b7e3eab960c322aa54cf87982f967c02d78519942288`
  - Proposed evidence: `see R. v. West (2005), 199 C.C.C. (3d) 449 (Ont. C.A.), at paras. 27-28`
  - Decision context: `[155] To meet this burden, the Crown may have to call evidence of the person’s unlawful acts in the context of the forfeiture hearing (see British Columbia (Attorney General) v. Forseth (1995), 99 C.C.C. (3d) 296 (B.C.C.A.), at paras. 27 and 30). The Crown can rely on a previous conviction or adduce evidence to prove unlawful possession in accordance with the applicable rules of criminal procedure. If the Crown adduces evidence, normal rules of criminal evidence will apply (see R. v. West (2005), 199 C.C.C. (3d) 449 (Ont. C.A.), at paras. 27-28; see also Fleming, at pp. 445‑46). While evidence may be adduced through affidavit, it must comply with the relevant rules of evidence in the context of criminal applications (see West, at paras. 27-31 and 35; Canada (Attorney General) v. Acero, 2006 BCSC 1015, 210 C.C.C. (3d) 549, at paras. 53 and 56-58; see also Uniform Law Conference of Canada, at para. 218).`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 9. `teacher-phrase-supportive-0009`

- Proposed treatment: **supportive**
- Support: **4** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `see vellone, at paras. 41 and 53; breton, at para. 76`

Evidence:
- `citation-context-0518`; citation: `Vellone, at paras. 41 and 53`; hash: `37467415cced7768ff24641a6dc76349717fa6127b81c5c2740ec3b71ba43809`
  - Proposed evidence: `see Vellone, at paras. 41 and 53; Breton, at para. 76`
  - Decision context: `[156] The forfeiture proceeding is distinct from any related criminal liability proceedings in terms of its evidentiary record (see Vellone, at paras. 41 and 53; Breton, at para. 76). For example, if evidence was excluded at trial under s. 24(2) of the Charter, this does not mean that this evidence will necessarily be excluded in an application for forfeiture (see Vellone, at paras. 48-49; Breton, at paras. 77-82). As the analysis prescribed in R. v. Grant, 2009 SCC 32, [2009] 2 S.C.R. 353, is inherently contextual, it may look different in a forfeiture application than it would even in a related trial to determine a person’s criminal liability (Breton, at para. 77; Vellone, at para. 55).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0519`; citation: `Breton, at para. 76`; hash: `37467415cced7768ff24641a6dc76349717fa6127b81c5c2740ec3b71ba43809`
  - Proposed evidence: `see Vellone, at paras. 41 and 53; Breton, at para. 76`
  - Decision context: `[156] The forfeiture proceeding is distinct from any related criminal liability proceedings in terms of its evidentiary record (see Vellone, at paras. 41 and 53; Breton, at para. 76). For example, if evidence was excluded at trial under s. 24(2) of the Charter, this does not mean that this evidence will necessarily be excluded in an application for forfeiture (see Vellone, at paras. 48-49; Breton, at paras. 77-82). As the analysis prescribed in R. v. Grant, 2009 SCC 32, [2009] 2 S.C.R. 353, is inherently contextual, it may look different in a forfeiture application than it would even in a related trial to determine a person’s criminal liability (Breton, at para. 77; Vellone, at para. 55).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0520`; citation: `Vellone, at paras. 48-49`; hash: `37467415cced7768ff24641a6dc76349717fa6127b81c5c2740ec3b71ba43809`
  - Proposed evidence: `see Vellone, at paras. 41 and 53; Breton, at para. 76`
  - Decision context: `[156] The forfeiture proceeding is distinct from any related criminal liability proceedings in terms of its evidentiary record (see Vellone, at paras. 41 and 53; Breton, at para. 76). For example, if evidence was excluded at trial under s. 24(2) of the Charter, this does not mean that this evidence will necessarily be excluded in an application for forfeiture (see Vellone, at paras. 48-49; Breton, at paras. 77-82). As the analysis prescribed in R. v. Grant, 2009 SCC 32, [2009] 2 S.C.R. 353, is inherently contextual, it may look different in a forfeiture application than it would even in a related trial to determine a person’s criminal liability (Breton, at para. 77; Vellone, at para. 55).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0521`; citation: `Breton, at paras. 77-82`; hash: `37467415cced7768ff24641a6dc76349717fa6127b81c5c2740ec3b71ba43809`
  - Proposed evidence: `see Vellone, at paras. 41 and 53; Breton, at para. 76`
  - Decision context: `[156] The forfeiture proceeding is distinct from any related criminal liability proceedings in terms of its evidentiary record (see Vellone, at paras. 41 and 53; Breton, at para. 76). For example, if evidence was excluded at trial under s. 24(2) of the Charter, this does not mean that this evidence will necessarily be excluded in an application for forfeiture (see Vellone, at paras. 48-49; Breton, at paras. 77-82). As the analysis prescribed in R. v. Grant, 2009 SCC 32, [2009] 2 S.C.R. 353, is inherently contextual, it may look different in a forfeiture application than it would even in a related trial to determine a person’s criminal liability (Breton, at para. 77; Vellone, at para. 55).`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 10. `teacher-phrase-supportive-0010`

- Proposed treatment: **supportive**
- Support: **3** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `see vellone, at paras. 48-49; breton, at paras. 77-82`

Evidence:
- `citation-context-0522`; citation: `R. v. Grant, 2009 SCC 32, [2009] 2 S.C.R. 353`; hash: `37467415cced7768ff24641a6dc76349717fa6127b81c5c2740ec3b71ba43809`
  - Proposed evidence: `see Vellone, at paras. 48-49; Breton, at paras. 77-82`
  - Decision context: `[156] The forfeiture proceeding is distinct from any related criminal liability proceedings in terms of its evidentiary record (see Vellone, at paras. 41 and 53; Breton, at para. 76). For example, if evidence was excluded at trial under s. 24(2) of the Charter, this does not mean that this evidence will necessarily be excluded in an application for forfeiture (see Vellone, at paras. 48-49; Breton, at paras. 77-82). As the analysis prescribed in R. v. Grant, 2009 SCC 32, [2009] 2 S.C.R. 353, is inherently contextual, it may look different in a forfeiture application than it would even in a related trial to determine a person’s criminal liability (Breton, at para. 77; Vellone, at para. 55).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0523`; citation: `Breton, at para. 77`; hash: `37467415cced7768ff24641a6dc76349717fa6127b81c5c2740ec3b71ba43809`
  - Proposed evidence: `see Vellone, at paras. 48-49; Breton, at paras. 77-82`
  - Decision context: `[156] The forfeiture proceeding is distinct from any related criminal liability proceedings in terms of its evidentiary record (see Vellone, at paras. 41 and 53; Breton, at para. 76). For example, if evidence was excluded at trial under s. 24(2) of the Charter, this does not mean that this evidence will necessarily be excluded in an application for forfeiture (see Vellone, at paras. 48-49; Breton, at paras. 77-82). As the analysis prescribed in R. v. Grant, 2009 SCC 32, [2009] 2 S.C.R. 353, is inherently contextual, it may look different in a forfeiture application than it would even in a related trial to determine a person’s criminal liability (Breton, at para. 77; Vellone, at para. 55).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0524`; citation: `Vellone, at para. 55`; hash: `37467415cced7768ff24641a6dc76349717fa6127b81c5c2740ec3b71ba43809`
  - Proposed evidence: `see Vellone, at paras. 48-49; Breton, at paras. 77-82`
  - Decision context: `[156] The forfeiture proceeding is distinct from any related criminal liability proceedings in terms of its evidentiary record (see Vellone, at paras. 41 and 53; Breton, at para. 76). For example, if evidence was excluded at trial under s. 24(2) of the Charter, this does not mean that this evidence will necessarily be excluded in an application for forfeiture (see Vellone, at paras. 48-49; Breton, at paras. 77-82). As the analysis prescribed in R. v. Grant, 2009 SCC 32, [2009] 2 S.C.R. 353, is inherently contextual, it may look different in a forfeiture application than it would even in a related trial to determine a person’s criminal liability (Breton, at para. 77; Vellone, at para. 55).`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 11. `teacher-phrase-supportive-0011`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `see, e.g., spindloe, at para. 119`

Evidence:
- `citation-context-0061`; citation: `(see, e.g., Spindloe, at para. 119)`; hash: `1108115ba4a9523191bb603fec3320d8369f7cd932f7f1c817b9ac66f4ca761b`
  - Proposed evidence: `see, e.g., Spindloe, at para. 119`
  - Decision context: `. But in my humble view, this does not account for the fact that, as discussed above, s. 491.1 applies (1) only to property obtained by the commission of an offence; (2) only if there has been a trial; and (3) only if there is still a trial court seized of the matter. Other decisions have pointed to s. 490(4) Cr. C., which provides that when an accused “has been ordered to stand trial” seized property is forwarded to the clerk of the court in which the trial will occur to be detained and “disposed of as the court directs”, as another means to close the resulting gap in forfeiture jurisdiction (see, e.g., Spindloe, at para. 119). But even if this is read to confer a forfeiture power on the trial court, from which there would be no appeal, an apparent gap would remain where charges are laid, commencing criminal proceedings, but the accused is not ordered to stand trial. While there may be other mechanisms through which property could be returned or forfeited, such as a Charter application, a civil forfeiture application, or a common law property claim by a lawful owner, there will be property that is not susceptible to disposition under any of these regimes. Not every case will involve a Charter breach, an applicable civil forfeiture regime or a lawful owner who can make out a common law action for the recovery of the property. Despite the various routes to disposition of the property before criminal courts, gaps would remain.`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-0586`; citation: `(see, e.g., Spindloe, at para. 119)`; hash: `1108115ba4a9523191bb603fec3320d8369f7cd932f7f1c817b9ac66f4ca761b`
  - Proposed evidence: `see, e.g., Spindloe, at para. 119`
  - Decision context: `. But in my humble view, this does not account for the fact that, as discussed above, s. 491.1 applies (1) only to property obtained by the commission of an offence; (2) only if there has been a trial; and (3) only if there is still a trial court seized of the matter. Other decisions have pointed to s. 490(4) Cr. C., which provides that when an accused “has been ordered to stand trial” seized property is forwarded to the clerk of the court in which the trial will occur to be detained and “disposed of as the court directs”, as another means to close the resulting gap in forfeiture jurisdiction (see, e.g., Spindloe, at para. 119). But even if this is read to confer a forfeiture power on the trial court, from which there would be no appeal, an apparent gap would remain where charges are laid, commencing criminal proceedings, but the accused is not ordered to stand trial. While there may be other mechanisms through which property could be returned or forfeited, such as a Charter application, a civil forfeiture application, or a common law property claim by a lawful owner, there will be property that is not susceptible to disposition under any of these regimes. Not every case will involve a Charter breach, an applicable civil forfeiture regime or a lawful owner who can make out a common law action for the recovery of the property. Despite the various routes to disposition of the property before criminal courts, gaps would remain.`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 12. `teacher-phrase-supportive-0012`

- Proposed treatment: **supportive**
- Support: **4** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `see, e.g., taylor, at para. 49; spindloe, at para. 111; echostar, at paras. 26-27`

Evidence:
- `citation-context-0063`; citation: `Taylor, at para. 49`; hash: `d754b47a5b37c644963e0b7599db2f5ed431f8cfd918ce55886e3a5031cb92e7`
  - Proposed evidence: `see, e.g., Taylor, at para. 49; Spindloe, at para. 111; Echostar, at paras. 26-27`
  - Decision context: `[133] To the extent that the case law suggests a narrow interpretation of s. 490(9), that reading is largely hinged on the words “proceedings have not been instituted” (“des procédures . . . n’ont pas été engagées”) (see, e.g., Taylor, at para. 49; Spindloe, at para. 111; Echostar, at paras. 26-27). I acknowledge that the plain meaning of these words, if read in isolation from the remainder of s. 490(9), could suggest that the requirement is that proceedings have never been instituted. But recall that the modern approach to statutory interpretation requires that even superficially plain text always be read in context and in light of its purpose (see Wilson, at para. 34). Applying that approach, with an eye to both linguistic texts and the context and purpose of the provision, shapes a proper reading of s. 490(9).`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-0064`; citation: `Spindloe, at para. 111`; hash: `d754b47a5b37c644963e0b7599db2f5ed431f8cfd918ce55886e3a5031cb92e7`
  - Proposed evidence: `see, e.g., Taylor, at para. 49; Spindloe, at para. 111; Echostar, at paras. 26-27`
  - Decision context: `[133] To the extent that the case law suggests a narrow interpretation of s. 490(9), that reading is largely hinged on the words “proceedings have not been instituted” (“des procédures . . . n’ont pas été engagées”) (see, e.g., Taylor, at para. 49; Spindloe, at para. 111; Echostar, at paras. 26-27). I acknowledge that the plain meaning of these words, if read in isolation from the remainder of s. 490(9), could suggest that the requirement is that proceedings have never been instituted. But recall that the modern approach to statutory interpretation requires that even superficially plain text always be read in context and in light of its purpose (see Wilson, at para. 34). Applying that approach, with an eye to both linguistic texts and the context and purpose of the provision, shapes a proper reading of s. 490(9).`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-0065`; citation: `Echostar, at paras. 26-27`; hash: `d754b47a5b37c644963e0b7599db2f5ed431f8cfd918ce55886e3a5031cb92e7`
  - Proposed evidence: `see, e.g., Taylor, at para. 49; Spindloe, at para. 111; Echostar, at paras. 26-27`
  - Decision context: `[133] To the extent that the case law suggests a narrow interpretation of s. 490(9), that reading is largely hinged on the words “proceedings have not been instituted” (“des procédures . . . n’ont pas été engagées”) (see, e.g., Taylor, at para. 49; Spindloe, at para. 111; Echostar, at paras. 26-27). I acknowledge that the plain meaning of these words, if read in isolation from the remainder of s. 490(9), could suggest that the requirement is that proceedings have never been instituted. But recall that the modern approach to statutory interpretation requires that even superficially plain text always be read in context and in light of its purpose (see Wilson, at para. 34). Applying that approach, with an eye to both linguistic texts and the context and purpose of the provision, shapes a proper reading of s. 490(9).`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-0066`; citation: `(see Wilson, at para. 34)`; hash: `d754b47a5b37c644963e0b7599db2f5ed431f8cfd918ce55886e3a5031cb92e7`
  - Proposed evidence: `see, e.g., Taylor, at para. 49; Spindloe, at para. 111; Echostar, at paras. 26-27`
  - Decision context: `[133] To the extent that the case law suggests a narrow interpretation of s. 490(9), that reading is largely hinged on the words “proceedings have not been instituted” (“des procédures . . . n’ont pas été engagées”) (see, e.g., Taylor, at para. 49; Spindloe, at para. 111; Echostar, at paras. 26-27). I acknowledge that the plain meaning of these words, if read in isolation from the remainder of s. 490(9), could suggest that the requirement is that proceedings have never been instituted. But recall that the modern approach to statutory interpretation requires that even superficially plain text always be read in context and in light of its purpose (see Wilson, at para. 34). Applying that approach, with an eye to both linguistic texts and the context and purpose of the provision, shapes a proper reading of s. 490(9).`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 13. `teacher-phrase-supportive-0013`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `some nexus to criminal liability proceedings is required`

Evidence:
- `citation-context-0551`; citation: `Hape`; hash: `d7f66cc646b410c36d2330ddfaea229cefe7900f1296351fb9aada36381bd3c7`
  - Proposed evidence: `some nexus to criminal liability proceedings is required`
  - Decision context: `[95] I therefore agree with the Court of Appeal for Ontario in Hape that some nexus to criminal liability proceedings is required (para. 40; see also R. v. Dolbec, 2011 QCCA 1610, at para. 27). Specifically, while no direct link between the property and the finding of guilt or the accused is necessary, there must be a sufficient nexus between the property and the criminal allegations underlying the proceedings in which the forfeiture power is triggered. This does not mean that all the evidence justifying forfeiture need be adduced at trial, but merely that there is some connection between the property and the criminal allegations underlying the information or indictment that circumscribes the criminal liability proceedings. The property must reasonably form part of the broader context surrounding the allegations. For example, in this case, the court that heard Manh Hung Nguyen’s guilty plea could have considered forfeiture of property if there was a reasonable basis to believe it was connected to the broader alleged cannabis production enterprise in respect of which he was charged. Forfeiture of the property could have been considered even if that property was not directly tied to Manh Hung Nguyen himself or to the offence of which he was found guilty.`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0552`; citation: `R. v. Dolbec, 2011 QCCA 1610, at para. 27`; hash: `d7f66cc646b410c36d2330ddfaea229cefe7900f1296351fb9aada36381bd3c7`
  - Proposed evidence: `some nexus to criminal liability proceedings is required`
  - Decision context: `[95] I therefore agree with the Court of Appeal for Ontario in Hape that some nexus to criminal liability proceedings is required (para. 40; see also R. v. Dolbec, 2011 QCCA 1610, at para. 27). Specifically, while no direct link between the property and the finding of guilt or the accused is necessary, there must be a sufficient nexus between the property and the criminal allegations underlying the proceedings in which the forfeiture power is triggered. This does not mean that all the evidence justifying forfeiture need be adduced at trial, but merely that there is some connection between the property and the criminal allegations underlying the information or indictment that circumscribes the criminal liability proceedings. The property must reasonably form part of the broader context surrounding the allegations. For example, in this case, the court that heard Manh Hung Nguyen’s guilty plea could have considered forfeiture of property if there was a reasonable basis to believe it was connected to the broader alleged cannabis production enterprise in respect of which he was charged. Forfeiture of the property could have been considered even if that property was not directly tied to Manh Hung Nguyen himself or to the offence of which he was found guilty.`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 14. `teacher-phrase-supportive-0014`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `states`

Evidence:
- `citation-context-1041`; citation: `states`; hash: `294faafe517db7c84630bcb89f0ec5cdbced2b4b75d3216772b06ee200cf0d13`
  - Proposed evidence: `states`
  - Decision context: ` :
…
…
(e) the claimant came directly or indirectly to Canada from a country designated by the regulations, other than a country of their nationality or their former habitual residence;
e) arrivée, directement ou indirectement, d’un pays désigné par règlement autre que celui dont il a la nationalité ou dans lequel il avait sa résidence habituelle;
…
…
102 (1) The regulations may govern matters relating to the application of sections 100 and 101, may, for the purposes of this Act, define the terms used in those sections and, for the purpose of sharing responsibility with governments of foreign states for the consideration of refugee claims, may include provisions
102 (1) Les règlements régissent l’application des articles 100 et 101, définissent, pour l’application de la présente loi, les termes qui y sont employés et, en vue du partage avec d’autres pays de la responsabilité de l’examen des demandes d’asile, prévoient notamment :
(a) designating countries that comply with Article 33 of the Refugee Convention and Article 3 of the Convention Against Torture;
a) la désignation des pays qui se conforment à l’article 33 de la Convention sur les réfugiés et à l’article 3 de la Convention contre la torture;
102 (2) The following factors are to be considered in designating a country under paragraph (1)(a):
102 (2) Il est tenu compte des facteurs suivants en vue de la désignation des pays :
(a) whether the country is a party to the Refugee Convention and to the Convention Against Torture;
a) le fait que ces pays sont parties à la Convention sur les réfugiés et à la Convention contre la torture;
(b) its policies and practices with respect to claims under the Refugee Convention and with respect to obligations under the Convention Against Torture;
b) leurs politique et usages en ce qui t`
  - Offsets repaired: `False`; confidence: `0.90`
- `citation-context-1047`; citation: `Canadian Council for Refugees v Canada, 2007 FC 1262`; hash: `6a43e4e85d80207d799984a4b64e2f00aceb7b84929973ce60ad5f4c424cd14e`
  - Proposed evidence: `states`
  - Decision context: ` nationality, membership of a particular social group or political opinion.
2. The benefit of the present provision may not, however, be claimed by a refugee whom there are reasonable grounds for regarding as a danger to the security of the country in which he is, or who, having been convicted by a final judgment of a particularly serious crime, constitutes a danger to the community of that country.
[56] Article 3 of the Convention against Torture states:
1. No State Party shall expel, return ("refouler") or extradite a person to another State where there are substantial grounds for believing that he would be in danger of being subjected to torture.
2. For the purpose of determining whether there are such grounds, the competent authorities shall take into account all relevant considerations including, where applicable, the existence in the State concerned of a consistent pattern of gross, flagrant or mass violations of human rights.
[57] These provisions were considered extensively in Canadian Council for Refugees v Canada, 2007 FC 1262 [CCR 2007] and Canada v Canadian Council for Refugees, 2008 FCA 229 [CCR 2008].
Applicants’ Submissions
[58] The Applicants argue that s. 159.3 of the Regulations is ultra vires because the ongoing designation of the US as a safe third country is inconsistent with the statutory purpose and the statutory grant of power. Further, they argue that the statutory conditions precedent for the ongoing designation of the US as a safe third country have not been satisfied.
Designation Inconsistent with Statutory Purpose and Grant of Power
[59] The Applicants submit that developments in the law since the FCA decision in CCR 2008 allow this Court to reconsider the vires issue. They rely upon West Fraser Mills Ltd v British Columbia (Workers’ Compensation Appeal Tribunal), 2018 SCC 22 [West Fraser Mills] (at paras 10 and 12) and Catalyst Paper Corp v North Cowichan (District), 2012 SCC 2 (at para 12) to argue that a regulation is ultra vires when it is "inconsistent with the objective of the enabling statute or the scope of the statutory mandate" (West Fraser Mills at para 12).
[60] According to the Applicants, based on the evidence of violations by the US of the Refugee Convention, the US is `
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 15. `teacher-phrase-supportive-0015`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) cr. c.) or cannot show was related to the commission of that offence (s. 16(2) cdsa).`

Evidence:
- `citation-context-0021`; citation: `R. v. Witvoet, 2015 ABCA 152`; hash: `61b4d43b9f1b6005450e4b350e9a7951cfd461104fcc8988b3efb90ceb20e58c`
  - Proposed evidence: `Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA).`
  - Decision context: `[87] Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA). Forfeiture is still available if the Crown can satisfy the court beyond a reasonable doubt that the property is otherwise proceeds of crime or offence-related property (see generally Craig, at para. 42; Lavigne, at para. 17; R. v. Lanteigne (1994), 156 N.B.R. (2d) 17 (Q.B.), at para. 29; R. v. Shearer, 2015 ONCA 355, 336 O.A.C. 30, at paras. 12-13; Croussette v. R., 2017 QCCA 1040, at para. 10 (Lexis); see also Procureur général du Québec v. Hydrobec (9031-7579 Québec inc.), 2022 QCCA 534, at para. 7; R. v. Witvoet, 2015 ABCA 152, 600 A.R. 200, at para. 27; Trecartin, at para. 31; Bergevin and Darbouze, at p. 65). In contrast to subsection (1) of each provision, which specifies that the court “shall” order forfeiture, subsection (2) says that the court “may” order forfeiture, indicating greater discretion for the sentencing court.`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0022`; citation: `Trecartin, at para. 31`; hash: `61b4d43b9f1b6005450e4b350e9a7951cfd461104fcc8988b3efb90ceb20e58c`
  - Proposed evidence: `Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA).`
  - Decision context: `[87] Subsection (2) of both provisions expressly broadens the basis for forfeiture to include property that the Crown cannot show was obtained through the commission of the offence on which there is a finding of guilt (s. 462.37(2) Cr. C.) or cannot show was related to the commission of that offence (s. 16(2) CDSA). Forfeiture is still available if the Crown can satisfy the court beyond a reasonable doubt that the property is otherwise proceeds of crime or offence-related property (see generally Craig, at para. 42; Lavigne, at para. 17; R. v. Lanteigne (1994), 156 N.B.R. (2d) 17 (Q.B.), at para. 29; R. v. Shearer, 2015 ONCA 355, 336 O.A.C. 30, at paras. 12-13; Croussette v. R., 2017 QCCA 1040, at para. 10 (Lexis); see also Procureur général du Québec v. Hydrobec (9031-7579 Québec inc.), 2022 QCCA 534, at para. 7; R. v. Witvoet, 2015 ABCA 152, 600 A.R. 200, at para. 27; Trecartin, at para. 31; Bergevin and Darbouze, at p. 65). In contrast to subsection (1) of each provision, which specifies that the court “shall” order forfeiture, subsection (2) says that the court “may” order forfeiture, indicating greater discretion for the sentencing court.`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 16. `teacher-phrase-supportive-0016`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `the purpose of s. 490 is to ensure that courts supervising seized property can carefully balance the private interests in that property against the public need for that property to be detained in pursuit of investigating and prosecuting crime`

Evidence:
- `citation-context-0571`; citation: `Breton, at para. 62`; hash: `028ab75a67b1d87d701dc4b7bc053b6d93662bf710132413839abcc8408a06e2`
  - Proposed evidence: `The purpose of s. 490 is to ensure that courts supervising seized property can carefully balance the private interests in that property against the public need for that property to be detained in pursuit of investigating and prosecuting crime`
  - Decision context: `ition of seized property, which apply unless Parliament has provided more specific, conflicting rules (“[s]ubject to this or any other Act of Parliament” / “[s]ous réserve des autres dispositions de la présente loi ou de toute autre loi fédérale” (s. 490(1) and (9))). Where s. 490 has not been displaced by legislation, police who seize any property in the execution of their duties under federal legislation, and who do not return it, must submit that property to judicial supervision under s. 490 (ss. 489.1(1)(b) and 490(1) Cr. C.; see N. Hasan et al., Search and Seizure (2021), at pp. 538-39). The purpose of s. 490 is to ensure that courts supervising seized property can carefully balance the private interests in that property against the public need for that property to be detained in pursuit of investigating and prosecuting crime (see Hollaman, at paras. 97-98; Breton, at para. 62; see also Uniform Law Conference of Canada, at paras. 12-13; Further Detention of Things Seized (Re), 2024 BCSC 354, at para. 15; Ayotte, at para. 51). It purports to provide a “complete scheme” for this purpose (Raponi, at para. 28; see also paras. 8‑15 and 30; R. v. Backhouse (2005), 195 O.A.C. 80, at para. 111). Section 490 also applies with necessary modifications to property that has not actually been seized but is nonetheless subject to judicial supervision, such as property subject to a restraint order, where this is contemplated by statute (see, e.g., s. 490.9(1) Cr. C.; s. 15(1) CDSA).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0572`; citation: `Ayotte, at para. 51`; hash: `15b574fd2db87430eabb0dd777839cc87559189772c508faf7cba08d469cdc58`
  - Proposed evidence: `The purpose of s. 490 is to ensure that courts supervising seized property can carefully balance the private interests in that property against the public need for that property to be detained in pursuit of investigating and prosecuting crime`
  - Decision context: ` which apply unless Parliament has provided more specific, conflicting rules (“[s]ubject to this or any other Act of Parliament” / “[s]ous réserve des autres dispositions de la présente loi ou de toute autre loi fédérale” (s. 490(1) and (9))). Where s. 490 has not been displaced by legislation, police who seize any property in the execution of their duties under federal legislation, and who do not return it, must submit that property to judicial supervision under s. 490 (ss. 489.1(1)(b) and 490(1) Cr. C.; see N. Hasan et al., Search and Seizure (2021), at pp. 538-39). The purpose of s. 490 is to ensure that courts supervising seized property can carefully balance the private interests in that property against the public need for that property to be detained in pursuit of investigating and prosecuting crime (see Hollaman, at paras. 97-98; Breton, at para. 62; see also Uniform Law Conference of Canada, at paras. 12-13; Further Detention of Things Seized (Re), 2024 BCSC 354, at para. 15; Ayotte, at para. 51). It purports to provide a “complete scheme” for this purpose (Raponi, at para. 28; see also paras. 8‑15 and 30; R. v. Backhouse (2005), 195 O.A.C. 80, at para. 111). Section 490 also applies with necessary modifications to property that has not actually been seized but is nonetheless subject to judicial supervision, such as property subject to a restraint order, where this is contemplated by statute (see, e.g., s. 490.9(1) Cr. C.; s. 15(1) CDSA).`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 17. `teacher-phrase-supportive-0017`

- Proposed treatment: **supportive**
- Support: **4** examples; mean confidence **0.90**
- Span quality: **repaired**
- Phrase: `the role of an expert is to assist the court, not to advocate`

Evidence:
- `citation-context-1027`; citation: `states`; hash: `1f46504d8116f1770de79329a419cf0f4eef02c297e69c06d22d379158610b69`
  - Proposed evidence: `the role of an expert is to assist the Court, not to advocate`
  - Decision context: ` pursued, whereas in her affidavits (September 22, 2017 and June 25, 2018) she claims that the likelihood of success is low. The challenge with how the Respondents have raised their objections to this evidence, is that they fail to specify what portions or what statements they take issue with. I agree with the Respondents that broad categorical statements on the success of asylum claims within the US system is irrelevant and I will therefore disregard these statements.
[42] Both Professors Anker and Musalo signed the expert witness certificate under the Federal Courts Rules which specifically states they “have read the Code of Conduct for Expert Witnesses set out in the schedule to the Federal Courts Rules and agree to be bound by it.” The Code of Conduct provides:
[a]n expert witness named to provide a report for use as evidence, or to testify in a proceeding, has an overriding duty to assist the Court impartially on matters relevant to his or her area of expertise.
… This duty overrides any duty to a party to the proceeding, including the person retaining the expert witness. An expert is to be independent and objective. An expert is not an advocate for a party.
[43] In White Burgess Langille Inman v Abbott and Haliburton Co, 2015 SCC 23 [White Burgess], the Supreme Court of Canada held that the role of an expert is to assist the Court, not to advocate. The Court further noted that experts “have a special duty to the court to provide fair, objective and non-partisan assistance” (White Burgess at para 2).
[44] Having considered Professors Anker and Musalo’s evidence in the full context of these Applications, I accept their evidence. I acknowledge that they are engaged in broader forms of advocacy in support of asylum causes. However, for the present Applications, their evidence was based on their professional views of the US asylum system and how it functions, or fails to function. It is in that regard that their evidence and opinions are of assistance to the Court.
[45] Given the failure of the Respondents to clearly articulate their specific objections, and considering the test outlined by the Supreme Court in White Burgess, I accept their evidence subject to the qualifications noted.
Ms. Mustefa’s Request to Make New Arguments
[46] At the hearing, Ms. Mustefa’s lawyers requested leave to amend her Application to make new procedural fairness arguments. I declined this request. As I stated at the hearing, these Applications had been ongoing for a number of years, accordingly, there was ample time to identify and raise these argu`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-1028`; citation: `White Burgess Langille Inman v Abbott and Haliburton Co, 2015 SCC 23 [White Burgess]`; hash: `1a3dc3a18936c7c7cf2d966338577eab66f53ae36c6e099be651776f388cef8e`
  - Proposed evidence: `the role of an expert is to assist the Court, not to advocate`
  - Decision context: `cifically states they “have read the Code of Conduct for Expert Witnesses set out in the schedule to the Federal Courts Rules and agree to be bound by it.” The Code of Conduct provides:
[a]n expert witness named to provide a report for use as evidence, or to testify in a proceeding, has an overriding duty to assist the Court impartially on matters relevant to his or her area of expertise.
… This duty overrides any duty to a party to the proceeding, including the person retaining the expert witness. An expert is to be independent and objective. An expert is not an advocate for a party.
[43] In White Burgess Langille Inman v Abbott and Haliburton Co, 2015 SCC 23 [White Burgess], the Supreme Court of Canada held that the role of an expert is to assist the Court, not to advocate. The Court further noted that experts “have a special duty to the court to provide fair, objective and non-partisan assistance” (White Burgess at para 2).
[44] Having considered Professors Anker and Musalo’s evidence in the full context of these Applications, I accept their evidence. I acknowledge that they are engaged in broader forms of advocacy in support of asylum causes. However, for the present Applications, their evidence was based on their professional views of the US asylum system and how it functions, or fails to function. It is in that regard that their evidence and opinions are of assistance to the Court.
[45] Given the failure of the Respondents to clearly articulate their specific objections, and considering the test outlined by the Supreme Court in White Burgess, I accept their evidence subject to the qualifications noted.
Ms. Mustefa’s Request to Make New Arguments
[46] At the hearing, Ms. Mustefa’s lawyers requested leave to amend her Application to make new procedural fairness arguments. I declined this request. As I stated at the hearing, these Applications had been ongoing for a number of years, accordingly, there was ample time to identify and raise these argu`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-1029`; citation: `(White Burgess at para 2)`; hash: `431253828b7ebaa2c4a88063e680456e914d6ded5579ca3b08d180a4c82af4a4`
  - Proposed evidence: `the role of an expert is to assist the Court, not to advocate`
  - Decision context: `s and agree to be bound by it.” The Code of Conduct provides:
[a]n expert witness named to provide a report for use as evidence, or to testify in a proceeding, has an overriding duty to assist the Court impartially on matters relevant to his or her area of expertise.
… This duty overrides any duty to a party to the proceeding, including the person retaining the expert witness. An expert is to be independent and objective. An expert is not an advocate for a party.
[43] In White Burgess Langille Inman v Abbott and Haliburton Co, 2015 SCC 23 [White Burgess], the Supreme Court of Canada held that the role of an expert is to assist the Court, not to advocate. The Court further noted that experts “have a special duty to the court to provide fair, objective and non-partisan assistance” (White Burgess at para 2).
[44] Having considered Professors Anker and Musalo’s evidence in the full context of these Applications, I accept their evidence. I acknowledge that they are engaged in broader forms of advocacy in support of asylum causes. However, for the present Applications, their evidence was based on their professional views of the US asylum system and how it functions, or fails to function. It is in that regard that their evidence and opinions are of assistance to the Court.
[45] Given the failure of the Respondents to clearly articulate their specific objections, and considering the test outlined by the Supreme Court in White Burgess, I accept their evidence subject to the qualifications noted.
Ms. Mustefa’s Request to Make New Arguments
[46] At the hearing, Ms. Mustefa’s lawyers requested leave to amend her Application to make new procedural fairness arguments. I declined this request. As I stated at the hearing, these Applications had been ongoing for a number of years, accordingly, there was ample time to identify and raise these arguments earlier. In my view, it was not fair to the Respondents, or in the interests of justice, to allow Ms. Mustefa to raise procedural fairness arguments`
  - Offsets repaired: `True`; confidence: `0.90`
- `citation-context-1030`; citation: `White Burgess`; hash: `6c0182635219d747b8003533a384e56a431bbe877e25ccd7a0bab408ea787a63`
  - Proposed evidence: `the role of an expert is to assist the Court, not to advocate`
  - Decision context: `is not an advocate for a party.
[43] In White Burgess Langille Inman v Abbott and Haliburton Co, 2015 SCC 23 [White Burgess], the Supreme Court of Canada held that the role of an expert is to assist the Court, not to advocate. The Court further noted that experts “have a special duty to the court to provide fair, objective and non-partisan assistance” (White Burgess at para 2).
[44] Having considered Professors Anker and Musalo’s evidence in the full context of these Applications, I accept their evidence. I acknowledge that they are engaged in broader forms of advocacy in support of asylum causes. However, for the present Applications, their evidence was based on their professional views of the US asylum system and how it functions, or fails to function. It is in that regard that their evidence and opinions are of assistance to the Court.
[45] Given the failure of the Respondents to clearly articulate their specific objections, and considering the test outlined by the Supreme Court in White Burgess, I accept their evidence subject to the qualifications noted.
Ms. Mustefa’s Request to Make New Arguments
[46] At the hearing, Ms. Mustefa’s lawyers requested leave to amend her Application to make new procedural fairness arguments. I declined this request. As I stated at the hearing, these Applications had been ongoing for a number of years, accordingly, there was ample time to identify and raise these arguments earlier. In my view, it was not fair to the Respondents, or in the interests of justice, to allow Ms. Mustefa to raise procedural fairness arguments at the hearing of this judicial review application.
VIII. ISSUES
[47] The following are the issues for determination:
Is s. 159.3 of the Regulations ultra vires?
Does the STCA infringe section 7 of the Charter?
Is the infringement justified under section 1 of the Charter?
Does the STCA infringe section 15 of the Charter?
Should the Court decline to consider Ms. Mustefa’s application?
Do certified questions arise?`
  - Offsets repaired: `True`; confidence: `0.90`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 18. `teacher-phrase-supportive-0018`

- Proposed treatment: **supportive**
- Support: **10** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `vavilov at para 68 states: reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`

Evidence:
- `citation-context-1031`; citation: `Supreme Court released its decision in Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov]`; hash: `ebe4848d043b2f67abac687b51879d19be3b6baa81386ec791d505e3e47a285d`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: `IX. STANDARD OF REVIEW
[48] After hearing these applications, the Supreme Court released its decision in Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov]. Accordingly, I invited the parties to make post-hearing submissions on the impact of Vavilov on the applicable standard of review.
[49] The Applicants assert that Vavilov strengthens their position that s. 159.3 of the Regulations is ultra vires for two reasons. First, because the Supreme Court held that external constraints limit the range of reasonable outcomes of administrative decisions (Vavilov at para 90). Second, they argue that, even when applying a deferential standard, interpretations that are contrary to the legislative purpose of the grant of power, contrary to the overarching purpose of the Act, or contrary to Canada’s international obligations will necessarily be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 15`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1032`; citation: `Vavilov`; hash: `23f61f113aa4c4279b482afea38dec300f381d5191f2e7ba453c89f1c2885d55`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: `IX. STANDARD OF REVIEW
[48] After hearing these applications, the Supreme Court released its decision in Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov]. Accordingly, I invited the parties to make post-hearing submissions on the impact of Vavilov on the applicable standard of review.
[49] The Applicants assert that Vavilov strengthens their position that s. 159.3 of the Regulations is ultra vires for two reasons. First, because the Supreme Court held that external constraints limit the range of reasonable outcomes of administrative decisions (Vavilov at para 90). Second, they argue that, even when applying a deferential standard, interpretations that are contrary to the legislative purpose of the grant of power, contrary to the overarching purpose of the Act, or contrary to Canada’s international obligations will necessarily be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on `
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1033`; citation: `Vavilov`; hash: `69f5bdbf52da5c60ccd02b7c2f3877729017a78599c756c8ee96543f1b76770e`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: `IX. STANDARD OF REVIEW
[48] After hearing these applications, the Supreme Court released its decision in Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov]. Accordingly, I invited the parties to make post-hearing submissions on the impact of Vavilov on the applicable standard of review.
[49] The Applicants assert that Vavilov strengthens their position that s. 159.3 of the Regulations is ultra vires for two reasons. First, because the Supreme Court held that external constraints limit the range of reasonable outcomes of administrative decisions (Vavilov at para 90). Second, they argue that, even when applying a deferential standard, interpretations that are contrary to the legislative purpose of the grant of power, contrary to the overarching purpose of the Act, or contrary to Canada’s international obligations will necessarily be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on a correctness standard (Vavilov at para 57).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1034`; citation: `(Vavilov at para 90)`; hash: `69f5bdbf52da5c60ccd02b7c2f3877729017a78599c756c8ee96543f1b76770e`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: `IX. STANDARD OF REVIEW
[48] After hearing these applications, the Supreme Court released its decision in Canada (Minister of Citizenship and Immigration) v Vavilov, 2019 SCC 65 [Vavilov]. Accordingly, I invited the parties to make post-hearing submissions on the impact of Vavilov on the applicable standard of review.
[49] The Applicants assert that Vavilov strengthens their position that s. 159.3 of the Regulations is ultra vires for two reasons. First, because the Supreme Court held that external constraints limit the range of reasonable outcomes of administrative decisions (Vavilov at para 90). Second, they argue that, even when applying a deferential standard, interpretations that are contrary to the legislative purpose of the grant of power, contrary to the overarching purpose of the Act, or contrary to Canada’s international obligations will necessarily be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on a correctness standard (Vavilov at para 57).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1035`; citation: `(Vavilov at paras 114 and 120)`; hash: `69f5bdbf52da5c60ccd02b7c2f3877729017a78599c756c8ee96543f1b76770e`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: ` applicable standard of review.
[49] The Applicants assert that Vavilov strengthens their position that s. 159.3 of the Regulations is ultra vires for two reasons. First, because the Supreme Court held that external constraints limit the range of reasonable outcomes of administrative decisions (Vavilov at para 90). Second, they argue that, even when applying a deferential standard, interpretations that are contrary to the legislative purpose of the grant of power, contrary to the overarching purpose of the Act, or contrary to Canada’s international obligations will necessarily be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on a correctness standard (Vavilov at para 57).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1036`; citation: `Vavilov`; hash: `69f5bdbf52da5c60ccd02b7c2f3877729017a78599c756c8ee96543f1b76770e`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: `t Vavilov strengthens their position that s. 159.3 of the Regulations is ultra vires for two reasons. First, because the Supreme Court held that external constraints limit the range of reasonable outcomes of administrative decisions (Vavilov at para 90). Second, they argue that, even when applying a deferential standard, interpretations that are contrary to the legislative purpose of the grant of power, contrary to the overarching purpose of the Act, or contrary to Canada’s international obligations will necessarily be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on a correctness standard (Vavilov at para 57).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1037`; citation: `Vavilov`; hash: `f9797fa95f307445bdb3a2bf0d8e7eae61cbc4400fefcb0f75fd3a8bd4b26cd3`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: `ching purpose of the Act, or contrary to Canada’s international obligations will necessarily be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on a correctness standard (Vavilov at para 57).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1038`; citation: `Vavilov at para 68`; hash: `92ddaa8e36c0ea879bddeeeb7b452fecc02fa3c94b98d501eeda468b78509718`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: ` be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on a correctness standard (Vavilov at para 57).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1039`; citation: `states`; hash: `6630f24b961bb00736e007e82e935915e3bd992e0d7da34a92daf339bdfc8072`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: ` be unreasonable (Vavilov at paras 114 and 120).
[50] The Respondents say that Vavilov does not change their position on the vires issue, because, according to the Respondents, the Court cannot consider evidence that post-dates the promulgation of s. 159.3 of the Regulations. Therefore, the standard of review question is irrelevant as the issue is resolved before it is necessary to consider the appropriate standard of review.
[51] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on a correctness standard (Vavilov at para 57).`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-1040`; citation: `(Vavilov at para 57)`; hash: `a36b39ded9013679ea8fdaf57b3d0cd5ce90ed1bc2e6f712b92c3ad2d97c9265`
  - Proposed evidence: `Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended.`
  - Decision context: `] Taking these positions into consideration, and the direction provided in Vavilov, in my view, the standard of review for the vires considerations is reasonableness. Vavilov at para 68 states:
Reasonableness review does not give administrative decision makers free rein in interpreting their enabling statutes, and therefore does not give them licence to enlarge their powers beyond what the legislature intended. Instead, it confirms that the governing statutory scheme will always operate as a constraint on administrative decision makers and as a limit on their authority. Even where the reasonableness standard is applied in reviewing a decision maker’s interpretation of its authority, precise or narrow statutory language will necessarily limit the number of reasonable interpretations open to the decision maker - perhaps limiting it [to] one…
[52] The issue of whether s. 159.3 of the Regulations and s. 101(1)(e) of the IRPA violate the Charter will be considered on a correctness standard (Vavilov at para 57).`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.

### 19. `teacher-phrase-supportive-0019`

- Proposed treatment: **supportive**
- Support: **2** examples; mean confidence **0.95**
- Span quality: **repaired**
- Phrase: `when it is validly engaged, s. 490(9) empowers the court to order the return of property to a lawful owner or possessor or, if there is no known lawful owner or possessor, order it forfeited to the crown`

Evidence:
- `citation-context-0575`; citation: `Breton, at paras. 68-69`; hash: `1b300844ba4eb9a2a1d4a04751196252df7194219d6451bdebd63ec7660c858d`
  - Proposed evidence: `When it is validly engaged, s. 490(9) empowers the court to order the return of property to a lawful owner or possessor or, if there is no known lawful owner or possessor, order it forfeited to the Crown`
  - Decision context: `[124] When it is validly engaged, s. 490(9) empowers the court to order the return of property to a lawful owner or possessor or, if there is no known lawful owner or possessor, order it forfeited to the Crown (see Breton, at paras. 68-69; Gagnon, at para. 105; see also Hollaman, at para. 97; Ayotte v. R., 2025 QCCS 546, 2 C.R. (8th) 289, at paras. 49-50). This is the forfeiture provision we are asked to consider here:
(9) Subject to this or any other Act of Parliament, if
(9) Sous réserve des autres dispositions de la présente loi ou de toute autre loi fédérale :
(a) a judge referred to in subsection (7), where a judge ordered the detention of anything seized under subsection (3), or
a) le juge visé au paragraphe (7), lorsqu’un juge a ordonné la détention d’une chose saisie en application du paragraphe (3);
(b) a justice, in any other case,
b) le juge de paix, dans tout autre cas,
is satisfied that the periods of detention provided for or ordered under subsections (1) to (3) in respect of anything seized have expired and proceedings have not been instituted in which the thing detained may be required or, where those periods have not expired, that the continued detention of the thing seized will not be required for any purpose mentioned in subsection (1) or (4), he shall
qui est convaincu que les périodes de détention prévues aux paragraphes (1) à (3) ou ordonnées en application de ceux-ci sont terminées et que des`
  - Offsets repaired: `True`; confidence: `0.95`
- `citation-context-0576`; citation: `Gagnon, at para. 105`; hash: `a2360277944f53be61a18b45d35a60fab5a86e0567c54bf658227707920caea5`
  - Proposed evidence: `When it is validly engaged, s. 490(9) empowers the court to order the return of property to a lawful owner or possessor or, if there is no known lawful owner or possessor, order it forfeited to the Crown`
  - Decision context: `[124] When it is validly engaged, s. 490(9) empowers the court to order the return of property to a lawful owner or possessor or, if there is no known lawful owner or possessor, order it forfeited to the Crown (see Breton, at paras. 68-69; Gagnon, at para. 105; see also Hollaman, at para. 97; Ayotte v. R., 2025 QCCS 546, 2 C.R. (8th) 289, at paras. 49-50). This is the forfeiture provision we are asked to consider here:
(9) Subject to this or any other Act of Parliament, if
(9) Sous réserve des autres dispositions de la présente loi ou de toute autre loi fédérale :
(a) a judge referred to in subsection (7), where a judge ordered the detention of anything seized under subsection (3), or
a) le juge visé au paragraphe (7), lorsqu’un juge a ordonné la détention d’une chose saisie en application du paragraphe (3);
(b) a justice, in any other case,
b) le juge de paix, dans tout autre cas,
is satisfied that the periods of detention provided for or ordered under subsections (1) to (3) in respect of anything seized have expired and proceedings have not been instituted in which the thing detained may be required or, where those periods have not expired, that the continued detention of the thing seized will not be required for any purpose mentioned in subsection (1) or (4), he shall
qui est convaincu que les périodes de détention prévues aux paragraphes (1) à (3) ou ordonnées en application de ceux-ci sont terminées et que des procédures à l’occasi`
  - Offsets repaired: `True`; confidence: `0.95`

Review fields: `review_decision = approve | reject | needs_context`; add rationale in `review_notes` in the JSON packet.
