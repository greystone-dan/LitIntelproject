# First Ruff and pip-audit baseline

Date: 2026-10-04

## Plain-language summary

The first Ruff pass found a large existing style/error baseline, mostly long
lines. The first dependency audit found advisories in several pinned direct and
transitive dependencies. These are visibility-only results: the workflow keeps
them reviewable without making pull requests fail, and this change does not
upgrade or otherwise alter dependencies.

## Tools and scope

The independent workflow is
[`.github/workflows/quality.yml`](../../.github/workflows/quality.yml).
It runs on pull requests and weekly. The tools are pinned in
`requirements-dev.txt`: Ruff 0.16.10 and pip-audit 2.10.1.

Commands, run against the current repository files:

```text
ruff check . --select E,F401 --output-format json
pip-audit --desc --format json -r requirements.txt
```

Ruff selects pycodestyle error rules and unused imports. pip-audit resolves the
dependencies named by `requirements.txt`; this is not a scan of an installed
production environment or a committed lockfile.

## Results

| Check | Result |
| --- | --- |
| Ruff 0.16.10 | 8,039 findings across 341 files; 135 are unused imports (`F401`). |
| pip-audit 2.10.1 | 188 packages audited; 242 known vulnerability matches across 18 packages. |

Ruff findings by rule:

| Rule | Findings |
| --- | ---: |
| `E501` line too long | 7,751 |
| `E402` module import not at top of file | 149 |
| `F401` unused import | 135 |
| `E101` indentation contains mixed spaces and tabs | 3 |
| `E713` test for membership should be `not in` | 1 |

Packages with pip-audit findings (package version and matching advisory count):

| Package | Version | Matches |
| --- | ---: | ---: |
| `aiohttp` | 3.9.5 | 68 |
| `pypdf` | 4.2.0 | 85 |
| `python-multipart` | 0.0.9 | 14 |
| `starlette` | 0.37.2 | 14 |
| `langchain-core` | 0.2.43 | 11 |
| `transformers` | 4.57.6 | 9 |
| `langchain` | 0.2.5 | 6 |
| `langchain-community` | 0.2.5 | 5 |
| `python-jose` | 3.3.0 | 5 |
| `langsmith` | 0.1.147 | 5 |
| `requests` | 2.32.3 | 4 |
| `langchain-text-splitters` | 0.2.4 | 4 |
| `black` | 24.4.2 | 3 |
| `langchain-openai` | 0.1.8 | 2 |
| `python-dotenv` | 1.0.1 | 2 |
| `pytest` | 8.2.2 | 2 |
| `ecdsa` | 0.19.2 | 2 |
| `sentence-transformers` | 3.0.0 | 1 |

## Interpretation and limits

The counts are a starting point for triage, not a claim that every reported
issue is reachable or exploitable in this application. pip-audit's advisory
data can change between runs, and a compatible fix may require dependency
testing. The Ruff baseline is similarly informational; broad cleanup is
outside this task. Each workflow job uploads its tool output, tool version, and
exit status separately so later runs can be compared without hiding findings.
