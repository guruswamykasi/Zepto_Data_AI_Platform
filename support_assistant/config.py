import os


MOCK_LLM = os.getenv("MOCK_LLM", "1")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

CHROMA_PATH = "data/chroma_db"

COLLECTION_NAME = "zepto_policies"

TOP_K = 3