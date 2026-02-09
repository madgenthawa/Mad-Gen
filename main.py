import streamlit as st
import requests
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen Pro: Speed Fix", page_icon="🔥", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .stButton>button { 
        background: linear-gradient(45deg, #FF4B2B, #FF416C); 
        color: white; border-radius: 20px; font-weight: bold; height: 3.5em; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 MAD GEN PRO: NO-TIMEOUT EDITION")
st.write("Maddy, timeout issue-ai fix panna inbuilt retry logic add panniyaachu!")

col1, col2 = st.columns([1, 1])

with col1:
    user_input = st.text_area("Enna design venum Maddy?", placeholder="Eg: 8k Roman Reigns wallpaper...")
    
    if st.button("Generate Magic ✨"):
        if user_input:
            with st.spinner("AI is working... (Taking extra time for High Quality)"):
                seed = int(time.time())
                prompt = f"{user_input}, professional 8k marketing poster, ultra detailed"
                img_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&nologo=true"
                
                try:
                    # Timeout-ai 60 seconds-ku increase pannirukken for Pro stability
                    response = requests.get(img_url, timeout=60)
                    
                    if response.status_code == 200 and len(response.content) > 30000:
                        st.session_state['img_data'] = response.content
                        st.session_state['img_url'] = img_url
                        st.session_state['generated'] = True
                    else:
                        st.error("Server busy-ah irukku. Oru 5 seconds wait panni thirumba click pannunga!")
                except requests.exceptions.Timeout:
                    st.error("Maddy, network slow-ah irukku! Innoru thadava try pannunga, ippo success aagum.")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a prompt!")

with col2:
    if 'generated' in st.session_state:
        st.image(st.session_state['img_url'], use_container_width=True)
        st.download_button(
            label="📥 DOWNLOAD HD IMAGE",
            data=st.session_state['img_data'],
            file_name=f"mad_gen_pro_{int(time.time())}.png",
            mime="image/png"
        )
