import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
import uuid
from datetime import datetime
from typing import Optional, Tuple

# ==============================================================================
# SECTION 1: SYSTEM KERNEL & LOGGING
# ==============================================================================
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s::STRANGER_CORE::%(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("MadGenStrangerThings")

if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())
    logger.info(f"Portal Opened. Session ID: {st.session_state['session_id']}")

# ==============================================================================
# SECTION 2: APP CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: Stranger Things Edition",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# SECTION 3: THE "UPSIDE DOWN" VISUAL ENGINE (CSS)
# ==============================================================================
class StrangerThingsTheme:
    """
    Manages the 'Upside Down' aesthetic: Red Neon, Dark Monsters, Glassmorphism.
    """
    
    # High-Res Stranger Things Mind Flayer Background
    WALLPAPER_URL = "https://images.alphacoders.com/133/1330612.png" 

    @staticmethod
    def inject_darkness():
        """Infects the DOM with the Stranger Things aesthetic."""
        st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Benguiat&display=swap');

            /* --- CORE BACKGROUND: THE MIND FLAYER --- */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.4), rgba(20,0,0,0.9)), url("{StrangerThingsTheme.WALLPAPER_URL}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #ff0000;
            }}

            /* --- STRANGER THINGS ANIMATIONS --- */
            @keyframes neon-flicker {{
                0%, 19%, 21%, 23%, 25%, 54%, 56%, 100% {{
                    text-shadow: -0.2rem -0.2rem 1rem #fff, 0.2rem 0.2rem 1rem #fff, 0 0 2rem #ff00de, 0 0 4rem #ff00de, 0 0 6rem #ff00de, 0 0 8rem #ff00de, 0 0 10rem #ff00de;
                }}
                20%, 24%, 55% {{        
                    text-shadow: none;
                }}
            }}

            /* --- TYPOGRAPHY --- */
            .stranger-header {{
                font-family: 'ITC Benguiat', serif; /* The Stranger Things Font */
                font-size: 5rem;
                text-align: center;
                text-transform: uppercase;
                color: #ff0000;
                text-shadow: 0 0 10px #000, 2px 2px 0px #330000;
                letter-spacing: -2px;
                margin-top: 20px;
                border-bottom: 2px solid #ff0000;
                padding-bottom: 20px;
            }}
            
            .stranger-sub {{
                text-align: center;
                color: #fff;
                font-size: 1.2rem;
                letter-spacing: 5px;
                margin-bottom: 40px;
                text-transform: uppercase;
                opacity: 0.8;
            }}

            /* --- GLASSMORPHISM CONTAINERS --- */
            .glass-panel {{
                background: rgba(20, 0, 0, 0.7); /* Dark Red Tint */
                backdrop-filter: blur(10px);
                border: 1px solid #ff0000;
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 0 30px rgba(255, 0, 0, 0.2);
            }}

            /* --- HIGH-PERFORMANCE INPUTS --- */
            .stTextArea textarea {{
                background-color: rgba(0, 0, 0, 0.9) !important;
                color: #ff0000 !important;
                border: 1px solid #ff0000 !important;
                font-family: 'Courier New', monospace !important;
                font-size: 1.1rem !important;
            }}

            /* --- NEON BUTTONS --- */
            .stButton > button {{
                width: 100%;
                background: transparent;
                color: #ff0000;
                font-family: 'ITC Benguiat', serif;
                font-weight: 900;
                border: 2px solid #ff0000;
                border-radius: 5px;
                height: 70px;
                font-size: 24px;
                text-transform: uppercase;
                transition: all 0.3s;
                box-shadow: 0 0 10px #ff0000;
            }}
            .stButton > button:hover {{
                background: #ff0000;
                color: black;
                box-shadow: 0 0 40px #ff0000, 0 0 80px #ff0000;
            }}
            
            /* --- DOWNLOAD ZONE --- */
            .download-zone {{
                border: 1px dashed #ff0000;
                padding: 20px;
                text-align: center;
                margin-top: 20px;
                background: rgba(0,0,0,0.8);
            }}

        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# SECTION 4: BUSINESS INTELLIGENCE (THAMA & LIC)
# ==============================================================================
class BusinessLogic:
    """
    Handles Tamil Localization. Detects context for LIC, Thawa, or Monsters.
    """
    def __init__(self):
        self.slogans = {
            "LIC": [
                "LIC: இருளான நேரத்திலும் ஒளி தரும் விளக்கு. 🏠",
                "ஆபத்து காலத்தில் கைகொடுக்கும் நண்பன் - LIC Housing Finance.",
                "உங்கள் குடும்பத்தின் பாதுகாப்பு அரண்."
            ],
            "THAWA": [
                "THAWA Financial: நிதி சிக்கல்களை உடைத்தெறியுங்கள். 📈",
                "Loan Against Property (LAP): உங்கள் சொத்து, உங்கள் பலம்.",
                "வேகமான கடன், முழுமையான வெளிப்படைத்தன்மை."
            ],
            "MONSTER": [
                "THE UPSIDE DOWN: The Mind Flayer Awakes. 🕷️",
                "Demogorgon Mode: Pure Terror & Quality.",
                "Run while you can. The image is loading."
            ]
        }

    def get_context(self, prompt: str) -> Tuple[str, str]:
        p = prompt.upper()
        if "LIC" in p: return ("LIC HOUSING FINANCE", random.choice(self.slogans["LIC"]))
        if "THAWA" in p: return ("THAWA FINANCIAL SERVICES", random.choice(self.slogans["THAWA"]))
        if "STRANGER" in p or "MONSTER" in p or "ANIMAL" in p: return ("STRANGER THINGS MODE", random.choice(self.slogans["MONSTER"]))
        return ("MAD GEN TITANIUM", "Creating Masterpiece in the Void...")

# ==============================================================================
# SECTION 5: NETWORK CONTROLLER (MAX FILE SIZE LOGIC)
# ==============================================================================
class NeuralNetwork:
    """
    Manages API calls with 'Raw Mode' enabled to maximize file size (MB).
    """
    def __init__(self):
        self.base_url = "https://image.pollinations.ai/prompt/"
        
    def fetch_heavy_image(self, prompt: str) -> bytes:
        # 1. Force Maximum Complexity (Increases File Size)
        # We use keywords that force the AI to add texture, noise, and detail.
        enhanced_prompt = f"{prompt}, 8k resolution, raw photo, ultra-detailed, intricate textures, noise, film grain, cinematic lighting, wide angle, uncompressed"
        
        # 2. Safety Encoding
        safe_prompt = urllib.parse.quote(enhanced_prompt)
        seed = int(time.time())
        
        # 3. URL Construction (Flux Model for Realism)
        url = f"{self.base_url}{safe_prompt}?width=1280&height=1280&seed={seed}&nologo=true&model=flux"
        
        # 4. Fetch with Retry Logic
        for i in range(3):
            try:
                logger.info(f"Attempt {i+1}: Opening Portal...")
                # Increased timeout to 90s because large files take longer
                response = requests.get(url, timeout=90)
                
                # 5. Validation (Must be valid binary)
                if response.status_code == 200 and len(response.content) > 50000:
                    file_size_mb = len(response.content) / (1024 * 1024)
                    logger.info(f"Success: Received {file_size_mb:.2f} MB")
                    return response.content
            except Exception as e:
                logger.error(f"Connection Failed: {e}")
                time.sleep(2)
        
        return None

# ==============================================================================
# SECTION 6: APP ORCHESTRATION
# ==============================================================================
class App:
    def __init__(self):
        self.visuals = StrangerThingsTheme()
        self.logic = BusinessLogic()
        self.network = NeuralNetwork()

    def run(self):
        self.visuals.inject_darkness()
        
        st.markdown('<h1 class="stranger-header">MAD GEN</h1>', unsafe_allow_html=True)
        st.markdown('<p class="stranger-sub">The Upside Down Edition | Maddy Core</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 1], gap="large")
        
        # --- INPUT PORTAL ---
        with col1:
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.markdown("### 📡 ENTER THE VOID")
            user_input = st.text_area("SUMMON ENTITY:", height=150, placeholder="Ex: Demogorgon in Chennai, Dark Monster, LIC Poster...")
            
            if st.button("OPEN PORTAL 🩸"):
                if user_input:
                    self.execute(user_input)
                else:
                    st.error("BLOOD SACRIFICE REQUIRED (Input Text).")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Simulated System Logs
            st.markdown("""
            <div style="font-family: 'Courier New'; color: #ff0000; font-size: 0.8rem; opacity: 0.7;">
            > SYSTEM: ONLINE<br>
            > DIMENSION: C-137<br>
            > THREAT LEVEL: MIDNIGHT
            </div>
            """, unsafe_allow_html=True)

        # --- OUTPUT PORTAL ---
        with col2:
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.markdown("### 🖼️ MANIFESTATION")
            
            if 'final_image' in st.session_state:
                st.image(st.session_state['final_image'], use_container_width=True)
                
                title, slogan = st.session_state['final_meta']
                st.info(f"**{title}**\n\n{slogan}")
                
                st.markdown('<div class="download-zone">', unsafe_allow_html=True)
                # BINARY DOWNLOAD (MAX QUALITY)
                st.download_button(
                    label="📥 DOWNLOAD RAW ARTIFACT (MAX MB)",
                    data=st.session_state['final_image'],
                    file_name=f"STRANGER_THINGS_{int(time.time())}.png",
                    mime="image/png"
                )
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("NO SIGNAL DETECTED.")
            st.markdown('</div>', unsafe_allow_html=True)

    def execute(self, prompt):
        with st.spinner("🔴 SUMMONING FROM THE UPSIDE DOWN..."):
            # 1. Context Analysis
            meta = self.logic.get_context(prompt)
            
            # 2. Heavy Binary Fetch
            image_data = self.network.fetch_heavy_image(prompt)
            
            if image_data:
                st.session_state['final_image'] = image_data
                st.session_state['final_meta'] = meta
                st.success("ENTITY STABILIZED.")
                st.rerun()
            else:
                st.error("CONNECTION SEVERED. RETRY.")

# ==============================================================================
# SECTION 7: INITIALIZATION
# ==============================================================================
if __name__ == "__main__":
    app = App()
    app.run()
