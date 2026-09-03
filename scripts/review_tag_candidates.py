"""Review candidate tags mined from stored decision text without writing to the database."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sqlalchemy import select

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.database import Case, SessionLocal
from backend.legal_tagger import COUNTRIES, ORGANIZATIONS, RULES


WORD_RE = re.compile(r"[A-Za-z][A-Za-z'’-]*")
SENTENCE_RE = re.compile(r"[^.!?\n]{20,}")
ORGANIZATION_RE = re.compile(
    r"\b(?:[A-Z][A-Za-z'’-]+\s+){0,5}"
    r"(?:Party|Movement|Front|Organization|Organisation|Association|Army|Brigade|Force|Committee|Council|Government|Militia|Group|Network|Coalition|Church|Union)\b"
)
COUNTRY_CONTEXT_RE = re.compile(
    r"\b(?:from|in|to|of|within|return(?:ed)?\s+to|citizen\s+of|national\s+of)\s+"
    r"([A-Z][A-Za-z'’-]*(?:\s+[A-Z][A-Za-z'’-]*){0,3})"
)
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "by", "for", "from", "in", "is", "of",
    "on", "or", "the", "to", "was", "were", "with", "that", "this", "which", "their",
    "there", "under", "has", "have", "had", "not", "into", "than", "also", "after",
}
STOP_PHRASES = {"The Federal Court", "The Court", "Federal Court", "Court of Appeal", "Supreme Court"}
NON_COUNTRY_TERMS = {
    "Canada", "Canadian", "Federal Court", "Supreme Court", "Minister", "Minister of",
    "Citizenship and Immigration", "Immigration and Refugee Protection Act",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=250)
    parser.add_argument("--limit", type=int, default=None, help="Maximum cases to scan")
    parser.add_argument("--min-count", type=int, default=5, help="Minimum candidate count")
    parser.add_argument("--sample-size", type=int, default=3, help="Samples per candidate")
    parser.add_argument("--report-json", type=Path, default=Path("data/eval/reports/tag-candidate-review.json"))
    return parser.parse_args()


def _known_patterns(patterns: dict[str, str]) -> tuple[re.Pattern[str], ...]:
    return tuple(re.compile(pattern, re.IGNORECASE) for pattern in patterns.values())


def _known(value: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(pattern.fullmatch(value) for pattern in patterns)


def _sample(case: Case, text: str, start: int, end: int) -> dict[str, object]:
    left = max(0, start - 100)
    right = min(len(text), end + 140)
    return {
        "case_id": case.id,
        "citation": case.citation,
        "title": case.title,
        "context": " ".join(text[left:right].split()),
    }


def _add_candidate(
    counts: Counter[str], samples: dict[str, list[dict[str, object]]], value: str,
    case: Case, text: str, start: int, end: int, sample_size: int,
) -> None:
    value = " ".join(value.split()).strip(" ,.;:()[]")
    words = value.lower().split()
    while words and words[0] in STOPWORDS:
        words.pop(0)
    while words and words[-1] in STOPWORDS:
        words.pop()
    value = " ".join(words)
    if len(value) < 4 or value in STOP_PHRASES or not any(word not in STOPWORDS for word in words):
        return
    counts[value] += 1
    if len(samples[value]) < sample_size:
        samples[value].append(_sample(case, text, start, end))


def _mine_sentence_phrases(sentence: str, start: int, end: int) -> list[tuple[str, int, int]]:
    words = list(WORD_RE.finditer(sentence))
    matches: list[tuple[str, int, int]] = []
    for index, word in enumerate(words):
        if word.end() < start or word.start() > end:
            continue
        for size in range(2, 6):
            first = max(0, index - size + 1)
            last = min(len(words), first + size)
            if last - first < 2 or not any(item.start() <= end and item.end() >= start for item in words[first:last]):
                continue
            phrase = sentence[words[first].start():words[last - 1].end()]
            matches.append((phrase, words[first].start(), words[last - 1].end()))
    return matches


def scan_cases(batch_size: int, limit: int | None, min_count: int, sample_size: int) -> dict[str, object]:
    compiled_rules = [(rule, re.compile(rule.pattern, re.IGNORECASE | re.DOTALL)) for rule in RULES]
    category_counts: Counter[str] = Counter()
    candidate_counts: dict[str, Counter[str]] = defaultdict(Counter)
    candidate_samples: dict[str, dict[str, list[dict[str, object]]]] = defaultdict(lambda: defaultdict(list))
    organization_patterns = _known_patterns(ORGANIZATIONS)
    country_patterns = _known_patterns(COUNTRIES)
    organizations: Counter[str] = Counter()
    countries: Counter[str] = Counter()
    organization_samples: dict[str, list[dict[str, object]]] = defaultdict(list)
    country_samples: dict[str, list[dict[str, object]]] = defaultdict(list)
    scanned = 0
    last_case_id = 0

    with SessionLocal() as session:
        while limit is None or scanned < limit:
            size = min(batch_size, limit - scanned) if limit else batch_size
            cases = session.scalars(select(Case).where(Case.id > last_case_id).order_by(Case.id).limit(size)).all()
            if not cases:
                break
            for case in cases:
                text = "\n".join(value for value in (case.title, case.summary, case.full_text) if value)
                for rule, pattern in compiled_rules:
                    matches = list(pattern.finditer(text))
                    category_counts[rule.category] += len(matches)
                    for match in matches:
                        sentence = next((item for item in SENTENCE_RE.finditer(text) if item.start() <= match.start() <= item.end()), None)
                        if sentence:
                            for phrase, start, end in _mine_sentence_phrases(sentence.group(0), match.start() - sentence.start(), match.end() - sentence.start()):
                                candidate = phrase.lower()
                                if candidate not in rule.pattern.lower() and candidate != rule.value.lower():
                                    _add_candidate(candidate_counts[rule.category], candidate_samples[rule.category], phrase, case, text, sentence.start() + start, sentence.start() + end, sample_size)
                for match in ORGANIZATION_RE.finditer(text):
                    if not _known(match.group(0), organization_patterns):
                        _add_candidate(organizations, organization_samples, match.group(0), case, text, match.start(), match.end(), sample_size)
                for match in COUNTRY_CONTEXT_RE.finditer(text):
                    candidate = match.group(1).strip(" ,.;:()[]")
                    if candidate in NON_COUNTRY_TERMS:
                        continue
                    if not _known(candidate, country_patterns) and not any(term in candidate for term in ("Court", "Minister", "Division", "Agency", "Canada")):
                        _add_candidate(countries, country_samples, match.group(1), case, text, match.start(1), match.end(1), sample_size)
                scanned += 1
                last_case_id = case.id
            if scanned % batch_size == 0:
                print(f"scanned_cases={scanned} last_case_id={last_case_id}", flush=True)

    categories = {}
    for category in sorted({rule.category for rule in RULES}):
        categories[category] = {
            "existing_match_count": category_counts[category],
            "candidate_phrases": [
                {"term": term, "occurrences": count, "samples": candidate_samples[category][term]}
                for term, count in candidate_counts[category].most_common()
                if count >= min_count
            ],
        }
    return {
        "scanned_cases": scanned,
        "categories": categories,
        "candidate_organizations": [
            {"term": term, "occurrences": count, "samples": organization_samples[term]}
            for term, count in organizations.most_common() if count >= min_count
        ],
        "candidate_countries": [
            {"term": term, "occurrences": count, "samples": country_samples[term]}
            for term, count in countries.most_common() if count >= min_count
        ],
    }


def main() -> None:
    args = parse_args()
    if args.batch_size < 1 or args.min_count < 1 or args.sample_size < 1:
        raise SystemExit("batch-size, min-count, and sample-size must be at least 1")
    report = scan_cases(args.batch_size, args.limit, args.min_count, args.sample_size)
    args.report_json.parent.mkdir(parents=True, exist_ok=True)
    args.report_json.write_text(json.dumps(report, indent=2, ensure_ascii=True), encoding="utf-8")
    print(f"scanned_cases={report['scanned_cases']}")
    print(f"categories={len(report['categories'])}")
    print(f"candidate_organizations={len(report['candidate_organizations'])}")
    print(f"candidate_countries={len(report['candidate_countries'])}")
    print(f"report_json={args.report_json}")


if __name__ == "__main__":
    main()