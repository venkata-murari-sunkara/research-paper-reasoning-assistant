from fastapi import FastAPI, UploadFile, File, HTTPException
from backend.schemas import QuestionRequest
from backend.query import ask_question
from backend.config import data_dir
from backend.ingest import ingest_single_pdf
import os, shutil


app = FastAPI()


@app.post("/ask")
async def ask(request: QuestionRequest):
    result = ask_question(request.question)
    return result



@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    file_path = os.path.join(data_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_result = ingest_single_pdf(file_path)

    return {
        "message": "PDF uploaded successfully",
        "file_name": file.filename,
        "ingestion": ingest_result
    }

# print(__name__)