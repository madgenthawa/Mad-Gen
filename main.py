import streamlit as st
import requests
import urllib.parse
import time

# --- 1. PROFESSIONAL UI CONFIG ---
st.set_page_config(page_title="Mad Gen Nano Pro", page_icon="🍌", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .main-header { 
        font-size: 3.5rem; font-weight: 900; text-align: center;
        background: -webkit-linear-gradient(#FFE000, #FFA500);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .stButton>button { 
        background: linear-gradient(45deg, #FFD700, #FFA500); 
        color: black; border-radius: 30px; font-weight: bold; height: 4em; width: 100%;
        border: none; box-shadow: 0 4px 15px rgba(255,215,0,0.3);
    }
    .download-section {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px; border-radius: 20px; text-align: center;
        border: 1px dashed #FFD700;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. NATIVE BINARY STREAMING LOGIC ---
def get_pro_image(prompt):
    # URI Encoding ensures characters don't break the connection
    safe_prompt = urllib.parse.quote(f"{prompt}, ultra-realistic, 8k, cinematic lighting, masterpiece")
    seed = int(time.time())
    
    # We use multiple high-capacity endpoints to bypass "Anonymous Tier" limits
    endpoints = [
        f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux",
        f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&seed={seed}&model=turbo"
    ]
    
    for url in endpoints:
        try:
            # Setting a long timeout for high-res data
            response = requests.get(url, timeout=60)
            # Validation: Must be a real image larger than 50KB
            if response.status_code == 200 and len(response.content) > 50000:
                return response.content
        except:
            continue
    return None

# --- 3. MAIN INTERFACE ---
st.markdown('<h1 class="main-header">🍌 MAD GEN: NANO PRO</h1>', unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Professional Gemini-Based Engine for Wallpapers & Marketing</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("🚀 Create Your Masterpiece")
    user_input = st.text_area("Describe anything (Dragon, LIC Poster, Thawa Financial...):", 
                              placeholder="Type your idea for a high-quality image...", height=180)
    
    if st.button("Generate Nano Magic ✨"):
        if user_input:
            with st.spinner("Nano Engine is fetching raw binary data... Please wait."):
                img_data = get_pro_image(user_input)
                
                if img_data:
                    st.session_state['img_data'] = img_data
                    st.session_state['generated'] = True
                else:
                    st.error("Maddy, the external server is heavily overloaded. Please wait 10
