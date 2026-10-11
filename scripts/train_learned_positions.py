"""Train the learned whose-position weights used by backend/learned_positions.py.

Labels: data/position_preview/case_<id>.json (main holder of each printed paragraph, from the stored propositions
run: model output, not a lawyer's truth). Text: a folder of <id>.json files with title, court, date and full_text
(``scripts/fetch_position_texts.py`` writes them). Decisions dated 2005 or later that concern immigration and whose id
is a multiple of 5 are the untouched hold-out: never trained on, only scored.

Stage 1 is a logistic model over opening words and rule results; stage 2 reads stage 1's out-of-fold guesses (5 folds
by decision) for the neighbouring paragraphs. Needs scikit-learn (training only; the site runs numpy only).

    python scripts/train_learned_positions.py --texts position_texts [--haiku-labels hk_labels.json] [--write]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
	sys.path.insert(0, str(REPO_ROOT))

from backend import learned_positions as lp  # noqa: E402
from backend.position_holder import HOLDERS, split_numbered_paragraphs, tag_decision  # noqa: E402

LABELS_DIR = REPO_ROOT / "data" / "position_preview"
_IMMIGRATION = re.compile(r"citizenship and immigration|public safety|immigration|refugee|border services", re.I)


class Case:
	pass


def is_immigration(title: str, court: str, text: str) -> bool:
	return bool(_IMMIGRATION.search(title or "") or court in ("RAD", "RPD", "IAD") or "Immigration and Refugee Protection Act" in (text or "")[:20000])


def load_cases(texts_dir: Path) -> list[Case]:
	cases = []
	for path in sorted(texts_dir.glob("*.json")):
		stored = json.loads(path.read_text(encoding="utf-8"))
		label_path = LABELS_DIR / f"case_{path.stem}.json"
		if not label_path.exists() or not stored.get("full_text"):
			continue
		labels = json.loads(label_path.read_text(encoding="utf-8"))["paragraphs"]
		full = stored["full_text"]
		header, body = lp.split_header(full)
		numbered = split_numbered_paragraphs(full)
		c = Case()
		c.id = int(path.stem)
		c.title, c.court, c.date = stored.get("title") or "", stored.get("court") or "", stored.get("date") or ""
		c.year = int(c.date[:4]) if c.date[:4].isdigit() else None
		c.immigration = is_immigration(c.title, c.court, full)
		c.numbers = sorted(numbered)
		c.texts = [numbered[n] for n in c.numbers]
		c.header, c.body = header, body
		c.label = [(labels[str(n)]["h"][0] if str(n) in labels and labels[str(n)].get("h") else None) for n in c.numbers]
		cases.append(c)
	return cases


def is_holdout(c: Case) -> bool:
	return bool(c.year and c.year >= 2005 and c.immigration and c.id % 5 == 0)


def main(argv=None) -> int:
	from scipy.sparse import csr_matrix, hstack, vstack
	from sklearn.linear_model import LogisticRegression
	from sklearn.preprocessing import StandardScaler

	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument("--texts", type=Path, required=True)
	parser.add_argument("--c", type=float, default=1.0)
	parser.add_argument("--haiku-labels", type=Path, help="optional JSON {case_id: [holder per paragraph index]} for an independent check")
	parser.add_argument("--write", action="store_true", help="write the weights file (otherwise only report)")
	args = parser.parse_args(argv)

	cases = load_cases(args.texts)
	for c in cases:
		c.dense, c.rules = lp.dense_features(c.texts, c.title, c.header, c.body)
		rows, cols, vals = [], [], []
		for i, text in enumerate(c.texts):
			for k, v in lp.text_features(text).items():
				rows.append(i), cols.append(k), vals.append(v)
		c.sparse = csr_matrix((vals, (rows, cols)), shape=(len(c.texts), lp.HASH_BUCKETS))
		c.x1 = hstack([c.sparse, csr_matrix(c.dense)]).tocsr()
		c.y = np.array([HOLDERS.index(h) if h in HOLDERS else -1 for h in c.label])
	train = [c for c in cases if not is_holdout(c)]
	hold = [c for c in cases if is_holdout(c)]
	print(f"{len(cases)} decisions: {len(train)} to train on, {len(hold)} untouched hold-out")

	def fit(subset):
		x = vstack([c.x1 for c in subset]).tocsr()
		y = np.concatenate([c.y for c in subset])
		keep = y >= 0
		return LogisticRegression(C=args.c, max_iter=3000).fit(x[keep], y[keep])

	def full_log_p(model, x):
		out = np.full((x.shape[0], len(HOLDERS)), lp._FLOOR)
		out[:, model.classes_] = np.log(np.clip(model.predict_proba(x), 1e-4, 1))
		return out

	folds = 5
	x2, y2 = [], []
	for fold in range(folds):
		model = fit([c for i, c in enumerate(train) if i % folds != fold])
		for c in train[fold::folds]:
			x2.append(lp.stack_features(full_log_p(model, c.x1), c.dense))
			y2.append(c.y)
	x2, y2 = np.vstack(x2), np.concatenate(y2)
	keep = y2 >= 0
	scaler = StandardScaler().fit(x2[keep])
	model2 = LogisticRegression(C=1.0, max_iter=3000).fit(scaler.transform(x2[keep]), y2[keep])
	model1 = fit(train)

	def predict(c):
		stacked = scaler.transform(lp.stack_features(full_log_p(model1, c.x1), c.dense))
		return [HOLDERS[i] for i in model2.predict(stacked)]

	def score(name, subset, pred_fn, label_fn=lambda c: c.label):
		hit = total = 0
		for c in subset:
			for g, p in zip(label_fn(c), pred_fn(c)):
				if g in HOLDERS:
					total += 1
					hit += g == p
		print(f"  {name:<12} {100 * hit / max(1, total):5.1f}%  ({total} paragraphs)")

	print("hold-out, against the stored labels:")
	score("rules", hold, lambda c: c.rules)
	score("all court", hold, lambda c: ["court"] * len(c.texts))
	score("learned", hold, predict)
	if args.haiku_labels:
		haiku = {int(k): v for k, v in json.loads(args.haiku_labels.read_text()).items()}
		sub = [c for c in hold if c.id in haiku]
		print(f"independent Haiku labels, {len(sub)} hold-out decisions:")
		for name, fn in (("rules", lambda c: c.rules), ("learned", predict)):
			score(name, sub, fn, lambda c: haiku[c.id])
		score("stored labels", sub, lambda c: c.label, lambda c: haiku[c.id])
	confusion = Counter()
	for c in hold:
		for g, p in zip(c.label, predict(c)):
			if g in HOLDERS:
				confusion[(g, p)] += 1
	for h in HOLDERS:
		n = sum(v for (g, _), v in confusion.items() if g == h)
		pn = sum(v for (_, p), v in confusion.items() if p == h)
		print(f"  {h:<26} n={n:5d} recall {100 * confusion[(h, h)] / max(1, n):3.0f}% precision {100 * confusion[(h, h)] / max(1, pn):3.0f}%")

	if args.write:
		width = train[0].x1.shape[1]
		coef = np.zeros((len(HOLDERS), width))
		coef[model1.classes_] = model1.coef_
		bias = np.full(len(HOLDERS), -9.0)
		bias[model1.classes_] = model1.intercept_
		s2_coef = np.zeros((len(HOLDERS), x2.shape[1]))
		s2_coef[model2.classes_] = model2.coef_
		s2_bias = np.full(len(HOLDERS), -9.0)
		s2_bias[model2.classes_] = model2.intercept_
		np.savez_compressed(
			lp.WEIGHTS_PATH,
			sparse=coef[:, : lp.HASH_BUCKETS].astype(np.float16),
			dense=coef[:, lp.HASH_BUCKETS :].astype(np.float16),
			bias=bias.astype(np.float32),
			s2_coef=s2_coef.astype(np.float32),
			s2_bias=s2_bias.astype(np.float32),
			s2_mean=scaler.mean_.astype(np.float32),
			s2_scale=scaler.scale_.astype(np.float32),
		)
		print(f"wrote {lp.WEIGHTS_PATH}")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
