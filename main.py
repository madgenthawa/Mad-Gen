import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
import uuid
import sys
import json
import base64
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageEnhance, ImageFilter
from typing import Optional, Dict, List, Tuple, Any, Union
from dataclasses import dataclass, field

# ==============================================================================
# --------------------- SECTION 1: KERNEL CONFIGURATION ------------------------
# ==============================================================================

# Configure the System Logger with Millisecond Precision
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s::MAD_GEN_LEVIATHAN::%(module)s::%(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("MadGenLeviathan")

@dataclass
class SystemConfig:
    """
    Central Configuration Class for the entire application.
    Stores constants, URLs, and Theme settings.
    """
    APP_NAME: str = "Mad Gen: Leviathan"
    VERSION: str = "500.0.1 (Enterprise)"
    AUTHOR: str = "Maddy Core"
    WALLPAPER_URL: str = "https://images.alphacoders.com/132/1329587.jpeg"
    API_ENDPOINT: str = "https://image.pollinations.ai/prompt/"
    TIMEOUT: int = 60
    MAX_RETRIES: int = 5
    USER_AGENTS: List[str] = field(default_factory=lambda: [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
    ])

# Initialize Streamlit Page Configuration
st.set_page_config(
    page_title=SystemConfig.APP_NAME,
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://google.com',
        'Report a bug': 'https://github.com/maddy',
        'About': f"Built by {SystemConfig.AUTHOR}. Version {SystemConfig.VERSION}"
    }
)

# ==============================================================================
# --------------------- SECTION 2: SESSION STATE MANAGER -----------------------
# ==============================================================================

class MemoryCore:
    """
    Manages the persistent memory (RAM) of the application.
    Ensures that history, settings, and logs are saved between clicks.
    """
    @staticmethod
    def initialize():
        """Bootstraps the session state variables."""
        defaults = {
            'session_id': str(uuid.uuid4()),
            'boot_time': datetime.now().strftime("%H:%M:%S"),
            'history': [],          # Stores text history
            'gallery': [],          # Stores image binary data
            'logs': [],             # Stores system logs for the terminal
            'last_prompt': "",
            'generated_count': 0,
            'user_agent': random.choice(SystemConfig.USER_AGENTS)
        }
        
        for key, value in defaults.items():
            if key not in st.session_state:
                st.session_state[key] = value
                
    @staticmethod
    def log(message: str):
        """Adds a message to the on-screen terminal."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {message}"
        st.session_state['logs'].append(entry)
        # Keep only last 10 logs
        if len(st.session_state['logs']) > 10:
            st.session_state['logs'].pop(0)
        logger.info(message)

    @staticmethod
    def add_to_gallery(image_bytes, prompt, category):
        """Saves a generated image to the session gallery."""
        st.session_state['gallery'].insert(0, {
            "image": image_bytes,
            "prompt": prompt,
            "category": category,
            "time": datetime.now().strftime("%H:%M")
        })
        # Limit gallery to 10 images to save memory
        if len(st.session_state['gallery']) > 10:
            st.session_state['gallery'].pop()

# Initialize Memory
MemoryCore.initialize()

# ==============================================================================
# --------------------- SECTION 3: VISUAL ENGINE (CSS) -------------------------
# ==============================================================================

class VisualEngine:
    """
    The Graphics Rendering Engine.
    Injects massive CSS to overhaul the UI into the 'Stranger Things' theme.
    """
    @staticmethod
    def inject_assets():
        st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Roboto+Mono:wght@400;700&display=swap');

            /* --- CORE BACKGROUND --- */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.85), rgba(20,0,0,0.95)), url("{SystemConfig.WALLPAPER_URL}");
                background-size: cover;
                background-attachment: fixed;
                color: #ff0000;
            }}

            /* --- HEADERS --- */
            h1, h2, h3 {{
                font-family: 'Creepster', cursive !important;
                color: #ff0000 !important;
                text-shadow: 0 0 10px #000;
            }}
            
            .leviathan-title {{
                font-size: 6rem;
                text-align: center;
                animation: glitch 2s infinite;
                margin-bottom: 0px;
            }}
            
            @keyframes glitch {{
                0% {{ text-shadow: 2px 0 #f00, -2px 0 #000; }}
                25% {{ text-shadow: -2px 0 #00f, 2px 0 #f00; }}
                50% {{ text-shadow: 2px 0 #0f0, -2px 0 #000; }}
                75% {{ text-shadow: -2px 0 #f00, 2px 0 #fff; }}
                100% {{ text-shadow: 2px 0 #f00, -2px 0 #000; }}
            }}

            /* --- INPUT TERMINAL --- */
            .stTextArea textarea {{
                background-color: #080000 !important;
                color: #ff0000 !important;
                border: 2px solid #800 !important;
                font-family: 'Roboto Mono', monospace !important;
                font-size: 1.1rem !important;
                border-radius: 5px !important;
                padding: 15px !important;
                box-shadow: inset 0 0 30px #200 !important;
            }}
            
            .stTextArea textarea:focus {{
                border-color: #f00 !important;
                box-shadow: 0 0 20px #f00 !important;
            }}

            /* --- ACTION BUTTONS --- */
            .stButton > button {{
                width: 100%;
                background: linear-gradient(180deg, #400, #000);
                color: #fff;
                font-family: 'Creepster', cursive;
                font-size: 2rem;
                border: 2px solid #f00;
                height: 75px;
                text-transform: uppercase;
                transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            }}
            .stButton > button:hover {{
                background: #f00;
                color: #000;
                box-shadow: 0 0 60px #f00;
                transform: scale(1.02);
            }}

            /* --- SIDEBAR --- */
            [data-testid="stSidebar"] {{
                background-color: rgba(5, 0, 0, 0.95);
                border-right: 2px solid #500;
            }}
            
            /* --- TERMINAL WINDOW --- */
            .terminal-window {{
                background: #000;
                border: 1px solid #333;
                border-radius: 5px;
                padding: 10px;
                font-family: 'Roboto Mono', monospace;
                font-size: 0.8rem;
                color: #0f0;
                height: 150px;
                overflow-y: auto;
                opacity: 0.8;
                margin-top: 20px;
            }}

            /* --- GALLERY CARD --- */
            .gallery-card {{
                background: rgba(0,0,0,0.8);
                border: 1px solid #500;
                padding: 10px;
                border-radius: 10px;
                margin-bottom: 10px;
                text-align: center;
            }}
            
            /* --- SCROLLBAR --- */
            ::-webkit-scrollbar {{
                width: 10px;
                background: #000;
            }}
            ::-webkit-scrollbar-thumb {{
                background: #500;
                border-radius: 5px;
            }}
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# --------------------- SECTION 4: BUSINESS INTELLIGENCE -----------------------
# ==============================================================================

class DataWarehouse:
    """
    Stores hardcoded marketing slogans and logic for Thawa/LIC.
    Acting as the brain of the operation.
    """
    
    LIC_DATA = [
        "LIC: உங்கள் வாழ்க்கையின் பாதுகாப்பு அரண். 🏠",
        "எதிர்பாராததை எதிர்கொள்ள, LIC என்றும் துணை நிற்கும்.",
        "சரியான முதலீடு, சிறந்த எதிர்காலம் - LIC Housing Finance.",
        "கனவு இல்லம் நனவாக, எங்களை நாடுங்கள்."
    ]
    
    THAWA_DATA = [
        "THAWA Financial: உங்கள் வளர்ச்சியே எங்கள் நோக்கம். 📈",
        "Loan Against Property (LAP): உங்கள் சொத்து, உங்கள் சக்தி.",
        "எளிய வட்டி, விரைவான கடன் - தவா நிதி சேவை.",
        "தொழில் வளர்ச்சிக்கு நம்பகமான கூட்டாளி - THAWA."
    ]
    
    STRANGER_DATA = [
        "THE VOID: Vecna is watching you. 🩸",
        "Run. The Mind Flayer approaches.",
        "Welcome to the Upside Down.",
        "Hellfire Club: Official Member."
    ]

    @staticmethod
    def get_context(prompt: str) -> Tuple[str, str, str]:
        """
        Analyzes the input prompt and returns:
        1. Enhanced Prompt (String)
        2. Category Name (String)
        3. Marketing Slogan (String)
        """
        p = prompt.upper()
        
        # Logic for LIC
        if "LIC" in p or "INSURANCE" in p:
            enhanced = f"{prompt}, corporate billboard style, warm lighting, family safety, financial growth, 8k, professional photography, trustworthy atmosphere, sharp focus"
            return enhanced, "LIC HOUSING FINANCE", random.choice(DataWarehouse.LIC_DATA)
            
        # Logic for THAWA
        elif "THAWA" in p or "FINANCE" in p or "LOAN" in p:
            enhanced = f"{prompt}, ultra-modern office background, financial charts overlay, success, golden lighting, 8k, sharp focus, business magazine cover quality"
            return enhanced, "THAWA FINANCIAL SERVICES", random.choice(DataWarehouse.THAWA_DATA)
            
        # Logic for STRANGER THINGS
        elif "STRANGER" in p or "MONSTER" in p or "DRAGON" in p or "HELLFIRE" in p:
            enhanced = f"{prompt}, red lightning, dark atmosphere, retro 80s grain, horror theme, cinematic composition, highly detailed, raw photo, unreal engine 5 render, volumetric fog"
            return enhanced, "THE UPSIDE DOWN", random.choice(DataWarehouse.STRANGER_DATA)
            
        # Default Logic
        else:
            enhanced = f"{prompt}, award winning photography, 8k, highly detailed, sharp focus, cinematic lighting, trending on artstation, masterpiece"
            return enhanced, "MAD GEN LEVIATHAN", "Creating Reality from Code. ✨"

# ==============================================================================
# --------------------- SECTION 5: NETWORK CONTROLLER --------------------------
# ==============================================================================

class NetworkController:
    """
    The Beast. Handles API requests with Rotation, Retry Logic, and Spoofing.
    Designed to kill the 'Rate Limit' error.
    """
    
    @staticmethod
    def generate_image(prompt: str, width: int, height: int, model: str) -> Optional[bytes]:
        """
        Attempts to fetch an image using multiple strategies.
        """
        encoded = urllib.parse.quote(prompt)
        seed = int(time.time())
        
        # Define 3 Different Strategies (URLs)
        # Strategy 1: Flux Model (Best Quality)
        url_1 = f"{SystemConfig.API_ENDPOINT}{encoded}?width={width}&height={height}&seed={seed}&nologo=true&model={model}"
        # Strategy 2: Turbo Model (Fastest)
        url_2 = f"{SystemConfig.API_ENDPOINT}{encoded}?width={width}&height={height}&seed={seed}&nologo=true&model=turbo"
        # Strategy 3: Random Seed + Flux (Cache Busting)
        url_3 = f"{SystemConfig.API_ENDPOINT}{encoded}?width={width}&height={height}&seed={seed+500}&nologo=true&model=flux"
        
        strategies = [url_1, url_2, url_3]
        
        headers = {
            "User-Agent": st.session_state['user_agent'],
            "Referer": "https://www.google.com/"
        }
        
        for i, url in enumerate(strategies):
            try:
                MemoryCore.log(f"Attempt {i+1}: Connecting to Neural Node...")
                
                # Random sleep to mimic human behavior
                time.sleep(random.uniform(0.5, 1.2))
                
                response = requests.get(url, headers=headers, timeout=SystemConfig.TIMEOUT)
                
                # Check 1: Status Code
                if response.status_code == 200:
                    # Check 2: File Size (The 3-Byte Fix)
                    if len(response.content) > 50000: # Must be > 50KB
                        MemoryCore.log(f"Success! Payload received: {len(response.content)} bytes.")
                        return response.content
                    else:
                        MemoryCore.log("Warning: File too small (3-Byte Error). Rotating...")
                elif response.status_code == 429:
                    MemoryCore.log("Error: Rate Limit Hit. Switching Strategy...")
                else:
                    MemoryCore.log(f"Server Error: {response.status_code}")
                    
            except Exception as e:
                MemoryCore.log(f"Network Failure: {str(e)}")
        
        MemoryCore.log("Critical Failure: All Strategies Exhausted.")
        return None

# ==============================================================================
# --------------------- SECTION 6: UI COMPONENT FACTORY ------------------------
# ==============================================================================

class UIComponents:
    """
    Generates complex UI elements like the Sidebar, Gallery, and Terminal.
    """
    
    @staticmethod
    def render_sidebar():
        with st.sidebar:
            st.markdown("## ⚙️ CONTROL DECK")
            st.divider()
            
            # Model Selection
            model = st.selectbox("Neural Model:", ["flux", "turbo", "unity"], index=0)
            
            # Aspect Ratio
            ratio = st.selectbox("Aspect Ratio:", ["Square (1:1)", "Cinematic (16:9)", "Portrait (9:16)"])
            
            # Mapping Ratio to Pixels
            dims = (1024, 1024)
            if "Cinematic" in ratio: dims = (1280, 720)
            if "Portrait" in ratio: dims = (720, 1280)
            
            st.divider()
            st.markdown("### 📊 SYSTEM DIAGNOSTICS")
            
            # Fake Terminal Window
            log_text = "\n".join(st.session_state['logs'])
            st.markdown(f"""
            <div class="terminal-window">
            {log_text}
            <br>>_ SYSTEM READY
            </div>
            """, unsafe_allow_html=True)
            
            st.divider()
            if st.button("🔴 RESET SYSTEM"):
                st.session_state.clear()
                st.rerun()
                
            return model, dims

    @staticmethod
    def render_gallery():
        """Displays previous images in a grid."""
        if not st.session_state['gallery']:
            return

        st.markdown("---")
        st.markdown("### 🎞️ ARCHIVE GALLERY")
        
        # Create a grid of 3 columns
        cols = st.columns(3)
        
        for idx, item in enumerate(st.session_state['gallery']):
            col = cols[idx % 3]
            with col:
                st.image(item['image'], use_container_width=True)
                st.caption(f"{item['category']} | {item['time']}")

# ==============================================================================
# --------------------- SECTION 7: MAIN APPLICATION LOOP -----------------------
# ==============================================================================

class LeviathanApp:
    def __init__(self):
        self.visuals = VisualEngine()
        self.network = NetworkController()
        self.brain = DataWarehouse()
        self.ui = UIComponents()

    def launch(self):
        # 1. Inject CSS
        self.visuals.inject_assets()
        
        # 2. Render Header
        st.markdown('<h1 class="leviathan-title">MAD GEN</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center; color:#ccc; letter-spacing:4px;">LEVIATHAN ARCHITECTURE | 500+ LINES | MADDY CORE</p>', unsafe_allow_html=True)
        
        # 3. Render Sidebar
        model, (width, height) = self.ui.render_sidebar()
        
        # 4. Main Grid
        col1, col2 = st.columns([1, 1], gap="large")
        
        # --- INPUT COLUMN ---
        with col1:
            st.markdown("### 👁️ SUMMONING CIRCLE")
            user_input = st.text_area(
                "DESCRIBE THE ENTITY:", 
                height=180, 
                placeholder="Ex: Golden Dragon, LIC Poster, Thawa Ad..."
            )
            
            if st.button("EXECUTE PROTOCOL 🩸"):
                if user_input:
                    self.execute(user_input, width, height, model)
                else:
                    st.error("BLOOD SACRIFICE (INPUT) REQUIRED.")
                    MemoryCore.log("Error: Input Missing.")

        # --- OUTPUT COLUMN ---
        with col2:
            st.markdown("### 🖼️ MANIFESTATION")
            
            if 'final_image' in st.session_state:
                st.image(st.session_state['final_image'], use_container_width=True)
                
                # Show Metadata
                title, slogan = st.session_state['final_meta']
                st.info(f"**{title}**\n\n{slogan}")
                
                # Download Button
                timestamp = int(time.time())
                st.download_button(
                    label="📥 DOWNLOAD LEVIATHAN ARTIFACT (HD)",
                    data=st.session_state['final_image'],
                    file_name=f"LEVIATHAN_{timestamp}.png",
                    mime="image/png"
                )
            else:
                st.markdown("""
                <div style="border:1px dashed #500; padding:40px; text-align:center; color:#500;">
                THE VOID IS EMPTY.<br>AWAITING DATA STREAM.
                </div>
                """, unsafe_allow_html=True)
                
        # 5. Render Gallery at Bottom
        self.ui.render_gallery()

    def execute(self, prompt, w, h, model):
        MemoryCore.log(f"Processing Request: {prompt[:20]}...")
        
        with st.spinner("🔴 OPENING PORTAL TO NEURAL CLOUD..."):
            # 1. Analyze Prompt
            enhanced_prompt, category, slogan = self.brain.get_context(prompt)
            MemoryCore.log(f"Logic Applied: {category}")
            
            # 2. Fetch Image
            image_bytes = self.network.generate_image(enhanced_prompt, w, h, model)
            
            # 3. Handle Result
            if image_bytes:
                # Save to State
                st.session_state['final_image'] = image_bytes
                st.session_state['final_meta'] = (category, slogan)
                
                # Add to Gallery
                MemoryCore.add_to_gallery(image_bytes, prompt, category)
                
                MemoryCore.log("Generation Complete.")
                st.success("ENTITY STABILIZED.")
                st.rerun()
            else:
                st.error("CONNECTION SEVERED. SERVERS OVERLOADED.")
                MemoryCore.log("Critical Error: Workflow Aborted.")

# ==============================================================================
# --------------------- SECTION 8: SYSTEM BOOTSTRAP ----------------------------
# ==============================================================================

if __name__ == "__main__":
    try:
        # Instantiate and Launch the Application
        app = LeviathanApp()
        app.launch()
    except Exception as e:
        st.error(f"SYSTEM CRASH: {e}")
        logging.critical(f"System Crash: {e}")
