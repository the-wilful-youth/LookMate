import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

def detect_face_shape(image):
    """
    Detect face shape using MediaPipe landmarks.
    Returns: 'Oval', 'Round', 'Square', 'Heart', or None
    """
    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1,
                               refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if not results.multi_face_landmarks:
            return None

        landmarks = results.multi_face_landmarks[0].landmark
        h, w, _ = image.shape
        points = np.array([[int(l.x * w), int(l.y * h)] for l in landmarks])

        jaw_width = np.linalg.norm(points[234] - points[454])  
        face_length = np.linalg.norm(points[10] - points[152])  

        ratio = face_length / jaw_width

        if ratio > 1.5:
            return "Oval"
        elif 1.3 < ratio <= 1.5:
            return "Round"
        elif ratio <= 1.2:
            return "Square"
        else:
            return "Heart"
