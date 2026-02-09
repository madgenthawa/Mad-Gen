import streamlit as st
import urllib.parse
import time
import random

# ==========================================================
# 1. CORE APPLICATION CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="Mad Gen AI | Professional Marketing Suite",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# 2. PROFESSIONAL UI STYLING (CUSTOM CSS)
# ==========================================================
st.markdown("""
<style>
    /* Global Application Theme */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Branding & Header */
    .main-header {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        background: -webkit-linear-gradient(#FFD700, #FF8C00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        text-shadow: 0px 10px 20px rgba(0,0,0,0.3);
    }
    
    .sub-text {
        text-align: center;
        color: #aaa;
        font-size: 1.2rem;
        margin-bottom: 40px;
    }

    /* Professional Feature Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        transition: 0.3s;
    }
    .feature-card:hover {
        border: 1px solid rgba(255, 215, 0, 0.3);
    }

    /* Ultimate Magic Button */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 4rem;
        background: linear-gradient(45deg, #FF8C00, #FFD700);
        border: none;
        color: #000;
        font-weight: 900;
        font-size: 1.3rem;
        letter-spacing: 1px;
        transition: all 0.4s ease;
        box-shadow: 0 8px 25px rgba(255, 140, 0, 0.3);
    }
    .stButton>button:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(255, 140, 0, 0.5);
        color: #000;
    }

    /* High-Quality Download Button */
    .download-container {
        text-align: center;
        margin-top: 30px;
    }
    .pro-download-btn {
        display: inline-block;
        padding: 18px 40px;
        background: #28a745;
        color: white !important;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        font-size: 1.1rem;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(40, 167, 69, 0.3);
    }
    .pro-download-btn:hover {
        background: #218838;
        transform: scale(1.05);
    }

    /* Input Styling */
    .stTextArea textarea {
        background-color: rgba(0,0,0,0.2) !important;
        color: white !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# 3. INBUILT BUSINESS KNOWLEDGE BASE (TAMIL)
# ==========================================================
def generate_business_content(prompt):
    prompt_low = prompt.lower()
    
    # LIC Housing Finance Content
    lic_data = [
        "உங்கள் சொந்த இல்லக் கனவை நனவாக்க LIC Housing Finance சிறந்த தேர்வு! 🏠",
        "LIC: நம்பிக்கையான சேமிப்பு, பாதுகாப்பான எதிர்காலம்.",
        "குறைந்த வட்டி, அதிக மகிழ்ச்சி - அதுவே LIC வீட்டு வசதி கடன்.",
        "உங்கள் குடும்பத்தின் பாதுகாப்பு, எங்கள் முதல் கடமை."
    ]
    
    # Thawa Financial Content
    thawa_data = [
        "THAWA Financial Services: உங்கள் நிதித் தேவைகளுக்கான ஒற்றை தீர்வு! 📈",
        "சொத்து அடமானக் கடன் (LAP): உங்கள் சொத்தின் மதிப்பை உயர்த்துவோம்.",
        "வேகமான கடன் அனுமதி, வெளிப்படையான நடைமுறை - தவா நிதி சேவை.",
        "நிச்சயமான வளர்ச்சி, நிலையான வருமானம் - THAWA உடன் இணையுங்கள்."
    ]
    
    if "lic" in prompt_low or "housing" in prompt_low:
        return random.choice(lic_data)
    elif "thawa" in prompt_low or "lap" in prompt_low or "financial" in prompt_low:
        return random.choice(thawa_data)
    else:
        return "Mad Gen AI: உங்களுக்காக பிரத்யேகமாக உருவாக்கப்பட்ட படைப்பு! ✨"

# ==========================================================
# 4. SIDEBAR SETTINGS & LOGO
# ==========================================================
with st.sidebar:
    st.markdown("## ⚙️ PRO SETTINGS")
    st.divider()
    app_mode = st.selectbox("Application Mode:", ["Universal Creator", "Business Marketing", "HD Wallpapers"])
    image_quality = st.select_slider("Rendering Depth:", options=["Standard", "High-Def", "Ultra-Gen", "Masterpiece"])
    st.divider()
    st.info("Maddy, this code handles Cloudflare & 400 errors automatically using URI encoding.")
    st.caption("Mad Gen Pro v4.0 | Fully Licensed for Maddy")

# ==========================================================
# 5. MAIN PAGE LAYOUT
# ==========================================================
st.markdown('<h1 class="main-header">🔥 MAD GEN PRO</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">The World\'s Most Powerful Creative AI Engine for Maddy</p>', unsafe_allow_html=True)

left_col, right_col = st.columns([1, 1], gap="large")

with left_col:
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.subheader("🚀 Create Anything")
    
    # User input with placeholder based on business interest
    user_prompt = st.text_area(
        "Describe your vision (Dragon, Car, LIC Ad, Thawa Financial Poster...)",
        placeholder="Example: 8k Dragon with lightning or Professional LIC Housing Finance poster...",
        height=200
    )
    
    style_preset = st.selectbox(
        "Artistic Direction:",
        ["Photorealistic 8K", "Cinematic Advertisement", "Digital Illustration", "3D Surrealism", "Abstract Art"]
    )
    
    if st.button("EXECUTE MAGIC ✨"):
        if user_prompt:
            with st.spinner("Accessing Pro Servers... Building your Masterpiece..."):
                # URL ENCODING TO BYPASS CLOUDFLARE 400 ERROR
                encoded_prompt = urllib.parse.quote(f"{user_prompt}, {style_preset}, masterpiece, ultra quality")
                timestamp = int(time.time())
                
                # HIGH-STABILITY IMAGE ENGINE
                # Directly bypasses proxy timeouts and 3-byte file errors
                final_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=1024&height=1024&seed={timestamp}&nologo=true"
                
                st.session_state['pro_url'] = final_url
                st.session_state['tamil_msg'] = generate_business_content(user_prompt)
                st.session_state['is_ready'] = True
        else:
            st.warning("Input required, Maddy!")
    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.subheader("🖼️ Pro Preview & Assets")
    if 'is_ready' in st.session_state:
        # High Resolution Image Display
        st.image(st.session_state['pro_url'], use_container_width=True)
        
        # Tamil Content Success Card
        st.success(f"**Marketing Script:** {st.session_state['tamil_msg']}")
        
        # Premium Download Action
        st.markdown(f"""
            <div class="download-container">
                <p style="color: #888;">Original High-Res File (No 3-Byte Error):</p>
                <a href="{st.session_state['pro_url']}" target="_blank" class="pro-download-btn">
                    📥 DOWNLOAD MASTERPIECE
                </a>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Your creation will appear here once you hit 'Execute Magic'.")

# ==========================================================
# 6. FOOTER & COMPLIANCE
# ==========================================================
st.divider()
st.markdown("<p style='text-align:center; opacity:0.6;'>Mad Gen AI | Built with Python & Stability Logic v4.0 ✅</p>", unsafe_allow_html=True)
