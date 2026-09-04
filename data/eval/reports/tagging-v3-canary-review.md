# V3 Canary Review

Status: proposed human review
Taxonomy: `ca_legal_v3_core`

Review every occurrence for exact evidence, canonical category/value, and whether `mention` is the correct evidence role. This is a review snapshot, not activation approval.

## Review checklist

- Confirm the evidence is an exact source span.
- Confirm the canonical category and value are appropriate.
- Confirm the match is a mention only, not an inferred finding.
- Record false positives or alias decisions before expanding the canary.

## Occurrences (115)

| Case | Court | Category | Value | Evidence | Start | End | Rule | Language | Role | Source |
| ---: | --- | --- | --- | --- | ---: | ---: | --- | --- | --- | --- |
| 22 | FC | statute_or_instrument | irpa | Immigration and Refugee Protection Act | 588 | 626 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 633 | 637 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | country_or_territory | mexico | Mexico | 690 | 696 | country_or_territory.mexico | unknown | mention | core_whitelist |
| 22 | FC | country_or_territory | mexico | Mexico | 1126 | 1132 | country_or_territory.mexico | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 1162 | 1179 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 1225 | 1242 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | Refugee Protection Division | 1284 | 1311 | tribunal.rpd | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 1384 | 1388 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 1469 | 1473 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | Misrepresentation | 1925 | 1942 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 2014 | 2031 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 2304 | 2321 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | RPD | 3767 | 3770 | tribunal.rpd | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 4118 | 4122 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 4369 | 4373 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 4420 | 4424 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 4488 | 4505 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | RPD | 4558 | 4561 | tribunal.rpd | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 4645 | 4649 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 4709 | 4713 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | RPD | 4734 | 4737 | tribunal.rpd | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 4853 | 4857 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | RPD | 4869 | 4872 | tribunal.rpd | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 4965 | 4982 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 5083 | 5087 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | RPD | 5131 | 5134 | tribunal.rpd | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | RPD | 5287 | 5290 | tribunal.rpd | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 5387 | 5404 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | RPD | 5590 | 5593 | tribunal.rpd | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 5631 | 5635 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 5903 | 5920 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 6182 | 6199 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | statute_or_instrument | irpa | IRPA | 6474 | 6478 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 22 | FC | explicit_legal_issue | misrepresentation | misrepresentation | 6518 | 6535 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 22 | FC | tribunal | rpd | Refugee Protection Division | 6585 | 6612 | tribunal.rpd | unknown | mention | core_whitelist |
| 35875 | FCA | explicit_legal_issue | stay_of_removal | stay of removal | 799 | 814 | explicit_legal_issue.stay_of_removal | unknown | mention | core_whitelist |
| 35875 | FCA | tribunal | iad | Immigration Appeal Division | 967 | 994 | tribunal.iad | unknown | mention | core_whitelist |
| 35875 | FCA | country_or_territory | india | India | 1056 | 1061 | country_or_territory.india | unknown | mention | core_whitelist |
| 35875 | FCA | tribunal | iad | Immigration Appeal Division | 1617 | 1644 | tribunal.iad | unknown | mention | core_whitelist |
| 35875 | FCA | procedure_or_record | prra | pre-removal risk assessment | 2044 | 2071 | procedure_or_record.prra | unknown | mention | core_whitelist |
| 35875 | FCA | country_or_territory | india | India | 2729 | 2734 | country_or_territory.india | unknown | mention | core_whitelist |
| 35875 | FCA | country_or_territory | india | India | 3519 | 3524 | country_or_territory.india | unknown | mention | core_whitelist |
| 35875 | FCA | procedure_or_record | prra | PRRA | 3558 | 3562 | procedure_or_record.prra | unknown | mention | core_whitelist |
| 35875 | FCA | country_or_territory | india | India | 3643 | 3648 | country_or_territory.india | unknown | mention | core_whitelist |
| 35875 | FCA | explicit_legal_issue | stay_of_removal | stay of removal | 4107 | 4122 | explicit_legal_issue.stay_of_removal | unknown | mention | core_whitelist |
| 35875 | FCA | country_or_territory | india | India | 5691 | 5696 | country_or_territory.india | unknown | mention | core_whitelist |
| 35875 | FCA | statute_or_instrument | irpa | Immigration and Refugee Protection Act | 6039 | 6077 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 35875 | FCA | tribunal | iad | Immigration Appeal Division | 6248 | 6275 | tribunal.iad | unknown | mention | core_whitelist |
| 37521 | RPD | tribunal | rpd | RPD | 0 | 3 | tribunal.rpd | unknown | mention | core_whitelist |
| 37521 | RPD | statute_or_instrument | irpa | Immigration and Refugee Protection Act | 816 | 854 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 37521 | RPD | statute_or_instrument | irpa | IRPA | 856 | 860 | statute_or_instrument.irpa | unknown | mention | core_whitelist |
| 37521 | RPD | tribunal | rpd | RPD | 19576 | 19579 | tribunal.rpd | unknown | mention | core_whitelist |
| 37521 | RPD | tribunal | rpd | RPD | 23603 | 23606 | tribunal.rpd | unknown | mention | core_whitelist |
| 37521 | RPD | tribunal | rpd | RPD | 23654 | 23657 | tribunal.rpd | unknown | mention | core_whitelist |
| 37521 | RPD | tribunal | rpd | RPD | 23704 | 23707 | tribunal.rpd | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 1549 | 1588 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 1868 | 1907 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 2187 | 2226 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 2570 | 2609 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 3106 | 3115 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | agency | csis | Canadian Security Intelligence Service | 3294 | 3332 | agency.csis | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | Liberation Tigers of Tamil Eelam | 3376 | 3408 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 3473 | 3482 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 3533 | 3542 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 4545 | 4584 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 13340 | 13379 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 19533 | 19542 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 19720 | 19729 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | Liberation Tigers of Tamil Eelam | 19780 | 19812 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 19815 | 19819 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 19882 | 19891 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 20044 | 20083 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 22857 | 22866 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 24240 | 24249 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | agency | csis | Canadian Security Intelligence Service | 24646 | 24684 | agency.csis | unknown | mention | core_whitelist |
| 35860 | SCC | agency | csis | CSIS | 24687 | 24691 | agency.csis | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 24725 | 24729 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | agency | csis | CSIS | 24766 | 24770 | agency.csis | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 24808 | 24817 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 24898 | 24902 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 25091 | 25100 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 25630 | 25639 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 25765 | 25769 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 25962 | 25966 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 26798 | 26802 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 26900 | 26904 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 26943 | 26947 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 27012 | 27016 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | explicit_legal_issue | misrepresentation | misrepresentation | 27064 | 27081 | explicit_legal_issue.misrepresentation | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 27163 | 27167 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 28276 | 28280 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 28545 | 28549 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 28870 | 28879 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 29007 | 29016 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | procedure_or_record | humanitarian_and_compassionate | humanitarian and compassionate | 29214 | 29244 | procedure_or_record.humanitarian_and_compassionate | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 33998 | 34007 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 34229 | 34268 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 34276 | 34315 | statute_or_instrument.charter | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 37492 | 37501 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | explicit_legal_issue | refoulement | refoulement | 42687 | 42698 | explicit_legal_issue.refoulement | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 52318 | 52327 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 52675 | 52684 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | explicit_legal_issue | refoulement | refoulement | 63210 | 63221 | explicit_legal_issue.refoulement | unknown | mention | core_whitelist |
| 35860 | SCC | explicit_legal_issue | refoulement | refoulement | 74982 | 74993 | explicit_legal_issue.refoulement | unknown | mention | core_whitelist |
| 35860 | SCC | explicit_legal_issue | refoulement | refoulement | 79393 | 79404 | explicit_legal_issue.refoulement | unknown | mention | core_whitelist |
| 35860 | SCC | explicit_legal_issue | refoulement | refoulement | 90544 | 90555 | explicit_legal_issue.refoulement | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 103385 | 103389 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 103689 | 103698 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 109563 | 109567 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 109692 | 109696 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 111473 | 111482 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 117037 | 117046 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | organization | ltte | LTTE | 117066 | 117070 | organization.ltte | unknown | mention | core_whitelist |
| 35860 | SCC | country_or_territory | sri_lanka | Sri Lanka | 127418 | 127427 | country_or_territory.sri_lanka | unknown | mention | core_whitelist |
| 35860 | SCC | statute_or_instrument | charter | Canadian Charter of Rights and Freedoms | 127967 | 128006 | statute_or_instrument.charter | unknown | mention | core_whitelist |

## Review decision

Pending human review. Do not activate corpus-wide V3 tagging until reviewed precision and corrections are recorded.
