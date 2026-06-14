import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

embed_model = "BAAI/bge-small-en-v1.5"
llm_model = "gpt-4o-mini"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_dir = os.path.join(BASE_DIR, "research-data")
chroma_db_dir = os.path.join(BASE_DIR, "chroma_db")

collection_name = "research_papers"