import streamlit as st

def load_css():
    """Load custom CSS styles with high contrast for maximum readability"""
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        
        /* Global Styles */
        * {
            font-family: 'Inter', sans-serif;
            color: #000000; /* Default to black text */
        }
        
        .main {
            padding-top: 2rem;
        }
        
        /* Vibrant Background */
        .stApp {
            background: linear-gradient(135deg, #F042FF 0%, #87F5F5 100%);
            background-attachment: fixed;
        }
        
        /* Hide Streamlit branding */
        .stToolbar, .stDeployButton, #MainMenu, footer {
            display: none !important;
        }
        
        /* Header Styles */
        .main-header {
            text-align: center;
            padding: 3rem 1rem 2rem;
            margin-bottom: 2rem;
            background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white backing for header */
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-left: 1rem;
            margin-right: 1rem;
        }
        
        .main-title {
            font-size: 3.5rem;
            font-weight: 800;
            color: #000000 !important; /* Pure black */
            margin-bottom: 0.5rem;
            letter-spacing: -0.03em;
            text-shadow: none; /* Remove shadow for cleaner look on white */
        }
        
        .main-subtitle {
            font-size: 1.2rem;
            color: #374151 !important; /* Dark gray */
            font-weight: 600;
        }
        
        /* Card Styles - Solid White */
        .result-card {
            background-color: #ffffff !important; /* Solid White */
            border: 1px solid #e5e7eb;
            padding: 2rem;
            border-radius: 16px;
            margin: 1rem 0;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); /* Stronger shadow for separation */
        }
        
        .result-card h4 {
            color: #000000 !important;
            margin-bottom: 1.5rem;
            font-weight: 700;
            font-size: 1.25rem;
            border-bottom: 2px solid #f3f4f6;
            padding-bottom: 1rem;
        }
        
        .result-card p, .result-card div, .result-card span {
            color: #000000 !important; /* Pure Black for max contrast */
            line-height: 1.6;
            font-weight: 500; /* Readable weight */
            font-size: 0.95rem; /* Slightly larger text */
        }
        
        /* Face Shape Result - Highlight */
        .face-shape-result {
            text-align: center;
            font-size: 1.75rem;
            font-weight: 800;
            color: #7c3aed !important; /* Violet text */
            background-color: #f5f3ff; /* Light violet bg */
            border: 2px solid #7c3aed;
            margin: 1.5rem 0;
            padding: 1.5rem;
            border-radius: 12px;
        }
        
        /* Alert Styles */
        .stSuccess, .stError, .stInfo {
            background-color: #ffffff !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 12px !important;
            padding: 1.25rem !important;
            color: #000000 !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            font-weight: 600 !important; /* Bold text in alerts */
        }
        
        .stSuccess { border-left: 6px solid #10b981 !important; }
        .stError { border-left: 6px solid #ef4444 !important; }
        .stInfo { border-left: 6px solid #F042FF !important; }
        
        /* Sidebar Styles */
        .stSidebar {
            background-color: #ffffff !important;
        }
        
        .stSidebar > div:first-child {
            background-color: #ffffff !important; /* Solid White Sidebar */
            border-right: 1px solid #e5e7eb;
        }
        
        .stSidebar .stMarkdown h3 {
            color: #000000 !important;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 800;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-bottom: 2px solid #F042FF;
            padding-bottom: 0.5rem;
            display: inline-block;
        }
        
        /* Form Elements - High Contrast */
        .stRadio > label, .stSelectbox > label, .stCheckbox > label, .stFileUploader > label, .stCameraInput > label {
            color: #000000 !important;
            font-weight: 800 !important; /* Extra bold labels */
            font-size: 1rem !important;
        }
        
        .stRadio div[role="radiogroup"] label {
            color: #000000 !important; /* Pure black options */
            font-weight: 600 !important;
        }
        
        /* Input Field Text Visibility Fix */
        .stTextInput input, .stSelectbox div[data-baseweb="select"] > div, .stNumberInput input, .stTextArea textarea {
            color: #000000 !important; /* Force black text inside inputs */
            background-color: #ffffff !important;
            font-weight: 600 !important;
        }
        
        /* Dropdown Menu Options */
        ul[data-baseweb="menu"] li {
            background-color: #ffffff !important;
            color: #000000 !important;
            font-weight: 600 !important;
        }
        
        /* Placeholder Text */
        ::placeholder {
            color: #6b7280 !important; /* Gray-500 for placeholders */
            opacity: 1 !important;
        }
        
        /* Button Styles */
        .stButton > button {
            background: #000000 !important; /* Black button for max contrast */
            color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.75rem 2rem !important;
            font-weight: 800 !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2) !important;
        }
        
        .stButton > button:hover {
            background: #333333 !important;
            transform: translateY(-2px) !important;
        }
        
        /* Info Box */
        .info-box {
            background-color: #f8fafc;
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            color: #000000;
            font-weight: 600; /* Bolder info text */
            border: 1px solid #cbd5e1;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        
        /* Typography Overrides */
        h1, h2, h3, h4, h5, h6 {
            color: #000000 !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        p, li, span {
            color: #000000 !important; /* Pure black for all text */
            font-weight: 500 !important;
        }
        
        /* List styling for better readability */
        ul, ol {
            color: #000000 !important;
            line-height: 1.8 !important;
        }
        
        li {
            margin-bottom: 0.5rem !important;
            color: #000000 !important;
        }
        
        /* Strong/Bold text */
        strong, b {
            color: #000000 !important;
            font-weight: 700 !important;
        }
        
        hr {
            border-color: #e5e7eb !important;
            margin: 2rem 0 !important;
        }
        
        /* Loading Spinner */
        .stSpinner > div {
            border-color: #000000 !important;
        }
        
        /* AR Selection Gallery */
        .ar-gallery-item {
            cursor: pointer;
            transition: transform 0.2s;
            border-radius: 10px;
            overflow: hidden;
            border: 2px solid transparent;
            text-align: center;
            background: white;
            padding: 5px;
        }
        
        .ar-gallery-item:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }
        
        .ar-gallery-item.selected {
            border-color: #7c3aed;
            background-color: #f5f3ff;
            box-shadow: 0 0 0 2px rgba(124, 58, 237, 0.3);
        }
        
        .ar-gallery-item img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            object-fit: cover;
        }
        
        .ar-gallery-label {
            font-size: 0.8rem;
            font-weight: 600;
            margin-top: 5px;
            color: #000000;
        }
    </style>
    """, unsafe_allow_html=True)

def render_header():
    """Render the main application header"""
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">LookMate</h1>
        <p class="main-subtitle">AI-Powered Style Analysis</p>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render the application footer"""
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; font-size: 0.9rem; font-weight: 600; background-color: rgba(255,255,255,0.9); border-radius: 10px; margin-top: 2rem;">
        <p style="color: #000000 !important; margin: 0;">LookMate v2.4 • High Contrast Edition</p>
    </div>
    """, unsafe_allow_html=True)

def get_style_recommendations_for_face_shape(face_shape, gender):
    """
    Get recommended hairstyles and beards for specific face shape
    Returns list of available overlay file names that match recommendations
    """
    recommendations = {
        "Male": {
            "Oval": {
                "hairstyles": ["pompadour", "quiff", "side_part"],
                "beards": ["full_beard", "stubble", "goatee"]
            },
            "Round": {
                "hairstyles": ["high_fade", "angular_fringe", "undercut"],
                "beards": ["chinstrap", "goatee", "van_dyke"]
            },
            "Square": {
                "hairstyles": ["textured_crop", "messy_quiff", "side_part"],
                "beards": ["full_beard", "circle_beard", "stubble"]
            },
            "Heart": {
                "hairstyles": ["side_swept", "textured_crop", "medium_layers"],
                "beards": ["full_beard", "mutton_chops", "extended_goatee"]
            },
            "Oblong": {
                "hairstyles": ["fringe", "side_part", "wavy_medium"],
                "beards": ["full_beard", "mutton_chops", "rounded_beard"]
            }
        },
        "Female": {
            "Oval": {
                "hairstyles": ["long_layers", "bob_cut", "pixie"],
                "beards": []
            },
            "Round": {
                "hairstyles": ["long_layers", "angled_bob", "high_updo"],
                "beards": []
            },
            "Square": {
                "hairstyles": ["soft_waves", "layered_long", "side_swept_bangs"],
                "beards": []
            },
            "Heart": {
                "hairstyles": ["bob_cut", "side_swept_bangs", "shoulder_curls"],
                "beards": []
            },
            "Oblong": {
                "hairstyles": ["blunt_bangs", "shoulder_waves", "layered_bob"],
                "beards": []
            }
        }
    }
    
    if gender in recommendations and face_shape in recommendations[gender]:
        return recommendations[gender][face_shape]
    
    return {"hairstyles": [], "beards": []}

