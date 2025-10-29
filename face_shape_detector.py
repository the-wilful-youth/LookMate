import cv2
import mediapipe as mp
import numpy as np
import torch
import torch.nn as nn
from torchvision import transforms

mp_face_mesh = mp.solutions.face_mesh

class CustomMobileNet(nn.Module):
    def __init__(self, num_classes=5):
        super(CustomMobileNet, self).__init__()
        self.features = nn.Sequential()
        self.classifier = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(1792, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = nn.functional.adaptive_avg_pool2d(x, (1, 1))
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

def detect_face_shape(image, model_path='model/model.pth'):
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

        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        x_min, x_max = max(0, min(x_coords) - 20), min(w, max(x_coords) + 20)
        y_min, y_max = max(0, min(y_coords) - 20), min(h, max(y_coords) + 20)
        
        face_crop = image[y_min:y_max, x_min:x_max]
        if face_crop.size == 0:
            return None, None
            
        face_resized = cv2.resize(face_crop, (224, 224))
        face_rgb = cv2.cvtColor(face_resized, cv2.COLOR_BGR2RGB)
        
        transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        
        face_tensor = transform(face_rgb).unsqueeze(0)
        
        try:
            model_state = torch.load(model_path, map_location=device)
            model = CustomMobileNet()
            model.load_state_dict(model_state, strict=False)
            model.eval()
            
            with torch.no_grad():
                outputs = model(face_tensor)
                _, predicted = torch.max(outputs, 1)
                shape = shape_classes[predicted.item()]
        except:
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
