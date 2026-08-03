import importlib

import numpy as np


class FakeEmbeddingModel:
    def __init__(self):
        self.batch_sizes = []

    def encode(self, texts, *, batch_size, show_progress_bar):
        self.batch_sizes.append(len(texts))
        return [np.array([len(text), 1.0], dtype=np.float32) for text in texts]


def test_embeddings_are_batched_and_existing_vectors_are_skipped(tmp_path, monkeypatch):
    monkeypatch.setenv("CANLAW_DB_PATH", str(tmp_path / "canlaw.db"))

    import canlaw.config as config
    import canlaw.db as db
    import canlaw.embeddings as embeddings

    importlib.reload(config)
    importlib.reload(db)
    importlib.reload(embeddings)
    db.init_db()

    with db.get_conn() as conn:
        for index in range(3):
            db.insert_case(
                conn,
                {
                    "citation_en": f"2024 FC {index}",
                    "unofficial_text_en": f"Decision text {index}",
                },
                "FC",
            )

    model = FakeEmbeddingModel()
    monkeypatch.setattr(embeddings, "get_embed_model", lambda: model)

    assert embeddings.embed_all_court_cases(["FC"], batch_size=2) == 3
    assert model.batch_sizes == [2, 1]
    assert embeddings.embed_all_court_cases(["FC"], batch_size=2) == 0
