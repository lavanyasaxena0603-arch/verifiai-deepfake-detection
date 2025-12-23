from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from models.detector import analyze_media
import os

app = FastAPI(title="VerifiAI Backend")

# Allow frontend access later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "VerifiAI backend is running"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Call ML detector logic
    analysis_result = analyze_media(file_path)

    # Remove temp file after analysis
    if os.path.exists(file_path):
        os.remove(file_path)

    return {
        "filename": file.filename,
        "analysis": analysis_result
    }
