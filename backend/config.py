import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

embed_model = "BAAI/bge-small-en-v1.5"
llm_model = "gpt-4o-mini"

data_dir = "./research-data"
chroma_db_dir = "./chroma_db"
collection_name = "research_papers"