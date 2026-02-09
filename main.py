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
# MODULE 1: SYSTEM KERNEL & ADVANCED LOGGING
# ==============================================================================
# We configure a 'Verbose' logger to simulate an industrial operating system.
logging.basicConfig(
    format='[%(asctime)s] %(levelname)s::HELLFIRE_CORE::%(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("MadGenHellfire")

class SystemKernel:
    """
    The Central Processing Unit of the application.
    Manages Memory, Session States, and Boot Protocols.
    """
    @staticmethod
    def initialize_session():
        """Bootstraps the session state variables if they don't exist."""
        if 'session_id' not in st.session_state:
            st.session_state['session_id'] = str(uuid.uuid4())
            st.session_state['boot_time'] = datetime.now().strftime("%H:%M:%S")
            st.session_state['history'] = [] # Stores prompt history
            st.session_state['render_count'] = 0
            logger.info(f"SYSTEM BOOT COMPLETE. SESSION: {st.session_state['session_id']}")

# Initialize the Kernel immediately
SystemKernel.initialize_session()

# ==============================================================================
# MODULE 2: APP CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: Hellfire Edition",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://google.com',
        'About': "Mad Gen Hellfire Edition v100.0 | High-Performance Engine."
    }
)

# ==============================================================================
# MODULE 3: THE "HELLFIRE" VISUAL ENGINE (POLISHED CSS)
# ==============================================================================
class VisualEngine:
    """
    Manages the Visual Layer.
    FOCUS: The Input Box (Chat Box) is heavily styled here.
    """
    
    # 4K Upside Down Background
    WALLPAPER_URL = "https://images.alphacoders.com/132/1329587.jpeg" 

    @staticmethod
    def inject_styles():
        st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Roboto+Mono:wght@500&display=swap');

            /* --- 1. GLOBAL ATMOSPHERE --- */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.7), rgba(20,0,0,0.9)), url("{VisualEngine.WALLPAPER_URL}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #ff0000;
            }}

            /* --- 2. THE CHAT BOX (INPUT AREA) - HEAVILY POLISHED --- */
            /* This is the specific part you asked for */
            .stTextArea label {{
                color: #ff0000 !important;
                font-family: 'Creepster', cursive !important;
                font-size: 1.5rem !important;
                letter-spacing: 2px;
                text-shadow: 0 0 10px #f00;
            }}
            
            .stTextArea textarea {{
                background-color: #000000 !important; /* Pure Black Void */
                color: #ff3333 !important; /* Glowing Red Text */
                font-family: 'Roboto Mono', monospace !important;
                font-size: 1.1rem !important;
                border: 2px solid #800000 !important; /* Dark Red Border */
                border-radius: 10px !important;
                padding: 15px !important;
                box-shadow: inset 0 0 30px #200000 !important; /* Inner Glow */
                transition: all 0.3s ease-in-out;
            }}
            
            .stTextArea textarea:focus {{
                border: 2px solid #ff0000 !important; /* Bright Red on Focus */
                box-shadow: 0 0 20px #ff0000, inset 0 0 20px #500 !important;
            }}

            /* --- 3. SIDEBAR STYLING --- */
            [data-testid="stSidebar"] {{
                background-color: rgba(10, 0, 0, 0.95);
                border-right: 2px solid #500;
            }}
            
            [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
                color: #ff0000 !important;
                font-family: 'Creepster', cursive !important;
            }}

            /* --- 4. BUTTONS --- */
            .stButton > button {{
                width: 10
