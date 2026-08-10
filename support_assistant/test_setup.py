import fastapi
import chromadb
import langgraph
import sentence_transformers
import pydantic

print("FastAPI:", fastapi.__version__)
print("ChromaDB:", chromadb.__version__)
print("LangGraph:", langgraph.__version__)
print("Sentence Transformers:", sentence_transformers.__version__)
print("Pydantic:", pydantic.__version__)

print("Module 3 environment is ready!")