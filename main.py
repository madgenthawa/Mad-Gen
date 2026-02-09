import streamlit as st
import requests
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen Pro", page_icon="🔥", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .stButton>button { 
        background: linear-gradient(45deg, #00c6ff, #0072ff); 
        color: white; border-radius: 15px; font-weight: bold; height: 3.5em; width: 100%;
    }
    .stDownloadButton>button {
        background: #28a745; color: white; border-radius: 15px; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 MAD GEN PRO: STABLE VERSION")
st.write("Maddy, indha version-la error handling and stability-ku priority kuduthurukken.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Describe Your Vision")
    # Prompt engineering simplified for better success
    user_input = st.text_area("Example: 8k Roman Reigns wallpaper, Realistic LIC Marketing Poster")
    
    if st.button("Generate Image"):
        if user_input:
            with st.spinner("Processing..."):
                # Unique seed avoids cache issues
                seed = int(time.time())
                # Using a backup high-speed engine
                img_url = f"https://image.pollinations.ai/prompt/{user_input.replace(' ', '%20')}?width=1024&height=1024&nologo=true&seed={seed}"
                
                try:
                    # Timeout set to 30s to ensure full image is fetched
                    response = requests.get(img_url, timeout=30)
                    
                    # VALIDATION: Checking if data is a real image (Size > 20KB)
                    if response.status_code == 200 and len(response.content) > 20000:
                        st.session_state['img_data'] = response.content
                        st.session_state['img_url'] = img_url
                        st.session_state['generated'] = True
                    else:
                        st.error("Server slow-ah irukku Maddy. Click 'Generate' again!")
                except Exception as e:
                    st.error("Connection error. Check internet and try again.")
        else:
            st.warning("Please type something first!")

with col2:
    st.subheader("🖼️ High-Res Result")
    if 'generated' in st.session_state:
        # Display using URL to avoid PIL library crashes
        st.image(st.session_state['img_url'], use_column_width=True)
        
        # Download using the actual Binary Data (Fixes the 3-byte issue)
        st.download_button(
            label="📥 DOWNLOAD HD IMAGE",
            data=st.session_state['img_data'],
            file_name=f"mad_gen_{int(time.time())}.png",
            mime="image/png"
        )
