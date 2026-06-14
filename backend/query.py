import chromadb

from llama_index.core import VectorStoreIndex, Settings
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.chroma import ChromaVectorStore

from backend.config import embed_model, llm_model, chroma_db_dir, collection_name

# Settings.embed_model = HuggingFaceEmbedding(model_name=embed_model)
Settings.embed_model = OpenAIEmbedding(model=embed_model)

Settings.llm = OpenAI(model=llm_model, temperature=0.1)

Chroma_client = chromadb.PersistentClient(path= chroma_db_dir)
Chroma_collection = Chroma_client.get_or_create_collection(collection_name)

vector_store = ChromaVectorStore(chroma_collection= Chroma_collection)

index = VectorStoreIndex.from_vector_store(vector_store= vector_store)

query_engine = index.as_query_engine(similarity_top_k= 5)


# question = "What is UR-BERT?"
MIN_SCORE = 0.25
def ask_question(question: str):
    response = query_engine.query(question)

    sources = []
    for source in response.source_nodes:
        if source.score > MIN_SCORE:
            sources.append({
                "file_name": source.node.metadata.get("file_name", "N/A"),
                "score": round(source.score, 4),
            })

    if not sources:
        return {
            "answer": "I don't know based on the uploaded documents.",
            "sources": []
        }


    return {
        "answer": str(response),
        "sources": sources
    }

