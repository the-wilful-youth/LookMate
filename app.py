import os
# Fix for Mac OpenMP runtime error
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time
import json

from face_shape_detector import FaceShapeDetector
from recommendation_engine import (
    get_recommendations, 
    format_recommendations_display,
    get_detailed_recommendations,
    format_detailed_recommendations_display
)
from ar_overlay import AROverlay
from utils import load_css, render_header, render_footer, get_style_recommendations_for_face_shape

st.set_page_config(
    page_title="LookMate – AI Styler", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="✨"
)

# Initialize AR Overlay system
if 'ar_overlay' not in st.session_state:
    st.session_state.ar_overlay = AROverlay()

# Initialize Face Shape Detector (persistent instance for performance)
if 'face_detector' not in st.session_state:
    st.session_state.face_detector = FaceShapeDetector()

# Load CSS and render header
load_css()
render_header()

with st.sidebar:
    st.markdown("### 📋 Input Method")
    input_mode = st.radio(
        "How would you like to analyze your face?",
        ["📤 Upload Photo", "📸 Use Webcam", "🎥 Live Detection"],
        help="Choose your preferred method for face analysis"
    )
    
    st.markdown("---")
    st.markdown("### 👤 Profile")
    gender_selection = st.radio(
        "Select your gender:",
        ["Male", "Female"],
        help="This helps us provide more accurate recommendations"
    )
    
    st.info(f"✓ Using {gender_selection} detection model")
    
    st.markdown("---")
    st.markdown("### 💡 Recommendations")
    recommendation_style = st.radio(
        "Detail level:",
        ["Quick Overview", "Detailed Guide"],
        help="Quick: Simple list • Detailed: Step-by-step with celebrity examples"
    )
    
    # AR overlay selections are now moved to after face detection   

col1, col2 = st.columns([1, 1], gap="large")

img = None
ar_hairstyle = None
ar_beard = None
enable_ar = False

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
            
elif input_mode == "📸 Use Webcam":
    with col1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("#### 📸 Take a Photo")
        capture = st.camera_input(
            "Capture your photo",
            help="Position your face in the center and ensure good lighting"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if capture:
            # Convert the file-like object to an image
            image = Image.open(capture)
            # Convert PIL image to numpy array (RGB)
            img_array = np.array(image)
            # Convert RGB to BGR for OpenCV
            img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

if input_mode == "🎥 Live Detection":
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown("#### 🎥 Live Face Shape Detection")
    st.markdown('<div class="info-box">Position your face in front of the camera for real-time analysis</div>', unsafe_allow_html=True)
    
    # Initialize session state for camera control
    if 'camera_running' not in st.session_state:
        st.session_state.camera_running = False
    if 'ar_hairstyle' not in st.session_state:
        st.session_state.ar_hairstyle = None
    if 'ar_beard' not in st.session_state:
        st.session_state.ar_beard = None
    
    FRAME_WINDOW = st.empty()
    control_col1, control_col2 = st.columns([1, 1])
    
    with control_col1:
        if st.button("🚀 Start Detection", type="primary"):
            st.session_state.camera_running = True
    with control_col2:
        if st.button("⏹️ Stop Detection"):
            st.session_state.camera_running = False
    
    # Style selectors (outside camera loop)
    st.markdown("---")
    st.markdown("### 💇 Select Styles to Try")
    
    style_col1, style_col2 = st.columns(2)
    
    with style_col1:
        st.markdown("**Hairstyles**")
        available_hairstyles = st.session_state.ar_overlay.get_available_overlays('hairstyle', gender_selection)
        if available_hairstyles:
            hairstyle_options = ["None"] + available_hairstyles
            current_hair_idx = 0
            if st.session_state.ar_hairstyle in available_hairstyles:
                current_hair_idx = hairstyle_options.index(st.session_state.ar_hairstyle)
            
            selected_hair = st.selectbox(
                "Choose hairstyle:",
                hairstyle_options,
                index=current_hair_idx,
                key="hair_selector"
            )
            if selected_hair == "None":
                st.session_state.ar_hairstyle = None
            else:
                st.session_state.ar_hairstyle = selected_hair
    
    with style_col2:
        if gender_selection == "Male":
            st.markdown("**Beard Styles**")
            available_beards = st.session_state.ar_overlay.get_available_overlays('beard', gender_selection)
            if available_beards:
                beard_options = ["None"] + available_beards
                current_beard_idx = 0
                if st.session_state.ar_beard in available_beards:
                    current_beard_idx = beard_options.index(st.session_state.ar_beard)
                
                selected_beard = st.selectbox(
                    "Choose beard:",
                    beard_options,
                    index=current_beard_idx,
                    key="beard_selector"
                )
                if selected_beard == "None":
                    st.session_state.ar_beard = None
                else:
                    st.session_state.ar_beard = selected_beard
    
    # Placeholder for details below the video
    details_placeholder = st.empty()
    
    if st.session_state.camera_running:
        # Use selected camera index
        cap = cv2.VideoCapture(1)
        
        # Set camera resolution to 640x480 for better performance
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        last_face_shape = None
        
        try:
            if not cap.isOpened():
                st.error(f"❌ Could not access camera at index {camera_index}. Please try a different index in the sidebar.")
            else:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        st.error("❌ Failed to read frame from webcam")
                        break
                        
                    frame = cv2.flip(frame, 1)
                    # Use persistent detector instance for performance
                    face_shape, landmarks, detected_gender = st.session_state.face_detector.detect_face_shape(frame, gender=gender_selection)
                    
                    if face_shape:
                        # Apply AR overlays from session state
                        if landmarks is not None:
                            current_hairstyle = st.session_state.get('ar_hairstyle')
                            current_beard = st.session_state.get('ar_beard')
                            
                            if current_hairstyle:
                                frame = st.session_state.ar_overlay.apply_overlay(
                                    frame, landmarks, 'hairstyle', gender_selection, current_hairstyle
                                )
                            if current_beard and gender_selection == "Male":
                                frame = st.session_state.ar_overlay.apply_overlay(
                                    frame, landmarks, 'beard', gender_selection, current_beard
                                )
                        
                        # Draw minimal info box with semi-transparent background
                        overlay = frame.copy()
                        cv2.rectangle(overlay, (10, 10), (200, 65), (0, 0, 0), -1)
                        cv2.addWeighted(overlay, 0.5, frame, 0.5, 0, frame)
                        cv2.rectangle(frame, (10, 10), (200, 65), (0, 255, 0), 2)
                        
                        # Helper to draw text with outline for maximum visibility
                        def draw_text(img, text, pos, scale, color, thickness=1):
                            # Draw black outline for contrast
                            cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, scale, (0, 0, 0), thickness + 2)
                            # Draw bright text
                            cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness)

                        # Display gender and face shape with smaller font
                        draw_text(frame, f"Gender: {gender_selection}", (15, 28), 0.4, (0, 255, 0), 1)
                        draw_text(frame, f"Face Shape: {face_shape}", (15, 45), 0.4, (0, 255, 0), 1)
                        
                        # Display AR status with smaller font
                        if landmarks is not None:
                            draw_text(frame, f"AR Points: {len(landmarks)}", (15, 60), 0.35, (255, 255, 0), 1)
                        else:
                            draw_text(frame, "AI Active", (15, 60), 0.35, (255, 255, 255), 1)
                        
                        # Update details panel if face shape changed
                        if face_shape != last_face_shape:
                            last_face_shape = face_shape
                            
                            with details_placeholder.container():
                                st.markdown('<div class="result-card">', unsafe_allow_html=True)
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
                                    
                                st.markdown('</div>', unsafe_allow_html=True)

                    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), use_container_width=True)
                    # Removed time.sleep for maximum FPS performance
                    
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            cap.release()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif img is not None:
    # Use persistent detector instance
    face_shape, landmarks, detected_gender = st.session_state.face_detector.detect_face_shape(img, gender=gender_selection)
    
    with col1:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("#### 📷 Your Photo")
        
        # Create annotated image with landmarks for AR mapping
        annotated_img = img.copy()
        
        # Apply AR overlays from selected styles in session state
        if landmarks is not None:
            if st.session_state.get('selected_hairstyle'):
                annotated_img = st.session_state.ar_overlay.apply_overlay(
                    annotated_img, landmarks, 'hairstyle', gender_selection, st.session_state.selected_hairstyle
                )
            if st.session_state.get('selected_beard') and gender_selection == "Male":
                annotated_img = st.session_state.ar_overlay.apply_overlay(
                    annotated_img, landmarks, 'beard', gender_selection, st.session_state.selected_beard
                )
        
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
    
    # NEW SECTION: Display recommended styles with AR try-on after detection
    if face_shape and landmarks is not None:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown("### ✨ Try Virtual Styles (AR)")
        st.markdown("Select recommended hairstyles and beards to see them on your photo!")
        
        # Initialize session state for selected styles
        if 'selected_hairstyle' not in st.session_state:
            st.session_state.selected_hairstyle = None
        if 'selected_beard' not in st.session_state:
            st.session_state.selected_beard = None
            
        # Get recommended styles based on detected face shape
        recommended_styles = get_style_recommendations_for_face_shape(face_shape, gender_selection)
        available_hairstyles = st.session_state.ar_overlay.get_available_overlays('hairstyle', gender_selection)
        
        # Filter to show only recommended styles that exist as overlays
        recommended_hairstyles = [h for h in recommended_styles['hairstyles'] if h in available_hairstyles]
        
        # Display Hairstyles
        if recommended_hairstyles:
            st.markdown(f"#### 💇 Recommended Hairstyles for {face_shape} Face")
            
            # Show hairstyle options with images in columns
            cols_per_row = 3
            for i in range(0, len(recommended_hairstyles), cols_per_row):
                cols = st.columns(cols_per_row)
                for j, col in enumerate(cols):
                    idx = i + j
                    if idx < len(recommended_hairstyles):
                        style = recommended_hairstyles[idx]
                        with col:
                            # Display style image
                            gender_folder = 'Men' if gender_selection == 'Male' else 'Women'
                            img_path = f"assets/{gender_folder}/hairstyles/{style}.png"
                            
                            if os.path.exists(img_path):
                                st.image(img_path, caption=style.replace('_', ' ').title(), use_container_width=True)
                            else:
                                st.write(f"📷 {style.replace('_', ' ').title()}")
                            
                            # Button to select this style
                            button_label = "✅ Selected" if st.session_state.selected_hairstyle == style else "Try This"
                            if st.button(button_label, key=f"hair_{style}", use_container_width=True):
                                st.session_state.selected_hairstyle = style
            
            # Clear selection button
            if st.session_state.selected_hairstyle:
                if st.button("🚫 Remove Hairstyle", use_container_width=False):
                    st.session_state.selected_hairstyle = None
        
        # Display Beards (Male only)
        if gender_selection == "Male":
            available_beards = st.session_state.ar_overlay.get_available_overlays('beard', gender_selection)
            recommended_beards = [b for b in recommended_styles['beards'] if b in available_beards]
            
            if recommended_beards:
                st.markdown(f"#### 🧔 Recommended Beard Styles for {face_shape} Face")
                
                # Show beard options with images in columns
                for i in range(0, len(recommended_beards), cols_per_row):
                    cols = st.columns(cols_per_row)
                    for j, col in enumerate(cols):
                        idx = i + j
                        if idx < len(recommended_beards):
                            style = recommended_beards[idx]
                            with col:
                                # Display style image
                                img_path = f"assets/Men/beards/{style}.png"
                                
                                if os.path.exists(img_path):
                                    st.image(img_path, caption=style.replace('_', ' ').title(), use_container_width=True)
                                else:
                                    st.write(f"📷 {style.replace('_', ' ').title()}")
                                
                                # Button to select this style
                                button_label = "✅ Selected" if st.session_state.selected_beard == style else "Try This"
                                if st.button(button_label, key=f"beard_{style}", use_container_width=True):
                                    st.session_state.selected_beard = style
                
                # Clear selection button
                if st.session_state.selected_beard:
                    if st.button("🚫 Remove Beard", use_container_width=False):
                        st.session_state.selected_beard = None
        
        # Display preview with selected styles
        if st.session_state.selected_hairstyle or st.session_state.selected_beard:
            st.markdown("---")
            st.markdown("#### 👁️ Preview with Selected Styles")
            
            preview_img = img.copy()
            if st.session_state.selected_hairstyle:
                preview_img = st.session_state.ar_overlay.apply_overlay(
                    preview_img, landmarks, 'hairstyle', gender_selection, st.session_state.selected_hairstyle
                )
            if st.session_state.selected_beard and gender_selection == "Male":
                preview_img = st.session_state.ar_overlay.apply_overlay(
                    preview_img, landmarks, 'beard', gender_selection, st.session_state.selected_beard
                )
            
            st.image(cv2.cvtColor(preview_img, cv2.COLOR_BGR2RGB), use_container_width=True)
            
            # Download button
            _, buf = cv2.imencode('.png', preview_img)
            st.download_button(
                label="📥 Download Preview",
                data=buf.tobytes(),
                file_name="lookmate_preview.png",
                mime="image/png"
            )
        
        st.markdown('</div>', unsafe_allow_html=True)

render_footer()
