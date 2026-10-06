"""Score deterministic case-structure labelling against hand-labelled decisions.

Gold: 22 Federal Court decisions from 2001-2004 (data/eval/case_structure/gold_fc_2001_2004_v2.json,
paragraphs from the stored reports) and 14 hand-labelled FC / FCA / SCC decisions from 2008-2024
(gold_new_cases.json). Each case has a 'dev' or 'holdout' split. Only dev cases may be used for tuning;
holdout is scored at declared checkpoints.

Approaches (all offline, no database, network or AI):
  main         the segmentation on main (continuity + boundary rules) with deterministic unit role labels
  structure    paragraph role labelling by cues + ordered skeleton, units from role changes
  structure+h  the same plus a split at each major heading inside the analysis

Run:  python scripts/evaluate_case_structure.py [--per-case] [--splits dev holdout]
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Callable, Sequence

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from backend.contextual_authority import case_structure  # noqa: E402
from scripts.evaluate_discussion_unit_boundaries import BoundaryScore, score_boundaries  # noqa: E402

GOLD_DIR = REPO_ROOT / "data/eval/case_structure"
REPORTS_DIR = REPO_ROOT / "data/eval/llm_discussion_units_pilot/core_300_run/reports"
ROLES = case_structure.ROLES


class Case:
    def __init__(self, key: str, court: str, split: str, paragraphs: list[str], starts: list[int], roles: list[str], report: dict | None = None):
        self.key, self.court, self.split = key, court, split
        self.paragraphs, self.starts, self.roles, self.report = paragraphs, sorted(set(starts) | {0}), roles, report

    def paragraph_roles(self) -> list[str]:
        out: list[str] = []
        bounds = self.starts + [len(self.paragraphs)]
        for role, a, b in zip(self.roles, bounds, bounds[1:]):
            out.extend([role] * (b - a))
        return out


_FOOTER_START = re.compile(r"^\s*(?:SOLICITORS OF RECORD|STYLE OF CAUSE|NAMES OF COUNSEL|DOCKET\b)")


def normalize_footer(starts: list[int], roles: list[str], paragraphs: list[str]) -> tuple[list[int], list[str], list[int]]:
    """Apply the role definition to the 2001-04 labels: a counsel/style-of-cause block is metadata.

    Those labels were mapped from free-text roles and call the closing block 'disposition' in some
    cases and 'metadata' in others. Every paragraph that starts with SOLICITORS OF RECORD, STYLE OF
    CAUSE, NAMES OF COUNSEL or DOCKET after the middle of the case becomes its own metadata unit.
    Returns the new starts, roles and the paragraph indexes that changed.
    """
    n = len(paragraphs)
    para_roles: list[str] = []
    bounds = starts + [n]
    for role, a, b in zip(roles, bounds, bounds[1:]):
        para_roles.extend([role] * (b - a))
    changed = []
    for i in range(n // 2, n):
        if _FOOTER_START.match(paragraphs[i]) and para_roles[i] != "metadata":
            para_roles[i] = "metadata"
            changed.append(i)
    # a footer block runs to the end of the case
    if changed:
        for i in range(changed[0], n):
            if para_roles[i] != "metadata":
                para_roles[i] = "metadata"
                changed.append(i)
    new_starts, new_roles = [0], [para_roles[0]]
    for i in range(1, n):
        if para_roles[i] != para_roles[i - 1] or i in starts and para_roles[i] == para_roles[i - 1] and i in starts:
            new_starts.append(i)
            new_roles.append(para_roles[i])
    return new_starts, new_roles, sorted(set(changed))


def load_cases(gold_dir: Path = GOLD_DIR, reports_dir: Path = REPORTS_DIR) -> list[Case]:
    cases: list[Case] = []
    old = json.loads((gold_dir / "gold_fc_2001_2004_v2.json").read_text())
    hold = set(old["hold_out"])
    for case_id, item in old["cases"].items():
        report = json.loads((reports_dir / f"case_{case_id}_deterministic.json").read_text())
        paragraphs = [p["text"] for p in report["paragraphs"]]
        starts, roles, _ = normalize_footer(sorted(set(item["starts"]) | {0}), list(item["roles"]), paragraphs)
        cases.append(Case(f"FC-old-{case_id}", "FC 2001-04", "holdout" if int(case_id) in hold else "dev", paragraphs, starts, roles, report))
    new = json.loads((gold_dir / "gold_new_cases.json").read_text())["cases"]
    for cite, item in new.items():
        report = None
        if "report_case_id" in item:
            report = json.loads((reports_dir / f"case_{item['report_case_id']}_deterministic.json").read_text())
        cases.append(Case(cite, item["court"] + (" 2008-24" if item["court"] == "FC" else ""), item["split"], item["paragraphs"], item["starts"], item["roles"], report))
    cases.extend(load_rpd_cases(gold_dir))
    return cases


def load_rpd_cases(gold_dir: Path = GOLD_DIR) -> list[Case]:
    """RPD labels are in the repo; the decision text is not. Read it from the extract if present."""
    csv_path = Path(os.environ.get("RPD_SAMPLE_CSV", "/mnt/project-files/rpd-structure-sample.csv"))
    if not csv_path.exists():
        return []
    labels = json.loads((gold_dir / "gold_rpd_labels.json").read_text())["cases"]
    rows: dict[str, list[tuple[int, str]]] = defaultdict(list)
    with csv_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows[row["case_id"]].append((int(row["chunk_index"]), row["text"].replace("\r\n", "\n").replace("\r", "\n")))
    cases: list[Case] = []
    for case_id, item in labels.items():
        paragraphs = [text for _, text in sorted(rows.get(case_id, []))]
        if hashlib.sha256("\f".join(paragraphs).encode()).hexdigest() != item["text_sha256"]:
            continue  # a different extract: do not score labels against other text
        cases.append(Case(f"RPD-{case_id}", "RPD", item["split"], paragraphs, item["starts"], item["roles"]))
    return cases


# --------------------------------------------------------------------------- approaches


def predict_main(case: Case) -> tuple[list[int], list[str]]:
    from backend.contextual_authority import discussion_units as du
    from backend.contextual_authority.unit_roles import label_unit_roles

    reported = {p["paragraph_index"]: p for p in case.report["paragraphs"]} if case.report else {}
    features = []
    for i, text in enumerate(case.paragraphs):
        src = reported.get(i, {})
        features.append(
            du.ParagraphFeatures(
                case_id=0, chunk_id=i, paragraph_index=i, start_offset=0, end_offset=len(text), text=text,
                source_text_hash="", source_paragraph_index=i,
                citation_ids=tuple(src.get("citation_ids", ())), statute_ids=tuple(src.get("statute_ids", ())),
                tag_ids=tuple(src.get("tag_ids", ())), is_heading=src.get("is_heading", False),
            )
        )
    continuity = [du.compute_continuity(a, b) for a, b in zip(features, features[1:])]
    starts = sorted(u.start_paragraph for u in du.segment_discussion_units(features, continuity))
    bounds = starts + [len(case.paragraphs)]
    unit_roles = label_unit_roles([case.paragraphs[a:b] for a, b in zip(bounds, bounds[1:])])
    roles: list[str] = []
    for role, a, b in zip(unit_roles, bounds, bounds[1:]):
        roles.extend([role] * (b - a))
    return starts, roles


def predict_structure(case: Case, split_headings: bool = False, openers: bool = False) -> tuple[list[int], list[str]]:
    roles = case_structure.label_paragraph_roles(case.paragraphs)
    starts = case_structure.structural_unit_starts(case.paragraphs, roles, split_analysis_headings=split_headings, split_issue_openers=openers)
    return starts, roles


def predict_hybrid(case: Case) -> tuple[list[int], list[str]]:
    """Structure units, plus main's boundaries inside the analysis where a discourse cue corroborates them."""
    from backend.contextual_authority import discussion_units as du

    starts, roles = predict_structure(case, True)
    main_starts, _ = predict_main(case)
    extra = [
        s for s in main_starts
        if s not in starts and roles[s] == "analysis" and roles[s - 1] == "analysis" and du._detect_discourse_cue(case.paragraphs[s])
    ]
    return sorted(set(starts) | set(extra)), roles


APPROACHES: dict[str, Callable[[Case], tuple[list[int], list[str]]]] = {
    "main": predict_main,
    "structure": predict_structure,
    "structure+h": lambda case: predict_structure(case, True),
    "structure+h+openers": lambda case: predict_structure(case, True, True),
    "hybrid": predict_hybrid,
}


# --------------------------------------------------------------------------- scoring


def pct(a: int, b: int) -> str:
    return f"{100 * a / b:5.1f}%" if b else "  n/a"


def first_body_index(paragraphs: Sequence[str]) -> int:
    return next((i for i, text in enumerate(paragraphs) if case_structure._strip_number(text)[0] is not None), 1)


def lenient(case: Case, starts: Sequence[int], roles: Sequence[str], gold_starts: Sequence[int], gold_roles: Sequence[str]):
    """Preamble convention: paragraphs before the first numbered paragraph form one block.

    The 2001-04 labels call that block 'overview' and the 2008-24 labels call it 'metadata', so
    boundaries inside it are dropped on both sides and its roles are not compared.
    """
    cut = first_body_index(case.paragraphs)
    keep = lambda values: [v for v in values if v == 0 or v > cut]
    mask = [i >= cut for i in range(len(roles))]
    return keep(gold_starts), keep(starts), [(g, p) for g, p, m in zip(gold_roles, roles, mask) if m]


def evaluate(cases: Sequence[Case], approach: Callable[[Case], tuple[list[int], list[str]]]):
    boundary = BoundaryScore()
    role_hits = role_total = 0
    confusion: dict[tuple[str, str], int] = defaultdict(int)
    per_case = []
    lenient_boundary = BoundaryScore()
    lenient_hits = lenient_total = 0
    for case in cases:
        starts, roles = approach(case)
        score = score_boundaries(case.starts, starts)
        boundary.add(score)
        gold_roles = case.paragraph_roles()
        hits = sum(g == p for g, p in zip(gold_roles, roles))
        role_hits += hits
        role_total += len(gold_roles)
        for g, p in zip(gold_roles, roles):
            confusion[(g, p)] += 1
        gs, ps, pairs = lenient(case, starts, roles, case.starts, gold_roles)
        lenient_boundary.add(score_boundaries(gs, ps))
        lenient_hits += sum(g == p for g, p in pairs)
        lenient_total += len(pairs)
        per_case.append((case.key, score, hits, len(gold_roles)))
    evaluate.lenient = (lenient_boundary, (lenient_hits, lenient_total))  # type: ignore[attr-defined]
    return boundary, (role_hits, role_total), confusion, per_case


def macro_role_accuracy(per_case) -> float:
    """Mean of per-case paragraph role accuracy, so one 240-paragraph decision cannot dominate."""
    return sum(hits / total for _, _, hits, total in per_case) / len(per_case) if per_case else 0.0


def row(label: str, boundary: BoundaryScore, roles: tuple[int, int]) -> str:
    return (
        f"{label:<26} n={boundary.cases:>2}  interior gold {boundary.interior_gold:>3} pred {boundary.interior_predicted:>3}  "
        f"exact {pct(boundary.interior_hits, boundary.interior_gold)}  within-1 {pct(boundary.interior_within_1, boundary.interior_gold)}  "
        f"precision {pct(boundary.interior_hits, boundary.interior_predicted)}  role acc {pct(*roles)}"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--splits", nargs="+", default=["dev"], choices=["dev", "holdout", "holdout2"])
    parser.add_argument("--approach", action="append", choices=list(APPROACHES))
    parser.add_argument("--per-case", action="store_true")
    parser.add_argument("--confusion", action="store_true")
    args = parser.parse_args(argv)
    cases = [c for c in load_cases() if c.split in args.splits]
    for name in args.approach or list(APPROACHES):
        print(f"== {name}  (splits: {', '.join(args.splits)})")
        for label, subset in [("ALL", cases)] + [(court, [c for c in cases if c.court == court]) for court in dict.fromkeys(c.court for c in cases)]:
            if not subset:
                continue
            boundary, roles, confusion, per_case = evaluate(subset, APPROACHES[name])
            print(row(label, boundary, roles) + f"  per-case mean {100 * macro_role_accuracy(per_case):5.1f}%")
            lb, lr = evaluate.lenient  # type: ignore[attr-defined]
            print(" " * 8 + "lenient preamble:" + row("", lb, lr)[26:])
            if label == "ALL" and args.confusion:
                for g in ROLES:
                    print("   gold", f"{g:<12}", " ".join(f"{p[:4]}={confusion.get((g, p), 0):<4}" for p in ROLES))
            if label == "ALL" and args.per_case:
                for key, score, hits, total in per_case:
                    print(f"   {key:<16} exact {score.interior_hits}/{score.interior_gold} pred {score.interior_predicted}  roles {hits}/{total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
