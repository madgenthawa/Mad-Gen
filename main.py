import streamlit as st
import requests
import urllib.parse
import time

# --- 1. UI CONFIG ---
st.set_page_config(page_title="Mad Gen Nano Pro", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .main-header { 
        font-size: 3rem; font-weight: 800; text-align: center;
        background: -webkit-linear-gradient(#FFE000, #FFA500);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .stButton>button { 
        background: linear-gradient(45deg, #FFD700, #FFA500); 
        color: black; border-radius: 20px; font-weight: bold; height: 3.5em; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. IMAGE FETCH LOGIC ---
def get_image(prompt):
    safe_prompt = urllib.parse.quote(f"{prompt}, 8k, ultra-realistic, cinematic")
    seed = int(time.time())
    url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=1024&height=1024&seed={seed}&nologo=true"
    try:
        response = requests.get(url, timeout=60)
        if response.status_code == 200 and len(response.content) > 50000:
            return response.content
    except:
        return None
    return None

# --- 3. APP MAIN ---
st.markdown('<h1 class="main-header">🚀 MAD GEN NANO</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    user_input = st.text_input("Enna generate pannanum Maddy?", placeholder="Dragon, Car, etc...")
    if st.button("Generate ✨"):
        if user_input:
            with st.spinner("Processing..."):
                img_data = get_image(user_input)
                if img_data:
                    st.session_state['img_data'] = img_data
                    st.session_state['done'] = True
                else:
                    st.error("Server busy. Please try again in 10 seconds.")
        else:
            st.warning("Input kudunga Maddy!")

with col2:
    if 'done' in st.session_state:
        st.image(st.session_state['img_data'])
        st.download_button(
            label="📥 Download HD Image",
            data=st.session_state['img_data'],
            file_name="mad_gen_image.png",
            mime="image/png"
        )
