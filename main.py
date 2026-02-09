import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
import uuid
import sys
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageEnhance
from typing import Optional, Dict, List, Tuple, Any, Union
from dataclasses import dataclass

# ==============================================================================
# MODULE 1: SYSTEM KERNEL & ADVANCED LOGGING PROTOCOLS
# ==============================================================================
# We configure a custom logging format to track millisecond-level events.
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s::MAD_GEN_TITAN::%(module)s::%(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("MadGenTitan")

@dataclass
class AppConfig:
    """Configuration Data Class for System Constants."""
    APP_NAME: str = "Mad Gen: Titan Edition"
    VERSION: str = "100.0.1"
    THEME_COLOR: str = "#ff0000"
    WALLPAPER_URL: str = "https://images.alphacoders.com/132/1329587.jpeg"
    TIMEOUT_SECONDS: int = 60

# Initialize Page Configuration immediately
st.set_page_config(
    page_title=AppConfig.APP_NAME,
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={'About': f"{AppConfig.APP_NAME} v{AppConfig.VERSION}"}
)

# ==============================================================================
# MODULE 2: SESSION STATE MANAGER (MEMORY CONTROLLER)
# ==============================================================================
class SessionManager:
    """
    Manages the application's persistent memory state across re-runs.
    Ensures user history and configuration settings are saved.
    """
    @staticmethod
    def initialize():
        """Bootstraps the session state variables if they are missing."""
        defaults = {
            'session_id': str(uuid.uuid4()),
            'boot_time': datetime.now().strftime("%H:%M:%S"),
            'history': [],
            'user_agent_seed': random.randint(1000, 9999),
            'generated_count': 0,
            'last_prompt': ""
        }
        
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value
                logger.info(f"Initialized Session Key: {key}")

# Boot the Session Manager
SessionManager.initialize()

# ==============================================================================
# MODULE 3: VISUAL ENGINE (HELLFIRE CSS INJECTION)
# ==============================================================================
class VisualEngine:
    """
    Responsible for injecting High-Level CSS to transform the UI 
    into the 'Stranger Things' aesthetic (Red/Black/Neon).
    """
    @staticmethod
    def deploy_styles():
        st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Roboto+Mono:wght@500&display=swap');

            /* --- GLOBAL ATMOSPHERE --- */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.85), rgba(20,0,0,0.95)), url("{AppConfig.WALLPAPER_URL}");
                background-size: cover;
                background-attachment: fixed;
                color: #ff0000;
            }}

            /* --- TITAN HEADER --- */
            .titan-header {{
                font-family: 'Creepster', cursive;
                font-size: 5.5rem;
                text-align: center;
                color: #ff0000;
                text-shadow: 0 0 20px #000, 4px 4px 0px #500;
                margin-bottom: 10px;
                animation: pulse 4s infinite;
            }}
            
            @keyframes pulse {{
                0% {{ text-shadow: 0 0 10px #500; }}
                50% {{ text-shadow: 0 0 30px #f00; }}
                100% {{ text-shadow: 0 0 10px #500; }}
            }}

            /* --- HIGH-LEVEL INPUT BOX --- */
            .stTextArea textarea {{
                background-color: #050505 !important;
                color: #ff3333 !important;
                border: 2px solid #800 !important;
                font-family: 'Roboto Mono', monospace !important;
                font-size: 1.1rem !important;
                border-radius: 8px !important;
                padding: 20px !important;
                box-shadow: inset 0 0 40px #200 !important;
                transition: all 0.3s ease;
            }}
            
            .stTextArea textarea:focus {{
                border-color: #f00 !important;
                box-shadow: 0 0 20px #f00, inset 0 0 10px #f00 !important;
            }}

            /* --- SIDEBAR STYLING --- */
            [data-testid="stSidebar"] {{
                background-color: rgba(5, 0, 0, 0.95);
                border-right: 2px solid #500;
            }}
            
            /* --- ACTION BUTTONS --- */
            .stButton > button {{
                width: 100%;
                background: linear-gradient(180deg, #400, #000);
                color: #fff;
                font-family: 'Creepster', cursive;
                font-size: 1.8rem;
                border: 2px solid #f00;
                height: 70px;
                cursor: pointer;
                transition: 0.3s;
                text-transform: uppercase;
            }}
            .stButton > button:hover {{
                background: #f00;
                color: #000;
                box-shadow: 0 0 50px #f00;
            }}

            /* --- GLASS PANELS --- */
            .glass-panel {{
                background: rgba(0, 0, 0, 0.7);
                backdrop-filter: blur(10px);
                border: 1px solid #500;
                border-radius: 15px;
                padding: 25px;
                margin-bottom: 20px;
            }}
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# MODULE 4: PROMPT ENGINEERING CORTEX (LOGIC CONTROLLER)
# ==============================================================================
class PromptCortex:
    """
    Advanced Logic to detect business context (LIC/Thawa) vs Fantasy context.
    Expands simple user inputs into 'God Tier' prompts.
    """
    BUSINESS_LOGIC = {
        "LIC": ("LIC HOUSING FINANCE", "பாதுகாப்பான எதிர்காலம். 🏠"),
        "THAWA": ("THAWA FINANCIAL SERVICES", "நிதி சிக்கல்களை உடைத்தெறியுங்கள். 📈"),
        "LOAN": ("FINANCIAL SERVICES", "Low Interest. High Trust."),
    }
    
    FANTASY_LOGIC = {
        "DRAGON": ("MYTHICAL REALM", "Unreal Engine 5 Render."),
        "STRANGER": ("THE UPSIDE DOWN", "Vecna is Watching."),
        "MONSTER": ("HORROR CORE", "Cinematic Lighting.")
    }

    @classmethod
    def analyze(cls, prompt: str) -> Tuple[str, str, str]:
        """
        Analyzes the prompt and returns: (Enhanced Prompt, Category Title, Slogan)
        """
        p_upper = prompt.upper()
        
        # 1. Check Business Logic
        for key, (title, slogan) in cls.BUSINESS_LOGIC.items():
            if key in p_upper:
                enhanced = f"{prompt}, corporate billboard style, 8k resolution, professional photography, warm lighting, trustworthy, high detailed, commercial quality"
                return enhanced, title, slogan
                
        # 2. Check Fantasy Logic
        for key, (title, slogan) in cls.FANTASY_LOGIC.items():
            if key in p_upper:
                enhanced = f"{prompt}, dark atmosphere, red lightning, cinematic composition, volumetric fog, hyper-realistic, 8k, raw photo, film grain"
                return enhanced, title, slogan
                
        # 3. Default Logic
        return f"{prompt}, award winning photography, 8k, masterpiece, sharp focus", "MAD GEN TITAN", "Creating Reality from Code."

# ==============================================================================
# MODULE 5: STEALTH NETWORK TRANSPORT (ANTI-BAN SYSTEM)
# ==============================================================================
class StealthTransport:
    """
    Handles API communication using User-Agent rotation and Model switching.
    Designed to bypass 'Rate Limit' errors.
    """
    BASE_URL = "https://image.pollinations.ai/prompt/"
    
    @staticmethod
    def get_headers() -> Dict[str, str]:
        """Spoofs a legitimate browser request."""
        return {
            "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.{st.session_state['user_agent_seed']} Safari/537.36",
            "Referer": "https://www.google.com/"
        }

    @classmethod
    def fetch_image(cls, prompt: str, model: str = "flux") -> Optional[bytes]:
        """
        Fetches image data with robust error handling and model fallback.
        """
        encoded_prompt = urllib.parse.quote(prompt)
        seed = int(time.time())
        
        # Strategy List for Redundancy
        strategies = [
            f"{cls.BASE_URL}{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model={model}",
            f"{cls.BASE_URL}{encoded_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=turbo", # Fallback 1
            f"{cls.BASE_URL}{encoded_prompt}?width=1024&height=1024&seed={seed+100}&nologo=true" # Fallback 2
        ]
        
        for url in strategies:
            try:
                # Artificial Delay to prevent spam detection
                time.sleep(0.5)
                
                logger.info(f"Connecting to Neural Cloud: {url}")
                response = requests.get(url, headers=cls.get_headers(), timeout=AppConfig.TIMEOUT_SECONDS)
                
                if response.status_code == 200 and len(response.content) > 50000:
                    return response.content
                elif response.status_code == 429:
                    logger.warning("Rate Limit Detected. Switching Strategy...")
                    continue
                    
            except Exception as e:
                logger.error(f"Transport Failure: {e}")
                
        return None

# ==============================================================================
# MODULE 6: UI COMPONENT FACTORY (DASHBOARD & WIDGETS)
# ==============================================================================
class UIComponentFactory:
    """
    Generates UI components like Sidebars, Metrics, and History logs.
    """
    @staticmethod
    def render_sidebar():
        with st.sidebar:
            st.markdown("## ⚙️ TITAN CONTROLS")
            st.divider()
            
            # Advanced Settings
            model_choice = st.selectbox("Neural Model:", ["flux", "turbo", "unity"], index=0)
            st.caption("Flux = Max Quality | Turbo = Max Speed")
            
            st.divider()
            st.markdown("### 📜 SUMMONING HISTORY")
            
            if st.session_state['history']:
                for item in reversed(st.session_state['history'][-5:]):
                    st.text(f"• {item[:30]}...")
                
                if st.button("Clear Memory"):
                    st.session_state['history'] = []
                    st.rerun()
            else:
                st.caption("Memory Empty.")
                
            st.divider()
            st.caption(f"Session ID: {st.session_state['session_id'][:8]}")
            
            return model_choice

# ==============================================================================
# MODULE 7: MAIN APPLICATION ORCHESTRATOR
# ==============================================================================
class TitanApp:
    def __init__(self):
        self.visuals = VisualEngine()
        self.network = StealthTransport()
        self.cortex = PromptCortex()
        self.ui = UIComponentFactory()

    def launch(self):
        # 1. Inject Theme
        self.visuals.deploy_styles()
        
        # 2. Render Header
        st.markdown('<h1 class="titan-header">MAD GEN: TITAN</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center; color:#ccc; letter-spacing:4px;">ENTERPRISE EDITION v100.0 | MADDY CORE</p>', unsafe_allow_html=True)
        
        # 3. Render Sidebar & Get Settings
        selected_model = self.ui.render_sidebar()
        
        # 4. Main Grid Layout
        col1, col2 = st.columns([1, 1], gap="large")
        
        # --- INPUT SECTOR ---
        with col1:
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.markdown("### 👁️ INPUT TERMINAL")
            user_input = st.text_area("ENTER VISUAL PARAMETERS:", height=180, placeholder="Ex: Golden Dragon, LIC Poster, Thawa Ad...")
            
            if st.button("EXECUTE PROTOCOL 🩸"):
                if user_input:
                    self.execute_workflow(user_input, selected_model)
                else:
                    st.warning("INPUT REQUIRED.")
            st.markdown('</div>', unsafe_allow_html=True)

        # --- OUTPUT SECTOR ---
        with col2:
            st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
            st.markdown("### 🖼️ VISUAL OUTPUT")
            
            if 'titan_image' in st.session_state:
                st.image(st.session_state['titan_image'], use_container_width=True)
                
                title, slogan = st.session_state['titan_meta']
                st.info(f"**{title}**\n\n{slogan}")
                
                # High-Res Download Logic
                st.download_button(
                    label="📥 DOWNLOAD TITAN ARTIFACT (HD)",
                    data=st.session_state['titan_image'],
                    file_name=f"TITAN_{int(time.time())}.png",
                    mime="image/png"
                )
            else:
                st.info("SYSTEM STANDBY. AWAITING INPUT.")
            st.markdown('</div>', unsafe_allow_html=True)

    def execute_workflow(self, prompt, model):
        with st.spinner("🔴 TITAN CORE PROCESSING..."):
            # 1. Analyze and Enhance Prompt
            enhanced, title, slogan = self.cortex.analyze(prompt)
            st.toast(f"Logic Detected: {title}", icon="🧠")
            
            # 2. Fetch Image (Stealth Mode)
            image_bytes = self.network.fetch_image(enhanced, model)
            
            # 3. Update State
            if image_bytes:
                st.session_state['titan_image'] = image_bytes
                st.session_state['titan_meta'] = (title, slogan)
                st.session_state['history'].append(prompt)
                st.success("GENERATION COMPLETE.")
                st.rerun()
            else:
                st.error("NETWORK ERROR: ALL SERVERS BUSY. RETRYING RECOMMENDED.")

# ==============================================================================
# MODULE 8: SYSTEM BOOTSTRAP
# ==============================================================================
if __name__ == "__main__":
    try:
        app = TitanApp()
        app.launch()
    except Exception as e:
        st.error(f"CRITICAL SYSTEM FAILURE: {e}")
