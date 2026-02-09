import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import base64
import time

# --- APP CONFIG & THEME ---
st.set_page_config(
    page_title="Mad Gen AI | Ultra Professional",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS Styling for Maddy
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
        background: -webkit-linear-gradient(#FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5rem;
        background: linear-gradient(to right, #FF416C, #FF4B2B);
        border: none;
        color: white;
        font-weight: bold;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 65, 108, 0.6);
    }
    .info-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR SETTINGS ---
with st.sidebar:
    st.image("https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d473530393318e422bb7.svg", width=100)
    st.title("Mad Gen Settings")
    st.info("Maddy, ippo inbuilt logic-la images 100% download aagum.")
    
    aspect_ratio = st.selectbox("Select Dimension:", ["1:1 (Square)", "16:9 (Cinematic)", "9:16 (Story)"])
    if aspect_ratio == "1:1 (Square)":
        width, height = 1024, 1024
    elif aspect_ratio == "16:9 (Cinematic)":
        width, height = 1920, 1080
    else:
        width, height = 1080, 1920

# --- MAIN UI ---
st.markdown('<h1 class="main-title">🔥 MAD GEN: ULTRA HQ ENGINE</h1>', unsafe_allow_html=True)
st.write("<p style='text-align:center;'>World-class creative engine for Wallpapers & Marketing Posters</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)
    st.subheader("💡 Your Creative Vision")
    user_input = st.text_area("Enna design venum? (Eg: 8k Roman Reigns wallpaper, Cinematic Car...)", 
                              placeholder="Describe your idea in detail for better quality...", height=150)
    
    style = st.select_slider("Artistic Style:", options=["Hyper-Realistic", "Cinematic", "3D Render", "Epic Poster", "Anime Style"])
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Mad Gen, Magic Pannu! ✨"):
        if user_input:
            with st.spinner("AI is crafting your masterpiece... Please wait."):
                # INBUILT PROMPT ENGINEERING
                final_prompt = f"{user_input}, {style}, professional color grading, ultra-detailed 8k resolution, cinematic lighting, sharp focus, digital art masterpiece"
                
                # Fetching Logic with Quality Headers
                img_url = f"https://pollinations.ai/p/{final_prompt.replace(' ', '%20')}?width={width}&height={height}&seed={int(time.time())}&model=flux"
                
                try:
                    response = requests.get(img_url, timeout=60)
                    if response.status_code == 200:
                        # VALIDATING IMAGE DATA
                        img_bytes = response.content
                        if len(img_bytes) > 1000: # Ensuring it's not a 3-byte error
                            st.session_state['img_data'] = img_bytes
                            st.session_state['img_url'] = img_url
                            st.session_state['generated'] = True
                            st.session_state['file_name'] = f"MadGen_{int(time.time())}.png"
                        else:
                            st.error("Error: Received broken image data. Try again.")
                    else:
                        st.error(f"Server Issue (Error {response.status_code}). Please refresh.")
                except Exception as e:
                    st.error(f"Network error: {e}")
        else:
            st.warning("Input kudunga Maddy!")

with col2:
    st.subheader("🖼️ Premium Output Preview")
    if 'generated' in st.session_state and st.session_state['generated']:
        # DISPLAY IMAGE
        st.image(st.session_state['img_data'], use_column_width=True)
        
        # QUALITY CHECK INFO
        st.success(f"✅ Image Ready! Size: {len(st.session_state['img_data']) // 1024} KB")
        
        # THE ULTIMATE DOWNLOAD BUTTON
        st.download_button(
            label="📥 DOWNLOAD HD IMAGE",
            data=st.session_state['img_data'],
            file_name=st.session_state['file_name'],
            mime="image/png"
        )
    else:
        st.info("Input kuduthu Magic Pannunga Maddy! Result inga varum.")

st.divider()
st.markdown("<p style='text-align:center;'>Mad Gen AI | Powered by Maddy's Creativity 🚀</p>", unsafe_allow_html=True)
