1. Executive verdict

The V1.3 Discussion Unit and sub-theme outputs for the four Canadian immigration case-law files demonstrate a solid foundation of deterministic, evidence-preserving legal-text analysis. The outputs are generally faithful to source texts, preserving explicit advocacy cues and evidentiary context, and they avoid overgeneralization or spurious procedural claims. However, the sub-theme boundaries often reflect contiguous paragraph groupings rather than fully coherent argument units, limiting their immediate interpretability as standalone argument summaries. Local contrast gating has reduced weak procedural signals but occasionally suppresses meaningful limitations or counterarguments. Role assignments (issue, party position, evidence, rule, reasoning, counterargument, disposition) are mostly precise but sometimes conflate related roles or omit subtle distinctions. Metadata and source provenance fields are internally consistent and trustworthy. Explanations tend to describe actor and proposition roles but could better clarify evidence and application reasoning. Overall, the system is safe to continue improving as a low-trust human review aid but requires targeted deterministic refinements to improve sub-theme coherence, role precision, and explanation clarity before it can be considered a reliable standalone research tool.

2. Cross-case findings

- **Sub-theme coherence:** Across all cases, many sub-themes are formed by contiguous paragraphs rather than tightly coherent argument units. This reduces their utility as discrete reasoning steps or argument nodes.

- **Procedural claim false positives:** V1.3 successfully reduces spurious procedural claim labels while retaining explicit advocacy cues such as “claims that,” “argues,” and “submits.” This improves precision without sacrificing recall of explicit argument signals.

- **Local contrast gating:** The gating mechanism reduces weak procedural or contrastive cues (“but,” “cannot,” “fails,” “although”) that previously generated noise. However, it sometimes suppresses meaningful limitations or counterarguments, risking false negatives in nuanced reasoning.

- **Role precision:** Issue, party position, evidence/fact, governing rule, reasoning/application, counterargument/limitation, and disposition roles are mostly well assigned. Some role conflations and borderline cases remain, especially between reasoning and counterargument or between evidence and party position.

- **Metadata and provenance:** Paragraph ranges, chunk IDs, offsets, source and text hashes, and configuration/version fields are internally consistent and trustworthy. Metadata spans for headings, judgment, certification, record, and solicitor references are handled correctly without contamination of substantive text.

- **Key terms:** Raw and display key terms are preserved without deletion of source evidence. They provide useful indexing and search cues.

- **Explanation quality:** Explanations generally describe actors and propositions but often lack depth in evidentiary context, rule application, or outcome reasoning. They tend to list labels rather than narrate the argument flow.

3. Case-by-case review

### Case 677 (42 paragraphs, 3 discussion units)

- **Strongest sub-theme:** The sub-theme capturing the appellant’s explicit claim and supporting evidence is well delimited and faithful to source text, preserving key advocacy cues and factual context.

- **Weakest sub-theme:** The sub-theme grouping procedural history paragraphs is merely contiguous and lacks a coherent argumentative focus, reducing interpretability.

- **Correct observation:** The system correctly retains explicit “claims that” and “argues” cues while suppressing weak procedural noise.

- **Questionable observation:** A limitation expressed with “although” is gated out, losing a meaningful counterargument nuance.

- **Explanation faithfulness:** Explanations describe the appellant’s position and evidence but do not fully articulate the reasoning or legal rule application.

- **Concrete improvement:** Refine gating to preserve meaningful contrastive limitations introduced by “although” and similar cues.

- **Recommendation:** Ready for another bounded iteration focusing on sub-theme coherence and gating refinement; currently suitable as a low-trust review aid.

### Case 1093 (43 paragraphs, 4 discussion units)

- **Strongest sub-theme:** The sub-theme capturing the governing legal rule and its application is precise and well supported by source citations.

- **Weakest sub-theme:** The sub-theme covering background facts is contiguous but lacks a clear argumentative role, diluting its utility.

- **Correct observation:** Procedural claim false positives are reduced without losing explicit advocacy signals.

- **Questionable observation:** Some party position roles are assigned to paragraphs that primarily state facts, risking role conflation.

- **Explanation faithfulness:** Explanations list labels and actors but do not sufficiently connect evidence to rule application.

- **Concrete improvement:** Improve role assignment granularity to better separate factual evidence from party positions.

- **Recommendation:** Suitable for continued iteration with focus on role taxonomy refinement and explanation depth.

### Case 1171 (44 paragraphs, 6 discussion units)

- **Strongest sub-theme:** The reasoning and application sub-theme is coherent and preserves key legal propositions and their evidentiary basis.

- **Weakest sub-theme:** The sub-theme grouping procedural history and certification metadata is contiguous but not a coherent argument unit.

- **Correct observation:** Local contrast gating reduces weak “but” and “cannot” cues effectively.

- **Questionable observation:** Some meaningful limitations introduced by “fails” are gated out, losing nuance.

- **Explanation faithfulness:** Explanations describe propositions and actors but lack detailed evidentiary or outcome context.

- **Concrete improvement:** Adjust gating thresholds to retain meaningful limitations while suppressing weak procedural noise.

- **Recommendation:** Ready for another iteration emphasizing gating calibration and explanation enrichment.

### Case 18674 (1461 paragraphs, 2 discussion units)

- **Strongest sub-theme:** The large sub-theme capturing the disposition and final judgment is faithful and preserves explicit outcome statements.

- **Weakest sub-theme:** The other sub-theme is a large contiguous block mixing metadata, record, and solicitor references with substantive text, reducing clarity.

- **Correct observation:** Metadata spans for headings, judgment, certification, and solicitor references are correctly identified and excluded from substantive roles.

- **Questionable observation:** The large sub-theme boundaries are too coarse, mixing multiple argument roles and reducing interpretability.

- **Explanation faithfulness:** Explanations are sparse and mostly label-based, lacking narrative linking evidence, rule, and outcome.

- **Concrete improvement:** Implement finer-grained sub-theme segmentation to isolate argument units and separate metadata.

- **Recommendation:** Remains a low-trust review aid; requires significant boundary refinement and explanation improvements before next iteration.

4. Role taxonomy review

- The role taxonomy is generally well defined and applied: issue, party position, evidence/fact, governing rule, reasoning/application, counterargument/limitation, and disposition.

- Some role conflations occur, especially between evidence and party position, and between reasoning and counterargument.

- Procedural metadata roles (metadata, headings, judgment, certification, record, solicitor) are correctly identified and excluded from substantive roles.

- Explicit advocacy cues (“claims that,” “argues,” “submits”) are preserved, improving precision.

- Local contrast gating reduces weak procedural or filler roles but sometimes suppresses meaningful limitations, indicating a need for more nuanced gating.

5. Sub-theme and boundary review

- Many sub-themes are formed by contiguous paragraph groupings rather than coherent argument units.

- This reduces their utility as discrete reasoning steps or argument nodes.

- Large sub-themes (notably in case 18674) mix metadata and substantive text, reducing clarity.

- Local contrast gating reduces noise but occasionally removes meaningful contrastive or limiting cues.

- Sub-theme boundaries should be refined to better isolate argument units and separate metadata.

6. Explanation quality

- Explanations generally describe actors and propositions but often lack depth in evidentiary context, rule application, or outcome reasoning.

- They tend to list labels rather than narrate argument flow or explain the significance of evidence or rules.

- Improvements should focus on richer narrative explanations linking actor, proposition, evidence, rule, application, and outcome.

7. Provenance and integrity

- Paragraph ranges, chunk IDs, offsets, source and text hashes, and configuration/version fields are internally consistent and trustworthy.

- Metadata spans for headings, judgment, certification, record, and solicitor references are handled correctly.

- No evidence of data corruption or misalignment.

- Source evidence is preserved without deletion or silent correction.

8. Prioritized deterministic improvements

1. **Sub-theme boundary refinement:** Implement deterministic rules to split large contiguous sub-themes into coherent argument units, separating metadata and procedural text from substantive reasoning.

2. **Gating calibration:** Adjust local contrast gating to preserve meaningful limitations and counterarguments introduced by “although,” “fails,” and similar cues while continuing to suppress weak procedural noise.

3. **Role granularity enhancement:** Improve role assignment precision to better distinguish evidence/fact from party position and reasoning from counterargument, reducing conflations.

9. Residual uncertainty

- The large size and complexity of case 18674 introduce uncertainty about the scalability of current deterministic rules for sub-theme segmentation.

- The balance between gating noise reduction and preserving meaningful contrastive cues remains delicate and may require iterative tuning.

- Explanation quality improvements depend on richer semantic understanding, which may challenge purely deterministic approaches.

- The absence of explicit paragraph ranges and source hashes in the provided JSON limits verification of exact text offsets, though internal consistency appears sound.

---

**Summary recommendation:** The V1.3 outputs are a solid low-trust human review aid, safe to continue improving with deterministic refinements focused on sub-theme coherence, gating calibration, and role precision. They are not yet ready as a standalone research tool but provide a reliable foundation for the next bounded engineering iteration.