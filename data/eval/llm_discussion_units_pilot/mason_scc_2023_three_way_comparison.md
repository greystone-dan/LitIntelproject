# Mason v. Canada, 2023 SCC 21: Three-Way Comparison

The same 189 numbered legal paragraphs were reviewed in the same five bounded windows.

| Approach | Input to the model/system | Segmentation result | Plain-language output |
|---|---|---:|---|
| Deterministic | Database chunks plus rule-based continuity, citation/statute/tag signals, and argument-role cues | 1 broad chunk-level unit; 8 evidence subthemes | Rule-based evidence descriptions, not fluent semantic summaries |
| Hybrid | Paragraph text plus deterministic baseline and metadata | 52 LLM units across five windows | Semantic labels, explanations, transitions, and confidence |
| LLM-only | Paragraph indices and source text only | 60 LLM units across five windows | Semantic labels, explanations, transitions, and confidence without deterministic context |

## Interpretation

The deterministic layer processed the full case but operated on 18 database chunks, not the 189 numbered legal paragraphs. It produced one broad unit spanning the case and eight finer evidence clusters.

The hybrid model received the paragraph text and deterministic baseline signals. It produced 52 units and was able to use the rule-based signals as additional context.

The LLM-only model received only numbered paragraph text. It produced 60 units, slightly finer segmentation than the hybrid run. This shows that the model can identify Discussion Unit boundaries from the decision text itself; the deterministic layer is not required for basic segmentation.

The deterministic layer remains valuable for provenance, citation/statute/tag evidence, offsets, validation, and comparison. The hybrid version may be more grounded, while the blind version is the cleaner test of the LLM's independent segmentation ability.

## Text-Only Cost

The five successful LLM-only windows used 37,401 input tokens and 5,717 output tokens, for an estimated total cost of **$0.0060269**.

## Review Files

- Deterministic: [Mason deterministic reading](mason_scc_2023_deterministic.md)
- Hybrid combined summary: [Mason hybrid plain-language summary](mason_scc_2023_plain_language_combined.md)
- LLM-only window 1: [paragraphs 1-60](mason_scc_2023_llm_only_window_01_plain_language.md)
- LLM-only window 2: [paragraphs 61-120](mason_scc_2023_llm_only_window_02_plain_language.md)
- LLM-only window 3a1: [paragraphs 121-122](mason_scc_2023_llm_only_window_03a1_plain_language.md)
- LLM-only window 3a2: [paragraphs 123-155](mason_scc_2023_llm_only_window_03a2_plain_language.md)
- LLM-only window 3b: [paragraphs 156-189](mason_scc_2023_llm_only_window_03b_plain_language.md)
