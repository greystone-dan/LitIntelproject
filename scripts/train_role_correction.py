"""Train the court-specific role correction used by backend/contextual_authority/role_correction.py.

Input is a jsonl.gz of labelled decisions, one per line:
``{"source", "court", "id", "text", "labels": {printed paragraph number: role letter}}`` (role letters M O F I A D).
``--train`` picks the sources to fit on and ``--eval`` the sources to report on (labeller alone vs corrected, per court,
strict and within one paragraph). ``--cv K`` also reports K-fold cross-validation by decision over the training sources.
Needs scikit-learn and scipy (training only; the site runs numpy only).

Run:  python scripts/train_role_correction.py DATASET --train readers_w1 readers_w2 readers_w3 hand_dev --eval hand_fresh [--cv 5] [--write]
"""

from __future__ import annotations

import argparse
import collections
import gzip
import json
import os
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

os.environ["ILIT_LEARNED_ROLES"] = "1"
os.environ["ILIT_OUTLINE_V2"] = "1"
os.environ["ILIT_OUTLINE_HEADINGS"] = "1"
os.environ.pop("ILIT_ROLE_CORRECTION", None)

from backend.contextual_authority import case_structure as cs  # noqa: E402
from backend.contextual_authority import learned_roles  # noqa: E402
from backend.contextual_authority import opinions  # noqa: E402
from backend.contextual_authority import outline_v2 as ov  # noqa: E402
from backend.contextual_authority import role_correction as rc  # noqa: E402
from backend.live_decision import decision_format_blocks  # noqa: E402

LETTER_ROLE = {"M": "metadata", "O": "overview", "F": "facts", "I": "issues", "A": "analysis", "D": "disposition"}
SECTION = {"metadata": "B", "overview": "B", "facts": "B", "issues": "I", "analysis": "A", "disposition": "D"}


def decision_rows(record: dict) -> dict:
    """Features, the labeller's roles and the labels for the numbered paragraphs of one decision."""
    text = record["text"]
    units, _ = ov._prepared_units(text, decision_format_blocks(text))
    units = ov._drop_notes(text, units)
    roles, log_p = learned_roles.label_paragraph_roles_scored([u["text"] for u in units])
    try:
        starts = [o.first_unit for o in opinions.find_opinions(text, units)]
    except Exception:  # noqa: BLE001
        starts = []
    numbered, features = rc.feature_terms(record["court"], units, roles, log_p, rc.holders_by_number(text), starts)
    labels = []
    for i in numbered:
        letter = record["labels"].get(str(cs._strip_number(units[i]["text"])[0]))
        labels.append(LETTER_ROLE.get(letter) if letter else None)
    return {"id": record["id"], "court": record["court"], "features": features, "base": [roles[i] for i in numbered], "labels": labels}


def to_matrix(rows):
    from scipy.sparse import csr_matrix

    r, c, v = [], [], []
    for n, feats in enumerate(rows):
        for k, val in feats.items():
            r.append(n), c.append(k), v.append(val)
    return csr_matrix((v, (r, c)), shape=(len(rows), rc.HASH_BUCKETS))


def fit(decisions, c):
    from sklearn.linear_model import LogisticRegression

    feats = [f for d in decisions for f, lab in zip(d["features"], d["labels"]) if lab]
    y = np.array([cs.ROLES.index(lab) for d in decisions for lab in d["labels"] if lab])
    model = LogisticRegression(C=c, max_iter=2000).fit(to_matrix(feats), y)
    coef = np.zeros((len(cs.ROLES), rc.HASH_BUCKETS))
    coef[model.classes_] = model.coef_
    bias = np.full(len(cs.ROLES), -9.0)
    bias[model.classes_] = model.intercept_
    counts = np.full((len(cs.ROLES), len(cs.ROLES)), 0.5)
    for d in decisions:
        seq = [lab for lab in d["labels"]]
        for a, b in zip(seq, seq[1:]):
            if a and b:
                counts[cs.ROLES.index(a), cs.ROLES.index(b)] += 1
    return coef.astype(np.float32), bias.astype(np.float32), np.log(counts / counts.sum(axis=1, keepdims=True))


def predict(d, coef, bias, transitions):
    scores = rc.log_probabilities(d["features"], coef, bias)
    return [cs.ROLES[k] for k in rc.decode(scores, transitions)]


def near(truth, predicted, mapper=lambda x: x):
    """Right if the prediction matches the label of the paragraph or of the one just before or after it."""
    t = [mapper(x) if x else None for x in truth]
    p = [mapper(x) for x in predicted]
    hits = total = 0
    for j, label in enumerate(t):
        if label is None:
            continue
        total += 1
        hits += p[j] in {t[k] for k in (j - 1, j, j + 1) if 0 <= k < len(t) and t[k] is not None}
    return hits, total


def report(title, decisions, predictions):
    print(title)
    for court in rc.FORUMS:
        stats = np.zeros(8)
        used = 0
        for d, pred in zip(decisions, predictions):
            if d["court"] != court:
                continue
            used += 1
            labelled = [(b, p, t) for b, p, t in zip(d["base"], pred, d["labels"]) if t]
            stats[0] += len(labelled)
            stats[1] += sum(b == t for b, p, t in labelled)
            stats[2] += sum(p == t for b, p, t in labelled)
            stats[3] += sum(SECTION[b] == SECTION[t] for b, p, t in labelled)
            stats[4] += sum(SECTION[p] == SECTION[t] for b, p, t in labelled)
            stats[5] += near(d["labels"], d["base"])[0]
            stats[6] += near(d["labels"], pred)[0]
            stats[7] += near(d["labels"], pred, SECTION.get)[0]
        if stats[0]:
            n = stats[0]
            print(
                f"  {court}: {used} decisions, {int(n)} paragraphs | role strict {stats[1]/n:.3f} -> {stats[2]/n:.3f}"
                f" | within 1 paragraph {stats[5]/n:.3f} -> {stats[6]/n:.3f} | 4-section strict {stats[3]/n:.3f} -> {stats[4]/n:.3f}"
                f" | 4-section within 1 {stats[7]/n:.3f}"
            )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset", type=Path)
    parser.add_argument("--train", nargs="+", required=True)
    parser.add_argument("--eval", nargs="*", default=[])
    parser.add_argument("--c", type=float, default=0.5)
    parser.add_argument("--cv", type=int, default=0)
    parser.add_argument("--write", action="store_true", help="write role_correction_weights.npz")
    args = parser.parse_args(argv)
    by_source = collections.defaultdict(list)
    with gzip.open(args.dataset, "rt") as handle:
        for line in handle:
            record = json.loads(line)
            by_source[record["source"]].append(decision_rows(record))
    train = [d for s in args.train for d in by_source[s]]
    if args.cv:
        folds = [[d for j, d in enumerate(train) if j % args.cv == k] for k in range(args.cv)]
        predictions = []
        ordered = []
        for k in range(args.cv):
            coef, bias, transitions = fit([d for j, f in enumerate(folds) if j != k for d in f], args.c)
            for d in folds[k]:
                ordered.append(d)
                predictions.append(predict(d, coef, bias, transitions))
        report(f"{args.cv}-fold cross-validation over {len(train)} training decisions:", ordered, predictions)
    coef, bias, transitions = fit(train, args.c)
    print(f"trained on {len(train)} decisions")
    for source in args.eval:
        report(f"held out: {source}", by_source[source], [predict(d, coef, bias, transitions) for d in by_source[source]])
    if args.write:
        np.savez_compressed(rc.WEIGHTS_PATH, coef=coef.astype(np.float16), bias=bias, transitions=transitions.astype(np.float32))
        print(f"wrote {rc.WEIGHTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
