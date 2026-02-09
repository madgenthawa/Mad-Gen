import streamlit as st
import time

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen Pro: Ultra Speed", page_icon="🚀", layout="wide")

# Mass CSS with Logo Styling
st.markdown("""
<style>
    .stApp { background: #0e1117; color: white; }
    .stButton>button { 
        background: linear-gradient(45deg, #FF4B2B, #FF416C); 
        color: white; border-radius: 20px; font-weight: bold; height: 3.5em; width: 100%;
    }
    .download-btn {
        background-color: #28a745; color: white; padding: 12px 24px; 
        border-radius: 10px; text-decoration: none; font-weight: bold; display: inline-block;
    }
    .logo-text {
        font-size: 40px; font-weight: bold; color: #FF4B2B; text-align: center; margin-bottom: 0px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<p class="logo-text">🔥 MAD GEN PRO</p>', unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Maddy's Instant Creative Engine</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Your Idea")
    user_input = st.text_area("Enna design venum Maddy?", placeholder="Eg: 8k Roman Reigns wallpaper...")
    
    if st.button("Generate Magic ✨"):
        if user_input:
            with st.spinner("Mad Gen is summoning your image..."):
                seed = int(time.time())
                # Direct URL method to avoid timeouts
                img_url = f"https://image.pollinations.ai/prompt/{user_input.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&nologo=true"
                
                st.session_state['img_url'] = img_url
                st.session_state['generated'] = True
        else:
            st.warning("Please enter a prompt!")

with col2:
    st.subheader("🖼️ High-Res Preview")
    if 'generated' in st.session_state:
        # Direct URL display bypasses PIL and timeout errors
        st.image(st.session_state['img_url'], use_container_width=True)
        
        # COMPLETE & FIXED DOWNLOAD SECTION
        st.markdown(f"""
            <div style="text-align: center; margin-top: 20px;">
                <p style="color: #bbb;">Maddy, click below to save in Original High Quality:</p>
                <a href="{st.session_state['img_url']}" target="_blank" class="download-btn">
                   📥 DOWNLOAD FULL IMAGE
                </a>
            </div>
        """, unsafe_allow_html=True)

st.divider()
st.caption("Mad Gen AI | Branding & Syntax Fixed ✅")
