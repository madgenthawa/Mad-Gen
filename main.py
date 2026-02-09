import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
import time
import uuid

# ==============================================================================
# MODULE 1: CONFIG & THEME
# ==============================================================================
st.set_page_config(
    page_title="Mad Gen: JS Force",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp { background-color: #000000; color: #ff0000; }
    header, footer {visibility: hidden;}
    
    .stTextArea textarea {
        background-color: #050505 !important;
        color: #ff0000 !important;
        border: 2px solid #800 !important;
        font-family: monospace !important;
    }
    
    .stButton > button {
        background: #000; color: #f00; border: 2px solid #f00;
        font-size: 1.5rem; width: 100%; font-weight: bold;
    }
    .stButton > button:hover {
        box-shadow: 0 0 30px #f00;
    }
</style>
""", unsafe_allow_html=True)

if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())

# ==============================================================================
# MODULE 2: LOGIC CORE
# ==============================================================================
class LogicCore:
    @staticmethod
    def get_details(prompt):
        p = prompt.upper()
        if "LIC" in p: return "LIC HOUSING FINANCE", "பாதுகாப்பான எதிர்காலம். 🏠"
        elif "THAWA" in p: return "THAWA FINANCIAL SERVICES", "நிதி சிக்கல்களை உடைத்தெறியுங்கள். 📈"
        elif "DRAGON" in p: return "MYTHICAL REALM", "Fire and Blood. 🔥"
        else: return "MAD GEN CORE", "Creating Reality... ✨"

# ==============================================================================
# MODULE 3: JAVASCRIPT FORCE ENGINE (THE FIX)
# ==============================================================================
class BrowserEngine:
    @staticmethod
    def render_image(prompt):
        # 1. Enhance Prompt
        enhanced = f"{prompt}, 8k resolution, raw photo, cinematic lighting, highly detailed, sharp focus"
        encoded = urllib.parse.quote(enhanced)
        seed = int(time.time())
        filename = f"MAD_GEN_{seed}.jpg"
        
        # 2. Image URL
        image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&seed={seed}&nologo=true&model=flux"
        
        # 3. HTML + JAVASCRIPT (Force Download Logic)
        html_code = f"""
        <div style="background: #000; border: 2px solid #f00; padding: 20px; text-align: center; border-radius: 15px;">
            <h3 style="color: #f00; font-family: monospace;">STATUS: MANIFESTED</h3>
            
            <img src="{image_url}" style="width: 100%; border-radius: 10px; border: 1px solid #333; margin-bottom: 20px;">
            
            <button id="dl-btn" onclick="forceDownload('{image_url}', '{filename}')" style="
                background-color: #f00; color: #000; padding: 15px 30px; 
                font-weight: bold; font-family: sans-serif; border: none; 
                border-radius: 5px; cursor: pointer; font-size: 16px;">
                📥 DOWNLOAD HD IMAGE
            </button>
            
            <p id="status-msg" style="color: #666; margin-top: 10px; font-family: monospace;"></p>
        </div>

        <script>
            async function forceDownload(url, filename) {{
                const btn = document.getElementById('dl-btn');
                const msg = document.getElementById('status-msg');
                
                btn.innerText = "⏳ PROCESSING...";
                btn.style.opacity = "0.7";
                
                try {{
                    // Fetch the image as a 'Blob' (Binary File)
                    const response = await fetch(url);
                    const blob = await response.blob();
                    
                    // Create a temporary link to the Blob
                    const blobUrl = window.URL.createObjectURL(blob);
                    const link = document.createElement('a');
                    link.href = blobUrl;
                    link.download = filename;
                    
                    // Click the link automatically
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    
                    // Cleanup
                    window.URL.revokeObjectURL(blobUrl);
                    btn.innerText = "✅ DOWNLOADED";
                    btn.style.opacity = "1";
                    msg.innerText = "Saved to your device!";
                    
                }} catch (e) {{
                    console.error(e);
                    // Fallback: Open in new tab if blob fails
                    window.open(url, '_blank');
                    btn.innerText = "⚠️ OPENED IN NEW TAB";
                    msg.innerText = "Auto-download blocked. Long press image to save.";
                }}
            }}
        </script>
        """
        return html_code

# ==============================================================================
# MODULE 4: MAIN APP
# ==============================================================================
def main():
    st.markdown('<h1 style="text-align:center; color:#f00; font-family:monospace;">MAD GEN</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("### 👁️ INPUT")
        user_input = st.text_area("DESCRIBE VISUAL:", height=150, placeholder="Ex: Golden Dragon...")
        
        if st.button("EXECUTE 🩸"):
            if user_input:
                st.session_state['prompt'] = user_input
                st.session_state['run'] = True
                st.rerun()
            else:
                st.warning("INPUT REQUIRED.")

    with col2:
        st.markdown("### 🖼️ OUTPUT")
        if st.session_state.get('run'):
            prompt = st.session_state['prompt']
            title, slogan = LogicCore.get_details(prompt)
            st.info(f"**{title}**\n\n{slogan}")
            
            # Render JS Force Engine
            html_content = BrowserEngine.render_image(prompt)
            components.html(html_content, height=850, scrolling=True)

if __name__ == "__main__":
    main()
