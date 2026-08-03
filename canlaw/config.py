import os

DB_PATH = os.getenv("CANLAW_DB_PATH", "canlaw.db")
HF_DATASET = os.getenv("CANLAW_HF_DATASET", "a2aj/canadian-case-law")
DEFAULT_COURTS = ["FC", "RPD", "FCA", "SCC"]
HF_COURT_DATA_DIRS = {
    "FC": os.getenv("CANLAW_HF_FC_DATA_DIR", "FC"),
    "RPD": os.getenv("CANLAW_HF_RPD_DATA_DIR", "RPD"),
    "FCA": os.getenv("CANLAW_HF_FCA_DATA_DIR", "FCA"),
    "SCC": os.getenv("CANLAW_HF_SCC_DATA_DIR", "SCC"),
}
EMBEDDING_MODEL_NAME = os.getenv("CANLAW_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
SUMMARIZATION_MODEL_NAME = os.getenv("CANLAW_SUMMARIZATION_MODEL", "facebook/bart-large-cnn")
