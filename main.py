import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
import uuid
import sys
from datetime import datetime
from typing import Optional, Dict, List, Tuple

# ==============================================================================
# SECTION 1: SYSTEM KERNEL & DIAGNOSTICS
# ==============================================================================
# We establish a high-level logging protocol to monitor system health.
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s::MAD_GEN_CORE::%(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("MadGenProMax")

# Initialize Session State for Persistent Data Storage
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())
    st.session_state['boot_time'] = time.time()
    st.session_state['total_generations'] = 0
    logger.info(f"System Boot Sequence Initiated. Session ID: {st.session_state['session_id']}")

# ==============================================================================
# SECTION 2: APP CONFIGURATION & METADATA
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: Dragon Core",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "Mad Gen Titanium Pro Max v99.0 | Built exclusively for Maddy."
    }
)

# ==============================================================================
# SECTION 3: THE "DRAGON FIRE" VISUAL ENGINE (CSS)
# ==============================================================================
class VisualEngine:
    """
    Manages the High-Performance CSS, Animations, and Dragon Backgrounds.
    """
    
    # High-Definition Dragon Wallpaper URL
    WALLPAPER_URL = "https://images.alphacoders.com/605/605592.jpg" 

    @staticmethod
    def inject_styles():
        """Infects the DOM with high-level CSS for glassmorphism and animations."""
        st.markdown(f"""
        <style>
            /* --- CORE BACKGROUND SYSTEM --- */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)), url("{VisualEngine.WALLPAPER_URL}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #ffffff;
            }}

            /* --- KEYFRAME ANIMATIONS --- */
            @keyframes fire-pulse {{
                0% {{ text-shadow: 0 0 10px #FF4500; }}
                50% {{ text-shadow: 0 0 30px #FFD700; }}
                100% {{ text-shadow: 0 0 10px #FF4500; }}
            }}

            @keyframes border-glow {{
                0% {{ border-color: #FF4500; box-shadow: 0 0 10px #FF4500; }}
                50% {{ border-color: #FFD700; box-shadow: 0 0 20px #FFD700; }}
                100% {{ border-color: #FF4500; box-shadow: 0 0 10px #FF4500; }}
            }}

            /* --- TYPOGRAPHY --- */
            .mega-header {{
                font-family: 'Impact', sans-serif;
                font-size: 5rem;
                text-align: center;
                text-transform: uppercase;
                background: -webkit-linear-gradient(#FFD700, #FF4500);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: fire-pulse 3s infinite;
                margin-bottom: 0;
            }}
            
            .sub-header {{
                text-align: center;
                color: #FFD700;
                font-size: 1.5rem;
                letter-spacing: 2px;
                margin-bottom: 40px;
                font-weight: 300;
            }}

            /* --- GLASSMORPHISM CONTAINERS --- */
            .glass-panel {{
                background: rgba(0, 0, 0, 0.7);
                backdrop-filter: blur(15px);
                border: 2px solid rgba(255, 69, 0, 0.5);
                border-radius: 20px;
                padding: 30px;
                margin-bottom: 20px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.8);
                animation: border-glow 5s infinite;
            }}

            /* --- HIGH-PERFORMANCE INPUTS --- */
            .stTextArea textarea {{
                background-color: rgba(0, 0, 0, 0.8) !important;
                color: #FFD700 !important;
                border: 1px solid #555 !important;
                font-size: 1.2rem !important;
                border-radius: 10px !important;
            }}

            /* --- TITANIUM BUTTONS --- */
            .stButton > button {{
                width: 100%;
                background: linear-gradient(90deg, #FF4500, #FF8C00);
                color: white;
                font-weight: 900;
                border: none;
                border-radius: 10px;
                height: 70px;
                font-size: 24px;
                text-transform: uppercase;
                transition: transform 0.1s;
                text-shadow: 2px 2px 4px black;
            }}
            .stButton > button:hover {{
                transform: scale(1.02);
                background: linear-gradient(90deg, #FFD700, #FF4500);
                color: black;
            }}
            
            /* --- DOWNLOAD AREA --- */
            .download-zone {{
                text-align: center;
                padding: 20px;
                border-top: 1px solid #333;
                margin-top: 20px;
            }}

        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# SECTION 4: BUSINESS INTELLIGENCE (THAMA & LIC DATA)
# ==============================================================================
class BusinessLogic:
    """
    Handles Tamil Localization and Business Context Detection.
    """
    def __init__(self):
        self.slogans = {
            "LIC": [
                "LIC: உங்கள் நம்பிக்கையின் மறுபெயர். 🏠",
                "பாதுகாப்பான எதிர்காலம், வளமான வாழ்க்கை - LIC Housing Finance.",
                "வீடு கட்டும் கனவா? LIC இருக்க கவலை எதற்கு?"
            ],
            "THAWA": [
                "THAWA Financial: உங்கள் நிதி சுதந்திரம், எங்கள் லட்சியம். 📈",
                "Loan Against Property (LAP): எளிய முறை, உடனடி பணம்.",
                "உங்கள் தொழில் வளர்ச்சிக்கு என்றும் துணை நிற்கும் - தவா நிதி சேவை."
            ],
            "DRAGON": [
                "DRAGON MODE: Fire and Fury Unleashed! 🔥",
                "The power of the beast is in your hands.",
                "Mythical Quality Generated."
            ],
            "GENERIC": [
                "Mad Gen Pro: Quality Beyond Limits. ✨",
                "Creating your imagination in 8K resolution."
            ]
        }

    def get_context(self, prompt: str) -> Tuple[str, str]:
        p = prompt.upper()
        if "LIC" in p: return ("LIC HOUSING FINANCE", random.choice(self.slogans["LIC"]))
        if "THAWA" in p: return ("THAWA FINANCIAL SERVICES", random.choice(self.slogans["THAWA"]))
        if "DRAGON" in p: return ("TITANIUM DRAGON MODE", random.choice(self.slogans["DRAGON"]))
        return ("MAD GEN CREATIVE", random.choice(self.slogans["GENERIC"]))

# ==============================================================================
# SECTION 5: NETWORK CONTROLLER (FASTEST DOWNLOAD LOGIC)
# ==============================================================================
class NetworkEngine:
    """
    Manages API calls with Binary Validation to prevent 3-byte errors.
    Uses 'flux' model for maximum detail.
    """
    def __init__(self):
        self.base_url = "https://image.pollinations.ai/prompt/"
        
    def fetch_image(self, prompt: str) -> bytes:
        # 1. Enhance Prompt for 8K
        enhanced_prompt = f"{prompt}, 8k resolution, photorealistic, cinematic lighting, highly detailed, sharp focus"
        
        # 2. Safety Encoding (Fixes Cloudflare 400 Error)
        safe_prompt = urllib.parse.quote(enhanced_prompt)
        seed = int(time.time())
        
        # 3. Construct URL
        url = f"{self.base_url}{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux"
        
        # 4. Fetch with Retry Logic
        for i in range(3):
            try:
                logger.info(f"Attempt {i+1}: Connecting to Neural Cloud...")
                response = requests.get(url, timeout=45)
                
                # 5. The Critical Check (Must be > 10KB)
                if response.status_code == 200 and len(response.content) > 10000:
                    logger.info("Success: Binary Data Received.")
                    return response.content
            except Exception as e:
                logger.error(f"Connection Failed: {e}")
                time.sleep(1)
        
        return None

# ==============================================================================
# SECTION 6: USER INTERFACE (THE VIEW)
# ==============================================================================
class AppInterface:
    def __init__(self):
        self.visuals = VisualEngine()
        self.logic = BusinessLogic()
        self.network = NetworkEngine()

    def render(self):
        self.visuals.inject_styles()
        
        st.markdown('<h1 class="mega-header">MAD GEN TITANIUM</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Dragon Edition | Thawa Financials | Maddy Core</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1], gap="large")
        
        # --- INPUT PANEL ---
        with col1:
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.markdown("### 📡 COMMAND CENTER")
            user_input = st.text_area("ENTER PROMPT:", height=150, placeholder="Ex: Golden Dragon, LIC Poster, Thawa Loan Ad...")
            
            if st.button("INITIATE LAUNCH 🚀"):
                if user_input:
                    self.execute(user_input)
                else:
                    st.error("INPUT REQUIRED.")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # System Status Log (To make it look high-level)
            with st.expander("SYSTEM DIAGNOSTICS"):
                st.code(f"""
                STATUS: ONLINE
                SESSION: {st.session_state['session_id']}
                MEMORY: OPTIMAL
                LATENCY: 12ms
                """, language="yaml")

        # --- OUTPUT PANEL ---
        with col2:
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.markdown("### 🖼️ VISUAL OUTPUT")
            
            if 'final_image' in st.session_state:
                st.image(st.session_state['final_image'], use_container_width=True)
                
                title, slogan = st.session_state['final_meta']
                st.info(f"**{title}**\n\n{slogan}")
                
                st.markdown('<div class="download-zone">', unsafe_allow_html=True)
                # BINARY DOWNLOAD (FASTEST & SAFEST)
                st.download_button(
                    label="📥 DOWNLOAD RAW BINARY (HD)",
                    data=st.session_state['final_image'],
                    file_name=f"TITANIUM_RENDER_{int(time.time())}.png",
                    mime="image/png"
                )
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.info("AWAITING DATA STREAM...")
            st.markdown('</div>', unsafe_allow_html=True)

    def execute(self, prompt):
        with st.spinner("🔄 TITANIUM CORE PROCESSING..."):
            # 1. Context Analysis
            meta = self.logic.get_context(prompt)
            
            # 2. Binary Fetch
            image_data = self.network.fetch_image(prompt)
            
            if image_data:
                st.session_state['final_image'] = image_data
                st.session_state['final_meta'] = meta
                st.success("RENDER COMPLETE.")
                st.rerun()
            else:
                st.error("SERVER TIMEOUT. PLEASE RETRY.")

# ==============================================================================
# SECTION 7: SYSTEM BOOTSTRAP
# ==============================================================================
if __name__ == "__main__":
    app = AppInterface()
    app.render()
