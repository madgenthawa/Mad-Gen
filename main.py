import streamlit as st
import requests
import base64

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen AI", page_icon="🎨", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #1e1e2f, #232235); color: white; }
    .stButton>button { border-radius: 20px; background: #FF4B4B; font-weight: bold; color: white; width: 100%; border: none; height: 3em; }
    .download-link { 
        display: inline-block; padding: 10px 20px; background-color: #4CAF50; 
        color: white; border-radius: 10px; text-decoration: none; font-weight: bold; margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Mad Gen: Pro AI Marketer")
st.write("Vanakka Maddy! Ippo unga creative ideas-ku proper-ana images ready aagum!")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Your Idea")
    user_input = st.text_input("Enna poster venum? (Eg: LIC Loan, Biryani Shop...)", placeholder="Type here...")
    style_type = st.select_slider("Select Quality:", options=["Standard", "Professional", "Cinematic 8K", "Ultra-Realistic"])

    if st.button("Mad Gen, Magic Pannu! ✨"):
        if user_input:
            with st.spinner("Maddy, unga poster-ai AI design pannitu irukku..."):
                # PROMPT ENHANCEMENT: Idhu dhaan proper image varavekkum
                enhanced_prompt = f"{user_input}, {style_type} marketing poster, highly detailed, professional lighting, 8k resolution, advertisement style, sharp focus"
                img_url = f"https://pollinations.ai/p/{enhanced_prompt.replace(' ', '%20')}?width=1080&height=1080&seed=100&model=flux"
                
                try:
                    response = requests.get(img_url, timeout=30)
                    if response.status_code == 200:
                        st.session_state['img_data'] = response.content
                        st.session_state['img_url_display'] = img_url
                        st.session_state['generated'] = True
                        st.session_state['topic'] = user_input
                    else:
                        st.error("Server konjam busy, thirumba click pannunga!")
                except:
                    st.error("Network issue Maddy, refresh pannunga!")
        else:
            st.warning("Maddy, edhavadhu type pannunga!")

with col2:
    st.subheader("🖼️ Result")
    if 'generated' in st.session_state:
        st.image(st.session_state['img_url_display'], caption=f"Mad Gen Design: {st.session_state['topic']}")
        
        # Proper Download Link
        b64 = base64.b64encode(st.session_state['img_data']).decode()
        href = f'<a href="data:file/png;base64,{b64}" download="mad_gen_{st.session_state["topic"]}.png" class="download-link">📥 Click to Download Poster</a>'
        st.markdown(href, unsafe_allow_html=True)

st.divider()
st.caption("Mad Gen AI | Enhanced Image Quality ✅")
