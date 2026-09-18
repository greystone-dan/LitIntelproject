# Executive verdict
The V1.4 Discussion Unit and V1.3 sub-theme outputs demonstrate a significant improvement in the coherence and precision of legal-text analysis for Canadian immigration case law. However, while the outputs are generally faithful to the source text, there are areas requiring further refinement to enhance their utility as a low-trust human review aid. The system is safe to continue improving, but specific deterministic changes are necessary to address identified issues.

# Cross-case findings
1. **Coherence of sub-themes**: Most sub-themes are coherent argument units, particularly in cases with more complex legal issues (e.g., Case 18674). However, some sub-themes in shorter cases (e.g., Case 677) appear merely contiguous without clear argumentative structure.
2. **Reduction of false positives**: V1.3 has successfully reduced procedural `claim` false positives while retaining explicit forms such as `claims that`, `argues`, and `submits`. This is evident in the outputs for Cases 677 and 1093.
3. **Local contrast gating**: The implementation of local contrast gating has effectively reduced weak cues like `but`, `cannot`, and `fails` without losing meaningful limitations. This is particularly noticeable in Case 1171.
4. **Role precision**: The roles of issue, party position, evidence/fact, governing rule, reasoning/application, counterargument/limitation, and disposition are generally precise, though some roles in Case 18674 could benefit from clearer delineation.
5. **Metadata handling**: Metadata, headings, judgment, certification, record, and solicitor spans are handled correctly across all cases, maintaining integrity and traceability.
6. **Key terms utility**: Raw and display key terms are useful, but some outputs could benefit from clearer contextualization to avoid confusion with source evidence.
7. **Explanation quality**: Explanations generally describe the actor, proposition, evidence, rule, application, or outcome effectively, though some explanations could be more concise.
8. **Provenance and integrity**: Paragraph ranges, chunk IDs, offsets, source hashes, text hashes, and configuration/version fields are internally trustworthy, supporting the integrity of the outputs.
9. **Boundary structure improvement**: V1.4 has improved the large-case boundary structure without altering smaller-case unit counts or source identity, ensuring consistency across cases.

# Case-by-case review
### Case 677
- **Strongest sub-theme**: Sub-theme 1 (disposition, evidence_fact, governing_rule, reasoning_application).
- **Weakest sub-theme**: Sub-theme 3 (counterargument_limitation, evidence_fact, issue, reasoning_application).
- **Correct observation**: The outputs accurately reflect the disposition and reasoning of the case.
- **Questionable observation**: The role of counterargument in sub-theme 3 lacks clarity and could mislead users.
- **Explanation faithfulness**: Explanations are generally faithful but could be more concise.
- **Concrete improvement**: Clarify the role of counterarguments in sub-theme 3 to enhance understanding.

### Case 1093
- **Strongest sub-theme**: Sub-theme 3 (counterargument_limitation, evidence_fact, governing_rule, issue, party_position, reasoning_application).
- **Weakest sub-theme**: Sub-theme 1 (governing_rule).
- **Correct observation**: The outputs effectively capture the party position and its implications.
- **Questionable observation**: The governing rule in sub-theme 1 lacks sufficient context.
- **Explanation faithfulness**: Explanations are mostly faithful but could benefit from additional context.
- **Concrete improvement**: Provide more context for the governing rule in sub-theme 1.

### Case 1171
- **Strongest sub-theme**: Sub-theme 1 (counterargument_limitation, disposition, evidence_fact, governing_rule, reasoning_application).
- **Weakest sub-theme**: Sub-theme 2 (no explicit argument role cue).
- **Correct observation**: The outputs accurately reflect the reasoning and application of the law.
- **Questionable observation**: The lack of explicit argument role cues in sub-theme 2 may confuse users.
- **Explanation faithfulness**: Explanations are generally faithful and informative.
- **Concrete improvement**: Enhance the clarity of sub-theme 2 to avoid confusion.

### Case 18674
- **Strongest sub-theme**: Sub-theme 1 (disposition, evidence_fact, governing_rule, reasoning_application).
- **Weakest sub-theme**: Sub-theme 72 (no explicit argument role cue).
- **Correct observation**: The outputs effectively capture the complexity of the case.
- **Questionable observation**: The lack of explicit argument role cues in sub-theme 72 may mislead users.
- **Explanation faithfulness**: Explanations are mostly faithful but could be more concise.
- **Concrete improvement**: Clarify the role of arguments in sub-theme 72 to enhance understanding.

# Role taxonomy review
The role taxonomy is generally well-defined, with clear distinctions between issue, party position, evidence/fact, governing rule, reasoning/application, counterargument/limitation, and disposition. However, some roles, particularly in shorter cases, could benefit from more explicit definitions to avoid ambiguity.

# Sub-theme and boundary review
Sub-themes are mostly coherent and well-structured, but some shorter cases exhibit a lack of depth in argumentation. The boundary structure has improved, particularly in larger cases, without compromising the integrity of smaller cases.

# Explanation quality
Explanations are generally clear and informative, describing the relevant actors, propositions, and outcomes. However, some explanations could be more concise and focused to enhance clarity.

# Provenance and integrity
Provenance and integrity are well-maintained, with accurate tracking of paragraph ranges, chunk IDs, offsets, and hashes. This supports the reliability of the outputs.

# Prioritized deterministic improvements
1. Clarify the role of counterarguments in sub-themes, particularly in Cases 677 and 18674.
2. Provide more context for governing rules in sub-themes, especially in Cases 1093 and 1171.
3. Enhance the clarity of sub-theme outputs that lack explicit argument role cues, particularly in Cases 1171 and 18674.

# Residual uncertainty
While the outputs are generally reliable, there remains some uncertainty regarding the clarity of certain roles and the depth of argumentation in shorter cases. Further refinement is needed to ensure that all outputs are equally informative and clear.

In conclusion, the system is ready for another bounded engineering iteration, with specific improvements identified to enhance its utility as a low-trust human review aid.