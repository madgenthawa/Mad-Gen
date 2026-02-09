import streamlit as st
import time
import random

# ==========================================
# 1. APP CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Mad Gen Pro: Ultra Stability",
    page_icon="🔥",
    layout="wide"
)

# Professional CSS Injection - Carefully Quoted
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        background: -webkit-linear-gradient(#FF4B2B, #FF416C);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5rem;
        background: linear-gradient(to right, #FF416C, #FF4B2B);
        border: none;
        color: white;
        font-weight: bold;
        transition: 0.3s;
    }
    .download-btn {
        display: inline-block;
        padding: 15px 30px;
        background: #28a745;
        color: white !important;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. BUSINESS CONTENT LOGIC
# ==========================================
def get_tamil_content(user_query):
    query = user_query.upper()
    lic_quotes = [
        "உங்கள் குடும்பத்தின் எதிர்காலம், LIC-யுடன் பாதுகாப்பானது. 🏠",
        "கனவு இல்லம் நனவாக, LIC Housing Finance-ஐ நாடுங்கள்.",
        "சேமிப்பு என்பது வெறும் பழக்கமல்ல, அது உங்கள் குடும்பத்தின் பாதுகாப்பு."
    ]
    thawa_quotes = [
        "THAWA Financial: உங்கள் சொத்தின் மதிப்பை உயர்த்துவோம். 📈",
        "Loan Against Property (LAP): எளிய நடைமுறை, வேகமான கடன்.",
        "உங்கள் நிதி தேவைகளுக்கு தவா நிதி சேவை என்றும் துணையாக இருக்கும்."
    ]
    
    if "LIC" in query:
        return random.choice(lic_quotes)
    elif "THAWA" in query or "LAP" in query:
        return random.choice(thawa_quotes)
    else:
        return "உங்களுடைய தனித்துவமான படைப்பு இதோ! ✨"

# ==========================================
# 3. MAIN UI LAYOUT
# ==========================================
st.markdown('<h1 class="main-title">🚀 MAD GEN PRO</h1>', unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Professional AI Marketing Engine for Maddy</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("🎨 Input Panel")
    user_input = st.text_area("Describe your poster (e.g., LIC Housing Loan ad in high quality)", height=150)
    
    if st.button("Magic Pannu! ✨"):
        if user_input:
            with st.spinner("Processing your High-Quality request..."):
                seed = int(time.time())
                # Using direct rendering to bypass server timeouts
                img_url = f"https://image.pollinations.ai/prompt/{user_input.replace(' ', '%20')}?width=1024&height=1024&seed={seed}&nologo=true"
                
                st.session_state['current_img'] = img_url
                st.session_state['tamil_msg'] = get_tamil_content(user_input)
                st.session_state['done'] = True
        else:
            st.warning("Please enter some text first, Maddy!")

with col2:
    st.subheader("🖼️ Preview & Download")
    if 'done' in st.session_state:
        # Render image directly from URL
        st.image(st.session_state['current_img'], use_container_width=True)
        
        # Display Tamil Business Content
        st.info(st.session_state['tamil_msg'])
        
        # Professional Download Link
        st.markdown(f"""
            <div style="text-align: center;">
                <a href="{st.session_state['current_img']}" target="_blank" class="download-btn">
                   📥 DOWNLOAD FULL QUALITY
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Input panel-la unga idea-vai type panni button-ai click pannunga Maddy!")

st.divider()
st.caption("Mad Gen AI | Logic Structure: Professional | Stability: 100% ✅")
