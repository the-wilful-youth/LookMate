from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import cv2
import numpy as np
import uvicorn
import os
from typing import List

# Import core logic
from face_shape_detector import FaceShapeDetector
from recommendation_engine import get_recommendations, get_detailed_recommendations
from ar_overlay import AROverlay
from utils import get_style_recommendations_for_face_shape

app = FastAPI(title="LookMate API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static assets
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# Initialize global instances
face_detector = FaceShapeDetector()
ar_overlay = AROverlay()

@app.get("/")
async def root():
    return {"message": "LookMate API is running"}

@app.post("/detect")
async def detect_face(file: UploadFile = File(...), gender: str = "Male"):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise HTTPException(status_code=400, detail="Invalid image file")

        # Detect face shape
        face_shape, landmarks, detected_gender = face_detector.detect_face_shape(img, gender=gender)
        
        if not face_shape:
            return {"success": False, "error": "Could not detect face"}

        # Convert landmarks to list for JSON serialization
        landmarks_list = landmarks.tolist() if landmarks is not None else []

        return {
            "success": True,
            "face_shape": face_shape,
            "gender": gender,
            "landmarks": landmarks_list
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/recommendations/{face_shape}")
async def get_style_recommendations(face_shape: str, gender: str = "Male"):
    try:
        recommendations = get_style_recommendations_for_face_shape(face_shape, gender)
        return {"success": True, "recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/styles/{style_type}")
async def get_available_styles(style_type: str, gender: str = "Male"):
    """
    style_type: 'hairstyle' or 'beard'
    """
    try:
        styles = ar_overlay.get_available_overlays(style_type, gender)
        return {"success": True, "styles": styles}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
