import streamlit as st
import requests
import urllib.parse
import time
import random
import logging
from datetime import datetime

# ==============================================================================
# 1. SYSTEM CONFIGURATION & LOGGING
# ==============================================================================
# Configuring the enterprise logger to track errors
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

st.set_page_config(
    page_title="Mad Gen Enterprise | Thawa Financials",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. ENTERPRISE STYLING (CSS ENGINE)
# ==============================================================================
class StyleEngine:
    """Handles all CSS and UI transformations for the application."""
    
    @staticmethod
    def inject_css():
        st.markdown("""
        <style>
            /* CORE THEME */
            .stApp {
                background-color: #000000;
                color: #ffffff;
                font-family: 'Helvetica Neue', sans-serif;
            }
            
            /* HEADER TYPOGRAPHY */
            .mega-title {
                font-size: 4rem;
                font-weight: 900;
                text-align: center;
                background: linear-gradient(90deg, #FFD700, #FF8C00, #FF0000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-top: 20px;
                text-transform: uppercase;
                letter-spacing: 3px;
            }
            
            .subtitle {
                font-size: 1.2rem;
                text-align: center;
                color: #888;
                margin-bottom: 40px;
                font-weight: 300;
            }
            
            /* INPUT FIELDS */
            .stTextInput > div > div > input {
                background-color: #1a1a1a;
                color: white;
                border: 1px solid #333;
                border-radius: 10px;
                padding: 15px;
            }
            
            /* BUTTON ENGINEERING */
            .stButton > button {
                width: 100%;
                background: linear-gradient(90deg, #FF4B2B, #FF416C);
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 50px;
                height: 60px;
                font-size: 18px;
                cursor: pointer;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .stButton > button:hover {
                transform: scale(1.02);
                box-shadow: 0 10px 20px rgba(255, 75, 43, 0.4);
            }
            
            /* BUSINESS CARDS */
            .business-card {
                background: #111;
                border-left: 5px solid #FFD700;
                padding: 20px;
                margin-top: 20px;
                border-radius: 0 10px 10px 0;
            }
            
            /* DOWNLOAD SECTION */
            .success-box {
                padding: 20px;
                border: 1px solid #28a745;
                background: rgba(40, 167, 69, 0.1);
                border-radius: 10px;
                text-align: center;
                margin-top: 20px;
            }
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# 3. BUSINESS INTELLIGENCE MODULE (TAMIL DATA)
# ==============================================================================
class BusinessIntelligence:
    """Manages business logic for LIC and Thawa Financials."""
    
    def __init__(self):
        self.lic_data = [
            "LIC: உங்கள் வாழ்க்கையின் ஒவ்வொரு கட்டத்திலும் பாதுகாப்பு. 🏠",
            "எதிர்பாராததை எதிர்கொள்ள, LIC என்றும் துணை நிற்கும்.",
            "சிறிய சேமிப்பு, பெரிய எதிர்காலம் - LIC Housing Finance.",
            "கனவு இல்லம் நனவாக, எங்களை நாடுங்கள்."
        ]
        
        self.thawa_data = [
            "THAWA Financial: உங்கள் வளர்ச்சியே எங்கள் நோக்கம். 📈",
            "Loan Against Property (LAP): உங்கள் சொத்து, உங்கள் சக்தி.",
            "எளிய வட்டி, விரைவான கடன் - தவா நிதி சேவை.",
            "தொழில் வளர்ச்சிக்கு நம்பகமான கூட்டாளி - THAWA."
        ]
        
        self.dragon_data = [
            "Dragon Mode Activated: Power & Fury! 🐉",
            "Unleashing the beast within the pixels.",
            "Mythical quality generated successfully."
        ]

    def get_marketing_copy(self, prompt):
        """Analyzes the prompt and returns context-aware Tamil text."""
        p_lower = prompt.lower()
        
        if "lic" in p_lower or "housing" in p_lower:
            return "LIC MARKETING", random.choice(self.lic_data)
        elif "thawa" in p_lower or "loan" in p_lower or "finance" in p_lower:
            return "THAWA FINANCIALS", random.choice(self.thawa_data)
        elif "dragon" in p_lower:
            return "MYTHICAL ENGINE", random.choice(self.dragon_data)
        else:
            return "MAD GEN CREATIVE", "உங்களுடைய தனித்துவமான படைப்பு தயார்! ✨"

# ==============================================================================
# 4. GENERATION ENGINE (CORE LOGIC)
# ==============================================================================
class ImageEngine:
    """Handles the complex logic of API communication and Binary Fetching."""
    
    def __init__(self):
        self.base_url = "https://image.pollinations.ai/prompt/"
        self.width = 1024
        self.height = 1024
        self.model = "flux" # High quality model
    
    def construct_url(self, prompt):
        """Builds a Cloudflare-safe URL."""
        # Enhancement keywords for 8k quality
        enhancers = "8k, masterpiece, cinematic lighting, ultra-detailed, professional photography, sharp focus"
        full_prompt = f"{prompt}, {enhancers}"
        
        # URI Encoding to prevent 400 Bad Request
        safe_prompt = urllib.parse.quote(full_prompt)
        seed = int(time.time())
        
        url = f"{self.base_url}{safe_prompt}?width={self.width}&height={self.height}&seed={seed}&nologo=true&model={self.model}"
        return url

    def fetch_binary(self, url):
        """Fetches raw bytes with retry logic to prevent 3-byte errors."""
        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            try:
                # 60 Second timeout for high-res files
                response = requests.get(url, timeout=60)
                
                # VALIDATION: Check if file is larger than 10KB
                if response.status_code == 200 and len(response.content) > 10000:
                    return response.content
                else:
                    logging.warning(f"Attempt {attempts+1} failed: File too small or status {response.status_code}")
                    time.sleep(2)
                    attempts += 1
            except Exception as e:
                logging.error(f"Network Error: {e}")
                attempts += 1
                time.sleep(2)
        return None

# ==============================================================================
# 5. USER INTERFACE (VIEW LAYER)
# ==============================================================================
class UserInterface:
    """Manages the Streamlit Frontend."""
    
    def __init__(self):
        self.style = StyleEngine()
        self.biz = BusinessIntelligence()
        self.engine = ImageEngine()
        
    def render(self):
        # 1. Inject Styles
        self.style.inject_css()
        
        # 2. Header
        st.markdown('<h1 class="mega-title">MAD GEN ENTERPRISE</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">Thawa Financials & Creative Studio | Powered by Maddy</p>', unsafe_allow_html=True)
        
        # 3. Layout
        col1, col2 = st.columns([1, 0.8], gap="large")
        
        with col1:
            st.markdown("### 📡 COMMAND CENTER")
            user_input = st.text_area("Enter your vision (LIC, Thawa, Dragon...)", height=150)
            
            # Action Button
            if st.button("INITIATE GENERATION SEQUENCE 🚀"):
                if user_input:
                    self.process_request(user_input)
                else:
                    st.error("Input Required: Please enter a prompt to proceed.")

        with col2:
            st.markdown("### 🖼️ RENDER PREVIEW")
            if 'generated' in st.session_state and st.session_state['generated']:
                self.show_results()
            else:
                st.info("System Standby... Waiting for input.")

    def process_request(self, user_input):
        """Orchestrates the generation process."""
        with st.spinner("🔄 CONNECTING TO NEURAL CLOUD..."):
            # 1. Get Marketing Copy
            title, text = self.biz.get_marketing_copy(user_input)
            
            # 2. Construct URL
            img_url = self.engine.construct_url(user_input)
            
            # 3. Save to Session State
            st.session_state['current_url'] = img_url
            st.session_state['marketing_title'] = title
            st.session_state['marketing_text'] = text
            st.session_state['generated'] = True
            
            # Force refresh to show results
            st.rerun()

    def show_results(self):
        """Displays the generated content."""
        img_url = st.session_state.get('current_url')
        title = st.session_state.get('marketing_title')
        text = st.session_state.get('marketing_text')
        
        # A. Display Image (Direct URL for speed)
        st.image(img_url, use_container_width=True)
        
        # B. Display Business Logic
        st.markdown(f"""
        <div class="business-card">
            <h3 style="color:#FFD700; margin:0;">{title}</h3>
            <p style="font-size:18px; margin-top:10px;">{text}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # C. Binary Download Logic (The "Proper" Way)
        st.markdown("---")
        if st.button("📥 DOWNLOAD HD FILE (SERVER FETCH)"):
            with st.spinner("Downloading Raw Binary Data..."):
                img_bytes = self.engine.fetch_binary(img_url)
                if img_bytes:
                    # We use a trick to auto-download by showing a secondary button
                    # In a real 1000-line app, this would be a callback, but here we do this:
                    st.download_button(
                        label="✅ CLICK TO SAVE NOW",
                        data=img_bytes,
                        file_name=f"MadGen_Enterprise_{int(time.time())}.png",
                        mime="image/png"
                    )
                    st.success("File retrieved successfully! Click the button above.")
                else:
                    st.error("Server Timeout: The image is too large. Try generating again.")

# ==============================================================================
# 6. MAIN EXECUTION ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    # Initialize the Application
    app = UserInterface()
    app.render()
