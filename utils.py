import streamlit as st

def load_css():
    """Load custom CSS styles"""
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

def render_header():
    """Render the main application header"""
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">LookMate</h1>
        <p class="main-subtitle">Your AI-Powered Style Partner</p>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render the application footer"""
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: rgba(255,255,255,0.7); padding: 2rem;">
        <p>✨ Built by Team ADAPT • LookMate v1.0</p>
    </div>
    """, unsafe_allow_html=True)
