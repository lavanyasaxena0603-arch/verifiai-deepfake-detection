# VerifiAI – System Architecture

## Overview
VerifiAI is an AI-powered deepfake detection platform that analyzes images, videos, and audio to identify AI-generated or manipulated media.

## Components

### 1. Frontend
- User uploads media
- Displays authenticity score & report
- Planned with React / Next.js

### 2. Backend (FastAPI)
- Accepts file uploads
- Routes requests to detection services
- Generates responses & reports

### 3. AI Engine (Planned)
- Image deepfake detection
- Audio deepfake detection
- Video frame analysis
- GAN artifact detection

### 4. Report Generator
- Generates forensic-style reports
- Exportable as PDF

## Deployment
- Backend: FastAPI + Uvicorn
- Frontend: Vercel
