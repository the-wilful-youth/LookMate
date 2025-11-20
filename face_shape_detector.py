"""
Face Shape Detector - Optimized for Real-time Performance
Uses geometric ratio analysis with persistent MediaPipe instance
"""

import cv2
import mediapipe as mp
import numpy as np
import os


class FaceShapeDetector:
    """
    Real-time face shape detector using geometric analysis.
    Optimized for >30 FPS performance with persistent MediaPipe instance.
    """
    
    def __init__(self):
        """Initialize MediaPipe Face Mesh once for the entire session."""
        self.mp_face_mesh = mp.solutions.face_mesh
        # Use static_image_mode=False for video (enables temporal tracking)
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.shape_classes = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']
    
    def detect_face_shape(self, image, gender=None):
        """
        Detect face shape using geometric ratio analysis.
        
        Args:
            image: BGR image from OpenCV
            gender: User's gender (Male/Female) - kept for compatibility
        
        Returns:
            tuple: (face_shape, landmarks, gender)
        """
        # Convert BGR to RGB for MediaPipe
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Process the image
        results = self.face_mesh.process(image_rgb)
        
        if not results.multi_face_landmarks:
            return None, None, None
        
        # Get landmarks
        landmarks = results.multi_face_landmarks[0].landmark
        h, w, _ = image.shape
        points = np.array([[int(l.x * w), int(l.y * h)] for l in landmarks])
        
        # Calculate geometric ratios
        face_shape = self._calculate_face_shape(points)
        
        # Use provided gender or default to Male
        if gender is None:
            gender = "Male"
        
        return face_shape, points, gender
    
    def _calculate_face_shape(self, points):
        """
        Calculate face shape using geometric ratios.
        
        Key landmarks:
        - Jaw: 234 (left), 454 (right)
        - Forehead: 10 (top), 152 (chin)
        - Forehead width: 21 (left), 251 (right)
        - Cheek width: 116 (left), 345 (right)
        """
        try:
            # Calculate key measurements
            jaw_width = np.linalg.norm(points[234] - points[454])
            face_length = np.linalg.norm(points[10] - points[152])
            forehead_width = np.linalg.norm(points[21] - points[251])
            cheek_width = np.linalg.norm(points[116] - points[345])
            
            # Prevent division by zero
            if jaw_width == 0:
                return "Oval"  # Default fallback
            
            # Calculate aspect ratio
            ratio = face_length / jaw_width
            
            # Classify based on geometric ratios
            if ratio > 1.6:
                # Very long face
                shape = "Oblong"
            elif ratio > 1.4:
                # Medium-long face - check forehead vs cheeks
                if forehead_width > cheek_width * 1.1:
                    shape = "Heart"
                else:
                    shape = "Oval"
            elif ratio > 1.2:
                # Slightly long face
                shape = "Round"
            else:
                # Wide face
                shape = "Square"
            
            return shape
            
        except Exception as e:
            print(f"Error in geometric calculation: {e}")
            return "Oval"  # Default fallback
    
    def __del__(self):
        """Clean up MediaPipe resources."""
        if hasattr(self, 'face_mesh'):
            self.face_mesh.close()


# Legacy function for backward compatibility
def detect_face_shape(image, gender=None):
    """
    Legacy function wrapper for backward compatibility.
    Note: Creates a new detector instance each time (not optimal).
    For best performance, use FaceShapeDetector class directly.
    """
    detector = FaceShapeDetector()
    return detector.detect_face_shape(image, gender)
