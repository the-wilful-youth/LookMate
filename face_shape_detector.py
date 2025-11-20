import cv2
import mediapipe as mp
import numpy as np
from tensorflow import keras
import tensorflow as tf

mp_face_mesh = mp.solutions.face_mesh

_male_model = None
_female_model = None

import os

def load_male_model(model_path=None):
    global _male_model
    if _male_model is None:
        try:
            if model_path is None:
                model_path = os.path.join(os.path.dirname(__file__), 'model', 'men.keras')
            _male_model = keras.models.load_model(model_path, compile=False)
        except Exception as e:
            print(f"Warning: Male model loading error: {e}")
            _male_model = None
    return _male_model

def load_female_model(model_path=None):
    global _female_model
    if _female_model is None:
        try:
            if model_path is None:
                model_path = os.path.join(os.path.dirname(__file__), 'model', 'Female.h5')
            _female_model = keras.models.load_model(model_path, compile=False)
        except Exception as e:
            print(f"Warning: Female model not found at {model_path}")
            _female_model = None
    return _female_model

def detect_face_shape(image, gender=None):
    shape_classes = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']
    
    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1,
                               refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if not results.multi_face_landmarks:
            return None, None, None

        landmarks = results.multi_face_landmarks[0].landmark
        h, w, _ = image.shape
        points = np.array([[int(l.x * w), int(l.y * h)] for l in landmarks])

        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        x_min, x_max = max(0, min(x_coords) - 20), min(w, max(x_coords) + 20)
        y_min, y_max = max(0, min(y_coords) - 20), min(h, max(y_coords) + 20)
        
        face_crop = image[y_min:y_max, x_min:x_max]
        if face_crop.size == 0:
            return None, None, None
        
        # Gender should be provided by user, not detected
        if gender is None:
            gender = "Male"  # Default fallback
        
        try:
            if gender == "Male":
                # Men model expects 300x300 input and has 4 classes
                face_resized = cv2.resize(face_crop, (300, 300))
                face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
                face_normalized = face_rgb / 255.0
                face_batch = np.expand_dims(face_normalized, axis=0)
                
                model = load_male_model()
                if model:
                    predictions = model.predict(face_batch, verbose=0)
                    shape_idx = np.argmax(predictions[0])
                    # Men model has 4 classes
                    shape_map = ['Heart', 'Oblong', 'Oval', 'Round']
                    if shape_idx < len(shape_map):
                        shape = shape_map[shape_idx]
                    else:
                        shape = 'Square'
                else:
                    raise Exception("Male model not loaded")
            else:
                # Female model expects 224x224 input and has 5 classes
                face_resized = cv2.resize(face_crop, (224, 224))
                face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
                face_normalized = face_rgb / 255.0
                face_batch = np.expand_dims(face_normalized, axis=0)
                
                model = load_female_model()
                if model:
                    predictions = model.predict(face_batch, verbose=0)
                    shape_idx = np.argmax(predictions[0])
                    # Female model has 5 classes: Heart, Oblong, Oval, Round, Square
                    if shape_idx < len(shape_classes):
                        shape = shape_classes[shape_idx]
                    else:
                        shape = shape_classes[0]
                else:
                    raise Exception("Female model not found")
        except Exception as e:
            print(f"Face shape detection error: {e}, using fallback method")
            jaw_width = np.linalg.norm(points[234] - points[454])
            face_length = np.linalg.norm(points[10] - points[152])
            
            if jaw_width == 0:
                return None, None, None
                
            ratio = face_length / jaw_width
            forehead_width = np.linalg.norm(points[21] - points[251])
            cheek_width = np.linalg.norm(points[116] - points[345])
            
            if ratio > 1.6:
                shape = "Oblong"
            elif ratio > 1.4:
                if forehead_width > cheek_width * 1.1:
                    shape = "Heart"
                else:
                    shape = "Oval"
            elif ratio > 1.2:
                shape = "Round"
            else:
                shape = "Square"

        return shape, points, gender
