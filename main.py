import streamlit as st
import requests

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen AI", page_icon="🎨", layout="wide")

# Custom Styling for Maddy
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #1e1e2f, #232235); color: white; }
    .stButton>button { border-radius: 20px; background: #FF4B4B; font-weight: bold; color: white; width: 100%; border: none; height: 3em; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Mad Gen: Super-Fast AI")
st.write("Vanakka Maddy! Inniku namma direct-ah images generate panna porom, No more errors!")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Your Creative Idea")
    user_input = st.text_input("Enna poster venum? (Eg: LIC, Biryani, Car...)", placeholder="Type here...")
    
    style_type = st.select_slider("Select Style:", 
                                  options=["Professional", "Cinematic", "Anime", "Cyberpunk"])

    if st.button("Mad Gen, Magic Pannu! ✨"):
        if user_input:
            with st.spinner("Creating your magic..."):
                # Direct Image Generation using Pollinations (No API Key needed for this!)
                prompt_refined = f"{user_input}, {style_type} style, high quality, 4k, marketing poster"
                st.session_state['img_url'] = f"https://pollinations.ai/p/{prompt_refined.replace(' ', '%20')}?width=1080&height=1080&seed=99"
                st.session_state['generated'] = True
        else:
            st.warning("Maddy, edhavadhu type pannunga!")

with col2:
    st.subheader("🖼️ Output")
    if 'generated' in st.session_state:
        st.image(st.session_state['img_url'], caption=f"Mad Gen: {user_input}")
        
        # Download Button
        try:
            img_data = requests.get(st.session_state['img_url']).content
            st.download_button(
                label="📥 Download This Image",
                data=img_data,
                file_name="mad_gen_design.png",
                mime="image/png"
            )
        except:
            st.info("Image-ai long press panni save pannikonga Maddy!")

st.divider()
st.caption("Mad Gen AI | Error-Free Version Powered by Maddy ✅")
