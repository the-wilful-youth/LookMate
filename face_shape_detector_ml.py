import cv2
import mediapipe as mp
import numpy as np
import torch
import torch.nn as nn

mp_face_mesh = mp.solutions.face_mesh

def detect_face_shape(image, model_path='/Users/Anurag/Downloads/model.pth'):
    device = torch.device('cpu')
    
    shape_classes = ['Heart', 'Oblong', 'Oval', 'Round', 'Square']
    
    with mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1,
                               refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:
        results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if not results.multi_face_landmarks:
            return None, None

        landmarks = results.multi_face_landmarks[0].landmark
        h, w, _ = image.shape
        points = np.array([[int(l.x * w), int(l.y * h)] for l in landmarks])

        jaw_width = np.linalg.norm(points[234] - points[454])
        face_length = np.linalg.norm(points[10] - points[152])
        
        if jaw_width == 0:
            return None, None
            
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

        return shape, points
