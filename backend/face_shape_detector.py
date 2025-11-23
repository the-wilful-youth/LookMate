import numpy as np
import cv2

class FaceShapeDetector:
    def __init__(self):
        print("⚠️ FaceShapeDetector running in MOCK MODE (MediaPipe not available)")

    def detect_face_shape(self, image, gender='Male'):
        """
        Mock implementation of face shape detection.
        Returns a random or fixed face shape and dummy landmarks.
        """
        # Return a fixed shape for consistency in testing
        face_shape = "Oval"
        
        # Create dummy landmarks (468 points, x/y/z)
        # We'll just make them all 0 or some center point to avoid errors if accessed
        # In a real mock, we might want valid coordinates, but for now this prevents crashes
        landmarks = np.zeros((468, 3))
        
        # Mock detected gender
        detected_gender = gender
        
        return face_shape, landmarks, detected_gender
