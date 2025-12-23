from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="VerifiAI Backend")

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
async def analyze_media(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "File received. Deepfake analysis coming soon."
    }

