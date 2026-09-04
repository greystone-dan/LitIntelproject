# Federal Court Metadata Anchor Boundary

Status: implemented

Evidence: Iteration-1 AI triage reviewed 921 occurrences and produced 778 advisory suggestions. Case 31 (`2004 FC 1732`) emitted repeated `Chemex` and `Fats` `case_short` matches whose anchor span was the page metadata block `Court (s) Database / Date / Neutral citation`, rather than legal prose. The same report showed 48 FC `WRONG_SPAN` suggestions and 7 `WRONG_ALIAS` suggestions. Exact source spans remained valid, so this is a semantic precision issue, not an offset issue.

Implemented: Added a regression fixture for Federal Court metadata headers and prevented metadata labels from becoming case-citation anchor content. The bounded FC report now verifies no short-form anchor contains the metadata block, while exact spans remain valid. Ordinary body-text mentions and valid duplicate occurrences remain eligible.

Risk boundary: Federal Court page-wrapper/header handling only. Do not suppress valid aliases globally, including `Sosa`, and do not change SCC short-form or pinpoint semantics without separate evidence.

Smallest falsifiable check: On case 31, the metadata block must produce no anchored short-form matches while body-text `Chemex` occurrences remain eligible; exact spans must remain valid.

Validation: `pytest tests/test_citations.py -q` passed 105 tests; the 10-case FC report verified 159/159 exact spans. Residual risk: the legal style-of-cause caption still produces some repeated party-name aliases, which requires a separate caption-boundary experiment.
