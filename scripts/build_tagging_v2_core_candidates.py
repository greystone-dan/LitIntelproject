"""Build a conservative Tagging V2 core candidate file from the brainstorming draft."""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path


HEADINGS = {
    "Refugees": "refugee",
    "Security": "security",
    "Human Rights and Complicity": "human_rights",
    "Criminality and organized crime": "criminality",
    "misrep and identity": "misrepresentation_identity",
    "evidence and credibility": "evidence_credibility",
    "Procedural Fairness": "procedural_fairness",
    "Risk and Country Conditions": "risk_country_conditions",
    "Detention": "detention",
    "Removal and Enforcement": "removal_enforcement",
    "Humanitarian and Family Considerations": "humanitarian_family",
    "Citizenship": "citizenship",
    "Immigration Status and Applications": "immigration_status",
    "Constitutional and International Law": "constitutional_international",
    "CBSA and IRCC Processes": "agency_process",
    "Territories and Countries": "country",
    "Groups/Orgs": "organization",
}

GENERIC = {
    "account", "application", "applicant", "applications", "assessment", "claim", "claimant",
    "claims", "conditions", "concern", "concerns", "country", "decision", "evidence", "facts",
    "fear", "finding", "findings", "information", "issue", "issues", "law", "member", "members",
    "national", "need", "person", "persons", "process", "protection", "record", "review", "risk",
    "security", "status", "support", "terms", "treatment", "violence", "victim", "victims",
    "immigration", "legal", "nationality", "residence", "application", "applications", "canada",
}
CONNECTORS = {"a", "an", "and", "for", "from", "in", "of", "on", "or", "the", "to", "under", "with"}
CORE_SINGLE_WORDS = {
    "asylum", "biometrics", "citizenship", "criminality", "deportation", "detention", "espionage",
    "inadmissibility", "interpreter", "mandamus", "misrepresentation", "persecution", "refoulement",
    "rehabilitation", "removal", "sponsorship", "statelessness", "terrorism", "torture", "trafficking",
    "transgender", "refugee", "genocide", "extortion", "kidnapping", "discrimination", "naturalization",
    "overstay", "repatriation", "reunification", "cessation", "vacation", "reavailment", "complicity",
    "corroboration", "credibility", "disclosure", "accommodation", "interpreter", "translation",
}
CORE_PHRASES = {
    "asylum seeker", "convention refugee", "family reunification", "humanitarian and compassionate",
    "internal flight alternative", "judicial review", "permanent resident", "procedural fairness",
    "refugee claim", "refugee protection", "state protection", "stay of removal", "work permit",
}
ENTITY_GROUPS = {
    "ipob": {"ipob", "indigenous people of biafra"},
    "massob": {"massob", "movement for the actualization of the sovereign state of biafra"},
    "esn": {"esn", "eastern security network"},
    "boko_haram": {"boko haram"},
    "islamic_state": {"isis", "isil", "daesh", "islamic state"},
    "al_shabaab": {"al shabaab", "al-shabaab"},
    "al_qaeda": {"al qaeda", "al-qaida"},
    "taliban": {"taliban", "afghan taliban"},
    "hezbollah": {"hezbollah", "hizballah"},
    "pkk": {"pkk", "kurdistan workers party"},
    "ltte": {"ltte", "tamil tigers", "liberation tigers of tamil eelam"},
    "farc": {"farc", "revolutionary armed forces of colombia"},
    "hamas": {"hamas"},
}
DROP_PREFIXES = (
    "application for ", "claim for ", "failure to ", "lack of ", "right to ", "risk of ",
    "request for ", "response to ", "the ", "under the ",
)


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.replace("’", "'").strip(" .;:"))


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def dedupe_key(value: str) -> str:
    value = value.casefold().replace("’", "'").replace("-", " ")
    value = re.sub(r"[^a-z0-9 ]", "", value)
    return re.sub(r"\s+", " ", value).strip()


def entity_group_key(term: str, category: str) -> str:
    key = dedupe_key(term)
    if category != "organization":
        return key
    for canonical, aliases in ENTITY_GROUPS.items():
        if key in {dedupe_key(alias) for alias in aliases}:
            return f"entity:{canonical}"
    return key


def is_acronym(term: str) -> bool:
    return bool(re.fullmatch(r"[A-Z][A-Z0-9&-]{1,9}", term))


def keep_term(term: str, category: str) -> bool:
    words = term.split()
    lowered = term.lower()
    if not term or len(term) < 2 or (category != "organization" and len(term) > 55):
        return False
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 &'’()/-]*", term):
        return False
    if category not in {"country", "organization"} and not is_acronym(term):
        if len(words) > 2 or set(words) & CONNECTORS:
            return False
        if len(words) == 1 and lowered not in CORE_SINGLE_WORDS:
            return False
        if len(words) == 2 and lowered not in CORE_PHRASES:
            return False
        if lowered in GENERIC or any(lowered.startswith(prefix) for prefix in DROP_PREFIXES):
            return False
        if len(words) == 1 and len(lowered) < 7:
            return False
    if category == "organization" and len(words) == 1 and not is_acronym(term) and len(term) < 5:
        return False
    return True


def parse_draft(path: Path) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = defaultdict(list)
    category = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line in HEADINGS:
            category = HEADINGS[line]
            continue
        if category:
            sections[category].extend(normalize(item) for item in line.split(","))
    return sections


def build_candidates(sections: dict[str, list[str]]) -> dict[str, dict[str, list[str]]]:
    result: dict[str, dict[str, list[str]]] = {}
    used_terms: set[str] = set()
    for category, terms in sections.items():
        by_key: dict[str, list[str]] = defaultdict(list)
        for term in terms:
            key = entity_group_key(term, category)
            if not keep_term(term, category):
                continue
            if key in by_key:
                by_key[key].append(term)
                continue
            if key in used_terms:
                continue
            used_terms.add(key)
            by_key[key].append(term)
        result[category] = {}
        for aliases in by_key.values():
            canonical_term = sorted(aliases, key=lambda value: (not is_acronym(value), len(value), value.casefold()))[0]
            canonical_key = next(
                (canonical for canonical, group_aliases in ENTITY_GROUPS.items() if category == "organization" and dedupe_key(canonical_term) in {dedupe_key(alias) for alias in group_aliases}),
                slug(canonical_term),
            )
            result[category][canonical_key] = sorted(set(aliases), key=lambda value: (value.casefold() != canonical_term.casefold(), value.casefold()))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("docs/TAGGING_V2_CORE_WHITELIST_DRAFT.md"))
    parser.add_argument("--output", type=Path, default=Path("data/eval/reports/tagging-v2-core-candidates.json"))
    args = parser.parse_args()
    categories = build_candidates(parse_draft(args.input))
    payload = {
        "taxonomy_version": "ca_legal_v2_core_candidates",
        "source": str(args.input),
        "description": "Conservative automated cleanup of the brainstorming draft; review before promotion to the core whitelist.",
        "categories": categories,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=True), encoding="utf-8")
    markdown = [
        "# Tagging V2 Core Candidates",
        "",
        "Automated cleanup of the brainstorming draft. This is a review file, not the authoritative whitelist.",
        "",
    ]
    for category, values in categories.items():
        markdown.extend([f"## {category}", ""])
        for canonical, aliases in values.items():
            markdown.append(f"- **{canonical}**" + (f": {', '.join(aliases)}" if aliases else ""))
        markdown.append("")
    args.output.with_suffix(".md").write_text("\n".join(markdown), encoding="utf-8")
    print(f"categories={len(categories)}")
    print(f"canonical_terms={sum(len(values) for values in categories.values())}")
    for category, values in categories.items():
        print(f"{category}={len(values)}")
    print(f"output={args.output}")


if __name__ == "__main__":
    main()