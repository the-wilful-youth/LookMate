import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time
import json

from face_shape_detector import detect_face_shape
from recommendation_engine import (
    get_recommendations, 
    format_recommendations_display,
    get_detailed_recommendations,
    format_detailed_recommendations_display
)
from ar_overlay import AROverlay

st.set_page_config(
    page_title="LookMate – AI Styler", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="✨"
)

# Initialize AR Overlay system
if 'ar_overlay' not in st.session_state:
    st.session_state.ar_overlay = AROverlay()

st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f2d4d 0%, #2c4a6b 25%, #a77693 75%, #ded1c6 100%);
    }
    
    .stApp > div {
        color: #ded1c6 !important;
    }
    
    .stMarkdown, .stText, p, span, div {
        color: #ded1c6 !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #ded1c6 !important;
    }
    
    header[data-testid="stHeader"] {
        display: none;
    }
    
    .stToolbar {
        display: none;
    }
    
    .stDeployButton {
        display: none;
    }
    
    #MainMenu {
        visibility: hidden;
    }
    
    footer {
        visibility: hidden;
    }
    
    .main-header {
        text-align: center;
        background: rgba(15, 45, 77, 0.8);
        padding: 2rem;
        border-radius: 20px;
        backdrop-filter: blur(15px);
        margin-bottom: 2rem;
        border: 2px solid rgba(222, 209, 198, 0.3);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
    }
    
    .main-subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 0;
    }
    
    .result-card {
        background: rgba(15, 45, 77, 0.85);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.25);
        margin: 1rem 0;
        border: 2px solid rgba(222, 209, 198, 0.4);
        backdrop-filter: blur(10px);
    }
    
    .result-card h4 {
        color: #ded1c6 !important;
        margin-bottom: 1rem;
    }
    
    .result-card p, .result-card div {
        color: #ded1c6 !important;
    }
    
    .face-shape-result {
        text-align: center;
        font-size: 2rem;
        font-weight: 600;
        color: black !important;
        margin: 1rem 0;
        padding: 1rem;
    }
    
    .stSuccess {
        background-color: rgba(15, 45, 77, 0.8) !important;
        color: #ded1c6 !important;
        border: 1px solid rgba(222, 209, 198, 0.5) !important;
    }
    
    .stError {
        background-color: rgba(15, 45, 77, 0.8) !important;
        color: #ded1c6 !important;
        border: 1px solid rgba(222, 209, 198, 0.5) !important;
    }
    
    .stInfo {
        background-color: rgba(15, 45, 77, 0.8) !important;
        color: #ded1c6 !important;
        border: 1px solid rgba(222, 209, 198, 0.5) !important;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #0f2d4d 0%, #a77693 100%);
        backdrop-filter: blur(10px);
    }
    
    .stSidebar > div:first-child {
        background: linear-gradient(180deg, #0f2d4d 0%, #2c4a6b 50%, #a77693 100%);
    }
    
    .stSidebar .stMarkdown {
        color: #ded1c6 !important;
    }
    
    .stSidebar .stMarkdown h3 {
        color: #ded1c6 !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    .stSidebar .stRadio > label {
        color: #ded1c6 !important;
        font-weight: 600;
    }
    
    .stSidebar .stRadio div[role="radiogroup"] label {
        color: #ded1c6 !important;
    }
    
    .stSidebar .stInfo {
        background-color: rgba(15, 45, 77, 0.7) !important;
        color: #ded1c6 !important;
        border: 1px solid rgba(222, 209, 198, 0.3);
    }
    
    .stFileUploader label {
        color: #ded1c6 !important;
    }
    
    .stCameraInput label {
        color: #ded1c6 !important;
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #0f2d4d, #a77693);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .live-feed {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
    
    .info-box {
        background: linear-gradient(45deg, #a77693, #ded1c6);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        color: #0f2d4d;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1 class="main-title">LookMate</h1>
    <p class="main-subtitle">Your AI-Powered Style Partner</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🎨 Controls")
    input_mode = st.radio(
        "Choose Input Method:",
        ["📤 Upload Photo", "📸 Webcam", "🎥 Live Detection"],
        help="Select how you want to analyze your face shape"
    )
    
    st.markdown("---")
    st.markdown("### 👤 Gender Selection")
    gender_selection = st.radio(
        "Select your gender:",
        ["Male", "Female"],
        help="Choose your gender for accurate face shape detection"
    )
    
    st.info(f"✓ Using {gender_selection} model for face shape detection")
    
    st.markdown("---")
    st.markdown("### 🎨 Recommendation Style")
    recommendation_style = st.radio(
        "Choose recommendation detail level:",
        ["Quick Overview", "Detailed Guide"],
        help="Quick Overview: Simple list. Detailed Guide: Step-by-step with celebrity examples"
    )
    
    st.markdown("---")
    st.markdown("### 🎨 AR Virtual Try-On")
    enable_ar = st.checkbox("Enable AR Overlays", value=False, 
                            help="Try virtual hairstyles and beards in real-time")
    
    ar_hairstyle = None
    ar_beard = None
    
    if enable_ar:
        # Get available overlays
        available_hairstyles = st.session_state.ar_overlay.get_available_overlays('hairstyle', gender_selection)
        
        if available_hairstyles:
            ar_hairstyle = st.selectbox("Choose Hairstyle:", 
                                        ["None"] + available_hairstyles,
                                        help="Select a hairstyle to try virtually")
            if ar_hairstyle == "None":
                ar_hairstyle = None
        else:
            st.info("💡 No hairstyle overlays available. Add PNG images to assests folder.")
        
        if gender_selection == "Male":
            available_beards = st.session_state.ar_overlay.get_available_overlays('beard', gender_selection)
            if available_beards:
                ar_beard = st.selectbox("Choose Beard:", 
                                       ["None"] + available_beards,
                                       help="Select a beard style to try virtually")
                if ar_beard == "None":
                    ar_beard = None
            else:
                st.info("💡 No beard overlays available. Add PNG images to assests folder.")

col1, col2 = st.columns([1, 1], gap="large")

img = None
if input_mode == "📤 Upload Photo":
    with col1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("#### 📤 Upload Your Photo")
        uploaded_file = st.file_uploader(
            "Choose a photo", 
            type=["jpg","jpeg","png"],
            help="Upload a clear front-facing photo for best results"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if uploaded_file:
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, 1)
            
elif input_mode == "📸 Webcam":
    with col1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("#### 📸 Take a Photo")
        capture = st.camera_input(
            "Capture your photo",
            help="Position your face in the center and ensure good lighting"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if capture:
            img = Image.open(capture)
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

if input_mode == "🎥 Live Detection":
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown("#### 🎥 Live Face Shape Detection")
    st.markdown('<div class="info-box">Position your face in front of the camera for real-time analysis</div>', unsafe_allow_html=True)
    
    FRAME_WINDOW = st.empty()
    control_col1, control_col2 = st.columns([1, 1])
    
    with control_col1:
        start_detection = st.button("🚀 Start Detection", type="primary")
    with control_col2:
        stop_detection = st.button("⏹️ Stop Detection")
    
    if start_detection:
        cap = cv2.VideoCapture(1)
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    st.error("❌ Could not access webcam")
                    break
                    
                frame = cv2.flip(frame, 1)
                face_shape, landmarks, detected_gender = detect_face_shape(frame, gender=gender_selection)
                
                if face_shape:
                    # Apply AR overlays if enabled
                    if enable_ar and landmarks is not None:
                        if ar_hairstyle:
                            frame = st.session_state.ar_overlay.apply_overlay(
                                frame, landmarks, 'hairstyle', gender_selection, ar_hairstyle
                            )
                        if ar_beard and gender_selection == "Male":
                            frame = st.session_state.ar_overlay.apply_overlay(
                                frame, landmarks, 'beard', gender_selection, ar_beard
                            )
                    
                    # Draw facial landmarks on frame for AR visualization (optional)
                    if landmarks is not None and not enable_ar:
                        for point in landmarks:
                            cv2.circle(frame, tuple(point), 1, (0, 255, 255), -1)
                    
                    # Draw info box
                    cv2.rectangle(frame, (10, 10), (450, 130), (0, 0, 0), -1)
                    cv2.rectangle(frame, (10, 10), (450, 130), (0, 255, 0), 2)
                    
                    # Display Gender
                    cv2.putText(frame, f"Gender: {gender_selection}", (20, 45), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    
                    # Display Face Shape
                    cv2.putText(frame, f"Face Shape: {face_shape}", (20, 80), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    
                    # Display landmarks count
                    if landmarks is not None:
                        cv2.putText(frame, f"AR Points: {len(landmarks)}", (20, 110), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                    
                    cv2.putText(frame, "AI Detection Active", (20, 122), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
                
                FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), use_container_width=True)
                time.sleep(0.03)
                
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            cap.release()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif img is not None:
    face_shape, landmarks, detected_gender = detect_face_shape(img, gender=gender_selection)
    
    with col1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("#### 📷 Your Photo")
        
        # Create annotated image with landmarks for AR mapping
        annotated_img = img.copy()
        
        # Apply AR overlays if enabled
        if enable_ar and landmarks is not None:
            if ar_hairstyle:
                annotated_img = st.session_state.ar_overlay.apply_overlay(
                    annotated_img, landmarks, 'hairstyle', gender_selection, ar_hairstyle
                )
            if ar_beard and gender_selection == "Male":
                annotated_img = st.session_state.ar_overlay.apply_overlay(
                    annotated_img, landmarks, 'beard', gender_selection, ar_beard
                )
        elif landmarks is not None and not enable_ar:
            # Draw key facial landmarks for AR mapping
            for i, point in enumerate(landmarks):
                cv2.circle(annotated_img, tuple(point), 1, (0, 255, 0), -1)
        
        st.image(cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        if face_shape:
            st.markdown("#### 🎯 Analysis Results")
            
            # Display Gender prominently
            gender_icon = "👨" if gender_selection == "Male" else "👩"
            st.markdown(f'<div class="face-shape-result">{gender_icon} Gender: {gender_selection}</div>', unsafe_allow_html=True)
            
            # Display Face Shape
            st.markdown(f'<div class="face-shape-result">Face Shape: {face_shape}</div>', unsafe_allow_html=True)
            
            descriptions = {
                "Oval": "🥚 Balanced proportions with gentle curves",
                "Round": "⭕ Soft, curved features with full cheeks", 
                "Square": "⬜ Strong jawline with angular features",
                "Heart": "💖 Wider forehead tapering to pointed chin",
                "Oblong": "📏 Longer face with balanced width"
            }
            
            if face_shape in descriptions:
                st.info(f"**Characteristics:** {descriptions[face_shape]}")
            
            # Display AR mapping information
            if landmarks is not None:
                st.success(f"✅ Face detection successful! {len(landmarks)} facial landmarks detected for AR mapping")
                
                # Store landmarks in session state for AR use
                st.session_state['face_landmarks'] = landmarks
                st.session_state['gender'] = gender_selection
                st.session_state['face_shape'] = face_shape
                
                with st.expander("📍 View AR Mapping Points"):
                    st.write(f"Total landmarks: {len(landmarks)}")
                    st.write("Key points for AR mapping:")
                    st.write(f"- Jawline points: {landmarks[[234, 454]]}")
                    st.write(f"- Forehead points: {landmarks[[21, 251]]}")
                    st.write(f"- Cheek points: {landmarks[[116, 345]]}")
                    st.write(f"- Chin point: {landmarks[152]}")
                    st.download_button(
                        label="📥 Download Landmarks (JSON)",
                        data=str(landmarks.tolist()),
                        file_name="face_landmarks.json",
                        mime="application/json"
                    )
            else:
                st.success("✅ Face detection successful!")
            
            # Display personalized recommendations
            st.markdown("---")
            st.markdown("### 🌟 Personalized Style Recommendations")
            
            if recommendation_style == "Detailed Guide":
                # Show detailed recommendations with styling instructions
                detailed_html = format_detailed_recommendations_display(face_shape, gender_selection)
                # Wrap in a container div for proper rendering
                st.markdown(f'<div class="result-card">{detailed_html}</div>', unsafe_allow_html=True)
            else:
                # Show quick overview  
                recommendations_html = format_recommendations_display(face_shape, gender_selection)
                st.markdown(recommendations_html, unsafe_allow_html=True)
        else:
            st.markdown("#### ❌ Detection Failed")
            st.error("Could not detect face shape")
            st.markdown("""
            **Tips for better detection:**
            - Ensure good lighting
            - Face the camera directly
            - Remove glasses or accessories
            - Use a clear, high-quality image
            """)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(255,255,255,0.7); padding: 2rem;">
    <p>✨ Built by Team ADAPT • LookMate v1.0</p>
</div>
""", unsafe_allow_html=True)
