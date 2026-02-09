import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
import uuid
from io import BytesIO
from PIL import Image

# ==============================================================================
# LEVEL 1: SYSTEM CONFIGURATION & LOGGING (Strong Foundation)
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: God Mode",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# High-Performance Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - GOD_MODE - %(message)s')
logger = logging.getLogger("MadGenGodMode")

if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())
    st.session_state['history'] = []

# ==============================================================================
# LEVEL 2: INTELLIGENT PROMPT ENGINE (God Level Understanding)
# ==============================================================================
class GodBrain:
    """
    This class handles the 'Understanding'. It takes simple words and 
    converts them into cinematic, professional descriptions.
    """
    @staticmethod
    def enhance_prompt(raw_input):
        # 1. Detect Category
        category = "GENERAL"
        p = raw_input.upper()
        
        if "LIC" in p or "BANK" in p or "LOAN" in p:
            category = "BUSINESS"
        elif "DRAGON" in p or "MONSTER" in p or "GOD" in p:
            category = "MYTHOLOGY"
        elif "CAR" in p or "BIKE" in p:
            category = "AUTOMOTIVE"
            
        # 2. Apply "God Level" Modifiers based on category
        modifiers = {
            "BUSINESS": ", professional corporate photography, 8k resolution, trustworthy, financial growth, sharp focus, billboard quality",
            "MYTHOLOGY": ", epic scale, cinematic lighting, volumetric fog, hyper-realistic, unreal engine 5 render, detailed texture, 8k, masterpiece",
            "AUTOMOTIVE": ", studio lighting, 4k automotive photography, reflection, metallic paint, speed blur, commercial quality",
            "GENERAL": ", award winning photography, 8k, highly detailed, sharp focus, cinematic composition"
        }
        
        # 3. Construct the Final "God Prompt"
        final_prompt = raw_input + modifiers.get(category, modifiers["GENERAL"])
        logger.info(f"Prompt Enhanced: {final_prompt}")
        return final_prompt, category

# ==============================================================================
# LEVEL 3: ROBUST NETWORK LAYER (Strong & Fast Processing)
# ==============================================================================
class NeuralNetwork:
    """
    Handles connections. Uses a 'Multi-Server Fallback' strategy.
    If one fails, it tries another. NO MORE CONNECTION ERRORS.
    """
    BASE_URL = "https://image.pollinations.ai/prompt/"
    
    @staticmethod
    def fetch_data(prompt):
        safe_prompt = urllib.parse.quote(prompt)
        seed = int(time.time())
        
        # Strategy: Try 3 different configurations if one fails
        configs = [
            f"{NeuralNetwork.BASE_URL}{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux", # Best Quality
            f"{NeuralNetwork.BASE_URL}{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=turbo", # Faster
            f"{NeuralNetwork.BASE_URL}{safe_prompt}?width=1024&height=1024&seed={seed+1}&nologo=true" # Backup Seed
        ]
        
        for attempt, url in enumerate(configs):
            try:
                logger.info(f"Attempt {attempt+1}: Connecting to Neural Core...")
                # Timeout set to 45 seconds to allow deep processing
                response = requests.get(url, timeout=45)
                
                if response.status_code == 200:
                    # VALIDATION: Check if it's a real image (Not 3 bytes)
                    if len(response.content) > 60000: # Minimum 60KB
                        return response.content
                    else:
                        logger.warning("File too small. Retrying...")
            except Exception as e:
                logger.error(f"Connection Failed on Attempt {attempt+1}: {e}")
                time.sleep(2) # Wait 2 seconds before retry
        
        return None

# ==============================================================================
# LEVEL 4: IMAGE PROCESSOR (Image Processing Strong)
# ==============================================================================
class ImageProcessor:
    """
    Uses Pillow (PIL) to verify and optimize the image before display.
    """
    @staticmethod
    def process(image_bytes):
        try:
            # 1. Open Image from Memory
            img = Image.open(BytesIO(image_bytes))
            
            # 2. Verify Integrity
            img.verify() 
            
            # 3. Re-open for display (verify closes the file)
            img = Image.open(BytesIO(image_bytes))
            
            # 4. Return as Bytes for Download
            buf = BytesIO()
            img.save(buf, format="PNG", optimize=True)
            return buf.getvalue()
        except Exception as e:
            logger.error(f"Image Corruption Detected: {e}")
            return None

# ==============================================================================
# LEVEL 5: VISUAL UI (Stranger Things / Hellfire Theme)
# ==============================================================================
class UI:
    WALLPAPER = "https://images.alphacoders.com/132/1329587.jpeg"

    @staticmethod
    def inject_css():
        st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Roboto+Mono:wght@500&display=swap');
            
            .stApp {{
                background: linear-gradient(rgba(0,0,0,0.85), rgba(20,0,0,0.95)), url("{UI.WALLPAPER}");
                background-size: cover;
                background-attachment: fixed;
                color: #ff0000;
            }}
            
            /* GOD LEVEL HEADER */
            .god-header {{
                font-family: 'Creepster', cursive;
                font-size: 6rem;
                text-align: center;
                color: #ff0000;
                text-shadow: 0 0 30px #000, 0 0 10px #f00;
                animation: pulse 3s infinite;
            }}
            
            @keyframes pulse {{
                0% {{ text-shadow: 0 0 20px #500; }}
                50% {{ text-shadow: 0 0 50px #f00; }}
                100% {{ text-shadow: 0 0 20px #500; }}
            }}
            
            /* STRONG INPUT BOX */
            .stTextArea textarea {{
                background-color: #000 !important;
                color: #ff3333 !important;
                border: 2px solid #900 !important;
                font-family: 'Roboto Mono', monospace !important;
                font-size: 1.2rem !important;
                border-radius: 10px;
                padding: 20px;
                box-shadow: inset 0 0 40px #200;
            }}
            
            /* DOWNLOAD BUTTON */
            .stButton > button {{
                background: linear-gradient(180deg, #300, #000);
                color: #f00;
                border: 2px solid #f00;
                font-family: 'Creepster', cursive;
                font-size: 1.8rem;
                height: 70px;
                transition: 0.4s;
            }}
            .stButton > button:hover {{
                box-shadow: 0 0 50px #f00;
                transform: scale(1.02);
            }}
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# MAIN ORCHESTRATION LOOP
# ==============================================================================
def main():
    UI.inject_css()
    
    st.markdown('<h1 class="god-header">MAD GEN: GOD MODE</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 👁️ ENTER COMMAND")
        user_input = st.text_area("DESCRIBE VISUAL:", height=180, placeholder="Ex: Golden Dragon, LIC Poster, Thawa Ad...")
        
        if st.button("EXECUTE PROTOCOL 🩸"):
            if user_input:
                with st.spinner("🔴 INITIALIZING GOD-LEVEL PROTOCOLS..."):
                    # Level 1: Brain
                    enhanced_prompt, category = GodBrain.enhance_prompt(user_input)
                    st.toast(f"Brain: Logic set to {category} Mode", icon="🧠")
                    
                    # Level 2: Network (With Auto-Retry)
                    raw_data = NeuralNetwork.fetch_data(enhanced_prompt)
                    
                    if raw_data:
                        # Level 3: Processing
                        processed_image = ImageProcessor.process(raw_data)
                        
                        if processed_image:
                            st.session_state['final_image'] = processed_image
                            st.session_state['category'] = category
                            st.success("GENERATION COMPLETE.")
                            st.rerun()
                        else:
                            st.error("PROCESSING ERROR: Image Data Corrupted.")
                    else:
                        st.error("NETWORK ERROR: All Servers Busy. Please retry in 10s.")
            else:
                st.warning("INPUT REQUIRED.")

    with col2:
        st.markdown("### 🖼️ OUTPUT")
        if 'final_image' in st.session_state:
            st.image(st.session_state['final_image'], use_container_width=True)
            
            st.info(f"Mode Used: {st.session_state.get('category', 'General')}")
            
            st.download_button(
                label="📥 DOWNLOAD GOD-TIER ARTIFACT",
                data=st.session_state['final_image'],
                file_name=f"GOD_MODE_{int(time.time())}.png",
                mime="image/png"
            )
        else:
            st.info("AWAITING DATA...")

if __name__ == "__main__":
    main()
