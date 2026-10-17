"""Train the court-specific role correction used by backend/contextual_authority/role_correction.py.

Input is a jsonl.gz of labelled decisions, one per line: ``{"source", "court", "id", "text", "labels": {paragraph number: role letter}}``
(role letters M O F I A D). ``--train`` picks the sources to fit on, ``--eval`` the sources to report on (base labeller
vs corrected, per court). Needs scikit-learn and scipy (training only; the site runs numpy only).

Run:  python scripts/train_role_correction.py DATASET --train readers_w1 readers_w2 --eval hand_fresh [--write]
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
os.environ.pop("ILIT_ROLE_CORRECTION", None)

from backend.contextual_authority import case_structure as cs  # noqa: E402
from backend.contextual_authority import outline_v2 as ov  # noqa: E402
from backend.contextual_authority import role_correction as rc  # noqa: E402
from backend.live_decision import decision_format_blocks  # noqa: E402

LETTER_ROLE = {"M": "metadata", "O": "overview", "F": "facts", "I": "issues", "A": "analysis", "D": "disposition"}


def decision_rows(record: dict):
    """(features, base role, label or None, court) for each numbered paragraph of a decision."""
    text = record["text"]
    units = ov._units(text, decision_format_blocks(text))
    texts = [u["text"] for u in units]
    roles = cs.label_paragraph_roles(texts)
    numbered = [i for i, t in enumerate(texts) if cs._strip_number(t)[0] is not None]
    features = rc.feature_terms(record["court"], texts, roles, numbered, rc.holders_by_number(text))
    out = []
    for i, feats in zip(numbered, features):
        letter = record["labels"].get(str(cs._strip_number(texts[i])[0]))
        out.append((feats, roles[i], LETTER_ROLE.get(letter) if letter else None, record["court"]))
    return out


def to_matrix(rows):
    from scipy.sparse import csr_matrix

    r, c, v = [], [], []
    for n, (feats, *_rest) in enumerate(rows):
        for k, val in feats.items():
            r.append(n), c.append(k), v.append(val)
    return csr_matrix((v, (r, c)), shape=(len(rows), rc.HASH_BUCKETS))


def main(argv=None) -> int:
    from sklearn.linear_model import LogisticRegression

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset", type=Path)
    parser.add_argument("--train", nargs="+", required=True)
    parser.add_argument("--eval", nargs="*", default=[])
    parser.add_argument("--c", type=float, default=0.3)
    parser.add_argument("--write", action="store_true", help="write role_correction_weights.npz")
    args = parser.parse_args(argv)
    by_source = collections.defaultdict(list)
    with gzip.open(args.dataset, "rt") as handle:
        for line in handle:
            record = json.loads(line)
            by_source[record["source"]].append(record)
    train = [row for s in args.train for rec in by_source[s] for row in decision_rows(rec) if row[2]]
    x, y = to_matrix(train), np.array([cs.ROLES.index(r[2]) for r in train])
    model = LogisticRegression(C=args.c, max_iter=3000).fit(x, y)
    print(f"trained on {len(y)} paragraphs from {sum(len(by_source[s]) for s in args.train)} decisions")
    coef = np.zeros((len(cs.ROLES), rc.HASH_BUCKETS))
    coef[model.classes_] = model.coef_
    bias = np.full(len(cs.ROLES), -9.0)
    bias[model.classes_] = model.intercept_
    for source in args.eval:
        rows = [row for rec in by_source[source] for row in decision_rows(rec) if row[2]]
        scores = to_matrix(rows) @ coef.T + bias
        predicted = [cs.ROLES[int(k)] for k in scores.argmax(axis=1)]
        for court in rc.FORUMS:
            idx = [n for n, r in enumerate(rows) if r[3] == court]
            if idx:
                base = sum(rows[n][1] == rows[n][2] for n in idx) / len(idx)
                fixed = sum(predicted[n] == rows[n][2] for n in idx) / len(idx)
                docs = len({rec["id"] for rec in by_source[source] if rec["court"] == court})
                print(f"{source} {court}: {len(idx)} paragraphs, {docs} decisions: base {base:.3f} corrected {fixed:.3f}")
    if args.write:
        np.savez_compressed(rc.WEIGHTS_PATH, coef=coef.astype(np.float16), bias=bias.astype(np.float32))
        print(f"wrote {rc.WEIGHTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
