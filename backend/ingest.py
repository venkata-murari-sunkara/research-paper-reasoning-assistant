import os, chromadb

from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex, Settings
from llama_index.core.node_parser import TokenTextSplitter
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from backend.config import embed_model, data_dir, chroma_db_dir, collection_name


# docs = SimpleDirectoryReader(data_dir).load_data()
# print(f"Loaded {len(docs)} documents")

# Settings.embed_model = HuggingFaceEmbedding(model_name=embed_model)
Settings.embed_model = OpenAIEmbedding(model=embed_model)

Settings.node_parser = TokenTextSplitter(
    chunk_size= 1000, 
    chunk_overlap= 150,
    separator= " "
)

os.makedirs(data_dir, exist_ok=True)

Chroma_client = chromadb.PersistentClient(path= chroma_db_dir)
Chroma_collection = Chroma_client.get_or_create_collection(collection_name)

vector_store = ChromaVectorStore(chroma_collection= Chroma_collection)

storage_context = StorageContext.from_defaults(vector_store= vector_store)

print("Starting ingestion...")


def ingest_single_pdf(file_path: str):
    docs = SimpleDirectoryReader(input_files=[file_path]).load_data()

    VectorStoreIndex.from_documents(
        docs,
        storage_context=storage_context
    )

    return {
        "message": "PDF ingested successfully",
        "file_name": os.path.basename(file_path),
        "collection_count": Chroma_collection.count()
    }


def ingest_all_papers():
    docs = SimpleDirectoryReader(data_dir).load_data()

    VectorStoreIndex.from_documents(
        docs,
        storage_context=storage_context
    )

    return {
        "message": "All papers ingested successfully",
        "documents_loaded": len(docs),
        "collection_count": Chroma_collection.count()
    }


if __name__ == "__main__":
    result = ingest_all_papers()
    print(result)