# Research Paper Reasoning Assistant 🤖

A Retrieval-Augmented Generation (RAG) application that allows users to upload research papers, parse and index them in a local vector database, and ask natural language questions deeply grounded in the document context.

## 🚀 Features

* **PDF Research Paper Upload:** Easily process dense, multi-page scientific papers.
* **Automated Ingestion Pipeline:** Smart document chunking and node parsing via LlamaIndex.
* **High-Quality Embeddings:** Dense vector generation using the state-of-the-art `BAAI/bge-small-en-v1.5` Sentence Transformer.
* **Local Vector Storage:** Fast, persistent vector management powered by `ChromaDB`.
* **Semantic Retrieval & RAG:** Context-focused retrieval paired with `OpenAI GPT-4o-mini` for precise, grounded answers.
* **Source Attribution:** Full transparency with similarity scores and exact context references mapped to every response.
* **Decoupled Architecture:** Enterprise-ready layout featuring a FastAPI backend and an interactive Streamlit UI.

---

## 🏗️ Architecture

Below is the system architecture illustrating how data flows dynamically between the frontend UI, the decoupled API endpoints, and the underlying RAG pipeline.

![Research Assistant Architecture](assets/architecture-diagram.png)

### Ingestion Pipeline (Left Branch)
1. **Upload:** User uploads a PDF via the Streamlit interface, hitting the `/upload` endpoint.
2. **Parsing:** LlamaIndex extracts text and splits the document into optimized chunks.
3. **Embedding:** Text chunks are transformed into dense vectors using the BGE model.
4. **Storage:** Vectors and metadata are indexed and persisted securely inside ChromaDB.

### Query Pipeline (Right Branch)
1. **Query:** User submits a natural language question through the UI to the `/ask` endpoint.
2. **Retrieval:** The Retriever cross-references the query vector against ChromaDB to extract the most semantically relevant chunks.
3. **Synthesis:** The retrieved context and user query are compiled into a prompt and sent to GPT-4o-mini.
4. **Response:** The user receives a comprehensive answer accompanied by source text attribution.

---

## 📸 Demo

![Application Screenshot](assets/ui.png)

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI (Python)
* **RAG Framework:** LlamaIndex
* **Vector Database:** ChromaDB
* **Embedding Model:** BAAI/bge-small-en-v1.5 (Local HuggingFace embedding)
* **Language Model:** OpenAI GPT-4o-mini
* **Frontend UI:** Streamlit

---

## 📂 Project Structure

```text
research-paper-reasoning-assistant/
├── backend/
│   ├── config.py
│   ├── ingest.py
│   ├── query.py
│   ├── schemas.py
│   └── main.py
├── frontend/
│   └── app.py
├── research-data/          # Local PDF storage cache
├── chroma_db/              # Persistent vector store directory
├── requirements.txt        # Shared project dependencies
├── .env                     # System environment variables (git-ignored)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/venkata-murari-sunkara/research-paper-reasoning-assistant.git
cd research-paper-reasoning-assistant
```

### 2. Set Up Virtual Environment

```bash
# Create environment
python -m venv venv

# Activate Environment (Mac/Linux)
source venv/bin/activate

# Activate Environment (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory of the project:

```text
OPENAI_API_KEY=your_actual_openai_api_key_here
```

### 5. Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL: `http://127.0.0.1:8000`

### 6. Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend URL: `http://localhost:8501`

---

## 🎯 Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector Search
- Semantic Retrieval
- Document Chunking
- Embedding Models
- FastAPI REST APIs
- Streamlit Frontend Development
- Production-Style AI System Architecture

---


## 👨‍💻 Author

**Venkata Murari**

- GitHub: [venkata-murari-sunkara](https://github.com/venkata-murari-sunkara)
- LinkedIn: [venkata-murari](https://www.linkedin.com/in/venkata-murari/)
