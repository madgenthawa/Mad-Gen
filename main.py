import streamlit as st
import time
import random
import logging
import uuid
import urllib.parse
from datetime import datetime
from typing import Tuple

# ==============================================================================
# MODULE 1: OMNI KERNEL CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: Omni Client",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# High-Level Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - OMNI_CORE - %(message)s')
logger = logging.getLogger("MadGenOmni")

if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())
    st.session_state['history'] = []

# ==============================================================================
# MODULE 2: VISUAL ENGINE (STRANGER THINGS THEME)
# ==============================================================================
class Visuals:
    """
    Manages the 'Upside Down' aesthetic using pure CSS injection.
    """
    WALLPAPER = "https://images.alphacoders.com/132/1329587.jpeg"

    @staticmethod
    def inject():
        st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Roboto+Mono:wght@500&display=swap');
            
            /* --- GLOBAL THEME --- */
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.85), rgba(10,0,0,0.95)), url("{Visuals.WALLPAPER}");
                background-size: cover;
                background-attachment: fixed;
                color: #ff0000;
            }}
            
            /* --- HEADER --- */
            .omni-header {{
                font-family: 'Creepster', cursive;
                font-size: 5rem;
                text-align: center;
                color: #ff0000;
                text-shadow: 0 0 20px #000, 4px 4px 0px #500;
                animation: glitch 3s infinite;
            }}
            
            @keyframes glitch {{
                0% {{ text-shadow: 2px 0 #f00, -2px 0 #000; }}
                50% {{ text-shadow: -2px 0 #f00, 2px 0 #000; }}
                100% {{ text-shadow: 2px 0 #f00, -2px 0 #000; }}
            }}
            
            /* --- INPUT TERMINAL --- */
            .stTextArea textarea {{
                background-color: #000 !important;
                color: #ff0000 !important;
                border: 2px solid #800 !important;
                font-family: 'Roboto Mono', monospace !important;
                font-size: 1.2rem !important;
                border-radius: 10px !important;
                box-shadow: inset 0 0 40px #200 !important;
            }}
            .stTextArea textarea:focus {{
                border-color: #f00 !important;
                box-shadow: 0 0 30px #f00 !important;
            }}
            
            /* --- ACTION BUTTON --- */
            .stButton > button {{
                background: linear-gradient(180deg, #500, #000);
                color: #fff;
                border: 1px solid #f00;
                font-family: 'Creepster', cursive;
                font-size: 1.8rem;
                height: 70px;
                width: 100%;
                text-transform: uppercase;
                transition: 0.3s;
            }}
            .stButton > button:hover {{
                background: #f00;
                color: #000;
                box-shadow: 0 0 50px #f00;
            }}
            
            /* --- CLIENT-SIDE IMAGE FRAME --- */
            .image-frame {{
                border: 2px solid #f00;
                border-radius: 15px;
                padding: 10px;
                background: rgba(0,0,0,0.8);
                box-shadow: 0 0 30px rgba(255, 0, 0, 0.3);
                text-align: center;
            }}
            
            .image-frame img {{
                width: 100%;
                border-radius: 10px;
                transition: transform 0.3s;
            }}
            
            .image-frame img:hover {{
                transform: scale(1.02);
            }}

            /* --- DOWNLOAD BUTTON (HTML) --- */
            .custom-dl-btn {{
                display: inline-block;
                margin-top: 20px;
                padding: 15px 40px;
                background: #f00;
                color: #000;
                font-family: 'Roboto Mono', monospace;
                font-weight: bold;
                text-decoration: none;
                border-radius: 5px;
                box-shadow: 0 0 20px #f00;
                transition: 0.3s;
            }}
            .custom-dl-btn:hover {{
                background: #fff;
                color: #f00;
                box-shadow: 0 0 50px #fff;
            }}
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# MODULE 3: PROMPT CORTEX (LOGIC EXPANSION)
# ==============================================================================
class Cortex:
    """
    Expands simple user inputs into professional 'God Tier' prompts.
    """
    @staticmethod
    def expand(prompt: str) -> Tuple[str, str]:
        p = prompt.upper()
        
        if "LIC" in p or "INSURANCE" in p:
            category = "LIC HOUSING"
            modifiers = ", corporate billboard style, warm lighting, family safety, financial growth, 8k, professional photography, trustworthy atmosphere"
        elif "THAWA" in p or "LOAN" in p:
            category = "THAWA FINANCE"
            modifiers = ", ultra-modern office background, financial charts overlay, success, golden lighting, 8k, sharp focus, business magazine cover quality"
        elif "DRAGON" in p or "MONSTER" in p:
            category = "MYTHICAL"
            modifiers = ", unreal engine 5 render, volumetric fog, bioluminescent scales, cinematic lighting, wide angle, hyper-realistic, masterpiece, 8k"
        elif "STRANGER" in p or "HELLFIRE" in p:
            category = "THE UPSIDE DOWN"
            modifiers = ", red lightning, dark atmosphere, retro 80s grain, horror theme, cinematic composition, highly detailed, raw photo"
        else:
            category = "GENERAL"
            modifiers = ", award winning photography, 8k, highly detailed, sharp focus, cinematic lighting"
            
        enhanced = f"{prompt}{modifiers}"
        return enhanced, category

# ==============================================================================
# MODULE 4: CLIENT-SIDE BRIDGE (THE BYPASS FIX)
# ==============================================================================
class ClientBridge:
    """
    Generates HTML that forces the User's Browser to fetch the image directly.
    Bypasses Streamlit Server IP blocking entirely.
    """
    BASE_URL = "https://image.pollinations.ai/prompt/"
    
    @staticmethod
    def generate_html(prompt):
        # 1. Encode Prompt
        encoded = urllib.parse.quote(prompt)
        seed = int(time.time())
        
        # 2. Construct URL (No Server Request here)
        # Using 'nologo=true' and 'flux' model
        img_url = f"{ClientBridge.BASE_URL}{encoded}?width=1024&height=1024&seed={seed}&nologo=true&model=flux"
        
        # 3. Create HTML Frame
        html_code = f"""
        <div class="image-frame">
            <h3 style="color:#f00; font-family:'Roboto Mono';">STATUS: MANIFESTED</h3>
            <img src="{img_url}" alt="Generated Image" onload="this.style.opacity=1;" onerror="this.src='https://via.placeholder.com/1024x1024/000000/FF0000?text=Load+Error';">
            <br>
            <a href="{img_url}" target="_blank" class="custom-dl-btn">
                📥 DOWNLOAD ORIGINAL (HD)
            </a>
            <p style="color:#888; font-size:0.8rem; margin-top:10px;">
                *Image rendered on local neural core (Client-Side)
            </p>
        </div>
        """
        return html_code, img_url

# ==============================================================================
# MODULE 5: MAIN APP LOOP
# ==============================================================================
def main():
    Visuals.inject()
    
    st.markdown('<h1 class="omni-header">MAD GEN</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#ccc; letter-spacing:3px;">OMNI CLIENT | SERVER BYPASS ACTIVE</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown('<div class="image-frame" style="text-align:left; border:1px solid #500;">', unsafe_allow_html=True)
        st.markdown("### 👁️ INPUT TERMINAL")
        user_input = st.text_area("DESCRIBE ENTITY:", height=180, placeholder="Ex: Golden Dragon, LIC Poster, Thawa Ad...")
        
        if st.button("EXECUTE PROTOCOL 🩸"):
            if user_input:
                # Expand Logic
                enhanced_prompt, category = Cortex.expand(user_input)
                
                # Save to State
                st.session_state['current_prompt'] = enhanced_prompt
                st.session_state['current_cat'] = category
                st.session_state['history'].append(user_input)
                
                # Trigger Rerun to update UI
                st.rerun()
            else:
                st.warning("BLOOD (INPUT) REQUIRED.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Sidebar History
        with st.sidebar:
            st.markdown("## 📜 HISTORY")
            for h in reversed(st.session_state['history'][-5:]):
                st.caption(f"• {h}")

    with col2:
        st.markdown("### 🖼️ VISUAL OUTPUT")
        
        if 'current_prompt' in st.session_state:
            # Generate the HTML Code
            html_output, direct_url = ClientBridge.generate_html(st.session_state['current_prompt'])
            
            # Render HTML directly (Browser fetches image, not Python)
            st.components.v1.html(html_output, height=600, scrolling=False)
            
            st.info(f"Logic Applied: **{st.session_state['current_cat']}**")
        else:
            st.info("THE VOID IS EMPTY. AWAITING INPUT.")

if __name__ == "__main__":
    main()
