# Five-Case Discussion Unit Pilot

Model: `gpt-4.1-nano`
Pricing used: `$0.10 / 1M` input tokens and `$0.40 / 1M` output tokens
Calls: 5 total, one per selected non-SCC case
Canonical writes: none

| Case ID | Window | Status | Units | Input tokens | Output tokens | Estimated cost | Review |
|---:|---:|---|---:|---:|---:|---:|---|
| 15108 | 0-0 | complete | 1 | 350 | 86 | $0.0000694 | [plain-language review](case_15108_plain_language.md) |
| 7948 | 1-5 | complete | 5 | 1,137 | 433 | $0.0002869 | [plain-language review](case_7948_plain_language.md) |
| 16200 | 0-10 | complete | 4 | 1,971 | 355 | $0.0003391 | [plain-language review](case_16200_plain_language.md) |
| 27697 | 1-11 | complete | 8 | 1,325 | 685 | $0.0004065 | [plain-language review](case_27697_plain_language.md) |
| 5169 | 1-12 | complete | 3 | 2,025 | 292 | $0.0003193 | [plain-language review](case_5169_plain_language.md) |

## Cost

All five calls total: **$0.0014212**
Average cost per case: **$0.0002842**

The initial three responses were rejected because the deterministic packet incorrectly treated an unnumbered case header as a semantic paragraph. The packager now excludes that header whenever numbered legal paragraphs exist, while retaining header-only records. The three cases were rerun with the corrected request windows.
