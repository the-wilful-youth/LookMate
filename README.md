# LookMate: Smart Face Shape & Virtual Styling with AR

An AI-powered virtual styling application that detects face shapes and provides personalized hairstyle and grooming recommendations with AR virtual try-on capabilities.

## 🌟 Features

### ✅ Implemented
- **Face Shape Detection**: Uses MediaPipe FaceMesh for precise facial landmark detection (468 points)
- **Gender-Based Classification**: Separate ML models for male and female face shape detection
  - Male model: Trained for Heart, Oblong, Oval, Round face shapes
  - Female model: Trained for Heart, Oblong, Oval, Round, Square face shapes
- **Multiple Input Modes**:
  - 📤 Upload Photo: Analyze images from your device
  - 📸 Webcam: Capture a photo using your webcam
  - 🎥 Live Detection: Real-time face shape analysis
- **AR Virtual Try-On**: Try different hairstyles and beard styles in real-time
- **Personalized Recommendations**: Get customized hairstyle, beard, and makeup suggestions based on your face shape and gender
- **Beautiful UI**: Gradient-themed Streamlit interface optimized for user experience

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Webcam (for live detection and webcam modes)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/the-wilful-youth/LookMate.git
cd LookMate
```

2. Create a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
LookMate/
├── app.py                      # Main Streamlit application
├── face_shape_detector.py      # Face shape detection logic
├── recommendation_engine.py    # Personalized recommendation system
├── ar_overlay.py              # AR virtual try-on module
├── model/
│   ├── men.keras              # Male face shape classification model
│   ├── Female.h5              # Female face shape classification model
│   └── gender.keras           # Gender detection model (optional)
├── assests/
│   ├── Men/
│   │   ├── hairstyles/        # PNG overlays for male hairstyles
│   │   └── beards/            # PNG overlays for beard styles
│   └── Women/
│       └── hairstyles/        # PNG overlays for female hairstyles
└── requirements.txt           # Python dependencies
```

## 🎨 Adding AR Overlays

To add custom hairstyle and beard overlays:

1. Create PNG images with **transparent backgrounds**
2. Place them in the appropriate folders:
   - Male hairstyles: `assests/Men/hairstyles/`
   - Beards: `assests/Men/beards/`
   - Female hairstyles: `assests/Women/hairstyles/`

3. Name your files descriptively (e.g., `pompadour.png`, `full_beard.png`)

### Creating Overlay Images
- Use image editing software (Photoshop, GIMP, etc.)
- Ensure transparent background (PNG with alpha channel)
- Recommended resolution: 500x500 to 1000x1000 pixels
- Center the hairstyle/beard in the image

## 🔍 How It Works

### Face Shape Detection
1. **Facial Landmark Detection**: MediaPipe FaceMesh detects 468 facial landmarks
2. **Feature Extraction**: Key measurements extracted (jaw width, face length, forehead width, etc.)
3. **Classification**: 
   - Gender-specific ML model predicts face shape
   - Fallback geometric algorithm for reliability
4. **Result**: Returns one of 5 face shapes: Oval, Round, Square, Heart, or Oblong

### Recommendation Engine
- Rule-based system with face-shape-specific styling advice
- Gender-aware recommendations
- Covers hairstyles, facial styling, and grooming tips
- Personalized to balance facial proportions

### AR Virtual Try-On
- Real-time overlay positioning based on facial landmarks
- Dynamic scaling and positioning
- Alpha blending for natural appearance
- Supports multiple overlay styles

## 🎯 Face Shape Categories

### Oval
- Balanced proportions with gentle curves
- Most versatile face shape

### Round
- Soft, curved features with full cheeks
- Equal width and length

### Square
- Strong jawline with angular features
- Similar width at forehead, cheeks, and jaw

### Heart
- Wider forehead tapering to pointed chin
- Pronounced cheekbones

### Oblong
- Longer face with balanced width
- Face length greater than width

## 🧪 Testing

The application has been tested for:
- ✅ Face detection accuracy across lighting conditions
- ✅ Real-time performance (30+ FPS)
- ✅ AR overlay alignment and scaling
- ✅ Recommendation accuracy
- ✅ Cross-browser compatibility
- ✅ User experience and interface responsiveness

## 🛠️ Technologies Used

- **Frontend**: Streamlit
- **Computer Vision**: OpenCV, MediaPipe
- **Machine Learning**: TensorFlow/Keras
- **Image Processing**: NumPy, PIL
- **AR Rendering**: Custom overlay engine with alpha blending

## 👥 Team ADAPT

- **Bhowmick, Anurag** (Team Lead) - 240211698
- **Bansal, Kshitij** - 24021455
- **Batra, Saloni** - 24022681

## 📝 License

This project is part of the PYTHON PROGRAMMING - TCS (346) course project.

## 🔮 Future Enhancements

- [ ] MiDaS depth estimation integration for enhanced 3D positioning
- [ ] More ML models for improved accuracy
- [ ] Expanded overlay library
- [ ] Color palette recommendations
- [ ] Accessory recommendations (glasses, jewelry)
- [ ] Save and share styled photos
- [ ] Mobile app version

## 🤝 Contributing

This is an educational project. For suggestions or improvements, please contact the team members.

## 📞 Support

For issues or questions, contact:
- Email: anuragbhowmick1711@gmail.com

---

**Built with ❤️ by Team ADAPT**
*LookMate v1.0 - Your AI-Powered Style Partner*
