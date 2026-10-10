"""Train the learned paragraph-role weights used by backend/contextual_authority/learned_roles.py.

Training data: the Haiku draft labels in data/eval/case_structure/haiku_drafts_v1.json (decision text from the
core_300_run reports). The hand-labelled decisions are NOT used, so evaluate_case_structure.py scores them as a
clean hold-out. Needs scikit-learn (training only; the site runs numpy only).

Run:  python scripts/train_learned_roles.py [--c 1.0]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from backend.contextual_authority import case_structure as cs  # noqa: E402
from backend.contextual_authority import learned_roles as lr  # noqa: E402

DRAFTS = REPO_ROOT / "data/eval/case_structure/haiku_drafts_v1.json"
REPORTS = REPO_ROOT / "data/eval/llm_discussion_units_pilot/core_300_run/reports"


def roles_from_runs(runs: list, count: int) -> list[str]:
    out = ["metadata"] * count
    runs = sorted(runs)
    for (start, role), nxt in zip(runs, runs[1:] + [[count, None]]):
        for i in range(start, min(nxt[0], count)):
            out[i] = role
    return out


def main(argv=None) -> int:
    from scipy.sparse import csr_matrix, hstack, vstack
    from sklearn.linear_model import LogisticRegression

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--c", type=float, default=1.0)
    args = parser.parse_args(argv)
    drafts = json.loads(DRAFTS.read_text())["cases"]
    blocks, labels = [], []
    for case_id, item in drafts.items():
        paragraphs = [p["text"] for p in json.loads((REPORTS / f"case_{case_id}_deterministic.json").read_text())["paragraphs"]]
        roles = roles_from_runs(item["runs"], len(paragraphs))
        texts, dense = lr.feature_matrix(paragraphs, cs._emissions(paragraphs))
        rows, cols, vals = [], [], []
        for i, feats in enumerate(texts):
            for k, v in feats.items():
                rows.append(i), cols.append(k), vals.append(v)
        sparse = csr_matrix((vals, (rows, cols)), shape=(len(paragraphs), lr.HASH_BUCKETS))
        blocks.append(hstack([sparse, csr_matrix(dense)]).tocsr())
        labels.extend(cs.ROLES.index(r) for r in roles)
    model = LogisticRegression(C=args.c, max_iter=3000).fit(vstack(blocks), np.array(labels))
    coef = np.zeros((len(cs.ROLES), lr.HASH_BUCKETS + blocks[0].shape[1] - lr.HASH_BUCKETS))
    coef[model.classes_] = model.coef_
    bias = np.full(len(cs.ROLES), -9.0)
    bias[model.classes_] = model.intercept_
    np.savez_compressed(
        lr.WEIGHTS_PATH,
        sparse=coef[:, : lr.HASH_BUCKETS].astype(np.float16),
        dense=coef[:, lr.HASH_BUCKETS :].astype(np.float16),
        bias=bias.astype(np.float32),
    )
    print(f"trained on {len(labels)} paragraphs from {len(drafts)} decisions; wrote {lr.WEIGHTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
