import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen Pro: Ultra Speed", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .stButton>button { 
        background: linear-gradient(45deg, #FF4B2B, #FF416C); 
        color: white; border-radius: 20px; font-weight: bold; height: 3.5em; width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 MAD GEN PRO: INSTANT ENGINE")
st.write("Maddy, indha version-la timeout error varaadhu. Image direct-ah load aagum!")

col1, col2 = st.columns([1, 1])

with col1:
    user_input = st.text_area("Enna creative venum Maddy?", placeholder="Eg: 8k Roman Reigns wallpaper...")
    
    if st.button("Generate Magic ✨"):
        if user_input:
            with st.spinner("Mad Gen is summoning your image..."):
                # Unique seed avoids cache
                seed = int(time.time())
                # Direct URL display method (This avoids 'Read Timeout' during processing)
                img_url = f"https://image.pollinations.ai/prompt/{user_input.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&nologo=true"
                
                st.session_state['img_url'] = img_url
                st.session_state['generated'] = True
        else:
            st.warning("Please enter a prompt!")

with col2:
    if 'generated' in st.session_state:
        # We display using the URL directly so Streamlit doesn't have to 'fetch' the bytes first
        st.image(st.session_state['img_url'], use_container_width=True)
        
        st.markdown(f"""
            <div style="text-align: center;">
                <p>Maddy, image load aaga konjam time edutha right-click panni save pannikonga!</p>
                <a href="{st.session_state['img_url']}" target="_blank" 
                   style="background-color: #28a745; color:
