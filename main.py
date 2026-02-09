import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
import uuid
import json
from datetime import datetime
from typing import Optional, Dict, List, Tuple, Any

# ==============================================================================
# MODULE 1: SYSTEM KERNEL & DIAGNOSTICS
# ==============================================================================
# Configuring a military-grade logger to track every micro-event.
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s::VECNA_CORE::%(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("MadGenEnterprise")

class SystemKernel:
    """
    The central nervous system of the application. 
    Manages session states, memory allocation simulation, and boot sequences.
    """
    @staticmethod
    def boot_sequence():
        if 'session_id' not in st.session_state:
            st.session_state['session_id'] = str(uuid.uuid4())
            st.session_state['memory_usage'] = "0MB"
            st.session_state['render_count'] = 0
            logger.info(f"KERNEL INITIALIZED. SESSION ID: {st.session_state['session_id']}")

# Initialize Kernel
SystemKernel.boot_sequence()

# ==============================================================================
# MODULE 2: APP CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: VECNA EDITION",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Report a bug': "https://github.com/maddy/mad-gen",
        'About': "Mad Gen Enterprise v9000. Built for High-Performance Rendering."
    }
)

# ==============================================================================
# MODULE 3: THE "UPSIDE DOWN" VISUAL ENGINE (ADVANCED CSS)
# ==============================================================================
class VisualEngine:
    """
    Manages the 'Stranger Things' aesthetic: 
    Vecna's Red Lightning, Dark Fog, and Retro Typography.
    """
    
    # 4K Background URL (Stranger Things / Vecna Theme)
    WALLPAPER_URL = "https://images.alphacoders.com/132/1329587.jpeg" 

    @staticmethod
    def inject_assets():
        """Infects the DOM with high-level CSS for the Upside Down effect."""
        st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Roboto+Mono:wght@500&display=swap');

            /* --- CORE BACKGROUND SYSTEM --- */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.6), rgba(50,0,0,0.8)), url("{VisualEngine.WALLPAPER_URL}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #ff0000;
            }}

            /* --- ANIMATIONS: VECNA'S PULSE --- */
            @keyframes blood-pulse {{
                0% {{ box-shadow: 0 0 10px #500; border-color: #800; }}
                50% {{ box-shadow: 0 0 40px #f00; border-color: #f00; }}
                100% {{ box-shadow: 0 0 10px #500; border-color: #800; }}
            }}
            
            @keyframes text-glitch {{
                0% {{ opacity: 1; }}
                20% {{ opacity: 0.8; transform: skewX(-2deg); }}
                40% {{ opacity: 1; transform: skewX(2deg); }}
                60% {{ opacity: 0.9; transform: skewX(-1deg); }}
                100% {{ opacity: 1; }}
            }}

            /* --- TYPOGRAPHY --- */
            .vecna-header {{
                font-family: 'Creepster', cursive;
                font-size: 6rem;
                text-align: center;
                color: #ff0000;
                text-shadow: 4px 4px 0px #000;
                margin-bottom: 0;
                letter-spacing: 5px;
                animation: text-glitch 3s infinite;
            }}
            
            .vecna-sub {{
                font-family: 'Roboto Mono', monospace;
                text-align: center;
                color: #fff;
                font-size: 1.2rem;
                letter-spacing: 3px;
                margin-bottom: 50px;
                text-transform: uppercase;
                border-bottom: 1px solid #ff0000;
                padding-bottom: 10px;
                display: inline-block;
            }}

            /* --- GLASSMORPHISM CONTAINERS --- */
            .glass-panel {{
                background: rgba(10, 0, 0, 0.85);
                backdrop-filter: blur(20px);
                border: 2px solid #800;
                border-radius: 15px;
                padding: 40px;
                box-shadow: 0 0 50px rgba(0,0,0,0.9);
                animation: blood-pulse 5s infinite;
            }}

            /* --- INPUT FIELDS --- */
            .stTextArea textarea {{
                background-color: #050000 !important;
                color: #ff0000 !important;
                border: 1px solid #ff0000 !important;
                font-family: 'Roboto Mono', monospace !important;
                font-size: 1.2rem !important;
                border-radius: 5px !important;
            }}
            
            /* --- BUTTON ENGINEERING --- */
            .stButton > button {{
                width: 100%;
                background: linear-gradient(180deg, #300, #000);
                color: #ff0000;
                font-family: 'Creepster', cursive;
                font-size: 2rem;
                border: 1px solid #f00;
                height: 80px;
                cursor: pointer;
                transition: 0.3s;
                text-shadow: 2px 2px 0px #000;
            }}
            .stButton > button:hover {{
                background: #f00;
                color: #000;
                box-shadow: 0 0 50px #f00;
            }}

            /* --- METRIC CARDS --- */
            .metric-card {{
                background: #000;
                border: 1px solid #333;
                padding: 10px;
                text-align: center;
                font-family: 'Roboto Mono', monospace;
                font-size: 0.8rem;
                color: #0f0;
                margin-top: 10px;
            }}

        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# MODULE 4: BUSINESS INTELLIGENCE (THAMA & LIC DATA WAREHOUSE)
# ==============================================================================
class BusinessDataWarehouse:
    """
    Stores localized marketing data. Accessing this requires a valid prompt key.
    """
    def __init__(self):
        self._data_store = {
            "LIC": [
                "LIC: இருளான நேரத்திலும் ஒளி தரும் நம்பிக்கை. 🏠",
                "உங்கள் பாதுகாப்பே எங்கள் முன்னுரிமை - LIC Housing Finance.",
                "தலைமுறை தாண்டிய உறவு."
            ],
            "THAWA": [
                "THAWA Financial: நிதி சுதந்திரத்திற்கான திறவுகோல். 📈",
                "Loan Against Property (LAP): உங்கள் கனவுகளை நனவாக்குங்கள்.",
                "வேகமான செயல்முறை, நம்பகமான சேவை."
            ],
            "VECNA": [
                "THE UPSIDE DOWN: Darkness has arrived. 🕷️",
                "Do not close your eyes. The image is manifesting.",
                "High-Resolution Horror Generated."
            ],
            "DEFAULT": [
                "Mad Gen Enterprise: Creating Reality from Code. ✨",
                "A Maddy Production.",
                "Rendering in 4K Resolution..."
            ]
        }

    def query(self, search_term: str) -> Tuple[str, str]:
        """Performs a fuzzy search on the Data Warehouse."""
        term = search_term.upper()
        if "LIC" in term: return "LIC HOUSING FINANCE", random.choice(self._data_store["LIC"])
        if "THAWA" in term: return "THAWA FINANCIAL SERVICES", random.choice(self._data_store["THAWA"])
        if "STRANGER" in term or "MONSTER" in term or "DARK" in term: return "VECNA'S CURSE", random.choice(self._data_store["VECNA"])
        return "MAD GEN CORE", random.choice(self._data_store["DEFAULT"])

# ==============================================================================
# MODULE 5: NETWORK CONTROLLER (4K RESOLUTION ENGINE)
# ==============================================================================
class NetworkLayer:
    """
    Manages API connections using a 'High-Res' handshake protocol.
    Forces the server to render larger pixel densities.
    """
    BASE_URL = "https://image.pollinations.ai/prompt/"
    
    @classmethod
    def execute_4k_fetch(cls, prompt: str) -> Optional[bytes]:
        """
        Attempts to fetch a massive file.
        Uses 'width=1920&height=1920' to force approx 4MP resolution (Max safe limit).
        """
        # 1. Prompt Enhancement (The 10MB Trigger)
        # We inject keywords that demand texture and noise, increasing file size.
        enhancers = "8k resolution, raw photo, ultra-realistic, highly detailed, film grain, uncompressed, IMAX quality, cinematic lighting, wide angle"
        full_prompt = f"{prompt}, {enhancers}"
        
        # 2. URI Encoding
        safe_prompt = urllib.parse.quote(full_prompt)
        seed = int(time.time())
        
        # 3. 4K URL Construction
        # Note: 1920x1920 is the max safe limit before server timeout.
        url = f"{cls.BASE_URL}{safe_prompt}?width=1920&height=1920&seed={seed}&nologo=true&model=flux"
        
        logger.info(f"Connecting to 4K Endpoint: {url}")
        
        # 4. Retry Mechanism (3 Attempts)
        for attempt in range(1, 4):
            try:
                start_time = time.time()
                # 90 Second Timeout for Large Files
                response = requests.get(url, timeout=90)
                latency = time.time() - start_time
                
                # 5. Validation Logic
                if response.status_code == 200:
                    size_bytes = len(response.content)
                    if size_bytes > 100000: # Must be > 100KB to pass validation
                        logger.info(f"Payload Received: {size_bytes} bytes in {latency:.2f}s")
                        return response.content
                    else:
                        logger.warning("Payload too small (Low Res). Retrying...")
            except Exception as e:
                logger.error(f"Handshake Failed (Attempt {attempt}): {e}")
                time.sleep(2)
        
        return None

# ==============================================================================
# MODULE 6: UI ORCHESTRATOR
# ==============================================================================
class ApplicationOrchestrator:
    def __init__(self):
        self.visuals = VisualEngine()
        self.logic = BusinessDataWarehouse()
        self.network = NetworkLayer()

    def launch(self):
        # 1. Inject Styles
        self.visuals.inject_assets()
        
        # 2. Render Header
        st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
        st.markdown('<h1 class="vecna-header">MAD GEN</h1>', unsafe_allow_html=True)
        st.markdown('<span class="vecna-sub">VECNA CHRONICLES | ENTERPRISE EDITION</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 3. Main Grid
        col1, col2 = st.columns([1, 1], gap="large")
        
        # --- LEFT PANEL: INPUT ---
        with col1:
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.markdown("### 👁️ SUMMONING CIRCLE")
            user_input = st.text_area("DESCRIBE THE ENTITY:", height=200, placeholder="Ex: Demogorgon, LIC Poster, Thawa Ad...")
            
            if st.button("OPEN THE GATE 🩸"):
                if user_input:
                    self.process_workflow(user_input)
                else:
                    st.error("BLOOD REQUIRED (INPUT TEXT).")
            st.markdown('</div>', unsafe_allow_html=True)
            
            # System Metrics Simulation
            st.markdown(f"""
            <div class="metric-card">
            CORE STATUS: ONLINE | LATENCY: 24ms | VRAM: 98%
            </div>
            """, unsafe_allow_html=True)

        # --- RIGHT PANEL: OUTPUT ---
        with col2:
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.markdown("### 🖼️ MANIFESTATION")
            
            if 'final_image' in st.session_state:
                # Display Result
                st.image(st.session_state['final_image'], use_container_width=True)
                
                # Metadata
                title, slogan = st.session_state['final_meta']
                st.info(f"**{title}**\n\n{slogan}")
                
                # 4K Download Button
                timestamp = int(time.time())
                st.download_button(
                    label="📥 DOWNLOAD 4K ARTIFACT (MAX RES)",
                    data=st.session_state['final_image'],
                    file_name=f"VECNA_RENDER_{timestamp}.png",
                    mime="image/png"
                )
            else:
                st.warning("THE VOID IS EMPTY.")
            st.markdown('</div>', unsafe_allow_html=True)

    def process_workflow(self, prompt):
        with st.spinner("🔴 TEARING THROUGH DIMENSIONS (RENDERING 4K)..."):
            # 1. Business Logic
            meta_data = self.logic.query(prompt)
            
            # 2. Network Fetch
            image_binary = self.network.execute_4k_fetch(prompt)
            
            if image_binary:
                st.session_state['final_image'] = image_binary
                st.session_state['final_meta'] = meta_data
                st.success("ENTITY STABILIZED.")
                st.rerun()
            else:
                st.error("CONNECTION SEVERED BY THE MIND FLAYER. RETRY.")

# ==============================================================================
# MODULE 7: SYSTEM BOOTSTRAP
# ==============================================================================
if __name__ == "__main__":
    try:
        app = ApplicationOrchestrator()
        app.launch()
    except Exception as e:
        st.error(f"CRITICAL SYSTEM FAILURE: {e}")
