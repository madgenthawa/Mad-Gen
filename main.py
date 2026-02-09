import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
import uuid
from datetime import datetime

# ==============================================================================
# 1. SYSTEM KERNEL CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: Omega",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure High-Level Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("MadGenOmega")

if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())
    st.session_state['history'] = []

# ==============================================================================
# 2. VISUAL ENGINE (STRANGER THINGS THEME)
# ==============================================================================
class Visuals:
    WALLPAPER = "https://images.alphacoders.com/132/1329587.jpeg" # Vecna Background

    @staticmethod
    def inject():
        st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Roboto+Mono:wght@500&display=swap');
            
            /* GLOBAL THEME */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.8), rgba(20,0,0,0.9)), url("{Visuals.WALLPAPER}");
                background-size: cover;
                background-attachment: fixed;
                color: #ff0000;
            }}
            
            /* HEADER STYLING */
            .omega-title {{
                font-family: 'Creepster', cursive;
                font-size: 5rem;
                text-align: center;
                color: #ff0000;
                text-shadow: 0 0 20px #000, 2px 2px 0px #500;
                margin-bottom: 0;
            }}
            
            /* INPUT BOX STYLING (The requested polish) */
            .stTextArea textarea {{
                background-color: #000 !important;
                color: #ff0000 !important;
                font-family: 'Roboto Mono', monospace !important;
                border: 2px solid #800 !important;
                border-radius: 10px !important;
                box-shadow: inset 0 0 20px #300 !important;
            }}
            .stTextArea textarea:focus {{
                border-color: #f00 !important;
                box-shadow: 0 0 30px #f00 !important;
            }}
            
            /* BUTTONS */
            .stButton > button {{
                background: #000;
                color: #f00;
                border: 2px solid #f00;
                font-family: 'Creepster', cursive;
                font-size: 1.5rem;
                height: 60px;
                width: 100%;
                transition: 0.3s;
            }}
            .stButton > button:hover {{
                background: #f00;
                color: #000;
                box-shadow: 0 0 40px #f00;
            }}
            
            /* DOWNLOAD ZONE */
            .download-box {{
                border: 1px dashed #f00;
                padding: 20px;
                text-align: center;
                background: rgba(0,0,0,0.8);
                border-radius: 10px;
                margin-top: 20px;
            }}
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# 3. BUSINESS LOGIC (LIC & THAWA)
# ==============================================================================
class Brain:
    @staticmethod
    def get_slogan(prompt):
        p = prompt.upper()
        if "LIC" in p:
            return "LIC HOUSING FINANCE", "பாதுகாப்பான எதிர்காலம், வளமான வாழ்க்கை. 🏠"
        elif "THAWA" in p:
            return "THAWA FINANCIAL SERVICES", "நிதி சிக்கல்களை உடைத்தெறியுங்கள் (LAP Specialist). 📈"
        elif "STRANGER" in p or "MONSTER" in p:
            return "HELLFIRE CLUB", "Vecna is watching. 🩸"
        else:
            return "MAD GEN OMEGA", "Creating Masterpiece from the Void... ✨"

# ==============================================================================
# 4. NETWORK ENGINE (BINARY DOWNLOADER)
# ==============================================================================
class Network:
    @staticmethod
    def fetch(prompt):
        # Enhance for 8K quality
        enhanced = f"{prompt}, 8k resolution, raw photo, cinematic lighting, ultra detailed, uncompressed"
        safe_prompt = urllib.parse.quote(enhanced)
        seed = int(time.time())
        url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux"
        
        try:
            # 60 Second Timeout
            r = requests.get(url, timeout=60)
            if r.status_code == 200 and len(r.content) > 50000: # Check > 50KB
                return r.content
        except Exception as e:
            return None
        return None

# ==============================================================================
# 5. MAIN APPLICATION LOOP
# ==============================================================================
def main():
    Visuals.inject()
    
    # Header
    st.markdown('<h1 class="omega-title">MAD GEN</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#fff; letter-spacing:3px;">OMEGA EDITION | MADDY CORE</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    # --- INPUT SECTION ---
    with col1:
        st.markdown("### 👁️ SUMMONING PORTAL")
        user_input = st.text_area("DESCRIBE ENTITY:", height=150, placeholder="Ex: Demogorgon, LIC Poster, Thawa Ad...")
        
        if st.button("OPEN GATE 🩸"):
            if user_input:
                with st.spinner("🔴 CONNECTING TO UPSIDE DOWN..."):
                    data = Network.fetch(user_input)
                    if data:
                        # Save to history
                        st.session_state['history'].append(user_input)
                        # Save Image
                        st.session_state['final_image'] = data
                        # Save Meta
                        st.session_state['final_meta'] = Brain.get_slogan(user_input)
                        st.success("ENTITY STABILIZED.")
                        st.rerun()
                    else:
                        st.error("CONNECTION FAILED. RETRY.")
            else:
                st.warning("BLOOD (INPUT) REQUIRED.")
                
        # Sidebar History
        with st.sidebar:
            st.markdown("## 📜 HISTORY")
            for h in reversed(st.session_state['history'][-5:]):
                st.caption(f"• {h}")

    # --- OUTPUT SECTION ---
    with col2:
        st.markdown("### 🖼️ MANIFESTATION")
        if 'final_image' in st.session_state:
            st.image(st.session_state['final_image'], use_container_width=True)
            
            title, slogan = st.session_state['final_meta']
            st.info(f"**{title}**\n\n{slogan}")
            
            st.markdown('<div class="download-box">', unsafe_allow_html=True)
            st.download_button(
                label="📥 DOWNLOAD HD ARTIFACT",
                data=st.session_state['final_image'],
                file_name=f"OMEGA_RENDER_{int(time.time())}.png",
                mime="image/png"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("THE VOID IS EMPTY.")

if __name__ == "__main__":
    main()
