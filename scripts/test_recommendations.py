import streamlit as st
from recommendation_engine import format_detailed_recommendations_display

st.set_page_config(page_title="Test Recommendations", layout="wide")

st.title("Testing Detailed Recommendations")

face_shape = st.selectbox("Face Shape", ["Oval", "Round", "Square", "Heart", "Oblong"])
gender = st.radio("Gender", ["Male", "Female"])

if st.button("Show Recommendations"):
    st.markdown("---")
    st.markdown("### Using st.markdown with unsafe_allow_html=True")
    
    detailed_html = format_detailed_recommendations_display(face_shape, gender)
    st.markdown(detailed_html, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Raw HTML (for debugging)")
    st.code(detailed_html[:500], language="html")
