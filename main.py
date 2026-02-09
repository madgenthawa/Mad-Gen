import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
import json
import uuid
from typing import Optional, Tuple, List, Dict
from datetime import datetime
from enum import Enum

# ==============================================================================
# SECTION 1: SYSTEM KERNEL & LOGGING CONFIGURATION
# ==============================================================================
# We set up a professional logging system to track every event in the console.
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s::MAD_GEN_KERNEL::%(message)s', 
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("MadGenTitanium")

# Initialize Session State Variables if they don't exist
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())
    logger.info(f"New Session Initialized: {st.session_state['session_id']}")

# ==============================================================================
# SECTION 2: APP CONFIGURATION & METADATA
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen Titanium | Dragon Edition",
    page_icon="🐉",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.google.com",
        'About': "# Mad Gen Titanium v25.0\nBuilt for Maddy."
    }
)

# ==============================================================================
# SECTION 3: DRAGON-FIRE UI ENGINE (ADVANCED CSS)
# ==============================================================================
class ThemeEngine:
    """
    Manages the visual presentation layer, specifically the 
    'Dragon with Fire' background and glass-morphism UI elements.
    """
    
    DRAGON_BG_URL = "https://wallpaperaccess.com/full/19066.jpg" # Epic Fire Dragon
    
    @staticmethod
    def deploy_styles():
        logger.info("Deploying Dragon Fire Stylesheets...")
        st.markdown(f"""
        <style>
            /* --- CORE BACKGROUND: DRAGON WITH FIRE --- */
            .stApp {{
                background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("{ThemeEngine.DRAGON_BG_URL}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #ffffff;
            }}
            
            /* --- TYPOGRAPHY SYSTEM --- */
            h1, h2, h3, h4, h5, h6 {{
                font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                text-shadow: 0px 2px 4px rgba(0,0,0,0.8);
            }}
            
            .titanium-header {{
                font-size: 4.5rem;
                font-weight: 900;
                text-align: center;
                background: linear-gradient(180deg, #FFD700 0%, #FF4500 50%, #8B0000 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0px;
                filter: drop-shadow(0px 0px 10px rgba(255, 69, 0, 0.5));
                letter-spacing: -2px;
                text-transform: uppercase;
            }}
            
            .titanium-sub {{
                text-align: center;
                color: #FFD700;
                font-size: 1.4rem;
                font-weight: 300;
                margin-bottom: 50px;
                letter-spacing: 2px;
                text-transform: uppercase;
            }}

            /* --- GLASSMORPHISM CARDS --- */
            .control-panel {{
                background: rgba(0, 0, 0, 0.6);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 69, 0, 0.3);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
                transition: transform 0.3s ease;
            }}
            
            .control-panel:hover {{
                border: 1px solid rgba(255, 215, 0, 0.5);
                transform: translateY(-2px);
            }}

            /* --- ADVANCED INPUT FIELDS --- */
            .stTextArea textarea {{
                background-color: rgba(0, 0, 0, 0.8) !important;
                color: #FFD700 !important; /* Gold Text */
                border: 1px solid #FF4500 !important;
                border-radius: 12px !important;
                font-size: 1.1rem !important;
            }}
            
            /* --- ACTION BUTTONS --- */
            .stButton > button {{
                background: linear-gradient(90deg, #FF4500, #FFD700);
                color: black;
                font-weight: 900;
                border: none;
                border-radius: 50px;
                height: 65px;
                font-size: 20px;
                text-transform: uppercase;
                box-shadow: 0 0 20px rgba(255, 69, 0, 0.6);
                transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            }}
            
            .stButton > button:hover {{
                transform: scale(1.03);
                box-shadow: 0 0 40px rgba(255, 215, 0, 0.8);
                color: black;
            }}
            
            /* --- DOWNLOAD BUTTON OVERRIDE --- */
            .download-btn-container {{
                text-align: center;
                margin-top: 20px;
            }}
            
            /* --- SCROLLBAR CUSTOMIZATION --- */
            ::-webkit-scrollbar {{
                width: 10px;
                background: #000;
            }}
            ::-webkit-scrollbar-thumb {{
                background: #FF4500;
                border-radius: 5px;
            }}
            
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# SECTION 4: BUSINESS LOGIC KERNEL (LIC & THAWA)
# ==============================================================================
class MarketingIntelligence:
    """
    Handles all Tamil localization and business-specific logic for
    LIC Housing Finance and Thawa Financial Services.
    """
    
    def __init__(self):
        self.db = {
            "LIC": [
                "LIC: உங்கள் பாதுகாப்பான எதிர்காலத்தின் திறவுகோல். 🗝️",
                "கனவு இல்லம் நனவாக, LIC Housing Finance-ஐ நாடுங்கள். 🏠",
                "தலைமுறை தாண்டியும் தொடரும் நம்பிக்கை - LIC.",
                "பாதுகாப்பு மற்றும் சேமிப்பு, இரண்டும் ஒரே இடத்தில்."
            ],
            "THAWA": [
                "THAWA Financial: உங்கள் நிதி சுதந்திரத்தின் ஆரம்பம். 📈",
                "Loan Against Property (LAP): சொத்து உங்கள் கையில், பணம் உங்கள் தேவையில்.",
                "வேகமான செயல்முறை, வெளிப்படையான வட்டி - தவா நிதி சேவை.",
                "உங்கள் தொழில் வளர்ச்சிக்கு உற்ற தோழன் - THAWA Financials."
            ],
            "DRAGON": [
                "DRAGON MODE: Fire and Fury Unleashed! 🔥",
                "Legendary Power. Mythical Quality.",
                "The Skies Burn with Creativity."
            ],
            "DEFAULT": [
                "Mad Gen Titanium: உருவாக்கம் உங்கள் கையில். ✨",
                "Quality so high, it feels real.",
                "Powered by Maddy's Vision."
            ]
        }
        logger.info("Marketing Intelligence Database Loaded.")

    def analyze_intent(self, prompt: str) -> Tuple[str, str]:
        """Analyzes user prompt to determine business context."""
        p = prompt.upper()
        if "LIC" in p or "HOUSING" in p:
            return "LIC HOUSING FINANCE", random.choice(self.db["LIC"])
        elif "THAWA" in p or "FINANC" in p or "LOAN" in p:
            return "THAWA FINANCIAL SERVICES", random.choice(self.db["THAWA"])
        elif "DRAGON" in p:
            return "MYTHICAL CREATURES", random.choice(self.db["DRAGON"])
        else:
            return "MAD GEN TITANIUM", random.choice(self.db["DEFAULT"])

# ==============================================================================
# SECTION 5: NETWORK CONTROLLER (API HANDLING)
# ==============================================================================
class NetworkController:
    """
    Manages all outbound API calls with retry logic, timeout handling,
    and binary data validation to prevent '3-byte' errors.
    """
    
    BASE_URL = "https://image.pollinations.ai/prompt/"
    
    @staticmethod
    def generate_asset(prompt: str) -> Optional[bytes]:
        """
        Attempts to generate an image from the prompt.
        Uses a retry mechanism with exponential backoff.
        """
        # 1. Enhance Prompt for 8K Quality
        enhanced_prompt = f"{prompt}, 8k, photorealistic, cinematic lighting, highly detailed, masterpiece, sharp focus, professional grading"
        
        # 2. URI Encode (Fixes Cloudflare 400 Errors)
        safe_prompt = urllib.parse.quote(enhanced_prompt)
        
        # 3. Dynamic Seed
        seed = int(time.time())
        
        # 4. Construct Endpoint
        url = f"{NetworkController.BASE_URL}{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux"
        
        logger.info(f"Initiating Request to: {url}")
        
        # 5. Retry Loop
        max_retries = 3
        for attempt in range(max_retries):
            try:
                with st.spinner(f"Titanium Core Processing... (Attempt {attempt+1}/{max_retries})"):
                    response = requests.get(url, timeout=60) # High timeout for HD
                    
                    # 6. Binary Validation (The Anti-3-Byte Filter)
                    if response.status_code == 200:
                        content_size = len(response.content)
                        if content_size > 50000: # Must be > 50KB
                            logger.info(f"Success! Image received. Size: {content_size} bytes.")
                            return response.content
                        else:
                            logger.warning(f"Validation Failed: File too small ({content_size} bytes). Retrying...")
                    else:
                        logger.warning(f"Server Error: {response.status_code}")
                        
            except requests.exceptions.Timeout:
                logger.error("Request Timed Out.")
            except Exception as e:
                logger.error(f"Critical Network Failure: {e}")
            
            time.sleep(2) # Cooldown before retry
            
        return None

# ==============================================================================
# SECTION 6: MAIN APPLICATION CLASS (UI ORCHESTRATION)
# ==============================================================================
class TitaniumApp:
    def __init__(self):
        self.theme = ThemeEngine()
        self.marketing = MarketingIntelligence()
        self.network = NetworkController()
        
    def render(self):
        # 1. Apply Styles
        self.theme.deploy_styles()
        
        # 2. Render Header
        st.markdown('<h1 class="titanium-header">MAD GEN TITANIUM</h1>', unsafe_allow_html=True)
        st.markdown('<p class="titanium-sub">Dragon Edition | Thawa Financials | Maddy Core</p>', unsafe_allow_html=True)
        
        # 3. Main Grid Layout
        col_input, col_display = st.columns([1, 1], gap="large")
        
        # --- INPUT COLUMN ---
        with col_input:
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)
            st.markdown("### 📡 COMMAND CENTER")
            
            user_input = st.text_area(
                "ENTER VISUAL PARAMETERS:", 
                height=200, 
                placeholder="Ex: Gold Dragon breathing fire, or LIC Housing Finance Poster..."
            )
            
            # Additional Controls
            quality_mode = st.select_slider(
                "RENDERING ENGINE POWER:", 
                options=["Standard", "High-Def", "Ultra", "TITANIUM"]
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("INITIATE GENERATION PROTOCOL 🚀"):
                if user_input:
                    self.execute_generation(user_input, quality_mode)
                else:
                    st.error("INPUT REQUIRED: ABORTING SEQUENCE.")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
        # --- DISPLAY COLUMN ---
        with col_display:
            st.markdown('<div class="control-panel">', unsafe_allow_html=True)
            st.markdown("### 🖼️ VISUAL OUTPUT")
            
            if 'titanium_image' in st.session_state:
                # Display Image
                st.image(st.session_state['titanium_image'], use_container_width=True)
                
                # Display Marketing Text
                title, slogan = st.session_state['titanium_meta']
                st.info(f"**{title}**\n\n{slogan}")
                
                # Binary Download Button
                timestamp = int(time.time())
                st.download_button(
                    label="📥 DOWNLOAD RAW BINARY (HD)",
                    data=st.session_state['titanium_image'],
                    file_name=f"TITANIUM_RENDER_{timestamp}.png",
                    mime="image/png"
                )
            else:
                st.markdown(
                    """
                    <div style='text-align:center; padding:50px; border:2px dashed #444; color:#666;'>
                        SYSTEM STANDBY.<br>AWAITING INPUT...
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            st.markdown('</div>', unsafe_allow_html=True)

    def execute_generation(self, prompt, quality):
        """Orchestrates the generation workflow."""
        # 1. Analyze Intent
        meta_data = self.marketing.analyze_intent(prompt)
        
        # 2. Fetch Data
        image_data = self.network.generate_asset(prompt)
        
        # 3. Update State
        if image_data:
            st.session_state['titanium_image'] = image_data
            st.session_state['titanium_meta'] = meta_data
            st.toast("GENERATION COMPLETE. SYSTEM STABLE.", icon="✅")
            st.rerun()
        else:
            st.error("CRITICAL FAILURE: EXTERNAL SERVERS UNRESPONSIVE. RETRY ADVISED.")

# ==============================================================================
# SECTION 7: BOOTSTRAPPER
# ==============================================================================
if __name__ == "__main__":
    try:
        app = TitaniumApp()
        app.render()
    except Exception as e:
        st.error(f"SYSTEM CRASH: {e}")
        logger.critical(f"System Crash: {e}")
