import streamlit as st
import requests
import base64

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
        background-color: #4CAF50; 
        color: white; 
        border-radius: 10px; 
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Mad Gen: Super-Fast AI Marketer")
st.write("Maddy, ippo image loading issue-ai fix panniyaachu! Try pannunga.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Your Creative Idea")
    user_input = st.text_input("Enna poster venum? (Eg: LIC, Biryani...)", placeholder="Type here...")
    
    style_options = ["Professional", "Cinematic", "Anime", "Cyberpunk", "Minimalist"]
    style_type = st.select_slider("Select Style:", options=style_options)

    if st.button("Mad Gen, Magic Pannu! ✨"):
        if user_input:
            with st.spinner("Wait Maddy, image ready aagudhu..."):
                # Unique URL build panroam
                prompt_refined = f"{user_input}, {style_type} style, high quality, 4k, marketing poster"
                img_url = f"https://pollinations.ai/p/{prompt_refined.replace(' ', '%20')}?width=1080&height=1080&seed=42"
                
                try:
                    response = requests.get(img_url, timeout=20)
                    if response.status_code == 200:
                        st.session_state['img_data'] = response.content
                        st.session_state['generated'] = True
                        st.session_state['img_name'] = user_input
                    else:
                        st.error("Maddy, image server konjam busy-ah irukku. 5 secs kazhichu thirumba click pannunga!")
                except:
                    st.error("Network slow-ah irukku Maddy. Refresh pannunga!")
        else:
            st.warning("Maddy, edhavadhu type pannunga!")

with col2:
    st.subheader("🖼️ Output")
    if 'generated' in st.session_state:
        # Direct URL use panradhu safe (UnidentifiedImageError thavirkka)
        image_url_display = f"https://pollinations.ai/p/{st.session_state['img_name'].replace(' ', '%20')}?width=1080&height=1080&seed=42"
        st.image(image_url_display, caption=f"Mad Gen: {st.session_state['img_name']}")
        
        # Download Link Logic
        if 'img_data' in st.session_state:
            b64 = base64.b64encode(st.session_state['img_data']).decode()
            href = f'<a href="data:file/png;base64,{b64}" download="mad_gen_{st.session_state["img_name"]}.png" class="download-link">📥 Click to Download Image</a>'
            st.markdown(href, unsafe_allow_html=True)

st.divider()
st.caption("Mad Gen AI | Stability Mode ✅")
