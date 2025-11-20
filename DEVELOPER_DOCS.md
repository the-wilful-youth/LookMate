# LookMate - Developer Documentation

## Architecture Overview

LookMate is built using a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────┐
│                     Streamlit UI (app.py)               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Input Mode  │  │  AR Controls │  │   Results    │  │
│  │   Selection  │  │   & Settings │  │   Display    │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐  ┌────────────────┐  ┌────────────────┐
│ Face Shape    │  │  Recommendation│  │   AR Overlay   │
│   Detector    │  │     Engine     │  │     Module     │
│               │  │                │  │                │
│ - MediaPipe   │  │ - Rule-based   │  │ - Landmark     │
│ - ML Models   │  │ - Gender-aware │  │   positioning  │
│ - Geometric   │  │ - Face shape   │  │ - Alpha blend  │
│   fallback    │  │   specific     │  │ - Scaling      │
└───────────────┘  └────────────────┘  └────────────────┘
```

---

## Module Specifications

### 1. app.py - Main Application

**Responsibilities:**
- Streamlit UI rendering and layout
- User input handling (upload, webcam, live feed)
- Session state management
- Module orchestration and integration

**Key Functions:**
- Input mode selection and routing
- AR overlay control interface
- Results display and formatting
- Real-time video processing loop

**Dependencies:**
- streamlit
- opencv-python
- numpy
- PIL
- face_shape_detector
- recommendation_engine
- ar_overlay

---

### 2. face_shape_detector.py - Face Detection & Classification

**Responsibilities:**
- Facial landmark detection using MediaPipe FaceMesh
- Face shape classification using ML models
- Geometric fallback algorithm
- Model loading and caching

**Key Functions:**

#### `detect_face_shape(image, gender=None)`
Detects face shape from image using ML model or geometric algorithm.

**Parameters:**
- `image` (numpy.ndarray): BGR image from OpenCV
- `gender` (str, optional): 'Male' or 'Female'

**Returns:**
- `shape` (str): Detected face shape (Oval, Round, Square, Heart, Oblong)
- `landmarks` (numpy.ndarray): 468 facial landmark coordinates
- `detected_gender` (str): Gender used for detection

**Algorithm:**
1. Use MediaPipe FaceMesh to detect 468 facial landmarks
2. Extract face region using landmark bounds
3. Preprocess image for ML model (resize, normalize)
4. Use gender-specific ML model for classification
5. If model fails, use geometric ratio-based fallback

**Geometric Fallback Logic:**
```python
jaw_width = distance(landmark_234, landmark_454)
face_length = distance(landmark_10, landmark_152)
ratio = face_length / jaw_width

if ratio > 1.6: shape = "Oblong"
elif ratio > 1.4:
    if forehead_width > cheek_width * 1.1: shape = "Heart"
    else: shape = "Oval"
elif ratio > 1.2: shape = "Round"
else: shape = "Square"
```

#### `load_male_model(model_path='model/men.keras')`
Loads and caches male face shape classification model.

**Model Specifications:**
- Input: 300x300 RGB image, normalized [0, 1]
- Output: 4 classes [Heart, Oblong, Oval, Round]
- Architecture: CNN-based (Keras)

#### `load_female_model(model_path='model/Female.h5')`
Loads and caches female face shape classification model.

**Model Specifications:**
- Input: 224x224 RGB image, normalized [0, 1]
- Output: 5 classes [Heart, Oblong, Oval, Round, Square]
- Architecture: CNN-based (Keras/H5)

**Key Landmarks Used:**
- 10: Forehead top
- 152: Chin bottom
- 234: Left jaw
- 454: Right jaw
- 21, 251: Forehead width
- 116, 345: Cheek width

---

### 3. recommendation_engine.py - Style Recommendations

**Responsibilities:**
- Generate personalized style recommendations
- Face shape specific styling advice
- Gender-aware suggestions
- HTML formatting for display

**Key Functions:**

#### `get_recommendations(face_shape, gender)`
Returns recommendations dictionary for given face shape and gender.

**Parameters:**
- `face_shape` (str): One of [Oval, Round, Square, Heart, Oblong]
- `gender` (str): 'Male' or 'Female'

**Returns:**
Dictionary containing:
```python
{
    'hairstyles': [list of 5 recommended hairstyles with descriptions],
    'beards': [list of beard styles] (Male only),
    'makeup': [list of makeup tips] (Female only),
    'tips': [list of general styling tips]
}
```

**Recommendation Logic:**
- **Oval**: Versatile, can wear any style
- **Round**: Add height, create vertical lines
- **Square**: Soften angles, add curves
- **Heart**: Balance wide forehead, add chin width
- **Oblong**: Add width, avoid height

#### `format_recommendations_display(face_shape, gender)`
Formats recommendations as HTML for Streamlit display.

**Returns:**
- HTML string with styled list elements
- Custom colors matching app theme (#ded1c6)

---

### 4. ar_overlay.py - Virtual Try-On System

**Responsibilities:**
- Load and cache overlay images
- Position overlays using facial landmarks
- Apply alpha blending for natural appearance
- Scale overlays to face dimensions

**Key Classes:**

#### `AROverlay`
Main class for AR overlay management.

**Methods:**

##### `__init__(assets_path='assests')`
Initialize overlay system with asset directory path.

##### `load_overlay_image(overlay_path)`
Load PNG overlay with alpha channel, cache for performance.

##### `apply_overlay(frame, landmarks, overlay_type, gender, style_name=None)`
Apply AR overlay to video frame.

**Parameters:**
- `frame`: BGR video frame
- `landmarks`: Facial landmark array (468 points)
- `overlay_type`: 'hairstyle' or 'beard'
- `gender`: 'Male' or 'Female'
- `style_name`: Specific style file name (optional)

**Algorithm:**
1. Calculate face dimensions from landmarks
2. Load appropriate overlay image
3. Resize overlay to match face size
4. Calculate anchor position from landmarks
5. Blend overlay using alpha channel

**Positioning Logic:**
```python
# Hairstyle positioning
anchor = forehead_top (landmark 10)
width = face_width * 1.2
height = face_height * 0.6
offset_y = -face_height * 0.3  # Above forehead

# Beard positioning
anchor = mouth_bottom (landmark 13)
width = face_width * 0.8
height = face_height * 0.4
offset_y = 0  # At mouth level
```

##### `get_available_overlays(overlay_type, gender)`
List available overlay styles from assets folder.

**Returns:**
- List of style names (without .png extension)

---

## Data Flow

### Upload Photo Mode
```
User uploads image
    ↓
Convert to OpenCV BGR format
    ↓
detect_face_shape(image, gender)
    ↓
MediaPipe detects 468 landmarks
    ↓
Extract face ROI, preprocess
    ↓
ML model predicts face shape
    ↓
get_recommendations(shape, gender)
    ↓
Display results + recommendations
    ↓
(Optional) Apply AR overlays
```

### Live Detection Mode
```
Initialize webcam
    ↓
Continuous loop:
    Read frame
    ↓
    Flip horizontally
    ↓
    detect_face_shape(frame, gender)
    ↓
    (Optional) Apply AR overlays
    ↓
    Draw landmarks and info box
    ↓
    Display frame in Streamlit
    ↓
    30ms delay
```

---

## Performance Optimization

### Model Loading
- **Lazy Loading**: Models loaded only when needed
- **Global Caching**: Single model instance per session
- **Singleton Pattern**: `_male_model` and `_female_model` globals

### Image Processing
- **Batch Size**: Single image inference (batch=1)
- **Verbose**: Disabled for faster prediction
- **Preprocessing**: Vectorized NumPy operations

### AR Rendering
- **Image Caching**: Overlays cached after first load
- **Alpha Blending**: Optimized NumPy operations
- **Frame Rate**: Target 30 FPS for live detection

### Streamlit Optimization
- **Session State**: Store AR overlay instance
- **Component Reuse**: Minimize re-rendering
- **Lazy Imports**: Import only when needed

---

## ML Model Training (Reference)

### Male Model (men.keras)
```python
Input: 300x300x3 RGB images
Classes: 4 [Heart, Oblong, Oval, Round]
Architecture: CNN
Training: Custom dataset of male faces
Format: Keras SavedModel
```

### Female Model (Female.h5)
```python
Input: 224x224x3 RGB images
Classes: 5 [Heart, Oblong, Oval, Round, Square]
Architecture: CNN
Training: Custom dataset of female faces
Format: HDF5 (Keras)
```

**Training Process:**
1. Data collection and labeling
2. Image augmentation (rotation, flip, brightness)
3. Normalization [0, 1]
4. CNN training with validation split
5. Model evaluation and fine-tuning
6. Export to production format

---

## Adding New Features

### Adding New Face Shapes

1. **Update Models**: Retrain with new class
2. **Update face_shape_detector.py**:
   ```python
   shape_classes = ['Heart', 'Oblong', 'Oval', 'Round', 'Square', 'NewShape']
   ```
3. **Update recommendation_engine.py**:
   ```python
   "NewShape": {
       "hairstyles": [...],
       "beards": [...],
       "tips": [...]
   }
   ```

### Adding AR Overlays

1. Create PNG with alpha transparency
2. Save to appropriate folder:
   - `assests/Men/hairstyles/`
   - `assests/Men/beards/`
   - `assests/Women/hairstyles/`
3. Name descriptively: `style_name.png`
4. Restart app - automatically detected

### Integrating MiDaS Depth Estimation

1. Install MiDaS:
   ```bash
   pip install timm
   ```

2. Load MiDaS model:
   ```python
   import torch
   midas = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
   ```

3. Estimate depth:
   ```python
   depth = midas(frame)
   ```

4. Use depth for overlay scaling:
   ```python
   scale_factor = calculate_scale_from_depth(depth, landmarks)
   overlay_resized = cv2.resize(overlay, (width*scale_factor, height*scale_factor))
   ```

---

## Testing

### Unit Tests
Create `tests/test_face_detection.py`:
```python
import unittest
from face_shape_detector import detect_face_shape

class TestFaceDetection(unittest.TestCase):
    def test_oval_detection(self):
        img = cv2.imread('test_images/oval_face.jpg')
        shape, landmarks, gender = detect_face_shape(img, 'Male')
        self.assertEqual(shape, 'Oval')
```

### Integration Tests
Test complete workflow:
1. Load test images for each face shape
2. Run detection
3. Verify correct recommendations returned
4. Test AR overlay positioning

### Performance Tests
```python
import time
start = time.time()
for i in range(100):
    detect_face_shape(test_image, 'Male')
avg_time = (time.time() - start) / 100
print(f"Average detection time: {avg_time:.3f}s")
```

---

## Deployment

### Streamlit Cloud
1. Push to GitHub
2. Connect repository in Streamlit Cloud
3. Deploy from `main` branch
4. Set `app.py` as entry point

### Local Deployment
```bash
streamlit run app.py --server.port 8501
```

### Docker (Optional)
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

---

## Code Style Guidelines

- **PEP 8**: Follow Python style guide
- **Type Hints**: Use for function parameters
- **Docstrings**: Document all public functions
- **Comments**: Explain complex logic
- **Variable Names**: Descriptive, snake_case
- **Constants**: UPPER_SNAKE_CASE

---

## Version Control

### Git Workflow
```bash
# Create feature branch
git checkout -b feature/new-face-shape

# Make changes and commit
git add .
git commit -m "Add new face shape detection"

# Push and create PR
git push origin feature/new-face-shape
```

### Commit Message Format
```
<type>: <subject>

<body>

<footer>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`

---

## License & Attribution

- MediaPipe: Apache 2.0 License
- TensorFlow/Keras: Apache 2.0 License
- OpenCV: Apache 2.0 License
- Streamlit: Apache 2.0 License

---

## Contact & Support

**Team ADAPT**
- Lead Developer: Anurag Bhowmick
- Email: anuragbhowmick1711@gmail.com
- Repository: https://github.com/the-wilful-youth/LookMate

---

*Last Updated: November 2024*
