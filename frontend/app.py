import streamlit as st
import requests

st.set_page_config(page_title="Melanoma Detection", layout="centered", page_icon="🧬")

# Custom CSS for a premium look
st.markdown("""
<style>
    /* Import modern typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Gradient Header */
    .main-header {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }

    /* Subheader text */
    .sub-header {
        text-align: center;
        color: #888;
        font-weight: 300;
        margin-top: -10px;
        margin-bottom: 40px;
    }

    /* St.Button hover effect */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        background: #4ECDC4;
        color: white;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(78, 205, 196, 0.4);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(78, 205, 196, 0.6);
        background: #45b7b0;
        color: white;
    }

    /* Hide default Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Melanoma Detection</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Upload a dermoscopic image for intelligent AI classification.</p>', unsafe_allow_html=True)

# Create a sleek container for the uploader
with st.container():
    uploaded_file = st.file_uploader("Upload Skin Lesion Image", type=["jpg", "png", "jpeg"], label_visibility="collapsed")

if uploaded_file is not None:
    # Use columns to center the image beautifully
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(uploaded_file, caption="Analyzed Specimen", use_column_width=True)
    
    st.write("")
    
    if st.button("Generate Diagnostic Report"):
        with st.spinner("AI is analyzing the cellular structure..."):
            try:
                response = requests.post("http://localhost:5050/api/predict")
                
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"🔍 **Prediction Output:** {data.get('prediction', 'Unknown')}")
                    st.info(f"💡 **System:** {data.get('message', '')}")
                else:
                    st.error(f"Error from backend API: {response.status_code}")
            except Exception as e:
                st.error(f"Failed to connect to Neural Network Backend: {e}")
