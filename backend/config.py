import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

embed_model = "sentence-transformers/all-MiniLM-L6-v2"
llm_model = "gpt-4o-mini"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_dir = os.path.join(BASE_DIR, "research-data")
chroma_db_dir = os.path.join(BASE_DIR, "chroma_db")

collection_name = "research_papers"