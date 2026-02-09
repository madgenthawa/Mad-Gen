import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import time
import uuid

# ==============================================================================
# MODULE 1: SYSTEM CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: Browser Core",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Force Dark Theme via CSS
st.markdown("""
<style>
    /* GLOBAL BLACK THEME */
    .stApp {
        background-color: #000000;
        color: #ff0000;
    }
    
    /* HIDE DEFAULT ELEMENTS */
    header, footer {visibility: hidden;}
    
    /* INPUT BOX STYLING */
    .stTextArea textarea {
        background-color: #111 !important;
        color: #ff0000 !important;
        border: 2px solid #500 !important;
        font-family: monospace !important;
        font-size: 1.2rem !important;
    }
    .stTextArea textarea:focus {
        border-color: #f00 !important;
        box-shadow: 0 0 20px #f00 !important;
    }
    
    /* BUTTON STYLING */
    .stButton > button {
        background: #000;
        color: #f00;
        border: 2px solid #f00;
        font-size: 1.5rem;
        width: 100%;
        text-transform: uppercase;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background: #f00;
        color: #000;
        box-shadow: 0 0 30px #f00;
    }
</style>
""", unsafe_allow_html=True)

if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())

# ==============================================================================
# MODULE 2: BUSINESS LOGIC (LIC & THAWA)
# ==============================================================================
class LogicCore:
    @staticmethod
    def get_details(prompt):
        p = prompt.upper()
        if "LIC" in p:
            return "LIC HOUSING FINANCE", "பாதுகாப்பான எதிர்காலம். 🏠"
        elif "THAWA" in p:
            return "THAWA FINANCIAL SERVICES", "நிதி சிக்கல்களை உடைத்தெறியுங்கள். 📈"
        elif "DRAGON" in p:
            return "MYTHICAL REALM", "Fire and Blood. 🔥"
        else:
            return "MAD GEN CORE", "Creating Reality... ✨"

# ==============================================================================
# MODULE 3: BROWSER-SIDE RENDERING ENGINE (THE FIX)
# ==============================================================================
class BrowserEngine:
    """
    Generates HTML/JS code. This forces the User's Browser to fetch the image,
    Bypassing the Streamlit Server IP block entirely.
    """
    @staticmethod
    def render_image(prompt):
        # 1. Enhance Prompt
        enhanced = f"{prompt}, 8k resolution, raw photo, cinematic lighting, highly detailed, sharp focus"
        encoded = urllib.parse.quote(enhanced)
        seed = int(time.time())
        
        # 2. Direct URL (No Python Requests)
        image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&seed={seed}&nologo=true&model=flux"
        
        # 3. HTML Payload (This runs in your browser, not on the server)
        html_code = f"""
        <div style="
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center; 
            background: #050505; 
            border: 2px solid #ff0000; 
            border-radius: 15px; 
            padding: 20px; 
            box-shadow: 0 0 40px rgba(255, 0, 0, 0.2);
            margin-top: 20px;">
            
            <h3 style="color: #ff0000; font-family: monospace; letter-spacing: 2px;">STATUS: MANIFESTED</h3>
            
            <img src="{image_url}" 
                 style="width: 100%; max-width: 700px; border-radius: 10px; border: 1px solid #333;" 
                 alt="Generated Content"
                 onerror="this.style.display='none'; document.getElementById('error-msg').style.display='block';">
            
            <div id="error-msg" style="display:none; color: #ff0000; margin-top: 10px;">
                CONNECTION LOST. PLEASE REFRESH.
            </div>

            <a href="{image_url}" target="_blank" style="
                margin-top: 25px;
                padding: 15px 40px;
                background-color: #ff0000;
                color: #000000;
                font-family: sans-serif;
                font-weight: bold;
                text-decoration: none;
                border-radius: 5px;
                box-shadow: 0 0 20px #ff0000;
                transition: 0.3s;">
                📥 DOWNLOAD HD IMAGE
            </a>
            
            <p style="color: #666; font-size: 0.8rem; margin-top: 15px; font-family: monospace;">
                *Rendered via Client-Side Protocol (Anti-Block Active)
            </p>
        </div>
        """
        return html_code

# ==============================================================================
# MODULE 4: MAIN APP
# ==============================================================================
def main():
    st.markdown('<h1 style="text-align:center; color:#f00; font-family:monospace; font-size:4rem;">MAD GEN</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#666;">BROWSER ENGINE v1.0 | NO SERVER REQUESTS</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 👁️ INPUT COMMAND")
        user_input = st.text_area("DESCRIBE VISUAL:", height=150, placeholder="Ex: Golden Dragon, LIC Poster...")
        
        if st.button("EXECUTE 🩸"):
            if user_input:
                # Save state
                st.session_state['prompt'] = user_input
                st.session_state['run'] = True
                st.rerun()
            else:
                st.warning("INPUT REQUIRED.")

    with col2:
        st.markdown("### 🖼️ OUTPUT STREAM")
        
        if st.session_state.get('run'):
            prompt = st.session_state['prompt']
            
            # Logic Display
            title, slogan = LogicCore.get_details(prompt)
            st.info(f"**{title}**\n\n{slogan}")
            
            # Render HTML (The Browser does the work now)
            html_content = BrowserEngine.render_image(prompt)
            components.html(html_content, height=800, scrolling=True)

if __name__ == "__main__":
    main()
