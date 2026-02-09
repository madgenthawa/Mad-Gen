import streamlit as st
import requests
from io import BytesIO

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen AI", page_icon="🎨", layout="wide")

# Custom Styling for Maddy
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #1e1e2f, #232235); color: white; }
    .stButton>button { border-radius: 20px; background: #FF4B4B; font-weight: bold; color: white; width: 100%; border: none; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Mad Gen: High-Quality Edition")
st.write("Maddy, ippo download error fix panniyaachu! High-quality images ippo ready.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Your Idea")
    user_input = st.text_input("Enna poster venum?", placeholder="Eg: LIC Professional Poster...")
    
    if st.button("Mad Gen, Magic Pannu! ✨"):
        if user_input:
            with st.spinner("AI is generating high-quality image..."):
                # Enhanced prompt for better quality
                enhanced_prompt = f"{user_input}, professional marketing poster, 8k resolution, highly detailed, sharp focus"
                img_url = f"https://pollinations.ai/p/{enhanced_prompt.replace(' ', '%20')}?width=1080&height=1080&seed=42&model=flux"
                
                try:
                    # FETCHING REAL IMAGE DATA
                    response = requests.get(img_url, timeout=30)
                    if response.status_code == 200:
                        # Image data-vai session-la save panroam
                        st.session_state['img_data'] = response.content
                        st.session_state['display_url'] = img_url
                        st.session_state['generated'] = True
                    else:
                        st.error("Server busy Maddy, try again!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Maddy, edhavadhu type pannunga!")

with col2:
    st.subheader("🖼️ Result")
    if 'generated' in st.session_state:
        # Displaying the image
        st.image(st.session_state['display_url'], caption="Mad Gen AI Result")
        
        # PROPER DOWNLOAD BUTTON (Fixing the 3 Bytes issue)
        st.download_button(
            label="📥 Download High-Quality Image",
            data=st.session_state['img_data'],
            file_name="mad_gen_poster.png",
            mime="image/png"
        )

st.divider()
st.caption("Mad Gen AI | High-Quality Fix Applied ✅")
