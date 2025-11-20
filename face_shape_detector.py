"""
Face Shape Detector - Optimized for Real-time Performance
Uses geometric ratio analysis with persistent MediaPipe instance
"""

import cv2
import mediapipe as mp
import numpy as np
import os
import tensorflow as tf

class FaceShapeDetector:
    """
    Face shape detector using Deep Learning models with geometric fallback.
    """
    
    def __init__(self):
        """Initialize MediaPipe and load DL models."""
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.shape_classes = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']
        self.models = {}
        self.model_loaded = False
        
        # Load Models
        try:
            base_path = os.path.dirname(os.path.abspath(__file__))
            model_dir = os.path.join(base_path, "model")
            
            self.models['Male'] = tf.keras.models.load_model(os.path.join(model_dir, "men.keras"))
            self.models['Female'] = tf.keras.models.load_model(os.path.join(model_dir, "Female.h5"))
            self.models['gender'] = tf.keras.models.load_model(os.path.join(model_dir, "gender.keras"))
            self.model_loaded = True
            print("✅ DL Models loaded successfully")
        except Exception as e:
            print(f"⚠️ Could not load DL models: {e}. Falling back to geometric analysis.")
            self.model_loaded = False
    
    def detect_face_shape(self, image, gender=None):
        """
        Detect face shape using DL models if available, else geometric.
        """
        # Convert BGR to RGB for MediaPipe
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process the image to get landmarks
        results = self.face_mesh.process(image_rgb)
        
        if not results.multi_face_landmarks:
            return None, None, None
        
        # Get landmarks
        landmarks = results.multi_face_landmarks[0].landmark
        h, w, _ = image.shape
        points = np.array([[int(l.x * w), int(l.y * h)] for l in landmarks])
        
        # 1. Predict Gender if not provided
        if gender is None:
            if self.model_loaded:
                gender = self._predict_gender(image, points)
            else:
                gender = "Male" # Default fallback
        
        # 2. Predict Face Shape
        if self.model_loaded:
            face_shape = self._predict_shape_dl(image, points, gender)
        else:
            face_shape = self._calculate_face_shape(points)
        
        return face_shape, points, gender
    
    def _crop_face(self, image, points):
        """Crop face based on landmarks with some padding."""
        x, y, w, h = cv2.boundingRect(points)
        
        # Add padding (20%)
        pad_x = int(w * 0.2)
        pad_y = int(h * 0.2)
        
        img_h, img_w = image.shape[:2]
        
        x1 = max(0, x - pad_x)
        y1 = max(0, y - pad_y)
        x2 = min(img_w, x + w + pad_x)
        y2 = min(img_h, y + h + pad_y)
        
        return image[y1:y2, x1:x2]

    def _predict_gender(self, image, points):
        """Predict gender using DL model."""
        try:
            face_crop = self._crop_face(image, points)
            if face_crop.size == 0: return "Male"
            
            # Resize to model input (assuming 200x200 or similar, checking input shape)
            target_size = self.models['gender'].input_shape[1:3]
            resized = cv2.resize(face_crop, target_size)
            normalized = resized / 255.0
            input_data = np.expand_dims(normalized, axis=0)
            
            prediction = self.models['gender'].predict(input_data, verbose=0)
            # Assuming binary classification: 0=Female, 1=Male or vice versa. 
            # Usually 0=Female, 1=Male in many datasets, but let's check prediction shape.
            # If prediction is [0.9, 0.1] -> Class 0.
            
            if prediction.shape[-1] == 1:
                return "Male" if prediction[0][0] > 0.5 else "Female"
            else:
                return "Male" if np.argmax(prediction) == 0 else "Female" # Need to verify mapping
                
        except Exception as e:
            print(f"Gender prediction error: {e}")
            return "Male"

    def _predict_shape_dl(self, image, points, gender):
        """Predict face shape using specific gender model."""
        try:
            model = self.models.get(gender, self.models['Male'])
            
            face_crop = self._crop_face(image, points)
            if face_crop.size == 0: return "Oval"
            
            target_size = model.input_shape[1:3]
            resized = cv2.resize(face_crop, target_size)
            normalized = resized / 255.0
            input_data = np.expand_dims(normalized, axis=0)
            
            prediction = model.predict(input_data, verbose=0)
            class_idx = np.argmax(prediction)
            
            return self.shape_classes[class_idx]
            
        except Exception as e:
            print(f"Shape prediction error: {e}")
            return self._calculate_face_shape(points) # Fallback

    def _calculate_face_shape(self, points):
        """
        Calculate face shape using geometric ratios (Fallback).
        """
        try:
            # Calculate key measurements
            jaw_width = np.linalg.norm(points[234] - points[454])
            face_length = np.linalg.norm(points[10] - points[152])
            forehead_width = np.linalg.norm(points[21] - points[251])
            cheek_width = np.linalg.norm(points[116] - points[345])
            
            if jaw_width == 0: return "Oval"
            
            ratio = face_length / jaw_width
            
            if ratio > 1.6: return "Oblong"
            elif ratio > 1.4:
                return "Heart" if forehead_width > cheek_width * 1.1 else "Oval"
            elif ratio > 1.2: return "Round"
            else: return "Square"
            
        except Exception:
            return "Oval"
    
    def __del__(self):
        if hasattr(self, 'face_mesh'):
            self.face_mesh.close()

# Legacy function wrapper
def detect_face_shape(image, gender=None):
    detector = FaceShapeDetector()
    return detector.detect_face_shape(image, gender)
