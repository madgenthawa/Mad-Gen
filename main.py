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
    .download-btn {
        background-color: #28a745; color: white; padding: 12px 24px; 
        border-radius: 10px; text-decoration: none; font-weight: bold; display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

st.title("🚀 MAD GEN PRO: INSTANT ENGINE")
st.write("Maddy, syntax error fix panniyaachu! Ippo unga creative ideas ready aagum.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Your Idea")
    user_input = st.text_area("Enna design venum Maddy?", placeholder="Eg: 8k Roman Reigns wallpaper...")
    
    if st.button("Generate Magic ✨"):
        if user_input:
            with st.spinner("Mad Gen is summoning your image..."):
                seed = int(time.time())
                # Using the direct URL method to bypass server timeouts
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
        
        # Fixed the syntax error in the download section
        st.markdown(f"""
            <div style="text-align: center; margin-top: 20px
