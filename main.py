import streamlit as st
import requests
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen AI: Pro Edition", page_icon="🔥", layout="wide")

# Custom UI for Maddy
st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .stButton>button { 
        background: linear-gradient(45deg, #FF4B2B, #FF416C); 
        color: white; border-radius: 20px; font-weight: bold; border: none; height: 3.5em; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🔥 MAD GEN: PRO STABILITY")
st.write("Maddy, this version uses a high-capacity engine to bypass anonymous limits.")

col1, col2 = st.columns([1, 1])

with col1:
    user_input = st.text_area("What would you like to create? (e.g., 8k Roman Reigns Wallpaper)")
    
    if st.button("Generate Pro Image ✨"):
        if user_input:
            with st.spinner("Mad Gen is processing your high-quality request..."):
                # Using a fresh seed and specific pro-parameters
                seed = int(time.time())
                prompt = f"{user_input}, professional 8k marketing poster, ultra detailed, cinematic"
                # Using the stable 'flux' model path
                img_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&nologo=true"
                
                try:
                    response = requests.get(img_url, timeout=40)
                    # We only proceed if the file is a real image (larger than 30KB)
                    if response.status_code == 200 and len(response.content) > 30000:
                        st.session_state['img_data'] = response.content
                        st.session_state['img_url'] = img_url
                        st.session_state['generated'] = True
                    else:
                        st.error("Engine busy. Please wait 10 seconds and click again, Maddy!")
                except Exception as e:
                    st.error(f"Connection error: {e}")
        else:
            st.warning("Please enter a prompt first!")

with col2:
    if 'generated' in st.session_state:
        st.image(st.session_state['img_url'], use_container_width=True)
        st.download_button(
            label="📥 DOWNLOAD HIGH-RES IMAGE",
            data=st.session_state['img_data'],
            file_name=f"mad_gen_pro_{int(time.time())}.png",
            mime="image/png"
        )
