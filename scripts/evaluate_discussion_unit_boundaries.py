#!/usr/bin/env python3
"""Score discussion-unit boundaries against hand-read gold labels.

One evaluator for every version of ``backend/contextual_authority/discussion_units.py``.
Everything runs offline from the stored deterministic case reports
(``data/eval/llm_discussion_units_pilot/core_300_run/reports``); no database,
network or model calls.

Counting is per boundary (a boundary is a unit start paragraph index):

* hits      = gold starts that the algorithm also predicts (exact)
* missed    = gold starts not predicted
* spurious  = predicted starts not in gold
* within-1  = gold starts matched one-to-one to a predicted start at most one
              paragraph away (exact matches are paired first, so one predicted
              start can never satisfy two gold starts)

Paragraph 0 is a boundary in every gold label and every prediction, so the
"interior" columns repeat the counts without it.

Usage:
    python scripts/evaluate_discussion_unit_boundaries.py                  # working tree
    python scripts/evaluate_discussion_unit_boundaries.py --rev main --rev ded7069
    python scripts/evaluate_discussion_unit_boundaries.py --stored         # units saved in the reports
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

REPORTS_DIR = REPO_ROOT / "data/eval/llm_discussion_units_pilot/core_300_run/reports"
MODULE_PATH = "backend/contextual_authority/discussion_units.py"
DEFAULT_GOLD_DIR = Path("/mnt/project-files/discussion-units")

HOLD_OUT = (126, 2517, 4006, 15005)
PRIOR_VERIFIED = (62, 126, 677, 1439, 1748, 1978, 2220, 2517, 2660, 2788, 4006, 4090, 15005, 17038, 23057, 24261)
NEW_VERIFIED = (8343, 12123, 13414, 13410, 3646, 32257)
# Labelled from algorithm output; kept only to reproduce the earlier 18-case figure.
LEGACY_ALGORITHM_DERIVED = (14508, 26844)


# --------------------------------------------------------------------------- counting


@dataclass
class BoundaryScore:
    gold: int = 0
    predicted: int = 0
    hits: int = 0
    within_1: int = 0
    interior_gold: int = 0
    interior_predicted: int = 0
    interior_hits: int = 0
    interior_within_1: int = 0
    cases: int = 0
    exact_cases: int = 0

    @property
    def missed(self) -> int:
        return self.gold - self.hits

    @property
    def spurious(self) -> int:
        return self.predicted - self.hits

    def add(self, other: "BoundaryScore") -> None:
        for name in self.__dataclass_fields__:
            setattr(self, name, getattr(self, name) + getattr(other, name))


def _within_one_matches(gold: set[int], predicted: set[int]) -> int:
    """One-to-one matches with distance <= 1, exact pairs taken first."""
    matched = gold & predicted
    free_pred = sorted(predicted - matched)
    count = len(matched)
    for g in sorted(gold - matched):
        for p in (g - 1, g + 1):
            if p in free_pred:
                free_pred.remove(p)
                count += 1
                break
    return count


def score_boundaries(gold: Iterable[int], predicted: Iterable[int]) -> BoundaryScore:
    gold_set, pred_set = set(gold), set(predicted)
    interior_gold, interior_pred = gold_set - {0}, pred_set - {0}
    return BoundaryScore(
        gold=len(gold_set),
        predicted=len(pred_set),
        hits=len(gold_set & pred_set),
        within_1=_within_one_matches(gold_set, pred_set),
        interior_gold=len(interior_gold),
        interior_predicted=len(interior_pred),
        interior_hits=len(interior_gold & interior_pred),
        interior_within_1=_within_one_matches(interior_gold, interior_pred),
        cases=1,
        exact_cases=int(gold_set == pred_set),
    )


def pct(numerator: int, denominator: int) -> str:
    return f"{100 * numerator / denominator:.1f}%" if denominator else "n/a"


# --------------------------------------------------------------------------- gold


def load_gold(gold_dir: Path) -> dict[int, list[int]]:
    """Gold unit starts per case: 16 prior verified, 6 new verified, 2 legacy."""
    verified = json.loads((gold_dir / "gold_set_labels_verified.json").read_text())["gold_labels"]
    expanded = json.loads((gold_dir / "gold_set_labels_verified_22cases.json").read_text())["merged_gold_labels"]
    legacy = json.loads((gold_dir / "gold_set_labels.json").read_text())["gold_labels"]
    gold: dict[int, list[int]] = {}
    for case_id in PRIOR_VERIFIED:
        gold[case_id] = sorted({u["start"] for u in verified[str(case_id)]["gold_unit_boundaries"]} | {0})
    for case_id in NEW_VERIFIED:
        gold[case_id] = sorted(set(expanded[f"new_cases_{case_id}"]["gold_unit_boundaries"]) | {0})
    for case_id in LEGACY_ALGORITHM_DERIVED:
        gold[case_id] = sorted({u["start"] for u in legacy[str(case_id)]["gold_unit_boundaries"]} | {0})
    return gold


# --------------------------------------------------------------------------- predictions


def load_report(case_id: int) -> dict:
    return json.loads((REPORTS_DIR / f"case_{case_id}_deterministic.json").read_text())


def stored_starts(case_id: int) -> list[int]:
    return sorted(u["start_paragraph"] for u in load_report(case_id)["discussion_units"])


def load_module(rev: str | None):
    """Import discussion_units.py from the working tree (rev=None) or a git revision."""
    if rev is None:
        from backend.contextual_authority import discussion_units

        return discussion_units
    source = subprocess.run(
        ["git", "show", f"{rev}:{MODULE_PATH}"], cwd=REPO_ROOT, check=True, capture_output=True, text=True
    ).stdout
    import backend.contextual_authority  # noqa: F401  (parent package for the relative import)

    safe = "".join(ch if ch.isalnum() else "_" for ch in rev)
    name = f"backend.contextual_authority._eval_{safe}"
    spec = importlib.util.spec_from_loader(name, loader=None)
    module = importlib.util.module_from_spec(spec)
    module.__package__ = "backend.contextual_authority"
    sys.modules[name] = module  # dataclasses look the module up by name
    exec(compile(source, f"{rev}:{MODULE_PATH}", "exec"), module.__dict__)
    return module


def predictor_for(module, **segment_kwargs) -> Callable[[int], list[int]]:
    """Recompute continuity with this version's own code, then segment."""

    def predict(case_id: int) -> list[int]:
        report = load_report(case_id)
        paragraphs = [
            module.ParagraphFeatures(
                case_id=case_id,
                chunk_id=p["chunk_id"],
                paragraph_index=p["paragraph_index"],
                start_offset=p["start_offset"],
                end_offset=p["end_offset"],
                text=p["text"],
                source_text_hash=p.get("source_text_sha256", ""),
                source_paragraph_index=p.get("source_paragraph_index", -1),
                citation_ids=tuple(p.get("citation_ids", ())),
                statute_ids=tuple(p.get("statute_ids", ())),
                tag_ids=tuple(p.get("tag_ids", ())),
                is_heading=p.get("is_heading", False),
            )
            for p in report["paragraphs"]
        ]
        continuity = [module.compute_continuity(a, b) for a, b in zip(paragraphs, paragraphs[1:])]
        units = module.segment_discussion_units(paragraphs, continuity, **segment_kwargs)
        return sorted(u.start_paragraph for u in units)

    return predict


# --------------------------------------------------------------------------- report


@dataclass
class SetResult:
    label: str
    total: BoundaryScore = field(default_factory=BoundaryScore)
    per_case: dict[int, tuple[list[int], list[int], BoundaryScore]] = field(default_factory=dict)


def evaluate(label: str, case_ids: Sequence[int], gold: dict[int, list[int]], predict) -> SetResult:
    result = SetResult(label)
    for case_id in case_ids:
        predicted = predict(case_id)
        score = score_boundaries(gold[case_id], predicted)
        result.per_case[case_id] = (gold[case_id], predicted, score)
        result.total.add(score)
    return result


def format_row(version: str, result: SetResult) -> str:
    t = result.total
    return (
        f"| {version} | {result.label} | {t.cases} | {t.gold} | {t.predicted} | {t.hits} | {t.missed} | {t.spurious} "
        f"| {pct(t.hits, t.gold)} | {pct(t.within_1, t.gold)} | {pct(t.hits, t.predicted)} "
        f"| {pct(t.interior_hits, t.interior_gold)} | {pct(t.interior_within_1, t.interior_gold)} "
        f"| {pct(t.interior_hits, t.interior_predicted)} |"
    )


HEADER = (
    "| Version | Set | Cases | Gold | Predicted | Hits | Missed | Spurious | Exact recall | Within-1 recall "
    "| Precision | Interior exact | Interior within-1 | Interior precision |\n"
    "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"
)

SETS = {
    "tuning (18)": tuple(c for c in PRIOR_VERIFIED + NEW_VERIFIED if c not in HOLD_OUT),
    "hold-out (4)": HOLD_OUT,
    "all verified (22)": PRIOR_VERIFIED + NEW_VERIFIED,
}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--gold-dir", type=Path, default=DEFAULT_GOLD_DIR)
    parser.add_argument("--rev", action="append", default=[], help="git revision of discussion_units.py (repeatable)")
    parser.add_argument("--stored", action="store_true", help="score the units saved in the stored reports")
    parser.add_argument("--kwarg", action="append", default=[], help="segment kwarg as name=json, e.g. require_corroboration_for_signal_vacuum=true")
    parser.add_argument("--per-case", action="store_true")
    parser.add_argument("--json", type=Path, help="write per-case results here")
    args = parser.parse_args(argv)

    gold = load_gold(args.gold_dir)
    kwargs = {k: json.loads(v) for k, v in (item.split("=", 1) for item in args.kwarg)}
    versions: list[tuple[str, Callable[[int], list[int]]]] = []
    if args.stored:
        versions.append(("stored reports", stored_starts))
    for rev in args.rev:
        versions.append((rev, predictor_for(load_module(rev), **kwargs)))
    if not versions:
        versions.append(("working tree", predictor_for(load_module(None), **kwargs)))

    print(HEADER)
    dump = {}
    for name, predict in versions:
        for set_label, case_ids in SETS.items():
            result = evaluate(set_label, case_ids, gold, predict)
            print(format_row(name, result))
            dump.setdefault(name, {})[set_label] = {
                str(c): {"gold": g, "predicted": p, "hits": s.hits, "within_1": s.within_1}
                for c, (g, p, s) in result.per_case.items()
            }
            if args.per_case:
                for c, (g, p, s) in result.per_case.items():
                    print(f"    {c}: hits {s.hits}/{s.gold}, spurious {s.spurious}, gold {g}, predicted {p}")
    if args.json:
        args.json.write_text(json.dumps(dump, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
