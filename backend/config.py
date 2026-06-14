import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

# Switched from local HuggingFace embeddings (sentence-transformers/all-MiniLM-L6-v2)
# to OpenAI embeddings — local model + PyTorch caused out-of-memory errors
# on Render's free tier (512MB limit). OpenAI embeddings via API have a
# negligible memory footprint and a small per-call cost.
embed_model = "text-embedding-3-small"
llm_model = "gpt-4o-mini"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_dir = os.path.join(BASE_DIR, "research-data")
chroma_db_dir = os.path.join(BASE_DIR, "chroma_db")

collection_name = "research_papers"