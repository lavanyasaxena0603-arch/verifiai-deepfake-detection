from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="VerifiAI Backend")

# Allow frontend to connect later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "VerifiAI backend is running"}

@app.post("/analyze")
async def analyze_media(file: UploadFile = File(...)):
    """
    This endpoint will later analyze uploaded media
    (image/video/audio) for deepfake detection.
    """
    return {
        "filename": file.filename,
        "status": "received",
        "message": "Deepfake analysis will be implemented here"
    }
