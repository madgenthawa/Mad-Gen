import streamlit as st
import google.generativeai as genai

# --- API SETUP ---
# Streamlit secrets-la irundhu key-ai edukka
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-pro')
except:
    st.error("Maddy, API Key innum set pannaala! Settings-la add pannunga.")

# --- APP CONFIG ---
st.set_page_config(page_title="Mad Gen AI", page_icon="🎨", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(to right, #1e1e2f, #232235); color: white; }
    .stButton>button { border-radius: 20px; background: #FF4B4B; font-weight: bold; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Mad Gen: Pro Edition")
st.write("Vanakka Maddy! Real AI image generation ippo activate aagudhu!")

col1, col2 = st.columns([1, 1])

with col1:
    user_input = st.text_area("Enna creative venum?", placeholder="Eg: Festive offer poster for LIC...")
    style_type = st.select_slider("Quality Style:", options=["Minimalist", "High-End Professional", "Cinematic 8K", "Hyper-Realistic"])
    
    if st.button("Mad Gen, Magic Pannu! ✨"):
        if user_input:
            with st.spinner("AI is generating your high-quality content..."):
                # Logic to generate tagline and prompt
                response = model.generate_content(f"Create a catchy Tamil marketing tagline and a detailed DALL-E image prompt for: {user_input}")
                st.session_state['ai_text'] = response.text
                st.session_state['generated'] = True
        else:
            st.warning("Input kudunga Maddy!")

with col2:
    if 'generated' in st.session_state:
        st.subheader("🚀 Mad Gen Result")
        st.write(st.session_state['ai_text'])
        # Actual Image generation link (using a dummy placeholder for now until API key is active)
        st.image("https://pollinations.ai/p/" + user_input.replace(" ", "%20"), caption="Mad Gen Generated Image")
