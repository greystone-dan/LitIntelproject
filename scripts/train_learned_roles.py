"""Train the learned paragraph-role weights used by backend/contextual_authority/learned_roles.py.

Training data (Haiku labels, never the hand-labelled decisions, so evaluate_case_structure.py scores those as a
clean hold-out):
  - data/eval/case_structure/haiku_drafts_v1.json (text from the core_300_run reports)
  - data/eval/case_structure/haiku_labels_export_v1.json, "train" split only (text from --export-dir, a folder of
    case_<id>.json files with a "paragraphs" list). Without --export-dir only the drafts are used.
Stage 1 is a word + position model; stage 2 is trained on stage-1 log-probabilities from 5-fold (by decision)
cross-fitting. Needs scikit-learn (training only; the site runs numpy only).

Run:  python scripts/train_learned_roles.py [--export-dir PATH] [--c 1.0]
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
EXPORT_LABELS = REPO_ROOT / "data/eval/case_structure/haiku_labels_export_v1.json"
REPORTS = REPO_ROOT / "data/eval/llm_discussion_units_pilot/core_300_run/reports"


def roles_from_runs(runs: list, count: int) -> list[str]:
    out = ["metadata"] * count
    runs = sorted(runs)
    for (start, role), nxt in zip(runs, runs[1:] + [[count, None]]):
        for i in range(start, min(nxt[0], count)):
            out[i] = role
    return out


def case_matrix(paragraphs):
    from scipy.sparse import csr_matrix, hstack

    emissions = cs._emissions(paragraphs)
    texts, dense = lr.feature_matrix(paragraphs, emissions)
    rows, cols, vals = [], [], []
    for i, feats in enumerate(texts):
        for k, v in feats.items():
            rows.append(i), cols.append(k), vals.append(v)
    sparse = csr_matrix((vals, (rows, cols)), shape=(len(paragraphs), lr.HASH_BUCKETS))
    return hstack([sparse, csr_matrix(dense)]).tocsr(), emissions


def full_log_p(model, x):
    out = np.full((x.shape[0], len(cs.ROLES)), np.log(1e-4))
    out[:, model.classes_] = np.log(np.clip(model.predict_proba(x), 1e-4, 1))
    return out


def main(argv=None) -> int:
    from scipy.sparse import vstack
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--c", type=float, default=1.0)
    parser.add_argument("--export-dir", type=Path)
    args = parser.parse_args(argv)
    cases = []  # (matrix, emissions, label indices)
    drafts = json.loads(DRAFTS.read_text())["cases"]
    for case_id, item in drafts.items():
        paragraphs = [p["text"] for p in json.loads((REPORTS / f"case_{case_id}_deterministic.json").read_text())["paragraphs"]]
        roles = roles_from_runs(item["runs"], len(paragraphs))
        matrix, emissions = case_matrix(paragraphs)
        cases.append((matrix, emissions, np.array([cs.ROLES.index(r) for r in roles])))
    if args.export_dir:
        labels = json.loads(EXPORT_LABELS.read_text())
        for case_id in labels["split"]["train"]:
            paragraphs = [p["text"] for p in json.loads((args.export_dir / f"case_{case_id}.json").read_text())["paragraphs"]]
            roles = roles_from_runs(labels["cases"][case_id], len(paragraphs))
            matrix, emissions = case_matrix(paragraphs)
            cases.append((matrix, emissions, np.array([cs.ROLES.index(r) for r in roles])))

    def fit(subset):
        return LogisticRegression(C=args.c, max_iter=3000).fit(vstack([c[0] for c in subset]), np.concatenate([c[2] for c in subset]))

    folds = 5
    stage2_x, stage2_y = [], []
    for fold in range(folds):
        model = fit([c for i, c in enumerate(cases) if i % folds != fold])
        for i in range(fold, len(cases), folds):
            stage2_x.append(lr.stack_features(full_log_p(model, cases[i][0]), cases[i][1]))
            stage2_y.append(cases[i][2])
    x2, y2 = np.vstack(stage2_x), np.concatenate(stage2_y)
    scaler = StandardScaler().fit(x2)
    model2 = LogisticRegression(C=1.0, max_iter=3000).fit(scaler.transform(x2), y2)

    model = fit(cases)
    width = cases[0][0].shape[1]
    coef = np.zeros((len(cs.ROLES), width))
    coef[model.classes_] = model.coef_
    bias = np.full(len(cs.ROLES), -9.0)
    bias[model.classes_] = model.intercept_
    s2_coef = np.zeros((len(cs.ROLES), x2.shape[1]))
    s2_coef[model2.classes_] = model2.coef_
    s2_bias = np.full(len(cs.ROLES), -9.0)
    s2_bias[model2.classes_] = model2.intercept_
    np.savez_compressed(
        lr.WEIGHTS_PATH,
        sparse=coef[:, : lr.HASH_BUCKETS].astype(np.float16),
        dense=coef[:, lr.HASH_BUCKETS :].astype(np.float16),
        bias=bias.astype(np.float32),
        s2_coef=s2_coef.astype(np.float32),
        s2_bias=s2_bias.astype(np.float32),
        s2_mean=scaler.mean_.astype(np.float32),
        s2_scale=scaler.scale_.astype(np.float32),
    )
    print(f"trained on {len(y2)} paragraphs from {len(cases)} decisions; wrote {lr.WEIGHTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
