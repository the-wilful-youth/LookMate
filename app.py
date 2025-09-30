import streamlit as st
import cv2
import numpy as np
from PIL import Image
from face_shape_detector import detect_face_shape
from recommender import recommend_styles
from overlay_utils import overlay_image

st.set_page_config(page_title="LookMate – AI Styler", layout="wide")

st.title("LookMate: Your Style Partner 💇")

option = st.radio("Choose Input Mode:", ["📤 Upload Photo", "📸 Use Webcam"])

img = None
if option == "📤 Upload Photo":
    uploaded_file = st.file_uploader("Upload a photo", type=["jpg","jpeg","png"])
    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
elif option == "📸 Use Webcam":
    capture = st.camera_input("Take a picture")
    if capture:
        img = Image.open(capture)
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

if img is not None:
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Your Photo", use_column_width=True)

    gender = st.radio("Select Gender:", ["male", "female"])
    face_shape = detect_face_shape(img)

    if face_shape:
        st.success(f"✅ Detected Face Shape: **{face_shape}**")
        styles = recommend_styles(face_shape, gender)

        if gender == "male":
            st.subheader("👨 Recommended Hairstyles")
            for h in styles["hairstyles"]:
                st.image(f"assets/{h}", caption=h.split("/")[-1].replace(".png","").title())

            st.subheader("🧔 Recommended Beards")
            for b in styles["beards"]:
                st.image(f"assets/{b}", caption=b.split("/")[-1].replace(".png","").title())

        else:
            st.subheader("👩 Recommended Hairstyles")
            for h in styles:
                st.image(f"assets/{h}", caption=h.split("/")[-1].replace(".png","").title())

    else:
        st.error("❌ Face not detected. Try another photo or better lighting.")
