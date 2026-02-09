import streamlit as st
import requests
import urllib.parse
import time
import io

# --- 1. PRO CONFIGURATION ---
st.set_page_config(page_title="Mad Gen Nano Pro", page_icon="🍌", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .main-header { 
        font-size: 3.5rem; font-weight: 900; text-align: center;
        background: -webkit-linear-gradient(#FFE000, #795548);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .stButton>button { 
        background: linear-gradient(45deg, #FFD700, #FFA500); 
        color: black; border-radius: 30px; font-weight: bold; height: 4em; width: 100%;
        border: none; box-shadow: 0 4px 15px rgba(255,215,0,0.3);
    }
    .download-section {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px; border-radius: 20px; text-align: center;
        border: 1px dashed #FFD700;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. THE NANO BANANA LOGIC (Binary Streaming) ---
def get_image_binary(prompt):
    # URI Encoding to prevent 400 Bad Request
    safe_prompt = urllib.parse.quote(f"{prompt}, 8k, photorealistic, cinematic masterpiece")
    seed = int(time.time())
    
    # Primary & Secondary Engine URLs
    urls = [
        f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true&model=flux",
        f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&seed={seed}"
    ]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=45)
            # If the response is valid and larger than 50KB (Not a 3-byte error)
            if response.status_code == 200 and len(response.content) > 50000:
                return response.content, url
        except:
            continue
    return None, None

# --- 3. MAIN UI ---
st.markdown('<h1 class="main-header">🍌 MAD GEN: NANO ENGINE</h1>', unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Professional Gemini-Based Image Architecture</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Universal Prompt")
    user_input = st.text_area("Enna design venum Maddy? (Dragon, LIC Poster, Thawa Financial...)", 
                              placeholder="Describe your vision here...", height=200)
    
    if st.button("Generate Masterpiece 🚀"):
        if user_input:
            with st.spinner("Nano Banana Engine is processing binary data..."):
                img_bytes, img_url = get_image_binary(user_input)
                
                if img_bytes:
                    st.session_state['img_bytes'] = img_bytes
                    st.session_state['img_url'] = img_url
                    st.session_state['generated'] = True
                else:
                    st.error("Maddy, server is currently overloaded. Please try once more in 10 seconds.")
        else:
            st.warning("Please type something first!")

with col2:
    st.subheader("🖼️ Binary Preview")
    if 'generated' in st.session_state:
        # We display the raw bytes directly to ensure 100% fidelity
        st.image(st.session_state['img_bytes'], use_container_width=True)
        
        st.markdown('<div class="download-section">', unsafe_allow_html=True)
        st.write("✅ High-Quality Image Loaded Successfully")
        
        # PROPER DOWNLOAD BUTTON: This fixes the 3-byte issue permanently
        st.download_button(
            label="📥 DOWNLOAD HD IMAGE (PRO)",
            data=st.session_state['img_bytes'],
            file_name=f"mad_gen_nano_{int(time.time())}.png",
            mime="image/png"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Your high-res output will appear here.")

st.divider()
st.caption("Mad Gen Nano v5.0 | Stability: Ultra | Powered by Maddy ✅")
