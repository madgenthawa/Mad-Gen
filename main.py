import streamlit as st
import requests
import base64
from io import BytesIO

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen AI", page_icon="🎨", layout="wide")

# Custom Styling for Maddy
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #1e1e2f, #232235); color: white; }
    .stButton>button { border-radius: 20px; background: #FF4B4B; font-weight: bold; color: white; width: 100%; border: none; height: 3em; }
    .stTextInput>div>div>input { border-radius: 10px; }
    .download-link { 
        display: inline-block; 
        padding: 10px 20px; 
        background-color: #4CAF50; /* Green */
        color: white; 
        border-radius: 10px; 
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Mad Gen: Super-Fast AI Marketer")
st.write("Vanakka Maddy! Ippo unga idea-ku adhiradiyaana poster-gal ready!")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Unga Creative Idea")
    user_input = st.text_input("Enna poster venum? (Eg: LIC, Biryani, Car...)", 
                                placeholder="Type here...", key="user_input_key")
    
    style_options = ["Professional", "Cinematic", "Anime", "Cyberpunk", "Minimalist", "Hyper-Realistic"]
    style_type = st.select_slider("Select Style:", 
                                  options=style_options, key="style_key")

    if st.button("Mad Gen, Magic Pannu! ✨", key="magic_button_key"):
        if user_input:
            with st.spinner("Unga magic-kai Mad Gen create pannitu irukku..."):
                prompt_refined = f"{user_input}, {style_type} style, high quality, 4k, marketing poster"
                img_url = f"https://pollinations.ai/p/{prompt_refined.replace(' ', '%20')}?width=1080&height=1080&seed=99"
                
                try:
                    # Fetch image data
                    img_response = requests.get(img_url)
                    img_response.raise_for_status() # Check for HTTP errors
                    img_data = img_response.content
                    
                    st.session_state['img_data'] = img_data
                    st.session_state['img_caption'] = f"Mad Gen: {user_input} ({style_type})"
                    st.session_state['generated'] = True
                    st.session_state['download_trigger'] = True # To trigger auto download
                except requests.exceptions.RequestException as e:
                    st.error(f"Image generation-la error Maddy: {e}. Network-ai check pannunga.")
                    st.session_state['generated'] = False
        else:
            st.warning("Maddy, edhavadhu type pannunga!")

with col2:
    st.subheader("🖼️ Output")
    if 'generated' in st.session_state and st.session_state['generated']:
        # Display the image
        st.image(st.session_state['img_data'], caption=st.session_state['img_caption'])
        
        # Manual Download Button
        st.download_button(
            label="📥 Download This Image (Manual)",
            data=st.session_state['img_data'],
            file_name=f"mad_gen_{st.session_state['img_caption'].replace(' ', '_')}.png",
            mime="image/png",
            key="manual_download_key"
        )

# --- Automatic Download Logic ---
if 'download_trigger' in st.session_state and st.session_state['download_trigger']:
    if st.session_state['generated']:
        # Encode image data to base64 for direct download link
        b64 = base64.b64encode(st.session_state['img_data']).decode()
        dl_filename = f"mad_gen_{st.session_state['img_caption'].replace(' ', '_')}.png"
        href = f'<a href="data:file/png;base64,{b64}" download="{dl_filename}" class="download-link">Click here to Download Automatically!</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.session_state['download_trigger'] = False # Reset trigger

st.divider()
st.caption("Mad Gen AI | Download Feature Activated ✅")

# --- REQUIREMENTS.TXT ---
# Make sure your requirements.txt has these:
# streamlit
# requests
