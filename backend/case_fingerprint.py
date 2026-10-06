"""Case fingerprint: deterministic "similar cases by subject" and "shares authorities" (no AI).

A fingerprint is a sparse bag of terms read from one decision:

* tags: the core legal tags (``legal_tagger_v3``), each counted with the structural role of the
  paragraph it appears in (overview, facts, issues, analysis, disposition, metadata);
* statute provisions: Act plus top-level section (``Immigration and Refugee Protection Act s96``),
  also counted by role;
* authorities: the cases the decision cites (kept apart on purpose).

Similarity by subject is TF-IDF cosine over the tag and statute terms (a block of plain terms plus
a block of role-qualified terms). "Shares authorities" is a separate IDF-weighted overlap of cited
cases. The two are not blended: on 150 hand-labelled pairs a blend scored lower than the subject
ranking alone (see ``case-fingerprints/round2-report.md`` in the project files).

Everything here is pure and deterministic; storage lives in ``case_fingerprint_store``.
"""

from __future__ import annotations

import bisect
import collections
import math
import re
from dataclasses import dataclass, field
from typing import Iterable, Sequence

import numpy as np
import scipy.sparse as sp

from .citations import extract_case_citation_matches, extract_statute_reference_matches
from .contextual_authority.case_structure import label_paragraph_roles, split_decision_text
from .legal_tagger_v3 import CoreLegalTaggerV3

FINGERPRINT_VERSION = "cfp-1"
DEFAULT_ROLE = "analysis"
ROLE_BLOCK_WEIGHT = 1.0
MIN_DF_PLAIN = 3
MIN_DF_ROLE = 5
MIN_DF_AUTHORITY = 2

_NEUTRAL_RE = re.compile(r"(\d{4}) (scc|fca|fc|fct|fcj|onca|bcca|abca|cacf|csc|cf) (\d+)")
_REPORTER_RE = re.compile(r"\[?(\d{4})\]? (\d+) (s\.?c\.?r\.?|f\.?c\.?|c\.?t\.?c?\.?) ?\.?(\d+)")
_COURT_ALIAS = {"fct": "fc", "cf": "fc", "cacf": "fca", "csc": "scc"}
_STATUTE_SECTION_RE = re.compile(
    r"(.*?)(?:, (?:S\.?C\.|R\.S\.C\.|S\.O\.)[^,]*(?:, c\. [^,]+)?)?,? (?:ss?|art|para|reg)\.? ?(\d+(?:\.\d+)?)"
)
_STATUTE_TAIL_RE = re.compile(r",? (?:R\.S\.C\.|S\.C\.).*$")
_CASE_KINDS = ("neutral", "case", "case_name")

_tagger: CoreLegalTaggerV3 | None = None


def _get_tagger() -> CoreLegalTaggerV3:
    global _tagger
    if _tagger is None:
        _tagger = CoreLegalTaggerV3()
    return _tagger


@dataclass(frozen=True)
class CaseFingerprint:
    """Sparse, JSON-friendly fingerprint of one decision."""

    version: str
    terms: dict[str, int]  # "t:<tag>@<role>" and "s:<provision>@<role>" -> count
    authorities: dict[str, int]  # cited-case key -> mentions
    length: int = 0
    role_chars: dict[str, int] = field(default_factory=dict)

    def plain_terms(self) -> dict[str, int]:
        """Counts summed over roles: ``t:<tag>`` and ``s:<provision>``."""
        plain: dict[str, int] = collections.Counter()
        for key, count in self.terms.items():
            plain[key.rsplit("@", 1)[0]] += count
        return dict(plain)


def authority_key(normalized_citation: str | None) -> str | None:
    """Neutral citation (or reporter citation) as a lower-case key; None for aliases."""
    text = (normalized_citation or "").lower()
    match = _NEUTRAL_RE.search(text)
    if match:
        court = _COURT_ALIAS.get(match.group(2), match.group(2))
        return f"{match.group(1)} {court} {match.group(3)}"
    match = _REPORTER_RE.search(text)
    if match:
        return f"{match.group(1)} {match.group(2)} {match.group(3)} {match.group(4)}".replace(".", "")
    return None


def statute_key(normalized_citation: str) -> str:
    """Act plus top-level section, e.g. ``Immigration and Refugee Protection Act s96``."""
    text = normalized_citation.replace(" ", " ")
    match = _STATUTE_SECTION_RE.match(text)
    if match:
        act = _STATUTE_TAIL_RE.sub("", match.group(1)).strip()
        return f"{act} s{match.group(2)}"
    return _STATUTE_TAIL_RE.sub("", text).strip()


def paragraph_role_spans(text: str) -> list[tuple[int, str]]:
    """(start offset, role) for each paragraph, in order, using the case-structure labeller."""
    paragraphs = split_decision_text(text)
    if not paragraphs:
        return []
    roles = label_paragraph_roles(paragraphs)
    spans: list[tuple[int, str]] = []
    cursor = 0
    for paragraph, role in zip(paragraphs, roles):
        first_line = paragraph.split("\n", 1)[0]
        found = text.find(first_line, cursor)
        if found < 0:
            found = cursor
        spans.append((found, role))
        cursor = found + max(1, len(first_line))
    return spans


def _role_at(starts: Sequence[int], spans: Sequence[tuple[int, str]], offset: int) -> str:
    if not spans:
        return DEFAULT_ROLE
    return spans[max(bisect.bisect_right(starts, offset) - 1, 0)][1]


def _statute_matches(content: str, window: int = 30000):
    """Statute matches over the whole text, scanned in paragraph-aligned windows.

    The statute scanner is super-linear on very long decisions (a 129,000-character decision ran
    past 60 seconds even after PR 309), so the text is cut at line breaks into windows of about
    ``window`` characters and offsets are shifted back.
    """
    matches = []
    position = 0
    while position < len(content):
        end = min(len(content), position + window)
        if end < len(content):
            line_break = content.rfind("\n", position + window // 2, end)
            end = line_break + 1 if line_break > 0 else end
        for match in extract_statute_reference_matches(content[position:end]):
            matches.append((match.offset_start + position, match.normalized_citation))
        position = end
    return matches


def compute_fingerprint(text: str | None, own_citation: str | None = None) -> CaseFingerprint:
    """Fingerprint one decision's full text. ``own_citation`` keeps a case out of its own authorities."""
    content = text or ""
    spans = paragraph_role_spans(content) if content.strip() else []
    starts = [start for start, _ in spans]
    terms: dict[str, int] = collections.Counter()
    if content.strip():
        for tag in _get_tagger().tag_occurrences(content):
            role = _role_at(starts, spans, tag.offset_start or 0)
            terms[f"t:{tag.value}@{role}"] += 1
        for offset, normalized in _statute_matches(content):
            role = _role_at(starts, spans, offset)
            terms[f"s:{statute_key(normalized)}@{role}"] += 1
    own = authority_key(own_citation)
    authorities: dict[str, int] = collections.Counter()
    if content.strip():
        for match in extract_case_citation_matches(content):
            if match.kind not in _CASE_KINDS:
                continue
            key = authority_key(match.normalized_citation)
            if key and key != own:
                authorities[key] += 1
    role_chars: dict[str, int] = collections.Counter()
    if spans:
        bounds = starts[1:] + [len(content)]
        for (start, role), end in zip(spans, bounds):
            role_chars[role] += max(0, end - start)
    return CaseFingerprint(
        version=FINGERPRINT_VERSION,
        terms=dict(terms),
        authorities=dict(authorities),
        length=len(content),
        role_chars=dict(role_chars),
    )


# --------------------------------------------------------------------------- similarity index


def _tfidf(rows: list[dict[str, int]], min_df: int) -> tuple[sp.csr_matrix, dict[str, int]]:
    """Sublinear TF x smoothed IDF, rows L2-normalised. Returns the matrix and its vocabulary."""
    document_frequency: collections.Counter[str] = collections.Counter()
    for row in rows:
        document_frequency.update(row.keys())
    vocabulary: dict[str, int] = {}
    data: list[float] = []
    row_index: list[int] = []
    column_index: list[int] = []
    n_docs = len(rows)
    for i, row in enumerate(rows):
        for key, count in sorted(row.items()):
            if document_frequency[key] < min_df:
                continue
            idf = math.log((1 + n_docs) / (1 + document_frequency[key])) + 1
            column = vocabulary.setdefault(key, len(vocabulary))
            data.append((1 + math.log(count)) * idf)
            row_index.append(i)
            column_index.append(column)
    matrix = sp.csr_matrix((data, (row_index, column_index)), shape=(n_docs, len(vocabulary)))
    return _l2(matrix), vocabulary


def _l2(matrix: sp.spmatrix) -> sp.csr_matrix:
    norms = np.sqrt(matrix.multiply(matrix).sum(axis=1)).A1
    norms[norms == 0] = 1.0
    return (sp.diags(1.0 / norms) @ matrix).tocsr()


class FingerprintIndex:
    """In-memory index over stored fingerprints (about 61k cases fit comfortably)."""

    def __init__(
        self,
        items: Iterable[tuple[int, CaseFingerprint]],
        role_weight: float = ROLE_BLOCK_WEIGHT,
        min_df_plain: int = MIN_DF_PLAIN,
        min_df_role: int = MIN_DF_ROLE,
        min_df_authority: int = MIN_DF_AUTHORITY,
    ):
        pairs = list(items)
        self.case_ids = [case_id for case_id, _ in pairs]
        self._row = {case_id: i for i, case_id in enumerate(self.case_ids)}
        tags, stat, role_rows, auth_rows = [], [], [], []
        for _, fingerprint in pairs:
            plain = fingerprint.plain_terms()
            tags.append({k: v for k, v in plain.items() if k.startswith("t:")})
            stat.append({k: v for k, v in plain.items() if k.startswith("s:")})
            role_rows.append(fingerprint.terms)
            auth_rows.append(fingerprint.authorities)
        tag_matrix, self._tag_vocab = _tfidf(tags, min_df_plain)
        stat_matrix, self._stat_vocab = _tfidf(stat, min_df_plain)
        role_matrix, self._role_vocab = _tfidf(role_rows, min_df_role)
        plain_block = _l2(sp.hstack([tag_matrix, stat_matrix]).tocsr())
        self.subject = _l2(sp.hstack([plain_block, role_matrix * role_weight]).tocsr())
        self.authorities, self._auth_vocab = _tfidf(auth_rows, min_df_authority)

    def __len__(self) -> int:
        return len(self.case_ids)

    def _top(self, matrix: sp.csr_matrix, case_id: int, k: int, min_score: float) -> list[tuple[int, float]]:
        row = self._row.get(case_id)
        if row is None:
            return []
        scores = (matrix @ matrix[row].T).toarray().ravel()
        scores[row] = -1.0
        count = min(k, len(scores) - 1)
        if count <= 0:
            return []
        top = np.argpartition(-scores, count - 1)[:count]
        # ties break on case id so results are stable
        ranked = sorted(top, key=lambda i: (-scores[i], self.case_ids[i]))
        return [(self.case_ids[i], float(scores[i])) for i in ranked if scores[i] > min_score]

    def similar_by_subject(self, case_id: int, k: int = 10, min_score: float = 0.0) -> list[tuple[int, float]]:
        """Cases closest in subject (tags + statute provisions + where in the decision they sit)."""
        return self._top(self.subject, case_id, k, min_score)

    def shares_authorities(self, case_id: int, k: int = 10, min_score: float = 0.0) -> list[tuple[int, float]]:
        """Cases that cite the most similar set of authorities (rare authorities count for more)."""
        return self._top(self.authorities, case_id, k, min_score)

    def _percentile(self, matrix: sp.csr_matrix, a: int, b: int) -> float:
        """Where ``b`` ranks among all cases for query ``a`` (1.0 = nearest), both directions averaged."""
        total = 0.0
        for query, target in ((a, b), (b, a)):
            row, other = self._row[query], self._row[target]
            scores = (matrix @ matrix[row].T).toarray().ravel()
            scores[row] = -1.0
            total += float((scores < scores[other]).sum() + 1) / len(scores)
        return total / 2

    def subject_percentile(self, a: int, b: int) -> float:
        return self._percentile(self.subject, a, b)

    def authority_percentile(self, a: int, b: int) -> float:
        return self._percentile(self.authorities, a, b)

    def explain_subject(self, a: int, b: int, limit: int = 8) -> list[tuple[str, float]]:
        """Plain (role-free) terms that two cases share, ranked by their weight in the comparison."""
        row_a, row_b = self._row.get(a), self._row.get(b)
        if row_a is None or row_b is None:
            return []
        shared: list[tuple[str, float]] = []
        names = list(self._tag_vocab) + list(self._stat_vocab)
        va = self.subject[row_a].toarray().ravel()[: len(names)]
        vb = self.subject[row_b].toarray().ravel()[: len(names)]
        for i in np.nonzero(va * vb)[0]:
            shared.append((names[i], float(va[i] * vb[i])))
        shared.sort(key=lambda item: (-item[1], item[0]))
        return shared[:limit]
